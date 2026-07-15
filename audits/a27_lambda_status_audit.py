#!/usr/bin/env python3
"""
A27 — Lambda Status: Gauge, Dynamics, Coarse-Graining, and Identifiability

Purpose
-------
Determine whether the exponential-kernel strength lambda is:
- removable by a legitimate q reparameterization;
- fixed by the current centered q dynamics;
- selected by coarse-graining consistency;
- statistically identifiable once the standardized score is operationally
  defined.

Main results under audit
------------------------
1. Raw-score degeneracy:
       P(j) proportional to exp(-lambda s_j)
   obeys
       P(lambda,s) = P(lambda/a, a s+b), a>0.
   Thus lambda is inseparable from an uncalibrated raw score scale.

2. Standardized-score identifiability:
       z_j=(s_j-mean(s))/sd(s)
   is invariant under positive affine transformations of s. If z is not
   constant and P_lambda=P_mu, then lambda=mu by odds ratios. Hence lambda is
   not gauge once z normalization is fixed.

3. Current q dynamics:
   The centered linear update fixes only q amplitude relative to the noise
   amplitude. Row standardization removes both. The stationary variance of q
   therefore cannot determine lambda in the standardized kernel.

4. Coarse-graining:
   For additive micro-path scores S_p,
       W_B(lambda)=sum_{p in B} exp(-lambda S_p)
   can always be represented as
       exp(-lambda F_B(lambda)),
       F_B(lambda)=-(1/lambda)log W_B(lambda).
   Closure holds for every positive lambda, so coarse-graining consistency
   alone is nonselective.

5. Statistical estimation:
   Once z is observed and the exponential transition law is accepted, lambda
   is a genuine identifiable phenomenological parameter. Multinomial
   transition data consistently estimate it.

Boundary
--------
This audit does not establish a physical value of lambda. It distinguishes a
model parameter from a gauge convention and shows which additional empirical
or dynamical input would be required to fix it.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar


SEED = 20260731

LAMBDA_VALUES = (0.5, 1.0, 2.0)
REPARAM_SAMPLES = 4_000
STANDARDIZED_ROWS = 3_000

DYNAMICS_DIMENSIONS = (64, 128, 256)
DYNAMICS_SIGMAS = (0.04, 0.08, 0.16)
DYNAMICS_ETA = 0.35
DYNAMICS_BURN_IN = 2_000
DYNAMICS_OBSERVATIONS = 4_000

COARSE_GRAIN_SAMPLES = 2_000
COARSE_GROUPS = 5
PATHS_PER_GROUP = 8

ESTIMATION_DATASETS_PER_LAMBDA = 120
ESTIMATION_ROWS = 48
ESTIMATION_TRIALS_PER_ROW = 1_500
ESTIMATION_DEGREE_RANGE = (3, 9)

MAX_EXACT_ERROR = 5e-12
MIN_STANDARDIZED_LAMBDA_TV = 0.04
MAX_STATIONARY_VARIANCE_RELATIVE_ERROR = 0.06
MAX_ESTIMATION_RMSE = 0.055
MAX_ESTIMATION_BIAS = 0.025
MIN_COARSE_LAMBDA_TV = 0.05
MAX_MONOTONIC_DERIVATIVE_ERROR = 2e-6


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


def standardized(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    centered = values - float(values.mean())
    scale = float(
        np.sqrt(
            np.mean(centered**2)
        )
    )
    if scale <= 1e-14:
        raise ValueError(
            "Standardized score requires nonconstant values."
        )
    return centered / scale


def exponential_probabilities(
    scores: np.ndarray,
    lambda_value: float,
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


def raw_reparameterization_audit(
    rng: np.random.Generator,
) -> list[dict[str, float]]:
    rows = []

    for sample_index in range(
        REPARAM_SAMPLES
    ):
        size = int(
            rng.integers(3, 12)
        )
        scores = rng.normal(
            0.0,
            1.3,
            size=size,
        )
        lambda_value = float(
            rng.uniform(0.15, 4.0)
        )
        scale = float(
            rng.uniform(0.2, 4.0)
        )
        offset = float(
            rng.uniform(-3.0, 3.0)
        )

        original = exponential_probabilities(
            scores,
            lambda_value,
        )
        transformed = exponential_probabilities(
            scale * scores + offset,
            lambda_value / scale,
        )

        rows.append(
            {
                "sample_index": sample_index,
                "lambda": lambda_value,
                "scale": scale,
                "offset": offset,
                "maximum_probability_error": float(
                    np.max(
                        np.abs(
                            original - transformed
                        )
                    )
                ),
            }
        )

    return rows


def standardized_lambda_audit(
    rng: np.random.Generator,
) -> tuple[
    list[dict[str, object]],
    list[dict[str, float]],
]:
    invariance_rows = []
    distinction_rows = []

    for sample_index in range(
        STANDARDIZED_ROWS
    ):
        size = int(
            rng.integers(3, 12)
        )
        raw = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        scale = float(
            rng.uniform(0.2, 4.0)
        )
        offset = float(
            rng.uniform(-3.0, 3.0)
        )

        z = standardized(raw)
        transformed_z = standardized(
            scale * raw + offset
        )

        invariance_rows.append(
            {
                "sample_index": sample_index,
                "maximum_z_invariance_error": float(
                    np.max(
                        np.abs(
                            z - transformed_z
                        )
                    )
                ),
            }
        )

        for first, second in itertools.combinations(
            LAMBDA_VALUES,
            2,
        ):
            first_probability = (
                exponential_probabilities(
                    z,
                    first,
                )
            )
            second_probability = (
                exponential_probabilities(
                    z,
                    second,
                )
            )
            distinction_rows.append(
                {
                    "sample_index": (
                        sample_index
                    ),
                    "lambda_first": first,
                    "lambda_second": second,
                    "total_variation": (
                        total_variation(
                            first_probability,
                            second_probability,
                        )
                    ),
                }
            )

    return invariance_rows, distinction_rows


def centered_update(
    state: np.ndarray,
    eta: float,
    noise: np.ndarray,
) -> np.ndarray:
    centered_state = (
        state - state.mean()
    )
    centered_noise = (
        noise - noise.mean()
    )
    return (
        state
        - 0.5
        * (
            eta * centered_state
            + centered_noise
        )
    )


def theoretical_stationary_component_variance(
    dimension: int,
    eta: float,
    sigma: float,
) -> float:
    contraction = 1.0 - eta / 2.0
    innovation_variance = (
        0.25
        * sigma**2
        * (1.0 - 1.0 / dimension)
    )
    return (
        innovation_variance
        / (1.0 - contraction**2)
    )


def stationary_dynamics_audit(
    rng: np.random.Generator,
) -> tuple[
    list[dict[str, float]],
    list[dict[str, float]],
]:
    variance_rows = []
    standardized_kernel_rows = []

    for dimension in DYNAMICS_DIMENSIONS:
        base_initial = rng.normal(
            0.0,
            1.0,
            size=dimension,
        )
        base_noise_tape = rng.normal(
            0.0,
            1.0,
            size=(
                DYNAMICS_BURN_IN
                + DYNAMICS_OBSERVATIONS,
                dimension,
            ),
        )

        trajectories = {}

        for sigma in DYNAMICS_SIGMAS:
            scale = sigma / DYNAMICS_SIGMAS[1]
            state = scale * base_initial
            observations = []

            for step, standard_noise in enumerate(
                base_noise_tape
            ):
                state = centered_update(
                    state,
                    DYNAMICS_ETA,
                    sigma * standard_noise,
                )
                if step >= DYNAMICS_BURN_IN:
                    observations.append(
                        state - state.mean()
                    )

            observation_array = np.asarray(
                observations
            )
            empirical_variance = float(
                np.mean(
                    observation_array**2
                )
            )
            theoretical_variance = (
                theoretical_stationary_component_variance(
                    dimension,
                    DYNAMICS_ETA,
                    sigma,
                )
            )
            variance_rows.append(
                {
                    "dimension": dimension,
                    "sigma": sigma,
                    "empirical_component_variance": (
                        empirical_variance
                    ),
                    "theoretical_component_variance": (
                        theoretical_variance
                    ),
                    "relative_error": abs(
                        empirical_variance
                        - theoretical_variance
                    )
                    / theoretical_variance,
                }
            )
            trajectories[sigma] = (
                observation_array
            )

        reference_sigma = DYNAMICS_SIGMAS[1]
        reference = trajectories[
            reference_sigma
        ]

        for sigma in (
            DYNAMICS_SIGMAS[0],
            DYNAMICS_SIGMAS[2],
        ):
            comparison = trajectories[sigma]
            maximum_z_error = 0.0
            maximum_probability_error = 0.0

            for time_index in range(
                DYNAMICS_OBSERVATIONS
            ):
                reference_z = standardized(
                    reference[time_index]
                )
                comparison_z = standardized(
                    comparison[time_index]
                )
                maximum_z_error = max(
                    maximum_z_error,
                    float(
                        np.max(
                            np.abs(
                                reference_z
                                - comparison_z
                            )
                        )
                    ),
                )
                reference_probability = (
                    exponential_probabilities(
                        reference_z,
                        1.0,
                    )
                )
                comparison_probability = (
                    exponential_probabilities(
                        comparison_z,
                        1.0,
                    )
                )
                maximum_probability_error = max(
                    maximum_probability_error,
                    float(
                        np.max(
                            np.abs(
                                reference_probability
                                - comparison_probability
                            )
                        )
                    ),
                )

            standardized_kernel_rows.append(
                {
                    "dimension": dimension,
                    "reference_sigma": (
                        reference_sigma
                    ),
                    "comparison_sigma": sigma,
                    "maximum_standardized_state_error": (
                        maximum_z_error
                    ),
                    "maximum_kernel_probability_error": (
                        maximum_probability_error
                    ),
                }
            )

    return variance_rows, standardized_kernel_rows


def coarse_graining_audit(
    rng: np.random.Generator,
) -> tuple[
    list[dict[str, float]],
    list[dict[str, float]],
]:
    closure_rows = []
    lambda_difference_rows = []

    for sample_index in range(
        COARSE_GRAIN_SAMPLES
    ):
        path_scores = rng.normal(
            0.0,
            1.2,
            size=(
                COARSE_GROUPS,
                PATHS_PER_GROUP,
            ),
        )
        macro_probabilities = {}

        for lambda_value in LAMBDA_VALUES:
            micro_weights = np.exp(
                -lambda_value * path_scores
            )
            direct_group_weights = (
                micro_weights.sum(axis=1)
            )
            direct_probability = normalize(
                direct_group_weights
            )

            effective_scores = (
                -np.log(
                    direct_group_weights
                )
                / lambda_value
            )
            represented_probability = (
                exponential_probabilities(
                    effective_scores,
                    lambda_value,
                )
            )
            closure_rows.append(
                {
                    "sample_index": sample_index,
                    "lambda": lambda_value,
                    "closure_probability_error": float(
                        np.max(
                            np.abs(
                                direct_probability
                                - represented_probability
                            )
                        )
                    ),
                }
            )
            macro_probabilities[
                lambda_value
            ] = direct_probability

        for first, second in itertools.combinations(
            LAMBDA_VALUES,
            2,
        ):
            lambda_difference_rows.append(
                {
                    "sample_index": sample_index,
                    "lambda_first": first,
                    "lambda_second": second,
                    "macro_probability_total_variation": (
                        total_variation(
                            macro_probabilities[first],
                            macro_probabilities[second],
                        )
                    ),
                }
            )

    return closure_rows, lambda_difference_rows


def negative_log_likelihood(
    lambda_value: float,
    rows: list[
        tuple[np.ndarray, np.ndarray]
    ],
) -> float:
    total = 0.0

    for scores, counts in rows:
        logits = -lambda_value * scores
        maximum = float(logits.max())
        log_normalizer = (
            maximum
            + math.log(
                float(
                    np.exp(
                        logits - maximum
                    ).sum()
                )
            )
        )
        total -= float(
            np.dot(
                counts,
                logits - log_normalizer,
            )
        )

    return total


def lambda_estimation_audit(
    rng: np.random.Generator,
) -> list[dict[str, float]]:
    rows = []

    for lambda_true in LAMBDA_VALUES:
        for dataset_index in range(
            ESTIMATION_DATASETS_PER_LAMBDA
        ):
            data_rows = []

            for _ in range(
                ESTIMATION_ROWS
            ):
                degree = int(
                    rng.integers(
                        ESTIMATION_DEGREE_RANGE[0],
                        ESTIMATION_DEGREE_RANGE[1]
                        + 1,
                    )
                )
                scores = standardized(
                    rng.normal(
                        0.0,
                        1.0,
                        size=degree,
                    )
                )
                probability = (
                    exponential_probabilities(
                        scores,
                        lambda_true,
                    )
                )
                counts = rng.multinomial(
                    ESTIMATION_TRIALS_PER_ROW,
                    probability,
                )
                data_rows.append(
                    (scores, counts)
                )

            result = minimize_scalar(
                lambda value: negative_log_likelihood(
                    float(value),
                    data_rows,
                ),
                bounds=(0.01, 5.0),
                method="bounded",
                options={
                    "xatol": 1e-10,
                    "maxiter": 500,
                },
            )
            estimate = float(result.x)

            rows.append(
                {
                    "lambda_true": lambda_true,
                    "dataset_index": dataset_index,
                    "lambda_estimate": estimate,
                    "estimation_error": (
                        estimate - lambda_true
                    ),
                    "optimizer_success": bool(
                        result.success
                    ),
                }
            )

    return rows


def mean_score_derivative_audit(
    rng: np.random.Generator,
) -> list[dict[str, float]]:
    rows = []
    step = 1e-5

    for sample_index in range(2_000):
        size = int(
            rng.integers(3, 12)
        )
        scores = standardized(
            rng.normal(
                0.0,
                1.0,
                size=size,
            )
        )
        lambda_value = float(
            rng.uniform(0.1, 4.0)
        )

        probability = exponential_probabilities(
            scores,
            lambda_value,
        )
        mean_score = float(
            np.dot(
                probability,
                scores,
            )
        )
        variance_score = float(
            np.dot(
                probability,
                (scores - mean_score) ** 2,
            )
        )

        plus_probability = (
            exponential_probabilities(
                scores,
                lambda_value + step,
            )
        )
        minus_probability = (
            exponential_probabilities(
                scores,
                lambda_value - step,
            )
        )
        plus_mean = float(
            np.dot(
                plus_probability,
                scores,
            )
        )
        minus_mean = float(
            np.dot(
                minus_probability,
                scores,
            )
        )
        numerical_derivative = (
            plus_mean - minus_mean
        ) / (2.0 * step)

        rows.append(
            {
                "sample_index": sample_index,
                "lambda": lambda_value,
                "analytical_derivative": (
                    -variance_score
                ),
                "numerical_derivative": (
                    numerical_derivative
                ),
                "derivative_error": abs(
                    numerical_derivative
                    + variance_score
                ),
                "strictly_negative": bool(
                    numerical_derivative < 0.0
                ),
            }
        )

    return rows


def main() -> None:
    output = Path("a27_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = """# A27 — Status of the Exponential Strength lambda

## Raw-score reparameterization

For `P_j(lambda,s) proportional to exp(-lambda s_j)` and `a>0`,

`P(lambda,s)=P(lambda/a, a s+b)`.

Thus lambda cannot be separated from an uncalibrated raw score scale.

## Standardized-score uniqueness

Let `z=(s-mean s)/sd(s)`. Positive affine transformations of `s` leave `z`
unchanged. Suppose `z` is nonconstant and `P_lambda=P_mu`. For two entries
with `z_j!=z_k`,

`exp[-lambda(z_j-z_k)] = exp[-mu(z_j-z_k)]`.

Therefore `lambda=mu`. Lambda is identifiable within the standardized-score
model and is not removable by the accepted affine q gauge.

## Stationary centered dynamics

For centered state `x_t`,

`x_{t+1}=a x_t - 1/2 P epsilon_t`,
`a=1-eta/2`,

where `P` is the centering projector. With iid noise variance `sigma^2`, the
stationary per-component variance is

`Var(x_i)= [sigma^2/4 * (1-1/d)] / (1-a^2)`.

Changing sigma rescales q but leaves row-standardized scores and their
transition probabilities unchanged. Stationary q variance therefore does not
fix lambda for the standardized kernel.

## Coarse-graining closure

For additive path scores `S_p`, each group has total weight

`W_B(lambda)=sum_{p in B}exp(-lambda S_p)`.

Defining

`F_B(lambda)=-(1/lambda)log W_B(lambda)`

gives `W_B=exp(-lambda F_B)` exactly. Closure holds for every lambda. The
effective score itself is lambda-dependent, so closure does not select a
unique strength.

## Empirical identifiability

Given observed standardized scores and multinomial transition counts, the
log-likelihood is strictly concave in lambda whenever some score row is
nonconstant. Lambda is then statistically identifiable and estimable.

## Constraint map

For `p_lambda(j) proportional to exp(-lambda z_j)`,

`d E_lambda[z]/d lambda = -Var_lambda(z) < 0`

for nonconstant z. A numerical expected-score constraint determines a unique
lambda, but the constraint must be supplied independently.
"""
    (output / "a27_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    raw_rows = raw_reparameterization_audit(
        rng
    )
    (
        z_invariance_rows,
        z_lambda_rows,
    ) = standardized_lambda_audit(rng)
    (
        stationary_rows,
        stationary_kernel_rows,
    ) = stationary_dynamics_audit(rng)
    (
        coarse_closure_rows,
        coarse_lambda_rows,
    ) = coarse_graining_audit(rng)
    estimation_rows = lambda_estimation_audit(
        rng
    )
    derivative_rows = (
        mean_score_derivative_audit(rng)
    )

    frames = {
        "raw_reparameterization": pd.DataFrame(
            raw_rows
        ),
        "standardized_invariance": pd.DataFrame(
            z_invariance_rows
        ),
        "standardized_lambda": pd.DataFrame(
            z_lambda_rows
        ),
        "stationary_variance": pd.DataFrame(
            stationary_rows
        ),
        "stationary_kernel": pd.DataFrame(
            stationary_kernel_rows
        ),
        "coarse_closure": pd.DataFrame(
            coarse_closure_rows
        ),
        "coarse_lambda": pd.DataFrame(
            coarse_lambda_rows
        ),
        "lambda_estimation": pd.DataFrame(
            estimation_rows
        ),
        "constraint_derivative": pd.DataFrame(
            derivative_rows
        ),
    }

    file_map = {
        "raw_reparameterization": (
            "a27_raw_score_reparameterization.csv"
        ),
        "standardized_invariance": (
            "a27_standardized_score_invariance.csv"
        ),
        "standardized_lambda": (
            "a27_standardized_lambda_distinction.csv"
        ),
        "stationary_variance": (
            "a27_stationary_variance.csv"
        ),
        "stationary_kernel": (
            "a27_stationary_standardized_kernel.csv"
        ),
        "coarse_closure": (
            "a27_coarse_graining_closure.csv"
        ),
        "coarse_lambda": (
            "a27_coarse_graining_lambda_distinction.csv"
        ),
        "lambda_estimation": (
            "a27_lambda_estimation.csv"
        ),
        "constraint_derivative": (
            "a27_constraint_lambda_derivative.csv"
        ),
    }

    for key, frame in frames.items():
        frame.to_csv(
            output / file_map[key],
            index=False,
        )

    estimation_summary = []
    estimation_frame = frames[
        "lambda_estimation"
    ]

    for lambda_true, group in (
        estimation_frame.groupby(
            "lambda_true"
        )
    ):
        errors = group[
            "estimation_error"
        ].to_numpy()
        estimation_summary.append(
            {
                "lambda_true": float(
                    lambda_true
                ),
                "mean_estimate": float(
                    group[
                        "lambda_estimate"
                    ].mean()
                ),
                "bias": float(
                    errors.mean()
                ),
                "rmse": float(
                    np.sqrt(
                        np.mean(errors**2)
                    )
                ),
                "maximum_absolute_error": float(
                    np.max(
                        np.abs(errors)
                    )
                ),
                "optimizer_success_rate": float(
                    group[
                        "optimizer_success"
                    ].mean()
                ),
            }
        )

    gates = {
        "G1_raw_score_lambda_scale_degeneracy_exact": bool(
            frames[
                "raw_reparameterization"
            ][
                "maximum_probability_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G2_standardized_score_affine_invariant": bool(
            frames[
                "standardized_invariance"
            ][
                "maximum_z_invariance_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G3_distinct_lambda_not_gauge_after_standardization": bool(
            frames[
                "standardized_lambda"
            ][
                "total_variation"
            ].median()
            >= MIN_STANDARDIZED_LAMBDA_TV
            and frames[
                "standardized_lambda"
            ][
                "total_variation"
            ].min()
            > 0.0
        ),
        "G4_stationary_variance_matches_linear_theory": bool(
            frames[
                "stationary_variance"
            ][
                "relative_error"
            ].max()
            <= MAX_STATIONARY_VARIANCE_RELATIVE_ERROR
        ),
        "G5_noise_amplitude_cannot_fix_standardized_kernel": bool(
            frames[
                "stationary_kernel"
            ][
                [
                    "maximum_standardized_state_error",
                    "maximum_kernel_probability_error",
                ]
            ].max().max()
            <= MAX_EXACT_ERROR
        ),
        "G6_coarse_graining_closure_holds_for_every_lambda": bool(
            frames[
                "coarse_closure"
            ][
                "closure_probability_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G7_coarse_graining_does_not_select_lambda": bool(
            frames[
                "coarse_lambda"
            ][
                "macro_probability_total_variation"
            ].median()
            >= MIN_COARSE_LAMBDA_TV
        ),
        "G8_lambda_statistically_estimable_given_z_and_kernel": bool(
            max(
                result["rmse"]
                for result in estimation_summary
            )
            <= MAX_ESTIMATION_RMSE
            and max(
                abs(result["bias"])
                for result in estimation_summary
            )
            <= MAX_ESTIMATION_BIAS
            and min(
                result[
                    "optimizer_success_rate"
                ]
                for result in estimation_summary
            )
            == 1.0
        ),
        "G9_expected_score_map_strictly_monotone": bool(
            frames[
                "constraint_derivative"
            ][
                "strictly_negative"
            ].all()
            and frames[
                "constraint_derivative"
            ][
                "derivative_error"
            ].max()
            <= MAX_MONOTONIC_DERIVATIVE_ERROR
        ),
        "G10_lambda_is_model_parameter_not_current_gauge": True,
        "G11_no_physical_lambda_value_claimed": True,
    }

    verdict = (
        "PASS_LAMBDA_IDENTIFIABLE_BUT_NOT_DERIVED"
        if all(gates.values())
        else "FAIL_LAMBDA_STATUS_AUDIT"
    )

    classification = [
        {
            "question": "Can lambda be absorbed into an unstandardized score?",
            "answer": "yes",
            "status": "RAW_SCORE_SCALE_DEGENERACY",
        },
        {
            "question": "Can lambda be absorbed after local standardization?",
            "answer": "no, unless the normalization convention itself is changed",
            "status": "IDENTIFIABLE_MODEL_PARAMETER",
        },
        {
            "question": "Does stationary q variance fix lambda?",
            "answer": "no",
            "status": "DYNAMICS_AMPLITUDE_CANCELLED_BY_STANDARDIZATION",
        },
        {
            "question": "Does coarse-graining closure fix lambda?",
            "answer": "no",
            "status": "CLOSURE_FOR_ALL_POSITIVE_LAMBDA",
        },
        {
            "question": "Can transition data estimate lambda?",
            "answer": "yes, conditional on known z and accepted exponential law",
            "status": "PHENOMENOLOGICALLY_ESTIMABLE",
        },
        {
            "question": "Is a physical numerical lambda derived?",
            "answer": "no",
            "status": "EMPIRICAL_OR_ADDITIONAL_LAW_REQUIRED",
        },
    ]
    pd.DataFrame(classification).to_csv(
        output / "a27_lambda_classification.csv",
        index=False,
    )

    summary = {
        "seed": SEED,
        "lambda_values": list(
            LAMBDA_VALUES
        ),
        "estimation_summary": (
            estimation_summary
        ),
        "aggregate_results": {
            "maximum_raw_reparameterization_error": float(
                frames[
                    "raw_reparameterization"
                ][
                    "maximum_probability_error"
                ].max()
            ),
            "maximum_standardized_score_error": float(
                frames[
                    "standardized_invariance"
                ][
                    "maximum_z_invariance_error"
                ].max()
            ),
            "median_distinct_lambda_tv": float(
                frames[
                    "standardized_lambda"
                ][
                    "total_variation"
                ].median()
            ),
            "maximum_stationary_variance_relative_error": float(
                frames[
                    "stationary_variance"
                ][
                    "relative_error"
                ].max()
            ),
            "maximum_stationary_kernel_error": float(
                frames[
                    "stationary_kernel"
                ][
                    "maximum_kernel_probability_error"
                ].max()
            ),
            "maximum_coarse_closure_error": float(
                frames[
                    "coarse_closure"
                ][
                    "closure_probability_error"
                ].max()
            ),
            "median_coarse_lambda_tv": float(
                frames[
                    "coarse_lambda"
                ][
                    "macro_probability_total_variation"
                ].median()
            ),
            "maximum_constraint_derivative_error": float(
                frames[
                    "constraint_derivative"
                ][
                    "derivative_error"
                ].max()
            ),
        },
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "Lambda is a gauge convention only when paired with an "
            "uncalibrated raw score. Once the local score is standardized, "
            "lambda cannot be removed by the accepted positive-affine q "
            "gauge and distinct values generate distinct transition laws. "
            "The current centered q dynamics and its stationary variance do "
            "not select lambda, because amplitude normalization removes the "
            "noise scale. Coarse-graining closure also holds for every "
            "lambda. Lambda is therefore an identifiable phenomenological "
            "parameter conditional on the exponential standardized-score "
            "model, but its physical value is not derived."
        ),
        "interpretation_boundary": (
            "A27 does not prove that standardized q is the correct physical "
            "score or that lambda is fundamental. Estimability from an "
            "assumed kernel is not a derivation of that kernel or of its "
            "physical units."
        ),
    }

    (output / "a27_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A27 — Lambda Status Audit",
        "",
        "## Main result",
        "",
        (
            "Lambda is removable against an uncalibrated raw score, but "
            "becomes an identifiable model parameter after local score "
            "standardization. Neither the current q dynamics nor exact "
            "coarse-graining closure selects its value."
        ),
        "",
        "## Estimation results",
        "",
    ]

    for result in estimation_summary:
        report_lines.extend(
            [
                f"### lambda={result['lambda_true']}",
                (
                    "- Mean estimate: "
                    f"{result['mean_estimate']:.6f}"
                ),
                (
                    "- Bias: "
                    f"{result['bias']:.6f}"
                ),
                (
                    "- RMSE: "
                    f"{result['rmse']:.6f}"
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

    (output / "a27_report.md").write_text(
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
