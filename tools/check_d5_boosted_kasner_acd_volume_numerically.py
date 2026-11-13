#!/usr/bin/env python3
"""Direct numerical d=5 boosted LRS-Kasner Alexandrov-volume check.

Purpose
-------
Independently test the corrected all-d vacuum ACD coefficient in a geometry
with a genuinely nonzero hook/magnetic Weyl sector.

Background
----------
Use the five-dimensional LRS Kasner metric

    ds^2 = -dt^2 + t^(-1) dx^2 + t (dy_1^2+dy_2^2+dy_3^2)

and center the Alexandrov interval on a timelike geodesic carrying conserved
momentum in y_1.  At t=1 the local orthonormal speed is v.

The corrected d=5 invariant law predicts

    c_target(v)
      = (8 v^4 + 24 v^2 + 25)
        / [1152 (1-v^2)^2],

for

    (V/V_flat - 1)/L^4 -> c_target(v).

This script does NOT use that formula in the volume integration.

Method
------
At each coordinate time t:

1. construct the past and future null-cone spatial sections from exact null
   first integrals;
2. exploit LRS symmetry so each cone section is a body of revolution about x;
3. for fixed x, reduce the intersection to the exact lens volume of two
   three-balls in the transverse subspace;
4. integrate the lens over x;
5. integrate the spatial section over t with composite Gauss-Legendre panels.

The explicit three-ball lens formula removes the nonsmooth angular
"min-of-two-cones" boundary that spoiled the earlier generic angular
quadrature.

A small-L extrapolation is then performed against L^2, as required by the
centered-diamond even expansion.

Evidence status
---------------
This is an independent numerical geometry check, not an exact proof.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq
from scipy.special import roots_legendre


def tau_primitive(t: float, momentum: float) -> float:
    a = momentum * momentum

    if a == 0.0:
        return t

    return (
        math.sqrt(t * (t + a))
        - a * math.asinh(math.sqrt(t / a))
    )


def y_primitive(t: float, momentum: float) -> float:
    a = momentum * momentum

    if abs(momentum) < 1.0e-15:
        return 0.0

    return (
        2.0
        * momentum
        * math.asinh(math.sqrt(t / a))
    )


def centered_timelike_tips(
    L: float,
    v: float,
) -> tuple[float, float, float, float, float]:
    gamma = 1.0 / math.sqrt(1.0 - v * v)
    momentum = gamma * v

    tau_mid = tau_primitive(
        1.0,
        momentum,
    )

    t_past = brentq(
        lambda t:
            tau_primitive(t, momentum)
            - tau_mid
            + L,
        1.0e-10,
        1.0,
        xtol=2.0e-14,
        rtol=2.0e-14,
    )

    t_future = brentq(
        lambda t:
            tau_primitive(t, momentum)
            - tau_mid
            - L,
        1.0,
        2.0,
        xtol=2.0e-14,
        rtol=2.0e-14,
    )

    y_mid = y_primitive(
        1.0,
        momentum,
    )

    y_past = (
        y_primitive(
            t_past,
            momentum,
        )
        - y_mid
    )

    y_future = (
        y_primitive(
            t_future,
            momentum,
        )
        - y_mid
    )

    return (
        momentum,
        t_past,
        t_future,
        y_past,
        y_future,
    )


def three_ball_lens_volume(
    radius_a: float,
    radius_b: float,
    separation: float,
) -> float:
    if radius_a <= 0.0 or radius_b <= 0.0:
        return 0.0

    if separation <= 1.0e-15:
        radius = min(
            radius_a,
            radius_b,
        )

        return (
            4.0
            * math.pi
            * radius**3
            / 3.0
        )

    if separation >= radius_a + radius_b:
        return 0.0

    if separation <= abs(
        radius_a - radius_b
    ):
        radius = min(
            radius_a,
            radius_b,
        )

        return (
            4.0
            * math.pi
            * radius**3
            / 3.0
        )

    return (
        math.pi
        * (
            radius_a
            + radius_b
            - separation
        ) ** 2
        * (
            separation**2
            + 2.0
            * separation
            * (
                radius_a
                + radius_b
            )
            - 3.0
            * (
                radius_a
                - radius_b
            ) ** 2
        )
        / (
            12.0
            * separation
        )
    )


def cone_profile(
    t0: float,
    t1: float,
    *,
    profile_nodes: int,
    null_order: int,
) -> tuple[np.ndarray, np.ndarray, PchipInterpolator]:
    null_nodes, null_weights = roots_legendre(
        null_order
    )

    t = (
        0.5
        * (t1 - t0)
        * null_nodes
        + 0.5
        * (t1 + t0)
    )

    weights = (
        0.5
        * (t1 - t0)
        * null_weights
    )

    theta = np.linspace(
        0.0,
        0.5 * math.pi,
        profile_nodes,
    )

    c = np.sin(theta) ** 2

    c_matrix = c[:, None]
    t_matrix = t[None, :]

    energy = np.sqrt(
        c_matrix * t_matrix
        + (1.0 - c_matrix)
        / t_matrix
    )

    axial_integral = (
        t_matrix
        / energy
    ) @ weights

    transverse_integral = (
        (1.0 / t_matrix)
        / energy
    ) @ weights

    axial_radius = (
        np.sin(theta)
        * axial_integral
    )

    transverse_radius = (
        np.cos(theta)
        * transverse_integral
    )

    interpolator = PchipInterpolator(
        axial_radius,
        transverse_radius,
        extrapolate=False,
    )

    return (
        axial_radius,
        transverse_radius,
        interpolator,
    )


def spatial_intersection_volume(
    t: float,
    t_past: float,
    t_future: float,
    transverse_separation: float,
    *,
    profile_nodes: int,
    null_order: int,
) -> float:
    (
        x_past,
        _,
        rho_past,
    ) = cone_profile(
        t_past,
        t,
        profile_nodes=profile_nodes,
        null_order=null_order,
    )

    (
        x_future,
        _,
        rho_future,
    ) = cone_profile(
        t,
        t_future,
        profile_nodes=profile_nodes,
        null_order=null_order,
    )

    x_max = min(
        float(x_past[-1]),
        float(x_future[-1]),
    )

    if x_max <= 0.0:
        return 0.0

    def radii(
        x: float,
    ) -> tuple[float, float]:
        return (
            max(
                0.0,
                float(rho_past(x)),
            ),
            max(
                0.0,
                float(rho_future(x)),
            ),
        )

    def sum_minus_separation(
        x: float,
    ) -> float:
        radius_a, radius_b = radii(x)

        return (
            radius_a
            + radius_b
            - transverse_separation
        )

    if (
        sum_minus_separation(0.0)
        <= 0.0
    ):
        return 0.0

    if (
        sum_minus_separation(x_max)
        >= 0.0
    ):
        x_end = x_max
    else:
        x_end = brentq(
            sum_minus_separation,
            0.0,
            x_max,
            xtol=2.0e-12,
            rtol=2.0e-12,
        )

    # Locate containment/lens regime changes explicitly.
    scan_x = np.linspace(
        0.0,
        x_end,
        64,
    )

    containment = []

    for x in scan_x:
        radius_a, radius_b = radii(
            float(x)
        )

        containment.append(
            abs(
                radius_a
                - radius_b
            )
            - transverse_separation
        )

    split_points: list[float] = []

    for (
        x_left,
        x_right,
        g_left,
        g_right,
    ) in zip(
        scan_x[:-1],
        scan_x[1:],
        containment[:-1],
        containment[1:],
    ):
        if g_left * g_right < 0.0:
            split_points.append(
                brentq(
                    lambda x:
                        abs(
                            radii(x)[0]
                            - radii(x)[1]
                        )
                        - transverse_separation,
                    float(x_left),
                    float(x_right),
                    xtol=2.0e-12,
                    rtol=2.0e-12,
                )
            )

    def integrand(
        x: float,
    ) -> float:
        radius_a, radius_b = radii(x)

        return three_ball_lens_volume(
            radius_a,
            radius_b,
            transverse_separation,
        )

    integral, _ = quad(
        integrand,
        0.0,
        x_end,
        points=split_points,
        epsabs=1.0e-13,
        epsrel=2.0e-9,
        limit=200,
    )

    # Symmetry under x -> -x.
    return 2.0 * integral


def physical_volume(
    L: float,
    v: float,
    *,
    profile_nodes: int,
    null_order: int,
    time_panels: int,
    time_gauss_order: int,
) -> float:
    (
        _,
        t_past,
        t_future,
        y_past,
        y_future,
    ) = centered_timelike_tips(
        L,
        v,
    )

    transverse_separation = abs(
        y_future
        - y_past
    )

    nodes, weights = roots_legendre(
        time_gauss_order
    )

    panel_edges = np.linspace(
        t_past,
        t_future,
        time_panels + 1,
    )

    volume = 0.0

    for lower, upper in zip(
        panel_edges[:-1],
        panel_edges[1:],
    ):
        times = (
            0.5
            * (upper - lower)
            * nodes
            + 0.5
            * (upper + lower)
        )

        panel_weights = (
            0.5
            * (upper - lower)
            * weights
        )

        panel_values = []

        for t in times:
            spatial_volume = (
                spatial_intersection_volume(
                    float(t),
                    t_past,
                    t_future,
                    transverse_separation,
                    profile_nodes=profile_nodes,
                    null_order=null_order,
                )
            )

            # sqrt(det g_spatial) = t.
            panel_values.append(
                float(t)
                * spatial_volume
            )

        volume += float(
            np.dot(
                panel_weights,
                np.asarray(
                    panel_values,
                    dtype=float,
                ),
            )
        )

    return volume


def flat_d5_volume(
    L: float,
) -> float:
    return (
        math.pi**2
        * L**5
        / 5.0
    )


def target_coefficient(
    v: float,
) -> float:
    return (
        8.0 * v**4
        + 24.0 * v**2
        + 25.0
    ) / (
        1152.0
        * (1.0 - v**2) ** 2
    )


def extrapolate(
    L_values: list[float],
    measured: list[float],
) -> float:
    fit = np.polynomial.polynomial.polyfit(
        np.asarray(L_values) ** 2,
        np.asarray(measured),
        1,
    )

    return float(fit[0])


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--velocities",
        default="0.3,0.5,0.7",
    )

    parser.add_argument(
        "--L-values",
        default="0.07,0.06,0.05",
    )

    parser.add_argument(
        "--profile-nodes",
        type=int,
        default=2561,
    )

    parser.add_argument(
        "--null-order",
        type=int,
        default=56,
    )

    parser.add_argument(
        "--time-panels",
        type=int,
        default=320,
    )

    parser.add_argument(
        "--time-gauss-order",
        type=int,
        default=8,
    )

    parser.add_argument(
        "--absolute-tolerance",
        type=float,
        default=3.0e-5,
    )

    args = parser.parse_args()

    velocities = [
        float(value)
        for value in args.velocities.split(",")
        if value.strip()
    ]

    L_values = [
        float(value)
        for value in args.L_values.split(",")
        if value.strip()
    ]

    extrapolated_by_velocity: dict[float, float] = {}

    for v in velocities:
        measured = []

        for L in L_values:
            volume = physical_volume(
                L,
                v,
                profile_nodes=args.profile_nodes,
                null_order=args.null_order,
                time_panels=args.time_panels,
                time_gauss_order=args.time_gauss_order,
            )

            ratio = (
                volume
                / flat_d5_volume(L)
            )

            coefficient = (
                ratio - 1.0
            ) / L**4

            measured.append(
                coefficient
            )

            print(
                {
                    "v": v,
                    "L": L,
                    "V_over_Vflat": ratio,
                    "scaled_L4_coefficient":
                        coefficient,
                    "target":
                        target_coefficient(v),
                    "difference":
                        coefficient
                        - target_coefficient(v),
                }
            )

        extrapolated = extrapolate(
            L_values,
            measured,
        )

        target = target_coefficient(v)

        difference = (
            extrapolated
            - target
        )

        print(
            {
                "v": v,
                "L_to_0_extrapolation":
                    extrapolated,
                "target": target,
                "difference": difference,
            }
        )

        extrapolated_by_velocity[v] = extrapolated

        if abs(difference) > args.absolute_tolerance:
            raise AssertionError(
                "boosted Kasner extrapolation exceeded tolerance: "
                f"v={v}, difference={difference}"
            )

    # Independent coefficient reconstruction.
    #
    # Use the exact comoving d=5 Kasner result together with two boosted
    # numerical geometries.  The three invariant directions are linearly
    # independent, so they determine A_5, B_5, C_5 without using Wang Eq. (79)
    # or the corrected coefficient formula as input to the solve.
    if 0.5 in extrapolated_by_velocity and 0.7 in extrapolated_by_velocity:
        def invariants(v: float) -> np.ndarray:
            denominator = (1.0 - v * v) ** 2

            return np.asarray(
                [
                    (
                        v**4
                        + 2.0 * v**2
                        + 3.0
                    )
                    / (
                        4.0 * denominator
                    ),
                    (
                        3.0 * v**2
                        / denominator
                    ),
                    (
                        7.0 * v**4
                        + 2.0 * v**2
                        + 3.0
                    )
                    / (
                        2.0 * denominator
                    ),
                ],
                dtype=float,
            )

        invariant_matrix = np.vstack(
            [
                invariants(0.0),
                invariants(0.5),
                invariants(0.7),
            ]
        )

        measured_vector = np.asarray(
            [
                25.0 / 1152.0,
                extrapolated_by_velocity[0.5],
                extrapolated_by_velocity[0.7],
            ],
            dtype=float,
        )

        recovered = np.linalg.solve(
            invariant_matrix,
            measured_vector,
        )

        exact = np.asarray(
            [
                151.0 / 5184.0,
                11.0 / 5184.0,
                -1.0 / 10368.0,
            ],
            dtype=float,
        )

        recovery_error = recovered - exact

        print(
            {
                "recovered_A5":
                    float(recovered[0]),
                "recovered_B5":
                    float(recovered[1]),
                "recovered_C5":
                    float(recovered[2]),
                "exact_A5":
                    float(exact[0]),
                "exact_B5":
                    float(exact[1]),
                "exact_C5":
                    float(exact[2]),
                "coefficient_errors":
                    recovery_error.tolist(),
                "invariant_matrix_determinant":
                    float(
                        np.linalg.det(
                            invariant_matrix
                        )
                    ),
            }
        )

        if np.max(
            np.abs(
                recovery_error
            )
        ) > 1.0e-5:
            raise AssertionError(
                "independent A5/B5/C5 reconstruction exceeded tolerance"
            )

    print(
        "PASS: direct d=5 boosted LRS-Kasner causal-volume integration "
        "matches the predicted nonzero-H^2 coefficient function within "
        "the declared numerical tolerance."
    )


if __name__ == "__main__":
    main()
