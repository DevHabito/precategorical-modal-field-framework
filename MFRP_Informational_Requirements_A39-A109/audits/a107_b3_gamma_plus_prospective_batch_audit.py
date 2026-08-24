#!/usr/bin/env python3
"""A107-B3 prospective exact gamma-plus batch audit.

The preregistration was frozen and SHA256-hashed before this audit was
executed. The audit selects canonical gamma-plus ranks 18..25 inclusive with
no replacement, applies the exact A107-B1 local-stability machinery, tests the
upper-adjacent-atom boundary mechanism, and evaluates the preregistered
M mod 5 finite predictive rule only on its declared scope.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

import a105_legacy_two_band_continuum_segment_atlas_audit as a105
import a107_min_legacy_gamma_plus_first_record_audit as a107min
import a107_b1_gamma_plus_preregistered_batch_audit as a107b1

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
DEFAULT_PREREG = ROOT / "preregistrations" / "a107_a109" / "A107_B3_PREREGISTRATION.json"
EXPECTED_PREREG_SHA256 = "1eb7952fc98af4a865ef9943ff960ee27c53e74fc7bb7742e13dcae5677917d9"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def phase_from_source_key(source_key: str) -> str:
    for part in source_key.split("|"):
        if part.startswith("phase="):
            return part.split("=", 1)[1]
    return "UNKNOWN"


def residue_prediction(maximum: int, phase: str) -> tuple[bool, str | None]:
    residue = maximum % 5
    if phase != "unique_b_plus_1":
        return False, None
    if residue in {0, 4}:
        return True, "proper_strict_subcomponent"
    if residue in {1, 2}:
        return True, "full_segment_coverage"
    return False, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preregistration", default=str(DEFAULT_PREREG))
    parser.add_argument("--output", default=str(RESULTS / "a107_b3_gamma_plus_prospective_batch_result.json"))
    args = parser.parse_args()

    prereg = Path(args.preregistration)
    prereg_hash = sha256(prereg)
    if prereg_hash != EXPECTED_PREREG_SHA256:
        raise RuntimeError(f"preregistration hash mismatch: {prereg_hash}")

    source = a107b1.source_records()
    if len(source) != 922:
        raise RuntimeError(f"expected 922 gamma-plus records, found {len(source)}")
    batch = source[17:25]  # canonical ranks 18..25 inclusive
    if len(batch) != 8:
        raise RuntimeError("batch selection did not produce exactly 8 records")

    original = a105.build_integer_polynomials
    outputs: list[dict[str, Any]] = []
    try:
        a105.build_integer_polynomials = a107min.build_integer_polynomials
        for canonical_rank, record in enumerate(batch, start=18):
            analyzed = a105.analyze_record(record)
            analyzed["architecture_class"] = "legacy_three_band_gamma_plus"
            regression = a107b1.direct_checkpoint_regression(record, analyzed) if "strict_component" in analyzed else {
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
            success, reasons = a107b1.per_record_success(record, analyzed, regression)
            maximum = int(record["key_fields"]["maximum"])
            j = int(record["key_fields"]["compressed_maximizer_contact"])
            phase = phase_from_source_key(str(record["key"]))
            in_scope, predicted_class = residue_prediction(maximum, phase)
            observed_class = analyzed.get("status")
            residue_match = (observed_class == predicted_class) if in_scope else None
            outputs.append({
                "canonical_rank": canonical_rank,
                "source_key": record["key"],
                "maximum": maximum,
                "M_mod_5": maximum % 5,
                "phase": phase,
                "contact_j": j,
                "witness": str(record["key_fields"]["witness"]),
                "segment_open_bounds": record["segment_open_bounds"],
                "expected_upper_adjacent_boundary_condition": f"basic_p_{j+1}",
                "residue_prediction": {
                    "in_scope": in_scope,
                    "predicted_class": predicted_class,
                    "observed_class": observed_class,
                    "exact_match": residue_match,
                },
                "analysis": analyzed,
                "direct_checkpoint_regression": regression,
                "per_record_success": success,
                "failure_reasons": reasons,
                "selected_boundaries": a107b1.semantic_selected_boundaries(analyzed),
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
        primary_verdict = "INCONCLUSIVE_BATCH"

    selected_boundaries = [
        (x["canonical_rank"], b["side"], b["condition"], x["expected_upper_adjacent_boundary_condition"])
        for x in outputs for b in x["selected_boundaries"]
    ]
    partial_records = [x for x in outputs if x["analysis"].get("status") == "proper_strict_subcomponent"]
    if primary_verdict == "INCONCLUSIVE_BATCH":
        boundary_verdict = "NOT_ADJUDICATED_DUE_TO_INCONCLUSIVE_PRIMARY"
    elif not partial_records:
        boundary_verdict = "NOT_TESTED_BATCH"
    elif all(condition == expected for _, _, condition, expected in selected_boundaries):
        boundary_verdict = "SUPPORT_BATCH"
    else:
        boundary_verdict = "REFUTED_BATCH"

    in_scope = [x for x in outputs if x["residue_prediction"]["in_scope"]]
    residue_mismatches = [x for x in in_scope if x["residue_prediction"]["exact_match"] is False]
    if primary_verdict == "INCONCLUSIVE_BATCH":
        residue_verdict = "NOT_ADJUDICATED_DUE_TO_INCONCLUSIVE_PRIMARY"
    elif not in_scope:
        residue_verdict = "NOT_TESTED_NO_IN_SCOPE_RECORDS"
    elif residue_mismatches:
        residue_verdict = "REFUTED_B3_FINITE_RULE"
    else:
        residue_verdict = "PROSPECTIVE_SUPPORT_B3_FINITE_RULE"

    status_counts = Counter(x["analysis"].get("status", "missing") for x in outputs)
    boundary_condition_counts = Counter(cond for _, _, cond, _ in selected_boundaries)
    boundary_side_counts = Counter(side for _, side, _, _ in selected_boundaries)
    total_conditions = sum(int(x["analysis"].get("condition_count", 0)) for x in outputs)
    total_checkpoint_comparisons = sum(int(x["direct_checkpoint_regression"]["comparison_count"]) for x in outputs)
    total_checkpoint_mismatches = sum(int(x["direct_checkpoint_regression"]["mismatch_count"]) for x in outputs)

    result = {
        "audit": "A107-B3_PROSPECTIVE_GAMMA_PLUS_BATCH",
        "preregistration": {
            "path": str(prereg),
            "sha256": prereg_hash,
            "expected_sha256": EXPECTED_PREREG_SHA256,
            "hash_match": prereg_hash == EXPECTED_PREREG_SHA256,
        },
        "source_gamma_plus_count": len(source),
        "selection": {
            "canonical_ranks": list(range(18, 26)),
            "batch_size": len(batch),
            "selection_rule": "canonical gamma-plus order by (maximum, compressed_contact, witness), ranks 18..25 inclusive, no replacement",
        },
        "summary": {
            "status_counts": dict(status_counts),
            "per_record_success_count": success_count,
            "per_record_failure_count": 8 - success_count,
            "total_KKT_condition_count": total_conditions,
            "total_direct_checkpoint_comparisons": total_checkpoint_comparisons,
            "total_direct_checkpoint_mismatches": total_checkpoint_mismatches,
            "partial_record_count": len(partial_records),
            "selected_boundary_count": len(selected_boundaries),
            "boundary_condition_counts": dict(boundary_condition_counts),
            "boundary_side_counts": dict(boundary_side_counts),
            "witness_failure_count": len(witness_failures),
            "unresolved_count": len(unresolved),
            "other_failure_count": len(other_failures),
            "residue_prediction_in_scope_count": len(in_scope),
            "residue_prediction_match_count": len(in_scope) - len(residue_mismatches),
            "residue_prediction_mismatch_count": len(residue_mismatches),
        },
        "primary_verdict": primary_verdict,
        "secondary_upper_adjacent_atom_hypothesis": {
            "verdict": boundary_verdict,
            "selected_boundaries": [
                {"canonical_rank": rank, "side": side, "condition": condition, "expected": expected}
                for rank, side, condition, expected in selected_boundaries
            ],
        },
        "prospective_residue_prediction": {
            "verdict": residue_verdict,
            "scope_count": len(in_scope),
            "mismatch_count": len(residue_mismatches),
            "mismatches": [
                {
                    "canonical_rank": x["canonical_rank"],
                    "maximum": x["maximum"],
                    "M_mod_5": x["M_mod_5"],
                    "phase": x["phase"],
                    "predicted_class": x["residue_prediction"]["predicted_class"],
                    "observed_class": x["residue_prediction"]["observed_class"],
                }
                for x in residue_mismatches
            ],
        },
        "records": outputs,
        "scope": {
            "claim": "exact local-continuum classification only for canonical gamma-plus ranks 18..25",
            "nonclaims": [
                "not a theorem for all 922 gamma-plus witnesses",
                "not an all-M theorem",
                "not a claim for residue 3",
                "not a claim for non-unique_b_plus_1 phases",
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
        "boundary_verdict": boundary_verdict,
        "residue_verdict": residue_verdict,
        "status_counts": dict(status_counts),
        "success_count": success_count,
        "selected_boundary_count": len(selected_boundaries),
        "boundary_condition_counts": dict(boundary_condition_counts),
        "boundary_side_counts": dict(boundary_side_counts),
        "residue_in_scope_count": len(in_scope),
        "residue_mismatch_count": len(residue_mismatches),
        "total_KKT_condition_count": total_conditions,
        "checkpoint_comparisons": total_checkpoint_comparisons,
        "checkpoint_mismatches": total_checkpoint_mismatches,
        "output": str(out),
    }, indent=2))


if __name__ == "__main__":
    main()
