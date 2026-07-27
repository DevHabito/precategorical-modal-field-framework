#!/usr/bin/env python3
"""A95 exact rational-witness lift and restricted-family obstruction audit.

A94 proves the complete compressed-objective phase atlas on 858 algebraic
b-cells for 14 <= M <= 520 and 129/1000 <= s <= 133/1000.  A95 asks a
strictly narrower, but essential, question:

    Does the compressed maximizer lift to the previously declared full-LP
    contact families?

Every fixed A94 phase contributes one exact rational interior witness.  Every
simple adjacent transition contributes one witness on each open side.  This
produces 1,063 exact phase-segment witnesses.  If j is the A94 compressed
maximizer at a witness, A95 tests the natural lift triad

    C_j:       P={0,j,M},       gamma inactive,
    L_j^-:     P={0,j-1,j,M},   gamma-,
    L_j^+:     P={0,j,j+1,M},   gamma+,

with Q={1,h,h+1}, active alpha+, beta-, and the frozen central-mean error
contract.  Each candidate is checked against the complete finite LP KKT
system: basic variables, active dual multipliers, every nonbasic reduced cost,
and every inactive band slack.

The audit is a rational-witness theorem, not an interval lift theorem.  It
records where the natural lift succeeds and where it fails.  At the first
failure, and for the complete obstruction prefix through the first A90
offset-three support M=325, it additionally exhausts every previously declared
F2/F3 contact candidate.  This proves that the failure is not repaired by
choosing a distant contact inside those restricted families.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import multiprocessing as mp
import os
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A78_SCRIPT = HERE / "a78_rational_probe_contact_selection_audit.py"
A94_RESULT = RESULTS / "a94_all_cell_continuum_one_variation_results.json"
A94_CATALOGUE = RESULTS / "a94_all_cell_continuum_one_variation_catalogue.json"
A90_RESULT = RESULTS / "a90_prethreshold_all_k_one_variation_results.json"

EXPECTED_CELL_COUNT = 858
EXPECTED_SEGMENT_COUNT = 1063
EXPECTED_CANDIDATE_EVALUATION_COUNT = 3189
EXPECTED_UNIQUE_LIFT_COUNT = 980
EXPECTED_OBSTRUCTION_COUNT = 83
EXPECTED_OBSTRUCTION_SUPPORT_COUNT = 75
EXPECTED_PASS_COUNTS = {
    "three_band_gamma_plus": 922,
    "three_band_gamma_minus": 18,
    "two_band_compressed": 40,
}
EXPECTED_OBSTRUCTION_PHASE_COUNTS = {
    "b_plus_1_to_b_plus_2::right": 46,
    "unique_b_plus_3::full": 14,
    "unique_b_plus_2::full": 12,
    "b_plus_2_to_b_plus_3::right": 11,
}
EXPECTED_FIRST_OBSTRUCTION_M = 125
EXPECTED_FIRST_OFFSET_THREE_M = 325
EXPECTED_PREFIX_OBSTRUCTION_COUNT = 29
EXPECTED_PREFIX_CANDIDATE_COUNT = 19421
EXPECTED_PREFIX_STATUS_COUNTS = {
    "primal_infeasible": 18323,
    "reduced_cost_infeasible": 1069,
    "active_dual_infeasible": 29,
}

A78 = None


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


def worker_initializer() -> None:
    global A78
    A78 = load_module(A78_SCRIPT, f"a78_a95_worker_{os.getpid()}")


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def small_rational_witness(lower: F, upper: F) -> F:
    """Choose a reproducible low-denominator rational strictly inside an interval."""
    if not lower < upper:
        raise ValueError((lower, upper))
    midpoint = (lower + upper) / 2
    denominators = (
        10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9,
        10**10, 10**12, 10**15, 10**18, 10**24,
    )
    for denominator in denominators:
        center = (midpoint.numerator * denominator) // midpoint.denominator
        for numerator in (center, center + 1, center - 1):
            candidate = F(numerator, denominator)
            if lower < candidate < upper:
                return candidate
    return midpoint


def phase_segments(cell: dict[str, Any]) -> list[dict[str, Any]]:
    lower = F(cell["exact_cell_inner_rational_bounds"][0])
    upper = F(cell["exact_cell_inner_rational_bounds"][1])
    phase = str(cell["phase_classification"])
    statement = cell["phase_statement"]
    if phase.startswith("unique_"):
        return [{
            "side": "full",
            "lower": lower,
            "upper": upper,
            "witness": small_rational_witness(lower, upper),
            "compressed_contact": int(statement["unique_global_maximum_contact"]),
        }]

    root = statement["root"]
    root_lower = F(root["root_lower"])
    root_upper = F(root["root_upper"])
    return [
        {
            "side": "left",
            "lower": lower,
            "upper": root_lower,
            "witness": small_rational_witness(lower, root_lower),
            "compressed_contact": int(statement["left_unique_global_maximum_contact"]),
        },
        {
            "side": "right",
            "lower": root_upper,
            "upper": upper,
            "witness": small_rational_witness(root_upper, upper),
            "compressed_contact": int(statement["right_unique_global_maximum_contact"]),
        },
    ]


def failure_record(result: dict[str, Any]) -> dict[str, Any] | None:
    failure = result.get("failure")
    if not failure:
        return None
    name, value = failure
    return {
        "name": name,
        "sign": 1 if value > 0 else -1 if value < 0 else 0,
    }


def candidate_record(
    family: str,
    contact: int,
    gamma_sign: int | None,
    result: dict[str, Any],
) -> dict[str, Any]:
    record = {
        "family": family,
        "contact": contact,
        "gamma_sign": gamma_sign,
        "status": result["status"],
        "first_failure": failure_record(result),
    }
    if result["status"] == "pass" and result.get("record"):
        pass_record = result["record"]
        record["strict_pass_certificate"] = {
            "condition_count": pass_record["condition_count"],
            "condition_class_counts": pass_record["condition_class_counts"],
            "all_conditions_strictly_positive": pass_record["all_conditions_strictly_positive"],
        }
    return record


def evaluate_cell(cell: dict[str, Any]) -> list[dict[str, Any]]:
    a78 = A78
    if a78 is None:
        raise RuntimeError("A78 worker not initialized")
    maximum = int(cell["maximum"])
    output: list[dict[str, Any]] = []
    for segment in phase_segments(cell):
        witness = segment["witness"]
        contact = int(segment["compressed_contact"])
        a78.S0 = a78.sp.Rational(witness.numerator, witness.denominator)

        candidates: list[dict[str, Any]] = []
        compressed = a78.evaluate_two_band(maximum, contact, collect_pass=True)
        candidates.append(candidate_record("two_band_compressed", contact, None, compressed))

        gamma_minus = a78.evaluate_three_band(maximum, contact - 1, -1, collect_pass=True)
        candidates.append(candidate_record("three_band_adjacent", contact - 1, -1, gamma_minus))

        gamma_plus = a78.evaluate_three_band(maximum, contact, 1, collect_pass=True)
        candidates.append(candidate_record("three_band_adjacent", contact, 1, gamma_plus))

        passes = [
            {
                "family": item["family"],
                "contact": item["contact"],
                "gamma_sign": item["gamma_sign"],
            }
            for item in candidates
            if item["status"] == "pass"
        ]
        output.append({
            "maximum": maximum,
            "parity": cell["parity"],
            "base_contact": int(cell["base_contact"]),
            "compressed_phase": cell["phase_classification"],
            "phase_side": segment["side"],
            "segment_open_bounds": [fstr(segment["lower"]), fstr(segment["upper"])],
            "witness": fstr(witness),
            "compressed_maximizer_contact": contact,
            "natural_lift_candidates": candidates,
            "strict_pass_count": len(passes),
            "strict_passes": passes,
        })
    return output


def exhaustive_restricted_family(record: dict[str, Any]) -> dict[str, Any]:
    a78 = A78
    if a78 is None:
        raise RuntimeError("A78 worker not initialized")
    maximum = int(record["maximum"])
    witness = F(record["witness"])
    a78.S0 = a78.sp.Rational(witness.numerator, witness.denominator)
    status_counts: Counter[str] = Counter()
    passes: list[dict[str, Any]] = []

    for contact in range(1, maximum):
        result = a78.evaluate_two_band(maximum, contact, collect_pass=False)
        status_counts[result["status"]] += 1
        if result["status"] == "pass":
            passes.append({"family": "two_band_compressed", "contact": contact, "gamma_sign": None})

        if contact <= maximum - 2:
            for gamma_sign in (-1, 1):
                result = a78.evaluate_three_band(maximum, contact, gamma_sign, collect_pass=False)
                status_counts[result["status"]] += 1
                if result["status"] == "pass":
                    passes.append({
                        "family": "three_band_adjacent",
                        "contact": contact,
                        "gamma_sign": gamma_sign,
                    })

    return {
        "maximum": maximum,
        "base_contact": record["base_contact"],
        "compressed_phase": record["compressed_phase"],
        "phase_side": record["phase_side"],
        "witness": record["witness"],
        "compressed_maximizer_contact": record["compressed_maximizer_contact"],
        "candidate_count": 3 * maximum - 5,
        "status_counts": dict(status_counts),
        "strict_pass_count": len(passes),
        "strict_passes": passes,
    }


def exact_first_obstruction_details(record: dict[str, Any]) -> dict[str, Any]:
    a78 = load_module(A78_SCRIPT, "a78_a95_first_obstruction")
    maximum = int(record["maximum"])
    witness = F(record["witness"])
    contact = int(record["compressed_maximizer_contact"])
    a78.S0 = a78.sp.Rational(witness.numerator, witness.denominator)
    evaluations = [
        ("two_band_compressed", contact, None, a78.evaluate_two_band(maximum, contact, collect_pass=False)),
        ("three_band_adjacent", contact - 1, -1, a78.evaluate_three_band(maximum, contact - 1, -1, collect_pass=False)),
        ("three_band_adjacent", contact, 1, a78.evaluate_three_band(maximum, contact, 1, collect_pass=False)),
    ]
    candidates = []
    for family, candidate_contact, gamma_sign, result in evaluations:
        failure = result.get("failure")
        candidates.append({
            "family": family,
            "contact": candidate_contact,
            "gamma_sign": gamma_sign,
            "status": result["status"],
            "first_failure": (
                {"name": failure[0], "exact_value": str(failure[1])}
                if failure else None
            ),
        })
    return {
        "maximum": maximum,
        "witness": fstr(witness),
        "compressed_maximizer_contact": contact,
        "candidates": candidates,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=min(16, max(1, os.cpu_count() or 1)))
    args = parser.parse_args()

    RESULTS.mkdir(parents=True, exist_ok=True)
    a94_result = json.loads(A94_RESULT.read_text(encoding="utf-8"))
    a94_catalogue = json.loads(A94_CATALOGUE.read_text(encoding="utf-8"))
    a90_result = json.loads(A90_RESULT.read_text(encoding="utf-8"))

    a94_source_valid = (
        a94_result.get("verdict")
        == "PASS_EXACT_CONTINUUM_ALL_858_CELL_ONE_VARIATION_AND_205_GLOBAL_ADJACENT_TRANSITIONS"
        and all(a94_result.get("gates", {}).values())
        and len(a94_catalogue.get("cells", [])) == EXPECTED_CELL_COUNT
    )
    first_offset_three = int(
        a90_result["contact_strip_result"]["first_offset_three_case"]["maximum"]
    )

    workers = min(args.workers, len(a94_catalogue["cells"]))
    with mp.Pool(processes=workers, initializer=worker_initializer) as pool:
        grouped = list(pool.imap_unordered(evaluate_cell, a94_catalogue["cells"], chunksize=1))
    records = [record for group in grouped for record in group]
    records.sort(key=lambda item: (item["maximum"], item["base_contact"], item["phase_side"]))

    obstructions = [record for record in records if record["strict_pass_count"] == 0]
    multiple = [record for record in records if record["strict_pass_count"] > 1]
    unique = [record for record in records if record["strict_pass_count"] == 1]

    pass_counts = Counter()
    for record in unique:
        selected = record["strict_passes"][0]
        if selected["family"] == "two_band_compressed":
            pass_counts["two_band_compressed"] += 1
        elif selected["gamma_sign"] == 1:
            pass_counts["three_band_gamma_plus"] += 1
        else:
            pass_counts["three_band_gamma_minus"] += 1

    obstruction_phase_counts = Counter(
        f"{record['compressed_phase']}::{record['phase_side']}"
        for record in obstructions
    )
    obstruction_supports = sorted({int(record["maximum"]) for record in obstructions})

    prefix_obstructions = [
        record for record in obstructions
        if int(record["maximum"]) <= first_offset_three
    ]
    with mp.Pool(processes=min(workers, len(prefix_obstructions)), initializer=worker_initializer) as pool:
        prefix_exhaustive = list(
            pool.imap_unordered(exhaustive_restricted_family, prefix_obstructions, chunksize=1)
        )
    prefix_exhaustive.sort(key=lambda item: (item["maximum"], item["base_contact"], item["phase_side"]))
    prefix_status_counts: Counter[str] = Counter()
    prefix_candidate_count = 0
    for item in prefix_exhaustive:
        prefix_candidate_count += int(item["candidate_count"])
        prefix_status_counts.update(item["status_counts"])

    first_obstruction = obstructions[0]
    first_obstruction_details = exact_first_obstruction_details(first_obstruction)
    first_exhaustive = next(
        item for item in prefix_exhaustive
        if item["maximum"] == first_obstruction["maximum"]
        and item["witness"] == first_obstruction["witness"]
    )

    candidate_status_counts: Counter[str] = Counter()
    candidate_failure_class_counts: Counter[str] = Counter()
    for record in records:
        for candidate in record["natural_lift_candidates"]:
            candidate_status_counts[candidate["status"]] += 1
            failure = candidate.get("first_failure")
            if failure:
                candidate_failure_class_counts[failure["name"].split("_")[0]] += 1

    gates = {
        "A94_source_certificate_present_and_passed": a94_source_valid,
        "A90_first_offset_three_support_is_M325": first_offset_three == EXPECTED_FIRST_OFFSET_THREE_M,
        "all_858_A94_cells_loaded": len(a94_catalogue["cells"]) == EXPECTED_CELL_COUNT,
        "exactly_1063_open_phase_segment_witnesses": len(records) == EXPECTED_SEGMENT_COUNT,
        "exactly_3189_natural_lift_candidate_evaluations": sum(len(r["natural_lift_candidates"]) for r in records) == EXPECTED_CANDIDATE_EVALUATION_COUNT,
        "exactly_980_segments_have_one_strict_natural_lift": len(unique) == EXPECTED_UNIQUE_LIFT_COUNT,
        "exactly_83_segments_have_no_strict_natural_lift": len(obstructions) == EXPECTED_OBSTRUCTION_COUNT,
        "no_segment_has_multiple_strict_natural_lifts": len(multiple) == 0,
        "natural_lift_pass_family_counts_match": dict(pass_counts) == EXPECTED_PASS_COUNTS,
        "obstruction_phase_counts_match": dict(obstruction_phase_counts) == EXPECTED_OBSTRUCTION_PHASE_COUNTS,
        "obstructions_span_exactly_75_supports": len(obstruction_supports) == EXPECTED_OBSTRUCTION_SUPPORT_COUNT,
        "first_obstruction_is_M125": obstruction_supports[0] == EXPECTED_FIRST_OBSTRUCTION_M,
        "last_obstruction_in_declared_domain_is_M520": obstruction_supports[-1] == 520,
        "no_obstruction_occurs_on_transition_left_sides": all(record["phase_side"] != "left" for record in obstructions),
        "no_obstruction_occurs_in_unique_b_plus_1_phase": all(record["compressed_phase"] != "unique_b_plus_1" for record in obstructions),
        "prefix_through_first_offset_three_contains_29_obstructions": len(prefix_obstructions) == EXPECTED_PREFIX_OBSTRUCTION_COUNT,
        "prefix_restricted_family_candidate_count_exact": prefix_candidate_count == EXPECTED_PREFIX_CANDIDATE_COUNT,
        "prefix_restricted_family_status_counts_match": dict(prefix_status_counts) == EXPECTED_PREFIX_STATUS_COUNTS,
        "no_prefix_obstruction_is_repaired_anywhere_in_declared_F2_F3_catalogue": all(item["strict_pass_count"] == 0 for item in prefix_exhaustive),
        "first_obstruction_exhaustive_catalogue_has_370_candidates": first_exhaustive["candidate_count"] == 370,
        "first_obstruction_exhaustive_catalogue_has_no_strict_pass": first_exhaustive["strict_pass_count"] == 0,
        "all_natural_lift_decisions_are_exact_KKT_statuses": set(candidate_status_counts).issubset({
            "pass", "primal_infeasible", "active_dual_infeasible",
            "reduced_cost_infeasible", "inactive_slack_infeasible",
            "zero_condition", "singular",
        }),
        "rational_witness_and_restricted_family_scope_recorded": True,
        "no_continuum_lift_or_physical_claim_promoted": True,
    }

    summary = {
        "audit": "A95_EXACT_RATIONAL_WITNESS_LIFT_AND_RESTRICTED_FAMILY_OBSTRUCTION",
        "evidence_class": "exact finite rational-witness KKT audit with an exhaustive restricted-family prefix certificate",
        "scope": {
            "source_cell_count": EXPECTED_CELL_COUNT,
            "maximum_range": [14, 520],
            "probe_interval": ["129/1000", "133/1000"],
            "phase_segment_witness_count": len(records),
            "claim": "pointwise natural-lift classification on every open A94 phase side, plus exhaustive F2/F3 obstruction certificates through M=325",
            "explicit_nonclaim": "not a full continuum lifted-KKT atlas, not a complete LP basis classification, and not a physical theorem",
        },
        "natural_lift_result": {
            "candidate_evaluation_count": sum(len(r["natural_lift_candidates"]) for r in records),
            "unique_strict_lift_count": len(unique),
            "no_strict_lift_count": len(obstructions),
            "multiple_strict_lift_count": len(multiple),
            "pass_family_counts": dict(pass_counts),
            "candidate_status_counts": dict(candidate_status_counts),
            "obstruction_phase_counts": dict(obstruction_phase_counts),
            "obstruction_support_count": len(obstruction_supports),
            "obstruction_supports": obstruction_supports,
        },
        "first_obstruction": {
            **first_obstruction_details,
            "full_restricted_catalogue": first_exhaustive,
        },
        "restricted_family_prefix_stress": {
            "definition": "all natural-lift obstruction witnesses through and including the first A90 offset-three support M=325",
            "obstruction_record_count": len(prefix_exhaustive),
            "candidate_count": prefix_candidate_count,
            "status_counts": dict(prefix_status_counts),
            "strict_pass_count": sum(item["strict_pass_count"] for item in prefix_exhaustive),
            "supports": [item["maximum"] for item in prefix_exhaustive],
        },
        "interpretation": {
            "positive_result": "980 open phase segments admit exactly one strict KKT lift inside the natural triad.",
            "negative_result": "83 open phase segments admit no strict KKT lift inside the natural triad.",
            "structural_obstruction": "At M=125, s=33/250, no candidate anywhere in the previously declared F2/F3 contact catalogue passes the complete strict KKT system.",
            "consequence": "Compressed-objective globality does not imply liftability to the frozen contact-support architecture; a broader active-set family or changed Q support is required before a continuum lifted theorem can be attempted.",
        },
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "gates": gates,
        "verdict": (
            "PASS_EXACT_RATIONAL_WITNESS_LIFT_ATLAS_AND_RESTRICTED_FAMILY_OBSTRUCTION"
            if all(gates.values()) else "FAIL"
        ),
    }

    catalogue = {
        "audit": "A95_EXACT_RATIONAL_WITNESS_LIFT_CATALOGUE",
        "contract": summary["scope"],
        "summary": {
            "record_count": len(records),
            "unique_strict_lift_count": len(unique),
            "obstruction_count": len(obstructions),
            "multiple_count": len(multiple),
            "prefix_exhaustive_record_count": len(prefix_exhaustive),
        },
        "records": records,
        "prefix_exhaustive_obstructions": prefix_exhaustive,
    }

    result_path = RESULTS / "a95_rational_witness_lift_results.json"
    catalogue_path = RESULTS / "a95_rational_witness_lift_catalogue.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    catalogue_path.write_text(json.dumps(catalogue, indent=2), encoding="utf-8")

    print(json.dumps({
        "audit": summary["audit"],
        "phase_segment_witness_count": len(records),
        "unique_strict_lift_count": len(unique),
        "obstruction_count": len(obstructions),
        "prefix_candidate_count": prefix_candidate_count,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": summary["verdict"],
        "result": result_path.name,
        "catalogue": catalogue_path.name,
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
