#!/usr/bin/env python3
"""Independent numerical audit of the centered d=4 LRS-Kasner ACD volume.

Metric:
    ds^2 = -dt^2 + t^(-2/3) dx^2 + t^(4/3)(dy^2+dz^2).

Tips:
    p=(1-L,0,0,0), q=(1+L,0,0,0).

This script computes the PHYSICAL ratio V_Kasner/V_flat directly.

For each spatial coordinate direction mu=cos(theta), it:
1. solves the conserved-momentum direction equation for each null cone;
2. finds the time Y=(t-1)/L where the past and future cone radii cross;
3. integrates the past cone up to that crossing and the future cone after it;
4. integrates over mu with the correct full S^2 normalization.

The ratio is normalized so that the flat limit is exactly 1:
    V_flat = 2*pi*L^4/3.

This checker is deliberately independent of the symbolic Kasner series code.
"""

from __future__ import annotations

import argparse
from fractions import Fraction

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq


TARGET = Fraction(68, 8505)


def interval_integrals(
    t0: float,
    t1: float,
    c: float,
    nodes: np.ndarray,
    weights: np.ndarray,
) -> tuple[float, float]:
    """Coordinate displacement integrals for one Kasner null segment."""
    t = (
        0.5 * (t1 - t0) * nodes
        + 0.5 * (t1 + t0)
    )
    w = 0.5 * (t1 - t0) * weights

    energy = np.sqrt(
        c * t ** (2.0 / 3.0)
        + (1.0 - c) * t ** (-4.0 / 3.0)
    )

    ix = float(
        np.sum(
            w * t ** (2.0 / 3.0) / energy
        )
    )
    ip = float(
        np.sum(
            w * t ** (-4.0 / 3.0) / energy
        )
    )

    return ix, ip


def cone_radius(
    t0: float,
    t1: float,
    direction_w: float,
    nodes: np.ndarray,
    weights: np.ndarray,
) -> float:
    """Euclidean coordinate-ray radius of one null cone section."""
    if direction_w <= 1.0e-14:
        c = 0.0
    elif direction_w >= 1.0 - 1.0e-14:
        c = 1.0
    else:
        def equation(c_value: float) -> float:
            ix, ip = interval_integrals(
                t0,
                t1,
                c_value,
                nodes,
                weights,
            )

            return (
                c_value
                * (1.0 - direction_w)
                * ix * ix
                -
                direction_w
                * (1.0 - c_value)
                * ip * ip
            )

        c = brentq(
            equation,
            0.0,
            1.0,
            xtol=1.0e-14,
            rtol=1.0e-14,
        )

    ix, ip = interval_integrals(
        t0,
        t1,
        c,
        nodes,
        weights,
    )

    axial = np.sqrt(c) * ix
    transverse = np.sqrt(max(0.0, 1.0 - c)) * ip

    return float(
        np.hypot(
            axial,
            transverse,
        )
    )


def volume_ratio(
    L: float,
    angular_order: int,
    time_order: int,
    null_order: int,
) -> float:
    """Return V_Kasner/V_flat with flat normalization built in."""
    mu_nodes, mu_weights = leggauss(angular_order)
    y_nodes, y_weights = leggauss(time_order)
    null_nodes, null_weights = leggauss(null_order)

    def past_radius(Y: float, w: float) -> float:
        return cone_radius(
            1.0 - L,
            1.0 + L * Y,
            w,
            null_nodes,
            null_weights,
        )

    def future_radius(Y: float, w: float) -> float:
        return cone_radius(
            1.0 + L * Y,
            1.0 + L,
            w,
            null_nodes,
            null_weights,
        )

    total = 0.0

    for mu, mu_weight in zip(
        mu_nodes,
        mu_weights,
    ):
        direction_w = float(mu * mu)

        def crossing(Y: float) -> float:
            return (
                past_radius(Y, direction_w)
                -
                future_radius(Y, direction_w)
            )

        Y_edge = brentq(
            crossing,
            -0.5,
            0.5,
            xtol=2.0e-13,
            rtol=2.0e-13,
        )

        def integrate_side(
            lower: float,
            upper: float,
            past: bool,
        ) -> float:
            Y = (
                0.5 * (upper - lower) * y_nodes
                + 0.5 * (upper + lower)
            )
            weights = (
                0.5
                * (upper - lower)
                * y_weights
            )

            values = []

            for y in Y:
                radius = (
                    past_radius(float(y), direction_w)
                    if past
                    else future_radius(float(y), direction_w)
                )

                # sqrt(det spatial metric)=t in Kasner.
                values.append(
                    (1.0 + L * y)
                    * (radius / L) ** 3
                )

            return float(
                np.dot(
                    weights,
                    np.asarray(values),
                )
            )

        directional = (
            integrate_side(
                -1.0,
                Y_edge,
                True,
            )
            +
            integrate_side(
                Y_edge,
                1.0,
                False,
            )
        )

        # The full mu integral, not its normalized average, is required.
        # In flat space:
        #   int_{-1}^1 dmu = 2,
        #   int time = 1/2,
        # so the ratio is exactly 1.
        total += float(mu_weight) * directional

    return total


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--L-values",
        default="0.18,0.15,0.12,0.10,0.08",
    )
    parser.add_argument(
        "--angular-order",
        type=int,
        default=24,
    )
    parser.add_argument(
        "--time-order",
        type=int,
        default=30,
    )
    parser.add_argument(
        "--null-order",
        type=int,
        default=40,
    )

    args = parser.parse_args()

    L_values = np.asarray(
        [
            float(part.strip())
            for part in args.L_values.split(",")
            if part.strip()
        ],
        dtype=float,
    )

    measured = []

    for L in L_values:
        ratio = volume_ratio(
            float(L),
            args.angular_order,
            args.time_order,
            args.null_order,
        )

        coefficient = (
            ratio - 1.0
        ) / L**4

        measured.append(coefficient)

        print(
            {
                "L": float(L),
                "V_ratio": ratio,
                "scaled_L4_coefficient":
                    coefficient,
            }
        )

    # Centered symmetry permits an even extrapolation:
    # c(L)=c0+c2 L^2+c4 L^4+...
    fit = np.polynomial.polynomial.polyfit(
        L_values**2,
        np.asarray(measured),
        2,
    )

    intercept = float(fit[0])
    target = float(TARGET)

    print(
        {
            "T_to_0_extrapolation":
                intercept,
            "target_68_over_8505":
                target,
            "difference":
                intercept - target,
            "status":
                "NUMERICAL_VOLUME_AUDIT_INDEPENDENT_OF_SYMBOLIC_KASNER_SCRIPT",
        }
    )


if __name__ == "__main__":
    main()
