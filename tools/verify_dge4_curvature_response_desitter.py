#!/usr/bin/env python3
"""Independent de Sitter regression for the d>=4 curvature response.

In spatially-flat de Sitter coordinates, a centered proper-time diamond of
half-duration L maps conformally to the unit Minkowski diamond with raw
sprinkling weight

    w_x(t) = [cosh(x) - t sinh(x)]^(-d),
    x = H L.

For d>=4, the exact weighted joint formula is evaluated by Gauss-Legendre
quadrature.  The measured coefficient

    (K_dS/K_Mink - 1) / x^2

must approach

    c_d = alpha_d * d(d-1) - gamma_d * (d-1),

because de Sitter has
    R = d(d-1) H^2,
    R_TT = -(d-1) H^2.

This regression is independent of the FLRW Taylor algebra used to derive
alpha_d and gamma_d; it starts from the exact de Sitter conformal density.
"""

from __future__ import annotations

import argparse
import math
import numpy as np


def alpha_d(d: int) -> float:
    return (
        -d
        * (d + 6)
        /
        (
            4
            * (d - 1)
            * (d + 1)
            * (d + 2)
        )
    )


def gamma_d(d: int) -> float:
    return (
        (
            d * d
            +
            2 * d
            -
            4
        )
        /
        (
            4
            * (d - 1)
            * (d + 1)
        )
    )


def predicted_desitter_coefficient(
    d: int,
) -> float:
    return (
        alpha_d(d)
        * d
        * (d - 1)
        -
        gamma_d(d)
        * (d - 1)
    )


def gauss_legendre(
    n: int,
    a: float,
    b: float,
) -> tuple[np.ndarray, np.ndarray]:
    x, w = np.polynomial.legendre.leggauss(
        n
    )

    mapped_x = (
        (b - a) * x
        +
        (b + a)
    ) / 2

    mapped_w = (
        (b - a)
        * w
        / 2
    )

    return mapped_x, mapped_w


def weighted_ratio(
    d: int,
    x: float,
    quadrature_points: int,
) -> float:
    m = d / 2.0
    a_m = 1.0 + 2.0 / d

    def weight(t: np.ndarray) -> np.ndarray:
        return (
            np.cosh(x)
            -
            t * np.sinh(x)
        ) ** (-d)

    # Diamond average.
    t, wt = gauss_legendre(
        quadrature_points,
        -1.0,
        1.0,
    )

    diamond_integral = np.sum(
        wt
        * weight(t)
        * (1.0 - np.abs(t)) ** (d - 1)
    )

    diamond_average = (
        diamond_integral
        /
        (2.0 / d)
    )

    # Beta(m,m) null-kernel averages.
    s, ws = gauss_legendre(
        quadrature_points,
        0.0,
        1.0,
    )

    beta_mm = (
        math.gamma(m)
        * math.gamma(m)
        /
        math.gamma(2.0 * m)
    )

    kernel = (
        s ** (m - 1.0)
        * (1.0 - s) ** (m - 1.0)
    )

    null_minus = np.sum(
        ws
        * weight(s - 1.0)
        * kernel
    ) / beta_mm

    null_plus = np.sum(
        ws
        * weight(1.0 - s)
        * kernel
    ) / beta_mm

    edge_weight = float(
        weight(np.array([0.0]))[0]
    )

    return (
        edge_weight**2
        * null_minus ** (-a_m)
        * null_plus ** (-a_m)
        * diamond_average ** (
            2.0 * a_m - 2.0
        )
    )


def parse_dimensions(
    text: str,
) -> list[int]:
    return [
        int(part.strip())
        for part in text.split(",")
        if part.strip()
    ]


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dimensions",
        default="4,5,6,8",
    )

    parser.add_argument(
        "--x-values",
        default="0.1,0.05,0.02,0.01",
    )

    parser.add_argument(
        "--quadrature-points",
        type=int,
        default=500,
    )

    args = parser.parse_args()

    dimensions = parse_dimensions(
        args.dimensions
    )

    x_values = [
        float(part.strip())
        for part
        in args.x_values.split(",")
        if part.strip()
    ]

    for d in dimensions:
        if d < 4:
            raise ValueError(
                "This joint regression is for d>=4."
            )

        predicted = (
            predicted_desitter_coefficient(
                d
            )
        )

        print(
            {
                "d": d,
                "predicted_x2_coefficient":
                    predicted,
            }
        )

        errors = []

        for x in x_values:
            ratio = weighted_ratio(
                d,
                x,
                args.quadrature_points,
            )

            measured = (
                ratio - 1.0
            ) / (x * x)

            error = abs(
                measured - predicted
            )

            errors.append(error)

            print(
                {
                    "x": x,
                    "K_ratio": ratio,
                    "measured_x2_coefficient":
                        measured,
                    "absolute_error":
                        error,
                }
            )

        # The asymptotic error should improve as x decreases.
        if len(errors) >= 2:
            assert (
                errors[-1]
                <
                errors[0]
            )

    print(
        "PASS: exact de Sitter weighted-joint regression approaches the predicted curvature response."
    )


if __name__ == "__main__":
    main()
