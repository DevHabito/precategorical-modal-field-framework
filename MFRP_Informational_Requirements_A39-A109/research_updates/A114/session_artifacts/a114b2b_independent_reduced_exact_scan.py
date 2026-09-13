from fractions import Fraction as F
from decimal import Decimal, getcontext
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2B_INDEPENDENT_REDUCED_EXACT_SCAN_20260913.json'
BETA=F(1,8); GAMMA=F(1,16)

def sgn(x): return 1 if x>0 else -1 if x<0 else 0

def exact_b(M,s):
    getcontext().prec=80
    sd=Decimal(s.numerator)/Decimal(s.denominator)
    k=int((Decimal(M)*Decimal(2).ln()/(-2*sd.ln())).to_integral_value(rounding='ROUND_CEILING'))
    def lt_mc(q): return (2**M)*(s.numerator**(2*q)) > s.denominator**(2*q)
    while lt_mc(k): k+=1
    while k>0 and not lt_mc(k-1): k-=1
    return k

def det3(A):
 return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])

def solve3(A,b):
 D=det3(A)
 if not D: raise ZeroDivisionError
 out=[]
 for c in range(3):
  C=[row[:] for row in A]
  for r in range(3): C[r][c]=b[r]
  out.append(det3(C)/D)
 return out

def blocks(M,k):
 h=M//2; u=F(1,2**h); eps=F(1,(1875 if M%2==0 else 2500)*2**h); d=1-(h+1)*u
 def B(r): return r**k-F(M-k,M)-F(k,M)*r**M
 def C(r): return (2*r-2*h*r**h+2*(h-1)*r**(h+1))/d
 if M%2==0:
  def D(r): return (-2*u*r+(1+2*h*u/d)*0) # overwritten below
  Dc={1:-2*u/d,h:1+2*h*u/d,h+1:-2*(h-1)*u/d}
 else:
  Dc={1:-F(3,2)*u/d,h:F(1,2)+F(3,2)*h*u/d,h+1:F(1,2)-F(3,2)*(h-1)*u/d}
 def Dv(r): return sum(c*r**e for e,c in Dc.items())
 def Hs(r): return F(1,2)-2*eps + F(1,2)*r**M - Dv(r) # A-D-2eps
 return h,u,eps,d,B,C,Dv,Hs

def upper_F(M,k,s):
 h,u,eps,d,B,C,Dv,Hs=blocks(M,k)
 Bb=B(BETA); Cb=C(BETA); Ab=(1+BETA**M)/2; Db=Dv(BETA); Hb=Ab-Db+2*eps
 Bg=B(GAMMA); Cg=C(GAMMA); Ag=(1+GAMMA**M)/2; Dg=Dv(GAMMA); Gg=Ag-Dg
 q=Gg-2*eps
 X=q*Cb-Cg*Hb; Y=Bg*Hb-q*Bb; Z=Cg*Bb-Bg*Cb
 return X*B(s)+Y*C(s)+Z*Hs(s)

def gamma_minus_primal(M,j,s):
 # P={0,j-1,j,M}, Q central; beta-, gamma-, alpha+
 h=M//2; u=F(1,2**h); eps=F(1,(1875 if M%2==0 else 2500)*2**h); d=1-(h+1)*u
 if M%2==0:
  Dc={1:-2*u/d,h:1+2*h*u/d,h+1:-2*(h-1)*u/d}
 else:
  Dc={1:-F(3,2)*u/d,h:F(1,2)+F(3,2)*h*u/d,h+1:F(1,2)-F(3,2)*(h-1)*u/d}
 def C(r): return (2*r-2*h*r**h+2*(h-1)*r**(h+1))/d
 def Dv(r): return sum(c*r**e for e,c in Dc.items())
 def Br(r,k): return r**k-F(M-k,M)-F(k,M)*r**M
 def A(r): return (1+r**M)/2
 a=j-1
 rows=[]; rhs=[]
 # beta-
 rows.append([Br(BETA,a),Br(BETA,j),A(BETA)-Dv(BETA)+2*eps]); rhs.append(C(BETA))
 # gamma-
 rows.append([Br(GAMMA,a),Br(GAMMA,j),A(GAMMA)-Dv(GAMMA)+2*eps]); rhs.append(C(GAMMA))
 # alpha+
 rows.append([Br(s,a),Br(s,j),A(s)-Dv(s)-2*eps]); rhs.append(C(s))
 pm,pj,t=solve3(rows,rhs)
 pM=F(1,2)*t-F(a,M)*pm-F(j,M)*pj
 p0=F(1,2)*t-F(M-a,M)*pm-F(M-j,M)*pj
 return p0,pm,pj,pM,t

def dec(x):
 getcontext().prec=32; return str(Decimal(x.numerator)/Decimal(x.denominator))

def main():
 probes=[F(258+i,2000) for i in range(9)]
 n=0; bad=[]; danger=[]; dmin=10**9
 for M in range(521,1001):
  h=M//2
  for s in probes:
   b=exact_b(M,s); j=b+2
   phi=upper_F(M,j,s)
   if phi>=0: continue
   p0,pm,pj,pM,t=gamma_minus_primal(M,j,s); n+=1; d=3*j-h; dmin=min(dmin,d)
   if d<13 or (pj>0 and p0>=0): bad.append((M,str(s),j,d,sgn(p0),sgn(pm),sgn(pj),sgn(pM),sgn(t)))
   danger.append((abs(p0),M,s,j,d,p0,pm,pj,pM,t))
 danger.sort(key=lambda z:z[0])
 out={'audit':'A114B2_GAMMA_MINUS_REDUCED_EXACT_SCAN','M_range':[521,1000],'probes':[str(x) for x in probes],
      'phi_negative_cases':n,'failures':bad,'min_3j_minus_h':dmin,
      'all_pj_positive_implies_p0_negative':len(bad)==0,
      'dangerous':[{'M':z[1],'s':str(z[2]),'j':z[3],'3j-h':z[4],'p0':dec(z[5]),'p_jm1':dec(z[6]),'p_j':dec(z[7]),'pM':dec(z[8]),'t':dec(z[9])} for z in danger[:10]]}
 OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps(out,indent=2))
if __name__=='__main__': main()
