
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 20260813

LAMBDA = 1.25

SCALAR_SAMPLES = 5000
REFINEMENT_SAMPLES = 4000
KERNEL_SAMPLES = 4000
GRAPH_SAMPLES = 1200

MAX_EXACT_ERROR = 3e-12
MIN_MEDIAN_ASSOCIATIVITY_FAILURE_RATE = 0.70
MIN_UNWEIGHTED_CLONE_TV = 0.01
MIN_ARITHMETIC_KERNEL_MEDIAN_TV = 0.01
MIN_OCCUPANCY_MEDIAN_ROW_TV = 0.03


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


def normalize(values: np.ndarray, axis: int = -1) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    total = values.sum(axis=axis, keepdims=True)
    if np.any(total <= 0.0):
        raise ValueError("Nonpositive normalization total.")
    return values / total


def total_variation(
    first: np.ndarray,
    second: np.ndarray,
) -> float:
    return 0.5 * float(
        np.abs(
            np.asarray(first, dtype=float)
            - np.asarray(second, dtype=float)
        ).sum()
    )


def weighted_arithmetic(
    values: np.ndarray,
    masses: np.ndarray,
) -> float:
    return float(
        np.dot(masses, values)
        / masses.sum()
    )


def exponential_mean(
    values: np.ndarray,
    masses: np.ndarray,
    lambda_value: float = LAMBDA,
) -> float:
    masses = np.asarray(masses, dtype=float)
    values = np.asarray(values, dtype=float)
    logits = -lambda_value * values
    maximum = float(logits.max())
    log_weighted_mean = (
        maximum
        + math.log(
            float(
                np.dot(
                    masses,
                    np.exp(logits - maximum),
                )
                / masses.sum()
            )
        )
    )
    return -log_weighted_mean / lambda_value


def weighted_lower_median(
    values: np.ndarray,
    masses: np.ndarray,
) -> float:
    values = np.asarray(values, dtype=float)
    masses = np.asarray(masses, dtype=float)
    order = np.argsort(values)
    sorted_values = values[order]
    sorted_masses = masses[order]
    threshold = 0.5 * float(sorted_masses.sum())
    index = int(
        np.searchsorted(
            np.cumsum(sorted_masses),
            threshold,
            side="left",
        )
    )
    return float(sorted_values[index])


def minimum_score(
    values: np.ndarray,
    masses: np.ndarray,
) -> float:
    del masses
    return float(np.min(values))


def rms_score(
    values: np.ndarray,
    masses: np.ndarray,
) -> float:
    return float(
        math.sqrt(
            np.dot(masses, values**2)
            / masses.sum()
        )
    )


SCALAR_OPERATORS = {
    "weighted_arithmetic": weighted_arithmetic,
    "exponential_mean": exponential_mean,
    "weighted_median": weighted_lower_median,
    "minimum": minimum_score,
}


def random_partition(
    size: int,
    rng: np.random.Generator,
    minimum_groups: int = 2,
    maximum_groups: int | None = None,
) -> list[np.ndarray]:
    if maximum_groups is None:
        maximum_groups = min(7, size)
    group_count = int(
        rng.integers(
            minimum_groups,
            min(maximum_groups, size) + 1,
        )
    )
    labels = np.arange(group_count)
    if size > group_count:
        labels = np.concatenate(
            [
                labels,
                rng.integers(
                    0,
                    group_count,
                    size=size - group_count,
                ),
            ]
        )
    rng.shuffle(labels)
    return [
        np.flatnonzero(labels == label)
        for label in range(group_count)
    ]


def two_stage_scalar(
    values: np.ndarray,
    masses: np.ndarray,
    groups: list[np.ndarray],
    operator_name: str,
) -> tuple[float, float]:
    operator = SCALAR_OPERATORS[
        operator_name
    ]

    direct = operator(values, masses)
    group_masses = np.asarray(
        [
            masses[group].sum()
            for group in groups
        ],
        dtype=float,
    )
    group_scores = np.asarray(
        [
            operator(
                values[group],
                masses[group],
            )
            for group in groups
        ],
        dtype=float,
    )
    hierarchical = operator(
        group_scores,
        group_masses,
    )
    return direct, hierarchical


def scalar_associativity_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(
        SCALAR_SAMPLES
    ):
        size = int(
            rng.integers(5, 35)
        )
        values = rng.normal(
            0.0,
            1.2,
            size=size,
        )
        masses = np.exp(
            rng.normal(
                0.0,
                0.8,
                size=size,
            )
        )
        groups = random_partition(
            size,
            rng,
        )

        for operator_name in (
            "weighted_arithmetic",
            "exponential_mean",
            "weighted_median",
            "minimum",
        ):
            direct, hierarchical = (
                two_stage_scalar(
                    values,
                    masses,
                    groups,
                    operator_name,
                )
            )
            error = abs(
                direct - hierarchical
            )
            rows.append(
                {
                    "sample_index": sample_index,
                    "operator": operator_name,
                    "size": size,
                    "group_count": len(groups),
                    "direct_score": direct,
                    "hierarchical_score": (
                        hierarchical
                    ),
                    "absolute_associativity_error": (
                        error
                    ),
                    "associative_at_tolerance": bool(
                        error <= MAX_EXACT_ERROR
                    ),
                }
            )

    return rows


def refinement_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(
        REFINEMENT_SAMPLES
    ):
        size = int(
            rng.integers(4, 22)
        )
        values = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        masses = np.exp(
            rng.normal(
                0.0,
                0.7,
                size=size,
            )
        )
        target = int(
            rng.integers(0, size)
        )
        clone_count = int(
            rng.integers(2, 8)
        )
        fractions = rng.dirichlet(
            np.ones(clone_count)
        )

        clone_values = np.full(
            clone_count,
            values[target],
        )
        clone_masses = (
            masses[target] * fractions
        )
        refined_values = np.concatenate(
            [
                values[:target],
                clone_values,
                values[target + 1 :],
            ]
        )
        refined_masses = np.concatenate(
            [
                masses[:target],
                clone_masses,
                masses[target + 1 :],
            ]
        )

        for operator_name, operator in (
            SCALAR_OPERATORS.items()
        ):
            original = operator(
                values,
                masses,
            )
            refined = operator(
                refined_values,
                refined_masses,
            )
            rows.append(
                {
                    "sample_index": sample_index,
                    "operator": operator_name,
                    "absolute_refinement_error": abs(
                        original - refined
                    ),
                }
            )

        unweighted_original = float(
            values.mean()
        )
        unweighted_refined = float(
            refined_values.mean()
        )
        rows.append(
            {
                "sample_index": sample_index,
                "operator": "unweighted_mean",
                "absolute_refinement_error": abs(
                    unweighted_original
                    - unweighted_refined
                ),
            }
        )

    return rows


def gauge_covariance_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(3000):
        size = int(
            rng.integers(4, 25)
        )
        values = rng.normal(
            0.0,
            1.1,
            size=size,
        )
        masses = np.exp(
            rng.normal(
                0.0,
                0.6,
                size=size,
            )
        )
        offset = float(
            rng.uniform(-4.0, 4.0)
        )

        for operator_name, operator in (
            {
                **SCALAR_OPERATORS,
                "rms": rms_score,
            }.items()
        ):
            original = operator(
                values,
                masses,
            )
            shifted = operator(
                values + offset,
                masses,
            )
            rows.append(
                {
                    "sample_index": sample_index,
                    "operator": operator_name,
                    "offset": offset,
                    "absolute_gauge_covariance_error": abs(
                        shifted
                        - original
                        - offset
                    ),
                }
            )

    return rows


def kernel_preservation_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(
        KERNEL_SAMPLES
    ):
        size = int(
            rng.integers(6, 40)
        )
        values = rng.normal(
            0.0,
            1.0,
            size=size,
        )
        masses = np.exp(
            rng.normal(
                0.0,
                0.7,
                size=size,
            )
        )
        groups = random_partition(
            size,
            rng,
            minimum_groups=2,
            maximum_groups=min(8, size),
        )

        direct_group_weights = np.asarray(
            [
                np.dot(
                    masses[group],
                    np.exp(
                        -LAMBDA
                        * values[group]
                    ),
                )
                for group in groups
            ],
            dtype=float,
        )
        direct_group_probability = (
            normalize(
                direct_group_weights
            )
        )

        for operator_name in (
            "weighted_arithmetic",
            "exponential_mean",
            "weighted_median",
            "minimum",
        ):
            operator = SCALAR_OPERATORS[
                operator_name
            ]
            group_masses = np.asarray(
                [
                    masses[group].sum()
                    for group in groups
                ],
                dtype=float,
            )
            group_scores = np.asarray(
                [
                    operator(
                        values[group],
                        masses[group],
                    )
                    for group in groups
                ],
                dtype=float,
            )
            predicted_weights = (
                group_masses
                * np.exp(
                    -LAMBDA
                    * group_scores
                )
            )
            predicted_probability = (
                normalize(
                    predicted_weights
                )
            )

            rows.append(
                {
                    "sample_index": sample_index,
                    "operator": operator_name,
                    "group_count": len(groups),
                    "macro_probability_tv": total_variation(
                        direct_group_probability,
                        predicted_probability,
                    ),
                    "maximum_group_weight_relative_error": float(
                        np.max(
                            np.abs(
                                predicted_weights
                                - direct_group_weights
                            )
                            / direct_group_weights
                        )
                    ),
                }
            )

    return rows


def random_nested_partition(
    size: int,
    rng: np.random.Generator,
) -> tuple[
    np.ndarray,
    np.ndarray,
]:
    fine_count = int(
        rng.integers(
            4,
            min(9, size) + 1,
        )
    )
    fine_labels = np.arange(fine_count)
    if size > fine_count:
        fine_labels = np.concatenate(
            [
                fine_labels,
                rng.integers(
                    0,
                    fine_count,
                    size=size - fine_count,
                ),
            ]
        )
    rng.shuffle(fine_labels)

    coarse_count = int(
        rng.integers(
            2,
            fine_count,
        )
    )
    fine_to_coarse = np.arange(
        fine_count
    ) % coarse_count
    rng.shuffle(fine_to_coarse)

    coarse_labels = (
        fine_to_coarse[
            fine_labels
        ]
    )
    return fine_labels, coarse_labels


def aggregate_matrix(
    matrix: np.ndarray,
    source_labels: np.ndarray,
    target_labels: np.ndarray,
    source_count: int,
    target_count: int,
) -> np.ndarray:
    result = np.zeros(
        (source_count, target_count),
        dtype=float,
    )
    for source in range(
        len(source_labels)
    ):
        for target in range(
            len(target_labels)
        ):
            result[
                int(source_labels[source]),
                int(target_labels[target]),
            ] += matrix[source, target]
    return result


def graph_audit(
    rng: np.random.Generator,
) -> tuple[
    list[dict[str, object]],
    list[dict[str, object]],
    list[dict[str, object]],
]:
    nested_rows = []
    occupancy_rows = []
    flow_rows = []

    for sample_index in range(
        GRAPH_SAMPLES
    ):
        size = int(
            rng.integers(12, 33)
        )
        q = rng.normal(
            0.0,
            0.9,
            size=(size, size),
        )
        edge_mass = np.exp(
            rng.normal(
                0.0,
                0.7,
                size=(size, size),
            )
        )
        microscopic_weight = (
            edge_mass
            * np.exp(-LAMBDA * q)
        )
        transition = normalize(
            microscopic_weight,
            axis=1,
        )

        fine_labels, coarse_labels = (
            random_nested_partition(
                size,
                rng,
            )
        )
        fine_count = int(
            fine_labels.max() + 1
        )
        coarse_count = int(
            coarse_labels.max() + 1
        )

        direct_coarse_weight = (
            aggregate_matrix(
                microscopic_weight,
                coarse_labels,
                coarse_labels,
                coarse_count,
                coarse_count,
            )
        )
        fine_weight = aggregate_matrix(
            microscopic_weight,
            fine_labels,
            fine_labels,
            fine_count,
            fine_count,
        )

        fine_to_coarse = np.zeros(
            fine_count,
            dtype=int,
        )
        for fine_region in range(
            fine_count
        ):
            member = int(
                np.flatnonzero(
                    fine_labels
                    == fine_region
                )[0]
            )
            fine_to_coarse[
                fine_region
            ] = coarse_labels[member]

        nested_coarse_weight = (
            aggregate_matrix(
                fine_weight,
                fine_to_coarse,
                fine_to_coarse,
                coarse_count,
                coarse_count,
            )
        )

        nested_rows.append(
            {
                "sample_index": sample_index,
                "size": size,
                "fine_count": fine_count,
                "coarse_count": coarse_count,
                "maximum_nested_weight_error": float(
                    np.max(
                        np.abs(
                            direct_coarse_weight
                            - nested_coarse_weight
                        )
                    )
                ),
            }
        )

        # Same microscopic transition matrix and same region partition,
        # but two different conditional source occupancies.
        occupancy_uniform = []
        occupancy_skewed = []
        macro_uniform = np.zeros(
            (coarse_count, coarse_count),
            dtype=float,
        )
        macro_skewed = np.zeros_like(
            macro_uniform
        )

        for region in range(
            coarse_count
        ):
            members = np.flatnonzero(
                coarse_labels == region
            )
            uniform = np.full(
                len(members),
                1.0 / len(members),
            )
            skewed = rng.dirichlet(
                np.full(
                    len(members),
                    0.25,
                )
            )
            occupancy_uniform.append(
                uniform
            )
            occupancy_skewed.append(
                skewed
            )

            destination_macro = np.zeros(
                (len(members), coarse_count),
                dtype=float,
            )
            for local_index, source in enumerate(
                members
            ):
                for target_region in range(
                    coarse_count
                ):
                    destination_macro[
                        local_index,
                        target_region,
                    ] = transition[
                        source,
                        coarse_labels
                        == target_region,
                    ].sum()

            macro_uniform[region] = (
                uniform
                @ destination_macro
            )
            macro_skewed[region] = (
                skewed
                @ destination_macro
            )

        row_tvs = np.asarray(
            [
                total_variation(
                    macro_uniform[row],
                    macro_skewed[row],
                )
                for row in range(
                    coarse_count
                )
            ]
        )

        occupancy_rows.append(
            {
                "sample_index": sample_index,
                "coarse_count": coarse_count,
                "mean_macro_row_tv": float(
                    row_tvs.mean()
                ),
                "maximum_macro_row_tv": float(
                    row_tvs.max()
                ),
            }
        )

        # Exact flow aggregation when a source occupancy pi is supplied.
        pi = normalize(
            np.exp(
                rng.normal(
                    0.0,
                    0.8,
                    size=size,
                )
            )
        )
        joint_flow = (
            pi[:, None]
            * transition
        )
        coarse_flow = aggregate_matrix(
            joint_flow,
            coarse_labels,
            coarse_labels,
            coarse_count,
            coarse_count,
        )
        coarse_pi = np.asarray(
            [
                pi[
                    coarse_labels
                    == region
                ].sum()
                for region in range(
                    coarse_count
                )
            ]
        )
        flow_transition = (
            coarse_flow
            / coarse_pi[:, None]
        )

        direct_occupancy_transition = (
            np.zeros_like(
                flow_transition
            )
        )
        for region in range(
            coarse_count
        ):
            members = np.flatnonzero(
                coarse_labels == region
            )
            conditional_pi = (
                pi[members]
                / pi[members].sum()
            )
            destination_macro = np.zeros(
                (len(members), coarse_count),
                dtype=float,
            )
            for local_index, source in enumerate(
                members
            ):
                for target_region in range(
                    coarse_count
                ):
                    destination_macro[
                        local_index,
                        target_region,
                    ] = transition[
                        source,
                        coarse_labels
                        == target_region,
                    ].sum()
            direct_occupancy_transition[
                region
            ] = (
                conditional_pi
                @ destination_macro
            )

        flow_rows.append(
            {
                "sample_index": sample_index,
                "maximum_flow_aggregation_error": float(
                    np.max(
                        np.abs(
                            flow_transition
                            - direct_occupancy_transition
                        )
                    )
                ),
                "maximum_macro_row_sum_error": float(
                    np.max(
                        np.abs(
                            flow_transition.sum(
                                axis=1
                            )
                            - 1.0
                        )
                    )
                ),
            }
        )

    return (
        nested_rows,
        occupancy_rows,
        flow_rows,
    )



def weighted_median_counterexample() -> dict[str, float]:
    """
    Exact non-closure witness for summaries consisting only of group mass
    and weighted lower median.

    Group 1:
      values 0 and 2, masses 0.4 and 0.1 -> group median 0, mass 0.5.
    Group 2:
      value 1, mass 0.5 -> group median 1, mass 0.5.

    Hierarchical lower median of group medians is 0.
    Direct lower median of all leaves is 1.
    """
    values = np.asarray([0.0, 2.0, 1.0])
    masses = np.asarray([0.4, 0.1, 0.5])
    groups = [
        np.asarray([0, 1]),
        np.asarray([2]),
    ]

    direct, hierarchical = two_stage_scalar(
        values,
        masses,
        groups,
        "weighted_median",
    )
    return {
        "direct_weighted_median": direct,
        "hierarchical_weighted_median": hierarchical,
        "absolute_difference": abs(
            direct - hierarchical
        ),
    }

def main() -> None:
    output = Path(
        "a38_1_exact_results"
    )
    output.mkdir(exist_ok=True)

    theorem_text = r"""# A38.1 — Corrected Gauge-Compatible Coarse-Graining Audit

## Corrective gate note

The original A38 used a 70% empirical failure-rate threshold to reject closure
of weighted medians. That threshold measured prevalence, not the universal
closure property. A single exact counterexample is logically decisive.
A38.1 preserves the original result and replaces only that misaligned gate
with an explicit counterexample; all other gates and tolerances are unchanged.

## Translation-covariant decomposable means

Within the class of continuous strictly monotone weighted quasi-arithmetic
means

\[
M_f(q;\mu)
=
f^{-1}
\left(
\frac{\sum_i\mu_i f(q_i)}
{\sum_i\mu_i}
\right),
\]

decomposability is automatic when a block passes its mass and its mean.
Requiring translation covariance

\[
M_f(q+c;\mu)=M_f(q;\mu)+c
\]

restricts the generator, up to equivalent affine changes, to two families:

1. \(f(q)=q\), giving the weighted arithmetic mean;
2. \(f(q)=e^{kq}\), giving the exponential or log-sum-exp means.

Thus gauge covariance and hierarchical decomposability do not select a unique
coarse variable. They select arithmetic and exponential families inside the
audited regular mean class.

## Observable-relative sufficiency

The arithmetic mean exactly preserves the first weighted moment.

For the exponential microscopic weight

\[
w_i=\mu_i e^{-\lambda q_i},
\]

the exact block message is

\[
W_B=\sum_{i\in B}\mu_i e^{-\lambda q_i}.
\]

Equivalently, a block may pass

\[
\mu_B=\sum_{i\in B}\mu_i,
\qquad
Q_B=-\lambda^{-1}\log(W_B/\mu_B).
\]

Then

\[
W_B=\mu_Be^{-\lambda Q_B}
\]

and nested aggregation is exact. Replacing \(Q_B\) by the arithmetic mean,
median, or minimum generally does not preserve the exponential observable.

## Dynamic graph obstruction

A microscopic row-stochastic kernel \(K_{ij}\) does not determine a unique
macro transition from a source region \(A\) unless a conditional source
occupancy \(\rho(i\mid A)\) is supplied:

\[
K^{\mathrm{macro}}_{AB}
=
\sum_{i\in A}\rho(i\mid A)
\sum_{j\in B}K_{ij}.
\]

Different occupancies on the same microscopic graph can give different macro
kernels.

If a global occupancy \(\pi_i\) is supplied, the joint flow

\[
F_{ij}=\pi_iK_{ij}
\]

aggregates exactly:

\[
F_{AB}=\sum_{i\in A,j\in B}F_{ij},
\qquad
K^{\mathrm{macro}}_{AB}
=
F_{AB}/\pi_A.
\]

## Boundary

The audit selects sufficient messages relative to declared observables. It
does not prove that the exponential kernel is physical, derive lambda, or
supply the source occupancy required for dynamic graph coarse-graining.
"""
    (
        output / "a38_theorem.md"
    ).write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    (
        nested_rows,
        occupancy_rows,
        flow_rows,
    ) = graph_audit(rng)

    frames = {
        "associativity": pd.DataFrame(
            scalar_associativity_audit(
                rng
            )
        ),
        "refinement": pd.DataFrame(
            refinement_audit(rng)
        ),
        "gauge": pd.DataFrame(
            gauge_covariance_audit(rng)
        ),
        "kernel": pd.DataFrame(
            kernel_preservation_audit(
                rng
            )
        ),
        "nested_graph": pd.DataFrame(
            nested_rows
        ),
        "occupancy": pd.DataFrame(
            occupancy_rows
        ),
        "flow": pd.DataFrame(
            flow_rows
        ),
        "median_counterexample": pd.DataFrame(
            [weighted_median_counterexample()]
        ),
    }

    file_map = {
        "associativity": (
            "a38_scalar_associativity.csv"
        ),
        "refinement": (
            "a38_refinement_invariance.csv"
        ),
        "gauge": (
            "a38_gauge_covariance.csv"
        ),
        "kernel": (
            "a38_exponential_kernel_preservation.csv"
        ),
        "nested_graph": (
            "a38_nested_graph_aggregation.csv"
        ),
        "occupancy": (
            "a38_source_occupancy_obstruction.csv"
        ),
        "flow": (
            "a38_flow_aggregation.csv"
        ),
        "median_counterexample": (
            "a38_weighted_median_counterexample.csv"
        ),
    }

    for key, frame in frames.items():
        frame.to_csv(
            output / file_map[key],
            index=False,
        )

    associativity_summary = []
    for operator, group in (
        frames["associativity"]
        .groupby("operator")
    ):
        associativity_summary.append(
            {
                "operator": operator,
                "associativity_pass_rate": float(
                    group[
                        "associative_at_tolerance"
                    ].mean()
                ),
                "median_absolute_error": float(
                    group[
                        "absolute_associativity_error"
                    ].median()
                ),
                "maximum_absolute_error": float(
                    group[
                        "absolute_associativity_error"
                    ].max()
                ),
            }
        )

    kernel_summary = []
    for operator, group in (
        frames["kernel"]
        .groupby("operator")
    ):
        kernel_summary.append(
            {
                "operator": operator,
                "median_macro_probability_tv": float(
                    group[
                        "macro_probability_tv"
                    ].median()
                ),
                "maximum_macro_probability_tv": float(
                    group[
                        "macro_probability_tv"
                    ].max()
                ),
            }
        )

    associativity_by = {
        row["operator"]: row
        for row in associativity_summary
    }
    kernel_by = {
        row["operator"]: row
        for row in kernel_summary
    }

    weighted_refinement = (
        frames["refinement"]
        .query(
            "operator in "
            "['weighted_arithmetic', "
            "'exponential_mean', "
            "'weighted_median', "
            "'minimum']"
        )
    )
    unweighted_refinement = (
        frames["refinement"]
        .query(
            "operator == 'unweighted_mean'"
        )
    )

    gauge_good = (
        frames["gauge"]
        .query(
            "operator in "
            "['weighted_arithmetic', "
            "'exponential_mean', "
            "'weighted_median', "
            "'minimum']"
        )
    )
    gauge_rms = (
        frames["gauge"]
        .query("operator == 'rms'")
    )

    gates = {
        "G1_translation_covariant_quasi_arithmetic_classification_stated": True,
        "G2_weighted_arithmetic_associative_refinement_consistent_and_gauge_covariant": bool(
            associativity_by[
                "weighted_arithmetic"
            ][
                "maximum_absolute_error"
            ]
            <= MAX_EXACT_ERROR
            and frames["refinement"]
            .query(
                "operator == "
                "'weighted_arithmetic'"
            )[
                "absolute_refinement_error"
            ].max()
            <= MAX_EXACT_ERROR
            and frames["gauge"]
            .query(
                "operator == "
                "'weighted_arithmetic'"
            )[
                "absolute_gauge_covariance_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G3_exponential_mean_associative_refinement_consistent_and_gauge_covariant": bool(
            associativity_by[
                "exponential_mean"
            ][
                "maximum_absolute_error"
            ]
            <= MAX_EXACT_ERROR
            and frames["refinement"]
            .query(
                "operator == "
                "'exponential_mean'"
            )[
                "absolute_refinement_error"
            ].max()
            <= MAX_EXACT_ERROR
            and frames["gauge"]
            .query(
                "operator == "
                "'exponential_mean'"
            )[
                "absolute_gauge_covariance_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G4_weighted_median_not_closed_by_mass_and_median_message": bool(
            frames["median_counterexample"][
                "absolute_difference"
            ].iloc[0]
            >= 0.9
        ),
        "G5_minimum_is_associative_but_mass_insensitive_extremal_control": bool(
            associativity_by[
                "minimum"
            ][
                "maximum_absolute_error"
            ]
            <= MAX_EXACT_ERROR
        ),
        "G6_unweighted_mean_is_clone_sensitive_under_mass_preserving_refinement": bool(
            unweighted_refinement[
                "absolute_refinement_error"
            ].median()
            >= MIN_UNWEIGHTED_CLONE_TV
            and weighted_refinement[
                "absolute_refinement_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G7_rms_fails_additive_gauge_covariance": bool(
            gauge_rms[
                "absolute_gauge_covariance_error"
            ].median()
            >= 0.1
            and gauge_good[
                "absolute_gauge_covariance_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G8_exponential_mean_exactly_preserves_exponential_kernel": bool(
            kernel_by[
                "exponential_mean"
            ][
                "maximum_macro_probability_tv"
            ]
            <= MAX_EXACT_ERROR
        ),
        "G9_arithmetic_mean_does_not_preserve_exponential_kernel": bool(
            kernel_by[
                "weighted_arithmetic"
            ][
                "median_macro_probability_tv"
            ]
            >= MIN_ARITHMETIC_KERNEL_MEDIAN_TV
        ),
        "G10_nested_graph_partition_sum_aggregation_exact": bool(
            frames["nested_graph"][
                "maximum_nested_weight_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G11_macro_transition_depends_on_source_occupancy": bool(
            frames["occupancy"][
                "mean_macro_row_tv"
            ].median()
            >= MIN_OCCUPANCY_MEDIAN_ROW_TV
        ),
        "G12_supplied_occupancy_flow_aggregation_exact": bool(
            frames["flow"][
                [
                    "maximum_flow_aggregation_error",
                    "maximum_macro_row_sum_error",
                ]
            ].max().max()
            <= MAX_EXACT_ERROR
        ),
        "G13_coarse_graining_declared_observable_relative_not_unique": True,
        "G14_no_physical_lambda_or_source_occupancy_claimed": True,
    }

    verdict = (
        "PASS_CORRECTED_OBSERVABLE_RELATIVE_COARSE_GRAINING_WITH_OCCUPANCY_OBSTRUCTION"
        if all(gates.values())
        else "FAIL_RZS_COARSE_GRAINING_AUDIT"
    )

    classification = [
        {
            "operator": "weighted arithmetic mean",
            "gauge_covariant": True,
            "refinement_consistent": True,
            "hierarchically_decomposable": True,
            "preserves_exponential_kernel": False,
            "status": "FIRST_MOMENT_COARSE_GRAINING",
        },
        {
            "operator": "exponential effective score",
            "gauge_covariant": True,
            "refinement_consistent": True,
            "hierarchically_decomposable": True,
            "preserves_exponential_kernel": True,
            "status": "KERNEL_SUFFICIENT_STATIC_MESSAGE",
        },
        {
            "operator": "weighted median",
            "gauge_covariant": True,
            "refinement_consistent": True,
            "hierarchically_decomposable": False,
            "preserves_exponential_kernel": False,
            "status": "ROBUST_BUT_SUMMARY_NOT_CLOSED",
        },
        {
            "operator": "minimum",
            "gauge_covariant": True,
            "refinement_consistent": True,
            "hierarchically_decomposable": True,
            "preserves_exponential_kernel": False,
            "status": "EXTREMAL_TROPICAL_LIMIT",
        },
        {
            "operator": "unweighted mean",
            "gauge_covariant": True,
            "refinement_consistent": False,
            "hierarchically_decomposable": "with counts, not supplied mu",
            "preserves_exponential_kernel": False,
            "status": "COUNTING_MEASURE_DEPENDENT",
        },
        {
            "operator": "macro transition from q alone",
            "gauge_covariant": "kernel dependent",
            "refinement_consistent": None,
            "hierarchically_decomposable": False,
            "preserves_exponential_kernel": None,
            "status": "SOURCE_OCCUPANCY_UNDERDETERMINED",
        },
        {
            "operator": "joint-flow aggregation with supplied pi",
            "gauge_covariant": "inherited from micro kernel",
            "refinement_consistent": True,
            "hierarchically_decomposable": True,
            "preserves_exponential_kernel": True,
            "status": "EXACT_DYNAMIC_COARSE_GRAINING_WITH_EXTRA_STATE",
        },
    ]

    pd.DataFrame(classification).to_csv(
        output / "a38_coarse_graining_classification.csv",
        index=False,
    )

    aggregate_results = {
        "associativity_results": (
            associativity_summary
        ),
        "kernel_preservation_results": (
            kernel_summary
        ),
        "median_unweighted_refinement_error": float(
            unweighted_refinement[
                "absolute_refinement_error"
            ].median()
        ),
        "median_occupancy_macro_row_tv": float(
            frames["occupancy"][
                "mean_macro_row_tv"
            ].median()
        ),
        "maximum_nested_graph_error": float(
            frames["nested_graph"][
                "maximum_nested_weight_error"
            ].max()
        ),
        "maximum_flow_aggregation_error": float(
            frames["flow"][
                "maximum_flow_aggregation_error"
            ].max()
        ),
        "weighted_median_exact_counterexample_difference": float(
            frames["median_counterexample"][
                "absolute_difference"
            ].iloc[0]
        ),
    }

    summary = {
        "seed": SEED,
        "lambda": LAMBDA,
        "aggregate_results": (
            aggregate_results
        ),
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "There is no observable-independent unique scalar "
            "coarse-graining of q. Within the regular decomposable "
            "translation-covariant quasi-arithmetic class, the arithmetic "
            "and exponential families survive. The arithmetic mean is the "
            "correct sufficient statistic for the first moment; the "
            "exponential effective score is the exact static sufficient "
            "message for the audited exponential kernel. For graph "
            "dynamics, q and edge weights alone do not determine a unique "
            "macro transition because the distribution of source occupancy "
            "inside each region matters. Exact dynamic aggregation is "
            "restored by carrying joint flows or an explicit occupancy "
            "measure."
        ),
        "interpretation_boundary": (
            "A38 determines consistency requirements relative to declared "
            "observables. It does not establish the physical exponential "
            "kernel, a physical lambda, a unique regional partition, or the "
            "occupancy measure required by dynamic coarse-graining."
        ),
    }

    (
        output / "a38_summary.json"
    ).write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A38.1 — Corrected RZS Coarse-Graining Audit",
        "",
        "## Main result",
        "",
        (
            "Coarse-graining is observable-relative. The exponential score "
            "is exact for the exponential kernel, while dynamic graph "
            "aggregation additionally requires source occupancy or flow."
        ),
        "",
        "## Scalar associativity",
        "",
    ]

    for item in associativity_summary:
        report_lines.extend(
            [
                f"### {item['operator']}",
                (
                    "- Pass rate: "
                    f"{item['associativity_pass_rate']:.6f}"
                ),
                (
                    "- Median error: "
                    f"{item['median_absolute_error']:.12g}"
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

    (
        output / "a38_report.md"
    ).write_text(
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
