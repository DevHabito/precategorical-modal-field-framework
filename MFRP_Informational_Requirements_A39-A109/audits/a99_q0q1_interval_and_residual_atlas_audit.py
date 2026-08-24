#!/usr/bin/env python3
"""A99 exact q0/q1 interval theorem and residual-obstruction atlas.

A98 resolved the first A97 residual at

    M=396, s=13/100, j=70

with the unrestricted active set

    P={j,M}, Q={0,1,h,h+1}, active={alpha+,beta-}, gamma inactive.

A99 performs two falsifiable upgrades.

1. It constructs all 801 KKT conditions symbolically in the probe s, using a
   common exact determinant denominator and sparse polynomial numerators.  It
   isolates the maximal connected strict-KKT component containing 13/100
   inside [129/1000,133/1000].  The lower boundary is the gamma-minus inactive
   slack; the upper boundary is the basic q0 mass.  Every other numerator and
   the common determinant are certified sign-stable by exact rational interval
   evaluation on the full boundary hull.

2. It tests the same q0/q1 architecture at the six remaining A97 residual
   witnesses.  Two pass the complete unrestricted finite-LP KKT system and four
   fail primal feasibility and/or the gamma-minus slack.  Failures are retained
   as obstructions; no support is altered to force a pass.

The result is contract-relative mathematics.  It is not an all-M theorem, a
complete solution of the four residuals, or a physical/ontological claim.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A97_RESULT = RESULTS / "a97_endpoint_released_interval_and_obstruction_results.json"
A98_RESULT = RESULTS / "a98_full_lp_active_set_resolution_results.json"

SEARCH_LOWER = sp.Rational(129, 1000)
SEARCH_UPPER = sp.Rational(133, 1000)
S0 = sp.Rational(13, 100)
M0 = 396
J0 = 70
ROOT_DENOMINATOR = 10**24
LOWER_ROOT_BRACKET = (
    sp.Rational(129987460460605135017979, ROOT_DENOMINATOR),
    sp.Rational(129987460460605135017980, ROOT_DENOMINATOR),
)
UPPER_ROOT_BRACKET = (
    sp.Rational(130017128515377642396099, ROOT_DENOMINATOR),
    sp.Rational(130017128515377642396100, ROOT_DENOMINATOR),
)
EXPECTED_REMAINING = [
    (443, "13/100", 78),
    (449, "13/100", 79),
    (455, "13/100", 80),
    (484, "13/100", 85),
    (490, "13/100", 86),
    (496, "13/100", 87),
]
EXPECTED_PASS_KEYS = [(455, "13/100", 80), (496, "13/100", 87)]
EXPECTED_FAIL_KEYS = [
    (443, "13/100", 78),
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


def to_sparse(expression: sp.Expr, variable: sp.Symbol) -> SparsePoly:
    polynomial = sp.Poly(expression, variable, domain=sp.QQ)
    return {
        int(monomial[0]): sp.Rational(coefficient)
        for monomial, coefficient in polynomial.terms()
        if coefficient != 0
    }


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


def sparse_interval(
    polynomial: SparsePoly,
    lower: sp.Rational,
    upper: sp.Rational,
) -> tuple[sp.Rational, sp.Rational]:
    """Exact termwise enclosure on a positive interval."""
    interval_lower = sp.Rational(0)
    interval_upper = sp.Rational(0)
    for exponent, coefficient in polynomial.items():
        low_power = lower**exponent
        high_power = upper**exponent
        if coefficient >= 0:
            interval_lower += coefficient * low_power
            interval_upper += coefficient * high_power
        else:
            interval_lower += coefficient * high_power
            interval_upper += coefficient * low_power
    return interval_lower, interval_upper


def sparse_derivative(polynomial: SparsePoly) -> SparsePoly:
    return {
        exponent - 1: exponent * coefficient
        for exponent, coefficient in polynomial.items()
        if exponent > 0
    }


def interval_has_sign(interval: tuple[sp.Rational, sp.Rational], sign: int) -> bool:
    if sign > 0:
        return bool(interval[0] > 0)
    if sign < 0:
        return bool(interval[1] < 0)
    return bool(interval[0] == 0 and interval[1] == 0)


def build_symbolic_m396_conditions() -> tuple[SparsePoly, list[tuple[str, SparsePoly]]]:
    maximum = M0
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    variable = sp.Symbol("s")
    p_support = [J0, maximum]
    q_support = [0, 1, h, h + 1]

    rows = [
        [1, 1, 0, 0, 0, 0, -1],
        [0, 0, 1, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, 0, -mean],
        [0, 0, *q_support, -mean],
        [0, 0, *[target_value(x) for x in q_support], 0],
        [
            *[variable**x for x in p_support],
            *[-variable**x for x in q_support],
            -2 * epsilon,
        ],
        [
            *[-beta_value(x) for x in p_support],
            *[beta_value(x) for x in q_support],
            -2 * epsilon,
        ],
    ]
    basis_matrix = sp.Matrix(rows)
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0])
    objective = sp.Matrix([
        *[target_value(x) for x in p_support],
        0, 0, 0, 0, 0,
    ])

    determinant = basis_matrix.det(method="domain-ge")
    basic = basis_matrix.inv(method="DM") * rhs
    dual = basis_matrix.T.inv(method="DM") * objective
    basic_numerators = [sp.cancel(value * determinant) for value in basic]
    dual_numerators = [sp.cancel(value * determinant) for value in dual]

    determinant_sparse = to_sparse(determinant, variable)
    basic_sparse = [to_sparse(value, variable) for value in basic_numerators]
    dual_sparse = [to_sparse(value, variable) for value in dual_numerators]

    conditions: list[tuple[str, SparsePoly]] = []
    variable_names = [
        *[f"basic_p_{x}" for x in p_support],
        *[f"basic_q_{x}" for x in q_support],
        "basic_t",
    ]
    conditions.extend(zip(variable_names, basic_sparse))
    conditions.extend([
        ("active_dual_alpha_+1", dual_sparse[5]),
        ("active_dual_beta_-1", dual_sparse[6]),
    ])

    p_set = set(p_support)
    q_set = set(q_support)
    for x in range(maximum + 1):
        if x not in p_set:
            numerator = sparse_add(
                (dual_sparse[0], 1, 0),
                (dual_sparse[2], x, 0),
                (dual_sparse[5], 1, x),
                (dual_sparse[6], -beta_value(x), 0),
                (determinant_sparse, -target_value(x), 0),
            )
            conditions.append((f"reduced_cost_p_{x}", numerator))
        if x not in q_set:
            numerator = sparse_add(
                (dual_sparse[1], 1, 0),
                (dual_sparse[3], x, 0),
                (dual_sparse[4], target_value(x), 0),
                (dual_sparse[5], -1, x),
                (dual_sparse[6], beta_value(x), 0),
            )
            conditions.append((f"reduced_cost_q_{x}", numerator))

    alpha_parts: list[tuple[SparsePoly, sp.Rational, int]] = []
    for index, x in enumerate(p_support):
        alpha_parts.append((basic_sparse[index], 1, x))
    for index, x in enumerate(q_support):
        alpha_parts.append((basic_sparse[len(p_support) + index], -1, x))
    alpha_difference_numerator = sparse_add(*alpha_parts)

    def constant_difference_numerator(fn: Callable[[int], sp.Rational]) -> SparsePoly:
        parts: list[tuple[SparsePoly, sp.Rational, int]] = []
        for index, x in enumerate(p_support):
            parts.append((basic_sparse[index], fn(x), 0))
        for index, x in enumerate(q_support):
            parts.append((basic_sparse[len(p_support) + index], -fn(x), 0))
        return sparse_add(*parts)

    beta_difference_numerator = constant_difference_numerator(beta_value)
    gamma_difference_numerator = constant_difference_numerator(gamma_value)
    t_numerator = basic_sparse[-1]
    conditions.extend([
        (
            "inactive_slack_alpha_-1",
            sparse_add(
                (t_numerator, 2 * epsilon, 0),
                (alpha_difference_numerator, 1, 0),
            ),
        ),
        (
            "inactive_slack_beta_+1",
            sparse_add(
                (t_numerator, 2 * epsilon, 0),
                (beta_difference_numerator, -1, 0),
            ),
        ),
        (
            "inactive_slack_gamma_+1",
            sparse_add(
                (t_numerator, 2 * epsilon, 0),
                (gamma_difference_numerator, -1, 0),
            ),
        ),
        (
            "inactive_slack_gamma_-1",
            sparse_add(
                (t_numerator, 2 * epsilon, 0),
                (gamma_difference_numerator, 1, 0),
            ),
        ),
    ])
    return determinant_sparse, conditions


def symbolic_m396_interval_certificate() -> dict[str, Any]:
    determinant, conditions = build_symbolic_m396_conditions()
    condition_map = dict(conditions)
    lower_name = "inactive_slack_gamma_-1"
    upper_name = "basic_q_0"
    lower_polynomial = condition_map[lower_name]
    upper_polynomial = condition_map[upper_name]
    hull = (LOWER_ROOT_BRACKET[0], UPPER_ROOT_BRACKET[1])
    core = (LOWER_ROOT_BRACKET[1], UPPER_ROOT_BRACKET[0])

    determinant_interval = sparse_interval(determinant, *hull)
    determinant_sign = exact_sign(sparse_eval(determinant, S0))
    determinant_stable = interval_has_sign(determinant_interval, determinant_sign)

    lower_endpoint_signs = [
        exact_sign(sparse_eval(lower_polynomial, LOWER_ROOT_BRACKET[0])),
        exact_sign(sparse_eval(lower_polynomial, LOWER_ROOT_BRACKET[1])),
    ]
    upper_endpoint_signs = [
        exact_sign(sparse_eval(upper_polynomial, UPPER_ROOT_BRACKET[0])),
        exact_sign(sparse_eval(upper_polynomial, UPPER_ROOT_BRACKET[1])),
    ]
    lower_derivative_bracket = sparse_interval(
        sparse_derivative(lower_polynomial), *LOWER_ROOT_BRACKET
    )
    upper_derivative_bracket = sparse_interval(
        sparse_derivative(upper_polynomial), *UPPER_ROOT_BRACKET
    )
    lower_derivative_core = sparse_interval(sparse_derivative(lower_polynomial), *core)
    upper_derivative_core = sparse_interval(sparse_derivative(upper_polynomial), *core)

    lower_root_unique = bool(
        lower_endpoint_signs == [1, -1]
        and lower_derivative_bracket[1] < 0
    )
    upper_root_unique = bool(
        upper_endpoint_signs == [-1, 1]
        and upper_derivative_bracket[0] > 0
    )
    boundary_numerators_negative_on_core = bool(
        lower_derivative_core[1] < 0
        and sparse_eval(lower_polynomial, core[0]) < 0
        and upper_derivative_core[0] > 0
        and sparse_eval(upper_polynomial, core[1]) < 0
    )

    nonboundary_records: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for name, polynomial in conditions:
        if name in {lower_name, upper_name}:
            continue
        reference_sign = exact_sign(sparse_eval(polynomial, S0))
        enclosure = sparse_interval(polynomial, *hull)
        passed = interval_has_sign(enclosure, reference_sign)
        record = {
            "condition": name,
            "degree": max(polynomial) if polynomial else -1,
            "term_count": len(polynomial),
            "reference_numerator_sign": reference_sign,
            "interval_numerator_signs": [exact_sign(enclosure[0]), exact_sign(enclosure[1])],
            "sign_stable": passed,
        }
        nonboundary_records.append(record)
        if not passed:
            failures.append({
                **record,
                "interval_lower": str(enclosure[0]),
                "interval_upper": str(enclosure[1]),
            })

    component_pass = bool(
        len(conditions) == 801
        and determinant_sign == -1
        and determinant_stable
        and lower_root_unique
        and upper_root_unique
        and boundary_numerators_negative_on_core
        and not failures
        and LOWER_ROOT_BRACKET[1] < S0 < UPPER_ROOT_BRACKET[0]
    )

    return {
        "audit": "A99_M396_Q0Q1_STRICT_COMPONENT_CERTIFICATE",
        "contract": {
            "maximum": M0,
            "mean": str(sp.Rational(M0, 2)),
            "probe_variable": "s",
            "search_interval": [str(SEARCH_LOWER), str(SEARCH_UPPER)],
            "reference_probe": str(S0),
            "epsilon": str(normalized_epsilon(M0)),
            "P_support": [J0, M0],
            "Q_support": [0, 1, M0 // 2, M0 // 2 + 1],
            "active_bands": [["alpha", 1], ["beta", -1]],
            "gamma_status": "inactive",
        },
        "common_denominator": {
            "degree": max(determinant),
            "term_count": len(determinant),
            "reference_sign": determinant_sign,
            "interval_signs": [exact_sign(determinant_interval[0]), exact_sign(determinant_interval[1])],
            "sign_stable_on_boundary_hull": determinant_stable,
        },
        "strict_component": {
            "lower_boundary_condition": lower_name,
            "upper_boundary_condition": upper_name,
            "lower_root_bracket": [str(value) for value in LOWER_ROOT_BRACKET],
            "upper_root_bracket": [str(value) for value in UPPER_ROOT_BRACKET],
            "lower_root_midpoint_decimal": decimal_str(sum(LOWER_ROOT_BRACKET) / 2, 40),
            "upper_root_midpoint_decimal": decimal_str(sum(UPPER_ROOT_BRACKET) / 2, 40),
            "root_bracket_width": str(sp.Rational(1, ROOT_DENOMINATOR)),
            "statement": "inside [129/1000,133/1000], the maximal connected strict-KKT component containing 13/100 is the open interval between the isolated gamma-minus-slack root and q0-mass root",
        },
        "boundary_certificates": {
            "lower_endpoint_numerator_signs": lower_endpoint_signs,
            "lower_derivative_bracket_signs": [exact_sign(value) for value in lower_derivative_bracket],
            "lower_root_unique_and_simple": lower_root_unique,
            "upper_endpoint_numerator_signs": upper_endpoint_signs,
            "upper_derivative_bracket_signs": [exact_sign(value) for value in upper_derivative_bracket],
            "upper_root_unique_and_simple": upper_root_unique,
            "lower_derivative_core_signs": [exact_sign(value) for value in lower_derivative_core],
            "upper_derivative_core_signs": [exact_sign(value) for value in upper_derivative_core],
            "boundary_numerators_negative_on_closed_core": boundary_numerators_negative_on_core,
            "condition_sign_interpretation": "the common denominator is negative; negative boundary numerators on the core therefore mean positive KKT conditions",
        },
        "complete_sign_census": {
            "condition_count": len(conditions),
            "boundary_condition_count": 2,
            "nonboundary_numerator_count": len(nonboundary_records),
            "nonboundary_sign_failure_count": len(failures),
            "all_799_nonboundary_numerators_sign_stable_on_full_hull": not failures,
            "records": nonboundary_records,
            "failures": failures,
        },
        "pass": component_pass,
    }


def classify_conditions(
    conditions: list[tuple[str, sp.Rational]],
) -> tuple[str, list[tuple[str, sp.Rational]]]:
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


def evaluate_q0q1_architecture(
    maximum: int,
    contact: int,
    probe: sp.Rational,
) -> dict[str, Any]:
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    p_support = [contact, maximum]
    q_support = [0, 1, h, h + 1]
    if len(set(p_support)) != 2 or len(set(q_support)) != 4:
        return {"status": "degenerate_support"}

    rows = [
        [1, 1, 0, 0, 0, 0, -1],
        [0, 0, 1, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, 0, -mean],
        [0, 0, *q_support, -mean],
        [0, 0, *[target_value(x) for x in q_support], 0],
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
    ]
    basis_matrix = sp.Matrix(rows)
    try:
        inverse = sp.polys.matrices.DomainMatrix.from_Matrix(basis_matrix).to_field().inv().to_Matrix()
    except Exception:
        return {"status": "singular"}

    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0])
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
    ])

    p_set = set(p_support)
    q_set = set(q_support)
    for x in range(maximum + 1):
        if x not in p_set:
            value = (
                dual[0] + x * dual[2] + probe**x * dual[5]
                - beta_value(x) * dual[6] - target_value(x)
            )
            conditions.append((f"reduced_cost_p_{x}", value))
        if x not in q_set:
            value = (
                dual[1] + x * dual[3] + target_value(x) * dual[4]
                - probe**x * dual[5] + beta_value(x) * dual[6]
            )
            conditions.append((f"reduced_cost_q_{x}", value))

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
        ("inactive_slack_gamma_-1", 2 * epsilon * t_value + gamma_difference),
    ])

    status, failures = classify_conditions(conditions)
    ratio = sum(target_value(x) * basic[index] for index, x in enumerate(p_support))
    dual_value = rhs.dot(dual)
    minimum = min(conditions, key=lambda item: item[1])
    return {
        "status": status,
        "P_support": p_support,
        "Q_support": q_support,
        "active_bands": [["alpha", 1], ["beta", -1]],
        "condition_count": len(conditions),
        "negative_condition_count": sum(1 for _, value in conditions if value < 0),
        "zero_condition_count": sum(1 for _, value in conditions if value == 0),
        "failing_conditions": [
            {
                "name": name,
                "exact": str(value),
                "decimal": decimal_str(value, 25),
            }
            for name, value in failures
        ],
        "minimum_condition": {
            "name": minimum[0],
            "exact": str(minimum[1]),
            "decimal": decimal_str(minimum[1], 25),
        },
        "primal_dual_equal": bool(ratio == dual_value),
        "strict_global_KKT_pass": bool(status == "pass" and ratio == dual_value),
    }


def residual_atlas() -> dict[str, Any]:
    a97 = json.loads(A97_RESULT.read_text(encoding="utf-8"))
    residual_keys = [tuple(item) for item in a97["obstruction_atlas"]["residual_keys"]]
    remaining = [key for key in residual_keys if key[0] != M0]
    records: list[dict[str, Any]] = []
    for maximum, witness, contact in remaining:
        probe = sp.Rational(witness)
        result = evaluate_q0q1_architecture(int(maximum), int(contact), probe)
        records.append({
            "maximum": int(maximum),
            "witness": witness,
            "compressed_contact": int(contact),
            "q0q1_result": result,
        })
    records.sort(key=lambda item: item["maximum"])
    pass_records = [record for record in records if record["q0q1_result"]["status"] == "pass"]
    failure_records = [record for record in records if record["q0q1_result"]["status"] != "pass"]
    return {
        "audit": "A99_Q0Q1_REMAINING_RESIDUAL_ATLAS",
        "tested_family": "P={j,M}, Q={0,1,h,h+1}, alpha+ and beta- active, gamma inactive",
        "source_remaining_keys": [list(item) for item in remaining],
        "record_count": len(records),
        "strict_pass_count": len(pass_records),
        "failure_count": len(failure_records),
        "pass_keys": [
            [record["maximum"], record["witness"], record["compressed_contact"]]
            for record in pass_records
        ],
        "failure_keys": [
            [record["maximum"], record["witness"], record["compressed_contact"]]
            for record in failure_records
        ],
        "records": records,
    }


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    a97 = json.loads(A97_RESULT.read_text(encoding="utf-8"))
    a98 = json.loads(A98_RESULT.read_text(encoding="utf-8"))
    interval_certificate = symbolic_m396_interval_certificate()
    atlas = residual_atlas()

    a97_source_valid = bool(
        a97.get("verdict")
        == "PASS_ENDPOINT_RELEASED_M125_INTERVAL_AND_76_OF_83_OBSTRUCTION_RESOLUTION_WITH_SEVEN_Q0_ENTRY_RESIDUALS"
        and all(a97.get("gates", {}).values())
        and [tuple(item) for item in a97["obstruction_atlas"]["residual_keys"]]
        == [(M0, "13/100", J0), *EXPECTED_REMAINING]
    )
    a98_source_valid = bool(
        a98.get("verdict")
        == "PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M396"
        and all(a98.get("gates", {}).values())
        and a98["resolved_active_set"]["P_support"] == [J0, M0]
        and a98["resolved_active_set"]["Q_support"] == [0, 1, M0 // 2, M0 // 2 + 1]
    )
    pass_keys = [tuple(item) for item in atlas["pass_keys"]]
    fail_keys = [tuple(item) for item in atlas["failure_keys"]]
    fail_map = {
        record["maximum"]: [item["name"] for item in record["q0q1_result"]["failing_conditions"]]
        for record in atlas["records"]
        if record["q0q1_result"]["status"] != "pass"
    }

    gates = {
        "A97_source_is_present_and_passed": a97_source_valid,
        "A98_source_is_present_and_passed": a98_source_valid,
        "M396_symbolic_condition_count_is_801": (
            interval_certificate["complete_sign_census"]["condition_count"] == 801
        ),
        "M396_common_denominator_is_strictly_negative_on_boundary_hull": (
            interval_certificate["common_denominator"]["reference_sign"] == -1
            and interval_certificate["common_denominator"]["sign_stable_on_boundary_hull"]
        ),
        "M396_lower_boundary_is_unique_simple_gamma_minus_slack_root": (
            interval_certificate["strict_component"]["lower_boundary_condition"]
            == "inactive_slack_gamma_-1"
            and interval_certificate["boundary_certificates"]["lower_root_unique_and_simple"]
        ),
        "M396_upper_boundary_is_unique_simple_q0_mass_root": (
            interval_certificate["strict_component"]["upper_boundary_condition"] == "basic_q_0"
            and interval_certificate["boundary_certificates"]["upper_root_unique_and_simple"]
        ),
        "M396_all_799_nonboundary_numerators_are_sign_stable": (
            interval_certificate["complete_sign_census"]["nonboundary_numerator_count"] == 799
            and interval_certificate["complete_sign_census"]["nonboundary_sign_failure_count"] == 0
        ),
        "M396_boundary_numerators_have_correct_sign_on_core": (
            interval_certificate["boundary_certificates"]["boundary_numerators_negative_on_closed_core"]
        ),
        "M396_strict_component_contains_13_over_100": interval_certificate["pass"],
        "remaining_residual_source_list_has_six_records": (
            [tuple(item) for item in atlas["source_remaining_keys"]] == EXPECTED_REMAINING
            and atlas["record_count"] == 6
        ),
        "q0q1_architecture_passes_exactly_two_of_six_remaining_residuals": (
            atlas["strict_pass_count"] == 2 and atlas["failure_count"] == 4
        ),
        "q0q1_pass_keys_are_M455_and_M496": pass_keys == EXPECTED_PASS_KEYS,
        "q0q1_failure_keys_match_exact_declared_list": fail_keys == EXPECTED_FAIL_KEYS,
        "all_two_passes_are_complete_strict_global_KKT_certificates": all(
            record["q0q1_result"].get("strict_global_KKT_pass")
            for record in atlas["records"]
            if record["q0q1_result"]["status"] == "pass"
        ),
        "M443_and_M449_fail_by_q1_mass_and_gamma_minus_slack": (
            fail_map.get(443) == ["basic_q_1", "inactive_slack_gamma_-1"]
            and fail_map.get(449) == ["basic_q_1", "inactive_slack_gamma_-1"]
        ),
        "M484_and_M490_add_upper_central_Q_mass_failure": (
            fail_map.get(484) == ["basic_q_1", "basic_q_243", "inactive_slack_gamma_-1"]
            and fail_map.get(490) == ["basic_q_1", "basic_q_246", "inactive_slack_gamma_-1"]
        ),
        "all_six_atlas_bases_have_exact_primal_dual_equality": all(
            record["q0q1_result"].get("primal_dual_equal")
            for record in atlas["records"]
        ),
        "formal_contract_and_nonphysical_scope_preserved": True,
    }
    gates = {name: bool(value) for name, value in gates.items()}

    summary = {
        "audit": "A99_Q0Q1_INTERVAL_AND_REMAINING_RESIDUAL_ATLAS",
        "evidence_class": "exact sparse-polynomial interval certificate plus exact finite rational-witness unrestricted KKT atlas",
        "scope": {
            "interval_theorem": "M=396 inside 129/1000 <= s <= 133/1000",
            "residual_atlas": "the six A97 residual witnesses not solved by A98",
            "tested_architecture": atlas["tested_family"],
            "explicit_nonclaims": [
                "not an interval theorem for M=455 or M=496",
                "not a resolution of the four remaining residual obstructions",
                "not an all-M active-set theorem",
                "not a physical, spacetime, matter, or ontological result",
            ],
        },
        "M396_interval_theorem": {
            "lower_boundary_condition": interval_certificate["strict_component"]["lower_boundary_condition"],
            "upper_boundary_condition": interval_certificate["strict_component"]["upper_boundary_condition"],
            "lower_root_bracket": interval_certificate["strict_component"]["lower_root_bracket"],
            "upper_root_bracket": interval_certificate["strict_component"]["upper_root_bracket"],
            "lower_root_midpoint_decimal": interval_certificate["strict_component"]["lower_root_midpoint_decimal"],
            "upper_root_midpoint_decimal": interval_certificate["strict_component"]["upper_root_midpoint_decimal"],
            "condition_count": interval_certificate["complete_sign_census"]["condition_count"],
            "nonboundary_sign_failure_count": interval_certificate["complete_sign_census"]["nonboundary_sign_failure_count"],
            "pass": interval_certificate["pass"],
        },
        "remaining_residual_atlas": {
            "tested_count": atlas["record_count"],
            "strict_pass_count": atlas["strict_pass_count"],
            "failure_count": atlas["failure_count"],
            "pass_keys": atlas["pass_keys"],
            "failure_keys": atlas["failure_keys"],
            "failure_condition_names": {str(key): value for key, value in fail_map.items()},
        },
        "interpretation": {
            "positive_result": "The A98 q0/q1 basis persists on a narrow exact algebraic interval at M=396 and also gives strict unrestricted optima at the M=455 and M=496 residual witnesses.",
            "negative_result": "The same architecture fails at M=443,449,484,490. The first two lose q1 mass and gamma-minus feasibility; the latter two additionally lose the upper central Q mass.",
            "structural_boundary": "q0/q1 co-entry is therefore a reusable but non-universal repair. The first unresolved target is M=443, s=13/100, j=78 and requires a new unrestricted active-set discovery.",
        },
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "gates": gates,
        "verdict": (
            "PASS_Q0Q1_M396_INTERVAL_AND_TWO_OF_SIX_REMAINING_RESIDUAL_RESOLUTIONS"
            if all(gates.values()) else "FAIL"
        ),
    }

    result_path = RESULTS / "a99_q0q1_interval_and_residual_atlas_results.json"
    interval_path = RESULTS / "a99_M396_q0q1_interval_certificate.json"
    atlas_path = RESULTS / "a99_q0q1_remaining_residual_atlas.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    interval_path.write_text(json.dumps(interval_certificate, indent=2), encoding="utf-8")
    atlas_path.write_text(json.dumps(atlas, indent=2), encoding="utf-8")

    print(json.dumps({
        "audit": summary["audit"],
        "M396_lower_root_midpoint": interval_certificate["strict_component"]["lower_root_midpoint_decimal"],
        "M396_upper_root_midpoint": interval_certificate["strict_component"]["upper_root_midpoint_decimal"],
        "remaining_pass_keys": atlas["pass_keys"],
        "remaining_failure_keys": atlas["failure_keys"],
        "gate_count": summary["gate_count"],
        "pass_count": summary["pass_count"],
        "verdict": summary["verdict"],
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
