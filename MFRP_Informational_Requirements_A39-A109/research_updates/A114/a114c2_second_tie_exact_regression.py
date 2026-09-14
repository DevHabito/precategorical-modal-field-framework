#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114C2_SECOND_TIE_EXACT_REGRESSION_20260914.json'
B=F(1,8); G=F(1,16); T=F(1,2)

# Two exact rational brackets around E_(b+2)=0.  They cover odd/even
# parity and two substantially different dyadic offsets (d=11 and d=13).
CONTROLS=[
 (525,89,'lo',F(16180839119,125000000000),-1,'GP2'),
 (525,89,'hi',F(129446712953,1000000000000), 1,'ER3'),
 (760,129,'lo',F(259562519,2000000000),-1,'GP2'),
 (760,129,'hi',F(129781259501,1000000000000), 1,'ER3'),
]

def sg(x): return (x>0)-(x<0)
def eps(M): return F(1,(1875 if M%2==0 else 2500)*2**(M//2))
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def tr(A): return [list(x) for x in zip(*A)]
def powers(v,M):
 out=[F(1)]*(M+1)
 for i in range(1,M+1): out[i]=out[i-1]*v
 return out

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

def spec(M,j,label):
 h=M//2
 if label=='GP': return [0,j,j+1,M],[1,h,h+1],[('alpha',1),('beta',-1),('gamma',1)]
 if label=='ER': return [j-1,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
 raise KeyError(label)

def build(M,s,j,label):
 ps,qs,acts=spec(M,j,label); h=M//2; m=F(M,2); ep=eps(M)
 cache={'alpha':powers(s,M),'beta':powers(B,M),'gamma':powers(G,M),'tau':powers(T,M)}
 A=[
  [F(1)]*len(ps)+[F(0)]*len(qs)+[-1],
  [F(0)]*len(ps)+[F(1)]*len(qs)+[-1],
  [F(x) for x in ps]+[F(0)]*len(qs)+[-m],
  [F(0)]*len(ps)+[F(x) for x in qs]+[-m],
  [F(0)]*len(ps)+[cache['tau'][x] for x in qs]+[0],
 ]
 for n,sign in acts:
  A.append([F(sign)*cache[n][x] for x in ps]+[-F(sign)*cache[n][x] for x in qs]+[-2*ep])
 rhs=[0,0,0,0,1]+[0]*len(acts)
 obj=[cache['tau'][x] for x in ps]+[0]*len(qs)+[0]
 p=solve(A,rhs); y=solve(tr(A),obj)
 return dict(ps=ps,qs=qs,acts=acts,A=A,rhs=rhs,obj=obj,p=p,y=y,cache=cache)

def slack(M,z,n,sign):
 p=z['p']; ps=z['ps']; qs=z['qs']; c=z['cache'][n]
 d=sum((c[x]*p[i] for i,x in enumerate(ps)),F(0))-sum((c[x]*p[len(ps)+i] for i,x in enumerate(qs)),F(0))
 return 2*eps(M)*p[-1]-F(sign)*d

def kkt(M,z):
 ps=z['ps']; qs=z['qs']; acts=z['acts']; y=z['y']; c=z['cache']
 gates=[]
 gates.append(all(x>0 for x in z['p']))
 gates.append(all(y[5+i]>0 for i in range(len(acts))))
 active=set(acts)
 gates.append(all(slack(M,z,n,sign)>0 for n in ('alpha','beta','gamma') for sign in (1,-1) if (n,sign) not in active))
 pr=True
 for x in range(M+1):
  if x in ps: continue
  col=[1,0,F(x),0,0]+[F(sign)*c[n][x] for n,sign in acts]
  if dot(col,y)-c['tau'][x] <= 0: pr=False; break
 gates.append(pr)
 qr=True
 for x in range(M+1):
  if x in qs: continue
  col=[0,1,0,F(x),c['tau'][x]]+[-F(sign)*c[n][x] for n,sign in acts]
  if dot(col,y) <= 0: qr=False; break
 gates.append(qr)
 gates.append(all(dot(row,z['p'])==F(rhs) for row,rhs in zip(z['A'],z['rhs'])))
 gates.append(dot(z['obj'],z['p'])==dot(z['rhs'],z['y']))
 return all(gates)

# Exact A84 adjacent factor.
def dval(M,v,p):
 h=M//2; u=F(1,2**h); den=1-(h+1)*u
 if M%2==0:
  return (-2*u/den)*v+(1+2*h*u/den)*p[h]+(-2*(h-1)*u/den)*p[h+1]
 return (-F(3,2)*u/den)*v+(F(1,2)+F(3,2)*h*u/den)*p[h]+(F(1,2)-F(3,2)*(h-1)*u/den)*p[h+1]
def bv(M,k,p): return p[k]-F(M-k,M)-F(k,M)*p[M]
def dbv(M,k,p): return p[k+1]-p[k]+F(1-p[M],M)
def E(M,s,k):
 bp=powers(B,M); tp=powers(T,M); sp=powers(s,M); ep=eps(M)
 hb=F(1+bp[M],2)-dval(M,B,bp)+2*ep
 hs=F(1+sp[M],2)-dval(M,s,sp)-2*ep
 A=F(1+tp[M],2)
 x=A*bv(M,k,bp)-hb*bv(M,k,tp)
 y=-A*dbv(M,k,bp)+hb*dbv(M,k,tp)
 w=-bv(M,k,bp)*dbv(M,k,tp)+bv(M,k,tp)*dbv(M,k,bp)
 return x*dbv(M,k,sp)+y*bv(M,k,sp)+w*hs

rows=[]; gates=[]
for M,b,side,s,e_expected,selected in CONTROLS:
 j=b+2
 gp=build(M,s,j,'GP')
 e_sign=sg(E(M,s,j))
 # D_G>0 is promoted, so sign of p_(j+1) is sign of Phi.
 phi_sign=sg(gp['p'][gp['ps'].index(j+1)])
 z=gp if selected=='GP2' else build(M,s,j+1,'ER')
 passed=kkt(M,z)
 local=[e_sign==e_expected,phi_sign==1,passed]
 gates.extend(local)
 rows.append({'M':M,'b':b,'d':3*j-M//2,'side':side,'s':str(s),'E_bplus2_sign':e_sign,'Phi_sign':phi_sign,'selected':selected,'full_strict_KKT':passed})

out={
 'audit':'A114C2_SECOND_TIE_EXACT_REGRESSION',
 'status':'PASS' if all(gates) else 'FAIL',
 'gate_count':len(gates),'pass_count':sum(gates),'failed_indices':[i for i,v in enumerate(gates) if not v],
 'controls':rows,
 'interpretation':'Exact Fraction brackets straddle E_(b+2)=0. On the negative side GP2 passes complete KKT; on the positive side ER3 passes complete KKT. Phi is positive on all four bracket endpoints.',
 'claim_limit':'Regression/falsification evidence only; equality-surface closure is analytic/compositional.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count']},indent=2))
