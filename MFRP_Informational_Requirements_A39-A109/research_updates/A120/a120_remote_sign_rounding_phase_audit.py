#!/usr/bin/env python3
from fractions import Fraction as F
import json, sys
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"): sys.set_int_max_str_digits(0)

BETA=F(1,8); DELTA=F(1,1875)
OUT=Path(__file__).resolve().parent/"A120_EXACT_AUDIT_RESULTS_20260915.json"

def sgn(x): return (x>0)-(x<0)
def pows(x,n):
    a=[F(1)]*(n+1)
    for i in range(1,n+1): a[i]=a[i-1]*x
    return a
def B(M,k,p): return p[k]-F(M-k,M)-F(k,M)*p[M]
def dB(M,k,p): return p[k+1]-p[k]+F(1-p[M],M)
def den(M,tau):
    h=M//2; u=tau**h
    return tau-h*u+(h-1)*tau*u
def eps(M,tau):
    h=M//2; u=tau**h
    return DELTA*(u if M%2==0 else F(1+tau,2)*u)
def dt(M,r,p,tau):
    h=M//2; u=tau**h
    L=r-h*p[h]+(h-1)*p[h+1]
    if M%2==0: return p[h]-u*L/den(M,tau)
    return F(p[h]+p[h+1],2)-F(1+tau,2)*u*L/den(M,tau)
def E(M,k,s,tau):
    bp,tp,sp=pows(BETA,M),pows(tau,M),pows(s,M)
    e=eps(M,tau)
    hb=F(1+bp[M],2)-dt(M,BETA,bp,tau)+2*e
    hs=F(1+sp[M],2)-dt(M,s,sp,tau)-2*e
    bb,bt=B(M,k,bp),B(M,k,tp)
    xb,xt=dB(M,k,bp),dB(M,k,tp)
    A=F(1+tp[M],2)
    X=A*bb-hb*bt; Y=-A*xb+hb*xt; W=-bb*xt+bt*xb
    return X*dB(M,k,sp)+Y*B(M,k,sp)+W*hs
def b_exact(M,s,tau):
    lo,hi=0,M; target=tau**M
    while lo<hi:
        m=(lo+hi)//2
        if s**(2*m)<=target: hi=m
        else: lo=m+1
    return lo
def admiss(M,b): return b+3<=M//2-2

def c_bound_exact(s,t,lo,hi):
    p,q=lo.numerator,lo.denominator
    lower = s**(2*p)>t**q
    p,q=hi.numerator,hi.denominator
    upper = s**(2*p)<t**q
    return lower and upper

def phase_even(s,t,j,rho,c):
    G=(s-BETA)/t-4*DELTA
    return (t-s)*s**(j+rho)/2-(1-t)*G*(1-c)

def main():
    frozen=[]
    for M in (521,522,561,600,760,1000,2049):
        for s in (F(129,1000),F(131,1000),F(133,1000)):
            t=F(1,2); b=b_exact(M,s,t)
            eb=E(M,b,s,t); e3=E(M,b+3,s,t)
            assert eb>0 and e3<0
            frozen.append((M,str(s),b))

    sA,tA=F(131,1000),F(1,5); MA=1200; bA=b_exact(MA,sA,tA)
    assert admiss(MA,bA)
    eA=E(MA,bA,sA,tA); assert eA<0

    sB,tB=F(129,1000),F(9,10); MB=536; bB=b_exact(MB,sB,tB)
    assert admiss(MB,bB)
    eB=E(MB,bB+3,sB,tB); assert eB>0

    cAlo,cAhi=F(395,1000),F(397,1000)
    cBlo,cBhi=F(25,1000),F(27,1000)
    assert c_bound_exact(sA,tA,cAlo,cAhi)
    assert c_bound_exact(sB,tB,cBlo,cBhi)

    A_left_lb=phase_even(sA,tA,0,0,cAlo)
    A_right_ub=phase_even(sA,tA,0,1,cAhi)
    B_left_lb=phase_even(sB,tB,3,0,cBlo)
    B_right_ub=phase_even(sB,tB,3,1,cBhi)
    assert A_left_lb>0 and A_right_ub<0
    assert B_left_lb>0 and B_right_ub<0

    out={
      "audit":"A120_REMOTE_SIGN_ROUNDING_PHASE_AUDIT",
      "date":"2026-09-15",
      "status":"PASS_WITH_REFUTATION_OF_NAIVE_STABILIZATION",
      "frozen_tau_half_regression_count":len(frozen),
      "exact_counterexamples":{
        "E_b_negative":{"M":MA,"s":"131/1000","tau":"1/5","b":bA,"sign":-1},
        "E_bplus3_positive":{"M":MB,"s":"129/1000","tau":"9/10","b":bB,"sign":1}
      },
      "irrational_phase_pairs":{
        "pair_A":{"s":"131/1000","tau":"1/5","c_bounds":["395/1000","397/1000"],
                  "even_j0_phase_at_rho0_lower":str(A_left_lb),
                  "even_j0_phase_at_rho1_upper":str(A_right_ub)},
        "pair_B":{"s":"129/1000","tau":"9/10","c_bounds":["25/1000","27/1000"],
                  "even_j3_phase_at_rho0_lower":str(B_left_lb),
                  "even_j3_phase_at_rho1_upper":str(B_right_ub)}
      },
      "nonclaims":[
        "finite counterexamples alone do not prove infinite sign alternation",
        "infinite alternation uses the analytic rounding-phase theorem plus irrationality/density",
        "no target-deformed A114 theorem",
        "no physical or ontological interpretation"
      ]
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__": main()
