#!/usr/bin/env python3
"""A42 exact finite-catalogue minimax transform-design audit.

The audit exhaustively evaluates all 10 three-parameter designs selected from
{2,3,4,5,6}*log(2). Two declared error contracts are tested:

1. epsilon = 0;
2. epsilon = 1/10000.

Each design value is certified by exact rational primal and dual feasible
solutions with equal objective values. No design ranking depends on floating
point optimization.
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


def row(k: int) -> list[sp.Rational]:
    return [sp.Rational(1, 2 ** (k * x)) for x in SUPPORT]


ZERO_PATTERN = {
    design: ([0, 1, 3, 5], [0, 2, 4], None)
    for design in DESIGNS
}

NOISY_PATTERN = {
    (2, 3, 4): ([0, 3, 5], [0, 1, 2, 4], [1, -1, 1]),
    (2, 3, 5): ([0, 3, 5], [0, 1, 2, 4], [1, -1, 1]),
    (2, 3, 6): ([0, 3, 5], [0, 1, 2, 4], [1, -1, 1]),
    (2, 4, 5): ([0, 2, 3, 5], [0, 1, 4], [1, -1, 1]),
    (2, 4, 6): ([0, 3, 5], [0, 1, 2, 4], [1, -1, 1]),
    (2, 5, 6): ([0, 2, 3, 5], [0, 1, 4], [1, -1, 1]),
    (3, 4, 5): ([0, 2, 3, 5], [0, 1, 4], [1, -1, 1]),
    (3, 4, 6): ([0, 2, 3, 5], [0, 1, 4], [1, -1, 1]),
    (3, 5, 6): ([0, 2, 5], [0, 1, 3, 4], [1, -1, 1]),
    (4, 5, 6): ([0, 2, 5], [0, 1, 3], [1, -1, 0]),
}


def exact_certificate(
    design: tuple[int, int, int],
    epsilon: sp.Rational,
    p_indices: list[int],
    q_indices: list[int],
    signs: list[int] | None,
) -> dict[str, Any]:
    pvars = sp.symbols(f"p0:{len(p_indices)}")
    qvars = sp.symbols(f"q0:{len(q_indices)}")

    equations = [
        sp.Eq(sum(pvars), 1),
        sp.Eq(sum(qvars), 1),
        sp.Eq(
            sum(sp.Rational(p_indices[i]) * pvars[i] for i in range(len(p_indices))),
            MEAN,
        ),
        sp.Eq(
            sum(sp.Rational(q_indices[i]) * qvars[i] for i in range(len(q_indices))),
            MEAN,
        ),
    ]

    if epsilon == 0:
        for k in design:
            equations.append(
                sp.Eq(
                    sum(row(k)[p_indices[i]] * pvars[i] for i in range(len(p_indices)))
                    - sum(row(k)[q_indices[i]] * qvars[i] for i in range(len(q_indices))),
                    0,
                )
            )
    else:
        assert signs is not None
        for k, sign in zip(design, signs):
            if sign != 0:
                equations.append(
                    sp.Eq(
                        sum(row(k)[p_indices[i]] * pvars[i] for i in range(len(p_indices)))
                        - sum(row(k)[q_indices[i]] * qvars[i] for i in range(len(q_indices))),
                        2 * sign * epsilon,
                    )
                )

    solutions = sp.solve(equations, list(pvars) + list(qvars), dict=True)
    if len(solutions) != 1:
        raise RuntimeError(f"Unexpected primal solution count for {design}: {len(solutions)}")
    solution = solutions[0]

    z = [sp.Rational(0)] * 12
    for i, index in enumerate(p_indices):
        z[index] = sp.factor(solution[pvars[i]])
    for i, index in enumerate(q_indices):
        z[6 + index] = sp.factor(solution[qvars[i]])

    objective_coefficients = TARGET + [-value for value in TARGET]
    primal_objective = sp.factor(
        sum(objective_coefficients[i] * z[i] for i in range(12))
    )

    base_rows = [
        [sp.Rational(1)] * 6 + [sp.Rational(0)] * 6,
        [sp.Rational(0)] * 6 + [sp.Rational(1)] * 6,
        [sp.Rational(x) for x in SUPPORT] + [sp.Rational(0)] * 6,
        [sp.Rational(0)] * 6 + [sp.Rational(x) for x in SUPPORT],
    ]
    base_rhs = [sp.Rational(1), sp.Rational(1), MEAN, MEAN]

    positive_indices = [i for i, value in enumerate(z) if value > 0]

    if epsilon == 0:
        dual_rows = list(base_rows)
        dual_rhs = list(base_rhs)
        for k in design:
            values = row(k)
            dual_rows.append(values + [-value for value in values])
            dual_rhs.append(sp.Rational(0))

        dual_symbols = sp.symbols(f"y0:{len(dual_rows)}")
        dual_equations = [
            sp.Eq(
                sum(dual_symbols[j] * dual_rows[j][index] for j in range(len(dual_rows))),
                objective_coefficients[index],
            )
            for index in positive_indices
        ]
        dual_solutions = sp.solve(dual_equations, list(dual_symbols), dict=True)
        if len(dual_solutions) != 1:
            raise RuntimeError(f"Unexpected exact-data dual solution for {design}")
        dual_solution = dual_solutions[0]
        dual_values = [sp.factor(dual_solution[symbol]) for symbol in dual_symbols]
        nonnegative_multiplier_gate = True
    else:
        assert signs is not None
        active_observations: list[tuple[int, int]] = []
        dual_rows = list(base_rows)
        dual_rhs = list(base_rhs)

        for k, sign in zip(design, signs):
            if sign != 0:
                values = row(k)
                signed = [sign * value for value in values]
                dual_rows.append(signed + [-value for value in signed])
                dual_rhs.append(2 * epsilon)
                active_observations.append((k, sign))

        free_symbols = sp.symbols("y0:4")
        nonnegative_symbols = sp.symbols(f"u0:{len(active_observations)}")
        dual_symbols = list(free_symbols) + list(nonnegative_symbols)

        dual_equations = [
            sp.Eq(
                sum(free_symbols[j] * dual_rows[j][index] for j in range(4))
                + sum(
                    nonnegative_symbols[j] * dual_rows[4 + j][index]
                    for j in range(len(active_observations))
                ),
                objective_coefficients[index],
            )
            for index in positive_indices
        ]
        dual_solutions = sp.solve(dual_equations, dual_symbols, dict=True)
        if len(dual_solutions) != 1:
            raise RuntimeError(f"Unexpected noisy dual solution for {design}")
        dual_solution = dual_solutions[0]
        dual_values = [sp.factor(dual_solution[symbol]) for symbol in dual_symbols]
        nonnegative_multiplier_gate = all(
            dual_values[4 + j] >= 0 for j in range(len(active_observations))
        )

    dual_lhs = [
        sp.factor(
            sum(dual_values[j] * dual_rows[j][i] for j in range(len(dual_rows)))
        )
        for i in range(12)
    ]
    reduced_costs = [
        sp.factor(dual_lhs[i] - objective_coefficients[i]) for i in range(12)
    ]
    dual_objective = sp.factor(
        sum(dual_rhs[j] * dual_values[j] for j in range(len(dual_rows)))
    )

    p = z[:6]
    q = z[6:]
    difference = [sp.factor(p[i] - q[i]) for i in range(6)]
    observed_differences = {
        str(k): sp.factor(sum(row(k)[i] * difference[i] for i in range(6)))
        for k in design
    }

    tolerance_gate = all(
        abs(value) <= 2 * epsilon
        for value in observed_differences.values()
    ) if epsilon > 0 else all(value == 0 for value in observed_differences.values())

    gates = {
        "primal_weights_nonnegative": bool(all(value >= 0 for value in z)),
        "p_normalized": bool(sp.factor(sum(p)) == 1),
        "q_normalized": bool(sp.factor(sum(q)) == 1),
        "p_mean_exact": bool(sp.factor(sum(SUPPORT[i] * p[i] for i in range(6))) == MEAN),
        "q_mean_exact": bool(sp.factor(sum(SUPPORT[i] * q[i] for i in range(6))) == MEAN),
        "observed_constraints_satisfied": bool(tolerance_gate),
        "dual_reduced_costs_nonnegative": bool(all(value >= 0 for value in reduced_costs)),
        "dual_inequality_multipliers_nonnegative": bool(nonnegative_multiplier_gate),
        "primal_dual_objectives_equal": bool(sp.factor(primal_objective - dual_objective) == 0),
    }

    return {
        "design": list(design),
        "epsilon": str(epsilon),
        "risk_exact": str(primal_objective),
        "risk_decimal": f"{float(primal_objective):.18g}",
        "p": [str(value) for value in p],
        "q": [str(value) for value in q],
        "observed_differences": {
            key: str(value) for key, value in observed_differences.items()
        },
        "dual_values": [str(value) for value in dual_values],
        "reduced_costs": [str(value) for value in reduced_costs],
        "gates": gates,
    }


def audit_contract(
    epsilon: sp.Rational,
    patterns: dict[
        tuple[int, int, int],
        tuple[list[int], list[int], list[int] | None],
    ],
) -> dict[str, Any]:
    results = []
    for design in DESIGNS:
        p_indices, q_indices, signs = patterns[design]
        results.append(
            exact_certificate(
                design,
                epsilon,
                p_indices,
                q_indices,
                signs,
            )
        )

    ranked = sorted(results, key=lambda item: sp.Rational(item["risk_exact"]))
    winner = ranked[0]
    unique_winner = bool(
        sp.Rational(ranked[0]["risk_exact"])
        < sp.Rational(ranked[1]["risk_exact"])
    )

    return {
        "epsilon": str(epsilon),
        "ranking": [
            {
                "design": item["design"],
                "risk_exact": item["risk_exact"],
                "risk_decimal": item["risk_decimal"],
            }
            for item in ranked
        ],
        "winner": winner["design"],
        "winner_risk_exact": winner["risk_exact"],
        "winner_risk_decimal": winner["risk_decimal"],
        "unique_winner": unique_winner,
        "certificates": results,
    }


def main() -> None:
    exact_contract = audit_contract(sp.Rational(0), ZERO_PATTERN)
    noisy_contract = audit_contract(sp.Rational(1, 10000), NOISY_PATTERN)

    exact_winner_gate = exact_contract["winner"] == [2, 3, 4]
    noisy_winner_gate = noisy_contract["winner"] == [2, 3, 6]

    certificate_gates = []
    for contract in [exact_contract, noisy_contract]:
        for certificate in contract["certificates"]:
            certificate_gates.extend(certificate["gates"].values())

    exact_best = sp.Rational(exact_contract["winner_risk_exact"])
    noisy_best = sp.Rational(noisy_contract["winner_risk_exact"])

    exact_future_outer = sp.Rational(1, 2) * (
        sp.log(1 + sp.Rational(16, 3) * exact_best) / sp.log(2)
    )
    noisy_future_outer = sp.Rational(1, 2) * (
        sp.log(1 + sp.Rational(16, 3) * noisy_best) / sp.log(2)
    )

    comparison = {
        "zero_noise_relative_penalty_of_236_vs_234_percent": (
            float(
                (
                    sp.Rational(93, 34384)
                    / sp.Rational(105, 44432)
                    - 1
                )
                * 100
            )
        ),
        "epsilon_1e-4_improvement_of_236_vs_234_percent": (
            float(
                (
                    1
                    - sp.Rational(12851927671, 2974447980000)
                    / sp.Rational(13961617, 2900100000)
                )
                * 100
            )
        ),
        "induced_future_width_outer_bound_zero_noise": float(exact_future_outer),
        "induced_future_width_outer_bound_epsilon_1e-4": float(noisy_future_outer),
    }

    gates = {
        "all_10_exact_data_designs_certified": bool(len(exact_contract["certificates"]) == 10),
        "all_10_noisy_designs_certified": bool(len(noisy_contract["certificates"]) == 10),
        "all_primal_dual_certificate_gates_pass": bool(all(certificate_gates)),
        "exact_data_winner_is_234": bool(exact_winner_gate),
        "exact_data_winner_is_unique": bool(exact_contract["unique_winner"]),
        "noisy_winner_is_236": bool(noisy_winner_gate),
        "noisy_winner_is_unique": bool(noisy_contract["unique_winner"]),
        "optimal_design_changes_with_error_contract": bool(
            exact_contract["winner"] != noisy_contract["winner"]
        ),
        "exact_best_value_matches_closed_form": bool(
            exact_best == sp.Rational(105, 44432)
        ),
        "noisy_best_value_matches_closed_form": bool(
            noisy_best == sp.Rational(12851927671, 2974447980000)
        ),
    }

    verdict = (
        "PASS_FINITE_CATALOGUE_MINIMAX_DESIGN_WITH_NOISE_DEPENDENT_OPTIMUM"
        if all(gates.values())
        else "FAIL_A42_DESIGN_AUDIT"
    )

    result = {
        "audit": "A42_PROVISIONAL_FINITE_BUDGET_DESIGN",
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "target": "L(log(2))",
            "candidate_parameters": [f"{k}*log(2)" for k in CANDIDATES],
            "budget": 3,
            "risk": (
                "worst possible omitted-transform interval width over all reported "
                "data boxes compatible with the declared support, mean, and tolerance"
            ),
        },
        "exact_data_contract": exact_contract,
        "noisy_contract": noisy_contract,
        "comparison": comparison,
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The optimum is exact only within the declared finite candidate catalogue, "
            "support, mean, budget, absolute-error geometry, and transform-width risk. "
            "It is not a continuous-parameter optimum, a physical measurement design, "
            "or an exact minimax result for nonlinear Q-width."
        ),
    }

    output_path = Path(__file__).with_name("a42_finite_budget_design_results.json")
    output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
