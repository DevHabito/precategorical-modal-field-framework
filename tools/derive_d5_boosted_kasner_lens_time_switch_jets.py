#!/usr/bin/env python3
"""Exact moving time-switch jets for the v=1/2 boosted d=5 Kasner lens.

Geometry
--------
Five-dimensional LRS Kasner:

    ds^2 = -dt^2 + t^(-1) dx^2 + t(dy_1^2+dy_2^2+dy_3^2).

The central timelike geodesic has midpoint speed

    v = 1/2,

so

    P = 1/sqrt(3),
    gamma = 2/sqrt(3).

The boosted spatial slice has three flat-limit regimes separated by

    T_1(0) = sqrt(3)/6,
    T_2(0) = sqrt(3)/3.

This script derives their exact perturbative motion through L^4.

T_1 is defined by the future cone reaching its axial endpoint while the
past transverse radius equals the tip-center separation.

T_2 is defined on the transverse axis by

    R_- - R_+ = d_perp.

No fitted coefficient is used.
"""

from __future__ import annotations

import sympy as sp


def scaled_integral(
    coefficients: list[sp.Expr],
    lower: sp.Expr,
    upper: sp.Expr,
    L: sp.Symbol,
) -> sp.Expr:
    expression = sum(
        coefficient
        * (
            upper ** (degree + 1)
            - lower ** (degree + 1)
        )
        / sp.Integer(degree + 1)
        for degree, coefficient
        in enumerate(coefficients)
    )

    return sp.series(
        expression / L,
        L,
        0,
        5,
    ).removeO().expand()


def solve_order_by_order(
    equations: tuple[sp.Expr, ...],
    variable_groups: tuple[tuple[sp.Symbol, ...], ...],
    L: sp.Symbol,
) -> dict[sp.Symbol, sp.Expr]:
    solution: dict[sp.Symbol, sp.Expr] = {}

    order_count = len(variable_groups[0])

    for order in range(1, order_count + 1):
        variables = tuple(
            group[order - 1]
            for group in variable_groups
        )

        coefficients = [
            sp.expand(
                equation.subs(solution)
            ).coeff(
                L,
                order,
            )
            for equation in equations
        ]

        matrix = sp.Matrix(
            [
                [
                    sp.diff(
                        coefficient,
                        variable,
                    )
                    for variable in variables
                ]
                for coefficient in coefficients
            ]
        )

        rhs = sp.Matrix(
            [
                -coefficient.subs(
                    {
                        variable: 0
                        for variable in variables
                    }
                )
                for coefficient in coefficients
            ]
        )

        solved = matrix.LUsolve(rhs)

        for variable, value in zip(
            variables,
            solved,
        ):
            solution[variable] = sp.factor(
                value
            )

    return solution


def main() -> None:
    L, T, c = sp.symbols(
        "L T c",
        real=True,
    )

    sqrt3 = sp.sqrt(3)

    u_plus = (
        2 * sqrt3 * L / 3
        - L**2 / 12
        + sqrt3 * L**3 / 27
        - 25 * L**4 / 432
        + 107 * sqrt3 * L**5 / 3240
    )

    u_minus = (
        -2 * sqrt3 * L / 3
        - L**2 / 12
        - sqrt3 * L**3 / 27
        - 25 * L**4 / 432
        - 107 * sqrt3 * L**5 / 3240
    )

    u_mid = sp.expand(
        (
            u_plus
            + u_minus
        )
        / 2
    )

    u_slice = (
        u_mid
        + L * T
    )

    axial_density = [
        sp.Integer(1),
        -(2 * c - 3) / 2,
        (
            12 * c**2
            - 16 * c
            + 3
        ) / 8,
        -(
            (2 * c - 1)
            * (
                20 * c**2
                - 20 * c
                - 1
            )
        ) / 16,
        (
            560 * c**4
            - 960 * c**3
            + 408 * c**2
            - 16 * c
            + 3
        ) / 128,
    ]

    transverse_density = [
        sp.Integer(1),
        -(2 * c + 1) / 2,
        3 * (
            4 * c**2
            + 1
        ) / 8,
        -(
            40 * c**3
            - 12 * c**2
            + 2 * c
            + 5
        ) / 16,
        (
            560 * c**4
            - 320 * c**3
            + 24 * c**2
            + 16 * c
            + 35
        ) / 128,
    ]

    past_axial = scaled_integral(
        axial_density,
        u_minus,
        u_slice,
        L,
    )

    past_transverse = scaled_integral(
        transverse_density,
        u_minus,
        u_slice,
        L,
    )

    future_axial = scaled_integral(
        axial_density,
        u_slice,
        u_plus,
        L,
    )

    future_transverse = scaled_integral(
        transverse_density,
        u_slice,
        u_plus,
        L,
    )

    separation = (
        2 / sqrt3
        + 17 * sqrt3 * L**2 / 54
        + 251 * sqrt3 * L**4 / 810
    )

    # ------------------------------------------------------------
    # First critical time T_1:
    #
    # Future cone axial endpoint c=1, hence R_+=0.
    # Match the same axial coordinate on the past cone and impose
    #
    #     R_- = separation.
    # ------------------------------------------------------------

    t1, t2, t3, t4 = sp.symbols(
        "t1 t2 t3 t4"
    )

    k1, k2, k3, k4 = sp.symbols(
        "k1 k2 k3 k4"
    )

    T1_series = (
        sqrt3 / 6
        + t1 * L
        + t2 * L**2
        + t3 * L**3
        + t4 * L**4
    )

    c_past_series = (
        sp.Rational(9, 25)
        + k1 * L
        + k2 * L**2
        + k3 * L**3
        + k4 * L**4
    )

    past_axial_T1 = sp.series(
        past_axial.subs(
            {
                T: T1_series,
                c: c_past_series,
            }
        ),
        L,
        0,
        5,
    ).removeO()

    past_transverse_T1 = sp.series(
        past_transverse.subs(
            {
                T: T1_series,
                c: c_past_series,
            }
        ),
        L,
        0,
        5,
    ).removeO()

    future_endpoint_axial = sp.series(
        future_axial.subs(
            {
                T: T1_series,
                c: 1,
            }
        ),
        L,
        0,
        5,
    ).removeO()

    past_x = sp.series(
        sp.sqrt(
            c_past_series
        )
        * past_axial_T1,
        L,
        0,
        5,
    ).removeO().expand()

    future_x = sp.expand(
        future_endpoint_axial
    )

    past_radius = sp.series(
        sp.sqrt(
            1
            - c_past_series
        )
        * past_transverse_T1,
        L,
        0,
        5,
    ).removeO().expand()

    first_solution = solve_order_by_order(
        equations=(
            sp.expand(
                past_x
                - future_x
            ),
            sp.expand(
                past_radius
                - separation
            ),
        ),
        variable_groups=(
            (t1, t2, t3, t4),
            (k1, k2, k3, k4),
        ),
        L=L,
    )

    expected_T1 = {
        t1: sp.Rational(1, 16),
        t2: 61 * sqrt3 / 432,
        t3: -sp.Rational(367, 2304),
        t4: 25949 * sqrt3 / 207360,
    }

    for variable, expected in expected_T1.items():
        assert sp.simplify(
            first_solution[variable]
            - expected
        ) == 0

    # ------------------------------------------------------------
    # Second critical time T_2:
    #
    # On the transverse axis c=0 for both cones and
    #
    #     R_- - R_+ = separation.
    # ------------------------------------------------------------

    s1, s2, s3, s4 = sp.symbols(
        "s1 s2 s3 s4"
    )

    T2_series = (
        sqrt3 / 3
        + s1 * L
        + s2 * L**2
        + s3 * L**3
        + s4 * L**4
    )

    past_axis = sp.series(
        past_transverse.subs(
            {
                T: T2_series,
                c: 0,
            }
        ),
        L,
        0,
        5,
    ).removeO().expand()

    future_axis = sp.series(
        future_transverse.subs(
            {
                T: T2_series,
                c: 0,
            }
        ),
        L,
        0,
        5,
    ).removeO().expand()

    second_equation = sp.expand(
        past_axis
        - future_axis
        - separation
    )

    second_solution: dict[
        sp.Symbol,
        sp.Expr,
    ] = {}

    for order, variable in enumerate(
        (s1, s2, s3, s4),
        start=1,
    ):
        coefficient = sp.expand(
            second_equation.subs(
                second_solution
            )
        ).coeff(
            L,
            order,
        )

        slope = sp.diff(
            coefficient,
            variable,
        )

        base = coefficient.subs(
            variable,
            0,
        )

        second_solution[variable] = sp.factor(
            -base / slope
        )

    expected_T2 = {
        s1: -sp.Rational(1, 4),
        s2: 19 * sqrt3 / 216,
        s3: -sp.Rational(7, 72),
        s4: 3937 * sqrt3 / 51840,
    }

    for variable, expected in expected_T2.items():
        assert sp.simplify(
            second_solution[variable]
            - expected
        ) == 0

    print(
        {
            "T1": (
                "sqrt(3)/6 + L/16 + "
                "61*sqrt(3)*L^2/432 - "
                "367*L^3/2304 + "
                "25949*sqrt(3)*L^4/207360"
            ),
            "T2": (
                "sqrt(3)/3 - L/4 + "
                "19*sqrt(3)*L^2/216 - "
                "7*L^3/72 + "
                "3937*sqrt(3)*L^4/51840"
            ),
            "past_c_at_T1": {
                str(variable): str(
                    first_solution[variable]
                )
                for variable in (
                    k1,
                    k2,
                    k3,
                    k4,
                )
            },
        }
    )

    print(
        "PASS: exact moving regime-boundary jets T1(L) and T2(L) "
        "are derived through L^4 without fitting."
    )


if __name__ == "__main__":
    main()
