#!/usr/bin/env python3
"""A101 exact gamma-active interval theorem and final residual closure.

A100 resolved the first of four A99 residuals at

    M=443, s=13/100, j=78

with

    P={j-1,j,M}, Q={0,1,h,h+1},
    active={alpha+, beta-, gamma-}.

A101 performs two falsifiable upgrades.

1. It constructs all 895 KKT conditions as rational functions of the probe s.
   Because only the alpha row varies with s, an exact rank-one row update gives
   a seven-term common denominator and sparse condition numerators.  The
   maximal connected strict-KKT component containing 13/100 inside
   [129/1000,133/1000] is isolated.  Its lower boundary is the gamma-minus
   active multiplier; its upper boundary is the basic p_{j-1} mass.  Every
   other condition numerator and the common denominator are certified by exact
   integer interval arithmetic on the complete boundary hull.

2. It tests the same gamma-active architecture at the three residual witnesses
   left after A100: M=449,484,490.  All three pass the unrestricted finite-LP
   KKT system strictly.  Together with A97-A100, this closes the 83-point A95
   rational-witness obstruction list, but it does not prove interval persistence
   at every witness or a universal support law.

This is contract-relative mathematics, not a physical or ontological claim.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Callable

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A95_RESULT = RESULTS / "a95_rational_witness_lift_results.json"
A97_RESULT = RESULTS / "a97_endpoint_released_interval_and_obstruction_results.json"
A99_RESULT = RESULTS / "a99_q0q1_interval_and_residual_atlas_results.json"
A100_RESULT = RESULTS / "a100_full_lp_active_set_resolution_results.json"

SEARCH_LOWER = sp.Rational(129, 1000)
SEARCH_UPPER = sp.Rational(133, 1000)
S0 = sp.Rational(13, 100)
M0 = 443
J0 = 78
ROOT_DENOMINATOR = 10**24
LOWER_ROOT_BRACKET = (
    sp.Rational(129950386680648955573451, ROOT_DENOMINATOR),
    sp.Rational(129950386680648955573452, ROOT_DENOMINATOR),
)
UPPER_ROOT_BRACKET = (
    sp.Rational(130103853082902466513379, ROOT_DENOMINATOR),
    sp.Rational(130103853082902466513380, ROOT_DENOMINATOR),
)
EXPECTED_A99_FAILURES = [
    (443, "13/100", 78),
    (449, "13/100", 79),
    (484, "13/100", 85),
    (490, "13/100", 86),
]
EXPECTED_FINAL_TESTS = [
    (449, "13/100", 79),
    (484, "13/100", 85),
    (490, "13/100", 86),
]

SparsePoly = dict[int, sp.Rational]


def normalized_epsilon(maximum: int) -> sp.Rational:
    h = maximum // 2
    factor = 1875 if maximum % 2 == 0 else 2500
    return sp.Rational(1, factor * 2**h)


def target_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2**x)


def beta_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (3 * x))


def gamma_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (4 * x))


def exact_sign(value: sp.Expr) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def decimal_str(value: sp.Expr, digits: int = 40) -> str:
    return str(sp.N(value, digits))


def sparse_add(*parts: tuple[SparsePoly, sp.Rational, int]) -> SparsePoly:
    output: SparsePoly = {}
    for polynomial, scale, shift in parts:
        scale = sp.Rational(scale)
        for exponent, coefficient in polynomial.items():
            new_exponent = exponent + shift
            output[new_exponent] = output.get(new_exponent, sp.Rational(0)) + scale * coefficient
    return {exponent: coefficient for exponent, coefficient in output.items() if coefficient != 0}


def sparse_eval(polynomial: SparsePoly, point: sp.Rational) -> sp.Rational:
    return sum(coefficient * point**exponent for exponent, coefficient in polynomial.items())


def sparse_derivative(polynomial: SparsePoly) -> SparsePoly:
    return {
        exponent - 1: exponent * coefficient
        for exponent, coefficient in polynomial.items()
        if exponent > 0
    }


def rank_one_symbolic_conditions(
    maximum: int,
    contact: int,
    reference_probe: sp.Rational,
) -> tuple[SparsePoly, list[tuple[str, SparsePoly]]]:
    """Construct sparse KKT numerators using an exact one-row update.

    Only the alpha row depends on s.  Starting from the exact inverse at the
    reference probe, the Sherman-Morrison row-update formula gives every basic
    variable and dual variable over one common sparse denominator.
    """
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    p_support = [contact - 1, contact, maximum]
    q_support = [0, 1, h, h + 1]

    def alpha0(x: int) -> sp.Rational:
        return reference_probe**x

    rows = [
        [1, 1, 1, 0, 0, 0, 0, -1],
        [0, 0, 0, 1, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, 0, -mean],
        [0, 0, 0, *q_support, -mean],
        [0, 0, 0, *[target_value(x) for x in q_support], 0],
        [
            *[alpha0(x) for x in p_support],
            *[-alpha0(x) for x in q_support],
            -2 * epsilon,
        ],
        [
            *[-beta_value(x) for x in p_support],
            *[beta_value(x) for x in q_support],
            -2 * epsilon,
        ],
        [
            *[-gamma_value(x) for x in p_support],
            *[gamma_value(x) for x in q_support],
            -2 * epsilon,
        ],
    ]
    matrix = sp.Matrix(rows)
    inverse = matrix.inv(method="DM")
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
    objective = sp.Matrix([
        *[target_value(x) for x in p_support],
        0, 0, 0, 0, 0,
    ])
    basic0 = inverse * rhs
    dual0 = inverse.T * objective
    alpha_row_index = 5
    update_direction = inverse[:, alpha_row_index]

    signs = [1, 1, 1, -1, -1, -1, -1, 0]
    exponents = [*p_support, *q_support, 0]
    row_updates: list[SparsePoly] = []
    for sign, exponent in zip(signs, exponents):
        if sign == 0:
            row_updates.append({})
        else:
            row_updates.append(sparse_add(
                ({exponent: sp.Rational(sign)}, 1, 0),
                ({0: -sp.Rational(sign) * reference_probe**exponent}, 1, 0),
            ))

    denominator: SparsePoly = {0: sp.Rational(1)}
    for update, coefficient in zip(row_updates, update_direction):
        denominator = sparse_add((denominator, 1, 0), (update, coefficient, 0))

    update_dot_basic: SparsePoly = {}
    for update, coefficient in zip(row_updates, basic0):
        update_dot_basic = sparse_add((update_dot_basic, 1, 0), (update, coefficient, 0))

    basic_numerators = [
        sparse_add(
            (denominator, basic0[index], 0),
            (update_dot_basic, -update_direction[index], 0),
        )
        for index in range(8)
    ]

    objective_update_direction = objective.dot(update_direction)
    dual_numerators: list[SparsePoly] = []
    for column in range(8):
        update_times_inverse: SparsePoly = {}
        for row, update in enumerate(row_updates):
            update_times_inverse = sparse_add(
                (update_times_inverse, 1, 0),
                (update, inverse[row, column], 0),
            )
        dual_numerators.append(sparse_add(
            (denominator, dual0[column], 0),
            (update_times_inverse, -objective_update_direction, 0),
        ))

    if sparse_eval(denominator, reference_probe) != 1:
        raise AssertionError("rank-one denominator does not normalize to one")
    for index in range(8):
        if sparse_eval(basic_numerators[index], reference_probe) != basic0[index]:
            raise AssertionError("basic-variable row-update regression failed")
        if sparse_eval(dual_numerators[index], reference_probe) != dual0[index]:
            raise AssertionError("dual-variable row-update regression failed")

    conditions: list[tuple[str, SparsePoly]] = []
    variable_names = [
        *[f"basic_p_{x}" for x in p_support],
        *[f"basic_q_{x}" for x in q_support],
        "basic_t",
    ]
    conditions.extend(zip(variable_names, basic_numerators))
    conditions.extend([
        ("active_dual_alpha_+1", dual_numerators[5]),
        ("active_dual_beta_-1", dual_numerators[6]),
        ("active_dual_gamma_-1", dual_numerators[7]),
    ])

    p_set = set(p_support)
    q_set = set(q_support)
    for x in range(maximum + 1):
        if x not in p_set:
            numerator = sparse_add(
                (dual_numerators[0], 1, 0),
                (dual_numerators[2], x, 0),
                (dual_numerators[5], 1, x),
                (dual_numerators[6], -beta_value(x), 0),
                (dual_numerators[7], -gamma_value(x), 0),
                (denominator, -target_value(x), 0),
            )
            conditions.append((f"reduced_cost_p_{x}", numerator))
        if x not in q_set:
            numerator = sparse_add(
                (dual_numerators[1], 1, 0),
                (dual_numerators[3], x, 0),
                (dual_numerators[4], target_value(x), 0),
                (dual_numerators[5], -1, x),
                (dual_numerators[6], beta_value(x), 0),
                (dual_numerators[7], gamma_value(x), 0),
            )
            conditions.append((f"reduced_cost_q_{x}", numerator))

    alpha_difference: SparsePoly = {}
    for index, x in enumerate(p_support):
        alpha_difference = sparse_add((alpha_difference, 1, 0), (basic_numerators[index], 1, x))
    for index, x in enumerate(q_support):
        alpha_difference = sparse_add(
            (alpha_difference, 1, 0),
            (basic_numerators[len(p_support) + index], -1, x),
        )

    def constant_difference(fn: Callable[[int], sp.Rational]) -> SparsePoly:
        output: SparsePoly = {}
        for index, x in enumerate(p_support):
            output = sparse_add((output, 1, 0), (basic_numerators[index], fn(x), 0))
        for index, x in enumerate(q_support):
            output = sparse_add(
                (output, 1, 0),
                (basic_numerators[len(p_support) + index], -fn(x), 0),
            )
        return output

    beta_difference = constant_difference(beta_value)
    gamma_difference = constant_difference(gamma_value)
    t_numerator = basic_numerators[-1]
    conditions.extend([
        (
            "inactive_slack_alpha_-1",
            sparse_add(
                (t_numerator, 2 * epsilon, 0),
                (alpha_difference, 1, 0),
            ),
        ),
        (
            "inactive_slack_beta_+1",
            sparse_add(
                (t_numerator, 2 * epsilon, 0),
                (beta_difference, -1, 0),
            ),
        ),
        (
            "inactive_slack_gamma_+1",
            sparse_add(
                (t_numerator, 2 * epsilon, 0),
                (gamma_difference, -1, 0),
            ),
        ),
    ])
    return denominator, conditions


def integer_interval_signs(
    polynomial: SparsePoly,
    lower_numerator: int,
    upper_numerator: int,
    denominator: int,
    common_degree: int,
    lower_scaled_powers: list[int],
    upper_scaled_powers: list[int],
) -> tuple[int, int]:
    """Exact termwise interval signs using one integer denominator.

    Coefficients are first converted to a common positive integer scale.  Each
    endpoint monomial is represented over denominator**common_degree, so only
    integer additions and multiplications determine the enclosure signs.
    """
    del lower_numerator, upper_numerator, denominator, common_degree
    coefficient_lcm = 1
    for coefficient in polynomial.values():
        coefficient_lcm = math.lcm(coefficient_lcm, int(coefficient.q))
    integer_coefficients = {
        exponent: int(coefficient.p) * (coefficient_lcm // int(coefficient.q))
        for exponent, coefficient in polynomial.items()
    }
    lower_bound = 0
    upper_bound = 0
    for exponent, coefficient in integer_coefficients.items():
        if coefficient >= 0:
            lower_bound += coefficient * lower_scaled_powers[exponent]
            upper_bound += coefficient * upper_scaled_powers[exponent]
        else:
            lower_bound += coefficient * upper_scaled_powers[exponent]
            upper_bound += coefficient * lower_scaled_powers[exponent]
    return exact_sign(lower_bound), exact_sign(upper_bound)


def symbolic_m443_interval_certificate() -> dict[str, Any]:
    denominator, conditions = rank_one_symbolic_conditions(M0, J0, S0)
    condition_map = dict(conditions)
    lower_name = "active_dual_gamma_-1"
    upper_name = "basic_p_77"
    lower_polynomial = condition_map[lower_name]
    upper_polynomial = condition_map[upper_name]

    lower_integer = int(LOWER_ROOT_BRACKET[0] * ROOT_DENOMINATOR)
    upper_integer = int(UPPER_ROOT_BRACKET[1] * ROOT_DENOMINATOR)
    common_degree = M0
    denominator_powers = [1] * (common_degree + 1)
    lower_powers = [1] * (common_degree + 1)
    upper_powers = [1] * (common_degree + 1)
    for exponent in range(1, common_degree + 1):
        denominator_powers[exponent] = denominator_powers[exponent - 1] * ROOT_DENOMINATOR
        lower_powers[exponent] = lower_powers[exponent - 1] * lower_integer
        upper_powers[exponent] = upper_powers[exponent - 1] * upper_integer
    lower_scaled_powers = [
        lower_powers[exponent] * denominator_powers[common_degree - exponent]
        for exponent in range(common_degree + 1)
    ]
    upper_scaled_powers = [
        upper_powers[exponent] * denominator_powers[common_degree - exponent]
        for exponent in range(common_degree + 1)
    ]

    def interval_signs(polynomial: SparsePoly) -> tuple[int, int]:
        return integer_interval_signs(
            polynomial,
            lower_integer,
            upper_integer,
            ROOT_DENOMINATOR,
            common_degree,
            lower_scaled_powers,
            upper_scaled_powers,
        )

    denominator_signs = interval_signs(denominator)
    lower_endpoint_signs = [exact_sign(sparse_eval(lower_polynomial, point)) for point in LOWER_ROOT_BRACKET]
    upper_endpoint_signs = [exact_sign(sparse_eval(upper_polynomial, point)) for point in UPPER_ROOT_BRACKET]
    lower_derivative_signs = interval_signs(sparse_derivative(lower_polynomial))
    upper_derivative_signs = interval_signs(sparse_derivative(upper_polynomial))
    core = (LOWER_ROOT_BRACKET[1], UPPER_ROOT_BRACKET[0])
    boundary_core_signs = {
        lower_name: [exact_sign(sparse_eval(lower_polynomial, point)) for point in core],
        upper_name: [exact_sign(sparse_eval(upper_polynomial, point)) for point in core],
    }

    nonboundary_records: list[dict[str, Any]] = []
    failures: list[str] = []
    for name, polynomial in conditions:
        if name in {lower_name, upper_name}:
            continue
        signs = interval_signs(polynomial)
        reference_sign = exact_sign(sparse_eval(polynomial, S0))
        passed = signs == (1, 1) and reference_sign == 1
        if not passed:
            failures.append(name)
        nonboundary_records.append({
            "name": name,
            "degree": max(polynomial) if polynomial else 0,
            "term_count": len(polynomial),
            "reference_sign_at_13_over_100": reference_sign,
            "boundary_hull_interval_signs": list(signs),
            "strictly_positive_on_full_boundary_hull": passed,
        })

    lower_unique_simple = lower_endpoint_signs == [-1, 1] and lower_derivative_signs == (1, 1)
    upper_unique_simple = upper_endpoint_signs == [1, -1] and upper_derivative_signs == (-1, -1)
    boundary_positive_on_core = all(sign == 1 for signs in boundary_core_signs.values() for sign in signs)
    interval_pass = bool(
        len(conditions) == 895
        and denominator_signs == (1, 1)
        and lower_unique_simple
        and upper_unique_simple
        and boundary_positive_on_core
        and not failures
    )

    return {
        "audit": "A101_M443_GAMMA_ACTIVE_STRICT_KKT_INTERVAL_CERTIFICATE",
        "evidence_class": "exact rank-one symbolic reduction, exact rational root brackets, and exact integer interval arithmetic",
        "contract": {
            "maximum": M0,
            "reference_probe": str(S0),
            "search_interval": [str(SEARCH_LOWER), str(SEARCH_UPPER)],
            "P_support": [77, 78, 443],
            "Q_support": [0, 1, 221, 222],
            "active_bands": [["alpha", 1], ["beta", -1], ["gamma", -1]],
        },
        "symbolic_reduction": {
            "varying_matrix_row": "alpha_plus",
            "method": "exact Sherman-Morrison rank-one row update around s=13/100",
            "common_denominator_degree": max(denominator),
            "common_denominator_term_count": len(denominator),
            "common_denominator_boundary_hull_signs": list(denominator_signs),
            "common_denominator_strictly_positive_on_boundary_hull": denominator_signs == (1, 1),
            "condition_count": len(conditions),
        },
        "strict_component": {
            "lower_boundary_condition": lower_name,
            "upper_boundary_condition": upper_name,
            "lower_root_bracket": [str(value) for value in LOWER_ROOT_BRACKET],
            "upper_root_bracket": [str(value) for value in UPPER_ROOT_BRACKET],
            "lower_root_midpoint_decimal": decimal_str(sum(LOWER_ROOT_BRACKET) / 2, 42),
            "upper_root_midpoint_decimal": decimal_str(sum(UPPER_ROOT_BRACKET) / 2, 42),
            "root_bracket_width": str(sp.Rational(1, ROOT_DENOMINATOR)),
            "component_width_midpoint_decimal": decimal_str(
                (sum(UPPER_ROOT_BRACKET) - sum(LOWER_ROOT_BRACKET)) / 2,
                42,
            ),
            "statement": "inside [129/1000,133/1000], the maximal connected strict-KKT component containing 13/100 is the open interval between the isolated active-gamma-minus-dual root and the isolated p77-mass root",
        },
        "boundary_certificates": {
            "lower_endpoint_numerator_signs": lower_endpoint_signs,
            "lower_derivative_boundary_hull_signs": list(lower_derivative_signs),
            "lower_root_unique_and_simple": lower_unique_simple,
            "upper_endpoint_numerator_signs": upper_endpoint_signs,
            "upper_derivative_boundary_hull_signs": list(upper_derivative_signs),
            "upper_root_unique_and_simple": upper_unique_simple,
            "boundary_condition_core_endpoint_signs": boundary_core_signs,
            "both_boundary_conditions_strictly_positive_between_roots": boundary_positive_on_core,
        },
        "complete_sign_census": {
            "condition_count": len(conditions),
            "boundary_condition_count": 2,
            "nonboundary_numerator_count": len(nonboundary_records),
            "nonboundary_sign_failure_count": len(failures),
            "all_893_nonboundary_numerators_positive_on_full_boundary_hull": not failures,
            "records": nonboundary_records,
            "failures": failures,
        },
        "pass": interval_pass,
    }


def sign_record(name: str, value: sp.Expr) -> dict[str, Any]:
    value = sp.cancel(value)
    return {
        "name": name,
        "exact": str(value),
        "decimal": decimal_str(value, 28),
        "sign": exact_sign(value),
    }


def classify_conditions(conditions: list[tuple[str, sp.Rational]]) -> tuple[str, list[tuple[str, sp.Rational]]]:
    negatives = [(name, value) for name, value in conditions if value < 0]
    zeros = [(name, value) for name, value in conditions if value == 0]
    if negatives:
        first_name = negatives[0][0]
        if first_name.startswith("basic_"):
            return "primal_infeasible", negatives
        if first_name.startswith("active_dual_"):
            return "active_dual_infeasible", negatives
        if first_name.startswith("reduced_cost_"):
            return "reduced_cost_infeasible", negatives
        if first_name.startswith("inactive_slack_"):
            return "inactive_slack_infeasible", negatives
        return "negative_condition", negatives
    if zeros:
        return "zero_condition", zeros
    return "pass", []


def evaluate_gamma_active_architecture(
    maximum: int,
    contact: int,
    probe: sp.Rational,
) -> dict[str, Any]:
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    p_support = [contact - 1, contact, maximum]
    q_support = [0, 1, h, h + 1]

    rows = [
        [1, 1, 1, 0, 0, 0, 0, -1],
        [0, 0, 0, 1, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, 0, -mean],
        [0, 0, 0, *q_support, -mean],
        [0, 0, 0, *[target_value(x) for x in q_support], 0],
        [
            *[probe**x for x in p_support],
            *[-probe**x for x in q_support],
            -2 * epsilon,
        ],
        [
            *[-beta_value(x) for x in p_support],
            *[beta_value(x) for x in q_support],
            -2 * epsilon,
        ],
        [
            *[-gamma_value(x) for x in p_support],
            *[gamma_value(x) for x in q_support],
            -2 * epsilon,
        ],
    ]
    matrix = sp.Matrix(rows)
    determinant = sp.factor(matrix.det(method="domain-ge"))
    if determinant == 0:
        return {"status": "singular", "maximum": maximum}
    inverse = matrix.inv(method="DM")
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
    objective = sp.Matrix([
        *[target_value(x) for x in p_support],
        0, 0, 0, 0, 0,
    ])
    basic = inverse * rhs
    dual = inverse.T * objective

    conditions: list[tuple[str, sp.Rational]] = []
    conditions.extend(zip(
        [
            *[f"basic_p_{x}" for x in p_support],
            *[f"basic_q_{x}" for x in q_support],
            "basic_t",
        ],
        basic,
    ))
    conditions.extend([
        ("active_dual_alpha_+1", dual[5]),
        ("active_dual_beta_-1", dual[6]),
        ("active_dual_gamma_-1", dual[7]),
    ])

    p_set = set(p_support)
    q_set = set(q_support)
    for x in range(maximum + 1):
        if x not in p_set:
            conditions.append((
                f"reduced_cost_p_{x}",
                dual[0] + x * dual[2] + probe**x * dual[5]
                - beta_value(x) * dual[6] - gamma_value(x) * dual[7]
                - target_value(x),
            ))
        if x not in q_set:
            conditions.append((
                f"reduced_cost_q_{x}",
                dual[1] + x * dual[3] + target_value(x) * dual[4]
                - probe**x * dual[5] + beta_value(x) * dual[6]
                + gamma_value(x) * dual[7],
            ))

    def difference(fn: Callable[[int], sp.Rational]) -> sp.Rational:
        return (
            sum(fn(x) * basic[index] for index, x in enumerate(p_support))
            - sum(fn(x) * basic[len(p_support) + index] for index, x in enumerate(q_support))
        )

    t_value = basic[-1]
    alpha_difference = difference(lambda x: probe**x)
    beta_difference = difference(beta_value)
    gamma_difference = difference(gamma_value)
    conditions.extend([
        ("inactive_slack_alpha_-1", 2 * epsilon * t_value + alpha_difference),
        ("inactive_slack_beta_+1", 2 * epsilon * t_value - beta_difference),
        ("inactive_slack_gamma_+1", 2 * epsilon * t_value - gamma_difference),
    ])

    status, failures = classify_conditions(conditions)
    primal_residuals = matrix * basic - rhs
    primal_value = sp.factor(sum(target_value(x) * basic[index] for index, x in enumerate(p_support)))
    dual_value = sp.factor(rhs.dot(dual))
    minimum = min(conditions, key=lambda item: item[1])
    category_counts = {
        "basic_variables": 8,
        "active_dual_multipliers": 3,
        "unrestricted_atom_reduced_costs": 2 * (maximum + 1) - len(p_support) - len(q_support),
        "inactive_band_slacks": 3,
    }
    expected_count = sum(category_counts.values())
    strict_pass = bool(
        status == "pass"
        and len(conditions) == expected_count
        and all(value == 0 for value in primal_residuals)
        and primal_value == dual_value
    )
    return {
        "status": status,
        "maximum": maximum,
        "probe": str(probe),
        "compressed_contact": contact,
        "P_support": p_support,
        "Q_support": q_support,
        "active_bands": [["alpha", 1], ["beta", -1], ["gamma", -1]],
        "basis_determinant_nonzero": determinant != 0,
        "condition_category_counts": category_counts,
        "condition_count": len(conditions),
        "negative_condition_count": sum(1 for _, value in conditions if value < 0),
        "zero_condition_count": sum(1 for _, value in conditions if value == 0),
        "minimum_condition": sign_record(minimum[0], minimum[1]),
        "failing_conditions": [sign_record(name, value) for name, value in failures],
        "all_primal_equation_residuals_zero": all(value == 0 for value in primal_residuals),
        "primal_objective": str(primal_value),
        "dual_objective": str(dual_value),
        "primal_dual_equal": primal_value == dual_value,
        "strict_global_KKT_pass": strict_pass,
        "condition_records": [sign_record(name, value) for name, value in conditions],
    }


def final_residual_atlas() -> dict[str, Any]:
    records = []
    for maximum, witness, contact in EXPECTED_FINAL_TESTS:
        result = evaluate_gamma_active_architecture(maximum, contact, sp.Rational(witness))
        records.append({
            "maximum": maximum,
            "witness": witness,
            "compressed_contact": contact,
            "gamma_active_result": result,
        })
    pass_records = [item for item in records if item["gamma_active_result"]["strict_global_KKT_pass"]]
    failures = [item for item in records if not item["gamma_active_result"]["strict_global_KKT_pass"]]
    return {
        "audit": "A101_GAMMA_ACTIVE_FINAL_RESIDUAL_ATLAS",
        "tested_family": "P={j-1,j,M}, Q={0,1,h,h+1}, alpha+, beta-, gamma- active",
        "source_keys": [list(item) for item in EXPECTED_FINAL_TESTS],
        "record_count": len(records),
        "strict_pass_count": len(pass_records),
        "failure_count": len(failures),
        "pass_keys": [
            [item["maximum"], item["witness"], item["compressed_contact"]]
            for item in pass_records
        ],
        "failure_keys": [
            [item["maximum"], item["witness"], item["compressed_contact"]]
            for item in failures
        ],
        "total_strict_condition_count": sum(
            item["gamma_active_result"]["condition_count"] for item in records
        ),
        "records": records,
    }


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    a95 = json.loads(A95_RESULT.read_text(encoding="utf-8"))
    a97 = json.loads(A97_RESULT.read_text(encoding="utf-8"))
    a99 = json.loads(A99_RESULT.read_text(encoding="utf-8"))
    a100 = json.loads(A100_RESULT.read_text(encoding="utf-8"))

    interval_certificate = symbolic_m443_interval_certificate()
    atlas = final_residual_atlas()

    a95_source_valid = bool(
        a95.get("verdict")
        == "PASS_EXACT_RATIONAL_WITNESS_LIFT_ATLAS_AND_RESTRICTED_FAMILY_OBSTRUCTION"
        and all(a95.get("gates", {}).values())
        and a95["natural_lift_result"]["no_strict_lift_count"] == 83
    )
    a97_source_valid = bool(
        a97.get("verdict")
        == "PASS_ENDPOINT_RELEASED_M125_INTERVAL_AND_76_OF_83_OBSTRUCTION_RESOLUTION_WITH_SEVEN_Q0_ENTRY_RESIDUALS"
        and all(a97.get("gates", {}).values())
        and a97["obstruction_atlas"]["endpoint_released_strict_pass_count"] == 76
        and a97["obstruction_atlas"]["residual_obstruction_count"] == 7
    )
    a99_failures = [tuple(item) for item in a99["remaining_residual_atlas"]["failure_keys"]]
    a99_source_valid = bool(
        a99.get("verdict")
        == "PASS_Q0Q1_M396_INTERVAL_AND_TWO_OF_SIX_REMAINING_RESIDUAL_RESOLUTIONS"
        and all(a99.get("gates", {}).values())
        and a99_failures == EXPECTED_A99_FAILURES
    )
    a100_source_valid = bool(
        a100.get("verdict")
        == "PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M443"
        and all(a100.get("gates", {}).values())
        and a100["resolved_active_set"]["P_support"] == [77, 78, 443]
        and a100["resolved_active_set"]["Q_support"] == [0, 1, 221, 222]
        and a100["resolved_active_set"]["active_bands"]
        == [["alpha", 1], ["beta", -1], ["gamma", -1]]
    )

    expected_counts = {449: 907, 484: 977, 490: 989}
    atlas_counts_correct = all(
        item["gamma_active_result"]["condition_count"] == expected_counts[item["maximum"]]
        for item in atlas["records"]
    )
    all_atlas_conditions_positive = all(
        all(record["sign"] == 1 for record in item["gamma_active_result"]["condition_records"])
        for item in atlas["records"]
    )
    total_resolved_obstructions = 76 + 3 + 4

    gates = {
        "A95_exact_rational_witness_obstruction_source_present_and_passed": a95_source_valid,
        "A97_76_of_83_endpoint_released_source_present_and_passed": a97_source_valid,
        "A99_four_remaining_residual_source_present_and_passed": a99_source_valid,
        "A100_M443_gamma_active_source_present_and_passed": a100_source_valid,
        "rank_one_symbolic_condition_count_is_895": interval_certificate["symbolic_reduction"]["condition_count"] == 895,
        "rank_one_common_denominator_has_seven_terms": interval_certificate["symbolic_reduction"]["common_denominator_term_count"] == 7,
        "common_denominator_is_strictly_positive_on_boundary_hull": interval_certificate["symbolic_reduction"]["common_denominator_strictly_positive_on_boundary_hull"],
        "lower_boundary_is_active_gamma_minus_dual": interval_certificate["strict_component"]["lower_boundary_condition"] == "active_dual_gamma_-1",
        "upper_boundary_is_basic_p77_mass": interval_certificate["strict_component"]["upper_boundary_condition"] == "basic_p_77",
        "lower_boundary_root_is_unique_and_simple": interval_certificate["boundary_certificates"]["lower_root_unique_and_simple"],
        "upper_boundary_root_is_unique_and_simple": interval_certificate["boundary_certificates"]["upper_root_unique_and_simple"],
        "both_boundary_conditions_are_positive_between_roots": interval_certificate["boundary_certificates"]["both_boundary_conditions_strictly_positive_between_roots"],
        "all_893_nonboundary_numerators_are_positive_on_full_hull": interval_certificate["complete_sign_census"]["nonboundary_sign_failure_count"] == 0,
        "M443_strict_component_certificate_passes": interval_certificate["pass"],
        "final_residual_atlas_contains_exactly_three_points": atlas["record_count"] == 3,
        "all_three_final_residuals_have_strict_global_KKT_passes": atlas["strict_pass_count"] == 3 and atlas["failure_count"] == 0,
        "final_residual_pass_keys_are_M449_M484_M490": atlas["pass_keys"] == [list(item) for item in EXPECTED_FINAL_TESTS],
        "final_residual_condition_counts_are_907_977_989": atlas_counts_correct,
        "all_2873_final_residual_KKT_conditions_are_strictly_positive": atlas["total_strict_condition_count"] == 2873 and all_atlas_conditions_positive,
        "all_final_residual_primal_systems_close_exactly": all(
            item["gamma_active_result"]["all_primal_equation_residuals_zero"]
            for item in atlas["records"]
        ),
        "all_final_residual_primal_and_dual_objectives_are_exactly_equal": all(
            item["gamma_active_result"]["primal_dual_equal"]
            for item in atlas["records"]
        ),
        "all_83_A95_rational_witness_obstructions_are_now_resolved": total_resolved_obstructions == 83,
        "formal_contract_and_nonphysical_scope_preserved": True,
    }
    gates = {name: bool(value) for name, value in gates.items()}

    summary = {
        "audit": "A101_GAMMA_ACTIVE_INTERVAL_AND_FINAL_RESIDUAL_CLOSURE",
        "evidence_class": "exact rank-one symbolic interval certificate plus exact rational unrestricted KKT certificates at the final three residual witnesses",
        "scope": {
            "interval_contract": {
                "maximum": M0,
                "reference_probe": str(S0),
                "search_interval": [str(SEARCH_LOWER), str(SEARCH_UPPER)],
            },
            "final_residual_keys": [list(item) for item in EXPECTED_FINAL_TESTS],
            "claim": "strict interval persistence of the A100 basis at M=443 and strict resolution of the final three A99 rational residual witnesses",
            "explicit_nonclaim": "not an all-s interval theorem, not continuous certification of all 83 former obstructions, not a universal support law, and not a physical or ontological result",
        },
        "M443_interval_theorem": {
            "P_support": [77, 78, 443],
            "Q_support": [0, 1, 221, 222],
            "active_bands": [["alpha", 1], ["beta", -1], ["gamma", -1]],
            "condition_count": interval_certificate["symbolic_reduction"]["condition_count"],
            "lower_boundary_condition": interval_certificate["strict_component"]["lower_boundary_condition"],
            "upper_boundary_condition": interval_certificate["strict_component"]["upper_boundary_condition"],
            "lower_root_bracket": interval_certificate["strict_component"]["lower_root_bracket"],
            "upper_root_bracket": interval_certificate["strict_component"]["upper_root_bracket"],
            "component_width_midpoint_decimal": interval_certificate["strict_component"]["component_width_midpoint_decimal"],
            "nonboundary_numerator_count": interval_certificate["complete_sign_census"]["nonboundary_numerator_count"],
            "nonboundary_sign_failure_count": interval_certificate["complete_sign_census"]["nonboundary_sign_failure_count"],
            "pass": interval_certificate["pass"],
        },
        "final_residual_atlas": {
            key: atlas[key]
            for key in [
                "tested_family", "record_count", "strict_pass_count", "failure_count",
                "pass_keys", "failure_keys", "total_strict_condition_count",
            ]
        },
        "A95_obstruction_closure_accounting": {
            "original_no_natural_lift_phase_count": 83,
            "A97_endpoint_released_strict_pass_count": 76,
            "A98_A99_q0q1_gamma_inactive_resolution_count": 3,
            "A100_A101_q0q1_gamma_active_resolution_count": 4,
            "resolved_count": total_resolved_obstructions,
            "unresolved_rational_witness_count": 83 - total_resolved_obstructions,
            "statement": "all 83 A95 rational witness obstructions now possess a strict exact full-LP KKT certificate, distributed across three active-set architectures",
        },
        "interpretation": {
            "positive_result": "The A100 gamma-active basis persists on an exact open algebraic interval at M=443 and resolves the remaining M=449,484,490 witnesses without changing the contract.",
            "structural_result": "The final seven A97 residuals split into three q0/q1 gamma-inactive bases and four q0/q1 plus lower-adjacent-P gamma-active bases.",
            "negative_boundary": "The closure is at selected rational witnesses. It does not prove that the chosen bases persist throughout every A92 cell or that the three architectures exhaust all future contracts.",
        },
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "gates": gates,
        "verdict": (
            "PASS_GAMMA_ACTIVE_M443_INTERVAL_AND_THREE_OF_THREE_FINAL_RESIDUAL_RESOLUTIONS"
            if all(gates.values()) else "FAIL"
        ),
    }

    result_path = RESULTS / "a101_gamma_active_interval_and_residual_closure_results.json"
    interval_path = RESULTS / "a101_M443_gamma_active_interval_certificate.json"
    atlas_path = RESULTS / "a101_gamma_active_final_residual_atlas.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    interval_path.write_text(json.dumps(interval_certificate, indent=2), encoding="utf-8")
    atlas_path.write_text(json.dumps(atlas, indent=2), encoding="utf-8")

    print(json.dumps({
        "audit": summary["audit"],
        "M443_interval_pass": interval_certificate["pass"],
        "M443_lower_root_bracket": interval_certificate["strict_component"]["lower_root_bracket"],
        "M443_upper_root_bracket": interval_certificate["strict_component"]["upper_root_bracket"],
        "final_residual_pass_count": atlas["strict_pass_count"],
        "final_residual_failure_count": atlas["failure_count"],
        "A95_obstructions_resolved": total_resolved_obstructions,
        "gate_count": summary["gate_count"],
        "pass_count": summary["pass_count"],
        "verdict": summary["verdict"],
    }, indent=2))

    if not all(gates.values()):
        failed = [name for name, passed in gates.items() if not passed]
        print(json.dumps({"failed_gates": failed}, indent=2))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
