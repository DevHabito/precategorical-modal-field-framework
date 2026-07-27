#!/usr/bin/env python3
"""A80 exact local compression-window atlas.

A78 selected one contact index k(M) at the exact probe s0=131/1000 for
M=10,...,80. A79 then proved exact gamma-inactive compression intervals only
for the three intervals that contain s0, namely M=40,57,74.

A80 asks a broader but still finite and local question:

    For the A78-selected contact k(M), which support sizes possess an exact
    gamma-inactive compression window inside

        I = [129/1000, 133/1000]?

The audit derives the two contact-entry Cramer polynomials for every selected
(M,k), proves a parity-reduced six-monomial boundary law, certifies strict
monotonicity on I, isolates every ordered root pair by exact rational
bisection, and verifies the complete compressed-branch KKT system over every
resulting open algebraic interval.

The result is exact only for M=10,...,80, for the A78-selected contacts, and on
the declared local interval I. It is not an all-M recurrence theorem and it
does not assign a physical meaning to the LP contacts.
"""

from __future__ import annotations

import gc
import hashlib
import importlib.util
import json
import math
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT_DIR = ROOT / "results"
A78_SCRIPT = HERE / "a78_rational_probe_contact_selection_audit.py"
A79_SCRIPT = HERE / "a79_compression_interval_certificate_audit.py"
A78_RESULT = OUTPUT_DIR / "a78_rational_probe_contact_selection_results.json"
A79_POLYNOMIALS = OUTPUT_DIR / "a79_boundary_polynomials.json"

S = sp.Symbol("s")
LOCAL_LOWER = sp.Rational(129, 1000)
LOCAL_UPPER = sp.Rational(133, 1000)
S0 = sp.Rational(131, 1000)
BISECTION_STEPS = 80
OUTSIDE_DELTA = sp.Rational(1, 10**9)


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


def normalized_epsilon(maximum: int) -> sp.Rational:
    h = maximum // 2
    denominator = (1875 if maximum % 2 == 0 else 2500) * 2**h
    return sp.Rational(1, denominator)


def target_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2**x)


def beta_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (3 * x))


def gamma_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (4 * x))


def primitive_integer_poly(expression: sp.Expr) -> sp.Poly:
    numerator, _ = sp.fraction(sp.cancel(expression))
    polynomial = sp.Poly(numerator, S, domain=sp.QQ)
    _, integer_poly = polynomial.clear_denoms(convert=True)
    _, primitive_expression = sp.primitive(integer_poly.as_expr(), S)
    primitive_poly = sp.Poly(primitive_expression, S, domain=sp.ZZ)
    if primitive_poly.LC() < 0:
        primitive_poly = -primitive_poly
    return primitive_poly


def coefficient_hash(polynomial: sp.Poly) -> str:
    coefficients = [str(value) for value in polynomial.all_coeffs()]
    canonical = json.dumps(coefficients, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def polynomial_record(polynomial: sp.Poly) -> dict[str, Any]:
    nonzero = {
        str(exponents[0]): str(coefficient)
        for exponents, coefficient in polynomial.terms()
        if coefficient != 0
    }
    return {
        "degree": polynomial.degree(),
        "term_count": len(nonzero),
        "nonzero_coefficients_by_exponent": nonzero,
        "coefficient_sha256": coefficient_hash(polynomial),
    }


def exact_polynomial_interval(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
    *,
    derivative: bool = False,
) -> tuple[sp.Rational, sp.Rational]:
    """A dependency-safe monomial interval enclosure on a positive interval."""
    enclosure_lower = sp.Rational(0)
    enclosure_upper = sp.Rational(0)
    for (exponent,), coefficient in polynomial.terms():
        if derivative:
            if exponent == 0:
                continue
            coefficient *= exponent
            exponent -= 1
        power_lower = lower**exponent
        power_upper = upper**exponent
        if coefficient >= 0:
            enclosure_lower += coefficient * power_lower
            enclosure_upper += coefficient * power_upper
        else:
            enclosure_lower += coefficient * power_upper
            enclosure_upper += coefficient * power_lower
    return sp.factor(enclosure_lower), sp.factor(enclosure_upper)


def multiply_intervals(
    left: tuple[sp.Rational, sp.Rational],
    right: tuple[sp.Rational, sp.Rational],
) -> tuple[sp.Rational, sp.Rational]:
    a, b = left
    c, d = right
    products = (a * c, a * d, b * c, b * d)
    return min(products), max(products)


def horner_interval(
    coefficients: tuple[sp.Rational, ...],
    lower: sp.Rational,
    upper: sp.Rational,
) -> tuple[sp.Rational, sp.Rational]:
    enclosure = (sp.Rational(0), sp.Rational(0))
    variable_interval = (lower, upper)
    for coefficient in coefficients:
        enclosure = multiply_intervals(enclosure, variable_interval)
        enclosure = (
            enclosure[0] + coefficient,
            enclosure[1] + coefficient,
        )
    return enclosure


def certify_polynomial_fixed_sign(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
    *,
    maximum_depth: int = 24,
) -> dict[str, Any]:
    coefficients = tuple(
        sp.Rational(value) for value in polynomial.all_coeffs()
    )
    stack = [(lower, upper, 0)]
    certified_sign: int | None = None
    piece_count = 0
    maximum_depth_used = 0

    while stack:
        current_lower, current_upper, depth = stack.pop()
        piece_count += 1
        maximum_depth_used = max(maximum_depth_used, depth)
        enclosure_lower, enclosure_upper = horner_interval(
            coefficients,
            current_lower,
            current_upper,
        )
        current_sign = (
            1 if enclosure_lower > 0 else -1 if enclosure_upper < 0 else 0
        )
        if current_sign == 0:
            if depth >= maximum_depth:
                return {
                    "pass": False,
                    "sign": 0,
                    "piece_count": piece_count,
                    "maximum_depth_used": maximum_depth_used,
                    "failure_interval": [
                        str(current_lower),
                        str(current_upper),
                    ],
                    "failure_enclosure": [
                        str(enclosure_lower),
                        str(enclosure_upper),
                    ],
                }
            midpoint = (current_lower + current_upper) / 2
            stack.append((midpoint, current_upper, depth + 1))
            stack.append((current_lower, midpoint, depth + 1))
            continue

        if certified_sign is None:
            certified_sign = current_sign
        elif certified_sign != current_sign:
            return {
                "pass": False,
                "sign": 0,
                "piece_count": piece_count,
                "maximum_depth_used": maximum_depth_used,
                "failure": "mixed certified signs",
            }

    return {
        "pass": True,
        "sign": int(certified_sign or 0),
        "piece_count": piece_count,
        "maximum_depth_used": maximum_depth_used,
    }


def certify_expression_positive(
    expression: sp.Expr,
    lower: sp.Rational,
    upper: sp.Rational,
) -> dict[str, Any]:
    numerator, denominator = sp.fraction(sp.cancel(expression))
    numerator_poly = sp.Poly(numerator, S, domain=sp.QQ)
    denominator_poly = sp.Poly(denominator, S, domain=sp.QQ)
    numerator_certificate = certify_polynomial_fixed_sign(
        numerator_poly,
        lower,
        upper,
    )
    denominator_certificate = certify_polynomial_fixed_sign(
        denominator_poly,
        lower,
        upper,
    )
    passes = (
        numerator_certificate["pass"]
        and denominator_certificate["pass"]
        and numerator_certificate["sign"]
        * denominator_certificate["sign"]
        == 1
    )
    return {
        "pass": passes,
        "numerator_degree": numerator_poly.degree(),
        "denominator_degree": denominator_poly.degree(),
        "numerator": numerator_certificate,
        "denominator": denominator_certificate,
    }


def exact_bisection_root(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
) -> RootBracket:
    lower_sign = sp.sign(polynomial.eval(lower))
    upper_sign = sp.sign(polynomial.eval(upper))
    if not (lower_sign < 0 and upper_sign > 0):
        raise RuntimeError(
            f"Bisection requires negative/positive endpoint signs, got "
            f"{lower_sign}, {upper_sign}"
        )
    for _ in range(BISECTION_STEPS):
        midpoint = (lower + upper) / 2
        midpoint_sign = sp.sign(polynomial.eval(midpoint))
        if midpoint_sign < 0:
            lower = midpoint
        elif midpoint_sign > 0:
            upper = midpoint
        else:
            return RootBracket(midpoint, midpoint)
    return RootBracket(lower, upper)


def bracket_record(bracket: RootBracket) -> dict[str, Any]:
    return {
        "lower": str(bracket.lower),
        "upper": str(bracket.upper),
        "width": str(bracket.upper - bracket.lower),
        "midpoint_decimal": f"{float(bracket.midpoint):.18f}",
    }


def build_compressed_symbolic_branch(
    maximum: int,
    contact: int,
) -> dict[str, Any]:
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    p_points = [0, contact, maximum]
    q_points = [1, h, h + 1]

    basis = sp.Matrix([
        [1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 1, 1, 1, -1],
        [*p_points, 0, 0, 0, -mean],
        [0, 0, 0, *q_points, -mean],
        [0, 0, 0, *[target_value(x) for x in q_points], 0],
        [
            *[S**x for x in p_points],
            *[-S**x for x in q_points],
            -2 * epsilon,
        ],
        [
            *[-beta_value(x) for x in p_points],
            *[beta_value(x) for x in q_points],
            -2 * epsilon,
        ],
    ])
    inverse = basis.inv(method="DM")
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0])
    objective = sp.Matrix([
        *[target_value(x) for x in p_points],
        0, 0, 0, 0,
    ])
    basic = inverse * rhs
    dual = inverse.T * objective

    conditions: list[tuple[str, sp.Expr]] = []
    for index, x in enumerate(p_points):
        conditions.append((f"basic_p_{x}", sp.cancel(basic[index])))
    for index, x in enumerate(q_points):
        conditions.append((
            f"basic_q_{x}",
            sp.cancel(basic[3 + index]),
        ))
    conditions.append(("basic_t", sp.cancel(basic[6])))
    conditions.append((
        "active_dual_alpha_+1",
        sp.cancel(dual[5]),
    ))
    conditions.append((
        "active_dual_beta_-1",
        sp.cancel(dual[6]),
    ))

    p_set = set(p_points)
    q_set = set(q_points)
    for x in range(maximum + 1):
        if x not in p_set:
            conditions.append((
                f"reduced_cost_p_{x}",
                sp.cancel(
                    dual[0]
                    + x * dual[2]
                    + S**x * dual[5]
                    - beta_value(x) * dual[6]
                    - target_value(x)
                ),
            ))
        if x not in q_set:
            conditions.append((
                f"reduced_cost_q_{x}",
                sp.cancel(
                    dual[1]
                    + x * dual[3]
                    + target_value(x) * dual[4]
                    - S**x * dual[5]
                    + beta_value(x) * dual[6]
                ),
            ))

    t_value = basic[6]
    alpha_difference = (
        sum(S**x * basic[i] for i, x in enumerate(p_points))
        - sum(
            S**x * basic[3 + i]
            for i, x in enumerate(q_points)
        )
    )
    beta_difference = (
        sum(beta_value(x) * basic[i] for i, x in enumerate(p_points))
        - sum(
            beta_value(x) * basic[3 + i]
            for i, x in enumerate(q_points)
        )
    )
    gamma_difference = (
        sum(gamma_value(x) * basic[i] for i, x in enumerate(p_points))
        - sum(
            gamma_value(x) * basic[3 + i]
            for i, x in enumerate(q_points)
        )
    )
    conditions.extend([
        (
            "inactive_slack_alpha_-1",
            sp.cancel(2 * epsilon * t_value + alpha_difference),
        ),
        (
            "inactive_slack_beta_+1",
            sp.cancel(2 * epsilon * t_value - beta_difference),
        ),
        (
            "inactive_slack_gamma_+1",
            sp.cancel(2 * epsilon * t_value - gamma_difference),
        ),
        (
            "inactive_slack_gamma_-1",
            sp.cancel(2 * epsilon * t_value + gamma_difference),
        ),
    ])
    return {
        "p_support": p_points,
        "q_support": q_points,
        "conditions": conditions,
    }


def evaluate_adjacent_candidate(
    a78,
    maximum: int,
    contact: int,
    gamma_sign: int,
    witness: sp.Rational,
) -> dict[str, Any]:
    original_probe = a78.S0
    a78.S0 = witness
    try:
        result = a78.evaluate_three_band(
            maximum,
            contact,
            gamma_sign,
            collect_pass=True,
        )
    finally:
        a78.S0 = original_probe
    return {
        "witness": str(witness),
        "contact_pair": [contact, contact + 1],
        "gamma_sign": gamma_sign,
        "status": result["status"],
        "first_failure": (
            {
                "name": result["failure"][0],
                "value": str(result["failure"][1]),
            }
            if result["failure"]
            else None
        ),
    }


def main() -> None:
    for required in (A78_SCRIPT, A79_SCRIPT, A78_RESULT, A79_POLYNOMIALS):
        if not required.exists():
            raise FileNotFoundError(required)

    a78 = load_module(A78_SCRIPT, "a78_for_a80")
    a79 = load_module(A79_SCRIPT, "a79_for_a80")
    a78_data = json.loads(A78_RESULT.read_text(encoding="utf-8"))
    selected = a78_data["selected"]
    a79_polynomial_data = json.loads(
        A79_POLYNOMIALS.read_text(encoding="utf-8")
    )

    a79_lookup: dict[tuple[int, str], sp.Poly] = {}
    for item in a79_polynomial_data["polynomials"]:
        coefficients = [
            sp.Integer(value)
            for value in item["polynomial"]["coefficients_descending"]
        ]
        a79_lookup[(item["maximum"], item["boundary"])] = sp.Poly.from_list(
            coefficients,
            gens=S,
            domain=sp.ZZ,
        )

    boundary_catalogue: list[dict[str, Any]] = []
    contact_records: list[dict[str, Any]] = []
    complete_pairs: list[dict[str, Any]] = []
    derivative_failures: list[dict[str, Any]] = []
    sparsity_failures: list[dict[str, Any]] = []

    for selected_item in selected:
        maximum = int(selected_item["maximum"])
        contact = int(selected_item["contact"])
        h = maximum // 2
        expected_exponents = {maximum, h + 1, h, contact, 1, 0}

        lower_polynomial = a79.cramer_entering_atom_polynomial(
            maximum,
            contact - 1,
            -1,
            contact - 1,
            S,
        )
        upper_polynomial = a79.cramer_entering_atom_polynomial(
            maximum,
            contact,
            1,
            contact + 1,
            S,
        )

        boundary_items = []
        for boundary, polynomial, adjacent_pair, entering_atom, gamma_sign in (
            (
                "lower",
                lower_polynomial,
                [contact - 1, contact],
                contact - 1,
                -1,
            ),
            (
                "upper",
                upper_polynomial,
                [contact, contact + 1],
                contact + 1,
                1,
            ),
        ):
            derivative_lower, derivative_upper = exact_polynomial_interval(
                polynomial,
                LOCAL_LOWER,
                LOCAL_UPPER,
                derivative=True,
            )
            derivative_positive = bool(derivative_lower > 0)
            nonzero_exponents = {
                exponents[0]
                for exponents, coefficient in polynomial.terms()
                if coefficient != 0
            }
            sparse_match = bool(nonzero_exponents == expected_exponents)
            endpoint_signs = {
                "local_lower": int(sp.sign(polynomial.eval(LOCAL_LOWER))),
                "s0": int(sp.sign(polynomial.eval(S0))),
                "local_upper": int(sp.sign(polynomial.eval(LOCAL_UPPER))),
            }
            root_bracket: RootBracket | None = None
            if (
                derivative_positive
                and endpoint_signs["local_lower"] < 0
                and endpoint_signs["local_upper"] > 0
            ):
                root_bracket = exact_bisection_root(
                    polynomial,
                    LOCAL_LOWER,
                    LOCAL_UPPER,
                )

            if not derivative_positive:
                derivative_failures.append({
                    "maximum": maximum,
                    "contact": contact,
                    "boundary": boundary,
                })
            if not sparse_match:
                sparsity_failures.append({
                    "maximum": maximum,
                    "contact": contact,
                    "boundary": boundary,
                    "observed": sorted(nonzero_exponents),
                    "expected": sorted(expected_exponents),
                })

            record = {
                "maximum": maximum,
                "contact": contact,
                "parity": "even" if maximum % 2 == 0 else "odd",
                "h": h,
                "boundary": boundary,
                "adjacent_pair": adjacent_pair,
                "gamma_sign": gamma_sign,
                "entering_atom": entering_atom,
                "expected_six_term_exponents": sorted(
                    expected_exponents,
                    reverse=True,
                ),
                "sparsity_match": sparse_match,
                "strictly_increasing_on_local_interval": (
                    derivative_positive
                ),
                "derivative_interval": {
                    "lower": str(derivative_lower),
                    "upper": str(derivative_upper),
                },
                "endpoint_signs": endpoint_signs,
                "root_bracket": (
                    bracket_record(root_bracket)
                    if root_bracket is not None
                    else None
                ),
                "polynomial": polynomial_record(polynomial),
            }
            boundary_catalogue.append(record)
            boundary_items.append((record, polynomial, root_bracket))

        lower_record, lower_polynomial, lower_root = boundary_items[0]
        upper_record, upper_polynomial, upper_root = boundary_items[1]
        root_class = (
            "complete_ordered_pair"
            if lower_root is not None and upper_root is not None
            and lower_root.upper < upper_root.lower
            else "upper_only"
            if lower_root is None and upper_root is not None
            else "lower_only"
            if lower_root is not None and upper_root is None
            else "none"
        )
        contact_record = {
            "maximum": maximum,
            "contact": contact,
            "selected_family_at_s0": selected_item["family"],
            "selected_gamma_sign_at_s0": selected_item.get("gamma_sign"),
            "root_class": root_class,
            "lower_root": lower_record["root_bracket"],
            "upper_root": upper_record["root_bracket"],
        }
        contact_records.append(contact_record)

        if root_class == "complete_ordered_pair":
            assert lower_root is not None and upper_root is not None
            complete_pairs.append({
                "maximum": maximum,
                "contact": contact,
                "selected_item": selected_item,
                "lower_polynomial": lower_polynomial,
                "upper_polynomial": upper_polynomial,
                "lower_root": lower_root,
                "upper_root": upper_root,
            })

    interval_condition_certificates: list[dict[str, Any]] = []
    window_results: list[dict[str, Any]] = []
    all_interval_conditions_pass = True
    all_boundary_identities_pass = True
    all_midpoints_pass = True
    lower_adjacent_pass_count = 0
    upper_adjacent_pass_count = 0
    worker_script = HERE / "a80_local_compression_window_worker.py"

    for pair in complete_pairs:
        maximum = pair["maximum"]
        contact = pair["contact"]
        print(f"A80 worker start M={maximum} k={contact}", flush=True)
        completed = subprocess.run(
            [sys.executable, str(worker_script), str(maximum), str(contact)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"A80 worker failed for M={maximum}, k={contact}: "
                f"{completed.stderr}"
            )
        print(f"A80 worker done M={maximum}", flush=True)
        payload = json.loads(completed.stdout)
        window = payload["window_result"]
        window_results.append(window)
        interval_condition_certificates.extend(
            payload["condition_certificates"]
        )
        identities = window["boundary_numerator_identities"]
        all_boundary_identities_pass &= all(identities.values())
        all_interval_conditions_pass &= window[
            "full_interval_KKT_certificate"
        ]["all_nonboundary_conditions_positive_on_rational_hull"]
        all_midpoints_pass &= (
            window["independent_midpoint_KKT_check"]["status"] == "pass"
        )
        lower_adjacent_pass_count += (
            window["declared_adjacent_candidate_checks"]
            ["below_lower_boundary"]["status"] == "pass"
        )
        upper_adjacent_pass_count += (
            window["declared_adjacent_candidate_checks"]
            ["above_upper_boundary"]["status"] == "pass"
        )

    root_class_counts: dict[str, int] = {}
    for record in contact_records:
        root_class_counts[record["root_class"]] = (
            root_class_counts.get(record["root_class"], 0) + 1
        )

    windows_containing_s0 = [
        item["maximum"]
        for item in window_results
        if item["open_window"]["contains_s0"]
    ]
    windows_below_s0 = [
        item["maximum"]
        for item in window_results
        if item["open_window"]["lies_strictly_below_s0"]
    ]

    a79_reproduction: list[dict[str, Any]] = []
    for maximum in (40, 57, 74):
        pair = next(
            item for item in complete_pairs
            if item["maximum"] == maximum
        )
        for boundary, polynomial in (
            ("lower", pair["lower_polynomial"]),
            ("upper", pair["upper_polynomial"]),
        ):
            previous = a79_lookup[(maximum, boundary)]
            a79_reproduction.append({
                "maximum": maximum,
                "boundary": boundary,
                "same_monic_primitive_polynomial": (
                    polynomial.monic() == previous.monic()
                ),
                "same_coefficient_hash": (
                    coefficient_hash(polynomial)
                    == coefficient_hash(previous)
                ),
            })

    total_nonboundary_conditions = sum(
        item["full_interval_KKT_certificate"][
            "nonboundary_condition_count"
        ]
        for item in window_results
    )

    gates = {
        "A78_selected_contact_domain_loaded_exactly": (
            len(selected) == 71
            and selected[0]["maximum"] == 10
            and selected[-1]["maximum"] == 80
        ),
        "all_142_boundary_polynomials_generated": (
            len(boundary_catalogue) == 142
        ),
        "all_boundary_polynomials_have_degree_M": all(
            item["polynomial"]["degree"] == item["maximum"]
            for item in boundary_catalogue
        ),
        "all_boundary_polynomials_obey_six_term_parity_reduction": (
            not sparsity_failures
            and all(
                item["polynomial"]["term_count"] == 6
                for item in boundary_catalogue
            )
        ),
        "all_boundary_polynomials_strictly_increase_on_local_interval": (
            not derivative_failures
        ),
        "root_classification_is_20_complete_3_upper_only_48_none": (
            root_class_counts
            == {
                "complete_ordered_pair": 20,
                "upper_only": 3,
                "none": 48,
            }
        ),
        "all_20_complete_root_pairs_are_strictly_ordered": (
            len(complete_pairs) == 20
            and all(
                item["lower_root"].upper
                < item["upper_root"].lower
                for item in complete_pairs
            )
        ),
        "all_20_boundary_numerator_identities_hold": (
            all_boundary_identities_pass
        ),
        "all_1888_nonboundary_KKT_conditions_are_interval_positive": (
            all_interval_conditions_pass
            and total_nonboundary_conditions == 1888
        ),
        "all_20_independent_midpoint_KKT_checks_pass": (
            all_midpoints_pass
        ),
        "only_M40_M57_M74_windows_contain_s0": (
            windows_containing_s0 == [40, 57, 74]
        ),
        "all_other_17_windows_lie_strictly_below_s0": (
            len(windows_below_s0) == 17
            and set(windows_below_s0).isdisjoint({40, 57, 74})
        ),
        "A79_boundary_polynomials_reproduced_exactly": all(
            item["same_monic_primitive_polynomial"]
            and item["same_coefficient_hash"]
            for item in a79_reproduction
        ),
        "upper_adjacent_candidate_passes_at_all_20_outer_witnesses": (
            upper_adjacent_pass_count == 20
        ),
        "lower_adjacent_candidate_failure_exception_is_exactly_M10_M15": (
            lower_adjacent_pass_count == 18
            and [
                item["maximum"]
                for item in window_results
                if item["declared_adjacent_candidate_checks"]
                ["below_lower_boundary"]["status"] != "pass"
            ]
            == [10, 15]
        ),
        "finite_local_scope_preserved": (
            LOCAL_LOWER == sp.Rational(129, 1000)
            and LOCAL_UPPER == sp.Rational(133, 1000)
            and S0 == sp.Rational(131, 1000)
            and BISECTION_STEPS == 80
        ),
    }

    summary = {
        "audit": "A80_EXACT_LOCAL_COMPRESSION_WINDOW_ATLAS",
        "contract": {
            "M_min": 10,
            "M_max": 80,
            "contact_source": (
                "A78 unique strict-KKT selected contact k(M) at s0"
            ),
            "local_s_interval": [str(LOCAL_LOWER), str(LOCAL_UPPER)],
            "s0": str(S0),
            "alpha_interval_decimal": [
                f"{-math.log2(float(LOCAL_UPPER)):.15f}",
                f"{-math.log2(float(LOCAL_LOWER)):.15f}",
            ],
            "mean": "M/2",
            "target_exponent": 1,
            "beta_exponent": 3,
            "gamma_exponent": 4,
            "epsilon_even": "1/(1875*2^(M/2))",
            "epsilon_odd": "1/(2500*2^floor(M/2))",
        },
        "boundary_law": {
            "even_M_2h": (
                "F^±_{M,k}(s)=c_M s^(2h)+c_{h+1} s^(h+1)+"
                "c_h s^h+c_k s^k+c_1 s+c_0"
            ),
            "odd_M_2h_plus_1": (
                "F^±_{M,k}(s)=c_M s^(2h+1)+c_{h+1} s^(h+1)+"
                "c_h s^h+c_k s^k+c_1 s+c_0"
            ),
            "coefficient_definition": (
                "Each coefficient is the exact signed cofactor generated by "
                "the corresponding alpha-row monomial in the entering-atom "
                "Cramer determinant."
            ),
            "scope": (
                "The six-term support law is certified here for all 142 "
                "selected-contact boundary polynomials; no closed all-M "
                "formula for the six coefficients is claimed."
            ),
        },
        "selected_contact_count": len(selected),
        "boundary_polynomial_count": len(boundary_catalogue),
        "root_class_counts": root_class_counts,
        "exact_compression_window_count": len(window_results),
        "compression_window_supports": [
            item["maximum"] for item in window_results
        ],
        "windows_containing_s0": windows_containing_s0,
        "windows_below_s0": windows_below_s0,
        "total_nonboundary_interval_KKT_conditions": (
            total_nonboundary_conditions
        ),
        "lower_adjacent_candidate_pass_count": lower_adjacent_pass_count,
        "upper_adjacent_candidate_pass_count": upper_adjacent_pass_count,
        "contact_records": contact_records,
        "window_results": window_results,
        "A79_reproduction": a79_reproduction,
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": (
            "PASS_EXACT_LOCAL_COMPRESSION_WINDOW_ATLAS_AND_SIX_TERM_BOUNDARY_LAW"
            if all(gates.values())
            else "FAIL"
        ),
        "claim_boundary": [
            "Exact only for integer supports 10<=M<=80.",
            "Exact only for the contact k(M) selected by A78 at s0.",
            "Exact only on the local interval 129/1000<=s<=133/1000.",
            "Twenty local compression windows do not imply periodicity in M.",
            "The lower Cramer contact-entry equation does not by itself make "
            "the declared adjacent branch globally KKT-valid; M=10 and M=15 "
            "are exact counterexamples within this atlas.",
            "No physical ontology or experimental interpretation is inferred.",
        ],
    }

    polynomial_output = {
        "audit": "A80_SIX_TERM_BOUNDARY_POLYNOMIAL_CATALOGUE",
        "normalization": (
            "primitive integer polynomial with positive leading coefficient"
        ),
        "local_interval": [str(LOCAL_LOWER), str(LOCAL_UPPER)],
        "polynomial_count": len(boundary_catalogue),
        "polynomials": boundary_catalogue,
    }
    condition_output = {
        "audit": "A80_INTERVAL_KKT_CONDITION_CERTIFICATES",
        "window_count": len(window_results),
        "condition_certificate_count": len(interval_condition_certificates),
        "certificates": interval_condition_certificates,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    result_path = OUTPUT_DIR / "a80_local_compression_window_atlas_results.json"
    polynomial_path = OUTPUT_DIR / "a80_boundary_polynomial_catalogue.json"
    condition_path = OUTPUT_DIR / "a80_interval_KKT_condition_certificates.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    polynomial_path.write_text(
        json.dumps(polynomial_output, indent=2),
        encoding="utf-8",
    )
    condition_path.write_text(
        json.dumps(condition_output, indent=2),
        encoding="utf-8",
    )

    print(json.dumps({
        "audit": summary["audit"],
        "boundary_polynomial_count": len(boundary_catalogue),
        "exact_compression_window_count": len(window_results),
        "windows_containing_s0": windows_containing_s0,
        "total_nonboundary_interval_KKT_conditions": (
            total_nonboundary_conditions
        ),
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": summary["verdict"],
        "result": result_path.name,
        "polynomials": polynomial_path.name,
        "condition_certificates": condition_path.name,
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
