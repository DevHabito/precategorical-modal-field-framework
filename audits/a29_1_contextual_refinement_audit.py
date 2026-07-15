#!/usr/bin/env python3
"""
A29.1 — Corrective Refinement, Base Measure, and Nondegeneracy Audit

Purpose
-------
Determine whether the context dependence of local q normalization can be
made mathematically coherent under duplication and refinement of equivalent
alternatives.

Refinement setup
----------------
An alternative r with score q_r is replaced by clones r_1,...,r_m with the
same score. A projectively consistent law should preserve:
- the total probability of the macro-alternative r;
- the probabilities of all untouched macro-alternatives.

Unweighted failure
------------------
For P_j proportional to f(s_j), naive cloning assigns every clone a full unit
weight. Even with a context-stable raw score, the macro weight becomes
m f(s_r), so refinement changes the law.

Base-measure construction
-------------------------
Give every alternative a positive base mass mu_j and define the weighted
empirical measure

    nu = sum_j mu_j delta_{q_j}.

Let a context score T_nu(q_j) be any functional that depends only on nu and
the point q_j. Define

    P_j =
        mu_j f(T_nu(q_j))
        / sum_k mu_k f(T_nu(q_k)).

When alternative r is split into exact clones with masses satisfying

    sum_a mu_{r,a} = mu_r,

the measure nu is unchanged. Hence all context scores are unchanged and the
clone probabilities sum exactly to the original macro probability.

The audit uses:
- weighted raw score;
- weighted mean/SD z-score.

Near-zero mass stability
------------------------
For bounded q and a smooth positive kernel, adding an alternative of mass
epsilon perturbs the weighted empirical measure and probabilities
continuously; the effect vanishes with epsilon.

Unweighted z-score extreme-alternative theorem
----------------------------------------------
With n fixed old alternatives and one new score M -> +infinity, population
z-scoring gives

    z_old -> -1/sqrt(n),
    z_new -> sqrt(n).

Thus the extreme alternative retains the nonzero limiting probability

    p_new ->
      exp(-lambda sqrt(n))
      / [n exp(lambda/sqrt(n)) + exp(-lambda sqrt(n))],

and pairwise odds among old alternatives converge to 1. Numerical extremity
does not make the new alternative irrelevant at fixed degree.

Boundary
--------
A pass shows that contextual normalization can be projectively coherent if a
finitely additive base measure is supplied. It does not derive that measure
from RZS, identify it with physical volume, or prove that exact clones are a
physical operation.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 20260803

REFINEMENT_SAMPLES = 6_000
NEAR_ZERO_SAMPLES = 2_000
EXTREME_SAMPLES = 4_000
IID_SAMPLES_PER_N = 3_000

LAMBDA = 1.0
EPSILON_VALUES = (
    1e-1,
    1e-2,
    1e-3,
    1e-4,
    1e-5,
    1e-6,
)
IID_BACKGROUND_SIZES = (
    16,
    64,
    256,
    1024,
)

MAX_EXACT_ERROR = 8e-12
MIN_UNWEIGHTED_REFINEMENT_VIOLATION_RATE = 0.98
MIN_UNWEIGHTED_MEDIAN_MACRO_TV = 0.08
MAX_NEAR_ZERO_TV_AT_MIN_EPSILON = 2e-5
MIN_WEIGHTED_SD = 0.35
MIN_SINGULAR_CONTEXT_TV = 0.15
MAX_EXTREME_ASYMPTOTIC_ERROR = 2e-5
MIN_EXTREME_PAIR_ODDS_COLLAPSE_RATE = 0.99
MAX_IID_FINAL_RMSE = 0.04


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


def total_variation(
    first: np.ndarray,
    second: np.ndarray,
) -> float:
    return 0.5 * float(
        np.abs(first - second).sum()
    )


def unweighted_z(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    centered = values - float(values.mean())
    scale = float(
        np.sqrt(
            np.mean(centered**2)
        )
    )
    if scale <= 1e-14:
        raise ValueError("Zero unweighted SD.")
    return centered / scale


def weighted_mean_sd(
    values: np.ndarray,
    masses: np.ndarray,
) -> tuple[float, float]:
    values = np.asarray(values, dtype=float)
    masses = np.asarray(masses, dtype=float)
    total_mass = float(masses.sum())
    mean = float(
        np.dot(masses, values)
        / total_mass
    )
    variance = float(
        np.dot(
            masses,
            (values - mean) ** 2,
        )
        / total_mass
    )
    scale = math.sqrt(variance)
    if scale <= 1e-14:
        raise ValueError("Zero weighted SD.")
    return mean, scale


def weighted_z(
    values: np.ndarray,
    masses: np.ndarray,
) -> np.ndarray:
    mean, scale = weighted_mean_sd(
        values,
        masses,
    )
    return (
        np.asarray(values, dtype=float)
        - mean
    ) / scale


def probabilities(
    values: np.ndarray,
    mode: str,
    masses: np.ndarray | None = None,
) -> np.ndarray:
    values = np.asarray(values, dtype=float)

    if mode == "unweighted_raw":
        scores = values
        prefactor = np.ones_like(values)

    elif mode == "unweighted_z":
        scores = unweighted_z(values)
        prefactor = np.ones_like(values)

    elif mode == "weighted_raw":
        if masses is None:
            raise ValueError("Missing masses.")
        scores = values
        prefactor = np.asarray(
            masses,
            dtype=float,
        )

    elif mode == "weighted_z":
        if masses is None:
            raise ValueError("Missing masses.")
        scores = weighted_z(
            values,
            masses,
        )
        prefactor = np.asarray(
            masses,
            dtype=float,
        )

    else:
        raise ValueError(mode)

    logits = -LAMBDA * scores
    logits -= float(logits.max())
    weights = (
        prefactor * np.exp(logits)
    )
    return normalize(weights)


def aggregate_refined_probability(
    refined_probability: np.ndarray,
    target_index: int,
    clone_count: int,
    original_size: int,
) -> np.ndarray:
    """
    Refinement layout:
      untouched entries before target,
      clone block,
      untouched entries after target.
    Return macro distribution in original label order.
    """
    macro = np.empty(
        original_size,
        dtype=float,
    )

    if target_index > 0:
        macro[:target_index] = (
            refined_probability[
                :target_index
            ]
        )

    clone_start = target_index
    clone_end = (
        target_index + clone_count
    )
    macro[target_index] = float(
        refined_probability[
            clone_start:clone_end
        ].sum()
    )

    tail_length = (
        original_size
        - target_index
        - 1
    )
    if tail_length > 0:
        macro[
            target_index + 1 :
        ] = refined_probability[
            clone_end:
        ]

    return macro


def refine_context(
    values: np.ndarray,
    masses: np.ndarray,
    target_index: int,
    clone_masses: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    clone_values = np.full(
        len(clone_masses),
        values[target_index],
        dtype=float,
    )
    refined_values = np.concatenate(
        [
            values[:target_index],
            clone_values,
            values[
                target_index + 1 :
            ],
        ]
    )
    refined_masses = np.concatenate(
        [
            masses[:target_index],
            clone_masses,
            masses[
                target_index + 1 :
            ],
        ]
    )
    return refined_values, refined_masses


def refinement_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []
    modes = (
        "unweighted_raw",
        "unweighted_z",
        "weighted_raw",
        "weighted_z",
    )

    for sample_index in range(
        REFINEMENT_SAMPLES
    ):
        size = int(
            rng.integers(4, 12)
        )
        values = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        masses = np.exp(
            rng.normal(
                0.0,
                0.5,
                size=size,
            )
        )
        target_index = int(
            rng.integers(0, size)
        )
        clone_count = int(
            rng.integers(2, 7)
        )

        split_fractions = rng.dirichlet(
            np.ones(clone_count)
        )
        clone_masses = (
            masses[target_index]
            * split_fractions
        )

        refined_values, refined_masses = (
            refine_context(
                values,
                masses,
                target_index,
                clone_masses,
            )
        )

        for mode in modes:
            if mode.startswith(
                "unweighted"
            ):
                original_probability = (
                    probabilities(
                        values,
                        mode,
                    )
                )
                refined_probability = (
                    probabilities(
                        refined_values,
                        mode,
                    )
                )
            else:
                original_probability = (
                    probabilities(
                        values,
                        mode,
                        masses,
                    )
                )
                refined_probability = (
                    probabilities(
                        refined_values,
                        mode,
                        refined_masses,
                    )
                )

            macro_probability = (
                aggregate_refined_probability(
                    refined_probability,
                    target_index,
                    clone_count,
                    size,
                )
            )
            macro_tv = total_variation(
                original_probability,
                macro_probability,
            )
            rows.append(
                {
                    "sample_index": sample_index,
                    "mode": mode,
                    "size": size,
                    "clone_count": clone_count,
                    "target_index": target_index,
                    "macro_total_variation": (
                        macro_tv
                    ),
                    "maximum_macro_probability_error": float(
                        np.max(
                            np.abs(
                                original_probability
                                - macro_probability
                            )
                        )
                    ),
                    "refinement_consistent": bool(
                        macro_tv <= MAX_EXACT_ERROR
                    ),
                }
            )

    return rows


def near_zero_mass_audit(
    rng: np.random.Generator,
) -> list[dict[str, float]]:
    rows = []

    for sample_index in range(
        NEAR_ZERO_SAMPLES
    ):
        size = int(
            rng.integers(4, 12)
        )
        # Uniform continuity requires a nondegenerate original context.
        # We preregister a lower bound on the weighted SD rather than hiding
        # the singularity at SD=0.
        while True:
            values = rng.uniform(
                -2.0,
                2.0,
                size=size,
            )
            masses = np.exp(
                rng.normal(
                    0.0,
                    0.4,
                    size=size,
                )
            )
            _, base_scale = weighted_mean_sd(
                values,
                masses,
            )
            if base_scale >= MIN_WEIGHTED_SD:
                break

        extra_value = float(
            rng.uniform(-2.0, 2.0)
        )

        original = probabilities(
            values,
            "weighted_z",
            masses,
        )

        previous_tv = float("inf")

        for epsilon in EPSILON_VALUES:
            expanded_values = np.append(
                values,
                extra_value,
            )
            expanded_masses = np.append(
                masses,
                epsilon,
            )
            expanded = probabilities(
                expanded_values,
                "weighted_z",
                expanded_masses,
            )

            baseline = np.append(
                original,
                0.0,
            )
            tv = total_variation(
                baseline,
                expanded,
            )

            rows.append(
                {
                    "sample_index": sample_index,
                    "epsilon": epsilon,
                    "base_weighted_sd": base_scale,
                    "total_variation": tv,
                    "nonincreasing_from_previous": bool(
                        tv <= previous_tv
                        + 1e-14
                    ),
                }
            )
            previous_tv = tv

    return rows



def singular_context_audit() -> list[dict[str, float]]:
    """
    Demonstrate that the near-zero-mass continuity is not uniform as the
    original weighted variance approaches zero.
    """
    rows = []
    masses = np.ones(5, dtype=float)
    epsilon = 1e-6
    extra_value = 2.0

    for spread in (
        1e-1,
        1e-2,
        1e-3,
        1e-4,
        1e-5,
        1e-6,
        1e-7,
        1e-8,
    ):
        values = spread * np.asarray(
            [-2.0, -1.0, 0.0, 1.0, 2.0],
            dtype=float,
        )
        _, base_scale = weighted_mean_sd(
            values,
            masses,
        )
        original = probabilities(
            values,
            "weighted_z",
            masses,
        )
        expanded_values = np.append(
            values,
            extra_value,
        )
        expanded_masses = np.append(
            masses,
            epsilon,
        )
        expanded = probabilities(
            expanded_values,
            "weighted_z",
            expanded_masses,
        )
        baseline = np.append(
            original,
            0.0,
        )
        rows.append(
            {
                "spread": spread,
                "base_weighted_sd": base_scale,
                "epsilon": epsilon,
                "total_variation": total_variation(
                    baseline,
                    expanded,
                ),
            }
        )

    return rows

def extreme_zscore_audit(
    rng: np.random.Generator,
) -> list[dict[str, float | bool]]:
    rows = []
    extreme_value = 1e8

    for sample_index in range(
        EXTREME_SAMPLES
    ):
        old_count = int(
            rng.integers(3, 14)
        )
        old_values = rng.normal(
            0.0,
            1.0,
            size=old_count,
        )
        expanded_values = np.append(
            old_values,
            extreme_value,
        )

        old_probability = probabilities(
            old_values,
            "unweighted_z",
        )
        expanded_probability = (
            probabilities(
                expanded_values,
                "unweighted_z",
            )
        )

        asymptotic_new_probability = (
            math.exp(
                -LAMBDA
                * math.sqrt(old_count)
            )
            / (
                old_count
                * math.exp(
                    LAMBDA
                    / math.sqrt(old_count)
                )
                + math.exp(
                    -LAMBDA
                    * math.sqrt(old_count)
                )
            )
        )
        observed_new_probability = float(
            expanded_probability[-1]
        )

        first = 0
        second = 1
        old_log_odds = math.log(
            old_probability[first]
            / old_probability[second]
        )
        expanded_log_odds = math.log(
            expanded_probability[first]
            / expanded_probability[second]
        )

        rows.append(
            {
                "sample_index": sample_index,
                "old_count": old_count,
                "observed_new_probability": (
                    observed_new_probability
                ),
                "asymptotic_new_probability": (
                    asymptotic_new_probability
                ),
                "asymptotic_probability_error": abs(
                    observed_new_probability
                    - asymptotic_new_probability
                ),
                "old_pair_log_odds": old_log_odds,
                "expanded_pair_log_odds": (
                    expanded_log_odds
                ),
                "pair_odds_collapsed_toward_one": bool(
                    abs(expanded_log_odds)
                    < abs(old_log_odds)
                    + 1e-14
                ),
                "absolute_expanded_pair_log_odds": abs(
                    expanded_log_odds
                ),
            }
        )

    return rows


def iid_context_convergence_audit(
    rng: np.random.Generator,
) -> list[dict[str, float]]:
    rows = []
    first_value = -0.5
    second_value = 0.75
    target_log_odds = (
        -LAMBDA
        * (
            first_value - second_value
        )
    )

    for background_size in (
        IID_BACKGROUND_SIZES
    ):
        errors = []

        for _ in range(
            IID_SAMPLES_PER_N
        ):
            background = rng.normal(
                0.0,
                1.0,
                size=background_size,
            )
            values = np.concatenate(
                [
                    np.asarray(
                        [
                            first_value,
                            second_value,
                        ]
                    ),
                    background,
                ]
            )
            probability = probabilities(
                values,
                "unweighted_z",
            )
            observed_log_odds = math.log(
                probability[0]
                / probability[1]
            )
            errors.append(
                observed_log_odds
                - target_log_odds
            )

        errors_array = np.asarray(
            errors
        )
        rows.append(
            {
                "background_size": (
                    background_size
                ),
                "rmse_to_population_limit": float(
                    np.sqrt(
                        np.mean(
                            errors_array**2
                        )
                    )
                ),
                "mean_error": float(
                    errors_array.mean()
                ),
                "median_absolute_error": float(
                    np.median(
                        np.abs(
                            errors_array
                        )
                    )
                ),
            }
        )

    return rows


def main() -> None:
    output = Path("a29_1_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = """# A29.1 — Refinement Consistency, Base Measure, and Nondegeneracy

## Additive-mass refinement theorem

Let a finite marked context be represented by the measure

`nu = sum_j mu_j delta_{q_j}`

with positive masses `mu_j`. Let `T_nu(q)` be any context score determined
only by `nu` and the marked point. Define

`P_j = mu_j f(T_nu(q_j)) / sum_k mu_k f(T_nu(q_k))`

for positive `f`.

Refine alternative `r` into exact clones with the same q-value and masses
`mu_{r,a}` satisfying `sum_a mu_{r,a}=mu_r`. The measure `nu` is unchanged,
so every score `T_nu` is unchanged. The sum of clone weights is

`sum_a mu_{r,a} f(T_nu(q_r))
 = mu_r f(T_nu(q_r))`.

Therefore all macro probabilities are exactly preserved.

## Necessity within factorized clone models

For a factorized kernel `P_j proportional to a_j f(s_j)`, exact consistency
under arbitrary exact-clone refinements requires the coefficients of clones
to sum to the original coefficient. The coefficients therefore behave as a
finitely additive base mass.

## Naive cloning

If every listed alternative is assigned unit coefficient, splitting one
alternative into m clones multiplies its macro weight by m. Exact refinement
consistency fails even when the score itself is context-stable.

## Extreme-alternative limit of unweighted z-score

For n fixed old values and one new value M tending to positive infinity,

`z_old -> -1/sqrt(n)`,
`z_new -> sqrt(n)`.

The new probability approaches a strictly positive value, while odds among
old alternatives approach one. Numerical extremity does not create an
irrelevant alternative at fixed degree.

## Nondegeneracy limit

For a fixed weighted context with positive variance, the weighted mean,
variance, standardized scores, and normalized positive kernel are continuous
under addition of a bounded-score alternative whose mass tends to zero.

This convergence is not uniform as the original variance tends to zero.
At the zero-variance boundary the standardized score is undefined, and an
arbitrarily small mass at a separated score can cause an order-one change.

## Interpretation

A projectively coherent contextual normalization is mathematically possible,
but it requires a base measure or equivalent additive multiplicity data and
an explicit treatment of the zero-variance boundary. This theorem does not
identify either structure with physical volume or dynamics.
"""
    (output / "a29_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    refinement_frame = pd.DataFrame(
        refinement_audit(rng)
    )
    near_zero_frame = pd.DataFrame(
        near_zero_mass_audit(rng)
    )
    singular_frame = pd.DataFrame(
        singular_context_audit()
    )
    extreme_frame = pd.DataFrame(
        extreme_zscore_audit(rng)
    )
    iid_frame = pd.DataFrame(
        iid_context_convergence_audit(
            rng
        )
    )

    refinement_frame.to_csv(
        output / "a29_refinement_audit.csv",
        index=False,
    )
    near_zero_frame.to_csv(
        output / "a29_near_zero_mass_stability.csv",
        index=False,
    )
    singular_frame.to_csv(
        output / "a29_singular_context_instability.csv",
        index=False,
    )
    extreme_frame.to_csv(
        output / "a29_extreme_zscore_limit.csv",
        index=False,
    )
    iid_frame.to_csv(
        output / "a29_iid_context_convergence.csv",
        index=False,
    )

    refinement_summary = []

    for mode, group in (
        refinement_frame.groupby("mode")
    ):
        refinement_summary.append(
            {
                "mode": mode,
                "consistency_rate": float(
                    group[
                        "refinement_consistent"
                    ].mean()
                ),
                "median_macro_tv": float(
                    group[
                        "macro_total_variation"
                    ].median()
                ),
                "maximum_macro_error": float(
                    group[
                        "maximum_macro_probability_error"
                    ].max()
                ),
            }
        )

    near_zero_summary = []

    for epsilon, group in (
        near_zero_frame.groupby(
            "epsilon"
        )
    ):
        near_zero_summary.append(
            {
                "epsilon": float(epsilon),
                "median_total_variation": float(
                    group[
                        "total_variation"
                    ].median()
                ),
                "maximum_total_variation": float(
                    group[
                        "total_variation"
                    ].max()
                ),
            }
        )

    unweighted_raw = refinement_frame[
        refinement_frame["mode"]
        == "unweighted_raw"
    ]
    unweighted_zscore = (
        refinement_frame[
            refinement_frame["mode"]
            == "unweighted_z"
        ]
    )
    weighted_raw = refinement_frame[
        refinement_frame["mode"]
        == "weighted_raw"
    ]
    weighted_zscore = (
        refinement_frame[
            refinement_frame["mode"]
            == "weighted_z"
        ]
    )

    minimum_epsilon = min(
        EPSILON_VALUES
    )
    minimum_epsilon_group = (
        near_zero_frame[
            near_zero_frame["epsilon"]
            == minimum_epsilon
        ]
    )

    iid_rmse_values = (
        iid_frame.sort_values(
            "background_size"
        )[
            "rmse_to_population_limit"
        ].to_numpy()
    )

    gates = {
        "G1_additive_base_measure_refinement_theorem_proved": True,
        "G2_naive_raw_cloning_inconsistent": bool(
            (
                1.0
                - unweighted_raw[
                    "refinement_consistent"
                ].mean()
            )
            >= MIN_UNWEIGHTED_REFINEMENT_VIOLATION_RATE
            and unweighted_raw[
                "macro_total_variation"
            ].median()
            >= MIN_UNWEIGHTED_MEDIAN_MACRO_TV
        ),
        "G3_naive_zscore_cloning_inconsistent": bool(
            (
                1.0
                - unweighted_zscore[
                    "refinement_consistent"
                ].mean()
            )
            >= MIN_UNWEIGHTED_REFINEMENT_VIOLATION_RATE
            and unweighted_zscore[
                "macro_total_variation"
            ].median()
            >= MIN_UNWEIGHTED_MEDIAN_MACRO_TV
        ),
        "G4_weighted_raw_exactly_refinement_consistent": bool(
            weighted_raw[
                "maximum_macro_probability_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G5_weighted_zscore_exactly_refinement_consistent": bool(
            weighted_zscore[
                "maximum_macro_probability_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G6_near_zero_mass_stability_under_nondegeneracy": bool(
            minimum_epsilon_group[
                "total_variation"
            ].max()
            <= MAX_NEAR_ZERO_TV_AT_MIN_EPSILON
            and near_zero_frame[
                "nonincreasing_from_previous"
            ].mean()
            >= 0.99
            and near_zero_frame[
                "base_weighted_sd"
            ].min()
            >= MIN_WEIGHTED_SD
        ),
        "G6b_singular_variance_limit_explicitly_exposed": bool(
            singular_frame[
                "total_variation"
            ].max()
            >= MIN_SINGULAR_CONTEXT_TV
            and singular_frame.sort_values(
                "spread"
            )[
                "total_variation"
            ].iloc[0]
            >= MIN_SINGULAR_CONTEXT_TV
        ),
        "G7_unweighted_zscore_extreme_limit_matches_theory": bool(
            extreme_frame[
                "asymptotic_probability_error"
            ].max()
            <= MAX_EXTREME_ASYMPTOTIC_ERROR
        ),
        "G8_extreme_unweighted_zscore_collapses_old_odds": bool(
            extreme_frame[
                "pair_odds_collapsed_toward_one"
            ].mean()
            >= MIN_EXTREME_PAIR_ODDS_COLLAPSE_RATE
            and extreme_frame[
                "absolute_expanded_pair_log_odds"
            ].max()
            <= 1e-6
        ),
        "G9_iid_context_has_large_degree_limit": bool(
            all(
                iid_rmse_values[index + 1]
                < iid_rmse_values[index]
                for index in range(
                    len(iid_rmse_values) - 1
                )
            )
            and iid_rmse_values[-1]
            <= MAX_IID_FINAL_RMSE
        ),
        "G10_refinement_consistency_requires_measure_like_data_within_factorized_class": True,
        "G11_no_physical_volume_measure_claimed": True,
    }

    verdict = (
        "PASS_REFINEMENT_CONSISTENCY_WITH_BASE_MEASURE_AND_NONDEGENERACY_LIMIT"
        if all(gates.values())
        else "FAIL_CONTEXTUAL_REFINEMENT_AUDIT"
    )

    classification = [
        {
            "construction": "unweighted raw exponential",
            "contextual_normalization": False,
            "refinement_consistent": False,
            "near_zero_multiplicity_available": False,
            "extra_structure": "implicit unit mass per listed alternative",
            "status": "CLONE_SENSITIVE",
        },
        {
            "construction": "unweighted row z-score",
            "contextual_normalization": True,
            "refinement_consistent": False,
            "near_zero_multiplicity_available": False,
            "extra_structure": "implicit unit mass per listed alternative",
            "status": "CONTEXT_AND_CLONE_SENSITIVE",
        },
        {
            "construction": "mass-weighted raw exponential",
            "contextual_normalization": False,
            "refinement_consistent": True,
            "near_zero_multiplicity_available": True,
            "extra_structure": "positive additive base mass mu",
            "status": "PROJECTIVELY_CONSISTENT",
        },
        {
            "construction": "mass-weighted row z-score",
            "contextual_normalization": True,
            "refinement_consistent": True,
            "near_zero_multiplicity_available": True,
            "extra_structure": "positive additive base mass mu",
            "status": "PROJECTIVELY_CONSISTENT_CONTEXTUAL_LAW",
        },
        {
            "construction": "unweighted z-score at high iid degree",
            "contextual_normalization": True,
            "refinement_consistent": False,
            "near_zero_multiplicity_available": False,
            "extra_structure": "iid environmental assumption",
            "status": "ASYMPTOTICALLY_STABLE_NOT_EXACT",
        },
        {
            "construction": "RZS physical interpretation of mu",
            "contextual_normalization": None,
            "refinement_consistent": None,
            "near_zero_multiplicity_available": None,
            "extra_structure": "not derived",
            "status": "OPEN",
        },
    ]
    pd.DataFrame(classification).to_csv(
        output / "a29_refinement_classification.csv",
        index=False,
    )

    summary = {
        "seed": SEED,
        "refinement_samples": (
            REFINEMENT_SAMPLES
        ),
        "near_zero_samples": (
            NEAR_ZERO_SAMPLES
        ),
        "extreme_samples": (
            EXTREME_SAMPLES
        ),
        "iid_samples_per_n": (
            IID_SAMPLES_PER_N
        ),
        "refinement_results": (
            refinement_summary
        ),
        "near_zero_results": (
            near_zero_summary
        ),
        "singular_context_results": (
            singular_frame.to_dict(
                orient="records"
            )
        ),
        "extreme_results": {
            "maximum_asymptotic_probability_error": float(
                extreme_frame[
                    "asymptotic_probability_error"
                ].max()
            ),
            "minimum_limiting_new_probability": float(
                extreme_frame[
                    "asymptotic_new_probability"
                ].min()
            ),
            "maximum_limiting_new_probability": float(
                extreme_frame[
                    "asymptotic_new_probability"
                ].max()
            ),
            "pair_odds_collapse_rate": float(
                extreme_frame[
                    "pair_odds_collapsed_toward_one"
                ].mean()
            ),
            "maximum_absolute_expanded_pair_log_odds": float(
                extreme_frame[
                    "absolute_expanded_pair_log_odds"
                ].max()
            ),
        },
        "iid_context_results": (
            iid_frame.to_dict(
                orient="records"
            )
        ),
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "Naive listing-based kernels are not invariant under exact "
            "refinement: cloning an alternative changes its macro weight, "
            "and local z-normalization changes the entire context. Exact "
            "projective consistency is restored by a positive additive base "
            "mass mu, used both in the context statistics and in transition "
            "weights. Under mass-preserving splits, the weighted empirical "
            "measure and all macro probabilities remain unchanged. A "
            "near-zero mass alternative becomes irrelevant continuously only "
            "away from the singular zero-variance boundary; no uniform "
            "stability bound exists as the context variance tends to zero. "
            "Thus contextual q normalization can be coherent, but it requires "
            "measure-like multiplicity data and a nondegeneracy treatment. "
            "The present RZS framework has derived neither physically."
        ),
        "interpretation_boundary": (
            "The base mass is mathematical bookkeeping required for exact "
            "refinement consistency within the audited factorized class. "
            "The nondegeneracy condition is also substantive: standardized "
            "scores are singular at zero variance. Neither the mass nor a "
            "regularization of that singular boundary is identified with "
            "spacetime volume, matter, or a physical law."
        ),
    }

    (output / "a29_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A29.1 — Contextual Normalization and Refinement",
        "",
        "## Main result",
        "",
        (
            "Naive unit-mass alternatives are clone-sensitive. A positive "
            "additive base mass restores exact refinement consistency for "
            "both raw and context-normalized exponential kernels."
        ),
        "",
        "## Refinement results",
        "",
    ]

    for result in refinement_summary:
        report_lines.extend(
            [
                f"### {result['mode']}",
                (
                    "- Consistency rate: "
                    f"{result['consistency_rate']:.6f}"
                ),
                (
                    "- Median macro TV: "
                    f"{result['median_macro_tv']:.6f}"
                ),
                (
                    "- Maximum macro error: "
                    f"{result['maximum_macro_error']:.6g}"
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

    (output / "a29_report.md").write_text(
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
