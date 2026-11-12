#!/usr/bin/env python3
"""Derive the d=3 first curvature response as exact bulk integrals.

The calculation uses a spatially-flat FLRW calibration family and the exact
Minkowski moment tensors of weighted Alexandrov subintervals.

It reduces the relative response

    K_3(g,L)/K_3(Mink)
      = 1 + L^2 [alpha_3 R + gamma_3 R_TT] + o(L^2)

to two explicit convergent integrals over

    s in (0,2), w in (-1,1),

where
    u = s(1+w)/2,
    v = s(1-w)/2.

The script evaluates those integrals with tensor-product Gauss-Legendre
quadrature.  No closed form for alpha_3 or gamma_3 is assumed.

SymPy is used only to generate the perturbation algebra; NumPy performs the
quadrature.
"""

from __future__ import annotations

import argparse
import numpy as np
import sympy as sp


def build_integrands():
    u, v = sp.symbols(
        "u v",
        positive=True,
        real=True,
    )

    h, k = sp.symbols(
        "h k",
        real=True,
    )

    s, w = sp.symbols(
        "s w",
        positive=True,
        real=True,
    )

    t = (u**2 - v**2) / 4

    cross = (
        4 - u**2 - v**2
    ) / (2 * u * v)

    def norm_bilinear(f, g):
        fu = sp.diff(f, u)
        fv = sp.diff(f, v)
        gu = sp.diff(g, u)
        gv = sp.diff(g, v)

        return sp.expand(
            fu * gu
            +
            fv * gv
            -
            cross
            * (
                fu * gv
                +
                fv * gu
            )
        )

    # Common Minkowski interval-volume factor pi/12 is omitted.
    # It cancels from all relative norm variations.
    psi0 = u**3 - v**3

    # First time moment of a 2+1 Alexandrov interval:
    # M1 = V * midpoint_time.
    m1_p = (
        u**3
        * (t - 1)
        / 2
    )

    m1_f = (
        v**3
        * (t + 1)
        / 2
    )

    psi1 = (
        3 * h
        * (m1_p - m1_f)
    )

    # Second time moment:
    #
    # M2/V
    #   = midpoint_time^2
    #     - 3 tau^2/80
    #     + Delta_t^2/16.
    m2_p = u**3 * (
        (t - 1) ** 2 / 4
        -
        sp.Rational(3, 80) * u**2
        +
        (1 + t) ** 2 / 16
    )

    m2_f = v**3 * (
        (t + 1) ** 2 / 4
        -
        sp.Rational(3, 80) * v**2
        +
        (1 - t) ** 2 / 16
    )

    q0 = (
        -sp.Rational(3, 2)
        * h**2
    )

    q2 = (
        sp.Rational(3, 2)
        * (
            k
            +
            2 * h**2
        )
    )

    psi2 = (
        q0 * psi0
        +
        q2 * (m2_p - m2_f)
    )

    s0 = norm_bilinear(
        psi0,
        psi0,
    )

    s1 = (
        2
        * norm_bilinear(
            psi0,
            psi1,
        )
    )

    s2 = (
        2
        * norm_bilinear(
            psi0,
            psi2,
        )
        +
        norm_bilinear(
            psi1,
            psi1,
        )
    )

    r1 = sp.simplify(
        s1 / s0
    )

    r2 = sp.simplify(
        s2 / s0
    )

    # Physical conformal metric factor A^6.
    a1 = 6 * h * t

    a2 = (
        -3 * h**2
        +
        (
            3 * k
            +
            15 * h**2
        )
        * t**2
    )

    # Expansion of
    # A^6 * S^(-3/2).
    b2 = sp.simplify(
        a2
        -
        sp.Rational(3, 2)
        * r2
        +
        sp.Rational(15, 8)
        * r1**2
        -
        sp.Rational(3, 2)
        * a1 * r1
    )

    substitution = {
        u: s * (1 + w) / 2,
        v: s * (1 - w) / 2,
    }

    b2_sw = sp.simplify(
        b2.subs(substitution)
    )

    b2_k = sp.simplify(
        sp.diff(
            b2_sw,
            k,
        )
    )

    b2_h2 = sp.simplify(
        sp.diff(
            b2_sw,
            h,
            2,
        ) / 2
    )

    denominator = (
        4 * (1 - w**2)
        +
        s**2
        * w**2
        * (w**2 + 3)
    )

    base = (
        (1 - w**2)
        /
        denominator ** sp.Rational(3, 2)
    )

    return (
        sp.lambdify(
            (s, w),
            base,
            "numpy",
        ),
        sp.lambdify(
            (s, w),
            base * b2_k,
            "numpy",
        ),
        sp.lambdify(
            (s, w),
            base * b2_h2,
            "numpy",
        ),
    )


def integrate_tensor_product(
    function,
    order: int,
) -> float:
    nodes, weights = (
        np.polynomial.legendre.leggauss(
            order
        )
    )

    # s: [-1,1] -> [0,2].
    s = nodes + 1.0
    ws = weights

    # w remains on [-1,1].
    w = nodes
    ww = weights

    S, W = np.meshgrid(
        s,
        w,
        indexing="ij",
    )

    values = function(
        S,
        W,
    )

    return float(
        np.sum(
            ws[:, None]
            * ww[None, :]
            * values
        )
    )


def evaluate(
    order: int,
):
    base, ik, ih = build_integrands()

    i0 = integrate_tensor_product(
        base,
        order,
    )

    ik_value = integrate_tensor_product(
        ik,
        order,
    )

    ih_value = integrate_tensor_product(
        ih,
        order,
    )

    # Z = V0 [1 + L^2 z2],
    # z2 = 3 k/20 - 6 h^2/5.
    coeff_k = (
        3.0 / 20.0
        +
        ik_value / i0
    )

    coeff_h2 = (
        -6.0 / 5.0
        +
        ih_value / i0
    )

    # In 2+1 spatially-flat FLRW:
    #
    # R    = 4 k - 2 h^2,
    # R_TT = -2 k + 2 h^2.
    #
    # Thus:
    # coeff_k  = 4 alpha - 2 gamma
    # coeff_h2 = -2 alpha + 2 gamma.
    alpha3 = (
        coeff_k
        +
        coeff_h2
    ) / 2.0

    gamma3 = (
        coeff_h2 / 2.0
        +
        alpha3
    )

    return {
        "order": order,
        "base_integral": i0,
        "coeff_k": coeff_k,
        "coeff_h2": coeff_h2,
        "alpha3": alpha3,
        "gamma3": gamma3,
    }


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--orders",
        default="100,200,400,800",
    )

    args = parser.parse_args()

    orders = [
        int(part.strip())
        for part
        in args.orders.split(",")
        if part.strip()
    ]

    for order in orders:
        result = evaluate(order)

        print(result)

    print(
        "Reference flat base integral: pi/8 =",
        float(np.pi / 8.0),
    )

    print(
        "No closed form is asserted for alpha3 or gamma3."
    )


if __name__ == "__main__":
    main()
