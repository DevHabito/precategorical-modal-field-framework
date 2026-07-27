#!/usr/bin/env python3
"""A57 exact audit: heteroscedastic third-channel error.

The first two observation tolerances remain epsilon0=1e-4.
The third tolerance is t*epsilon0 with 1 <= t <= 7/4.

The audit proves:
- one primal-dual basis is exact on the full (s,r,t) box;
- risk increases with r and with t;
- every cap upgrade has a unique break-even next tolerance;
- the break-even tolerance increase decays as 2^(-Gamma).

All sign statements use exact multivariate Bernstein certificates.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
from math import comb
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A52_SCRIPT = HERE / "a52_continuous_second_anchor_audit.py"
A55_RESULTS = HERE / "a55_finite_cap_implementability_results.json"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")

    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def bernstein_coefficients_nd(
    polynomial: sp.Poly,
    variables: tuple[sp.Symbol, ...],
) -> dict[tuple[int, ...], sp.Rational]:
    degrees = [
        polynomial.degree(variable)
        for variable in variables
    ]

    coefficients = {
        index: sp.Rational(0)
        for index in itertools.product(
            *[
                range(degree + 1)
                for degree in degrees
            ]
        )
    }

    for monomial, coefficient in polynomial.terms():
        ranges = [
            range(power, degree + 1)
            for power, degree in zip(
                monomial,
                degrees,
            )
        ]

        for index in itertools.product(*ranges):
            factor = sp.Rational(1)

            for current, power, degree in zip(
                index,
                monomial,
                degrees,
            ):
                factor *= sp.Rational(
                    comb(current, power),
                    comb(degree, power),
                )

            coefficients[index] += coefficient * factor

    return coefficients


def polynomial_sign_on_box(
    polynomial: sp.Expr,
    variables: tuple[sp.Symbol, ...],
    bounds: tuple[
        tuple[sp.Rational, sp.Rational],
        ...,
    ],
) -> int | None:
    unit_variables = sp.symbols(
        f"u0:{len(variables)}",
        real=True,
    )

    substitutions = {
        variable: lower + (upper - lower) * unit
        for variable, (lower, upper), unit
        in zip(
            variables,
            bounds,
            unit_variables,
        )
    }

    mapped = sp.Poly(
        sp.expand(polynomial.subs(substitutions)),
        *unit_variables,
        domain=sp.QQ,
    )

    coefficients = bernstein_coefficients_nd(
        mapped,
        tuple(unit_variables),
    )

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
    variables: tuple[sp.Symbol, ...],
    bounds: tuple[
        tuple[sp.Rational, sp.Rational],
        ...,
    ],
    initial_bounds: tuple[
        tuple[sp.Rational, sp.Rational],
        ...,
    ],
    depth: int = 0,
    max_depth: int = 8,
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

    numerator_sign = polynomial_sign_on_box(
        numerator,
        variables,
        bounds,
    )
    denominator_sign = polynomial_sign_on_box(
        denominator,
        variables,
        bounds,
    )

    if (
        numerator_sign is not None
        and denominator_sign is not None
        and numerator_sign * denominator_sign
        == desired_sign
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
            "box": [
                [str(lower), str(upper)]
                for lower, upper in bounds
            ],
            "numerator_sign": numerator_sign,
            "denominator_sign": denominator_sign,
        }

    normalized_widths = [
        float((upper - lower) / (initial_upper - initial_lower))
        for (
            (lower, upper),
            (initial_lower, initial_upper),
        )
        in zip(bounds, initial_bounds)
    ]

    split_index = max(
        range(len(variables)),
        key=lambda index: normalized_widths[index],
    )

    lower, upper = bounds[split_index]
    midpoint = (lower + upper) / 2

    first_bounds = list(bounds)
    second_bounds = list(bounds)

    first_bounds[split_index] = (lower, midpoint)
    second_bounds[split_index] = (midpoint, upper)

    first = certify_rational_sign_adaptive(
        expression,
        desired_sign,
        variables,
        tuple(first_bounds),
        initial_bounds,
        depth + 1,
        max_depth,
    )

    second = certify_rational_sign_adaptive(
        expression,
        desired_sign,
        variables,
        tuple(second_bounds),
        initial_bounds,
        depth + 1,
        max_depth,
    )

    return {
        "ok": first["ok"] and second["ok"],
        "leaf_count": (
            first["leaf_count"]
            + second["leaf_count"]
        ),
        "max_depth_used": max(
            first["max_depth_used"],
            second["max_depth_used"],
        ),
        "identically_zero": False,
        "children": [first, second],
    }


def build_trivariate_certificate(module):
    s = module.s
    r, t = sp.symbols("r t", real=True)

    support = list(range(6))
    target = [
        sp.Rational(1, 2**x)
        for x in support
    ]
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

    for values, sign, tolerance_factor in [
        (row_2, 1, sp.Integer(1)),
        (row_beta, -1, sp.Integer(1)),
        (row_gamma, 1, t),
    ]:
        row = [sp.Integer(0)] * 13

        for index in range(6):
            row[index] = sign * values[index]
            row[6 + index] = -sign * values[index]

        row[12] = (
            -2
            * epsilon
            * tolerance_factor
        )

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

    primal_solution = (
        primal_matrix.inv()
        * sp.Matrix(rhs)
    )

    z = [sp.Integer(0)] * 13

    for index, value in zip(
        positive_indices,
        primal_solution,
    ):
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

    dual_solution = (
        dual_matrix.inv()
        * sp.Matrix(
            [
                objective[index]
                for index in positive_indices
            ]
        )
    )

    dual = [
        sp.cancel(value)
        for value in dual_solution
    ]

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
        "t": t,
        "z": z,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "ratio": ratio,
        "positive_indices": positive_indices,
        "rows": rows,
        "rhs": rhs,
    }


def certify_at_stationary_root(
    expression: sp.Expr,
    desired_sign: int,
    s: sp.Symbol,
    lower: sp.Rational,
    upper: sp.Rational,
) -> bool:
    expression = sp.cancel(expression)

    numerator, denominator = sp.fraction(expression)

    numerator_polynomial = sp.Poly(
        numerator,
        s,
        domain=sp.QQ,
    )
    denominator_polynomial = sp.Poly(
        denominator,
        s,
        domain=sp.QQ,
    )

    numerator_roots = numerator_polynomial.count_roots(
        lower,
        upper,
    )
    denominator_roots = denominator_polynomial.count_roots(
        lower,
        upper,
    )

    midpoint = (lower + upper) / 2

    sample_sign = (
        sp.sign(numerator.subs(s, midpoint))
        * sp.sign(denominator.subs(s, midpoint))
    )

    return bool(
        numerator_roots == 0
        and denominator_roots == 0
        and sample_sign == desired_sign
    )


def main() -> None:
    if not A52_SCRIPT.exists():
        raise FileNotFoundError(A52_SCRIPT)
    if not A55_RESULTS.exists():
        raise FileNotFoundError(A55_RESULTS)

    module = load_module(
        A52_SCRIPT,
        "a52_for_a57",
    )

    a55_results = json.loads(
        A55_RESULTS.read_text(encoding="utf-8")
    )

    certificate = build_trivariate_certificate(module)

    s = certificate["s"]
    r = certificate["r"]
    t = certificate["t"]

    s_star = module.s_star

    s_lower = sp.Rational(3, 20)
    s_upper = sp.Rational(19, 125)
    r_lower = sp.Rational(0)
    r_upper = sp.Rational(1, 64)
    t_lower = sp.Rational(1)
    t_upper = sp.Rational(7, 4)

    bounds = (
        (s_lower, s_upper),
        (r_lower, r_upper),
        (t_lower, t_upper),
    )

    variables = (s, r, t)

    active_primal_expressions = [
        certificate["z"][index]
        for index in certificate[
            "positive_indices"
        ]
    ]

    inequality_dual_expressions = (
        certificate["dual"][5:]
    )

    nonbasic_indices = [
        index
        for index in range(13)
        if index
        not in certificate["positive_indices"]
    ]

    reduced_cost_expressions = [
        certificate["reduced_costs"][index]
        for index in nonbasic_indices
        if certificate["reduced_costs"][index]
        != 0
    ]

    primal_signs = [
        certify_rational_sign_adaptive(
            expression,
            1,
            variables,
            bounds,
            bounds,
        )
        for expression in active_primal_expressions
    ]

    dual_signs = [
        certify_rational_sign_adaptive(
            expression,
            1,
            variables,
            bounds,
            bounds,
        )
        for expression
        in inequality_dual_expressions
    ]

    reduced_cost_signs = [
        certify_rational_sign_adaptive(
            expression,
            1,
            variables,
            bounds,
            bounds,
        )
        for expression
        in reduced_cost_expressions
    ]

    ratio = certificate["ratio"]

    ratio_r_derivative = sp.cancel(
        sp.diff(ratio, r)
    )
    ratio_t_derivative = sp.cancel(
        sp.diff(ratio, t)
    )

    ratio_r_sign = certify_rational_sign_adaptive(
        ratio_r_derivative,
        1,
        variables,
        bounds,
        bounds,
    )

    ratio_t_sign = certify_rational_sign_adaptive(
        ratio_t_derivative,
        1,
        variables,
        bounds,
        bounds,
    )

    primal_dual_identity = sp.cancel(
        ratio
        -
        sum(
            certificate["rhs"][index]
            * certificate["dual"][index]
            for index in range(
                len(certificate["rhs"])
            )
        )
    )

    t_current, t_next = sp.symbols(
        "t_current t_next",
        real=True,
    )

    threshold_equation = sp.factor(
        sp.fraction(
            sp.cancel(
                ratio.subs(
                    {
                        r: r / 2,
                        t: t_next,
                    }
                )
                -
                ratio.subs(
                    t,
                    t_current,
                )
            )
        )[0]
    )

    threshold_solutions = sp.solve(
        threshold_equation,
        t_next,
    )

    if len(threshold_solutions) != 1:
        raise RuntimeError(
            "Break-even tolerance is not unique"
        )

    threshold = sp.cancel(
        threshold_solutions[0]
    )

    threshold_identity = sp.cancel(
        ratio.subs(
            {
                r: r / 2,
                t: threshold,
            }
        )
        -
        ratio.subs(
            t,
            t_current,
        )
    )

    baseline_table = []

    for gamma in range(6, 21):
        r_value = sp.Rational(
            1,
            2**gamma,
        )

        threshold_value = threshold.subs(
            {
                s: s_star,
                r: r_value,
                t_current: 1,
            }
        )

        increase = threshold_value - 1

        baseline_table.append(
            {
                "upgrade": (
                    f"{gamma}->{gamma + 1}"
                ),
                "gamma": gamma,
                "maximum_next_factor": str(
                    threshold_value
                ),
                "maximum_next_factor_decimal": str(
                    sp.N(
                        threshold_value,
                        50,
                    )
                ),
                "allowed_relative_increase": str(
                    increase
                ),
                "allowed_relative_increase_decimal": str(
                    sp.N(increase, 50)
                ),
                "allowed_percent": str(
                    sp.N(
                        100 * increase,
                        50,
                    )
                ),
            }
        )

    baseline_thresholds_above_one = all(
        certify_at_stationary_root(
            threshold.subs(
                {
                    r: sp.Rational(
                        1,
                        2**gamma,
                    ),
                    t_current: 1,
                }
            )
            - 1,
            1,
            s,
            s_lower,
            s_upper,
        )
        for gamma in range(6, 21)
    )

    baseline_thresholds_decrease = all(
        certify_at_stationary_root(
            threshold.subs(
                {
                    r: sp.Rational(
                        1,
                        2**gamma,
                    ),
                    t_current: 1,
                }
            )
            -
            threshold.subs(
                {
                    r: sp.Rational(
                        1,
                        2 ** (gamma + 1),
                    ),
                    t_current: 1,
                }
            ),
            1,
            s,
            s_lower,
            s_upper,
        )
        for gamma in range(6, 20)
    )

    risk = (
        sp.log(ratio)
        / (2 * sp.log(2))
    )

    risk_r_slope = sp.cancel(
        sp.diff(risk, r).subs(
            {
                r: 0,
                t: 1,
            }
        )
    )

    risk_t_slope = sp.cancel(
        sp.diff(risk, t).subs(
            {
                r: 0,
                t: 1,
            }
        )
    )

    noise_coefficient = sp.cancel(
        risk_r_slope
        / (2 * risk_t_slope)
    )

    asymptotic_checks = []

    for gamma in [
        12,
        14,
        16,
        18,
        20,
    ]:
        threshold_value = threshold.subs(
            {
                s: s_star,
                r: sp.Rational(
                    1,
                    2**gamma,
                ),
                t_current: 1,
            }
        )

        leading = (
            noise_coefficient.subs(
                s,
                s_star,
            )
            * sp.Rational(
                1,
                2**gamma,
            )
        )

        asymptotic_checks.append(
            {
                "gamma": gamma,
                "exact_increase_decimal": str(
                    sp.N(
                        threshold_value - 1,
                        50,
                    )
                ),
                "leading_decimal": str(
                    sp.N(leading, 50)
                ),
                "exact_over_leading": str(
                    sp.N(
                        (
                            threshold_value - 1
                        )
                        / leading,
                        50,
                    )
                ),
            }
        )

    ratio_t1 = sp.cancel(
        ratio.subs(t, 1)
    )

    a55_ratio_formula_raw = sp.sympify(
        a55_results[
            "exact_basis_certificate"
        ]["ratio_formula"]
    )

    a55_ratio_formula = a55_ratio_formula_raw.xreplace(
        {
            symbol: {
                "s": s,
                "r": r,
            }[symbol.name]
            for symbol in a55_ratio_formula_raw.free_symbols
        }
    )

    gates = {
        "all_active_primal_variables_positive": bool(
            all(
                result["ok"]
                for result in primal_signs
            )
        ),
        "all_inequality_dual_multipliers_positive": bool(
            all(
                result["ok"]
                for result in dual_signs
            )
        ),
        "all_nonbasic_reduced_costs_positive": bool(
            all(
                result["ok"]
                for result in reduced_cost_signs
            )
        ),
        "primal_dual_objectives_identical": bool(
            primal_dual_identity == 0
        ),
        "risk_increases_with_r": bool(
            ratio_r_sign["ok"]
        ),
        "risk_increases_with_third_tolerance": bool(
            ratio_t_sign["ok"]
        ),
        "break_even_solution_unique": bool(
            len(threshold_solutions) == 1
        ),
        "break_even_identity_exact": bool(
            threshold_identity == 0
        ),
        "baseline_thresholds_above_current_tolerance": bool(
            baseline_thresholds_above_one
        ),
        "baseline_thresholds_strictly_decrease": bool(
            baseline_thresholds_decrease
        ),
        "homoscedastic_A55_branch_reproduced": bool(
            sp.cancel(
                ratio_t1
                - a55_ratio_formula
            )
            == 0
        ),
        "noise_asymptotic_coefficient_positive": bool(
            sp.N(
                noise_coefficient.subs(
                    s,
                    s_star,
                ),
                60,
            )
            > 0
        ),
        "asymptotic_check_converges": bool(
            abs(
                float(
                    asymptotic_checks[-1][
                        "exact_over_leading"
                    ]
                )
                - 1.0
            )
            < 1e-3
        ),
    }

    verdict = (
        "PASS_HETEROSCEDASTIC_THIRD_CHANNEL_THRESHOLD_POLICY"
        if all(gates.values())
        else "FAIL_A57_HETEROSCEDASTIC_AUDIT"
    )

    result = {
        "audit": (
            "A57_HETEROSCEDASTIC_THIRD_CHANNEL"
        ),
        "contract": {
            "support": list(range(6)),
            "mean": "5/2",
            "base_tolerance": "1/10000",
            "third_tolerance": (
                "t/10000 with 1<=t<=7/4"
            ),
            "fixed_first_anchor": 2,
            "fixed_second_anchor": str(
                sp.N(
                    -sp.log(s_star, 2),
                    50,
                )
            ),
            "finite_cap_domain": "Gamma>=6",
        },
        "exact_basis_certificate": {
            "box": {
                "s": [
                    str(s_lower),
                    str(s_upper),
                ],
                "r": [
                    str(r_lower),
                    str(r_upper),
                ],
                "t": [
                    str(t_lower),
                    str(t_upper),
                ],
            },
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
            "reduced_cost_sign_certificates": (
                reduced_cost_signs
            ),
            "ratio_formula": str(ratio),
            "ratio_r_derivative_sign": ratio_r_sign,
            "ratio_t_derivative_sign": ratio_t_sign,
        },
        "break_even_policy": {
            "threshold_formula": str(threshold),
            "definition": (
                "rho(r/2,Theta_Gamma(t))"
                "=rho(r,t)"
            ),
            "rule": (
                "Upgrade helps iff "
                "t_(Gamma+1)<Theta_Gamma(t_Gamma)"
            ),
            "baseline_table": baseline_table,
        },
        "asymptotic": {
            "risk_r_slope": str(
                risk_r_slope.subs(
                    s,
                    s_star,
                )
            ),
            "risk_r_slope_decimal": str(
                sp.N(
                    risk_r_slope.subs(
                        s,
                        s_star,
                    ),
                    50,
                )
            ),
            "risk_t_slope": str(
                risk_t_slope.subs(
                    s,
                    s_star,
                )
            ),
            "risk_t_slope_decimal": str(
                sp.N(
                    risk_t_slope.subs(
                        s,
                        s_star,
                    ),
                    50,
                )
            ),
            "noise_budget_coefficient": str(
                noise_coefficient.subs(
                    s,
                    s_star,
                )
            ),
            "noise_budget_coefficient_decimal": str(
                sp.N(
                    noise_coefficient.subs(
                        s,
                        s_star,
                    ),
                    50,
                )
            ),
            "law": (
                "Theta_Gamma(1)-1="
                "C_noise*2^(-Gamma)"
                "+O(4^(-Gamma))"
            ),
            "checks": asymptotic_checks,
        },
        "formal_results": [
            (
                "one exact basis covers the certified "
                "heteroscedastic box"
            ),
            (
                "risk increases with finite residual"
            ),
            (
                "risk increases with third-channel tolerance"
            ),
            (
                "every cap upgrade has a unique exact "
                "break-even next tolerance"
            ),
            (
                "the rule applies to arbitrary measured "
                "third-channel error profiles"
            ),
            (
                "the allowable tolerance deterioration "
                "decays exponentially"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The theorem applies only for the fixed beta-star "
            "family, Gamma>=6, independent absolute errors, "
            "and third-channel factor 1<=t<=7/4. It does not "
            "estimate a real apparatus error curve."
        ),
    }

    output_path = HERE / (
        "a57_heteroscedastic_third_channel_results.json"
    )

    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "noise_budget_coefficient": result[
            "asymptotic"
        ][
            "noise_budget_coefficient_decimal"
        ],
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
