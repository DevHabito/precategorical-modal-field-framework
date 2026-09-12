#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2_W1_M521_FRACTION_CROSSCHECK_20260912.json'
M=521; H=M//2; S=F(129,1000); MEAN=F(M,2); EPS=F(1,2500*2**H)

def powers(base):
    a=[F(1)]*(M+1)
    for i in range(1,M+1): a[i]=a[i-1]*base
    return a
T=powers(F(1,2)); A=powers(S); BE=powers(F(1,8)); GA=powers(F(1,16))
FUN={'alpha':A,'beta':BE,'gamma':GA}

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

def check(ps,qs,acts,label):
    rows=[
      [1]*len(ps)+[0]*len(qs)+[-1],
      [0]*len(ps)+[1]*len(qs)+[-1],
      ps+[0]*len(qs)+[-MEAN],
      [0]*len(ps)+qs+[-MEAN],
      [0]*len(ps)+[T[x] for x in qs]+[0],
    ]
    for name,sg in acts:
        f=FUN[name]
        rows.append([sg*f[x] for x in ps]+[-sg*f[x] for x in qs]+[-2*EPS])
    rhs=[F(0),F(0),F(0),F(0),F(1),F(0),F(0),F(0)]
    obj=[T[x] for x in ps]+[F(0)]*len(qs)+[F(0)]
    basic=solve(rows,rhs)
    dual=solve(transpose(rows),obj)
    cond=[]
    names=[*[f'basic_p_{x}' for x in ps],*[f'basic_q_{x}' for x in qs],'basic_t']
    cond.extend(zip(names,basic))
    for i,(name,sg) in enumerate(acts): cond.append((f'active_dual_{name}_{sg:+d}',dual[5+i]))
    pset=set(ps); qset=set(qs)
    for x in range(M+1):
        if x not in pset:
            col=[F(1),F(0),F(x),F(0),F(0)]+[F(sg)*FUN[name][x] for name,sg in acts]
            cond.append((f'reduced_cost_p_{x}',dot(col,dual)-T[x]))
        if x not in qset:
            col=[F(0),F(1),F(0),F(x),T[x]]+[-F(sg)*FUN[name][x] for name,sg in acts]
            cond.append((f'reduced_cost_q_{x}',dot(col,dual)))
    t=basic[-1]
    for name,sg in acts:
        f=FUN[name]
        d=sum((f[x]*basic[i] for i,x in enumerate(ps)),F(0))-sum((f[x]*basic[len(ps)+i] for i,x in enumerate(qs)),F(0))
        cond.append((f'inactive_slack_{name}_{-sg:+d}',2*EPS*t+F(sg)*d))
    failures=[n for n,v in cond if v<=0]
    mn,mv=min(cond,key=lambda z:z[1])
    residual=[dot(rows[i],basic)-rhs[i] for i in range(8)]
    return {
      'label':label,'pass':not failures,'condition_count':len(cond),'expected_count':2*M+9,
      'failures':failures,'min_condition':mn,'min_decimal':f'{float(mv):.12e}',
      'all_equations_exact':all(v==0 for v in residual),
      'primal_dual_equal':dot(obj,basic)==dot(rhs,dual)
    }

candidate=check([90,91,521],[0,1,260,261],[('alpha',1),('beta',-1),('gamma',-1)],'candidate')
ctrl1=check([0,90,91,521],[1,260,261],[('alpha',1),('beta',-1),('gamma',1)],'gamma_plus_bplus1')
ctrl2=check([0,91,92,521],[1,260,261],[('alpha',1),('beta',-1),('gamma',1)],'gamma_plus_bplus2')
gates={
 'candidate_1051_of_1051':candidate['pass'] and candidate['condition_count']==1051,
 'candidate_equations_exact':candidate['all_equations_exact'],
 'candidate_primal_dual_equal':candidate['primal_dual_equal'],
 'gamma_plus_bplus1_rejected':not ctrl1['pass'],
 'gamma_plus_bplus2_rejected':not ctrl2['pass'],
}
out={'audit':'A114B2_W1_M521_FRACTION_CROSSCHECK','method':'standalone Python fractions.Fraction; no SymPy and no import from the primary certificate','status':'PASS' if all(gates.values()) else 'FAIL','candidate':candidate,'negative_controls':[ctrl1,ctrl2],'gates':gates,'claim_limits':['Pointwise exact replication only; not an all-M theorem.']}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
