#!/usr/bin/env python3
"""Exact A115 near-wall counterexample recheck.

Independent reconstruction from the published closed Q-block and cofactor
formulas, using fractions.Fraction. The first two negative controls belong to
the A84 adjacent-factor domain. The third negative value does not; it must
NOT be counted as a valid counterexample.
"""
from fractions import Fraction as F
import hashlib
import sys

# Converting a several-thousand-digit fraction to text may exceed Python's
# default safety limit. No bound in the mathematical calculation is removed.
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

BETA=F(1,8)
DELTA=F(1,1875)

def b_exact(M,s,tau):
    lo,hi=0,M
    while lo<hi:
        mid=(lo+hi)//2
        if s**(2*mid)<=tau**M:hi=mid
        else:lo=mid+1
    return lo

def D(M,t):
    h=M//2;u=t**h
    return t-h*u+(h-1)*t*u

def d(M,r,t):
    h=M//2;u=t**h
    L=r-h*r**h+(h-1)*r**(h+1)
    return (r**h-u*L/D(M,t) if M%2==0 else
            (r**h+r**(h+1))/2-(1+t)*u*L/(2*D(M,t)))

def B(M,k,r):
    return r**k-F(M-k,M)-F(k,M)*r**M

def dB(M,k,r):
    return r**(k+1)-r**k+F(1-r**M,M)

def E(M,k,s,t):
    h=M//2
    eps=DELTA*t**h*(F(1) if M%2==0 else F(1+t,2))
    Hb=F(1+BETA**M,2)-d(M,BETA,t)+2*eps
    Hs=F(1+s**M,2)-d(M,s,t)-2*eps
    A=F(1+t**M,2)
    bb,bt=B(M,k,BETA),B(M,k,t)
    xb,xt=dB(M,k,BETA),dB(M,k,t)
    X=A*bb-Hb*bt
    Y=-A*xb+Hb*xt
    W=-bb*xt+bt*xb
    return X*dB(M,k,s)+Y*B(M,k,s)+W*Hs

def main():
    probes=(
        (521,F(131,1000),F(141,1000),True,
         "dc0efb5b23581db2a5c4983e87097884582dddee1fd68d5ec28d9b459bef8bac"),
        (521,F(133,1000),F(143,1000),True,
         "e60c0f4b4bf1ef74867c3d80cebb5fb805364b7d542114fe2f858b6aeea7e34f"),
        (521,F(129,1000),F(667,5000),False,None)
    )
    for M,s,t,expected_valid,expected_hash in probes:
        h=M//2
        b=b_exact(M,s,t)
        k=b+1
        J=E(M,k,s,t)-E(M,k+1,s,t)/t
        digest=hashlib.sha256(f"{J.numerator}/{J.denominator}".encode()).hexdigest()
        valid=(2<=k and k+1<=h-2)
        assert J<0
        assert valid==expected_valid
        if expected_hash is not None:
            assert digest==expected_hash
        status="IN_DOMAIN_COUNTEREXAMPLE" if valid else "REJECTED_OUTSIDE_FACTOR_DOMAIN"
        print("M",M,"s",s,"tau",t,"b",b,"domain",valid,
              "negative",J<0,"sha256",digest,"status",status)
    print("PASS: 2 in-domain counterexamples and 1 correctly rejected out-of-domain candidate")

if __name__=="__main__":
    main()
