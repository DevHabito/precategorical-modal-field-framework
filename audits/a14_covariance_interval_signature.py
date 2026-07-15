#!/usr/bin/env python3
"""
A14 — Covariance-Aware Analytic Interval Signature

Classifier-free goodness-of-fit audit for 2D Minkowski interval abundances.

For each n:
1. The analytic fixed-n expectation from A13 defines the mean profile.
2. A Minkowski-only estimation sample defines the covariance matrix.
3. A separate Minkowski-only calibration sample defines empirical p-values.
4. Independent holdout sprinklings and matched null families are tested.

The statistic is

    Q = (p - mu)^T Sigma_reg^{-1} (p - mu),

where p is a binned normalized interval-abundance profile, mu is the exact
analytic profile, and Sigma_reg is a Ledoit–Wolf covariance estimate obtained
only from Minkowski sprinklings.

Prospective sizes:
    n = 96, 128, 160

Nulls:
    - matched transitive percolation;
    - matched random three-layer posets;
    - adversarial matched transitive percolation selected to minimize the
      L1 error in bins N_0,...,N_5.

No null sample is used to choose bins, weights, covariance, or thresholds.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.covariance import LedoitWolf

from a13_analytic_interval_signature import (
    analytic_expectation,
    delete_cover_fraction,
    empirical_p_value,
    hellinger_squared,
    interval_abundance,
    matched_three_layer_poset,
    matched_transitive_percolation,
    relation_fraction,
    sample_minkowski_2d,
    wilson_interval,
)


SEED = 20260714
N_VALUES = (96, 128, 160)

COVARIANCE_ESTIMATION_SAMPLES = 300
CALIBRATION_SAMPLES = 250
HOLDOUT_MINKOWSKI = 80
NULL_SAMPLES = 60

ADVERSARIAL_POOL = 220
ADVERSARIAL_SELECTED = 50
ADVERSARIAL_LOW_BINS = 6

PERTURBATION_SAMPLES = 50
PERTURBATION_LEVELS = (0.0, 0.10, 0.20, 0.30)

EXPECTED_COUNT_BIN_THRESHOLD = 10.0
ALPHA = 0.05
MAX_MATCH_MISMATCH = 0.02


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


def make_bins(
    expected_counts: np.ndarray,
) -> list[tuple[int, int]]:
    """
    Keep every m with E[N_m] >= threshold as an individual bin and pool the
    remaining analytic tail. Binning therefore depends only on the exact
    theoretical expectation, not on observed or null data.
    """
    retained = np.flatnonzero(
        expected_counts >= EXPECTED_COUNT_BIN_THRESHOLD
    )
    if len(retained) == 0:
        return [(0, len(expected_counts))]

    last_individual = int(retained[-1])
    bins = [
        (index, index + 1)
        for index in range(last_individual + 1)
    ]
    if last_individual + 1 < len(expected_counts):
        bins.append(
            (last_individual + 1, len(expected_counts))
        )
    return bins


def bin_vector(
    values: np.ndarray,
    bins: list[tuple[int, int]],
) -> np.ndarray:
    return np.asarray(
        [
            float(values[start:end].sum())
            for start, end in bins
        ],
        dtype=float,
    )


def normalized_profile(
    relation: np.ndarray,
    bins: list[tuple[int, int]],
) -> np.ndarray:
    counts = interval_abundance(relation)
    total = counts.sum()
    if total <= 0:
        raise RuntimeError(
            "A tested relation has no comparable pairs."
        )
    return bin_vector(counts, bins) / total


def quadratic_score(
    profile: np.ndarray,
    analytic_profile: np.ndarray,
    precision: np.ndarray,
) -> float:
    difference = profile - analytic_profile
    return float(
        difference @ precision @ difference
    )


def acceptance_rate(
    rows: list[dict[str, object]],
) -> float:
    return float(
        np.mean(
            [
                bool(row["compatible_at_alpha"])
                for row in rows
            ]
        )
    )


def rejection_rate(
    rows: list[dict[str, object]],
) -> float:
    return 1.0 - acceptance_rate(rows)


def append_row(
    rows: list[dict[str, object]],
    *,
    n: int,
    family: str,
    sample_index: int,
    relation: np.ndarray,
    bins: list[tuple[int, int]],
    analytic_binned_profile: np.ndarray,
    precision: np.ndarray,
    calibration_scores: np.ndarray,
    analytic_full_profile: np.ndarray,
    target_fraction: float | None = None,
    perturbation_fraction: float = 0.0,
) -> dict[str, object]:
    profile = normalized_profile(relation, bins)
    q_score = quadratic_score(
        profile,
        analytic_binned_profile,
        precision,
    )
    p_value = empirical_p_value(
        q_score,
        calibration_scores,
    )

    counts = interval_abundance(relation)
    full_profile = counts / counts.sum()
    h2_score = hellinger_squared(
        counts,
        analytic_full_profile,
    )

    actual_fraction = relation_fraction(relation)
    row: dict[str, object] = {
        "n": n,
        "family": family,
        "sample_index": sample_index,
        "q_score": q_score,
        "p_value": p_value,
        "compatible_at_alpha": p_value >= ALPHA,
        "hellinger_squared": h2_score,
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
    }

    for index in range(ADVERSARIAL_LOW_BINS):
        row[f"profile_m{index}"] = float(
            full_profile[index]
        )

    rows.append(row)
    return row


def main() -> None:
    output = Path("a14_exact_results")
    output.mkdir(exist_ok=True)

    rng = np.random.default_rng(SEED)

    sample_rows: list[dict[str, object]] = []
    covariance_rows: list[dict[str, object]] = []
    perturbation_rows: list[dict[str, object]] = []
    size_results: list[dict[str, object]] = []

    all_covariance_pass = True
    all_holdout_pass = True
    all_tp_pass = True
    all_layer_pass = True
    all_adversarial_pass = True
    all_adversarial_strength_pass = True
    all_perturbation_pass = True

    for n in N_VALUES:
        expected_counts, analytic_full_profile = (
            analytic_expectation(n)
        )
        bins = make_bins(expected_counts)
        analytic_binned_profile = bin_vector(
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
                    COVARIANCE_ESTIMATION_SAMPLES
                )
            ]
        )

        covariance_model = LedoitWolf(
            assume_centered=False,
        ).fit(estimation_profiles)
        covariance = covariance_model.covariance_
        precision = covariance_model.precision_
        condition_number = float(
            np.linalg.cond(covariance)
        )
        minimum_eigenvalue = float(
            np.linalg.eigvalsh(covariance).min()
        )
        covariance_pass = (
            np.isfinite(condition_number)
            and condition_number <= 1e8
            and minimum_eigenvalue > 0.0
        )
        all_covariance_pass &= covariance_pass

        for row_index in range(len(bins)):
            for column_index in range(len(bins)):
                covariance_rows.append(
                    {
                        "n": n,
                        "row": row_index,
                        "column": column_index,
                        "covariance": float(
                            covariance[
                                row_index,
                                column_index,
                            ]
                        ),
                        "precision": float(
                            precision[
                                row_index,
                                column_index,
                            ]
                        ),
                    }
                )

        calibration_profiles = np.vstack(
            [
                normalized_profile(
                    sample_minkowski_2d(n, rng),
                    bins,
                )
                for _ in range(CALIBRATION_SAMPLES)
            ]
        )
        calibration_scores = np.asarray(
            [
                quadratic_score(
                    profile,
                    analytic_binned_profile,
                    precision,
                )
                for profile in calibration_profiles
            ],
            dtype=float,
        )

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
                append_row(
                    sample_rows,
                    n=n,
                    family="minkowski_holdout",
                    sample_index=sample_index,
                    relation=relation,
                    bins=bins,
                    analytic_binned_profile=(
                        analytic_binned_profile
                    ),
                    precision=precision,
                    calibration_scores=calibration_scores,
                    analytic_full_profile=(
                        analytic_full_profile
                    ),
                )
            )

        tp_rows = []
        layer_rows = []

        for sample_index in range(NULL_SAMPLES):
            target = target_fractions[
                sample_index % len(target_fractions)
            ]

            relation, _ = matched_transitive_percolation(
                n,
                target,
                rng,
            )
            tp_rows.append(
                append_row(
                    sample_rows,
                    n=n,
                    family="transitive_percolation",
                    sample_index=sample_index,
                    relation=relation,
                    bins=bins,
                    analytic_binned_profile=(
                        analytic_binned_profile
                    ),
                    precision=precision,
                    calibration_scores=calibration_scores,
                    analytic_full_profile=(
                        analytic_full_profile
                    ),
                    target_fraction=target,
                )
            )

            relation, _ = matched_three_layer_poset(
                n,
                target,
                rng,
            )
            layer_rows.append(
                append_row(
                    sample_rows,
                    n=n,
                    family="three_layer",
                    sample_index=sample_index,
                    relation=relation,
                    bins=bins,
                    analytic_binned_profile=(
                        analytic_binned_profile
                    ),
                    precision=precision,
                    calibration_scores=calibration_scores,
                    analytic_full_profile=(
                        analytic_full_profile
                    ),
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
            counts = interval_abundance(relation)
            profile = counts / counts.sum()
            low_six_error = float(
                np.abs(
                    profile[:ADVERSARIAL_LOW_BINS]
                    - analytic_full_profile[
                        :ADVERSARIAL_LOW_BINS
                    ]
                ).sum()
            )
            adversarial_candidates.append(
                {
                    "relation": relation,
                    "target": target,
                    "low_six_error": low_six_error,
                }
            )

        adversarial_candidates.sort(
            key=lambda item: item["low_six_error"]
        )
        selected_adversarial = adversarial_candidates[
            :ADVERSARIAL_SELECTED
        ]

        adversarial_rows = []
        for sample_index, item in enumerate(
            selected_adversarial
        ):
            adversarial_rows.append(
                append_row(
                    sample_rows,
                    n=n,
                    family=(
                        "adversarial_transitive_percolation"
                    ),
                    sample_index=sample_index,
                    relation=item["relation"],
                    bins=bins,
                    analytic_binned_profile=(
                        analytic_binned_profile
                    ),
                    precision=precision,
                    calibration_scores=calibration_scores,
                    analytic_full_profile=(
                        analytic_full_profile
                    ),
                    target_fraction=float(item["target"]),
                )
            )

        ordinary_low_six = [
            sum(
                abs(
                    float(row[f"profile_m{index}"])
                    - analytic_full_profile[index]
                )
                for index in range(
                    ADVERSARIAL_LOW_BINS
                )
            )
            for row in tp_rows
        ]
        adversarial_low_six = [
            float(item["low_six_error"])
            for item in selected_adversarial
        ]

        ordinary_low_six_median = float(
            np.median(ordinary_low_six)
        )
        adversarial_low_six_median = float(
            np.median(adversarial_low_six)
        )
        low_six_reduction = (
            1.0
            - adversarial_low_six_median
            / ordinary_low_six_median
        )

        perturbation_by_level: dict[
            float,
            list[dict[str, object]],
        ] = {
            level: []
            for level in PERTURBATION_LEVELS
        }
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
                row = append_row(
                    perturbation_rows,
                    n=n,
                    family="cover_deletion",
                    sample_index=sample_index,
                    relation=relation,
                    bins=bins,
                    analytic_binned_profile=(
                        analytic_binned_profile
                    ),
                    precision=precision,
                    calibration_scores=calibration_scores,
                    analytic_full_profile=(
                        analytic_full_profile
                    ),
                    perturbation_fraction=level,
                )
                perturbation_by_level[level].append(row)

        holdout_acceptance = acceptance_rate(holdout_rows)
        tp_rejection = rejection_rate(tp_rows)
        layer_rejection = rejection_rate(layer_rows)
        adversarial_rejection = rejection_rate(
            adversarial_rows
        )

        maximum_mismatch = max(
            max(
                float(row["ordering_fraction_mismatch"])
                for row in tp_rows
            ),
            max(
                float(row["ordering_fraction_mismatch"])
                for row in layer_rows
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
                        float(row["q_score"])
                        for row in perturbation_by_level[
                            level
                        ]
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
        median_sequence = [
            perturbation_medians[str(level)]
            for level in PERTURBATION_LEVELS
        ]
        perturbation_monotonic = all(
            later >= earlier
            for earlier, later in zip(
                median_sequence,
                median_sequence[1:],
            )
        )
        perturbation_pass = (
            perturbation_monotonic
            and perturbation_rejections[str(0.20)]
            >= 0.80
            and perturbation_rejections[str(0.30)]
            >= 0.95
        )

        holdout_pass = holdout_acceptance >= 0.90
        tp_pass = tp_rejection >= 0.90
        layer_pass = layer_rejection >= 0.90
        adversarial_pass = adversarial_rejection >= 0.80
        adversarial_strength_pass = (
            low_six_reduction >= 0.10
            and maximum_mismatch <= MAX_MATCH_MISMATCH
        )

        all_holdout_pass &= holdout_pass
        all_tp_pass &= tp_pass
        all_layer_pass &= layer_pass
        all_adversarial_pass &= adversarial_pass
        all_adversarial_strength_pass &= (
            adversarial_strength_pass
        )
        all_perturbation_pass &= perturbation_pass

        size_results.append(
            {
                "n": n,
                "number_bins": len(bins),
                "bins": bins,
                "ledoit_wolf_shrinkage": float(
                    covariance_model.shrinkage_
                ),
                "covariance_condition_number": (
                    condition_number
                ),
                "covariance_minimum_eigenvalue": (
                    minimum_eigenvalue
                ),
                "covariance_gate_pass": covariance_pass,
                "calibration_score_median": float(
                    np.median(calibration_scores)
                ),
                "calibration_score_95_quantile": float(
                    np.quantile(calibration_scores, 0.95)
                ),
                "minkowski_holdout_acceptance_rate": (
                    holdout_acceptance
                ),
                "minkowski_holdout_wilson_95": (
                    wilson_interval(
                        int(
                            round(
                                holdout_acceptance
                                * len(holdout_rows)
                            )
                        ),
                        len(holdout_rows),
                    )
                ),
                "transitive_percolation_rejection_rate": (
                    tp_rejection
                ),
                "transitive_percolation_wilson_95": (
                    wilson_interval(
                        int(
                            round(
                                tp_rejection
                                * len(tp_rows)
                            )
                        ),
                        len(tp_rows),
                    )
                ),
                "three_layer_rejection_rate": (
                    layer_rejection
                ),
                "adversarial_rejection_rate": (
                    adversarial_rejection
                ),
                "ordinary_low_six_error_median": (
                    ordinary_low_six_median
                ),
                "adversarial_low_six_error_median": (
                    adversarial_low_six_median
                ),
                "adversarial_low_six_error_reduction": (
                    low_six_reduction
                ),
                "maximum_ordering_fraction_mismatch": (
                    maximum_mismatch
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
                "perturbation_gate_pass": (
                    perturbation_pass
                ),
            }
        )

    pd.DataFrame(sample_rows).to_csv(
        output / "a14_sample_scores.csv",
        index=False,
    )
    pd.DataFrame(covariance_rows).to_csv(
        output / "a14_covariance_matrices.csv",
        index=False,
    )
    pd.DataFrame(perturbation_rows).to_csv(
        output / "a14_perturbation_scores.csv",
        index=False,
    )
    pd.DataFrame(size_results).to_csv(
        output / "a14_size_summary.csv",
        index=False,
    )

    gates = {
        "G1_covariance_positive_and_conditioned": (
            all_covariance_pass
        ),
        "G2_minkowski_holdout_acceptance_ge_0_90": (
            all_holdout_pass
        ),
        "G3_transitive_percolation_rejection_ge_0_90": (
            all_tp_pass
        ),
        "G4_three_layer_rejection_ge_0_90": (
            all_layer_pass
        ),
        "G5_adversarial_rejection_ge_0_80": (
            all_adversarial_pass
        ),
        "G6_adversarial_low_six_matching_and_density": (
            all_adversarial_strength_pass
        ),
        "G7_perturbation_response": (
            all_perturbation_pass
        ),
        "G8_no_null_used_for_weights_or_thresholds": True,
        "G9_no_trained_discriminative_classifier": True,
    }

    verdict = (
        "PASS_COVARIANCE_AWARE_INTERVAL_SIGNATURE"
        if all(gates.values())
        else "FAIL_COVARIANCE_AWARE_INTERVAL_SIGNATURE"
    )

    summary = {
        "seed": SEED,
        "n_values": list(N_VALUES),
        "covariance_estimation_samples_per_n": (
            COVARIANCE_ESTIMATION_SAMPLES
        ),
        "calibration_samples_per_n": (
            CALIBRATION_SAMPLES
        ),
        "holdout_minkowski_per_n": (
            HOLDOUT_MINKOWSKI
        ),
        "null_samples_per_family_per_n": NULL_SAMPLES,
        "adversarial_pool_per_n": ADVERSARIAL_POOL,
        "adversarial_selected_per_n": (
            ADVERSARIAL_SELECTED
        ),
        "adversarial_bins": list(
            range(ADVERSARIAL_LOW_BINS)
        ),
        "statistic": (
            "Q=(p-mu)^T Sigma_reg^{-1}(p-mu), with exact "
            "analytic mu and Ledoit-Wolf Sigma_reg estimated only "
            "from Minkowski sprinklings"
        ),
        "binning_rule": (
            "individual m bins while analytic E[N_m] >= 10, "
            "then one pooled tail bin"
        ),
        "size_results": size_results,
        "gates": gates,
        "verdict": verdict,
        "interpretation_boundary": (
            "A pass establishes finite-size goodness-of-fit "
            "rejection of the specified matched nulls using "
            "Minkowski-only covariance information. It does not "
            "prove sufficient manifoldlikeness or derive physical "
            "spacetime."
        ),
    }

    (output / "a14_summary.json").write_text(
        json.dumps(json_safe(summary), indent=2),
        encoding="utf-8",
    )

    report = [
        "# A14 — Covariance-Aware Analytic Interval Signature",
        "",
        "## Design",
        "",
        "- No trained discriminative classifier.",
        "- Exact A13 analytic mean profile.",
        "- Minkowski-only Ledoit–Wolf covariance.",
        "- Independent Minkowski calibration and holdout samples.",
        "- Fresh matched ordinary and adversarial nulls.",
        "",
        "## Results by size",
        "",
    ]

    for result in size_results:
        report.extend(
            [
                f"### n = {result['n']}",
                "",
                (
                    "- Binned dimension: "
                    f"{result['number_bins']}"
                ),
                (
                    "- Minkowski acceptance: "
                    f"{result['minkowski_holdout_acceptance_rate']:.4f}"
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
                    "- Adversarial low-six error reduction: "
                    f"{result['adversarial_low_six_error_reduction']:.4f}"
                ),
                (
                    "- Maximum ordering-fraction mismatch: "
                    f"{result['maximum_ordering_fraction_mismatch']:.6f}"
                ),
                (
                    "- Perturbation rejection rates: "
                    f"{result['perturbation_rejection_rates']}"
                ),
                "",
            ]
        )

    report.extend(
        [
            "## Gates",
            "",
            *[
                f"- {key}: {'PASS' if value else 'FAIL'}"
                for key, value in gates.items()
            ],
            "",
            "## Verdict",
            "",
            verdict,
            "",
            "## Boundary",
            "",
            (
                "The result is a model-checking statement against "
                "specified finite nulls. It is not a proof that the "
                "accepted structures possess a physical Lorentzian "
                "continuum."
            ),
        ]
    )

    (output / "a14_report.md").write_text(
        "\n".join(report),
        encoding="utf-8",
    )

    print(json.dumps(json_safe(summary), indent=2))
    print()
    print(f"Results written to: {output.resolve()}")


if __name__ == "__main__":
    main()
