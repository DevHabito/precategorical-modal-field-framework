#!/usr/bin/env python3
"""Portable exact holdout runner for the A109 gamma-plus adjacent-boundary program.

This file is a repository-path adaptation of the frozen shard runners used in
A109. It does not choose records or predictions. The caller supplies a frozen
preregistration and its expected SHA-256 hash; the requested rank range must be
one of the preregistered shards.
"""
from __future__ import annotations
import argparse, hashlib, json, sys, time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "audits"))
import a105_legacy_two_band_continuum_segment_atlas_audit as a105
import a107_min_legacy_gamma_plus_first_record_audit as amin
import a107_b1_gamma_plus_preregistered_batch_audit as b1

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--preregistration", required=True)
    ap.add_argument("--expected-sha256", required=True)
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--end", type=int, required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    prereg = Path(args.preregistration)
    if not prereg.is_absolute():
        prereg = ROOT / prereg
    digest = sha256(prereg)
    if digest != args.expected_sha256:
        raise RuntimeError(f"preregistration hash mismatch: {digest}")

    pr = json.loads(prereg.read_text(encoding="utf-8"))
    allowed = [tuple(x) for x in pr["holdout_selection"]["shards"]]
    if (args.start, args.end) not in allowed:
        raise RuntimeError("requested range is not a frozen preregistered shard")

    predictions = {int(x["canonical_rank"]): x for x in pr["holdout_predictions"]}
    source = b1.source_records()
    batch = source[args.start - 1:args.end]
    outputs = []
    original = a105.build_integer_polynomials

    for rank, record in enumerate(batch, start=args.start):
        started = time.time()
        prediction = predictions[rank]
        try:
            a105.build_integer_polynomials = amin.build_integer_polynomials
            atlas = a105.analyze_record(record)
        finally:
            a105.build_integer_polynomials = original
        atlas["architecture_class"] = "legacy_three_band_gamma_plus"
        selected = b1.semantic_selected_boundaries(atlas)
        regression = b1.direct_checkpoint_regression(record, atlas) if "strict_component" in atlas else None
        core = atlas.get("core_certificate", {})
        hull = atlas.get("nonselected_boundary_hull_certificate", {})
        failures = []
        if prediction["predicted_class"] != "NO_CLASSIFICATION":
            if atlas.get("status") != prediction["predicted_class"]:
                failures.append("class_mismatch")
            if selected != prediction["predicted_boundaries"]:
                failures.append("boundary_mismatch")
        if atlas.get("root_failures"):
            failures.append("root_failure")
        if core.get("failure_count", 0):
            failures.append("core_certificate_failure")
        if hull.get("failure_count", 0):
            failures.append("hull_certificate_failure")
        if regression and (
            regression["mismatch_count"]
            or regression["positivity_failure_count"]
            or regression["outside_sign_failure_count"]
        ):
            failures.append("direct_regression_failure")

        outputs.append({
            "canonical_rank": rank,
            "source_key": record["key"],
            "maximum": int(record["key_fields"]["maximum"]),
            "contact_j": int(record["key_fields"]["compressed_maximizer_contact"]),
            "frozen_prediction": prediction,
            "atlas_class": atlas.get("status"),
            "selected_boundaries": selected,
            "endpoint_nonpositive_conditions": atlas.get("endpoint_nonpositive_conditions"),
            "core_certificate_summary": {k: core.get(k) for k in ["condition_count", "pass_count", "failure_count", "method_counts"]},
            "hull_certificate_summary": {k: hull.get(k) for k in ["condition_count", "pass_count", "failure_count", "method_counts"]},
            "root_failure_count": len(atlas.get("root_failures", [])),
            "direct_regression_summary": None if regression is None else {k: regression[k] for k in ["checkpoint_count", "comparison_count", "mismatch_count", "positivity_failure_count", "outside_sign_failure_count"]},
            "failures": failures,
            "strict_component": atlas.get("strict_component"),
            "outside_counterexamples": atlas.get("outside_counterexamples"),
            "seconds": time.time() - started,
        })

    failures = [{"rank": x["canonical_rank"], "failures": x["failures"]} for x in outputs if x["failures"]]
    verdict = "REFUTED_A109_TWO_SIDED_RULE" if failures else "PASS_A109_TWO_SIDED_HOLDOUT"
    result = {
        "audit": "A109_PORTABLE_TWO_SIDED_ADJACENT_BOUNDARY_HOLDOUT_SHARD",
        "preregistration_sha256": digest,
        "rank_range": [args.start, args.end],
        "verdict": verdict,
        "summary": {
            "record_count": len(outputs),
            "predicted_class_counts": dict(Counter(x["frozen_prediction"]["predicted_class"] for x in outputs)),
            "atlas_class_counts": dict(Counter(x["atlas_class"] for x in outputs)),
            "match_count": sum(not x["failures"] for x in outputs),
            "partial_count": sum(x["atlas_class"] == "proper_strict_subcomponent" for x in outputs),
            "direct_comparisons": sum((x["direct_regression_summary"] or {}).get("comparison_count", 0) for x in outputs),
            "direct_mismatches": sum((x["direct_regression_summary"] or {}).get("mismatch_count", 0) for x in outputs),
            "core_failures": sum((x["core_certificate_summary"].get("failure_count") or 0) for x in outputs),
            "hull_failures": sum((x["hull_certificate_summary"].get("failure_count") or 0) for x in outputs),
        },
        "failures": failures,
        "records": outputs,
        "scope": {"nonclaims": pr.get("nonclaims", [])},
    }
    out = Path(args.output)
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"verdict": verdict, **result["summary"], "output": str(out)}, indent=2))

if __name__ == "__main__":
    main()
