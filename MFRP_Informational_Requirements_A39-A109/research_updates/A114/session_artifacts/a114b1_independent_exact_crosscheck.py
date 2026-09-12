#!/usr/bin/env python3
from __future__ import annotations
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

OUT=Path('/mnt/data/a114b1_audit/A114B1_INDEPENDENT_EXACT_CROSSCHECK_20260912.json')

def Q(x): return sp.Rational(1,2**x)
def BETA(x): return sp.Rational(1,2**(3*x))
def GAMMA(x): return sp.Rational(1,2**(4*x))
def eps(M): return sp.Rational(1, (1875 if M%2==0 else 2500)*2**(M//2))
def sg(x): return 1 if x>0 else -1 if x<0 else 0

def rat(s):
    if isinstance(s,sp.Rational): return s
    return sp.Rational(s.numerator,s.denominator)

def certify_b(M,s,b):
    s=rat(s); n=int(s.p); d=int(s.q)
    left=(2**M)*(n**(2*(b-1))) > d**(2*(b-1))
    right=(2**M)*(n**(2*b)) <= d**(2*b)
    return left and right

def compressed_obj(M,s,k):
    s=rat(s); h=M//2; e=eps(M); mean=sp.Rational(M,2)
    ps=[0,k,M]; qs=[1,h,h+1]
    rows=[
      [1,1,1,0,0,0,-1],
      [0,0,0,1,1,1,-1],
      [*ps,0,0,0,-mean],
      [0,0,0,*qs,-mean],
      [0,0,0,*[Q(x) for x in qs],0],
      [*[s**x for x in ps],*[-s**x for x in qs],-2*e],
      [*[-BETA(x) for x in ps],*[BETA(x) for x in qs],-2*e],
    ]
    A=sp.Matrix(rows); rhs=sp.Matrix([0,0,0,0,1,0,0]); x=A.inv(method='DM')*rhs
    return sp.cancel(sum(Q(xx)*x[i] for i,xx in enumerate(ps)))

def reduced_gamma(M,s,j):
    s=rat(s); h=M//2; e=eps(M); mean=sp.Rational(M,2)
    qs=[1,h,h+1]
    AQ=sp.Matrix([[1,1,1],qs,[Q(x) for x in qs]])
    slope=AQ.inv(method='DM')*sp.Matrix([1,mean,0])
    const=AQ.inv(method='DM')*sp.Matrix([0,0,1])
    def qc(base): return sp.cancel(sum(const[i]*base**qs[i] for i in range(3)))
    def qd(base): return sp.cancel(sum(slope[i]*base**qs[i] for i in range(3)))
    def br(base,k): return sp.cancel(base**k-sp.Rational(M-k,M)-sp.Rational(k,M)*base**M)
    def ar(base): return sp.cancel((1+base**M)/2)
    b=sp.Rational(1,8); g=sp.Rational(1,16)
    Hb=sp.cancel(ar(b)-qd(b)+2*e); Hg=sp.cancel(ar(g)-qd(g)-2*e); Hs=sp.cancel(ar(s)-qd(s)-2*e)
    G=sp.Matrix([[br(b,j),br(b,j+1),Hb],[br(g,j),br(g,j+1),Hg],[br(s,j),br(s,j+1),Hs]])
    rhs=sp.Matrix([qc(b),qc(g),qc(s)])
    DG=sp.factor(G.det(method='domain-ge'))
    G0=G.copy(); G0[:,0]=rhs
    G1=G.copy(); G1[:,1]=rhs
    Npj=sp.factor(G0.det(method='domain-ge')); Np1=sp.factor(G1.det(method='domain-ge'))
    return {'DG':DG,'F_j':Np1,'F_jp1':-Npj,'pj':sp.cancel(Npj/DG),'pj1':sp.cancel(Np1/DG)}

def gamma_plus_check(M,s,j):
    s=rat(s); h=M//2; e=eps(M); mean=sp.Rational(M,2)
    ps=[0,j,j+1,M]; qs=[1,h,h+1]
    rows=[
      [1,1,1,1,0,0,0,-1],
      [0,0,0,0,1,1,1,-1],
      [*ps,0,0,0,-mean],
      [0,0,0,0,*qs,-mean],
      [0,0,0,0,*[Q(x) for x in qs],0],
      [*[s**x for x in ps],*[-s**x for x in qs],-2*e],
      [*[-BETA(x) for x in ps],*[BETA(x) for x in qs],-2*e],
      [*[GAMMA(x) for x in ps],*[-GAMMA(x) for x in qs],-2*e],
    ]
    A=sp.Matrix(rows); rhs=sp.Matrix([0,0,0,0,1,0,0,0]); obj=sp.Matrix([*[Q(x) for x in ps],0,0,0,0])
    basic=A.inv(method='DM')*rhs; dual=A.T.inv(method='DM')*obj
    cond=[]
    names=[*[f'basic_p_{x}' for x in ps],*[f'basic_q_{x}' for x in qs],'basic_t']
    cond += list(zip(names,basic))
    cond += [('active_dual_alpha_+1',dual[5]),('active_dual_beta_-1',dual[6]),('active_dual_gamma_+1',dual[7])]
    pset=set(ps);qset=set(qs)
    for x in range(M+1):
        if x not in pset:
            col=sp.Matrix([1,0,x,0,0,s**x,-BETA(x),GAMMA(x)])
            cond.append((f'reduced_cost_p_{x}',sp.factor(col.dot(dual)-Q(x))))
        if x not in qset:
            col=sp.Matrix([0,1,0,x,Q(x),-s**x,BETA(x),-GAMMA(x)])
            cond.append((f'reduced_cost_q_{x}',sp.factor(col.dot(dual))))
    t=basic[-1]
    def diff(fn): return sp.factor(sum(fn(x)*basic[i] for i,x in enumerate(ps))-sum(fn(x)*basic[len(ps)+i] for i,x in enumerate(qs)))
    ad=diff(lambda x:s**x); bd=diff(BETA); gd=diff(GAMMA)
    cond += [('inactive_slack_alpha_-1',sp.factor(2*e*t+ad)),('inactive_slack_beta_+1',sp.factor(2*e*t-bd)),('inactive_slack_gamma_-1',sp.factor(2*e*t+gd))]
    fails=[name for name,v in cond if v<=0]
    minrec=min(cond,key=lambda z:z[1])
    return {'pass':not fails,'condition_count':len(cond),'expected_count':2*M+9,'failures':fails,'min_condition':minrec[0],'min_decimal':str(sp.N(minrec[1],12)),'adjacent_signs':[sg(basic[1]),sg(basic[2])]}

cases=[
  ('even_left',522,F(131,1000),90),
  ('odd_left',561,F(53,400),97),
  ('odd_right',561,F(13277,100000),97),
]
out={'audit':'A114B1_INDEPENDENT_EXACT_CROSSCHECK','method':'standalone exact-rational compressed checks and full 8x8 gamma-plus KKT scans; no import from the A114-B1 orientation theorem certificate','cases':[]}
for label,M,sf,b in cases:
    s=rat(sf)
    vals={str(b+d):compressed_obj(M,s,b+d) for d in (1,2,3)}
    maxj=max(vals,key=lambda k:vals[k])
    rg1=reduced_gamma(M,s,b+1)
    pivot=rg1['F_jp1'] # F_(b+2)
    pred=b+1 if pivot<0 else b+2 if pivot>0 else None
    alt=b+2 if pred==b+1 else b+1 if pred==b+2 else None
    pc=gamma_plus_check(M,s,pred) if pred else None
    ac=gamma_plus_check(M,s,alt) if alt else None
    rec={
      'label':label,'M':M,'s':str(s),'b':b,'b_certified':certify_b(M,s,b),
      'compressed_values_decimal':{k:str(sp.N(v,18)) for k,v in vals.items()},
      'compressed_strict_winner':int(maxj),'expected_winner':b+1,
      'DG_sign':sg(rg1['DG']),'F_bplus1_sign':sg(rg1['F_j']),'F_bplus2_sign':sg(pivot),
      'predicted_gamma_contact':pred,'alternate_contact':alt,
      'predicted_check':pc,'alternate_check':ac,
    }
    out['cases'].append(rec)
out['gates']={
 'all_b_exact':all(c['b_certified'] for c in out['cases']),
 'all_strict_compressed_bplus1':all(c['compressed_strict_winner']==c['expected_winner'] for c in out['cases']),
 'all_DG_positive':all(c['DG_sign']==1 for c in out['cases']),
 'all_predicted_full_KKT':all(c['predicted_check']['pass'] and c['predicted_check']['condition_count']==c['predicted_check']['expected_count'] for c in out['cases']),
 'all_alternatives_rejected':all(not c['alternate_check']['pass'] for c in out['cases']),
 'both_pivot_signs_tested':set(c['F_bplus2_sign'] for c in out['cases'])=={-1,1},
}
out['claim_limits']=['The three cases are adversarial replication controls, not the analytic proof.', 'The analytic all-M statement depends on the proved A112/A113 structural theorems and the separate A114-B1 orientation certificate.']
out['verdict']='PASS' if all(out['gates'].values()) else 'FAIL'
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'verdict':out['verdict'],'gates':out['gates'],'cases':[{k:c[k] for k in ('label','M','s','b','F_bplus2_sign','predicted_gamma_contact','predicted_check','alternate_check')} for c in out['cases']]},indent=2))
