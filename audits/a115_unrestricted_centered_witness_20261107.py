#!/usr/bin/env python3
"""A115 red-team: prove the finite centered equal-measure sanity witness by exact arithmetic.

For every positive tau and M>=1 the equal-measure construction below has
mass t>0, mean M/2, Q_tau=1, and zero gap at *every* transform node.
Thus imposing additional symmetric difference bands of nonnegative width
cannot make the unrestricted equal-mean two-measure LP infeasible, provided
coincident measures/supports are permitted by the full contract.

This does NOT rescue the particular compressed P={0,k,M}, Q={1,h,h+1}
active-band candidate, and it is not a KKT/optimality certificate.
"""
from fractions import Fraction as F

def centered_equal_measures(M: int, tau: F):
    assert M>=1 and 0<tau<1
    h=M//2
    if M%2==0:
        w={h: F(1)/tau**h}
    else:
        v=F(1)/(tau**h*(1+tau))
        w={h:v,h+1:v}
    t=sum(w.values(), F(0))
    return w,w.copy(),t

def transform(w,r):
    return sum((mass*r**x for x,mass in w.items()),F(0))

def audit():
    tested=0
    for M in (4,5,24,25,40,41,100,101,521,522):
        for tau in (F(14,100),F(1,5),F(1,2),F(4,5)):
            p,q,t=centered_equal_measures(M,tau)
            assert t>0 and all(v>0 for v in p.values())
            assert sum(p.values())==sum(q.values())==t
            assert sum(x*v for x,v in p.items())==F(M,2)*t
            assert sum(x*v for x,v in q.items())==F(M,2)*t
            assert transform(q,tau)==1
            assert transform(p,tau)==1   # objective is exactly 1
            eps=F(1,1875)*tau**(M//2)*(F(1) if M%2==0 else (1+tau)/2)
            assert eps>0
            for r in (F(1,16),F(1,8),F(129,1000),F(131,1000),F(133,1000)):
                gap=transform(p,r)-transform(q,r)
                assert gap==0 and -2*eps*t<=gap<=2*eps*t
            tested+=1
    print(f"PASS: {tested} exact centered P=Q full-band feasibility witnesses; all objectives = 1")
    print("SCOPE: requires full LP to admit coincident distributions; not a proof of compressed candidate feasibility")

if __name__=="__main__":
    audit()
