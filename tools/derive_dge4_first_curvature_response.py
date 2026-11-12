#!/usr/bin/env python3
"""Symbolic derivation of the first curvature response for d >= 4.

The derivation uses a spatially-flat FLRW metric in conformal time,

    g = A(eta)^2 eta_Mink,

with
    A(0)=1,
    A'(0)=h,
    A''(0)=k.

After centering a proper-time diamond of half-duration L and mapping its
conformal-coordinate diamond to the unit Minkowski diamond, the sprinkling
weight is expanded to O(L^2).

For the null-joint coefficient, the exact weighted-Minkowski ratio is

 K[w]/K[1]
   = w(0)^2
     <w>_-^{-a_m}
     <w>_+^{-a_m}
     <w>_D^{2 a_m - 2},

where the null averages use a Beta(m,m) kernel and
a_m = 1 + 2/d.

The script derives the relative curvature coefficients alpha_d, beta_d in

 K_g(D_L)/K_Mink
   = 1 + L^2 [alpha_d R + beta_d R_TT] + o(L^2),

for fixed d >= 4.

This is an algebraic regression of the analytic derivation.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    d = sp.symbols(
        "d",
        positive=True,
    )

    h, k = sp.symbols(
        "h k",
        real=True,
    )

    a_m = 1 + 2 / d

    # Unit-diamond Minkowski time moments.
    mean_t2_diamond = (
        sp.Integer(2)
        /
        ((d + 1) * (d + 2))
    )

    # Thin-null Beta(m,m) kernel, m=d/2.
    mean_t2_null = (
        (d + 2)
        /
        (4 * (d + 1))
    )

    # Centered proper-time diamond mapped to unit conformal diamond:
    #
    # A(eta)^d
    # = 1 + p L t + L^2(q0 + q2 t^2) + O(L^3).
    p = d * h

    q0 = -d * h**2 / 2

    q2 = (
        d
        * (
            k
            +
            (d - 1) * h**2
        )
        / 2
    )

    # In log K, q0 cancels exactly because a constant conformal rescaling
    # cannot change the normalized sprinkling experiment.
    coeff = sp.simplify(
        -2
        * a_m
        * q2
        * mean_t2_null
        +
        a_m
        * p**2
        / 4
        +
        (2 * a_m - 2)
        * q2
        * mean_t2_diamond
    )

    coeff = sp.factor(coeff)

    # Spatially-flat FLRW curvature invariants at A(0)=1.
    R = (
        (d - 1)
        * (
            2 * k
            +
            (d - 4) * h**2
        )
    )

    R_TT = (
        -(d - 1)
        * (
            k
            -
            h**2
        )
    )

    alpha, beta = sp.symbols(
        "alpha beta",
    )

    solved = sp.solve(
        [
            sp.Eq(
                sp.expand(
                    alpha * R
                    +
                    beta * R_TT
                ).coeff(k),
                sp.expand(coeff).coeff(k),
            ),
            sp.Eq(
                sp.expand(
                    alpha * R
                    +
                    beta * R_TT
                ).coeff(h**2),
                sp.expand(coeff).coeff(h**2),
            ),
        ],
        [alpha, beta],
        simplify=True,
    )

    alpha_d = sp.factor(
        solved[alpha]
    )

    beta_d = sp.factor(
        solved[beta]
    )

    expected_alpha = (
        -d
        * (d + 6)
        /
        (
            4
            * (d - 1)
            * (d + 1)
            * (d + 2)
        )
    )

    expected_beta = (
        (
            d**2
            +
            2 * d
            -
            4
        )
        /
        (
            4
            * (d - 1)
            * (d + 1)
        )
    )

    assert (
        sp.simplify(
            alpha_d
            -
            expected_alpha
        )
        ==
        0
    )

    assert (
        sp.simplify(
            beta_d
            -
            expected_beta
        )
        ==
        0
    )

    print(
        "log(K/K0) coefficient in h,k:"
    )

    print(coeff)

    print(
        "alpha_d =",
        alpha_d,
    )

    print(
        "beta_d =",
        beta_d,
    )

    for value in (
        4,
        5,
        6,
        8,
        10,
    ):
        print(
            {
                "d": value,
                "alpha_d":
                    sp.simplify(
                        alpha_d.subs(
                            d,
                            value,
                        )
                    ),
                "beta_d":
                    sp.simplify(
                        beta_d.subs(
                            d,
                            value,
                        )
                    ),
            }
        )

    print(
        "PASS: first curved d>=4 response coefficients derived symbolically."
    )


if __name__ == "__main__":
    main()
