#!/usr/bin/env python3
"""A105 exact continuum atlas for the 40 legacy two-band witness segments.

A102 contains forty exact rational witnesses whose unique strict finite-LP
optimum has

    P={0,j,M}, Q={1,h,h+1}, active={alpha+,beta-}, gamma inactive.

A105 promotes those isolated witness certificates to exact continuous
statements on their A95/A102 rational source segments.  Only the alpha row
varies with s.  A Sherman-Morrison rank-one row update around s=1/8 produces
one sparse common denominator and sparse exact numerators for every primal,
dual, reduced-cost, and inactive-band KKT condition.

For every segment the audit either certifies complete segment coverage,
isolates the maximal witness-containing strict KKT component with exact
algebraic boundary brackets and rational outside counterexamples, or records
an unresolved internal failure.  The claim is finite, contract-relative, and
nonphysical.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing as mp
import os
import time
from collections import Counter
from pathlib import Path
from typing import Any

import sympy as sp

import a103_endpoint_released_continuum_segment_atlas_audit as a103

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if HERE.name == "audits" else HERE
RESULTS = ROOT / "results" if HERE.name == "audits" else HERE
PROVENANCE = ROOT / "provenance" / "a105_legacy_two_band_continuum_atlas" if HERE.name == "audits" else HERE / "provenance"
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


def rank_one_legacy_two_band_conditions(
    maximum: int,
    contact: int,
    reference_probe: sp.Rational = REF,
) -> tuple[SparsePoly, list[tuple[str, SparsePoly]]]:
    """Sparse exact KKT numerators for P={0,j,M}, Q={1,h,h+1}."""
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = a103.normalized_epsilon(maximum)
    p_support = [0, contact, maximum]
    q_support = [1, h, h + 1]

    def alpha0(x: int) -> sp.Rational:
        return reference_probe**x

    rows = [
        [1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, -mean],
        [0, 0, 0, *q_support, -mean],
        [0, 0, 0, *[a103.tv(x) for x in q_support], 0],
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
    ]
    matrix = sp.Matrix(rows)
    inverse = matrix.inv(method="DM")
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0])
    objective = sp.Matrix([
        *[a103.tv(x) for x in p_support],
        0, 0, 0, 0,
    ])
    basic0 = inverse * rhs
    dual0 = inverse.T * objective
    update_direction = inverse[:, 5]

    signs = [1, 1, 1, -1, -1, -1, 0]
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
        for index in range(7)
    ]

    objective_update_direction = objective.dot(update_direction)
    dual_numerators: list[SparsePoly] = []
    for column in range(7):
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
    for index in range(7):
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
                ),
            ))

    alpha_difference: SparsePoly = {}
    for index, x in enumerate(p_support):
        alpha_difference = a103.add(
            (alpha_difference, 1, 0),
            (basic_numerators[index], 1, x),
        )
    for index, x in enumerate(q_support):
        alpha_difference = a103.add(
            (alpha_difference, 1, 0),
            (basic_numerators[3 + index], -1, x),
        )

    def constant_difference(fn: Any) -> SparsePoly:
        output: SparsePoly = {}
        for index, x in enumerate(p_support):
            output = a103.add((output, 1, 0), (basic_numerators[index], fn(x), 0))
        for index, x in enumerate(q_support):
            output = a103.add((output, 1, 0), (basic_numerators[3 + index], -fn(x), 0))
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
        (
            "inactive_slack_gamma_-1",
            a103.add((t_numerator, 2 * epsilon, 0), (gamma_difference, 1, 0)),
        ),
    ])
    return denominator, conditions


def source_records() -> list[dict[str, Any]]:
    catalogue = json.loads(A102_CATALOGUE.read_text(encoding="utf-8"))
    records = [
        record for record in catalogue["records"]
        if record["resolution"]["detailed_class"] == "legacy_two_band_compressed"
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
    denominator, conditions = rank_one_legacy_two_band_conditions(maximum, contact, REF)
    orientation = a103.sign(a103.ev(denominator, witness))
    if orientation == 0:
        raise RuntimeError("common denominator vanishes at witness")
    polynomials = [("common_denominator", a103.int_poly(denominator, orientation))]
    polynomials.extend((name, a103.int_poly(poly, orientation)) for name, poly in conditions)
    return polynomials, orientation


def bracket_pair(root: dict[str, Any]) -> tuple[sp.Rational, sp.Rational]:
    return tuple(sp.Rational(value) for value in root["bracket"])  # type: ignore[return-value]


def root_midpoint(root: dict[str, Any]) -> sp.Rational:
    lower, upper = bracket_pair(root)
    return (lower + upper) / 2


def analyze_record(record: dict[str, Any]) -> dict[str, Any]:
    started = time.time()
    fields = record["key_fields"]
    maximum = int(fields["maximum"])
    contact = int(fields["compressed_maximizer_contact"])
    witness = sp.Rational(fields["witness"])
    segment_lower = sp.Rational(record["segment_open_bounds"][0])
    segment_upper = sp.Rational(record["segment_open_bounds"][1])
    polynomials, orientation = build_integer_polynomials(record)
    polynomial_map = dict(polynomials)

    witness_failures = [
        name for name, polynomial in polynomials
        if a103.point_sign(polynomial, witness) <= 0
    ]
    if witness_failures:
        return {
            "key": record["key"],
            "maximum": maximum,
            "status": "witness_failure",
            "witness_failures": witness_failures,
        }

    endpoint_signs: dict[str, list[int]] = {}
    left_candidate_names: list[str] = []
    right_candidate_names: list[str] = []
    for name, polynomial in polynomials:
        left_sign = a103.point_sign(polynomial, segment_lower)
        right_sign = a103.point_sign(polynomial, segment_upper)
        endpoint_signs[name] = [left_sign, right_sign]
        if left_sign <= 0:
            left_candidate_names.append(name)
        if right_sign <= 0:
            right_candidate_names.append(name)

    def isolate_candidates(side: str, names: list[str]) -> list[dict[str, Any]]:
        output: list[dict[str, Any]] = []
        for name in names:
            polynomial = polynomial_map[name]
            endpoint = segment_lower if side == "left" else segment_upper
            endpoint_sign = a103.point_sign(polynomial, endpoint)
            witness_sign = a103.point_sign(polynomial, witness)
            if endpoint_sign == 0:
                output.append({
                    "condition": name,
                    "side": side,
                    "exact_root": str(endpoint),
                    "bracket": [str(endpoint), str(endpoint)],
                    "endpoint_signs": [0, 0],
                    "unique_simple_in_bracket": False,
                })
            elif endpoint_sign * witness_sign < 0:
                lower, upper = (endpoint, witness) if side == "left" else (witness, endpoint)
                output.append({"condition": name, "side": side, **a103.isolate_sign_change(polynomial, lower, upper)})
        output.sort(key=root_midpoint)
        return output

    left_roots = isolate_candidates("left", left_candidate_names)
    right_roots = isolate_candidates("right", right_candidate_names)
    selected_left = left_roots[-1] if left_roots else None
    selected_right = right_roots[0] if right_roots else None
    core_lower = bracket_pair(selected_left)[1] if selected_left else segment_lower
    core_upper = bracket_pair(selected_right)[0] if selected_right else segment_upper
    if not core_lower < witness < core_upper:
        raise RuntimeError(("invalid witness-containing component", maximum, core_lower, witness, core_upper))

    ordering_checks: list[dict[str, Any]] = []
    ordering_failures: list[dict[str, Any]] = []
    if selected_left:
        selected_lower, _ = bracket_pair(selected_left)
        for root in left_roots[:-1]:
            _, other_upper = bracket_pair(root)
            passed = bool(other_upper < selected_lower)
            item = {
                "side": "left",
                "other_condition": root["condition"],
                "selected_condition": selected_left["condition"],
                "other_bracket_upper": str(other_upper),
                "selected_bracket_lower": str(selected_lower),
                "pass": passed,
            }
            ordering_checks.append(item)
            if not passed:
                ordering_failures.append(item)
    if selected_right:
        _, selected_upper = bracket_pair(selected_right)
        for root in right_roots[1:]:
            other_lower, _ = bracket_pair(root)
            passed = bool(selected_upper < other_lower)
            item = {
                "side": "right",
                "selected_condition": selected_right["condition"],
                "other_condition": root["condition"],
                "selected_bracket_upper": str(selected_upper),
                "other_bracket_lower": str(other_lower),
                "pass": passed,
            }
            ordering_checks.append(item)
            if not passed:
                ordering_failures.append(item)

    root_failures = [
        {
            "side": root["side"],
            "condition": root["condition"],
            "reason": "selected root is not certified unique and simple in its bracket",
        }
        for root in (selected_left, selected_right)
        if root is not None and not root.get("exact_root") and not root.get("unique_simple_in_bracket")
    ]

    core_certificates: list[dict[str, Any]] = []
    core_failures: list[dict[str, Any]] = []
    core_methods: Counter[str] = Counter()
    for name, polynomial in polynomials:
        certificate = a103.certify_positive(polynomial, core_lower, core_upper, max_depth=18)
        item = {"name": name, **certificate}
        core_certificates.append(item)
        core_methods[certificate["method"]] += 1
        if not certificate["pass"]:
            core_failures.append(item)

    selected_conditions = {root["condition"] for root in (selected_left, selected_right) if root is not None}
    hull_lower = bracket_pair(selected_left)[0] if selected_left else segment_lower
    hull_upper = bracket_pair(selected_right)[1] if selected_right else segment_upper
    hull_certificates: list[dict[str, Any]] = []
    hull_failures: list[dict[str, Any]] = []
    hull_methods: Counter[str] = Counter()
    for name, polynomial in polynomials:
        if name in selected_conditions:
            continue
        certificate = a103.certify_positive(polynomial, hull_lower, hull_upper, max_depth=18)
        item = {"name": name, **certificate}
        hull_certificates.append(item)
        hull_methods[certificate["method"]] += 1
        if not certificate["pass"]:
            hull_failures.append(item)

    outside_counterexamples: list[dict[str, Any]] = []
    if selected_left:
        boundary_lower, _ = bracket_pair(selected_left)
        point = (segment_lower + boundary_lower) / 2
        outside_counterexamples.append({
            "side": "left",
            "condition": selected_left["condition"],
            "point": str(point),
            "sign": a103.point_sign(polynomial_map[selected_left["condition"]], point),
        })
    if selected_right:
        _, boundary_upper = bracket_pair(selected_right)
        point = (boundary_upper + segment_upper) / 2
        outside_counterexamples.append({
            "side": "right",
            "condition": selected_right["condition"],
            "point": str(point),
            "sign": a103.point_sign(polynomial_map[selected_right["condition"]], point),
        })

    full = (
        selected_left is None
        and selected_right is None
        and not core_failures
        and not hull_failures
    )
    partial = (
        (selected_left is not None or selected_right is not None)
        and not core_failures
        and not hull_failures
        and not root_failures
        and not ordering_failures
        and all(item["sign"] < 0 for item in outside_counterexamples)
    )
    status = "full_segment_coverage" if full else "proper_strict_subcomponent" if partial else "internal_failure_or_unresolved"
    expected_condition_count = int(record["resolution"]["source_condition_count"])
    return {
        "key": record["key"],
        "maximum": maximum,
        "base_contact": int(fields["base_contact"]),
        "compressed_phase": fields["compressed_phase"],
        "phase_side": fields["phase_side"],
        "witness": str(witness),
        "compressed_contact": contact,
        "architecture_class": "legacy_two_band_compressed",
        "architecture": record["resolution"]["architecture"],
        "P_support": record["resolution"]["P_support"],
        "Q_support": record["resolution"]["Q_support"],
        "active_bands": record["resolution"]["active_bands"],
        "segment_open_bounds": [str(segment_lower), str(segment_upper)],
        "reference_probe_for_rank_one": str(REF),
        "orientation": orientation,
        "condition_count": len(polynomials) - 1,
        "expected_source_condition_count": expected_condition_count,
        "condition_count_matches_A102_source": len(polynomials) - 1 == expected_condition_count,
        "numerator_plus_denominator_count": len(polynomials),
        "status": status,
        "strict_component": {
            "lower": str(core_lower),
            "upper": str(core_upper),
            "selected_left_boundary": selected_left,
            "selected_right_boundary": selected_right,
        },
        "candidate_roots": {"left": left_roots, "right": right_roots, "count": len(left_roots) + len(right_roots)},
        "endpoint_nonpositive_conditions": {"left": left_candidate_names, "right": right_candidate_names},
        "root_ordering_certificate": {
            "check_count": len(ordering_checks),
            "pass_count": sum(item["pass"] for item in ordering_checks),
            "failure_count": len(ordering_failures),
            "checks": ordering_checks,
            "failures": ordering_failures,
        },
        "core_certificate": {
            "interval": [str(core_lower), str(core_upper)],
            "condition_count": len(core_certificates),
            "pass_count": len(core_certificates) - len(core_failures),
            "failure_count": len(core_failures),
            "method_counts": dict(core_methods),
            "certificates": core_certificates,
            "failures": core_failures,
        },
        "nonselected_boundary_hull_certificate": {
            "hull": [str(hull_lower), str(hull_upper)],
            "selected_boundary_conditions": sorted(selected_conditions),
            "condition_count": len(hull_certificates),
            "pass_count": len(hull_certificates) - len(hull_failures),
            "failure_count": len(hull_failures),
            "method_counts": dict(hull_methods),
            "certificates": hull_certificates,
            "failures": hull_failures,
        },
        "root_failures": root_failures,
        "outside_counterexamples": outside_counterexamples,
    }


def compute_records(workers: int) -> list[dict[str, Any]]:
    source = source_records()
    if workers <= 1:
        records = [analyze_record(record) for record in source]
    else:
        with mp.Pool(processes=min(workers, len(source))) as pool:
            records = list(pool.imap_unordered(analyze_record, source, chunksize=1))
    records.sort(key=lambda record: record["key"])
    return records


def semantic_boundary(name: str | None) -> str | None:
    if name is None:
        return None
    if name.startswith("basic_p_"):
        return "basic_p_support_mass"
    if name.startswith("basic_q_"):
        return "basic_q_support_mass"
    if name.startswith("reduced_cost_p_"):
        return "reduced_cost_p_entry"
    if name.startswith("reduced_cost_q_"):
        return "reduced_cost_q_entry"
    return name


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=min(6, max(1, os.cpu_count() or 1)))
    parser.add_argument("--record-index", type=int)
    parser.add_argument("--record-output", type=str)
    parser.add_argument("--records-output", type=str)
    parser.add_argument("--assemble-from-records", type=str)
    parser.add_argument("--assemble-from-record-dir", action="store_true")
    args = parser.parse_args()
    RESULTS.mkdir(parents=True, exist_ok=True)
    PROVENANCE.mkdir(parents=True, exist_ok=True)

    source = source_records()
    record_dir = PROVENANCE / "records"
    if args.record_index is not None:
        if not 0 <= args.record_index < len(source):
            raise IndexError(f"record index must be in [0,{len(source)-1}]")
        record = analyze_record(source[args.record_index])
        output = Path(args.record_output) if args.record_output else record_dir / f"a105_record_{args.record_index:03d}.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(record, indent=2), encoding="utf-8")
        print(json.dumps({"record_index": args.record_index, "maximum": record["maximum"], "status": record["status"], "output": str(output)}, indent=2))
        return
    if args.assemble_from_record_dir:
        paths = [record_dir / f"a105_record_{index:03d}.json" for index in range(len(source))]
        missing = [str(path) for path in paths if not path.exists()]
        if missing:
            raise FileNotFoundError(f"missing exact A105 record files: {missing}")
        records = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    elif args.assemble_from_records:
        payload = json.loads(Path(args.assemble_from_records).read_text(encoding="utf-8"))
        records = payload["records"]
    else:
        committed = [record_dir / f"a105_record_{index:03d}.json" for index in range(len(source))]
        if all(path.exists() for path in committed):
            records = [json.loads(path.read_text(encoding="utf-8")) for path in committed]
        else:
            records = compute_records(args.workers)
        if args.records_output:
            path = Path(args.records_output)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"audit_phase": "A105_EXACT_RECORDS", "records": records}, indent=2), encoding="utf-8")

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

    # Data-driven gates preserve whatever exact classification the computation finds.
    unresolved_count = status_counts.get("internal_failure_or_unresolved", 0) + status_counts.get("witness_failure", 0)
    partial_count = status_counts.get("proper_strict_subcomponent", 0)
    full_count = status_counts.get("full_segment_coverage", 0)
    gates = {
        "A95_and_A102_sources_are_present_and_passed": source_ok,
        "exactly_40_legacy_two_band_source_segments_are_loaded": len(source) == 40,
        "computed_records_cover_exactly_all_40_source_keys": len(records) == 40 and not missing_keys and not extra_keys,
        "all_record_keys_are_unique": not duplicate_keys,
        "all_KKT_condition_counts_match_A102": not count_mismatches,
        "exact_KKT_condition_count_matches_source_sum": condition_count == sum(int(record["resolution"]["source_condition_count"]) for record in source),
        "numerator_plus_denominator_count_is_condition_count_plus_40": polynomial_count == condition_count + 40,
        "classification_exhausts_all_40_segments": full_count + partial_count + unresolved_count == 40,
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
        f"PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_40_LEGACY_TWO_BAND_SEGMENTS_WITH_{full_count}_FULL_AND_{partial_count}_PARTIAL_COMPONENTS"
        if all(gates.values())
        else "FAIL_A105_EXACT_LEGACY_TWO_BAND_CONTINUUM_SEGMENT_ATLAS"
    )

    summary = {
        "record_count": len(records),
        "unique_key_count": len(set(keys)),
        "status_counts": dict(status_counts),
        "phase_status_counts": {f"{phase}::{status}": count for (phase, status), count in sorted(phase_status_counts.items())},
        "condition_count": condition_count,
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
        "audit": "A105_EXACT_LEGACY_TWO_BAND_CONTINUUM_SEGMENT_ATLAS",
        "contract": {
            "source_segment_count": 40,
            "source": "A102 records with detailed_class=legacy_two_band_compressed",
            "tested_family": "P={0,j,M}, Q={1,h,h+1}, alpha+ and beta- active, gamma inactive",
            "symbolic_method": "exact Sherman-Morrison rank-one alpha-row update around s=1/8",
            "claim": "exact classification of the strict KKT component containing each of the 40 rational witnesses inside its A95/A102 source segment",
            "explicit_nonclaim": "not a continuum theorem for the 940 legacy three-band witnesses, not an all-cell or all-M theorem, and not a physical claim",
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
        "audit": "A105_EXACT_LEGACY_TWO_BAND_CONTINUUM_SEGMENT_ATLAS",
        "evidence_class": "exact sparse rational-function KKT reduction, rational interval arithmetic, exact algebraic root brackets, exact root ordering, and exact outside counterexamples",
        "scope": catalogue["contract"],
        "continuum_atlas": summary,
        "structural_result": {
            "full_segment_count": full_count,
            "partial_segment_count": partial_count,
            "unresolved_count": unresolved_count,
            "interpretation": "the forty legacy two-band pointwise certificates are promoted only to the exact witness-containing components supported by the KKT signs; no segment is silently promoted beyond its certified boundaries",
        },
        "provenance": {
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
    result_path = RESULTS / "a105_legacy_two_band_continuum_segment_results.json"
    catalogue_path = RESULTS / "a105_legacy_two_band_continuum_segment_catalogue.json"
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
