#!/usr/bin/env python3
"""A79 exact compression-interval and contact-entry audit.

A78 found three gamma-inactive compression supports at the exact probe

    s0 = 131/1000,

namely M=40,57,74.  A79 upgrades those pointwise certificates to exact
connected interval theorems.  For each support it:

1. builds the selected compressed branch

       P={0,k,M}, Q={1,h,h+1}, active={alpha+,beta-};

2. isolates the two algebraic boundary roots at which the inactive gamma
   slacks vanish;
3. performs a complete exact root census for every numerator and denominator
   of every full-LP KKT condition on the enclosing rational hull;
4. proves that the resulting open algebraic interval is the maximal connected
   strict-KKT component containing s0;
5. proves that each boundary polynomial is exactly the Cramer numerator of the
   atom entering in the adjacent three-band branch; and
6. supplies exact rational witnesses immediately outside the compression
   interval where the adjacent branches pass the complete strict KKT test.

The result is exact for M in {40,57,74} under the frozen central-mean contract.
It is not an all-M theorem and does not establish periodicity of compression
supports.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE.parent / "results" if HERE.name == "audits" else HERE
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"
A78_SCRIPT = HERE / "a78_rational_probe_contact_selection_audit.py"

S0 = sp.Rational(131, 1000)
SEARCH_LOWER = sp.Rational(129, 1000)
SEARCH_UPPER = sp.Rational(133, 1000)
ROOT_EPS = sp.Rational(1, 10**18)
SUPPORTS = {
    40: 9,
    57: 12,
    74: 15,
}


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
    if maximum % 2 == 0:
        return sp.Rational(1, 1875 * 2**h)
    return sp.Rational(1, 2500 * 2**h)


def target_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2**x)


def beta_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (3 * x))


def gamma_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (4 * x))


def primitive_integer_poly(expression: sp.Expr, variable: sp.Symbol) -> sp.Poly:
    numerator, _ = sp.fraction(sp.cancel(expression))
    polynomial = sp.Poly(numerator, variable, domain=sp.QQ)
    _, integer_poly = polynomial.clear_denoms(convert=True)
    _, primitive_expression = sp.primitive(integer_poly.as_expr(), variable)
    primitive_poly = sp.Poly(primitive_expression, variable, domain=sp.ZZ)
    if primitive_poly.LC() < 0:
        primitive_poly = -primitive_poly
    return primitive_poly


def monic_poly(expression: sp.Expr, variable: sp.Symbol) -> sp.Poly:
    return primitive_integer_poly(expression, variable).monic()


def polynomial_record(polynomial: sp.Poly) -> dict[str, Any]:
    coefficients = [str(value) for value in polynomial.all_coeffs()]
    canonical = json.dumps(coefficients, separators=(",", ":"))
    return {
        "degree": polynomial.degree(),
        "leading_coefficient": str(polynomial.LC()),
        "coefficient_count": len(coefficients),
        "coefficients_descending": coefficients,
        "coefficient_sha256": hashlib.sha256(
            canonical.encode("utf-8")
        ).hexdigest(),
    }


def isolate_one_root(
    polynomial: sp.Poly,
    lower: sp.Rational = SEARCH_LOWER,
    upper: sp.Rational = SEARCH_UPPER,
) -> tuple[tuple[sp.Rational, sp.Rational], int]:
    intervals = polynomial.intervals(
        eps=ROOT_EPS,
        inf=lower,
        sup=upper,
        fast=True,
    )
    if len(intervals) != 1:
        raise RuntimeError(
            f"Expected one root for degree-{polynomial.degree()} polynomial, "
            f"found {intervals}"
        )
    interval, multiplicity = intervals[0]
    return (sp.Rational(interval[0]), sp.Rational(interval[1])), int(multiplicity)


def interval_record(interval: tuple[sp.Rational, sp.Rational]) -> dict[str, Any]:
    lower, upper = interval
    midpoint = (lower + upper) / 2
    return {
        "lower": str(lower),
        "upper": str(upper),
        "width": str(upper - lower),
        "midpoint_decimal": f"{float(midpoint):.18f}",
    }


def alpha_interval_record(
    s_lower: tuple[sp.Rational, sp.Rational],
    s_upper: tuple[sp.Rational, sp.Rational],
) -> dict[str, str]:
    # alpha=-log2(s), so the ordering reverses.
    alpha_lower = -math.log2(float(sum(s_upper) / 2))
    alpha_upper = -math.log2(float(sum(s_lower) / 2))
    return {
        "alpha_lower_decimal": f"{alpha_lower:.15f}",
        "alpha_upper_decimal": f"{alpha_upper:.15f}",
    }


def root_count(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
) -> int:
    if polynomial.degree() <= 0:
        return 0
    intervals = polynomial.intervals(
        inf=lower,
        sup=upper,
        fast=True,
    )
    return int(sum(multiplicity for _, multiplicity in intervals))


def exact_floor(value: sp.Rational, denominator: int) -> sp.Rational:
    numerator = (value * denominator).p // (value * denominator).q
    return sp.Rational(numerator, denominator)


def exact_ceil(value: sp.Rational, denominator: int) -> sp.Rational:
    scaled = value * denominator
    numerator = -((-scaled.p) // scaled.q)
    return sp.Rational(numerator, denominator)


def cramer_entering_atom_polynomial(
    maximum: int,
    contact: int,
    gamma_sign: int,
    entering_atom: int,
    variable: sp.Symbol,
) -> sp.Poly:
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    p_points = [0, contact, contact + 1, maximum]
    q_points = [1, h, h + 1]

    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [*p_points, 0, 0, 0, -mean],
        [0, 0, 0, 0, *q_points, -mean],
        [
            0, 0, 0, 0,
            *[target_value(x) for x in q_points],
            0,
        ],
        [
            *[variable**x for x in p_points],
            *[-variable**x for x in q_points],
            -2 * epsilon,
        ],
        [
            *[-beta_value(x) for x in p_points],
            *[beta_value(x) for x in q_points],
            -2 * epsilon,
        ],
        [
            *[gamma_sign * gamma_value(x) for x in p_points],
            *[-gamma_sign * gamma_value(x) for x in q_points],
            -2 * epsilon,
        ],
    ]

    basis = sp.Matrix(rows)
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
    entering_column = p_points.index(entering_atom)
    numerator_matrix = basis.copy()
    numerator_matrix[:, entering_column] = rhs
    determinant = numerator_matrix.det(method="domain-ge")
    return primitive_integer_poly(determinant, variable)


def full_root_census(
    conditions: list[tuple[str, sp.Expr]],
    variable: sp.Symbol,
    hull_lower: sp.Rational,
    hull_upper: sp.Rational,
    boundary_names: set[str],
) -> dict[str, Any]:
    cache: dict[tuple[str, ...], int] = {}
    failures: list[dict[str, Any]] = []
    checked_parts = 0
    denominator_root_count = 0
    nonboundary_numerator_root_count = 0

    for name, expression in conditions:
        numerator, denominator = sp.fraction(sp.cancel(expression))
        for part_name, part_expression in (
            ("numerator", numerator),
            ("denominator", denominator),
        ):
            polynomial = sp.Poly(part_expression, variable, domain=sp.QQ)
            key = tuple(str(value) for value in polynomial.all_coeffs())
            if key not in cache:
                cache[key] = root_count(
                    polynomial,
                    hull_lower,
                    hull_upper,
                )
            count = cache[key]
            checked_parts += 1

            expected = (
                1
                if part_name == "numerator" and name in boundary_names
                else 0
            )
            if part_name == "denominator":
                denominator_root_count += count
            elif name not in boundary_names:
                nonboundary_numerator_root_count += count

            if count != expected:
                failures.append({
                    "condition": name,
                    "part": part_name,
                    "root_count": count,
                    "expected_root_count": expected,
                    "degree": polynomial.degree(),
                })

    return {
        "condition_count": len(conditions),
        "checked_polynomial_parts": checked_parts,
        "unique_polynomials": len(cache),
        "denominator_root_count": denominator_root_count,
        "nonboundary_numerator_root_count": (
            nonboundary_numerator_root_count
        ),
        "failures": failures,
        "pass": not failures,
    }


def evaluate_adjacent_witness(
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
        "s": str(witness),
        "s_decimal": f"{float(witness):.10f}",
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
        "strict_pass_record": result.get("record"),
    }


def evaluate_compressed_witness(
    a78,
    maximum: int,
    contact: int,
    witness: sp.Rational,
) -> dict[str, Any]:
    original_probe = a78.S0
    a78.S0 = witness
    try:
        result = a78.evaluate_two_band(
            maximum,
            contact,
            collect_pass=True,
        )
    finally:
        a78.S0 = original_probe

    return {
        "s": str(witness),
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
    for required in (A67_SCRIPT, A78_SCRIPT):
        if not required.exists():
            raise FileNotFoundError(required)

    a67 = load_module(A67_SCRIPT, "a67_for_a79")
    a78 = load_module(A78_SCRIPT, "a78_for_a79")
    variable = a67.S

    support_results: list[dict[str, Any]] = []
    polynomial_results: list[dict[str, Any]] = []

    for maximum, contact in SUPPORTS.items():
        h = maximum // 2
        count = maximum + 1
        epsilon = normalized_epsilon(maximum)
        positive_indices = (
            0,
            contact,
            maximum,
            count + 1,
            count + h,
            count + h + 1,
            2 * count,
        )
        branch = a67.build_branch(
            maximum,
            sp.Rational(maximum, 2),
            epsilon,
            4,
            positive_indices,
            (("alpha", 1), ("beta", -1)),
        )
        conditions = branch["conditions"]
        condition_map = dict(conditions)
        lower_name = "inactive_slack_gamma_-1"
        upper_name = "inactive_slack_gamma_+1"

        lower_poly = primitive_integer_poly(
            condition_map[lower_name],
            variable,
        )
        upper_poly = primitive_integer_poly(
            condition_map[upper_name],
            variable,
        )
        lower_interval, lower_multiplicity = isolate_one_root(lower_poly)
        upper_interval, upper_multiplicity = isolate_one_root(upper_poly)

        hull_lower = lower_interval[0]
        hull_upper = upper_interval[1]
        lower_witness = exact_floor(lower_interval[0], 10_000)
        upper_witness = exact_ceil(upper_interval[1], 10_000)

        values_at_probe = {
            name: sp.factor(expression.subs(variable, S0))
            for name, expression in conditions
        }
        all_probe_positive = all(value > 0 for value in values_at_probe.values())

        census = full_root_census(
            conditions,
            variable,
            hull_lower,
            hull_upper,
            {lower_name, upper_name},
        )

        lower_signs = {
            "below": str(
                sp.sign(
                    condition_map[lower_name].subs(variable, lower_witness)
                )
            ),
            "at_probe": str(
                sp.sign(condition_map[lower_name].subs(variable, S0))
            ),
        }
        upper_signs = {
            "at_probe": str(
                sp.sign(condition_map[upper_name].subs(variable, S0))
            ),
            "above": str(
                sp.sign(
                    condition_map[upper_name].subs(variable, upper_witness)
                )
            ),
        }

        lower_cramer = cramer_entering_atom_polynomial(
            maximum,
            contact - 1,
            -1,
            contact - 1,
            variable,
        )
        upper_cramer = cramer_entering_atom_polynomial(
            maximum,
            contact,
            1,
            contact + 1,
            variable,
        )

        lower_poly_identity = lower_poly.monic() == lower_cramer.monic()
        upper_poly_identity = upper_poly.monic() == upper_cramer.monic()

        lower_adjacent = evaluate_adjacent_witness(
            a78,
            maximum,
            contact - 1,
            -1,
            lower_witness,
        )
        upper_adjacent = evaluate_adjacent_witness(
            a78,
            maximum,
            contact,
            1,
            upper_witness,
        )
        lower_compressed = evaluate_compressed_witness(
            a78,
            maximum,
            contact,
            lower_witness,
        )
        upper_compressed = evaluate_compressed_witness(
            a78,
            maximum,
            contact,
            upper_witness,
        )

        support_gates = {
            "probe_is_inside_isolated_interval": bool(
                lower_interval[1] < S0 < upper_interval[0]
            ),
            "lower_boundary_is_simple": lower_multiplicity == 1,
            "upper_boundary_is_simple": upper_multiplicity == 1,
            "boundary_intervals_are_disjoint": bool(
                lower_interval[1] < upper_interval[0]
            ),
            "all_KKT_conditions_positive_at_probe": all_probe_positive,
            "complete_root_census_passes": census["pass"],
            "no_denominator_root_on_hull": (
                census["denominator_root_count"] == 0
            ),
            "no_other_KKT_numerator_root_on_hull": (
                census["nonboundary_numerator_root_count"] == 0
            ),
            "lower_gamma_slack_crosses_negative_to_positive": (
                lower_signs == {"below": "-1", "at_probe": "1"}
            ),
            "upper_gamma_slack_crosses_positive_to_negative": (
                upper_signs == {"at_probe": "1", "above": "-1"}
            ),
            "lower_boundary_equals_entering_atom_Cramer_polynomial": (
                lower_poly_identity
            ),
            "upper_boundary_equals_entering_atom_Cramer_polynomial": (
                upper_poly_identity
            ),
            "lower_adjacent_branch_is_strict_global_KKT_at_witness": (
                lower_adjacent["status"] == "pass"
            ),
            "upper_adjacent_branch_is_strict_global_KKT_at_witness": (
                upper_adjacent["status"] == "pass"
            ),
            "compressed_branch_fails_below_by_gamma_minus_slack": (
                lower_compressed["status"] == "inactive_slack_infeasible"
                and lower_compressed["first_failure"] is not None
                and lower_compressed["first_failure"]["name"]
                == lower_name
            ),
            "compressed_branch_fails_above_by_gamma_plus_slack": (
                upper_compressed["status"] == "inactive_slack_infeasible"
                and upper_compressed["first_failure"] is not None
                and upper_compressed["first_failure"]["name"]
                == upper_name
            ),
        }

        support_results.append({
            "maximum": maximum,
            "compressed_contact": contact,
            "compressed_signature": {
                "p_support": [0, contact, maximum],
                "q_support": [1, h, h + 1],
                "active_bands": [["alpha", 1], ["beta", -1]],
                "gamma": "inactive",
            },
            "strict_KKT_component_containing_s0": {
                "s_lower_root": interval_record(lower_interval),
                "s_upper_root": interval_record(upper_interval),
                **alpha_interval_record(lower_interval, upper_interval),
                "open_interval_statement": (
                    "r_minus(M) < s < r_plus(M)"
                ),
                "maximality_reason": (
                    "the gamma-minus inactive slack changes sign at the "
                    "lower simple root and the gamma-plus inactive slack "
                    "changes sign at the upper simple root; all other KKT "
                    "numerators and all denominators are root-free on the "
                    "enclosing rational hull"
                ),
            },
            "root_census": census,
            "boundary_signs": {
                "lower_gamma_minus_slack": lower_signs,
                "upper_gamma_plus_slack": upper_signs,
            },
            "contact_entry_identity": {
                "lower": {
                    "adjacent_pair": [contact - 1, contact],
                    "gamma_sign": -1,
                    "entering_atom": contact - 1,
                    "same_monic_primitive_polynomial": lower_poly_identity,
                },
                "upper": {
                    "adjacent_pair": [contact, contact + 1],
                    "gamma_sign": 1,
                    "entering_atom": contact + 1,
                    "same_monic_primitive_polynomial": upper_poly_identity,
                },
            },
            "exact_outside_witnesses": {
                "below": {
                    "adjacent": lower_adjacent,
                    "compressed": lower_compressed,
                },
                "above": {
                    "adjacent": upper_adjacent,
                    "compressed": upper_compressed,
                },
            },
            "gates": support_gates,
            "gate_count": len(support_gates),
            "pass_count": sum(support_gates.values()),
            "verdict": "PASS" if all(support_gates.values()) else "FAIL",
        })

        polynomial_results.extend([
            {
                "maximum": maximum,
                "boundary": "lower",
                "condition": lower_name,
                "adjacent_pair": [contact - 1, contact],
                "gamma_sign": -1,
                "entering_atom": contact - 1,
                "root_interval": interval_record(lower_interval),
                "polynomial": polynomial_record(lower_poly),
            },
            {
                "maximum": maximum,
                "boundary": "upper",
                "condition": upper_name,
                "adjacent_pair": [contact, contact + 1],
                "gamma_sign": 1,
                "entering_atom": contact + 1,
                "root_interval": interval_record(upper_interval),
                "polynomial": polynomial_record(upper_poly),
            },
        ])

    all_support_gates = all(
        all(item["gates"].values()) for item in support_results
    )
    lower_sequence = [
        item["exact_outside_witnesses"]["below"]["adjacent"][
            "contact_pair"
        ]
        for item in support_results
    ]
    upper_sequence = [
        item["exact_outside_witnesses"]["above"]["adjacent"][
            "contact_pair"
        ]
        for item in support_results
    ]

    global_gates = {
        "declared_compression_supports_exact": (
            list(SUPPORTS) == [40, 57, 74]
        ),
        "all_three_interval_certificates_pass": all_support_gates,
        "all_lower_reentries_have_gamma_minus": all(
            item["exact_outside_witnesses"]["below"]["adjacent"][
                "gamma_sign"
            ] == -1
            for item in support_results
        ),
        "all_upper_reentries_have_gamma_plus": all(
            item["exact_outside_witnesses"]["above"]["adjacent"][
                "gamma_sign"
            ] == 1
            for item in support_results
        ),
        "contact_entry_sequence_is_left_single_right": (
            lower_sequence == [[8, 9], [11, 12], [14, 15]]
            and upper_sequence == [[9, 10], [12, 13], [15, 16]]
        ),
        "scope_remains_finite_and_contract_relative": (
            S0 == sp.Rational(131, 1000)
            and set(SUPPORTS) == {40, 57, 74}
        ),
    }

    summary = {
        "audit": "A79_EXACT_COMPRESSION_INTERVAL_AND_CONTACT_ENTRY",
        "contract": {
            "support": "{0,...,M}",
            "mean": "M/2",
            "target_exponent": 1,
            "s0": str(S0),
            "alpha0_decimal": f"{-math.log2(float(S0)):.15f}",
            "beta_exponent": 3,
            "gamma_exponent": 4,
            "compression_supports": list(SUPPORTS),
            "epsilon_even": "1/(1875*2^(M/2))",
            "epsilon_odd": "1/(2500*2^floor(M/2))",
        },
        "theorem_summary": [
            "For M=40,57,74, the A78 compressed branch has a maximal "
            "connected strict-KKT interval containing s0 bounded by two "
            "simple algebraic roots.",
            "The lower root is the gamma-minus inactive-slack boundary and "
            "the exact Cramer numerator for entry of atom k-1 in the "
            "{k-1,k}, gamma-minus branch.",
            "The upper root is the gamma-plus inactive-slack boundary and "
            "the exact Cramer numerator for entry of atom k+1 in the "
            "{k,k+1}, gamma-plus branch.",
            "Exact rational witnesses on the outer sides certify the "
            "adjacent branches as strict global KKT optima.",
        ],
        "support_results": support_results,
        "gates": global_gates,
        "gate_count": len(global_gates),
        "pass_count": sum(global_gates.values()),
        "nested_support_gate_count": sum(
            item["gate_count"] for item in support_results
        ),
        "nested_support_pass_count": sum(
            item["pass_count"] for item in support_results
        ),
        "verdict": (
            "PASS_EXACT_COMPRESSION_INTERVALS_AND_CONTACT_ENTRY_POLYNOMIALS"
            if all(global_gates.values())
            else "FAIL"
        ),
        "claim_boundary": [
            "Exact only for M=40,57,74 under the frozen central-mean contract.",
            "The adjacent branches are certified at exact rational witnesses; "
            "their complete maximal intervals are not claimed.",
            "No periodicity or all-M law for compression supports is claimed.",
            "No physical interpretation is inferred from support contacts or "
            "active-set compression.",
        ],
    }

    polynomial_output = {
        "audit": "A79_BOUNDARY_POLYNOMIAL_CERTIFICATES",
        "normalization": (
            "primitive integer polynomial with positive leading coefficient"
        ),
        "polynomials": polynomial_results,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    result_path = OUTPUT_DIR / "a79_compression_interval_results.json"
    polynomial_path = OUTPUT_DIR / "a79_boundary_polynomials.json"
    result_path.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    polynomial_path.write_text(
        json.dumps(polynomial_output, indent=2),
        encoding="utf-8",
    )

    print(json.dumps({
        "audit": summary["audit"],
        "compression_supports": list(SUPPORTS),
        "global_gates": f"{summary['pass_count']}/{summary['gate_count']}",
        "nested_support_gates": (
            f"{summary['nested_support_pass_count']}/"
            f"{summary['nested_support_gate_count']}"
        ),
        "verdict": summary["verdict"],
        "result": result_path.name,
        "polynomials": polynomial_path.name,
    }, indent=2))

    if not all(global_gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
