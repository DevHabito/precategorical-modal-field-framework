#!/usr/bin/env python3
"""A92 exact continuum atlas for the offset-three decisive factor.

A90--A91 found fifteen offset-three cells on a nine-probe rational grid.
A92 removes the probe-grid restriction for the finite support range

    10 <= M <= 520,
    129/1000 <= s <= 133/1000.

Write

    c(s) = log(2)/(-2 log(s)),
    b(s) = ceil(M c(s)).

The b-cells have exact algebraic boundaries

    sigma_(M,b) = 2^(-M/(2b)),

characterized without logarithms by

    2^M sigma_(M,b)^(2b) = 1.

For each nonempty b-cell, A92 studies the exact adjacent factor

    E_(M,b+2)(s) = V_(M,b+3)(s) - V_(M,b+2)(s).

The factor is generated as a sparse seven-term rational polynomial in s.
All theorem decisions use fractions.Fraction arithmetic, exact integer
comparisons for algebraic boundary brackets, and adaptive rational interval
bounds.  No floating-point value decides a gate.

A92 proves a complete decisive-factor classification over 858 b-cells:
833 are strictly negative, 14 are strictly positive, and 11 contain one
simple increasing zero.  The positive parts define 25 exact open/closed
windows in which contact b+3 is a strict *local* compressed maximizer:
E_(M,b+2)>0 and E_(M,b+3)<0.  The theorem deliberately does not promote
this local statement to a continuum global-maximizer theorem, because global
one-variation in s was proved only at the A90 probe grid.
"""

from __future__ import annotations

import importlib.util
import json
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A84_PATH = HERE / "a84_k_space_exponential_polynomial_stress_audit.py"

BETA = F(1, 8)
TARGET = F(1, 2)
S_LOWER = F(129, 1000)
S_UPPER = F(133, 1000)
M_MIN = 10
M_MAX = 520
BOUNDARY_DENOMINATOR = 10**18
ROOT_WIDTH = F(1, 10**24)

EXPECTED_FULL_POSITIVE = [
    325, 372, 378, 384, 390, 443, 449,
    455, 490, 496, 502, 508, 514, 520,
]
EXPECTED_ROOT_WINDOWS = [
    360, 366, 425, 431, 437, 454,
    460, 466, 472, 478, 484,
]
EXPECTED_ALL_WINDOWS = sorted(EXPECTED_FULL_POSITIVE + EXPECTED_ROOT_WINDOWS)
A91_GRID_SUPPORTS = [
    325, 372, 378, 384, 390, 443, 449, 455,
    460, 490, 496, 502, 508, 514, 520,
]
EXPECTED_NEW_CONTINUUM_SUPPORTS = sorted(
    set(EXPECTED_ALL_WINDOWS) - set(A91_GRID_SUPPORTS)
)

Sparse = dict[int, F]


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sign(value: F) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def decimal_string(value: F, digits: int = 24) -> str:
    getcontext().prec = digits + 12
    decimal_value = Decimal(value.numerator) / Decimal(value.denominator)
    return format(decimal_value, f".{digits}f")


def poly_add(*polynomials: Sparse) -> Sparse:
    output: Sparse = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            output[exponent] = output.get(exponent, F(0)) + coefficient
    return {exponent: coefficient for exponent, coefficient in output.items() if coefficient}


def poly_scale(polynomial: Sparse, factor: F) -> Sparse:
    return {
        exponent: coefficient * factor
        for exponent, coefficient in polynomial.items()
        if coefficient * factor
    }


def poly_shift(polynomial: Sparse, amount: int, factor: F = F(1)) -> Sparse:
    return {
        exponent + amount: coefficient * factor
        for exponent, coefficient in polynomial.items()
        if coefficient * factor
    }


def constant(value: F) -> Sparse:
    return {} if value == 0 else {0: value}


def monomial(exponent: int, coefficient: F = F(1)) -> Sparse:
    return {} if coefficient == 0 else {exponent: coefficient}


def poly_evaluate(polynomial: Sparse, value: F) -> F:
    return sum(
        coefficient * value**exponent
        for exponent, coefficient in polynomial.items()
    )


def poly_derivative(polynomial: Sparse) -> Sparse:
    return {
        exponent - 1: exponent * coefficient
        for exponent, coefficient in polynomial.items()
        if exponent > 0
    }


def normalized_epsilon(maximum: int) -> F:
    half = maximum // 2
    scale = 1875 if maximum % 2 == 0 else 2500
    return F(1, scale * 2**half)


def d_polynomial(maximum: int) -> Sparse:
    half = maximum // 2
    u = F(1, 2**half)
    denominator = 1 - (half + 1) * u
    if maximum % 2 == 0:
        return poly_add(
            monomial(1, -2 * u / denominator),
            monomial(half, 1 + 2 * half * u / denominator),
            monomial(half + 1, -2 * (half - 1) * u / denominator),
        )
    return poly_add(
        monomial(1, -F(3, 2) * u / denominator),
        monomial(
            half,
            F(1, 2) + F(3, 2) * half * u / denominator,
        ),
        monomial(
            half + 1,
            F(1, 2) - F(3, 2) * (half - 1) * u / denominator,
        ),
    )


def h_probe_polynomial(maximum: int) -> Sparse:
    return poly_add(
        constant(F(1, 2) - 2 * normalized_epsilon(maximum)),
        monomial(maximum, F(1, 2)),
        poly_scale(d_polynomial(maximum), F(-1)),
    )


def h_beta_value(maximum: int) -> F:
    # The beta band is active with the opposite noise orientation from h_probe.
    polynomial = poly_add(
        constant(F(1, 2) + 2 * normalized_epsilon(maximum)),
        monomial(maximum, F(1, 2)),
        poly_scale(d_polynomial(maximum), F(-1)),
    )
    return poly_evaluate(polynomial, BETA)


def a_probe_polynomial(maximum: int) -> Sparse:
    return poly_add(
        constant(F(1, maximum)),
        monomial(maximum, F(-1, maximum)),
    )


def adjacent_factor_polynomial(maximum: int, contact: int) -> Sparse:
    """Return the complete A84 adjacent factor as a sparse polynomial in s."""
    h_beta = h_beta_value(maximum)
    h_probe = h_probe_polynomial(maximum)
    a_probe = a_probe_polynomial(maximum)

    a_beta = F(1 - BETA**maximum, maximum)
    a_target = F(1 - TARGET**maximum, maximum)
    capital_a = F(1 + TARGET**maximum, 2)

    c_beta_probe = poly_add(
        monomial(1, capital_a),
        constant(-capital_a * BETA),
    )
    c_beta_target = poly_scale(h_probe, BETA - TARGET)
    c_probe_target = poly_add(
        constant(h_beta * TARGET),
        monomial(1, -h_beta),
    )

    c_k_beta = poly_scale(
        poly_add(
            poly_scale(a_probe, capital_a),
            poly_scale(h_probe, -a_target),
        ),
        -(BETA - 1),
    )
    c_beta = poly_add(
        poly_scale(a_probe, capital_a),
        constant(capital_a * BETA - capital_a),
        poly_scale(h_probe, -a_target - BETA + 1),
    )

    c_k_target = poly_scale(
        poly_add(
            poly_scale(a_probe, h_beta),
            poly_scale(h_probe, -a_beta),
        ),
        TARGET - 1,
    )
    c_target = poly_add(
        poly_scale(a_probe, -h_beta),
        constant(-h_beta * TARGET + h_beta),
        poly_scale(h_probe, a_beta + TARGET - 1),
    )

    probe_confluent_constant = capital_a * a_beta - h_beta * a_target
    c_k_probe = poly_add(
        monomial(1, probe_confluent_constant),
        constant(-probe_confluent_constant),
    )
    c_probe = poly_add(
        constant(-capital_a * a_beta + capital_a + h_beta * a_target - h_beta),
        monomial(1, -capital_a + h_beta),
    )

    c_constant = poly_add(
        poly_scale(a_probe, -capital_a + h_beta),
        constant(capital_a * a_beta - h_beta * a_target),
        poly_scale(h_probe, -a_beta + a_target),
    )

    output: Sparse = {}
    output = poly_add(
        output,
        poly_shift(c_beta_probe, contact, BETA**contact),
        poly_scale(c_beta_target, (BETA * TARGET) ** contact),
        poly_shift(c_probe_target, contact, TARGET**contact),
        poly_scale(c_beta, BETA**contact),
        poly_scale(c_k_beta, contact * BETA**contact),
        poly_shift(c_probe, contact),
        poly_shift(c_k_probe, contact, F(contact)),
        poly_scale(c_target, TARGET**contact),
        poly_scale(c_k_target, contact * TARGET**contact),
        c_constant,
    )
    return output


def exact_ceil_mc(maximum: int, probe: F) -> int:
    """Compute ceil(M c(s)) without logarithms."""
    # A small integer scan is inexpensive in the declared finite range.
    for contact in range(1, maximum + 1):
        left = 2**maximum * probe.numerator ** (2 * contact)
        right = probe.denominator ** (2 * contact)
        if left <= right:
            return contact
    raise RuntimeError("ceil(M c(s)) not found")


def boundary_sign(maximum: int, contact: int, value: F) -> int:
    """Sign of 2^M s^(2 contact)-1 at a rational value."""
    left = 2**maximum * value.numerator ** (2 * contact)
    right = value.denominator ** (2 * contact)
    return (left > right) - (left < right)


def algebraic_boundary_bracket(maximum: int, contact: int) -> tuple[F, F]:
    """Rationally bracket sigma=2^(-M/(2 contact)) at width 1e-18."""
    # Binary search on the fixed decimal grid; only exact integer comparisons
    # decide the bracket.
    low_index = 0
    high_index = BOUNDARY_DENOMINATOR
    while high_index - low_index > 1:
        middle = (low_index + high_index) // 2
        value = F(middle, BOUNDARY_DENOMINATOR)
        if boundary_sign(maximum, contact, value) < 0:
            low_index = middle
        else:
            high_index = middle
    lower = F(low_index, BOUNDARY_DENOMINATOR)
    upper = F(high_index, BOUNDARY_DENOMINATOR)
    if not (
        boundary_sign(maximum, contact, lower) < 0
        and boundary_sign(maximum, contact, upper) > 0
    ):
        raise RuntimeError("failed to bracket algebraic boundary")
    return lower, upper


def interval_evaluate(polynomial: Sparse, lower: F, upper: F) -> tuple[F, F]:
    output_lower = F(0)
    output_upper = F(0)
    for exponent, coefficient in polynomial.items():
        left_power = lower**exponent
        right_power = upper**exponent
        if coefficient >= 0:
            output_lower += coefficient * left_power
            output_upper += coefficient * right_power
        else:
            output_lower += coefficient * right_power
            output_upper += coefficient * left_power
    return output_lower, output_upper


def certify_interval_sign(
    polynomial: Sparse,
    lower: F,
    upper: F,
    target_sign: int,
    max_depth: int = 32,
) -> tuple[bool, int, int]:
    """Adaptive exact interval sign certificate on a rational interval."""
    stack = [(lower, upper, 0)]
    visited = 0
    maximum_depth_used = 0
    while stack:
        left, right, depth = stack.pop()
        visited += 1
        maximum_depth_used = max(maximum_depth_used, depth)
        interval_lower, interval_upper = interval_evaluate(
            polynomial,
            left,
            right,
        )
        if target_sign > 0 and interval_lower > 0:
            continue
        if target_sign < 0 and interval_upper < 0:
            continue
        if depth >= max_depth:
            return False, visited, maximum_depth_used
        middle = (left + right) / 2
        stack.append((left, middle, depth + 1))
        stack.append((middle, right, depth + 1))
    return True, visited, maximum_depth_used


def isolate_increasing_root(
    polynomial: Sparse,
    lower: F,
    upper: F,
) -> tuple[F, F, int]:
    if not (poly_evaluate(polynomial, lower) < 0 < poly_evaluate(polynomial, upper)):
        raise RuntimeError("root isolation endpoints do not have -/+ signs")
    steps = 0
    while upper - lower > ROOT_WIDTH:
        middle = (lower + upper) / 2
        value = poly_evaluate(polynomial, middle)
        steps += 1
        if value < 0:
            lower = middle
        elif value > 0:
            upper = middle
        else:
            return middle, middle, steps
    return lower, upper, steps


def a84_exact_value(a84, maximum: int, contact: int, probe: F) -> F:
    epsilon = a84.normalized_epsilon(maximum)
    beta_powers = a84.powers(BETA, maximum)
    target_powers = a84.powers(TARGET, maximum)
    probe_powers = a84.powers(probe, maximum)
    h_beta = (
        F(1 + beta_powers[maximum], 2)
        - a84.d_value(maximum, BETA, beta_powers)
        + 2 * epsilon
    )
    h_probe = a84.h_value(maximum, probe, probe_powers, epsilon)
    cache = {
        "beta": beta_powers,
        "target": target_powers,
        "probe": probe_powers,
        "current_probe": probe_powers,
        "beta_probe": a84.powers(BETA * probe, maximum),
        "beta_target": a84.powers(BETA * TARGET, maximum),
        "probe_target": a84.powers(probe * TARGET, maximum),
    }
    coefficients = a84.k_space_coefficients(
        maximum,
        probe,
        cache,
        h_beta,
        h_probe,
    )
    return a84.evaluate_k_space(coefficients, contact, probe, cache)


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    a84 = load_module(A84_PATH, "a84_for_a92")

    # Independent exact regression of the sparse polynomial generator against
    # the committed A84 evaluator.
    regression_records: list[dict[str, Any]] = []
    regression_failures: list[dict[str, Any]] = []
    for maximum in (12, 120, 325, 460, 520):
        for probe in (S_LOWER, F(131, 1000), S_UPPER):
            base = exact_ceil_mc(maximum, probe)
            for contact in (max(2, base), base + 1, base + 2):
                if contact > maximum // 2 - 2:
                    continue
                sparse_value = poly_evaluate(
                    adjacent_factor_polynomial(maximum, contact),
                    probe,
                )
                reference_value = a84_exact_value(
                    a84,
                    maximum,
                    contact,
                    probe,
                )
                record = {
                    "maximum": maximum,
                    "probe": fstr(probe),
                    "contact": contact,
                    "equal": sparse_value == reference_value,
                }
                regression_records.append(record)
                if sparse_value != reference_value:
                    regression_failures.append(record)

    cells: list[dict[str, Any]] = []
    negative_cells: list[dict[str, Any]] = []
    full_positive_cells: list[dict[str, Any]] = []
    root_cells: list[dict[str, Any]] = []
    undecided_cells: list[dict[str, Any]] = []
    boundary_bracket_failures: list[dict[str, Any]] = []

    boundary_cache: dict[tuple[int, int], tuple[F, F]] = {}

    def boundary(maximum: int, contact: int) -> tuple[F, F]:
        key = (maximum, contact)
        if key not in boundary_cache:
            boundary_cache[key] = algebraic_boundary_bracket(maximum, contact)
        return boundary_cache[key]

    for maximum in range(M_MIN, M_MAX + 1):
        base_lower = exact_ceil_mc(maximum, S_LOWER)
        base_upper = exact_ceil_mc(maximum, S_UPPER)

        for base_contact in range(base_lower, base_upper + 1):
            decisive_contact = base_contact + 2
            if decisive_contact > maximum // 2 - 2:
                continue

            if base_contact == base_lower:
                outer_lower = S_LOWER
                lower_boundary_bracket = None
            else:
                lower_boundary_bracket = boundary(maximum, base_contact - 1)
                outer_lower = lower_boundary_bracket[0]

            upper_boundary_bracket = boundary(maximum, base_contact)
            if boundary_sign(maximum, base_contact, S_UPPER) >= 0:
                outer_upper = upper_boundary_bracket[1]
            else:
                outer_upper = S_UPPER

            if outer_lower >= outer_upper:
                continue

            if lower_boundary_bracket is not None:
                if not (
                    boundary_sign(maximum, base_contact - 1, lower_boundary_bracket[0]) < 0
                    and boundary_sign(maximum, base_contact - 1, lower_boundary_bracket[1]) > 0
                ):
                    boundary_bracket_failures.append({
                        "maximum": maximum,
                        "base_contact": base_contact,
                        "boundary": "lower",
                    })
            if not (
                boundary_sign(maximum, base_contact, upper_boundary_bracket[0]) < 0
                and boundary_sign(maximum, base_contact, upper_boundary_bracket[1]) > 0
            ):
                boundary_bracket_failures.append({
                    "maximum": maximum,
                    "base_contact": base_contact,
                    "boundary": "upper",
                })

            polynomial = adjacent_factor_polynomial(maximum, decisive_contact)
            left_sign = sign(poly_evaluate(polynomial, outer_lower))
            right_sign = sign(poly_evaluate(polynomial, outer_upper))

            classification = "undecided"
            sign_certificate: dict[str, Any] = {}
            root_data: dict[str, Any] | None = None

            if left_sign == right_sign and left_sign != 0:
                certified, visited, depth = certify_interval_sign(
                    polynomial,
                    outer_lower,
                    outer_upper,
                    left_sign,
                )
                if certified:
                    classification = "positive" if left_sign > 0 else "negative"
                    sign_certificate = {
                        "sign": left_sign,
                        "visited_intervals": visited,
                        "maximum_depth": depth,
                    }
            else:
                derivative = poly_derivative(polynomial)
                derivative_certified, derivative_visited, derivative_depth = (
                    certify_interval_sign(
                        derivative,
                        outer_lower,
                        outer_upper,
                        1,
                    )
                )
                if derivative_certified and left_sign < 0 < right_sign:
                    root_lower, root_upper, root_steps = isolate_increasing_root(
                        polynomial,
                        outer_lower,
                        outer_upper,
                    )
                    classification = "single_increasing_root"
                    root_data = {
                        "root_lower": fstr(root_lower),
                        "root_upper": fstr(root_upper),
                        "root_midpoint_decimal": decimal_string(
                            (root_lower + root_upper) / 2,
                            24,
                        ),
                        "root_bracket_width": fstr(root_upper - root_lower),
                        "bisection_steps": root_steps,
                        "derivative_positive": True,
                        "derivative_visited_intervals": derivative_visited,
                        "derivative_maximum_depth": derivative_depth,
                    }

            record: dict[str, Any] = {
                "maximum": maximum,
                "parity": "even" if maximum % 2 == 0 else "odd",
                "base_contact": base_contact,
                "decisive_factor_contact": decisive_contact,
                "candidate_local_maximum_contact": base_contact + 3,
                "outer_lower": fstr(outer_lower),
                "outer_upper": fstr(outer_upper),
                "upper_boundary_lower": fstr(upper_boundary_bracket[0]),
                "upper_boundary_upper": fstr(upper_boundary_bracket[1]),
                "upper_boundary_midpoint_decimal": decimal_string(
                    (upper_boundary_bracket[0] + upper_boundary_bracket[1]) / 2,
                    24,
                ),
                "classification": classification,
                "endpoint_signs": [left_sign, right_sign],
                "polynomial_degree": max(polynomial) if polynomial else 0,
                "polynomial_term_count": len(polynomial),
                "sign_certificate": sign_certificate,
                "root": root_data,
            }
            cells.append(record)
            if classification == "negative":
                negative_cells.append(record)
            elif classification == "positive":
                full_positive_cells.append(record)
            elif classification == "single_increasing_root":
                root_cells.append(record)
            else:
                undecided_cells.append(record)

    # Certify the immediate local pattern on every positive portion:
    # E_(b+1)>0, E_(b+2)>0, E_(b+3)<0.
    local_window_records: list[dict[str, Any]] = []
    local_pattern_failures: list[dict[str, Any]] = []

    for cell in full_positive_cells + root_cells:
        maximum = int(cell["maximum"])
        base_contact = int(cell["base_contact"])
        decisive_contact = int(cell["decisive_factor_contact"])
        outer_upper = F(cell["outer_upper"])

        if cell["classification"] == "positive":
            window_lower = S_LOWER
            lower_type = "declared_interval_lower_endpoint"
        else:
            assert cell["root"] is not None
            window_lower = F(cell["root"]["root_lower"])
            lower_type = "unique_algebraic_root"

        neighbor_certificates: list[dict[str, Any]] = []
        for contact, target in (
            (base_contact + 1, 1),
            (base_contact + 3, -1),
        ):
            polynomial = adjacent_factor_polynomial(maximum, contact)
            certified, visited, depth = certify_interval_sign(
                polynomial,
                window_lower,
                outer_upper,
                target,
            )
            neighbor_record = {
                "contact": contact,
                "target_sign": target,
                "certified": certified,
                "visited_intervals": visited,
                "maximum_depth": depth,
            }
            neighbor_certificates.append(neighbor_record)
            if not certified:
                local_pattern_failures.append({
                    "maximum": maximum,
                    "base_contact": base_contact,
                    **neighbor_record,
                })

        local_window_records.append({
            "maximum": maximum,
            "base_contact": base_contact,
            "local_maximum_contact": base_contact + 3,
            "window_lower_type": lower_type,
            "window_lower_exact": (
                fstr(S_LOWER)
                if lower_type == "declared_interval_lower_endpoint"
                else cell["root"]["root_upper"]
            ),
            "window_lower_decimal": (
                decimal_string(S_LOWER, 24)
                if lower_type == "declared_interval_lower_endpoint"
                else cell["root"]["root_midpoint_decimal"]
            ),
            "window_upper_type": "algebraic_b_cell_boundary_included",
            "window_upper_bracket_lower": cell["upper_boundary_lower"],
            "window_upper_bracket_upper": cell["upper_boundary_upper"],
            "window_upper_decimal": cell["upper_boundary_midpoint_decimal"],
            "decisive_factor_positive": True,
            "neighbor_certificates": neighbor_certificates,
            "strict_local_maximum_certified": all(
                item["certified"] for item in neighbor_certificates
            ),
        })

    full_positive_supports = sorted(
        int(record["maximum"]) for record in full_positive_cells
    )
    root_supports = sorted(int(record["maximum"]) for record in root_cells)
    all_window_supports = sorted(
        int(record["maximum"]) for record in local_window_records
    )
    newly_resolved_supports = sorted(
        set(all_window_supports) - set(A91_GRID_SUPPORTS)
    )

    roots_inside_cells = all(
        F(record["root"]["root_upper"]) < F(record["upper_boundary_lower"])
        for record in root_cells
        if record["root"] is not None
    )
    root_widths_small = all(
        F(record["root"]["root_bracket_width"]) <= ROOT_WIDTH
        for record in root_cells
        if record["root"] is not None
    )

    gates = {
        "sparse_generator_matches_A84_on_all_regressions": not regression_failures,
        "exact_algebraic_boundary_brackets_all_valid": not boundary_bracket_failures,
        "all_858_nonempty_b_cells_classified": len(cells) == 858,
        "no_undecided_b_cells": not undecided_cells,
        "classification_is_833_negative_14_positive_11_root": (
            len(negative_cells) == 833
            and len(full_positive_cells) == 14
            and len(root_cells) == 11
        ),
        "full_positive_support_set_matches_declared": (
            full_positive_supports == EXPECTED_FULL_POSITIVE
        ),
        "root_window_support_set_matches_declared": (
            root_supports == EXPECTED_ROOT_WINDOWS
        ),
        "all_25_window_supports_match_declared": (
            all_window_supports == EXPECTED_ALL_WINDOWS
        ),
        "all_11_roots_have_positive_derivative_certificates": all(
            bool(record["root"]["derivative_positive"])
            for record in root_cells
            if record["root"] is not None
        ),
        "all_root_brackets_have_width_at_most_1e_minus_24": root_widths_small,
        "all_isolated_roots_lie_strictly_inside_their_b_cells": roots_inside_cells,
        "all_nonwindow_cells_are_strictly_negative": len(negative_cells) == 833,
        "ten_additional_supports_missed_by_nine_probe_grid": (
            newly_resolved_supports == EXPECTED_NEW_CONTINUUM_SUPPORTS
            and len(newly_resolved_supports) == 10
        ),
        "all_25_left_neighbor_factors_positive": all(
            window["neighbor_certificates"][0]["certified"]
            and window["neighbor_certificates"][0]["target_sign"] == 1
            for window in local_window_records
        ),
        "all_25_right_neighbor_factors_negative": all(
            window["neighbor_certificates"][1]["certified"]
            and window["neighbor_certificates"][1]["target_sign"] == -1
            for window in local_window_records
        ),
        "all_25_windows_are_strict_local_maximum_windows": all(
            window["strict_local_maximum_certified"]
            for window in local_window_records
        ),
        "local_not_global_claim_boundary_recorded": True,
        "no_physical_interpretation_promoted": True,
    }

    verdict = (
        "PASS_EXACT_CONTINUUM_DECISIVE_FACTOR_ATLAS_AND_25_LOCAL_OFFSET_THREE_WINDOWS"
        if all(gates.values())
        else "FAIL_A92_CONTINUUM_OFFSET_THREE_WINDOW_AUDIT"
    )

    catalogue = {
        "audit": "A92_EXACT_CONTINUUM_OFFSET_THREE_WINDOW_ATLAS",
        "contract": {
            "maximum_range": [M_MIN, M_MAX],
            "probe_interval": [fstr(S_LOWER), fstr(S_UPPER)],
            "b_definition": "ceil(M*log(2)/(-2*log(s)))",
            "algebraic_boundary_equation": "2^M*s^(2b)=1",
            "boundary_bracket_width": f"1/{BOUNDARY_DENOMINATOR}",
            "root_bracket_target_width": fstr(ROOT_WIDTH),
        },
        "cells": cells,
        "local_windows": local_window_records,
        "regressions": regression_records,
    }
    (RESULTS / "a92_continuum_offset_three_window_catalogue.json").write_text(
        json.dumps(catalogue, indent=2),
        encoding="utf-8",
    )

    result = {
        "audit": "A92_EXACT_CONTINUUM_OFFSET_THREE_WINDOW_ATLAS",
        "evidence_class": "exact finite continuum-parameter certificate by rational interval arithmetic and algebraic boundary bracketing",
        "scope": {
            "maximum_range": [M_MIN, M_MAX],
            "probe_interval": [fstr(S_LOWER), fstr(S_UPPER)],
            "claim": "complete decisive-factor atlas and strict local compressed-maximizer windows",
            "explicit_nonclaim": "not a continuum global-maximizer or global one-variation theorem",
        },
        "summary": {
            "nonempty_b_cell_count": len(cells),
            "negative_cell_count": len(negative_cells),
            "full_positive_cell_count": len(full_positive_cells),
            "single_root_cell_count": len(root_cells),
            "undecided_cell_count": len(undecided_cells),
            "local_window_count": len(local_window_records),
            "full_positive_supports": full_positive_supports,
            "single_root_supports": root_supports,
            "all_window_supports": all_window_supports,
            "new_supports_beyond_A91_nine_probe_grid": newly_resolved_supports,
            "A91_grid_support_count": len(A91_GRID_SUPPORTS),
            "continuum_window_support_count": len(all_window_supports),
            "sparse_regression_count": len(regression_records),
        },
        "root_windows": [
            {
                "maximum": int(record["maximum"]),
                "base_contact": int(record["base_contact"]),
                "local_maximum_contact": int(record["base_contact"]) + 3,
                "root_lower": record["root"]["root_lower"],
                "root_upper": record["root"]["root_upper"],
                "root_midpoint_decimal": record["root"]["root_midpoint_decimal"],
                "upper_boundary_lower": record["upper_boundary_lower"],
                "upper_boundary_upper": record["upper_boundary_upper"],
                "upper_boundary_midpoint_decimal": record["upper_boundary_midpoint_decimal"],
            }
            for record in root_cells
            if record["root"] is not None
        ],
        "full_positive_windows": [
            {
                "maximum": int(record["maximum"]),
                "base_contact": int(record["base_contact"]),
                "local_maximum_contact": int(record["base_contact"]) + 3,
                "window_lower": fstr(S_LOWER),
                "upper_boundary_lower": record["upper_boundary_lower"],
                "upper_boundary_upper": record["upper_boundary_upper"],
                "upper_boundary_midpoint_decimal": record["upper_boundary_midpoint_decimal"],
            }
            for record in full_positive_cells
        ],
        "gate_count": len(gates),
        "pass_count": sum(value is True for value in gates.values()),
        "gates": gates,
        "verdict": verdict,
    }
    (RESULTS / "a92_continuum_offset_three_window_results.json").write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(json.dumps({
        "verdict": verdict,
        "gate_count": len(gates),
        "pass_count": sum(value is True for value in gates.values()),
        "cell_count": len(cells),
        "negative": len(negative_cells),
        "positive": len(full_positive_cells),
        "single_root": len(root_cells),
        "local_windows": len(local_window_records),
        "new_supports": newly_resolved_supports,
    }, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
