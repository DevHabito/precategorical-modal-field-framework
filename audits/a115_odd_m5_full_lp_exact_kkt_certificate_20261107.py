#!/usr/bin/env python3
"""Exact-rational odd-M full F3 primal-dual uniqueness certificate.

Fixed contract: M=5, s=129/1000, tau=1/2, beta=1/8,
gamma=1/16, epsilon=1/10000 (odd parity).

Float HiGHS was only used to suggest a basis. This file uses
Fraction Gaussian elimination, no optimization solver, and
verifies all rows and complementary slackness exactly.

No extrapolation to all odd M is claimed.
"""
from fractions import Fraction as F
from a115_small_full_lp_exact_kkt_certificate_20261107 import exact_solve_square,dot
import a115_explicit_full_primal_and_dual_gate_20261107 as verifier

if not __debug__:
    raise RuntimeError("Assertions must remain enabled")

M=5
S=F(129,1000)
TAU=F(1,2)
BETA=F(1,8)
GAMMA=F(1,16)
EPS=F(1,1875)*(1+TAU)/2*TAU**(M//2)
DIM=2*(M+1)+1
BASIS=(0,1,2,5,7,9,12)  # P0,P1,P2,P5,Q1,Q3,t
ACTIVE=(0,5)             # s+, gamma-
EXPECTED=F(123288732982051199633,110644995632951812500)


def build():
    eq=[]
    for which in (0,1):
        row=[F(0)]*DIM
        for x in range(M+1):
            row[which*(M+1)+x]=F(1)
        row[-1]=-F(1)
        eq.append(row)
    for which in (0,1):
        row=[F(0)]*DIM
        for x in range(M+1):
            row[which*(M+1)+x]=F(x)-F(M,2)
        eq.append(row)
    target=[F(0)]*DIM
    for x in range(M+1):
        target[M+1+x]=TAU**x
    eq.append(target)
    rhs=[F(0)]*4+[F(1)]
    band=[]
    for r in (S,BETA,GAMMA):
        for orientation in (1,-1):
            row=[F(0)]*DIM
            for x in range(M+1):
                row[x]=orientation*r**x
                row[M+1+x]=-orientation*r**x
            row[-1]=-2*EPS
            band.append(row)
    objective=[TAU**x for x in range(M+1)]+[F(0)]*(M+2)
    return eq,rhs,band,objective


def verify():
    assert EPS==F(1,10000)
    eq,rhs,band,c=build()
    rows=eq+[band[j] for j in ACTIVE]
    xb,det=exact_solve_square([[row[j] for j in BASIS] for row in rows],
                               rhs+[F(0),F(0)])
    assert all(v>0 for v in xb)
    primal=[F(0)]*DIM
    for j,v in zip(BASIS,xb):
        primal[j]=v
    assert all(dot(row,primal)==b for row,b in zip(eq,rhs))
    slacks=[-dot(row,primal) for row in band]
    assert all(slacks[j]>0 for j in range(6) if j not in ACTIVE)
    assert all(slacks[j]==0 for j in ACTIVE)

    dual,det_transpose=exact_solve_square(
        [[row[j] for row in rows] for j in BASIS],
        [c[j] for j in BASIS])
    assert det==det_transpose and det!=0
    assert dual[5]>0 and dual[6]>0
    reduced=[dot(dual,[row[j] for row in rows])-c[j]
             for j in range(DIM)]
    assert all(reduced[j]==0 for j in BASIS)
    assert all(reduced[j]>0 for j in range(DIM) if j not in BASIS)

    Fprimal=dot(c,primal)
    Fdual=dot(dual[:5],rhs)
    assert Fprimal==Fdual==EXPECTED and Fprimal>1

    p={j:primal[j] for j in range(M+1) if primal[j]}
    q={j:primal[M+1+j] for j in range(M+1) if primal[M+1+j]}
    t=primal[-1]
    model=verifier.LP(M,S,TAU,True)
    assert not verifier.audit_primal(model,p,q,t)
    u={r:F(0) for r in model.nodes()}
    w={r:F(0) for r in model.nodes()}
    u[S]=dual[5];w[GAMMA]=dual[6]
    cert=verifier.Dual(*dual[:5],u,w)
    assert not verifier.audit_dual(model,cert)

    # Positive active dual multipliers force both active bands at any
    # alternate optimum. Strict other reduced costs force the same
    # active support. det!=0 then forces the identical basis solution.
    assert tuple(i for i,v in enumerate(primal) if v>0)==BASIS
    print("PASS: exact odd M=5 unrestricted F3 primal, full dual and UNIQUE optimum")
    print("P support:",sorted(p),"Q support:",sorted(q))
    print("exact objective:",Fprimal)
    print("nonzero active-basis determinant:",det)
    print("strict inactive band slacks and nonbasic reduced costs: PASS")
    print("LIMIT: fixed M=5 only; not a target-deformed or all-odd theorem")


if __name__=="__main__":
    verify()
