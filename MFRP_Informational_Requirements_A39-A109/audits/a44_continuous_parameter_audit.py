#!/usr/bin/env python3
"""A44 exact symbolic audit for continuous third-parameter design.

The audit proves:

1. exact-data direct ratio for D(gamma)={2,3,gamma};
2. primal and dual feasibility for every gamma>3;
3. strict monotonicity and the singular gamma->3+ infimum;
4. exact duplicated-parameter values;
5. exact noisy compactified-infinity optimum at epsilon=1/10000;
6. feasibility of the infinity extremizer for every finite gamma using
   exact Bernstein-sign certificates;
7. noncommuting limit endpoint values.

All algebraic gates use SymPy exact arithmetic.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


SUPPORT = list(range(6))
TARGET = [sp.Rational(1, 2**x) for x in SUPPORT]
MEAN = sp.Rational(5, 2)
EPSILON = sp.Rational(1, 10000)

r = sp.symbols("r", real=True)
tvar = sp.symbols("t", real=True)


def row_integer_exponent(k: int) -> list[sp.Rational]:
    return [sp.Rational(1, 2 ** (k * x)) for x in SUPPORT]


ROW2 = row_integer_exponent(2)
ROW3 = row_integer_exponent(3)
ROWR = [r**x for x in SUPPORT]


def build_base_rows() -> tuple[list[list[sp.Expr]], list[sp.Expr]]:
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
    row[12] = -MEAN
    rows.append(row)
    rhs.append(0)

    row = [sp.Integer(0)] * 13
    for index in range(6):
        row[6 + index] = index
    row[12] = -MEAN
    rows.append(row)
    rhs.append(0)

    row = [sp.Integer(0)] * 13
    for index in range(6):
        row[6 + index] = TARGET[index]
    rows.append(row)
    rhs.append(1)

    return rows, rhs


def exact_cc_certificate(
    p_support: list[int],
    q_support: list[int],
    observation_rows: list[list[sp.Expr]],
) -> dict[str, Any]:
    positive_indices = (
        p_support
        + [6 + index for index in q_support]
        + [12]
    )

    rows, rhs = build_base_rows()

    for values in observation_rows:
        row = [sp.Integer(0)] * 13
        for index in range(6):
            row[index] = values[index]
            row[6 + index] = -values[index]
        rows.append(row)
        rhs.append(0)

    primal_matrix = sp.Matrix(
        [
            [rows[row_index][column_index] for column_index in positive_indices]
            for row_index in range(len(rows))
        ]
    )
    primal_solution = primal_matrix.inv() * sp.Matrix(rhs)

    z = [sp.Integer(0)] * 13
    for index, value in zip(positive_indices, primal_solution):
        z[index] = sp.factor(value)

    objective = [sp.Integer(0)] * 13
    for index in range(6):
        objective[index] = TARGET[index]

    ratio = sp.factor(
        sum(objective[index] * z[index] for index in range(13))
    )

    dual_matrix = sp.Matrix(
        [
            [rows[row_index][column_index] for row_index in range(len(rows))]
            for column_index in positive_indices
        ]
    )
    dual_solution = dual_matrix.inv() * sp.Matrix(
        [objective[index] for index in positive_indices]
    )
    dual = [sp.factor(value) for value in dual_solution]

    reduced_costs = [
        sp.factor(
            sum(
                rows[row_index][column_index] * dual[row_index]
                for row_index in range(len(rows))
            )
            - objective[column_index]
        )
        for column_index in range(13)
    ]

    dual_objective = sp.factor(
        sum(rhs[index] * dual[index] for index in range(len(rows)))
    )

    scale = z[12]
    p = [sp.factor(z[index] / scale) for index in range(6)]
    q = [sp.factor(z[6 + index] / scale) for index in range(6)]

    return {
        "positive_indices": positive_indices,
        "rows": rows,
        "rhs": rhs,
        "z": z,
        "ratio": ratio,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "dual_objective": dual_objective,
        "p": p,
        "q": q,
    }


def noisy_cc_certificate(
    p_support: list[int],
    q_support: list[int],
    observation_rows: list[list[sp.Expr]],
    signs: list[int],
    epsilon: sp.Rational,
) -> dict[str, Any]:
    positive_indices = (
        p_support
        + [6 + index for index in q_support]
        + [12]
    )

    rows, rhs = build_base_rows()
    equality_count = len(rows)

    for values, sign in zip(observation_rows, signs):
        row = [sp.Integer(0)] * 13
        for index in range(6):
            row[index] = sign * values[index]
            row[6 + index] = -sign * values[index]
        row[12] = -2 * epsilon
        rows.append(row)
        rhs.append(0)

    primal_matrix = sp.Matrix(
        [
            [rows[row_index][column_index] for column_index in positive_indices]
            for row_index in range(len(rows))
        ]
    )
    primal_solution = primal_matrix.inv() * sp.Matrix(rhs)

    z = [sp.Integer(0)] * 13
    for index, value in zip(positive_indices, primal_solution):
        z[index] = sp.factor(value)

    objective = [sp.Integer(0)] * 13
    for index in range(6):
        objective[index] = TARGET[index]

    ratio = sp.factor(
        sum(objective[index] * z[index] for index in range(13))
    )

    dual_matrix = sp.Matrix(
        [
            [rows[row_index][column_index] for row_index in range(len(rows))]
            for column_index in positive_indices
        ]
    )
    dual_solution = dual_matrix.inv() * sp.Matrix(
        [objective[index] for index in positive_indices]
    )
    dual = [sp.factor(value) for value in dual_solution]

    reduced_costs = [
        sp.factor(
            sum(
                rows[row_index][column_index] * dual[row_index]
                for row_index in range(len(rows))
            )
            - objective[column_index]
        )
        for column_index in range(13)
    ]

    dual_objective = sp.factor(
        sum(rhs[index] * dual[index] for index in range(len(rows)))
    )

    scale = z[12]
    p = [sp.factor(z[index] / scale) for index in range(6)]
    q = [sp.factor(z[6 + index] / scale) for index in range(6)]

    return {
        "positive_indices": positive_indices,
        "rows": rows,
        "rhs": rhs,
        "equality_count": equality_count,
        "z": z,
        "ratio": ratio,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "dual_objective": dual_objective,
        "p": p,
        "q": q,
    }


def dot(values: list[sp.Expr], weights: list[sp.Expr]) -> sp.Expr:
    return sp.factor(
        sum(values[index] * weights[index] for index in range(6))
    )


def bernstein_coefficients_on_unit_interval(
    polynomial: sp.Expr,
    variable: sp.Symbol,
    degree: int,
) -> list[sp.Expr]:
    poly = sp.Poly(sp.expand(polynomial), variable)
    powers = [
        poly.coeff_monomial(variable**k)
        for k in range(degree + 1)
    ]

    coefficients = []
    for index in range(degree + 1):
        coefficient = sum(
            powers[k]
            * sp.Rational(
                sp.binomial(index, k),
                sp.binomial(degree, k),
            )
            for k in range(index + 1)
        )
        coefficients.append(sp.factor(coefficient))

    reconstruction = sum(
        coefficients[index]
        * sp.binomial(degree, index)
        * variable**index
        * (1 - variable) ** (degree - index)
        for index in range(degree + 1)
    )
    if sp.expand(reconstruction - polynomial) != 0:
        raise RuntimeError("Bernstein reconstruction failed")

    return coefficients


def main() -> None:
    exact_continuous = exact_cc_certificate(
        [1, 3, 5],
        [0, 1, 2, 4],
        [ROW2, ROW3, ROWR],
    )

    expected_ratio = sp.factor(
        (532 * r + 1063)
        / (2 * (275 * r + 527))
    )

    expected_p = [
        0,
        (76 * r + 217) / (4 * (76 * r + 121)),
        0,
        57 * (4 * r + 3) / (4 * (76 * r + 121)),
        0,
        24 / (76 * r + 121),
    ]
    expected_q = [
        3 * r / (4 * (76 * r + 121)),
        (17 * r + 107) / (2 * (76 * r + 121)),
        3 * (57 * r + 14) / (4 * (76 * r + 121)),
        0,
        3 * (8 * r + 19) / (76 * r + 121),
        0,
    ]

    exact_reduced_expected = [
        -3 * (2 * r - 1) / (4 * (275 * r + 527)),
        0,
        -3 * (2 * r - 1) / (8 * (275 * r + 527)),
        0,
        -81 * (2 * r - 1) / (32 * (275 * r + 527)),
        0,
        0,
        0,
        0,
        -21 * (2 * r - 1) / (16 * (275 * r + 527)),
        0,
        -249 * (2 * r - 1) / (64 * (275 * r + 527)),
        0,
    ]

    derivative_r = sp.factor(sp.diff(expected_ratio, r))
    exact_infimum_ratio = sp.factor(
        expected_ratio.subs(r, sp.Rational(1, 8))
    )
    exact_infinity_ratio = sp.factor(expected_ratio.subs(r, 0))

    duplicate_exact = exact_cc_certificate(
        [0, 1, 2, 5],
        [1, 3],
        [ROW2, ROW3],
    )

    row_infinity = [
        sp.Integer(1),
        sp.Integer(0),
        sp.Integer(0),
        sp.Integer(0),
        sp.Integer(0),
        sp.Integer(0),
    ]

    noisy_infinity = noisy_cc_certificate(
        [0, 1, 3, 5],
        [1, 2, 4],
        [ROW2, ROW3, row_infinity],
        [1, -1, 1],
        EPSILON,
    )

    expected_noisy_infinity_ratio = sp.Rational(
        26593405,
        26235854,
    )

    p_infinity = noisy_infinity["p"]
    q_infinity = noisy_infinity["q"]
    delta_weights = [
        sp.factor(p_infinity[index] - q_infinity[index])
        for index in range(6)
    ]

    delta_r = sp.factor(dot(ROWR, delta_weights))
    upper_residual = sp.factor(
        delta_r - sp.Rational(1, 5000)
    )
    lower_residual = sp.factor(
        delta_r + sp.Rational(1, 5000)
    )

    p1 = (
        29179880 * r**3
        - 57405373 * r**2
        + 27354112 * r
        + 835807
    )
    p2 = (
        14589940 * r**4
        - 30526429 * r**3
        + 17036924 * r**2
        - 871745 * r
        - 213444
    )

    p1_unit = sp.expand(p1.subs(r, tvar / 8))
    p2_unit = sp.expand(p2.subs(r, tvar / 8))
    p1_bernstein = bernstein_coefficients_on_unit_interval(
        p1_unit,
        tvar,
        3,
    )
    p2_bernstein = bernstein_coefficients_on_unit_interval(
        p2_unit,
        tvar,
        4,
    )

    duplicate_noisy = noisy_cc_certificate(
        [0, 1, 2, 5],
        [1, 3],
        [ROW2, ROW3],
        [1, -1],
        EPSILON,
    )

    exact_future_infimum = (
        sp.log(exact_infimum_ratio)
        / (2 * sp.log(2))
    )
    noisy_future_infinity = (
        sp.log(expected_noisy_infinity_ratio)
        / (2 * sp.log(2))
    )

    catalogue_exact_ratio = sp.Rational(8770, 8707)
    catalogue_noisy_ratio = sp.Rational(
        1828961429248,
        1804118444725,
    )

    exact_catalogue_risk = (
        sp.log(catalogue_exact_ratio)
        / (2 * sp.log(2))
    )
    noisy_catalogue_risk = (
        sp.log(catalogue_noisy_ratio)
        / (2 * sp.log(2))
    )

    exact_improvement_percent = sp.N(
        100
        * (
            1
            - exact_future_infimum / exact_catalogue_risk
        ),
        40,
    )
    noisy_improvement_percent = sp.N(
        100
        * (
            1
            - noisy_future_infinity / noisy_catalogue_risk
        ),
        40,
    )

    continuous_exact_gates = {
        "closed_ratio_formula_exact": bool(
            sp.factor(
                exact_continuous["ratio"]
                - expected_ratio
            )
            == 0
        ),
        "closed_primal_p_formula_exact": bool(
            all(
                sp.factor(
                    exact_continuous["p"][index]
                    - expected_p[index]
                )
                == 0
                for index in range(6)
            )
        ),
        "closed_primal_q_formula_exact": bool(
            all(
                sp.factor(
                    exact_continuous["q"][index]
                    - expected_q[index]
                )
                == 0
                for index in range(6)
            )
        ),
        "primal_normalization_symbolic": bool(
            sp.factor(sum(exact_continuous["p"])) == 1
            and sp.factor(sum(exact_continuous["q"])) == 1
        ),
        "primal_mean_symbolic": bool(
            sp.factor(
                sum(
                    index * exact_continuous["p"][index]
                    for index in range(6)
                )
            )
            == MEAN
            and sp.factor(
                sum(
                    index * exact_continuous["q"][index]
                    for index in range(6)
                )
            )
            == MEAN
        ),
        "three_exact_observations_match_symbolically": bool(
            all(
                sp.factor(
                    dot(values, exact_continuous["p"])
                    - dot(values, exact_continuous["q"])
                )
                == 0
                for values in [ROW2, ROW3, ROWR]
            )
        ),
        "dual_objective_matches_primal": bool(
            sp.factor(
                exact_continuous["dual_objective"]
                - expected_ratio
            )
            == 0
        ),
        "dual_reduced_cost_formulas_exact": bool(
            all(
                sp.factor(
                    exact_continuous["reduced_costs"][index]
                    - exact_reduced_expected[index]
                )
                == 0
                for index in range(13)
            )
        ),
        "derivative_formula_exact_and_negative": bool(
            derivative_r
            == -sp.Rational(11961, 2)
            / (275 * r + 527) ** 2
        ),
        "singular_infimum_ratio_exact": bool(
            exact_infimum_ratio == sp.Rational(502, 499)
        ),
        "large_gamma_limit_ratio_exact": bool(
            exact_infinity_ratio == sp.Rational(1063, 1054)
        ),
    }

    duplicate_gates = {
        "duplicate_exact_ratio": bool(
            duplicate_exact["ratio"]
            == sp.Rational(3665, 3458)
        ),
        "duplicate_exact_primal_dual_equal": bool(
            duplicate_exact["ratio"]
            == duplicate_exact["dual_objective"]
        ),
        "duplicate_exact_reduced_costs_nonnegative": bool(
            all(
                value >= 0
                for value in duplicate_exact["reduced_costs"]
            )
        ),
        "duplicate_noisy_ratio": bool(
            duplicate_noisy["ratio"]
            == sp.Rational(
                337423987,
                317703750,
            )
        ),
        "duplicate_noisy_primal_dual_equal": bool(
            duplicate_noisy["ratio"]
            == duplicate_noisy["dual_objective"]
        ),
        "duplicate_noisy_inequality_duals_nonnegative": bool(
            all(
                value >= 0
                for value
                in duplicate_noisy["dual"][
                    duplicate_noisy["equality_count"]:
                ]
            )
        ),
        "duplicate_noisy_reduced_costs_nonnegative": bool(
            all(
                value >= 0
                for value in duplicate_noisy["reduced_costs"]
            )
        ),
    }

    noisy_infinity_gates = {
        "noisy_infinity_ratio_exact": bool(
            noisy_infinity["ratio"]
            == expected_noisy_infinity_ratio
        ),
        "noisy_infinity_primal_dual_equal": bool(
            noisy_infinity["ratio"]
            == noisy_infinity["dual_objective"]
        ),
        "noisy_infinity_weights_nonnegative": bool(
            all(value >= 0 for value in p_infinity + q_infinity)
        ),
        "noisy_infinity_normalization": bool(
            sum(p_infinity) == 1
            and sum(q_infinity) == 1
        ),
        "noisy_infinity_mean": bool(
            dot([sp.Integer(x) for x in SUPPORT], p_infinity)
            == MEAN
            and dot(
                [sp.Integer(x) for x in SUPPORT],
                q_infinity,
            )
            == MEAN
        ),
        "noisy_infinity_anchor_differences_exact": bool(
            dot(ROW2, delta_weights)
            == sp.Rational(1, 5000)
            and dot(ROW3, delta_weights)
            == -sp.Rational(1, 5000)
            and delta_weights[0] == sp.Rational(1, 5000)
        ),
        "noisy_infinity_inequality_duals_nonnegative": bool(
            all(
                value >= 0
                for value
                in noisy_infinity["dual"][
                    noisy_infinity["equality_count"]:
                ]
            )
        ),
        "noisy_infinity_reduced_costs_nonnegative": bool(
            all(
                value >= 0
                for value in noisy_infinity["reduced_costs"]
            )
        ),
        "finite_gamma_delta_formula_exact": bool(
            delta_r
            == (
                (r - 1) ** 2
                * (
                    116719520 * r**3
                    - 25362332 * r**2
                    - 622363 * r
                    + 106722
                )
                / 533610000
            )
        ),
        "upper_residual_factorization_exact": bool(
            upper_residual
            == (
                r
                * (4 * r - 1)
                * p1
                / 533610000
            )
        ),
        "lower_residual_factorization_exact": bool(
            lower_residual
            == (
                (8 * r - 1)
                * p2
                / 533610000
            )
        ),
        "P1_bernstein_all_positive": bool(
            all(value > 0 for value in p1_bernstein)
        ),
        "P2_bernstein_all_negative": bool(
            all(value < 0 for value in p2_bernstein)
        ),
    }

    all_gates = {
        **{
            f"exact::{key}": value
            for key, value in continuous_exact_gates.items()
        },
        **{
            f"duplicate::{key}": value
            for key, value in duplicate_gates.items()
        },
        **{
            f"noisy_infinity::{key}": value
            for key, value in noisy_infinity_gates.items()
        },
    }

    verdict = (
        "PASS_CONTINUOUS_PARAMETER_SINGULAR_LIMIT_AND_COMPACTIFIED_NOISY_OPTIMUM"
        if all(all_gates.values())
        else "FAIL_A44_CONTINUOUS_PARAMETER_AUDIT"
    )

    result = {
        "audit": "A44_PROVISIONAL_CONTINUOUS_THIRD_PARAMETER",
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "design": "{2*log(2), 3*log(2), gamma*log(2)}",
            "gamma_domain_exact": "gamma > 3",
            "gamma_domain_noisy_compactified": "[3, infinity]",
            "target": "direct future Q at 2*log(2), contraction a=1/2",
            "noise_benchmark": str(EPSILON),
        },
        "exact_continuous_result": {
            "r_definition": "r = 2^(-gamma)",
            "ratio_formula": str(expected_ratio),
            "ratio_derivative_in_r": str(derivative_r),
            "infimum_ratio": str(exact_infimum_ratio),
            "infimum_future_risk_decimal": (
                f"{float(exact_future_infimum):.18g}"
            ),
            "duplicate_gamma_3_ratio": str(
                duplicate_exact["ratio"]
            ),
            "duplicate_gamma_3_future_risk_decimal": (
                f"{0.5 * math.log2(float(duplicate_exact['ratio'])):.18g}"
            ),
            "limiting_p_gamma_3_plus": [
                str(
                    sp.factor(
                        value.subs(r, sp.Rational(1, 8))
                    )
                )
                for value in exact_continuous["p"]
            ],
            "limiting_q_gamma_3_plus": [
                str(
                    sp.factor(
                        value.subs(r, sp.Rational(1, 8))
                    )
                )
                for value in exact_continuous["q"]
            ],
        },
        "noisy_compactified_result": {
            "epsilon": str(EPSILON),
            "infinity_ratio": str(
                expected_noisy_infinity_ratio
            ),
            "infinity_future_risk_decimal": (
                f"{float(noisy_future_infinity):.18g}"
            ),
            "p_infinity": [str(value) for value in p_infinity],
            "q_infinity": [str(value) for value in q_infinity],
            "delta_gamma_formula": str(delta_r),
            "P1_bernstein_coefficients": [
                str(value) for value in p1_bernstein
            ],
            "P2_bernstein_coefficients": [
                str(value) for value in p2_bernstein
            ],
            "duplicate_gamma_3_ratio": str(
                duplicate_noisy["ratio"]
            ),
            "duplicate_gamma_3_future_risk_decimal": (
                f"{0.5 * math.log2(float(duplicate_noisy['ratio'])):.18g}"
            ),
        },
        "comparison_with_A43": {
            "exact_catalogue_gamma": 4,
            "exact_catalogue_ratio": str(catalogue_exact_ratio),
            "exact_continuous_infimum_improvement_percent": (
                str(exact_improvement_percent)
            ),
            "noisy_catalogue_gamma": 6,
            "noisy_catalogue_ratio": str(catalogue_noisy_ratio),
            "noisy_compactified_improvement_percent": (
                str(noisy_improvement_percent)
            ),
        },
        "noncommuting_limits": {
            "noise_then_coalescence": str(
                duplicate_exact["ratio"]
            ),
            "coalescence_then_noise": str(
                exact_infimum_ratio
            ),
            "different": bool(
                duplicate_exact["ratio"]
                != exact_infimum_ratio
            ),
        },
        "formal_results_proved_in_note": [
            "exact direct ratio is globally certified for every gamma>3",
            "exact risk is strictly increasing in gamma",
            "exact continuous infimum is singular and unattained",
            "duplicated exact parameter has a discontinuously larger risk",
            "compactified infinity is a global noisy minimizer",
            "the infinity extremizer is feasible for every finite gamma",
            "finite noisy risks converge to the compactified boundary value",
            "zero-noise and coalescing-parameter limits do not commute",
        ],
        "gates": all_gates,
        "verdict": verdict,
        "boundary": (
            "The results are exact only under the declared finite support, "
            "mean, anchors, target, contraction, and common absolute-error "
            "contract. Gamma=infinity denotes the limiting functional p->p_0, "
            "not a finite physical measurement. No empirical noise model or "
            "physical parameter interpretation is claimed."
        ),
    }

    output_path = Path(__file__).with_name(
        "a44_continuous_parameter_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2))

    if not all(all_gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
