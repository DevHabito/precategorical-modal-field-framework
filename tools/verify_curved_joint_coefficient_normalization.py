#!/usr/bin/env python3
"""Symbolic normalization audit for the curved null-joint coefficient.

Checks:
1. invariance under independent optical rescalings
       a' = lambda a, b' = mu b;
2. exact reduction of the curved d=4 edge formula to
       C_4 = 3*pi, K_4 = 9*pi
   for the unit Minkowski Alexandrov interval.

This is a regression/audit, not a substitute for the analytic proof.
"""

from __future__ import annotations

import sympy as sp


def optical_invariance() -> None:
    d = sp.symbols("d", positive=True)
    m = d / 2
    a_m = 1 + 2 / d

    # A_d contains Omega^(d+2).
    # Under a'=lambda a, b'=mu b:
    # Omega'^2 = Omega^2/(lambda*mu).
    prefactor_power = -(d + 2) / 2

    # c_+'=c_+ lambda^(-m), c_-'=c_- mu^(-m).
    # Since S_d contains c_+^(-a_m)c_-^(-a_m),
    # each side contributes m*a_m.
    scalar_power = sp.simplify(m * a_m)

    total = sp.simplify(prefactor_power + scalar_power)

    print("optical prefactor exponent:", prefactor_power)
    print("optical scalar exponent:   ", scalar_power)
    print("total exponent:            ", total)

    assert total == 0


def flat_d4_reduction() -> None:
    pi = sp.pi

    d = sp.Integer(4)
    m = d / 2
    a_m = 1 + sp.Rational(2, d)

    # Unit diamond p=(-1,0), q=(1,0):
    # V_4 = pi*T^4/24 with T=2.
    V_D = sp.Rational(2, 3) * pi

    # In null-waist coordinates:
    # ds^2 has |cross coefficient| corresponding to Omega^2=1/2.
    Omega_sq = sp.Rational(1, 2)
    Omega = sp.sqrt(Omega_sq)

    omega_dminus2 = pi  # area of Euclidean unit 2-ball
    edge_area = 4 * pi  # S^2

    A_density = sp.simplify(
        omega_dminus2
        * 2 ** (m - 1)
        * Omega ** (d + 2)
        / V_D**2
    )

    A_integrated = sp.simplify(A_density * edge_area)

    # Near the flat null joint:
    # V(p,x)/V_D ~ (1/4) a^2, same for the other side.
    c_plus = sp.Rational(1, 4)
    c_minus = sp.Rational(1, 4)

    # For m=2, L_m = 1/3.
    L_m = sp.Rational(1, 3)

    S = sp.simplify(
        (a_m * L_m) ** 2
        * c_plus ** (-a_m)
        * c_minus ** (-a_m)
        * sp.gamma(a_m) ** 2
        / sp.gamma(2 * a_m + 1)
    )

    C4 = sp.simplify(2 * A_integrated * S)
    K4 = sp.simplify(sp.Rational(1, 2) * C4 * sp.gamma(4))

    print("A_density:     ", A_density)
    print("A_integrated:  ", A_integrated)
    print("S_scalar:      ", S)
    print("C4:            ", C4)
    print("K4:            ", K4)

    assert sp.simplify(C4 - 3 * pi) == 0
    assert sp.simplify(K4 - 9 * pi) == 0


def main() -> None:
    optical_invariance()
    flat_d4_reduction()
    print("PASS: curved coefficient normalization audit.")


if __name__ == "__main__":
    main()
