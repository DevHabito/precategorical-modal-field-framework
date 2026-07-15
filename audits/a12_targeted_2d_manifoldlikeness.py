#!/usr/bin/env python3
"""
A12 — Targeted 2D Manifoldlikeness Audit

Targeted comparison:
    2D Minkowski interval orders versus transitive-percolation posets.

Prospective split:
    train: n=64
    test_1: n=96
    test_2: n=128

The null for every manifold sample is matched individually to its ordering
fraction. The primary classifier uses three pre-registered feature families:

1. interval-abundance profile;
2. local dimension consistency;
3. exact local 2D-order obstruction rate on induced six-element subposets.

Scientific boundary:
A positive result would establish discrimination against this specified null,
not a derivation of spacetime, physical causality, gravity, or a continuum.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.special import gammaln
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

SEED = 20260712
SPLITS = {"train": 64, "test_96": 96, "test_128": 128}
PAIRS_PER_SPLIT = 28
MAX_MATCH_MISMATCH = 0.02
LOCAL_INTERVAL_SAMPLE = 192
GLOBAL_SIX_SUBSETS = 64
INTERVAL_SIX_SUBSETS = 32
BOOTSTRAPS = 3000

SMALL_INTERVAL_K = tuple(range(0, 6))
LOG_BINS = np.linspace(0.0, 1.0, 7)

INTERVAL_FEATURES = [
    *(f"interval_k_{k}" for k in SMALL_INTERVAL_K),
    *(f"interval_logbin_{i}" for i in range(len(LOG_BINS) - 1)),
    "interval_open_mean_fraction",
    "interval_open_median_fraction",
    "interval_open_q90_fraction",
]

LOCAL_DIM_FEATURES = [
    "local_dim_abs_median",
    "local_dim_abs_q90",
    "local_dim_mad",
    "local_dim_fraction_within_0_5",
    "local_dim_scale_drift",
    "local_dim_valid_fraction",
]

EMBED_FEATURES = [
    "global_dim2_obstruction_fraction",
    "interval_dim2_obstruction_fraction",
]

PRIMARY_FEATURES = INTERVAL_FEATURES + LOCAL_DIM_FEATURES + EMBED_FEATURES


def ordering_fraction_theory(dimension: float) -> float:
    return math.exp(
        gammaln(dimension + 1.0)
        + gammaln(dimension / 2.0)
        - math.log(2.0)
        - gammaln(1.5 * dimension)
    )


def myrheim_meyer_dimension(ordering_fraction: float) -> float:
    low, high = 1.01, 12.0
    f_low = ordering_fraction_theory(low)
    f_high = ordering_fraction_theory(high)
    if ordering_fraction >= f_low:
        return low
    if ordering_fraction <= f_high:
        return high
    return float(
        brentq(
            lambda d: ordering_fraction_theory(d) - ordering_fraction,
            low,
            high,
        )
    )


def relation_fraction(relation: np.ndarray) -> float:
    n = relation.shape[0]
    return float(relation.sum() / (n * (n - 1) / 2.0))


def sample_minkowski_2d(n: int, rng: np.random.Generator) -> np.ndarray:
    """Uniform sprinkling in a 2D Alexandrov interval in light-cone coordinates."""
    u = rng.random(n)
    v = rng.random(n)
    relation = (u[:, None] < u[None, :]) & (v[:, None] < v[None, :])
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
    for i, mask in enumerate(rows):
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
    max_attempts: int = 24,
) -> tuple[np.ndarray, float, int, int]:
    """Match a transitive-percolation sample to a target ordering fraction."""
    possible = n * (n - 1) // 2
    target_count = int(round(target_fraction * possible))
    best_relation: np.ndarray | None = None
    best_fraction = float("nan")
    best_error = float("inf")
    best_direct_edges = 0
    best_attempt = 0

    for attempt in range(1, max_attempts + 1):
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
                rows = bitset_closure_from_edge_prefix(n, ordered_edges, k)
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

        candidates = range(max(0, low - 3), min(len(ordered_edges), high + 3) + 1)
        for k in candidates:
            rows, count = evaluate(k)
            fraction = count / possible
            error = abs(fraction - target_fraction)
            if error < best_error:
                relation = bitsets_to_matrix(rows, n)
                permutation = rng.permutation(n)
                best_relation = relation[np.ix_(permutation, permutation)]
                best_fraction = fraction
                best_error = error
                best_direct_edges = k
                best_attempt = attempt

        if best_error <= MAX_MATCH_MISMATCH / 4.0:
            break

    if best_relation is None:
        raise RuntimeError("Failed to generate a matched transitive-percolation poset.")

    return best_relation, best_fraction, best_direct_edges, best_attempt


def interval_matrix(relation: np.ndarray) -> np.ndarray:
    n = relation.shape[0]
    reflexive = relation | np.eye(n, dtype=bool)
    return reflexive.astype(np.int16) @ reflexive.astype(np.int16)


def interval_abundance_features(
    relation: np.ndarray,
    intervals: np.ndarray,
) -> dict[str, float]:
    n = relation.shape[0]
    open_sizes = intervals[relation].astype(float) - 2.0
    total = len(open_sizes)
    features: dict[str, float] = {}

    for k in SMALL_INTERVAL_K:
        features[f"interval_k_{k}"] = (
            float(np.mean(open_sizes == k)) if total else 0.0
        )

    large = open_sizes[open_sizes >= 6.0]
    if len(large):
        normalized_log = np.log1p(large) / math.log1p(max(1, n - 2))
        histogram, _ = np.histogram(normalized_log, bins=LOG_BINS)
        histogram = histogram.astype(float) / total
    else:
        histogram = np.zeros(len(LOG_BINS) - 1, dtype=float)

    for index, value in enumerate(histogram):
        features[f"interval_logbin_{index}"] = float(value)

    if total:
        normalized = open_sizes / max(1, n - 2)
        features["interval_open_mean_fraction"] = float(np.mean(normalized))
        features["interval_open_median_fraction"] = float(np.median(normalized))
        features["interval_open_q90_fraction"] = float(np.quantile(normalized, 0.9))
    else:
        features["interval_open_mean_fraction"] = 0.0
        features["interval_open_median_fraction"] = 0.0
        features["interval_open_q90_fraction"] = 0.0

    return features


def local_dimension_features(
    relation: np.ndarray,
    intervals: np.ndarray,
    rng: np.random.Generator,
) -> dict[str, float]:
    n = relation.shape[0]
    global_dimension = myrheim_meyer_dimension(relation_fraction(relation))
    reflexive = relation | np.eye(n, dtype=bool)

    pairs = np.argwhere(relation & (intervals >= 8))
    if len(pairs) > LOCAL_INTERVAL_SAMPLE:
        selected = rng.choice(len(pairs), size=LOCAL_INTERVAL_SAMPLE, replace=False)
        pairs = pairs[selected]

    local_dimensions: list[float] = []
    local_sizes: list[int] = []

    for raw_i, raw_j in pairs:
        i, j = int(raw_i), int(raw_j)
        subset = np.flatnonzero(reflexive[i] & reflexive[:, j])
        size = len(subset)
        if size < 4:
            continue
        local_relation = relation[np.ix_(subset, subset)]
        fraction = relation_fraction(local_relation)
        local_dimensions.append(myrheim_meyer_dimension(fraction))
        local_sizes.append(size)

    if not local_dimensions:
        return {
            "local_dim_abs_median": float("nan"),
            "local_dim_abs_q90": float("nan"),
            "local_dim_mad": float("nan"),
            "local_dim_fraction_within_0_5": 0.0,
            "local_dim_scale_drift": float("nan"),
            "local_dim_valid_fraction": 0.0,
        }

    dimensions = np.asarray(local_dimensions, dtype=float)
    sizes = np.asarray(local_sizes, dtype=float)
    absolute = np.abs(dimensions - global_dimension)
    median_dimension = float(np.median(dimensions))
    mad = float(np.median(np.abs(dimensions - median_dimension)))

    size_median = float(np.median(sizes))
    small = dimensions[sizes <= size_median]
    large = dimensions[sizes > size_median]
    if len(small) and len(large):
        drift = abs(float(np.median(large) - np.median(small)))
    else:
        drift = float("nan")

    return {
        "local_dim_abs_median": float(np.median(absolute)),
        "local_dim_abs_q90": float(np.quantile(absolute, 0.9)),
        "local_dim_mad": mad,
        "local_dim_fraction_within_0_5": float(np.mean(absolute <= 0.5)),
        "local_dim_scale_drift": drift,
        "local_dim_valid_fraction": float(len(dimensions) / max(1, len(pairs))),
    }


def linear_extensions(relation: np.ndarray) -> Iterable[tuple[int, ...]]:
    k = relation.shape[0]
    predecessors = [set(np.flatnonzero(relation[:, vertex])) for vertex in range(k)]

    def recurse(prefix: list[int], remaining: set[int]) -> Iterable[tuple[int, ...]]:
        if not remaining:
            yield tuple(prefix)
            return
        available = sorted(
            vertex
            for vertex in remaining
            if not (predecessors[vertex] & remaining)
        )
        for vertex in available:
            prefix.append(vertex)
            yield from recurse(prefix, remaining - {vertex})
            prefix.pop()

    yield from recurse([], set(range(k)))


def is_dimension_at_most_two(relation: np.ndarray) -> bool:
    """Exact finite test by enumerating the first order in a two-order realizer."""
    k = relation.shape[0]

    for extension in linear_extensions(relation):
        position = np.empty(k, dtype=np.int8)
        for index, vertex in enumerate(extension):
            position[vertex] = index

        second = np.zeros((k, k), dtype=bool)
        for i in range(k):
            for j in range(i + 1, k):
                if relation[i, j]:
                    second[i, j] = True
                elif relation[j, i]:
                    second[j, i] = True
                elif position[i] < position[j]:
                    second[j, i] = True
                else:
                    second[i, j] = True

        indegree = second.sum(axis=0).astype(int)
        available = [int(x) for x in np.flatnonzero(indegree == 0)]
        seen = 0
        while available:
            vertex = available.pop()
            seen += 1
            for target in np.flatnonzero(second[vertex]):
                indegree[target] -= 1
                if indegree[target] == 0:
                    available.append(int(target))
        if seen == k:
            return True

    return False


def dim2_obstruction_fraction(
    relation: np.ndarray,
    intervals: np.ndarray,
    rng: np.random.Generator,
) -> tuple[float, float]:
    n = relation.shape[0]
    global_obstructions = 0

    for _ in range(GLOBAL_SIX_SUBSETS):
        subset = rng.choice(n, size=6, replace=False)
        local = relation[np.ix_(subset, subset)]
        global_obstructions += int(not is_dimension_at_most_two(local))

    reflexive = relation | np.eye(n, dtype=bool)
    candidate_pairs = np.argwhere(relation & (intervals >= 8))
    interval_obstructions = 0
    interval_tests = 0

    if len(candidate_pairs):
        order = rng.permutation(len(candidate_pairs))
        for pair_index in order:
            i, j = map(int, candidate_pairs[pair_index])
            elements = np.flatnonzero(reflexive[i] & reflexive[:, j])
            if len(elements) < 6:
                continue
            subset = rng.choice(elements, size=6, replace=False)
            local = relation[np.ix_(subset, subset)]
            interval_obstructions += int(not is_dimension_at_most_two(local))
            interval_tests += 1
            if interval_tests >= INTERVAL_SIX_SUBSETS:
                break

    return (
        global_obstructions / GLOBAL_SIX_SUBSETS,
        interval_obstructions / interval_tests if interval_tests else 0.0,
    )


def extract_features(relation: np.ndarray, rng: np.random.Generator) -> dict[str, float]:
    intervals = interval_matrix(relation)
    features = {
        "ordering_fraction": relation_fraction(relation),
        **interval_abundance_features(relation, intervals),
        **local_dimension_features(relation, intervals, rng),
    }
    global_obstruction, interval_obstruction = dim2_obstruction_fraction(
        relation,
        intervals,
        rng,
    )
    features["global_dim2_obstruction_fraction"] = global_obstruction
    features["interval_dim2_obstruction_fraction"] = interval_obstruction
    return features


def self_tests() -> dict[str, bool]:
    chain = np.triu(np.ones((6, 6), dtype=bool), k=1)
    antichain = np.zeros((6, 6), dtype=bool)
    standard_example = np.zeros((6, 6), dtype=bool)
    for i in range(3):
        for j in range(3):
            if i != j:
                standard_example[i, 3 + j] = True

    return {
        "chain_is_dim2": is_dimension_at_most_two(chain),
        "antichain_is_dim2": is_dimension_at_most_two(antichain),
        "standard_example_S3_is_not_dim2": not is_dimension_at_most_two(standard_example),
    }


def build_dataset(rng: np.random.Generator) -> pd.DataFrame:
    rows: list[dict[str, object]] = []

    for split, n in SPLITS.items():
        for pair_id in range(PAIRS_PER_SPLIT):
            manifold = sample_minkowski_2d(n, rng)
            target = relation_fraction(manifold)
            null, null_fraction, direct_edges, attempts = matched_transitive_percolation(
                n,
                target,
                rng,
            )

            manifold_features = extract_features(manifold, rng)
            null_features = extract_features(null, rng)

            rows.append(
                {
                    "split": split,
                    "n": n,
                    "pair_id": pair_id,
                    "family": "minkowski_2d",
                    "label_manifold": 1,
                    "target_ordering_fraction": target,
                    "ordering_fraction_mismatch": 0.0,
                    "null_direct_edges": float("nan"),
                    "null_matching_attempts": float("nan"),
                    **manifold_features,
                }
            )
            rows.append(
                {
                    "split": split,
                    "n": n,
                    "pair_id": pair_id,
                    "family": "transitive_percolation",
                    "label_manifold": 0,
                    "target_ordering_fraction": target,
                    "ordering_fraction_mismatch": abs(null_fraction - target),
                    "null_direct_edges": direct_edges,
                    "null_matching_attempts": attempts,
                    **null_features,
                }
            )

    return pd.DataFrame(rows)


def make_model() -> Pipeline:
    return Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(
                    max_iter=5000,
                    class_weight="balanced",
                    random_state=SEED,
                ),
            ),
        ]
    )


def paired_bootstrap_ci(
    frame: pd.DataFrame,
    predictions: np.ndarray,
    rng: np.random.Generator,
) -> tuple[float, float]:
    """Efficient paired bootstrap preserving one positive and one null per pair."""
    truth = frame["label_manifold"].to_numpy(dtype=int)
    pair_ids = frame["pair_id"].to_numpy(dtype=int)
    unique_pairs = np.asarray(sorted(np.unique(pair_ids)))
    pair_scores = np.empty(len(unique_pairs), dtype=float)

    for index, pair_id in enumerate(unique_pairs):
        selected = pair_ids == pair_id
        local_truth = truth[selected]
        local_prediction = predictions[selected]
        positive_correct = float(local_prediction[local_truth == 1][0] == 1)
        negative_correct = float(local_prediction[local_truth == 0][0] == 0)
        pair_scores[index] = 0.5 * (positive_correct + negative_correct)

    sampled_indices = rng.integers(
        0,
        len(pair_scores),
        size=(BOOTSTRAPS, len(pair_scores)),
    )
    scores = pair_scores[sampled_indices].mean(axis=1)
    low, high = np.quantile(scores, [0.025, 0.975])
    return float(low), float(high)


def evaluate(
    training: pd.DataFrame,
    testing: pd.DataFrame,
    feature_names: list[str],
    rng: np.random.Generator,
) -> tuple[dict[str, object], np.ndarray, np.ndarray]:
    model = make_model()
    model.fit(training[feature_names], training["label_manifold"])
    probability = model.predict_proba(testing[feature_names])[:, 1]
    prediction = (probability >= 0.5).astype(int)
    truth = testing["label_manifold"].to_numpy(dtype=int)
    low, high = paired_bootstrap_ci(testing, prediction, rng)
    metrics = {
        "features": feature_names,
        "balanced_accuracy": float(balanced_accuracy_score(truth, prediction)),
        "roc_auc": float(roc_auc_score(truth, probability)),
        "confusion_matrix": confusion_matrix(truth, prediction).tolist(),
        "paired_bootstrap_95_ci": [low, high],
    }
    return metrics, prediction, probability


def main() -> None:
    output = Path("a12_exact_results")
    output.mkdir(exist_ok=True)
    rng = np.random.default_rng(SEED)

    tests = self_tests()
    if not all(tests.values()):
        raise RuntimeError(f"Dimension-2 self-test failed: {tests}")

    dataset = build_dataset(rng)
    dataset.to_csv(output / "a12_dataset.csv", index=False)

    training = dataset[dataset["split"] == "train"].reset_index(drop=True)
    evaluations: dict[str, dict[str, object]] = {}
    prediction_frames = []

    feature_sets = {
        "primary_combined": PRIMARY_FEATURES,
        "interval_abundance_only": INTERVAL_FEATURES,
        "local_dimension_only": LOCAL_DIM_FEATURES,
        "local_embeddability_only": EMBED_FEATURES,
        "ordering_fraction_only": ["ordering_fraction"],
    }

    for split in ("test_96", "test_128"):
        testing = dataset[dataset["split"] == split].reset_index(drop=True)
        evaluations[split] = {}
        for name, features in feature_sets.items():
            metrics, prediction, probability = evaluate(
                training,
                testing,
                features,
                rng,
            )
            evaluations[split][name] = metrics
            if name == "primary_combined":
                prediction_frame = testing.copy()
                prediction_frame["predicted_probability"] = probability
                prediction_frame["predicted_label"] = prediction
                prediction_frames.append(prediction_frame)

    pd.concat(prediction_frames, ignore_index=True).to_csv(
        output / "a12_primary_predictions.csv",
        index=False,
    )

    null_rows = dataset[dataset["label_manifold"] == 0]
    maximum_mismatch = float(null_rows["ordering_fraction_mismatch"].max())
    mean_mismatch = float(null_rows["ordering_fraction_mismatch"].mean())

    primary_96 = evaluations["test_96"]["primary_combined"]
    primary_128 = evaluations["test_128"]["primary_combined"]
    density_96 = evaluations["test_96"]["ordering_fraction_only"]
    density_128 = evaluations["test_128"]["ordering_fraction_only"]

    gates = {
        "G1_all_self_tests_pass": all(tests.values()),
        "G2_max_ordering_fraction_mismatch_le_0_02": maximum_mismatch <= 0.02,
        "G3_balanced_accuracy_n96_ge_0_80": primary_96["balanced_accuracy"] >= 0.80,
        "G4_balanced_accuracy_n128_ge_0_80": primary_128["balanced_accuracy"] >= 0.80,
        "G5_bootstrap_lower_n96_gt_0_60": primary_96["paired_bootstrap_95_ci"][0] > 0.60,
        "G6_bootstrap_lower_n128_gt_0_60": primary_128["paired_bootstrap_95_ci"][0] > 0.60,
        "G7_density_baseline_n96_le_0_60": density_96["balanced_accuracy"] <= 0.60,
        "G8_density_baseline_n128_le_0_60": density_128["balanced_accuracy"] <= 0.60,
    }
    verdict = "PASS_TARGETED_2D_DISCRIMINATION" if all(gates.values()) else "FAIL_TARGETED_2D_DISCRIMINATION"

    family_means = (
        dataset.groupby(["split", "family"])[EMBED_FEATURES + LOCAL_DIM_FEATURES]
        .mean(numeric_only=True)
        .reset_index()
    )
    family_means.to_csv(output / "a12_family_feature_means.csv", index=False)

    summary = {
        "seed": SEED,
        "splits": SPLITS,
        "pairs_per_split": PAIRS_PER_SPLIT,
        "self_tests": tests,
        "feature_families": {
            "interval_abundance": INTERVAL_FEATURES,
            "local_dimension_consistency": LOCAL_DIM_FEATURES,
            "local_2d_embeddability": EMBED_FEATURES,
        },
        "matching": {
            "maximum_absolute_mismatch": maximum_mismatch,
            "mean_absolute_mismatch": mean_mismatch,
            "required_maximum": MAX_MATCH_MISMATCH,
        },
        "evaluations": evaluations,
        "gates": gates,
        "verdict": verdict,
        "interpretation_boundary": (
            "A pass establishes prospective discrimination between finite 2D "
            "Minkowski interval orders and individually ordering-fraction-matched "
            "transitive-percolation posets at n=96 and n=128. It does not establish "
            "that a generic relational domain is a spacetime or that physical time "
            "has emerged."
        ),
    }

    (output / "a12_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    report = f"""# A12 — Targeted 2D Manifoldlikeness Audit

## Frozen design

- Train: n=64.
- Prospective tests: n=96 and n=128.
- {PAIRS_PER_SPLIT} matched Minkowski/null pairs per split.
- Null: transitive percolation matched individually by ordering fraction.
- Feature families: interval abundance, local dimension consistency, and exact local 2D-order obstructions.

## Matching

- Mean absolute mismatch: {mean_mismatch:.8f}
- Maximum absolute mismatch: {maximum_mismatch:.8f}

## Primary results

- n=96 balanced accuracy: {primary_96['balanced_accuracy']:.6f}
- n=96 ROC AUC: {primary_96['roc_auc']:.6f}
- n=96 paired bootstrap CI: {primary_96['paired_bootstrap_95_ci']}
- n=128 balanced accuracy: {primary_128['balanced_accuracy']:.6f}
- n=128 ROC AUC: {primary_128['roc_auc']:.6f}
- n=128 paired bootstrap CI: {primary_128['paired_bootstrap_95_ci']}

## Verdict

{verdict}

## Boundary

This is a targeted finite discrimination result. It is not a derivation of a Lorentzian continuum, spacetime, gravity, physical causality, or a fundamental selection principle.
"""
    (output / "a12_report.md").write_text(report, encoding="utf-8")

    print(json.dumps(summary, indent=2))
    print(f"Results written to: {output.resolve()}")


if __name__ == "__main__":
    main()
