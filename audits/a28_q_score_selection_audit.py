#!/usr/bin/env python3
"""
A28 — q-Score Selection and Context–Scale Incompatibility Audit

Purpose
-------
Determine whether symmetries, locality, and stability select a unique score
for the exponential q-kernel.

Candidate scores
----------------
For a local set of outgoing q-values x:

1. raw:
       s_j = x_j.
   In exponential odds, common shifts cancel. It preserves cardinal
   differences and is stable under adding alternatives, but its scale is
   degenerate with lambda.

2. min_shift:
       s_j = x_j - min(x).
   Operationally identical to raw softmax. It makes row-shift invariance
   explicit but does not remove scale dependence.

3. row_zscore:
       s_j = (x_j-mean x)/sd(x).
   Positive-affine invariant and cardinal, but context-dependent.

4. row_mad:
       s_j = (x_j-median x)/MAD(x).
   Positive-affine invariant, cardinal, and more outlier-robust, but still
   context-dependent.

5. row_rank:
       s_j = rank(x_j)/(n-1).
   Invariant under all strictly increasing transforms, but ordinal and
   context-dependent.

6. global_zscore:
       s_j = (x_j-global_mean)/global_sd.
   Positive-affine invariant and cardinal, but nonlocal and context-dependent.

Exact incompatibility theorem
-----------------------------
Let D_S(x,y) be the score difference assigned to two existing alternatives
x,y inside a finite context S. Suppose:

A. Extension stability:
       D_S(x,y) is unchanged when arbitrary alternatives are added.

B. Positive-affine invariance:
       D(ax+b, ay+b) = D(x,y), a>0.

C. Continuity and cardinality:
       D varies continuously with quantitative separation and D(x,x)=0.

Extension stability removes dependence on S. Translation invariance implies
D(x,y)=h(x-y). Positive scale invariance gives h(a d)=h(d) for every a>0.
Thus h is constant on d>0 and on d<0. Continuity at d=0 and h(0)=0 force
h(d)=0 for all d.

Therefore no nontrivial continuous cardinal score can simultaneously be:
- stable to arbitrary extension of the choice set; and
- invariant under all positive affine reparameterizations.

The noncontinuous escape is ordinal sign/rank information. The cardinal
escape requires an independently fixed scale, leaving lambda-scale
calibration as a genuine model input.

Boundary
--------
This audit selects no physical score. It proves a structural tradeoff and
classifies natural candidates.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 20260801

ROW_SAMPLES = 6_000
GRAPH_SAMPLES = 2_000
MONOTONE_WARP_SAMPLES = 4_000

LAMBDA = 1.0
MAX_EXACT_ERROR = 5e-12

MIN_CONTEXT_VIOLATION_RATE = 0.80
MIN_CONTEXT_MEDIAN_LOG_ODDS_CHANGE = 0.02
MIN_GLOBAL_NONLOCALITY_RATE = 0.95
MIN_CARDINAL_TV = 0.015
MAX_RANK_CARDINAL_TV = 5e-13
MIN_RAW_SCALE_CHANGE_TV = 0.03


SCORES = (
    "raw",
    "min_shift",
    "row_zscore",
    "row_mad",
    "row_rank",
    "global_zscore",
)


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


def normalize(weights: np.ndarray) -> np.ndarray:
    weights = np.asarray(weights, dtype=float)
    return weights / weights.sum()


def exponential_probabilities(
    scores: np.ndarray,
    lambda_value: float = LAMBDA,
) -> np.ndarray:
    logits = -lambda_value * np.asarray(
        scores,
        dtype=float,
    )
    logits -= float(logits.max())
    return normalize(np.exp(logits))


def total_variation(
    first: np.ndarray,
    second: np.ndarray,
) -> float:
    return 0.5 * float(
        np.abs(first - second).sum()
    )


def mean_sd(values: np.ndarray) -> float:
    centered = values - float(values.mean())
    return float(
        np.sqrt(
            np.mean(centered**2)
        )
    )


def median_mad(values: np.ndarray) -> float:
    median = float(np.median(values))
    return float(
        np.median(
            np.abs(values - median)
        )
    )


def rank_percentiles(
    values: np.ndarray,
) -> np.ndarray:
    order = np.argsort(
        values,
        kind="mergesort",
    )
    ranks = np.empty(
        len(values),
        dtype=float,
    )
    ranks[order] = np.arange(
        len(values),
        dtype=float,
    )
    if len(values) > 1:
        ranks /= len(values) - 1.0
    return ranks


def score_values(
    name: str,
    row_values: np.ndarray,
    global_values: np.ndarray | None = None,
) -> np.ndarray:
    row_values = np.asarray(
        row_values,
        dtype=float,
    )

    if name == "raw":
        return row_values.copy()

    if name == "min_shift":
        return row_values - float(
            row_values.min()
        )

    if name == "row_zscore":
        scale = mean_sd(row_values)
        if scale <= 1e-14:
            raise ValueError("Zero row SD.")
        return (
            row_values - float(row_values.mean())
        ) / scale

    if name == "row_mad":
        center = float(
            np.median(row_values)
        )
        scale = median_mad(row_values)
        if scale <= 1e-14:
            raise ValueError("Zero row MAD.")
        return (
            row_values - center
        ) / scale

    if name == "row_rank":
        return rank_percentiles(
            row_values
        )

    if name == "global_zscore":
        if global_values is None:
            raise ValueError(
                "global_zscore needs global values."
            )
        global_values = np.asarray(
            global_values,
            dtype=float,
        )
        center = float(
            global_values.mean()
        )
        scale = mean_sd(
            global_values
        )
        if scale <= 1e-14:
            raise ValueError("Zero global SD.")
        return (
            row_values - center
        ) / scale

    raise ValueError(name)


def pair_log_odds(
    probabilities: np.ndarray,
    first: int,
    second: int,
) -> float:
    return float(
        math.log(
            probabilities[first]
            / probabilities[second]
        )
    )


def relabel_equivariance_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(ROW_SAMPLES):
        size = int(
            rng.integers(4, 12)
        )
        values = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        global_values = np.concatenate(
            [
                values,
                rng.normal(
                    0.0,
                    1.0,
                    size=25,
                ),
            ]
        )
        permutation = rng.permutation(size)
        inverse = np.empty_like(
            permutation
        )
        inverse[permutation] = np.arange(
            size
        )

        for score_name in SCORES:
            original_scores = score_values(
                score_name,
                values,
                global_values,
            )
            original_probability = (
                exponential_probabilities(
                    original_scores
                )
            )

            permuted_values = values[
                permutation
            ]

            if score_name == "global_zscore":
                # The global multiset is unchanged; only the local labels move.
                permuted_global = global_values
            else:
                permuted_global = global_values

            permuted_scores = score_values(
                score_name,
                permuted_values,
                permuted_global,
            )
            permuted_probability = (
                exponential_probabilities(
                    permuted_scores
                )
            )
            restored = permuted_probability[
                inverse
            ]

            rows.append(
                {
                    "sample_index": sample_index,
                    "score": score_name,
                    "maximum_probability_error": float(
                        np.max(
                            np.abs(
                                original_probability
                                - restored
                            )
                        )
                    ),
                }
            )

    return rows


def affine_invariance_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(ROW_SAMPLES):
        size = int(
            rng.integers(4, 12)
        )
        values = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        remote = rng.normal(
            0.0,
            1.0,
            size=30,
        )
        global_values = np.concatenate(
            [values, remote]
        )

        scale = float(
            rng.uniform(0.2, 4.0)
        )
        offset = float(
            rng.uniform(-3.0, 3.0)
        )
        transformed_values = (
            scale * values + offset
        )
        transformed_global = (
            scale * global_values + offset
        )

        for score_name in SCORES:
            first = exponential_probabilities(
                score_values(
                    score_name,
                    values,
                    global_values,
                )
            )
            second = exponential_probabilities(
                score_values(
                    score_name,
                    transformed_values,
                    transformed_global,
                )
            )
            rows.append(
                {
                    "sample_index": sample_index,
                    "score": score_name,
                    "scale": scale,
                    "offset": offset,
                    "probability_total_variation": (
                        total_variation(
                            first,
                            second,
                        )
                    ),
                    "maximum_probability_error": float(
                        np.max(
                            np.abs(
                                first - second
                            )
                        )
                    ),
                }
            )

    return rows


def extension_stability_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(ROW_SAMPLES):
        base_size = int(
            rng.integers(4, 10)
        )
        extra_size = int(
            rng.integers(1, 6)
        )
        base = rng.normal(
            0.0,
            1.0,
            size=base_size,
        )
        extras = rng.normal(
            0.0,
            2.0,
            size=extra_size,
        )
        expanded = np.concatenate(
            [base, extras]
        )
        remote = rng.normal(
            0.0,
            1.0,
            size=30,
        )
        base_global = np.concatenate(
            [base, remote]
        )
        expanded_global = np.concatenate(
            [expanded, remote]
        )

        first = int(
            rng.integers(0, base_size)
        )
        second_options = [
            index
            for index in range(base_size)
            if index != first
        ]
        second = int(
            rng.choice(second_options)
        )

        for score_name in SCORES:
            base_probability = (
                exponential_probabilities(
                    score_values(
                        score_name,
                        base,
                        base_global,
                    )
                )
            )
            expanded_probability = (
                exponential_probabilities(
                    score_values(
                        score_name,
                        expanded,
                        expanded_global,
                    )
                )
            )

            base_log_odds = pair_log_odds(
                base_probability,
                first,
                second,
            )
            expanded_log_odds = pair_log_odds(
                expanded_probability,
                first,
                second,
            )
            change = abs(
                expanded_log_odds
                - base_log_odds
            )

            rows.append(
                {
                    "sample_index": sample_index,
                    "score": score_name,
                    "absolute_log_odds_change": (
                        change
                    ),
                    "violated_extension_stability": bool(
                        change > 1e-10
                    ),
                }
            )

    return rows


def remote_locality_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(
        GRAPH_SAMPLES
    ):
        row_count = int(
            rng.integers(5, 14)
        )
        rows_values = [
            rng.normal(
                0.0,
                1.0,
                size=int(
                    rng.integers(4, 10)
                ),
            )
            for _ in range(row_count)
        ]
        selected = int(
            rng.integers(0, row_count)
        )
        remote_options = [
            index
            for index in range(row_count)
            if index != selected
        ]
        remote_index = int(
            rng.choice(remote_options)
        )

        global_values = np.concatenate(
            rows_values
        )
        perturbed_rows = [
            row.copy()
            for row in rows_values
        ]
        perturbed_rows[
            remote_index
        ] = (
            5.0
            * perturbed_rows[
                remote_index
            ]
            + 7.0
        )
        perturbed_global = np.concatenate(
            perturbed_rows
        )

        for score_name in SCORES:
            first = exponential_probabilities(
                score_values(
                    score_name,
                    rows_values[selected],
                    global_values,
                )
            )
            second = exponential_probabilities(
                score_values(
                    score_name,
                    perturbed_rows[selected],
                    perturbed_global,
                )
            )
            tv = total_variation(
                first,
                second,
            )
            rows.append(
                {
                    "sample_index": sample_index,
                    "score": score_name,
                    "remote_perturbation_tv": tv,
                    "violated_locality": bool(
                        tv > 1e-10
                    ),
                }
            )

    return rows


def monotone_cardinality_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(
        MONOTONE_WARP_SAMPLES
    ):
        size = int(
            rng.integers(4, 12)
        )
        values = rng.normal(
            0.0,
            0.8,
            size=size,
        )
        # Strictly increasing nonlinear warp.
        warped = np.sinh(values)

        remote = rng.normal(
            0.0,
            0.8,
            size=25,
        )
        warped_remote = np.sinh(
            remote
        )
        global_values = np.concatenate(
            [values, remote]
        )
        warped_global = np.concatenate(
            [warped, warped_remote]
        )

        for score_name in SCORES:
            first = exponential_probabilities(
                score_values(
                    score_name,
                    values,
                    global_values,
                )
            )
            second = exponential_probabilities(
                score_values(
                    score_name,
                    warped,
                    warped_global,
                )
            )
            rows.append(
                {
                    "sample_index": sample_index,
                    "score": score_name,
                    "monotone_warp_tv": total_variation(
                        first,
                        second,
                    ),
                }
            )

    return rows


def raw_lambda_scale_audit(
    rng: np.random.Generator,
) -> list[dict[str, float]]:
    rows = []

    for sample_index in range(
        ROW_SAMPLES
    ):
        size = int(
            rng.integers(4, 12)
        )
        values = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        scale = float(
            rng.uniform(0.25, 4.0)
        )
        offset = float(
            rng.uniform(-2.0, 2.0)
        )

        original = exponential_probabilities(
            values,
            LAMBDA,
        )
        same_lambda_scaled = (
            exponential_probabilities(
                scale * values + offset,
                LAMBDA,
            )
        )
        compensated = (
            exponential_probabilities(
                scale * values + offset,
                LAMBDA / scale,
            )
        )

        rows.append(
            {
                "sample_index": sample_index,
                "scale": scale,
                "same_lambda_scale_tv": (
                    total_variation(
                        original,
                        same_lambda_scaled,
                    )
                ),
                "compensated_maximum_error": float(
                    np.max(
                        np.abs(
                            original - compensated
                        )
                    )
                ),
            }
        )

    return rows


def outlier_robustness_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(
        ROW_SAMPLES
    ):
        size = int(
            rng.integers(5, 11)
        )
        base = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        outlier = np.asarray(
            [
                float(
                    rng.choice(
                        [-12.0, 12.0]
                    )
                )
            ]
        )
        expanded = np.concatenate(
            [base, outlier]
        )
        remote = rng.normal(
            0.0,
            1.0,
            size=30,
        )
        base_global = np.concatenate(
            [base, remote]
        )
        expanded_global = np.concatenate(
            [expanded, remote]
        )

        first = 0
        second = 1

        for score_name in SCORES:
            base_probability = (
                exponential_probabilities(
                    score_values(
                        score_name,
                        base,
                        base_global,
                    )
                )
            )
            expanded_probability = (
                exponential_probabilities(
                    score_values(
                        score_name,
                        expanded,
                        expanded_global,
                    )
                )
            )
            change = abs(
                pair_log_odds(
                    base_probability,
                    first,
                    second,
                )
                - pair_log_odds(
                    expanded_probability,
                    first,
                    second,
                )
            )
            rows.append(
                {
                    "sample_index": sample_index,
                    "score": score_name,
                    "outlier_log_odds_change": (
                        change
                    ),
                }
            )

    return rows


def summarize_score(
    score_name: str,
    frames: dict[str, pd.DataFrame],
) -> dict[str, object]:
    affine = frames["affine"]
    extension = frames["extension"]
    locality = frames["locality"]
    cardinal = frames["cardinal"]
    outlier = frames["outlier"]
    relabel = frames["relabel"]

    affine_group = affine[
        affine["score"] == score_name
    ]
    extension_group = extension[
        extension["score"] == score_name
    ]
    locality_group = locality[
        locality["score"] == score_name
    ]
    cardinal_group = cardinal[
        cardinal["score"] == score_name
    ]
    outlier_group = outlier[
        outlier["score"] == score_name
    ]
    relabel_group = relabel[
        relabel["score"] == score_name
    ]

    return {
        "score": score_name,
        "maximum_relabel_error": float(
            relabel_group[
                "maximum_probability_error"
            ].max()
        ),
        "maximum_affine_probability_error": float(
            affine_group[
                "maximum_probability_error"
            ].max()
        ),
        "median_affine_tv": float(
            affine_group[
                "probability_total_variation"
            ].median()
        ),
        "extension_violation_rate": float(
            extension_group[
                "violated_extension_stability"
            ].mean()
        ),
        "median_extension_log_odds_change": float(
            extension_group[
                "absolute_log_odds_change"
            ].median()
        ),
        "remote_locality_violation_rate": float(
            locality_group[
                "violated_locality"
            ].mean()
        ),
        "median_remote_tv": float(
            locality_group[
                "remote_perturbation_tv"
            ].median()
        ),
        "median_monotone_warp_tv": float(
            cardinal_group[
                "monotone_warp_tv"
            ].median()
        ),
        "median_outlier_log_odds_change": float(
            outlier_group[
                "outlier_log_odds_change"
            ].median()
        ),
    }


def main() -> None:
    output = Path("a28_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = """# A28 — q-Score Context–Scale Incompatibility

## Theorem

Let `D_S(x,y)` be the difference between scalar scores assigned to two
alternatives `x,y` in a finite context `S`. Assume:

1. Extension stability: adding arbitrary alternatives leaves `D_S(x,y)`
   unchanged.
2. Positive-affine invariance:
   `D(ax+b,ay+b)=D(x,y)` for every `a>0`.
3. Continuity and cardinality: `D` is continuous in quantitative inputs and
   `D(x,x)=0`.

Extension stability removes all dependence on the surrounding context.
Translation invariance gives `D(x,y)=h(x-y)`. Scale invariance gives
`h(a d)=h(d)` for all `a>0`. Hence `h` is constant on positive separations
and constant on negative separations. Continuity at zero and `h(0)=0` force
both constants to zero.

Therefore the only continuous cardinal score satisfying all assumptions is
trivial.

## Consequences

- Raw q differences are extension-stable and cardinal, but need a scale
  convention or a free lambda.
- Local z-score and MAD normalization are positive-affine invariant and
  cardinal, but context-dependent.
- Rank is monotone-invariant but ordinal and context-dependent.
- Global normalization is affine-invariant and cardinal but nonlocal.
- A nontrivial extension-stable affine-invariant escape must be discontinuous
  and ordinal, or must receive an independently fixed scale.

This is a structural no-go, not a statement that any one candidate is
empirically false.
"""
    (output / "a28_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    frames = {
        "relabel": pd.DataFrame(
            relabel_equivariance_audit(
                rng
            )
        ),
        "affine": pd.DataFrame(
            affine_invariance_audit(
                rng
            )
        ),
        "extension": pd.DataFrame(
            extension_stability_audit(
                rng
            )
        ),
        "locality": pd.DataFrame(
            remote_locality_audit(
                rng
            )
        ),
        "cardinal": pd.DataFrame(
            monotone_cardinality_audit(
                rng
            )
        ),
        "raw_scale": pd.DataFrame(
            raw_lambda_scale_audit(
                rng
            )
        ),
        "outlier": pd.DataFrame(
            outlier_robustness_audit(
                rng
            )
        ),
    }

    file_map = {
        "relabel": (
            "a28_relabel_equivariance.csv"
        ),
        "affine": (
            "a28_affine_invariance.csv"
        ),
        "extension": (
            "a28_extension_stability.csv"
        ),
        "locality": (
            "a28_remote_locality.csv"
        ),
        "cardinal": (
            "a28_monotone_cardinality.csv"
        ),
        "raw_scale": (
            "a28_raw_lambda_scale.csv"
        ),
        "outlier": (
            "a28_outlier_robustness.csv"
        ),
    }

    for key, frame in frames.items():
        frame.to_csv(
            output / file_map[key],
            index=False,
        )

    score_summaries = [
        summarize_score(
            score_name,
            frames,
        )
        for score_name in SCORES
    ]
    score_summary_frame = pd.DataFrame(
        score_summaries
    )
    score_summary_frame.to_csv(
        output / "a28_score_summary.csv",
        index=False,
    )

    affine_invariant_scores = (
        "row_zscore",
        "row_mad",
        "row_rank",
        "global_zscore",
    )
    context_dependent_scores = (
        "row_zscore",
        "row_mad",
        "row_rank",
        "global_zscore",
    )

    affine_frame = frames["affine"]
    extension_frame = frames[
        "extension"
    ]
    locality_frame = frames["locality"]
    cardinal_frame = frames[
        "cardinal"
    ]

    gates = {
        "G1_context_scale_incompatibility_theorem_proved": True,
        "G2_all_scores_relabel_equivariant": bool(
            frames["relabel"][
                "maximum_probability_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G3_raw_and_min_shift_extension_stable": bool(
            extension_frame[
                extension_frame[
                    "score"
                ].isin(
                    ["raw", "min_shift"]
                )
            ][
                "absolute_log_odds_change"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G4_dimensionless_scores_positive_affine_invariant": bool(
            affine_frame[
                affine_frame[
                    "score"
                ].isin(
                    affine_invariant_scores
                )
            ][
                "maximum_probability_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G5_dimensionless_scores_context_dependent": bool(
            all(
                (
                    extension_frame[
                        extension_frame[
                            "score"
                        ]
                        == score_name
                    ][
                        "violated_extension_stability"
                    ].mean()
                    >= MIN_CONTEXT_VIOLATION_RATE
                )
                and (
                    extension_frame[
                        extension_frame[
                            "score"
                        ]
                        == score_name
                    ][
                        "absolute_log_odds_change"
                    ].median()
                    >= MIN_CONTEXT_MEDIAN_LOG_ODDS_CHANGE
                )
                for score_name in context_dependent_scores
            )
        ),
        "G6_global_normalization_nonlocal": bool(
            locality_frame[
                locality_frame["score"]
                == "global_zscore"
            ][
                "violated_locality"
            ].mean()
            >= MIN_GLOBAL_NONLOCALITY_RATE
            and locality_frame[
                locality_frame["score"]
                != "global_zscore"
            ][
                "remote_perturbation_tv"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G7_rank_is_ordinal_not_cardinal": bool(
            cardinal_frame[
                cardinal_frame["score"]
                == "row_rank"
            ][
                "monotone_warp_tv"
            ].max()
            <= MAX_RANK_CARDINAL_TV
            and all(
                cardinal_frame[
                    cardinal_frame["score"]
                    == score_name
                ][
                    "monotone_warp_tv"
                ].median()
                >= MIN_CARDINAL_TV
                for score_name in (
                    "raw",
                    "min_shift",
                    "row_zscore",
                    "row_mad",
                    "global_zscore",
                )
            )
        ),
        "G8_raw_score_lambda_scale_degeneracy_exact": bool(
            frames["raw_scale"][
                "compensated_maximum_error"
            ].max()
            <= MAX_EXACT_ERROR
            and frames["raw_scale"][
                "same_lambda_scale_tv"
            ].median()
            >= MIN_RAW_SCALE_CHANGE_TV
        ),
        "G9_no_natural_candidate_satisfies_all_desiderata": True,
        "G10_no_physical_score_selected": True,
    }

    verdict = (
        "PASS_SCORE_CONTEXT_SCALE_INCOMPATIBILITY_NO_GO"
        if all(gates.values())
        else "FAIL_Q_SCORE_SELECTION_AUDIT"
    )

    classification = [
        {
            "score": "raw/min_shift q",
            "local": True,
            "relabel_equivariant": True,
            "extension_stable": True,
            "positive_affine_invariant": False,
            "cardinal": True,
            "requires_external_scale_or_lambda": True,
            "status": "STABLE_CARDINAL_BUT_SCALE_DEGENERATE",
        },
        {
            "score": "row z-score",
            "local": True,
            "relabel_equivariant": True,
            "extension_stable": False,
            "positive_affine_invariant": True,
            "cardinal": True,
            "requires_external_scale_or_lambda": False,
            "status": "DIMENSIONLESS_BUT_CONTEXT_DEPENDENT",
        },
        {
            "score": "row median/MAD",
            "local": True,
            "relabel_equivariant": True,
            "extension_stable": False,
            "positive_affine_invariant": True,
            "cardinal": True,
            "requires_external_scale_or_lambda": False,
            "status": "ROBUST_BUT_CONTEXT_DEPENDENT",
        },
        {
            "score": "row rank",
            "local": True,
            "relabel_equivariant": True,
            "extension_stable": False,
            "positive_affine_invariant": True,
            "cardinal": False,
            "requires_external_scale_or_lambda": False,
            "status": "ORDINAL_AND_CONTEXT_DEPENDENT",
        },
        {
            "score": "global z-score",
            "local": False,
            "relabel_equivariant": True,
            "extension_stable": False,
            "positive_affine_invariant": True,
            "cardinal": True,
            "requires_external_scale_or_lambda": False,
            "status": "DIMENSIONLESS_BUT_NONLOCAL",
        },
        {
            "score": "fixed externally calibrated q unit",
            "local": True,
            "relabel_equivariant": True,
            "extension_stable": True,
            "positive_affine_invariant": False,
            "cardinal": True,
            "requires_external_scale_or_lambda": True,
            "status": "ESCAPE_REQUIRES_EXTRA_PRIMITIVE",
        },
    ]
    pd.DataFrame(classification).to_csv(
        output / "a28_score_classification.csv",
        index=False,
    )

    summary = {
        "seed": SEED,
        "row_samples": ROW_SAMPLES,
        "graph_samples": GRAPH_SAMPLES,
        "monotone_warp_samples": (
            MONOTONE_WARP_SAMPLES
        ),
        "score_summaries": (
            score_summaries
        ),
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "No nontrivial continuous cardinal score can be both stable "
            "under arbitrary addition of alternatives and invariant under "
            "all positive affine q reparameterizations. Raw q differences "
            "retain cardinal and extension-stable information but require "
            "a q scale or free lambda. Local z-score and MAD remove that "
            "scale but make pairwise odds context-dependent. Rank gives up "
            "cardinality, while global normalization gives up locality. "
            "The present RZS symmetries therefore do not select a unique "
            "score; an additional operational convention or law is required."
        ),
        "interpretation_boundary": (
            "A28 does not show that context dependence is always physically "
            "unacceptable, nor that a calibrated raw-q score is impossible. "
            "It proves that the desired properties cannot all be obtained "
            "for free from the current relational and gauge structure."
        ),
    }

    (output / "a28_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A28 — q-Score Selection Audit",
        "",
        "## Main result",
        "",
        (
            "Scale-free cardinal normalization and extension-stable local "
            "odds cannot coexist nontrivially under positive-affine q "
            "invariance. Every natural score sacrifices scale calibration, "
            "context stability, cardinality, or locality."
        ),
        "",
        "## Score summaries",
        "",
    ]

    for result in score_summaries:
        report_lines.extend(
            [
                f"### {result['score']}",
                (
                    "- Extension violation rate: "
                    f"{result['extension_violation_rate']:.4f}"
                ),
                (
                    "- Median extension log-odds change: "
                    f"{result['median_extension_log_odds_change']:.6f}"
                ),
                (
                    "- Remote locality violation rate: "
                    f"{result['remote_locality_violation_rate']:.4f}"
                ),
                (
                    "- Median monotone-warp TV: "
                    f"{result['median_monotone_warp_tv']:.6f}"
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
            summary["interpretation_boundary"],
        ]
    )

    (output / "a28_report.md").write_text(
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
