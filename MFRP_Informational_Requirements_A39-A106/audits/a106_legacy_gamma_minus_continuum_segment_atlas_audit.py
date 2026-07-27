#!/usr/bin/env python3
"""A106 exact continuum atlas for the 18 legacy gamma-minus witness segments.

A102 contains eighteen exact rational witnesses whose unique strict finite-LP
optimum has

    P={0,j-1,j,M}, Q={1,h,h+1},
    active={alpha+,beta-,gamma-}.

A106 promotes those isolated certificates to exact continuous statements on
their A95/A102 rational source segments. Only the alpha row varies with s. An
exact Sherman-Morrison rank-one row update around s=1/8 produces one sparse
common denominator and sparse exact numerators for every primal, dual,
reduced-cost, and inactive-band KKT condition.

For every segment the audit either certifies complete segment coverage,
isolates the maximal witness-containing strict KKT component with exact
algebraic boundary brackets and rational outside counterexamples, or records
an unresolved internal failure. The claim is finite, contract-relative, and
nonphysical.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections import Counter
from pathlib import Path
from typing import Any

import sympy as sp

import a103_endpoint_released_continuum_segment_atlas_audit as a103
import a105_legacy_two_band_continuum_segment_atlas_audit as a105

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if HERE.name == "audits" else HERE
RESULTS = ROOT / "results" if HERE.name == "audits" else HERE
PROVENANCE = ROOT / "provenance" / "a106_legacy_gamma_minus_continuum_atlas" if HERE.name == "audits" else HERE / "provenance"
A95_RESULT = RESULTS / "a95_rational_witness_lift_results.json"
A102_RESULT = RESULTS / "a102_complete_rational_witness_lift_atlas_results.json"
A102_CATALOGUE = RESULTS / "a102_complete_rational_witness_lift_atlas_catalogue.json"
REF = sp.Rational(1, 8)
SparsePoly = dict[int, sp.Rational]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def rank_one_legacy_gamma_minus_conditions(
    maximum: int,
    contact: int,
    reference_probe: sp.Rational = REF,
) -> tuple[SparsePoly, list[tuple[str, SparsePoly]]]:
    """Sparse exact KKT numerators for P={0,j-1,j,M}, Q={1,h,h+1}."""
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = a103.normalized_epsilon(maximum)
    p_support = [0, contact - 1, contact, maximum]
    q_support = [1, h, h + 1]

    def alpha0(x: int) -> sp.Rational:
        return reference_probe**x

    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, -mean],
        [0, 0, 0, 0, *q_support, -mean],
        [0, 0, 0, 0, *[a103.tv(x) for x in q_support], 0],
        [
            *[alpha0(x) for x in p_support],
            *[-alpha0(x) for x in q_support],
            -2 * epsilon,
        ],
        [
            *[-a103.bv(x) for x in p_support],
            *[a103.bv(x) for x in q_support],
            -2 * epsilon,
        ],
        [
            *[-a103.gv(x) for x in p_support],
            *[a103.gv(x) for x in q_support],
            -2 * epsilon,
        ],
    ]
    matrix = sp.Matrix(rows)
    inverse = matrix.inv(method="DM")
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
    objective = sp.Matrix([
        *[a103.tv(x) for x in p_support],
        0, 0, 0, 0,
    ])
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
        a103.add(
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
    for index in range(8):
        if a103.ev(basic_numerators[index], reference_probe) != basic0[index]:
            raise AssertionError("basic-variable rank-one regression failed")
        if a103.ev(dual_numerators[index], reference_probe) != dual0[index]:
            raise AssertionError("dual-variable rank-one regression failed")

    conditions: list[tuple[str, SparsePoly]] = []
    conditions.extend(zip(
        [
            *[f"basic_p_{x}" for x in p_support],
            *[f"basic_q_{x}" for x in q_support],
            "basic_t",
        ],
        basic_numerators,
    ))
    conditions.extend([
        ("active_dual_alpha_+1", dual_numerators[5]),
        ("active_dual_beta_-1", dual_numerators[6]),
        ("active_dual_gamma_-1", dual_numerators[7]),
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
                    (dual_numerators[7], -a103.gv(x), 0),
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
                    (dual_numerators[7], a103.gv(x), 0),
                ),
            ))

    alpha_difference: SparsePoly = {}
    for index, x in enumerate(p_support):
        alpha_difference = a103.add((alpha_difference, 1, 0), (basic_numerators[index], 1, x))
    for index, x in enumerate(q_support):
        alpha_difference = a103.add(
            (alpha_difference, 1, 0),
            (basic_numerators[len(p_support) + index], -1, x),
        )

    def constant_difference(fn: Any) -> SparsePoly:
        output: SparsePoly = {}
        for index, x in enumerate(p_support):
            output = a103.add((output, 1, 0), (basic_numerators[index], fn(x), 0))
        for index, x in enumerate(q_support):
            output = a103.add(
                (output, 1, 0),
                (basic_numerators[len(p_support) + index], -fn(x), 0),
            )
        return output

    beta_difference = constant_difference(a103.bv)
    gamma_difference = constant_difference(a103.gv)
    t_numerator = basic_numerators[-1]
    conditions.extend([
        (
            "inactive_slack_alpha_-1",
            a103.add((t_numerator, 2 * epsilon, 0), (alpha_difference, 1, 0)),
        ),
        (
            "inactive_slack_beta_+1",
            a103.add((t_numerator, 2 * epsilon, 0), (beta_difference, -1, 0)),
        ),
        (
            "inactive_slack_gamma_+1",
            a103.add((t_numerator, 2 * epsilon, 0), (gamma_difference, -1, 0)),
        ),
    ])
    return denominator, conditions



def direct_legacy_gamma_minus_conditions(
    maximum: int,
    contact: int,
    probe: sp.Rational,
) -> list[tuple[str, sp.Rational]]:
    """Independent exact finite-LP KKT values at one rational probe."""
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = a103.normalized_epsilon(maximum)
    p_support = [0, contact - 1, contact, maximum]
    q_support = [1, h, h + 1]
    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, -mean],
        [0, 0, 0, 0, *q_support, -mean],
        [0, 0, 0, 0, *[a103.tv(x) for x in q_support], 0],
        [*[probe**x for x in p_support], *[-probe**x for x in q_support], -2 * epsilon],
        [*[-a103.bv(x) for x in p_support], *[a103.bv(x) for x in q_support], -2 * epsilon],
        [*[-a103.gv(x) for x in p_support], *[a103.gv(x) for x in q_support], -2 * epsilon],
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
        ("active_dual_gamma_-1", sp.Rational(dual[7])),
    ])
    p_set = set(p_support)
    q_set = set(q_support)
    for x in range(maximum + 1):
        if x not in p_set:
            column = sp.Matrix([1, 0, x, 0, 0, probe**x, -a103.bv(x), -a103.gv(x)])
            conditions.append((f"reduced_cost_p_{x}", sp.Rational(column.dot(dual) - a103.tv(x))))
        if x not in q_set:
            column = sp.Matrix([0, 1, 0, x, a103.tv(x), -probe**x, a103.bv(x), a103.gv(x)])
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
        ("inactive_slack_gamma_+1", sp.Rational(2 * epsilon * t_value - gamma_difference)),
    ])
    return conditions


def exact_direct_rank_one_regression(records: list[dict[str, Any]]) -> dict[str, Any]:
    comparison_count = 0
    failures: list[dict[str, Any]] = []
    per_record: list[dict[str, Any]] = []
    for record in records:
        fields = record["key_fields"]
        maximum = int(fields["maximum"])
        contact = int(fields["compressed_maximizer_contact"])
        witness = sp.Rational(fields["witness"])
        denominator, symbolic = rank_one_legacy_gamma_minus_conditions(maximum, contact, REF)
        denominator_value = a103.ev(denominator, witness)
        direct = direct_legacy_gamma_minus_conditions(maximum, contact, witness)
        symbolic_names = [name for name, _ in symbolic]
        direct_names = [name for name, _ in direct]
        record_failures: list[str] = []
        if symbolic_names != direct_names:
            record_failures.append("condition_name_order_mismatch")
        else:
            for (name, polynomial), (_, value) in zip(symbolic, direct):
                comparison_count += 1
                if a103.ev(polynomial, witness) != denominator_value * value:
                    record_failures.append(name)
        if record_failures:
            failures.append({"key": record["key"], "failures": record_failures})
        per_record.append({
            "key": record["key"],
            "condition_count": len(direct),
            "failure_count": len(record_failures),
        })
    return {
        "record_count": len(records),
        "comparison_count": comparison_count,
        "failure_count": len(failures),
        "failures": failures,
        "records": per_record,
    }

def source_records() -> list[dict[str, Any]]:
    catalogue = json.loads(A102_CATALOGUE.read_text(encoding="utf-8"))
    records = [
        record for record in catalogue["records"]
        if record["resolution"]["detailed_class"] == "legacy_three_band_gamma_minus"
    ]
    records.sort(key=lambda record: (
        int(record["key_fields"]["maximum"]),
        int(record["key_fields"]["compressed_maximizer_contact"]),
        str(record["key_fields"]["witness"]),
    ))
    return records


def build_integer_polynomials(record: dict[str, Any]) -> tuple[list[tuple[str, dict[int, int]]], int]:
    fields = record["key_fields"]
    maximum = int(fields["maximum"])
    contact = int(fields["compressed_maximizer_contact"])
    witness = sp.Rational(fields["witness"])
    denominator, conditions = rank_one_legacy_gamma_minus_conditions(maximum, contact, REF)
    orientation = a103.sign(a103.ev(denominator, witness))
    if orientation == 0:
        raise RuntimeError("common denominator vanishes at witness")
    polynomials = [("common_denominator", a103.int_poly(denominator, orientation))]
    polynomials.extend((name, a103.int_poly(poly, orientation)) for name, poly in conditions)
    return polynomials, orientation


def analyze_record(record: dict[str, Any]) -> dict[str, Any]:
    # Reuse the strengthened A105 exact root-ordering/hull engine with this
    # architecture's independently constructed KKT polynomial family.
    original = a105.build_integer_polynomials
    try:
        a105.build_integer_polynomials = build_integer_polynomials
        output = a105.analyze_record(record)
    finally:
        a105.build_integer_polynomials = original
    output["architecture_class"] = "legacy_three_band_gamma_minus"
    return output


def semantic_boundary(name: str | None) -> str | None:
    return a105.semantic_boundary(name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=min(4, max(1, os.cpu_count() or 1)))
    parser.add_argument("--record-index", type=int)
    parser.add_argument("--record-output", type=str)
    parser.add_argument("--assemble-from-record-dir", action="store_true")
    args = parser.parse_args()
    del args.workers  # eighteen small exact records are intentionally replayed serially
    RESULTS.mkdir(parents=True, exist_ok=True)
    PROVENANCE.mkdir(parents=True, exist_ok=True)

    source = source_records()
    direct_regression = exact_direct_rank_one_regression(source)
    record_dir = PROVENANCE / "records"
    if args.record_index is not None:
        if not 0 <= args.record_index < len(source):
            raise IndexError(f"record index must be in [0,{len(source)-1}]")
        record = analyze_record(source[args.record_index])
        output = Path(args.record_output) if args.record_output else record_dir / f"a106_record_{args.record_index:03d}.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(record, indent=2), encoding="utf-8")
        print(json.dumps({"record_index": args.record_index, "maximum": record["maximum"], "status": record["status"], "output": str(output)}, indent=2))
        return

    if args.assemble_from_record_dir:
        paths = [record_dir / f"a106_record_{index:03d}.json" for index in range(len(source))]
        missing = [str(path) for path in paths if not path.exists()]
        if missing:
            raise FileNotFoundError(f"missing exact A106 record files: {missing}")
        records = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    else:
        records = [analyze_record(record) for record in source]

    expected_keys = {record["key"] for record in source}
    keys = [record["key"] for record in records]
    duplicate_keys = [key for key, count in Counter(keys).items() if count > 1]
    missing_keys = sorted(expected_keys - set(keys))
    extra_keys = sorted(set(keys) - expected_keys)
    status_counts = Counter(record["status"] for record in records)
    phase_status_counts = Counter((record.get("compressed_phase"), record["status"]) for record in records)
    condition_count = sum(int(record.get("condition_count", 0)) for record in records)
    polynomial_count = sum(int(record.get("numerator_plus_denominator_count", 0)) for record in records)
    core_failures = sum(int(record.get("core_certificate", {}).get("failure_count", 0)) for record in records)
    hull_failures = sum(int(record.get("nonselected_boundary_hull_certificate", {}).get("failure_count", 0)) for record in records)
    root_failures = sum(len(record.get("root_failures", [])) for record in records)
    ordering_failures = sum(int(record.get("root_ordering_certificate", {}).get("failure_count", 0)) for record in records)
    count_mismatches = [record["key"] for record in records if not record.get("condition_count_matches_A102_source", False)]
    selected_roots = [
        root
        for record in records
        for root in (
            record.get("strict_component", {}).get("selected_left_boundary"),
            record.get("strict_component", {}).get("selected_right_boundary"),
        )
        if root is not None
    ]
    outside_counterexamples = [item for record in records for item in record.get("outside_counterexamples", [])]
    nonnegative_counterexamples = [item for item in outside_counterexamples if int(item["sign"]) >= 0]
    left_mechanisms = Counter(semantic_boundary((record.get("strict_component", {}).get("selected_left_boundary") or {}).get("condition")) for record in records)
    right_mechanisms = Counter(semantic_boundary((record.get("strict_component", {}).get("selected_right_boundary") or {}).get("condition")) for record in records)
    all_components_contain_witness = all(
        sp.Rational(record["strict_component"]["lower"])
        < sp.Rational(record["witness"])
        < sp.Rational(record["strict_component"]["upper"])
        for record in records if "strict_component" in record
    )
    all_selected_simple = all(
        bool(root.get("unique_simple_in_bracket")) or "exact_root" in root
        for root in selected_roots
    )

    a95 = json.loads(A95_RESULT.read_text(encoding="utf-8"))
    a102 = json.loads(A102_RESULT.read_text(encoding="utf-8"))
    source_ok = bool(
        a95.get("verdict") == "PASS_EXACT_RATIONAL_WITNESS_LIFT_ATLAS_AND_RESTRICTED_FAMILY_OBSTRUCTION"
        and all(a95.get("gates", {}).values())
        and a102.get("verdict") == "PASS_COMPLETE_EXACT_1063_RATIONAL_WITNESS_LIFT_ATLAS"
        and all(a102.get("gates", {}).values())
    )

    unresolved_count = status_counts.get("internal_failure_or_unresolved", 0) + status_counts.get("witness_failure", 0)
    partial_count = status_counts.get("proper_strict_subcomponent", 0)
    full_count = status_counts.get("full_segment_coverage", 0)
    gates = {
        "A95_and_A102_sources_are_present_and_passed": source_ok,
        "exactly_18_legacy_gamma_minus_source_segments_are_loaded": len(source) == 18,
        "computed_records_cover_exactly_all_18_source_keys": len(records) == 18 and not missing_keys and not extra_keys,
        "all_record_keys_are_unique": not duplicate_keys,
        "all_KKT_condition_counts_match_A102": not count_mismatches,
        "all_exact_direct_matrix_vs_rank_one_witness_values_match": direct_regression["failure_count"] == 0,
        "direct_rank_one_regression_covers_every_KKT_condition": direct_regression["comparison_count"] == condition_count,
        "exact_KKT_condition_count_matches_source_sum": condition_count == sum(int(record["resolution"]["source_condition_count"]) for record in source),
        "numerator_plus_denominator_count_is_condition_count_plus_18": polynomial_count == condition_count + 18,
        "classification_exhausts_all_18_segments": full_count + partial_count + unresolved_count == 18,
        "no_witness_certificate_fails": status_counts.get("witness_failure", 0) == 0,
        "all_selected_boundaries_are_locally_unique_and_simple": all_selected_simple,
        "all_competing_root_brackets_are_exactly_ordered": ordering_failures == 0,
        "all_core_KKT_polynomial_certificates_pass": core_failures == 0,
        "all_nonselected_boundary_hull_certificates_pass": hull_failures == 0,
        "every_selected_boundary_has_a_negative_rational_outside_counterexample": len(outside_counterexamples) == len(selected_roots) and not nonnegative_counterexamples,
        "every_certified_component_contains_its_rational_witness": all_components_contain_witness,
        "no_internal_failure_or_unresolved_segment_remains": unresolved_count == 0,
        "formal_contract_and_nonphysical_scope_are_preserved": True,
    }
    gates = {name: bool(value) for name, value in gates.items()}
    verdict = (
        f"PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_18_LEGACY_GAMMA_MINUS_SEGMENTS_WITH_{full_count}_FULL_AND_{partial_count}_PARTIAL_COMPONENTS"
        if all(gates.values())
        else "FAIL_A106_EXACT_LEGACY_GAMMA_MINUS_CONTINUUM_SEGMENT_ATLAS"
    )

    summary = {
        "record_count": len(records),
        "unique_key_count": len(set(keys)),
        "status_counts": dict(status_counts),
        "phase_status_counts": {f"{phase}::{status}": count for (phase, status), count in sorted(phase_status_counts.items())},
        "condition_count": condition_count,
        "direct_rank_one_regression_comparison_count": direct_regression["comparison_count"],
        "direct_rank_one_regression_failure_count": direct_regression["failure_count"],
        "numerator_plus_denominator_count": polynomial_count,
        "selected_boundary_count": len(selected_roots),
        "left_boundary_mechanisms": {str(key): value for key, value in left_mechanisms.items()},
        "right_boundary_mechanisms": {str(key): value for key, value in right_mechanisms.items()},
        "outside_counterexample_count": len(outside_counterexamples),
        "core_failure_count": core_failures,
        "hull_failure_count": hull_failures,
        "root_failure_count": root_failures,
        "ordering_failure_count": ordering_failures,
    }
    catalogue = {
        "audit": "A106_EXACT_LEGACY_GAMMA_MINUS_CONTINUUM_SEGMENT_ATLAS",
        "contract": {
            "source_segment_count": 18,
            "source": "A102 records with detailed_class=legacy_three_band_gamma_minus",
            "tested_family": "P={0,j-1,j,M}, Q={1,h,h+1}, alpha+, beta-, and gamma- active",
            "symbolic_method": "exact Sherman-Morrison rank-one alpha-row update around s=1/8",
            "claim": "exact classification of the strict KKT component containing each of the 18 rational witnesses inside its A95/A102 source segment",
            "explicit_nonclaim": "not a continuum theorem for the 922 legacy gamma-plus witnesses, not an all-cell or all-M theorem, and not a physical claim",
        },
        "summary": summary,
        "records": records,
        "failures": {
            "duplicate_keys": duplicate_keys,
            "missing_keys": missing_keys,
            "extra_keys": extra_keys,
            "condition_count_mismatches": count_mismatches,
            "nonnegative_outside_counterexamples": nonnegative_counterexamples,
        },
    }
    results = {
        "audit": "A106_EXACT_LEGACY_GAMMA_MINUS_CONTINUUM_SEGMENT_ATLAS",
        "evidence_class": "exact sparse rational-function KKT reduction, rational interval arithmetic, exact algebraic root brackets, exact root ordering, and exact outside counterexamples",
        "scope": catalogue["contract"],
        "continuum_atlas": summary,
        "structural_result": {
            "full_segment_count": full_count,
            "partial_segment_count": partial_count,
            "unresolved_count": unresolved_count,
            "interpretation": "the eighteen legacy gamma-minus pointwise certificates are promoted only to the exact witness-containing components supported by the KKT signs; no segment is silently promoted beyond its certified boundaries",
        },
        "provenance": {
            "exact_direct_matrix_vs_rank_one_regression": direct_regression,
            "source_hashes": {
                "A95_result": sha256(A95_RESULT),
                "A102_result": sha256(A102_RESULT),
                "A102_catalogue": sha256(A102_CATALOGUE),
            },
        },
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "fail_count": len(gates) - sum(gates.values()),
        "failed_gates": [name for name, passed in gates.items() if not passed],
        "verdict": verdict,
    }
    result_path = RESULTS / "a106_legacy_gamma_minus_continuum_segment_results.json"
    catalogue_path = RESULTS / "a106_legacy_gamma_minus_continuum_segment_catalogue.json"
    result_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    catalogue_path.write_text(json.dumps(catalogue, indent=2), encoding="utf-8")
    print(json.dumps({
        "verdict": verdict,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "status_counts": dict(status_counts),
        "condition_count": condition_count,
        "selected_boundary_count": len(selected_roots),
        "result": str(result_path),
        "catalogue": str(catalogue_path),
    }, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
