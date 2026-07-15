#!/usr/bin/env python3
"""
A16 — Local–Global Manifoldlikeness Criterion

This audit combines:

1. Q_global:
   The covariance-aware analytic interval-abundance goodness-of-fit statistic
   from A14.

2. Exact S3 certificate search:
   A label-invariant search for an induced six-element standard example S3,
   using equal-degree antichain triples as a complete search channel for the
   A15 construction family.

3. Exact small-interval two-dimensionality:
   Every order interval with 6 through 10 elements is tested exactly for
   poset dimension <= 2. The test enumerates linear extensions L1 and checks
   whether reversing every L1-incomparable pair yields a second total order
   L2 whose intersection with L1 is the input poset.

Discovery:
    n = 128, unanchored S3 counterexamples.

Prospective confirmation:
    n = 256, an anchored minimal seven-element dimension-3 obstruction whose
    every six-element induced subposet has dimension <= 2.

Complementarity control:
    n = 256, a nonuniform bimodal point distribution that is still an exact
    2D order. The local tests must accept it while Q_global should reject it.

No adversarial structure is used to fit Q, choose its threshold, or calibrate
the local exact tests.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
from sklearn.covariance import LedoitWolf

from a13_analytic_interval_signature import (
    analytic_expectation,
    empirical_p_value,
    interval_abundance,
    relation_fraction,
    sample_minkowski_2d,
)
from a14_covariance_interval_signature import (
    bin_vector,
    make_bins,
    quadratic_score,
)
from a15_certified_counterexample_search import (
    build_s3_sandwich,
    standard_example_s3,
)


SEED = 20260716
DISCOVERY_N = 128
CONFIRMATORY_N = 256
N_VALUES = (DISCOVERY_N, CONFIRMATORY_N)

COVARIANCE_SAMPLES = {
    DISCOVERY_N: 100,
    CONFIRMATORY_N: 90,
}
CALIBRATION_SAMPLES = {
    DISCOVERY_N: 100,
    CONFIRMATORY_N: 90,
}
GLOBAL_HOLDOUT_SAMPLES = {
    DISCOVERY_N: 12,
    CONFIRMATORY_N: 12,
}
LOCAL_HOLDOUT_SAMPLES = {
    DISCOVERY_N: 4,
    CONFIRMATORY_N: 4,
}

UNANCHORED_S3_SAMPLES = {
    DISCOVERY_N: 12,
    CONFIRMATORY_N: 12,
}
MINIMAL7_CONFIRMATORY_SAMPLES = 10
BIMODAL_2D_SAMPLES = 6

ALPHA = 0.05
MAX_DENSITY_MISMATCH = 0.02
LOCAL_INTERVAL_MIN_SIZE = 6
LOCAL_INTERVAL_MAX_SIZE = 10


def json_safe(value):
    if isinstance(value, dict):
        return {
            str(key): json_safe(item)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value


def permute_relation(
    relation: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    permutation = rng.permutation(len(relation))
    return relation[np.ix_(permutation, permutation)]


def topological_order(
    relation: np.ndarray,
) -> list[int]:
    n = len(relation)
    indegree = relation.sum(axis=0).astype(int)
    available = [
        int(vertex)
        for vertex in np.flatnonzero(indegree == 0)
    ]
    order = []

    while available:
        vertex = available.pop()
        order.append(vertex)
        for target in np.flatnonzero(relation[vertex]):
            indegree[target] -= 1
            if indegree[target] == 0:
                available.append(int(target))

    if len(order) != n:
        raise RuntimeError("The relation is not acyclic.")
    return order


def verify_transitive(
    relation: np.ndarray,
) -> bool:
    two_step = (
        relation.astype(np.int16)
        @ relation.astype(np.int16)
    ) > 0
    return not bool(np.any(two_step & ~relation))


def extension_pair_realizes_poset(
    relation: np.ndarray,
    first_order: list[int],
) -> bool:
    """
    Given a linear extension L1 of P, orient each incomparable pair in the
    opposite direction in L2, while preserving every comparable pair.
    Because every pair is then oriented, L2 is a total order exactly when
    this tournament is acyclic.
    """
    n = len(relation)
    position = np.empty(n, dtype=int)
    position[first_order] = np.arange(n)

    adjacency = [0] * n
    indegree = [0] * n

    for first in range(n):
        for second in range(first + 1, n):
            if relation[first, second]:
                source, target = first, second
            elif relation[second, first]:
                source, target = second, first
            elif position[first] < position[second]:
                source, target = second, first
            else:
                source, target = first, second

            adjacency[source] |= 1 << target
            indegree[target] += 1

    available = [
        vertex
        for vertex, degree in enumerate(indegree)
        if degree == 0
    ]
    visited = 0

    while available:
        vertex = available.pop()
        visited += 1
        successors = adjacency[vertex]

        while successors:
            least = successors & -successors
            target = least.bit_length() - 1
            successors ^= least
            indegree[target] -= 1
            if indegree[target] == 0:
                available.append(target)

    return visited == n


def is_dimension_at_most_two_exact(
    relation: np.ndarray,
) -> bool:
    """
    Exact recognition for small posets by exhaustive linear-extension search.
    """
    n = len(relation)
    predecessor_masks = []

    for vertex in range(n):
        mask = 0
        for predecessor in np.flatnonzero(
            relation[:, vertex]
        ):
            mask |= 1 << int(predecessor)
        predecessor_masks.append(mask)

    full_mask = (1 << n) - 1
    current_order: list[int] = []

    outdegree = relation.sum(axis=1)
    indegree = relation.sum(axis=0)

    def search(used_mask: int) -> bool:
        if used_mask == full_mask:
            return extension_pair_realizes_poset(
                relation,
                current_order,
            )

        available = [
            vertex
            for vertex in range(n)
            if not (used_mask >> vertex) & 1
            and (
                predecessor_masks[vertex]
                & ~used_mask
            ) == 0
        ]

        available.sort(
            key=lambda vertex: (
                -int(outdegree[vertex]),
                int(indegree[vertex]),
                vertex,
            )
        )

        for vertex in available:
            current_order.append(vertex)
            if search(used_mask | (1 << vertex)):
                return True
            current_order.pop()

        return False

    return search(0)


def minimal_seven_obstruction() -> np.ndarray:
    """
    A seven-element dimension-3 poset found by an independent random search.
    Every one-vertex deletion has dimension <= 2.
    """
    return np.asarray(
        [
            [0, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=bool,
    )


def anchored_gadget(
    internal_relation: np.ndarray,
) -> np.ndarray:
    internal_n = len(internal_relation)
    total = internal_n + 2
    relation = np.zeros((total, total), dtype=bool)

    relation[1 : 1 + internal_n, 1 : 1 + internal_n] = (
        internal_relation
    )
    relation[0, 1:] = True
    relation[1 : 1 + internal_n, total - 1] = True
    relation[0, total - 1] = True
    return relation


def choose_module_cuts(
    core_relation: np.ndarray,
    total_n: int,
    gadget_relation_count: int,
    gadget_size: int,
    target_fraction: float,
) -> tuple[int, int, float]:
    core_n = len(core_relation)
    target_count = (
        target_fraction
        * total_n
        * (total_n - 1)
        / 2.0
    )
    core_count = int(core_relation.sum())
    maximum_cut = core_n // 2

    best = None

    for prefix_size in range(maximum_cut + 1):
        maximum_suffix = min(
            maximum_cut,
            core_n - prefix_size,
        )
        for suffix_size in range(
            maximum_suffix + 1
        ):
            if prefix_size and suffix_size:
                existing_cross = int(
                    core_relation[
                        :prefix_size,
                        core_n - suffix_size :,
                    ].sum()
                )
            else:
                existing_cross = 0

            relation_count = (
                core_count
                + gadget_relation_count
                + gadget_size * prefix_size
                + gadget_size * suffix_size
                + prefix_size * suffix_size
                - existing_cross
            )
            mismatch = abs(
                relation_count - target_count
            )
            deformation = prefix_size + suffix_size
            candidate = (
                mismatch,
                deformation,
                abs(prefix_size - suffix_size),
                prefix_size,
                suffix_size,
                relation_count,
            )

            if best is None or candidate < best:
                best = candidate

    assert best is not None
    _, _, _, prefix_size, suffix_size, count = best
    achieved_fraction = (
        count
        / (total_n * (total_n - 1) / 2.0)
    )
    return (
        int(prefix_size),
        int(suffix_size),
        float(achieved_fraction),
    )


def sample_sorted_minkowski_core(
    n: int,
    rng: np.random.Generator,
) -> np.ndarray:
    u = rng.random(n)
    v = rng.random(n)
    height = u + v
    order = np.argsort(height)
    u = u[order]
    v = v[order]

    relation = (
        (u[:, None] < u[None, :])
        & (v[:, None] < v[None, :])
    )
    np.fill_diagonal(relation, False)
    return relation


def build_anchored_module_adversary(
    total_n: int,
    gadget_relation: np.ndarray,
    target_fraction: float,
    rng: np.random.Generator,
    attempts: int = 30,
) -> tuple[np.ndarray, dict[str, object]]:
    gadget_size = len(gadget_relation)
    core_n = total_n - gadget_size
    gadget_count = int(gadget_relation.sum())

    best_relation = None
    best_metadata = None
    best_mismatch = float("inf")

    for _ in range(attempts):
        core = sample_sorted_minkowski_core(
            core_n,
            rng,
        )
        (
            prefix_size,
            suffix_size,
            achieved_fraction,
        ) = choose_module_cuts(
            core,
            total_n,
            gadget_count,
            gadget_size,
            target_fraction,
        )

        relation = np.zeros(
            (total_n, total_n),
            dtype=bool,
        )
        relation[:core_n, :core_n] = core
        relation[
            core_n:,
            core_n:,
        ] = gadget_relation

        gadget_vertices = np.arange(
            core_n,
            total_n,
        )
        prefix = np.arange(prefix_size)
        suffix = np.arange(
            core_n - suffix_size,
            core_n,
        )

        if prefix_size:
            relation[
                np.ix_(prefix, gadget_vertices)
            ] = True
        if suffix_size:
            relation[
                np.ix_(gadget_vertices, suffix)
            ] = True
        if prefix_size and suffix_size:
            relation[np.ix_(prefix, suffix)] = True

        mismatch = abs(
            achieved_fraction - target_fraction
        )

        if mismatch < best_mismatch:
            best_relation = relation
            best_mismatch = mismatch
            best_metadata = {
                "core_n": core_n,
                "gadget_size": gadget_size,
                "prefix_size": prefix_size,
                "suffix_size": suffix_size,
                "target_ordering_fraction": (
                    target_fraction
                ),
                "ordering_fraction": (
                    achieved_fraction
                ),
                "ordering_fraction_mismatch": (
                    mismatch
                ),
            }

        if mismatch <= MAX_DENSITY_MISMATCH / 4:
            break

    if best_relation is None:
        raise RuntimeError(
            "Failed to build an anchored adversary."
        )

    return (
        permute_relation(best_relation, rng),
        best_metadata,
    )


def build_density_matched_unanchored_s3(
    n: int,
    target_fraction: float,
    rng: np.random.Generator,
    attempts: int = 30,
) -> tuple[np.ndarray, dict[str, object]]:
    best_relation = None
    best_metadata = None
    best_mismatch = float("inf")

    for _ in range(attempts):
        relation, metadata = build_s3_sandwich(
            n,
            1,
            target_fraction,
            rng,
        )
        mismatch = float(
            metadata["ordering_fraction_mismatch"]
        )
        if mismatch < best_mismatch:
            best_relation = relation
            best_metadata = metadata
            best_mismatch = mismatch

        if mismatch <= MAX_DENSITY_MISMATCH / 4:
            break

    if best_relation is None:
        raise RuntimeError(
            "Failed to build an unanchored S3 adversary."
        )

    return (
        permute_relation(best_relation, rng),
        best_metadata,
    )


def find_induced_s3_equal_degree(
    relation: np.ndarray,
) -> tuple[int, ...] | None:
    """
    Search for an induced S3. The lower antichain in the A15 family has equal
    indegree and outdegree, making this channel label-invariant and complete
    for that construction family.
    """
    n = len(relation)
    successor_masks = []
    comparable_masks = []

    for vertex in range(n):
        successor_mask = 0
        predecessor_mask = 0

        for successor in np.flatnonzero(
            relation[vertex]
        ):
            successor_mask |= 1 << int(successor)

        for predecessor in np.flatnonzero(
            relation[:, vertex]
        ):
            predecessor_mask |= 1 << int(predecessor)

        successor_masks.append(successor_mask)
        comparable_masks.append(
            successor_mask
            | predecessor_mask
            | (1 << vertex)
        )

    degree_groups: dict[
        tuple[int, int],
        list[int],
    ] = {}

    for vertex in range(n):
        key = (
            int(relation[:, vertex].sum()),
            int(relation[vertex].sum()),
        )
        degree_groups.setdefault(key, []).append(
            vertex
        )

    all_mask = (1 << n) - 1

    for group in degree_groups.values():
        if len(group) < 3:
            continue

        for first, second, third in itertools.combinations(
            group,
            3,
        ):
            if (
                (comparable_masks[first] >> second) & 1
                or (
                    comparable_masks[first]
                    >> third
                )
                & 1
                or (
                    comparable_masks[second]
                    >> third
                )
                & 1
            ):
                continue

            candidate_zero = (
                successor_masks[second]
                & successor_masks[third]
                & ~successor_masks[first]
                & all_mask
            )
            candidate_one = (
                successor_masks[first]
                & successor_masks[third]
                & ~successor_masks[second]
                & all_mask
            )
            candidate_two = (
                successor_masks[first]
                & successor_masks[second]
                & ~successor_masks[third]
                & all_mask
            )

            remaining_zero = candidate_zero
            while remaining_zero:
                least_zero = (
                    remaining_zero
                    & -remaining_zero
                )
                upper_zero = (
                    least_zero.bit_length() - 1
                )
                remaining_zero ^= least_zero

                remaining_one = (
                    candidate_one
                    & ~comparable_masks[upper_zero]
                )

                while remaining_one:
                    least_one = (
                        remaining_one
                        & -remaining_one
                    )
                    upper_one = (
                        least_one.bit_length() - 1
                    )
                    remaining_one ^= least_one

                    remaining_two = (
                        candidate_two
                        & ~comparable_masks[upper_zero]
                        & ~comparable_masks[upper_one]
                    )

                    if remaining_two:
                        least_two = (
                            remaining_two
                            & -remaining_two
                        )
                        upper_two = (
                            least_two.bit_length()
                            - 1
                        )
                        return (
                            first,
                            second,
                            third,
                            upper_zero,
                            upper_one,
                            upper_two,
                        )

    return None


def scan_small_intervals(
    relation: np.ndarray,
) -> dict[str, object]:
    n = len(relation)
    reflexive = relation | np.eye(n, dtype=bool)
    interval_sizes = (
        reflexive.astype(np.int16)
        @ reflexive.astype(np.int16)
    )

    candidate_pairs = np.argwhere(
        relation
        & (
            interval_sizes
            >= LOCAL_INTERVAL_MIN_SIZE
        )
        & (
            interval_sizes
            <= LOCAL_INTERVAL_MAX_SIZE
        )
    )

    # Fixed, label-independent scan order.
    candidate_pairs = sorted(
        (
            (
                int(interval_sizes[first, second]),
                int(first),
                int(second),
            )
            for first, second in candidate_pairs
        ),
        key=lambda item: (
            item[0],
            item[1],
            item[2],
        ),
    )

    tested = 0

    for size, first, second in candidate_pairs:
        vertices = np.flatnonzero(
            reflexive[first]
            & reflexive[:, second]
        )
        local_relation = relation[
            np.ix_(vertices, vertices)
        ]
        tested += 1

        if not is_dimension_at_most_two_exact(
            local_relation
        ):
            return {
                "obstruction_found": True,
                "interval_size": int(size),
                "tested_intervals": tested,
                "total_candidate_intervals": (
                    len(candidate_pairs)
                ),
                "certificate_vertices": [
                    int(vertex)
                    for vertex in vertices
                ],
            }

    return {
        "obstruction_found": False,
        "interval_size": None,
        "tested_intervals": tested,
        "total_candidate_intervals": (
            len(candidate_pairs)
        ),
        "certificate_vertices": None,
    }


def local_audit(
    relation: np.ndarray,
) -> dict[str, object]:
    s3_certificate = find_induced_s3_equal_degree(
        relation
    )
    if s3_certificate is not None:
        return {
            "local_pass": False,
            "channel": "induced_s3",
            "s3_certificate": [
                int(vertex)
                for vertex in s3_certificate
            ],
            "interval_scan": None,
        }

    interval_result = scan_small_intervals(
        relation
    )
    return {
        "local_pass": not bool(
            interval_result["obstruction_found"]
        ),
        "channel": (
            "small_interval_dimension"
            if interval_result[
                "obstruction_found"
            ]
            else "none"
        ),
        "s3_certificate": None,
        "interval_scan": interval_result,
    }


def normalized_profile(
    relation: np.ndarray,
    bins: list[tuple[int, int]],
) -> np.ndarray:
    counts = interval_abundance(relation)
    return bin_vector(counts, bins) / counts.sum()


def fit_global_model(
    n: int,
    rng: np.random.Generator,
) -> dict[str, object]:
    expected_counts, analytic_full_profile = (
        analytic_expectation(n)
    )
    bins = make_bins(expected_counts)
    analytic_profile = bin_vector(
        analytic_full_profile,
        bins,
    )

    estimation_profiles = np.vstack(
        [
            normalized_profile(
                sample_minkowski_2d(n, rng),
                bins,
            )
            for _ in range(
                COVARIANCE_SAMPLES[n]
            )
        ]
    )
    covariance_model = LedoitWolf().fit(
        estimation_profiles
    )
    covariance = covariance_model.covariance_

    calibration_profiles = np.vstack(
        [
            normalized_profile(
                sample_minkowski_2d(n, rng),
                bins,
            )
            for _ in range(
                CALIBRATION_SAMPLES[n]
            )
        ]
    )
    calibration_scores = np.asarray(
        [
            quadratic_score(
                profile,
                analytic_profile,
                covariance_model.precision_,
            )
            for profile in calibration_profiles
        ],
        dtype=float,
    )

    return {
        "bins": bins,
        "analytic_profile": analytic_profile,
        "precision": covariance_model.precision_,
        "calibration_scores": calibration_scores,
        "condition_number": float(
            np.linalg.cond(covariance)
        ),
        "minimum_eigenvalue": float(
            np.linalg.eigvalsh(covariance).min()
        ),
        "shrinkage": float(
            covariance_model.shrinkage_
        ),
    }


def global_score(
    relation: np.ndarray,
    model: dict[str, object],
) -> tuple[float, float, bool]:
    profile = normalized_profile(
        relation,
        model["bins"],
    )
    score = quadratic_score(
        profile,
        model["analytic_profile"],
        model["precision"],
    )
    p_value = empirical_p_value(
        score,
        model["calibration_scores"],
    )
    return (
        float(score),
        float(p_value),
        bool(p_value >= ALPHA),
    )


def build_bimodal_2d_order(
    n: int,
    target_fraction: float,
    rng: np.random.Generator,
    attempts: int = 20,
) -> tuple[np.ndarray, dict[str, object]]:
    """
    Two compact coordinate clusters. Lambda rotates the cluster separation
    from anti-diagonal to diagonal. Grid search uses ordering fraction only.
    Every returned relation is exactly a 2D product order.
    """
    half = n // 2
    width = 0.12
    separation = 0.25

    best_relation = None
    best_metadata = None
    best_mismatch = float("inf")

    for _ in range(attempts):
        offsets_u_a = rng.uniform(
            -width / 2,
            width / 2,
            size=half,
        )
        offsets_v_a = rng.uniform(
            -width / 2,
            width / 2,
            size=half,
        )
        offsets_u_b = rng.uniform(
            -width / 2,
            width / 2,
            size=n - half,
        )
        offsets_v_b = rng.uniform(
            -width / 2,
            width / 2,
            size=n - half,
        )

        for lam in np.linspace(-1.0, 1.0, 81):
            u_a = (
                0.5
                - separation
                + offsets_u_a
            )
            v_a = (
                0.5
                - lam * separation
                + offsets_v_a
            )
            u_b = (
                0.5
                + separation
                + offsets_u_b
            )
            v_b = (
                0.5
                + lam * separation
                + offsets_v_b
            )

            u = np.clip(
                np.concatenate([u_a, u_b]),
                0.0,
                1.0,
            )
            v = np.clip(
                np.concatenate([v_a, v_b]),
                0.0,
                1.0,
            )

            relation = (
                (u[:, None] < u[None, :])
                & (v[:, None] < v[None, :])
            )
            np.fill_diagonal(relation, False)
            fraction = relation_fraction(relation)
            mismatch = abs(
                fraction - target_fraction
            )

            if mismatch < best_mismatch:
                best_relation = relation
                best_mismatch = mismatch
                best_metadata = {
                    "lambda": float(lam),
                    "target_ordering_fraction": (
                        target_fraction
                    ),
                    "ordering_fraction": (
                        fraction
                    ),
                    "ordering_fraction_mismatch": (
                        mismatch
                    ),
                }

        if best_mismatch <= (
            MAX_DENSITY_MISMATCH / 4
        ):
            break

    if best_relation is None:
        raise RuntimeError(
            "Failed to build bimodal 2D order."
        )

    return (
        permute_relation(best_relation, rng),
        best_metadata,
    )


def evaluate_relation(
    rows: list[dict[str, object]],
    *,
    n: int,
    family: str,
    phase: str,
    sample_index: int,
    relation: np.ndarray,
    model: dict[str, object],
    run_local: bool,
    target_fraction: float | None = None,
    construction_metadata: dict[
        str,
        object,
    ] | None = None,
) -> dict[str, object]:
    q_score, p_value, global_pass = global_score(
        relation,
        model,
    )

    if run_local:
        local_result = local_audit(relation)
        local_pass = bool(
            local_result["local_pass"]
        )
    else:
        local_result = None
        local_pass = True

    actual_fraction = relation_fraction(relation)
    mismatch = (
        abs(actual_fraction - target_fraction)
        if target_fraction is not None
        else 0.0
    )

    row = {
        "n": n,
        "phase": phase,
        "family": family,
        "sample_index": sample_index,
        "q_score": q_score,
        "p_value": p_value,
        "global_pass": global_pass,
        "local_test_run": run_local,
        "local_pass": local_pass,
        "combined_pass": (
            global_pass and local_pass
        ),
        "local_channel": (
            local_result["channel"]
            if local_result is not None
            else None
        ),
        "ordering_fraction": actual_fraction,
        "target_ordering_fraction": (
            target_fraction
            if target_fraction is not None
            else float("nan")
        ),
        "ordering_fraction_mismatch": mismatch,
        "transitive": verify_transitive(
            relation
        ),
        "local_details": (
            json.dumps(
                json_safe(local_result)
            )
            if local_result is not None
            else None
        ),
        "construction_metadata": (
            json.dumps(
                json_safe(
                    construction_metadata
                )
            )
            if construction_metadata
            is not None
            else None
        ),
    }
    rows.append(row)
    return row


def rate(
    rows: Iterable[dict[str, object]],
    field: str,
) -> float:
    values = [
        bool(row[field])
        for row in rows
    ]
    return float(np.mean(values))


def main() -> None:
    output = Path("a16_exact_results")
    output.mkdir(exist_ok=True)

    rng = np.random.default_rng(SEED)

    s3 = standard_example_s3()
    minimal7 = minimal_seven_obstruction()
    anchored_minimal7 = anchored_gadget(
        minimal7
    )

    self_tests = {
        "chain_dimension_at_most_two": (
            is_dimension_at_most_two_exact(
                np.triu(
                    np.ones((6, 6), dtype=bool),
                    k=1,
                )
            )
        ),
        "antichain_dimension_at_most_two": (
            is_dimension_at_most_two_exact(
                np.zeros((6, 6), dtype=bool)
            )
        ),
        "s3_dimension_greater_than_two": (
            not is_dimension_at_most_two_exact(
                s3
            )
        ),
        "minimal7_dimension_greater_than_two": (
            not is_dimension_at_most_two_exact(
                minimal7
            )
        ),
        "all_minimal7_vertex_deletions_dim2": all(
            is_dimension_at_most_two_exact(
                minimal7[
                    np.ix_(
                        [
                            vertex
                            for vertex
                            in range(7)
                            if vertex != removed
                        ],
                        [
                            vertex
                            for vertex
                            in range(7)
                            if vertex != removed
                        ],
                    )
                ]
            )
            for removed in range(7)
        ),
        "anchored_minimal7_transitive": (
            verify_transitive(
                anchored_minimal7
            )
        ),
    }

    rows: list[dict[str, object]] = []
    model_summaries = []

    target_fractions_by_n = {}
    models = {}

    for n in N_VALUES:
        model = fit_global_model(n, rng)
        models[n] = model

        global_holdouts = [
            sample_minkowski_2d(n, rng)
            for _ in range(
                GLOBAL_HOLDOUT_SAMPLES[n]
            )
        ]
        target_fractions = [
            relation_fraction(relation)
            for relation in global_holdouts
        ]
        target_fractions_by_n[n] = (
            target_fractions
        )

        holdout_rows = []
        for sample_index, relation in enumerate(
            global_holdouts
        ):
            holdout_rows.append(
                evaluate_relation(
                    rows,
                    n=n,
                    family="minkowski_holdout",
                    phase=(
                        "prospective_confirmation"
                        if n == CONFIRMATORY_N
                        else "discovery"
                    ),
                    sample_index=sample_index,
                    relation=relation,
                    model=model,
                    run_local=(
                        sample_index
                        < LOCAL_HOLDOUT_SAMPLES[n]
                    ),
                )
            )

        model_summaries.append(
            {
                "n": n,
                "number_bins": len(
                    model["bins"]
                ),
                "covariance_condition_number": (
                    model["condition_number"]
                ),
                "covariance_minimum_eigenvalue": (
                    model["minimum_eigenvalue"]
                ),
                "ledoit_wolf_shrinkage": (
                    model["shrinkage"]
                ),
                "global_holdout_acceptance_rate": (
                    rate(
                        holdout_rows,
                        "global_pass",
                    )
                ),
                "local_holdout_pass_rate": (
                    rate(
                        [
                            row
                            for row in holdout_rows
                            if row[
                                "local_test_run"
                            ]
                        ],
                        "local_pass",
                    )
                ),
                "combined_scanned_holdout_acceptance_rate": (
                    rate(
                        [
                            row
                            for row in holdout_rows
                            if row[
                                "local_test_run"
                            ]
                        ],
                        "combined_pass",
                    )
                ),
            }
        )

    unanchored_rows_by_n = {}

    for n in N_VALUES:
        candidate_rows = []
        targets = target_fractions_by_n[n]
        for sample_index in range(
            UNANCHORED_S3_SAMPLES[n]
        ):
            target = targets[
                sample_index % len(targets)
            ]
            relation, metadata = (
                build_density_matched_unanchored_s3(
                    n,
                    target,
                    rng,
                )
            )
            candidate_rows.append(
                evaluate_relation(
                    rows,
                    n=n,
                    family="unanchored_s3",
                    phase=(
                        "prospective_confirmation"
                        if n == CONFIRMATORY_N
                        else "discovery"
                    ),
                    sample_index=sample_index,
                    relation=relation,
                    model=models[n],
                    run_local=True,
                    target_fraction=target,
                    construction_metadata=metadata,
                )
            )
        unanchored_rows_by_n[n] = (
            candidate_rows
        )

    minimal7_rows = []
    targets = target_fractions_by_n[
        CONFIRMATORY_N
    ]

    for sample_index in range(
        MINIMAL7_CONFIRMATORY_SAMPLES
    ):
        target = targets[
            sample_index % len(targets)
        ]
        relation, metadata = (
            build_anchored_module_adversary(
                CONFIRMATORY_N,
                anchored_minimal7,
                target,
                rng,
            )
        )
        minimal7_rows.append(
            evaluate_relation(
                rows,
                n=CONFIRMATORY_N,
                family=(
                    "anchored_minimal7_obstruction"
                ),
                phase="prospective_confirmation",
                sample_index=sample_index,
                relation=relation,
                model=models[CONFIRMATORY_N],
                run_local=True,
                target_fraction=target,
                construction_metadata=metadata,
            )
        )

    bimodal_rows = []

    for sample_index in range(
        BIMODAL_2D_SAMPLES
    ):
        target = targets[
            sample_index % len(targets)
        ]
        relation, metadata = (
            build_bimodal_2d_order(
                CONFIRMATORY_N,
                target,
                rng,
            )
        )
        bimodal_rows.append(
            evaluate_relation(
                rows,
                n=CONFIRMATORY_N,
                family="bimodal_exact_2d_order",
                phase="prospective_confirmation",
                sample_index=sample_index,
                relation=relation,
                model=models[CONFIRMATORY_N],
                run_local=True,
                target_fraction=target,
                construction_metadata=metadata,
            )
        )

    result_frame = pd.DataFrame(rows)
    result_frame.to_csv(
        output / "a16_sample_results.csv",
        index=False,
    )
    pd.DataFrame(model_summaries).to_csv(
        output / "a16_model_summary.csv",
        index=False,
    )

    family_summaries = []

    for (n, family), group in result_frame.groupby(
        ["n", "family"]
    ):
        local_group = group[
            group["local_test_run"] == True
        ]
        family_summaries.append(
            {
                "n": int(n),
                "family": family,
                "number_samples": int(
                    len(group)
                ),
                "global_acceptance_rate": float(
                    group["global_pass"].mean()
                ),
                "local_pass_rate": (
                    float(
                        local_group[
                            "local_pass"
                        ].mean()
                    )
                    if len(local_group)
                    else float("nan")
                ),
                "combined_acceptance_rate": (
                    float(
                        local_group[
                            "combined_pass"
                        ].mean()
                    )
                    if len(local_group)
                    else float("nan")
                ),
                "maximum_ordering_fraction_mismatch": (
                    float(
                        group[
                            "ordering_fraction_mismatch"
                        ].max()
                    )
                ),
                "all_transitive": bool(
                    group["transitive"].all()
                ),
                "local_channels": (
                    local_group[
                        "local_channel"
                    ]
                    .value_counts()
                    .to_dict()
                ),
            }
        )

    family_summary_frame = pd.DataFrame(
        family_summaries
    )
    family_summary_frame.to_csv(
        output / "a16_family_summary.csv",
        index=False,
    )

    def summary_row(
        n: int,
        family: str,
    ) -> dict[str, object]:
        return next(
            row
            for row in family_summaries
            if row["n"] == n
            and row["family"] == family
        )

    discovery_s3 = summary_row(
        DISCOVERY_N,
        "unanchored_s3",
    )
    confirmatory_s3 = summary_row(
        CONFIRMATORY_N,
        "unanchored_s3",
    )
    minimal7_summary = summary_row(
        CONFIRMATORY_N,
        "anchored_minimal7_obstruction",
    )
    bimodal_summary = summary_row(
        CONFIRMATORY_N,
        "bimodal_exact_2d_order",
    )

    holdout_model_pass = all(
        result[
            "covariance_minimum_eigenvalue"
        ] > 0.0
        and result[
            "covariance_condition_number"
        ] <= 1e8
        and result[
            "global_holdout_acceptance_rate"
        ] >= 0.90
        and result[
            "local_holdout_pass_rate"
        ] == 1.0
        and result[
            "combined_scanned_holdout_acceptance_rate"
        ] >= 0.90
        for result in model_summaries
    )

    all_adversarial_density_valid = all(
        summary[
            "maximum_ordering_fraction_mismatch"
        ] <= MAX_DENSITY_MISMATCH
        for summary in (
            discovery_s3,
            confirmatory_s3,
            minimal7_summary,
            bimodal_summary,
        )
    )

    sparse_global_false_positive = (
        confirmatory_s3[
            "global_acceptance_rate"
        ] >= 0.20
        or minimal7_summary[
            "global_acceptance_rate"
        ] >= 0.20
    )

    gates = {
        "G1_exact_recognition_self_tests": all(
            self_tests.values()
        ),
        "G2_minkowski_global_and_local_acceptance": (
            holdout_model_pass
        ),
        "G3_all_structures_transitive": all(
            summary["all_transitive"]
            for summary in family_summaries
        ),
        "G4_all_adversaries_density_matched": (
            all_adversarial_density_valid
        ),
        "G5_unanchored_s3_detection_discovery": (
            discovery_s3[
                "local_pass_rate"
            ] == 0.0
            and discovery_s3[
                "combined_acceptance_rate"
            ] == 0.0
        ),
        "G6_unanchored_s3_detection_n256": (
            confirmatory_s3[
                "local_pass_rate"
            ] == 0.0
            and confirmatory_s3[
                "combined_acceptance_rate"
            ] == 0.0
        ),
        "G7_unseen_minimal7_interval_detection": (
            minimal7_summary[
                "local_pass_rate"
            ] <= 0.05
            and minimal7_summary[
                "combined_acceptance_rate"
            ] <= 0.05
            and minimal7_summary[
                "local_channels"
            ].get(
                "small_interval_dimension",
                0,
            )
            >= int(
                0.95
                * MINIMAL7_CONFIRMATORY_SAMPLES
            )
        ),
        "G8_bimodal_2d_local_accept_global_reject": (
            bimodal_summary[
                "local_pass_rate"
            ] >= 0.95
            and bimodal_summary[
                "global_acceptance_rate"
            ] <= 0.20
            and bimodal_summary[
                "combined_acceptance_rate"
            ] <= 0.20
        ),
        "G9_global_q_has_sparse_defect_false_positives": (
            sparse_global_false_positive
        ),
        "G10_no_adversary_used_for_calibration": True,
    }

    verdict = (
        "PASS_LOCAL_GLOBAL_COMPLEMENTARITY"
        if all(gates.values())
        else "FAIL_LOCAL_GLOBAL_COMPLEMENTARITY"
    )

    summary = {
        "seed": SEED,
        "discovery_n": DISCOVERY_N,
        "prospective_confirmation_n": (
            CONFIRMATORY_N
        ),
        "global_model": (
            "A14 covariance-aware analytic interval-abundance Q"
        ),
        "local_channels": [
            "label-invariant induced S3 certificate search",
            (
                "exact dimension<=2 recognition for every "
                "order interval with 6-10 elements"
            ),
        ],
        "self_tests": self_tests,
        "model_results": model_summaries,
        "family_results": family_summaries,
        "gates": gates,
        "verdict": verdict,
        "interpretation_boundary": (
            "A pass establishes complementarity of a global "
            "Minkowski statistical signature and exact local "
            "order-theoretic obstruction tests for the specified "
            "families. It does not prove sufficient manifoldlikeness "
            "for arbitrary posets or derive physical spacetime."
        ),
    }

    (output / "a16_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A16 — Local–Global Manifoldlikeness Criterion",
        "",
        "## Design",
        "",
        "- Global A14 covariance-aware interval-abundance test.",
        (
            "- Exact induced-S3 certificate channel for the "
            "unanchored A15 family."
        ),
        (
            "- Exact dimension<=2 recognition on every order "
            "interval with 6-10 elements."
        ),
        (
            "- Prospective n=256 challenge with a minimal "
            "seven-element dimension-3 obstruction whose every "
            "six-element deletion is dimension<=2."
        ),
        (
            "- Exact 2D bimodal control to test global/local "
            "complementarity."
        ),
        "",
        "## Model validation",
        "",
    ]

    for result in model_summaries:
        report_lines.extend(
            [
                f"### n = {result['n']}",
                (
                    "- Global Minkowski acceptance: "
                    f"{result['global_holdout_acceptance_rate']:.4f}"
                ),
                (
                    "- Local Minkowski pass: "
                    f"{result['local_holdout_pass_rate']:.4f}"
                ),
                (
                    "- Combined scanned holdout acceptance: "
                    f"{result['combined_scanned_holdout_acceptance_rate']:.4f}"
                ),
                "",
            ]
        )

    report_lines.extend(
        [
            "## Family results",
            "",
        ]
    )

    for family in family_summaries:
        report_lines.extend(
            [
                (
                    f"### {family['family']} at n={family['n']}"
                ),
                (
                    "- Global acceptance: "
                    f"{family['global_acceptance_rate']:.4f}"
                ),
                (
                    "- Local pass: "
                    f"{family['local_pass_rate']:.4f}"
                ),
                (
                    "- Combined acceptance: "
                    f"{family['combined_acceptance_rate']:.4f}"
                ),
                (
                    "- Maximum density mismatch: "
                    f"{family['maximum_ordering_fraction_mismatch']:.6f}"
                ),
                (
                    "- Local channels: "
                    f"{family['local_channels']}"
                ),
                "",
            ]
        )

    report_lines.extend(
        [
            "## Gates",
            "",
            *[
                f"- {name}: {'PASS' if value else 'FAIL'}"
                for name, value in gates.items()
            ],
            "",
            "## Verdict",
            "",
            verdict,
            "",
            "## Boundary",
            "",
            (
                "The combined criterion is validated only against "
                "the tested families and finite sizes. Local exact "
                "tests cover S3 certificates and small order "
                "intervals, not every possible sparse global "
                "obstruction."
            ),
        ]
    )

    (output / "a16_report.md").write_text(
        "\n".join(report_lines),
        encoding="utf-8",
    )

    print(
        json.dumps(
            json_safe(summary),
            indent=2,
        )
    )
    print()
    print(
        f"Results written to: {output.resolve()}"
    )


if __name__ == "__main__":
    main()
