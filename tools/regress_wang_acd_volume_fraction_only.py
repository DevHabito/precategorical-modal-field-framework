#!/usr/bin/env python3
"""CAS-independent exact rational regression for the Wang ACD re-integration.

This checker intentionally does NOT import SymPy or another computer-algebra
system.  It uses only Python's fractions.Fraction, factorials, and elementary
Beta-integral identities.

For each integer d in a configurable range it re-integrates the angularly
averaged terms of Wang (2019), Eqs. (74) and (76), keeping the electric,
magnetic-H, and spatial-Weyl-D sectors separate.

The purpose is software-method independence from
derive_wang_acd_volume_from_intermediate_equations_all_d.py.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial


def beta_cone_integral(
    spatial_dimension: int,
    t_power: int,
    extra_r_power: int,
) -> Fraction:
    """Return integral_0^1 dt t^a integral_0^(1-t) dr r^(s-1+b)."""
    s = spatial_dimension
    a = t_power
    b = extra_r_power

    return Fraction(
        factorial(a)
        * factorial(s + b - 1),
        factorial(s + b + a + 1),
    )


def direct_coefficients(
    d: int,
) -> tuple[Fraction, Fraction, Fraction]:
    if d < 4:
        raise ValueError("The vacuum Weyl audit is intended for d >= 4.")

    s = d - 1

    # ---------------------------------------------------------------
    # Eq. (74): null-cone boundary.
    # ---------------------------------------------------------------
    #
    # S^(s-1) moments:
    #   <E_nn^2>/E^2     = 2/[s(s+2)]
    #   <(E^2)_nn>/E^2   = 1/s
    #   <HH quartic>/H^2 = 3/[2 s(s+2)]
    #
    # For r=(1-t)(1+a1+a2),
    #   r^s = (1-t)^s [1+s a1+s a2+s(s-1)a1^2/2+...].
    e_a2_constant = Fraction(
        2,
        24 * s * (s + 2),
    )

    e_a2_t = -Fraction(
        1,
        45 * s,
    )

    e_a2_y2 = Fraction(1, 90) * (
        Fraction(1, s)
        - Fraction(
            2,
            s * (s + 2),
        )
    )

    e_a1_sq = Fraction(
        2,
        36 * s * (s + 2),
    )

    # Elementary one-dimensional integrals:
    # integral y^s dt = 1/(s+1)
    # integral t y^s dt = 1/[(s+1)(s+2)]
    # integral y^(s+2) dt = 1/(s+3), y=1-t.
    e_cone = d * (
        s
        * e_a2_constant
        * Fraction(1, s + 1)
        +
        s
        * e_a2_t
        * Fraction(
            1,
            (s + 1) * (s + 2),
        )
        +
        s
        * e_a2_y2
        * Fraction(1, s + 3)
        +
        Fraction(
            s * (s - 1),
            2,
        )
        * e_a1_sq
        * Fraction(1, s + 1)
    )

    h_a2_y2 = (
        Fraction(1, 90)
        * Fraction(
            3,
            2 * s * (s + 2),
        )
    )

    h_cone = (
        d
        * s
        * h_a2_y2
        * Fraction(1, s + 3)
    )

    # ---------------------------------------------------------------
    # Eq. (76): RNC volume density.
    # ---------------------------------------------------------------
    #
    # <Q> =
    #   E^2 t^4
    # + 3 H^2 r^2 t^2/s
    # + [3E^2-3H^2+(3/2)D^2] r^4/[s(s+2)].
    #
    # Relative normalization of the doubled upper cone:
    density_prefactor = -Fraction(
        d * s,
        180,
    )

    i_t4 = beta_cone_integral(
        s,
        t_power=4,
        extra_r_power=0,
    )

    i_t2_r2 = beta_cone_integral(
        s,
        t_power=2,
        extra_r_power=2,
    )

    i_r4 = beta_cone_integral(
        s,
        t_power=0,
        extra_r_power=4,
    )

    e_density = density_prefactor * (
        i_t4
        +
        Fraction(
            3,
            s * (s + 2),
        )
        * i_r4
    )

    h_density = density_prefactor * (
        Fraction(3, s)
        * i_t2_r2
        -
        Fraction(
            3,
            s * (s + 2),
        )
        * i_r4
    )

    d_density = density_prefactor * (
        Fraction(
            3,
            2 * s * (s + 2),
        )
        * i_r4
    )

    return (
        e_cone + e_density,
        h_cone + h_density,
        d_density,
    )


def expected_direct_coefficients(
    d: int,
) -> tuple[Fraction, Fraction, Fraction]:
    return (
        Fraction(
            d
            * (
                7 * d * d
                + 44 * d
                + 58
            ),
            180
            * (d + 1)
            * (d + 3)
            * (d + 4),
        ),
        Fraction(
            d * (d + 6),
            60
            * (d + 1)
            * (d + 3)
            * (d + 4),
        ),
        -Fraction(
            d,
            120
            * (d + 1)
            * (d + 3)
            * (d + 4),
        ),
    )


def printed_eq79_coefficients(
    d: int,
) -> tuple[Fraction, Fraction, Fraction]:
    denominator = (
        180
        * (d + 1)
        * (d + 2)
        * (d + 3)
        * (d + 4)
    )

    return (
        Fraction(
            d
            * (
                7 * d**3
                + 58 * d**2
                + 146 * d
                + 108
            ),
            denominator,
        ),
        Fraction(
            d
            * 6
            * (d + 2)
            * (d + 6),
            denominator,
        ),
        Fraction(
            -3 * d * (d + 2),
            2 * denominator,
        ),
    )


def main() -> None:
    checked = []

    for d in range(4, 21):
        direct = direct_coefficients(d)
        expected = expected_direct_coefficients(d)
        printed = printed_eq79_coefficients(d)

        assert direct == expected

        delta_e = direct[0] - printed[0]
        delta_h = direct[1] - printed[1]
        delta_d = direct[2] - printed[2]

        assert delta_e == Fraction(
            2 * d,
            45
            * (d + 1)
            * (d + 2)
            * (d + 3)
            * (d + 4),
        )

        assert direct[1] * 2 == printed[1]
        assert delta_d == 0

        checked.append(
            {
                "d": d,
                "vE": str(direct[0]),
                "vH": str(direct[1]),
                "vD": str(direct[2]),
            }
        )

    # Four-dimensional physical reduction:
    # D^2=4E^2 and H^2=2B^2.
    v_e_raw, v_h_raw, v_d_raw = direct_coefficients(4)

    v_e_4 = (
        v_e_raw
        + 4 * v_d_raw
    )

    v_b_4 = 2 * v_h_raw

    assert v_e_4 == Fraction(17, 630)
    assert v_b_4 == Fraction(1, 210)

    print(
        {
            "dimensions_checked":
                f"{checked[0]['d']}..{checked[-1]['d']}",
            "d4_physical_vE":
                str(v_e_4),
            "d4_physical_vB":
                str(v_b_4),
            "sympy_imported":
                False,
        }
    )

    print(
        "PASS: Fraction-only re-integration agrees with the symbolic "
        "all-d result for every tested dimension."
    )


if __name__ == "__main__":
    main()
