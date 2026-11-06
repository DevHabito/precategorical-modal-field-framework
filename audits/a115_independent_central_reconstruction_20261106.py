#!/usr/bin/env python3
"""Independent exact checks of the A115 three-support Q block.

All equality and inequality decisions use fractions.Fraction.
Finite controls do not prove the statements for arbitrary parameters.
"""
from fractions import Fraction as F


def denom(h, tau):
    return tau - h * tau**h + (h-1) * tau**(h+1)


def qcoords(M, tau, t):
    h = M // 2
    D = denom(h, tau)
    u = tau**h
    odd = M % 2
    first = (1 - (u if not odd else (1+tau)*u/2)*t)/D
    if odd:
        second = t/2-h*first
        third = t/2+(h-1)*first
    else:
        second = t-h*first
        third = (h-1)*first
    return (first, second, third)


def predicted_slope(M, tau, r):
    h = M//2
    D = denom(h,tau)
    u = tau**h
    L = r-h*r**h+(h-1)*r**(h+1)
    return (r**h-u*L/D if M%2==0 else
            (r**h+r**(h+1))/2-(1+tau)*u*L/(2*D))


def main():
    count=0
    for M in range(4, 105):
        h=M//2
        for tau in (F(1,7), F(1,3), F(1,2), F(4,5), F(9,10)):
            D=denom(h,tau)
            assert D == tau*(1-tau)**2 * sum((j+1)*tau**j for j in range(h-1))
            assert D>0
            for t in (F(0),F(2,7),F(1)):
                a,b,c=qcoords(M,tau,t)
                assert a+b+c==t
                assert a+h*b+(h+1)*c==F(M,2)*t
                assert tau*a+tau**h*b+tau**(h+1)*c==1
                count+=1
            for r in (F(1,8),F(129,1000),F(131,1000),F(133,1000)):
                q0=qcoords(M,tau,F(0))
                q1=qcoords(M,tau,F(1))
                slope=sum((r,r**h,r**(h+1))[i]*(q1[i]-q0[i]) for i in range(3))
                assert slope==predicted_slope(M,tau,r)
    print(f"PASS: {count} exact central-system controls; {101*5} exact denominator identities; {101*5*4} exact D_r slope checks")


if __name__=='__main__':
    main()
