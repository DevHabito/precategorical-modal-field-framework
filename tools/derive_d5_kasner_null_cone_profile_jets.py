#!/usr/bin/env python3
"""Exact d=5 LRS-Kasner null-cone profile jets around t=1.

For the metric

    ds^2 = -dt^2 + t^(-1) dx^2 + t d y_perp^2,

let c in [0,1] be the conserved axial null-momentum fraction.

The null energy is

    E(t,c) = sqrt(c t + (1-c)/t).

The coordinate first-integral densities are

    f_x(t,c)   = t/E(t,c),
    f_perp(t,c) = (1/t)/E(t,c).

This checker derives their exact Taylor expansions in

    u = t-1

through u^5 and integrates those jets between arbitrary nearby endpoints
u0 and u1.

These formulas are the second analytic building block for an exact boosted
Kasner causal-diamond lens expansion.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    u = sp.symbols("u", real=True)
    c = sp.symbols("c", real=True)

    t = 1 + u

    energy = sp.sqrt(
        c * t
        + (1 - c) / t
    )

    f_x = t / energy
    f_perp = (1 / t) / energy

    x_coefficients = [
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
        -(
            2016 * c**5
            - 3920 * c**4
            + 2160 * c**3
            - 264 * c**2
            - 2 * c
            + 3
        ) / 256,
    ]

    perp_coefficients = [
        sp.Integer(1),
        -(2 * c + 1) / 2,
        3 * (4 * c**2 + 1) / 8,
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
        -3 * (
            672 * c**5
            - 560 * c**4
            + 80 * c**3
            + 8 * c**2
            + 10 * c
            + 21
        ) / 256,
    ]

    x_jet = sum(
        coefficient * u**degree
        for degree, coefficient
        in enumerate(
            x_coefficients
        )
    )

    perp_jet = sum(
        coefficient * u**degree
        for degree, coefficient
        in enumerate(
            perp_coefficients
        )
    )

    exact_x_series = sp.series(
        f_x,
        u,
        0,
        6,
    ).removeO().expand()

    exact_perp_series = sp.series(
        f_perp,
        u,
        0,
        6,
    ).removeO().expand()

    assert sp.simplify(
        exact_x_series
        - x_jet
    ) == 0

    assert sp.simplify(
        exact_perp_series
        - perp_jet
    ) == 0

    u0, u1 = sp.symbols(
        "u0 u1",
        real=True,
    )

    axial_integral_jet = sp.expand(
        sum(
            coefficient
            * (
                u1 ** (degree + 1)
                - u0 ** (degree + 1)
            )
            / (degree + 1)
            for degree, coefficient
            in enumerate(
                x_coefficients
            )
        )
    )

    transverse_integral_jet = sp.expand(
        sum(
            coefficient
            * (
                u1 ** (degree + 1)
                - u0 ** (degree + 1)
            )
            / (degree + 1)
            for degree, coefficient
            in enumerate(
                perp_coefficients
            )
        )
    )

    # Endpoint controls.
    flat_limit_axial = sp.simplify(
        axial_integral_jet.subs(
            c,
            sp.Rational(1, 2),
        ).subs(
            {
                u0: 0,
                u1: 0,
            }
        )
    )

    flat_limit_transverse = sp.simplify(
        transverse_integral_jet.subs(
            c,
            sp.Rational(1, 2),
        ).subs(
            {
                u0: 0,
                u1: 0,
            }
        )
    )

    assert flat_limit_axial == 0
    assert flat_limit_transverse == 0

    print(
        {
            "axial_density_jet":
                str(sp.factor(x_jet)),
            "transverse_density_jet":
                str(sp.factor(perp_jet)),
            "axial_integral_jet":
                str(axial_integral_jet),
            "transverse_integral_jet":
                str(transverse_integral_jet),
        }
    )

    print(
        "PASS: exact d5 Kasner null-cone first-integral jets agree with "
        "the direct Taylor expansion through u^5."
    )


if __name__ == "__main__":
    main()
