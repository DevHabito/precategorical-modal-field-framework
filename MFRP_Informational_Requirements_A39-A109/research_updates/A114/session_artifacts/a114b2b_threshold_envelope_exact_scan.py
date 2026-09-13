from fractions import Fraction as F
from pathlib import Path
import json,math

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2B_THRESHOLD_ENVELOPE_EXACT_SCAN_20260913.json'
B=F(1,8); G=F(1,16)

def solve(A,b):
 n=len(A); aug=[A[i][:]+[b[i]] for i in range(n)]
 for c in range(n):
  p=next(r for r in range(c,n) if aug[r][c])
  aug[c],aug[p]=aug[p],aug[c]; v=aug[c][c]
  aug[c]=[x/v for x in aug[c]]
  for r in range(n):
   if r==c: continue
   q=aug[r][c]
   if q: aug[r]=[aug[r][k]-q*aug[c][k] for k in range(n+1)]
 return [aug[i][-1] for i in range(n)]

def q_CD(M,r):
 h=M//2; u=F(1,2**h); d=1-(h+1)*u
 C=(2*r-2*h*r**h+2*(h-1)*r**(h+1))/d
 if M%2==0:
  D=(-2*u/d)*r+(1+2*h*u/d)*r**h+(-2*(h-1)*u/d)*r**(h+1)
 else:
  D=(-F(3,2)*u/d)*r+(F(1,2)+F(3,2)*h*u/d)*r**h+(F(1,2)-F(3,2)*(h-1)*u/d)*r**(h+1)
 return C,D

def coeffs(M,j):
 h=M//2; eps=F(1,(1875 if M%2==0 else 2500)*2**h); mean=F(M,2)
 ps=[0,j-1,j,M]
 A=[[F(1)]*4,[F(x) for x in ps],[B**x for x in ps],[G**x for x in ps]]
 Cb,Db=q_CD(M,B); Cg,Dg=q_CD(M,G)
 c=solve(A,[F(0),F(0),Cb,Cg])
 a=solve(A,[F(1),mean,Db-2*eps,Dg-2*eps])
 return a,c

def main():
 bad=[]; n=0; margins=[]
 # Deliberately broaden the possible j envelope slightly beyond A89 slope brackets.
 for M in range(521,1001):
  h=M//2
  jlo=max(2, math.floor(F(169,1000)*M)+1)
  jhi=min(h-1, math.ceil(F(173,1000)*M)+3)
  for j in range(jlo,jhi+1):
   if 3*j-h<13: continue
   a,c=coeffs(M,j); n+=1
   a0,aj=a[0],a[2]; c0,cj=c[0],c[2]
   K=c0*aj-cj*a0
   ok=(a0<0 and c0>0 and aj>0 and cj<0 and K<0)
   if not ok: bad.append({'M':M,'j':j,'3j-h':3*j-h,'signs':[int(a0>0)-int(a0<0),int(c0>0)-int(c0<0),int(aj>0)-int(aj<0),int(cj>0)-int(cj<0),int(K>0)-int(K<0)]})
   # normalized threshold gap t_j-t_0 = -cj/aj + c0/a0 (positive iff K<0 under signs)
   gap=(-cj/aj)-(-c0/a0)
   margins.append((gap,M,j,K,a0,c0,aj,cj))
 margins.sort(key=lambda z:z[0])
 out={'audit':'A114B2_GAMMA_MINUS_THRESHOLD_EXACT_ENVELOPE_SCAN','M_range':[521,1000],
      'j_envelope':'floor(0.169 M)+1 through ceil(0.173 M)+3, restricted by 3j-h>=13',
      'cases':n,'failures':bad,
      'all_a0_neg_c0_pos_aj_pos_cj_neg_K_neg':len(bad)==0,
      'smallest_threshold_gaps':[{'M':z[1],'j':z[2],'3j-h':3*z[2]-(z[1]//2),'gap_float':float(z[0])} for z in margins[:12]]}
 OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps(out,indent=2))
if __name__=='__main__': main()
