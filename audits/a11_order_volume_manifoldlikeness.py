#!/usr/bin/env python3
"""
A11 — Order–Volume Correspondence and Manifoldlikeness Audit

Confirmatory dimensions: 2D and 3D Minkowski Alexandrov intervals.
Prospective size split:
    training: n = 64
    testing:  n = 96

Diagnostic only:
    4D Minkowski, n = 128

Non-geometric null families:
    1. transitive percolation / random DAG closure;
    2. random three-layer posets.

The nulls are matched to the ordering fraction of manifold samples.
A classifier is trained only on n=64 and evaluated only on n=96.

Primary gate (frozen before the confirmatory run):
    balanced accuracy >= 0.75 and bootstrap 95% lower bound > 0.50.

Scientific boundary:
This audit tests whether order–volume statistics distinguish finite
Minkowski sprinklings from matched non-geometric nulls. It does not derive
spacetime, physical causality, gravity, or a fundamental selection law.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.special import gammaln
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


SEED = 20260712
TRAIN_N = 64
TEST_N = 96
D4_N = 128

CONFIRMATORY_DIMS = (2, 3)
MANIFOLD_PER_DIM_SPLIT = 20
NULL_PER_FAMILY_DIM_SPLIT = 10
D4_DIAGNOSTIC_SAMPLES = 16

MIN_REG_INTERVAL = 8
MIN_MID_INTERVAL = 16

FEATURES = [
    "abs_d_lc_minus_d_mm",
    "abs_d_mid_minus_d_mm",
    "r2_lc",
    "mad_mid",
    "branch_excess",
    "usable_reg_fraction",
    "usable_mid_fraction",
]


def ordering_fraction_theory(dimension: float) -> float:
    """Myrheim–Meyer ordering fraction for a Minkowski interval."""
    return math.exp(
        gammaln(dimension + 1.0)
        + gammaln(dimension / 2.0)
        - math.log(2.0)
        - gammaln(1.5 * dimension)
    )


def myrheim_meyer_dimension(ordering_fraction: float) -> float:
    low = 1.01
    high = 12.0
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


def transitive_closure(relation: np.ndarray) -> np.ndarray:
    reach = relation.copy()
    n = reach.shape[0]
    for k in range(n):
        reach |= reach[:, k, None] & reach[None, k, :]
    np.fill_diagonal(reach, False)
    return reach


def sample_minkowski_poset(
    n: int,
    dimension: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """
    Uniformly sample n points in a unit Alexandrov interval of d-dimensional
    Minkowski spacetime, then retain only the induced causal order.
    """
    radial_cap = 0.5 * np.power(rng.random(n), 1.0 / dimension)
    second_half = rng.random(n) >= 0.5
    time = np.where(second_half, 1.0 - radial_cap, radial_cap)

    spatial_dimension = dimension - 1
    if spatial_dimension == 1:
        sign = np.where(rng.random(n) < 0.5, -1.0, 1.0)
        radius = radial_cap * rng.random(n)
        spatial = (sign * radius)[:, None]
    else:
        direction = rng.normal(size=(n, spatial_dimension))
        norms = np.linalg.norm(direction, axis=1)
        direction /= norms[:, None]
        radius = radial_cap * np.power(
            rng.random(n),
            1.0 / spatial_dimension,
        )
        spatial = direction * radius[:, None]

    dt = time[None, :] - time[:, None]
    dx = spatial[None, :, :] - spatial[:, None, :]
    distance_squared = np.sum(dx * dx, axis=2)

    relation = (dt > 0.0) & (
        dt * dt >= distance_squared - 1e-14
    )
    np.fill_diagonal(relation, False)
    return relation


def random_dag_closure(
    n: int,
    probability: float,
    rng: np.random.Generator,
) -> np.ndarray:
    edges = np.triu(
        rng.random((n, n)) < probability,
        k=1,
    )
    permutation = rng.permutation(n)
    permuted = np.zeros((n, n), dtype=bool)
    permuted[np.ix_(permutation, permutation)] = edges
    return transitive_closure(permuted)


def random_three_layer_poset(
    n: int,
    probability: float,
    rng: np.random.Generator,
) -> np.ndarray:
    permutation = rng.permutation(n)
    first_size = n // 4
    second_size = n // 2
    first = permutation[:first_size]
    second = permutation[first_size : first_size + second_size]
    third = permutation[first_size + second_size :]

    relation = np.zeros((n, n), dtype=bool)

    block_01 = rng.random((len(first), len(second))) < probability
    block_12 = rng.random((len(second), len(third))) < probability

    relation[np.ix_(first, second)] = block_01
    relation[np.ix_(second, third)] = block_12

    return transitive_closure(relation)


NULL_GENERATORS: dict[
    str,
    Callable[[int, float, np.random.Generator], np.ndarray],
] = {
    "transitive_percolation": random_dag_closure,
    "three_layer": random_three_layer_poset,
}


def topological_order(relation: np.ndarray) -> list[int]:
    n = relation.shape[0]
    indegree = relation.sum(axis=0).astype(int)
    available = [int(x) for x in np.flatnonzero(indegree == 0)]
    order: list[int] = []

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


def longest_chain_matrix(relation: np.ndarray) -> np.ndarray:
    n = relation.shape[0]
    order = topological_order(relation)
    longest = np.zeros((n, n), dtype=np.int16)

    for source_index, source in enumerate(order):
        longest[source, source] = 1

        for target in order[source_index + 1 :]:
            if not relation[source, target]:
                continue

            predecessors = np.flatnonzero(
                relation[:, target] & (longest[source] > 0)
            )
            if len(predecessors):
                longest[source, target] = (
                    int(longest[source, predecessors].max()) + 1
                )

    return longest


def extract_features(relation: np.ndarray) -> dict[str, float]:
    n = relation.shape[0]
    reflexive = relation | np.eye(n, dtype=bool)

    interval_volume = (
        reflexive.astype(np.int16) @ reflexive.astype(np.int16)
    ).astype(np.int16)
    longest = longest_chain_matrix(relation)

    comparable_pairs = np.argwhere(relation)
    number_pairs = len(comparable_pairs)

    ordering_fraction = relation_fraction(relation)
    d_mm = myrheim_meyer_dimension(ordering_fraction)

    regression_pairs = [
        (int(i), int(j))
        for i, j in comparable_pairs
        if interval_volume[i, j] >= MIN_REG_INTERVAL
        and longest[i, j] >= 3
    ]

    d_lc = float("nan")
    r2_lc = float("nan")

    if len(regression_pairs) >= 8:
        x = np.log(
            np.asarray(
                [interval_volume[i, j] for i, j in regression_pairs],
                dtype=float,
            )
        )
        y = np.log(
            np.asarray(
                [longest[i, j] for i, j in regression_pairs],
                dtype=float,
            )
        )

        slope, intercept = np.polyfit(x, y, 1)
        prediction = intercept + slope * x
        residual = float(np.sum((y - prediction) ** 2))
        total = float(np.sum((y - y.mean()) ** 2))

        if slope > 1e-8:
            d_lc = float(1.0 / slope)
        if total > 0.0:
            r2_lc = float(1.0 - residual / total)

    midpoint_dimensions: list[float] = []

    for raw_i, raw_j in comparable_pairs:
        i = int(raw_i)
        j = int(raw_j)

        if interval_volume[i, j] < MIN_MID_INTERVAL:
            continue

        interior = np.flatnonzero(relation[i] & relation[:, j])
        if len(interior) == 0:
            continue

        best_balance = max(
            min(
                int(interval_volume[i, middle]),
                int(interval_volume[middle, j]),
            )
            for middle in interior
        )

        if best_balance > 0:
            midpoint_dimensions.append(
                float(
                    math.log(
                        interval_volume[i, j] / best_balance,
                        2.0,
                    )
                )
            )

    if midpoint_dimensions:
        midpoint_array = np.asarray(midpoint_dimensions)
        d_mid = float(np.median(midpoint_array))
        mad_mid = float(
            np.median(np.abs(midpoint_array - d_mid))
        )
    else:
        d_mid = float("nan")
        mad_mid = float("nan")

    branching_values = [
        float(
            (interval_volume[i, j] - longest[i, j])
            / interval_volume[i, j]
        )
        for i, j in regression_pairs
    ]
    branch_excess = (
        float(np.median(branching_values))
        if branching_values
        else float("nan")
    )

    usable_reg_fraction = (
        len(regression_pairs) / number_pairs
        if number_pairs
        else 0.0
    )
    usable_mid_fraction = (
        len(midpoint_dimensions) / number_pairs
        if number_pairs
        else 0.0
    )

    return {
        "n": n,
        "ordering_fraction": ordering_fraction,
        "d_mm": d_mm,
        "d_lc": d_lc,
        "r2_lc": r2_lc,
        "d_mid": d_mid,
        "mad_mid": mad_mid,
        "branch_excess": branch_excess,
        "usable_reg_fraction": usable_reg_fraction,
        "usable_mid_fraction": usable_mid_fraction,
        "number_comparable_pairs": number_pairs,
        "number_regression_intervals": len(regression_pairs),
        "number_midpoint_intervals": len(midpoint_dimensions),
        "abs_d_lc_minus_d_mm": (
            abs(d_lc - d_mm) if math.isfinite(d_lc) else float("nan")
        ),
        "abs_d_mid_minus_d_mm": (
            abs(d_mid - d_mm)
            if math.isfinite(d_mid)
            else float("nan")
        ),
    }


def calibrate_null_probability(
    generator: Callable[[int, float, np.random.Generator], np.ndarray],
    n: int,
    target_fraction: float,
    rng: np.random.Generator,
) -> float:
    low = 1e-5
    high = 0.999

    for _ in range(10):
        midpoint = math.sqrt(low * high)
        observed = np.median(
            [
                relation_fraction(generator(n, midpoint, rng))
                for _ in range(5)
            ]
        )

        if observed < target_fraction:
            low = midpoint
        else:
            high = midpoint

    return math.sqrt(low * high)


def matched_null(
    generator: Callable[[int, float, np.random.Generator], np.ndarray],
    n: int,
    calibrated_probability: float,
    target_fraction: float,
    rng: np.random.Generator,
) -> tuple[np.ndarray, float]:
    multipliers = np.exp(
        np.linspace(-0.45, 0.45, 10)
        + rng.normal(0.0, 0.04, size=10)
    )

    best_relation: np.ndarray | None = None
    best_probability = calibrated_probability
    best_error = float("inf")

    for multiplier in multipliers:
        probability = float(
            np.clip(
                calibrated_probability * multiplier,
                1e-6,
                0.999999,
            )
        )
        candidate = generator(n, probability, rng)
        error = abs(relation_fraction(candidate) - target_fraction)

        if error < best_error:
            best_error = error
            best_relation = candidate
            best_probability = probability

    assert best_relation is not None
    return best_relation, best_probability


def build_split(
    split_name: str,
    n: int,
    rng: np.random.Generator,
    calibrated: dict[tuple[str, int, int], float],
) -> list[dict[str, float | str | int]]:
    rows: list[dict[str, float | str | int]] = []

    manifold_by_dimension: dict[int, list[dict[str, object]]] = {}

    for dimension in CONFIRMATORY_DIMS:
        samples: list[dict[str, object]] = []

        for sample_index in range(MANIFOLD_PER_DIM_SPLIT):
            relation = sample_minkowski_poset(n, dimension, rng)
            features = extract_features(relation)

            row: dict[str, float | str | int] = {
                "split": split_name,
                "family": "minkowski",
                "label_manifold": 1,
                "dimension_target": dimension,
                "sample_index": sample_index,
                "null_probability": float("nan"),
                "target_ordering_fraction": features[
                    "ordering_fraction"
                ],
                "ordering_fraction_mismatch": 0.0,
                **features,
            }
            rows.append(row)
            samples.append(
                {
                    "relation_fraction": features[
                        "ordering_fraction"
                    ],
                }
            )

        manifold_by_dimension[dimension] = samples

    for dimension in CONFIRMATORY_DIMS:
        manifold_samples = manifold_by_dimension[dimension]

        for family_name, generator in NULL_GENERATORS.items():
            probability = calibrated[(family_name, n, dimension)]

            for sample_index in range(NULL_PER_FAMILY_DIM_SPLIT):
                target = float(
                    manifold_samples[
                        sample_index % len(manifold_samples)
                    ]["relation_fraction"]
                )

                relation, used_probability = matched_null(
                    generator,
                    n,
                    probability,
                    target,
                    rng,
                )
                features = extract_features(relation)

                rows.append(
                    {
                        "split": split_name,
                        "family": family_name,
                        "label_manifold": 0,
                        "dimension_target": dimension,
                        "sample_index": sample_index,
                        "null_probability": used_probability,
                        "target_ordering_fraction": target,
                        "ordering_fraction_mismatch": abs(
                            features["ordering_fraction"] - target
                        ),
                        **features,
                    }
                )

    return rows


def bootstrap_balanced_accuracy(
    truth: np.ndarray,
    prediction: np.ndarray,
    rng: np.random.Generator,
    repetitions: int = 2000,
) -> tuple[float, float]:
    values = []
    n = len(truth)

    for _ in range(repetitions):
        indices = rng.integers(0, n, size=n)
        sampled_truth = truth[indices]

        if len(np.unique(sampled_truth)) < 2:
            continue

        values.append(
            balanced_accuracy_score(
                sampled_truth,
                prediction[indices],
            )
        )

    low, high = np.quantile(values, [0.025, 0.975])
    return float(low), float(high)


def evaluate_classifier(
    training: pd.DataFrame,
    testing: pd.DataFrame,
    feature_names: list[str],
    rng: np.random.Generator,
) -> tuple[Pipeline, dict[str, object], np.ndarray, np.ndarray]:
    model = Pipeline(
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

    x_train = training[feature_names].to_numpy()
    y_train = training["label_manifold"].to_numpy(dtype=int)
    x_test = testing[feature_names].to_numpy()
    y_test = testing["label_manifold"].to_numpy(dtype=int)

    model.fit(x_train, y_train)
    probability = model.predict_proba(x_test)[:, 1]
    prediction = (probability >= 0.5).astype(int)

    low, high = bootstrap_balanced_accuracy(
        y_test,
        prediction,
        rng,
    )

    metrics: dict[str, object] = {
        "features": feature_names,
        "accuracy": float(accuracy_score(y_test, prediction)),
        "balanced_accuracy": float(
            balanced_accuracy_score(y_test, prediction)
        ),
        "roc_auc": float(roc_auc_score(y_test, probability)),
        "confusion_matrix": confusion_matrix(
            y_test,
            prediction,
        ).tolist(),
        "bootstrap_95_ci_balanced_accuracy": [low, high],
    }

    return model, metrics, prediction, probability


def grouped_balanced_accuracy(
    testing: pd.DataFrame,
    prediction: np.ndarray,
) -> list[dict[str, object]]:
    frame = testing.copy()
    frame["prediction"] = prediction

    rows: list[dict[str, object]] = []

    for dimension in CONFIRMATORY_DIMS:
        for null_family in NULL_GENERATORS:
            selected = frame[
                (frame["dimension_target"] == dimension)
                & (
                    (frame["family"] == "minkowski")
                    | (frame["family"] == null_family)
                )
            ]

            rows.append(
                {
                    "dimension": dimension,
                    "null_family": null_family,
                    "number_samples": int(len(selected)),
                    "balanced_accuracy": float(
                        balanced_accuracy_score(
                            selected["label_manifold"],
                            selected["prediction"],
                        )
                    ),
                }
            )

    return rows


def main() -> None:
    output = Path("a11_exact_results")
    output.mkdir(exist_ok=True)

    rng = np.random.default_rng(SEED)

    calibrated: dict[tuple[str, int, int], float] = {}
    calibration_rows = []

    for n in (TRAIN_N, TEST_N):
        for dimension in CONFIRMATORY_DIMS:
            target = ordering_fraction_theory(dimension)

            for family_name, generator in NULL_GENERATORS.items():
                probability = calibrate_null_probability(
                    generator,
                    n,
                    target,
                    rng,
                )
                calibrated[(family_name, n, dimension)] = probability
                calibration_rows.append(
                    {
                        "family": family_name,
                        "n": n,
                        "dimension_target": dimension,
                        "theoretical_ordering_fraction": target,
                        "calibrated_probability": probability,
                    }
                )

    pd.DataFrame(calibration_rows).to_csv(
        output / "a11_null_calibration.csv",
        index=False,
    )

    rows = []
    rows.extend(build_split("train", TRAIN_N, rng, calibrated))
    rows.extend(build_split("test", TEST_N, rng, calibrated))

    dataset = pd.DataFrame(rows)
    dataset.to_csv(
        output / "a11_confirmatory_dataset.csv",
        index=False,
    )

    training = dataset[dataset["split"] == "train"].reset_index(drop=True)
    testing = dataset[dataset["split"] == "test"].reset_index(drop=True)

    _, primary_metrics, prediction, probability = evaluate_classifier(
        training,
        testing,
        FEATURES,
        rng,
    )

    _, baseline_metrics, _, _ = evaluate_classifier(
        training,
        testing,
        ["ordering_fraction"],
        rng,
    )

    testing_predictions = testing.copy()
    testing_predictions["predicted_manifold_probability"] = probability
    testing_predictions["predicted_label"] = prediction
    testing_predictions.to_csv(
        output / "a11_test_predictions.csv",
        index=False,
    )

    grouped_results = grouped_balanced_accuracy(
        testing,
        prediction,
    )
    pd.DataFrame(grouped_results).to_csv(
        output / "a11_grouped_performance.csv",
        index=False,
    )

    d4_rows = []
    for sample_index in range(D4_DIAGNOSTIC_SAMPLES):
        relation = sample_minkowski_poset(D4_N, 4, rng)
        features = extract_features(relation)
        d4_rows.append(
            {
                "sample_index": sample_index,
                "dimension_target": 4,
                **features,
            }
        )

    d4_frame = pd.DataFrame(d4_rows)
    d4_frame.to_csv(
        output / "a11_d4_feasibility.csv",
        index=False,
    )

    null_rows = dataset[dataset["family"] != "minkowski"]
    matching_mae = float(
        null_rows["ordering_fraction_mismatch"].mean()
    )
    matching_max = float(
        null_rows["ordering_fraction_mismatch"].max()
    )

    d4_sufficient = (
        (d4_frame["number_regression_intervals"] >= 20)
        & (d4_frame["number_midpoint_intervals"] >= 5)
    )
    d4_sufficient_fraction = float(d4_sufficient.mean())

    primary_balanced = float(primary_metrics["balanced_accuracy"])
    primary_lower = float(
        primary_metrics["bootstrap_95_ci_balanced_accuracy"][0]
    )
    baseline_balanced = float(baseline_metrics["balanced_accuracy"])

    grouped_minimum = float(
        min(row["balanced_accuracy"] for row in grouped_results)
    )

    gates = {
        "G1_ordering_fraction_matching_mae_le_0_02": (
            matching_mae <= 0.02
        ),
        "G2_test_balanced_accuracy_ge_0_75": (
            primary_balanced >= 0.75
        ),
        "G3_bootstrap_lower_bound_gt_0_50": (
            primary_lower > 0.50
        ),
        "G4_each_dimension_null_pair_ge_0_65": (
            grouped_minimum >= 0.65
        ),
        "G5_ordering_fraction_only_baseline_le_0_60": (
            baseline_balanced <= 0.60
        ),
        "G6_d4_finite_sample_feasibility_ge_0_80": (
            d4_sufficient_fraction >= 0.80
        ),
    }

    confirmatory_pass = all(
        gates[key]
        for key in (
            "G1_ordering_fraction_matching_mae_le_0_02",
            "G2_test_balanced_accuracy_ge_0_75",
            "G3_bootstrap_lower_bound_gt_0_50",
            "G4_each_dimension_null_pair_ge_0_65",
            "G5_ordering_fraction_only_baseline_le_0_60",
        )
    )

    summary = {
        "seed": SEED,
        "confirmatory_dimensions": list(CONFIRMATORY_DIMS),
        "training_size_n": TRAIN_N,
        "testing_size_n": TEST_N,
        "d4_diagnostic_size_n": D4_N,
        "training_samples": int(len(training)),
        "testing_samples": int(len(testing)),
        "primary_features": FEATURES,
        "null_matching": {
            "mean_absolute_ordering_fraction_mismatch": matching_mae,
            "maximum_ordering_fraction_mismatch": matching_max,
        },
        "primary_classifier": primary_metrics,
        "ordering_fraction_only_baseline": baseline_metrics,
        "grouped_performance": grouped_results,
        "d4_diagnostic": {
            "number_samples": D4_DIAGNOSTIC_SAMPLES,
            "fraction_with_at_least_20_regression_and_5_midpoint_intervals": (
                d4_sufficient_fraction
            ),
            "median_number_regression_intervals": float(
                d4_frame["number_regression_intervals"].median()
            ),
            "median_number_midpoint_intervals": float(
                d4_frame["number_midpoint_intervals"].median()
            ),
            "median_d_mm": float(d4_frame["d_mm"].median()),
            "median_d_lc": float(d4_frame["d_lc"].median()),
            "median_d_mid": float(d4_frame["d_mid"].median()),
        },
        "gates": gates,
        "confirmatory_verdict": (
            "PASS_ORDER_VOLUME_DISCRIMINATION"
            if confirmatory_pass
            else "FAIL_ORDER_VOLUME_DISCRIMINATION"
        ),
        "interpretation_boundary": (
            "A pass means the frozen order-volume feature set separates "
            "finite 2D/3D Minkowski sprinklings from the two tested matched "
            "null families across a prospective size shift. It does not "
            "show that generic relational structures generate spacetime."
        ),
    }

    (output / "a11_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    report = f"""# A11 — Order–Volume Correspondence and Manifoldlikeness Audit

## Design

- Confirmatory dimensions: 2 and 3.
- Train size: n={TRAIN_N}.
- Prospective test size: n={TEST_N}.
- Nulls: transitive percolation and random three-layer posets.
- Null matching: ordering fraction.
- Primary endpoint: balanced accuracy >= 0.75 with bootstrap lower bound > 0.50.
- 4D was diagnostic only because the feasibility pilot showed sparse large intervals.

## Results

- Mean absolute ordering-fraction mismatch: {matching_mae:.6f}
- Test balanced accuracy: {primary_balanced:.6f}
- Test ROC AUC: {primary_metrics["roc_auc"]:.6f}
- Bootstrap 95% CI: {primary_metrics["bootstrap_95_ci_balanced_accuracy"]}
- Ordering-fraction-only balanced accuracy: {baseline_balanced:.6f}
- Minimum grouped balanced accuracy: {grouped_minimum:.6f}
- 4D sufficient-interval fraction: {d4_sufficient_fraction:.6f}

## Verdict

{summary["confirmatory_verdict"]}

## Boundary

This result is a discrimination result against two specified null families.
It is not a derivation of spacetime, gravity, a Lorentzian continuum, or a
fundamental law of selection.
"""

    (output / "a11_report.md").write_text(
        report,
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2))
    print()
    print(f"Results written to: {output.resolve()}")


if __name__ == "__main__":
    main()
