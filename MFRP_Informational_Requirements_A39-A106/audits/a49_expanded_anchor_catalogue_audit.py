#!/usr/bin/env python3
"""A49 exact expanded target-excluding anchor catalogue audit.

Candidate exponents:
    {2,3,4,5,6,7,8,9,10}

Budget:
    3 observations

Contracts:
    epsilon = 0
    epsilon = 1/10000

All 84 designs are solved at both contracts using SymPy's exact rational
simplex implementation. The primal and dual programmes are solved
independently and their exact objective values are compared.

The script also verifies consistency with A43 and the continuous boundary
value from A44.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.solvers.simplex import lpmax, lpmin


HERE = Path(__file__).resolve().parent
A43_RESULTS = HERE / "a43_direct_q_minimax_design_results.json"
A44_RESULTS = HERE / "a44_continuous_parameter_results.json"

SUPPORT = list(range(6))
TARGET = [sp.Rational(1, 2**x) for x in SUPPORT]
MEAN = sp.Rational(5, 2)
CATALOGUE = list(range(2, 11))
DESIGNS = list(itertools.combinations(CATALOGUE, 3))

YP = sp.symbols("yp0:6")
YQ = sp.symbols("yq0:6")
T = sp.symbols("t")
PRIMAL_VARIABLES = list(YP) + list(YQ) + [T]


def transform_row(exponent: int) -> list[sp.Rational]:
    return [
        sp.Rational(1, 2 ** (exponent * x))
        for x in SUPPORT
    ]


def build_matrices(
    design: tuple[int, int, int],
    epsilon: sp.Rational,
) -> tuple[
    list[list[sp.Rational]],
    list[sp.Rational],
    list[list[sp.Rational]],
    list[sp.Rational],
    list[sp.Rational],
]:
    a_eq: list[list[sp.Rational]] = []
    b_eq: list[sp.Rational] = []

    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[index] = 1
    row[12] = -1
    a_eq.append(row)
    b_eq.append(0)

    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[6 + index] = 1
    row[12] = -1
    a_eq.append(row)
    b_eq.append(0)

    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[index] = index
    row[12] = -MEAN
    a_eq.append(row)
    b_eq.append(0)

    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[6 + index] = index
    row[12] = -MEAN
    a_eq.append(row)
    b_eq.append(0)

    row = [sp.Rational(0)] * 13
    for index in range(6):
        row[6 + index] = TARGET[index]
    a_eq.append(row)
    b_eq.append(1)

    a_ub: list[list[sp.Rational]] = []
    b_ub: list[sp.Rational] = []

    for exponent in design:
        values = transform_row(exponent)

        difference = [sp.Rational(0)] * 13
        for index in range(6):
            difference[index] = values[index]
            difference[6 + index] = -values[index]

        if epsilon == 0:
            a_eq.append(difference)
            b_eq.append(0)
        else:
            positive = list(difference)
            positive[12] = -2 * epsilon
            a_ub.append(positive)
            b_ub.append(0)

            negative = [-value for value in difference]
            negative[12] = -2 * epsilon
            a_ub.append(negative)
            b_ub.append(0)

    objective = [sp.Rational(0)] * 13
    for index in range(6):
        objective[index] = TARGET[index]

    return a_eq, b_eq, a_ub, b_ub, objective


def solve_primal(
    design: tuple[int, int, int],
    epsilon: sp.Rational,
) -> tuple[sp.Rational, dict[sp.Symbol, sp.Expr]]:
    objective = sum(
        TARGET[index] * YP[index]
        for index in range(6)
    )

    constraints: list[sp.Rel] = [
        sp.Eq(sum(YP), T),
        sp.Eq(sum(YQ), T),
        sp.Eq(
            sum(index * YP[index] for index in range(6)),
            MEAN * T,
        ),
        sp.Eq(
            sum(index * YQ[index] for index in range(6)),
            MEAN * T,
        ),
        sp.Eq(
            sum(TARGET[index] * YQ[index] for index in range(6)),
            1,
        ),
    ]

    constraints.extend(
        variable >= 0
        for variable in PRIMAL_VARIABLES
    )

    for exponent in design:
        values = transform_row(exponent)
        difference = sum(
            values[index] * (YP[index] - YQ[index])
            for index in range(6)
        )

        if epsilon == 0:
            constraints.append(sp.Eq(difference, 0))
        else:
            constraints.append(difference <= 2 * epsilon * T)
            constraints.append(-difference <= 2 * epsilon * T)

    value, solution = lpmax(objective, constraints)
    return sp.factor(value), solution


def solve_dual(
    design: tuple[int, int, int],
    epsilon: sp.Rational,
) -> tuple[sp.Rational, dict[sp.Symbol, sp.Expr]]:
    a_eq, b_eq, a_ub, b_ub, objective = build_matrices(
        design,
        epsilon,
    )

    equality_count = len(a_eq)
    inequality_count = len(a_ub)

    y_plus = sp.symbols(f"ypd0:{equality_count}")
    y_minus = sp.symbols(f"ymd0:{equality_count}")
    u = (
        sp.symbols(f"ud0:{inequality_count}")
        if inequality_count
        else ()
    )

    dual_variables = list(y_plus) + list(y_minus) + list(u)

    dual_objective = sum(
        b_eq[index] * (y_plus[index] - y_minus[index])
        for index in range(equality_count)
    )
    dual_objective += sum(
        b_ub[index] * u[index]
        for index in range(inequality_count)
    )

    constraints: list[sp.Rel] = [
        variable >= 0
        for variable in dual_variables
    ]

    for column in range(13):
        lhs = sum(
            a_eq[row][column]
            * (y_plus[row] - y_minus[row])
            for row in range(equality_count)
        )
        lhs += sum(
            a_ub[row][column] * u[row]
            for row in range(inequality_count)
        )
        constraints.append(lhs >= objective[column])

    value, solution = lpmin(dual_objective, constraints)
    return sp.factor(value), solution


def validate_primal(
    design: tuple[int, int, int],
    epsilon: sp.Rational,
    value: sp.Rational,
    solution: dict[sp.Symbol, sp.Expr],
) -> dict[str, bool]:
    z = [
        sp.factor(solution.get(variable, 0))
        for variable in PRIMAL_VARIABLES
    ]

    y_p = z[:6]
    y_q = z[6:12]
    scale = z[12]

    observation_gates = []
    for exponent in design:
        values = transform_row(exponent)
        difference = sp.factor(
            sum(values[index] * y_p[index] for index in range(6))
            -
            sum(values[index] * y_q[index] for index in range(6))
        )

        if epsilon == 0:
            observation_gates.append(difference == 0)
        else:
            observation_gates.append(
                abs(difference) <= 2 * epsilon * scale
            )

    objective_value = sp.factor(
        sum(TARGET[index] * y_p[index] for index in range(6))
    )

    return {
        "variables_nonnegative": bool(all(item >= 0 for item in z)),
        "p_normalization_cc": bool(sp.factor(sum(y_p) - scale) == 0),
        "q_normalization_cc": bool(sp.factor(sum(y_q) - scale) == 0),
        "p_mean_cc": bool(
            sp.factor(
                sum(index * y_p[index] for index in range(6))
                - MEAN * scale
            )
            == 0
        ),
        "q_mean_cc": bool(
            sp.factor(
                sum(index * y_q[index] for index in range(6))
                - MEAN * scale
            )
            == 0
        ),
        "denominator_normalization": bool(
            sp.factor(
                sum(TARGET[index] * y_q[index] for index in range(6))
                - 1
            )
            == 0
        ),
        "observation_constraints": bool(all(observation_gates)),
        "objective_matches_solver_value": bool(
            sp.factor(objective_value - value) == 0
        ),
        "scale_positive": bool(scale > 0),
    }


def validate_dual(
    solution: dict[sp.Symbol, sp.Expr],
) -> bool:
    return bool(
        all(
            value >= 0
            for value in solution.values()
        )
    )


def audit_design(
    design: tuple[int, int, int],
    epsilon: sp.Rational,
) -> dict[str, Any]:
    primal_value, primal_solution = solve_primal(design, epsilon)
    dual_value, dual_solution = solve_dual(design, epsilon)

    primal_gates = validate_primal(
        design,
        epsilon,
        primal_value,
        primal_solution,
    )

    primal_vector = [
        sp.factor(primal_solution.get(variable, 0))
        for variable in PRIMAL_VARIABLES
    ]
    scale = primal_vector[12]
    p = [
        sp.factor(primal_vector[index] / scale)
        for index in range(6)
    ]
    q = [
        sp.factor(primal_vector[6 + index] / scale)
        for index in range(6)
    ]

    gates = {
        **primal_gates,
        "dual_variables_nonnegative": validate_dual(dual_solution),
        "primal_dual_objectives_equal": bool(
            sp.factor(primal_value - dual_value) == 0
        ),
    }

    future_risk = (
        sp.log(primal_value)
        / (2 * sp.log(2))
    )

    return {
        "design": list(design),
        "epsilon": str(epsilon),
        "ratio_exact": str(primal_value),
        "ratio_decimal": f"{float(primal_value):.18g}",
        "future_score_risk_decimal": f"{float(future_risk):.18g}",
        "p": [str(item) for item in p],
        "q": [str(item) for item in q],
        "primal_solution": {
            str(variable): str(
                primal_solution.get(variable, 0)
            )
            for variable in PRIMAL_VARIABLES
        },
        "dual_solution": {
            str(variable): str(value)
            for variable, value in dual_solution.items()
        },
        "gates": gates,
    }


def audit_contract(
    epsilon: sp.Rational,
) -> dict[str, Any]:
    certificates = [
        audit_design(design, epsilon)
        for design in DESIGNS
    ]

    ranking = sorted(
        certificates,
        key=lambda item: sp.Rational(item["ratio_exact"]),
    )

    winner_ratio = sp.Rational(ranking[0]["ratio_exact"])
    unique_winner = bool(
        winner_ratio
        <
        sp.Rational(ranking[1]["ratio_exact"])
    )

    best_without_pair = next(
        item
        for item in ranking
        if not (
            2 in item["design"]
            and 3 in item["design"]
        )
    )

    winner_risk = sp.Float(
        ranking[0]["future_score_risk_decimal"],
        50,
    )
    best_without_pair_risk = sp.Float(
        best_without_pair["future_score_risk_decimal"],
        50,
    )

    return {
        "epsilon": str(epsilon),
        "winner": ranking[0]["design"],
        "winner_ratio_exact": ranking[0]["ratio_exact"],
        "winner_future_score_risk_decimal": ranking[0][
            "future_score_risk_decimal"
        ],
        "unique_winner": unique_winner,
        "best_without_anchor_pair": {
            "design": best_without_pair["design"],
            "ratio_exact": best_without_pair["ratio_exact"],
            "future_score_risk_decimal": best_without_pair[
                "future_score_risk_decimal"
            ],
            "winner_improvement_percent": str(
                sp.N(
                    100
                    * (
                        1
                        - winner_risk
                        / best_without_pair_risk
                    ),
                    40,
                )
            ),
        },
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
        "certificates": certificates,
    }


def a43_consistency(
    current: dict[str, Any],
    a43_contract: dict[str, Any],
) -> bool:
    current_lookup = {
        tuple(item["design"]): item["ratio_exact"]
        for item in current["ranking"]
        if max(item["design"]) <= 6
    }
    previous_lookup = {
        tuple(item["design"]): item["ratio_exact"]
        for item in a43_contract["ranking"]
    }
    return current_lookup == previous_lookup


def main() -> None:
    if not A43_RESULTS.exists():
        raise FileNotFoundError(A43_RESULTS)
    if not A44_RESULTS.exists():
        raise FileNotFoundError(A44_RESULTS)

    a43 = json.loads(A43_RESULTS.read_text(encoding="utf-8"))
    a44 = json.loads(A44_RESULTS.read_text(encoding="utf-8"))

    exact_contract = audit_contract(sp.Rational(0))
    noisy_contract = audit_contract(sp.Rational(1, 10000))

    all_internal_gates = [
        gate
        for contract in [exact_contract, noisy_contract]
        for certificate in contract["certificates"]
        for gate in certificate["gates"].values()
    ]

    continuous_ratio = sp.Rational(
        a44["noisy_compactified_result"]["infinity_ratio"]
    )
    finite_ratio = sp.Rational(
        noisy_contract["winner_ratio_exact"]
    )

    continuous_risk = (
        sp.log(continuous_ratio)
        / (2 * sp.log(2))
    )
    finite_risk = (
        sp.log(finite_ratio)
        / (2 * sp.log(2))
    )

    gates = {
        "catalogue_has_9_parameters": bool(len(CATALOGUE) == 9),
        "catalogue_has_84_designs": bool(len(DESIGNS) == 84),
        "168_exact_primal_dual_certificates": bool(
            len(exact_contract["certificates"])
            + len(noisy_contract["certificates"])
            == 168
        ),
        "all_internal_certificate_gates_pass": bool(
            all(all_internal_gates)
        ),
        "exact_winner_is_234": bool(
            exact_contract["winner"] == [2, 3, 4]
        ),
        "exact_winner_unique": bool(
            exact_contract["unique_winner"]
        ),
        "noisy_winner_is_2310": bool(
            noisy_contract["winner"] == [2, 3, 10]
        ),
        "noisy_winner_unique": bool(
            noisy_contract["unique_winner"]
        ),
        "exact_top_7_contain_anchor_pair": bool(
            all(
                2 in item["design"] and 3 in item["design"]
                for item in exact_contract["ranking"][:7]
            )
        ),
        "noisy_top_6_contain_anchor_pair": bool(
            all(
                2 in item["design"] and 3 in item["design"]
                for item in noisy_contract["ranking"][:6]
            )
        ),
        "A43_exact_subcatalogue_reproduced": a43_consistency(
            exact_contract,
            a43["exact_data_contract"],
        ),
        "A43_noisy_subcatalogue_reproduced": a43_consistency(
            noisy_contract,
            a43["noisy_contract"],
        ),
        "finite_noisy_winner_above_continuous_boundary": bool(
            finite_ratio > continuous_ratio
        ),
        "finite_noisy_risk_gap_below_0_04_percent": bool(
            100 * (finite_risk / continuous_risk - 1)
            < sp.Rational(4, 100)
        ),
    }

    verdict = (
        "PASS_EXPANDED_TARGET_EXCLUDING_ANCHOR_CATALOGUE"
        if all(gates.values())
        else "FAIL_A49_EXPANDED_ANCHOR_CATALOGUE"
    )

    result = {
        "audit": "A49_EXPANDED_TARGET_EXCLUDING_ANCHOR_CATALOGUE",
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "target_exponent": 1,
            "candidate_exponents": CATALOGUE,
            "budget": 3,
            "design_count": len(DESIGNS),
            "error_contracts": ["0", "1/10000"],
        },
        "exact_contract": exact_contract,
        "noisy_contract": noisy_contract,
        "continuous_comparison": {
            "finite_winner_design": noisy_contract["winner"],
            "finite_winner_ratio": str(finite_ratio),
            "continuous_infinity_ratio": str(continuous_ratio),
            "finite_future_risk": str(sp.N(finite_risk, 40)),
            "continuous_future_risk": str(sp.N(continuous_risk, 40)),
            "finite_excess_percent": str(
                sp.N(
                    100
                    * (
                        finite_risk / continuous_risk
                        - 1
                    ),
                    40,
                )
            ),
        },
        "formal_results": [
            "84 target-excluding designs audited at two error contracts",
            "168 independent exact primal-dual certificates",
            "unique exact winner {2,3,4}",
            "unique noisy winner {2,3,10}",
            "lower anchor pair {2,3} selected at both contracts",
            "A43 subcatalogue exactly reproduced",
            "finite noisy cap lies within 0.04 percent of compactified optimum",
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The result is exact only for the integer catalogue "
            "{2,...,10}, the six-point support, exact mean, common "
            "absolute-error contracts, and direct future-Q risk. "
            "It does not prove continuous global anchor optimality."
        ),
    }

    output_path = HERE / (
        "a49_expanded_target_excluding_anchor_catalogue_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "exact_winner": exact_contract["winner"],
        "exact_ratio": exact_contract["winner_ratio_exact"],
        "noisy_winner": noisy_contract["winner"],
        "noisy_ratio": noisy_contract["winner_ratio_exact"],
        "continuous_gap_percent": result[
            "continuous_comparison"
        ]["finite_excess_percent"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": verdict,
    }

    print(json.dumps(summary, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
