#!/usr/bin/env python3
"""A46 exact audit: noise-separation boundary layer and local bifurcations.

The script certifies local/asymptotic structure in the (epsilon, gamma) plane.
It deliberately does not claim a complete globally optimal two-dimensional
phase diagram.

Certified components:
- duplicated-anchor redundancy boundary and linear scaling;
- regular finite stationary branch and sqrt(epsilon) scaling;
- algebraic branch-annihilation threshold epsilon_a;
- boundary-active stationary branch;
- exact compactified threshold epsilon_b;
- symbolic derivative/sign identities and root isolation.
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

r, epsilon = sp.symbols("r epsilon", real=True)
h, u, t = sp.symbols("h u t", real=True)


def transform_row(exponent: int) -> list[sp.Rational]:
    return [
        sp.Rational(1, 2 ** (exponent * x))
        for x in SUPPORT
    ]


ROW2 = transform_row(2)
ROW3 = transform_row(3)
ROWR = [r**x for x in SUPPORT]


def build_base_rows() -> tuple[list[list[sp.Expr]], list[sp.Expr]]:
    rows: list[list[sp.Expr]] = []
    rhs: list[sp.Expr] = []

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[index] = 1
    current[12] = -1
    rows.append(current)
    rhs.append(0)

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[6 + index] = 1
    current[12] = -1
    rows.append(current)
    rhs.append(0)

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[index] = index
    current[12] = -MEAN
    rows.append(current)
    rhs.append(0)

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[6 + index] = index
    current[12] = -MEAN
    rows.append(current)
    rhs.append(0)

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[6 + index] = TARGET[index]
    rows.append(current)
    rhs.append(1)

    return rows, rhs


def symbolic_noisy_certificate(
    p_support: list[int],
    q_support: list[int],
    observations: list[list[sp.Expr]],
    signs: list[int],
) -> dict[str, Any]:
    positive_indices = (
        p_support
        + [6 + index for index in q_support]
        + [12]
    )

    rows, rhs = build_base_rows()
    equality_count = len(rows)

    for values, sign in zip(observations, signs):
        current = [sp.Integer(0)] * 13
        for index in range(6):
            current[index] = sign * values[index]
            current[6 + index] = -sign * values[index]
        current[12] = -2 * epsilon
        rows.append(current)
        rhs.append(0)

    matrix = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(len(rows))
        ]
    )

    solution = matrix.inv() * sp.Matrix(rhs)

    z = [sp.Integer(0)] * 13
    for index, value in zip(positive_indices, solution):
        z[index] = sp.factor(value)

    scale = z[12]
    p = [sp.factor(z[index] / scale) for index in range(6)]
    q = [
        sp.factor(z[6 + index] / scale)
        for index in range(6)
    ]

    objective = [sp.Integer(0)] * 13
    for index in range(6):
        objective[index] = TARGET[index]

    ratio = sp.factor(
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
    dual = [sp.factor(value) for value in dual_solution]

    reduced_costs = [
        sp.factor(
            sum(
                rows[row_index][column_index]
                * dual[row_index]
                for row_index in range(len(rows))
            )
            - objective[column_index]
        )
        for column_index in range(13)
    ]

    dual_objective = sp.factor(
        sum(
            rhs[index] * dual[index]
            for index in range(len(rows))
        )
    )

    return {
        "p": p,
        "q": q,
        "z": z,
        "scale": scale,
        "ratio": ratio,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "dual_objective": dual_objective,
        "equality_count": equality_count,
    }


def symbolic_duplicate_certificate() -> dict[str, Any]:
    positive_indices = [0, 1, 2, 5, 7, 9, 12]
    rows, rhs = build_base_rows()
    equality_count = len(rows)

    for values, sign in zip([ROW2, ROW3], [1, -1]):
        current = [sp.Integer(0)] * 13
        for index in range(6):
            current[index] = sign * values[index]
            current[6 + index] = -sign * values[index]
        current[12] = -2 * epsilon
        rows.append(current)
        rhs.append(0)

    matrix = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(len(rows))
        ]
    )

    solution = matrix.inv() * sp.Matrix(rhs)

    z = [sp.Integer(0)] * 13
    for index, value in zip(positive_indices, solution):
        z[index] = sp.factor(value)

    scale = z[12]
    p = [sp.factor(z[index] / scale) for index in range(6)]
    q = [
        sp.factor(z[6 + index] / scale)
        for index in range(6)
    ]

    objective = [sp.Integer(0)] * 13
    for index in range(6):
        objective[index] = TARGET[index]

    ratio = sp.factor(
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
    dual = [sp.factor(value) for value in dual_solution]

    reduced_costs = [
        sp.factor(
            sum(
                rows[row_index][column_index]
                * dual[row_index]
                for row_index in range(len(rows))
            )
            - objective[column_index]
        )
        for column_index in range(13)
    ]

    dual_objective = sp.factor(
        sum(
            rhs[index] * dual[index]
            for index in range(len(rows))
        )
    )

    return {
        "p": p,
        "q": q,
        "z": z,
        "scale": scale,
        "ratio": ratio,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "dual_objective": dual_objective,
        "equality_count": equality_count,
    }


def dot(values: list[sp.Expr], weights: list[sp.Expr]) -> sp.Expr:
    return sp.factor(
        sum(
            values[index] * weights[index]
            for index in range(6)
        )
    )


def bernstein_coefficients(
    polynomial: sp.Expr,
    variable: sp.Symbol,
    degree: int,
) -> list[sp.Expr]:
    poly = sp.Poly(sp.expand(polynomial), variable)
    powers = [
        poly.coeff_monomial(variable**index)
        for index in range(degree + 1)
    ]

    coefficients = []
    for index in range(degree + 1):
        value = sum(
            powers[k]
            * sp.Rational(
                sp.binomial(index, k),
                sp.binomial(degree, k),
            )
            for k in range(index + 1)
        )
        coefficients.append(sp.factor(value))

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


def count_roots(
    polynomial: sp.Expr,
    lower: sp.Rational,
    upper: sp.Rational,
) -> int:
    return int(
        sp.Poly(polynomial, r).count_roots(lower, upper)
    )


def main() -> None:
    duplicate = symbolic_duplicate_certificate()
    phase5 = symbolic_noisy_certificate(
        [1, 3, 5],
        [0, 1, 2, 4],
        [ROW2, ROW3, ROWR],
        [1, -1, 1],
    )
    phase4 = symbolic_noisy_certificate(
        [0, 1, 3, 5],
        [1, 2, 4],
        [ROW2, ROW3, ROWR],
        [1, -1, 1],
    )

    duplicate_delta = sp.factor(
        dot(ROWR, duplicate["p"])
        - dot(ROWR, duplicate["q"])
    )

    boundary_factor = sp.factor(
        (
            duplicate_delta - 2 * epsilon
        )
        * 1742832
        / (4 * r - 1)
    )

    T0 = sp.factor(
        -boundary_factor.subs(epsilon, 0)
        / sp.diff(boundary_factor, epsilon)
    )

    T0_derivative_anchor = sp.factor(
        sp.diff(T0, r).subs(r, sp.Rational(1, 8))
    )

    F5_full = sp.factor(
        sp.fraction(
            sp.cancel(
                sp.diff(phase5["ratio"], r)
            )
        )[0]
        /
        (
            -(2125824 * epsilon - 21707)
            * (r - 1)
        )
    )

    F4_full = sp.factor(
        sp.fraction(
            sp.cancel(
                sp.diff(phase4["ratio"], r)
            )
        )[0]
        /
        (
            -9
            * (22388480 * epsilon - 195069)
            * (r - 1)
        )
    )

    B_common = sp.factor(F5_full.subs(epsilon, 0))
    C5 = sp.factor(sp.diff(F5_full, epsilon))
    C4 = sp.factor(sp.diff(F4_full, epsilon))

    E5 = sp.factor(-B_common / C5)
    E4 = sp.factor(-B_common / C4)

    transition_numerator = sp.factor(
        sp.fraction(phase4["p"][0])[0]
    )

    T4 = sp.factor(
        -transition_numerator.subs(epsilon, 0)
        / sp.diff(transition_numerator, epsilon)
    )

    J = (
        123904 * r**5
        - 359168 * r**4
        + 338000 * r**3
        - 96856 * r**2
        - 8379 * r
        + 441
    )

    domain_roots_J = [
        root
        for root in sp.Poly(J, r).real_roots()
        if bool(root > 0)
        and bool(root < sp.Rational(1, 8))
    ]

    if len(domain_roots_J) != 1:
        raise RuntimeError("Expected one bifurcation root")

    r_a = domain_roots_J[0]
    epsilon_a = sp.factor(T4.subs(r, r_a))
    epsilon_b = sp.factor(E4.subs(r, 0))

    H = (
        174080 * r**4
        - 658688 * r**3
        + 908064 * r**2
        - 592636 * r
        + 147571
    )

    H_unit = sp.expand(H.subs(r, t / 8))
    H_bernstein = bernstein_coefficients(H_unit, t, 4)

    E5_derivative = sp.factor(sp.diff(E5, r))
    E4_derivative = sp.factor(sp.diff(E4, r))

    # Denominator root certificates on rational supersets of the
    # algebraic branch intervals.
    E5_denominator_polynomial = (
        348160 * r**5
        + 522240 * r**4
        - 2258368 * r**3
        + 394480 * r**2
        + 1826712 * r
        - 1035937
    )

    E4_denominator_polynomial = (
        1516544 * r**5
        + 1729792 * r**4
        - 8695472 * r**3
        + 1481064 * r**2
        + 7298469 * r
        - 4143307
    )

    E5_denominator_roots = count_roots(
        E5_denominator_polynomial,
        sp.Rational(38, 1000),
        sp.Rational(1, 8),
    )
    E4_denominator_roots = count_roots(
        E4_denominator_polynomial,
        sp.Rational(0),
        sp.Rational(39, 1000),
    )

    # Small-noise stationary expansion.
    F5_u = sp.expand(
        F5_full.subs(
            {
                r: sp.Rational(1, 8) - u,
                epsilon: h**2,
            }
        )
    )

    c = 8 * sp.sqrt(174) / 7
    d = -sp.Rational(19456, 147)

    expansion_substitution = sp.expand(
        F5_u.subs(u, c * h + d * h**2)
    )
    expansion_series = sp.series(
        expansion_substitution,
        h,
        0,
        4,
    ).removeO()

    ratio_stationary_series = sp.series(
        phase5["ratio"].subs(
            {
                r: sp.Rational(1, 8)
                - c * h
                - d * h**2,
                epsilon: h**2,
            }
        ),
        h,
        0,
        3,
    ).removeO().expand()

    expected_ratio_series = (
        sp.Rational(502, 499)
        +
        sp.Rational(226816, 5229021)
        * sp.sqrt(174)
        * h
        +
        sp.Rational(
            7391973997568,
            383564377413,
        )
        * h**2
    )

    gamma_sqrt_coefficient = (
        64 * sp.sqrt(174)
        / (7 * sp.log(2))
    )
    gamma_epsilon_coefficient = (
        sp.Rational(913408, 147)
        / sp.log(2)
    )

    risk_sqrt_coefficient = (
        56704 * sp.sqrt(174)
        / (2630229 * sp.log(2))
    )

    E4_derivative_zero = sp.factor(
        E4_derivative.subs(r, 0)
    )
    compactified_linear_coefficient = sp.factor(
        -1 / E4_derivative_zero
    )

    R_infinity = sp.factor(
        phase4["ratio"].subs(r, 0)
    )

    # Algebraic factor identities at the branch annihilation.
    difference_E5_T4 = sp.factor(E5 - T4)
    difference_E4_T4 = sp.factor(E4 - T4)
    difference_E5_E4 = sp.factor(E5 - E4)

    transition_factor_gates = {
        "E5_minus_T4_contains_J": bool(
            sp.rem(
                sp.Poly(
                    sp.fraction(
                        sp.cancel(difference_E5_T4)
                    )[0],
                    r,
                ),
                sp.Poly(J, r),
            )
            == 0
        ),
        "E4_minus_T4_contains_J": bool(
            sp.rem(
                sp.Poly(
                    sp.fraction(
                        sp.cancel(difference_E4_T4)
                    )[0],
                    r,
                ),
                sp.Poly(J, r),
            )
            == 0
        ),
        "E5_minus_E4_contains_J": bool(
            sp.rem(
                sp.Poly(
                    sp.fraction(
                        sp.cancel(difference_E5_E4)
                    )[0],
                    r,
                ),
                sp.Poly(J, r),
            )
            == 0
        ),
    }

    # Representative local branch values.
    representative_epsilons = [
        sp.Rational(1, 10**8),
        sp.Rational(1, 10**7),
        sp.Rational(1, 10**6),
        sp.Rational(5, 10**6),
        sp.Rational(1, 10**5),
        sp.Rational(2, 10**5),
        sp.Rational(5, 10**5),
        sp.Rational(7, 10**5),
        sp.Rational(1, 10**4),
    ]

    representative_table = []

    for current_epsilon in representative_epsilons:
        current_float = float(current_epsilon)

        if bool(current_epsilon < epsilon_a):
            polynomial = sp.Poly(
                sp.together(
                    E5 - current_epsilon
                ).as_numer_denom()[0],
                r,
            )
            roots = [
                root
                for root in polynomial.real_roots()
                if bool(root > r_a)
                and bool(root < sp.Rational(1, 8))
            ]
            if len(roots) != 1:
                raise RuntimeError(
                    "Unexpected regular stationary root count"
                )
            current_r = roots[0]
            current_ratio = phase5["ratio"].subs(
                {
                    r: current_r,
                    epsilon: current_epsilon,
                }
            )
            branch = "regular"
        elif bool(current_epsilon < epsilon_b):
            polynomial = sp.Poly(
                sp.together(
                    E4 - current_epsilon
                ).as_numer_denom()[0],
                r,
            )
            roots = [
                root
                for root in polynomial.real_roots()
                if bool(root > 0)
                and bool(root < r_a)
            ]
            if len(roots) != 1:
                raise RuntimeError(
                    "Unexpected boundary-active root count"
                )
            current_r = roots[0]
            current_ratio = phase4["ratio"].subs(
                {
                    r: current_r,
                    epsilon: current_epsilon,
                }
            )
            branch = "boundary-active"
        else:
            current_r = sp.Integer(0)
            current_ratio = R_infinity.subs(
                epsilon,
                current_epsilon,
            )
            branch = "compactified"

        current_gamma = (
            sp.oo
            if current_r == 0
            else -sp.log(current_r, 2)
        )
        current_risk = (
            sp.log(current_ratio)
            / (2 * sp.log(2))
        )

        representative_table.append(
            {
                "epsilon": str(current_epsilon),
                "branch": branch,
                "r_decimal": (
                    "0"
                    if current_r == 0
                    else str(sp.N(current_r, 30))
                ),
                "gamma_decimal": (
                    "infinity"
                    if current_r == 0
                    else str(sp.N(current_gamma, 30))
                ),
                "future_risk_decimal": str(
                    sp.N(current_risk, 30)
                ),
            }
        )

    gates = {
        "duplicate_primal_dual_identity": bool(
            duplicate["ratio"]
            == duplicate["dual_objective"]
        ),
        "duplicate_third_difference_at_anchor": bool(
            duplicate_delta.subs(
                r,
                sp.Rational(1, 8),
            )
            == -2 * epsilon
        ),
        "redundancy_boundary_derivative_exact": bool(
            T0_derivative_anchor
            == -sp.Rational(735, 63232)
        ),
        "H_bernstein_coefficients_all_positive": bool(
            all(value > 0 for value in H_bernstein)
        ),
        "J_has_one_domain_root": bool(
            len(domain_roots_J) == 1
        ),
        "r_a_in_certified_interval": bool(
            sp.Rational(38038004, 10**9)
            < r_a
            < sp.Rational(38038005, 10**9)
        ),
        "epsilon_a_in_certified_interval": bool(
            sp.Rational(36878499, 10**12)
            < epsilon_a
            < sp.Rational(36878500, 10**12)
        ),
        "transition_curve_identities_pass": bool(
            all(transition_factor_gates.values())
        ),
        "E5_denominator_has_no_branch_root": bool(
            E5_denominator_roots == 0
        ),
        "E4_denominator_has_no_branch_root": bool(
            E4_denominator_roots == 0
        ),
        "E5_anchor_endpoint_zero": bool(
            E5.subs(r, sp.Rational(1, 8)) == 0
        ),
        "E4_compactified_endpoint_exact": bool(
            epsilon_b == sp.Rational(189, 2367604)
        ),
        "stationary_expansion_cancels_through_h3": bool(
            sp.expand(expansion_series) == 0
        ),
        "stationary_ratio_series_exact": bool(
            sp.expand(
                ratio_stationary_series
                - expected_ratio_series
            )
            == 0
        ),
        "gamma_sqrt_coefficient_exact": bool(
            gamma_sqrt_coefficient
            == 64
            * sp.sqrt(174)
            / (7 * sp.log(2))
        ),
        "gamma_epsilon_coefficient_exact": bool(
            gamma_epsilon_coefficient
            == sp.Rational(913408, 147)
            / sp.log(2)
        ),
        "risk_sqrt_coefficient_exact": bool(
            risk_sqrt_coefficient
            == 56704
            * sp.sqrt(174)
            / (2630229 * sp.log(2))
        ),
        "boundary_linear_coefficient_exact": bool(
            compactified_linear_coefficient
            == sp.Rational(
                350346793801,
                482114457,
            )
        ),
        "compactified_ratio_formula_exact": bool(
            sp.factor(
                R_infinity
                - (
                    10998100 * epsilon + 52087
                )
                /
                (
                    2
                    * (
                        4128540 * epsilon
                        + 25823
                    )
                )
            )
            == 0
        ),
        "benchmark_1e-4_above_epsilon_b": bool(
            sp.Rational(1, 10000) > epsilon_b
        ),
    }

    verdict = (
        "PASS_NOISE_SEPARATION_BOUNDARY_LAYER_AND_LOCAL_BIFURCATION_SKELETON"
        if all(gates.values())
        else "FAIL_A46_BOUNDARY_LAYER_AUDIT"
    )

    result = {
        "audit": (
            "A46_PROVISIONAL_NOISE_SEPARATION_BOUNDARY_LAYER"
        ),
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "anchors": ["2*log(2)", "3*log(2)"],
            "third_parameter": "gamma*log(2)",
            "r_definition": "r=2^(-gamma)",
            "target": (
                "direct future-Q minimax ratio under a=1/2"
            ),
        },
        "redundancy_boundary": {
            "T0": str(T0),
            "r_expansion": (
                "1/8 - (63232/735)*epsilon + O(epsilon^2)"
            ),
            "gamma_expansion": (
                "3 + 505856/(735*log(2))*epsilon "
                "+ O(epsilon^2)"
            ),
        },
        "regular_stationary_branch": {
            "E5": str(E5),
            "r_expansion": (
                "1/8 - 8*sqrt(174)/7*sqrt(epsilon) "
                "+ 19456/147*epsilon + O(epsilon^(3/2))"
            ),
            "gamma_expansion": (
                "3 + 64*sqrt(174)/(7*log(2))*sqrt(epsilon) "
                "+ 913408/(147*log(2))*epsilon "
                "+ O(epsilon^(3/2))"
            ),
            "ratio_expansion": str(expected_ratio_series),
            "future_risk_sqrt_coefficient": str(
                risk_sqrt_coefficient
            ),
        },
        "branch_annihilation": {
            "J": str(J),
            "r_a_object": str(r_a),
            "r_a_decimal": str(sp.N(r_a, 40)),
            "gamma_a_decimal": str(
                sp.N(-sp.log(r_a, 2), 40)
            ),
            "epsilon_a_object": str(epsilon_a),
            "epsilon_a_decimal": str(
                sp.N(epsilon_a, 40)
            ),
            "T4": str(T4),
        },
        "boundary_active_branch": {
            "E4": str(E4),
            "epsilon_b_exact": str(epsilon_b),
            "epsilon_b_decimal": str(
                sp.N(epsilon_b, 40)
            ),
            "near_boundary_r_coefficient": str(
                compactified_linear_coefficient
            ),
            "infinity_ratio": str(R_infinity),
        },
        "representative_stationary_values": (
            representative_table
        ),
        "transition_factor_gates": (
            transition_factor_gates
        ),
        "H_bernstein_coefficients": [
            str(value) for value in H_bernstein
        ],
        "formal_status": {
            "established": [
                (
                    "linear redundancy-plateau scaling near "
                    "zero noise"
                ),
                (
                    "unique regular stationary local-minimum "
                    "branch and sqrt-noise separation"
                ),
                (
                    "algebraic annihilation threshold "
                    "epsilon_a"
                ),
                (
                    "unique boundary-active stationary branch "
                    "between epsilon_a and epsilon_b"
                ),
                (
                    "exact compactified local threshold "
                    "epsilon_b"
                ),
            ],
            "not_established": [
                (
                    "complete globally optimal two-dimensional "
                    "phase partition"
                ),
                (
                    "global optimality of every small-noise "
                    "local stationary branch"
                ),
                "empirical noise or cost model",
                "physical interpretation",
            ],
        },
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A46 certifies local and asymptotic bifurcation "
            "structure. It deliberately does not claim a complete "
            "global (epsilon,gamma) phase diagram. A45 remains the "
            "global theorem at epsilon=1/10000."
        ),
    }

    output_path = Path(__file__).with_name(
        "a46_noise_separation_boundary_layer_results.json"
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
