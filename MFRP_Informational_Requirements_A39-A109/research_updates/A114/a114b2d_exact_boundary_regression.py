#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json, math

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2D_EXACT_BOUNDARY_REGRESSION_20260914.json'
B=F(1,8); G=F(1,16); T=F(1,2)

# Two independent cells (even/odd M) exhibiting all five strict architectures
# on rational controls bracketing the four discovered transition locations.
CONTROLS=[
 (538,F(1291,10000),'E'),
 (538,F(1294,10000),'QA'),
 (538,F(12961,100000),'QI'),
 (538,F(12965,100000),'C'),
 (538,F(12972,100000),'GP'),
 (555,F(1297,10000),'E'),
 (555,F(1299,10000),'QA'),
 (555,F(12999,100000),'QI'),
 (555,F(13004,100000),'C'),
 (555,F(13010,100000),'GP'),
]
EXPECTED={
 'E':(-1,-1,1,-1),
 'QA':(-1,-1,-1,-1),
 'QI':(-1,-1,-1,1),
 'C':(-1,1,-1,1),
 'GP':(1,1,-1,1),
}

def eps(M): return F(1,(1875 if M%2==0 else 2500)*2**(M//2))
def sgn(x): return (x>0)-(x<0)
def fs(x): return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def tr(A): return [list(x) for x in zip(*A)]

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

def f(name,s,x): return {'alpha':s,'beta':B,'gamma':G}[name]**x

def spec(M,j,label):
 h=M//2
 if label=='C': return [0,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
 if label=='E': return [j-1,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
 if label=='QI': return [j,M],[0,1,h,h+1],[('alpha',1),('beta',-1)]
 if label=='QA': return [j-1,j,M],[0,1,h,h+1],[('alpha',1),('beta',-1),('gamma',-1)]
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

def obj(M,s,j):
 z=build(M,s,j,'C')
 return dot(z['obj'],z['p'])

def full_kkt(M,s,j,label):
 z=build(M,s,j,label); ps=z['ps']; qs=z['qs']; acts=z['acts']
 basic=all(x>0 for x in z['p'])
 dual=all(z['y'][5+i]>0 for i in range(len(acts)))
 active=set(acts)
 slacks=all(slack(M,s,z,n,sg)>0 for n in ('alpha','beta','gamma') for sg in (1,-1) if (n,sg) not in active)
 prc=all(rcp(M,s,z,x)>0 for x in range(M+1) if x not in ps)
 qrc=all(rcq(M,s,z,x)>0 for x in range(M+1) if x not in qs)
 eq=all(dot(row,z['p'])==F(rhs) for row,rhs in zip(z['A'],z['rhs']))
 pd=dot(z['obj'],z['p'])==dot(z['rhs'],z['y'])
 return {'basic_positive':basic,'active_duals_positive':dual,'inactive_slacks_positive':slacks,'all_P_reduced_costs_positive':prc,'all_Q_reduced_costs_positive':qrc,'raw_equations_exact':eq,'primal_dual_equality_exact':pd,'pass':all((basic,dual,slacks,prc,qrc,eq,pd))}

rows=[]; gates=[]
for M,s,label in CONTROLS:
 b=bx(M,s); j=b+2
 vals=[obj(M,s,k) for k in (b+1,b+2,b+3)]
 strict=vals[1]>vals[0] and vals[1]>vals[2]
 Z={lab:build(M,s,j,lab) for lab in ('C','E','QI','QA','GP')}
 phi=Z['GP']['p'][Z['GP']['ps'].index(j+1)]
 p0=Z['C']['p'][0]
 re=rcq(M,s,Z['E'],0)
 gamma=slack(M,s,Z['QI'],'gamma',-1)
 signature=(sgn(phi),sgn(p0),sgn(re),sgn(gamma))
 kkt=full_kkt(M,s,j,label)
 rowg={'strict_bplus2':strict,'expected_signature':signature==EXPECTED[label],'selected_full_strict_KKT':kkt['pass']}
 gates.extend(rowg.values())
 rows.append({'M':M,'s':fs(s),'b':b,'j':j,'selected':label,'signature':{'Phi':signature[0],'p0C':signature[1],'rE_q0':signature[2],'Gamma':signature[3]},'gates':rowg,'kkt':kkt})

out={
 'audit':'A114B2D_EXACT_BOUNDARY_REGRESSION',
 'status':'PASS' if all(gates) else 'FAIL',
 'gate_count':len(gates),
 'pass_count':sum(gates),
 'controls':rows,
 'interpretation':'The controls give exact-rational finite witnesses for E -> QA -> QI -> C -> GP in one even and one odd tail cell. They are regression/falsification evidence only and are not premises of the all-tail boundary theorem.',
 'nonclaim':'This audit does not prove a universal monotone ordering of zero surfaces in s.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count']},indent=2))