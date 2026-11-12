#!/usr/bin/env python3
"""Independent numerical audit of the d=4 LRS-Kasner intrinsic edge factor.

Metric:
    ds^2 = -dt^2 + t^(-2/3) dx^2 + t^(4/3)(dy^2+dz^2).

For the centered diamond with tips t=1+-L, this script evaluates directly

    < (dA/dA_flat) * (chi/chi_flat)^(-3) >,

where

    chi = |g^{-1}(d(2 sigma_-), d(2 sigma_+))|.

The calculation uses:
1. exact first integrals of Kasner null geodesics;
2. direction-by-direction solution of the past/future cone crossing;
3. affine lengths lambda_+- from dt/E;
4. Synge endpoint-gradient relation d(2 sigma)=2 lambda p;
5. numerical differentiation of the exact edge embedding;
6. Gauss--Legendre angular quadrature.

The expected small-L coefficient is

    37/675 * E^2 L^4,

with E^2=8/27 at t=1.

This implementation is independent of the symbolic Kasner series checker.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import math

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq


E2 = 8.0 / 27.0
TARGET = Fraction(37, 675)


def make_edge_solver(
    L: float,
    null_order: int,
):
    nodes, weights = leggauss(null_order)

    def interval_data(
        t0: float,
        t1: float,
        c: float,
    ) -> tuple[float, float, float]:
        t = (
            0.5 * (t1 - t0) * nodes
            + 0.5 * (t1 + t0)
        )
        w = 0.5 * (t1 - t0) * weights

        energy = np.sqrt(
            c * t ** (2.0 / 3.0)
            + (1.0 - c) * t ** (-4.0 / 3.0)
        )

        inv_energy = 1.0 / energy

        ix = float(
            np.sum(
                w
                * t ** (2.0 / 3.0)
                * inv_energy
            )
        )

        ip = float(
            np.sum(
                w
                * t ** (-4.0 / 3.0)
                * inv_energy
            )
        )

        affine = float(
            np.sum(
                w * inv_energy
            )
        )

        return ix, ip, affine

    def cone(
        t0: float,
        t1: float,
        direction_w: float,
    ) -> tuple[float, float, float]:
        if direction_w <= 1.0e-14:
            c = 0.0
        elif direction_w >= 1.0 - 1.0e-14:
            c = 1.0
        else:
            def equation(c_value: float) -> float:
                ix, ip, _ = interval_data(
                    t0,
                    t1,
                    c_value,
                )

                return (
                    c_value
                    * (1.0 - direction_w)
                    * ix**2
                    -
                    direction_w
                    * (1.0 - c_value)
                    * ip**2
                )

            c = brentq(
                equation,
                0.0,
                1.0,
                xtol=1.0e-14,
                rtol=1.0e-14,
            )

        ix, ip, affine = interval_data(
            t0,
            t1,
            c,
        )

        radius = float(
            np.hypot(
                np.sqrt(c) * ix,
                np.sqrt(max(0.0, 1.0 - c)) * ip,
            )
        )

        return radius, c, affine

    def edge(mu: float):
        direction_w = mu * mu

        def crossing(Y: float) -> float:
            t = 1.0 + L * Y

            past_radius, _, _ = cone(
                1.0 - L,
                t,
                direction_w,
            )
            future_radius, _, _ = cone(
                t,
                1.0 + L,
                direction_w,
            )

            return (
                past_radius
                - future_radius
            )

        Y_edge = brentq(
            crossing,
            -0.5,
            0.5,
            xtol=2.0e-13,
            rtol=2.0e-13,
        )

        t_edge = 1.0 + L * Y_edge

        radius, c_minus, lambda_minus = cone(
            1.0 - L,
            t_edge,
            direction_w,
        )

        radius_plus, c_plus, lambda_plus = cone(
            t_edge,
            1.0 + L,
            direction_w,
        )

        assert abs(radius - radius_plus) < 1.0e-10

        return (
            t_edge,
            radius,
            c_minus,
            c_plus,
            lambda_minus,
            lambda_plus,
        )

    return edge


def edge_cross_ratio(
    L: float,
    angular_order: int,
    null_order: int,
    derivative_step: float,
) -> float:
    edge = make_edge_solver(
        L,
        null_order,
    )

    nodes, weights = leggauss(
        angular_order
    )

    cache: dict[float, tuple] = {}

    def get(mu: float):
        key = round(float(mu), 13)

        if key not in cache:
            cache[key] = edge(float(mu))

        return cache[key]

    values = []

    for mu in nodes:
        (
            t_edge,
            radius,
            c_minus,
            c_plus,
            lambda_minus,
            lambda_plus,
        ) = get(float(mu))

        h = min(
            derivative_step,
            0.2 * (1.0 - abs(float(mu))),
        )

        t_hi, r_hi, *_ = get(float(mu + h))
        t_lo, r_lo, *_ = get(float(mu - h))

        dt_dmu = (t_hi - t_lo) / (2.0 * h)
        dr_dmu = (r_hi - r_lo) / (2.0 * h)

        one_minus_mu2 = max(
            1.0 - float(mu) ** 2,
            1.0e-30,
        )

        sqrt_one_minus = math.sqrt(
            one_minus_mu2
        )

        dx_dmu = (
            dr_dmu * float(mu)
            + radius
        )

        dy_dmu = (
            dr_dmu * sqrt_one_minus
            -
            radius
            * float(mu)
            / sqrt_one_minus
        )

        q_mumu = (
            -dt_dmu**2
            +
            t_edge ** (-2.0 / 3.0)
            * dx_dmu**2
            +
            t_edge ** (4.0 / 3.0)
            * dy_dmu**2
        )

        q_phiphi = (
            t_edge ** (4.0 / 3.0)
            * radius**2
            * one_minus_mu2
        )

        area_ratio = (
            math.sqrt(
                q_mumu * q_phiphi
            )
            / L**2
        )

        e_minus = math.sqrt(
            c_minus
            * t_edge ** (2.0 / 3.0)
            +
            (1.0 - c_minus)
            * t_edge ** (-4.0 / 3.0)
        )

        e_plus = math.sqrt(
            c_plus
            * t_edge ** (2.0 / 3.0)
            +
            (1.0 - c_plus)
            * t_edge ** (-4.0 / 3.0)
        )

        spatial_cross = (
            t_edge ** (2.0 / 3.0)
            * math.sqrt(
                c_minus * c_plus
            )
            +
            t_edge ** (-4.0 / 3.0)
            * math.sqrt(
                (1.0 - c_minus)
                * (1.0 - c_plus)
            )
        )

        chi_ratio = (
            4.0
            * lambda_minus
            * lambda_plus
            * (
                e_minus * e_plus
                + spatial_cross
            )
            / (
                8.0 * L**2
            )
        )

        values.append(
            area_ratio
            * chi_ratio ** (-3.0)
        )

    # Normalized S^2 average for an axisymmetric integrand.
    return float(
        0.5
        * np.dot(
            weights,
            np.asarray(values),
        )
    )


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
        "--null-order",
        type=int,
        default=50,
    )
    parser.add_argument(
        "--derivative-step",
        type=float,
        default=1.0e-5,
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

    scaled = []

    for L in L_values:
        ratio = edge_cross_ratio(
            float(L),
            args.angular_order,
            args.null_order,
            args.derivative_step,
        )

        coefficient = (
            ratio - 1.0
        ) / (
            E2 * L**4
        )

        scaled.append(coefficient)

        print(
            {
                "L": float(L),
                "edge_cross_ratio": ratio,
                "scaled_E2_coefficient":
                    coefficient,
            }
        )

    fit = np.polynomial.polynomial.polyfit(
        L_values**2,
        np.asarray(scaled),
        2,
    )

    extrapolated = float(fit[0])
    target = float(TARGET)

    print(
        {
            "L_to_0_extrapolation":
                extrapolated,
            "target_37_over_675":
                target,
            "difference":
                extrapolated - target,
            "status":
                "NUMERICAL_EDGE_CROSS_AUDIT_INDEPENDENT_OF_SYMBOLIC_SERIES",
        }
    )


if __name__ == "__main__":
    main()
