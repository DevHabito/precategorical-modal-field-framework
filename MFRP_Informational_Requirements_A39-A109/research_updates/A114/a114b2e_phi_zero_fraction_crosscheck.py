#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json, math

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2E_PHI_ZERO_FRACTION_CROSSCHECK_20260914.json'
B=F(1,8); G=F(1,16); T=F(1,2)
CONTROLS=[
 (538,F(129698549,10**9),'C',-1),
 (538,F(129698550,10**9),'GP',+1),
 (555,F(130085841,10**9),'C',-1),
 (555,F(130085842,10**9),'GP',+1),
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

def spec(M,j,label):
 h=M//2
 if label=='C': return [0,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
 if label=='GP': return [0,j,j+1,M],[1,h,h+1],[('alpha',1),('beta',-1),('gamma',1)]
 raise KeyError(label)

def build(M,s,j,label):
 ps,qs,acts=spec(M,j,label); m=F(M,2); ep=eps(M)
 A=[[F(1)]*len(ps)+[F(0)]*len(qs)+[-1],
    [F(0)]*len(ps)+[F(1)]*len(qs)+[-1],
    [F(x) for x in ps]+[F(0)]*len(qs)+[-m],
    [F(0)]*len(ps)+[F(x) for x in qs]+[-m],
    [F(0)]*len(ps)+[T**x for x in qs]+[0]]
 for n,sg in acts:
  A.append([F(sg)*f(n,s,x) for x in ps]+[-F(sg)*f(n,s,x) for x in qs]+[-2*ep])
 rhs=[0,0,0,0,1]+[0]*len(acts)
 obj=[T**x for x in ps]+[0]*len(qs)+[0]
 p=solve(A,rhs); y=solve(tr(A),obj)
 return {'ps':ps,'qs':qs,'acts':acts,'A':A,'rhs':rhs,'obj':obj,'p':p,'y':y}

def slack(M,s,z,name,sg):
 p=z['p']; ps=z['ps']; qs=z['qs']
 d=sum((f(name,s,x)*p[i] for i,x in enumerate(ps)),F(0))-sum((f(name,s,x)*p[len(ps)+i] for i,x in enumerate(qs)),F(0))
 return 2*eps(M)*p[-1]-F(sg)*d

def rcp(M,s,z,x):
 col=[1,0,F(x),0,0]+[F(sg)*f(n,s,x) for n,sg in z['acts']]
 return dot(col,z['y'])-T**x

def rcq(M,s,z,x):
 col=[0,1,0,F(x),T**x]+[-F(sg)*f(n,s,x) for n,sg in z['acts']]
 return dot(col,z['y'])

def obj(M,s,k):
 z=build(M,s,k,'C'); return dot(z['obj'],z['p'])

def strict_bplus2(M,s):
 b=bx(M,s); v=[obj(M,s,k) for k in (b+1,b+2,b+3)]
 return v[1]>v[0] and v[1]>v[2]

def full_strict_kkt(M,s,j,label):
 z=build(M,s,j,label); ps=z['ps']; qs=z['qs']; acts=z['acts']; active=set(acts)
 basic=all(x>0 for x in z['p'])
 dual=all(z['y'][5+i]>0 for i in range(len(acts)))
 slacks=all(slack(M,s,z,n,sg)>0 for n in ('alpha','beta','gamma') for sg in (1,-1) if (n,sg) not in active)
 prc=all(rcp(M,s,z,x)>0 for x in range(M+1) if x not in ps)
 qrc=all(rcq(M,s,z,x)>0 for x in range(M+1) if x not in qs)
 eq=all(dot(row,z['p'])==F(rhs) for row,rhs in zip(z['A'],z['rhs']))
 pd=dot(z['obj'],z['p'])==dot(z['rhs'],z['y'])
 return all((basic,dual,slacks,prc,qrc,eq,pd)), {'basic':basic,'dual':dual,'slacks':slacks,'P_rc':prc,'Q_rc':qrc,'equations':eq,'primal_dual':pd}

rows=[]; gates=[]
for M,s,label,want_phi in CONTROLS:
 b=bx(M,s); j=b+2
 C=build(M,s,j,'C'); GP=build(M,s,j,'GP')
 phi=GP['p'][GP['ps'].index(j+1)]
 p0=C['p'][C['ps'].index(0)]
 sgp=slack(M,s,C,'gamma',1)
 kpass,kparts=full_strict_kkt(M,s,j,label)
 gg={
   'strict_bplus2':strict_bplus2(M,s),
   'phi_expected_sign':sgn(phi)==want_phi,
   'p0C_positive':p0>0,
   'C_gamma_plus_opposite_phi_sign':sgn(sgp)==-want_phi,
   'selected_full_strict_KKT':kpass,
   'raw_pivot_nonzero':phi!=0 and sgp!=0,
 }
 gates.extend(gg.values())
 rows.append({'M':M,'s':f'{s.numerator}/{s.denominator}','b':b,'j':j,'selected':label,'phi_sign':sgn(phi),'Sgamma_plus_C_sign':sgn(sgp),'p0C_sign':sgn(p0),'gates':gg,'kkt_parts':kparts})

out={
 'audit':'A114B2E_PHI_ZERO_INDEPENDENT_FRACTION_CROSSCHECK',
 'status':'PASS' if all(gates) else 'FAIL',
 'gate_count':len(gates),
 'pass_count':sum(gates),
 'failed_count':len(gates)-sum(gates),
 'controls':rows,
 'exact_brackets':[
   {'M':538,'left':'129698549/1000000000','right':'129698550/1000000000'},
   {'M':555,'left':'130085841/1000000000','right':'130085842/1000000000'}
 ],
 'interpretation':'Exact rational brackets place a Phi sign change between each pair. C is strict KKT on the Phi<0 side and GP is strict KKT on the Phi>0 side; p0^C stays positive and S_(gamma+)^C has the exact opposite sign of Phi. These are falsification/regression controls only, not the all-tail proof.',
 'nonclaim':'No rational endpoint is asserted to be the exact Phi=0 root.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count']},indent=2))
