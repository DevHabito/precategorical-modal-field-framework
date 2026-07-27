#!/usr/bin/env python3
"""A55 exact audit: finite-cap implementability of the A54 optimum.

The script proves that the A52 final active basis remains primal-dual optimal
for the fixed design {2,beta*,Gamma} whenever Gamma >= 6.

It then combines:
- the A54 universal minimax lower bound;
- the exact fixed-design finite-cap value;

to produce a rigorous sandwich for the fully reoptimized finite-cap problem.

All sign certificates use exact rational Bernstein subdivision.
"""

from __future__ import annotations

import importlib.util
import json
from math import comb
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A52_SCRIPT = HERE / "a52_continuous_second_anchor_audit.py"
A52_RESULTS = HERE / "a52_continuous_second_anchor_results.json"
A54_RESULTS = HERE / "a54_universal_continuum_witness_results.json"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")

    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def bernstein_coefficients_2d(
    polynomial: sp.Poly,
    x: sp.Symbol,
    y: sp.Symbol,
) -> dict[tuple[int, int], sp.Rational]:
    degree_x = polynomial.degree(x)
    degree_y = polynomial.degree(y)

    coefficients = {
        (index_x, index_y): sp.Rational(0)
        for index_x in range(degree_x + 1)
        for index_y in range(degree_y + 1)
    }

    for (power_x, power_y), coefficient in polynomial.terms():
        for index_x in range(power_x, degree_x + 1):
            factor_x = sp.Rational(
                comb(index_x, power_x),
                comb(degree_x, power_x),
            )

            for index_y in range(power_y, degree_y + 1):
                factor_y = sp.Rational(
                    comb(index_y, power_y),
                    comb(degree_y, power_y),
                )

                coefficients[(index_x, index_y)] += (
                    coefficient * factor_x * factor_y
                )

    return coefficients


def polynomial_sign_on_box(
    polynomial: sp.Expr,
    s: sp.Symbol,
    r: sp.Symbol,
    s_lower: sp.Rational,
    s_upper: sp.Rational,
    r_lower: sp.Rational,
    r_upper: sp.Rational,
) -> int | None:
    """Return +1/-1 if Bernstein coefficients certify a strict sign."""

    u, v = sp.symbols("u v", real=True)

    mapped = sp.Poly(
        sp.expand(
            polynomial.subs(
                {
                    s: s_lower + (s_upper - s_lower) * u,
                    r: r_lower + (r_upper - r_lower) * v,
                }
            )
        ),
        u,
        v,
        domain=sp.QQ,
    )

    coefficients = bernstein_coefficients_2d(mapped, u, v)
    minimum = min(coefficients.values())
    maximum = max(coefficients.values())

    if minimum > 0:
        return 1
    if maximum < 0:
        return -1
    return None


def certify_rational_sign_adaptive(
    expression: sp.Expr,
    desired_sign: int,
    s: sp.Symbol,
    r: sp.Symbol,
    box: tuple[
        sp.Rational,
        sp.Rational,
        sp.Rational,
        sp.Rational,
    ],
    depth: int = 0,
    max_depth: int = 7,
) -> dict[str, Any]:
    expression = sp.cancel(expression)

    if expression == 0:
        return {
            "ok": desired_sign == 0,
            "leaf_count": 1,
            "max_depth_used": depth,
            "identically_zero": True,
        }

    numerator, denominator = sp.fraction(expression)
    s_lower, s_upper, r_lower, r_upper = box

    numerator_sign = polynomial_sign_on_box(
        numerator,
        s,
        r,
        s_lower,
        s_upper,
        r_lower,
        r_upper,
    )
    denominator_sign = polynomial_sign_on_box(
        denominator,
        s,
        r,
        s_lower,
        s_upper,
        r_lower,
        r_upper,
    )

    if (
        numerator_sign is not None
        and denominator_sign is not None
        and numerator_sign * denominator_sign == desired_sign
    ):
        return {
            "ok": True,
            "leaf_count": 1,
            "max_depth_used": depth,
            "identically_zero": False,
        }

    if depth >= max_depth:
        return {
            "ok": False,
            "leaf_count": 1,
            "max_depth_used": depth,
            "identically_zero": False,
            "box": [str(item) for item in box],
            "numerator_sign": numerator_sign,
            "denominator_sign": denominator_sign,
        }

    s_width = s_upper - s_lower
    r_width = r_upper - r_lower

    if s_width >= r_width:
        midpoint = (s_lower + s_upper) / 2
        children = [
            (s_lower, midpoint, r_lower, r_upper),
            (midpoint, s_upper, r_lower, r_upper),
        ]
    else:
        midpoint = (r_lower + r_upper) / 2
        children = [
            (s_lower, s_upper, r_lower, midpoint),
            (s_lower, s_upper, midpoint, r_upper),
        ]

    child_results = [
        certify_rational_sign_adaptive(
            expression,
            desired_sign,
            s,
            r,
            child,
            depth + 1,
            max_depth,
        )
        for child in children
    ]

    return {
        "ok": all(result["ok"] for result in child_results),
        "leaf_count": sum(
            result["leaf_count"] for result in child_results
        ),
        "max_depth_used": max(
            result["max_depth_used"] for result in child_results
        ),
        "identically_zero": False,
        "children": child_results,
    }


def build_bivariate_certificate(module):
    s = module.s
    r = sp.symbols("r", real=True)

    support = list(range(6))
    target = [sp.Rational(1, 2**x) for x in support]
    mean = sp.Rational(5, 2)
    epsilon = sp.Rational(1, 10000)

    row_2 = [
        sp.Rational(1, 2 ** (2 * x))
        for x in support
    ]
    row_beta = [s**x for x in support]
    row_gamma = [r**x for x in support]

    rows: list[list[sp.Expr]] = []
    rhs: list[sp.Expr] = []

    row = [sp.Integer(0)] * 13
    for index in range(6):
        row[index] = 1
    row[12] = -1
    rows.append(row)
    rhs.append(0)

    row = [sp.Integer(0)] * 13
    for index in range(6):
        row[6 + index] = 1
    row[12] = -1
    rows.append(row)
    rhs.append(0)

    row = [sp.Integer(0)] * 13
    for index in range(6):
        row[index] = index
    row[12] = -mean
    rows.append(row)
    rhs.append(0)

    row = [sp.Integer(0)] * 13
    for index in range(6):
        row[6 + index] = index
    row[12] = -mean
    rows.append(row)
    rhs.append(0)

    row = [sp.Integer(0)] * 13
    for index in range(6):
        row[6 + index] = target[index]
    rows.append(row)
    rhs.append(1)

    for values, sign in [
        (row_2, 1),
        (row_beta, -1),
        (row_gamma, 1),
    ]:
        row = [sp.Integer(0)] * 13
        for index in range(6):
            row[index] = sign * values[index]
            row[6 + index] = -sign * values[index]
        row[12] = -2 * epsilon
        rows.append(row)
        rhs.append(0)

    p_support = [0, 1, 3, 5]
    q_support = [1, 2, 4]
    positive_indices = (
        p_support
        + [6 + index for index in q_support]
        + [12]
    )

    primal_matrix = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(len(rows))
        ]
    )

    primal_solution = primal_matrix.inv() * sp.Matrix(rhs)

    z = [sp.Integer(0)] * 13
    for index, value in zip(positive_indices, primal_solution):
        z[index] = sp.cancel(value)

    objective = [sp.Integer(0)] * 13
    for index in range(6):
        objective[index] = target[index]

    ratio = sp.cancel(
        sum(
            objective[index] * z[index]
            for index in range(13)
        )
    )

    dual_matrix = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for row_index in range(len(rows))
            ]
            for column_index in positive_indices
        ]
    )

    dual_solution = dual_matrix.inv() * sp.Matrix(
        [objective[index] for index in positive_indices]
    )
    dual = [sp.cancel(value) for value in dual_solution]

    reduced_costs = [
        sp.cancel(
            sum(
                rows[row_index][column_index]
                * dual[row_index]
                for row_index in range(len(rows))
            )
            - objective[column_index]
        )
        for column_index in range(13)
    ]

    return {
        "s": s,
        "r": r,
        "z": z,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "ratio": ratio,
        "positive_indices": positive_indices,
        "p_support": p_support,
        "q_support": q_support,
        "rows": rows,
        "rhs": rhs,
    }


def main() -> None:
    if not A52_SCRIPT.exists():
        raise FileNotFoundError(A52_SCRIPT)
    if not A52_RESULTS.exists():
        raise FileNotFoundError(A52_RESULTS)
    if not A54_RESULTS.exists():
        raise FileNotFoundError(A54_RESULTS)

    module = load_module(A52_SCRIPT, "a52_for_a55")
    a52_results = json.loads(
        A52_RESULTS.read_text(encoding="utf-8")
    )
    a54_results = json.loads(
        A54_RESULTS.read_text(encoding="utf-8")
    )

    certificate = build_bivariate_certificate(module)

    s = certificate["s"]
    r = certificate["r"]
    s_star = module.s_star

    s_lower = sp.Rational(3, 20)
    s_upper = sp.Rational(19, 125)
    r_lower = sp.Rational(0)
    r_upper = sp.Rational(1, 64)
    box = (s_lower, s_upper, r_lower, r_upper)

    active_primal_expressions = [
        certificate["z"][index]
        for index in certificate["positive_indices"]
    ]

    inequality_dual_expressions = certificate["dual"][5:]

    nonbasic_indices = [
        index
        for index in range(13)
        if index not in certificate["positive_indices"]
    ]
    reduced_cost_expressions = [
        certificate["reduced_costs"][index]
        for index in nonbasic_indices
        if certificate["reduced_costs"][index] != 0
    ]

    primal_signs = [
        certify_rational_sign_adaptive(
            expression,
            1,
            s,
            r,
            box,
        )
        for expression in active_primal_expressions
    ]

    dual_signs = [
        certify_rational_sign_adaptive(
            expression,
            1,
            s,
            r,
            box,
        )
        for expression in inequality_dual_expressions
    ]

    reduced_cost_signs = [
        certify_rational_sign_adaptive(
            expression,
            1,
            s,
            r,
            box,
        )
        for expression in reduced_cost_expressions
    ]

    ratio = certificate["ratio"]
    ratio_at_zero = sp.cancel(ratio.subs(r, 0))
    ratio_derivative = sp.cancel(
        sp.diff(ratio, r).subs(r, 0)
    )

    ratio_star = ratio_at_zero.subs(s, s_star)
    ratio_slope = ratio_derivative.subs(s, s_star)

    risk_star = (
        sp.log(ratio_star)
        / (2 * sp.log(2))
    )

    risk_slope = (
        ratio_slope
        / (
            2
            * sp.log(2)
            * ratio_star
        )
    )

    gamma_values = list(range(6, 21))
    table = []

    for gamma in gamma_values:
        r_value = sp.Rational(1, 2**gamma)
        ratio_value = ratio.subs(
            {
                s: s_star,
                r: r_value,
            }
        )
        risk_value = (
            sp.log(ratio_value)
            / (2 * sp.log(2))
        )
        absolute_excess = risk_value - risk_star
        relative_excess = (
            100 * absolute_excess / risk_star
        )

        table.append(
            {
                "gamma": gamma,
                "r": str(r_value),
                "ratio_decimal": str(
                    sp.N(ratio_value, 45)
                ),
                "risk_decimal": str(
                    sp.N(risk_value, 45)
                ),
                "absolute_excess_decimal": str(
                    sp.N(absolute_excess, 45)
                ),
                "relative_excess_percent": str(
                    sp.N(relative_excess, 45)
                ),
            }
        )

    threshold_requirements = {
        "relative_below_0_1_percent": next(
            row["gamma"]
            for row in table
            if sp.Float(
                row["relative_excess_percent"]
            )
            < sp.Rational(1, 10)
        ),
        "relative_below_0_05_percent": next(
            row["gamma"]
            for row in table
            if sp.Float(
                row["relative_excess_percent"]
            )
            < sp.Rational(5, 100)
        ),
        "relative_below_0_01_percent": next(
            row["gamma"]
            for row in table
            if sp.Float(
                row["relative_excess_percent"]
            )
            < sp.Rational(1, 100)
        ),
        "relative_below_0_001_percent": next(
            row["gamma"]
            for row in table
            if sp.Float(
                row["relative_excess_percent"]
            )
            < sp.Rational(1, 1000)
        ),
        "relative_below_0_0001_percent": next(
            row["gamma"]
            for row in table
            if sp.Float(
                row["relative_excess_percent"]
            )
            < sp.Rational(1, 10000)
        ),
    }

    primal_dual_identity = sp.cancel(
        ratio
        -
        sum(
            certificate["rhs"][index]
            * certificate["dual"][index]
            for index in range(len(certificate["rhs"]))
        )
    )

    a52_gates = a52_results["gates"]
    a54_gates = a54_results["gates"]

    gates = {
        "A52_audit_passed": bool(all(a52_gates.values())),
        "A54_global_audit_passed": bool(all(a54_gates.values())),
        "all_active_primal_variables_positive": bool(
            all(item["ok"] for item in primal_signs)
        ),
        "all_inequality_dual_multipliers_positive": bool(
            all(item["ok"] for item in dual_signs)
        ),
        "all_nonbasic_reduced_costs_positive": bool(
            all(item["ok"] for item in reduced_cost_signs)
        ),
        "primal_dual_objectives_identical": bool(
            primal_dual_identity == 0
        ),
        "compactified_ratio_reproduced": bool(
            sp.cancel(
                ratio_at_zero
                -
                module.PHASES["P5"]["ratio"]
            )
            == 0
        ),
        "risk_slope_positive": bool(
            sp.N(risk_slope, 60) > 0
        ),
        "gamma_9_below_0_05_percent": bool(
            threshold_requirements[
                "relative_below_0_05_percent"
            ]
            == 9
        ),
        "gamma_12_below_0_01_percent": bool(
            threshold_requirements[
                "relative_below_0_01_percent"
            ]
            == 12
        ),
        "gamma_15_below_0_001_percent": bool(
            threshold_requirements[
                "relative_below_0_001_percent"
            ]
            == 15
        ),
        "gamma_18_below_0_0001_percent": bool(
            threshold_requirements[
                "relative_below_0_0001_percent"
            ]
            == 18
        ),
    }

    verdict = (
        "PASS_FINITE_CAP_IMPLEMENTABILITY_AND_EXPONENTIAL_CONVERGENCE"
        if all(gates.values())
        else "FAIL_A55_FINITE_CAP_AUDIT"
    )

    result = {
        "audit": "A55_FINITE_CAP_IMPLEMENTABILITY",
        "contract": {
            "support": list(range(6)),
            "mean": "5/2",
            "epsilon": "1/10000",
            "target_exponent": 1,
            "fixed_first_anchor": 2,
            "fixed_second_anchor": str(
                sp.N(
                    -sp.log(s_star, 2),
                    50,
                )
            ),
            "finite_cap_domain": "Gamma>=6",
            "r_domain": "[0,1/64]",
        },
        "exact_basis_certificate": {
            "s_isolation_interval": [
                str(s_lower),
                str(s_upper),
            ],
            "r_interval": [
                str(r_lower),
                str(r_upper),
            ],
            "active_primal_expression_count": len(
                active_primal_expressions
            ),
            "inequality_dual_expression_count": len(
                inequality_dual_expressions
            ),
            "reduced_cost_expression_count": len(
                reduced_cost_expressions
            ),
            "primal_sign_certificates": primal_signs,
            "dual_sign_certificates": dual_signs,
            "reduced_cost_sign_certificates": reduced_cost_signs,
            "ratio_formula": str(ratio),
        },
        "asymptotic": {
            "ratio_star": str(ratio_star),
            "ratio_star_decimal": str(
                sp.N(ratio_star, 50)
            ),
            "future_risk_star_decimal": str(
                sp.N(risk_star, 50)
            ),
            "ratio_linear_coefficient": str(
                ratio_slope
            ),
            "ratio_linear_coefficient_decimal": str(
                sp.N(ratio_slope, 50)
            ),
            "risk_linear_coefficient": str(
                risk_slope
            ),
            "risk_linear_coefficient_decimal": str(
                sp.N(risk_slope, 50)
            ),
            "law": (
                "R_fixed(Gamma)-R_star = "
                "kappa_Q*2^(-Gamma)+O(4^(-Gamma))"
            ),
        },
        "finite_cap_table": table,
        "threshold_requirements": threshold_requirements,
        "global_sandwich": {
            "lower": (
                "A54 universal floor "
                "R_star <= R_opt(Gamma)"
            ),
            "upper": (
                "R_opt(Gamma) <= "
                "R_fixed_beta_star(Gamma)"
            ),
            "consequence": (
                "0 <= cap penalty <= exact fixed-design excess"
            ),
        },
        "formal_results": [
            (
                "the compactified active basis remains exactly "
                "optimal for fixed beta-star and every Gamma>=6"
            ),
            (
                "the fully reoptimized finite-cap risk is "
                "rigorously sandwiched"
            ),
            (
                "the implementation penalty decays exponentially "
                "as 2^(-Gamma)"
            ),
            (
                "finite accuracy thresholds are certified"
            ),
            (
                "a literal infinite instrument setting is not required"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The theorem is contract-relative and does not assign "
            "instrumental cost or physical meaning to Gamma. It "
            "controls the information loss from replacing the "
            "compactified endpoint by a finite exponent."
        ),
    }

    output_path = HERE / (
        "a55_finite_cap_implementability_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "risk_slope": result["asymptotic"][
            "risk_linear_coefficient_decimal"
        ],
        "thresholds": threshold_requirements,
        "failed_gates": [
            name
            for name, value in gates.items()
            if not value
        ],
        "verdict": verdict,
    }

    print(json.dumps(summary, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
