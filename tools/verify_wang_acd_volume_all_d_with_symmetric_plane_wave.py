#!/usr/bin/env python3
"""All-d symmetric-plane-wave check of the vacuum ACD volume coefficient.

This is independent of Wang's RNC integration.

For a d-dimensional symmetric Ricci-flat Brinkmann plane wave with constant
trace-free transverse profile A_ij, let

    T2 = tr(A^2),

and let U be the null-phase separation of the centered tips.

For each transverse Jacobi eigenvalue kappa_i=-A_i, the exact channel is

    B_i(r) = r - kappa_i r^3/6 + kappa_i^2 r^5/120 + ...

The causal cross-section determinant gives

    V_PW / V_flat
      = 1 + Lambda_d U^4 T2 + O(A^3 U^6),

where

    Lambda_d
      = (1/360) [1 - 2 (d/2)_4/(d)_4].

Since U=sqrt(2)L,

    delta V / V0
      = 4 Lambda_d T2 L^4.

For the central timelike observer,

    E^2 = T2/4,
    H^2 = T2/2,
    D^2 = T2.

The re-integrated coefficient from Wang Eqs. (74)+(76) is therefore tested by

    v_E/4 + v_H/2 + v_D = 4 Lambda_d.

The identity holds exactly for symbolic d.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    d = sp.symbols(
        "d",
        positive=True,
    )

    lambda_d = sp.factor(
        sp.Rational(1, 360)
        * (
            1
            -
            2
            * sp.rf(d / 2, 4)
            / sp.rf(d, 4)
        )
    )

    exact_plane_wave = sp.factor(
        4 * lambda_d
    )

    expected_exact = (
        d
        * (7 * d + 22)
        /
        (
            720
            * (d + 1)
            * (d + 3)
        )
    )

    assert sp.simplify(
        exact_plane_wave
        - expected_exact
    ) == 0

    # Direct re-integration of Wang's printed intermediate equations.
    v_e = (
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

    v_h = (
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

    v_D = (
        -d
        /
        (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    reintegrated_plane_wave = sp.factor(
        v_e / 4
        + v_h / 2
        + v_D
    )

    assert sp.simplify(
        reintegrated_plane_wave
        - exact_plane_wave
    ) == 0

    # Printed Eq. (79).
    common = (
        180
        * (d + 1)
        * (d + 2)
        * (d + 3)
        * (d + 4)
    )

    printed_e = (
        d
        * (
            7 * d**3
            + 58 * d**2
            + 146 * d
            + 108
        )
        / common
    )

    printed_h = (
        d
        * 6
        * (d + 2)
        * (d + 6)
        / common
    )

    printed_D = (
        -sp.Rational(3, 2)
        * d
        * (d + 2)
        / common
    )

    printed_plane_wave = sp.factor(
        printed_e / 4
        + printed_h / 2
        + printed_D
    )

    discrepancy = sp.factor(
        exact_plane_wave
        - printed_plane_wave
    )

    expected_discrepancy = (
        -d
        * (
            3 * d**2
            + 24 * d
            + 32
        )
        /
        (
            360
            * (d + 1)
            * (d + 2)
            * (d + 3)
            * (d + 4)
        )
    )

    assert sp.simplify(
        discrepancy
        - expected_discrepancy
    ) == 0

    # Concrete dimensions as regression points.
    for dimension in range(4, 13):
        exact_value = sp.factor(
            exact_plane_wave.subs(
                d,
                dimension,
            )
        )
        reintegrated_value = sp.factor(
            reintegrated_plane_wave.subs(
                d,
                dimension,
            )
        )

        assert exact_value == reintegrated_value

    print(
        {
            "4Lambda_d":
                str(exact_plane_wave),
            "Wang_74_76_plane_wave":
                str(reintegrated_plane_wave),
            "printed_79_plane_wave":
                str(printed_plane_wave),
            "exact_minus_printed":
                str(discrepancy),
        }
    )

    print(
        "PASS: the exact symmetric-plane-wave parent volume agrees with "
        "the all-d re-integration of Eqs. (74)+(76), not with printed Eq. (79)."
    )


if __name__ == "__main__":
    main()
