#!/usr/bin/env python3
"""Generate one exact A77 interval certificate for M=23,24,25."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
CORE = HERE / "a77_active_contact_reset_core.py"
A67 = HERE / "a67_central_mean_support_family_audit.py"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python a77_support_interval_certificate.py <M>")

    maximum = int(sys.argv[1])
    if maximum not in {23, 24, 25}:
        raise SystemExit("M must be 23, 24, or 25")

    core = load_module(CORE, f"a77_core_M{maximum}")
    core.LOWER = sp.Rational(131, 1000)
    core.UPPER = sp.Rational(263, 2000)
    a67 = load_module(A67, f"a67_for_a77_M{maximum}")

    contact = core.selected_contact(maximum)
    gamma_sign = core.selected_gamma_sign(maximum)
    branch = core.build_branch(
        a67,
        maximum,
        contact,
        gamma_sign,
    )

    conditions = []
    for name, expression in branch["conditions"]:
        certificate = core.rational_sign(expression, a67.S)
        conditions.append({
            "name": name,
            "certificate": certificate,
        })

    opposite_sign = -gamma_sign
    opposite_branch = core.build_branch(
        a67,
        maximum,
        contact,
        opposite_sign,
    )
    opposite_name = (
        "active_dual_gamma_"
        + ("+1" if opposite_sign > 0 else "-1")
    )
    opposite_expression = core.condition_expression(
        opposite_branch,
        opposite_name,
    )
    opposite_certificate = core.rational_sign(
        opposite_expression,
        a67.S,
    )

    determinants = core.gamma_plus_determinants(
        maximum,
        contact,
    )
    numerator_certificate = core.polynomial_sign(
        determinants["numerator"],
        determinants["variable"],
    )
    denominator_certificate = core.polynomial_sign(
        determinants["denominator"],
        determinants["variable"],
    )
    gamma_plus_sign = (
        numerator_certificate["sign"]
        * denominator_certificate["sign"]
    )

    if maximum == 23:
        adjacent_contact = 6
        adjacent_gamma = 1
        condition_name = "basic_7"
    else:
        adjacent_contact = 5
        adjacent_gamma = -1
        condition_name = "basic_5"

    adjacent_branch = core.build_branch(
        a67,
        maximum,
        adjacent_contact,
        adjacent_gamma,
    )
    adjacent_expression = core.condition_expression(
        adjacent_branch,
        condition_name,
    )
    adjacent_certificate = core.rational_sign(
        adjacent_expression,
        a67.S,
    )

    expected_plus_sign = -1 if maximum == 23 else 1

    gates = {
        "all_selected_conditions_positive": all(
            item["certificate"]["sign"] == 1
            for item in conditions
        ),
        "opposite_gamma_multiplier_negative": bool(
            opposite_certificate["sign"] == -1
        ),
        "gamma_plus_Cramer_orientation_correct": bool(
            gamma_plus_sign == expected_plus_sign
        ),
        "adjacent_contact_family_primal_infeasible": bool(
            adjacent_certificate["sign"] == -1
        ),
    }

    result = {
        "audit": f"A77_INTERVAL_SUPPORT_M{maximum}",
        "maximum": maximum,
        "interval": {
            "s_lower": str(core.LOWER),
            "s_upper": str(core.UPPER),
            "probe_s": str(core.S0),
        },
        "selected_signature": core.signature(maximum),
        "selected_condition_count": len(conditions),
        "selected_conditions": conditions,
        "selected_ratio_at_probe": str(
            sp.factor(branch["ratio"].subs(a67.S, core.S0))
        ),
        "opposite_gamma": {
            "sign": opposite_sign,
            "multiplier_name": opposite_name,
            "certificate": opposite_certificate,
            "value_at_probe": str(
                sp.factor(
                    opposite_expression.subs(a67.S, core.S0)
                )
            ),
        },
        "gamma_plus_Cramer": {
            "contact_pair": [contact, contact + 1],
            "numerator_certificate": numerator_certificate,
            "denominator_certificate": denominator_certificate,
            "multiplier_sign": gamma_plus_sign,
        },
        "rejected_adjacent_family": {
            "contact_pair": [
                adjacent_contact,
                adjacent_contact + 1,
            ],
            "condition_name": condition_name,
            "certificate": adjacent_certificate,
            "value_at_probe": str(
                sp.factor(
                    adjacent_expression.subs(a67.S, core.S0)
                )
            ),
        },
        "gates": gates,
        "verdict": "PASS" if all(gates.values()) else "FAIL",
    }

    output = HERE / f"a77_interval_support_M{maximum}.json"
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(json.dumps({
        "maximum": maximum,
        "condition_count": len(conditions),
        "pass_count": sum(gates.values()),
        "gate_count": len(gates),
        "gamma_plus_sign": gamma_plus_sign,
        "verdict": result["verdict"],
        "output": output.name,
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
