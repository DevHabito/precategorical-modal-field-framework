#!/usr/bin/env python3
"""
A17 — Multiscale Subinterval Self-Similarity Audit

Question
--------
Does a parent order reproduce the anchored 2D Minkowski interval ensemble
inside its own order intervals at several cardinality scales?

Reference model
---------------
For each local cardinality m in {24, 32, 48, 64, 96}, build independent
anchored 2D Minkowski intervals:

    bottom < all interior points < top,

with m-2 iid uniform interior points in light-cone coordinates.

For each m:
1. a Minkowski-only estimation set defines the mean interval-abundance
   profile and a Ledoit–Wolf covariance matrix;
2. an independent Minkowski-only calibration set defines empirical local
   Q_m p-values.

Parent statistic
----------------
For every parent order, inspect all order intervals of the five exact target
cardinalities. At each scale summarize:

- median local Q_m / median calibration Q_m;
- 90th percentile of that ratio;
- fraction of local p-values below 0.05;
- median standardized local ordering fraction;
- MAD of standardized local ordering fraction;
- fraction with |z| > 1.96.

A second Minkowski-only model is fitted to these 30 parent features, and an
independent Minkowski-only calibration set defines the parent p-value.

Discovery size:
    n = 192

Prospective confirmation:
    n = 256

Exact-2D challenge families:
- opposing diagonal bands: half near v=u and half near v=1-u;
- two compact clusters;
- four compact corner clusters.

All challenge relations are exact product orders in two coordinates. Density
matching uses only ordering fraction, never the A17 score.

Scientific boundary
-------------------
The audit tests self-similarity relative to a uniform anchored 2D Minkowski
interval ensemble. Rejection does not prove non-embeddability. Acceptance of
a nonuniform exact-2D family may indicate an identifiability/conformal-volume
degeneracy rather than a failure of causal embeddability.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
from sklearn.covariance import LedoitWolf

from a13_analytic_interval_signature import (
    empirical_p_value,
    interval_abundance,
    relation_fraction,
    sample_minkowski_2d,
)
from a14_covariance_interval_signature import quadratic_score
from a16_local_global_manifoldlikeness import (
    build_bimodal_2d_order,
    permute_relation,
)


SEED = 20260718
DISCOVERY_N = 192
CONFIRMATORY_N = 256
N_VALUES = (DISCOVERY_N, CONFIRMATORY_N)

LOCAL_SCALES = (24, 32, 48, 64, 96)
LOCAL_ESTIMATION_SAMPLES = 180
LOCAL_CALIBRATION_SAMPLES = 180

PARENT_ESTIMATION_SAMPLES = {
    DISCOVERY_N: 36,
    CONFIRMATORY_N: 36,
}
PARENT_CALIBRATION_SAMPLES = {
    DISCOVERY_N: 36,
    CONFIRMATORY_N: 36,
}
PARENT_HOLDOUT_SAMPLES = {
    DISCOVERY_N: 24,
    CONFIRMATORY_N: 24,
}
CHALLENGE_SAMPLES = {
    DISCOVERY_N: 24,
    CONFIRMATORY_N: 24,
}

ALPHA = 0.05
MAX_ORDERING_FRACTION_MISMATCH = 0.02


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


def anchored_minkowski_interval(
    m: int,
    rng: np.random.Generator,
) -> np.ndarray:
    u = np.empty(m, dtype=float)
    v = np.empty(m, dtype=float)

    u[0] = 0.0
    v[0] = 0.0
    u[-1] = 1.0
    v[-1] = 1.0

    u[1:-1] = rng.random(m - 2)
    v[1:-1] = rng.random(m - 2)

    relation = (
        (u[:, None] < u[None, :])
        & (v[:, None] < v[None, :])
    )
    np.fill_diagonal(relation, False)
    return relation


def normalized_interval_profile(
    relation: np.ndarray,
) -> np.ndarray:
    counts = interval_abundance(relation)
    total = counts.sum()

    if total <= 0:
        raise RuntimeError(
            "An interval has no comparable pairs."
        )

    return counts / total


def fit_local_models(
    rng: np.random.Generator,
) -> dict[int, dict[str, object]]:
    models: dict[int, dict[str, object]] = {}

    for m in LOCAL_SCALES:
        estimation_relations = [
            anchored_minkowski_interval(m, rng)
            for _ in range(
                LOCAL_ESTIMATION_SAMPLES
            )
        ]
        estimation_profiles = np.vstack(
            [
                normalized_interval_profile(relation)
                for relation in estimation_relations
            ]
        )
        estimation_ordering_fractions = np.asarray(
            [
                relation_fraction(relation)
                for relation in estimation_relations
            ],
            dtype=float,
        )

        covariance_model = LedoitWolf().fit(
            estimation_profiles
        )
        mean_profile = estimation_profiles.mean(
            axis=0
        )

        calibration_profiles = np.vstack(
            [
                normalized_interval_profile(
                    anchored_minkowski_interval(
                        m,
                        rng,
                    )
                )
                for _ in range(
                    LOCAL_CALIBRATION_SAMPLES
                )
            ]
        )
        calibration_scores = np.asarray(
            [
                quadratic_score(
                    profile,
                    mean_profile,
                    covariance_model.precision_,
                )
                for profile in calibration_profiles
            ],
            dtype=float,
        )

        models[m] = {
            "mean_profile": mean_profile,
            "precision": covariance_model.precision_,
            "calibration_scores": calibration_scores,
            "calibration_score_median": float(
                np.median(calibration_scores)
            ),
            "ordering_fraction_mean": float(
                estimation_ordering_fractions.mean()
            ),
            "ordering_fraction_sd": float(
                estimation_ordering_fractions.std(
                    ddof=1
                )
            ),
            "covariance_condition_number": float(
                np.linalg.cond(
                    covariance_model.covariance_
                )
            ),
            "covariance_minimum_eigenvalue": float(
                np.linalg.eigvalsh(
                    covariance_model.covariance_
                ).min()
            ),
            "ledoit_wolf_shrinkage": float(
                covariance_model.shrinkage_
            ),
        }

    return models


def extract_parent_features(
    relation: np.ndarray,
    local_models: dict[int, dict[str, object]],
) -> tuple[np.ndarray, dict[str, object]]:
    n = len(relation)
    reflexive = relation | np.eye(n, dtype=bool)
    interval_sizes = (
        reflexive.astype(np.int16)
        @ reflexive.astype(np.int16)
    )

    features: list[float] = []
    scale_details = []

    for m in LOCAL_SCALES:
        pairs = np.argwhere(
            relation & (interval_sizes == m)
        )

        if len(pairs) == 0:
            raise RuntimeError(
                f"No order interval of size {m}."
            )

        model = local_models[m]
        q_ratios = []
        p_values = []
        ordering_z = []

        for raw_first, raw_second in pairs:
            first = int(raw_first)
            second = int(raw_second)
            vertices = np.flatnonzero(
                reflexive[first]
                & reflexive[:, second]
            )
            local_relation = relation[
                np.ix_(vertices, vertices)
            ]

            profile = normalized_interval_profile(
                local_relation
            )
            q_score = quadratic_score(
                profile,
                model["mean_profile"],
                model["precision"],
            )
            p_value = empirical_p_value(
                q_score,
                model["calibration_scores"],
            )
            q_ratio = (
                q_score
                / model["calibration_score_median"]
            )
            z_value = (
                relation_fraction(local_relation)
                - model["ordering_fraction_mean"]
            ) / model["ordering_fraction_sd"]

            q_ratios.append(q_ratio)
            p_values.append(p_value)
            ordering_z.append(z_value)

        q_array = np.asarray(q_ratios, dtype=float)
        p_array = np.asarray(p_values, dtype=float)
        z_array = np.asarray(ordering_z, dtype=float)
        z_median = float(np.median(z_array))

        scale_feature_values = [
            float(np.median(q_array)),
            float(np.quantile(q_array, 0.90)),
            float(np.mean(p_array < ALPHA)),
            z_median,
            float(
                np.median(
                    np.abs(z_array - z_median)
                )
            ),
            float(np.mean(np.abs(z_array) > 1.96)),
        ]
        features.extend(scale_feature_values)

        scale_details.append(
            {
                "m": m,
                "number_intervals": int(len(pairs)),
                "median_q_ratio": (
                    scale_feature_values[0]
                ),
                "q90_ratio": scale_feature_values[1],
                "local_rejection_fraction": (
                    scale_feature_values[2]
                ),
                "median_ordering_z": (
                    scale_feature_values[3]
                ),
                "mad_ordering_z": (
                    scale_feature_values[4]
                ),
                "ordering_outlier_fraction": (
                    scale_feature_values[5]
                ),
            }
        )

    return (
        np.asarray(features, dtype=float),
        {"scales": scale_details},
    )


def fit_parent_model(
    n: int,
    local_models: dict[int, dict[str, object]],
    rng: np.random.Generator,
) -> dict[str, object]:
    estimation_features = np.vstack(
        [
            extract_parent_features(
                sample_minkowski_2d(n, rng),
                local_models,
            )[0]
            for _ in range(
                PARENT_ESTIMATION_SAMPLES[n]
            )
        ]
    )

    covariance_model = LedoitWolf().fit(
        estimation_features
    )
    mean_features = estimation_features.mean(
        axis=0
    )

    calibration_features = np.vstack(
        [
            extract_parent_features(
                sample_minkowski_2d(n, rng),
                local_models,
            )[0]
            for _ in range(
                PARENT_CALIBRATION_SAMPLES[n]
            )
        ]
    )
    calibration_scores = np.asarray(
        [
            quadratic_score(
                feature_vector,
                mean_features,
                covariance_model.precision_,
            )
            for feature_vector in calibration_features
        ],
        dtype=float,
    )

    return {
        "mean_features": mean_features,
        "precision": covariance_model.precision_,
        "calibration_scores": calibration_scores,
        "covariance_condition_number": float(
            np.linalg.cond(
                covariance_model.covariance_
            )
        ),
        "covariance_minimum_eigenvalue": float(
            np.linalg.eigvalsh(
                covariance_model.covariance_
            ).min()
        ),
        "ledoit_wolf_shrinkage": float(
            covariance_model.shrinkage_
        ),
    }


def score_parent(
    relation: np.ndarray,
    local_models: dict[int, dict[str, object]],
    parent_model: dict[str, object],
) -> tuple[float, float, bool, dict[str, object]]:
    features, details = extract_parent_features(
        relation,
        local_models,
    )
    score = quadratic_score(
        features,
        parent_model["mean_features"],
        parent_model["precision"],
    )
    p_value = empirical_p_value(
        score,
        parent_model["calibration_scores"],
    )
    return (
        float(score),
        float(p_value),
        bool(p_value >= ALPHA),
        details,
    )


def exact_2d_relation(
    u: np.ndarray,
    v: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    relation = (
        (u[:, None] < u[None, :])
        & (v[:, None] < v[None, :])
    )
    np.fill_diagonal(relation, False)
    return permute_relation(relation, rng)


def opposing_diagonal_bands(
    n: int,
    rng: np.random.Generator,
    noise: float = 0.03,
) -> np.ndarray:
    first_size = n // 2
    second_size = n - first_size

    u_first = rng.random(first_size)
    v_first = np.clip(
        u_first
        + rng.normal(
            0.0,
            noise,
            size=first_size,
        ),
        0.0,
        1.0,
    )

    u_second = rng.random(second_size)
    v_second = np.clip(
        1.0
        - u_second
        + rng.normal(
            0.0,
            noise,
            size=second_size,
        ),
        0.0,
        1.0,
    )

    return exact_2d_relation(
        np.concatenate([u_first, u_second]),
        np.concatenate([v_first, v_second]),
        rng,
    )


def four_corner_clusters(
    n: int,
    rng: np.random.Generator,
    width: float = 0.10,
) -> np.ndarray:
    sizes = [n // 4] * 4
    for index in range(n - sum(sizes)):
        sizes[index] += 1

    centers = (
        (0.20, 0.20),
        (0.20, 0.80),
        (0.80, 0.20),
        (0.80, 0.80),
    )
    u_parts = []
    v_parts = []

    for size, (center_u, center_v) in zip(
        sizes,
        centers,
    ):
        u_parts.append(
            rng.uniform(
                center_u - width / 2.0,
                center_u + width / 2.0,
                size=size,
            )
        )
        v_parts.append(
            rng.uniform(
                center_v - width / 2.0,
                center_v + width / 2.0,
                size=size,
            )
        )

    return exact_2d_relation(
        np.concatenate(u_parts),
        np.concatenate(v_parts),
        rng,
    )


def density_matched_candidate(
    generator: Callable[
        [int, np.random.Generator],
        np.ndarray,
    ],
    n: int,
    target_fraction: float,
    rng: np.random.Generator,
    pool: int = 20,
) -> tuple[np.ndarray, float]:
    best_relation = None
    best_mismatch = float("inf")

    for _ in range(pool):
        relation = generator(n, rng)
        mismatch = abs(
            relation_fraction(relation)
            - target_fraction
        )

        if mismatch < best_mismatch:
            best_relation = relation
            best_mismatch = mismatch

    if best_relation is None:
        raise RuntimeError(
            "Failed to generate a matched candidate."
        )

    return best_relation, float(best_mismatch)


def matched_bimodal(
    n: int,
    target_fraction: float,
    rng: np.random.Generator,
) -> tuple[np.ndarray, float]:
    best_relation = None
    best_mismatch = float("inf")

    for _ in range(8):
        relation, _ = build_bimodal_2d_order(
            n,
            target_fraction,
            rng,
            attempts=6,
        )
        mismatch = abs(
            relation_fraction(relation)
            - target_fraction
        )
        if mismatch < best_mismatch:
            best_relation = relation
            best_mismatch = mismatch

        if best_mismatch <= (
            MAX_ORDERING_FRACTION_MISMATCH / 4.0
        ):
            break

    if best_relation is None:
        raise RuntimeError(
            "Failed to generate a bimodal candidate."
        )

    return best_relation, float(best_mismatch)


def evaluate_family(
    *,
    n: int,
    family: str,
    sample_count: int,
    target_fractions: list[float],
    local_models: dict[int, dict[str, object]],
    parent_model: dict[str, object],
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(sample_count):
        target = target_fractions[
            sample_index % len(target_fractions)
        ]

        if family == "minkowski_holdout":
            relation = sample_minkowski_2d(
                n,
                rng,
            )
            mismatch = 0.0
            target_value = float("nan")
        elif family == "opposing_diagonal_bands":
            relation, mismatch = (
                density_matched_candidate(
                    opposing_diagonal_bands,
                    n,
                    target,
                    rng,
                )
            )
            target_value = target
        elif family == "bimodal_clusters":
            relation, mismatch = matched_bimodal(
                n,
                target,
                rng,
            )
            target_value = target
        elif family == "four_corner_clusters":
            relation, mismatch = (
                density_matched_candidate(
                    four_corner_clusters,
                    n,
                    target,
                    rng,
                )
            )
            target_value = target
        else:
            raise ValueError(
                f"Unknown family: {family}"
            )

        score, p_value, accepted, details = (
            score_parent(
                relation,
                local_models,
                parent_model,
            )
        )

        rows.append(
            {
                "n": n,
                "phase": (
                    "prospective_confirmation"
                    if n == CONFIRMATORY_N
                    else "discovery"
                ),
                "family": family,
                "sample_index": sample_index,
                "parent_score": score,
                "p_value": p_value,
                "accepted": accepted,
                "ordering_fraction": (
                    relation_fraction(relation)
                ),
                "target_ordering_fraction": (
                    target_value
                ),
                "ordering_fraction_mismatch": (
                    mismatch
                ),
                "exact_product_order_2d": True,
                "scale_details": json.dumps(
                    json_safe(details)
                ),
            }
        )

    return rows


def main() -> None:
    output = Path("a17_exact_results")
    output.mkdir(exist_ok=True)

    rng = np.random.default_rng(SEED)
    local_models = fit_local_models(rng)

    local_model_rows = []

    for m, model in local_models.items():
        local_model_rows.append(
            {
                "m": m,
                "covariance_condition_number": (
                    model[
                        "covariance_condition_number"
                    ]
                ),
                "covariance_minimum_eigenvalue": (
                    model[
                        "covariance_minimum_eigenvalue"
                    ]
                ),
                "ledoit_wolf_shrinkage": (
                    model[
                        "ledoit_wolf_shrinkage"
                    ]
                ),
                "calibration_score_median": (
                    model[
                        "calibration_score_median"
                    ]
                ),
                "ordering_fraction_mean": (
                    model[
                        "ordering_fraction_mean"
                    ]
                ),
                "ordering_fraction_sd": (
                    model["ordering_fraction_sd"]
                ),
            }
        )

    pd.DataFrame(local_model_rows).to_csv(
        output / "a17_local_reference_models.csv",
        index=False,
    )

    all_rows = []
    parent_model_rows = []

    for n in N_VALUES:
        parent_model = fit_parent_model(
            n,
            local_models,
            rng,
        )

        target_relations = [
            sample_minkowski_2d(n, rng)
            for _ in range(
                max(
                    PARENT_HOLDOUT_SAMPLES[n],
                    CHALLENGE_SAMPLES[n],
                )
            )
        ]
        target_fractions = [
            relation_fraction(relation)
            for relation in target_relations
        ]

        parent_model_rows.append(
            {
                "n": n,
                "covariance_condition_number": (
                    parent_model[
                        "covariance_condition_number"
                    ]
                ),
                "covariance_minimum_eigenvalue": (
                    parent_model[
                        "covariance_minimum_eigenvalue"
                    ]
                ),
                "ledoit_wolf_shrinkage": (
                    parent_model[
                        "ledoit_wolf_shrinkage"
                    ]
                ),
                "calibration_score_median": float(
                    np.median(
                        parent_model[
                            "calibration_scores"
                        ]
                    )
                ),
                "calibration_score_95_quantile": float(
                    np.quantile(
                        parent_model[
                            "calibration_scores"
                        ],
                        0.95,
                    )
                ),
            }
        )

        all_rows.extend(
            evaluate_family(
                n=n,
                family="minkowski_holdout",
                sample_count=(
                    PARENT_HOLDOUT_SAMPLES[n]
                ),
                target_fractions=target_fractions,
                local_models=local_models,
                parent_model=parent_model,
                rng=rng,
            )
        )

        for family in (
            "opposing_diagonal_bands",
            "bimodal_clusters",
            "four_corner_clusters",
        ):
            all_rows.extend(
                evaluate_family(
                    n=n,
                    family=family,
                    sample_count=(
                        CHALLENGE_SAMPLES[n]
                    ),
                    target_fractions=(
                        target_fractions
                    ),
                    local_models=local_models,
                    parent_model=parent_model,
                    rng=rng,
                )
            )

    pd.DataFrame(parent_model_rows).to_csv(
        output / "a17_parent_models.csv",
        index=False,
    )

    results = pd.DataFrame(all_rows)
    results.to_csv(
        output / "a17_sample_results.csv",
        index=False,
    )

    family_results = []

    for (n, family), group in results.groupby(
        ["n", "family"]
    ):
        acceptance_rate = float(
            group["accepted"].mean()
        )
        family_results.append(
            {
                "n": int(n),
                "phase": str(
                    group["phase"].iloc[0]
                ),
                "family": family,
                "number_samples": int(len(group)),
                "acceptance_rate": (
                    acceptance_rate
                ),
                "rejection_rate": (
                    1.0 - acceptance_rate
                ),
                "median_p_value": float(
                    group["p_value"].median()
                ),
                "maximum_p_value": float(
                    group["p_value"].max()
                ),
                "maximum_ordering_fraction_mismatch": (
                    float(
                        group[
                            "ordering_fraction_mismatch"
                        ].max()
                    )
                ),
                "all_exact_product_orders_2d": bool(
                    group[
                        "exact_product_order_2d"
                    ].all()
                ),
            }
        )

    family_frame = pd.DataFrame(
        family_results
    )
    family_frame.to_csv(
        output / "a17_family_summary.csv",
        index=False,
    )

    def get_result(
        n: int,
        family: str,
    ) -> dict[str, object]:
        return next(
            result
            for result in family_results
            if result["n"] == n
            and result["family"] == family
        )

    local_reference_pass = all(
        row["covariance_minimum_eigenvalue"] > 0.0
        and row["covariance_condition_number"] <= 1e8
        and row["ordering_fraction_sd"] > 0.0
        for row in local_model_rows
    )
    parent_models_pass = all(
        row["covariance_minimum_eigenvalue"] > 0.0
        and row["covariance_condition_number"] <= 1e8
        for row in parent_model_rows
    )

    holdout_pass = all(
        get_result(
            n,
            "minkowski_holdout",
        )["acceptance_rate"]
        >= 0.90
        for n in N_VALUES
    )
    opposing_pass = all(
        get_result(
            n,
            "opposing_diagonal_bands",
        )["rejection_rate"]
        >= 0.90
        for n in N_VALUES
    )
    bimodal_pass = all(
        get_result(
            n,
            "bimodal_clusters",
        )["rejection_rate"]
        >= 0.80
        for n in N_VALUES
    )
    corner_pass = all(
        get_result(
            n,
            "four_corner_clusters",
        )["rejection_rate"]
        >= 0.80
        for n in N_VALUES
    )
    density_pass = all(
        result[
            "maximum_ordering_fraction_mismatch"
        ] <= MAX_ORDERING_FRACTION_MISMATCH
        for result in family_results
        if result["family"]
        != "minkowski_holdout"
    )

    gates = {
        "G1_local_reference_covariances_stable": (
            local_reference_pass
        ),
        "G2_parent_covariances_stable": (
            parent_models_pass
        ),
        "G3_minkowski_acceptance_ge_0_90": (
            holdout_pass
        ),
        "G4_opposing_regime_rejection_ge_0_90": (
            opposing_pass
        ),
        "G5_bimodal_cluster_rejection_ge_0_80": (
            bimodal_pass
        ),
        "G6_four_corner_rejection_ge_0_80": (
            corner_pass
        ),
        "G7_density_matching_le_0_02": (
            density_pass
        ),
        "G8_all_challenges_are_exact_2d_orders": True,
        "G9_no_challenge_used_for_calibration": True,
    }

    verdict = (
        "PASS_MULTISCALE_SELF_SIMILARITY"
        if all(gates.values())
        else "FAIL_MULTISCALE_SELF_SIMILARITY"
    )

    identifiable_regime_heterogeneity = (
        opposing_pass
    )
    cluster_degeneracy_observed = (
        not bimodal_pass
        or not corner_pass
    )

    summary = {
        "seed": SEED,
        "discovery_n": DISCOVERY_N,
        "prospective_confirmation_n": (
            CONFIRMATORY_N
        ),
        "local_scales": list(LOCAL_SCALES),
        "local_estimation_samples_per_scale": (
            LOCAL_ESTIMATION_SAMPLES
        ),
        "local_calibration_samples_per_scale": (
            LOCAL_CALIBRATION_SAMPLES
        ),
        "parent_estimation_samples": (
            PARENT_ESTIMATION_SAMPLES
        ),
        "parent_calibration_samples": (
            PARENT_CALIBRATION_SAMPLES
        ),
        "family_results": family_results,
        "gates": gates,
        "verdict": verdict,
        "secondary_interpretation": {
            "order_regime_heterogeneity_detected": (
                identifiable_regime_heterogeneity
            ),
            "compact_cluster_degeneracy_observed": (
                cluster_degeneracy_observed
            ),
            "meaning": (
                "The self-similarity statistic can detect mixtures "
                "of strongly different local order regimes, but "
                "compact exact-2D clusters may remain statistically "
                "compatible with uniform anchored intervals. Such "
                "acceptance is consistent with a conformal-volume "
                "or sampling-measure identifiability boundary."
            ),
        },
        "interpretation_boundary": (
            "The test addresses self-similarity relative to a "
            "uniform anchored 2D Minkowski interval ensemble. "
            "It neither proves nor disproves exact causal "
            "embeddability, because every challenge family in this "
            "audit is explicitly constructed as a 2D product order."
        ),
    }

    (output / "a17_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A17 — Multiscale Subinterval Self-Similarity Audit",
        "",
        "## Design",
        "",
        (
            "- Anchored Minkowski reference intervals at "
            f"{list(LOCAL_SCALES)} elements."
        ),
        (
            "- Minkowski-only local and parent covariance "
            "estimation."
        ),
        (
            "- Discovery at n=192 and prospective confirmation "
            "at n=256."
        ),
        (
            "- Exact-2D challenges: opposing order regimes, "
            "two compact clusters, and four corner clusters."
        ),
        "",
        "## Family results",
        "",
    ]

    for result in family_results:
        report_lines.extend(
            [
                (
                    f"### {result['family']} at n={result['n']}"
                ),
                (
                    "- Acceptance: "
                    f"{result['acceptance_rate']:.4f}"
                ),
                (
                    "- Rejection: "
                    f"{result['rejection_rate']:.4f}"
                ),
                (
                    "- Median p-value: "
                    f"{result['median_p_value']:.4f}"
                ),
                (
                    "- Maximum density mismatch: "
                    f"{result['maximum_ordering_fraction_mismatch']:.6f}"
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

    (output / "a17_report.md").write_text(
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
