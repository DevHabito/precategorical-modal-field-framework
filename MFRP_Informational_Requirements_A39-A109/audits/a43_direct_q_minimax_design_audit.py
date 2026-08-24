#!/usr/bin/env python3
"""A43 exact direct-Q minimax design audit.

The audit optimizes the nonlinear future effective-score width directly.
For each design, symmetry reduces the risk to one maximum target-transform
ratio. The ratio is converted by the Charnes-Cooper substitution to an exact
rational linear programme.

All 10 designs are certified at:
- epsilon = 0;
- epsilon = 1/10000.

Every candidate has exact rational primal and dual certificates.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


SUPPORT = list(range(6))
TARGET = [sp.Rational(1, 2**x) for x in SUPPORT]
MEAN = sp.Rational(5, 2)
CANDIDATES = [2, 3, 4, 5, 6]
DESIGNS = list(itertools.combinations(CANDIDATES, 3))


def transform_row(k: int) -> list[sp.Rational]:
    return [sp.Rational(1, 2 ** (k * x)) for x in SUPPORT]


ZERO_PATTERNS = {
    design: ([1, 3, 5], [0, 1, 2, 4], [])
    for design in DESIGNS
}

NOISY_PATTERNS = {
    (2, 3, 4): ([0, 2, 3, 5], [1, 2, 4], [1, -1, 1]),
    (2, 3, 5): ([0, 1, 3, 5], [1, 2, 4], [1, -1, 1]),
    (2, 3, 6): ([0, 1, 3, 5], [1, 2, 4], [1, -1, 1]),
    (2, 4, 5): ([0, 2, 3, 5], [1, 2, 4], [1, -1, 1]),
    (2, 4, 6): ([0, 1, 3, 5], [1, 2, 4], [1, -1, 1]),
    (2, 5, 6): ([0, 2, 5], [1, 2, 3, 4], [1, -1, 1]),
    (3, 4, 5): ([0, 2, 5], [1, 2, 3, 4], [1, -1, 1]),
    (3, 4, 6): ([0, 2, 5], [1, 2, 3, 4], [1, -1, 1]),
    (3, 5, 6): ([0, 2, 5], [1, 2, 3, 4], [1, -1, 1]),
    (4, 5, 6): ([0, 1, 2, 5], [1, 3], [1, -1, 0]),
}


def exact_certificate(
    design: tuple[int, int, int],
    epsilon: sp.Rational,
    pattern: tuple[list[int], list[int], list[int]],
) -> dict[str, Any]:
    p_support, q_support, signs = pattern

    # Charnes-Cooper variables:
    # y_p[0:6], y_q[0:6], t.
    positive_indices = (
        p_support
        + [6 + index for index in q_support]
        + [12]
    )

    equality_rows: list[list[sp.Rational]] = []
    equality_rhs: list[sp.Rational] = []

    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[index] = 1
    row[12] = -1
    equality_rows.append(row)
    equality_rhs.append(0)

    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[6 + index] = 1
    row[12] = -1
    equality_rows.append(row)
    equality_rhs.append(0)

    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[index] = index
    row[12] = -MEAN
    equality_rows.append(row)
    equality_rhs.append(0)

    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[6 + index] = index
    row[12] = -MEAN
    equality_rows.append(row)
    equality_rhs.append(0)

    # Denominator normalization L_{y_q}(log 2) = 1.
    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[6 + index] = TARGET[index]
    equality_rows.append(row)
    equality_rhs.append(1)

    active_inequality_rows: list[list[sp.Rational]] = []

    if epsilon == 0:
        for exponent in design:
            values = transform_row(exponent)
            row = [sp.Rational(0)] * 13
            for index in range(6):
                row[index] = values[index]
                row[6 + index] = -values[index]
            equality_rows.append(row)
            equality_rhs.append(0)
    else:
        for exponent, sign in zip(design, signs):
            if sign == 0:
                continue
            values = transform_row(exponent)
            row = [sp.Rational(0)] * 13
            for index in range(6):
                row[index] = sign * values[index]
                row[6 + index] = -sign * values[index]
            row[12] = -2 * epsilon
            active_inequality_rows.append(row)

    active_rows = equality_rows + active_inequality_rows
    active_rhs = equality_rhs + [sp.Rational(0)] * len(active_inequality_rows)

    primal_matrix = sp.Matrix(
        [
            [row[index] for index in positive_indices]
            for row in active_rows
        ]
    )
    if primal_matrix.rows != primal_matrix.cols:
        raise RuntimeError(
            f"Non-square active primal system for {design}: "
            f"{primal_matrix.shape}"
        )

    primal_solution = primal_matrix.inv() * sp.Matrix(active_rhs)

    z = [sp.Rational(0)] * 13
    for index, value in zip(positive_indices, primal_solution):
        z[index] = sp.factor(value)

    objective_coefficients = [sp.Rational(0)] * 13
    for index in range(6):
        objective_coefficients[index] = TARGET[index]

    ratio = sp.factor(
        sum(objective_coefficients[index] * z[index] for index in range(13))
    )

    # Dual for:
    # max c^T z
    # A_eq z = b, A_ub z <= 0, z >= 0.
    # Equality multipliers are free; inequality multipliers are nonnegative.
    dual_rows = active_rows
    dual_variable_count = len(dual_rows)

    dual_matrix = sp.Matrix(
        [
            [dual_rows[row_index][column_index]
             for row_index in range(dual_variable_count)]
            for column_index in positive_indices
        ]
    )

    dual_solution = dual_matrix.inv() * sp.Matrix(
        [objective_coefficients[index] for index in positive_indices]
    )
    dual_values = [sp.factor(value) for value in dual_solution]

    reduced_costs = [
        sp.factor(
            sum(
                dual_rows[row_index][column_index] * dual_values[row_index]
                for row_index in range(dual_variable_count)
            )
            - objective_coefficients[column_index]
        )
        for column_index in range(13)
    ]

    dual_objective = sp.factor(
        sum(
            equality_rhs[row_index] * dual_values[row_index]
            for row_index in range(len(equality_rows))
        )
    )

    transformed_observation_differences: dict[str, sp.Expr] = {}
    original_observation_differences: dict[str, sp.Expr] = {}

    t_value = z[12]
    p = [sp.factor(z[index] / t_value) for index in range(6)]
    q = [sp.factor(z[6 + index] / t_value) for index in range(6)]

    for exponent in design:
        values = transform_row(exponent)
        transformed_difference = sp.factor(
            sum(values[index] * z[index] for index in range(6))
            -
            sum(values[index] * z[6 + index] for index in range(6))
        )
        original_difference = sp.factor(
            sum(values[index] * p[index] for index in range(6))
            -
            sum(values[index] * q[index] for index in range(6))
        )
        transformed_observation_differences[str(exponent)] = transformed_difference
        original_observation_differences[str(exponent)] = original_difference

    if epsilon == 0:
        observation_gate = all(
            value == 0
            for value in original_observation_differences.values()
        )
    else:
        observation_gate = all(
            abs(value) <= 2 * epsilon
            for value in original_observation_differences.values()
        )

    inequality_dual_values = dual_values[len(equality_rows):]

    gates = {
        "primal_variables_nonnegative": bool(all(value >= 0 for value in z)),
        "p_normalized": bool(sp.factor(sum(p)) == 1),
        "q_normalized": bool(sp.factor(sum(q)) == 1),
        "p_mean_exact": bool(
            sp.factor(sum(index * p[index] for index in range(6))) == MEAN
        ),
        "q_mean_exact": bool(
            sp.factor(sum(index * q[index] for index in range(6))) == MEAN
        ),
        "denominator_normalization_exact": bool(
            sp.factor(sum(TARGET[index] * z[6 + index] for index in range(6)))
            == 1
        ),
        "observation_constraints_exact": bool(observation_gate),
        "dual_inequality_multipliers_nonnegative": bool(
            all(value >= 0 for value in inequality_dual_values)
        ),
        "dual_reduced_costs_nonnegative": bool(
            all(value >= 0 for value in reduced_costs)
        ),
        "primal_dual_objectives_equal": bool(
            sp.factor(ratio - dual_objective) == 0
        ),
        "ratio_matches_original_distributions": bool(
            sp.factor(
                ratio
                -
                (
                    sum(TARGET[index] * p[index] for index in range(6))
                    /
                    sum(TARGET[index] * q[index] for index in range(6))
                )
            )
            == 0
        ),
    }

    future_risk = 0.5 * math.log2(float(ratio))

    return {
        "design": list(design),
        "epsilon": str(epsilon),
        "ratio_exact": str(ratio),
        "ratio_decimal": f"{float(ratio):.18g}",
        "future_score_risk_decimal": f"{future_risk:.18g}",
        "t": str(t_value),
        "p": [str(value) for value in p],
        "q": [str(value) for value in q],
        "original_observation_differences": {
            key: str(value)
            for key, value in original_observation_differences.items()
        },
        "dual_values": [str(value) for value in dual_values],
        "reduced_costs": [str(value) for value in reduced_costs],
        "gates": gates,
    }


def audit_contract(
    epsilon: sp.Rational,
    patterns: dict[
        tuple[int, int, int],
        tuple[list[int], list[int], list[int]],
    ],
) -> dict[str, Any]:
    certificates = [
        exact_certificate(design, epsilon, patterns[design])
        for design in DESIGNS
    ]

    ranking = sorted(
        certificates,
        key=lambda item: sp.Rational(item["ratio_exact"]),
    )

    unique_winner = bool(
        sp.Rational(ranking[0]["ratio_exact"])
        <
        sp.Rational(ranking[1]["ratio_exact"])
    )

    return {
        "epsilon": str(epsilon),
        "ranking": [
            {
                "design": item["design"],
                "ratio_exact": item["ratio_exact"],
                "ratio_decimal": item["ratio_decimal"],
                "future_score_risk_decimal": item[
                    "future_score_risk_decimal"
                ],
            }
            for item in ranking
        ],
        "winner": ranking[0]["design"],
        "winner_ratio_exact": ranking[0]["ratio_exact"],
        "winner_future_score_risk_decimal": ranking[0][
            "future_score_risk_decimal"
        ],
        "unique_winner": unique_winner,
        "certificates": certificates,
    }


def main() -> None:
    exact_contract = audit_contract(sp.Rational(0), ZERO_PATTERNS)
    noisy_contract = audit_contract(
        sp.Rational(1, 10000),
        NOISY_PATTERNS,
    )

    certificate_gates = []
    for contract in [exact_contract, noisy_contract]:
        for certificate in contract["certificates"]:
            certificate_gates.extend(certificate["gates"].values())

    exact_direct = float(
        exact_contract["winner_future_score_risk_decimal"]
    )
    noisy_direct = float(
        noisy_contract["winner_future_score_risk_decimal"]
    )

    # Outer bounds established in A42.
    exact_a42_outer = 0.009034708626844655
    noisy_a42_outer = 0.016434200690519877

    comparison = {
        "exact_data_A42_outer_bound": exact_a42_outer,
        "exact_data_A43_direct_risk": exact_direct,
        "exact_data_outer_excess_percent": (
            (exact_a42_outer / exact_direct - 1) * 100
        ),
        "noisy_A42_outer_bound": noisy_a42_outer,
        "noisy_A43_direct_risk": noisy_direct,
        "noisy_outer_excess_percent": (
            (noisy_a42_outer / noisy_direct - 1) * 100
        ),
    }

    gates = {
        "all_10_exact_designs_certified": bool(
            len(exact_contract["certificates"]) == 10
        ),
        "all_10_noisy_designs_certified": bool(
            len(noisy_contract["certificates"]) == 10
        ),
        "all_internal_certificate_gates_pass": bool(
            all(certificate_gates)
        ),
        "exact_winner_is_234": bool(
            exact_contract["winner"] == [2, 3, 4]
        ),
        "exact_winner_unique": bool(
            exact_contract["unique_winner"]
        ),
        "noisy_winner_is_236": bool(
            noisy_contract["winner"] == [2, 3, 6]
        ),
        "noisy_winner_unique": bool(
            noisy_contract["unique_winner"]
        ),
        "exact_winner_ratio_matches_closed_form": bool(
            sp.Rational(exact_contract["winner_ratio_exact"])
            == sp.Rational(8770, 8707)
        ),
        "noisy_winner_ratio_matches_closed_form": bool(
            sp.Rational(noisy_contract["winner_ratio_exact"])
            == sp.Rational(
                1828961429248,
                1804118444725,
            )
        ),
        "A42_and_A43_winners_agree_at_both_benchmarks": bool(
            exact_contract["winner"] == [2, 3, 4]
            and noisy_contract["winner"] == [2, 3, 6]
        ),
        "direct_risks_are_strictly_below_A42_outer_bounds": bool(
            exact_direct < exact_a42_outer
            and noisy_direct < noisy_a42_outer
        ),
    }

    verdict = (
        "PASS_DIRECT_Q_MINIMAX_DESIGN_WITH_EXACT_FRACTIONAL_CERTIFICATES"
        if all(gates.values())
        else "FAIL_A43_DIRECT_Q_DESIGN_AUDIT"
    )

    result = {
        "audit": "A43_PROVISIONAL_DIRECT_Q_MINIMAX_DESIGN",
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "target": "future Q at 2*log(2) under contraction a=1/2",
            "candidate_parameters": [
                f"{value}*log(2)"
                for value in CANDIDATES
            ],
            "budget": 3,
            "risk": (
                "worst possible nonlinear future-score interval width "
                "over all compatible reported-data boxes"
            ),
        },
        "method": (
            "pairwise maximum target-transform ratio followed by "
            "Charnes-Cooper exact linear-programme reduction"
        ),
        "exact_data_contract": exact_contract,
        "noisy_contract": noisy_contract,
        "comparison_with_A42": comparison,
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The direct optimum is exact only for the declared finite support, "
            "mean, catalogue, budget, target, contraction, and absolute-error "
            "contracts. Agreement with A42 at the two benchmarks is not a "
            "general equivalence theorem. No continuous-parameter or physical "
            "measurement optimum is claimed."
        ),
    }

    output_path = Path(__file__).with_name(
        "a43_direct_q_minimax_design_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
