#!/usr/bin/env python3
"""
A13 — Analytic Interval-Abundance Signature

Exact fixed-cardinality expectation for interval abundances in a 2D
Minkowski Alexandrov interval, followed by a classifier-free model test.

For n iid points sampled uniformly in light-cone coordinates (u,v) in the
unit square, let N_m count ordered comparable pairs with exactly m points
strictly between them. The exact expectation is

E[N_m] = n(n-1) C(n-2,m) sum_{j=0}^{n-2-m}
         (-1)^j C(n-2-m,j)
         / ((m+j+1)^2 (m+j+2)^2).

The observed normalized interval-abundance profile is compared with this
analytic profile using squared Hellinger distance. Finite-sample p-values are
calibrated only from fresh 2D Minkowski sprinklings at the same n. No
classifier is trained.

Prospective sizes:
    n = 96, 128, 160

Nulls:
    - transitive percolation matched to ordering fraction;
    - random three-layer posets matched to ordering fraction;
    - adversarial transitive-percolation samples selected to minimize
      mismatch in the first three interval abundances N_0, N_1, N_2.

Robustness:
    - delete 10%, 20%, and 30% of cover relations from genuine sprinklings,
      then take transitive closure.

Scientific boundary:
Passing this audit means the analytic 2D interval-abundance curve rejects
the specified null families at the tested finite sizes. It does not derive
spacetime, physical causality, gravity, or a fundamental selection law.
"""

from __future__ import annotations

import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Callable

import mpmath as mp
import numpy as np
import pandas as pd


SEED = 20260712
N_VALUES = (96, 128, 160)

REFERENCE_SAMPLES = 300
HOLDOUT_MINKOWSKI = 80
NULL_SAMPLES = 80
ADVERSARIAL_POOL = 260
ADVERSARIAL_SELECTED = 60
PERTURBATION_SAMPLES = 60

ALPHA = 0.05
MAX_MATCH_MISMATCH = 0.02
PERTURBATION_LEVELS = (0.0, 0.10, 0.20, 0.30)


def relation_fraction(relation: np.ndarray) -> float:
    n = relation.shape[0]
    return float(relation.sum() / (n * (n - 1) / 2.0))


def sample_minkowski_2d(
    n: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Uniform fixed-n sprinkling in a 2D Alexandrov interval."""
    u = rng.random(n)
    v = rng.random(n)
    relation = (
        (u[:, None] < u[None, :])
        & (v[:, None] < v[None, :])
    )
    np.fill_diagonal(relation, False)
    permutation = rng.permutation(n)
    return relation[np.ix_(permutation, permutation)]


def bitset_closure_from_edge_prefix(
    n: int,
    ordered_edges: list[tuple[int, int]],
    edge_count: int,
) -> list[int]:
    direct = [0] * n

    for i, j in ordered_edges[:edge_count]:
        direct[i] |= 1 << j

    reach = direct.copy()

    for i in range(n - 1, -1, -1):
        successors = direct[i]
        while successors:
            least = successors & -successors
            j = least.bit_length() - 1
            reach[i] |= reach[j]
            successors ^= least

    return reach


def bitsets_to_matrix(rows: list[int], n: int) -> np.ndarray:
    relation = np.zeros((n, n), dtype=bool)

    for i, original_mask in enumerate(rows):
        mask = original_mask
        while mask:
            least = mask & -mask
            j = least.bit_length() - 1
            relation[i, j] = True
            mask ^= least

    return relation


def matched_transitive_percolation(
    n: int,
    target_fraction: float,
    rng: np.random.Generator,
    max_attempts: int = 16,
) -> tuple[np.ndarray, float]:
    """
    Generate a random DAG and choose a direct-edge prefix whose transitive
    closure is as close as possible to target_fraction.
    """
    possible = n * (n - 1) // 2
    target_count = int(round(target_fraction * possible))

    best_relation: np.ndarray | None = None
    best_fraction = float("nan")
    best_error = float("inf")

    for _ in range(max_attempts):
        edge_values = [
            (float(rng.random()), i, j)
            for i in range(n)
            for j in range(i + 1, n)
        ]
        edge_values.sort(key=lambda item: item[0])
        ordered_edges = [(i, j) for _, i, j in edge_values]

        low, high = 0, len(ordered_edges)
        evaluated: dict[int, tuple[list[int], int]] = {}

        def evaluate(k: int) -> tuple[list[int], int]:
            if k not in evaluated:
                rows = bitset_closure_from_edge_prefix(
                    n,
                    ordered_edges,
                    k,
                )
                count = sum(mask.bit_count() for mask in rows)
                evaluated[k] = (rows, count)
            return evaluated[k]

        while high - low > 1:
            middle = (low + high) // 2
            _, count = evaluate(middle)
            if count < target_count:
                low = middle
            else:
                high = middle

        candidates = range(
            max(0, low - 4),
            min(len(ordered_edges), high + 4) + 1,
        )

        for k in candidates:
            rows, count = evaluate(k)
            fraction = count / possible
            error = abs(fraction - target_fraction)

            if error < best_error:
                relation = bitsets_to_matrix(rows, n)
                permutation = rng.permutation(n)
                best_relation = relation[
                    np.ix_(permutation, permutation)
                ]
                best_fraction = fraction
                best_error = error

        if best_error <= MAX_MATCH_MISMATCH / 4.0:
            break

    if best_relation is None:
        raise RuntimeError(
            "Failed to generate matched transitive percolation."
        )

    return best_relation, best_fraction


def layer_rows(
    n: int,
    probability: float,
    values_01: np.ndarray,
    values_12: np.ndarray,
) -> list[int]:
    first_size = values_01.shape[0]
    second_size = values_01.shape[1]
    third_start = first_size + second_size

    rows = [0] * n

    for second_index in range(second_size):
        mask = 0
        for third_index in np.flatnonzero(
            values_12[second_index] < probability
        ):
            mask |= 1 << (third_start + int(third_index))
        rows[first_size + second_index] = mask

    for first_index in range(first_size):
        mask = 0
        for raw_second in np.flatnonzero(
            values_01[first_index] < probability
        ):
            second_vertex = first_size + int(raw_second)
            mask |= 1 << second_vertex
            mask |= rows[second_vertex]
        rows[first_index] = mask

    return rows


def matched_three_layer_poset(
    n: int,
    target_fraction: float,
    rng: np.random.Generator,
    max_attempts: int = 16,
) -> tuple[np.ndarray, float]:
    first_size = n // 4
    second_size = n // 2
    third_size = n - first_size - second_size
    possible = n * (n - 1) // 2

    best_relation: np.ndarray | None = None
    best_fraction = float("nan")
    best_error = float("inf")

    for _ in range(max_attempts):
        values_01 = rng.random((first_size, second_size))
        values_12 = rng.random((second_size, third_size))

        low, high = 0.0, 1.0

        for _ in range(18):
            middle = (low + high) / 2.0
            rows = layer_rows(
                n,
                middle,
                values_01,
                values_12,
            )
            fraction = (
                sum(mask.bit_count() for mask in rows) / possible
            )

            if fraction < target_fraction:
                low = middle
            else:
                high = middle

        for probability in (low, (low + high) / 2.0, high):
            rows = layer_rows(
                n,
                probability,
                values_01,
                values_12,
            )
            fraction = (
                sum(mask.bit_count() for mask in rows) / possible
            )
            error = abs(fraction - target_fraction)

            if error < best_error:
                relation = bitsets_to_matrix(rows, n)
                permutation = rng.permutation(n)
                best_relation = relation[
                    np.ix_(permutation, permutation)
                ]
                best_fraction = fraction
                best_error = error

        if best_error <= MAX_MATCH_MISMATCH / 4.0:
            break

    if best_relation is None:
        raise RuntimeError("Failed to generate matched layered poset.")

    return best_relation, best_fraction


@lru_cache(maxsize=None)
def analytic_expectation(n: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Return exact fixed-n expected counts and normalized profile for 2D.
    High precision is used because the finite alternating sum can suffer
    severe cancellation in ordinary floating-point arithmetic.
    """
    mp.mp.dps = 90
    expected = []

    for m in range(n - 1):
        remaining = n - 2 - m
        total = mp.mpf("0")

        for j in range(remaining + 1):
            total += (
                (-1) ** j
                * mp.binomial(remaining, j)
                / (
                    (m + j + 1) ** 2
                    * (m + j + 2) ** 2
                )
            )

        value = (
            n
            * (n - 1)
            * mp.binomial(n - 2, m)
            * total
        )
        expected.append(float(value))

    expected_array = np.asarray(expected, dtype=float)
    profile = expected_array / expected_array.sum()
    return expected_array, profile


def interval_abundance(relation: np.ndarray) -> np.ndarray:
    n = relation.shape[0]
    reflexive = relation | np.eye(n, dtype=bool)
    interval_sizes = (
        reflexive.astype(np.int16)
        @ reflexive.astype(np.int16)
    )
    open_sizes = interval_sizes[relation] - 2

    return np.bincount(
        open_sizes,
        minlength=n - 1,
    )[: n - 1].astype(float)


def hellinger_squared(
    counts: np.ndarray,
    expected_profile: np.ndarray,
) -> float:
    total = counts.sum()

    if total <= 0:
        return 1.0

    observed_profile = counts / total
    affinity = np.sqrt(
        observed_profile * expected_profile
    ).sum()
    return float(max(0.0, 1.0 - affinity))


def empirical_p_value(
    score: float,
    reference_scores: np.ndarray,
) -> float:
    return float(
        (
            1
            + np.count_nonzero(reference_scores >= score)
        )
        / (len(reference_scores) + 1)
    )


def wilson_interval(
    successes: int,
    total: int,
    z: float = 1.959963984540054,
) -> tuple[float, float]:
    if total == 0:
        return float("nan"), float("nan")

    proportion = successes / total
    denominator = 1.0 + z * z / total
    center = (
        proportion + z * z / (2.0 * total)
    ) / denominator
    radius = (
        z
        * math.sqrt(
            proportion * (1.0 - proportion) / total
            + z * z / (4.0 * total * total)
        )
        / denominator
    )
    return float(center - radius), float(center + radius)


def topological_order(relation: np.ndarray) -> list[int]:
    n = relation.shape[0]
    indegree = relation.sum(axis=0).astype(int)
    available = [
        int(vertex)
        for vertex in np.flatnonzero(indegree == 0)
    ]
    order: list[int] = []

    while available:
        vertex = available.pop()
        order.append(vertex)

        for target in np.flatnonzero(relation[vertex]):
            indegree[target] -= 1
            if indegree[target] == 0:
                available.append(int(target))

    if len(order) != n:
        raise RuntimeError("Relation is not acyclic.")

    return order


def closure_from_direct_relation(
    direct: np.ndarray,
) -> np.ndarray:
    n = direct.shape[0]
    order = topological_order(direct)

    direct_rows = [0] * n
    reach_rows = [0] * n

    for i in range(n):
        mask = 0
        for j in np.flatnonzero(direct[i]):
            mask |= 1 << int(j)
        direct_rows[i] = mask
        reach_rows[i] = mask

    for i in reversed(order):
        successors = direct_rows[i]
        while successors:
            least = successors & -successors
            j = least.bit_length() - 1
            reach_rows[i] |= reach_rows[j]
            successors ^= least

    return bitsets_to_matrix(reach_rows, n)


def delete_cover_fraction(
    relation: np.ndarray,
    fraction: float,
    rng: np.random.Generator,
) -> np.ndarray:
    if fraction <= 0.0:
        return relation.copy()

    n = relation.shape[0]
    reflexive = relation | np.eye(n, dtype=bool)
    interval_sizes = (
        reflexive.astype(np.int16)
        @ reflexive.astype(np.int16)
    )
    cover = relation & (interval_sizes == 2)
    edges = np.argwhere(cover)

    if len(edges) == 0:
        return relation.copy()

    number_to_remove = max(
        1,
        int(round(fraction * len(edges))),
    )
    chosen = rng.choice(
        len(edges),
        size=min(number_to_remove, len(edges)),
        replace=False,
    )

    direct = cover.copy()
    selected_edges = edges[chosen]
    direct[
        selected_edges[:, 0],
        selected_edges[:, 1],
    ] = False

    return closure_from_direct_relation(direct)


def score_relation(
    relation: np.ndarray,
    expected_profile: np.ndarray,
) -> tuple[float, np.ndarray]:
    counts = interval_abundance(relation)
    score = hellinger_squared(counts, expected_profile)
    observed_profile = counts / counts.sum()
    return score, observed_profile


def append_scored_sample(
    rows: list[dict[str, object]],
    *,
    n: int,
    family: str,
    sample_index: int,
    relation: np.ndarray,
    expected_profile: np.ndarray,
    reference_scores: np.ndarray,
    target_fraction: float | None = None,
    perturbation_fraction: float = 0.0,
) -> dict[str, object]:
    score, profile = score_relation(
        relation,
        expected_profile,
    )
    p_value = empirical_p_value(score, reference_scores)
    actual_fraction = relation_fraction(relation)

    row: dict[str, object] = {
        "n": n,
        "family": family,
        "sample_index": sample_index,
        "score_hellinger_squared": score,
        "p_value": p_value,
        "compatible_at_alpha_0_05": p_value >= ALPHA,
        "ordering_fraction": actual_fraction,
        "target_ordering_fraction": (
            target_fraction
            if target_fraction is not None
            else float("nan")
        ),
        "ordering_fraction_mismatch": (
            abs(actual_fraction - target_fraction)
            if target_fraction is not None
            else 0.0
        ),
        "perturbation_fraction": perturbation_fraction,
        "profile_m0": float(profile[0]),
        "profile_m1": float(profile[1]),
        "profile_m2": float(profile[2]),
    }
    rows.append(row)
    return row



def json_safe(value):
    """Recursively convert NumPy scalar types to standard JSON types."""
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value


def main() -> None:
    output = Path("a13_exact_results")
    output.mkdir(exist_ok=True)

    rng = np.random.default_rng(SEED)

    theory_rows: list[dict[str, object]] = []
    sample_rows: list[dict[str, object]] = []
    perturbation_rows: list[dict[str, object]] = []
    size_summaries: list[dict[str, object]] = []

    all_formula_normalization_pass = True
    all_monte_carlo_pass = True
    all_minkowski_acceptance_pass = True
    all_tp_rejection_pass = True
    all_layer_rejection_pass = True
    all_adversarial_rejection_pass = True
    all_adversarial_matching_pass = True
    all_perturbation_pass = True

    for n in N_VALUES:
        expected_counts, expected_profile = analytic_expectation(n)
        expected_total = n * (n - 1) / 4.0
        normalization_error = abs(
            expected_counts.sum() - expected_total
        )
        formula_normalization_pass = normalization_error < 1e-8
        all_formula_normalization_pass &= formula_normalization_pass

        for m, (count, probability) in enumerate(
            zip(expected_counts, expected_profile)
        ):
            theory_rows.append(
                {
                    "n": n,
                    "m": m,
                    "expected_count": float(count),
                    "expected_profile": float(probability),
                }
            )

        reference_scores = []
        reference_count_vectors = []

        for sample_index in range(REFERENCE_SAMPLES):
            relation = sample_minkowski_2d(n, rng)
            counts = interval_abundance(relation)
            reference_count_vectors.append(counts)
            reference_scores.append(
                hellinger_squared(
                    counts,
                    expected_profile,
                )
            )

        reference_scores_array = np.asarray(
            reference_scores,
            dtype=float,
        )
        reference_counts = np.vstack(reference_count_vectors)

        reference_mean = reference_counts.mean(axis=0)
        reference_sd = reference_counts.std(
            axis=0,
            ddof=1,
        )
        standard_error = reference_sd / math.sqrt(
            REFERENCE_SAMPLES
        )

        valid_bins = (
            (expected_counts >= 5.0)
            & (standard_error > 0.0)
        )
        z_scores = np.zeros_like(expected_counts)
        z_scores[valid_bins] = (
            reference_mean[valid_bins]
            - expected_counts[valid_bins]
        ) / standard_error[valid_bins]
        maximum_absolute_z = float(
            np.max(np.abs(z_scores[valid_bins]))
        )
        monte_carlo_pass = maximum_absolute_z <= 4.5
        all_monte_carlo_pass &= monte_carlo_pass

        holdout_relations = [
            sample_minkowski_2d(n, rng)
            for _ in range(HOLDOUT_MINKOWSKI)
        ]
        target_fractions = [
            relation_fraction(relation)
            for relation in holdout_relations
        ]

        holdout_rows = []
        for sample_index, relation in enumerate(
            holdout_relations
        ):
            holdout_rows.append(
                append_scored_sample(
                    sample_rows,
                    n=n,
                    family="minkowski_holdout",
                    sample_index=sample_index,
                    relation=relation,
                    expected_profile=expected_profile,
                    reference_scores=reference_scores_array,
                )
            )

        ordinary_tp_rows = []
        layered_rows = []

        for sample_index in range(NULL_SAMPLES):
            target = target_fractions[
                sample_index % len(target_fractions)
            ]

            tp_relation, _ = matched_transitive_percolation(
                n,
                target,
                rng,
            )
            ordinary_tp_rows.append(
                append_scored_sample(
                    sample_rows,
                    n=n,
                    family="transitive_percolation",
                    sample_index=sample_index,
                    relation=tp_relation,
                    expected_profile=expected_profile,
                    reference_scores=reference_scores_array,
                    target_fraction=target,
                )
            )

            layered_relation, _ = matched_three_layer_poset(
                n,
                target,
                rng,
            )
            layered_rows.append(
                append_scored_sample(
                    sample_rows,
                    n=n,
                    family="three_layer",
                    sample_index=sample_index,
                    relation=layered_relation,
                    expected_profile=expected_profile,
                    reference_scores=reference_scores_array,
                    target_fraction=target,
                )
            )

        adversarial_candidates = []

        for candidate_index in range(ADVERSARIAL_POOL):
            target = target_fractions[
                candidate_index % len(target_fractions)
            ]
            relation, _ = matched_transitive_percolation(
                n,
                target,
                rng,
            )
            score, profile = score_relation(
                relation,
                expected_profile,
            )
            low_m_error = float(
                np.abs(
                    profile[:3] - expected_profile[:3]
                ).sum()
            )
            adversarial_candidates.append(
                {
                    "candidate_index": candidate_index,
                    "relation": relation,
                    "target": target,
                    "score": score,
                    "profile": profile,
                    "low_m_error": low_m_error,
                }
            )

        adversarial_candidates.sort(
            key=lambda item: item["low_m_error"]
        )
        selected_adversarial = adversarial_candidates[
            :ADVERSARIAL_SELECTED
        ]

        adversarial_rows = []
        for sample_index, item in enumerate(
            selected_adversarial
        ):
            adversarial_rows.append(
                append_scored_sample(
                    sample_rows,
                    n=n,
                    family="adversarial_transitive_percolation",
                    sample_index=sample_index,
                    relation=item["relation"],
                    expected_profile=expected_profile,
                    reference_scores=reference_scores_array,
                    target_fraction=float(item["target"]),
                )
            )

        perturbation_by_level: dict[
            float,
            list[dict[str, object]],
        ] = {level: [] for level in PERTURBATION_LEVELS}

        perturbation_bases = [
            sample_minkowski_2d(n, rng)
            for _ in range(PERTURBATION_SAMPLES)
        ]

        for level in PERTURBATION_LEVELS:
            for sample_index, base_relation in enumerate(
                perturbation_bases
            ):
                relation = delete_cover_fraction(
                    base_relation,
                    level,
                    rng,
                )
                row = append_scored_sample(
                    perturbation_rows,
                    n=n,
                    family="cover_deletion",
                    sample_index=sample_index,
                    relation=relation,
                    expected_profile=expected_profile,
                    reference_scores=reference_scores_array,
                    perturbation_fraction=level,
                )
                perturbation_by_level[level].append(row)

        def acceptance_rate(
            rows: list[dict[str, object]],
        ) -> float:
            return float(
                np.mean(
                    [
                        bool(row["compatible_at_alpha_0_05"])
                        for row in rows
                    ]
                )
            )

        def rejection_rate(
            rows: list[dict[str, object]],
        ) -> float:
            return 1.0 - acceptance_rate(rows)

        minkowski_acceptance = acceptance_rate(holdout_rows)
        tp_rejection = rejection_rate(ordinary_tp_rows)
        layer_rejection = rejection_rate(layered_rows)
        adversarial_rejection = rejection_rate(
            adversarial_rows
        )

        ordinary_low_m_errors = [
            abs(float(row["profile_m0"]) - expected_profile[0])
            + abs(float(row["profile_m1"]) - expected_profile[1])
            + abs(float(row["profile_m2"]) - expected_profile[2])
            for row in ordinary_tp_rows
        ]
        adversarial_low_m_errors = [
            float(item["low_m_error"])
            for item in selected_adversarial
        ]

        ordinary_low_m_median = float(
            np.median(ordinary_low_m_errors)
        )
        adversarial_low_m_median = float(
            np.median(adversarial_low_m_errors)
        )
        low_m_reduction = (
            1.0
            - adversarial_low_m_median
            / ordinary_low_m_median
        )

        maximum_null_mismatch = max(
            max(
                float(row["ordering_fraction_mismatch"])
                for row in ordinary_tp_rows
            ),
            max(
                float(row["ordering_fraction_mismatch"])
                for row in layered_rows
            ),
            max(
                float(row["ordering_fraction_mismatch"])
                for row in adversarial_rows
            ),
        )

        perturbation_medians = {
            str(level): float(
                np.median(
                    [
                        float(row["score_hellinger_squared"])
                        for row in perturbation_by_level[level]
                    ]
                )
            )
            for level in PERTURBATION_LEVELS
        }
        perturbation_rejections = {
            str(level): rejection_rate(
                perturbation_by_level[level]
            )
            for level in PERTURBATION_LEVELS
        }

        medians_in_order = [
            perturbation_medians[str(level)]
            for level in PERTURBATION_LEVELS
        ]
        perturbation_monotonic = all(
            later >= earlier
            for earlier, later in zip(
                medians_in_order,
                medians_in_order[1:],
            )
        )
        perturbation_detection_pass = (
            perturbation_rejections[str(0.20)] >= 0.80
            and perturbation_rejections[str(0.30)] >= 0.95
            and perturbation_monotonic
        )

        minkowski_pass = minkowski_acceptance >= 0.90
        tp_pass = tp_rejection >= 0.90
        layer_pass = layer_rejection >= 0.90
        adversarial_pass = adversarial_rejection >= 0.80
        adversarial_matching_pass = (
            low_m_reduction >= 0.15
            and maximum_null_mismatch <= MAX_MATCH_MISMATCH
        )

        all_minkowski_acceptance_pass &= minkowski_pass
        all_tp_rejection_pass &= tp_pass
        all_layer_rejection_pass &= layer_pass
        all_adversarial_rejection_pass &= adversarial_pass
        all_adversarial_matching_pass &= (
            adversarial_matching_pass
        )
        all_perturbation_pass &= perturbation_detection_pass

        minkowski_successes = int(
            round(
                minkowski_acceptance
                * len(holdout_rows)
            )
        )
        tp_successes = int(
            round(tp_rejection * len(ordinary_tp_rows))
        )
        layer_successes = int(
            round(layer_rejection * len(layered_rows))
        )
        adversarial_successes = int(
            round(
                adversarial_rejection
                * len(adversarial_rows)
            )
        )

        size_summaries.append(
            {
                "n": n,
                "formula_normalization_error": normalization_error,
                "formula_normalization_pass": (
                    formula_normalization_pass
                ),
                "maximum_absolute_monte_carlo_z": (
                    maximum_absolute_z
                ),
                "monte_carlo_formula_check_pass": (
                    monte_carlo_pass
                ),
                "reference_score_median": float(
                    np.median(reference_scores_array)
                ),
                "reference_score_95_quantile": float(
                    np.quantile(
                        reference_scores_array,
                        0.95,
                    )
                ),
                "minkowski_acceptance_rate": (
                    minkowski_acceptance
                ),
                "minkowski_acceptance_wilson_95": (
                    wilson_interval(
                        minkowski_successes,
                        len(holdout_rows),
                    )
                ),
                "transitive_percolation_rejection_rate": (
                    tp_rejection
                ),
                "transitive_percolation_rejection_wilson_95": (
                    wilson_interval(
                        tp_successes,
                        len(ordinary_tp_rows),
                    )
                ),
                "three_layer_rejection_rate": (
                    layer_rejection
                ),
                "three_layer_rejection_wilson_95": (
                    wilson_interval(
                        layer_successes,
                        len(layered_rows),
                    )
                ),
                "adversarial_rejection_rate": (
                    adversarial_rejection
                ),
                "adversarial_rejection_wilson_95": (
                    wilson_interval(
                        adversarial_successes,
                        len(adversarial_rows),
                    )
                ),
                "ordinary_low_m_error_median": (
                    ordinary_low_m_median
                ),
                "adversarial_low_m_error_median": (
                    adversarial_low_m_median
                ),
                "adversarial_low_m_error_reduction": (
                    low_m_reduction
                ),
                "maximum_ordering_fraction_mismatch": (
                    maximum_null_mismatch
                ),
                "perturbation_score_medians": (
                    perturbation_medians
                ),
                "perturbation_rejection_rates": (
                    perturbation_rejections
                ),
                "perturbation_monotonic": (
                    perturbation_monotonic
                ),
                "perturbation_detection_pass": (
                    perturbation_detection_pass
                ),
            }
        )

    pd.DataFrame(theory_rows).to_csv(
        output / "a13_theory_profiles.csv",
        index=False,
    )
    pd.DataFrame(sample_rows).to_csv(
        output / "a13_sample_scores.csv",
        index=False,
    )
    pd.DataFrame(perturbation_rows).to_csv(
        output / "a13_perturbation_scores.csv",
        index=False,
    )
    pd.DataFrame(size_summaries).to_csv(
        output / "a13_size_summary.csv",
        index=False,
    )

    gates = {
        "G1_exact_formula_normalization": (
            all_formula_normalization_pass
        ),
        "G2_monte_carlo_formula_validation": (
            all_monte_carlo_pass
        ),
        "G3_minkowski_holdout_acceptance_ge_0_90": (
            all_minkowski_acceptance_pass
        ),
        "G4_transitive_percolation_rejection_ge_0_90": (
            all_tp_rejection_pass
        ),
        "G5_three_layer_rejection_ge_0_90": (
            all_layer_rejection_pass
        ),
        "G6_adversarial_rejection_ge_0_80": (
            all_adversarial_rejection_pass
        ),
        "G7_adversarial_low_m_matching_and_density_control": (
            all_adversarial_matching_pass
        ),
        "G8_perturbation_response": (
            all_perturbation_pass
        ),
        "G9_no_trained_classifier": True,
    }

    verdict = (
        "PASS_ANALYTIC_INTERVAL_SIGNATURE"
        if all(gates.values())
        else "FAIL_ANALYTIC_INTERVAL_SIGNATURE"
    )

    summary = {
        "seed": SEED,
        "n_values": list(N_VALUES),
        "reference_samples_per_n": REFERENCE_SAMPLES,
        "holdout_minkowski_per_n": HOLDOUT_MINKOWSKI,
        "ordinary_null_samples_per_family_per_n": (
            NULL_SAMPLES
        ),
        "adversarial_pool_per_n": ADVERSARIAL_POOL,
        "adversarial_selected_per_n": ADVERSARIAL_SELECTED,
        "alpha": ALPHA,
        "analytic_formula": (
            "E[N_m] = n(n-1) C(n-2,m) "
            "sum_{j=0}^{n-2-m} (-1)^j C(n-2-m,j) / "
            "((m+j+1)^2 (m+j+2)^2)"
        ),
        "discrepancy": (
            "squared Hellinger distance between the observed "
            "normalized interval-abundance profile and the exact "
            "fixed-n 2D expectation"
        ),
        "size_results": size_summaries,
        "gates": gates,
        "verdict": verdict,
        "interpretation_boundary": (
            "A pass establishes finite-size rejection of the "
            "specified matched nulls by an analytic-reference "
            "interval-abundance test. It does not establish that "
            "the criterion is sufficient for manifoldlikeness or "
            "that spacetime is generated by arbitrary relations."
        ),
    }

    (output / "a13_summary.json").write_text(
        json.dumps(json_safe(summary), indent=2),
        encoding="utf-8",
    )

    report_lines = [
        "# A13 — Analytic Interval-Abundance Signature",
        "",
        "## Design",
        "",
        "- No trained classifier.",
        f"- Prospective sizes: {list(N_VALUES)}.",
        (
            "- Exact fixed-cardinality 2D interval-abundance "
            "expectation."
        ),
        (
            "- Squared Hellinger discrepancy with empirical "
            "same-n Minkowski calibration."
        ),
        (
            "- Matched transitive-percolation, three-layer, and "
            "low-m adversarial nulls."
        ),
        (
            "- Cover-deletion perturbations at 10%, 20%, and 30%."
        ),
        "",
        "## Results by size",
        "",
    ]

    for result in size_summaries:
        report_lines.extend(
            [
                f"### n = {result['n']}",
                "",
                (
                    "- Minkowski acceptance: "
                    f"{result['minkowski_acceptance_rate']:.4f}"
                ),
                (
                    "- Transitive-percolation rejection: "
                    f"{result['transitive_percolation_rejection_rate']:.4f}"
                ),
                (
                    "- Three-layer rejection: "
                    f"{result['three_layer_rejection_rate']:.4f}"
                ),
                (
                    "- Adversarial rejection: "
                    f"{result['adversarial_rejection_rate']:.4f}"
                ),
                (
                    "- Maximum ordering-fraction mismatch: "
                    f"{result['maximum_ordering_fraction_mismatch']:.6f}"
                ),
                (
                    "- Adversarial low-m error reduction: "
                    f"{result['adversarial_low_m_error_reduction']:.4f}"
                ),
                (
                    "- Perturbation rejection rates: "
                    f"{result['perturbation_rejection_rates']}"
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
                "This is a necessary-signature test against specified "
                "finite null families, not a proof of sufficient "
                "manifoldlikeness or a derivation of physical spacetime."
            ),
        ]
    )

    (output / "a13_report.md").write_text(
        "\n".join(report_lines),
        encoding="utf-8",
    )

    print(json.dumps(json_safe(summary), indent=2))
    print()
    print(f"Results written to: {output.resolve()}")


if __name__ == "__main__":
    main()
