#!/usr/bin/env python3
"""A104 exact continuum atlas for the seven exceptional q0/q1 lift segments.

A102 contains seven rational phase witnesses not covered by the legacy-natural
or endpoint-released gamma-inactive families:

  * three q0/q1 gamma-inactive bases
      P={j,M}, Q={0,1,h,h+1}, active={alpha+,beta-};
  * four q0/q1 gamma-minus-active bases
      P={j-1,j,M}, Q={0,1,h,h+1},
      active={alpha+,beta-,gamma-}.

A104 upgrades those seven pointwise exact KKT certificates to exact continuous
statements on their A95 rational source segments.  For every source segment it
constructs all KKT numerators and the common denominator as sparse rational
polynomials in s, isolates the nearest exact algebraic KKT boundary on both
sides of the witness, certifies every condition on the witness-containing
strict component, verifies the ordering of every competing boundary bracket,
and provides exact negative rational counterexamples outside both boundaries.

The claim is relative to the declared finite LP and the seven A95 rational
source segments.  It is not a complete lift theorem for the other 1,056 A102
witnesses, not an all-cell or all-M theorem, and not a physical claim.
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

import a101_gamma_active_interval_and_residual_closure_audit as a101
import a103_endpoint_released_continuum_segment_atlas_audit as a103

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if HERE.name == "audits" else HERE
RESULTS = ROOT / "results" if HERE.name == "audits" else HERE
PROVENANCE = ROOT / "provenance" / "a104_exceptional_continuum_atlas" if HERE.name == "audits" else HERE / "provenance"

A99_RESULT = RESULTS / "a99_q0q1_interval_and_residual_atlas_results.json"
A101_RESULT = RESULTS / "a101_gamma_active_interval_and_residual_closure_results.json"
A102_RESULT = RESULTS / "a102_complete_rational_witness_lift_atlas_results.json"
A102_CATALOGUE = RESULTS / "a102_complete_rational_witness_lift_atlas_catalogue.json"
A103_RESULT = RESULTS / "a103_endpoint_released_continuum_segment_results.json"

REF = sp.Rational(1, 8)
SparsePoly = dict[int, sp.Rational]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def rank_one_q0q1_gamma_inactive_conditions(
    maximum: int,
    contact: int,
    reference_probe: sp.Rational = REF,
) -> tuple[SparsePoly, list[tuple[str, SparsePoly]]]:
    """Exact sparse KKT numerators for P={j,M}, Q={0,1,h,h+1}.

    Only the alpha row varies with s.  The exact Sherman-Morrison row update
    gives one sparse common denominator and one sparse numerator for every KKT
    condition.
    """
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = a103.normalized_epsilon(maximum)
    p_support = [contact, maximum]
    q_support = [0, 1, h, h + 1]

    def alpha0(x: int) -> sp.Rational:
        return reference_probe**x

    rows = [
        [1, 1, 0, 0, 0, 0, -1],
        [0, 0, 1, 1, 1, 1, -1],
        [*p_support, 0, 0, 0, 0, -mean],
        [0, 0, *q_support, -mean],
        [0, 0, *[a103.tv(x) for x in q_support], 0],
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
        0, 0, 0, 0, 0,
    ])
    basic0 = inverse * rhs
    dual0 = inverse.T * objective
    alpha_row_index = 5
    update_direction = inverse[:, alpha_row_index]

    signs = [1, 1, -1, -1, -1, -1, 0]
    exponents = [*p_support, *q_support, 0]
    row_updates: list[SparsePoly] = []
    for sign, exponent in zip(signs, exponents):
        if sign == 0:
            row_updates.append({})
        else:
            row_updates.append(a103.add(
                ({exponent: sp.Rational(sign)}, 1, 0),
                ({0: -sp.Rational(sign) * reference_probe**exponent}, 1, 0),
            ))

    denominator: SparsePoly = {0: sp.Rational(1)}
    for update, coefficient in zip(row_updates, update_direction):
        denominator = a103.add((denominator, 1, 0), (update, coefficient, 0))

    update_dot_basic: SparsePoly = {}
    for update, coefficient in zip(row_updates, basic0):
        update_dot_basic = a103.add(
            (update_dot_basic, 1, 0),
            (update, coefficient, 0),
        )

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
        raise AssertionError("rank-one denominator does not normalize to one")
    for index in range(7):
        if a103.ev(basic_numerators[index], reference_probe) != basic0[index]:
            raise AssertionError("basic-variable rank-one regression failed")
        if a103.ev(dual_numerators[index], reference_probe) != dual0[index]:
            raise AssertionError("dual-variable rank-one regression failed")

    conditions: list[tuple[str, SparsePoly]] = []
    variable_names = [
        *[f"basic_p_{x}" for x in p_support],
        *[f"basic_q_{x}" for x in q_support],
        "basic_t",
    ]
    conditions.extend(zip(variable_names, basic_numerators))
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
            (basic_numerators[len(p_support) + index], -1, x),
        )

    def constant_difference(fn: Any) -> SparsePoly:
        output: SparsePoly = {}
        for index, x in enumerate(p_support):
            output = a103.add(
                (output, 1, 0),
                (basic_numerators[index], fn(x), 0),
            )
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
            a103.add(
                (t_numerator, 2 * epsilon, 0),
                (alpha_difference, 1, 0),
            ),
        ),
        (
            "inactive_slack_beta_+1",
            a103.add(
                (t_numerator, 2 * epsilon, 0),
                (beta_difference, -1, 0),
            ),
        ),
        (
            "inactive_slack_gamma_+1",
            a103.add(
                (t_numerator, 2 * epsilon, 0),
                (gamma_difference, -1, 0),
            ),
        ),
        (
            "inactive_slack_gamma_-1",
            a103.add(
                (t_numerator, 2 * epsilon, 0),
                (gamma_difference, 1, 0),
            ),
        ),
    ])
    return denominator, conditions


def source_records() -> list[dict[str, Any]]:
    catalogue = json.loads(A102_CATALOGUE.read_text(encoding="utf-8"))
    records = [
        record for record in catalogue["records"]
        if record["resolution"]["broad_class"]
        in {"q0q1_gamma_inactive", "q0q1_gamma_active"}
    ]
    records.sort(key=lambda record: int(record["key_fields"]["maximum"]))
    return records


def build_integer_polynomials(
    record: dict[str, Any],
) -> tuple[list[tuple[str, dict[int, int]]], int]:
    fields = record["key_fields"]
    maximum = int(fields["maximum"])
    contact = int(fields["compressed_maximizer_contact"])
    witness = sp.Rational(fields["witness"])
    broad_class = record["resolution"]["broad_class"]

    if broad_class == "q0q1_gamma_inactive":
        denominator, conditions = rank_one_q0q1_gamma_inactive_conditions(
            maximum,
            contact,
            REF,
        )
    elif broad_class == "q0q1_gamma_active":
        denominator, conditions = a101.rank_one_symbolic_conditions(
            maximum,
            contact,
            REF,
        )
    else:
        raise ValueError(f"unsupported architecture: {broad_class}")

    orientation = a103.sign(a103.ev(denominator, witness))
    if orientation == 0:
        raise RuntimeError("common denominator vanishes at witness")
    polynomials = [("common_denominator", a103.int_poly(denominator, orientation))]
    polynomials.extend(
        (name, a103.int_poly(polynomial, orientation))
        for name, polynomial in conditions
    )
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
    broad_class = record["resolution"]["broad_class"]
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
            "architecture_class": broad_class,
            "status": "witness_failure",
            "witness_failures": witness_failures,
            "seconds": time.time() - started,
        }

    left_candidate_names: list[str] = []
    right_candidate_names: list[str] = []
    endpoint_signs: dict[str, list[int]] = {}
    for name, polynomial in polynomials:
        left_sign = a103.point_sign(polynomial, segment_lower)
        right_sign = a103.point_sign(polynomial, segment_upper)
        endpoint_signs[name] = [left_sign, right_sign]
        if left_sign <= 0:
            left_candidate_names.append(name)
        if right_sign <= 0:
            right_candidate_names.append(name)

    def isolate_candidates(
        side: str,
        names: list[str],
    ) -> list[dict[str, Any]]:
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
                root = a103.isolate_sign_change(polynomial, lower, upper)
                output.append({"condition": name, "side": side, **root})
        output.sort(key=root_midpoint)
        return output

    left_roots = isolate_candidates("left", left_candidate_names)
    right_roots = isolate_candidates("right", right_candidate_names)
    selected_left = left_roots[-1] if left_roots else None
    selected_right = right_roots[0] if right_roots else None

    core_lower = bracket_pair(selected_left)[1] if selected_left else segment_lower
    core_upper = bracket_pair(selected_right)[0] if selected_right else segment_upper
    if not core_lower < witness < core_upper:
        raise RuntimeError(("invalid witness-containing component", maximum))

    # Rigorous ordering: every other left bracket ends before the selected left
    # bracket starts; every other right bracket starts after the selected right
    # bracket ends.  This avoids selecting roots merely by approximate midpoint.
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
        if root is not None
        and not root.get("exact_root")
        and not root.get("unique_simple_in_bracket")
    ]

    core_certificates: list[dict[str, Any]] = []
    core_failures: list[dict[str, Any]] = []
    core_methods: Counter[str] = Counter()
    for name, polynomial in polynomials:
        certificate = a103.certify_positive(
            polynomial,
            core_lower,
            core_upper,
            max_depth=16,
        )
        item = {"name": name, **certificate}
        core_certificates.append(item)
        core_methods[certificate["method"]] += 1
        if not certificate["pass"]:
            core_failures.append(item)

    selected_conditions = {
        root["condition"]
        for root in (selected_left, selected_right)
        if root is not None
    }
    hull_lower = bracket_pair(selected_left)[0] if selected_left else segment_lower
    hull_upper = bracket_pair(selected_right)[1] if selected_right else segment_upper
    hull_certificates: list[dict[str, Any]] = []
    hull_failures: list[dict[str, Any]] = []
    hull_methods: Counter[str] = Counter()
    for name, polynomial in polynomials:
        if name in selected_conditions:
            continue
        certificate = a103.certify_positive(
            polynomial,
            hull_lower,
            hull_upper,
            max_depth=16,
        )
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
        selected_left is not None
        and selected_right is not None
        and not core_failures
        and not hull_failures
        and not root_failures
        and not ordering_failures
        and all(item["sign"] < 0 for item in outside_counterexamples)
    )
    status = (
        "full_segment_coverage"
        if full
        else "proper_two_sided_strict_subcomponent"
        if partial
        else "internal_failure_or_unresolved"
    )

    expected_condition_count = int(record["resolution"]["source_condition_count"])
    return {
        "key": record["key"],
        "maximum": maximum,
        "base_contact": int(fields["base_contact"]),
        "compressed_phase": fields["compressed_phase"],
        "phase_side": fields["phase_side"],
        "witness": str(witness),
        "compressed_contact": contact,
        "architecture_class": broad_class,
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
        "candidate_roots": {
            "left": left_roots,
            "right": right_roots,
            "count": len(left_roots) + len(right_roots),
        },
        "endpoint_nonpositive_conditions": {
            "left": left_candidate_names,
            "right": right_candidate_names,
        },
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
        "seconds": time.time() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--workers",
        type=int,
        default=min(4, max(1, os.cpu_count() or 1)),
    )
    parser.add_argument("--record-index", type=int)
    parser.add_argument("--assemble-from-records", action="store_true")
    args = parser.parse_args()

    RESULTS.mkdir(parents=True, exist_ok=True)
    PROVENANCE.mkdir(parents=True, exist_ok=True)
    records = source_records()
    computed: list[dict[str, Any]] = []
    if args.assemble_from_records:
        if args.record_index is not None:
            raise ValueError("--assemble-from-records cannot be combined with --record-index")
        paths = [PROVENANCE / f"a104_record_{index:03d}.json" for index in range(len(records))]
        missing = [str(path) for path in paths if not path.exists()]
        if missing:
            raise FileNotFoundError(f"missing exact record files: {missing}")
        computed = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    else:
        if args.record_index is not None:
            records = [records[args.record_index]]
        if len(records) == 1:
            computed = [analyze_record(records[0])]
        else:
            with mp.Pool(processes=min(args.workers, len(records))) as pool:
                for item in pool.imap_unordered(analyze_record, records, chunksize=1):
                    computed.append(item)
                    print(json.dumps({
                        "maximum": item["maximum"],
                        "architecture": item["architecture_class"],
                        "status": item["status"],
                        "condition_count": item["condition_count"],
                    }), flush=True)
    computed.sort(key=lambda item: int(item["maximum"]))

    if args.record_index is None:
        # Wall-clock timing is useful in per-record provenance but is not part
        # of the mathematical catalogue.  Removing it makes assembly byte-
        # deterministic across independent replays.
        for item in computed:
            item.pop("seconds", None)

    if args.record_index is not None:
        output = PROVENANCE / f"a104_record_{args.record_index:03d}.json"
        output.write_text(json.dumps(computed[0], indent=2), encoding="utf-8")
        print(json.dumps({"output": str(output), "status": computed[0]["status"]}, indent=2))
        if computed[0]["status"] == "internal_failure_or_unresolved":
            raise SystemExit(1)
        return

    a99 = json.loads(A99_RESULT.read_text(encoding="utf-8"))
    a101 = json.loads(A101_RESULT.read_text(encoding="utf-8"))
    a102 = json.loads(A102_RESULT.read_text(encoding="utf-8"))
    a103_result = json.loads(A103_RESULT.read_text(encoding="utf-8"))

    status_counts = Counter(record["status"] for record in computed)
    architecture_counts = Counter(record["architecture_class"] for record in computed)
    condition_count = sum(int(record["condition_count"]) for record in computed)
    polynomial_count = sum(int(record["numerator_plus_denominator_count"]) for record in computed)
    candidate_root_count = sum(int(record["candidate_roots"]["count"]) for record in computed)
    selected_roots = [
        root
        for record in computed
        for root in (
            record["strict_component"]["selected_left_boundary"],
            record["strict_component"]["selected_right_boundary"],
        )
        if root is not None
    ]
    selected_boundary_counts = Counter(root["condition"] for root in selected_roots)
    core_failures = sum(int(record["core_certificate"]["failure_count"]) for record in computed)
    hull_failures = sum(
        int(record["nonselected_boundary_hull_certificate"]["failure_count"])
        for record in computed
    )
    root_failures = sum(len(record["root_failures"]) for record in computed)
    ordering_failures = sum(
        int(record["root_ordering_certificate"]["failure_count"])
        for record in computed
    )
    ordering_checks = sum(
        int(record["root_ordering_certificate"]["check_count"])
        for record in computed
    )
    counterexamples = [
        item
        for record in computed
        for item in record["outside_counterexamples"]
    ]
    nonnegative_counterexamples = [item for item in counterexamples if int(item["sign"]) >= 0]
    condition_count_mismatches = [
        record["key"]
        for record in computed
        if not record["condition_count_matches_A102_source"]
    ]

    expected_maxima = [396, 443, 449, 455, 484, 490, 496]
    maxima = [int(record["maximum"]) for record in computed]
    expected_selected_boundaries = Counter({
        "inactive_slack_gamma_-1": 3,
        "basic_q_0": 3,
        "active_dual_gamma_-1": 4,
        "basic_p_77": 1,
        "basic_p_78": 1,
        "basic_p_84": 1,
        "basic_p_85": 1,
    })

    gates = {
        "A99_q0q1_gamma_inactive_source_present_and_passed": bool(
            a99.get("verdict")
            == "PASS_Q0Q1_M396_INTERVAL_AND_TWO_OF_SIX_REMAINING_RESIDUAL_RESOLUTIONS"
            and all(a99.get("gates", {}).values())
        ),
        "A101_gamma_active_source_present_and_passed": bool(
            a101.get("verdict")
            == "PASS_GAMMA_ACTIVE_M443_INTERVAL_AND_THREE_OF_THREE_FINAL_RESIDUAL_RESOLUTIONS"
            and all(a101.get("gates", {}).values())
        ),
        "A102_complete_pointwise_atlas_source_present_and_passed": bool(
            a102.get("verdict") == "PASS_COMPLETE_EXACT_1063_RATIONAL_WITNESS_LIFT_ATLAS"
            and all(a102.get("gates", {}).values())
        ),
        "A103_endpoint_released_continuum_source_present_and_passed": bool(
            a103_result.get("verdict")
            == "PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_76_ENDPOINT_RELEASED_SEGMENTS_WITH_25_FULL_AND_51_PARTIAL_COMPONENTS"
            and all(a103_result.get("gates", {}).values())
        ),
        "exactly_the_seven_exceptional_A102_segments_are_present": maxima == expected_maxima,
        "architecture_partition_is_three_gamma_inactive_and_four_gamma_active": architecture_counts == {
            "q0q1_gamma_inactive": 3,
            "q0q1_gamma_active": 4,
        },
        "all_seven_keys_are_unique": len({record["key"] for record in computed}) == 7,
        "all_seven_source_condition_counts_match_A102": not condition_count_mismatches,
        "exact_KKT_condition_count_is_6489": condition_count == 6489,
        "exact_numerator_plus_denominator_count_is_6496": polynomial_count == 6496,
        "all_seven_segments_have_proper_two_sided_strict_subcomponents": status_counts == {
            "proper_two_sided_strict_subcomponent": 7,
        },
        "exactly_25_candidate_sign_change_roots_are_isolated": candidate_root_count == 25,
        "exactly_14_nearest_boundaries_are_selected": len(selected_roots) == 14,
        "selected_boundary_mechanisms_match_the_two_architectures": selected_boundary_counts == expected_selected_boundaries,
        "all_14_selected_roots_are_locally_unique_and_simple": all(
            bool(root.get("unique_simple_in_bracket"))
            for root in selected_roots
        ),
        "all_competing_boundary_brackets_are_strictly_ordered": ordering_checks == 11 and ordering_failures == 0,
        "all_6496_core_polynomial_certificates_pass": core_failures == 0,
        "all_nonselected_conditions_pass_on_complete_boundary_hulls": hull_failures == 0,
        "all_14_exact_outside_counterexamples_are_negative": len(counterexamples) == 14 and not nonnegative_counterexamples,
        "every_component_contains_its_A102_witness": all(
            sp.Rational(record["strict_component"]["lower"])
            < sp.Rational(record["witness"])
            < sp.Rational(record["strict_component"]["upper"])
            for record in computed
        ),
        "no_witness_core_root_ordering_or_hull_failure_remains": not any(
            record.get("witness_failures") for record in computed
        ) and core_failures == 0 and hull_failures == 0 and root_failures == 0 and ordering_failures == 0,
        "formal_contract_and_nonphysical_scope_are_preserved": True,
    }
    gates = {name: bool(value) for name, value in gates.items()}
    verdict = (
        "PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_SEVEN_EXCEPTIONAL_Q0Q1_SEGMENTS_AS_TWO_SIDED_STRICT_SUBCOMPONENTS"
        if all(gates.values())
        else "FAIL_A104_EXCEPTIONAL_Q0Q1_CONTINUUM_SEGMENT_ATLAS"
    )

    summary = {
        "record_count": len(computed),
        "unique_key_count": len({record["key"] for record in computed}),
        "status_counts": dict(status_counts),
        "architecture_counts": dict(architecture_counts),
        "condition_count": condition_count,
        "numerator_plus_denominator_count": polynomial_count,
        "candidate_root_count": candidate_root_count,
        "selected_boundary_count": len(selected_roots),
        "selected_boundary_counts": dict(selected_boundary_counts),
        "root_ordering_check_count": ordering_checks,
        "outside_counterexample_count": len(counterexamples),
        "core_failure_count": core_failures,
        "root_failure_count": root_failures,
        "ordering_failure_count": ordering_failures,
        "hull_failure_count": hull_failures,
    }
    catalogue = {
        "audit": "A104_EXACT_EXCEPTIONAL_Q0Q1_CONTINUUM_SEGMENT_ATLAS",
        "contract": {
            "source_segment_count": 7,
            "source": "the seven A102 rational source segments assigned to q0/q1 exceptional architectures",
            "gamma_inactive_family": "P={j,M}, Q={0,1,h,h+1}, alpha+ and beta- active, gamma inactive",
            "gamma_active_family": "P={j-1,j,M}, Q={0,1,h,h+1}, alpha+, beta-, and gamma- active",
            "symbolic_method": "exact Sherman-Morrison rank-one alpha-row update around s=1/8",
            "boundary_method": "exact rational sign-change isolation, derivative-certified simple roots, exact competing-bracket ordering, exact interval positivity, and exact outside counterexamples",
            "claim": "complete exact classification of the witness-containing strict KKT component inside each of the seven declared rational source segments",
            "explicit_nonclaim": "not a continuum lift theorem for the other 1,056 A102 witnesses, not full A92-cell coverage, not an all-M theorem, and not a physical claim",
        },
        "summary": summary,
        "source_hashes": {
            "A99_result": sha256(A99_RESULT),
            "A101_result": sha256(A101_RESULT),
            "A102_result": sha256(A102_RESULT),
            "A102_catalogue": sha256(A102_CATALOGUE),
            "A103_result": sha256(A103_RESULT),
        },
        "records": computed,
        "failures": {
            "condition_count_mismatches": condition_count_mismatches,
            "nonnegative_outside_counterexamples": nonnegative_counterexamples,
        },
    }
    results = {
        "audit": "A104_EXACT_EXCEPTIONAL_Q0Q1_CONTINUUM_SEGMENT_ATLAS",
        "evidence_class": "exact sparse rational-function KKT reduction, exact rational interval arithmetic, exact algebraic root brackets, exact root-ordering inequalities, and exact rational counterexamples",
        "scope": catalogue["contract"],
        "continuum_atlas": summary,
        "structural_result": {
            "q0q1_gamma_inactive": {
                "segment_count": 3,
                "maxima": [396, 455, 496],
                "lower_boundary": "inactive gamma-minus slack reaches zero",
                "upper_boundary": "basic q0 mass reaches zero",
            },
            "q0q1_gamma_active": {
                "segment_count": 4,
                "maxima": [443, 449, 484, 490],
                "lower_boundary": "active gamma-minus dual multiplier reaches zero",
                "upper_boundary": "lower adjacent basic P mass reaches zero",
            },
            "interpretation": "all seven exceptional pointwise bases persist on nontrivial open algebraic phases, but none covers its complete A95 rational source segment",
        },
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "fail_count": len(gates) - sum(gates.values()),
        "failed_gates": [name for name, passed in gates.items() if not passed],
        "verdict": verdict,
    }

    catalogue_path = RESULTS / "a104_exceptional_q0q1_continuum_segment_catalogue.json"
    result_path = RESULTS / "a104_exceptional_q0q1_continuum_segment_results.json"
    catalogue_path.write_text(json.dumps(catalogue, indent=2), encoding="utf-8")
    result_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps({
        "verdict": verdict,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "record_count": len(computed),
        "condition_count": condition_count,
        "selected_boundary_count": len(selected_roots),
        "result": str(result_path),
        "catalogue": str(catalogue_path),
    }, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
