#!/usr/bin/env python3
"""A107-MIN exact local-continuum audit for the first deterministic A102 gamma-plus record.

Question frozen before execution:
    Does the first deterministic legacy_three_band_gamma_plus A102 witness
    persist on a nonzero open source-probe interval under the same exact
    finite-LP support and active-band architecture?

This is deliberately a one-record audit. It does not claim a finite atlas for
all 922 gamma-plus records. It uses the same exact rank-one / root-ordering /
hull-certification machinery as A105-A106, with gamma sign +1 and
P={0,j,j+1,M}. Only the alpha row varies with source probe s.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import sympy as sp

import a103_endpoint_released_continuum_segment_atlas_audit as a103
import a105_legacy_two_band_continuum_segment_atlas_audit as a105

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if HERE.name == "audits" else HERE
RESULTS = ROOT / "results" if HERE.name == "audits" else HERE
A102_CATALOGUE = RESULTS / "a102_complete_rational_witness_lift_atlas_catalogue.json"
REF = sp.Rational(1, 8)
SparsePoly = dict[int, sp.Rational]


def rank_one_gamma_plus_conditions(
    maximum: int,
    contact: int,
    reference_probe: sp.Rational = REF,
) -> tuple[SparsePoly, list[tuple[str, SparsePoly]]]:
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = a103.normalized_epsilon(maximum)
    p_support = [0, contact, contact + 1, maximum]
    q_support = [1, h, h + 1]

    def alpha0(x: int) -> sp.Rational:
        return reference_probe**x

    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, -mean],
        [0, 0, 0, 0, *q_support, -mean],
        [0, 0, 0, 0, *[a103.tv(x) for x in q_support], 0],
        [*[alpha0(x) for x in p_support], *[-alpha0(x) for x in q_support], -2 * epsilon],
        [*[-a103.bv(x) for x in p_support], *[a103.bv(x) for x in q_support], -2 * epsilon],
        [*[a103.gv(x) for x in p_support], *[-a103.gv(x) for x in q_support], -2 * epsilon],
    ]
    matrix = sp.Matrix(rows)
    inverse = matrix.inv(method="DM")
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
    objective = sp.Matrix([*[a103.tv(x) for x in p_support], 0, 0, 0, 0])
    basic0 = inverse * rhs
    dual0 = inverse.T * objective
    update_direction = inverse[:, 5]

    signs = [1, 1, 1, 1, -1, -1, -1, 0]
    exponents = [*p_support, *q_support, 0]
    row_updates: list[SparsePoly] = []
    for row_sign, exponent in zip(signs, exponents):
        if row_sign == 0:
            row_updates.append({})
        else:
            row_updates.append(a103.add(
                ({exponent: sp.Rational(row_sign)}, 1, 0),
                ({0: -sp.Rational(row_sign) * reference_probe**exponent}, 1, 0),
            ))

    denominator: SparsePoly = {0: sp.Rational(1)}
    for update, coefficient in zip(row_updates, update_direction):
        denominator = a103.add((denominator, 1, 0), (update, coefficient, 0))

    update_dot_basic: SparsePoly = {}
    for update, coefficient in zip(row_updates, basic0):
        update_dot_basic = a103.add((update_dot_basic, 1, 0), (update, coefficient, 0))

    basic_numerators = [
        a103.add((denominator, basic0[i], 0), (update_dot_basic, -update_direction[i], 0))
        for i in range(8)
    ]

    objective_update_direction = objective.dot(update_direction)
    dual_numerators: list[SparsePoly] = []
    for column in range(8):
        update_times_inverse: SparsePoly = {}
        for row, update in enumerate(row_updates):
            update_times_inverse = a103.add(
                (update_times_inverse, 1, 0),
                (update, inverse[row, column], 0),
            )
        dual_numerators.append(a103.add(
            (denominator, dual0[column], 0),
            (update_times_inverse, -objective_update_direction, 0),
        ))

    if a103.ev(denominator, reference_probe) != 1:
        raise AssertionError("rank-one denominator normalization failed")
    for i in range(8):
        if a103.ev(basic_numerators[i], reference_probe) != basic0[i]:
            raise AssertionError("basic-variable rank-one regression failed")
        if a103.ev(dual_numerators[i], reference_probe) != dual0[i]:
            raise AssertionError("dual-variable rank-one regression failed")

    conditions: list[tuple[str, SparsePoly]] = []
    conditions.extend(zip(
        [*[f"basic_p_{x}" for x in p_support], *[f"basic_q_{x}" for x in q_support], "basic_t"],
        basic_numerators,
    ))
    conditions.extend([
        ("active_dual_alpha_+1", dual_numerators[5]),
        ("active_dual_beta_-1", dual_numerators[6]),
        ("active_dual_gamma_+1", dual_numerators[7]),
    ])

    p_set = set(p_support)
    q_set = set(q_support)
    for x in range(maximum + 1):
        if x not in p_set:
            conditions.append((
                f"reduced_cost_p_{x}",
                a103.add(
                    (dual_numerators[0], 1, 0),
                    (dual_numerators[2], x, 0),
                    (dual_numerators[5], 1, x),
                    (dual_numerators[6], -a103.bv(x), 0),
                    (dual_numerators[7], a103.gv(x), 0),
                    (denominator, -a103.tv(x), 0),
                ),
            ))
        if x not in q_set:
            conditions.append((
                f"reduced_cost_q_{x}",
                a103.add(
                    (dual_numerators[1], 1, 0),
                    (dual_numerators[3], x, 0),
                    (dual_numerators[4], a103.tv(x), 0),
                    (dual_numerators[5], -1, x),
                    (dual_numerators[6], a103.bv(x), 0),
                    (dual_numerators[7], -a103.gv(x), 0),
                ),
            ))

    alpha_difference: SparsePoly = {}
    for i, x in enumerate(p_support):
        alpha_difference = a103.add((alpha_difference, 1, 0), (basic_numerators[i], 1, x))
    for i, x in enumerate(q_support):
        alpha_difference = a103.add(
            (alpha_difference, 1, 0),
            (basic_numerators[len(p_support) + i], -1, x),
        )

    def constant_difference(fn: Any) -> SparsePoly:
        output: SparsePoly = {}
        for i, x in enumerate(p_support):
            output = a103.add((output, 1, 0), (basic_numerators[i], fn(x), 0))
        for i, x in enumerate(q_support):
            output = a103.add(
                (output, 1, 0),
                (basic_numerators[len(p_support) + i], -fn(x), 0),
            )
        return output

    beta_difference = constant_difference(a103.bv)
    gamma_difference = constant_difference(a103.gv)
    t_numerator = basic_numerators[-1]
    conditions.extend([
        ("inactive_slack_alpha_-1", a103.add((t_numerator, 2 * epsilon, 0), (alpha_difference, 1, 0))),
        ("inactive_slack_beta_+1", a103.add((t_numerator, 2 * epsilon, 0), (beta_difference, -1, 0))),
        ("inactive_slack_gamma_-1", a103.add((t_numerator, 2 * epsilon, 0), (gamma_difference, 1, 0))),
    ])
    return denominator, conditions


def direct_gamma_plus_conditions(maximum: int, contact: int, probe: sp.Rational) -> list[tuple[str, sp.Rational]]:
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = a103.normalized_epsilon(maximum)
    p_support = [0, contact, contact + 1, maximum]
    q_support = [1, h, h + 1]
    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, -mean],
        [0, 0, 0, 0, *q_support, -mean],
        [0, 0, 0, 0, *[a103.tv(x) for x in q_support], 0],
        [*[probe**x for x in p_support], *[-probe**x for x in q_support], -2 * epsilon],
        [*[-a103.bv(x) for x in p_support], *[a103.bv(x) for x in q_support], -2 * epsilon],
        [*[a103.gv(x) for x in p_support], *[-a103.gv(x) for x in q_support], -2 * epsilon],
    ]
    inverse = sp.Matrix(rows).inv(method="DM")
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
    objective = sp.Matrix([*[a103.tv(x) for x in p_support], 0, 0, 0, 0])
    basic = inverse * rhs
    dual = inverse.T * objective
    conditions: list[tuple[str, sp.Rational]] = []
    conditions.extend(zip(
        [*[f"basic_p_{x}" for x in p_support], *[f"basic_q_{x}" for x in q_support], "basic_t"],
        map(sp.Rational, basic),
    ))
    conditions.extend([
        ("active_dual_alpha_+1", sp.Rational(dual[5])),
        ("active_dual_beta_-1", sp.Rational(dual[6])),
        ("active_dual_gamma_+1", sp.Rational(dual[7])),
    ])
    p_set = set(p_support)
    q_set = set(q_support)
    for x in range(maximum + 1):
        if x not in p_set:
            column = sp.Matrix([1, 0, x, 0, 0, probe**x, -a103.bv(x), a103.gv(x)])
            conditions.append((f"reduced_cost_p_{x}", sp.Rational(column.dot(dual) - a103.tv(x))))
        if x not in q_set:
            column = sp.Matrix([0, 1, 0, x, a103.tv(x), -probe**x, a103.bv(x), -a103.gv(x)])
            conditions.append((f"reduced_cost_q_{x}", sp.Rational(column.dot(dual))))
    t_value = sp.Rational(basic[-1])
    alpha_difference = sum(probe**x * basic[i] for i, x in enumerate(p_support)) - sum(
        probe**x * basic[len(p_support) + i] for i, x in enumerate(q_support)
    )
    beta_difference = sum(a103.bv(x) * basic[i] for i, x in enumerate(p_support)) - sum(
        a103.bv(x) * basic[len(p_support) + i] for i, x in enumerate(q_support)
    )
    gamma_difference = sum(a103.gv(x) * basic[i] for i, x in enumerate(p_support)) - sum(
        a103.gv(x) * basic[len(p_support) + i] for i, x in enumerate(q_support)
    )
    conditions.extend([
        ("inactive_slack_alpha_-1", sp.Rational(2 * epsilon * t_value + alpha_difference)),
        ("inactive_slack_beta_+1", sp.Rational(2 * epsilon * t_value - beta_difference)),
        ("inactive_slack_gamma_-1", sp.Rational(2 * epsilon * t_value + gamma_difference)),
    ])
    return conditions


def build_integer_polynomials(record: dict[str, Any]) -> tuple[list[tuple[str, dict[int, int]]], int]:
    fields = record["key_fields"]
    maximum = int(fields["maximum"])
    contact = int(fields["compressed_maximizer_contact"])
    witness = sp.Rational(fields["witness"])
    denominator, conditions = rank_one_gamma_plus_conditions(maximum, contact, REF)
    orientation = a103.sign(a103.ev(denominator, witness))
    if orientation == 0:
        raise RuntimeError("common denominator vanishes at witness")
    polynomials = [("common_denominator", a103.int_poly(denominator, orientation))]
    polynomials.extend((name, a103.int_poly(poly, orientation)) for name, poly in conditions)
    return polynomials, orientation


def deterministic_source_records() -> list[dict[str, Any]]:
    catalogue = json.loads(A102_CATALOGUE.read_text(encoding="utf-8"))
    records = [
        record for record in catalogue["records"]
        if record["resolution"]["detailed_class"] == "legacy_three_band_gamma_plus"
    ]
    records.sort(key=lambda record: (
        int(record["key_fields"]["maximum"]),
        int(record["key_fields"]["compressed_maximizer_contact"]),
        str(record["key_fields"]["witness"]),
    ))
    return records


def exact_checkpoint_regression(record: dict[str, Any], analyzed: dict[str, Any]) -> dict[str, Any]:
    fields = record["key_fields"]
    maximum = int(fields["maximum"])
    contact = int(fields["compressed_maximizer_contact"])
    witness = sp.Rational(fields["witness"])
    denominator, symbolic = rank_one_gamma_plus_conditions(maximum, contact, REF)
    lower_safe = sp.Rational(analyzed["strict_component"]["lower"])
    outside = sp.Rational(analyzed["outside_counterexamples"][0]["point"]) if analyzed["outside_counterexamples"] else None
    checkpoints = [
        ("interior_left", lower_safe + (witness - lower_safe) / 2),
        ("witness", witness),
        ("interior_right", (witness + sp.Rational(record["segment_open_bounds"][1])) / 2),
    ]
    if outside is not None:
        checkpoints.append(("outside_left", outside))

    output = []
    total = 0
    failures = 0
    for label, probe in checkpoints:
        direct = direct_gamma_plus_conditions(maximum, contact, probe)
        denominator_value = a103.ev(denominator, probe)
        if [name for name, _ in symbolic] != [name for name, _ in direct]:
            raise AssertionError("condition order mismatch")
        mismatches = []
        nonpositive = []
        for (name, poly), (_, value) in zip(symbolic, direct):
            total += 1
            if a103.ev(poly, probe) != denominator_value * value:
                mismatches.append(name)
                failures += 1
            if value <= 0:
                nonpositive.append(name)
        output.append({
            "label": label,
            "probe": str(probe),
            "comparison_count": len(direct),
            "mismatches": mismatches,
            "nonpositive_conditions": nonpositive,
        })
    return {
        "checkpoint_count": len(checkpoints),
        "comparison_count": total,
        "failure_count": failures,
        "checkpoints": output,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(RESULTS / "a107_min_first_gamma_plus_result.json"))
    args = parser.parse_args()

    source = deterministic_source_records()
    if len(source) != 922:
        raise RuntimeError(f"expected 922 gamma-plus source records, found {len(source)}")
    record = source[0]

    original = a105.build_integer_polynomials
    try:
        a105.build_integer_polynomials = build_integer_polynomials
        analyzed = a105.analyze_record(record)
    finally:
        a105.build_integer_polynomials = original
    analyzed["architecture_class"] = "legacy_three_band_gamma_plus"

    checkpoint = exact_checkpoint_regression(record, analyzed)
    local_stability_pass = bool(
        analyzed.get("status") in {"full_segment_coverage", "proper_strict_subcomponent"}
        and analyzed.get("condition_count_matches_A102_source")
        and analyzed.get("core_certificate", {}).get("failure_count") == 0
        and analyzed.get("nonselected_boundary_hull_certificate", {}).get("failure_count") == 0
        and analyzed.get("root_ordering_certificate", {}).get("failure_count") == 0
        and not analyzed.get("root_failures")
        and checkpoint["failure_count"] == 0
    )
    analyzed["a107_min_meta"] = {
        "question": "Does the first deterministic legacy_three_band_gamma_plus witness persist on a nonzero open source-probe interval under the frozen A102 basis/active-set architecture?",
        "source_gamma_plus_count": len(source),
        "selection_rule": "first record after deterministic sort by (maximum, compressed_contact, witness)",
        "checkpoint_regression": checkpoint,
        "verdict": "PASS_LOCAL_OPEN_STABILITY" if local_stability_pass else "FAIL_OR_UNRESOLVED_LOCAL_OPEN_STABILITY",
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(analyzed, indent=2), encoding="utf-8")
    print(json.dumps({
        "key": analyzed["key"],
        "status": analyzed["status"],
        "verdict": analyzed["a107_min_meta"]["verdict"],
        "condition_count": analyzed.get("condition_count"),
        "checkpoint_comparisons": checkpoint["comparison_count"],
        "checkpoint_failures": checkpoint["failure_count"],
        "selected_left_boundary": analyzed["strict_component"].get("selected_left_boundary"),
        "selected_right_boundary": analyzed["strict_component"].get("selected_right_boundary"),
        "outside_counterexamples": analyzed.get("outside_counterexamples"),
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
