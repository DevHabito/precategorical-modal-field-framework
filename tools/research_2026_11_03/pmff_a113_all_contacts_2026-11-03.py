#!/usr/bin/env python3
"""Extra exact A113 frozen-domain regression for all k in [2,29].

Independent of the historical project's implementation. Tests 336 finite
combinations; no inference of universal M/real-s quantification.
"""
from fractions import Fraction as Q
from pathlib import Path
import runpy

# Load the exact adjacent standalone source file; its main() is not invoked.
_source = runpy.run_path(str(Path(__file__).with_name(
    'pmff_a113_independent_remainder_2026-11-03.py')))
BETA, TARGET, SOURCES, SIZES, actual_h, slope, cofactor, ten_term, ideal = (
    _source[key] for key in (
        'BETA', 'TARGET', 'SOURCES', 'SIZES', 'actual_h', 'slope',
        'cofactor', 'ten_term', 'ideal'))

def coefficients(m,s):
    A=(1+TARGET**m)/2
    hb=actual_h(m,BETA,True)
    hs=actual_h(m,s,False)
    ab,at,ass=slope(m,BETA),slope(m,TARGET),slope(m,s)
    vb=A*ass-hs*at
    vs=A*ab-hb*at
    vt=hb*ass-hs*ab
    cb=vb+(BETA-1)*(A-hs)
    cs=-vs+(1-s)*(A-hb)
    ct=-vt+(1-TARGET)*(hb-hs)
    db=(1-BETA)*vb
    ds=(s-1)*vs
    dt=(TARGET-1)*vt
    c1=(hb-A)*ass+(A-hs)*ab+(hs-hb)*at
    return (cb,cs,ct),(db,ds,dt),c1

def main():
    n=0
    u_ratio_ceiling=Q(0)
    for m in SIZES:
        U=Q(1,2)**(m//2)
        for s in SOURCES:
            cs,ds,c1=coefficients(m,s)
            assert all(abs(v)<5*U for v in cs)
            assert all(abs(v)<=3*U/m for v in ds)
            assert abs(c1)<=6*U/m
            for k in range(2,30):
                E=cofactor(m,k,s)
                assert E==ten_term(m,k,s)
                F=ideal(k,s)
                assert F>20*Q(1,2)**260
                assert abs(E-F)<(Q(18)+Q(9*k+6,m))*U
                assert (Q(18)+Q(9*k+6,m))*U<20*U
                assert E>0
                u_ratio_ceiling=max(u_ratio_ceiling,abs(E-F)/U)
                n+=1
    assert n==336
    print('A113 ALL-K RATIONAL REGRESSION PASS')
    print(f'exact checks: {n}; 4 M values, 3 rational sources, all k=2,...,29')
    print('Checked: A83=A84, coefficient envelopes, analytical proposed remainder cap, strict positivity')
    print('maximum sampled |E-F| / U <',int(u_ratio_ceiling)+1,' (integer ceiling)')
    print('Scope: 336 finite tests, not a universal proof nor a Lean result')

if __name__=='__main__':main()