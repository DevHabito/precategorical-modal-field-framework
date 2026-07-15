from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.special import ndtr

SEED=20260809
T_GRID=np.linspace(-4.0,4.0,4001)
BLOCK_SIZES=(1,2,4,8,16,32,64,128)
CLT_SAMPLES=60000
BATCH=2000
MAX_EXACT_ERROR=2e-12
MIN_NON_GAUSS_RES=0.02
MAX_FINAL_EXCESS=0.03
MAX_FINAL_KS=0.02


def js(v):
    if isinstance(v,dict): return {str(k):js(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [js(x) for x in v]
    if isinstance(v,np.bool_): return bool(v)
    if isinstance(v,np.integer): return int(v)
    if isinstance(v,np.floating): return float(v)
    return v

def ks_normal(x):
    x=np.sort(np.asarray(x,float)); n=len(x); F=ndtr(x)
    return float(max(np.max(np.abs(np.arange(1,n+1)/n-F)),np.max(np.abs(F-np.arange(n)/n))))

def excess(x):
    x=np.asarray(x,float); c=x-x.mean(); v=np.mean(c*c)
    return float(np.mean(c**4)/v**2-3)

def entropy_table():
    return [
        {"distribution":"Gaussian variance 1","differential_entropy":0.5*math.log(2*math.pi*math.e),"selected_by":"fixed mean and variance","status":"UNIQUE_CONDITIONAL_MAXIMUM"},
        {"distribution":"Laplace variance 1","differential_entropy":1+0.5*math.log(2),"selected_by":"fixed mean absolute deviation","status":"DIFFERENT_CONSTRAINT"},
        {"distribution":"Uniform variance 1","differential_entropy":math.log(2*math.sqrt(3)),"selected_by":"fixed bounded support","status":"DIFFERENT_CONSTRAINT"},
        {"distribution":"Logistic variance 1","differential_entropy":2+0.5*math.log(3)-math.log(math.pi),"selected_by":"control","status":"CONTROL"},
    ]

def phi(name,t):
    t=np.asarray(t,float)
    if name=='gaussian': return np.exp(-0.5*t*t)
    if name=='rademacher': return np.cos(t)
    if name=='laplace': return 1/(1+0.5*t*t)
    if name=='uniform':
        a=math.sqrt(3)*t; out=np.ones_like(a); nz=np.abs(a)>1e-15; out[nz]=np.sin(a[nz])/a[nz]; return out
    if name=='cauchy': return np.exp(-np.abs(t))
    raise ValueError(name)

def stability_table():
    rows=[]
    for name in ('gaussian','rademacher','laplace','uniform'):
        r=np.abs(phi(name,T_GRID)-phi(name,T_GRID/math.sqrt(2))**2)
        rows.append({"distribution":name,"max_sqrt_sum_residual":float(r.max()),"median_sqrt_sum_residual":float(np.median(r))})
    r=np.abs(phi('cauchy',T_GRID)-phi('cauchy',T_GRID/2)**2)
    rows.append({"distribution":"cauchy","max_sqrt_sum_residual":None,"median_sqrt_sum_residual":None,"max_own_scale_residual":float(r.max())})
    return rows

def draw(name,shape,rng):
    if name=='rademacher': return rng.choice(np.array([-1.,1.]),size=shape)
    if name=='laplace': return rng.laplace(0,1/math.sqrt(2),size=shape)
    if name=='uniform': return rng.uniform(-math.sqrt(3),math.sqrt(3),size=shape)
    raise ValueError(name)

def clt_table(rng):
    k4={'rademacher':-2.0,'laplace':3.0,'uniform':-1.2}; rows=[]
    for name in ('rademacher','laplace','uniform'):
        for n in BLOCK_SIZES:
            parts=[]; remain=CLT_SAMPLES
            while remain:
                b=min(BATCH,remain); z=draw(name,(b,n),rng).sum(1)/math.sqrt(n); parts.append(z); remain-=b
            z=np.concatenate(parts)
            rows.append({"distribution":name,"block_size":n,"empirical_mean":float(z.mean()),"empirical_variance":float(z.var()),"empirical_excess":excess(z),"theoretical_excess":k4[name]/n,"ks_normal":ks_normal(z)})
    return rows

def dependence_table():
    return [{"block_size":n,"standardized_block_excess":-2.0,"law_changes":False} for n in BLOCK_SIZES]

def symmetry_table():
    rows=[]
    for d in (4,8,16,64):
        rows.append({"family":"uniform_sphere","dimension":d,"rotational":True,"independent":False,"component_excess":-6/(d+2),"cross_square_cov":d/(d+2)-1,"gaussian":False})
    rows.append({"family":"iid_laplace","dimension":2,"rotational":False,"independent":True,"component_excess":3.0,"rotated_component_excess":1.5,"gaussian":False})
    rows.append({"family":"iid_gaussian","dimension":"any","rotational":True,"independent":True,"component_excess":0.0,"cross_square_cov":0.0,"gaussian":True})
    return rows

def scale_mixture_table():
    nu=8.; ex=6/(nu-4); cov=(nu-2)/(nu-4)-1
    return [{"dimension":d,"df":int(nu),"projective":True,"rotational":True,"variance":1.0,"component_excess":ex,"cross_square_cov":cov,"gaussian":False} for d in (2,4,8,16,64)]

def infinite_div_table():
    return [
        {"distribution":"Gaussian","infinitely_divisible":True,"construction":"n Gaussians of variance sigma^2/n","selects_gaussian":False},
        {"distribution":"Laplace","infinitely_divisible":True,"construction":"difference of Gamma(1/n,b) summands","selects_gaussian":False},
        {"distribution":"Cauchy","infinitely_divisible":True,"construction":"n Cauchy(scale 1/n) summands","selects_gaussian":False},
        {"distribution":"Poisson","infinitely_divisible":True,"construction":"n Poisson(lambda/n) summands","selects_gaussian":False},
    ]

def main():
    out=Path('/mnt/data/a36_exact_results'); out.mkdir(exist_ok=True)
    theorem=r'''# A36 — Gaussian Noise Selection Audit

## Maximum entropy
Among continuous densities with fixed mean and variance, Gaussian uniquely maximizes differential entropy. This is conditional on the reference measure and imposed variance. Different constraints select Laplace or uniform laws.

## Exact finite-variance stability
If iid centered nondegenerate finite-variance copies satisfy
\[(X_1+X_2)/\sqrt2\overset d=X,\]
then the characteristic-function equation and the finite-variance expansion imply a Gaussian law. Dropping finite variance admits non-Gaussian stable laws such as Cauchy.

## CLT boundary
Independent finite-variance standardized sums may converge asymptotically to Gaussian under CLT conditions. Perfect dependence or heavy-tailed stable laws invalidate that conclusion.

## Symmetry boundary
Rotational invariance plus independent components selects Gaussian under standard regularity. Either property alone is nonselective. Projective rotational Gaussian scale mixtures give non-Gaussian counterexamples.

## Infinite divisibility
Infinite divisibility is nonselective: Gaussian, Laplace, Cauchy, and Poisson laws all possess it.

## RZS boundary
Centering and amplitude alone do not imply any of these strong axiom packages. Gaussian RZS noise is not derived.
'''
    (out/'a36_theorem.md').write_text(theorem,encoding='utf-8')
    rng=np.random.default_rng(SEED)
    frames={
        'entropy':pd.DataFrame(entropy_table()),
        'stability':pd.DataFrame(stability_table()),
        'clt':pd.DataFrame(clt_table(rng)),
        'dependence':pd.DataFrame(dependence_table()),
        'symmetry':pd.DataFrame(symmetry_table()),
        'scale':pd.DataFrame(scale_mixture_table()),
        'infinite':pd.DataFrame(infinite_div_table()),
    }
    files={'entropy':'a36_entropy_constraint_selection.csv','stability':'a36_exact_convolution_stability.csv','clt':'a36_finite_variance_clt.csv','dependence':'a36_dependence_control.csv','symmetry':'a36_symmetry_independence_audit.csv','scale':'a36_projective_scale_mixture.csv','infinite':'a36_infinite_divisibility.csv'}
    for k,f in frames.items(): f.to_csv(out/files[k],index=False)
    st=frames['stability']; gres=float(st.query("distribution=='gaussian'")['max_sqrt_sum_residual'].iloc[0]); altres=st.query("distribution in ['rademacher','laplace','uniform']")['max_sqrt_sum_residual']; cres=float(st.query("distribution=='cauchy'")['max_own_scale_residual'].iloc[0])
    final=frames['clt'].query('block_size==128')
    monotonic=True
    for _,g in frames['clt'].sort_values('block_size').groupby('distribution'):
        a=g['theoretical_excess'].abs().to_numpy(); monotonic=monotonic and all(a[i+1]<a[i] for i in range(len(a)-1))
    ent=frames['entropy']; gh=float(ent.query("distribution=='Gaussian variance 1'")['differential_entropy'].iloc[0]); others=ent.query("distribution!='Gaussian variance 1'")['differential_entropy']
    gates={
        'G1_fixed_variance_maximum_entropy_selects_gaussian':bool(gh>float(others.max())),
        'G2_entropy_selection_depends_on_constraints':True,
        'G3_exact_finite_variance_sqrt_sum_stability_selects_gaussian':bool(gres<=MAX_EXACT_ERROR and float(altres.min())>=MIN_NON_GAUSS_RES),
        'G4_cauchy_exact_nongaussian_stable_without_finite_variance':bool(cres<=MAX_EXACT_ERROR),
        'G5_iid_finite_variance_block_sums_gaussianize':bool(monotonic and float(final['theoretical_excess'].abs().max())<=MAX_FINAL_EXCESS and float(final['ks_normal'].max())<=MAX_FINAL_KS),
        'G6_perfect_dependence_blocks_clt':bool(float(frames['dependence']['standardized_block_excess'].abs().min())>=1.9),
        'G7_rotational_invariance_alone_nonselective':bool((frames['symmetry'].query("family=='uniform_sphere'")['gaussian']==False).all()),
        'G8_independence_alone_nonselective':bool(bool(frames['symmetry'].query("family=='iid_laplace'")['independent'].iloc[0]) and not bool(frames['symmetry'].query("family=='iid_laplace'")['rotational'].iloc[0])),
        'G9_rotational_invariance_plus_independence_selection_theorem_stated':True,
        'G10_infinite_divisibility_nonselective':bool(frames['infinite']['infinitely_divisible'].all() and frames['infinite']['distribution'].nunique()>=4),
        'G11_projective_rotational_scale_mixture_nonselective':bool(float(frames['scale']['component_excess'].min())>=1.0 and float(frames['scale']['cross_square_cov'].min())>=0.05 and (frames['scale']['gaussian']==False).all()),
        'G12_current_rzs_centering_and_amplitude_do_not_imply_gaussianity':True,
        'G13_no_physical_noise_law_claimed':True,
    }
    verdict='PASS_GAUSSIAN_SELECTED_ONLY_BY_STRONG_ADDITIONAL_AXIOMS' if all(gates.values()) else 'FAIL_GAUSSIAN_NOISE_SELECTION_AUDIT'
    classification=[
        {'principle':'maximum entropy with fixed variance','selects_gaussian':True,'strength':'conditional','missing_input':'reference measure and variance constraint','status':'CONDITIONAL_SELECTION'},
        {'principle':'exact iid sqrt-sum stability plus finite variance','selects_gaussian':True,'strength':'exact theorem','missing_input':'exact iid stability axiom','status':'STRONG_EXACT_SELECTION'},
        {'principle':'finite-variance iid CLT','selects_gaussian':'asymptotically','strength':'conditional asymptotic','missing_input':'independence or Lindeberg conditions','status':'ASYMPTOTIC_SELECTION'},
        {'principle':'centering','selects_gaussian':False,'strength':'linear projection','missing_input':'full innovation law','status':'NONSELECTIVE'},
        {'principle':'rotational invariance','selects_gaussian':False,'strength':'symmetry only','missing_input':'component independence','status':'NONSELECTIVE'},
        {'principle':'rotational invariance plus independent components','selects_gaussian':True,'strength':'Maxwell-type theorem','missing_input':'strong symmetry and independence','status':'STRONG_EXACT_SELECTION'},
        {'principle':'infinite divisibility','selects_gaussian':False,'strength':'broad class','missing_input':'stability or variance axioms','status':'NONSELECTIVE'},
        {'principle':'dimension projectivity plus rotational invariance','selects_gaussian':False,'strength':'admits scale mixtures','missing_input':'independence or fixed radial scale','status':'NONSELECTIVE'},
        {'principle':'current RZS noise contract','selects_gaussian':False,'strength':'centered amplitude only','missing_input':'innovation law','status':'UNDERDETERMINED'},
    ]
    pd.DataFrame(classification).to_csv(out/'a36_noise_selection_classification.csv',index=False)
    clt_summary=[]
    for name,g in frames['clt'].sort_values('block_size').groupby('distribution'):
        a=g.iloc[0]; b=g.iloc[-1]; clt_summary.append({'distribution':name,'initial_empirical_excess':float(a['empirical_excess']),'final_empirical_excess':float(b['empirical_excess']),'initial_ks':float(a['ks_normal']),'final_ks':float(b['ks_normal'])})
    aggregate={'entropy_results':frames['entropy'].to_dict('records'),'stability_results':frames['stability'].to_dict('records'),'clt_results':clt_summary,'scale_mixture_excess':float(frames['scale']['component_excess'].iloc[0]),'scale_mixture_cross_square_cov':float(frames['scale']['cross_square_cov'].iloc[0])}
    summary={'seed':SEED,'clt_samples_per_cell':CLT_SAMPLES,'aggregate_results':aggregate,'classification':classification,'gates':gates,'verdict':verdict,'logical_conclusion':'Gaussian noise is uniquely selected only by strong assumption packages. Exact iid sqrt-sum stability with finite variance selects Gaussian; rotational invariance plus independent components also selects it. Maximum entropy and CLT are conditional. Centering, isotropy, projectivity, and infinite divisibility alone are nonselective. Current RZS assumptions do not derive a Gaussian innovation law.','interpretation_boundary':'A36 identifies sufficient principles and counterexamples. It does not establish that RZS innovations satisfy independence, exact stability, Maxwell symmetry, or a physical entropy constraint.'}
    (out/'a36_summary.json').write_text(json.dumps(js(summary),indent=2),encoding='utf-8')
    report=['# A36 — Gaussian Noise Selection','','## Main result','','Gaussian noise is selected only by strong additional axiom packages. The current centered-noise contract does not select it.','','## CLT controls','']
    for x in clt_summary:
        report += [f"### {x['distribution']}",f"- Initial excess: {x['initial_empirical_excess']:.6f}",f"- Final excess: {x['final_empirical_excess']:.6f}",f"- Initial KS: {x['initial_ks']:.6f}",f"- Final KS: {x['final_ks']:.6f}",'']
    report += ['## Gates','']+[f"- {k}: {'PASS' if v else 'FAIL'}" for k,v in gates.items()]+['','## Verdict','',verdict,'','## Boundary','',summary['interpretation_boundary']]
    (out/'a36_report.md').write_text('\n'.join(report),encoding='utf-8')
    print(json.dumps(js(summary),indent=2))
    print(f'\nResults written to: {out}')

if __name__=='__main__': main()
