#!/usr/bin/env python3
"""
A26 — Kernel Selection Principles Audit

Purpose
-------
Test whether common structural principles select a unique q-dependent local
transition kernel from the non-circular family exposed in A25.

Candidate pointwise weights
---------------------------
For a local standardized q-score z, consider

    K_f(j | S) = f(z_j) / sum_{k in S} f(z_k),  f>0.

Audited functions:
- exp_0_5:   f(z)=exp(-0.5 z)
- exp_1:     f(z)=exp(-z)
- exp_2:     f(z)=exp(-2 z)
- asinh:     f(z)=exp(-asinh(z))
- logistic:  f(z)=1/(1+exp(z))

A context-dependent rank kernel is included as a control.

Exact results under audit
-------------------------
1. IIA:
   Every pointwise normalized positive f satisfies
       K_f(j|S)/K_f(k|S) = f(z_j)/f(z_k),
   independent of other alternatives. IIA does not select f.

2. Detailed balance:
   On an undirected graph with symmetric edge score s_ij, every symmetric
   positive weight w_ij=f(s_ij) yields a reversible chain with
       pi_i proportional to sum_j w_ij.
   Detailed balance does not select f.

3. Aggregation:
   If a block B is represented by its total weight sum_{j in B} f(z_j),
   aggregation is exact for every f. Aggregation in weight space does not
   select f.

4. Difference-only odds / additive composition:
   If log odds depend only on z_j-z_k, continuously, then
       f(x)/f(y)=g(x-y).
   This implies g(a+b)=g(a)g(b), hence
       f(z)=C exp(-lambda z).
   This selects the exponential family, not lambda.

5. Maximum entropy:
   Maximizing Shannon entropy under normalization and a fixed expected score
       sum p_j z_j = m
   gives
       p_j proportional to exp(-lambda z_j).
   The multiplier lambda is fixed by the externally specified constraint m.
   Different m values produce different lambda values.

Boundary
--------
A pass means that exponential weights have a rigorous axiomatic route, but
the present principles do not derive a unique physical lambda or show that
the required expected-score constraint is an RZS law.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
from scipy.linalg import null_space
from scipy.optimize import brentq


SEED = 20260730

FUNCTIONAL_SAMPLES = 50_000
CHOICE_SET_SAMPLES = 2_000
DETAILED_BALANCE_SAMPLES = 600
MAX_ENTROPY_SAMPLES = 1_000
MAX_ENTROPY_PERTURBATIONS = 80

LAMBDA_VALUES = (0.25, 0.5, 1.0, 2.0, 4.0)

MAX_EXACT_ERROR = 2e-11
MIN_NONEXP_SHIFT_RESIDUAL = 0.01
MIN_NONEXP_COMPOSITION_RESIDUAL = 0.01
MIN_DISTINCT_LAMBDA_TV = 0.05
MIN_CONTEXT_RANK_IIA_VIOLATION_RATE = 0.20
MAX_ENTROPY_LAMBDA_ERROR = 2e-9
MAX_ENTROPY_PROBABILITY_ERROR = 2e-9
MAX_ENTROPY_VIOLATION = 2e-12


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


def stable_normalize(weights: np.ndarray) -> np.ndarray:
    weights = np.asarray(weights, dtype=float)
    if np.any(weights <= 0.0):
        raise ValueError("Weights must be strictly positive.")
    return weights / weights.sum()


def weight_function(
    name: str,
    z: np.ndarray,
) -> np.ndarray:
    z = np.asarray(z, dtype=float)

    if name == "exp_0_5":
        return np.exp(-0.5 * z)
    if name == "exp_1":
        return np.exp(-z)
    if name == "exp_2":
        return np.exp(-2.0 * z)
    if name == "asinh":
        return np.exp(-np.arcsinh(z))
    if name == "logistic":
        return 1.0 / (1.0 + np.exp(z))

    raise ValueError(name)


def pointwise_probabilities(
    name: str,
    scores: np.ndarray,
) -> np.ndarray:
    return stable_normalize(
        weight_function(name, scores)
    )


def rank_probabilities(
    scores: np.ndarray,
) -> np.ndarray:
    order = np.argsort(
        scores,
        kind="mergesort",
    )
    ranks = np.empty(
        len(scores),
        dtype=float,
    )
    ranks[order] = np.arange(
        len(scores),
        dtype=float,
    )
    if len(scores) > 1:
        ranks /= len(scores) - 1.0
    return stable_normalize(
        np.exp(-ranks)
    )


def total_variation(
    first: np.ndarray,
    second: np.ndarray,
) -> float:
    return 0.5 * float(
        np.abs(first - second).sum()
    )


def entropy(probabilities: np.ndarray) -> float:
    probabilities = np.asarray(
        probabilities,
        dtype=float,
    )
    positive = probabilities > 0.0
    return float(
        -np.sum(
            probabilities[positive]
            * np.log(
                probabilities[positive]
            )
        )
    )


def softmax_negative_lambda(
    scores: np.ndarray,
    lambda_value: float,
) -> np.ndarray:
    logits = -lambda_value * scores
    logits -= float(logits.max())
    return stable_normalize(
        np.exp(logits)
    )


def iia_audit(
    rng: np.random.Generator,
) -> tuple[
    list[dict[str, object]],
    dict[str, float],
]:
    functions = (
        "exp_0_5",
        "exp_1",
        "exp_2",
        "asinh",
        "logistic",
    )
    rows = []
    rank_violations = 0

    for sample_index in range(
        CHOICE_SET_SAMPLES
    ):
        base_size = int(
            rng.integers(3, 10)
        )
        extra_size = int(
            rng.integers(1, 6)
        )
        base_scores = rng.normal(
            0.0,
            1.0,
            size=base_size,
        )
        extra_scores = rng.normal(
            0.0,
            1.0,
            size=extra_size,
        )
        expanded_scores = np.concatenate(
            [base_scores, extra_scores]
        )

        first = int(
            rng.integers(0, base_size)
        )
        second_candidates = [
            index
            for index in range(base_size)
            if index != first
        ]
        second = int(
            rng.choice(second_candidates)
        )

        for function_name in functions:
            base_probability = (
                pointwise_probabilities(
                    function_name,
                    base_scores,
                )
            )
            expanded_probability = (
                pointwise_probabilities(
                    function_name,
                    expanded_scores,
                )
            )
            base_ratio = (
                base_probability[first]
                / base_probability[second]
            )
            expanded_ratio = (
                expanded_probability[first]
                / expanded_probability[second]
            )
            relative_error = abs(
                expanded_ratio - base_ratio
            ) / max(abs(base_ratio), 1e-15)

            rows.append(
                {
                    "sample_index": (
                        sample_index
                    ),
                    "function": (
                        function_name
                    ),
                    "relative_odds_error": (
                        relative_error
                    ),
                }
            )

        base_rank = rank_probabilities(
            base_scores
        )
        expanded_rank = rank_probabilities(
            expanded_scores
        )
        base_rank_ratio = (
            base_rank[first]
            / base_rank[second]
        )
        expanded_rank_ratio = (
            expanded_rank[first]
            / expanded_rank[second]
        )
        if not math.isclose(
            base_rank_ratio,
            expanded_rank_ratio,
            rel_tol=1e-12,
            abs_tol=1e-12,
        ):
            rank_violations += 1

    return rows, {
        "rank_iia_violation_rate": (
            rank_violations
            / CHOICE_SET_SAMPLES
        )
    }


def functional_equation_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    functions = (
        "exp_0_5",
        "exp_1",
        "exp_2",
        "asinh",
        "logistic",
    )
    accumulators = {
        name: {
            "shift": [],
            "composition": [],
        }
        for name in functions
    }

    x = rng.normal(
        0.0,
        1.2,
        size=FUNCTIONAL_SAMPLES,
    )
    y = rng.normal(
        0.0,
        1.2,
        size=FUNCTIONAL_SAMPLES,
    )
    shift = rng.normal(
        0.0,
        0.8,
        size=FUNCTIONAL_SAMPLES,
    )

    a = rng.normal(
        0.0,
        0.8,
        size=FUNCTIONAL_SAMPLES,
    )
    b = rng.normal(
        0.0,
        0.8,
        size=FUNCTIONAL_SAMPLES,
    )
    zero = np.zeros_like(a)

    for name in functions:
        log_fx = np.log(
            weight_function(name, x)
        )
        log_fy = np.log(
            weight_function(name, y)
        )
        log_shift_x = np.log(
            weight_function(
                name,
                x + shift,
            )
        )
        log_shift_y = np.log(
            weight_function(
                name,
                y + shift,
            )
        )
        shift_residual = (
            (log_shift_x - log_shift_y)
            - (log_fx - log_fy)
        )

        log_f_a = np.log(
            weight_function(name, a)
        )
        log_f_b = np.log(
            weight_function(name, b)
        )
        log_f_ab = np.log(
            weight_function(name, a + b)
        )
        log_f_zero = np.log(
            weight_function(name, zero)
        )
        composition_residual = (
            log_f_ab
            + log_f_zero
            - log_f_a
            - log_f_b
        )

        accumulators[name]["shift"] = (
            np.abs(shift_residual)
        )
        accumulators[name]["composition"] = (
            np.abs(composition_residual)
        )

    rows = []
    for name, values in accumulators.items():
        rows.append(
            {
                "function": name,
                "maximum_shift_odds_residual": float(
                    np.max(values["shift"])
                ),
                "median_shift_odds_residual": float(
                    np.median(values["shift"])
                ),
                "maximum_additive_composition_residual": float(
                    np.max(
                        values["composition"]
                    )
                ),
                "median_additive_composition_residual": float(
                    np.median(
                        values["composition"]
                    )
                ),
            }
        )
    return rows


def detailed_balance_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    functions = (
        "exp_0_5",
        "exp_1",
        "exp_2",
        "asinh",
        "logistic",
    )
    rows = []

    for sample_index in range(
        DETAILED_BALANCE_SAMPLES
    ):
        n = int(
            rng.integers(5, 18)
        )
        raw_scores = rng.normal(
            0.0,
            1.0,
            size=(n, n),
        )
        scores = 0.5 * (
            raw_scores + raw_scores.T
        )
        np.fill_diagonal(scores, 0.0)

        adjacency = (
            rng.random((n, n)) < 0.30
        )
        adjacency = np.triu(
            adjacency,
            k=1,
        )
        adjacency |= adjacency.T

        # Ensure a symmetric ring, so no isolated rows.
        for vertex in range(n):
            adjacency[
                vertex,
                (vertex + 1) % n,
            ] = True
            adjacency[
                (vertex + 1) % n,
                vertex,
            ] = True
        np.fill_diagonal(adjacency, False)

        for name in functions:
            weights = np.zeros(
                (n, n),
                dtype=float,
            )
            weights[adjacency] = (
                weight_function(
                    name,
                    scores[adjacency],
                )
            )
            row_sums = weights.sum(
                axis=1
            )
            transition = (
                weights
                / row_sums[:, None]
            )
            stationary = (
                row_sums
                / row_sums.sum()
            )
            flux = (
                stationary[:, None]
                * transition
            )
            error = float(
                np.max(
                    np.abs(
                        flux - flux.T
                    )
                )
            )
            rows.append(
                {
                    "sample_index": (
                        sample_index
                    ),
                    "function": name,
                    "detailed_balance_error": (
                        error
                    ),
                }
            )

    return rows


def aggregation_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    functions = (
        "exp_0_5",
        "exp_1",
        "exp_2",
        "asinh",
        "logistic",
    )
    rows = []

    for sample_index in range(
        CHOICE_SET_SAMPLES
    ):
        size = int(
            rng.integers(4, 14)
        )
        scores = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        block_mask = (
            rng.random(size) < 0.45
        )
        if (
            block_mask.sum() == 0
            or block_mask.sum() == size
        ):
            block_mask[0] = True
            block_mask[-1] = False

        for name in functions:
            weights = weight_function(
                name,
                scores,
            )
            probabilities = stable_normalize(
                weights
            )
            direct_block_probability = float(
                probabilities[
                    block_mask
                ].sum()
            )

            block_weight = float(
                weights[
                    block_mask
                ].sum()
            )
            outside_weights = weights[
                ~block_mask
            ]
            aggregated_probability = (
                block_weight
                / (
                    block_weight
                    + float(
                        outside_weights.sum()
                    )
                )
            )
            rows.append(
                {
                    "sample_index": (
                        sample_index
                    ),
                    "function": name,
                    "aggregation_error": abs(
                        direct_block_probability
                        - aggregated_probability
                    ),
                }
            )

    return rows


def maximum_entropy_audit(
    rng: np.random.Generator,
) -> tuple[
    list[dict[str, object]],
    list[dict[str, object]],
]:
    rows = []
    lambda_family_rows = []

    for sample_index in range(
        MAX_ENTROPY_SAMPLES
    ):
        size = int(
            rng.integers(4, 12)
        )
        scores = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        scores = (
            scores - scores.mean()
        ) / scores.std(ddof=0)

        lambda_true = float(
            rng.uniform(0.15, 3.0)
        )
        optimum = (
            softmax_negative_lambda(
                scores,
                lambda_true,
            )
        )
        target_mean = float(
            np.dot(
                optimum,
                scores,
            )
        )

        def mean_residual(
            lambda_value: float,
        ) -> float:
            probability = (
                softmax_negative_lambda(
                    scores,
                    lambda_value,
                )
            )
            return float(
                np.dot(
                    probability,
                    scores,
                )
                - target_mean
            )

        lambda_recovered = float(
            brentq(
                mean_residual,
                -30.0,
                30.0,
                xtol=1e-13,
                rtol=1e-13,
            )
        )
        recovered = (
            softmax_negative_lambda(
                scores,
                lambda_recovered,
            )
        )

        constraints = np.vstack(
            [
                np.ones(size),
                scores,
            ]
        )
        basis = null_space(
            constraints
        )
        optimum_entropy = entropy(
            optimum
        )
        maximum_entropy_excess = (
            -float("inf")
        )

        for _ in range(
            MAX_ENTROPY_PERTURBATIONS
        ):
            if basis.shape[1] == 0:
                continue
            coefficients = rng.normal(
                0.0,
                1.0,
                size=basis.shape[1],
            )
            direction = (
                basis @ coefficients
            )
            norm = float(
                np.linalg.norm(direction)
            )
            if norm <= 1e-15:
                continue
            direction /= norm

            negative = direction < 0.0
            positive = direction > 0.0
            limits = []

            if np.any(negative):
                limits.append(
                    float(
                        np.min(
                            optimum[negative]
                            / -direction[negative]
                        )
                    )
                )
            if np.any(positive):
                limits.append(
                    float(
                        np.min(
                            (1.0 - optimum[positive])
                            / direction[positive]
                        )
                    )
                )

            if not limits:
                continue

            maximum_step = min(limits)
            step = float(
                rng.uniform(
                    -0.70,
                    0.70,
                )
            ) * maximum_step
            candidate = (
                optimum + step * direction
            )

            if (
                np.min(candidate) <= 0.0
                or abs(candidate.sum() - 1.0)
                > 1e-10
                or abs(
                    np.dot(
                        candidate,
                        scores,
                    )
                    - target_mean
                )
                > 1e-10
            ):
                continue

            entropy_excess = (
                entropy(candidate)
                - optimum_entropy
            )
            maximum_entropy_excess = max(
                maximum_entropy_excess,
                entropy_excess,
            )

        if maximum_entropy_excess == -float(
            "inf"
        ):
            maximum_entropy_excess = 0.0

        rows.append(
            {
                "sample_index": (
                    sample_index
                ),
                "choice_size": size,
                "lambda_true": (
                    lambda_true
                ),
                "lambda_recovered": (
                    lambda_recovered
                ),
                "lambda_absolute_error": abs(
                    lambda_recovered
                    - lambda_true
                ),
                "maximum_probability_error": float(
                    np.max(
                        np.abs(
                            recovered - optimum
                        )
                    )
                ),
                "target_mean_score": (
                    target_mean
                ),
                "maximum_feasible_entropy_excess": (
                    maximum_entropy_excess
                ),
            }
        )

    # Same score set, several lambda values: all obey exponential axioms,
    # but represent distinct laws and distinct expected-score constraints.
    scores = np.asarray(
        [-1.8, -0.7, -0.1, 0.4, 1.2, 2.0],
        dtype=float,
    )
    probabilities_by_lambda = {}

    for lambda_value in LAMBDA_VALUES:
        probability = (
            softmax_negative_lambda(
                scores,
                lambda_value,
            )
        )
        probabilities_by_lambda[
            lambda_value
        ] = probability
        lambda_family_rows.append(
            {
                "lambda": lambda_value,
                "expected_score_constraint": float(
                    np.dot(
                        probability,
                        scores,
                    )
                ),
                "entropy": entropy(
                    probability
                ),
                "probabilities": json.dumps(
                    [
                        float(value)
                        for value in probability
                    ]
                ),
            }
        )

    for first, second in itertools.combinations(
        LAMBDA_VALUES,
        2,
    ):
        lambda_family_rows.append(
            {
                "lambda": (
                    f"{first}_vs_{second}"
                ),
                "expected_score_constraint": (
                    float("nan")
                ),
                "entropy": float("nan"),
                "probabilities": (
                    f"TV={total_variation(probabilities_by_lambda[first], probabilities_by_lambda[second])}"
                ),
            }
        )

    return rows, lambda_family_rows


def extract_lambda_pair_tvs(
    lambda_family_rows: list[
        dict[str, object]
    ],
) -> list[float]:
    values = []

    for row in lambda_family_rows:
        label = str(row["lambda"])
        if "_vs_" not in label:
            continue
        text = str(row["probabilities"])
        values.append(
            float(
                text.split("TV=", 1)[1]
            )
        )

    return values


def main() -> None:
    output = Path("a26_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = """# A26 — Kernel Selection Principles

## IIA theorem

For any strictly positive pointwise weight `f`,

`P(j|S)=f(z_j)/sum_{k in S}f(z_k)`.

Therefore

`P(j|S)/P(k|S)=f(z_j)/f(z_k)`,

which is independent of all alternatives other than `j,k`. IIA admits every
positive pointwise `f` and does not select the exponential.

## Detailed-balance theorem

On an undirected graph with symmetric score `s_ij=s_ji`, set
`w_ij=f(s_ij)=w_ji` and `P_ij=w_ij/sum_k w_ik`. Then

`pi_i = sum_k w_ik / sum_{a,b} w_ab`

satisfies `pi_i P_ij = pi_j P_ji`. Every positive `f` is reversible.

## Aggregation theorem

For a block `B`, its direct probability is

`sum_{j in B}f(z_j)/sum_k f(z_k)`.

Representing the block by its total weight `W_B=sum_{j in B}f(z_j)` reproduces
that probability exactly for every positive `f`.

## Exponential-family uniqueness theorem

Assume the odds ratio depends only on score difference:

`f(x)/f(y)=g(x-y)`,

with positive continuous `f`. Setting `y=0` and comparing three scores gives

`g(a+b)=g(a)g(b)`.

The continuous positive solutions are `g(t)=exp(-lambda t)`, so

`f(z)=C exp(-lambda z)`.

This selects the exponential family. It does not fix `lambda`.

## Maximum-entropy theorem

Maximize `H(p)=-sum_j p_j log p_j` subject to

`sum_j p_j=1`,
`sum_j p_j z_j=m`.

The Lagrange stationary condition gives

`p_j proportional to exp(-lambda z_j)`.

Strict concavity makes this the unique maximizer for an interior feasible
constraint. The multiplier `lambda` is determined by the specified value
`m`. Without a law fixing `m`, maximum entropy does not choose a unique
kernel strength.

## Boundary

The exponential family has rigorous axiomatic support. A unique physical
transition law still requires an independently justified score, constraint,
and value of `lambda`.
"""
    (output / "a26_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    iia_rows, rank_iia = iia_audit(
        rng
    )
    functional_rows = (
        functional_equation_audit(
            rng
        )
    )
    detailed_rows = (
        detailed_balance_audit(
            rng
        )
    )
    aggregation_rows = aggregation_audit(
        rng
    )
    (
        maximum_entropy_rows,
        lambda_family_rows,
    ) = maximum_entropy_audit(rng)

    iia_frame = pd.DataFrame(iia_rows)
    functional_frame = pd.DataFrame(
        functional_rows
    )
    detailed_frame = pd.DataFrame(
        detailed_rows
    )
    aggregation_frame = pd.DataFrame(
        aggregation_rows
    )
    maximum_entropy_frame = pd.DataFrame(
        maximum_entropy_rows
    )
    lambda_family_frame = pd.DataFrame(
        lambda_family_rows
    )

    iia_frame.to_csv(
        output / "a26_iia_audit.csv",
        index=False,
    )
    functional_frame.to_csv(
        output / "a26_functional_equation_audit.csv",
        index=False,
    )
    detailed_frame.to_csv(
        output / "a26_detailed_balance_audit.csv",
        index=False,
    )
    aggregation_frame.to_csv(
        output / "a26_aggregation_audit.csv",
        index=False,
    )
    maximum_entropy_frame.to_csv(
        output / "a26_maximum_entropy_audit.csv",
        index=False,
    )
    lambda_family_frame.to_csv(
        output / "a26_lambda_family.csv",
        index=False,
    )

    exponential_names = (
        "exp_0_5",
        "exp_1",
        "exp_2",
    )
    nonexponential_names = (
        "asinh",
        "logistic",
    )

    exponential_functional = (
        functional_frame[
            functional_frame[
                "function"
            ].isin(
                exponential_names
            )
        ]
    )
    nonexponential_functional = (
        functional_frame[
            functional_frame[
                "function"
            ].isin(
                nonexponential_names
            )
        ]
    )

    lambda_pair_tvs = (
        extract_lambda_pair_tvs(
            lambda_family_rows
        )
    )

    gates = {
        "G1_all_pointwise_kernels_satisfy_iia": bool(
            iia_frame[
                "relative_odds_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G2_rank_context_control_violates_iia": bool(
            rank_iia[
                "rank_iia_violation_rate"
            ]
            >= MIN_CONTEXT_RANK_IIA_VIOLATION_RATE
        ),
        "G3_detailed_balance_is_nonselective": bool(
            detailed_frame[
                "detailed_balance_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G4_weight_aggregation_is_nonselective": bool(
            aggregation_frame[
                "aggregation_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G5_exponential_family_satisfies_difference_and_composition": bool(
            exponential_functional[
                [
                    "maximum_shift_odds_residual",
                    "maximum_additive_composition_residual",
                ]
            ].max().max()
            <= MAX_EXACT_ERROR
        ),
        "G6_nonexponential_controls_fail_exponential_axioms": bool(
            nonexponential_functional[
                "median_shift_odds_residual"
            ].min()
            >= MIN_NONEXP_SHIFT_RESIDUAL
            and nonexponential_functional[
                "median_additive_composition_residual"
            ].min()
            >= MIN_NONEXP_COMPOSITION_RESIDUAL
        ),
        "G7_maximum_entropy_recovers_exponential_solution": bool(
            maximum_entropy_frame[
                "lambda_absolute_error"
            ].max()
            <= MAX_ENTROPY_LAMBDA_ERROR
            and maximum_entropy_frame[
                "maximum_probability_error"
            ].max()
            <= MAX_ENTROPY_PROBABILITY_ERROR
        ),
        "G8_maximum_entropy_solution_dominates_feasible_perturbations": bool(
            maximum_entropy_frame[
                "maximum_feasible_entropy_excess"
            ].max()
            <= MAX_ENTROPY_VIOLATION
        ),
        "G9_lambda_remains_observationally_nonunique": bool(
            min(lambda_pair_tvs)
            >= MIN_DISTINCT_LAMBDA_TV
        ),
        "G10_different_constraints_generate_different_lambda": bool(
            lambda_family_frame[
                lambda_family_frame[
                    "lambda"
                ].apply(
                    lambda value: isinstance(
                        value,
                        (int, float, np.integer, np.floating),
                    )
                )
            ][
                "expected_score_constraint"
            ].nunique()
            == len(LAMBDA_VALUES)
        ),
        "G11_exponential_form_not_physical_strength_claimed": True,
        "G12_no_unique_rzs_kernel_claimed": True,
    }

    verdict = (
        "PASS_EXPONENTIAL_FAMILY_SELECTION_WITH_FREE_STRENGTH"
        if all(gates.values())
        else "FAIL_KERNEL_SELECTION_PRINCIPLES_AUDIT"
    )

    principle_classification = [
        {
            "principle": "IIA",
            "selects": "all positive pointwise weight functions",
            "unique": False,
            "hidden_input": "none beyond pointwise score",
            "status": "NONSELECTIVE",
        },
        {
            "principle": "detailed balance on symmetric weights",
            "selects": "all positive symmetric edge-weight functions",
            "unique": False,
            "hidden_input": "stationary measure follows from row sums",
            "status": "NONSELECTIVE",
        },
        {
            "principle": "aggregation by total weight",
            "selects": "all additive positive weight representations",
            "unique": False,
            "hidden_input": "choice of weight representation",
            "status": "NONSELECTIVE",
        },
        {
            "principle": "difference-only odds plus continuity",
            "selects": "f(z)=C exp(-lambda z)",
            "unique": "family only",
            "hidden_input": "cardinal additive score z",
            "status": "SELECTS_EXPONENTIAL_FAMILY",
        },
        {
            "principle": "maximum entropy with fixed expected score",
            "selects": "f(z)=exp(-lambda z)",
            "unique": "yes after target mean m is fixed",
            "hidden_input": "choice of score and numerical constraint m",
            "status": "CONDITIONAL_SELECTION",
        },
        {
            "principle": "present RZS postulates alone",
            "selects": "no unique lambda or target mean",
            "unique": False,
            "hidden_input": "missing empirical or dynamical constraint",
            "status": "LAW_STRENGTH_UNDERDETERMINED",
        },
    ]
    pd.DataFrame(
        principle_classification
    ).to_csv(
        output / "a26_principle_classification.csv",
        index=False,
    )

    summary = {
        "seed": SEED,
        "functional_samples": (
            FUNCTIONAL_SAMPLES
        ),
        "choice_set_samples": (
            CHOICE_SET_SAMPLES
        ),
        "detailed_balance_samples": (
            DETAILED_BALANCE_SAMPLES
        ),
        "maximum_entropy_samples": (
            MAX_ENTROPY_SAMPLES
        ),
        "rank_iia_violation_rate": (
            rank_iia[
                "rank_iia_violation_rate"
            ]
        ),
        "functional_results": (
            functional_rows
        ),
        "minimum_pairwise_lambda_tv": (
            min(lambda_pair_tvs)
        ),
        "maximum_pairwise_lambda_tv": (
            max(lambda_pair_tvs)
        ),
        "maximum_entropy_results": {
            "maximum_lambda_error": float(
                maximum_entropy_frame[
                    "lambda_absolute_error"
                ].max()
            ),
            "maximum_probability_error": float(
                maximum_entropy_frame[
                    "maximum_probability_error"
                ].max()
            ),
            "maximum_feasible_entropy_excess": float(
                maximum_entropy_frame[
                    "maximum_feasible_entropy_excess"
                ].max()
            ),
        },
        "principle_classification": (
            principle_classification
        ),
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "IIA, detailed balance, and aggregation do not select a "
            "unique q-kernel. Continuity plus difference-only odds, "
            "equivalently additive composition of weights, selects the "
            "exponential family. Maximum entropy reaches the same family "
            "only after a numerical expected-score constraint is supplied. "
            "Neither route fixes lambda from the current RZS postulates, so "
            "the functional form can be justified more strongly than the "
            "coupling strength."
        ),
        "interpretation_boundary": (
            "A26 does not establish that transitions in nature obey the "
            "difference-only odds axiom, that standardized q is the correct "
            "constraint variable, or that any tested lambda is physical. "
            "The result narrows the admissible family without deriving a "
            "complete RZS law."
        ),
    }

    (output / "a26_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A26 — Kernel Selection Principles Audit",
        "",
        "## Main result",
        "",
        (
            "IIA, detailed balance, and aggregation were nonselective. "
            "Difference-only odds plus continuity selected the exponential "
            "family. Maximum entropy selected the same family conditional "
            "on a fixed expected-score constraint. Lambda remained free."
        ),
        "",
        "## Functional results",
        "",
    ]

    for result in functional_rows:
        report_lines.extend(
            [
                f"### {result['function']}",
                (
                    "- Median shift residual: "
                    f"{result['median_shift_odds_residual']:.6g}"
                ),
                (
                    "- Median composition residual: "
                    f"{result['median_additive_composition_residual']:.6g}"
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
            summary[
                "interpretation_boundary"
            ],
        ]
    )

    (output / "a26_report.md").write_text(
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
