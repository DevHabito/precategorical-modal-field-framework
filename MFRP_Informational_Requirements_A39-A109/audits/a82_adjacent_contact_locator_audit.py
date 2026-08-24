#!/usr/bin/env python3
"""A82 exact adjacent-contact locator and local orientation-switch audit.

A78 found the exact LP optimum at the rational probe s0=131/1000 by
exhaustively testing 9,230 candidate bases. A81 reduced every gamma-inactive
compressed contact family

    C(M,k): P={0,k,M}, Q={1,h,h+1}, active={alpha+,beta-}

to a two-variable system. A82 uses that reduction to ask whether the full
A78 selection can be recovered from a one-dimensional adjacent-contact
comparison rather than an exhaustive basis catalogue.

For each compressed family let V(M,k;s) be its target ratio and z(M,k;s)>0
its interior P mass. For adjacent contacts define

    D(M,k;s) = V(M,k+1;s) - V(M,k;s).

The simplex basis-exchange identity gives the cross reduced costs

    rho_forward  = -D/z(M,k+1),
    rho_backward =  D/z(M,k),

and hence rho_backward/rho_forward = -z(M,k+1)/z(M,k). Thus one exact sign
locates which of two adjacent compressed bases has the larger objective.

The main theorem is exact at s=s0 for 10<=M<=80. A secondary local scan on
I=[129/1000,133/1000] records endpoint-crossing candidates and certifies one
simple algebraic orientation-switch root for each candidate. It does *not*
claim a complete root atlas for all same-endpoint-sign polynomials.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A78_SCRIPT = HERE / "a78_rational_probe_contact_selection_audit.py"
A80_SCRIPT = HERE / "a80_local_compression_window_atlas_audit.py"
A81_SCRIPT = HERE / "a81_reduced_boundary_system_audit.py"
A78_RESULT = RESULTS / "a78_rational_probe_contact_selection_results.json"

S = sp.Symbol("s")
S0 = sp.Rational(131, 1000)
LOCAL_LOWER = sp.Rational(129, 1000)
LOCAL_UPPER = sp.Rational(133, 1000)
M_MIN = 10
M_MAX = 80
BISECTION_STEPS = 100
DIRECT_PIVOT_WITNESSES = (
    (10, 2),
    (13, 3),
    (28, 6),
    (40, 8),
    (57, 11),
    (64, 12),
    (79, 15),
    (80, 15),
)


@dataclass(frozen=True)
class RootBracket:
    lower: sp.Rational
    upper: sp.Rational

    @property
    def midpoint(self) -> sp.Rational:
        return (self.lower + self.upper) / 2


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


def add_scaled(
    target: dict[int, sp.Rational],
    source: dict[int, sp.Rational],
    scale: sp.Rational,
) -> None:
    for exponent, coefficient in source.items():
        value = sp.cancel(target.get(exponent, sp.Rational(0)) + scale * coefficient)
        if value == 0:
            target.pop(exponent, None)
        else:
            target[exponent] = value


def multiply_coefficients(
    left: dict[int, sp.Rational],
    right: dict[int, sp.Rational],
) -> dict[int, sp.Rational]:
    output: dict[int, sp.Rational] = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            output[exponent] = sp.cancel(
                output.get(exponent, sp.Rational(0))
                + left_coefficient * right_coefficient
            )
    return {exponent: value for exponent, value in output.items() if value != 0}


def evaluate_coefficients(
    coefficients: dict[int, sp.Rational],
    point: sp.Rational | sp.Symbol,
) -> sp.Expr:
    return sp.cancel(sum(
        coefficient * point**exponent
        for exponent, coefficient in coefficients.items()
    ))


def primitive_integer_polynomial(
    coefficients: dict[int, sp.Rational],
) -> sp.Poly:
    polynomial = sp.Poly(evaluate_coefficients(coefficients, S), S, domain=sp.QQ)
    _, integer_polynomial = polynomial.clear_denoms(convert=True)
    _, primitive_expression = sp.primitive(integer_polynomial.as_expr(), S)
    primitive = sp.Poly(primitive_expression, S, domain=sp.ZZ)
    if primitive.LC() < 0:
        primitive = -primitive
    return primitive


def coefficient_hash(polynomial: sp.Poly) -> str:
    canonical = json.dumps(
        [str(value) for value in polynomial.all_coeffs()],
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def polynomial_record(polynomial: sp.Poly, *, include_coefficients: bool = False) -> dict[str, Any]:
    nonzero = {
        str(exponents[0]): str(coefficient)
        for exponents, coefficient in polynomial.terms()
        if coefficient != 0
    }
    record: dict[str, Any] = {
        "degree": polynomial.degree(),
        "term_count": len(nonzero),
        "coefficient_sha256": coefficient_hash(polynomial),
    }
    if include_coefficients:
        record["nonzero_coefficients_by_exponent"] = nonzero
    return record


def reduced_point_values(maximum: int, contact: int, point: sp.Rational) -> dict[str, sp.Rational]:
    """Evaluate the A81 two-variable reduction directly at one rational point."""
    h = maximum // 2
    epsilon = sp.Rational(1, (1875 if maximum % 2 == 0 else 2500) * 2**h)
    u = sp.Rational(1, 2**h)
    d = sp.cancel(1 - (h + 1) * u)

    def blocks(r: sp.Rational) -> tuple[sp.Rational, sp.Rational, sp.Rational, sp.Rational]:
        A = sp.cancel((1 + r**maximum) / 2)
        B = sp.cancel(
            r**contact
            - sp.Rational(maximum - contact, maximum)
            - sp.Rational(contact, maximum) * r**maximum
        )
        W = sp.cancel(r - h * r**h + (h - 1) * r**(h + 1))
        C = sp.cancel(2 * W / d)
        if maximum % 2 == 0:
            D = sp.cancel(r**h - 2 * u * W / d)
        else:
            D = sp.cancel(
                (r**h + r**(h + 1)) / 2
                - sp.Rational(3, 2) * u * W / d
            )
        return A, B, C, D

    A_s, B_s, C_s, D_s = blocks(point)
    beta = sp.Rational(1, 8)
    A_beta, B_beta, C_beta, D_beta = blocks(beta)
    H_s = sp.cancel(A_s - D_s - 2 * epsilon)
    H_beta = sp.cancel(A_beta - D_beta + 2 * epsilon)
    determinant = sp.cancel(B_s * H_beta - B_beta * H_s)
    z_numerator = sp.cancel(C_s * H_beta - C_beta * H_s)
    t_numerator = sp.cancel(B_s * C_beta - B_beta * C_s)
    z = sp.cancel(z_numerator / determinant)
    t = sp.cancel(t_numerator / determinant)

    target = sp.Rational(1, 2)
    A_target, B_target, _, _ = blocks(target)
    value = sp.cancel(A_target * t + B_target * z)
    return {
        "determinant": determinant,
        "z": z,
        "t": t,
        "value": value,
    }


def objective_parts(a81, maximum: int, contact: int) -> dict[str, Any]:
    system = a81.reduced_system(maximum, contact)
    target_base = sp.Rational(1, 2)
    A_target = sp.cancel((1 + target_base**maximum) / 2)
    B_target = sp.cancel(
        target_base**contact
        - sp.Rational(maximum - contact, maximum)
        - sp.Rational(contact, maximum) * target_base**maximum
    )
    numerator: dict[int, sp.Rational] = {}
    add_scaled(numerator, system["t_numerator_coefficients"], A_target)
    add_scaled(numerator, system["z_numerator_coefficients"], B_target)
    return {
        "system": system,
        "numerator": numerator,
        "denominator": system["determinant_coefficients"],
    }


def objective_value(parts: dict[str, Any], point: sp.Rational) -> sp.Rational:
    return sp.cancel(
        evaluate_coefficients(parts["numerator"], point)
        / evaluate_coefficients(parts["denominator"], point)
    )


def reduced_values(parts: dict[str, Any], point: sp.Rational) -> dict[str, sp.Rational]:
    system = parts["system"]
    determinant = evaluate_coefficients(system["determinant_coefficients"], point)
    z = sp.cancel(
        evaluate_coefficients(system["z_numerator_coefficients"], point)
        / determinant
    )
    t = sp.cancel(
        evaluate_coefficients(system["t_numerator_coefficients"], point)
        / determinant
    )
    return {"determinant": determinant, "z": z, "t": t}


def adjacent_difference_coefficients(
    lower_parts: dict[str, Any],
    upper_parts: dict[str, Any],
) -> dict[int, sp.Rational]:
    # V_{k+1}-V_k with the positive determinants kept explicit.
    upper_cross = multiply_coefficients(
        upper_parts["numerator"],
        lower_parts["denominator"],
    )
    lower_cross = multiply_coefficients(
        lower_parts["numerator"],
        upper_parts["denominator"],
    )
    add_scaled(upper_cross, lower_cross, sp.Rational(-1))
    return upper_cross


def full_compressed_conditions_at_point(
    a78,
    maximum: int,
    contact: int,
    point: sp.Rational,
) -> dict[str, Any]:
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = a78.normalized_epsilon(maximum)
    p_points = [0, contact, maximum]
    q_points = [1, h, h + 1]

    rows = [
        [1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 1, 1, 1, -1],
        [*p_points, 0, 0, 0, -mean],
        [0, 0, 0, *q_points, -mean],
        [0, 0, 0, *[a78.target_value(x) for x in q_points], 0],
        [
            *[point**x for x in p_points],
            *[-point**x for x in q_points],
            -2 * epsilon,
        ],
        [
            *[-a78.beta_value(x) for x in p_points],
            *[a78.beta_value(x) for x in q_points],
            -2 * epsilon,
        ],
    ]

    domain = sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix(rows)).to_field()
    inverse = domain.inv().to_Matrix()
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0])
    objective = sp.Matrix([
        *[a78.target_value(x) for x in p_points],
        0, 0, 0, 0,
    ])
    basic = inverse * rhs
    dual = inverse.T * objective

    conditions: dict[str, sp.Rational] = {}
    for index, x in enumerate(p_points):
        conditions[f"basic_p_{x}"] = sp.cancel(basic[index])
    for index, x in enumerate(q_points):
        conditions[f"basic_q_{x}"] = sp.cancel(basic[3 + index])
    conditions["basic_t"] = sp.cancel(basic[6])
    conditions["active_dual_alpha_+1"] = sp.cancel(dual[5])
    conditions["active_dual_beta_-1"] = sp.cancel(dual[6])

    p_set = set(p_points)
    q_set = set(q_points)
    for x in range(maximum + 1):
        if x not in p_set:
            p_column = sp.Matrix([
                1, 0, x, 0, 0,
                point**x,
                -a78.beta_value(x),
            ])
            conditions[f"reduced_cost_p_{x}"] = sp.cancel(
                p_column.dot(dual) - a78.target_value(x)
            )
        if x not in q_set:
            q_column = sp.Matrix([
                0, 1, 0, x, a78.target_value(x),
                -point**x,
                a78.beta_value(x),
            ])
            conditions[f"reduced_cost_q_{x}"] = sp.cancel(q_column.dot(dual))

    t_value = basic[6]
    alpha_difference = sp.cancel(
        sum(point**x * basic[index] for index, x in enumerate(p_points))
        - sum(point**x * basic[3 + index] for index, x in enumerate(q_points))
    )
    beta_difference = sp.cancel(
        sum(a78.beta_value(x) * basic[index] for index, x in enumerate(p_points))
        - sum(
            a78.beta_value(x) * basic[3 + index]
            for index, x in enumerate(q_points)
        )
    )
    gamma_difference = sp.cancel(
        sum(a78.gamma_value(x) * basic[index] for index, x in enumerate(p_points))
        - sum(
            a78.gamma_value(x) * basic[3 + index]
            for index, x in enumerate(q_points)
        )
    )
    conditions["inactive_slack_alpha_-1"] = sp.cancel(
        2 * epsilon * t_value + alpha_difference
    )
    conditions["inactive_slack_beta_+1"] = sp.cancel(
        2 * epsilon * t_value - beta_difference
    )
    conditions["inactive_slack_gamma_+1"] = sp.cancel(
        2 * epsilon * t_value - gamma_difference
    )
    conditions["inactive_slack_gamma_-1"] = sp.cancel(
        2 * epsilon * t_value + gamma_difference
    )

    ratio = sp.cancel(sum(
        a78.target_value(x) * basic[index]
        for index, x in enumerate(p_points)
    ))
    return {
        "conditions": conditions,
        "basic": [sp.cancel(value) for value in basic],
        "dual": [sp.cancel(value) for value in dual],
        "ratio": ratio,
        "p_support": p_points,
        "q_support": q_points,
    }


def exact_bisection_root(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
) -> RootBracket:
    lower_sign = int(sp.sign(polynomial.eval(lower)))
    upper_sign = int(sp.sign(polynomial.eval(upper)))
    if lower_sign == 0 or upper_sign == 0 or lower_sign == upper_sign:
        raise RuntimeError("Bisection requires opposite nonzero endpoint signs")
    for _ in range(BISECTION_STEPS):
        midpoint = (lower + upper) / 2
        midpoint_sign = int(sp.sign(polynomial.eval(midpoint)))
        if midpoint_sign == 0:
            return RootBracket(midpoint, midpoint)
        if midpoint_sign == lower_sign:
            lower = midpoint
        else:
            upper = midpoint
    return RootBracket(lower, upper)


def decimal_floor(point: sp.Rational, scale: int) -> sp.Rational:
    return sp.Rational(math.floor(point * scale), scale)


def decimal_ceil(point: sp.Rational, scale: int) -> sp.Rational:
    return sp.Rational(math.ceil(point * scale), scale)


def bracket_record(bracket: RootBracket) -> dict[str, Any]:
    return {
        "lower": str(bracket.lower),
        "upper": str(bracket.upper),
        "width": str(bracket.upper - bracket.lower),
        "midpoint_decimal": f"{float(bracket.midpoint):.18f}",
    }


def main() -> None:
    for required in (A78_SCRIPT, A80_SCRIPT, A81_SCRIPT, A78_RESULT):
        if not required.exists():
            raise FileNotFoundError(required)

    a78 = load_module(A78_SCRIPT, "a78_for_a82")
    a80 = load_module(A80_SCRIPT, "a80_for_a82")
    a81 = load_module(A81_SCRIPT, "a81_for_a82")
    a78_data = json.loads(A78_RESULT.read_text(encoding="utf-8"))
    actual_lookup = {
        int(item["maximum"]): (
            item["family"],
            int(item["contact"]),
            item.get("gamma_sign"),
        )
        for item in a78_data["selected"]
    }

    compressed_pair_count = 0
    adjacent_pair_count = 0
    positive_determinant_count = 0
    positive_z_count = 0
    positive_t_count = 0
    nonzero_difference_count = 0
    pivot_sign_identity_count = 0
    direct_pivot_identity_count = 0
    non_gamma_condition_count = 0
    non_gamma_positive_count = 0
    non_gamma_negative_count = 0
    non_gamma_zero_count = 0
    non_gamma_failure_records: list[dict[str, Any]] = []
    predicted_branch_pass_count = 0
    classification_counts = {
        "gamma_plus": 0,
        "gamma_minus": 0,
        "compressed": 0,
        "invalid": 0,
    }
    locator_records: list[dict[str, Any]] = []
    adjacent_catalogue: list[dict[str, Any]] = []
    endpoint_crossing_candidates: list[dict[str, Any]] = []
    direct_pivot_failures: list[dict[str, Any]] = []

    parts_cache: dict[tuple[int, int], dict[str, Any]] = {}

    def get_parts(maximum: int, contact: int) -> dict[str, Any]:
        key = (maximum, contact)
        if key not in parts_cache:
            parts_cache[key] = objective_parts(a81, maximum, contact)
        return parts_cache[key]

    for maximum in range(M_MIN, M_MAX + 1):
        h = maximum // 2
        contacts = list(range(2, h))
        values: dict[int, sp.Rational] = {}
        reduced: dict[int, dict[str, sp.Rational]] = {}

        endpoint_values: dict[str, dict[int, sp.Rational]] = {
            "local_lower": {},
            "local_upper": {},
        }
        for contact in contacts:
            current_reduced = reduced_point_values(maximum, contact, S0)
            values[contact] = current_reduced["value"]
            reduced[contact] = current_reduced
            endpoint_values["local_lower"][contact] = reduced_point_values(
                maximum, contact, LOCAL_LOWER
            )["value"]
            endpoint_values["local_upper"][contact] = reduced_point_values(
                maximum, contact, LOCAL_UPPER
            )["value"]
            compressed_pair_count += 1
            positive_determinant_count += int(bool(current_reduced["determinant"] > 0))
            positive_z_count += int(bool(current_reduced["z"] > 0))
            positive_t_count += int(bool(current_reduced["t"] > 0))

        differences: list[tuple[int, sp.Rational, int]] = []
        for contact in contacts[:-1]:
            difference = sp.cancel(values[contact + 1] - values[contact])
            sign = int(sp.sign(difference))
            endpoint_signs = {
                "local_lower": int(sp.sign(
                    endpoint_values["local_lower"][contact + 1]
                    - endpoint_values["local_lower"][contact]
                )),
                "s0": sign,
                "local_upper": int(sp.sign(
                    endpoint_values["local_upper"][contact + 1]
                    - endpoint_values["local_upper"][contact]
                )),
            }
            record = {
                "maximum": maximum,
                "lower_contact": contact,
                "upper_contact": contact + 1,
                "s0_sign": sign,
                "endpoint_signs": endpoint_signs,
            }
            adjacent_catalogue.append(record)
            differences.append((contact, difference, sign))
            adjacent_pair_count += 1
            nonzero_difference_count += int(sign != 0)

            z_lower = reduced[contact]["z"]
            z_upper = reduced[contact + 1]["z"]
            rho_forward = sp.cancel(-difference / z_upper)
            rho_backward = sp.cancel(difference / z_lower)
            identity_ok = bool(
                rho_forward != 0
                and rho_backward != 0
                and sp.cancel(rho_backward / rho_forward + z_upper / z_lower) == 0
                and sp.sign(rho_forward) == -sp.sign(rho_backward)
            )
            pivot_sign_identity_count += int(identity_ok)

            if endpoint_signs["local_lower"] != endpoint_signs["local_upper"]:
                lower_parts = get_parts(maximum, contact)
                upper_parts = get_parts(maximum, contact + 1)
                difference_coefficients = adjacent_difference_coefficients(
                    lower_parts, upper_parts
                )
                polynomial = primitive_integer_polynomial(difference_coefficients)
                record["polynomial"] = polynomial_record(polynomial)
                endpoint_crossing_candidates.append({
                    "maximum": maximum,
                    "lower_contact": contact,
                    "upper_contact": contact + 1,
                    "polynomial_object": polynomial,
                    "polynomial": polynomial_record(polynomial, include_coefficients=True),
                    "endpoint_signs": endpoint_signs,
                })

        signs = [item[2] for item in differences]
        transition_positions = [
            index
            for index in range(len(signs) - 1)
            if signs[index] != signs[index + 1]
        ]
        strict_unimodal = bool(
            signs
            and 0 not in signs
            and signs[0] == 1
            and signs[-1] == -1
            and len(transition_positions) == 1
        )
        compressed_maximizer = max(contacts, key=lambda contact: values[contact])
        expected_signs = [
            1 if contact < compressed_maximizer else -1
            for contact in contacts[:-1]
        ]
        strict_unimodal = bool(strict_unimodal and signs == expected_signs)

        compressed_full = full_compressed_conditions_at_point(
            a78,
            maximum,
            compressed_maximizer,
            S0,
        )
        gamma_plus_slack = compressed_full["conditions"]["inactive_slack_gamma_+1"]
        gamma_minus_slack = compressed_full["conditions"]["inactive_slack_gamma_-1"]
        non_gamma_conditions = {
            name: value
            for name, value in compressed_full["conditions"].items()
            if not name.startswith("inactive_slack_gamma_")
        }
        non_gamma_condition_count += len(non_gamma_conditions)
        current_non_gamma_failures = [
            {"name": name, "sign": int(sp.sign(value))}
            for name, value in non_gamma_conditions.items()
            if value <= 0
        ]
        current_positive_count = sum(
            1 for value in non_gamma_conditions.values() if bool(value > 0)
        )
        current_negative_count = sum(
            1 for value in non_gamma_conditions.values() if bool(value < 0)
        )
        current_zero_count = sum(
            1 for value in non_gamma_conditions.values() if value == 0
        )
        non_gamma_positive_count += current_positive_count
        non_gamma_negative_count += current_negative_count
        non_gamma_zero_count += current_zero_count
        if current_non_gamma_failures:
            non_gamma_failure_records.append({
                "maximum": maximum,
                "compressed_maximizer": compressed_maximizer,
                "failures": current_non_gamma_failures,
            })

        if gamma_plus_slack < 0 < gamma_minus_slack:
            classification = "gamma_plus"
            predicted = (
                "three_band_adjacent",
                compressed_maximizer,
                1,
            )
        elif gamma_minus_slack < 0 < gamma_plus_slack:
            classification = "gamma_minus"
            predicted = (
                "three_band_adjacent",
                compressed_maximizer - 1,
                -1,
            )
        elif gamma_plus_slack > 0 and gamma_minus_slack > 0:
            classification = "compressed"
            predicted = (
                "two_band_compressed",
                compressed_maximizer,
                None,
            )
        else:
            classification = "invalid"
            predicted = ("invalid", compressed_maximizer, None)
        classification_counts[classification] += 1

        if predicted[0] == "three_band_adjacent":
            branch_result = a78.evaluate_three_band(
                maximum,
                int(predicted[1]),
                int(predicted[2]),
                collect_pass=True,
            )
            branch_pass = branch_result["status"] == "pass"
        elif predicted[0] == "two_band_compressed":
            branch_pass = all(
                bool(value > 0) for value in compressed_full["conditions"].values()
            )
        else:
            branch_pass = False
        predicted_branch_pass_count += int(branch_pass)

        locator_records.append({
            "maximum": maximum,
            "compressed_contact_count": len(contacts),
            "adjacent_difference_signs": signs,
            "sign_transition_count": len(transition_positions),
            "strict_unimodal": strict_unimodal,
            "compressed_maximizer": compressed_maximizer,
            "gamma_slack_signs": {
                "gamma_plus": int(sp.sign(gamma_plus_slack)),
                "gamma_minus": int(sp.sign(gamma_minus_slack)),
            },
            "classification": classification,
            "predicted_selection": {
                "family": predicted[0],
                "contact": int(predicted[1]),
                "gamma_sign": predicted[2],
            },
            "actual_A78_selection": {
                "family": actual_lookup[maximum][0],
                "contact": actual_lookup[maximum][1],
                "gamma_sign": actual_lookup[maximum][2],
            },
            "selection_matches_A78": predicted == actual_lookup[maximum],
            "predicted_branch_full_KKT_pass": branch_pass,
            "non_gamma_condition_count": len(non_gamma_conditions),
            "all_non_gamma_conditions_positive": all(
                bool(value > 0) for value in non_gamma_conditions.values()
            ),
            "non_gamma_failure_names": [
                item["name"] for item in current_non_gamma_failures
            ],
        })

    # Directly verify the basis-exchange formulas against dual reduced costs
    # on a declared spread of support sizes. The all-pair identity is analytic;
    # these witnesses guard the implementation and sign convention.
    for maximum, contact in DIRECT_PIVOT_WITNESSES:
        lower_full = full_compressed_conditions_at_point(a78, maximum, contact, S0)
        upper_full = full_compressed_conditions_at_point(a78, maximum, contact + 1, S0)
        lower_point = reduced_point_values(maximum, contact, S0)
        upper_point = reduced_point_values(maximum, contact + 1, S0)
        difference = sp.cancel(upper_point["value"] - lower_point["value"])
        lower_z = lower_point["z"]
        upper_z = upper_point["z"]
        predicted_forward = sp.cancel(-difference / upper_z)
        predicted_backward = sp.cancel(difference / lower_z)
        direct_forward = lower_full["conditions"][f"reduced_cost_p_{contact + 1}"]
        direct_backward = upper_full["conditions"][f"reduced_cost_p_{contact}"]
        passed = bool(
            sp.cancel(predicted_forward - direct_forward) == 0
            and sp.cancel(predicted_backward - direct_backward) == 0
        )
        direct_pivot_identity_count += int(passed)
        if not passed:
            direct_pivot_failures.append({
                "maximum": maximum,
                "contact": contact,
            })

    transition_records: list[dict[str, Any]] = []
    for candidate in endpoint_crossing_candidates:
        maximum = int(candidate["maximum"])
        contact = int(candidate["lower_contact"])
        polynomial: sp.Poly = candidate.pop("polynomial_object")
        bracket = exact_bisection_root(polynomial, LOCAL_LOWER, LOCAL_UPPER)
        derivative_certificate = a80.certify_polynomial_fixed_sign(
            polynomial.diff(),
            bracket.lower,
            bracket.upper,
            maximum_depth=8,
        )

        scale = 10**12
        below = decimal_floor(bracket.lower, scale)
        above = decimal_ceil(bracket.upper, scale)
        if not (LOCAL_LOWER < below < bracket.lower):
            below = (LOCAL_LOWER + bracket.lower) / 2
        if not (bracket.upper < above < LOCAL_UPPER):
            above = (bracket.upper + LOCAL_UPPER) / 2

        side_candidates = []
        for side, witness in (("below", below), ("above", above)):
            for gamma_sign in (-1, 1):
                evaluated = a80.evaluate_adjacent_candidate(
                    a78,
                    maximum,
                    contact,
                    gamma_sign,
                    witness,
                )
                side_candidates.append({"side": side, **evaluated})

        passing = [
            item for item in side_candidates if item["status"] == "pass"
        ]
        transition_records.append({
            "maximum": maximum,
            "contact_pair": [contact, contact + 1],
            "objective_difference": "V_(k+1)-V_k",
            "polynomial": candidate["polynomial"],
            "endpoint_signs": candidate["endpoint_signs"],
            "root_bracket": bracket_record(bracket),
            "simple_root_certificate": {
                "derivative_fixed_sign_on_bracket": derivative_certificate,
                "pass": bool(
                    derivative_certificate["pass"]
                    and derivative_certificate["sign"] != 0
                ),
            },
            "side_witnesses": side_candidates,
            "passing_orientation_by_side": {
                "below": [
                    item["gamma_sign"] for item in passing if item["side"] == "below"
                ],
                "above": [
                    item["gamma_sign"] for item in passing if item["side"] == "above"
                ],
            },
        })

    exact_expected_transitions = {
        28: {"pair": [6, 7], "below": [-1], "above": [1]},
        79: {"pair": [15, 16], "below": [1], "above": [-1]},
    }

    non_gamma_failure_supports = [
        item["maximum"] for item in non_gamma_failure_records
    ]
    non_gamma_failure_names = [
        failure["name"]
        for item in non_gamma_failure_records
        for failure in item["failures"]
    ]

    selection_matches = sum(
        item["selection_matches_A78"] for item in locator_records
    )
    strict_unimodal_count = sum(item["strict_unimodal"] for item in locator_records)
    transition_side_pass = all(
        record["contact_pair"] == exact_expected_transitions[record["maximum"]]["pair"]
        and record["passing_orientation_by_side"]["below"]
        == exact_expected_transitions[record["maximum"]]["below"]
        and record["passing_orientation_by_side"]["above"]
        == exact_expected_transitions[record["maximum"]]["above"]
        for record in transition_records
    )

    gates = {
        "compressed_contact_count_exact": compressed_pair_count == 1438,
        "adjacent_comparison_count_exact": adjacent_pair_count == 1367,
        "all_probe_determinants_positive": positive_determinant_count == compressed_pair_count,
        "all_probe_interior_masses_positive": positive_z_count == compressed_pair_count,
        "all_probe_scaled_masses_positive": positive_t_count == compressed_pair_count,
        "all_probe_adjacent_differences_nonzero": nonzero_difference_count == adjacent_pair_count,
        "all_probe_pivot_sign_identities_hold": pivot_sign_identity_count == adjacent_pair_count,
        "direct_dual_pivot_witnesses_match": (
            direct_pivot_identity_count == len(DIRECT_PIVOT_WITNESSES)
            and not direct_pivot_failures
        ),
        "all_supports_have_strict_unimodal_compressed_objective": strict_unimodal_count == 71,
        "locator_non_gamma_condition_census_exact": (
            non_gamma_condition_count == 6887
            and non_gamma_positive_count == 6872
            and non_gamma_negative_count == 15
            and non_gamma_zero_count == 0
        ),
        "locator_primal_feasibility_exceptions_exact": (
            non_gamma_failure_supports == [23, 28, 34, 45, 51, 56, 62, 68]
            and all(name.startswith("basic_") for name in non_gamma_failure_names)
            and all(
                item["classification"] == "gamma_minus"
                for item in locator_records
                if item["maximum"] in non_gamma_failure_supports
            )
        ),
        "gamma_slack_trichotomy_exact": classification_counts == {
            "gamma_plus": 57,
            "gamma_minus": 11,
            "compressed": 3,
            "invalid": 0,
        },
        "locator_reproduces_all_A78_selections": selection_matches == 71,
        "all_predicted_full_branches_pass_KKT": predicted_branch_pass_count == 71,
        "local_endpoint_crossing_candidates_exact": [
            (item["maximum"], item["lower_contact"])
            for item in endpoint_crossing_candidates
        ] == [(28, 6), (79, 15)],
        "both_local_candidate_roots_are_simple_on_isolating_brackets": all(
            item["simple_root_certificate"]["pass"] for item in transition_records
        ),
        "local_orientation_switches_certified_by_exact_side_KKT": transition_side_pass,
        "scope_and_nonclaim_boundary_preserved": (
            M_MIN == 10
            and M_MAX == 80
            and S0 == sp.Rational(131, 1000)
            and LOCAL_LOWER == sp.Rational(129, 1000)
            and LOCAL_UPPER == sp.Rational(133, 1000)
        ),
    }

    summary = {
        "audit": "A82_EXACT_ADJACENT_CONTACT_LOCATOR",
        "contract": {
            "maximum_range": [M_MIN, M_MAX],
            "compressed_contact_rule": "2 <= k < floor(M/2)",
            "probe": str(S0),
            "local_interval": [str(LOCAL_LOWER), str(LOCAL_UPPER)],
            "target_exponent": 1,
            "beta_exponent": 3,
            "gamma_exponent": 4,
        },
        "analytic_identity": {
            "compressed_value": "V_(M,k)(s)",
            "adjacent_difference": "D_(M,k)=V_(M,k+1)-V_(M,k)",
            "forward_reduced_cost": "rho_forward=-D/z_(M,k+1)",
            "backward_reduced_cost": "rho_backward=D/z_(M,k)",
            "ratio_identity": "rho_backward/rho_forward=-z_(M,k+1)/z_(M,k)",
            "consequence": "Positive adjacent basic masses force opposite cross-reduced-cost signs.",
        },
        "probe_theorem": {
            "compressed_contact_count": compressed_pair_count,
            "adjacent_comparison_count": adjacent_pair_count,
            "strict_unimodal_support_count": strict_unimodal_count,
            "unique_compressed_maximizer_count": len(locator_records),
            "classification_counts": classification_counts,
            "selection_matches_A78_count": selection_matches,
            "predicted_full_KKT_pass_count": predicted_branch_pass_count,
            "non_gamma_KKT_condition_count": non_gamma_condition_count,
            "non_gamma_KKT_positive_count": non_gamma_positive_count,
            "non_gamma_KKT_negative_count": non_gamma_negative_count,
            "non_gamma_KKT_zero_count": non_gamma_zero_count,
            "compressed_maximizer_primal_feasibility_exceptions": non_gamma_failure_records,
            "interpretation": (
                "The algebraic compressed objective is strictly unimodal, but its maximizer is not always a feasible compressed LP basis. "
                "Eight gamma-minus supports have 15 negative basic variables, so the exact full KKT check of the predicted adjacent lift remains necessary."
            ),
            "locator": locator_records,
        },
        "local_interval_extension": {
            "status": "certified endpoint-crossing roots; not a complete same-sign root atlas",
            "adjacent_polynomial_count": adjacent_pair_count,
            "endpoint_crossing_candidate_count": len(endpoint_crossing_candidates),
            "candidate_pairs": [
                [item["maximum"], item["lower_contact"], item["upper_contact"]]
                for item in endpoint_crossing_candidates
            ],
            "certified_transitions": transition_records,
            "nonclaim": (
                "Same endpoint signs do not by themselves exclude an even number of interior roots. "
                "A82 therefore does not promote the endpoint scan to a complete interval atlas."
            ),
        },
        "direct_pivot_witnesses": {
            "declared": [list(item) for item in DIRECT_PIVOT_WITNESSES],
            "pass_count": direct_pivot_identity_count,
            "failure_count": len(direct_pivot_failures),
        },
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": (
            "PASS_EXACT_ADJACENT_CONTACT_LOCATOR_AND_LOCAL_ORIENTATION_SWITCHES"
            if all(gates.values())
            else "FAIL"
        ),
        "claim_boundary": [
            "The complete contact-locator theorem is exact only at s=131/1000.",
            "The support range is finite: 10<=M<=80.",
            "The two local roots are certified inside narrow brackets, but A82 is not a complete root atlas for all adjacent-difference polynomials on I.",
            "No all-M recurrence or closed formula for the maximizing contact is claimed.",
            "The algebraic compressed maximizer is not asserted to be primal feasible; eight exact finite exceptions are recorded.",
            "No physical interpretation is inferred from contacts, gamma orientation, or objective switches.",
        ],
    }

    catalogue = {
        "audit": "A82_ADJACENT_OBJECTIVE_DIFFERENCE_CATALOGUE",
        "polynomial_count": len(adjacent_catalogue),
        "scope": {
            "maximum_range": [M_MIN, M_MAX],
            "contact_rule": "2 <= k < floor(M/2)-1",
            "local_interval": [str(LOCAL_LOWER), str(LOCAL_UPPER)],
        },
        "polynomials": adjacent_catalogue,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    result_path = RESULTS / "a82_adjacent_contact_locator_results.json"
    catalogue_path = RESULTS / "a82_adjacent_difference_catalogue.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    catalogue_path.write_text(json.dumps(catalogue, indent=2), encoding="utf-8")

    print(json.dumps({
        "audit": summary["audit"],
        "compressed_contact_count": compressed_pair_count,
        "adjacent_comparison_count": adjacent_pair_count,
        "strict_unimodal_support_count": strict_unimodal_count,
        "classification_counts": classification_counts,
        "selection_matches_A78_count": selection_matches,
        "endpoint_crossing_candidates": summary["local_interval_extension"]["candidate_pairs"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": summary["verdict"],
        "result": result_path.name,
        "catalogue": catalogue_path.name,
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
