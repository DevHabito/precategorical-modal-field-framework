#!/usr/bin/env python3
"""Numerical Schwarzschild calibration of the d=4 vacuum recovery coefficient.

This script evaluates the intrinsic volume-null edge functional for a small
Schwarzschild Alexandrov interval whose tips are at the same static spatial
position and at coordinate times +/-T. In the T->0 limit this calibrates the
purely electric d=4 vacuum response coefficient.

Status: numerical calibration / regression, not an analytic proof.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import math

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp

TARGET = Fraction(683, 9450)
PLANE_WAVE_SUM = Fraction(508, 4725)
CONDITIONAL_B = PLANE_WAVE_SUM - TARGET


def sectional_curvatures(r: float, mass: float) -> tuple[float, float]:
    """Radial and tangential sectional curvatures of Schwarzschild optical space."""
    k_rad = mass * (3.0 * mass - 2.0 * r) / r**4
    k_tan = mass * (4.0 * r - 9.0 * mass) / r**4
    return k_rad, k_tan


def direction_integrals(
    mu: float,
    half_time: float,
    mass: float,
    radius: float,
    radial_nodes: int,
) -> tuple[float, float]:
    """Return directional parent-volume and edge-functional integrands.

    mu is the cosine of the initial optical angle with the outward radial
    direction. Spherical symmetry leaves only this angular variable.
    """
    a0 = 1.0 - 2.0 * mass / radius
    if a0 <= 0.0:
        raise ValueError("radius must lie outside the Schwarzschild horizon")

    f0 = radius / math.sqrt(a0)
    ell2 = f0 * f0 * max(0.0, 1.0 - mu * mu)

    y0 = np.array(
        [radius, mu, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
        dtype=float,
    )

    def rhs(_s: float, y: np.ndarray) -> np.ndarray:
        r, v, j1, p1, k1, q1, j2, p2, k2, q2 = y
        a = 1.0 - 2.0 * mass / r
        f2 = r * r / a
        tangential_speed2 = ell2 / f2

        k_rad, k_tan = sectional_curvatures(r, mass)
        k_out = v * v * k_rad + tangential_speed2 * k_tan

        dr = a * v
        dv = ell2 * a * (1.0 - 3.0 * mass / r) / r**3

        return np.array(
            [
                dr,
                dv,
                p1,
                -k_rad * j1,
                q1,
                -k_rad * k1,
                p2,
                -k_out * j2,
                q2,
                -k_out * k2,
            ],
            dtype=float,
        )

    sol = solve_ivp(
        rhs,
        (0.0, half_time),
        y0,
        method="DOP853",
        rtol=2.0e-12,
        atol=2.0e-14,
        dense_output=True,
        max_step=half_time / 10.0,
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    y_t = sol.sol(half_time)
    r_t = float(y_t[0])
    a_t = 1.0 - 2.0 * mass / r_t
    j1_t, k1_t = float(y_t[2]), float(y_t[4])
    j2_t, k2_t = float(y_t[6]), float(y_t[8])

    if j1_t <= 0.0 or j2_t <= 0.0:
        raise RuntimeError("conjugate or degenerate optical generator encountered")

    x, w = leggauss(radial_nodes)
    s = 0.5 * half_time * (x + 1.0)
    weights = 0.5 * half_time * w
    ys = sol.sol(s)

    r = ys[0]
    a = 1.0 - 2.0 * mass / r
    j1, k1 = ys[2], ys[4]
    j2, k2 = ys[6], ys[8]

    b1 = j1_t * k1 - k1_t * j1
    b2 = j2_t * k2 - k2_t * j2
    inside = (j1 * b1 * j2 * b2) / (j1_t * j2_t)
    if np.any(inside <= 0.0):
        raise RuntimeError("invalid Jacobi determinant before the endpoint")

    thin_coefficient = math.pi * float(
        np.sum(weights * a**2 * np.sqrt(inside))
    )

    parent_direction = 2.0 * float(
        np.sum(weights * (half_time - s) * a**2 * j1 * j2)
    )

    edge_direction = a_t**4 * j1_t * j2_t / thin_coefficient**3

    return parent_direction, edge_direction


def recovery_ratio(
    half_time: float,
    mass: float,
    radius: float,
    angular_nodes: int,
    radial_nodes: int,
) -> float:
    mu, w = leggauss(angular_nodes)
    parent = 0.0
    edge = 0.0

    for mu_i, w_i in zip(mu, w):
        v_i, e_i = direction_integrals(
            float(mu_i),
            half_time,
            mass,
            radius,
            radial_nodes,
        )
        parent += float(w_i) * v_i
        edge += float(w_i) * e_i

    parent *= 2.0 * math.pi
    edge *= 2.0 * math.pi

    return parent * edge / (576.0 / math.pi)


def extrapolate_electric_coefficient(
    mass: float,
    radius: float,
    half_times: np.ndarray,
    angular_nodes: int,
    radial_nodes: int,
    fit_degree: int,
) -> tuple[float, np.ndarray]:
    a0 = 1.0 - 2.0 * mass / radius
    e2 = 6.0 * mass * mass / radius**6

    scaled = []
    for half_time in half_times:
        ratio = recovery_ratio(
            float(half_time),
            mass,
            radius,
            angular_nodes,
            radial_nodes,
        )

        local_half_size = math.sqrt(a0) * float(half_time)
        scaled.append((ratio - 1.0) / (e2 * local_half_size**4))

    x = half_times**2
    coeffs = np.polynomial.polynomial.polyfit(
        x,
        np.asarray(scaled),
        fit_degree,
    )
    return float(coeffs[0]), np.asarray(scaled)


def parse_half_times(text: str) -> np.ndarray:
    values = [float(part.strip()) for part in text.split(",") if part.strip()]
    if len(values) < 4:
        raise ValueError("provide at least four half-time values")
    if any(value <= 0.0 for value in values):
        raise ValueError("half-times must be positive")
    return np.asarray(values, dtype=float)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mass", type=float, default=1.0)
    parser.add_argument("--radius", type=float, default=8.0)
    parser.add_argument(
        "--half-times",
        default="0.45,0.55,0.65,0.75,0.85,0.95,1.05",
    )
    parser.add_argument("--angular-nodes", type=int, default=48)
    parser.add_argument("--radial-nodes", type=int, default=80)
    parser.add_argument("--fit-degree", type=int, default=3)
    parser.add_argument(
        "--cross-checks",
        action="store_true",
        help="also run several mass/radius universality checks",
    )
    args = parser.parse_args()

    half_times = parse_half_times(args.half_times)
    candidate, scaled = extrapolate_electric_coefficient(
        args.mass,
        args.radius,
        half_times,
        args.angular_nodes,
        args.radial_nodes,
        args.fit_degree,
    )

    print(
        {
            "mass": args.mass,
            "radius": args.radius,
            "angular_nodes": args.angular_nodes,
            "radial_nodes": args.radial_nodes,
            "half_times": half_times.tolist(),
            "scaled_values": scaled.tolist(),
            "T_to_0_extrapolation": candidate,
            "candidate_683_over_9450": float(TARGET),
            "difference": candidate - float(TARGET),
        }
    )

    if args.cross_checks:
        cases = [
            (0.5, 8.0),
            (1.0, 8.0),
            (1.5, 8.0),
            (1.0, 6.0),
            (0.8, 7.0),
        ]
        for mass, radius in cases:
            value, _ = extrapolate_electric_coefficient(
                mass,
                radius,
                half_times,
                args.angular_nodes,
                args.radial_nodes,
                args.fit_degree,
            )
            print(
                {
                    "mass": mass,
                    "radius": radius,
                    "extrapolation": value,
                    "difference_from_candidate": value - float(TARGET),
                }
            )

    print(
        {
            "status": "NUMERICAL_CANDIDATE_NOT_ANALYTIC_PROOF",
            "a4_candidate": str(TARGET),
            "plane_wave_exact_sum": str(PLANE_WAVE_SUM),
            "conditional_b4": str(CONDITIONAL_B),
        }
    )


if __name__ == "__main__":
    main()
