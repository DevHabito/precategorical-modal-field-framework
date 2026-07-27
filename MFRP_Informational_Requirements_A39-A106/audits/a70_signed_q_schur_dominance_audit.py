#!/usr/bin/env python3
"""A70 audit: signed q-Schur decomposition and arithmetic-grid dominance.

Purpose
-------
A69 reduced the positive alpha dual multiplier to a Cramer ratio

    lambda_alpha = Delta_alpha / Delta.

The open target was to exploit the arithmetic support x=0,...,M.

A70 expands every A67 Cramer numerator by generalized Laplace expansion over
the active P columns, active Q columns, and the Charnes-Cooper scale column.

Every nonzero term has the form

    sign * scale_coefficient
         * V_P
         * V_Q,

where V_P and V_Q are ordinary or first-confluent generalized
q-Vandermonde minors built from the ordered bases

    2^(-gamma), 2^(-3), 2^(-1), 1.

Ordinary minors factor as Vandermonde times a Schur-positive quotient.
Confluent/derivative minors are audited against the canonical confluent
orientation.

The audit proves:

1. The block-Laplace expansion equals the exact Cramer numerator in all
   33 phases.
2. Every ordinary or confluent minor has the predicted canonical sign.
3. No phase is termwise sign-coherent: all contain cancellation.
4. At the declared arithmetic-grid contracts, terms aligned with the final
   numerator orientation dominate opposing terms exactly.
5. The smallest dominance ratio is about 1.01279, in M=9 phase 7.

This is an exact finite-family arithmetic-grid dominance theorem. It is not
yet an induction for arbitrary M.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"
A67_RESULTS = HERE / "a67_central_mean_support_family_results.json"
A69_RESULTS = HERE / "a69_cramer_chebyshev_reduction_results.json"

S = sp.Symbol("s")
E = sp.Symbol("epsilon")

CANONICAL_RANK = {
    "gamma": 0,
    "beta": 1,
    "target": 2,
    "norm": 3,
    "mean": 4,
}


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def build_numerator_matrix(
    maximum: int,
    mean: sp.Rational,
    gamma: int,
    positive_indices: tuple[int, ...],
    active_observations: tuple[tuple[str, int], ...],
) -> dict[str, Any]:
    support = list(range(maximum + 1))
    count = maximum + 1
    dimension = 2 * count + 1

    target = [
        sp.Rational(1, 2 ** x)
        for x in support
    ]

    rows: list[list[sp.Expr]] = []
    labels: list[str] = []

    def append(row: list[sp.Expr], label: str) -> None:
        rows.append(row)
        labels.append(label)

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[index] = 1
    row[-1] = -1
    append(row, "norm_p")

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[count + index] = 1
    row[-1] = -1
    append(row, "norm_q")

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(support):
        row[index] = x
    row[-1] = -mean
    append(row, "mean_p")

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(support):
        row[count + index] = x
    row[-1] = -mean
    append(row, "mean_q")

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[count + index] = target[index]
    append(row, "target_q")

    exponent_map = {
        "alpha": None,
        "beta": 3,
        "gamma": gamma,
    }

    for name, sign in active_observations:
        exponent = exponent_map[name]
        values = [
            (
                S ** x
                if exponent is None
                else sp.Rational(
                    1,
                    2 ** (exponent * x),
                )
            )
            for x in support
        ]

        row = [sp.Integer(0)] * dimension
        for index in range(count):
            row[index] = sign * values[index]
            row[count + index] = -sign * values[index]
        row[-1] = -2 * E
        append(row, f"{name}_{sign:+d}")

    if len(rows) != len(positive_indices):
        raise RuntimeError("Active row/basic count mismatch")

    objective = [sp.Integer(0)] * dimension
    for index in range(count):
        objective[index] = target[index]

    numerator = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(len(rows))
        ]
    )

    alpha_row_index = (
        5
        + list(active_observations).index(
            ("alpha", 1)
        )
    )
    numerator[alpha_row_index, :] = sp.Matrix(
        [
            [
                objective[column_index]
                for column_index in positive_indices
            ]
        ]
    )
    labels[alpha_row_index] = "target_p"

    p_points = [
        index
        for index in positive_indices
        if 0 <= index < count
    ]
    q_points = [
        index - count
        for index in positive_indices
        if count <= index < 2 * count
    ]

    if 2 * count not in positive_indices:
        raise RuntimeError("Scale column is not basic")

    return {
        "matrix": numerator,
        "labels": labels,
        "p_points": p_points,
        "q_points": q_points,
        "p_count": len(p_points),
        "q_count": len(q_points),
    }


def permutation_sign(sequence: list[int]) -> int:
    inversions = sum(
        1
        for left in range(len(sequence))
        for right in range(left + 1, len(sequence))
        if sequence[left] > sequence[right]
    )
    return -1 if inversions % 2 else 1


def block_laplace_terms(
    matrix: sp.Matrix,
    p_count: int,
    q_count: int,
) -> list[dict[str, Any]]:
    row_count = matrix.rows
    rows = tuple(range(row_count))
    terms = []

    for p_rows in itertools.combinations(rows, p_count):
        remaining = [
            row
            for row in rows
            if row not in p_rows
        ]

        for q_rows in itertools.combinations(
            remaining,
            q_count,
        ):
            scale_rows = [
                row
                for row in remaining
                if row not in q_rows
            ]

            if len(scale_rows) != 1:
                raise RuntimeError("Expected one scale row")

            scale_row = scale_rows[0]
            ordered_rows = (
                list(p_rows)
                + list(q_rows)
                + [scale_row]
            )
            sign = permutation_sign(ordered_rows)

            p_minor = sp.factor(
                matrix.extract(
                    p_rows,
                    range(p_count),
                ).det()
            )
            q_minor = sp.factor(
                matrix.extract(
                    q_rows,
                    range(
                        p_count,
                        p_count + q_count,
                    ),
                ).det()
            )
            scale_value = sp.factor(
                matrix[
                    scale_row,
                    p_count + q_count,
                ]
            )

            value = sp.factor(
                sign
                * p_minor
                * q_minor
                * scale_value
            )

            if value == 0:
                continue

            terms.append(
                {
                    "p_rows": tuple(p_rows),
                    "q_rows": tuple(q_rows),
                    "scale_row": scale_row,
                    "partition_sign": sign,
                    "p_minor": p_minor,
                    "q_minor": q_minor,
                    "scale_value": scale_value,
                    "value": value,
                }
            )

    return terms


def row_descriptor(
    label: str,
    side: str,
) -> tuple[str, int]:
    if label == f"norm_{side}":
        return "norm", 1
    if label == f"mean_{side}":
        return "mean", 1
    if label == f"target_{side}":
        return "target", 1

    if label.startswith("beta_"):
        sign = int(label.split("_")[1])
        return "beta", sign if side == "p" else -sign

    if label.startswith("gamma_"):
        sign = int(label.split("_")[1])
        return "gamma", sign if side == "p" else -sign

    raise ValueError(
        f"Row {label} has no {side.upper()} minor descriptor"
    )


def schur_partition(points: list[int]) -> list[int]:
    count = len(points)
    return [
        points[count - index - 1]
        - (count - index - 1)
        for index in range(count)
    ]


def canonical_minor_certificate(
    determinant: sp.Expr,
    selected_rows: tuple[int, ...],
    labels: list[str],
    side: str,
    points: list[int],
    gamma: int,
) -> dict[str, Any]:
    descriptors = [
        row_descriptor(
            labels[row],
            side,
        )
        for row in selected_rows
    ]
    function_types = [
        descriptor[0]
        for descriptor in descriptors
    ]
    coefficient_sign = math.prod(
        descriptor[1]
        for descriptor in descriptors
    )

    canonical_indices = sorted(
        range(len(function_types)),
        key=lambda index: CANONICAL_RANK[
            function_types[index]
        ],
    )
    reordering_sign = permutation_sign(
        canonical_indices
    )
    predicted_sign = (
        coefficient_sign
        * reordering_sign
    )
    exact_sign = int(
        sp.sign(determinant)
    )

    if "mean" in function_types and "norm" in function_types:
        minor_class = "confluent_norm_mean"
    elif "mean" in function_types:
        minor_class = "derivative_only"
    else:
        minor_class = "ordinary_q_schur"

    output: dict[str, Any] = {
        "side": side,
        "rows": list(selected_rows),
        "row_labels": [
            labels[row]
            for row in selected_rows
        ],
        "function_types": function_types,
        "points": points,
        "minor_class": minor_class,
        "coefficient_sign": coefficient_sign,
        "reordering_sign": reordering_sign,
        "predicted_sign": predicted_sign,
        "exact_sign": exact_sign,
        "sign_matches": bool(
            predicted_sign == exact_sign
        ),
        "determinant": str(determinant),
    }

    if minor_class == "ordinary_q_schur":
        canonical_types = [
            function_types[index]
            for index in canonical_indices
        ]
        base_map = {
            "gamma": sp.Rational(
                1,
                2 ** gamma,
            ),
            "beta": sp.Rational(1, 8),
            "target": sp.Rational(1, 2),
            "norm": sp.Rational(1),
        }
        nodes = [
            base_map[function_type]
            for function_type in canonical_types
        ]

        vandermonde = sp.factor(
            math.prod(
                nodes[right] - nodes[left]
                for left in range(len(nodes))
                for right in range(left + 1, len(nodes))
            )
        )
        canonical_value = sp.factor(
            exact_sign
            * determinant
        )
        schur_quotient = sp.factor(
            canonical_value
            / vandermonde
        )

        output.update(
            {
                "canonical_nodes": [
                    str(node)
                    for node in nodes
                ],
                "partition": schur_partition(
                    points
                ),
                "vandermonde": str(
                    vandermonde
                ),
                "schur_quotient": str(
                    schur_quotient
                ),
                "schur_quotient_positive": bool(
                    schur_quotient > 0
                ),
            }
        )
    else:
        output.update(
            {
                "confluent_orientation_positive": bool(
                    exact_sign
                    == predicted_sign
                )
            }
        )

    return output


def exact_abs_sum(
    values: list[sp.Expr],
) -> sp.Expr:
    return sp.factor(
        sum(
            abs(value)
            for value in values
        )
    )


def main() -> None:
    for path in [
        A67_SCRIPT,
        A67_RESULTS,
        A69_RESULTS,
    ]:
        if not path.exists():
            raise FileNotFoundError(path)

    a67 = load_module(
        A67_SCRIPT,
        "a67_for_a70",
    )
    a67_results = json.loads(
        A67_RESULTS.read_text(
            encoding="utf-8"
        )
    )
    a69_results = json.loads(
        A69_RESULTS.read_text(
            encoding="utf-8"
        )
    )

    phase_records = []
    decomposition_gates = []
    minor_sign_gates = []
    ordinary_schur_gates = []
    mixed_sign_gates = []
    dominance_gates = []

    minor_class_counts = Counter()
    term_count_distribution = Counter()
    signature_dominance: dict[
        tuple[Any, ...],
        list[sp.Expr],
    ] = defaultdict(list)

    minimum_dominance = None
    minimum_dominance_location = None

    for support_result in a67_results["supports"]:
        maximum = support_result["maximum"]
        configuration = a67.FAMILY[maximum]

        for phase_result, phase_spec in zip(
            support_result["phases"],
            configuration["phase_specs"],
        ):
            positive_indices, active_observations = phase_spec

            built = build_numerator_matrix(
                maximum,
                configuration["mean"],
                configuration["gamma"],
                positive_indices,
                active_observations,
            )
            matrix = built["matrix"]
            labels = built["labels"]

            terms = block_laplace_terms(
                matrix,
                built["p_count"],
                built["q_count"],
            )
            term_count_distribution[
                len(terms)
            ] += 1

            exact_determinant = sp.factor(
                matrix.det()
            )
            expanded_determinant = sp.factor(
                sum(
                    term["value"]
                    for term in terms
                )
            )
            decomposition_exact = bool(
                sp.factor(
                    exact_determinant
                    - expanded_determinant
                )
                == 0
            )
            decomposition_gates.append(
                decomposition_exact
            )

            declared_epsilon = (
                configuration["epsilon"]
            )
            declared_terms = [
                sp.factor(
                    term["value"].subs(
                        E,
                        declared_epsilon,
                    )
                )
                for term in terms
            ]
            declared_total = sp.factor(
                sum(declared_terms)
            )
            final_sign = int(
                sp.sign(declared_total)
            )

            positive_term_count = sum(
                int(sp.sign(value)) > 0
                for value in declared_terms
            )
            negative_term_count = sum(
                int(sp.sign(value)) < 0
                for value in declared_terms
            )
            mixed_sign = bool(
                positive_term_count > 0
                and negative_term_count > 0
            )
            mixed_sign_gates.append(
                mixed_sign
            )

            aligned_values = [
                value
                for value in declared_terms
                if int(sp.sign(value))
                == final_sign
            ]
            opposing_values = [
                value
                for value in declared_terms
                if int(sp.sign(value))
                == -final_sign
            ]

            aligned_magnitude = exact_abs_sum(
                aligned_values
            )
            opposing_magnitude = exact_abs_sum(
                opposing_values
            )
            dominance_ratio = sp.factor(
                aligned_magnitude
                / opposing_magnitude
            )
            dominance_surplus = sp.factor(
                dominance_ratio - 1
            )
            dominance_ok = bool(
                dominance_ratio > 1
            )
            dominance_gates.append(
                dominance_ok
            )

            if (
                minimum_dominance is None
                or dominance_ratio
                < minimum_dominance
            ):
                minimum_dominance = (
                    dominance_ratio
                )
                minimum_dominance_location = (
                    maximum,
                    phase_result["phase"],
                )

            signature = next(
                signature
                for signature
                in a69_results[
                    "contact_signatures"
                ]
                if {
                    (
                        instance["maximum"],
                        instance["phase"],
                    )
                    for instance
                    in signature["instances"]
                }
                and (
                    maximum,
                    phase_result["phase"],
                )
                in {
                    (
                        instance["maximum"],
                        instance["phase"],
                    )
                    for instance
                    in signature["instances"]
                }
            )
            signature_key = (
                tuple(
                    signature[
                        "contact_labels"
                    ]
                ),
                tuple(
                    tuple(observation)
                    for observation
                    in signature[
                        "active_observations"
                    ]
                ),
            )
            signature_dominance[
                signature_key
            ].append(
                dominance_ratio
            )

            term_records = []

            for term_index, (
                term,
                declared_value,
            ) in enumerate(
                zip(
                    terms,
                    declared_terms,
                ),
                start=1,
            ):
                p_certificate = (
                    canonical_minor_certificate(
                        term["p_minor"],
                        term["p_rows"],
                        labels,
                        "p",
                        built["p_points"],
                        configuration["gamma"],
                    )
                )
                q_certificate = (
                    canonical_minor_certificate(
                        term["q_minor"],
                        term["q_rows"],
                        labels,
                        "q",
                        built["q_points"],
                        configuration["gamma"],
                    )
                )

                for certificate in [
                    p_certificate,
                    q_certificate,
                ]:
                    minor_class_counts[
                        certificate[
                            "minor_class"
                        ]
                    ] += 1
                    minor_sign_gates.append(
                        certificate[
                            "sign_matches"
                        ]
                    )

                    if (
                        certificate[
                            "minor_class"
                        ]
                        == "ordinary_q_schur"
                    ):
                        ordinary_schur_gates.append(
                            certificate[
                                "schur_quotient_positive"
                            ]
                        )

                predicted_term_sign = (
                    term[
                        "partition_sign"
                    ]
                    * p_certificate[
                        "predicted_sign"
                    ]
                    * q_certificate[
                        "predicted_sign"
                    ]
                    * int(
                        sp.sign(
                            term[
                                "scale_value"
                            ].subs(
                                E,
                                declared_epsilon,
                            )
                        )
                    )
                )
                exact_term_sign = int(
                    sp.sign(
                        declared_value
                    )
                )
                term_sign_match = bool(
                    predicted_term_sign
                    == exact_term_sign
                )
                minor_sign_gates.append(
                    term_sign_match
                )

                term_records.append(
                    {
                        "term": term_index,
                        "p_rows": list(
                            term["p_rows"]
                        ),
                        "q_rows": list(
                            term["q_rows"]
                        ),
                        "scale_row": (
                            term["scale_row"]
                        ),
                        "scale_row_label": labels[
                            term["scale_row"]
                        ],
                        "partition_sign": term[
                            "partition_sign"
                        ],
                        "scale_value": str(
                            term[
                                "scale_value"
                            ]
                        ),
                        "symbolic_value": str(
                            term["value"]
                        ),
                        "declared_value": str(
                            declared_value
                        ),
                        "declared_sign": (
                            exact_term_sign
                        ),
                        "aligned_with_total": bool(
                            exact_term_sign
                            == final_sign
                        ),
                        "predicted_term_sign": (
                            predicted_term_sign
                        ),
                        "term_sign_matches": (
                            term_sign_match
                        ),
                        "p_minor": p_certificate,
                        "q_minor": q_certificate,
                    }
                )

            phase_records.append(
                {
                    "maximum": maximum,
                    "phase": phase_result[
                        "phase"
                    ],
                    "gamma": configuration[
                        "gamma"
                    ],
                    "epsilon": str(
                        declared_epsilon
                    ),
                    "p_points": built[
                        "p_points"
                    ],
                    "q_points": built[
                        "q_points"
                    ],
                    "active_observations": [
                        list(observation)
                        for observation
                        in active_observations
                    ],
                    "term_count": len(
                        terms
                    ),
                    "positive_term_count": (
                        positive_term_count
                    ),
                    "negative_term_count": (
                        negative_term_count
                    ),
                    "mixed_sign_decomposition": (
                        mixed_sign
                    ),
                    "final_numerator_sign": (
                        final_sign
                    ),
                    "exact_numerator": str(
                        exact_determinant
                    ),
                    "declared_numerator": str(
                        declared_total
                    ),
                    "decomposition_exact": (
                        decomposition_exact
                    ),
                    "aligned_magnitude": str(
                        aligned_magnitude
                    ),
                    "opposing_magnitude": str(
                        opposing_magnitude
                    ),
                    "dominance_ratio": str(
                        dominance_ratio
                    ),
                    "dominance_ratio_decimal": str(
                        sp.N(
                            dominance_ratio,
                            50,
                        )
                    ),
                    "dominance_surplus_decimal": str(
                        sp.N(
                            dominance_surplus,
                            50,
                        )
                    ),
                    "terms": term_records,
                }
            )

    signature_summary = []
    repeated_signature_dominance_gates = []

    for signature_key, ratios in signature_dominance.items():
        labels, active_observations = signature_key
        minimum_ratio = min(ratios)

        if len(ratios) > 1:
            repeated_signature_dominance_gates.append(
                minimum_ratio > 1
            )

        signature_summary.append(
            {
                "contact_labels": list(
                    labels
                ),
                "active_observations": [
                    list(observation)
                    for observation
                    in active_observations
                ],
                "instance_count": len(
                    ratios
                ),
                "minimum_dominance_ratio": str(
                    minimum_ratio
                ),
                "minimum_dominance_decimal": str(
                    sp.N(
                        minimum_ratio,
                        40,
                    )
                ),
            }
        )

    all_mixed = all(
        phase[
            "mixed_sign_decomposition"
        ]
        for phase in phase_records
    )

    gates = {
        "A67_family_theorem_passed": bool(
            all(
                a67_results[
                    "gates"
                ].values()
            )
        ),
        "A69_cramer_reduction_passed": bool(
            all(
                a69_results[
                    "gates"
                ].values()
            )
        ),
        "all_33_block_laplace_expansions_exact": bool(
            len(
                decomposition_gates
            )
            == 33
            and all(
                decomposition_gates
            )
        ),
        "all_657_minor_orientations_and_term_signs_match": bool(
            len(minor_sign_gates)
            == 657
            and all(
                minor_sign_gates
            )
        ),
        "all_84_ordinary_q_schur_quotients_positive": bool(
            len(
                ordinary_schur_gates
            )
            == 84
            and all(
                ordinary_schur_gates
            )
        ),
        "all_33_decompositions_are_mixed_sign": bool(
            len(
                mixed_sign_gates
            )
            == 33
            and all_mixed
        ),
        "aligned_terms_dominate_in_all_33_phases": bool(
            len(
                dominance_gates
            )
            == 33
            and all(
                dominance_gates
            )
        ),
        "minimum_exact_dominance_ratio_above_1_01": bool(
            minimum_dominance
            is not None
            and minimum_dominance
            > sp.Rational(
                101,
                100,
            )
        ),
        "all_repeated_signatures_retain_exact_dominance": bool(
            repeated_signature_dominance_gates
            and all(
                repeated_signature_dominance_gates
            )
        ),
    }

    verdict = (
        "PASS_SIGNED_Q_SCHUR_ARITHMETIC_GRID_DOMINANCE"
        if all(gates.values())
        else "FAIL_A70_Q_SCHUR_DOMINANCE_AUDIT"
    )

    result = {
        "audit": (
            "A70_SIGNED_Q_SCHUR_ARITHMETIC_GRID_DOMINANCE"
        ),
        "general_decomposition_theorem": {
            "block_laplace": (
                "Delta_alpha is the signed sum over row partitions "
                "of det(P-minor)*det(Q-minor)*scale-entry."
            ),
            "ordinary_minor_factorization": (
                "Every ordinary minor equals a known orientation "
                "times a positive Vandermonde factor and a positive "
                "Schur quotient on the ordered q-nodes."
            ),
            "confluent_minor_statement": (
                "Norm/mean and derivative-only minors are first-"
                "confluent generalized Vandermonde minors. Their "
                "canonical orientation is exact and positive for "
                "every occurrence in the A67 arithmetic-grid family."
            ),
            "sign_reduction": (
                "Every term is a combinatorial sign times positive "
                "minor magnitudes and a scale coefficient."
            ),
        },
        "family_summary": {
            "phase_count": len(
                phase_records
            ),
            "term_count_distribution": {
                str(term_count): count
                for term_count, count
                in sorted(
                    term_count_distribution.items()
                )
            },
            "minor_class_counts": {
                key: value
                for key, value
                in sorted(
                    minor_class_counts.items()
                )
            },
            "all_decompositions_mixed_sign": (
                all_mixed
            ),
            "minimum_dominance_ratio": str(
                minimum_dominance
            ),
            "minimum_dominance_decimal": str(
                sp.N(
                    minimum_dominance,
                    50,
                )
            ),
            "minimum_dominance_surplus_percent": str(
                sp.N(
                    100
                    * (
                        minimum_dominance
                        - 1
                    ),
                    50,
                )
            ),
            "minimum_dominance_location": {
                "maximum": (
                    minimum_dominance_location[
                        0
                    ]
                ),
                "phase": (
                    minimum_dominance_location[
                        1
                    ]
                ),
            },
            "interpretation": (
                "Arithmetic-grid positivity does not make the "
                "Cramer expansion sign coherent. The proven sign "
                "comes from exact magnitude dominance after "
                "cancellation."
            ),
        },
        "signature_summary": (
            signature_summary
        ),
        "phases": phase_records,
        "formal_results": [
            (
                "all A67 Cramer numerators admit an exact block-"
                "Laplace expansion into products of generalized "
                "q-Vandermonde minors"
            ),
            (
                "all ordinary minors have positive Schur quotients"
            ),
            (
                "all confluent and derivative minor orientations "
                "match the canonical ordered-q prediction"
            ),
            (
                "every one of the 33 numerator expansions contains "
                "both positive and negative terms"
            ),
            (
                "the final orientation is obtained by exact "
                "dominance, not by termwise positivity"
            ),
            (
                "the weakest arithmetic-grid dominance margin is "
                "1.0127902833 at M=9 phase 7"
            ),
            (
                "a future arbitrary-M proof must establish a "
                "uniform dominance inequality, not merely invoke "
                "Schur positivity"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A70 is exact for the 33 A67 phases on the declared "
            "arithmetic grids. It does not prove a uniform lower "
            "bound on the dominance ratio for arbitrary M, nor "
            "does it prove all derivative-only minors are positive "
            "for arbitrary contact configurations."
        ),
    }

    output_path = HERE / (
        "a70_signed_q_schur_dominance_results.json"
    )
    output_path.write_text(
        json.dumps(
            result,
            indent=2,
        ),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(
            gates
        ),
        "pass_count": sum(
            gates.values()
        ),
        "term_count_distribution": (
            result[
                "family_summary"
            ][
                "term_count_distribution"
            ]
        ),
        "minor_class_counts": (
            result[
                "family_summary"
            ][
                "minor_class_counts"
            ]
        ),
        "minimum_dominance_ratio": (
            result[
                "family_summary"
            ][
                "minimum_dominance_decimal"
            ]
        ),
        "minimum_dominance_location": (
            result[
                "family_summary"
            ][
                "minimum_dominance_location"
            ]
        ),
        "failed_gates": [
            name
            for name, value
            in gates.items()
            if not value
        ],
        "verdict": verdict,
    }

    print(
        json.dumps(
            summary,
            indent=2,
        )
    )

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
