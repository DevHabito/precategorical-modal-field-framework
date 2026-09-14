#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114C1_TIE_BRACKET_EXACT_REGRESSION_20260914.json'
B=F(1,8); G=F(1,16); T=F(1,2)

CONTROLS=[
 (521,90,'lo',F(1354427,10240000),-1,-1, 1,'GP1'),
 (521,90,'hi',F(8668333,65536000), 1,-1, 1,'C'),
 (522,90,'lo',F(43086649,327680000),-1,-1,-1,'GP1'),
 (522,90,'hi',F(861733,6553600), 1,-1,-1,'E'),
 (555,96,'lo',F(8708321,65536000),-1, 1, 1,'GP2'),
 (555,96,'hi',F(21770803,163840000), 1, 1, 1,'GP2'),
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
 if label=='C': return [0,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
 if label=='E': return [j-1,j,M],[1,h,h+1],[('alpha',1),('beta',-1)]
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

# A84 exact adjacent factor.
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
for M,b,side,s,e_expected,phi_expected,p0_expected,selected in CONTROLS:
 # Phi sign is the sign of the right adjacent mass in GP2 because D_G>0.
 gp2=build(M,s,b+2,'GP')
 phi_sign=sg(gp2['p'][gp2['ps'].index(b+3)])
 c=build(M,s,b+2,'C'); p0_sign=sg(c['p'][0])
 e_sign=sg(E(M,s,b+1))
 if selected=='GP1': z=build(M,s,b+1,'GP')
 elif selected=='GP2': z=gp2
 elif selected=='C': z=c
 else: z=build(M,s,b+2,'E')
 passed=kkt(M,z)
 local=[e_sign==e_expected,phi_sign==phi_expected,p0_sign==p0_expected,passed]
 gates.extend(local)
 rows.append({'M':M,'b':b,'side':side,'s':str(s),'E_bplus1_sign':e_sign,'Phi_sign':phi_sign,'p0C_sign':p0_sign,'selected':selected,'full_strict_KKT':passed})

out={
 'audit':'A114C1_TIE_BRACKET_EXACT_REGRESSION',
 'status':'PASS' if all(gates) else 'FAIL',
 'gate_count':len(gates),'pass_count':sum(gates),'controls':rows,
 'interpretation':'Three exact rational brackets straddle E_(b+1)=0 in the GP1->C, GP1->E, and GP2->GP2 regimes. Complete unused-atom P/Q reduced-cost scans are exact Fraction arithmetic.',
 'claim_limit':'Regression/falsification evidence only; the equality-surface theorem is analytic/compositional.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count']},indent=2))
