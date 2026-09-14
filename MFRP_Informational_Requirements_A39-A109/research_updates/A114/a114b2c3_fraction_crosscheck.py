#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json, math
HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2C3_FRACTION_CROSSCHECK_20260914.json'
B=F(1,8); G=F(1,16); T=F(1,2)
CONTROLS=[(555,F(13,100),'QI'),(908,F(13,100),'QI'),(967,F(13,100),'QI'),(521,F(129,1000),'QA'),(970,F(129,1000),'QA'),(1000,F(129,1000),'QA')]

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
def tr(A): return [list(x) for x in zip(*A)]
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def sgn(x): return (x>0)-(x<0)
def fs(x): return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def eps(M): return F(1,(1875 if M%2==0 else 2500)*2**(M//2))
def f(name,s,x): return {'alpha':s,'beta':B,'gamma':G}[name]**x

def bx(M,s):
 e=math.ceil(M*math.log(2)/(-2*math.log(float(s))))
 def gt(k): return 2**M*s.numerator**(2*k)>s.denominator**(2*k)
 while gt(e): e+=1
 while e and not gt(e-1): e-=1
 return e

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
 for n,sg in acts: A.append([F(sg)*f(n,s,x) for x in ps]+[-F(sg)*f(n,s,x) for x in qs]+[-2*ep])
 rhs=[0,0,0,0,1]+[0]*len(acts); obj=[T**x for x in ps]+[0]*len(qs)+[0]
 primal=solve(A,rhs); dual=solve(tr(A),obj)
 return {'ps':ps,'qs':qs,'acts':acts,'A':A,'rhs':rhs,'obj':obj,'p':primal,'y':dual}
def slack(M,s,z,name,sg):
 p=z['p']; ps=z['ps']; qs=z['qs']; d=sum(f(name,s,x)*p[i] for i,x in enumerate(ps))-sum(f(name,s,x)*p[len(ps)+i] for i,x in enumerate(qs))
 return 2*eps(M)*p[-1]-F(sg)*d
def rcp(M,s,z,x):
 col=[1,0,F(x),0,0]+[F(sg)*f(n,s,x) for n,sg in z['acts']]
 return dot(col,z['y'])-T**x
def rcq(M,s,z,x):
 col=[0,1,0,F(x),T**x]+[-F(sg)*f(n,s,x) for n,sg in z['acts']]
 return dot(col,z['y'])
def obj(M,s,j):
 z=build(M,s,j,'C'); return dot(z['obj'],z['p'])

rows=[]; gates=[]; false_conv=[]
for M,s,exp in CONTROLS:
 b=bx(M,s); j=b+2; vals=[obj(M,s,k) for k in (b+1,b+2,b+3)]; strict=vals[1]>vals[0] and vals[1]>vals[2]
 Z={lab:build(M,s,j,lab) for lab in ('C','E','QI','QA','GP')}
 phi=Z['GP']['p'][Z['GP']['ps'].index(j+1)]
 p0=Z['C']['p'][0]; re=rcq(M,s,Z['E'],0); gamma=slack(M,s,Z['QI'],'gamma',-1)
 q0qi=Z['QI']['p'][len(Z['QI']['ps'])+Z['QI']['qs'].index(0)]
 pjmqa=Z['QA']['p'][Z['QA']['ps'].index(j-1)]; ygm=Z['QA']['y'][7]
 exact={}
 for lab in ('QI','QA'):
  z=Z[lab]; exact[lab]=all(dot(row,z['p'])==F(rhs) for row,rhs in zip(z['A'],z['rhs'])) and dot(z['obj'],z['p'])==dot(z['rhs'],z['y'])
 sel=Z[exp]
 basic_positive=all(x>0 for x in sel['p'])
 dual_positive=all(sel['y'][5+i]>0 for i in range(len(sel['acts'])))
 opp_slacks=all(slack(M,s,sel,n,-sg)>0 for n,sg in sel['acts'])
 if exp=='QI': extra_slack=slack(M,s,sel,'gamma',1)>0 and gamma>0
 else: extra_slack=True
 sentinels={
  'p0': rcp(M,s,sel,0) if 0 not in sel['ps'] else F(1),
  'pjm2': rcp(M,s,sel,j-2),
  'pjm1': rcp(M,s,sel,j-1) if j-1 not in sel['ps'] else F(1),
  'pjp1': rcp(M,s,sel,j+1),
  'pM1': rcp(M,s,sel,M-1),
  'q2': rcq(M,s,sel,2) if 2 not in sel['qs'] else F(1),
 }
 sentinel_positive=all(v>0 for v in sentinels.values())
 q1qi=Z['QI']['p'][len(Z['QI']['ps'])+1]
 qhqi=Z['QI']['p'][len(Z['QI']['ps'])+Z['QI']['qs'].index(M//2)]
 if exp=='QA' and (q1qi<=0 or qhqi<=0): false_conv.append({'M':M,'s':fs(s),'q1QI':sgn(q1qi),'qhQI':sgn(qhqi)})
 gg={
  'strict_bplus2':strict,'phi_negative':phi<0,'p0C_negative':p0<0,'rE_q0_negative':re<0,
  'Gamma_selects':gamma>0 if exp=='QI' else gamma<0,'q0QI_positive':q0qi>0,
  'QA_pivot_mass_sign':pjmqa<0 if exp=='QI' else pjmqa>0,'QA_gamma_dual_positive':ygm>0,
  'raw_QI_QA_exact':exact['QI'] and exact['QA'],'selected_basic_positive':basic_positive,
  'selected_active_duals_positive':dual_positive,'selected_opposite_slacks_positive':opp_slacks and extra_slack,
  'selected_sentinels_positive':sentinel_positive,
 }
 gates += list(gg.values())
 rows.append({'M':M,'s':fs(s),'j':j,'expected':exp,'signs':{'p0C':sgn(p0),'rE_q0':sgn(re),'Gamma':sgn(gamma),'q0QI':sgn(q0qi),'p_jm1_QA':sgn(pjmqa),'lambda_gamma_QA':sgn(ygm),'q1QI':sgn(q1qi),'qhQI':sgn(qhqi)},'gates':gg,'sentinel_signs':{k:sgn(v) for k,v in sentinels.items()}})
out={'audit':'A114B2C3_INDEPENDENT_FRACTION_CROSSCHECK','status':'PASS' if all(gates) and false_conv else 'FAIL','gate_count':len(gates)+1,'pass_count':sum(gates)+(1 if false_conv else 0),'false_convexity_route_rejected':bool(false_conv),'false_convexity_witnesses':false_conv,'controls':rows,'archival_full_kkt_dependency':'A114B2C_12_POINT_FULL_KKT_SUMMARY_20260913.json independently records complete 2M+9 exact KKT passes for these same six QI/QA controls.','claim_limits':['This crosscheck independently reconstructs raw QI/QA matrices, pivot signs, primal/dual/slack gates and P/Q sentinels.','The complete atom-by-atom control scans are supplied independently by the pre-existing 12-point full-KKT certificate; neither finite control set is an all-tail premise.']}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count'],'false_convexity_witnesses':false_conv},indent=2))
