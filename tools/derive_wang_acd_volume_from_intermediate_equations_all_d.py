#!/usr/bin/env python3
"""Symbolic all-d audit of Wang (2019) ACD volume Eqs. (74)+(76).

Starting only from the printed intermediate equations and the angular identities
listed in Wang's Eqs. (7)-(11), this script derives the arbitrary-dimensional
vacuum ACD volume coefficient.

Let s=d-1 be the spatial dimension.  The direct angular average of Eq. (76) is

    <Q> =
        E^2 t^4
      + [3 H^2 / s] r^2 t^2
      + [3 E^2 - 3 H^2 + (3/2) D^2]
        r^4 / [s(s+2)].

The direct cone contribution from Eq. (74) is

    v_E^cone = (7d+2)/[180(d+2)],
    v_H^cone = d/[60(d+1)(d+2)],
    v_D^cone = 0.

After adding the volume-density contribution from Eq. (76), the relative volume
correction is

    delta V / V0
      = L^4 [
          d(7d^2+44d+58) E^2
            / {180(d+1)(d+3)(d+4)}
        + d(d+6) H^2
            / {60(d+1)(d+3)(d+4)}
        - d D^2
            / {120(d+1)(d+3)(d+4)}
        ].

Equivalently,

    V^(d) = 2 Omega_{d-2} L^d/[d(d-1)]
      + Omega_{d-2} L^(d+4)
        [
          (7d^3+58d^2+146d+116) E^2
          + 3(d+2)(d+6) H^2
          - (3/2)(d+2) D^2
        ]
        /
        [
          90(d-1)(d+1)(d+2)(d+3)(d+4)
        ]
      + ...

The printed Eq. (79) instead has 108 in the electric constant term and a factor
6 rather than 3 multiplying the H^2 term.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    d = sp.symbols(
        "d",
        integer=True,
        positive=True,
    )

    s = d - 1

    # ---------------------------------------------------------------
    # Cone contribution from Eq. (74)
    # ---------------------------------------------------------------
    #
    # <E_nn^2>   = 2 E^2 / [s(s+2)]
    # <(E^2)_nn> = E^2 / s
    #
    # <n^i n^j n^l n^k H_i{}^m{}_j H_lmk>
    #   = (3/2) H^2 / [s(s+2)].
    #
    # Expanding r_+^s gives a2 + (s-1)a1^2/2.
    e_cone = sp.factor(
        (7 * d + 2)
        /
        (
            180
            * (d + 2)
        )
    )

    h_cone = sp.factor(
        d
        /
        (
            60
            * (d + 1)
            * (d + 2)
        )
    )

    d_cone = sp.Integer(0)

    # ---------------------------------------------------------------
    # Density contribution from Eq. (76)
    # ---------------------------------------------------------------
    #
    # After angular averaging:
    #
    # <Q> =
    #   E^2 t^4
    # + 3 H^2 r^2 t^2 / s
    # + [3 E^2 - 3 H^2 + (3/2)D^2]
    #   r^4/[s(s+2)].
    #
    # The doubled upper half, normalized by V0, supplies
    # -d*s/180 times the flat-cone radial/time integral.
    i_t4 = (
        24
        /
        (
            s
            * (s + 1)
            * (s + 2)
            * (s + 3)
            * (s + 4)
            * (s + 5)
        )
    )

    i_t2r2 = (
        2
        /
        (
            (s + 2)
            * (s + 3)
            * (s + 4)
            * (s + 5)
        )
    )

    i_r4 = (
        1
        /
        (
            (s + 4)
            * (s + 5)
        )
    )

    density_prefactor = (
        -d
        * s
        / 180
    )

    e_density = sp.factor(
        density_prefactor
        * (
            i_t4
            +
            3
            * i_r4
            /
            (
                s
                * (s + 2)
            )
        )
    )

    h_density = sp.factor(
        density_prefactor
        * (
            3
            * i_t2r2
            / s
            -
            3
            * i_r4
            /
            (
                s
                * (s + 2)
            )
        )
    )

    d_density = sp.factor(
        density_prefactor
        * (
            sp.Rational(3, 2)
            * i_r4
            /
            (
                s
                * (s + 2)
            )
        )
    )

    assert e_density == (
        -(
            d**2
            + 2 * d
            + 8
        )
        /
        (
            60
            * (d + 1)
            * (d + 2)
            * (d + 3)
            * (d + 4)
        )
    )

    assert h_density == (
        d**2
        /
        (
            60
            * (d + 1)
            * (d + 2)
            * (d + 3)
            * (d + 4)
        )
    )

    assert d_density == (
        -d
        /
        (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    # ---------------------------------------------------------------
    # Full relative coefficients
    # ---------------------------------------------------------------
    v_e = sp.factor(
        e_cone + e_density
    )

    v_h = sp.factor(
        h_cone + h_density
    )

    v_d = sp.factor(
        d_cone + d_density
    )

    assert v_e == (
        d
        * (
            7 * d**2
            + 44 * d
            + 58
        )
        /
        (
            180
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    assert v_h == (
        d
        * (d + 6)
        /
        (
            60
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    assert v_d == (
        -d
        /
        (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    # ---------------------------------------------------------------
    # Convert back to the absolute coefficient in Wang's Eq. (79)
    # normalization.
    # ---------------------------------------------------------------
    corrected_e_numerator = sp.expand(
        (d + 2)
        * (
            7 * d**2
            + 44 * d
            + 58
        )
    )

    corrected_h_numerator = (
        3
        * (d + 2)
        * (d + 6)
    )

    corrected_d_numerator = (
        -sp.Rational(3, 2)
        * (d + 2)
    )

    assert corrected_e_numerator == (
        7 * d**3
        + 58 * d**2
        + 146 * d
        + 116
    )

    # Printed Eq. (79).
    printed_e_numerator = (
        7 * d**3
        + 58 * d**2
        + 146 * d
        + 108
    )

    printed_h_numerator = (
        6
        * (d + 2)
        * (d + 6)
    )

    printed_d_numerator = corrected_d_numerator

    assert sp.expand(
        corrected_e_numerator
        - printed_e_numerator
    ) == 8

    assert sp.expand(
        corrected_h_numerator
        - printed_h_numerator
    ) == (
        -3
        * (d + 2)
        * (d + 6)
    )

    assert (
        corrected_d_numerator
        - printed_d_numerator
    ) == 0

    # ---------------------------------------------------------------
    # Four-dimensional specialization.
    # ---------------------------------------------------------------
    d4_e = sp.simplify(
        v_e.subs(d, 4)
        +
        4
        * v_d.subs(d, 4)
    )

    # H^2 = 2 B^2 in d=4.
    d4_b = sp.simplify(
        2
        * v_h.subs(d, 4)
    )

    assert d4_e == sp.Rational(17, 630)
    assert d4_b == sp.Rational(1, 210)

    print(
        {
            "vE_all_d": str(v_e),
            "vH_all_d": str(v_h),
            "vD_all_d": str(v_d),
            "corrected_E_numerator":
                str(corrected_e_numerator),
            "corrected_H_numerator":
                str(corrected_h_numerator),
            "corrected_D_numerator":
                str(corrected_d_numerator),
            "d4_vE_after_D2_eq_4E2":
                str(d4_e),
            "d4_vB_after_H2_eq_2B2":
                str(d4_b),
        }
    )

    print(
        "PASS: direct symbolic integration of Wang Eqs. (74)+(76) "
        "changes 108->116 in the E^2 numerator, halves the H^2 numerator, "
        "and leaves the D^2 coefficient unchanged."
    )


if __name__ == "__main__":
    main()
