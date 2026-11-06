#!/usr/bin/env python3
"""Exact-rational boundary controls for A115 central Q-block feasibility.

This is a finite falsification harness, not a proof of the global equivalence.
No floating point is used.
"""
from fractions import Fraction as F


def bounds(M, tau):
    h=M//2
    u=tau**h
    D=tau-h*u+(h-1)*tau*u
    a=(1+tau)/2 if M%2 else F(1)
    lower=F(2*h,D+2*h*a*u) if M%2 else F(h,D+h*u)
    upper=1/(a*u)
    assert D>0 and lower<upper
    return lower,upper


def weights(M,tau,t):
    h=M//2
    u=tau**h
    D=tau-h*u+(h-1)*tau*u
    a=(1+tau)/2 if M%2 else F(1)
    x=(1-a*u*t)/D
    if M%2:
        return x,t/2-h*x,t/2+(h-1)*x
    return x,t-h*x,(h-1)*x


def main():
    controls=0
    for M in range(4,60):
        for tau in (F(1,7),F(1,3),F(1,2),F(4,5),F(9,10)):
            lower,upper=bounds(M,tau)
            for t in (lower-F(1,1000),lower,(lower+upper)/2,upper,upper+F(1,1000)):
                x,y,z=weights(M,tau,t)
                assert (x>=0 and y>=0 and z>=0)==(lower<=t<=upper)
                controls+=1
    print(f"PASS: {controls} exact feasibility comparisons, including both interval boundaries and outside points")


if __name__=="__main__":
    main()
