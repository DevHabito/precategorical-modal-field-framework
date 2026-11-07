#!/usr/bin/env python3
"""A115 third-node gamma-band red-team: exact fractions, no floats.

This is a deliberately *conditional* compatibility test. A81 explicitly
uses gamma=1/16 and the +/-2*epsilon*t band. The A115 target-deformation
family fixes active beta-lower and s-upper bands, but does not itself
establish that the A81 gamma band survives the deformation unchanged.

We test what happens *if* that inherited gamma band is imposed.
This does not prove that gamma is an A115 hypothesis.
"""
from fractions import Fraction as F
import a115_independent_compressed_adjacent_identity_20261107 as base

GAMMA=F(1,16)

def verify_gamma(M,k,s,tau):
    sol=base.solve(M,k,s,tau)
    P=base.pweights(M,k,sol["t"],sol["z"])
    Q=base.qcoords(M,tau,sol["t"])
    eps=base.DELTA*tau**(M//2)*(F(1) if M%2==0 else (1+tau)/2)
    gamma_gap=base.transform(P,GAMMA)-base.transform(Q,GAMMA)
    assert sol["t"]>0 and eps>0
    gamma_ok=-2*eps*sol["t"]<=gamma_gap<=2*eps*sol["t"]
    nonnegative=all(v>=0 for _,v in P+Q)
    return nonnegative,gamma_ok,gamma_gap,2*eps*sol["t"]

def main():
    counts=dict(pairs=0,both_nonnegative=0,both_gamma=0,
                both_nonnegative_and_gamma=0,single_contacts=0,
                single_gamma=0)
    examples=[]
    for M in (24,25,40,41,100,101,521,522):
        for s in (F(129,1000),F(131,1000),F(133,1000)):
            for tau in (F(14,100),F(1,5),F(1,2),F(4,5)):
                b=base.b_exact(M,s,tau)
                for k in sorted({max(2,b-1),b,b+1}):
                    if k<2 or k+1>M//2-2:
                        continue
                    a=verify_gamma(M,k,s,tau)
                    c=verify_gamma(M,k+1,s,tau)
                    counts["pairs"]+=1
                    counts["both_nonnegative"]+=int(a[0] and c[0])
                    counts["both_gamma"]+=int(a[1] and c[1])
                    counts["both_nonnegative_and_gamma"]+=int(all((a[0],c[0],a[1],c[1])))
                    counts["single_contacts"]+=2
                    counts["single_gamma"]+=int(a[1])+int(c[1])
                    if a[0] and c[0] and not(a[1] and c[1]) and len(examples)<2:
                        examples.append((M,k,str(s),str(tau),
                                         str(a[2]/a[3]),str(c[2]/c[3])))
    assert counts["pairs"]==213
    assert counts["both_nonnegative"]==159
    assert counts["both_gamma"]==0
    assert counts["both_nonnegative_and_gamma"]==0
    assert counts["single_gamma"]==0
    print("PASS: conditional inherited A81 gamma-band exact stress:",counts)
    print("PASS: exact gamma-gap / (2*epsilon*t) witness ratios:",examples)
    print("SCOPE: only if the A81 gamma band is imposed on A115 deformed candidates")

if __name__=="__main__":
    main()
