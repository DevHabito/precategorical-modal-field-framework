#!/usr/bin/env python3
"""Isolated worker for A80 exact interval-KKT certification."""
from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
MAIN_SCRIPT = HERE / "a80_local_compression_window_atlas_audit.py"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def run(maximum: int, contact: int) -> dict:
    a80 = load(MAIN_SCRIPT, f"a80_worker_core_{maximum}")
    a78 = a80.load_module(a80.A78_SCRIPT, f"a78_worker_{maximum}")
    a79 = a80.load_module(a80.A79_SCRIPT, f"a79_worker_{maximum}")

    lower_polynomial = a79.cramer_entering_atom_polynomial(
        maximum, contact - 1, -1, contact - 1, a80.S
    )
    upper_polynomial = a79.cramer_entering_atom_polynomial(
        maximum, contact, 1, contact + 1, a80.S
    )
    lower_root = a80.exact_bisection_root(
        lower_polynomial, a80.LOCAL_LOWER, a80.LOCAL_UPPER
    )
    upper_root = a80.exact_bisection_root(
        upper_polynomial, a80.LOCAL_LOWER, a80.LOCAL_UPPER
    )
    if not lower_root.upper < upper_root.lower:
        raise RuntimeError("Root pair is not strictly ordered")

    hull_lower = lower_root.lower
    hull_upper = upper_root.upper
    strict_midpoint = (lower_root.upper + upper_root.lower) / 2

    symbolic_branch = a80.build_compressed_symbolic_branch(maximum, contact)
    condition_map = dict(symbolic_branch["conditions"])
    lower_name = "inactive_slack_gamma_-1"
    upper_name = "inactive_slack_gamma_+1"
    lower_identity = bool(
        a80.primitive_integer_poly(condition_map[lower_name]).monic()
        == lower_polynomial.monic()
    )
    upper_identity = bool(
        a80.primitive_integer_poly(condition_map[upper_name]).monic()
        == upper_polynomial.monic()
    )

    condition_certificates = []
    failures = []
    total_pieces = 0
    max_depth = 0
    for name, expression in symbolic_branch["conditions"]:
        if name in {lower_name, upper_name}:
            continue
        certificate = a80.certify_expression_positive(
            expression, hull_lower, hull_upper
        )
        total_pieces += (
            certificate["numerator"]["piece_count"]
            + certificate["denominator"]["piece_count"]
        )
        max_depth = max(
            max_depth,
            certificate["numerator"]["maximum_depth_used"],
            certificate["denominator"]["maximum_depth_used"],
        )
        if not certificate["pass"]:
            failures.append({"condition": name, "certificate": certificate})
        condition_certificates.append({
            "maximum": maximum,
            "contact": contact,
            "condition": name,
            "certificate": certificate,
        })

    original_probe = a78.S0
    a78.S0 = strict_midpoint
    try:
        midpoint = a78.evaluate_two_band(maximum, contact, collect_pass=True)
    finally:
        a78.S0 = original_probe

    lower_adjacent = a80.evaluate_adjacent_candidate(
        a78,
        maximum,
        contact - 1,
        -1,
        lower_root.lower - a80.OUTSIDE_DELTA,
    )
    upper_adjacent = a80.evaluate_adjacent_candidate(
        a78,
        maximum,
        contact,
        1,
        upper_root.upper + a80.OUTSIDE_DELTA,
    )

    contains_s0 = bool(lower_root.upper < a80.S0 < upper_root.lower)
    lies_below_s0 = bool(upper_root.upper < a80.S0)
    condition_count = len(condition_certificates)

    window_result = {
        "maximum": maximum,
        "contact": contact,
        "compressed_signature": {
            "p_support": symbolic_branch["p_support"],
            "q_support": symbolic_branch["q_support"],
            "active_bands": [["alpha", 1], ["beta", -1]],
            "gamma": "inactive",
        },
        "open_window": {
            "lower_root": a80.bracket_record(lower_root),
            "upper_root": a80.bracket_record(upper_root),
            "s_width_decimal": f"{float(upper_root.midpoint-lower_root.midpoint):.18f}",
            "alpha_lower_decimal": f"{-math.log2(float(upper_root.midpoint)):.15f}",
            "alpha_upper_decimal": f"{-math.log2(float(lower_root.midpoint)):.15f}",
            "contains_s0": contains_s0,
            "lies_strictly_below_s0": lies_below_s0,
        },
        "boundary_numerator_identities": {
            "lower_gamma_minus_equals_left_entering_atom_cramer": lower_identity,
            "upper_gamma_plus_equals_right_entering_atom_cramer": upper_identity,
        },
        "full_interval_KKT_certificate": {
            "nonboundary_condition_count": condition_count,
            "all_nonboundary_conditions_positive_on_rational_hull": not failures,
            "total_interval_polynomial_pieces": total_pieces,
            "maximum_subdivision_depth_used": max_depth,
            "failures": failures,
            "gamma_boundary_reason": (
                "Both gamma slack numerators have exactly one monotone root "
                "on the local interval; the lower slack is positive to the "
                "right of its root and the upper slack is positive to the "
                "left of its root."
            ),
        },
        "independent_midpoint_KKT_check": {
            "s": str(strict_midpoint),
            "status": midpoint["status"],
            "first_failure": midpoint["failure"][0] if midpoint["failure"] else None,
        },
        "declared_adjacent_candidate_checks": {
            "below_lower_boundary": lower_adjacent,
            "above_upper_boundary": upper_adjacent,
        },
    }
    return {
        "window_result": window_result,
        "condition_certificates": condition_certificates,
    }


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: worker.py MAXIMUM CONTACT")
    payload = run(int(sys.argv[1]), int(sys.argv[2]))
    def _default(value):
        if value is sp.S.true or value is sp.S.false:
            return bool(value)
        if isinstance(value, sp.Integer):
            return int(value)
        return str(value)
    print(json.dumps(payload, separators=(",", ":"), default=_default))


if __name__ == "__main__":
    main()
