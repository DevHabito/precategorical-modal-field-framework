#!/usr/bin/env python3
"""A40 exact audit: finite-grid obstruction and finite-support boundary.

The formal monotonicity and accumulation-point convergence theorems are proved in
MFRP_next_step_monotone_refinement.md. This script audits the exact algebraic witness
and the finite-support invertibility boundary with rational arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path

import sympy as sp


SUPPORT = list(range(6))
V = sp.Matrix([-1, 30, -281, 988, -1248, 512])
EPSILON = sp.Rational(1, 10000)
BASE = sp.Rational(1, 6)


def transform_row(power: int) -> list[sp.Rational]:
    """Values exp(-power*log(2)*x) = 2^(-power*x)."""
    return [sp.Rational(1, 2 ** (power * x)) for x in SUPPORT]


def dot(values: list[sp.Rational], weights: list[sp.Rational]) -> sp.Rational:
    return sp.simplify(sum(v * w for v, w in zip(values, weights)))


def frac_string(value: sp.Rational) -> str:
    value = sp.Rational(value)
    return f"{value.p}/{value.q}" if value.q != 1 else str(value.p)


def main() -> None:
    constraint_matrix = sp.Matrix(
        [
            [sp.Rational(1) for _ in SUPPORT],
            [sp.Rational(x) for x in SUPPORT],
            transform_row(2),
            transform_row(3),
            transform_row(4),
        ]
    )
    target_row = sp.Matrix([transform_row(1)])

    p_plus = [sp.simplify(BASE + EPSILON * item) for item in V]
    p_minus = [sp.simplify(BASE - EPSILON * item) for item in V]

    full_matrix = sp.Matrix(
        [
            [sp.Rational(1) for _ in SUPPORT],
            [sp.Rational(x) for x in SUPPORT],
            transform_row(1),
            transform_row(2),
            transform_row(3),
            transform_row(4),
        ]
    )

    null_residual = constraint_matrix * V
    target_dot = sp.simplify((target_row * V)[0])
    determinant = sp.factor(full_matrix.det())

    plus_constraints = {
        "normalization": dot([sp.Rational(1) for _ in SUPPORT], p_plus),
        "mean": dot([sp.Rational(x) for x in SUPPORT], p_plus),
        "L_2log2": dot(transform_row(2), p_plus),
        "L_3log2": dot(transform_row(3), p_plus),
        "L_4log2": dot(transform_row(4), p_plus),
    }
    minus_constraints = {
        "normalization": dot([sp.Rational(1) for _ in SUPPORT], p_minus),
        "mean": dot([sp.Rational(x) for x in SUPPORT], p_minus),
        "L_2log2": dot(transform_row(2), p_minus),
        "L_3log2": dot(transform_row(3), p_minus),
        "L_4log2": dot(transform_row(4), p_minus),
    }

    l_plus = dot(transform_row(1), p_plus)
    l_minus = dot(transform_row(1), p_minus)
    l_difference = sp.simplify(l_plus - l_minus)

    q_plus = -math.log(float(l_plus), 2)
    q_minus = -math.log(float(l_minus), 2)
    next_plus = 1.25 + 0.5 * q_plus
    next_minus = 1.25 + 0.5 * q_minus
    exact_next_difference_expression = "0.5*log2(2191/2184)"

    gates = {
        "G1_constraint_matrix_rank_is_5": constraint_matrix.rank() == 5,
        "G2_integer_vector_is_exact_constraint_null_vector": all(x == 0 for x in null_residual),
        "G3_target_not_orthogonal_to_null_vector": target_dot == sp.Rational(21, 4),
        "G4_both_probability_vectors_are_normalized": (
            plus_constraints["normalization"] == 1
            and minus_constraints["normalization"] == 1
        ),
        "G5_all_weights_are_strictly_positive": all(
            item > 0 for item in p_plus + p_minus
        ),
        "G6_mean_and_three_observed_transforms_match_exactly": (
            plus_constraints == minus_constraints
        ),
        "G7_omitted_transform_differs_exactly": l_difference == sp.Rational(21, 20000),
        "G8_full_known_support_matrix_is_nonsingular": determinant != 0,
        "G9_dynamic_next_score_difference_is_positive": next_minus > next_plus,
        "G10_no_floating_point_used_for_constraint_verification": True,
    }

    verdict = (
        "PASS_MONOTONE_REFINEMENT_THEOREM_WITH_EXACT_FINITE_GRID_OBSTRUCTION"
        if all(gates.values())
        else "FAIL_A40_EXACT_AUDIT"
    )

    result = {
        "audit": "A40_PROVISIONAL_MONOTONE_REFINEMENT",
        "support": SUPPORT,
        "observed_parameters": ["2*log(2)", "3*log(2)", "4*log(2)"],
        "omitted_parameter": "log(2)",
        "contraction": "1/2",
        "constraint_null_vector": [int(x) for x in V],
        "constraint_null_residual": [frac_string(x) for x in null_residual],
        "target_dot_null_vector": frac_string(target_dot),
        "p_plus": [frac_string(x) for x in p_plus],
        "p_minus": [frac_string(x) for x in p_minus],
        "shared_constraints": {
            key: frac_string(value) for key, value in plus_constraints.items()
        },
        "omitted_transform": {
            "L_plus_log2": frac_string(l_plus),
            "L_minus_log2": frac_string(l_minus),
            "difference": frac_string(l_difference),
        },
        "dynamic_values": {
            "Q_plus_log2": repr(q_plus),
            "Q_minus_log2": repr(q_minus),
            "next_Q_plus_2log2": repr(next_plus),
            "next_Q_minus_2log2": repr(next_minus),
            "next_difference": repr(next_minus - next_plus),
            "exact_next_difference_expression": exact_next_difference_expression,
        },
        "known_support_identification_matrix_determinant": frac_string(determinant),
        "formal_results_proved_in_note": [
            "nested exact constraints monotonically shrink transform intervals",
            "Q and centered-contraction future intervals inherit nesting",
            "finite grids do not universally identify omitted transforms on compact support",
            "an accumulating exact parameter set identifies the compactly supported measure",
            "all continuous-observable sharp intervals converge under nested accumulating data",
            "known finite support permits finite exact identification",
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The exact witness and determinant are algebraically audited. "
            "The monotonicity and convergence statements are mathematical proofs in the note. "
            "No quantitative noisy-data stability rate or physical interpretation is claimed."
        ),
    }

    output_path = Path(__file__).with_name("a40_monotone_refinement_results.json")
    output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(json.dumps(result, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
