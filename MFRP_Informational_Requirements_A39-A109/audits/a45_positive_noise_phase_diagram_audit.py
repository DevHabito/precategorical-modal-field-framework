#!/usr/bin/env python3
"""A45 exact audit: complete positive-noise phase diagram.

Contract
--------
support = {0,1,2,3,4,5}
mean = 5/2
anchors = 2*log(2), 3*log(2)
third parameter = gamma*log(2), gamma >= 3
common absolute tolerance = 1/10000
target = direct future-Q width under contraction a=1/2

The script constructs symbolic Charnes-Cooper primal and dual certificates for
all active regimes, isolates the four algebraic transition roots exactly, and
certifies positivity/nonnegativity on algebraic intervals using exact real-root
isolation. No design ranking is inferred from floating-point optimization.
"""

from __future__ import annotations

import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Any

import sympy as sp


SUPPORT = list(range(6))
TARGET = [sp.Rational(1, 2**x) for x in SUPPORT]
MEAN = sp.Rational(5, 2)
EPSILON = sp.Rational(1, 10000)

r = sp.symbols("r", real=True)


def transform_row_integer(exponent: int) -> list[sp.Rational]:
    return [
        sp.Rational(1, 2 ** (exponent * x))
        for x in SUPPORT
    ]


ROW2 = transform_row_integer(2)
ROW3 = transform_row_integer(3)
ROWR = [r**x for x in SUPPORT]


def dot(
    values: list[sp.Expr],
    weights: list[sp.Expr],
) -> sp.Expr:
    return sp.factor(
        sum(
            values[index] * weights[index]
            for index in range(6)
        )
    )


def build_base_rows() -> tuple[
    list[list[sp.Expr]],
    list[sp.Expr],
]:
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
    observation_rows: list[list[sp.Expr]],
    signs: list[int],
) -> dict[str, Any]:
    positive_indices = (
        p_support
        + [6 + index for index in q_support]
        + [12]
    )

    rows, rhs = build_base_rows()
    equality_count = len(rows)

    for values, sign in zip(observation_rows, signs):
        current = [sp.Integer(0)] * 13
        for index in range(6):
            current[index] = sign * values[index]
            current[6 + index] = -sign * values[index]
        current[12] = -2 * EPSILON
        rows.append(current)
        rhs.append(0)

    primal_matrix = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(len(rows))
        ]
    )

    if primal_matrix.rows != primal_matrix.cols:
        raise RuntimeError("Active primal system is not square")

    primal_solution = primal_matrix.inv() * sp.Matrix(rhs)

    z = [sp.Integer(0)] * 13
    for index, value in zip(
        positive_indices,
        primal_solution,
    ):
        z[index] = sp.factor(value)

    scale = z[12]
    p = [
        sp.factor(z[index] / scale)
        for index in range(6)
    ]
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
        [
            objective[index]
            for index in positive_indices
        ]
    )
    dual = [
        sp.factor(value)
        for value in dual_solution
    ]

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
        "positive_indices": positive_indices,
        "equality_count": equality_count,
        "rows": rows,
        "rhs": rhs,
        "z": z,
        "scale": scale,
        "p": p,
        "q": q,
        "ratio": ratio,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "dual_objective": dual_objective,
    }


def symbolic_duplicate_certificate() -> dict[str, Any]:
    positive_indices = [
        0,
        1,
        2,
        5,
        6 + 1,
        6 + 3,
        12,
    ]

    rows, rhs = build_base_rows()
    equality_count = len(rows)

    for values, sign in zip(
        [ROW2, ROW3],
        [1, -1],
    ):
        current = [sp.Integer(0)] * 13
        for index in range(6):
            current[index] = sign * values[index]
            current[6 + index] = -sign * values[index]
        current[12] = -2 * EPSILON
        rows.append(current)
        rhs.append(0)

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
    for index, value in zip(
        positive_indices,
        primal_solution,
    ):
        z[index] = sp.factor(value)

    scale = z[12]
    p = [
        sp.factor(z[index] / scale)
        for index in range(6)
    ]
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
        [
            objective[index]
            for index in positive_indices
        ]
    )
    dual = [
        sp.factor(value)
        for value in dual_solution
    ]

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
        "positive_indices": positive_indices,
        "equality_count": equality_count,
        "rows": rows,
        "rhs": rhs,
        "z": z,
        "scale": scale,
        "p": p,
        "q": q,
        "ratio": ratio,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "dual_objective": dual_objective,
    }


TRANSITION_POLYNOMIALS = [
    (
        53268160 * r**4
        + 13317040 * r**3
        - 200908865 * r**2
        + 148890794 * r
        - 14639747
    ),
    (
        35156096 * r**4
        + 8789024 * r**3
        - 132490502 * r**2
        + 98061088 * r
        - 9569361
    ),
    (
        334069952 * r**4
        - 455233544 * r**3
        - 113808386 * r**2
        + 257741432 * r
        - 23297331
    ),
    (
        1838752 * r**4
        - 4611812 * r**3
        + 3732866 * r**2
        - 989812 * r
        + 33387
    ),
]

ISOLATING_INTERVALS = [
    (
        sp.Rational(11640178, 10**8),
        sp.Rational(11640179, 10**8),
    ),
    (
        sp.Rational(11536718, 10**8),
        sp.Rational(11536719, 10**8),
    ),
    (
        sp.Rational(9589933, 10**8),
        sp.Rational(9589934, 10**8),
    ),
    (
        sp.Rational(3926824, 10**8),
        sp.Rational(3926825, 10**8),
    ),
]


def unique_domain_root(
    polynomial: sp.Expr,
) -> sp.Expr:
    roots = sp.Poly(polynomial, r).real_roots()
    candidates = [
        root
        for root in roots
        if bool(root > 0)
        and bool(root < sp.Rational(1, 8))
    ]
    if len(candidates) != 1:
        raise RuntimeError(
            "Transition polynomial does not have one domain root"
        )
    return candidates[0]


TRANSITION_ROOTS = [
    unique_domain_root(polynomial)
    for polynomial in TRANSITION_POLYNOMIALS
]

r0, r1, r2, r3 = TRANSITION_ROOTS


@lru_cache(maxsize=None)
def cached_real_roots(
    coefficients: tuple[sp.Expr, ...],
) -> tuple[sp.Expr, ...]:
    polynomial = sp.Poly.from_list(
        list(coefficients),
        gens=r,
        domain=sp.QQ,
    )
    return tuple(polynomial.real_roots())


def primitive_polynomial(
    expression: sp.Expr,
) -> sp.Poly:
    polynomial = sp.Poly(
        sp.factor(expression),
        r,
        domain=sp.QQ,
    )
    _, primitive = polynomial.primitive()
    if primitive.LC() < 0:
        primitive = -primitive
    return primitive


def rational_midpoint(
    lower: sp.Expr,
    upper: sp.Expr,
) -> sp.Rational:
    lower_decimal = float(sp.N(lower, 30))
    upper_decimal = float(sp.N(upper, 30))
    midpoint = sp.Rational(
        str((lower_decimal + upper_decimal) / 2)
    )
    if not bool(lower < midpoint < upper):
        raise RuntimeError("Failed to build an interior point")
    return midpoint


def certify_nonnegative_on_interval(
    expression: sp.Expr,
    lower: sp.Expr,
    upper: sp.Expr,
    *,
    strict_interior: bool = False,
) -> dict[str, Any]:
    expression = sp.factor(expression)

    if expression == 0:
        return {
            "ok": not strict_interior,
            "identically_zero": True,
        }

    numerator, denominator = sp.fraction(
        sp.cancel(expression)
    )

    numerator_polynomial = primitive_polynomial(numerator)
    denominator_polynomial = primitive_polynomial(
        denominator
    )

    numerator_roots = cached_real_roots(
        tuple(numerator_polynomial.all_coeffs())
    )
    denominator_roots = cached_real_roots(
        tuple(denominator_polynomial.all_coeffs())
    )

    interior_numerator_roots = [
        root
        for root in numerator_roots
        if bool(lower < root < upper)
    ]
    interior_denominator_roots = [
        root
        for root in denominator_roots
        if bool(lower < root < upper)
    ]

    midpoint = rational_midpoint(lower, upper)

    midpoint_sign = sp.sign(
        expression.subs(r, midpoint)
    )
    lower_sign = sp.sign(
        expression.subs(r, lower)
    )
    upper_sign = sp.sign(
        expression.subs(r, upper)
    )

    denominator_lower = sp.sign(
        denominator.subs(r, lower)
    )
    denominator_upper = sp.sign(
        denominator.subs(r, upper)
    )

    ok = (
        not interior_numerator_roots
        and not interior_denominator_roots
        and denominator_lower != 0
        and denominator_upper != 0
        and midpoint_sign == 1
        and lower_sign >= 0
        and upper_sign >= 0
    )

    if strict_interior:
        ok = ok and midpoint_sign == 1

    return {
        "ok": bool(ok),
        "identically_zero": False,
        "midpoint_sign": str(midpoint_sign),
        "lower_sign": str(lower_sign),
        "upper_sign": str(upper_sign),
        "interior_numerator_root_count": len(
            interior_numerator_roots
        ),
        "interior_denominator_root_count": len(
            interior_denominator_roots
        ),
    }


def exact_phase_gates(
    certificate: dict[str, Any],
    lower: sp.Expr,
    upper: sp.Expr,
) -> dict[str, Any]:
    p = certificate["p"]
    q = certificate["q"]

    original_differences = [
        sp.factor(
            dot(values, p) - dot(values, q)
        )
        for values in [ROW2, ROW3, ROWR]
    ]

    nonzero_primal = [
        value
        for value in p + q
        if value != 0
    ]
    nonzero_primal.append(certificate["scale"])

    inequality_duals = certificate["dual"][
        certificate["equality_count"]:
    ]

    nonzero_reduced_costs = [
        value
        for value in certificate["reduced_costs"]
        if value != 0
    ]

    primal_sign_certificates = [
        certify_nonnegative_on_interval(
            expression,
            lower,
            upper,
        )
        for expression in nonzero_primal
    ]

    dual_sign_certificates = [
        certify_nonnegative_on_interval(
            expression,
            lower,
            upper,
        )
        for expression in inequality_duals
    ]

    reduced_cost_certificates = [
        certify_nonnegative_on_interval(
            expression,
            lower,
            upper,
        )
        for expression in nonzero_reduced_costs
    ]

    derivative = sp.factor(
        sp.diff(certificate["ratio"], r)
    )
    derivative_certificate = (
        certify_nonnegative_on_interval(
            derivative,
            lower,
            upper,
            strict_interior=True,
        )
    )

    gates = {
        "normalization_symbolic": bool(
            sp.factor(sum(p)) == 1
            and sp.factor(sum(q)) == 1
        ),
        "mean_symbolic": bool(
            dot(
                [sp.Integer(x) for x in SUPPORT],
                p,
            )
            == MEAN
            and dot(
                [sp.Integer(x) for x in SUPPORT],
                q,
            )
            == MEAN
        ),
        "observational_differences_symbolic": bool(
            original_differences
            == [
                sp.Rational(1, 5000),
                -sp.Rational(1, 5000),
                sp.Rational(1, 5000),
            ]
        ),
        "primal_dual_objective_identity": bool(
            sp.factor(
                certificate["ratio"]
                - certificate["dual_objective"]
            )
            == 0
        ),
        "all_primal_sign_certificates_pass": bool(
            all(
                item["ok"]
                for item in primal_sign_certificates
            )
        ),
        "all_dual_sign_certificates_pass": bool(
            all(
                item["ok"]
                for item in dual_sign_certificates
            )
        ),
        "all_reduced_cost_certificates_pass": bool(
            all(
                item["ok"]
                for item in reduced_cost_certificates
            )
        ),
        "ratio_derivative_positive_in_r": bool(
            derivative_certificate["ok"]
        ),
    }

    return {
        "gates": gates,
        "derivative": str(derivative),
        "original_differences": [
            str(value)
            for value in original_differences
        ],
        "sign_certificate_counts": {
            "primal": len(primal_sign_certificates),
            "dual": len(dual_sign_certificates),
            "reduced_cost": len(
                reduced_cost_certificates
            ),
        },
    }


def adjacent_continuity_gate(
    left: sp.Expr,
    right: sp.Expr,
    transition_polynomial: sp.Expr,
) -> bool:
    numerator = sp.fraction(
        sp.cancel(left - right)
    )[0]

    remainder = sp.rem(
        sp.Poly(numerator, r, domain=sp.QQ),
        sp.Poly(
            transition_polynomial,
            r,
            domain=sp.QQ,
        ),
    )

    return bool(remainder == 0)


def main() -> None:
    duplicate = symbolic_duplicate_certificate()

    phases = {
        "phase_1": symbolic_noisy_certificate(
            [0, 1, 2, 5],
            [1, 2, 3],
            [ROW2, ROW3, ROWR],
            [1, -1, 1],
        ),
        "phase_2": symbolic_noisy_certificate(
            [0, 2, 5],
            [1, 2, 3, 4],
            [ROW2, ROW3, ROWR],
            [1, -1, 1],
        ),
        "phase_3": symbolic_noisy_certificate(
            [0, 2, 3, 5],
            [1, 2, 4],
            [ROW2, ROW3, ROWR],
            [1, -1, 1],
        ),
        "phase_4": symbolic_noisy_certificate(
            [0, 1, 3, 5],
            [1, 2, 4],
            [ROW2, ROW3, ROWR],
            [1, -1, 1],
        ),
    }

    phase_intervals = {
        "phase_1": (r1, r0),
        "phase_2": (r2, r1),
        "phase_3": (r3, r2),
        "phase_4": (sp.Rational(0), r3),
    }

    phase_audits = {
        name: exact_phase_gates(
            certificate,
            *phase_intervals[name],
        )
        for name, certificate in phases.items()
    }

    duplicate_delta = sp.factor(
        dot(ROWR, duplicate["p"])
        - dot(ROWR, duplicate["q"])
    )

    plateau_lower = sp.factor(
        duplicate_delta
        + sp.Rational(1, 5000)
    )
    plateau_upper = sp.factor(
        sp.Rational(1, 5000)
        - duplicate_delta
    )

    plateau_lower_certificate = (
        certify_nonnegative_on_interval(
            plateau_lower,
            r0,
            sp.Rational(1, 8),
        )
    )
    plateau_upper_certificate = (
        certify_nonnegative_on_interval(
            plateau_upper,
            r0,
            sp.Rational(1, 8),
        )
    )

    duplicate_nonzero_primal = [
        value
        for value in duplicate["p"] + duplicate["q"]
        if value != 0
    ]
    duplicate_nonzero_primal.append(
        duplicate["scale"]
    )

    duplicate_primal_signs = [
        sp.sign(value)
        for value in duplicate_nonzero_primal
    ]
    duplicate_dual_signs = [
        sp.sign(value)
        for value in duplicate["dual"][
            duplicate["equality_count"]:
        ]
    ]
    duplicate_reduced_signs = [
        sp.sign(value)
        for value in duplicate["reduced_costs"]
        if value != 0
    ]

    root_isolation_gates = {}
    for index, (
        polynomial,
        root,
        interval,
    ) in enumerate(
        zip(
            TRANSITION_POLYNOMIALS,
            TRANSITION_ROOTS,
            ISOLATING_INTERVALS,
        )
    ):
        lower, upper = interval
        root_isolation_gates[
            f"transition_{index}_unique_domain_root"
        ] = bool(
            sp.Poly(
                polynomial,
                r,
            ).count_roots(
                0,
                sp.Rational(1, 8),
            )
            == 1
        )
        root_isolation_gates[
            f"transition_{index}_inside_declared_interval"
        ] = bool(
            lower < root < upper
            and sp.Poly(
                polynomial,
                r,
            ).count_roots(
                lower,
                upper,
            )
            == 1
        )

    root_order_gate = bool(
        0 < r3 < r2 < r1 < r0 < sp.Rational(1, 8)
    )

    ratios = [
        duplicate["ratio"],
        phases["phase_1"]["ratio"],
        phases["phase_2"]["ratio"],
        phases["phase_3"]["ratio"],
        phases["phase_4"]["ratio"],
    ]

    continuity_gates = {
        "plateau_to_phase_1": adjacent_continuity_gate(
            ratios[0],
            ratios[1],
            TRANSITION_POLYNOMIALS[0],
        ),
        "phase_1_to_phase_2": adjacent_continuity_gate(
            ratios[1],
            ratios[2],
            TRANSITION_POLYNOMIALS[1],
        ),
        "phase_2_to_phase_3": adjacent_continuity_gate(
            ratios[2],
            ratios[3],
            TRANSITION_POLYNOMIALS[2],
        ),
        "phase_3_to_phase_4": adjacent_continuity_gate(
            ratios[3],
            ratios[4],
            TRANSITION_POLYNOMIALS[3],
        ),
    }

    infinity_ratio = sp.factor(
        phases["phase_4"]["ratio"].subs(r, 0)
    )

    expected_infinity_ratio = sp.Rational(
        26593405,
        26235854,
    )

    selected_gammas = [3, 4, 6, 10]
    risk_table = []

    def ratio_at_integer_gamma(
        gamma: int,
    ) -> sp.Expr:
        current_r = sp.Rational(
            1,
            2**gamma,
        )

        if bool(current_r >= r0):
            return duplicate["ratio"]
        if bool(current_r >= r1):
            return sp.factor(
                phases["phase_1"]["ratio"].subs(
                    r,
                    current_r,
                )
            )
        if bool(current_r >= r2):
            return sp.factor(
                phases["phase_2"]["ratio"].subs(
                    r,
                    current_r,
                )
            )
        if bool(current_r >= r3):
            return sp.factor(
                phases["phase_3"]["ratio"].subs(
                    r,
                    current_r,
                )
            )
        return sp.factor(
            phases["phase_4"]["ratio"].subs(
                r,
                current_r,
            )
        )

    for gamma in selected_gammas:
        ratio_value = ratio_at_integer_gamma(gamma)
        future_risk = (
            sp.log(ratio_value)
            / (2 * sp.log(2))
        )
        risk_table.append(
            {
                "gamma": gamma,
                "ratio_exact": str(ratio_value),
                "future_risk_decimal": (
                    f"{float(future_risk):.18g}"
                ),
            }
        )

    transition_table = []
    for index, root in enumerate(TRANSITION_ROOTS):
        gamma_value = -sp.log(root, 2)
        ratio_value = ratios[index].subs(r, root)
        future_risk = (
            sp.log(ratio_value)
            / (2 * sp.log(2))
        )

        transition_table.append(
            {
                "transition": index,
                "root_object": str(root),
                "r_decimal": str(sp.N(root, 40)),
                "gamma_decimal": str(
                    sp.N(gamma_value, 40)
                ),
                "future_risk_decimal": str(
                    sp.N(future_risk, 40)
                ),
                "isolating_interval": [
                    str(ISOLATING_INTERVALS[index][0]),
                    str(ISOLATING_INTERVALS[index][1]),
                ],
            }
        )

    phase_gate_values = [
        value
        for phase in phase_audits.values()
        for value in phase["gates"].values()
    ]

    global_gates = {
        **root_isolation_gates,
        "transition_roots_strictly_ordered": root_order_gate,
        "duplicate_ratio_matches_A44": bool(
            duplicate["ratio"]
            == sp.Rational(
                337423987,
                317703750,
            )
        ),
        "duplicate_primal_dual_equal": bool(
            duplicate["ratio"]
            == duplicate["dual_objective"]
        ),
        "duplicate_primal_positive": bool(
            all(sign > 0 for sign in duplicate_primal_signs)
        ),
        "duplicate_dual_inequality_multipliers_nonnegative": bool(
            all(sign >= 0 for sign in duplicate_dual_signs)
        ),
        "duplicate_reduced_costs_nonnegative": bool(
            all(sign >= 0 for sign in duplicate_reduced_signs)
        ),
        "plateau_lower_tolerance_certified": bool(
            plateau_lower_certificate["ok"]
        ),
        "plateau_upper_tolerance_certified": bool(
            plateau_upper_certificate["ok"]
        ),
        "all_phase_internal_gates_pass": bool(
            all(phase_gate_values)
        ),
        "all_adjacent_branches_continuous": bool(
            all(continuity_gates.values())
        ),
        "phase_4_limit_matches_A44_infinity": bool(
            infinity_ratio
            == expected_infinity_ratio
        ),
        "global_curve_nonincreasing_in_gamma": bool(
            all(
                phase["gates"][
                    "ratio_derivative_positive_in_r"
                ]
                for phase in phase_audits.values()
            )
        ),
        "compactified_infinity_strictly_below_plateau": bool(
            expected_infinity_ratio
            < duplicate["ratio"]
        ),
    }

    verdict = (
        "PASS_COMPLETE_POSITIVE_NOISE_PHASE_DIAGRAM_AND_HARD_CAP_RULE"
        if all(global_gates.values())
        else "FAIL_A45_PHASE_DIAGRAM_AUDIT"
    )

    result = {
        "audit": (
            "A45_PROVISIONAL_COMPLETE_POSITIVE_NOISE_PHASE_DIAGRAM"
        ),
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "epsilon": str(EPSILON),
            "design": (
                "{2*log(2), 3*log(2), gamma*log(2)}"
            ),
            "gamma_domain": "[3, infinity]",
            "target": (
                "direct future-Q minimax width, contraction a=1/2"
            ),
        },
        "transition_polynomials": [
            str(sp.factor(polynomial))
            for polynomial in TRANSITION_POLYNOMIALS
        ],
        "transition_table": transition_table,
        "piecewise_ratios": {
            "plateau": str(duplicate["ratio"]),
            "phase_1": str(
                phases["phase_1"]["ratio"]
            ),
            "phase_2": str(
                phases["phase_2"]["ratio"]
            ),
            "phase_3": str(
                phases["phase_3"]["ratio"]
            ),
            "phase_4": str(
                phases["phase_4"]["ratio"]
            ),
            "infinity": str(infinity_ratio),
        },
        "support_patterns": {
            "plateau": {
                "p": [0, 1, 2, 5],
                "q": [1, 3],
                "third_constraint": "inactive",
            },
            "phase_1": {
                "p": [0, 1, 2, 5],
                "q": [1, 2, 3],
            },
            "phase_2": {
                "p": [0, 2, 5],
                "q": [1, 2, 3, 4],
            },
            "phase_3": {
                "p": [0, 2, 3, 5],
                "q": [1, 2, 4],
            },
            "phase_4": {
                "p": [0, 1, 3, 5],
                "q": [1, 2, 4],
            },
        },
        "phase_audits": phase_audits,
        "continuity_gates": continuity_gates,
        "plateau": {
            "third_difference": str(duplicate_delta),
            "lower_certificate": plateau_lower_certificate,
            "upper_certificate": plateau_upper_certificate,
        },
        "selected_integer_gamma_risks": risk_table,
        "hard_cap_rule": {
            "plateau_end_gamma_decimal": str(
                sp.N(-sp.log(r0, 2), 40)
            ),
            "if_cap_at_or_below_plateau_end": (
                "all gamma in [3, cap] tie"
            ),
            "if_cap_above_plateau_end": (
                "unique minimizer gamma = cap"
            ),
        },
        "formal_results": [
            (
                "complete piecewise-rational direct-risk curve "
                "for epsilon=1/10000"
            ),
            "four algebraic transition roots",
            "five globally optimal active regimes",
            (
                "constant redundancy plateau followed by strict "
                "risk decrease in gamma"
            ),
            "unique compactified minimizer gamma=infinity",
            "exact finite hard-cap endpoint rule",
            (
                "endpoint reversal relative to exact-data "
                "minimum-separation design"
            ),
        ],
        "gates": global_gates,
        "verdict": verdict,
        "boundary": (
            "The phase diagram is exact only under the declared finite "
            "support, exact mean, anchor pair, target, contraction, common "
            "absolute tolerance, and direct-ratio risk. No empirical error "
            "model, physical cost, or physical meaning of gamma is inferred."
        ),
    }

    output_path = Path(__file__).with_name(
        "a45_positive_noise_phase_diagram_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2))

    if not all(global_gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
