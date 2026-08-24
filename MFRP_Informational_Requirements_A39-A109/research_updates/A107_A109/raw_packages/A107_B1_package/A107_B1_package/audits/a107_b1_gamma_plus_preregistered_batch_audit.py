#!/usr/bin/env python3
"""A107-B1 preregistered exact gamma-plus batch audit.

The preregistration is external and hashed before execution. This script does
not choose favorable records: it loads the canonical gamma-plus order used by
A107-MIN, skips canonical rank 1 (already tested there), and analyzes ranks
2..9 inclusive.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

import sympy as sp

import a103_endpoint_released_continuum_segment_atlas_audit as a103
import a105_legacy_two_band_continuum_segment_atlas_audit as a105
import a107_min_legacy_gamma_plus_first_record_audit as a107min

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A102_CATALOGUE = RESULTS / "a102_complete_rational_witness_lift_atlas_catalogue.json"
DEFAULT_PREREG = Path("/mnt/data/A107_B1_PREREGISTRATION.json")
EXPECTED_PREREG_SHA256 = "eb2a7cdba3e490c4acc0a0e113fb398b38fb46524ccacfd66e898a99c52fe501"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def source_records() -> list[dict[str, Any]]:
    payload = json.loads(A102_CATALOGUE.read_text(encoding="utf-8"))
    records = [
        r for r in payload["records"]
        if r["resolution"]["detailed_class"] == "legacy_three_band_gamma_plus"
    ]
    records.sort(key=lambda r: (
        int(r["key_fields"]["maximum"]),
        int(r["key_fields"]["compressed_maximizer_contact"]),
        str(r["key_fields"]["witness"]),
    ))
    return records


def direct_checkpoint_regression(record: dict[str, Any], analyzed: dict[str, Any]) -> dict[str, Any]:
    fields = record["key_fields"]
    maximum = int(fields["maximum"])
    contact = int(fields["compressed_maximizer_contact"])
    witness = sp.Rational(fields["witness"])
    denominator, symbolic = a107min.rank_one_gamma_plus_conditions(maximum, contact, a107min.REF)

    component = analyzed["strict_component"]
    lower = sp.Rational(component["lower"])
    upper = sp.Rational(component["upper"])
    checkpoints: list[tuple[str, sp.Rational, str | None]] = [
        ("interior_left", (lower + witness) / 2, None),
        ("witness", witness, None),
        ("interior_right", (witness + upper) / 2, None),
    ]
    for item in analyzed.get("outside_counterexamples", []):
        checkpoints.append((f"outside_{item['side']}", sp.Rational(item["point"]), str(item["condition"])))

    total = 0
    mismatches: list[dict[str, str]] = []
    checkpoint_rows: list[dict[str, Any]] = []
    positivity_failures: list[dict[str, str]] = []
    outside_sign_failures: list[dict[str, str]] = []
    symbolic_names = [name for name, _ in symbolic]

    for label, probe, expected_negative in checkpoints:
        direct = a107min.direct_gamma_plus_conditions(maximum, contact, probe)
        if [name for name, _ in direct] != symbolic_names:
            raise AssertionError("direct/symbolic condition order mismatch")
        den_value = a103.ev(denominator, probe)
        direct_map = dict(direct)
        local_mismatches: list[str] = []
        for (name, poly), (_, value) in zip(symbolic, direct):
            total += 1
            if a103.ev(poly, probe) != den_value * value:
                local_mismatches.append(name)
                mismatches.append({"checkpoint": label, "condition": name})
        if expected_negative is None:
            bad = [name for name, value in direct if value <= 0]
            if bad:
                positivity_failures.extend({"checkpoint": label, "condition": name} for name in bad)
        else:
            if direct_map[expected_negative] >= 0:
                outside_sign_failures.append({"checkpoint": label, "condition": expected_negative})
        checkpoint_rows.append({
            "label": label,
            "probe": str(probe),
            "expected_negative_condition": expected_negative,
            "comparison_count": len(direct),
            "mismatch_count": len(local_mismatches),
            "mismatches": local_mismatches,
        })

    return {
        "checkpoint_count": len(checkpoints),
        "comparison_count": total,
        "mismatch_count": len(mismatches),
        "positivity_failure_count": len(positivity_failures),
        "outside_sign_failure_count": len(outside_sign_failures),
        "mismatches": mismatches,
        "positivity_failures": positivity_failures,
        "outside_sign_failures": outside_sign_failures,
        "checkpoints": checkpoint_rows,
    }


def per_record_success(record: dict[str, Any], analyzed: dict[str, Any], regression: dict[str, Any]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    if analyzed.get("status") not in {"full_segment_coverage", "proper_strict_subcomponent"}:
        reasons.append(f"status={analyzed.get('status')}")
    if not analyzed.get("condition_count_matches_A102_source", False):
        reasons.append("condition_count_mismatch")
    if int(analyzed.get("core_certificate", {}).get("failure_count", 1)) != 0:
        reasons.append("core_certificate_failure")
    if int(analyzed.get("nonselected_boundary_hull_certificate", {}).get("failure_count", 1)) != 0:
        reasons.append("hull_certificate_failure")
    if int(analyzed.get("root_ordering_certificate", {}).get("failure_count", 1)) != 0:
        reasons.append("root_ordering_failure")
    if analyzed.get("root_failures"):
        reasons.append("root_certification_failure")
    selected = [
        x for x in (
            analyzed.get("strict_component", {}).get("selected_left_boundary"),
            analyzed.get("strict_component", {}).get("selected_right_boundary"),
        ) if x is not None
    ]
    outside = analyzed.get("outside_counterexamples", [])
    if len(outside) != len(selected) or any(int(x["sign"]) >= 0 for x in outside):
        reasons.append("outside_counterexample_failure")
    if regression["mismatch_count"] != 0:
        reasons.append("direct_rank_one_mismatch")
    if regression["positivity_failure_count"] != 0:
        reasons.append("direct_interior_nonpositive")
    if regression["outside_sign_failure_count"] != 0:
        reasons.append("direct_outside_sign_failure")
    return not reasons, reasons


def semantic_selected_boundaries(analyzed: dict[str, Any]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for side, field in (("left", "selected_left_boundary"), ("right", "selected_right_boundary")):
        root = analyzed.get("strict_component", {}).get(field)
        if root is not None:
            out.append({"side": side, "condition": str(root["condition"])})
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preregistration", default=str(DEFAULT_PREREG))
    parser.add_argument("--output", default=str(RESULTS / "a107_b1_gamma_plus_batch_result.json"))
    args = parser.parse_args()

    prereg = Path(args.preregistration)
    prereg_hash = sha256(prereg)
    if prereg_hash != EXPECTED_PREREG_SHA256:
        raise RuntimeError(f"preregistration hash mismatch: {prereg_hash}")

    source = source_records()
    if len(source) != 922:
        raise RuntimeError(f"expected 922 gamma-plus records, found {len(source)}")
    batch = source[1:9]  # canonical ranks 2..9 inclusive
    if len(batch) != 8:
        raise RuntimeError("batch selection did not produce exactly 8 records")

    original = a105.build_integer_polynomials
    outputs: list[dict[str, Any]] = []
    try:
        a105.build_integer_polynomials = a107min.build_integer_polynomials
        for canonical_rank, record in enumerate(batch, start=2):
            analyzed = a105.analyze_record(record)
            analyzed["architecture_class"] = "legacy_three_band_gamma_plus"
            regression = direct_checkpoint_regression(record, analyzed) if "strict_component" in analyzed else {
                "checkpoint_count": 0,
                "comparison_count": 0,
                "mismatch_count": 0,
                "positivity_failure_count": 0,
                "outside_sign_failure_count": 0,
                "mismatches": [],
                "positivity_failures": [],
                "outside_sign_failures": [],
                "checkpoints": [],
            }
            success, reasons = per_record_success(record, analyzed, regression)
            j = int(record["key_fields"]["compressed_maximizer_contact"])
            outputs.append({
                "canonical_rank": canonical_rank,
                "source_key": record["key"],
                "maximum": int(record["key_fields"]["maximum"]),
                "contact_j": j,
                "witness": str(record["key_fields"]["witness"]),
                "segment_open_bounds": record["segment_open_bounds"],
                "expected_upper_adjacent_boundary_condition": f"basic_p_{j+1}",
                "analysis": analyzed,
                "direct_checkpoint_regression": regression,
                "per_record_success": success,
                "failure_reasons": reasons,
                "selected_boundaries": semantic_selected_boundaries(analyzed),
            })
    finally:
        a105.build_integer_polynomials = original

    success_count = sum(bool(x["per_record_success"]) for x in outputs)
    witness_failures = [x for x in outputs if x["analysis"].get("status") == "witness_failure"]
    unresolved = [x for x in outputs if x["analysis"].get("status") == "internal_failure_or_unresolved"]
    other_failures = [x for x in outputs if not x["per_record_success"] and x not in witness_failures and x not in unresolved]

    if success_count == 8:
        primary_verdict = "PASS_BATCH_LOCAL_STABILITY"
    elif witness_failures:
        primary_verdict = "FAIL_BATCH_LOCAL_STABILITY"
    else:
        # Source mismatch, proof/certification failure, or implementation disagreement
        # is not promoted to a mathematical counterexample.
        primary_verdict = "INCONCLUSIVE_BATCH"

    selected_boundaries = [
        (x["canonical_rank"], b["side"], b["condition"], x["expected_upper_adjacent_boundary_condition"])
        for x in outputs for b in x["selected_boundaries"]
    ]
    if primary_verdict == "INCONCLUSIVE_BATCH":
        secondary_verdict = "NOT_ADJUDICATED_DUE_TO_INCONCLUSIVE_PRIMARY"
    elif not selected_boundaries:
        secondary_verdict = "NOT_TESTED_BATCH"
    elif all(condition == expected for _, _, condition, expected in selected_boundaries):
        secondary_verdict = "SUPPORT_BATCH"
    else:
        secondary_verdict = "REFUTED_BATCH"

    status_counts = Counter(x["analysis"].get("status", "missing") for x in outputs)
    boundary_condition_counts = Counter(cond for _, _, cond, _ in selected_boundaries)
    boundary_side_counts = Counter(side for _, side, _, _ in selected_boundaries)
    total_conditions = sum(int(x["analysis"].get("condition_count", 0)) for x in outputs)
    total_checkpoint_comparisons = sum(int(x["direct_checkpoint_regression"]["comparison_count"]) for x in outputs)
    total_checkpoint_mismatches = sum(int(x["direct_checkpoint_regression"]["mismatch_count"]) for x in outputs)

    result = {
        "audit": "A107-B1_PREREGISTERED_GAMMA_PLUS_BATCH",
        "preregistration": {
            "path": str(prereg),
            "sha256": prereg_hash,
            "expected_sha256": EXPECTED_PREREG_SHA256,
            "hash_match": prereg_hash == EXPECTED_PREREG_SHA256,
        },
        "source_gamma_plus_count": len(source),
        "selection": {
            "canonical_ranks": [2, 3, 4, 5, 6, 7, 8, 9],
            "batch_size": len(batch),
            "selection_rule": "canonical gamma-plus order by (maximum, compressed_contact, witness), excluding already-tested rank 1",
        },
        "summary": {
            "status_counts": dict(status_counts),
            "per_record_success_count": success_count,
            "per_record_failure_count": 8 - success_count,
            "total_KKT_condition_count": total_conditions,
            "total_direct_checkpoint_comparisons": total_checkpoint_comparisons,
            "total_direct_checkpoint_mismatches": total_checkpoint_mismatches,
            "selected_boundary_count": len(selected_boundaries),
            "boundary_condition_counts": dict(boundary_condition_counts),
            "boundary_side_counts": dict(boundary_side_counts),
            "witness_failure_count": len(witness_failures),
            "unresolved_count": len(unresolved),
            "other_failure_count": len(other_failures),
        },
        "primary_verdict": primary_verdict,
        "secondary_upper_adjacent_atom_hypothesis": {
            "verdict": secondary_verdict,
            "selected_boundaries": [
                {"canonical_rank": rank, "side": side, "condition": condition, "expected": expected}
                for rank, side, condition, expected in selected_boundaries
            ],
        },
        "records": outputs,
        "scope": {
            "claim": "exact local-continuum classification only for canonical gamma-plus ranks 2..9",
            "nonclaims": [
                "not a theorem for all 922 gamma-plus witnesses",
                "not an all-M theorem",
                "not beyond the A95/A102 source segments",
                "not a physical claim",
            ],
        },
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({
        "primary_verdict": primary_verdict,
        "secondary_verdict": secondary_verdict,
        "status_counts": dict(status_counts),
        "success_count": success_count,
        "selected_boundary_count": len(selected_boundaries),
        "boundary_condition_counts": dict(boundary_condition_counts),
        "boundary_side_counts": dict(boundary_side_counts),
        "total_KKT_condition_count": total_conditions,
        "checkpoint_comparisons": total_checkpoint_comparisons,
        "checkpoint_mismatches": total_checkpoint_mismatches,
        "output": str(out),
    }, indent=2))


if __name__ == "__main__":
    main()
