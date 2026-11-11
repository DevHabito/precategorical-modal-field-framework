#!/usr/bin/env python3
"""Held-out adjacent-twin scaling test for Minkowski comparability graphs.

The exponent hypothesis was frozen beforehand in:
docs/physics_bridge/ADJACENT_TWIN_SCALING_PREREGISTRATION_20261111.md
(commit 01d38cafb959ab395c2c1666ad9be143335e2a5f).

Held-out targets:
  d = 3, 4 spacetime dimensions
  n = 320, 384
  2500 trials per target

Primary diagnostic:
  n * E[T_n]

The preregistered prediction is E[T_n] = Theta(1/n) for both d=3 and d=4.
No asymptotic constant was preregistered.
"""

from __future__ import annotations

import json
import math
import numpy as np


TARGETS = (
    (3, 320, 2500, 202611113320),
    (3, 384, 2500, 202611113384),
    (4, 320, 2500, 202611114320),
    (4, 384, 2500, 202611114384),
)


def sprinkle(n: int, d: int, rng: np.random.Generator):
    spatial_dimension = d - 1

    absolute_time = 1.0 - rng.random(n) ** (1.0 / d)
    time = np.where(
        rng.random(n) < 0.5,
        absolute_time,
        -absolute_time,
    )

    directions = rng.normal(
        size=(n, spatial_dimension)
    )
    directions /= np.linalg.norm(
        directions,
        axis=1,
    )[:, None]

    radius = (
        (1.0 - absolute_time)
        * rng.random(n) ** (
            1.0 / spatial_dimension
        )
    )

    space = directions * radius[:, None]
    return time, space


def comparability_adjacency(
    time: np.ndarray,
    space: np.ndarray,
) -> np.ndarray:
    delta_time = (
        time[:, None]
        - time[None, :]
    )

    spatial_norm_square = np.sum(
        space * space,
        axis=1,
    )

    spatial_distance_square = (
        spatial_norm_square[:, None]
        + spatial_norm_square[None, :]
        - 2.0 * space @ space.T
    )

    adjacency = (
        delta_time * delta_time
        >
        spatial_distance_square + 1.0e-15
    )

    np.fill_diagonal(adjacency, False)
    return adjacency


def adjacent_twin_pair_count(
    adjacency: np.ndarray,
) -> int:
    """Count adjacent twin pairs.

    Two adjacent vertices are twins iff their closed neighborhoods are
    identical.  Packing each closed-neighborhood row and grouping equal rows
    therefore counts all such pairs exactly.
    """
    closed = adjacency.copy()
    np.fill_diagonal(closed, True)

    packed = np.packbits(
        closed,
        axis=1,
        bitorder="little",
    )

    _, multiplicities = np.unique(
        packed,
        axis=0,
        return_counts=True,
    )

    return int(
        np.sum(
            multiplicities
            * (multiplicities - 1)
            // 2
        )
    )


def direct_adjacent_twin_pair_count(
    adjacency: np.ndarray,
) -> int:
    """Literal O(n^3) definition used only for regression."""
    n = adjacency.shape[0]
    count = 0

    for u in range(n):
        for v in range(u + 1, n):
            if not adjacency[u, v]:
                continue

            same_external_neighborhood = True

            for w in range(n):
                if w == u or w == v:
                    continue

                if (
                    bool(adjacency[u, w])
                    != bool(adjacency[v, w])
                ):
                    same_external_neighborhood = False
                    break

            if same_external_neighborhood:
                count += 1

    return count


def detector_self_test() -> dict:
    rng = np.random.default_rng(731991)
    checks = 0

    for d in (2, 3, 4):
        for n in (7, 11, 17, 23):
            for _ in range(100):
                time, space = sprinkle(
                    n,
                    d,
                    rng,
                )
                adjacency = (
                    comparability_adjacency(
                        time,
                        space,
                    )
                )

                fast = (
                    adjacent_twin_pair_count(
                        adjacency
                    )
                )
                direct = (
                    direct_adjacent_twin_pair_count(
                        adjacency
                    )
                )

                assert fast == direct
                checks += 1

    return {
        "status": "PASS",
        "checks": checks,
        "seed": 731991,
    }


def wilson_interval(
    successes: int,
    trials: int,
) -> tuple[float, float]:
    z = 1.959963984540054
    p = successes / trials
    denominator = 1.0 + z * z / trials

    center = (
        p + z * z / (2.0 * trials)
    ) / denominator

    half_width = (
        z
        * math.sqrt(
            p * (1.0 - p) / trials
            + z * z / (
                4.0 * trials * trials
            )
        )
        / denominator
    )

    return (
        center - half_width,
        center + half_width,
    )


def run_target(
    d: int,
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
        time, space = sprinkle(
            n,
            d,
            rng,
        )
        adjacency = comparability_adjacency(
            time,
            space,
        )
        counts[index] = (
            adjacent_twin_pair_count(
                adjacency
            )
        )

    mean = float(counts.mean())
    variance = float(counts.var(ddof=1))
    standard_error = math.sqrt(
        variance / trials
    )
    z = 1.959963984540054

    any_count = int(
        np.count_nonzero(counts)
    )

    return {
        "dimension": d,
        "n": n,
        "trials": trials,
        "seed": seed,
        "total_twin_pairs": int(
            counts.sum()
        ),
        "mean_twin_pairs": mean,
        "mean_twin_pairs_ci95_normal": [
            max(
                0.0,
                mean - z * standard_error,
            ),
            mean + z * standard_error,
        ],
        "variance": variance,
        "samples_with_any_twin": any_count,
        "p_any_twin": (
            any_count / trials
        ),
        "p_any_twin_wilson95": (
            wilson_interval(
                any_count,
                trials,
            )
        ),
        "n_times_mean": n * mean,
        "maximum_twin_pairs_in_one_sample": (
            int(counts.max())
        ),
    }


def main() -> None:
    result = {
        "audit": "ADJACENT_TWIN_HELDOUT_SCALING_V1",
        "preregistration_commit": (
            "01d38cafb959ab395c2c1666ad9be143335e2a5f"
        ),
        "prediction": (
            "E[T_n] = Theta(1/n) "
            "for d=3 and d=4"
        ),
        "self_test": detector_self_test(),
        "targets": [
            run_target(
                d,
                n,
                trials,
                seed,
            )
            for d, n, trials, seed
            in TARGETS
        ],
        "interpretation_rule": (
            "Primary diagnostic is n*E[T_n]. "
            "No constant was preregistered."
        ),
        "nonclaims": [
            "A finite scaling-consistency pass is not an asymptotic proof.",
            "The normal interval for the rare-count mean is diagnostic only.",
            "Vanishing adjacent twins would not by itself prove UPO probability tends to one.",
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
