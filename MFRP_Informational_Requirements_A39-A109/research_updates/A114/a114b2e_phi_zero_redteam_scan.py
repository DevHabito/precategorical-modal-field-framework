#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json, math

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2E_PHI_ZERO_REDTEAM_SCAN_20260914.json'
B=F(1,8); G=F(1,16); T=F(1,2)
BRACKETS=[
 (521,89,F(647,5000),F(259,2000)),
 (521,90,F(1323,10000),F(331,2500)),
 (522,90,F(1317,10000),F(659,5000)),
 (523,90,F(1313,10000),F(657,5000)),
 (538,92,F(81,625),F(1297,10000)),
 (538,93,F(53,400),F(663,5000)),
 (555,95,F(13,100),F(1301,10000)),
 (600,103,F(1309,10000),F(131,1000)),
 (700,120,F(327,2500),F(1309,10000)),
 (800,137,F(1307,10000),F(327,2500)),
 (900,154,F(653,5000),F(1307,10000)),
 (1000,170,F(129,1000),F(1291,10000)),
 (1000,171,F(653,5000),F(1307,10000)),
]

def eps(M): return F(1,(1875 if M%2==0 else 2500)*2**(M//2))
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def tr(A): return [list(x) for x in zip(*A)]
def sgn(x): return (x>0)-(x<0)
def f(name,s,x): return {'alpha':s,'beta':B,'gamma':G}[name]**x

def solve(A,b):
 n=len(b); a=[[F(x) for x in A[i]]+[F(b[i])] for i in range(n)]
 for c in range(n):
  p=next(i for i in range(c,n) if a[i][c]); a[c],a[p]=a[p],a[c]
  q=a[c][c]; a[c]=[x/q for x in a[c]]
  for i in range(n):
   if i==c: continue
   q=a[i][c]
   if q: a[i]=[a[i][k]-q*a[c][k] for k in range(n+1)]
 return [a[i][-1] for i in range(n)]

def bx(M,s):
 e=math.ceil(M*math.log(2)/(-2*math.log(float(s))))
 def gt(k): return 2**M*s.numerator**(2*k)>s.denominator**(2*k)
 while gt(e): e+=1
 while e and not gt(e-1): e-=1
 return e

def build(M,s,j,label):
 h=M//2; m=F(M,2); ep=eps(M)
 if label=='C': ps,qs,acts=[0,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
 elif label=='GP': ps,qs,acts=[0,j,j+1,M],[1,h,h+1],[('alpha',1),('beta',-1),('gamma',1)]
 else: raise KeyError(label)
 A=[[F(1)]*len(ps)+[F(0)]*len(qs)+[-1],
    [F(0)]*len(ps)+[F(1)]*len(qs)+[-1],
    [F(x) for x in ps]+[F(0)]*len(qs)+[-m],
    [F(0)]*len(ps)+[F(x) for x in qs]+[-m],
    [F(0)]*len(ps)+[T**x for x in qs]+[0]]
 for n,sg in acts:
  A.append([F(sg)*f(n,s,x) for x in ps]+[-F(sg)*f(n,s,x) for x in qs]+[-2*ep])
 rhs=[0,0,0,0,1]+[0]*len(acts); obj=[T**x for x in ps]+[0]*len(qs)+[0]
 return {'ps':ps,'qs':qs,'acts':acts,'A':A,'rhs':rhs,'obj':obj,'p':solve(A,rhs)}

def slack(M,s,z,name,sg):
 p=z['p']; ps=z['ps']; qs=z['qs']
 d=sum((f(name,s,x)*p[i] for i,x in enumerate(ps)),F(0))-sum((f(name,s,x)*p[len(ps)+i] for i,x in enumerate(qs)),F(0))
 return 2*eps(M)*p[-1]-F(sg)*d

def phi(M,s,b):
 j=b+2; z=build(M,s,j,'GP'); return z['p'][z['ps'].index(j+1)]
def p0c(M,s,b): return build(M,s,b+2,'C')['p'][0]
def sgpc(M,s,b): return slack(M,s,build(M,s,b+2,'C'),'gamma',1)

def cobj(M,s,k):
 z=build(M,s,k,'C'); return dot(z['obj'],z['p'])
def strict_b2(M,s,b):
 if bx(M,s)!=b: return False
 v=[cobj(M,s,k) for k in (b+1,b+2,b+3)]
 return v[1]>v[0] and v[1]>v[2]

def bisect(M,b,lo,hi,steps=18):
 assert bx(M,lo)==b==bx(M,hi)
 assert strict_b2(M,lo,b) and strict_b2(M,hi,b)
 assert phi(M,lo,b)<0<phi(M,hi,b)
 for _ in range(steps):
  mid=(lo+hi)/2
  assert bx(M,mid)==b and strict_b2(M,mid,b)
  if phi(M,mid,b)<0: lo=mid
  else: hi=mid
 return lo,hi

rows=[]; gates=[]; p0_values=[]; widths=[]
for M,b,lo0,hi0 in BRACKETS:
 lo,hi=bisect(M,b,lo0,hi0)
 vals={
  'same_b':bx(M,lo)==b==bx(M,hi),
  'strict_bplus2_both':strict_b2(M,lo,b) and strict_b2(M,hi,b),
  'Phi_bracketed':phi(M,lo,b)<0<phi(M,hi,b),
  'p0_positive_both':p0c(M,lo,b)>0 and p0c(M,hi,b)>0,
  'Sgamma_plus_opposite_both':sgpc(M,lo,b)>0 and sgpc(M,hi,b)<0,
  'bracket_width_le_4e10':hi-lo<=F(1,2500000000),
 }
 gates.extend(vals.values()); p0_values += [p0c(M,lo,b),p0c(M,hi,b)]; widths.append(hi-lo)
 rows.append({'M':M,'b':b,'left':f'{lo.numerator}/{lo.denominator}','right':f'{hi.numerator}/{hi.denominator}','gates':vals})

min_p0=min(p0_values); max_width=max(widths)
out={
 'audit':'A114B2E_PHI_ZERO_MULTI_CELL_REDTEAM_SCAN',
 'status':'PASS' if all(gates) and min_p0>F(3,1000) else 'FAIL',
 'cell_count':len(rows),
 'gate_count':len(gates)+1,
 'pass_count':sum(gates)+(1 if min_p0>F(3,1000) else 0),
 'failed_count':len(gates)+1-(sum(gates)+(1 if min_p0>F(3,1000) else 0)),
 'minimum_p0C_decimal':f'{float(min_p0):.18e}',
 'maximum_bracket_width_decimal':f'{float(max_width):.18e}',
 'rows':rows,
 'interpretation':'Thirteen independent strict-b+2 cells from M=521 through M=1000 were adversarially bracketed around a Phi sign change using exact rational bisection. No Phi/p0 collision or pivot-sign reversal was found.',
 'nonclaim':'Finite scanning does not prove the all-tail theorem; the analytic B0/B1 certificate is the proof layer.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'cell_count':out['cell_count'],'gate_count':out['gate_count'],'pass_count':out['pass_count'],'minimum_p0C_decimal':out['minimum_p0C_decimal'],'maximum_bracket_width_decimal':out['maximum_bracket_width_decimal']},indent=2))
