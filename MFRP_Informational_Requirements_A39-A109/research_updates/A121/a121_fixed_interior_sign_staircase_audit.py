#!/usr/bin/env python3
from fractions import Fraction as F
import json, sys
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"): sys.set_int_max_str_digits(0)

BETA=F(1,8); DELTA=F(1,1875)
OUT=Path(__file__).resolve().parent/"A121_EXACT_AUDIT_RESULTS_20260915.json"

def sg(x): return (x>0)-(x<0)
def B(M,k,r):
    rM=r**M
    return r**k-F(M-k,M)-F(k,M)*rM
def dB(M,k,r):
    rM=r**M
    return r**(k+1)-r**k+F(1-rM,M)
def den(M,tau):
    h=M//2; u=tau**h
    return tau-h*u+(h-1)*tau*u
def eps(M,tau):
    h=M//2; u=tau**h
    return DELTA*(u if M%2==0 else F(1+tau,2)*u)
def dt(M,r,tau):
    h=M//2; u=tau**h
    rh=r**h; rh1=rh*r
    L=r-h*rh+(h-1)*rh1
    if M%2==0:
        return rh-u*L/den(M,tau)
    return F(rh+rh1,2)-F(1+tau,2)*u*L/den(M,tau)
def E(M,k,s,tau):
    e=eps(M,tau)
    hb=F(1+BETA**M,2)-dt(M,BETA,tau)+2*e
    hs=F(1+s**M,2)-dt(M,s,tau)-2*e
    bb,bt=B(M,k,BETA),B(M,k,tau)
    xb,xt=dB(M,k,BETA),dB(M,k,tau)
    A=F(1+tau**M,2)
    X=A*bb-hb*bt; Y=-A*xb+hb*xt; W=-bb*xt+bt*xb
    return X*dB(M,k,s)+Y*B(M,k,s)+W*hs
def b_exact(M,s,tau):
    lo,hi=0,M; target=tau**M
    while lo<hi:
        m=(lo+hi)//2
        if s**(2*m)<=target: hi=m
        else: lo=m+1
    return lo
def one_variation(signs):
    seen_negative=False
    for z in signs:
        if z<0: seen_negative=True
        elif z>0 and seen_negative: return False
    return True

def check_case(M,s,tau,js,expected):
    b=b_exact(M,s,tau)
    vals={j:E(M,b+j,s,tau) for j in js}
    signs={j:sg(vals[j]) for j in js}
    assert signs==expected,(M,s,tau,b,signs,expected)
    Js={}
    for j in js[:-1]:
        J=vals[j]-vals[j+1]/tau
        Js[j]=sg(J)
        assert Js[j]>0,(M,s,tau,b,j,Js[j])
    return {"M":M,"s":str(s),"tau":str(tau),"b":b,
            "factor_signs":{str(j):signs[j] for j in js},
            "adjacent_J_signs":{str(j):Js[j] for j in js[:-1]}}

def main():
    frozen=[]
    for M in (521,522,561,600,760,1000,2049):
        for s in (F(129,1000),F(131,1000),F(133,1000)):
            tau=F(1,2); b=b_exact(M,s,tau)
            signs=[sg(E(M,b+j,s,tau)) for j in range(4)]
            assert signs[0]>0 and signs[3]<0 and one_variation(signs),(M,s,b,signs)
            frozen.append({"M":M,"s":str(s),"b":b,"signs_j0_to_j3":signs})

    sentinels=[]
    sentinels.append(check_case(500,F(131,1000),F(1,5),[-1,0,1],{-1:1,0:1,1:-1}))
    sentinels.append(check_case(508,F(131,1000),F(1,5),[-1,0,1],{-1:1,0:-1,1:-1}))
    sentinels.append(check_case(505,F(131,1000),F(1,5),[-1,0,1],{-1:1,0:1,1:-1}))
    sentinels.append(check_case(503,F(131,1000),F(1,5),[-1,0,1],{-1:1,0:-1,1:-1}))
    sentinels.append(check_case(500,F(129,1000),F(9,10),[2,3,4],{2:1,3:1,4:-1}))
    sentinels.append(check_case(506,F(129,1000),F(9,10),[2,3,4],{2:1,3:-1,4:-1}))
    sentinels.append(check_case(501,F(129,1000),F(9,10),[2,3,4],{2:1,3:1,4:-1}))
    sentinels.append(check_case(507,F(129,1000),F(9,10),[2,3,4],{2:1,3:-1,4:-1}))

    M=1200; s=F(129,1000); tau=F(15,100); b=b_exact(M,s,tau); j=3
    e0=E(M,b+j,s,tau); e1=E(M,b+j+1,s,tau)
    J=e0-e1/tau
    assert J<0
    finite_warning={"M":M,"s":str(s),"tau":str(tau),"b":b,"j":j,
                    "sign_E_j":sg(e0),"sign_E_jplus1":sg(e1),"sign_J":sg(J)}

    out={
      "audit":"A121_FIXED_INTERIOR_SIGN_STAIRCASE_AUDIT",
      "date":"2026-09-15",
      "status":"PASS",
      "frozen_tau_half_one_variation_regressions":len(frozen),
      "two_site_exact_sentinels":sentinels,
      "finite_M_scope_warning":finite_warning,
      "analytic_identity_checked_in_theorem":
        "Psi_j-Psi_(j+1)=P*s^(j+rho)*(1-s)>0; Xi threshold gives one +->- limiting staircase.",
      "nonclaims":[
        "no global compressed-maximizer theorem under target deformation",
        "no uniform finite M0 over all offsets or the full target region",
        "resonant leading-zero factor requires higher-order analysis",
        "collision scaling tau-s=O(1/M) is not covered",
        "no target-deformed A114 theorem",
        "no physical or ontological interpretation"
      ]
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__": main()
