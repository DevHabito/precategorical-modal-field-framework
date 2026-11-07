#!/usr/bin/env python3
"""Exact even/odd source-numerator sign controls in the A115 deformation.

Verifies the cancellation of target-dependent cross terms. This is a
finite falsification grid; a uniform monotonicity proof is documented
separately and is not obtained by enumerating the grid.
"""
from fractions import Fraction as F

BETA=F(1,8)
DELTA=F(1,1875)
S_VALUES=(F(129,1000),F(131,1000),F(133,1000))
TAUS=(F(67,500),F(7,50),F(1,5),F(1,2),F(4,5))


def L(h,r):
    return r-h*r**h+(h-1)*r**(h+1)


def R(M,h,r):
    return (1-r**h)*(1-r**(M-h))/2


def qcoords(M,tau,t):
    h=M//2;D=L(h,tau);u=tau**h
    a=F(1) if M%2==0 else (1+tau)/2
    q1=(1-a*u*t)/D
    if M%2==0:
        return ((1,q1),(h,t-h*q1),(h+1,(h-1)*q1))
    return ((1,q1),(h,t/2-h*q1),(h+1,t/2+(h-1)*q1))


def tr(w,r):
    return sum((v*r**j for j,v in w),F(0))


def main():
    count=0
    for h in range(2,81):
        for odd in (0,1):
            M=2*h+odd
            for s in S_VALUES:
                Lb,Ls=L(h,BETA),L(h,s)
                Rb,Rs=R(M,h,BETA),R(M,h,s)
                assert 0<Lb<Ls and 0<Rs<Rb
                for r in (BETA,s):
                    assert h*h*r**(h-1)<=4*r<1
                for tau in TAUS:
                    assert s<tau<1
                    D=L(h,tau)
                    a=F(1) if M%2==0 else (1+tau)/2
                    K=a*tau**h
                    eps=DELTA*K
                    Cb=Lb/D;Cs=Ls/D
                    Hbeta=Rb+K*Cb+2*eps
                    Hs=Rs+K*Cs-2*eps
                    Z=Cb*Hs-Cs*Hbeta
                    numerator=Lb*Rs-Ls*Rb-2*eps*(Lb+Ls)
                    assert D>0 and D*Z==numerator and numerator<0 and Z<0
                    qb0=tr(qcoords(M,tau,F(0)),BETA)
                    qs0=tr(qcoords(M,tau,F(0)),s)
                    Db=tr(qcoords(M,tau,F(1)),BETA)-qb0
                    Ds=tr(qcoords(M,tau,F(1)),s)-qs0
                    Ab=(1+BETA**M)/2
                    As=(1+s**M)/2
                    assert Cb==qb0 and Cs==qs0
                    assert Hbeta==Ab-Db+2*eps
                    assert Hs==As-Ds-2*eps
                    count+=1
    print(f"PASS: {count} exact Q-source cancellation, source negativity, parity and derivative-bound checks")


if __name__=="__main__":
    main()
