#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from typing import Callable
import sympy as sp

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2_W1_M521_EXACT_KKT_CERTIFICATE_20260912.json'
M=521
H=M//2
S=sp.Rational(129,1000)
MEAN=sp.Rational(M,2)
EPS=sp.Rational(1,2500*2**H)
TARGET_BASE=sp.Rational(1,2)
BETA_BASE=sp.Rational(1,8)
GAMMA_BASE=sp.Rational(1,16)
B=89


def target(x:int): return TARGET_BASE**x
def alpha(x:int): return S**x
def beta(x:int): return BETA_BASE**x
def gamma(x:int): return GAMMA_BASE**x
def sgn(v): return 1 if v>0 else -1 if v<0 else 0

def exact_b_gate():
    n,d=int(S.p),int(S.q)
    left=(2**M)*(n**(2*(B-1))) > d**(2*(B-1))
    right=(2**M)*(n**(2*B)) <= d**(2*B)
    return bool(left and right)

def compressed_obj(k:int):
    ps=[0,k,M]; qs=[1,H,H+1]
    rows=[
      [1,1,1,0,0,0,-1],
      [0,0,0,1,1,1,-1],
      [*ps,0,0,0,-MEAN],
      [0,0,0,*qs,-MEAN],
      [0,0,0,*[target(x) for x in qs],0],
      [*[alpha(x) for x in ps],*[-alpha(x) for x in qs],-2*EPS],
      [*[-beta(x) for x in ps],*[beta(x) for x in qs],-2*EPS],
    ]
    A=sp.Matrix(rows); rhs=sp.Matrix([0,0,0,0,1,0,0])
    z=A.inv(method='DM')*rhs
    return sp.cancel(sum(target(x)*z[i] for i,x in enumerate(ps)))

def gamma_upper_pivot():
    # Reconstruct A112-A reduced gamma-plus 3x3 bridge for j=b+1.
    j=B+1; qs=[1,H,H+1]
    AQ=sp.Matrix([[1,1,1],qs,[target(x) for x in qs]])
    slope=AQ.inv(method='DM')*sp.Matrix([1,MEAN,0])
    const=AQ.inv(method='DM')*sp.Matrix([0,0,1])
    def qc(base): return sp.cancel(sum(const[i]*base**qs[i] for i in range(3)))
    def qd(base): return sp.cancel(sum(slope[i]*base**qs[i] for i in range(3)))
    def br(base,k): return sp.cancel(base**k-sp.Rational(M-k,M)-sp.Rational(k,M)*base**M)
    def ar(base): return sp.cancel((1+base**M)/2)
    Hb=sp.cancel(ar(BETA_BASE)-qd(BETA_BASE)+2*EPS)
    Hg=sp.cancel(ar(GAMMA_BASE)-qd(GAMMA_BASE)-2*EPS)
    Hs=sp.cancel(ar(S)-qd(S)-2*EPS)
    G=sp.Matrix([
      [br(BETA_BASE,j),br(BETA_BASE,j+1),Hb],
      [br(GAMMA_BASE,j),br(GAMMA_BASE,j+1),Hg],
      [br(S,j),br(S,j+1),Hs],
    ])
    rhs=sp.Matrix([qc(BETA_BASE),qc(GAMMA_BASE),qc(S)])
    DG=sp.cancel(G.det(method='domain-ge'))
    G1=G.copy(); G1[:,1]=rhs
    G0=G.copy(); G0[:,0]=rhs
    # F_j = numerator p_(j+1), F_(j+1) = - numerator p_j.
    Fj=sp.cancel(G1.det(method='domain-ge'))
    Fjp1=sp.cancel(-G0.det(method='domain-ge'))
    return {'j':j,'DG':DG,'F_bplus1':Fj,'F_bplus2':Fjp1}

def basis_check(ps,qs,active_bands,label):
    assert len(ps)+len(qs)+1==8
    funcs={'alpha':alpha,'beta':beta,'gamma':gamma}
    rows=[
      [*[1]*len(ps), *[0]*len(qs), -1],
      [*[0]*len(ps), *[1]*len(qs), -1],
      [*ps, *[0]*len(qs), -MEAN],
      [*[0]*len(ps), *qs, -MEAN],
      [*[0]*len(ps), *[target(x) for x in qs], 0],
    ]
    for name,sign in active_bands:
        fn=funcs[name]
        rows.append([*[sign*fn(x) for x in ps], *[-sign*fn(x) for x in qs], -2*EPS])
    A=sp.Matrix(rows); rhs=sp.Matrix([0,0,0,0,1,0,0,0])
    obj=sp.Matrix([*[target(x) for x in ps], *[0]*len(qs), 0])
    det=sp.cancel(A.det(method='domain-ge'))
    if det==0:
        return {'label':label,'pass':False,'singular':True,'failures':['singular_basis']}
    basic=A.inv(method='DM')*rhs
    dual=A.T.inv(method='DM')*obj
    cond=[]
    names=[*[f'basic_p_{x}' for x in ps],*[f'basic_q_{x}' for x in qs],'basic_t']
    cond.extend(zip(names,basic))
    for row_idx,(name,sign) in enumerate(active_bands,start=5):
        cond.append((f'active_dual_{name}_{"+1" if sign>0 else "-1"}',dual[row_idx]))
    pset=set(ps); qset=set(qs)
    for x in range(M+1):
        if x not in pset:
            col=[1,0,x,0,0]
            for name,sign in active_bands: col.append(sign*funcs[name](x))
            v=sp.cancel(sp.Matrix(col).dot(dual)-target(x))
            cond.append((f'reduced_cost_p_{x}',v))
        if x not in qset:
            col=[0,1,0,x,target(x)]
            for name,sign in active_bands: col.append(-sign*funcs[name](x))
            v=sp.cancel(sp.Matrix(col).dot(dual))
            cond.append((f'reduced_cost_q_{x}',v))
    t=basic[-1]
    def diff(fn:Callable[[int],sp.Rational]):
        return sp.cancel(sum(fn(x)*basic[i] for i,x in enumerate(ps))-sum(fn(x)*basic[len(ps)+i] for i,x in enumerate(qs)))
    for name,sign in active_bands:
        d=diff(funcs[name])
        cond.append((f'inactive_slack_{name}_{"-1" if sign>0 else "+1"}',sp.cancel(2*EPS*t+sign*d)))
    fails=[name for name,v in cond if v<=0]
    min_name,min_val=min(cond,key=lambda kv:kv[1])
    # independent equation/objective checks
    residual=A*basic-rhs
    primal_obj=sp.cancel(obj.dot(basic))
    dual_obj=sp.cancel(rhs.dot(dual))
    return {
      'label':label,'pass':not fails,'singular':False,
      'P_support':ps,'Q_support':qs,'active_bands':[[a,b] for a,b in active_bands],
      'basis_det_sign':sgn(det),'condition_count':len(cond),'expected_count':2*M+9,
      'failures':fails,'min_condition':min_name,'min_decimal':str(sp.N(min_val,16)),
      'all_primal_equations_exact':bool(all(bool(v==0) for v in residual)),
      'primal_dual_objective_equal':bool(primal_obj==dual_obj),
      'basic_signs':{name:sgn(v) for name,v in zip(names,basic)},
      'active_dual_signs':{f'{name}_{sign}':sgn(dual[i+5]) for i,(name,sign) in enumerate(active_bands)},
    }

vals={k:compressed_obj(k) for k in (B+1,B+2,B+3)}
winner=max(vals,key=lambda k:vals[k])
pivot=gamma_upper_pivot()

candidate=basis_check([90,91,521],[0,1,260,261],[('alpha',1),('beta',-1),('gamma',-1)],'q0q1_gamma_minus_candidate')
control_same_support_gamma_plus=basis_check([90,91,521],[0,1,260,261],[('alpha',1),('beta',-1),('gamma',1)],'same_support_gamma_plus_control')
control_gamma_plus_b1=basis_check([0,90,91,521],[1,260,261],[('alpha',1),('beta',-1),('gamma',1)],'gamma_plus_contact_bplus1_control')
control_gamma_plus_b2=basis_check([0,91,92,521],[1,260,261],[('alpha',1),('beta',-1),('gamma',1)],'gamma_plus_contact_bplus2_control')

gates={
 'b_equals_89_exactly':exact_b_gate(),
 'compressed_winner_is_strict_bplus2': winner==B+2 and vals[B+2]>vals[B+1] and vals[B+2]>vals[B+3],
 'upper_gamma_pivot_F_bplus2_is_negative': pivot['F_bplus2']<0,
 'reduced_gamma_denominator_positive_at_bplus1':pivot['DG']>0,
 'candidate_full_exact_KKT_passes':candidate['pass'],
 'candidate_has_exact_1051_strict_conditions':candidate.get('condition_count')==1051,
 'candidate_equations_exact':candidate.get('all_primal_equations_exact') is True,
 'candidate_primal_dual_equality_exact':candidate.get('primal_dual_objective_equal') is True,
 'same_support_gamma_plus_is_rejected':not control_same_support_gamma_plus['pass'],
 'gamma_plus_contact_bplus1_is_rejected':not control_gamma_plus_b1['pass'],
 'gamma_plus_contact_bplus2_is_rejected':not control_gamma_plus_b2['pass'],
}
gates={k:bool(v) for k,v in gates.items()}
out={
 'audit':'A114B2_W1_M521_EXACT_KKT_CERTIFICATE',
 'status':'PASS' if all(gates.values()) else 'FAIL',
 'contract':{'M':M,'s':str(S),'epsilon':str(EPS),'h':H,'b':B},
 'compressed':{'values_decimal':{str(k):str(sp.N(v,24)) for k,v in vals.items()},'strict_winner':winner},
 'upper_gamma_pivot':{'DG_sign':sgn(pivot['DG']),'F_bplus1_sign':sgn(pivot['F_bplus1']),'F_bplus2_sign':sgn(pivot['F_bplus2'])},
 'candidate':candidate,
 'negative_controls':[control_same_support_gamma_plus,control_gamma_plus_b1,control_gamma_plus_b2],
 'gates':gates,
 'claim_limits':[
   'This is an exact pointwise full-LP KKT theorem at M=521,s=129/1000, not an all-M A114-B2 architecture theorem.',
   'The high-precision unrestricted simplex was used only for candidate discovery and is not a proof dependency.',
   'No claim is made that q0/q1 gamma-minus is the only non-gamma-plus architecture in the strict compressed b+2 phase.'
 ]
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gates':gates,'candidate':{k:candidate.get(k) for k in ('pass','condition_count','expected_count','failures','min_condition','min_decimal')},'controls':[{k:c.get(k) for k in ('label','pass','failures','min_condition','min_decimal')} for c in out['negative_controls']]},indent=2))
