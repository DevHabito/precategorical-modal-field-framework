#!/usr/bin/env python3
"""A58 exact audit: independent three-channel error vector.

The compactified design is fixed at {2,beta*,infinity}.
All three absolute-error factors vary independently in [1,11/10].

The audit proves:
- one exact primal-dual basis covers the full four-dimensional box;
- risk increases in every error coordinate;
- each lower channel is uniformly more than four times as sensitive as the
  compactified channel;
- exact baseline gradients and robust corner bounds.
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
A54_RESULTS = HERE / "a54_universal_continuum_witness_results.json"


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


def certify_rational_sign(
    expression: sp.Expr,
    desired_sign: int,
    variables: tuple[sp.Symbol, ...],
    bounds: tuple[
        tuple[sp.Rational, sp.Rational],
        ...,
    ],
) -> dict[str, Any]:
    expression = sp.cancel(expression)

    if expression == 0:
        return {
            "ok": desired_sign == 0,
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

    return {
        "ok": bool(
            numerator_sign is not None
            and denominator_sign is not None
            and numerator_sign
            * denominator_sign
            == desired_sign
        ),
        "identically_zero": False,
        "numerator_sign": numerator_sign,
        "denominator_sign": denominator_sign,
    }


def build_certificate(module):
    s = module.s
    u2, ub, ui = sp.symbols(
        "u2 ub ui",
        real=True,
    )

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
    row_infinity = [
        sp.Integer(1),
        sp.Integer(0),
        sp.Integer(0),
        sp.Integer(0),
        sp.Integer(0),
        sp.Integer(0),
    ]

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

    for values, sign, factor in [
        (row_2, 1, u2),
        (row_beta, -1, ub),
        (row_infinity, 1, ui),
    ]:
        row = [sp.Integer(0)] * 13

        for index in range(6):
            row[index] = sign * values[index]
            row[6 + index] = -sign * values[index]

        row[12] = -2 * epsilon * factor
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
        "u2": u2,
        "ub": ub,
        "ui": ui,
        "z": z,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "ratio": ratio,
        "rows": rows,
        "rhs": rhs,
        "positive_indices": positive_indices,
    }


def main() -> None:
    if not A52_SCRIPT.exists():
        raise FileNotFoundError(A52_SCRIPT)
    if not A54_RESULTS.exists():
        raise FileNotFoundError(A54_RESULTS)

    module = load_module(
        A52_SCRIPT,
        "a52_for_a58",
    )

    a54_results = json.loads(
        A54_RESULTS.read_text(encoding="utf-8")
    )

    certificate = build_certificate(module)

    s = certificate["s"]
    u2 = certificate["u2"]
    ub = certificate["ub"]
    ui = certificate["ui"]
    ratio = certificate["ratio"]
    s_star = module.s_star

    s_lower = sp.Rational(3, 20)
    s_upper = sp.Rational(19, 125)
    error_lower = sp.Rational(1)
    error_upper = sp.Rational(11, 10)

    variables = (s, u2, ub, ui)
    bounds = (
        (s_lower, s_upper),
        (error_lower, error_upper),
        (error_lower, error_upper),
        (error_lower, error_upper),
    )

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
        certify_rational_sign(
            expression,
            1,
            variables,
            bounds,
        )
        for expression in active_primal_expressions
    ]

    dual_signs = [
        certify_rational_sign(
            expression,
            1,
            variables,
            bounds,
        )
        for expression
        in inequality_dual_expressions
    ]

    reduced_cost_signs = [
        certify_rational_sign(
            expression,
            1,
            variables,
            bounds,
        )
        for expression
        in reduced_cost_expressions
    ]

    derivative_u2 = sp.cancel(
        sp.diff(ratio, u2)
    )
    derivative_ub = sp.cancel(
        sp.diff(ratio, ub)
    )
    derivative_ui = sp.cancel(
        sp.diff(ratio, ui)
    )

    derivative_signs = {
        "u2": certify_rational_sign(
            derivative_u2,
            1,
            variables,
            bounds,
        ),
        "ub": certify_rational_sign(
            derivative_ub,
            1,
            variables,
            bounds,
        ),
        "ui": certify_rational_sign(
            derivative_ui,
            1,
            variables,
            bounds,
        ),
    }

    fourfold_signs = {
        "u2_vs_ui": certify_rational_sign(
            derivative_u2
            - 4 * derivative_ui,
            1,
            variables,
            bounds,
        ),
        "ub_vs_ui": certify_rational_sign(
            derivative_ub
            - 4 * derivative_ui,
            1,
            variables,
            bounds,
        ),
    }

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

    risk = (
        sp.log(ratio)
        / (2 * sp.log(2))
    )

    baseline_substitution = {
        s: s_star,
        u2: 1,
        ub: 1,
        ui: 1,
    }

    worst_substitution = {
        s: s_star,
        u2: sp.Rational(11, 10),
        ub: sp.Rational(11, 10),
        ui: sp.Rational(11, 10),
    }

    baseline_ratio = sp.cancel(
        ratio.subs(baseline_substitution)
    )
    baseline_risk = risk.subs(
        baseline_substitution
    )

    worst_ratio = sp.cancel(
        ratio.subs(worst_substitution)
    )
    worst_risk = risk.subs(
        worst_substitution
    )

    risk_slopes = {
        "u2": sp.diff(risk, u2).subs(
            baseline_substitution
        ),
        "ub": sp.diff(risk, ub).subs(
            baseline_substitution
        ),
        "ui": sp.diff(risk, ui).subs(
            baseline_substitution
        ),
    }

    exchange_rates = {
        "u2_over_ui": sp.cancel(
            risk_slopes["u2"]
            / risk_slopes["ui"]
        ),
        "ub_over_ui": sp.cancel(
            risk_slopes["ub"]
            / risk_slopes["ui"]
        ),
    }

    individual_impacts = {}

    for name, variable in [
        ("u2", u2),
        ("ub", ub),
        ("ui", ui),
    ]:
        substitution = dict(
            baseline_substitution
        )
        substitution[variable] = sp.Rational(
            11,
            10,
        )

        current_risk = risk.subs(substitution)
        increase = current_risk - baseline_risk

        individual_impacts[name] = {
            "risk_decimal": str(
                sp.N(current_risk, 50)
            ),
            "absolute_increase_decimal": str(
                sp.N(increase, 50)
            ),
            "relative_increase_percent": str(
                sp.N(
                    100
                    * increase
                    / baseline_risk,
                    50,
                )
            ),
        }

    a54_risk = sp.Float(
        a54_results[
            "global_optimum"
        ]["future_risk"],
        80,
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
                for result
                in reduced_cost_signs
            )
        ),
        "primal_dual_objectives_identical": bool(
            primal_dual_identity == 0
        ),
        "risk_increases_with_each_error_factor": bool(
            all(
                result["ok"]
                for result
                in derivative_signs.values()
            )
        ),
        "lower_channels_more_than_fourfold_sensitive": bool(
            all(
                result["ok"]
                for result
                in fourfold_signs.values()
            )
        ),
        "baseline_reproduces_A54_risk": bool(
            abs(
                float(
                    sp.N(
                        baseline_risk,
                        50,
                    )
                )
                - float(a54_risk)
            )
            < 1e-14
        ),
        "worst_corner_above_baseline": bool(
            sp.N(
                worst_risk
                - baseline_risk,
                60,
            )
            > 0
        ),
        "exchange_rates_above_four": bool(
            sp.N(
                exchange_rates[
                    "u2_over_ui"
                ],
                60,
            )
            > 4
            and sp.N(
                exchange_rates[
                    "ub_over_ui"
                ],
                60,
            )
            > 4
        ),
    }

    verdict = (
        "PASS_INDEPENDENT_THREE_CHANNEL_ERROR_VECTOR_AND_CALIBRATION_PRIORITY"
        if all(gates.values())
        else "FAIL_A58_INDEPENDENT_ERROR_VECTOR_AUDIT"
    )

    result = {
        "audit": (
            "A58_INDEPENDENT_THREE_CHANNEL_ERROR_VECTOR"
        ),
        "contract": {
            "support": list(range(6)),
            "mean": "5/2",
            "base_tolerance": "1/10000",
            "design": (
                "{2,beta-star,infinity}*log(2)"
            ),
            "independent_error_factors": (
                "1<=u2,ub,ui<=11/10"
            ),
        },
        "exact_basis_certificate": {
            "box": {
                "s": [
                    str(s_lower),
                    str(s_upper),
                ],
                "u2": [
                    str(error_lower),
                    str(error_upper),
                ],
                "ub": [
                    str(error_lower),
                    str(error_upper),
                ],
                "ui": [
                    str(error_lower),
                    str(error_upper),
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
            "derivative_sign_certificates": derivative_signs,
            "fourfold_sensitivity_certificates": (
                fourfold_signs
            ),
            "ratio_formula": str(ratio),
        },
        "baseline": {
            "beta_star": str(
                sp.N(
                    -sp.log(s_star, 2),
                    50,
                )
            ),
            "ratio_decimal": str(
                sp.N(baseline_ratio, 50)
            ),
            "risk_decimal": str(
                sp.N(baseline_risk, 50)
            ),
            "risk_slopes": {
                name: {
                    "expression": str(value),
                    "decimal": str(
                        sp.N(value, 50)
                    ),
                }
                for name, value
                in risk_slopes.items()
            },
            "exchange_rates": {
                name: {
                    "expression": str(value),
                    "decimal": str(
                        sp.N(value, 50)
                    ),
                }
                for name, value
                in exchange_rates.items()
            },
        },
        "robust_box_bounds": {
            "minimum_risk_decimal": str(
                sp.N(baseline_risk, 50)
            ),
            "maximum_risk_decimal": str(
                sp.N(worst_risk, 50)
            ),
            "absolute_increase_decimal": str(
                sp.N(
                    worst_risk
                    - baseline_risk,
                    50,
                )
            ),
            "relative_increase_percent": str(
                sp.N(
                    100
                    * (
                        worst_risk
                        - baseline_risk
                    )
                    / baseline_risk,
                    50,
                )
            ),
        },
        "individual_ten_percent_impacts": (
            individual_impacts
        ),
        "formal_results": [
            (
                "one exact basis covers the full independent "
                "three-error box"
            ),
            (
                "risk increases monotonically in every "
                "error coordinate"
            ),
            (
                "both lower channels are uniformly more than "
                "four times as sensitive as the extreme channel"
            ),
            (
                "exact baseline gradient and local exchange "
                "rates are supplied"
            ),
            (
                "exact robust minimum and maximum corner "
                "risks are supplied"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The theorem applies to the fixed compactified "
            "beta-star design and independent box errors with "
            "factors between 1 and 1.1. It does not include "
            "correlation, factors below one, or anchor "
            "reoptimization."
        ),
    }

    output_path = HERE / (
        "a58_independent_three_channel_error_results.json"
    )

    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "risk_slopes": {
            name: values["decimal"]
            for name, values
            in result["baseline"][
                "risk_slopes"
            ].items()
        },
        "relative_worst_corner_increase_percent": (
            result["robust_box_bounds"][
                "relative_increase_percent"
            ]
        ),
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
