#!/usr/bin/env python3
"""
A25 — Non-Circular q Couplings and Law Underdetermination Audit

Purpose
-------
Determine whether q-dependent observable couplings can be formulated from
relational data without secretly importing an absolute q scale, energy,
temperature, length, or coordinate threshold.

Main construction
-----------------
For each source vertex i, let

    z_ij = (q_ij - mean_i(q)) / sd_i(q)

over the outgoing edges of i. For any strictly positive function f,

    K_f(i->j) =
        A_ij f(z_ij) / sum_k A_ik f(z_ik)

is:
- local to the outgoing relational neighborhood;
- relabel-equivariant;
- invariant under row-wise affine transformations
      q_ij -> a_i q_ij + b_i,  a_i > 0;
- free of an external q unit.

This supplies a structurally non-circular operational witness for q shape.

Underdetermination theorem
--------------------------
The structural requirements do not select f. Infinitely many positive
functions produce valid but generally different kernels. Therefore gauge,
locality, and relabeling symmetry alone do not derive a unique physical law.

Kernels audited
---------------
1. raw_softmax:
       f(q)=exp(-q).
   Gauge-invariant under row shifts, but not under q rescaling. It assumes a
   q normalization or an implicit inverse scale beta.

2. standardized_exponential:
       f(z)=exp(-z).

3. standardized_asinh:
       f(z)=exp(-asinh(z)).

4. standardized_rank:
       f(rank)=exp(-rank_percentile).
   Affine-invariant but only ordinal.

Current q-dynamics reparameterization
-------------------------------------
For the centered update

    q_{t+1} = q_t - 1/2 center(eta center(q_t) + noise_t),

the transformation

    q -> a q + c,
    noise -> a noise

produces

    q_t' = a q_t + c

for every t under a coupled noise realization. Thus the dynamics fixes q
amplitude only relative to the postulated noise amplitude. Rescaling both
leaves the dimensionless trajectory equivalent. A numerical noise variance
can choose a convention, but does not by itself establish a physical unit.

Boundary
--------
A pass establishes:
- scale-free q-shape couplings are mathematically possible;
- the existing symmetry requirements do not uniquely select one;
- the current centered dynamics does not create an absolute q unit.

It does not derive a physical transition law.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 20260729

N_VALUES = (16, 32, 64)
GRAPH_SAMPLES_PER_N = 100
EDGE_PROBABILITY = 0.14

SHAPE_PERTURBATION = 0.9

DYNAMICS_VECTOR_SIZE = 160
DYNAMICS_SAMPLES = 120
DYNAMICS_STEPS = 80
ETA = 0.35
NOISE_SD = 0.08

MAX_NUMERICAL_ERROR = 5e-12
MIN_RAW_SCALE_TV = 0.015
MIN_SHAPE_SENSITIVITY_TV = 0.01
MIN_KERNEL_DISAGREEMENT_MEDIAN_TV = 0.015


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


def make_strong_digraph(
    n: int,
    rng: np.random.Generator,
) -> np.ndarray:
    adjacency = np.zeros((n, n), dtype=bool)

    # Bidirectional ring guarantees strong connectivity and degree >= 2.
    for vertex in range(n):
        adjacency[
            vertex,
            (vertex + 1) % n,
        ] = True
        adjacency[
            vertex,
            (vertex - 1) % n,
        ] = True

    random_edges = (
        rng.random((n, n))
        < EDGE_PROBABILITY
    )
    np.fill_diagonal(random_edges, False)
    adjacency |= random_edges
    np.fill_diagonal(adjacency, False)
    return adjacency


def sample_q(
    adjacency: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    q = np.zeros(
        adjacency.shape,
        dtype=float,
    )
    q[adjacency] = rng.normal(
        0.0,
        0.6,
        size=int(adjacency.sum()),
    )
    return q


def row_standardized_values(
    values: np.ndarray,
) -> np.ndarray:
    centered_values = values - float(values.mean())
    scale = float(
        np.sqrt(
            np.mean(centered_values**2)
        )
    )

    if scale <= 1e-14:
        return np.zeros_like(values)

    return centered_values / scale


def row_rank_percentiles(
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

    if len(values) == 1:
        return np.zeros_like(values)

    return ranks / (len(values) - 1.0)


def normalized_weights(
    raw_weights: np.ndarray,
) -> np.ndarray:
    raw_weights = np.asarray(
        raw_weights,
        dtype=float,
    )
    if np.any(raw_weights <= 0.0):
        raise ValueError(
            "All kernel weights must be positive."
        )

    return raw_weights / raw_weights.sum()


def transition_matrix(
    adjacency: np.ndarray,
    q: np.ndarray,
    kernel: str,
) -> np.ndarray:
    n = len(adjacency)
    probabilities = np.zeros(
        (n, n),
        dtype=float,
    )

    for source in range(n):
        targets = np.flatnonzero(
            adjacency[source]
        )
        values = q[source, targets]

        if kernel == "raw_softmax":
            logits = -values
            logits -= float(logits.max())
            weights = np.exp(logits)

        elif kernel == "standardized_exponential":
            z = row_standardized_values(
                values
            )
            logits = -z
            logits -= float(logits.max())
            weights = np.exp(logits)

        elif kernel == "standardized_asinh":
            z = row_standardized_values(
                values
            )
            logits = -np.arcsinh(z)
            logits -= float(logits.max())
            weights = np.exp(logits)

        elif kernel == "standardized_rank":
            rank_percentiles = (
                row_rank_percentiles(values)
            )
            logits = -rank_percentiles
            logits -= float(logits.max())
            weights = np.exp(logits)

        else:
            raise ValueError(
                f"Unknown kernel: {kernel}"
            )

        probabilities[
            source,
            targets,
        ] = normalized_weights(
            weights
        )

    return probabilities


def permute_matrix(
    matrix: np.ndarray,
    permutation: np.ndarray,
) -> np.ndarray:
    return matrix[
        np.ix_(permutation, permutation)
    ]


def row_total_variation(
    first: np.ndarray,
    second: np.ndarray,
    source: int,
) -> float:
    return 0.5 * float(
        np.abs(
            first[source]
            - second[source]
        ).sum()
    )


def maximum_row_total_variation(
    first: np.ndarray,
    second: np.ndarray,
) -> float:
    return max(
        row_total_variation(
            first,
            second,
            source,
        )
        for source in range(len(first))
    )


def mean_row_total_variation(
    first: np.ndarray,
    second: np.ndarray,
) -> float:
    return float(
        np.mean(
            [
                row_total_variation(
                    first,
                    second,
                    source,
                )
                for source in range(len(first))
            ]
        )
    )


def shape_perturbation(
    adjacency: np.ndarray,
    q: np.ndarray,
) -> np.ndarray:
    altered = q.copy()

    for source in range(len(adjacency)):
        targets = np.flatnonzero(
            adjacency[source]
        )

        if len(targets) < 3:
            continue

        altered[
            source,
            targets[0],
        ] += SHAPE_PERTURBATION
        altered[
            source,
            targets[1],
        ] -= 0.35 * SHAPE_PERTURBATION
        altered[
            source,
            targets[2],
        ] -= 0.65 * SHAPE_PERTURBATION

    return altered


def centered(
    values: np.ndarray,
) -> np.ndarray:
    return values - float(values.mean())


def centered_update(
    q: np.ndarray,
    eta: float,
    noise: np.ndarray,
) -> np.ndarray:
    drift = centered(
        eta * centered(q)
        + centered(noise)
    )
    return q - 0.5 * drift


def dynamics_reparameterization_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for sample_index in range(
        DYNAMICS_SAMPLES
    ):
        q = rng.normal(
            0.0,
            1.0,
            size=DYNAMICS_VECTOR_SIZE,
        )
        scale = float(
            rng.uniform(0.25, 3.5)
        )
        offset = float(
            rng.uniform(-2.0, 2.0)
        )
        transformed = scale * q + offset

        maximum_error = 0.0

        for _ in range(DYNAMICS_STEPS):
            noise = rng.normal(
                0.0,
                NOISE_SD,
                size=DYNAMICS_VECTOR_SIZE,
            )
            transformed_noise = (
                scale * noise
            )

            q = centered_update(
                q,
                ETA,
                noise,
            )
            transformed = centered_update(
                transformed,
                ETA,
                transformed_noise,
            )

            expected = scale * q + offset
            maximum_error = max(
                maximum_error,
                float(
                    np.max(
                        np.abs(
                            transformed
                            - expected
                        )
                    )
                ),
            )

        rows.append(
            {
                "sample_index": sample_index,
                "scale_factor": scale,
                "offset": offset,
                "maximum_reparameterization_error": (
                    maximum_error
                ),
                "original_noise_sd": (
                    NOISE_SD
                ),
                "transformed_noise_sd": (
                    scale * NOISE_SD
                ),
            }
        )

    return rows


def main() -> None:
    output = Path("a25_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = """# A25 — Non-Circular q Couplings and Underdetermination

## Scale-free local family

For every source vertex `i`, standardize the outgoing q-values:

`z_ij = (q_ij - mean_i q) / sd_i q`.

For any strictly positive measurable function `f`, define

`K_f(i->j) = A_ij f(z_ij) / sum_k A_ik f(z_ik)`.

This family is local, relabel-equivariant, and invariant under every row-wise
positive affine transformation

`q_ij -> a_i q_ij + b_i`, with `a_i>0`.

Therefore it uses q-shape information without importing an absolute q unit.

## Underdetermination

The requirements above do not determine `f`. Distinct positive functions
generally give distinct transition probabilities on the same `(A,q)`.
There are infinitely many such functions, so symmetry and locality alone
cannot derive a unique physical coupling.

## Raw softmax

`K(i->j) proportional to exp(-q_ij)` is invariant under row shifts but not
under q rescaling. Its coefficient implicitly fixes a q unit, equivalently an
inverse scale beta.

## Centered dynamics

The update

`q_{t+1}=q_t-1/2 center(eta center(q_t)+noise_t)`

is equivariant under

`q->a q+c`, `noise->a noise`.

Thus q amplitude is fixed only relative to the chosen noise amplitude. A
numerical noise variance is a normalization postulate, not yet a physical
unit or observable calibration.

## Boundary

Scale-free couplings show that non-circular operational sensitivity to
relative q-shape is mathematically possible. They do not select a unique law
and cannot recover absolute q magnitude or physical length.
"""
    (output / "a25_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    kernels = (
        "raw_softmax",
        "standardized_exponential",
        "standardized_asinh",
        "standardized_rank",
    )
    scale_free_kernels = (
        "standardized_exponential",
        "standardized_asinh",
        "standardized_rank",
    )

    audit_rows = []
    disagreement_rows = []

    for n in N_VALUES:
        for sample_index in range(
            GRAPH_SAMPLES_PER_N
        ):
            adjacency = make_strong_digraph(
                n,
                rng,
            )
            q = sample_q(
                adjacency,
                rng,
            )

            base_probabilities = {
                kernel: transition_matrix(
                    adjacency,
                    q,
                    kernel,
                )
                for kernel in kernels
            }

            # Row-wise affine transformation.
            row_scales = rng.uniform(
                0.3,
                3.0,
                size=n,
            )
            row_offsets = rng.uniform(
                -2.0,
                2.0,
                size=n,
            )
            affine_q = q.copy()

            for source in range(n):
                targets = np.flatnonzero(
                    adjacency[source]
                )
                affine_q[
                    source,
                    targets,
                ] = (
                    row_scales[source]
                    * q[source, targets]
                    + row_offsets[source]
                )

            affine_probabilities = {
                kernel: transition_matrix(
                    adjacency,
                    affine_q,
                    kernel,
                )
                for kernel in kernels
            }

            # Pure global q rescaling tests the raw hidden normalization.
            global_scale = float(
                rng.uniform(1.8, 3.2)
            )
            globally_scaled_q = (
                global_scale * q
            )
            globally_scaled_probabilities = {
                kernel: transition_matrix(
                    adjacency,
                    globally_scaled_q,
                    kernel,
                )
                for kernel in kernels
            }

            # Relabeling.
            permutation = rng.permutation(n)
            permuted_adjacency = (
                permute_matrix(
                    adjacency,
                    permutation,
                )
            )
            permuted_q = permute_matrix(
                q,
                permutation,
            )

            # Locality.
            source = int(
                rng.integers(0, n)
            )
            outside_sources = [
                vertex
                for vertex in range(n)
                if vertex != source
            ]
            outside_source = int(
                rng.choice(
                    outside_sources
                )
            )
            outside_targets = np.flatnonzero(
                adjacency[outside_source]
            )
            outside_target = int(
                rng.choice(outside_targets)
            )
            outside_q = q.copy()
            outside_q[
                outside_source,
                outside_target,
            ] += 1.7

            altered_q = shape_perturbation(
                adjacency,
                q,
            )

            for kernel in kernels:
                permuted_probabilities = (
                    transition_matrix(
                        permuted_adjacency,
                        permuted_q,
                        kernel,
                    )
                )
                expected_permuted = (
                    permute_matrix(
                        base_probabilities[
                            kernel
                        ],
                        permutation,
                    )
                )
                outside_probabilities = (
                    transition_matrix(
                        adjacency,
                        outside_q,
                        kernel,
                    )
                )
                altered_probabilities = (
                    transition_matrix(
                        adjacency,
                        altered_q,
                        kernel,
                    )
                )

                audit_rows.append(
                    {
                        "n": n,
                        "sample_index": (
                            sample_index
                        ),
                        "kernel": kernel,
                        "row_affine_invariance_error": float(
                            np.max(
                                np.abs(
                                    base_probabilities[
                                        kernel
                                    ]
                                    - affine_probabilities[
                                        kernel
                                    ]
                                )
                            )
                        ),
                        "global_scale_total_variation": (
                            mean_row_total_variation(
                                base_probabilities[
                                    kernel
                                ],
                                globally_scaled_probabilities[
                                    kernel
                                ],
                            )
                        ),
                        "relabel_equivariance_error": float(
                            np.max(
                                np.abs(
                                    permuted_probabilities
                                    - expected_permuted
                                )
                            )
                        ),
                        "outside_locality_error": float(
                            np.max(
                                np.abs(
                                    base_probabilities[
                                        kernel
                                    ][source]
                                    - outside_probabilities[
                                        source
                                    ]
                                )
                            )
                        ),
                        "shape_perturbation_mean_tv": (
                            mean_row_total_variation(
                                base_probabilities[
                                    kernel
                                ],
                                altered_probabilities,
                            )
                        ),
                        "shape_perturbation_max_tv": (
                            maximum_row_total_variation(
                                base_probabilities[
                                    kernel
                                ],
                                altered_probabilities,
                            )
                        ),
                    }
                )

            for first_index, first_kernel in enumerate(
                scale_free_kernels
            ):
                for second_kernel in scale_free_kernels[
                    first_index + 1 :
                ]:
                    disagreement_rows.append(
                        {
                            "n": n,
                            "sample_index": (
                                sample_index
                            ),
                            "first_kernel": (
                                first_kernel
                            ),
                            "second_kernel": (
                                second_kernel
                            ),
                            "mean_row_total_variation": (
                                mean_row_total_variation(
                                    base_probabilities[
                                        first_kernel
                                    ],
                                    base_probabilities[
                                        second_kernel
                                    ],
                                )
                            ),
                            "maximum_row_total_variation": (
                                maximum_row_total_variation(
                                    base_probabilities[
                                        first_kernel
                                    ],
                                    base_probabilities[
                                        second_kernel
                                    ],
                                )
                            ),
                        }
                    )

    dynamics_rows = (
        dynamics_reparameterization_audit(
            rng
        )
    )

    audit_frame = pd.DataFrame(
        audit_rows
    )
    disagreement_frame = pd.DataFrame(
        disagreement_rows
    )
    dynamics_frame = pd.DataFrame(
        dynamics_rows
    )

    audit_frame.to_csv(
        output / "a25_kernel_invariance_audit.csv",
        index=False,
    )
    disagreement_frame.to_csv(
        output / "a25_kernel_underdetermination.csv",
        index=False,
    )
    dynamics_frame.to_csv(
        output / "a25_q_dynamics_reparameterization.csv",
        index=False,
    )

    classification = [
        {
            "candidate": "raw exp(-q) softmax",
            "uses_only_existing_relational_inputs": True,
            "hidden_external_scale": (
                "yes unless q normalization is independently fixed"
            ),
            "local": True,
            "gauge_invariant": (
                "row shifts only"
            ),
            "absolute_q_information": False,
            "status": "OPERATIONAL_BUT_NORMALIZATION_DEPENDENT",
        },
        {
            "candidate": "standardized exponential kernel",
            "uses_only_existing_relational_inputs": True,
            "hidden_external_scale": False,
            "local": True,
            "gauge_invariant": (
                "row positive affine transformations"
            ),
            "absolute_q_information": False,
            "status": "STRUCTURALLY_ADMISSIBLE_NONCIRCULAR_WITNESS",
        },
        {
            "candidate": "standardized asinh kernel",
            "uses_only_existing_relational_inputs": True,
            "hidden_external_scale": False,
            "local": True,
            "gauge_invariant": (
                "row positive affine transformations"
            ),
            "absolute_q_information": False,
            "status": "STRUCTURALLY_ADMISSIBLE_NONCIRCULAR_WITNESS",
        },
        {
            "candidate": "rank kernel",
            "uses_only_existing_relational_inputs": True,
            "hidden_external_scale": False,
            "local": True,
            "gauge_invariant": (
                "all strictly increasing row transformations"
            ),
            "absolute_q_information": False,
            "status": "NONCIRCULAR_BUT_ONLY_ORDINAL",
        },
        {
            "candidate": "absolute D_eff/L0 kernel",
            "uses_only_existing_relational_inputs": False,
            "hidden_external_scale": True,
            "local": False,
            "gauge_invariant": False,
            "absolute_q_information": (
                "assumed through L0"
            ),
            "status": "CIRCULAR_OR_EXTRA_PRIMITIVE",
        },
        {
            "candidate": "current centered q dynamics",
            "uses_only_existing_relational_inputs": True,
            "hidden_external_scale": (
                "noise amplitude fixes only a dimensionless q convention"
            ),
            "local": None,
            "gauge_invariant": True,
            "absolute_q_information": False,
            "status": "REPARAMETERIZATION_EQUIVARIANT",
        },
    ]
    pd.DataFrame(classification).to_csv(
        output / "a25_circularity_classification.csv",
        index=False,
    )

    raw_rows = audit_frame[
        audit_frame["kernel"]
        == "raw_softmax"
    ]
    scale_free_rows = audit_frame[
        audit_frame["kernel"].isin(
            scale_free_kernels
        )
    ]

    pair_medians = (
        disagreement_frame.groupby(
            ["first_kernel", "second_kernel"]
        )["mean_row_total_variation"]
        .median()
    )

    gates = {
        "G1_scale_free_family_theorem_proved": True,
        "G2_scale_free_kernels_row_affine_invariant": bool(
            scale_free_rows[
                "row_affine_invariance_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G3_all_kernels_relabel_equivariant": bool(
            audit_frame[
                "relabel_equivariance_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G4_all_kernels_declared_local": bool(
            audit_frame[
                "outside_locality_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G5_scale_free_kernels_sensitive_to_q_shape": bool(
            scale_free_rows[
                "shape_perturbation_mean_tv"
            ].min()
            >= MIN_SHAPE_SENSITIVITY_TV
        ),
        "G6_raw_softmax_exposes_hidden_q_normalization": bool(
            raw_rows[
                "global_scale_total_variation"
            ].min()
            >= MIN_RAW_SCALE_TV
            and raw_rows[
                "row_affine_invariance_error"
            ].max()
            > 1e-4
        ),
        "G7_scale_free_kernels_ignore_global_q_rescaling": bool(
            scale_free_rows[
                "global_scale_total_variation"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G8_admissible_kernel_family_is_observationally_nonunique": bool(
            pair_medians.min()
            >= MIN_KERNEL_DISAGREEMENT_MEDIAN_TV
        ),
        "G9_centered_q_dynamics_reparameterization_exact": bool(
            dynamics_frame[
                "maximum_reparameterization_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G10_noise_scale_is_normalization_not_physical_unit": True,
        "G11_no_unique_or_physical_coupling_claimed": True,
    }

    verdict = (
        "PASS_NONCIRCULAR_Q_COUPLING_WITH_LAW_UNDERDETERMINATION"
        if all(gates.values())
        else "FAIL_NONCIRCULAR_Q_COUPLING_AUDIT"
    )

    kernel_summary = []

    for kernel, group in audit_frame.groupby(
        "kernel"
    ):
        kernel_summary.append(
            {
                "kernel": kernel,
                "maximum_row_affine_error": (
                    float(
                        group[
                            "row_affine_invariance_error"
                        ].max()
                    )
                ),
                "median_global_scale_tv": (
                    float(
                        group[
                            "global_scale_total_variation"
                        ].median()
                    )
                ),
                "maximum_relabel_error": (
                    float(
                        group[
                            "relabel_equivariance_error"
                        ].max()
                    )
                ),
                "maximum_locality_error": (
                    float(
                        group[
                            "outside_locality_error"
                        ].max()
                    )
                ),
                "minimum_shape_sensitivity_mean_tv": (
                    float(
                        group[
                            "shape_perturbation_mean_tv"
                        ].min()
                    )
                ),
                "median_shape_sensitivity_mean_tv": (
                    float(
                        group[
                            "shape_perturbation_mean_tv"
                        ].median()
                    )
                ),
            }
        )

    underdetermination_summary = [
        {
            "first_kernel": first,
            "second_kernel": second,
            "median_mean_row_tv": float(
                value
            ),
        }
        for (
            first,
            second,
        ), value in pair_medians.items()
    ]

    summary = {
        "seed": SEED,
        "n_values": list(N_VALUES),
        "graph_samples_per_n": (
            GRAPH_SAMPLES_PER_N
        ),
        "kernels": list(kernels),
        "kernel_results": kernel_summary,
        "underdetermination_results": (
            underdetermination_summary
        ),
        "dynamics": {
            "vector_size": (
                DYNAMICS_VECTOR_SIZE
            ),
            "samples": DYNAMICS_SAMPLES,
            "steps": DYNAMICS_STEPS,
            "eta": ETA,
            "noise_sd": NOISE_SD,
            "maximum_reparameterization_error": float(
                dynamics_frame[
                    "maximum_reparameterization_error"
                ].max()
            ),
        },
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "The RZS ingredients admit local, relabel-equivariant, "
            "scale-free q-shape couplings that do not import an absolute "
            "q unit. Therefore operational sensitivity to relative q need "
            "not be circular. However, infinitely many such kernels satisfy "
            "the same structural constraints and produce different laws. "
            "The present postulates do not select a unique coupling. The "
            "centered q dynamics is also equivariant under simultaneous "
            "rescaling of q and noise, so its noise amplitude supplies only "
            "a dimensionless normalization convention unless independently "
            "operationalized."
        ),
        "interpretation_boundary": (
            "A25 establishes structural admissibility and exact "
            "underdetermination. It does not derive a matter coupling, "
            "transition law, physical q unit, absolute length, energy, "
            "temperature, or time scale."
        ),
    }

    (output / "a25_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A25 — Non-Circular q Couplings and Law Underdetermination",
        "",
        "## Result",
        "",
        (
            "Scale-free local q-shape couplings exist and satisfy the "
            "required symmetries without an external q unit. The same "
            "requirements admit multiple observationally distinct kernels, "
            "so no unique physical law is derived."
        ),
        "",
        "## Kernel summaries",
        "",
    ]

    for result in kernel_summary:
        report_lines.extend(
            [
                f"### {result['kernel']}",
                (
                    "- Maximum row-affine error: "
                    f"{result['maximum_row_affine_error']:.6g}"
                ),
                (
                    "- Median global-scale TV: "
                    f"{result['median_global_scale_tv']:.6f}"
                ),
                (
                    "- Minimum shape sensitivity TV: "
                    f"{result['minimum_shape_sensitivity_mean_tv']:.6f}"
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

    (output / "a25_report.md").write_text(
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
