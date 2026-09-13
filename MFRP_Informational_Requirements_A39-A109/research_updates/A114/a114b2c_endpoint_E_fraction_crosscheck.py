#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2C1_ENDPOINT_E_FRACTION_CROSSCHECK_20260913.json'
BETA=F(1,8); GAMMA=F(1,16); TARGET=F(1,2)

def solve(mat,rhs):
    n=len(rhs); aug=[[F(v) for v in mat[i]]+[F(rhs[i])] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if aug[i][c])
        if p!=c: aug[c],aug[p]=aug[p],aug[c]
        q=aug[c][c]; aug[c]=[v/q for v in aug[c]]
        for i in range(n):
            if i==c: continue
            q=aug[i][c]
            if q: aug[i]=[aug[i][j]-q*aug[c][j] for j in range(n+1)]
    return [aug[i][-1] for i in range(n)]

def tr(a): return [list(x) for x in zip(*a)]
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def sgn(x): return (x>0)-(x<0)
def eps_for(M): return F(1,(1875 if M%2==0 else 2500)*2**(M//2))
def fun(name,s,x): return {'alpha':s,'beta':BETA,'gamma':GAMMA}[name]**x

def b_exact(M,s):
    est=math.ceil(M*math.log(2)/(-2*math.log(float(s))))
    def gt(k): return (2**M)*(s.numerator**(2*k)) > s.denominator**(2*k)
    b=est
    while gt(b): b+=1
    while b>0 and not gt(b-1): b-=1
    assert not gt(b) and gt(b-1)
    return b

def arch(M,j,label):
    h=M//2
    if label=='C': return [0,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
    if label=='E': return [j-1,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
    if label=='GP': return [0,j,j+1,M],[1,h,h+1],[('alpha',1),('beta',-1),('gamma',1)]
    raise KeyError(label)

def basis(M,s,j,label):
    ps,qs,acts=arch(M,j,label); mean=F(M,2); eps=eps_for(M)
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
    basic=solve(rows,rhs); dual=solve(tr(rows),obj)
    return {'ps':ps,'qs':qs,'acts':acts,'rows':rows,'rhs':rhs,'obj':obj,'basic':basic,'dual':dual}

def rc_p(M,s,z,x):
    col=[F(1),F(0),F(x),F(0),F(0)]+[F(sg)*fun(name,s,x) for name,sg in z['acts']]
    return dot(col,z['dual'])-TARGET**x

def rc_q(M,s,z,x):
    col=[F(0),F(1),F(0),F(x),TARGET**x]+[-F(sg)*fun(name,s,x) for name,sg in z['acts']]
    return dot(col,z['dual'])

def slack(M,s,z,name,sg):
    ps,qs,basic=z['ps'],z['qs'],z['basic']; t=basic[-1]
    d=sum((fun(name,s,x)*basic[i] for i,x in enumerate(ps)),F(0))-sum((fun(name,s,x)*basic[len(ps)+i] for i,x in enumerate(qs)),F(0))
    return 2*eps_for(M)*t-F(sg)*d

def full_E(M,s,j):
    z=basis(M,s,j,'E'); ps,qs,acts=z['ps'],z['qs'],z['acts']; cond=[]
    cond += [(f'basic_p_{x}',z['basic'][i]) for i,x in enumerate(ps)]
    cond += [(f'basic_q_{x}',z['basic'][len(ps)+i]) for i,x in enumerate(qs)]
    cond += [('basic_t',z['basic'][-1])]
    for i,(name,sg) in enumerate(acts): cond.append((f'active_dual_{name}_{sg:+d}',z['dual'][5+i]))
    for x in range(M+1):
        if x not in set(ps): cond.append((f'rc_p_{x}',rc_p(M,s,z,x)))
        if x not in set(qs): cond.append((f'rc_q_{x}',rc_q(M,s,z,x)))
    for name,sg in acts: cond.append((f'slack_{name}_{-sg:+d}',slack(M,s,z,name,-sg)))
    cond.append(('slack_gamma_-1',slack(M,s,z,'gamma',-1)))
    cond.append(('slack_gamma_+1',slack(M,s,z,'gamma',1)))
    failures=[n for n,v in cond if v<=0]
    residual=[dot(z['rows'][i],z['basic'])-z['rhs'][i] for i in range(len(z['rhs']))]
    return z,cond,failures,all(x==0 for x in residual),dot(z['obj'],z['basic'])==dot(z['rhs'],z['dual'])

def compressed_value(M,s,k):
    z=basis(M,s,k,'C'); return dot(z['obj'],z['basic'])

def premise(M,s):
    b=b_exact(M,s); j=b+2
    vals={k:compressed_value(M,s,k) for k in (b+1,b+2,b+3)}
    strict=vals[j]>vals[b+1] and vals[j]>vals[b+3]
    gp=basis(M,s,j,'GP'); phi_sign=sgn(gp['basic'][gp['ps'].index(j+1)])
    return b,j,strict,phi_sign

def row(M,s,role,expected_failures):
    b,j,strict,phi=premise(M,s)
    C=basis(M,s,j,'C'); E=basis(M,s,j,'E')
    p0C=C['basic'][C['ps'].index(0)]; rq0=rc_q(M,s,E,0)
    Q=s**(j-1)/F(1,2**(M//2))
    z,cond,failures,eq,pd=full_E(M,s,j)
    return {'M':M,'s':f'{s.numerator}/{s.denominator}','role':role,'b':b,'j':j,'strict_bplus2':strict,'phi_sign':phi,'Q_in_source_box':F(9,1000)<Q<F(1,25),'p0C_sign':sgn(p0C),'rE_q0_sign':sgn(rq0),'E_condition_count':len(cond),'expected_count':2*M+9,'E_failures':failures,'expected_failures':expected_failures,'failure_match':failures==expected_failures,'equations_exact':eq,'primal_dual_equal':pd}

controls=[
  row(522,F(263,2000),'E_even_pass',[]),
  row(999,F(129,1000),'E_odd_pass',[]),
  row(1000,F(261,2000),'E_even_large_pass',[]),
  row(538,F(53,400),'C_negative_control',['basic_p_94']),
  row(555,F(13,100),'QI_negative_control',['rc_q_0']),
  row(521,F(129,1000),'QA_negative_control',['rc_q_0']),
]
gates={
  'all_premises_exact':all(r['strict_bplus2'] and r['phi_sign']<0 and r['Q_in_source_box'] for r in controls),
  'E_passes_have_both_branch_signs':all(r['p0C_sign']<0 and r['rE_q0_sign']>0 for r in controls[:3]),
  'E_passes_full_KKT':all(not r['E_failures'] and r['E_condition_count']==r['expected_count'] for r in controls[:3]),
  'negative_controls_fail_exactly_as_declared':all(r['failure_match'] for r in controls[3:]),
  'C_control_fails_pjm1_only':controls[3]['E_failures']==['basic_p_94'] and controls[3]['p0C_sign']>0,
  'QI_QA_controls_fail_rq0_only':all(r['E_failures']==['rc_q_0'] and r['p0C_sign']<0 and r['rE_q0_sign']<0 for r in controls[4:]),
  'all_equations_exact':all(r['equations_exact'] for r in controls),
  'all_primal_dual_equal':all(r['primal_dual_equal'] for r in controls),
}
out={'audit':'A114B2C1_ENDPOINT_E_FRACTION_CROSSCHECK','status':'PASS' if all(gates.values()) else 'FAIL','method':'standalone fractions.Fraction LP reconstruction; no import from analytic certificate','controls':controls,'gates':gates,'claim_limits':['Finite regression/negative controls only; analytic all-tail proof is separate.']}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
