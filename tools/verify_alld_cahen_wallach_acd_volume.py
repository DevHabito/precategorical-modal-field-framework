#!/usr/bin/env python3
"""All-d symmetric-plane-wave check of the corrected vacuum ACD volume law.

Consider a d-dimensional Cahen--Wallach plane wave

    ds^2 = -2 du dv + dx^A dx^A + P_AB x^A x^B du^2,

with a constant trace-free transverse profile P, A=1,...,d-2.

For a centered timelike Alexandrov interval on the central geodesic, let

    U = sqrt(2) L

be the null-phase separation of the tips.

The exact transverse Jacobi matrix B obeys

    B'' = P B,
    B(0)=0,
    B'(0)=I.

For trace(P)=0,

    sqrt(det B(t))
      = t^((d-2)/2)
        [1 - t^4 Tr(P^2)/360 + O(P^3 t^6)].

The exact causal-volume integral therefore gives

    V_PW / V_flat
      = 1 + lambda_d U^4 Tr(P^2) + ...

with

    lambda_d
      = [1 - 2 (d/2)_4/(d)_4]/360
      = d(7d+22)/[2880(d+1)(d+3)].

Relative to the central timelike observer,

    E^2 = Tr(P^2)/4,
    H^2 = Tr(P^2)/2,
    D^2 = Tr(P^2).

The corrected all-d coefficients inferred by direct integration of Wang's
published intermediate equations are

    A_d = d(7d^2+44d+58)/[180(d+1)(d+3)(d+4)],
    B_d = d(d+6)/[60(d+1)(d+3)(d+4)],
    C_d = -d/[120(d+1)(d+3)(d+4)].

This checker proves symbolically that

    A_d/4 + B_d/2 + C_d = 4 lambda_d,

which is exactly the independent Cahen--Wallach volume response because
U^4=4L^4.

Thus the corrected all-d formula passes a nontrivial exact-geometry check in
every dimension d>=4 along the plane-wave invariant direction.
"""

from __future__ import annotations

import sympy as sp


def rising4(x):
    return x * (x + 1) * (x + 2) * (x + 3)


def main() -> None:
    d = sp.symbols("d", integer=True, positive=True)

    lambda_d = sp.factor(
        (
            1
            - 2
            * rising4(sp.Rational(1, 2) * d)
            / rising4(d)
        )
        / 360
    )

    expected_lambda = (
        d
        * (7 * d + 22)
        / (
            2880
            * (d + 1)
            * (d + 3)
        )
    )

    assert sp.simplify(lambda_d - expected_lambda) == 0

    A_d = (
        d
        * (7 * d**2 + 44 * d + 58)
        / (
            180
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    B_d = (
        d
        * (d + 6)
        / (
            60
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    C_d = -(
        d
        / (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    plane_wave_from_corrected_formula = sp.factor(
        A_d / 4
        + B_d / 2
        + C_d
    )

    plane_wave_from_exact_geometry = sp.factor(
        4 * lambda_d
    )

    assert sp.simplify(
        plane_wave_from_corrected_formula
        - plane_wave_from_exact_geometry
    ) == 0

    expected_combination = (
        d
        * (7 * d + 22)
        / (
            720
            * (d + 1)
            * (d + 3)
        )
    )

    assert sp.simplify(
        plane_wave_from_exact_geometry
        - expected_combination
    ) == 0

    print(
        {
            "lambda_d_for_U4_TrP2": str(lambda_d),
            "exact_plane_wave_L4_TrP2": str(
                plane_wave_from_exact_geometry
            ),
            "corrected_all_d_combination": str(
                plane_wave_from_corrected_formula
            ),
        }
    )

    for dimension in (4, 5, 6, 7, 8, 10):
        exact = sp.simplify(
            plane_wave_from_exact_geometry.subs(
                d,
                dimension,
            )
        )
        corrected = sp.simplify(
            plane_wave_from_corrected_formula.subs(
                d,
                dimension,
            )
        )
        assert exact == corrected

        print(
            {
                "d": dimension,
                "plane_wave_L4_TrP2": str(exact),
            }
        )

    print(
        "PASS: corrected all-d ACD volume law agrees exactly with "
        "the symmetric Cahen--Wallach plane-wave volume in every d>=4."
    )


if __name__ == "__main__":
    main()
