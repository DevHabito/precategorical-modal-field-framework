#!/usr/bin/env python3
"""Exact world-function cross-normalization audit in the symmetric d=4 plane wave.

For the Ricci-flat symmetric plane wave with transverse Jacobi channels

    B1(r) = sin(omega r)/omega,
    B2(r) = sinh(omega r)/omega,

the two null sheets admit exact world-function defining functions.

Writing x=u/U, z=omega U and phi for the transverse ellipse angle, the exact
world-function cross-normalization ratio is

    chi/chi0
      = x(1-x) [a_z(x) cos^2(phi) + b_z(x) sin^2(phi)],

where

    a_z = z sin(z) / [sin(zx) sin(z(1-x))],
    b_z = z sinh(z) / [sinh(zx) sinh(z(1-x))].

This checker expands q=log(chi/chi0) through z^4 and performs the flat-edge
angular average exactly.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    z, x, c = sp.symbols("z x c", real=True)

    a = (
        z
        * sp.sin(z)
        / (
            sp.sin(z * x)
            * sp.sin(z * (1 - x))
        )
    )

    b = (
        z
        * sp.sinh(z)
        / (
            sp.sinh(z * x)
            * sp.sinh(z * (1 - x))
        )
    )

    a_series = sp.series(a, z, 0, 6).removeO()
    b_series = sp.series(b, z, 0, 6).removeO()

    # c = cos^2(phi).
    chi_ratio = sp.series(
        x
        * (1 - x)
        * (
            a_series * c
            + b_series * (1 - c)
        ),
        z,
        0,
        6,
    ).removeO()

    q = sp.series(
        sp.log(chi_ratio),
        z,
        0,
        6,
    ).removeO().expand()

    q2 = sp.factor(q.coeff(z, 2))
    q4 = sp.factor(q.coeff(z, 4))

    expected_q2 = (
        -x
        * (1 - x)
        * (2 * c - 1)
        / 3
    )

    assert sp.simplify(q2 - expected_q2) == 0

    # phi average:
    # <cos^2 phi> = 1/2,
    # <cos^4 phi> = 3/8.
    q4_poly = sp.Poly(
        sp.expand(q4),
        c,
    )

    q4_phi_average = sp.expand(
        q4_poly.coeff_monomial(c**2)
        * sp.Rational(3, 8)
        +
        q4_poly.coeff_monomial(c)
        * sp.Rational(1, 2)
        +
        q4_poly.coeff_monomial(1)
    )

    q4_edge_average = sp.simplify(
        sp.integrate(
            q4_phi_average,
            (x, 0, 1),
        )
    )

    assert (
        q4_edge_average
        ==
        -sp.Rational(13, 5400)
    )

    # In the plane wave:
    # E^2 = B^2 = omega^4/2,
    # U = sqrt(2) L,
    # z^4 = 4 omega^4 L^4.
    invariant_sum_coefficient = sp.simplify(
        4 * q4_edge_average
    )

    assert (
        invariant_sum_coefficient
        ==
        -sp.Rational(13, 1350)
    )

    print(
        {
            "q_z2": str(q2),
            "mean_q_z4": str(q4_edge_average),
            "type_N_coefficient_for_(E2+B2)L4":
                str(invariant_sum_coefficient),
        }
    )

    print(
        "PASS: exact plane-wave world-function cross-normalization "
        "gives <q2> = -13 z^4 / 5400."
    )


if __name__ == "__main__":
    main()
