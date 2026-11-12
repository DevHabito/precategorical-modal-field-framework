#!/usr/bin/env python3
"""Symbolic regression for the d=4 comparable-twin asymptotic theorem.

Checks:
- exact joint-coordinate polynomial for Delta;
- first-order coefficients c_A and c_B;
- algebraic identities used in the positivity argument;
- analytic constants J_step=2*pi/3, J_Laplace=4*pi,
  F-tail coefficient=3*pi, and twin coefficient=9*pi.

This is a symbolic regression of the algebra.  It is not a substitute for the
measure-theoretic dominated-convergence argument in the theorem note.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    alpha, beta, A, B, u = sp.symbols(
        "alpha beta A B u", nonnegative=True, real=True
    )

    ax = alpha
    bx = beta + B
    ay = alpha + A
    by = beta

    px = ax * (2 - bx)
    py = ay * (2 - by)
    xq = bx * (2 - ax)
    yq = by * (2 - ay)

    # In d=4 and cap coordinate u:
    # tau(x,y)^2 = A B (1-u).
    xy = A * B * (1 - u)

    delta_exact = sp.expand(
        (py**2 - px**2 + xq**2 - yq**2 - 2 * xy**2) / 16
    )

    delta_expected = sp.expand(
        sp.Rational(1, 2) * alpha * A
        + sp.Rational(1, 4) * A**2
        + sp.Rational(1, 2) * beta * B
        + sp.Rational(1, 4) * B**2
        + sp.Rational(1, 4) * alpha**2 * B
        - sp.Rational(1, 2) * alpha * beta * A
        - sp.Rational(1, 2) * alpha * beta * B
        - sp.Rational(1, 4) * alpha * B**2
        + sp.Rational(1, 4) * beta**2 * A
        - sp.Rational(1, 4) * beta * A**2
        - sp.Rational(1, 8) * (1 - u) ** 2 * A**2 * B**2
    )

    assert sp.simplify(delta_exact - delta_expected) == 0

    cA = sp.simplify(sp.diff(delta_exact, A).subs({A: 0, B: 0}))
    cB = sp.simplify(sp.diff(delta_exact, B).subs({A: 0, B: 0}))

    expected_cA = (2 * alpha - 2 * alpha * beta + beta**2) / 4
    expected_cB = (alpha**2 - 2 * alpha * beta + 2 * beta) / 4

    assert sp.simplify(cA - expected_cA) == 0
    assert sp.simplify(cB - expected_cB) == 0

    # For beta >= 1, the minimum of 4*cA over
    # 0 <= alpha <= 2-beta occurs at alpha=2-beta.
    boundary_cA = sp.expand(
        (4 * expected_cA).subs(alpha, 2 - beta)
    )
    assert sp.simplify(boundary_cA - (3 * (beta - 1) ** 2 + 1)) == 0

    # Symmetric statement for 4*cB.
    boundary_cB = sp.expand(
        (4 * expected_cB).subs(beta, 2 - alpha)
    )
    assert sp.simplify(boundary_cB - (3 * (alpha - 1) ** 2 + 1)) == 0

    g1, g2 = sp.symbols("g1 g2", nonnegative=True, real=True)

    # Dirichlet-simplex evaluation:
    # 1/4 * int_{g1+g2<=4} sqrt(g1*g2) dg1 dg2.
    j_step = (
        sp.Rational(1, 4)
        * 4**3
        * sp.gamma(sp.Rational(3, 2)) ** 2
        / sp.gamma(4)
    )
    assert sp.simplify(j_step - 2 * sp.pi / 3) == 0

    one_laplace = (
        sp.Rational(1, 2)
        * sp.gamma(sp.Rational(3, 2))
        * 4 ** sp.Rational(3, 2)
    )
    j_laplace = sp.simplify(one_laplace**2)
    assert sp.simplify(j_laplace - 4 * sp.pi) == 0

    k_oriented = sp.Rational(9, 4)
    f_tail = sp.simplify(2 * k_oriented * j_step)
    twin_coefficient = sp.simplify(k_oriented * j_laplace)

    assert sp.simplify(f_tail - 3 * sp.pi) == 0
    assert sp.simplify(twin_coefficient - 9 * sp.pi) == 0

    print("PASS: exact Delta polynomial")
    print("PASS: first-order coefficients")
    print("PASS: positivity boundary identities")
    print("PASS: J_step =", j_step)
    print("PASS: J_Laplace =", j_laplace)
    print("PASS: F4 tail coefficient =", f_tail)
    print("PASS: twin expectation coefficient =", twin_coefficient)


if __name__ == "__main__":
    main()
