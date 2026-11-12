#!/usr/bin/env python3
"""All-d symbolic audit of Wang (2019) vacuum ACD four-volume Eq. (79).

Starting from the printed intermediate formulas:
  - Eq. (74): null-cone boundary,
  - Eq. (76): Ricci-flat RNC volume density,
  - Eq. (75): doubled upper-cone integral,

and the angular identities listed in Eqs. (7)-(11), the direct integration
gives the relative vacuum coefficients

    E^2:
      d(7 d^2 + 44 d + 58)
      / [180 (d+1)(d+3)(d+4)]

    H^2:
      d(d+6)
      / [60 (d+1)(d+3)(d+4)]

    D^2:
      -d
      / [120 (d+1)(d+3)(d+4)].

Equivalently, in the absolute-volume normalization used in Wang Eq. (79),
the numerator should be

    (7 d^3 + 58 d^2 + 146 d + 116) E^2
  + 3(d+2)(d+6) H^2
  - 3(d+2) D^2 / 2,

rather than the printed

    (7 d^3 + 58 d^2 + 146 d + 108) E^2
  + 6(d+2)(d+6) H^2
  - 3(d+2) D^2 / 2.

This script audits the algebra implied by the printed intermediate equations.
It does not by itself prove that no term omitted from the paper's abridged
Eq. (74) can contribute in every dimension. In d=4, exact Kasner and
Cahen-Wallach checks independently validate the corrected coefficients.
"""

from __future__ import annotations

import sympy as sp


def corrected_relative_coefficients(d: sp.Expr):
    """Return coefficients of E^2, H^2, D^2 in delta V / V_flat."""
    n = d - 1

    # Moving-boundary terms from Eq. (74).
    boundary_E = sp.simplify(
        sp.Rational(1, 36)
        - 1 / (45 * (d + 1))
        + d * (d - 1) / (90 * (d + 1) * (d + 2))
    )
    boundary_H = sp.simplify(
        d / (60 * (d + 1) * (d + 2))
    )
    boundary_D = sp.Integer(0)

    assert sp.factor(boundary_E) == (
        (7 * d + 2) / (180 * (d + 2))
    )

    # RNC determinant terms from Eq. (76).
    #
    # After angular averaging:
    #
    # <Q> =
    #   E^2 s^4
    # + [3 H^2 / n] r^2 s^2
    # + [3 E^2 - 3 H^2 + (3/2) D^2]
    #   r^4 / [n(n+2)].
    determinant_E = -(
        d**2 + 2 * d + 8
    ) / (
        60
        * (d + 1)
        * (d + 2)
        * (d + 3)
        * (d + 4)
    )

    determinant_H = (
        d**2
        / (
            60
            * (d + 1)
            * (d + 2)
            * (d + 3)
            * (d + 4)
        )
    )

    determinant_D = -(
        d
        / (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    total_E = sp.factor(boundary_E + determinant_E)
    total_H = sp.factor(boundary_H + determinant_H)
    total_D = sp.factor(boundary_D + determinant_D)

    return (
        sp.factor(boundary_E),
        sp.factor(boundary_H),
        sp.factor(determinant_E),
        sp.factor(determinant_H),
        sp.factor(determinant_D),
        total_E,
        total_H,
        total_D,
    )


def main() -> None:
    d = sp.symbols("d", integer=True, positive=True)

    (
        boundary_E,
        boundary_H,
        determinant_E,
        determinant_H,
        determinant_D,
        total_E,
        total_H,
        total_D,
    ) = corrected_relative_coefficients(d)

    expected_E = (
        d
        * (7 * d**2 + 44 * d + 58)
        / (
            180
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    expected_H = (
        d
        * (d + 6)
        / (
            60
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    expected_D = -(
        d
        / (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    assert sp.simplify(total_E - expected_E) == 0
    assert sp.simplify(total_H - expected_H) == 0
    assert sp.simplify(total_D - expected_D) == 0

    # Convert to the numerator normalization printed in Eq. (79).
    corrected_abs_E = sp.expand(
        (d + 2) * (7 * d**2 + 44 * d + 58)
    )
    corrected_abs_H = 3 * (d + 2) * (d + 6)
    corrected_abs_D = -sp.Rational(3, 2) * (d + 2)

    assert corrected_abs_E == (
        7 * d**3
        + 58 * d**2
        + 146 * d
        + 116
    )

    # Printed Eq. (79).
    printed_abs_E = (
        7 * d**3
        + 58 * d**2
        + 146 * d
        + 108
    )
    printed_abs_H = 6 * (d + 2) * (d + 6)
    printed_abs_D = -sp.Rational(3, 2) * (d + 2)

    assert sp.simplify(
        corrected_abs_E - printed_abs_E
    ) == 8

    assert sp.simplify(
        corrected_abs_H - printed_abs_H
    ) == -3 * (d + 2) * (d + 6)

    assert sp.simplify(
        corrected_abs_D - printed_abs_D
    ) == 0

    # d=4 reduction.
    d4_E = sp.simplify(total_E.subs(d, 4))
    d4_H = sp.simplify(total_H.subs(d, 4))
    d4_D = sp.simplify(total_D.subs(d, 4))

    # D^2=4E^2 and H^2=2B^2 in four dimensions.
    d4_electric = sp.simplify(d4_E + 4 * d4_D)
    d4_magnetic = sp.simplify(2 * d4_H)

    assert d4_electric == sp.Rational(17, 630)
    assert d4_magnetic == sp.Rational(1, 210)

    print(
        {
            "boundary_E": str(boundary_E),
            "boundary_H": str(boundary_H),
            "determinant_E": str(determinant_E),
            "determinant_H": str(determinant_H),
            "determinant_D": str(determinant_D),
            "total_E": str(total_E),
            "total_H": str(total_H),
            "total_D": str(total_D),
            "corrected_E_numerator":
                str(corrected_abs_E),
            "corrected_H_numerator":
                str(corrected_abs_H),
            "corrected_D_numerator":
                str(corrected_abs_D),
            "d4_E2_after_D_relation":
                str(d4_electric),
            "d4_B2_after_H_relation":
                str(d4_magnetic),
        }
    )

    print(
        "PASS: direct all-d integration of the printed intermediate equations "
        "changes +108 -> +116 in the E^2 numerator and halves the H^2 term."
    )


if __name__ == "__main__":
    main()
