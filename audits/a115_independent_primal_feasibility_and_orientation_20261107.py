#!/usr/bin/env python3
"""Exact checks of P-support feasibility and two-band determinant orientation.

No floating-point comparisons. The results test precise algebraic statements;
they do not prove all remaining LP bands or dual optimality.
"""
from fractions import Fraction as F


def p_masses(M, k, t, z):
    return t / 2 - F(M-k, M) * z, z, t / 2 - F(k, M) * z


def exact_p_feasibility():
    cases = 0
    outside = 0
    for M in range(4, 121):
        for k in range(1, M):
            for t in (F(0), F(1, 3), F(1), F(2)):
                zmax = min(F(M, 2 * (M-k)) * t, F(M, 2*k) * t)
                for z in (-F(1, 1000), F(0), zmax/2, zmax, zmax+F(1, 1000)):
                    p0, zi, pM = p_masses(M, k, t, z)
                    actual = p0 >= 0 and zi >= 0 and pM >= 0
                    linear = (zi >= 0 and 2 * (M-k) * zi <= M*t
                              and 2 * k * zi <= M*t)
                    interval = (0 <= zi <= zmax)
                    assert actual == linear == interval, (M,k,t,z)
                    assert p0+zi+pM == t
                    assert k*zi+M*pM == F(M,2)*t
                    cases += 1
                    outside += not actual
    return cases, outside


def exact_orientation_tests():
    # Two active band equations:
    # Bb*z+Hb*t=Cb and Bs*z+Hs*t=Cs.
    # The next contact replaces Bb with Bb+Db and Bs with Bs+Ds.
    count = 0
    neg_z_count = 0
    pos_z_count = 0
    for Hb in (F(1), F(3, 2)):
        for Hs in (F(1), F(2)):
            for Cb in (F(1), F(2), F(3)):
                for Cs in (F(1), F(2), F(3)):
                    Z = Cb*Hs-Cs*Hb
                    if Z==0:
                        continue
                    for Bb in (F(-2), F(1), F(2)):
                        for Bs in (F(-3), F(1), F(3)):
                            D = Bb*Hs-Bs*Hb
                            if D==0:
                                continue
                            for Db, Ds in ((F(1, 2), F(1, 4)),(F(-1),F(1,3)),(F(1),F(-2))):
                                Dnext=(Bb+Db)*Hs-(Bs+Ds)*Hb
                                if Dnext==0:
                                    continue
                                z=Z/D
                                znext=Z/Dnext
                                if z<=0 or znext<=0:
                                    continue
                                t=(Bb*Cs-Bs*Cb)/D
                                tnext=((Bb+Db)*Cs-(Bs+Ds)*Cb)/Dnext
                                assert Bb*z+Hb*t==Cb
                                assert Bs*z+Hs*t==Cs
                                assert (Bb+Db)*znext+Hb*tnext==Cb
                                assert (Bs+Ds)*znext+Hs*tnext==Cs
                                assert D*Dnext>0
                                assert (D<0 and Dnext<0) if Z<0 else (D>0 and Dnext>0)
                                count+=1
                                neg_z_count += Z<0
                                pos_z_count += Z>0
    assert count and neg_z_count and pos_z_count
    return count,neg_z_count,pos_z_count


if __name__=="__main__":
    total,outside=exact_p_feasibility()
    print(f"PASS: {total} exact P feasibility / endpoint / mass / mean controls; {outside} deliberately infeasible")
    total,negative,positive=exact_orientation_tests()
    print(f"PASS: {total} exact two-band determinant-orientation controls; Z<0: {negative}; Z>0: {positive}")
