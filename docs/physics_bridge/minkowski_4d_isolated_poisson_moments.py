#!/usr/bin/env python3
"""Finite factorial-moment audit for isolated vertices in 3+1 Minkowski.

The graph is the undirected causal-comparability graph of n iid uniform points
in the standard Alexandrov interval between (-1,0,0,0) and (1,0,0,0).

The analytic expectation calculation in this repository predicts

    E[I_n] -> 3*pi.

This script tests the stronger conjecture

    I_n => Poisson(3*pi)

by reporting the Fano factor and normalized factorial moments.  For a Poisson
random variable all normalized factorial moments equal one.

This is a finite Monte Carlo diagnostic, not a proof.
"""

from __future__ import annotations

import argparse
import json
import math

import numpy as np


DEFAULT_SCHEDULE = (
    (128, 1500, 94128),
    (256, 1000, 94256),
    (512, 1000, 94512),
    (1024, 500, 95024),
    (2048, 500, 962048),
)


def sprinkle(n: int, rng: np.random.Generator):
    d = 4
    spatial_dimension = 3

    absolute_time = (
        1.0
        - rng.random(n) ** (1.0 / d)
    )
    time = np.where(
        rng.random(n) < 0.5,
        absolute_time,
        -absolute_time,
    )

    direction = rng.normal(
        size=(n, spatial_dimension)
    )
    direction /= np.linalg.norm(
        direction,
        axis=1,
    )[:, None]

    radius = (
        (1.0 - absolute_time)
        * rng.random(n) ** (
            1.0 / spatial_dimension
        )
    )

    return (
        time,
        direction * radius[:, None],
    )


def isolated_vertex_count(
    n: int,
    rng: np.random.Generator,
) -> int:
    time, space = sprinkle(n, rng)

    delta_time = (
        time[:, None]
        - time[None, :]
    )

    norm_square = np.sum(
        space * space,
        axis=1,
    )

    spatial_distance_square = (
        norm_square[:, None]
        + norm_square[None, :]
        - 2.0 * space @ space.T
    )

    adjacency = (
        delta_time * delta_time
        >
        spatial_distance_square
        + 1.0e-14
    )

    np.fill_diagonal(
        adjacency,
        False,
    )

    return int(
        np.sum(
            ~adjacency.any(axis=1)
        )
    )


def run_block(
    n: int,
    trials: int,
    seed: int,
) -> dict:
    rng = np.random.default_rng(seed)

    counts = np.empty(
        trials,
        dtype=np.int32,
    )

    for index in range(trials):
        counts[index] = (
            isolated_vertex_count(
                n,
                rng,
            )
        )

    mean = float(counts.mean())
    variance = float(
        counts.var(ddof=1)
    )

    factorial_2 = float(
        np.mean(
            counts
            * (counts - 1)
        )
    )

    factorial_3 = float(
        np.mean(
            counts
            * (counts - 1)
            * (counts - 2)
        )
    )

    return {
        "n": n,
        "trials": trials,
        "seed": seed,
        "mean": mean,
        "variance": variance,
        "fano_factor": (
            variance / mean
        ),
        "p_zero": float(
            np.mean(counts == 0)
        ),
        "factorial_moment_2": (
            factorial_2
        ),
        "factorial_moment_2_ratio": (
            factorial_2 / mean**2
        ),
        "factorial_moment_3": (
            factorial_3
        ),
        "factorial_moment_3_ratio": (
            factorial_3 / mean**3
        ),
        "maximum": int(counts.max()),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--single-n",
        type=int,
        default=None,
    )
    parser.add_argument(
        "--trials",
        type=int,
        default=500,
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=20261111,
    )
    args = parser.parse_args()

    if args.single_n is None:
        schedule = DEFAULT_SCHEDULE
    else:
        schedule = (
            (
                args.single_n,
                args.trials,
                args.seed,
            ),
        )

    result = {
        "audit": (
            "MINKOWSKI_4D_ISOLATED_"
            "POISSON_MOMENTS_V1"
        ),
        "candidate_limit": {
            "distribution": (
                "Poisson(3*pi)"
            ),
            "mean": 3.0 * math.pi,
            "p_zero": math.exp(
                -3.0 * math.pi
            ),
        },
        "runs": [
            run_block(
                n,
                trials,
                seed,
            )
            for n, trials, seed
            in schedule
        ],
        "nonclaims": [
            "Finite factorial-moment agreement is not a proof of distributional convergence.",
            "The general Penrose 2018 homogeneous IRG theorem does not apply directly to this deterministic, boundary-degenerate causal kernel.",
            "A proof still requires control of interacting isolated candidates in shrinking angular collision regions.",
        ],
    }

    print(
        json.dumps(
            result,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
