#!/usr/bin/env python3
"""Numerical all-d LRS-Kasner audit of the vacuum ACD four-volume.

For spacetime dimension d>=4 let n=d-1 and use the nontrivial LRS Kasner
exponents

    p_parallel = -(n-2)/n,
    p_perp     = 2/n

with p_perp repeated n-1 times.

The metric is

    ds^2 = -dt^2
           + t^(2 p_parallel) dx^2
           + t^(2 p_perp) d x_perp^2.

The centered tips are t=1+-L on the comoving geodesic.

The script computes V_Kasner/V_flat directly from null geodesics and compares
the L->0 coefficient with the all-d coefficient obtained by re-integrating
Wang's printed intermediate equations:

    delta V / V_flat
      = L^4 [A_d E^2 + B_d H^2 + C_d D^2] + ...

For LRS Kasner H=0 and

    E^2 = 4(n-2)^2(n-1)/n^3,
    D^2 = 16(n-1)(n-2)/n^3.

This is independent of the symbolic d=4 Kasner checker.
"""

from __future__ import annotations

import argparse

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.special import roots_jacobi


def invariants_lrs_kasner(d: int) -> tuple[float, float]:
    n = d - 1

    e2 = (
        4.0
        * (n - 2) ** 2
        * (n - 1)
        / n**3
    )

    d2 = (
        16.0
        * (n - 1)
        * (n - 2)
        / n**3
    )

    return e2, d2


def predicted_coefficient(d: int) -> float:
    dd = float(d)

    a_d = (
        dd
        * (
            7.0 * dd**2
            + 44.0 * dd
            + 58.0
        )
        / (
            180.0
            * (dd + 1.0)
            * (dd + 3.0)
            * (dd + 4.0)
        )
    )

    c_d = -(
        dd
        / (
            120.0
            * (dd + 1.0)
            * (dd + 3.0)
            * (dd + 4.0)
        )
    )

    e2, d2 = invariants_lrs_kasner(d)

    return a_d * e2 + c_d * d2


def volume_ratio(
    L: float,
    d: int,
    angular_order: int,
    time_order: int,
    null_order: int,
) -> float:
    n = d - 1

    p_parallel = -float(n - 2) / n
    p_perp = 2.0 / n

    null_nodes, null_weights = leggauss(
        null_order
    )
    time_nodes, time_weights = leggauss(
        time_order
    )

    alpha = 0.5 * (n - 3)

    mu_nodes, mu_weights = roots_jacobi(
        angular_order,
        alpha,
        alpha,
    )

    # Normalize the axisymmetric S^(n-1) angular measure.
    mu_weights = (
        mu_weights
        / np.sum(mu_weights)
    )

    def interval_integrals(
        t0: float,
        t1: float,
        c: float,
    ) -> tuple[float, float]:
        t = (
            0.5
            * (t1 - t0)
            * null_nodes
            +
            0.5
            * (t1 + t0)
        )

        weights = (
            0.5
            * (t1 - t0)
            * null_weights
        )

        energy = np.sqrt(
            c
            * t ** (-2.0 * p_parallel)
            +
            (1.0 - c)
            * t ** (-2.0 * p_perp)
        )

        axial = float(
            np.sum(
                weights
                * t ** (-2.0 * p_parallel)
                / energy
            )
        )

        transverse = float(
            np.sum(
                weights
                * t ** (-2.0 * p_perp)
                / energy
            )
        )

        return axial, transverse

    def radius(
        t0: float,
        t1: float,
        direction_w: float,
    ) -> float:
        if direction_w <= 1.0e-13:
            c = 0.0
        elif direction_w >= 1.0 - 1.0e-13:
            c = 1.0
        else:
            def equation(c_value: float) -> float:
                axial, transverse = (
                    interval_integrals(
                        t0,
                        t1,
                        c_value,
                    )
                )

                return (
                    c_value
                    * (1.0 - direction_w)
                    * axial**2
                    -
                    direction_w
                    * (1.0 - c_value)
                    * transverse**2
                )

            c = brentq(
                equation,
                0.0,
                1.0,
                xtol=2.0e-13,
                rtol=2.0e-13,
            )

        axial, transverse = interval_integrals(
            t0,
            t1,
            c,
        )

        x = np.sqrt(c) * axial
        y = (
            np.sqrt(max(0.0, 1.0 - c))
            * transverse
        )

        return float(np.hypot(x, y))

    directional_average = 0.0

    for mu, angular_weight in zip(
        mu_nodes,
        mu_weights,
    ):
        direction_w = float(mu * mu)

        def past_radius(Y: float) -> float:
            return radius(
                1.0 - L,
                1.0 + L * Y,
                direction_w,
            )

        def future_radius(Y: float) -> float:
            return radius(
                1.0 + L * Y,
                1.0 + L,
                direction_w,
            )

        Y_edge = brentq(
            lambda Y:
                past_radius(Y)
                - future_radius(Y),
            -0.5,
            0.5,
            xtol=5.0e-12,
            rtol=5.0e-12,
        )

        def integrate_side(
            lower: float,
            upper: float,
            past: bool,
        ) -> float:
            Y = (
                0.5
                * (upper - lower)
                * time_nodes
                +
                0.5
                * (upper + lower)
            )

            weights = (
                0.5
                * (upper - lower)
                * time_weights
            )

            values = []

            for y in Y:
                radial = (
                    past_radius(float(y))
                    if past
                    else future_radius(float(y))
                )

                # Kasner sqrt(det spatial metric)=t because sum p_i=1.
                values.append(
                    (1.0 + L * y)
                    * (radial / L) ** n
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

        directional_average += (
            float(angular_weight)
            * directional
        )

    # General flat normalization:
    # V_flat = 2 Omega_(n-1) L^(n+1) / [n(n+1)].
    return (
        0.5
        * (n + 1)
        * directional_average
    )


def parse_ints(text: str) -> list[int]:
    return [
        int(part.strip())
        for part in text.split(",")
        if part.strip()
    ]


def parse_floats(text: str) -> np.ndarray:
    return np.asarray(
        [
            float(part.strip())
            for part in text.split(",")
            if part.strip()
        ],
        dtype=float,
    )


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dimensions",
        default="4,5,6",
    )
    parser.add_argument(
        "--L-values",
        default="0.16,0.13,0.10,0.08",
    )
    parser.add_argument(
        "--angular-order",
        type=int,
        default=16,
    )
    parser.add_argument(
        "--time-order",
        type=int,
        default=22,
    )
    parser.add_argument(
        "--null-order",
        type=int,
        default=32,
    )

    args = parser.parse_args()

    dimensions = parse_ints(
        args.dimensions
    )
    L_values = parse_floats(
        args.L_values
    )

    for d in dimensions:
        if d < 4:
            raise ValueError(
                "Use spacetime dimension d>=4."
            )

        measured = []

        for L in L_values:
            ratio = volume_ratio(
                float(L),
                d,
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
                    "d": d,
                    "L": float(L),
                    "V_ratio": ratio,
                    "scaled_L4_coefficient":
                        coefficient,
                }
            )

        fit = np.polynomial.polynomial.polyfit(
            L_values**2,
            np.asarray(measured),
            2,
        )

        extrapolated = float(fit[0])
        predicted = predicted_coefficient(d)

        print(
            {
                "d": d,
                "L_to_0_extrapolation":
                    extrapolated,
                "all_d_prediction":
                    predicted,
                "difference":
                    extrapolated - predicted,
                "E2_D2":
                    invariants_lrs_kasner(d),
            }
        )


if __name__ == "__main__":
    main()
