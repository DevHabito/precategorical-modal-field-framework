#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install 'PyYAML>=6.0'", file=sys.stderr)
    raise SystemExit(2)

REQUIRED_TOP = {
    "schema_version", "audit", "source", "integrity", "environment",
    "randomness", "parameters", "generators", "procedure", "validation",
    "expected_outputs", "interpretation", "reproduction",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def get_dot(data: Any, path: str) -> Any:
    cur = data
    for part in path.split("."):
        if isinstance(cur, dict):
            cur = cur[part]
        elif isinstance(cur, list):
            cur = cur[int(part)]
        else:
            raise KeyError(path)
    return cur


def equal(expected: Any, actual: Any, abs_tol: float, rel_tol: float) -> bool:
    if isinstance(expected, bool) or isinstance(actual, bool):
        return expected is actual
    if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
        return math.isclose(float(expected), float(actual), abs_tol=abs_tol, rel_tol=rel_tol)
    return expected == actual


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=None, help="Repository root; defaults to parent of tools/.")
    parser.add_argument("--skip-output-hashes", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    protocol_dir = root / "protocols"
    classification_path = root / "docs" / "RESULT_CLASSIFICATION.json"
    errors: list[str] = []
    notices: list[str] = []

    if not classification_path.exists():
        errors.append(f"Missing classification matrix: {classification_path}")
        claim_ids = set()
    else:
        classification = json.loads(classification_path.read_text(encoding="utf-8"))
        claim_ids = {row["claim_id"] for row in classification}

    seen_ids: set[str] = set()
    files = sorted(p for p in protocol_dir.glob("A*.yaml") if p.is_file())
    if not files:
        errors.append(f"No protocol YAML files found in {protocol_dir}")

    for protocol_path in files:
        try:
            contract = yaml.safe_load(protocol_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{protocol_path}: YAML parse failed: {exc}")
            continue

        missing = REQUIRED_TOP - set(contract or {})
        if missing:
            errors.append(f"{protocol_path}: missing top-level fields {sorted(missing)}")
            continue

        audit_id = contract["audit"]["id"]
        if audit_id in seen_ids:
            errors.append(f"Duplicate audit id: {audit_id}")
        seen_ids.add(audit_id)

        for cid in contract["audit"].get("claim_ids", []):
            if cid not in claim_ids:
                errors.append(f"{audit_id}: unknown claim_id {cid}")

        source = root / contract["source"]["script"]
        summary_path = root / contract["source"]["summary"]
        for label, path in (("script", source), ("summary", summary_path)):
            if not path.exists():
                errors.append(f"{audit_id}: missing {label}: {path}")

        if source.exists():
            actual = sha256(source)
            expected = contract["integrity"]["script_sha256"]
            if actual != expected:
                errors.append(f"{audit_id}: script hash mismatch: {actual} != {expected}")
        if summary_path.exists():
            actual = sha256(summary_path)
            expected = contract["integrity"]["summary_sha256"]
            if actual != expected:
                errors.append(f"{audit_id}: summary hash mismatch: {actual} != {expected}")

            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            seed = contract["randomness"].get("seed")
            if seed is not None and summary.get("seed") != seed:
                errors.append(f"{audit_id}: seed mismatch: summary={summary.get('seed')} protocol={seed}")

            expected_verdict = contract["validation"].get("expected_verdict")
            if expected_verdict is not None and summary.get("verdict") != expected_verdict:
                errors.append(f"{audit_id}: verdict mismatch: {summary.get('verdict')} != {expected_verdict}")

            expected_gates = contract["validation"].get("expected_gates", {})
            actual_gates = summary.get("gates", {})
            for gate, expected_value in expected_gates.items():
                if gate not in actual_gates:
                    errors.append(f"{audit_id}: gate missing from summary: {gate}")
                elif actual_gates[gate] != expected_value:
                    errors.append(f"{audit_id}: gate {gate} mismatch: {actual_gates[gate]} != {expected_value}")

            tol = contract["validation"].get("numeric_tolerance", {})
            abs_tol = float(tol.get("absolute", 1e-12))
            rel_tol = float(tol.get("relative", 1e-10))
            for key, expected_value in contract["validation"].get("metric_snapshot", {}).items():
                try:
                    actual_value = get_dot(summary, key)
                except Exception:
                    errors.append(f"{audit_id}: metric path missing: {key}")
                    continue
                if not equal(expected_value, actual_value, abs_tol, rel_tol):
                    errors.append(f"{audit_id}: metric {key} mismatch: {actual_value!r} != {expected_value!r}")

        for item in contract.get("expected_outputs", []):
            path = root / item["path"]
            if not path.exists():
                errors.append(f"{audit_id}: missing expected output {path}")
            elif not args.skip_output_hashes:
                actual = sha256(path)
                if actual != item["sha256"]:
                    errors.append(f"{audit_id}: output hash mismatch {item['path']}")

        notices.append(f"{audit_id}: validated")

    print(f"Validated {len(files)} protocol contracts.")
    for notice in notices:
        print(f"  OK {notice}")
    if errors:
        print(f"Protocol validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"  ERROR {error}", file=sys.stderr)
        return 1
    print("Protocol validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
