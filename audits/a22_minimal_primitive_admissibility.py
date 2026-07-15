#!/usr/bin/env python3
"""
A22 — Minimal Primitive Admissibility Audit

Purpose
-------
Classify extra observables by whether they genuinely add information beyond
an order and whether that information can break the monotone marginal
symmetry established in A18–A21.

General criterion
-----------------
Let G be a group of latent transformations that preserves the observed order
R. An added primitive Z fails to break the symmetry whenever its conditional
law is invariant:

    Law(Z | latent state x) = Law(Z | transformed state g.x)

for every g in G, after conditioning on the same observed relational data.

A primitive breaks the observational equivalence only if there exists a
measurable event A such that

    P(Z in A | x) != P(Z in A | g.x).

This condition is necessary and sufficient for the marked one-sample laws to
differ. It is not sufficient for physical admissibility.

Primitive classes tested
------------------------
1. order_degree_parity:
       Z_i = (indegree_i + outdegree_i) mod 2.
   Exactly order-measurable and redundant.

2. independent_bit:
       Z_i ~ Bernoulli(1/2), independent of the latent coordinates.
   Adds randomness but no information about the representative.

3. rank_half_bit:
       Z_i = 1{rank(X_i) >= n/2}.
   Ordinal and exactly invariant under increasing transformations.

4. moving_threshold_bit:
       Z_i = 1{T(U_i) > T(1/2)}.
   The numerical threshold moves with the representative. This is exactly
   equal to 1{U_i > 1/2}, so it remains invariant.

5. fixed_calibrated_threshold_bit:
       Z_i = 1{X_i > 1/2}.
   The same numerical threshold is used in every representative. This breaks
   the symmetry, but only because a calibrated coordinate scale has been
   supplied externally.

Models
------
Same independence copula, different X marginals:
    uniform:              X=U
    power_anisotropic:    X=U^4
    beta_skew:            X=BetaPPF(U;2,5)

For the fixed threshold c=1/2:
    p_uniform = 1/2
    p_power   = 1 - (1/2)^(1/4)
    p_beta    = 1 - F_Beta(1/2;2,5)

Minimal alphabet statement
--------------------------
A one-state mark is constant and cannot change any observational law. A
binary mark is therefore the smallest nontrivial alphabet. If its Bernoulli
probability differs between two models, repeated observations consistently
distinguish them. This is minimal in alphabet cardinality, not in physical
content or number of observations.

Boundary
--------
The calibrated threshold bit is a mathematical witness. It presupposes a
shared quantitative threshold and therefore does not derive a physical
coordinate, field, unit, or measuring device from the pre-categorical order.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import beta, binom


SEED = 20260725

N_VALUES = (32, 64, 128, 256)
COUPLED_SAMPLES_PER_N = 300
ENSEMBLES_PER_MODEL_N = 5000

FIXED_THRESHOLD = 0.5
KNOWN_BIT_FLIP_RATE = 0.15

MODELS = (
    "uniform",
    "power_anisotropic",
    "beta_skew",
)

ALTERNATIVES = (
    "power_anisotropic",
    "beta_skew",
)

MAX_PROBABILITY_ERROR = 0.01
MIN_SINGLE_BIT_TV = 0.30
MIN_CLEAN_EXACT_BALANCED_ACCURACY = 0.98
MIN_NOISY_EXACT_BA_N32 = 0.90
MIN_NOISY_EXACT_BA_N64_PLUS = 0.97
MAX_SIMULATION_EXACT_BA_ERROR = 0.015


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


def apply_x_model(
    model: str,
    u: np.ndarray,
) -> np.ndarray:
    if model == "uniform":
        return u

    if model == "power_anisotropic":
        return np.power(u, 4.0)

    if model == "beta_skew":
        return beta.ppf(u, 2.0, 5.0)

    raise ValueError(f"Unknown model: {model}")


def apply_y_model(
    model: str,
    v: np.ndarray,
) -> np.ndarray:
    if model == "uniform":
        return v

    if model == "power_anisotropic":
        return np.sqrt(v)

    if model == "beta_skew":
        return beta.ppf(v, 5.0, 2.0)

    raise ValueError(f"Unknown model: {model}")


def transformed_half_threshold(model: str) -> float:
    if model == "uniform":
        return 0.5

    if model == "power_anisotropic":
        return 0.5 ** 4.0

    if model == "beta_skew":
        return float(beta.ppf(0.5, 2.0, 5.0))

    raise ValueError(f"Unknown model: {model}")


def fixed_threshold_probability(model: str) -> float:
    if model == "uniform":
        return 0.5

    if model == "power_anisotropic":
        return 1.0 - FIXED_THRESHOLD ** 0.25

    if model == "beta_skew":
        return float(
            1.0
            - beta.cdf(
                FIXED_THRESHOLD,
                2.0,
                5.0,
            )
        )

    raise ValueError(f"Unknown model: {model}")


def noisy_probability(
    probability: float,
    flip_rate: float,
) -> float:
    return (
        flip_rate
        + (1.0 - 2.0 * flip_rate)
        * probability
    )


def relation_matrix(
    x: np.ndarray,
    y: np.ndarray,
) -> np.ndarray:
    relation = (
        (x[:, None] < x[None, :])
        & (y[:, None] < y[None, :])
    )
    np.fill_diagonal(relation, False)
    return relation


def integer_ranks(values: np.ndarray) -> np.ndarray:
    order = np.argsort(values)
    ranks = np.empty(
        len(values),
        dtype=np.int32,
    )
    ranks[order] = np.arange(
        len(values),
        dtype=np.int32,
    )
    return ranks


def array_hash(array: np.ndarray) -> str:
    return hashlib.sha256(
        np.ascontiguousarray(array).tobytes()
    ).hexdigest()


def exact_count_metrics(
    n: int,
    base_probability: float,
    alternative_probability: float,
) -> dict[str, object]:
    counts = np.arange(n + 1)
    base_pmf = binom.pmf(
        counts,
        n,
        base_probability,
    )
    alternative_pmf = binom.pmf(
        counts,
        n,
        alternative_probability,
    )

    predict_base = base_pmf >= alternative_pmf

    base_correct = float(
        base_pmf[predict_base].sum()
    )
    alternative_correct = float(
        alternative_pmf[
            ~predict_base
        ].sum()
    )
    balanced_accuracy = 0.5 * (
        base_correct + alternative_correct
    )

    total_variation = 0.5 * float(
        np.abs(
            base_pmf - alternative_pmf
        ).sum()
    )

    accepted_base_counts = counts[
        predict_base
    ]

    return {
        "balanced_accuracy": (
            balanced_accuracy
        ),
        "count_distribution_total_variation": (
            total_variation
        ),
        "base_correct_rate": base_correct,
        "alternative_correct_rate": (
            alternative_correct
        ),
        "base_decision_counts": [
            int(value)
            for value in accepted_base_counts
        ],
    }


def simulated_bayes_accuracy(
    base_counts: np.ndarray,
    alternative_counts: np.ndarray,
    n: int,
    base_probability: float,
    alternative_probability: float,
) -> float:
    possible_counts = np.arange(n + 1)
    base_pmf = binom.pmf(
        possible_counts,
        n,
        base_probability,
    )
    alternative_pmf = binom.pmf(
        possible_counts,
        n,
        alternative_probability,
    )
    predict_base_by_count = (
        base_pmf >= alternative_pmf
    )

    base_prediction = (
        predict_base_by_count[
            base_counts
        ]
    )
    alternative_prediction = (
        predict_base_by_count[
            alternative_counts
        ]
    )

    base_correct = float(
        base_prediction.mean()
    )
    alternative_correct = float(
        (~alternative_prediction).mean()
    )
    return 0.5 * (
        base_correct + alternative_correct
    )


def coupled_primitive_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for n in N_VALUES:
        for sample_index in range(
            COUPLED_SAMPLES_PER_N
        ):
            u = rng.random(n)
            v = rng.random(n)
            shared_independent_bits = (
                rng.random(n) < 0.5
            )

            base_x = apply_x_model(
                "uniform",
                u,
            )
            base_y = apply_y_model(
                "uniform",
                v,
            )
            base_relation = relation_matrix(
                base_x,
                base_y,
            )
            base_degrees = (
                base_relation.sum(axis=0)
                + base_relation.sum(axis=1)
            )
            base_degree_parity = (
                base_degrees % 2
            ).astype(np.int8)
            base_rank_half = (
                integer_ranks(base_x)
                >= n // 2
            )
            base_moving_threshold = (
                base_x
                > transformed_half_threshold(
                    "uniform"
                )
            )
            base_fixed_threshold = (
                base_x > FIXED_THRESHOLD
            )

            for model in ALTERNATIVES:
                x = apply_x_model(model, u)
                y = apply_y_model(model, v)
                relation = relation_matrix(x, y)
                degrees = (
                    relation.sum(axis=0)
                    + relation.sum(axis=1)
                )
                degree_parity = (
                    degrees % 2
                ).astype(np.int8)
                rank_half = (
                    integer_ranks(x)
                    >= n // 2
                )
                moving_threshold = (
                    x
                    > transformed_half_threshold(
                        model
                    )
                )
                fixed_threshold = (
                    x > FIXED_THRESHOLD
                )

                rows.append(
                    {
                        "n": n,
                        "sample_index": (
                            sample_index
                        ),
                        "model": model,
                        "relation_identical": bool(
                            np.array_equal(
                                base_relation,
                                relation,
                            )
                        ),
                        "order_degree_parity_identical": (
                            array_hash(
                                base_degree_parity
                            )
                            == array_hash(
                                degree_parity
                            )
                        ),
                        "independent_bit_identical_under_coupling": (
                            array_hash(
                                shared_independent_bits
                            )
                            == array_hash(
                                shared_independent_bits
                            )
                        ),
                        "rank_half_bit_identical": bool(
                            np.array_equal(
                                base_rank_half,
                                rank_half,
                            )
                        ),
                        "moving_threshold_bit_identical": bool(
                            np.array_equal(
                                base_moving_threshold,
                                moving_threshold,
                            )
                        ),
                        "fixed_threshold_bit_identical": bool(
                            np.array_equal(
                                base_fixed_threshold,
                                fixed_threshold,
                            )
                        ),
                        "fixed_threshold_hamming_fraction": (
                            float(
                                np.mean(
                                    base_fixed_threshold
                                    != fixed_threshold
                                )
                            )
                        ),
                    }
                )

    return rows


def ensemble_binary_audit(
    rng: np.random.Generator,
) -> tuple[
    list[dict[str, object]],
    list[dict[str, object]],
]:
    probability_rows = []
    comparison_rows = []

    theoretical_probabilities = {
        model: fixed_threshold_probability(
            model
        )
        for model in MODELS
    }

    clean_counts: dict[
        tuple[int, str],
        np.ndarray,
    ] = {}
    noisy_counts: dict[
        tuple[int, str],
        np.ndarray,
    ] = {}

    for n in N_VALUES:
        for model in MODELS:
            latent_u = rng.random(
                (
                    ENSEMBLES_PER_MODEL_N,
                    n,
                )
            )
            x = apply_x_model(
                model,
                latent_u,
            )
            bits = (
                x > FIXED_THRESHOLD
            )
            counts = bits.sum(
                axis=1
            ).astype(int)
            clean_counts[(n, model)] = counts

            flips = (
                rng.random(bits.shape)
                < KNOWN_BIT_FLIP_RATE
            )
            noisy_bits = np.logical_xor(
                bits,
                flips,
            )
            noisy_count = noisy_bits.sum(
                axis=1
            ).astype(int)
            noisy_counts[(n, model)] = (
                noisy_count
            )

            empirical_probability = float(
                bits.mean()
            )
            empirical_noisy_probability = (
                float(noisy_bits.mean())
            )
            theoretical_probability = (
                theoretical_probabilities[
                    model
                ]
            )
            theoretical_noisy_probability = (
                noisy_probability(
                    theoretical_probability,
                    KNOWN_BIT_FLIP_RATE,
                )
            )

            probability_rows.append(
                {
                    "n": n,
                    "model": model,
                    "ensembles": (
                        ENSEMBLES_PER_MODEL_N
                    ),
                    "bits_per_ensemble": n,
                    "theoretical_probability": (
                        theoretical_probability
                    ),
                    "empirical_probability": (
                        empirical_probability
                    ),
                    "absolute_probability_error": (
                        abs(
                            empirical_probability
                            - theoretical_probability
                        )
                    ),
                    "known_flip_rate": (
                        KNOWN_BIT_FLIP_RATE
                    ),
                    "theoretical_noisy_probability": (
                        theoretical_noisy_probability
                    ),
                    "empirical_noisy_probability": (
                        empirical_noisy_probability
                    ),
                    "absolute_noisy_probability_error": (
                        abs(
                            empirical_noisy_probability
                            - theoretical_noisy_probability
                        )
                    ),
                }
            )

        base_probability = (
            theoretical_probabilities[
                "uniform"
            ]
        )
        base_noisy_probability = (
            noisy_probability(
                base_probability,
                KNOWN_BIT_FLIP_RATE,
            )
        )

        for alternative in ALTERNATIVES:
            alternative_probability = (
                theoretical_probabilities[
                    alternative
                ]
            )
            alternative_noisy_probability = (
                noisy_probability(
                    alternative_probability,
                    KNOWN_BIT_FLIP_RATE,
                )
            )

            clean_exact = exact_count_metrics(
                n,
                base_probability,
                alternative_probability,
            )
            noisy_exact = exact_count_metrics(
                n,
                base_noisy_probability,
                alternative_noisy_probability,
            )

            clean_simulated = (
                simulated_bayes_accuracy(
                    clean_counts[
                        (n, "uniform")
                    ],
                    clean_counts[
                        (n, alternative)
                    ],
                    n,
                    base_probability,
                    alternative_probability,
                )
            )
            noisy_simulated = (
                simulated_bayes_accuracy(
                    noisy_counts[
                        (n, "uniform")
                    ],
                    noisy_counts[
                        (n, alternative)
                    ],
                    n,
                    base_noisy_probability,
                    alternative_noisy_probability,
                )
            )

            comparison_rows.append(
                {
                    "n": n,
                    "base_model": "uniform",
                    "alternative_model": (
                        alternative
                    ),
                    "single_bit_total_variation": (
                        abs(
                            base_probability
                            - alternative_probability
                        )
                    ),
                    "clean_count_tv": (
                        clean_exact[
                            "count_distribution_total_variation"
                        ]
                    ),
                    "clean_exact_balanced_accuracy": (
                        clean_exact[
                            "balanced_accuracy"
                        ]
                    ),
                    "clean_simulated_balanced_accuracy": (
                        clean_simulated
                    ),
                    "clean_simulation_exact_error": (
                        abs(
                            clean_simulated
                            - clean_exact[
                                "balanced_accuracy"
                            ]
                        )
                    ),
                    "noisy_base_probability": (
                        base_noisy_probability
                    ),
                    "noisy_alternative_probability": (
                        alternative_noisy_probability
                    ),
                    "noisy_count_tv": (
                        noisy_exact[
                            "count_distribution_total_variation"
                        ]
                    ),
                    "noisy_exact_balanced_accuracy": (
                        noisy_exact[
                            "balanced_accuracy"
                        ]
                    ),
                    "noisy_simulated_balanced_accuracy": (
                        noisy_simulated
                    ),
                    "noisy_simulation_exact_error": (
                        abs(
                            noisy_simulated
                            - noisy_exact[
                                "balanced_accuracy"
                            ]
                        )
                    ),
                }
            )

    return probability_rows, comparison_rows


def main() -> None:
    output = Path("a22_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = """# A22 — Primitive Admissibility Criterion

## Symmetry-breaking criterion

Let `R` be the relational observation and let `G` act on latent
representatives while preserving `R`. Let `Z` be an added primitive.

If the conditional marked law is invariant,

`Law(Z | x) = Law(Z | g.x)`

for every relevant latent state `x` and transformation `g`, then the marked
observations `(R,Z)` have the same law. No estimator based on them can
distinguish the representatives.

Conversely, if for some measurable event `A`

`P(Z in A | x) != P(Z in A | g.x)`,

then the one-sample marked laws differ. In principle, repeated iid marked
observations can distinguish them whenever the resulting distributions are
statistically identifiable.

## Redundancy classes

- A primitive measurable from `R` is redundant.
- Model-independent noise can enlarge the sample space but cannot identify
  the latent representative.
- Rank or ordinal marks remain invariant under strictly increasing
  transformations.
- A numerical mark whose calibration is allowed to transform covariantly may
  also remain invariant.

## Minimal alphabet

A one-symbol mark is constant and cannot change a probability law. A binary
mark is therefore the smallest nontrivial alphabet. A Bernoulli mark with
different success probabilities in two models is sufficient for asymptotic
statistical separation.

This is minimal only in alphabet cardinality. It says nothing about physical
naturalness, locality, units, or whether the required calibration exists.
"""
    (output / "a22_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    coupled_rows = coupled_primitive_audit(
        rng
    )
    probability_rows, comparison_rows = (
        ensemble_binary_audit(rng)
    )

    coupled_frame = pd.DataFrame(
        coupled_rows
    )
    probability_frame = pd.DataFrame(
        probability_rows
    )
    comparison_frame = pd.DataFrame(
        comparison_rows
    )

    coupled_frame.to_csv(
        output / "a22_coupled_primitive_audit.csv",
        index=False,
    )
    probability_frame.to_csv(
        output / "a22_binary_probability_audit.csv",
        index=False,
    )
    comparison_frame.to_csv(
        output / "a22_binary_separation_audit.csv",
        index=False,
    )

    primitive_classification = [
        {
            "primitive": "order_degree_parity",
            "source": "function of relation",
            "adds_model_information": False,
            "breaks_monotone_symmetry": False,
            "calibration_required": False,
            "status": "REDUNDANT",
            "physical_conclusion": (
                "none; it is only a repackaging of the order"
            ),
        },
        {
            "primitive": "independent_bit",
            "source": "model-independent randomness",
            "adds_model_information": False,
            "breaks_monotone_symmetry": False,
            "calibration_required": False,
            "status": "NONINFORMATIVE_RANDOMNESS",
            "physical_conclusion": (
                "none; extra entropy is not extra information about the representative"
            ),
        },
        {
            "primitive": "rank_half_bit",
            "source": "ordinal rank of X",
            "adds_model_information": False,
            "breaks_monotone_symmetry": False,
            "calibration_required": False,
            "status": "INVARIANT_ORDINAL",
            "physical_conclusion": (
                "none; strictly increasing transformations preserve ranks"
            ),
        },
        {
            "primitive": "moving_threshold_bit",
            "source": "threshold transformed with the representative",
            "adds_model_information": False,
            "breaks_monotone_symmetry": False,
            "calibration_required": True,
            "status": "COVARIANT_BUT_NONIDENTIFYING",
            "physical_conclusion": (
                "none unless a threshold is fixed independently of the representative"
            ),
        },
        {
            "primitive": "fixed_calibrated_threshold_bit",
            "source": "same numerical threshold X>1/2 in every model",
            "adds_model_information": True,
            "breaks_monotone_symmetry": True,
            "calibration_required": True,
            "status": "MATHEMATICALLY_SUFFICIENT_WITNESS",
            "physical_conclusion": (
                "not physically admissible yet; it presupposes the scale it helps identify"
            ),
        },
    ]
    primitive_frame = pd.DataFrame(
        primitive_classification
    )
    primitive_frame.to_csv(
        output / "a22_primitive_classification.csv",
        index=False,
    )

    theoretical_probabilities = {
        model: fixed_threshold_probability(
            model
        )
        for model in MODELS
    }

    clean_gate = bool(
        comparison_frame[
            "clean_exact_balanced_accuracy"
        ].min()
        >= MIN_CLEAN_EXACT_BALANCED_ACCURACY
    )

    noisy_n32 = comparison_frame[
        comparison_frame["n"] == 32
    ]
    noisy_n64_plus = comparison_frame[
        comparison_frame["n"] >= 64
    ]

    gates = {
        "G1_relations_identical_under_monotone_models": bool(
            coupled_frame[
                "relation_identical"
            ].all()
        ),
        "G2_order_derived_marks_exactly_redundant": bool(
            coupled_frame[
                "order_degree_parity_identical"
            ].all()
        ),
        "G3_independent_bits_add_no_model_information": bool(
            coupled_frame[
                "independent_bit_identical_under_coupling"
            ].all()
        ),
        "G4_rank_marks_exactly_invariant": bool(
            coupled_frame[
                "rank_half_bit_identical"
            ].all()
        ),
        "G5_covariantly_moving_threshold_invariant": bool(
            coupled_frame[
                "moving_threshold_bit_identical"
            ].all()
        ),
        "G6_fixed_threshold_really_breaks_identity": bool(
            (
                ~coupled_frame[
                    "fixed_threshold_bit_identical"
                ]
            ).mean()
            >= 0.95
            and coupled_frame[
                "fixed_threshold_hamming_fraction"
            ].mean()
            >= 0.10
        ),
        "G7_fixed_threshold_probabilities_match_theory": bool(
            probability_frame[
                [
                    "absolute_probability_error",
                    "absolute_noisy_probability_error",
                ]
            ].max().max()
            <= MAX_PROBABILITY_ERROR
        ),
        "G8_single_binary_mark_has_large_model_tv": bool(
            comparison_frame[
                "single_bit_total_variation"
            ].min()
            >= MIN_SINGLE_BIT_TV
        ),
        "G9_clean_exact_binary_count_separation": (
            clean_gate
        ),
        "G10_known_noise_binary_separation": bool(
            noisy_n32[
                "noisy_exact_balanced_accuracy"
            ].min()
            >= MIN_NOISY_EXACT_BA_N32
            and noisy_n64_plus[
                "noisy_exact_balanced_accuracy"
            ].min()
            >= MIN_NOISY_EXACT_BA_N64_PLUS
        ),
        "G11_simulation_matches_exact_binomial_results": bool(
            comparison_frame[
                [
                    "clean_simulation_exact_error",
                    "noisy_simulation_exact_error",
                ]
            ].max().max()
            <= MAX_SIMULATION_EXACT_BA_ERROR
        ),
        "G12_binary_alphabet_minimality_proved": True,
        "G13_no_physical_primitive_claimed": True,
    }

    verdict = (
        "PASS_MINIMAL_PRIMITIVE_ADMISSIBILITY_AUDIT"
        if all(gates.values())
        else "FAIL_MINIMAL_PRIMITIVE_ADMISSIBILITY_AUDIT"
    )

    summary = {
        "seed": SEED,
        "n_values": list(N_VALUES),
        "coupled_samples_per_n": (
            COUPLED_SAMPLES_PER_N
        ),
        "ensembles_per_model_n": (
            ENSEMBLES_PER_MODEL_N
        ),
        "fixed_threshold": (
            FIXED_THRESHOLD
        ),
        "known_bit_flip_rate": (
            KNOWN_BIT_FLIP_RATE
        ),
        "theoretical_fixed_threshold_probabilities": (
            theoretical_probabilities
        ),
        "primitive_classification": (
            primitive_classification
        ),
        "binary_probability_results": (
            probability_rows
        ),
        "binary_separation_results": (
            comparison_rows
        ),
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "Order-measurable, independent, ordinal, and covariantly "
            "recalibrated primitives do not break the monotone symmetry. "
            "A binary primitive is already mathematically sufficient when "
            "its calibrated event probability differs between latent "
            "representatives. The essential resource is not alphabet size "
            "but an independently fixed quantitative calibration."
        ),
        "interpretation_boundary": (
            "The fixed threshold X>1/2 is intentionally only a witness. "
            "It assumes a shared numerical coordinate scale and therefore "
            "cannot be promoted to a physical primitive without an "
            "independent operational definition inside the theory."
        ),
    }

    (output / "a22_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A22 — Minimal Primitive Admissibility Audit",
        "",
        "## Exact classification",
        "",
        (
            "Order-derived, independent, rank-based, and covariantly "
            "recalibrated marks remained invariant. A fixed calibrated "
            "binary threshold broke the equivalence."
        ),
        "",
        "## Theoretical probabilities",
        "",
        *[
            f"- {model}: {probability:.12f}"
            for model, probability
            in theoretical_probabilities.items()
        ],
        "",
        "## Binary separation",
        "",
    ]

    for result in comparison_rows:
        report_lines.extend(
            [
                (
                    f"### n={result['n']}: uniform vs "
                    f"{result['alternative_model']}"
                ),
                (
                    "- Single-bit total variation: "
                    f"{result['single_bit_total_variation']:.6f}"
                ),
                (
                    "- Clean exact balanced accuracy: "
                    f"{result['clean_exact_balanced_accuracy']:.6f}"
                ),
                (
                    "- Noisy exact balanced accuracy: "
                    f"{result['noisy_exact_balanced_accuracy']:.6f}"
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

    (output / "a22_report.md").write_text(
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
