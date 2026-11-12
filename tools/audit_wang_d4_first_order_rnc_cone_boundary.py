#!/usr/bin/env python3
"""Generic first-order RNC audit of the ACD null-cone boundary in d=4 vacuum.

Purpose
-------
Check whether the "abridged" null-cone boundary used in Wang (2019), Eq. (74),
could have dropped a linear magnetic-Weyl term whose square later contributes
at O(C^2 L^4).

Result
------
For a generic four-dimensional Weyl tensor decomposed into electric and
magnetic STF tensors E_ij and B_ij, the first-curvature correction to Synge's
world function between a tip p=(-L,0) and x=(t,r n) is

    delta(2 sigma) = -(1/3) L^2 r^2 E_nn.

All linear B terms cancel identically. Therefore

    r_-(t,n)
      = (L+t) [1 + (1/6) L^2 E_nn] + O(C^2),

and similarly

    r_+(t,n)
      = (L-t) [1 + (1/6) L^2 E_nn] + O(C^2).

So the missing B^2 discrepancy cannot be explained by squaring an omitted
linear magnetic term in the abridged cone radius.
"""

from __future__ import annotations

import sympy as sp


def levi(i: int, j: int, k: int) -> sp.Expr:
    return sp.LeviCivita(i, j, k)


def main() -> None:
    L, t, r = sp.symbols("L t r", real=True)
    n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)

    e11, e22, e12, e13, e23 = sp.symbols(
        "e11 e22 e12 e13 e23",
        real=True,
    )
    b11, b22, b12, b13, b23 = sp.symbols(
        "b11 b22 b12 b13 b23",
        real=True,
    )

    e33 = -e11 - e22
    b33 = -b11 - b22

    E = [
        [e11, e12, e13],
        [e12, e22, e23],
        [e13, e23, e33],
    ]
    B = [
        [b11, b12, b13],
        [b12, b22, b23],
        [b13, b23, b33],
    ]

    C: dict[tuple[int, int, int, int], sp.Expr] = {}

    def setc(a: int, b: int, c: int, d: int, value: sp.Expr) -> None:
        C[(a, b, c, d)] = sp.expand(value)

    # C_{0i0j} = E_ij.
    for i in range(3):
        for j in range(3):
            value = E[i][j]
            setc(0, i + 1, 0, j + 1, value)
            setc(i + 1, 0, 0, j + 1, -value)
            setc(0, i + 1, j + 1, 0, -value)
            setc(i + 1, 0, j + 1, 0, value)

    # C_{0ijk} = eps_{jkm} B_{im}; overall magnetic sign convention is
    # irrelevant to this cancellation test.
    for i in range(3):
        for j in range(3):
            for k in range(3):
                value = sum(
                    levi(j, k, m) * B[i][m]
                    for m in range(3)
                )

                assignments = [
                    ((0, i + 1, j + 1, k + 1), +1),
                    ((i + 1, 0, j + 1, k + 1), -1),
                    ((0, i + 1, k + 1, j + 1), -1),
                    ((i + 1, 0, k + 1, j + 1), +1),
                    ((j + 1, k + 1, 0, i + 1), +1),
                    ((k + 1, j + 1, 0, i + 1), -1),
                    ((j + 1, k + 1, i + 1, 0), -1),
                    ((k + 1, j + 1, i + 1, 0), +1),
                ]

                for indices, sign in assignments:
                    setc(*indices, sign * value)

    # Four-dimensional vacuum spatial Weyl sector.
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for ell in range(3):
                    value = -sum(
                        levi(i, j, m)
                        * levi(k, ell, q)
                        * E[m][q]
                        for m in range(3)
                        for q in range(3)
                    )
                    setc(
                        i + 1,
                        j + 1,
                        k + 1,
                        ell + 1,
                        value,
                    )

    n = [n1, n2, n3]

    delta = [
        t + L,
        r * n1,
        r * n2,
        r * n3,
    ]

    midpoint = [
        (t - L) / 2,
        r * n1 / 2,
        r * n2 / 2,
        r * n3 / 2,
    ]

    contraction = sp.Integer(0)

    for (mu, alpha, nu, beta), value in C.items():
        contraction += (
            value
            * delta[mu]
            * delta[nu]
            * midpoint[alpha]
            * midpoint[beta]
        )

    contraction = sp.factor(sp.expand(contraction))

    e_nn = sp.expand(
        sum(
            E[i][j] * n[i] * n[j]
            for i in range(3)
            for j in range(3)
        )
    )

    expected = L**2 * r**2 * e_nn

    assert sp.simplify(contraction - expected) == 0

    # First-curvature world-function expansion:
    #
    # 2 sigma = eta(delta,delta) - (1/3) contraction + O(C^2).
    #
    # Put r=(L+t)(1+alpha), alpha=O(C), and solve.
    alpha = sp.symbols("alpha")
    r0 = L + t

    equation = sp.expand(
        (r0 * (1 + alpha)) ** 2
        - r0**2
        - sp.Rational(1, 3)
        * L**2
        * (r0**2)
        * e_nn
    )

    linear = sp.expand(equation).coeff(alpha, 1)
    constant = sp.expand(equation).subs(alpha, 0)

    alpha_solution = sp.simplify(-constant / linear)

    assert alpha_solution == L**2 * e_nn / 6

    print(
        {
            "world_function_curvature_contraction":
                "L^2 r^2 E_nn",
            "linear_B_terms":
                "cancel identically",
            "past_cone_radius":
                "(L+t) [1 + L^2 E_nn/6] + O(C^2)",
            "future_cone_radius":
                "(L-t) [1 + L^2 E_nn/6] + O(C^2)",
        }
    )

    print(
        "PASS: generic first-order RNC cone boundary contains only E_nn; "
        "the d=4 B^2 discrepancy must originate at genuine second order."
    )


if __name__ == "__main__":
    main()
