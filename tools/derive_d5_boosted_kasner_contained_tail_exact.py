#!/usr/bin/env python3
"""Exact contained-tail contribution for the v=1/2 boosted d=5 Kasner ACD.

This script treats regime III of the boosted causal-diamond slice, where the
entire future null-cone section is contained in the past one.

Because no partial lens remains, the spatial section can be integrated
exactly over the future conserved null parameter.

The result is an exact polynomial jet in the scaled time T.  Integrating it
between the exact moving lower boundary T2(L) and the exact future-tip
half-time gives the contained-tail contribution through relative order L^4.

No numerical quadrature is used.
"""

from __future__ import annotations

import sympy as sp


def moment(k: int) -> sp.Expr:
    """Integral_0^1 s^(2k) (1-s^2)^(3/2) ds."""
    return sp.simplify(
        sp.gamma(
            sp.Rational(
                2 * k + 1,
                2,
            )
        )
        * sp.gamma(
            sp.Rational(5, 2)
        )
        / (
            2
            * sp.gamma(
                k + 3
            )
        )
    )


def scaled_coefficients(
    densities: list[sp.Expr],
    lower: sp.Expr,
    upper: sp.Expr,
    L: sp.Symbol,
) -> list[sp.Expr]:
    expression = sum(
        density
        * (
            upper ** (degree + 1)
            - lower ** (degree + 1)
        )
        / sp.Integer(
            degree + 1
        )
        for degree, density
        in enumerate(densities)
    )

    scaled = sp.expand(
        expression / L
    )

    return [
        sp.expand(
            scaled.coeff(
                L,
                order,
            )
        )
        for order in range(5)
    ]


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

    axial = scaled_coefficients(
        axial_density,
        u_slice,
        u_plus,
        L,
    )

    transverse = scaled_coefficients(
        transverse_density,
        u_slice,
        u_plus,
        L,
    )

    dx_ds = [
        sp.expand(
            axial[order]
            + 2 * c
            * sp.diff(
                axial[order],
                c,
            )
        )
        for order in range(5)
    ]

    # Coefficients of B^3 * dX/ds.
    product_coefficients: list[
        sp.Expr
    ] = []

    for total_order in range(5):
        expression = sp.Integer(0)

        for i in range(
            total_order + 1
        ):
            for j in range(
                total_order
                - i
                + 1
            ):
                for k in range(
                    total_order
                    - i
                    - j
                    + 1
                ):
                    ell = (
                        total_order
                        - i
                        - j
                        - k
                    )

                    expression += (
                        transverse[i]
                        * transverse[j]
                        * transverse[k]
                        * dx_ds[ell]
                    )

        product_coefficients.append(
            sp.expand(
                expression
            )
        )

    # Spatial section:
    #
    # 2 * integral dx * (4 pi/3) R^3
    #
    # with c=s^2 and R=sqrt(1-c) B.
    section: list[
        sp.Expr
    ] = []

    for expression in product_coefficients:
        degree = int(
            sp.degree(
                expression,
                c,
            )
        )

        integrated = sp.Integer(0)

        for power in range(
            degree + 1
        ):
            coefficient = sp.expand(
                expression
            ).coeff(
                c,
                power,
            )

            if coefficient != 0:
                integrated += (
                    coefficient
                    * moment(power)
                )

        section.append(
            sp.factor(
                sp.Rational(8, 3)
                * sp.pi
                * integrated
            )
        )

    expected_section = [
        sp.pi**2
        * (
            9 * T**4
            - 24 * sqrt3 * T**3
            + 72 * T**2
            - 32 * sqrt3 * T
            + 16
        )
        / 18,
        -sp.pi**2
        * (
            3 * T**2
            - 4
        )
        * (
            9 * T**3
            - 18 * sqrt3 * T**2
            + 36 * T
            - 8 * sqrt3
        )
        / 108,
        sp.pi**2
        * (
            459 * T**6
            - 972 * sqrt3 * T**5
            + 2376 * T**4
            - 1728 * sqrt3 * T**3
            + 5040 * T**2
            - 2880 * sqrt3 * T
            + 1792
        )
        / 2592,
        -sp.pi**2
        * (
            2187 * T**7
            - 4698 * sqrt3 * T**6
            + 11340 * T**5
            - 4536 * sqrt3 * T**4
            - 2736 * T**3
            + 11808 * sqrt3 * T**2
            - 24768 * T
            + 5504 * sqrt3
        )
        / 15552,
        sp.pi**2
        * (
            581985 * T**8
            - 1237680 * sqrt3 * T**7
            + 2870640 * T**6
            - 1062720 * sqrt3 * T**5
            + 1167840 * T**4
            - 2444544 * sqrt3 * T**3
            + 10961664 * T**2
            - 6777856 * sqrt3 * T
            + 4385024
        )
        / 4976640,
    ]

    for actual, expected in zip(
        section,
        expected_section,
    ):
        assert sp.simplify(
            actual
            - expected
        ) == 0

    # Physical volume density t =
    #
    # 1 + L T - L^2/12 - 25 L^4/432 + ...
    physical: list[
        sp.Expr
    ] = []

    for order in range(5):
        expression = section[order]

        if order >= 1:
            expression += (
                T
                * section[order - 1]
            )

        if order >= 2:
            expression += (
                -sp.Rational(1, 12)
                * section[order - 2]
            )

        if order >= 4:
            expression += (
                -sp.Rational(25, 432)
                * section[order - 4]
            )

        physical.append(
            sp.factor(
                expression
            )
        )

    T2 = (
        sqrt3 / 3
        - L / 4
        + 19 * sqrt3 * L**2 / 216
        - 7 * L**3 / 72
        + 3937 * sqrt3 * L**4 / 51840
    )

    T_tip = (
        2 * sqrt3 / 3
        + sqrt3 * L**2 / 27
        + 107 * sqrt3 * L**4 / 3240
    )

    integrated = sp.Integer(0)

    for order, coefficient in enumerate(
        physical
    ):
        antiderivative = sp.integrate(
            coefficient,
            T,
        )

        integrated += (
            L**order
            * (
                antiderivative.subs(
                    T,
                    T_tip,
                )
                -
                antiderivative.subs(
                    T,
                    T2,
                )
            )
        )

    integrated = sp.series(
        integrated,
        L,
        0,
        5,
    ).removeO().expand()

    result = [
        sp.factor(
            integrated.coeff(
                L,
                order,
            )
        )
        for order in range(5)
    ]

    expected_result = [
        sqrt3 * sp.pi**2 / 270,
        sp.pi**2 / 81,
        7 * sqrt3 * sp.pi**2 / 2592,
        59 * sp.pi**2 / 41472,
        9199 * sqrt3 * sp.pi**2 / 8957952,
    ]

    for actual, expected in zip(
        result,
        expected_result,
    ):
        assert sp.simplify(
            actual
            - expected
        ) == 0

    print(
        {
            "section_coefficients": [
                str(value)
                for value in section
            ],
            "contained_tail_integral_coefficients": [
                str(value)
                for value in result
            ],
        }
    )

    print(
        "PASS: the boosted d5 Kasner fully-contained tail is integrated "
        "exactly through L^4 with no numerical quadrature."
    )


if __name__ == "__main__":
    main()
