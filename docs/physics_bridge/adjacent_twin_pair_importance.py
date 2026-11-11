#!/usr/bin/env python3
"""Two-point importance estimators for adjacent-twin expectation.

For n iid points in the standard flat Alexandrov diamond, an unordered
comparable pair X,Y is an adjacent twin pair iff every other point avoids the
symmetric difference of their comparability regions.  Therefore

    E[T_n] = binom(n,2) E[1_{X~Y} (1-D(X,Y))^(n-2)].

This script estimates that exact two-point expectation without generating the
remaining n-2 points.

The d=3 proposal is normalized by the analytically evaluated bulk coefficient
32*pi/3.  Its proposal has full support on the interior point x and on all
future timelike displacements h.

The d=4 proposal uses waist-adapted radial variables but samples the exact
finite-n angular causal cap, giving full support on all future-comparable pairs
in the diamond.  Its limiting normalization is 9*pi.

NumPy is required.
"""

from __future__ import annotations

import argparse
import json
import math
import numpy as np


C3 = 32.0 * math.pi / 3.0
C4 = 9.0 * math.pi
I1 = math.sqrt(math.pi) / 4.0


def d3_expected_twins(
    n: int,
    samples: int,
    seed: int,
) -> dict:
    rng = np.random.default_rng(seed)

    # q_x is proportional to the leading local cone integral.
    theta_z = rng.uniform(
        -math.pi / 4.0,
        math.pi / 4.0,
        size=samples,
    )
    z = np.tan(theta_z)

    a_coef = z * z * (z * z + 3.0)
    b_coef = 4.0 * (1.0 - z * z)
    uniform = rng.random(samples)

    denominator = (
        (1.0 + z * z) ** 2
        - uniform * uniform * a_coef
    )

    s = np.sqrt(
        np.maximum(
            uniform * uniform
            * b_coef
            / denominator,
            0.0,
        )
    )

    sqrt_u = s * (1.0 + z) / 2.0
    sqrt_v = s * (1.0 - z) / 2.0
    u = sqrt_u * sqrt_u
    v = sqrt_v * sqrt_v

    time_x = (u - v) / 4.0
    radius_square = (
        (1.0 + time_x) ** 2
        - u
    )
    radius = np.sqrt(
        np.maximum(radius_square, 0.0)
    )

    space_x = np.column_stack(
        (
            radius,
            np.zeros(samples),
        )
    )

    w0 = (
        sqrt_u * (1.0 + time_x)
        + sqrt_v * (1.0 - time_x)
    )
    w_space = (
        sqrt_u - sqrt_v
    )[:, None] * space_x

    w_square = (
        w0 * w0
        - np.sum(
            w_space * w_space,
            axis=1,
        )
    )
    w_square = np.maximum(
        w_square,
        1.0e-300,
    )

    ell_norm = (
        3.0 / 8.0
    ) * np.sqrt(w_square)

    # Proposal proportional to exp(-n ell(h)) over the future cone.
    proper_time = rng.gamma(
        shape=3.0,
        scale=1.0 / (n * ell_norm),
    )

    angle = (
        2.0
        * math.pi
        * rng.random(samples)
    )
    spatial_radius = (
        proper_time
        * np.sqrt(rng.random(samples))
    )

    rest_space = np.column_stack(
        (
            spatial_radius
            * np.cos(angle),
            spatial_radius
            * np.sin(angle),
        )
    )

    beta = w_space / w0[:, None]
    beta_square = np.sum(
        beta * beta,
        axis=1,
    )
    gamma = w0 / np.sqrt(w_square)
    beta_dot_h = np.sum(
        beta * rest_space,
        axis=1,
    )

    coefficient = np.where(
        beta_square > 1.0e-20,
        (
            (gamma - 1.0)
            * beta_dot_h
            / beta_square
            + gamma * proper_time
        ),
        gamma * proper_time,
    )

    delta_time = gamma * (
        proper_time
        + beta_dot_h
    )
    delta_space = (
        rest_space
        + coefficient[:, None] * beta
    )

    time_y = time_x + delta_time
    space_y = space_x + delta_space
    radius_y_square = np.sum(
        space_y * space_y,
        axis=1,
    )

    inside = (
        (np.abs(time_y) <= 1.0 + 1.0e-12)
        & (
            radius_y_square
            <= (
                1.0 - np.abs(time_y)
            ) ** 2
            + 1.0e-12
        )
    )

    u_y = (
        (1.0 + time_y) ** 2
        - radius_y_square
    )
    v_y = (
        (1.0 - time_y) ** 2
        - radius_y_square
    )

    interval_square = (
        delta_time * delta_time
        - np.sum(
            delta_space * delta_space,
            axis=1,
        )
    )

    distinguishing_fraction = (
        np.maximum(u_y, 0.0) ** 1.5
        - u ** 1.5
        + v ** 1.5
        - np.maximum(v_y, 0.0) ** 1.5
        - 2.0
        * np.maximum(
            interval_square,
            0.0,
        ) ** 1.5
    ) / 8.0

    ell = ell_norm * proper_time

    valid = (
        inside
        & (
            distinguishing_fraction
            >= -1.0e-9
        )
        & (
            distinguishing_fraction < 1.0
        )
    )

    log_ratio = np.full(
        samples,
        -np.inf,
    )

    d_value = np.clip(
        distinguishing_fraction[valid],
        0.0,
        1.0 - 1.0e-15,
    )

    log_ratio[valid] = (
        (n - 2)
        * np.log1p(-d_value)
        + n * ell[valid]
    )

    ratio = np.exp(
        np.minimum(log_ratio, 700.0)
    )
    ratio[
        ~np.isfinite(ratio)
    ] = 0.0

    weights = (
        C3
        * (n - 1)
        / (n * n)
        * ratio
    )

    mean = float(weights.mean())
    standard_error = float(
        weights.std(ddof=1)
        / math.sqrt(samples)
    )

    return {
        "dimension": 3,
        "n": n,
        "samples": samples,
        "seed": seed,
        "mean_twin_pairs": mean,
        "standard_error": standard_error,
        "n_times_mean": n * mean,
        "n_times_standard_error": (
            n * standard_error
        ),
        "proposal_inside_fraction": (
            float(inside.mean())
        ),
        "candidate_limit_n_times_mean": C3,
    }


def d4_expected_twins(
    n: int,
    samples: int,
    seed: int,
) -> dict:
    rng = np.random.default_rng(seed)

    # Limiting radial proposal:
    # p(A,C) proportional to (C-A) exp(-(C^2-A^2)).
    u1 = np.maximum(
        np.abs(
            rng.normal(
                scale=1.0 / math.sqrt(2.0),
                size=samples,
            )
        ),
        1.0e-14,
    )
    u2 = np.maximum(
        np.abs(
            rng.normal(
                scale=1.0 / math.sqrt(2.0),
                size=samples,
            )
        ),
        1.0e-14,
    )

    s1 = (
        u1
        + rng.exponential(
            scale=1.0 / u1
        )
    )
    s2 = (
        u2
        + rng.exponential(
            scale=1.0 / u2
        )
    )

    A = (s1 - u1) / 2.0
    C = (s1 + u1) / 2.0
    D = (s2 - u2) / 2.0
    B = (s2 + u2) / 2.0

    sqrt_n = math.sqrt(n)

    a_x = 2.0 * A / sqrt_n
    b_x = 2.0 * B / sqrt_n
    a_y = 2.0 * C / sqrt_n
    b_y = 2.0 * D / sqrt_n

    time_x = (a_x - b_x) / 2.0
    radius_x = 1.0 - (
        a_x + b_x
    ) / 2.0

    time_y = (a_y - b_y) / 2.0
    radius_y = 1.0 - (
        a_y + b_y
    ) / 2.0

    valid = (
        (radius_x >= 0.0)
        & (radius_y >= 0.0)
    )

    delta_time = time_y - time_x

    denominator = (
        2.0
        * radius_x
        * radius_y
    )

    cosine_threshold = np.ones(
        samples
    )

    radial_mask = (
        valid
        & (denominator > 0.0)
        & (delta_time > 0.0)
    )

    cosine_threshold[
        radial_mask
    ] = (
        radius_x[radial_mask] ** 2
        + radius_y[radial_mask] ** 2
        - delta_time[radial_mask] ** 2
    ) / denominator[radial_mask]

    cap_probability = np.zeros(
        samples
    )

    cap_probability[
        radial_mask
    ] = np.where(
        cosine_threshold[
            radial_mask
        ] <= -1.0,
        1.0,
        np.where(
            cosine_threshold[
                radial_mask
            ] < 1.0,
            (
                1.0
                - cosine_threshold[
                    radial_mask
                ]
            ) / 2.0,
            0.0,
        ),
    )

    active = cap_probability > 0.0

    cosine = np.ones(samples)
    lower = np.maximum(
        cosine_threshold[active],
        -1.0,
    )

    cosine[active] = (
        lower
        + (1.0 - lower)
        * rng.random(
            np.count_nonzero(active)
        )
    )

    spatial_distance_square = (
        radius_x * radius_x
        + radius_y * radius_y
        - 2.0
        * radius_x
        * radius_y
        * cosine
    )

    interval_square = (
        delta_time * delta_time
        - spatial_distance_square
    )

    u_x = a_x * (2.0 - b_x)
    v_x = b_x * (2.0 - a_x)
    u_y = a_y * (2.0 - b_y)
    v_y = b_y * (2.0 - a_y)

    distinguishing_fraction = (
        u_y * u_y
        - u_x * u_x
        + v_x * v_x
        - v_y * v_y
        - 2.0
        * np.maximum(
            interval_square,
            0.0,
        ) ** 2
    ) / 16.0

    exponent = (
        C * C
        - A * A
        + B * B
        - D * D
    )

    radial_base_over_proposal = (
        np.zeros(samples)
    )

    proposal_mask = (
        valid
        & (u1 > 0.0)
        & (u2 > 0.0)
    )

    radial_base_over_proposal[
        proposal_mask
    ] = (
        144.0
        * radius_x[
            proposal_mask
        ] ** 2
        * radius_y[
            proposal_mask
        ] ** 2
        / (n * n)
        * I1 * I1
        * np.exp(
            np.minimum(
                exponent[
                    proposal_mask
                ],
                700.0,
            )
        )
        / (
            u1[proposal_mask]
            * u2[proposal_mask]
        )
    )

    target = np.zeros(samples)

    target_mask = (
        active
        & (
            distinguishing_fraction
            >= -1.0e-10
        )
        & (
            distinguishing_fraction < 1.0
        )
    )

    d_value = np.clip(
        distinguishing_fraction[
            target_mask
        ],
        0.0,
        1.0 - 1.0e-15,
    )

    target[target_mask] = np.exp(
        (n - 2)
        * np.log1p(-d_value)
    )

    weights = (
        radial_base_over_proposal
        * cap_probability
        * target
    )

    weights[
        ~np.isfinite(weights)
    ] = 0.0

    # n(n-1) = 2*binom(n,2), accounting for the two causal directions.
    weights *= n * (n - 1)

    mean = float(weights.mean())
    standard_error = float(
        weights.std(ddof=1)
        / math.sqrt(samples)
    )

    return {
        "dimension": 4,
        "n": n,
        "samples": samples,
        "seed": seed,
        "mean_twin_pairs": mean,
        "standard_error": standard_error,
        "n_times_mean": n * mean,
        "n_times_standard_error": (
            n * standard_error
        ),
        "valid_radial_fraction": (
            float(valid.mean())
        ),
        "candidate_limit_n_times_mean": C4,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dimension",
        type=int,
        choices=(3, 4),
        required=True,
    )
    parser.add_argument(
        "--n",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--samples",
        type=int,
        default=500000,
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=20261111,
    )
    args = parser.parse_args()

    if args.dimension == 3:
        result = d3_expected_twins(
            args.n,
            args.samples,
            args.seed,
        )
    else:
        result = d4_expected_twins(
            args.n,
            args.samples,
            args.seed,
        )

    print(
        json.dumps(
            result,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
