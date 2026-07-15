#!/usr/bin/env python3
"""
A24.1 — Corrective Operational Origin of q Audit

Question
--------
When does an RZS q-field become operational rather than merely mathematical?

Operational criterion
---------------------
A q-field is operational only if a specified observable law K(O|R,q):

1. depends nontrivially on gauge-invariant information in q;
2. is invariant under the accepted q gauge;
3. is equivariant under relabeling;
4. is local according to a preregistered relational neighborhood;
5. permits at least some q information to be inferred from observations.

Witness coupling
----------------
On a directed graph with adjacency A and edge field q, define the local
transition law

    P(i -> j | q) =
        A_ij exp(-beta q_ij)
        / sum_k A_ik exp(-beta q_ik).

This law:
- uses no external coordinates;
- is local to outgoing edges of i;
- is invariant under q_ij -> q_ij + c;
- is relabel-equivariant;
- makes local q contrasts observable when beta is known:

    log[P(i->j)/P(i->k)] = -beta (q_ij-q_ik).

Limits
------
The witness does not derive a physical RZS transition law. It also has two
identifiability degeneracies:

1. row offsets q_ij -> q_ij + c_i are invisible to this local softmax;
2. q -> a q and beta -> beta/a leave all probabilities unchanged.

Thus observations identify beta times q-contrasts. A calibrated beta or q
unit is required to infer q magnitudes.

Negative controls
-----------------
- q determined by the graph/order is redundant.
- an arbitrary q-field is operationally silent if the observable kernel
  ignores q.

Boundary
--------
This audit establishes a mathematically valid operationalization template and
its exact limitations. It does not show that the actual RZS q is generated,
measured, or coupled in this way.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 20260728

N_VALUES = (16, 32, 64)
GRAPH_SAMPLES_PER_N = 80

EDGE_PROBABILITY = 0.12
BETA = 1.4
LOCAL_PERTURBATION = 1.0
STRUCTURED_PERTURBATION = 0.75

TRANSITION_TRIALS_PER_NODE = 30_000
PATH_STEPS = 80

MAX_NUMERICAL_ERROR = 3e-12
MAX_CONTRAST_RMSE = 0.035
MIN_PATH_DIVERGENCE_RATE = 0.95
MAX_MEDIAN_FIRST_DIVERGENCE_STEP = 8.0


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

    # Bidirectional ring: strong connectivity and outdegree >= 2.
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
        0.55,
        size=int(adjacency.sum()),
    )
    return q


def order_derived_q(
    adjacency: np.ndarray,
) -> np.ndarray:
    indegree = adjacency.sum(axis=0)
    outdegree = adjacency.sum(axis=1)

    q = np.zeros(
        adjacency.shape,
        dtype=float,
    )
    rows, columns = np.nonzero(adjacency)
    q[rows, columns] = np.log1p(
        indegree[columns]
        + outdegree[rows]
    )
    return q


def transition_matrix(
    adjacency: np.ndarray,
    q: np.ndarray,
    beta_value: float,
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
        logits = (
            -beta_value
            * q[source, targets]
        )
        logits -= float(logits.max())
        weights = np.exp(logits)
        probabilities[source, targets] = (
            weights / weights.sum()
        )

    return probabilities


def uniform_transition_matrix(
    adjacency: np.ndarray,
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
        probabilities[
            source,
            targets,
        ] = 1.0 / len(targets)

    return probabilities


def permute_matrix(
    matrix: np.ndarray,
    permutation: np.ndarray,
) -> np.ndarray:
    return matrix[
        np.ix_(permutation, permutation)
    ]


def inverse_permutation(
    permutation: np.ndarray,
) -> np.ndarray:
    inverse = np.empty_like(permutation)
    inverse[permutation] = np.arange(
        len(permutation)
    )
    return inverse


def categorical_choice(
    probabilities: np.ndarray,
    uniform_value: float,
) -> int:
    cumulative = np.cumsum(probabilities)
    target = min(
        float(uniform_value),
        np.nextafter(1.0, 0.0),
    )
    return int(
        np.searchsorted(
            cumulative,
            target,
            side="right",
        )
    )


def simulate_path(
    probabilities: np.ndarray,
    start: int,
    random_tape: np.ndarray,
) -> list[int]:
    current = int(start)
    path = [current]

    for uniform_value in random_tape:
        current = categorical_choice(
            probabilities[current],
            float(uniform_value),
        )
        path.append(current)

    return path


def first_path_divergence(
    first: list[int],
    second: list[int],
) -> int | None:
    for index, (a, b) in enumerate(
        zip(first, second)
    ):
        if a != b:
            return index
    return None


def row_total_variation(
    first: np.ndarray,
    second: np.ndarray,
    source: int,
) -> float:
    return 0.5 * float(
        np.abs(
            first[source] - second[source]
        ).sum()
    )


def structured_q_perturbation(
    adjacency: np.ndarray,
    q: np.ndarray,
) -> np.ndarray:
    altered = q.copy()

    for source in range(len(adjacency)):
        targets = np.flatnonzero(
            adjacency[source]
        )
        midpoint = len(targets) // 2
        altered[
            source,
            targets[:midpoint],
        ] += STRUCTURED_PERTURBATION
        altered[
            source,
            targets[midpoint:],
        ] -= STRUCTURED_PERTURBATION

    return altered


def recover_q_contrasts(
    adjacency: np.ndarray,
    q: np.ndarray,
    probabilities: np.ndarray,
    rng: np.random.Generator,
) -> tuple[float, int]:
    squared_errors = []
    comparison_count = 0

    for source in range(len(adjacency)):
        targets = np.flatnonzero(
            adjacency[source]
        )
        counts = rng.multinomial(
            TRANSITION_TRIALS_PER_NODE,
            probabilities[source, targets],
        )
        reference_index = int(
            np.argmax(counts)
        )
        reference_target = int(
            targets[reference_index]
        )

        for local_index, target in enumerate(
            targets
        ):
            if local_index == reference_index:
                continue

            estimated_log_ratio = math.log(
                (counts[local_index] + 0.5)
                / (counts[reference_index] + 0.5)
            )
            estimated_contrast = (
                -estimated_log_ratio / BETA
            )
            true_contrast = (
                q[source, target]
                - q[
                    source,
                    reference_target,
                ]
            )
            squared_errors.append(
                (
                    estimated_contrast
                    - true_contrast
                )
                ** 2
            )
            comparison_count += 1

    return (
        float(
            math.sqrt(
                np.mean(squared_errors)
            )
        ),
        comparison_count,
    )


def main() -> None:
    output = Path("a24_1_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = """# A24.1 — Corrective Operational Criterion for the RZS q-Field

## Criterion

A q-field is operational relative to an observation class only when there is
a specified observable kernel `K(O|R,q)` that is not constant on
gauge-inequivalent q configurations.

A valid relational operationalization should satisfy:

1. gauge invariance;
2. relabeling equivariance;
3. declared relational locality;
4. nontrivial sensitivity to gauge-invariant q contrasts;
5. inferability of at least some q information from observable frequencies.

## Local transition witness

For a directed graph,

`P(i->j|q) proportional to A_ij exp(-beta q_ij)`.

It obeys

`log(P(i->j)/P(i->k)) = -beta(q_ij-q_ik)`.

Therefore q contrasts are statistically recoverable when beta is calibrated.

## Identifiability limits

- Adding a common q offset leaves the transition law unchanged.
- This particular local coupling is also invariant under a separate offset
  for every source row.
- Replacing q by `a q` and beta by `beta/a` leaves the law unchanged.

Thus the observation identifies only dimensionless products of a coupling
strength with local q contrasts.

## Negative statements

- q inferred only from the relation contains no information beyond it.
- q with no q-dependent observable coupling is empirically silent.

## Boundary

The softmax kernel is a mathematical witness, not an asserted law of the RZS.
The actual origin and operational coupling of q remain unresolved unless the
theory supplies them independently.
"""
    (output / "a24_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    audit_rows = []
    recovery_rows = []
    path_rows = []

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
            probabilities = transition_matrix(
                adjacency,
                q,
                BETA,
            )

            # Negative control 1: q derived from the relation.
            derived_first = order_derived_q(
                adjacency
            )
            derived_second = order_derived_q(
                adjacency
            )

            # Negative control 2: arbitrary q is silent if the kernel ignores it.
            arbitrary_other_q = sample_q(
                adjacency,
                rng,
            )
            silent_first = (
                uniform_transition_matrix(
                    adjacency
                )
            )
            silent_second = (
                uniform_transition_matrix(
                    adjacency
                )
            )

            # Global gauge.
            gauge_offset = float(
                rng.uniform(-2.5, 2.5)
            )
            shifted_q = q.copy()
            shifted_q[adjacency] += (
                gauge_offset
            )
            shifted_probabilities = (
                transition_matrix(
                    adjacency,
                    shifted_q,
                    BETA,
                )
            )

            # Source-row gauge, an additional invariance of this witness.
            row_offsets = rng.uniform(
                -1.5,
                1.5,
                size=n,
            )
            row_shifted_q = q.copy()
            for source in range(n):
                row_shifted_q[
                    source,
                    adjacency[source],
                ] += row_offsets[source]
            row_shifted_probabilities = (
                transition_matrix(
                    adjacency,
                    row_shifted_q,
                    BETA,
                )
            )

            # Relabeling equivariance.
            permutation = rng.permutation(n)
            permuted_adjacency = permute_matrix(
                adjacency,
                permutation,
            )
            permuted_q = permute_matrix(
                q,
                permutation,
            )
            permuted_probabilities = (
                transition_matrix(
                    permuted_adjacency,
                    permuted_q,
                    BETA,
                )
            )
            expected_permuted_probabilities = (
                permute_matrix(
                    probabilities,
                    permutation,
                )
            )

            # Locality and local contrast sensitivity.
            source = int(
                rng.integers(0, n)
            )
            targets = np.flatnonzero(
                adjacency[source]
            )
            first_target = int(targets[0])
            second_target = int(targets[1])

            outside_q = q.copy()
            outside_sources = [
                vertex
                for vertex in range(n)
                if vertex != source
            ]
            outside_source = int(
                rng.choice(outside_sources)
            )
            outside_targets = np.flatnonzero(
                adjacency[outside_source]
            )
            outside_target = int(
                rng.choice(outside_targets)
            )
            outside_q[
                outside_source,
                outside_target,
            ] += 1.75
            outside_probabilities = (
                transition_matrix(
                    adjacency,
                    outside_q,
                    BETA,
                )
            )

            local_q = q.copy()
            local_q[
                source,
                first_target,
            ] += LOCAL_PERTURBATION
            local_q[
                source,
                second_target,
            ] -= LOCAL_PERTURBATION
            local_probabilities = (
                transition_matrix(
                    adjacency,
                    local_q,
                    BETA,
                )
            )
            local_tv = row_total_variation(
                probabilities,
                local_probabilities,
                source,
            )
            base_log_odds = math.log(
                probabilities[source, first_target]
                / probabilities[source, second_target]
            )
            altered_log_odds = math.log(
                local_probabilities[source, first_target]
                / local_probabilities[source, second_target]
            )
            expected_log_odds_shift = (
                -2.0 * BETA * LOCAL_PERTURBATION
            )
            local_log_odds_shift_error = abs(
                (altered_log_odds - base_log_odds)
                - expected_log_odds_shift
            )

            # beta-q scale degeneracy.
            scale_factor = float(
                rng.uniform(0.35, 2.8)
            )
            scaled_probabilities = (
                transition_matrix(
                    adjacency,
                    scale_factor * q,
                    BETA / scale_factor,
                )
            )

            contrast_rmse, comparisons = (
                recover_q_contrasts(
                    adjacency,
                    q,
                    probabilities,
                    rng,
                )
            )
            recovery_rows.append(
                {
                    "n": n,
                    "sample_index": sample_index,
                    "contrast_rmse": (
                        contrast_rmse
                    ),
                    "comparisons": comparisons,
                }
            )

            # Coupled paths under equivalent and inequivalent q.
            random_tape = rng.random(
                PATH_STEPS
            )
            start = int(
                rng.integers(0, n)
            )
            base_path = simulate_path(
                probabilities,
                start,
                random_tape,
            )
            gauge_path = simulate_path(
                shifted_probabilities,
                start,
                random_tape,
            )

            altered_q = (
                structured_q_perturbation(
                    adjacency,
                    q,
                )
            )
            altered_probabilities = (
                transition_matrix(
                    adjacency,
                    altered_q,
                    BETA,
                )
            )
            altered_path = simulate_path(
                altered_probabilities,
                start,
                random_tape,
            )
            divergence = first_path_divergence(
                base_path,
                altered_path,
            )

            path_rows.append(
                {
                    "n": n,
                    "sample_index": sample_index,
                    "gauge_equivalent_path_identical": (
                        base_path == gauge_path
                    ),
                    "gauge_inequivalent_path_diverged": (
                        divergence is not None
                    ),
                    "first_divergence_step": (
                        divergence
                    ),
                }
            )

            audit_rows.append(
                {
                    "n": n,
                    "sample_index": sample_index,
                    "order_derived_q_identical": bool(
                        np.array_equal(
                            derived_first,
                            derived_second,
                        )
                    ),
                    "silent_kernel_identical_for_distinct_q": bool(
                        np.array_equal(
                            silent_first,
                            silent_second,
                        )
                        and not np.array_equal(
                            q,
                            arbitrary_other_q,
                        )
                    ),
                    "global_gauge_probability_error": float(
                        np.max(
                            np.abs(
                                probabilities
                                - shifted_probabilities
                            )
                        )
                    ),
                    "row_gauge_probability_error": float(
                        np.max(
                            np.abs(
                                probabilities
                                - row_shifted_probabilities
                            )
                        )
                    ),
                    "relabel_equivariance_error": float(
                        np.max(
                            np.abs(
                                permuted_probabilities
                                - expected_permuted_probabilities
                            )
                        )
                    ),
                    "outside_locality_row_error": float(
                        np.max(
                            np.abs(
                                probabilities[source]
                                - outside_probabilities[
                                    source
                                ]
                            )
                        )
                    ),
                    "local_contrast_total_variation": (
                        local_tv
                    ),
                    "local_log_odds_shift_error": (
                        local_log_odds_shift_error
                    ),
                    "beta_q_scale_degeneracy_error": float(
                        np.max(
                            np.abs(
                                probabilities
                                - scaled_probabilities
                            )
                        )
                    ),
                }
            )

    audit_frame = pd.DataFrame(
        audit_rows
    )
    recovery_frame = pd.DataFrame(
        recovery_rows
    )
    path_frame = pd.DataFrame(
        path_rows
    )

    audit_frame.to_csv(
        output / "a24_operational_kernel_audit.csv",
        index=False,
    )
    recovery_frame.to_csv(
        output / "a24_q_contrast_recovery.csv",
        index=False,
    )
    path_frame.to_csv(
        output / "a24_path_coupling_audit.csv",
        index=False,
    )

    path_divergent = path_frame[
        path_frame[
            "gauge_inequivalent_path_diverged"
        ]
    ]

    classification = [
        {
            "candidate": "q inferred from relation",
            "operational_new_information": False,
            "reason": "deterministic recoding of observed graph/order",
            "status": "REDUNDANT",
        },
        {
            "candidate": "free q with no q-dependent observation",
            "operational_new_information": False,
            "reason": "latent variation has no observable consequence",
            "status": "EMPIRICALLY_SILENT",
        },
        {
            "candidate": "local softmax transition coupling",
            "operational_new_information": True,
            "reason": "transition odds depend on local q contrasts",
            "status": "MATHEMATICAL_OPERATIONAL_WITNESS",
        },
        {
            "candidate": "absolute q offset",
            "operational_new_information": False,
            "reason": "removed by global and row softmax normalization",
            "status": "GAUGE_UNIDENTIFIABLE",
        },
        {
            "candidate": "q contrast with known beta",
            "operational_new_information": True,
            "reason": "recoverable from log transition odds",
            "status": "STATISTICALLY_IDENTIFIABLE",
        },
        {
            "candidate": "q contrast with unknown beta",
            "operational_new_information": "only beta times contrast",
            "reason": "q->a q and beta->beta/a leave observations unchanged",
            "status": "CALIBRATION_DEGENERACY",
        },
        {
            "candidate": "actual RZS q",
            "operational_new_information": None,
            "reason": "no independently established measurement or coupling law in this audit",
            "status": "OPERATIONAL_ORIGIN_UNRESOLVED",
        },
    ]
    pd.DataFrame(classification).to_csv(
        output / "a24_operational_classification.csv",
        index=False,
    )

    gates = {
        "G1_order_derived_q_redundant": bool(
            audit_frame[
                "order_derived_q_identical"
            ].all()
        ),
        "G2_uncoupled_q_empirically_silent": bool(
            audit_frame[
                "silent_kernel_identical_for_distinct_q"
            ].all()
        ),
        "G3_global_q_gauge_invariant": bool(
            audit_frame[
                "global_gauge_probability_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G4_relabeling_equivariant": bool(
            audit_frame[
                "relabel_equivariance_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G5_declared_locality_holds": bool(
            audit_frame[
                "outside_locality_row_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G6_local_q_contrast_changes_observable_law": bool(
            audit_frame[
                "local_log_odds_shift_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
            and audit_frame[
                "local_contrast_total_variation"
            ].min()
            > 0.0
        ),
        "G7_gauge_equivalent_paths_identical": bool(
            path_frame[
                "gauge_equivalent_path_identical"
            ].all()
        ),
        "G8_gauge_inequivalent_paths_diverge": bool(
            path_frame[
                "gauge_inequivalent_path_diverged"
            ].mean()
            >= MIN_PATH_DIVERGENCE_RATE
            and float(
                path_divergent[
                    "first_divergence_step"
                ].median()
            )
            <= MAX_MEDIAN_FIRST_DIVERGENCE_STEP
        ),
        "G9_q_contrasts_recoverable_when_beta_known": bool(
            recovery_frame[
                "contrast_rmse"
            ].mean()
            <= MAX_CONTRAST_RMSE
        ),
        "G10_beta_q_scale_degeneracy_exact": bool(
            audit_frame[
                "beta_q_scale_degeneracy_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G11_local_kernel_has_additional_row_offset_gauge": bool(
            audit_frame[
                "row_gauge_probability_error"
            ].max()
            <= MAX_NUMERICAL_ERROR
        ),
        "G12_actual_rzs_operational_origin_not_assumed": True,
    }

    verdict = (
        "PASS_Q_OPERATIONALIZATION_CRITERIA_WITH_CALIBRATION_LIMIT_CORRECTED"
        if all(gates.values())
        else "FAIL_Q_OPERATIONALIZATION_CRITERIA_AUDIT"
    )

    summary = {
        "seed": SEED,
        "n_values": list(N_VALUES),
        "graph_samples_per_n": (
            GRAPH_SAMPLES_PER_N
        ),
        "beta": BETA,
        "transition_trials_per_node": (
            TRANSITION_TRIALS_PER_NODE
        ),
        "path_steps": PATH_STEPS,
        "classification": classification,
        "aggregate_results": {
            "maximum_global_gauge_error": float(
                audit_frame[
                    "global_gauge_probability_error"
                ].max()
            ),
            "maximum_relabel_error": float(
                audit_frame[
                    "relabel_equivariance_error"
                ].max()
            ),
            "maximum_locality_error": float(
                audit_frame[
                    "outside_locality_row_error"
                ].max()
            ),
            "minimum_local_contrast_tv": float(
                audit_frame[
                    "local_contrast_total_variation"
                ].min()
            ),
            "maximum_local_log_odds_shift_error": float(
                audit_frame[
                    "local_log_odds_shift_error"
                ].max()
            ),
            "mean_contrast_recovery_rmse": float(
                recovery_frame[
                    "contrast_rmse"
                ].mean()
            ),
            "maximum_contrast_recovery_rmse": float(
                recovery_frame[
                    "contrast_rmse"
                ].max()
            ),
            "gauge_inequivalent_path_divergence_rate": float(
                path_frame[
                    "gauge_inequivalent_path_diverged"
                ].mean()
            ),
            "median_first_path_divergence": float(
                path_divergent[
                    "first_divergence_step"
                ].median()
            ),
            "maximum_beta_q_degeneracy_error": float(
                audit_frame[
                    "beta_q_scale_degeneracy_error"
                ].max()
            ),
        },
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "A q-field becomes operational only through a specified "
            "q-dependent observable law. The local transition witness "
            "shows that gauge-invariant q contrasts can be measured from "
            "relational transition frequencies without coordinates when "
            "the coupling beta is calibrated. The same observations do "
            "not identify absolute q offsets, row offsets for this kernel, "
            "or q magnitude separately from beta."
        ),
        "interpretation_boundary": (
            "The audit supplies criteria and a mathematical witness, not "
            "the missing physical bridge. The actual RZS q remains "
            "operationally ungrounded until its preparation, measurement, "
            "noise law, and coupling to observable events are specified "
            "independently of the desired emergent geometry."
        ),
    }

    (output / "a24_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A24.1 — Corrective Operational Origin of q",
        "",
        "## Result",
        "",
        (
            "A local, gauge-invariant and relabel-equivariant transition "
            "kernel makes q contrasts operationally measurable. It does "
            "not identify absolute q or its magnitude independently of "
            "the coupling calibration."
        ),
        "",
        "## Aggregate results",
        "",
        *[
            f"- {key}: {value}"
            for key, value
            in summary[
                "aggregate_results"
            ].items()
        ],
        "",
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

    (output / "a24_report.md").write_text(
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
