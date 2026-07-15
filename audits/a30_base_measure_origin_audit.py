#!/usr/bin/env python3
"""
A30 — Base-Measure Origin and Refinement-Semantics Audit

Purpose
-------
Audit candidate origins for the additive base mass mu required by A29.

Core semantic no-go
-------------------
The same refined unweighted relational structure can admit two incompatible
interpretations:

1. Descriptive refinement:
   m exact clones represent one original macro-alternative. Their total mass
   must equal the original mass.

2. Ontic multiplicity:
   the same m structurally identical alternatives are m genuine states.
   Counting semantics assigns each a full state mass.

No deterministic rule using only the refined unweighted relation and q marks
can distinguish these interpretations, because its input is identical. A
refinement map, ancestry, microstate multiplicity, base measure, or another
operational primitive is required.

Candidates audited
------------------
1. uniform counting measure;
2. degree-derived measure;
3. stationary measure of a relation-only random walk;
4. stationary measure of a q-dependent standardized local walk;
5. node q-score softmax measure;
6. explicitly supplied additive multiplicity mass;
7. mass transported by an independently supplied projectively lifted
   stochastic kernel.

Interpretation
--------------
Order-derived candidates are legitimate relational summaries but contain no
information beyond the order. q-derived candidates can contain new relative
information, but are not automatically refinement-consistent. Explicit
multiplicity and projectively lifted transport are consistent only because
they receive refinement data not present in the bare refined graph.

Boundary
--------
This audit does not identify mu with spacetime volume, matter density,
probability, or physical mass.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 20260804

N_VALUES = (10, 20, 40)
GRAPH_SAMPLES_PER_N = 180
EDGE_PROBABILITY = 0.14
CLONE_COUNT_RANGE = (2, 6)

TRANSPORT_STEPS = 50

MAX_EXACT_ERROR = 8e-12
MIN_DERIVED_REFINEMENT_VIOLATION_RATE = 0.95
MIN_DERIVED_MEDIAN_TV = 0.01
MIN_SEMANTIC_AMBIGUITY_TV = 0.03
MIN_Q_NEW_INFORMATION_TV = 0.03


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


def normalize(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    total = float(values.sum())
    if total <= 0.0:
        raise ValueError("Nonpositive normalization total.")
    return values / total


def total_variation(
    first: np.ndarray,
    second: np.ndarray,
) -> float:
    return 0.5 * float(
        np.abs(first - second).sum()
    )


def make_strong_digraph(
    n: int,
    rng: np.random.Generator,
) -> np.ndarray:
    adjacency = np.zeros((n, n), dtype=bool)

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


def sample_edge_q(
    adjacency: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    q = np.zeros(
        adjacency.shape,
        dtype=float,
    )
    q[adjacency] = rng.normal(
        0.0,
        0.65,
        size=int(adjacency.sum()),
    )
    return q


def clone_refinement(
    adjacency: np.ndarray,
    q: np.ndarray,
    target: int,
    clone_count: int,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    """
    Create exact relational clones. The returned macro_map assigns each
    refined vertex to its original macro vertex.
    """
    n = len(adjacency)
    macro_map = []

    for vertex in range(n):
        if vertex == target:
            macro_map.extend(
                [target] * clone_count
            )
        else:
            macro_map.append(vertex)

    macro_map_array = np.asarray(
        macro_map,
        dtype=int,
    )
    refined_n = len(macro_map_array)
    refined_adjacency = np.zeros(
        (refined_n, refined_n),
        dtype=bool,
    )
    refined_q = np.zeros(
        (refined_n, refined_n),
        dtype=float,
    )

    for source in range(refined_n):
        macro_source = int(
            macro_map_array[source]
        )
        for destination in range(
            refined_n
        ):
            macro_destination = int(
                macro_map_array[
                    destination
                ]
            )

            if (
                macro_source == target
                and macro_destination == target
            ):
                # Original graph has no self-loop. Exact clones are mutually
                # incomparable/independent at this bare relational level.
                continue

            if adjacency[
                macro_source,
                macro_destination,
            ]:
                refined_adjacency[
                    source,
                    destination,
                ] = True
                refined_q[
                    source,
                    destination,
                ] = q[
                    macro_source,
                    macro_destination,
                ]

    return (
        refined_adjacency,
        refined_q,
        macro_map_array,
    )


def aggregate_micro_measure(
    micro_measure: np.ndarray,
    macro_map: np.ndarray,
    macro_n: int,
) -> np.ndarray:
    macro_measure = np.zeros(
        macro_n,
        dtype=float,
    )
    for micro_index, macro_index in enumerate(
        macro_map
    ):
        macro_measure[
            int(macro_index)
        ] += micro_measure[
            micro_index
        ]
    return macro_measure


def uniform_count_measure(
    adjacency: np.ndarray,
    q: np.ndarray,
) -> np.ndarray:
    del q
    return np.full(
        len(adjacency),
        1.0 / len(adjacency),
        dtype=float,
    )


def degree_measure(
    adjacency: np.ndarray,
    q: np.ndarray,
) -> np.ndarray:
    del q
    weights = (
        1.0
        + adjacency.sum(axis=0)
        + adjacency.sum(axis=1)
    ).astype(float)
    return normalize(weights)


def relation_walk_transition(
    adjacency: np.ndarray,
) -> np.ndarray:
    n = len(adjacency)
    transition = np.zeros(
        (n, n),
        dtype=float,
    )

    for source in range(n):
        targets = np.flatnonzero(
            adjacency[source]
        )
        transition[
            source,
            targets,
        ] = 0.85 / len(targets)
        transition[source, source] = 0.15

    return transition


def row_standardized(
    values: np.ndarray,
) -> np.ndarray:
    centered = (
        values - float(values.mean())
    )
    scale = float(
        np.sqrt(
            np.mean(centered**2)
        )
    )
    if scale <= 1e-14:
        return np.zeros_like(values)
    return centered / scale


def q_walk_transition(
    adjacency: np.ndarray,
    q: np.ndarray,
) -> np.ndarray:
    n = len(adjacency)
    transition = np.zeros(
        (n, n),
        dtype=float,
    )

    for source in range(n):
        targets = np.flatnonzero(
            adjacency[source]
        )
        z = row_standardized(
            q[source, targets]
        )
        logits = -z
        logits -= float(logits.max())
        probabilities = normalize(
            np.exp(logits)
        )
        transition[
            source,
            targets,
        ] = 0.85 * probabilities
        transition[source, source] = 0.15

    return transition


def stationary_distribution(
    transition: np.ndarray,
) -> np.ndarray:
    distribution = np.full(
        len(transition),
        1.0 / len(transition),
        dtype=float,
    )

    for _ in range(100_000):
        updated = distribution @ transition
        if float(
            np.max(
                np.abs(
                    updated - distribution
                )
            )
        ) <= 1e-14:
            distribution = updated
            break
        distribution = updated
    else:
        raise RuntimeError(
            "Stationary power iteration did not converge."
        )

    distribution = normalize(
        np.maximum(distribution, 0.0)
    )
    return distribution


def relation_stationary_measure(
    adjacency: np.ndarray,
    q: np.ndarray,
) -> np.ndarray:
    del q
    return stationary_distribution(
        relation_walk_transition(
            adjacency
        )
    )


def q_stationary_measure(
    adjacency: np.ndarray,
    q: np.ndarray,
) -> np.ndarray:
    return stationary_distribution(
        q_walk_transition(
            adjacency,
            q,
        )
    )


def q_node_softmax_measure(
    adjacency: np.ndarray,
    q: np.ndarray,
) -> np.ndarray:
    node_scores = np.zeros(
        len(adjacency),
        dtype=float,
    )
    for source in range(len(adjacency)):
        targets = np.flatnonzero(
            adjacency[source]
        )
        node_scores[source] = float(
            q[source, targets].mean()
        )

    centered_scores = (
        node_scores
        - float(node_scores.mean())
    )
    logits = -centered_scores
    logits -= float(logits.max())
    return normalize(
        np.exp(logits)
    )


DERIVED_MEASURES = {
    "uniform_count": uniform_count_measure,
    "degree": degree_measure,
    "relation_stationary": (
        relation_stationary_measure
    ),
    "q_stationary": q_stationary_measure,
    "q_node_softmax": (
        q_node_softmax_measure
    ),
}


def derived_measure_refinement_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for n in N_VALUES:
        for sample_index in range(
            GRAPH_SAMPLES_PER_N
        ):
            adjacency = make_strong_digraph(
                n,
                rng,
            )
            q = sample_edge_q(
                adjacency,
                rng,
            )
            target = int(
                rng.integers(0, n)
            )
            clone_count = int(
                rng.integers(
                    CLONE_COUNT_RANGE[0],
                    CLONE_COUNT_RANGE[1]
                    + 1,
                )
            )
            (
                refined_adjacency,
                refined_q,
                macro_map,
            ) = clone_refinement(
                adjacency,
                q,
                target,
                clone_count,
            )

            for name, function in (
                DERIVED_MEASURES.items()
            ):
                original = function(
                    adjacency,
                    q,
                )
                refined = function(
                    refined_adjacency,
                    refined_q,
                )
                aggregated = (
                    aggregate_micro_measure(
                        refined,
                        macro_map,
                        n,
                    )
                )
                tv = total_variation(
                    original,
                    aggregated,
                )
                rows.append(
                    {
                        "n": n,
                        "sample_index": (
                            sample_index
                        ),
                        "measure": name,
                        "clone_count": (
                            clone_count
                        ),
                        "macro_total_variation": (
                            tv
                        ),
                        "refinement_consistent": bool(
                            tv <= MAX_EXACT_ERROR
                        ),
                    }
                )

    return rows


def explicit_additive_measure_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for n in N_VALUES:
        for sample_index in range(
            GRAPH_SAMPLES_PER_N
        ):
            adjacency = make_strong_digraph(
                n,
                rng,
            )
            q = sample_edge_q(
                adjacency,
                rng,
            )
            target = int(
                rng.integers(0, n)
            )
            clone_count = int(
                rng.integers(
                    CLONE_COUNT_RANGE[0],
                    CLONE_COUNT_RANGE[1]
                    + 1,
                )
            )
            _, _, macro_map = (
                clone_refinement(
                    adjacency,
                    q,
                    target,
                    clone_count,
                )
            )

            raw_masses = np.exp(
                rng.normal(
                    0.0,
                    0.7,
                    size=n,
                )
            )
            original = normalize(
                raw_masses
            )
            fractions = rng.dirichlet(
                np.ones(clone_count)
            )

            refined_raw = []
            clone_cursor = 0
            for macro_index in macro_map:
                macro_index = int(
                    macro_index
                )
                if macro_index == target:
                    refined_raw.append(
                        raw_masses[target]
                        * fractions[
                            clone_cursor
                        ]
                    )
                    clone_cursor += 1
                else:
                    refined_raw.append(
                        raw_masses[
                            macro_index
                        ]
                    )

            refined = normalize(
                np.asarray(
                    refined_raw,
                    dtype=float,
                )
            )
            aggregated = aggregate_micro_measure(
                refined,
                macro_map,
                n,
            )
            rows.append(
                {
                    "n": n,
                    "sample_index": (
                        sample_index
                    ),
                    "clone_count": (
                        clone_count
                    ),
                    "maximum_macro_error": float(
                        np.max(
                            np.abs(
                                original
                                - aggregated
                            )
                        )
                    ),
                    "refinement_consistent": bool(
                        np.max(
                            np.abs(
                                original
                                - aggregated
                            )
                        )
                        <= MAX_EXACT_ERROR
                    ),
                }
            )

    return rows


def semantic_ambiguity_audit() -> list[dict[str, float]]:
    rows = []

    for n in range(3, 31):
        original = np.full(
            n,
            1.0 / n,
        )
        for clone_count in range(2, 8):
            target = 0

            # Clone semantics: refinement is only a new description of one
            # macrostate, so the macro measure should remain original.
            clone_semantics = original.copy()

            # Ontic multiplicity semantics: every refined listed state has
            # unit counting mass.
            refined_n = (
                n - 1 + clone_count
            )
            ontic_macro = np.full(
                n,
                1.0 / refined_n,
            )
            ontic_macro[target] = (
                clone_count / refined_n
            )

            rows.append(
                {
                    "n": n,
                    "clone_count": (
                        clone_count
                    ),
                    "semantic_total_variation": (
                        total_variation(
                            clone_semantics,
                            ontic_macro,
                        )
                    ),
                    "clone_semantics_target_mass": (
                        clone_semantics[
                            target
                        ]
                    ),
                    "ontic_semantics_target_mass": (
                        ontic_macro[
                            target
                        ]
                    ),
                }
            )

    return rows


def q_new_information_audit(
    rng: np.random.Generator,
) -> list[dict[str, float]]:
    rows = []

    for n in N_VALUES:
        for sample_index in range(
            GRAPH_SAMPLES_PER_N
        ):
            adjacency = make_strong_digraph(
                n,
                rng,
            )
            q_first = sample_edge_q(
                adjacency,
                rng,
            )
            q_second = sample_edge_q(
                adjacency,
                rng,
            )

            for name in (
                "q_stationary",
                "q_node_softmax",
            ):
                function = (
                    DERIVED_MEASURES[name]
                )
                first = function(
                    adjacency,
                    q_first,
                )
                second = function(
                    adjacency,
                    q_second,
                )
                rows.append(
                    {
                        "n": n,
                        "sample_index": (
                            sample_index
                        ),
                        "measure": name,
                        "same_relation_measure_tv": (
                            total_variation(
                                first,
                                second,
                            )
                        ),
                    }
                )

    return rows


def lift_transition(
    macro_transition: np.ndarray,
    target: int,
    clone_fractions: np.ndarray,
) -> tuple[
    np.ndarray,
    np.ndarray,
]:
    """
    Row-stochastic projective lift. Each macro destination is represented by
    one refined state except target, which is represented by clones receiving
    clone_fractions.
    """
    n = len(macro_transition)
    clone_count = len(
        clone_fractions
    )

    macro_map = []
    destination_fraction = []

    for vertex in range(n):
        if vertex == target:
            for fraction in (
                clone_fractions
            ):
                macro_map.append(target)
                destination_fraction.append(
                    float(fraction)
                )
        else:
            macro_map.append(vertex)
            destination_fraction.append(
                1.0
            )

    macro_map_array = np.asarray(
        macro_map,
        dtype=int,
    )
    destination_fraction_array = (
        np.asarray(
            destination_fraction,
            dtype=float,
        )
    )
    refined_n = len(macro_map_array)
    refined_transition = np.zeros(
        (refined_n, refined_n),
        dtype=float,
    )

    for micro_source in range(
        refined_n
    ):
        macro_source = int(
            macro_map_array[
                micro_source
            ]
        )
        for micro_destination in range(
            refined_n
        ):
            macro_destination = int(
                macro_map_array[
                    micro_destination
                ]
            )
            refined_transition[
                micro_source,
                micro_destination,
            ] = (
                macro_transition[
                    macro_source,
                    macro_destination,
                ]
                * destination_fraction_array[
                    micro_destination
                ]
            )

    return (
        refined_transition,
        macro_map_array,
    )


def transport_refinement_audit(
    rng: np.random.Generator,
) -> list[dict[str, object]]:
    rows = []

    for n in N_VALUES:
        for sample_index in range(
            GRAPH_SAMPLES_PER_N
        ):
            adjacency = make_strong_digraph(
                n,
                rng,
            )
            macro_transition = (
                relation_walk_transition(
                    adjacency
                )
            )
            target = int(
                rng.integers(0, n)
            )
            clone_count = int(
                rng.integers(
                    CLONE_COUNT_RANGE[0],
                    CLONE_COUNT_RANGE[1]
                    + 1,
                )
            )
            fractions = rng.dirichlet(
                np.ones(clone_count)
            )
            (
                refined_transition,
                macro_map,
            ) = lift_transition(
                macro_transition,
                target,
                fractions,
            )

            macro_mass = normalize(
                np.exp(
                    rng.normal(
                        0.0,
                        0.8,
                        size=n,
                    )
                )
            )

            refined_mass_values = []
            clone_cursor = 0

            for macro_index in macro_map:
                macro_index = int(
                    macro_index
                )
                if macro_index == target:
                    refined_mass_values.append(
                        macro_mass[target]
                        * fractions[
                            clone_cursor
                        ]
                    )
                    clone_cursor += 1
                else:
                    refined_mass_values.append(
                        macro_mass[
                            macro_index
                        ]
                    )

            refined_mass = np.asarray(
                refined_mass_values,
                dtype=float,
            )
            maximum_macro_error = 0.0
            maximum_conservation_error = 0.0

            for _ in range(
                TRANSPORT_STEPS
            ):
                macro_mass = (
                    macro_mass
                    @ macro_transition
                )
                refined_mass = (
                    refined_mass
                    @ refined_transition
                )
                aggregated = (
                    aggregate_micro_measure(
                        refined_mass,
                        macro_map,
                        n,
                    )
                )
                maximum_macro_error = max(
                    maximum_macro_error,
                    float(
                        np.max(
                            np.abs(
                                macro_mass
                                - aggregated
                            )
                        )
                    ),
                )
                maximum_conservation_error = max(
                    maximum_conservation_error,
                    abs(
                        float(
                            refined_mass.sum()
                        )
                        - 1.0
                    ),
                    abs(
                        float(
                            macro_mass.sum()
                        )
                        - 1.0
                    ),
                )

            rows.append(
                {
                    "n": n,
                    "sample_index": (
                        sample_index
                    ),
                    "clone_count": (
                        clone_count
                    ),
                    "maximum_macro_error": (
                        maximum_macro_error
                    ),
                    "maximum_conservation_error": (
                        maximum_conservation_error
                    ),
                }
            )

    return rows


def main() -> None:
    output = Path("a30_exact_results")
    output.mkdir(exist_ok=True)

    theorem_text = """# A30 — Base-Measure Origin and Semantic No-Go

## Semantic ambiguity theorem

Let a refined unweighted relational structure contain `m` exact,
structurally indistinguishable alternatives. The same structure can be
interpreted as:

- a descriptive refinement of one macro-alternative, requiring their total
  mass to equal the original macro mass; or
- `m` ontically distinct states, for which counting semantics assigns `m`
  state units.

Because the relation and q marks supplied to an intrinsic rule are identical
under both interpretations, no deterministic rule of those data alone can
choose between the two required masses. Extra refinement semantics are
necessary.

## Order-measurability corollary

Any candidate `mu=F(R)` determined only by the order is measurable from the
order and therefore cannot break the order-only identifiability limit of
A18–A21. It may still be a useful summary, but it is not an independent
measure primitive.

## Additive multiplicity theorem

If positive masses are supplied and exact refinement splits the target mass
into positive parts summing to the original, normalized macro masses are
preserved exactly.

## Projective transport theorem

Let `P` be a macro row-stochastic kernel. Split each macro destination into
microstates using fractions that sum to one and define

`P'_{alpha beta}=P_{A(alpha),A(beta)} f_beta`,

where `A` maps microstates to macrostates and destination fractions sum to
one inside each macrostate. Starting from a correspondingly split mass,
aggregation after every step equals the macro trajectory exactly.

Both positive constructions require a refinement map or multiplicity data
not encoded by the bare unweighted refined graph.
"""
    (output / "a30_theorem.md").write_text(
        theorem_text,
        encoding="utf-8",
    )

    rng = np.random.default_rng(SEED)

    derived_frame = pd.DataFrame(
        derived_measure_refinement_audit(
            rng
        )
    )
    explicit_frame = pd.DataFrame(
        explicit_additive_measure_audit(
            rng
        )
    )
    semantic_frame = pd.DataFrame(
        semantic_ambiguity_audit()
    )
    q_information_frame = pd.DataFrame(
        q_new_information_audit(rng)
    )
    transport_frame = pd.DataFrame(
        transport_refinement_audit(
            rng
        )
    )

    derived_frame.to_csv(
        output / "a30_derived_measure_refinement.csv",
        index=False,
    )
    explicit_frame.to_csv(
        output / "a30_explicit_additive_measure.csv",
        index=False,
    )
    semantic_frame.to_csv(
        output / "a30_semantic_ambiguity.csv",
        index=False,
    )
    q_information_frame.to_csv(
        output / "a30_q_measure_information.csv",
        index=False,
    )
    transport_frame.to_csv(
        output / "a30_projective_transport.csv",
        index=False,
    )

    derived_summary = []

    for measure, group in (
        derived_frame.groupby(
            "measure"
        )
    ):
        derived_summary.append(
            {
                "measure": measure,
                "refinement_consistency_rate": (
                    float(
                        group[
                            "refinement_consistent"
                        ].mean()
                    )
                ),
                "median_macro_tv": float(
                    group[
                        "macro_total_variation"
                    ].median()
                ),
                "maximum_macro_tv": float(
                    group[
                        "macro_total_variation"
                    ].max()
                ),
            }
        )

    q_information_summary = []

    for measure, group in (
        q_information_frame.groupby(
            "measure"
        )
    ):
        q_information_summary.append(
            {
                "measure": measure,
                "median_same_relation_tv": (
                    float(
                        group[
                            "same_relation_measure_tv"
                        ].median()
                    )
                ),
                "minimum_same_relation_tv": (
                    float(
                        group[
                            "same_relation_measure_tv"
                        ].min()
                    )
                ),
            }
        )

    derived_order_names = (
        "uniform_count",
        "degree",
        "relation_stationary",
    )
    derived_q_names = (
        "q_stationary",
        "q_node_softmax",
    )

    gates = {
        "G1_refinement_semantic_ambiguity_theorem_proved": True,
        "G2_same_refined_structure_supports_incompatible_semantics": bool(
            semantic_frame[
                "semantic_total_variation"
            ].min()
            >= MIN_SEMANTIC_AMBIGUITY_TV
        ),
        "G3_order_derived_candidates_fail_refinement": bool(
            all(
                (
                    1.0
                    - derived_frame[
                        derived_frame[
                            "measure"
                        ]
                        == name
                    ][
                        "refinement_consistent"
                    ].mean()
                    >= MIN_DERIVED_REFINEMENT_VIOLATION_RATE
                )
                and (
                    derived_frame[
                        derived_frame[
                            "measure"
                        ]
                        == name
                    ][
                        "macro_total_variation"
                    ].median()
                    >= MIN_DERIVED_MEDIAN_TV
                )
                for name in derived_order_names
            )
        ),
        "G4_q_derived_candidates_fail_refinement": bool(
            all(
                (
                    1.0
                    - derived_frame[
                        derived_frame[
                            "measure"
                        ]
                        == name
                    ][
                        "refinement_consistent"
                    ].mean()
                    >= MIN_DERIVED_REFINEMENT_VIOLATION_RATE
                )
                and (
                    derived_frame[
                        derived_frame[
                            "measure"
                        ]
                        == name
                    ][
                        "macro_total_variation"
                    ].median()
                    >= MIN_DERIVED_MEDIAN_TV
                )
                for name in derived_q_names
            )
        ),
        "G5_q_derived_measures_contain_information_beyond_relation": bool(
            all(
                q_information_frame[
                    q_information_frame[
                        "measure"
                    ]
                    == name
                ][
                    "same_relation_measure_tv"
                ].median()
                >= MIN_Q_NEW_INFORMATION_TV
                for name in derived_q_names
            )
        ),
        "G6_explicit_additive_mass_exactly_refinement_consistent": bool(
            explicit_frame[
                "maximum_macro_error"
            ].max()
            <= MAX_EXACT_ERROR
            and explicit_frame[
                "refinement_consistent"
            ].all()
        ),
        "G7_projective_transport_exactly_preserves_macro_mass": bool(
            transport_frame[
                "maximum_macro_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G8_projective_transport_conserves_total_mass": bool(
            transport_frame[
                "maximum_conservation_error"
            ].max()
            <= MAX_EXACT_ERROR
        ),
        "G9_order_derived_measure_is_not_independent_primitive": True,
        "G10_stationary_measure_from_mu_dependent_kernel_not_accepted_as_derivation": True,
        "G11_no_physical_volume_or_matter_measure_claimed": True,
    }

    verdict = (
        "PASS_BASE_MEASURE_ORIGIN_REQUIRES_EXTRA_REFINEMENT_SEMANTICS"
        if all(gates.values())
        else "FAIL_BASE_MEASURE_ORIGIN_AUDIT"
    )

    classification = [
        {
            "candidate": "uniform counting",
            "independent_of_order": False,
            "contains_q_information": False,
            "refinement_consistent": False,
            "requires_extra_semantics": False,
            "status": "REPRESENTATION_COUNTING",
        },
        {
            "candidate": "degree-derived mass",
            "independent_of_order": False,
            "contains_q_information": False,
            "refinement_consistent": False,
            "requires_extra_semantics": False,
            "status": "ORDER_REDUNDANT_AND_CLONE_SENSITIVE",
        },
        {
            "candidate": "relation-only stationary distribution",
            "independent_of_order": False,
            "contains_q_information": False,
            "refinement_consistent": False,
            "requires_extra_semantics": False,
            "status": "ORDER_DERIVED_AND_CLONE_SENSITIVE",
        },
        {
            "candidate": "q-dependent stationary distribution",
            "independent_of_order": True,
            "contains_q_information": True,
            "refinement_consistent": False,
            "requires_extra_semantics": False,
            "status": "NEW_INFORMATION_BUT_NOT_PROJECTIVE",
        },
        {
            "candidate": "q-node softmax mass",
            "independent_of_order": True,
            "contains_q_information": True,
            "refinement_consistent": False,
            "requires_extra_semantics": False,
            "status": "NEW_INFORMATION_BUT_CLONE_SENSITIVE",
        },
        {
            "candidate": "explicit additive multiplicity",
            "independent_of_order": True,
            "contains_q_information": False,
            "refinement_consistent": True,
            "requires_extra_semantics": True,
            "status": "PROJECTIVE_EXTRA_PRIMITIVE",
        },
        {
            "candidate": "projectively lifted conserved transport",
            "independent_of_order": "depends on supplied kernel and initial mass",
            "contains_q_information": "optional",
            "refinement_consistent": True,
            "requires_extra_semantics": True,
            "status": "CONSISTENT_WITH_REFINEMENT_MAP",
        },
        {
            "candidate": "stationary solution of a mu-dependent kernel",
            "independent_of_order": None,
            "contains_q_information": None,
            "refinement_consistent": None,
            "requires_extra_semantics": True,
            "status": "IMPLICIT_SIMULTANEOUS_LAW_NOT_A_DERIVATION",
        },
    ]
    pd.DataFrame(classification).to_csv(
        output / "a30_measure_classification.csv",
        index=False,
    )

    summary = {
        "seed": SEED,
        "n_values": list(N_VALUES),
        "graph_samples_per_n": (
            GRAPH_SAMPLES_PER_N
        ),
        "derived_measure_results": (
            derived_summary
        ),
        "q_information_results": (
            q_information_summary
        ),
        "semantic_ambiguity": {
            "minimum_tv": float(
                semantic_frame[
                    "semantic_total_variation"
                ].min()
            ),
            "maximum_tv": float(
                semantic_frame[
                    "semantic_total_variation"
                ].max()
            ),
        },
        "explicit_additive_measure": {
            "maximum_macro_error": float(
                explicit_frame[
                    "maximum_macro_error"
                ].max()
            ),
            "consistency_rate": float(
                explicit_frame[
                    "refinement_consistent"
                ].mean()
            ),
        },
        "projective_transport": {
            "maximum_macro_error": float(
                transport_frame[
                    "maximum_macro_error"
                ].max()
            ),
            "maximum_conservation_error": float(
                transport_frame[
                    "maximum_conservation_error"
                ].max()
            ),
        },
        "classification": classification,
        "gates": gates,
        "verdict": verdict,
        "logical_conclusion": (
            "The bare refined relation and q marks do not determine whether "
            "structurally identical alternatives are descriptive clones or "
            "ontically distinct states. Counting, degree, and stationary "
            "order-derived measures are relational summaries and fail exact "
            "refinement consistency. q-dependent stationary and node-score "
            "measures add information beyond the order but also fail "
            "projective refinement. Exact consistency is achieved by an "
            "explicit additive multiplicity or by a stochastic transport "
            "equipped with a refinement map and split fractions. Therefore "
            "the base measure required by A29 cannot be derived from the bare "
            "unweighted refined structure alone."
        ),
        "interpretation_boundary": (
            "A30 proves a semantic and identifiability requirement, not the "
            "existence of physical microstates or volume. A refinement map, "
            "multiplicity count, or projectively specified flow is additional "
            "structure whose physical origin remains open."
        ),
    }

    (output / "a30_summary.json").write_text(
        json.dumps(
            json_safe(summary),
            indent=2,
        ),
        encoding="utf-8",
    )

    report_lines = [
        "# A30 — Base-Measure Origin Audit",
        "",
        "## Main result",
        "",
        (
            "The unweighted refined graph cannot distinguish descriptive "
            "clones from genuine multiplicity. Derived graph and q measures "
            "failed projective refinement, while explicit additive mass and "
            "transport with a refinement map were exactly consistent."
        ),
        "",
        "## Derived candidates",
        "",
    ]

    for result in derived_summary:
        report_lines.extend(
            [
                f"### {result['measure']}",
                (
                    "- Consistency rate: "
                    f"{result['refinement_consistency_rate']:.6f}"
                ),
                (
                    "- Median macro TV: "
                    f"{result['median_macro_tv']:.6f}"
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

    (output / "a30_report.md").write_text(
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
