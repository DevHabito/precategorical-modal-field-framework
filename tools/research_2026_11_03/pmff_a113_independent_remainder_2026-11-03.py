#!/usr/bin/env python3
"""Independent finite exact audit of frozen A113 A83/A84 small-left factor.

Uses documented rational formulas, no project source imports or floats.
Numerical grid controls do not establish uniform inequalities.
"""
from __future__ import annotations
from fractions import Fraction as Q
import json
import sympy as sp

BETA = Q(1,8)
TARGET = Q(1,2)
SOURCES = (Q(129,1000), Q(131,1000), Q(133,1000))
SIZES = (521,522,561,661)
CONTACTS = (2,3,7,15,29)


def actual_defect(m: int, r: Q) -> Q:
    h = m//2
    u = Q(1,2)**h
    d = 1 - (h+1)*u
    assert d > 0
    if m % 2 == 0:
        return -2*u*r/d + (1+2*h*u/d)*r**h - 2*(h-1)*u*r**(h+1)/d
    return -Q(3,2)*u*r/d + (Q(1,2)+Q(3,2)*h*u/d)*r**h + (Q(1,2)-Q(3,2)*(h-1)*u/d)*r**(h+1)


def actual_h(m: int, r: Q, beta_channel: bool) -> Q:
    u = Q(1,2)**(m//2)
    eps = u / (1875 if m % 2 == 0 else 2500)
    return (1+r**m)/2 - actual_defect(m,r) + (2*eps if beta_channel else -2*eps)


def slope(m: int,r: Q) -> Q:
    return (1-r**m)/m


def cofactor(m:int,k:int,s:Q)->Q:
    target_mass=(1+TARGET**m)/2
    hb=actual_h(m,BETA,True)
    hs=actual_h(m,s,False)
    def mass(r:Q)->Q:
        return r**k - 1 + k*slope(m,r)
    def adjacent(r:Q)->Q:
        return (r-1)*r**k+slope(m,r)
    x=target_mass*mass(BETA)-hb*mass(TARGET)
    y=-target_mass*adjacent(BETA)+hb*adjacent(TARGET)
    w=-mass(BETA)*adjacent(TARGET)+mass(TARGET)*adjacent(BETA)
    return x*adjacent(s)+y*mass(s)+w*hs


def ten_term(m:int,k:int,s:Q)->Q:
    a=(1+TARGET**m)/2
    hb=actual_h(m,BETA,True)
    hs=actual_h(m,s,False)
    ab,at,ass=slope(m,BETA),slope(m,TARGET),slope(m,s)
    vb=a*ass-hs*at
    vs=a*ab-hb*at
    vt=hb*ass-hs*ab
    cb=vb+(BETA-1)*(a-hs)
    cs=-vs+(1-s)*(a-hb)
    ct=-vt+(1-TARGET)*(hb-hs)
    db=(1-BETA)*vb
    ds=(s-1)*vs
    dt=(TARGET-1)*vt
    c1=(hb-a)*ass+(a-hs)*ab+(hs-hb)*at
    return (a*(s-BETA)*(BETA*s)**k
        + hs*(BETA-TARGET)*(BETA*TARGET)**k
        + hb*(TARGET-s)*(s*TARGET)**k
        + (cb+k*db)*BETA**k
        + (cs+k*ds)*s**k
        + (ct+k*dt)*TARGET**k + c1)


def ideal(k:int,s:Q)->Q:
    return Q(1,2)*((s-BETA)*(BETA*s)**k + (BETA-TARGET)*(BETA*TARGET)**k + (TARGET-s)*(s*TARGET)**k)


def prove_algebraic_bridge():
    # Derive equality for arbitrary symbolic nodes, slopes, channels, k and
    # independently represented kth powers; no finite sample substitution.
    b,t,s,A,Hb,Hs,ab,at,ass,K,pb,pt,ps=sp.symbols('b t s A Hb Hs ab at ass K pb pt ps')
    massb=pb-1+K*ab; masst=pt-1+K*at; masss=ps-1+K*ass
    deltab=(b-1)*pb+ab; deltat=(t-1)*pt+at; deltas=(s-1)*ps+ass
    x=A*massb-Hb*masst
    y=-A*deltab+Hb*deltat
    w=-massb*deltat+masst*deltab
    cofactor_poly=x*deltas+y*masss+w*Hs
    vb=A*ass-Hs*at; vs=A*ab-Hb*at; vt=Hb*ass-Hs*ab
    cb=vb+(b-1)*(A-Hs); cs=-vs+(1-s)*(A-Hb); ct=-vt+(1-t)*(Hb-Hs)
    db=(1-b)*vb; ds=(s-1)*vs; dt=(t-1)*vt
    c1=(Hb-A)*ass+(A-Hs)*ab+(Hs-Hb)*at
    expanded=(A*(s-b)*pb*ps + Hs*(b-t)*pb*pt + Hb*(t-s)*ps*pt
              +(cb+K*db)*pb+(cs+K*ds)*ps+(ct+K*dt)*pt+c1)
    assert sp.Poly(sp.expand(cofactor_poly-expanded),pb,pt,ps,K,b,t,s,A,Hb,Hs,ab,at,ass).is_zero
    # Wrong orientation of one product channel must be caught.
    wrong=expanded-2*Hb*(t-s)*ps*pt
    assert sp.Poly(sp.expand(cofactor_poly-wrong),pb,pt,ps,K,b,t,s,A,Hb,Hs,ab,at,ass) != sp.Poly(0,pb,pt,ps,K,b,t,s,A,Hb,Hs,ab,at,ass)


def main():
    prove_algebraic_bridge()
    checked = 0
    max_ratio=Q(0)
    smallest_margin=None
    for m in SIZES:
        u=Q(1,2)**(m//2)
        assert u<=Q(1,2)**260
        for s in SOURCES:
            hb=actual_h(m,BETA,True)
            hs=actual_h(m,s,False)
            A=(1+TARGET**m)/2
            assert abs(A-Q(1,2))<=u/2
            assert abs(hb-Q(1,2))<u
            assert abs(hs-Q(1,2))<u
            for k in CONTACTS:
                e=cofactor(m,k,s)
                et=ten_term(m,k,s)
                f=ideal(k,s)
                assert e==et, ('A83/A84 mismatch',m,s,k)
                error=abs(e-f)
                bound=20*u
                assert error<bound, ('error bound fails',m,s,k)
                assert f>bound, ('ideal margin fails',m,s,k)
                assert e>0, ('sign fails',m,s,k)
                ratio=error/u
                max_ratio=max(max_ratio,ratio)
                margin=e
                smallest_margin=margin if smallest_margin is None else min(margin,smallest_margin)
                checked+=1
    # Exact rational constants behind the universal proposed inequality.
    L=Q(1,2)*(Q(129,1000)-BETA)*(TARGET-BETA)*(TARGET-Q(133,1000))*(Q(129,2000)**28)
    assert L>20*Q(1,2)**260
    assert Q(18)+Q(9*29+6,521)<20
    assert max_ratio<20
    print('Symbolic A83-to-A84 identity: PASS (arbitrary formal variables)')
    print('One-term sign mutation negative control: PASS')
    print('Exact rational frozen contract controls: PASS')
    print('Exact rational controls run:', checked)
    print('M values:', SIZES)
    print('s values:', [str(s) for s in SOURCES])
    print('k values:', CONTACTS)
    print('Maximum observed error / U: <', int(max_ratio)+1, '(integer ceiling, no float)')
    print('Exact uniform-margin arithmetic gate: PASS')
    print('Scope: symbolic algebra + 60 finite exact samples; no general Lean proof or all-M proof')

if __name__=='__main__':main()