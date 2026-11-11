#!/usr/bin/env python3
"""Residual higher-dimensional UPO obstruction audit.

Exploratory follow-up after the preregistered adjacent-twin held-out test.

For each Minkowski sprinkling, classify:
- UPO;
- non-UPO with at least one adjacent twin pair;
- residual non-UPO with no adjacent twin pair.

Residual failures are then split into:
- multiple nontrivial connected components;
- one nontrivial component, hence internal ambiguity beyond size-two twins.

The UPO test uses classical comparability forcing/color classes and does not
use a permutation representation.
"""

from __future__ import annotations

import itertools
import json
import numpy as np


SCHEDULE = (
    (3, 48, 2000, 202611113048),
    (3, 64, 1200, 202611143064),
    (3, 96, 800, 202611143096),
    (3, 128, 400, 202611143128),
    (4, 48, 2000, 202611114048),
    (4, 64, 1200, 202611144064),
    (4, 96, 800, 202611144096),
    (4, 128, 400, 202611144128),
)

EXACT_UPO_COUNTS = {
    2: 1,
    3: 4,
    4: 12,
    5: 38,
    6: 165,
    7: 1042,
}


def sprinkle(n, d, rng):
    s = d - 1
    absolute_time = (
        1.0
        - rng.random(n) ** (1.0 / d)
    )
    time = np.where(
        rng.random(n) < 0.5,
        absolute_time,
        -absolute_time,
    )

    direction = rng.normal(size=(n, s))
    direction /= np.linalg.norm(
        direction,
        axis=1,
    )[:, None]

    radius = (
        (1.0 - absolute_time)
        * rng.random(n) ** (1.0 / s)
    )

    return (
        time,
        direction * radius[:, None],
    )


def adjacency_from_points(time, space):
    delta_time = (
        time[:, None]
        - time[None, :]
    )

    norm_square = np.sum(
        space * space,
        axis=1,
    )

    distance_square = (
        norm_square[:, None]
        + norm_square[None, :]
        - 2.0 * space @ space.T
    )

    adjacency = (
        delta_time * delta_time
        >
        distance_square + 1.0e-14
    )

    np.fill_diagonal(adjacency, False)
    return adjacency


def adjacent_twin_pair_count(adjacency):
    closed = adjacency.copy()
    np.fill_diagonal(closed, True)

    packed = np.packbits(
        closed,
        axis=1,
        bitorder="little",
    )

    _, counts = np.unique(
        packed,
        axis=0,
        return_counts=True,
    )

    return int(
        np.sum(
            counts
            * (counts - 1)
            // 2
        )
    )


def edge_data(adjacency):
    n = len(adjacency)
    first, second = np.where(
        np.triu(adjacency, 1)
    )

    incident = [
        []
        for _ in range(n)
    ]

    for edge_id, (u, v) in enumerate(
        zip(
            first.tolist(),
            second.tolist(),
        )
    ):
        incident[u].append(
            (edge_id, v)
        )
        incident[v].append(
            (edge_id, u)
        )

    return first, second, incident


def is_upo_by_forcing(adjacency):
    first, second, incident = (
        edge_data(adjacency)
    )
    edge_count = len(first)

    if edge_count == 0:
        return False

    seen = np.zeros(
        edge_count,
        dtype=bool,
    )
    seen[0] = True
    visited = 1
    stack = [0]

    while stack:
        edge_id = stack.pop()
        u = int(first[edge_id])
        v = int(second[edge_id])

        for other_edge, w in incident[u]:
            if (
                not seen[other_edge]
                and not adjacency[v, w]
            ):
                seen[other_edge] = True
                visited += 1
                stack.append(other_edge)

        for other_edge, w in incident[v]:
            if (
                not seen[other_edge]
                and not adjacency[u, w]
            ):
                seen[other_edge] = True
                visited += 1
                stack.append(other_edge)

    return visited == edge_count


def nontrivial_component_count(adjacency):
    n = len(adjacency)
    seen = np.zeros(n, dtype=bool)
    count = 0

    for start in range(n):
        if seen[start]:
            continue

        stack = [start]
        seen[start] = True
        degree_sum = 0

        while stack:
            u = stack.pop()
            neighbors = np.flatnonzero(
                adjacency[u]
            )
            degree_sum += len(neighbors)

            for v in neighbors:
                if not seen[v]:
                    seen[v] = True
                    stack.append(int(v))

        if degree_sum > 0:
            count += 1

    return count


def permutation_adjacency(permutation):
    n = len(permutation)
    adjacency = np.zeros(
        (n, n),
        dtype=bool,
    )

    for i in range(n):
        for j in range(i + 1, n):
            if (
                permutation[i]
                < permutation[j]
            ):
                adjacency[i, j] = True
                adjacency[j, i] = True

    return adjacency


def exact_classifier_regression():
    observed = {}

    for n, expected in (
        EXACT_UPO_COUNTS.items()
    ):
        count = 0

        for permutation in (
            itertools.permutations(
                range(n)
            )
        ):
            adjacency = (
                permutation_adjacency(
                    permutation
                )
            )

            count += int(
                is_upo_by_forcing(
                    adjacency
                )
            )

        assert count == expected
        observed[str(n)] = count

    return {
        "status": "PASS",
        "observed": observed,
    }


def run_block(d, n, trials, seed):
    rng = np.random.default_rng(seed)

    upo = 0
    failure = 0
    failure_with_twin = 0
    residual = 0
    residual_multi = 0
    residual_internal = 0
    any_twin = 0
    multiple_nontrivial = 0

    for _ in range(trials):
        time, space = sprinkle(
            n,
            d,
            rng,
        )
        adjacency = (
            adjacency_from_points(
                time,
                space,
            )
        )

        twins = (
            adjacent_twin_pair_count(
                adjacency
            )
        )

        if twins:
            any_twin += 1

        nontrivial_components = (
            nontrivial_component_count(
                adjacency
            )
        )

        if nontrivial_components >= 2:
            multiple_nontrivial += 1

        if is_upo_by_forcing(
            adjacency
        ):
            upo += 1
            continue

        failure += 1

        if twins:
            failure_with_twin += 1
            continue

        residual += 1

        if nontrivial_components >= 2:
            residual_multi += 1
        elif nontrivial_components == 1:
            residual_internal += 1

    return {
        "dimension": d,
        "n": n,
        "trials": trials,
        "seed": seed,
        "upo_count": upo,
        "failure_count": failure,
        "failure_with_twin_count": (
            failure_with_twin
        ),
        "residual_no_twin_count": residual,
        "residual_multiple_component_count": (
            residual_multi
        ),
        "residual_internal_count": (
            residual_internal
        ),
        "any_twin_count": any_twin,
        "multiple_nontrivial_component_count": (
            multiple_nontrivial
        ),
        "p_upo": upo / trials,
        "p_failure": failure / trials,
        "p_residual_no_twin": (
            residual / trials
        ),
        "p_residual_multiple_component": (
            residual_multi / trials
        ),
        "p_residual_internal": (
            residual_internal / trials
        ),
        "fraction_failures_with_twin": (
            failure_with_twin / failure
            if failure
            else None
        ),
    }


def main():
    result = {
        "audit": (
            "MINKOWSKI_RESIDUAL_UPO_"
            "OBSTRUCTION_V1"
        ),
        "status": "EXPLORATORY",
        "classifier_regression": (
            exact_classifier_regression()
        ),
        "runs": [
            run_block(
                d,
                n,
                trials,
                seed,
            )
            for d, n, trials, seed
            in SCHEDULE
        ],
        "nonclaims": [
            "No residual asymptotic law is inferred.",
            "The n=128 blocks are small and zero observed residuals are not zero-probability claims.",
            "Adjacent twins are sufficient but not necessary for UPO failure.",
            "No claim that higher-dimensional UPO probability tends to one is made."
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
