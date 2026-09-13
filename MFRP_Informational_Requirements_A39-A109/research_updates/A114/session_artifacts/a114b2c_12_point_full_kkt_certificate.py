#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2C_12_POINT_FULL_KKT_CERTIFICATE_20260913.json'
BETA=F(1,8); GAMMA=F(1,16); TARGET=F(1,2)
PROBES=[F(129,1000),F(259,2000),F(13,100),F(261,2000),F(131,1000),F(263,2000),F(33,250),F(53,400),F(133,1000)]

# 12 adversarial exact controls spanning four residual architectures.
# These were selected by discovery, but every premise and full KKT verdict is recomputed exactly here.
CONTROL_POINTS=[
    (538,F(53,400),'C'),(973,F(13,100),'C'),(989,F(33,250),'C'),
    (522,F(263,2000),'E'),(800,F(261,2000),'E'),(1000,F(261,2000),'E'),
    (555,F(13,100),'QI'),(908,F(13,100),'QI'),(967,F(13,100),'QI'),
    (521,F(129,1000),'QA'),(970,F(129,1000),'QA'),(1000,F(129,1000),'QA'),
]
def solve(mat,rhs):
    n=len(rhs)
    aug=[[F(v) for v in mat[i]]+[F(rhs[i])] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if aug[i][c])
        if p!=c: aug[c],aug[p]=aug[p],aug[c]
        q=aug[c][c]
        aug[c]=[v/q for v in aug[c]]
        for i in range(n):
            if i==c: continue
            q=aug[i][c]
            if q:
                aug[i]=[aug[i][j]-q*aug[c][j] for j in range(n+1)]
    return [aug[i][-1] for i in range(n)]

def transpose(a): return [list(x) for x in zip(*a)]
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def sgn(x): return (x>0)-(x<0)
def fs(x): return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def powf(base,k): return base**k

def b_exact(M,s):
    # b=ceil(M*c(s)); c(s)>k/M iff 2^M*s^(2k)>1.
    est=math.ceil(M*math.log(2)/(-2*math.log(float(s))))
    def mc_gt(k):
        return (2**M)*(s.numerator**(2*k)) > s.denominator**(2*k)
    b=est
    while mc_gt(b): b+=1
    while b>0 and not mc_gt(b-1): b-=1
    # now M c <= b and > b-1
    assert not mc_gt(b) and mc_gt(b-1)
    return b

def eps_for(M):
    h=M//2
    return F(1,(1875 if M%2==0 else 2500)*2**h)

def fun(name,s,x):
    return {'alpha':s,'beta':BETA,'gamma':GAMMA}[name]**x

def basis_system(M,s,ps,qs,acts):
    mean=F(M,2); eps=eps_for(M)
    rows=[
      [F(1)]*len(ps)+[F(0)]*len(qs)+[F(-1)],
      [F(0)]*len(ps)+[F(1)]*len(qs)+[F(-1)],
      [F(x) for x in ps]+[F(0)]*len(qs)+[-mean],
      [F(0)]*len(ps)+[F(x) for x in qs]+[-mean],
      [F(0)]*len(ps)+[TARGET**x for x in qs]+[F(0)],
    ]
    for name,sg in acts:
        rows.append([F(sg)*fun(name,s,x) for x in ps]+[-F(sg)*fun(name,s,x) for x in qs]+[-2*eps])
    rhs=[F(0),F(0),F(0),F(0),F(1)]+[F(0)]*len(acts)
    obj=[TARGET**x for x in ps]+[F(0)]*len(qs)+[F(0)]
    basic=solve(rows,rhs)
    dual=solve(transpose(rows),obj)
    return rows,rhs,obj,basic,dual

def inactive_slack(M,s,ps,qs,acts,basic,name,sg):
    eps=eps_for(M); t=basic[-1]
    d=sum((fun(name,s,x)*basic[i] for i,x in enumerate(ps)),F(0))-sum((fun(name,s,x)*basic[len(ps)+i] for i,x in enumerate(qs)),F(0))
    # Slack for orientation sg: 2 eps t - sg * d >=0, matching row sg*d-2eps*t=0 when active.
    return 2*eps*t-F(sg)*d

def reduced_cost_q(M,s,ps,qs,acts,dual,x):
    col=[F(0),F(1),F(0),F(x),TARGET**x]+[-F(sg)*fun(name,s,x) for name,sg in acts]
    return dot(col,dual)

def reduced_cost_p(M,s,ps,qs,acts,dual,x):
    col=[F(1),F(0),F(x),F(0),F(0)]+[F(sg)*fun(name,s,x) for name,sg in acts]
    return dot(col,dual)-TARGET**x

def arch(M,s,j,label):
    h=M//2
    if label=='C': return [0,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
    if label=='E': return [j-1,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
    if label=='QI': return [j,M],[0,1,h,h+1],[('alpha',1),('beta',-1)]
    if label=='QA': return [j-1,j,M],[0,1,h,h+1],[('alpha',1),('beta',-1),('gamma',-1)]
    if label=='GM': return [0,j-1,j,M],[1,h,h+1],[('alpha',1),('beta',-1),('gamma',-1)]
    if label=='GP': return [0,j,j+1,M],[1,h,h+1],[('alpha',1),('beta',-1),('gamma',1)]
    raise KeyError(label)

def solve_arch(M,s,j,label):
    ps,qs,acts=arch(M,s,j,label)
    rows,rhs,obj,basic,dual=basis_system(M,s,ps,qs,acts)
    return {'ps':ps,'qs':qs,'acts':acts,'rows':rows,'rhs':rhs,'obj':obj,'basic':basic,'dual':dual}

def compressed_value(M,s,k):
    z=solve_arch(M,s,k,'C')
    return dot(z['obj'],z['basic'])

def premise(M,s):
    b=b_exact(M,s); j=b+2
    vals={k:compressed_value(M,s,k) for k in (b+1,b+2,b+3)}
    strict=vals[j]>vals[b+1] and vals[j]>vals[b+3]
    gp=solve_arch(M,s,j,'GP')
    pjp1=gp['basic'][gp['ps'].index(j+1)]
    # In the frozen tail D_G>0 is already proved in A114-B1, so sign(p_{j+1}^{GP})=sign(Phi).
    phi_sign=sgn(pjp1)
    return b,j,strict,phi_sign,vals

def diagnostics(M,s,j):
    C=solve_arch(M,s,j,'C'); E=solve_arch(M,s,j,'E'); QI=solve_arch(M,s,j,'QI'); QA=solve_arch(M,s,j,'QA')
    p0C=C['basic'][C['ps'].index(0)]
    pjm1E=E['basic'][E['ps'].index(j-1)]
    rcq0E=reduced_cost_q(M,s,E['ps'],E['qs'],E['acts'],E['dual'],0)
    lamgmQA=QA['dual'][5+2]
    slackgmQI=inactive_slack(M,s,QI['ps'],QI['qs'],QI['acts'],QI['basic'],'gamma',-1)
    pjm1QA=QA['basic'][QA['ps'].index(j-1)]
    q0QI=QI['basic'][len(QI['ps'])+QI['qs'].index(0)]
    gmE=inactive_slack(M,s,E['ps'],E['qs'],E['acts'],E['basic'],'gamma',-1)
    gpE=inactive_slack(M,s,E['ps'],E['qs'],E['acts'],E['basic'],'gamma',1)
    return {
      'p0C':p0C,'pjm1E':pjm1E,'rcq0E':rcq0E,'lamgmQA':lamgmQA,
      'slackgmQI':slackgmQI,'pjm1QA':pjm1QA,'q0QI':q0QI,'gmE':gmE,'gpE':gpE,
    }

def predicted(d):
    if d['p0C']>0: return 'C'
    if d['rcq0E']>0: return 'E'
    if d['slackgmQI']>0: return 'QI'
    return 'QA'

def full_kkt(M,s,j,label):
    z=solve_arch(M,s,j,label); ps,qs,acts=z['ps'],z['qs'],z['acts']; basic=z['basic']; dual=z['dual']
    cond=[]
    names=[*[f'basic_p_{x}' for x in ps],*[f'basic_q_{x}' for x in qs],'basic_t']
    cond.extend(zip(names,basic))
    for i,(name,sg) in enumerate(acts): cond.append((f'active_dual_{name}_{sg:+d}',dual[5+i]))
    pset=set(ps); qset=set(qs)
    for x in range(M+1):
        if x not in pset: cond.append((f'reduced_cost_p_{x}',reduced_cost_p(M,s,ps,qs,acts,dual,x)))
        if x not in qset: cond.append((f'reduced_cost_q_{x}',reduced_cost_q(M,s,ps,qs,acts,dual,x)))
    # opposite slacks of active bands
    for name,sg in acts:
        cond.append((f'inactive_slack_{name}_{-sg:+d}',inactive_slack(M,s,ps,qs,acts,basic,name,-sg)))
    # both orientations for inactive gamma when gamma is not active
    if all(name!='gamma' for name,_ in acts):
        cond.append(('inactive_slack_gamma_-1',inactive_slack(M,s,ps,qs,acts,basic,'gamma',-1)))
        cond.append(('inactive_slack_gamma_+1',inactive_slack(M,s,ps,qs,acts,basic,'gamma',1)))
    failures=[n for n,v in cond if v<=0]
    residual=[dot(z['rows'][i],basic)-z['rhs'][i] for i in range(len(z['rhs']))]
    mn,mv=min(cond,key=lambda q:q[1])
    return {
      'pass':not failures,'condition_count':len(cond),'expected_count':2*M+9,
      'failures':failures,'min_condition':mn,'min_decimal':f'{float(mv):.12e}',
      'equations_exact':all(v==0 for v in residual),'primal_dual_equal':dot(z['obj'],basic)==dot(z['rhs'],dual)
    }

controls=[]
for M,s,expected in CONTROL_POINTS:
    b,j,strict,phi_sign,vals=premise(M,s); d=diagnostics(M,s,j); pred=predicted(d); k=full_kkt(M,s,j,pred)
    controls.append({'M':M,'s':fs(s),'b':b,'j':j,'strict_bplus2':strict,'phi_sign':phi_sign,
                     'expected':expected,'predicted':pred,'kkt':k,
                     'signs':{q:sgn(v) for q,v in d.items()}})

control_gates=[c['strict_bplus2'] and c['phi_sign']<0 and c['predicted']==c['expected'] and c['kkt']['pass'] and c['kkt']['condition_count']==c['kkt']['expected_count'] and c['kkt']['equations_exact'] and c['kkt']['primal_dual_equal'] for c in controls]
out={
 'audit':'A114B2C_12_POINT_FULL_KKT_CERTIFICATE',
 'status':'PASS' if all(control_gates) else 'FAIL',
 'scope':{'M_range':[521,1000],'probe_count':len(PROBES),'probes':[fs(x) for x in PROBES],
          'premise':'strict compressed b+2 and Phi<0; Phi sign read via p_(j+1) of gamma+ basis using already-proved D_G>0'},
 'relations_tested':[
  'sign p_(j-1)^E = - sign p_0^C',
  'sign lambda_(gamma-)^QA = - sign r_E(q0)',
  'sign p_(j-1)^QA = - sign slack_(gamma-)^QI',
  'if p0^C<0 then p_(j-1)^E>0',
  'if p0^C<0 then q0^QI>0',
  'if p0^C<0 then both gamma slacks of E are positive',
 ],
 'full_kkt_controls':controls,
 'claim_limits':[
   'The 12 complete KKT controls are pointwise exact certificates.',
   'The sign tree C/E/QI/QA is not promoted here as an all-tail theorem.',
   'Phi=0 remains outside this audit.'
 ]
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'controls':[{'M':c['M'],'s':c['s'],'expected':c['expected'],'predicted':c['predicted'],'kkt_pass':c['kkt']['pass'],'count':c['kkt']['condition_count']} for c in controls]},indent=2))
