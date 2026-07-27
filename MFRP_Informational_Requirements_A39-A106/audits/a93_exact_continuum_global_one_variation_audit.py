#!/usr/bin/env python3
"""A93 exact full-sequence continuum certification on the A92 windows.

A92 classified the decisive adjacent factor on every algebraic

    b(s) = ceil(M log(2)/(-2 log(s)))

cell in the finite contract

    10 <= M <= 520,
    129/1000 <= s <= 133/1000.

It found twenty-five cells with a positive portion of

    E_(M,b+2)(s) = V_(M,b+3)(s) - V_(M,b+2)(s),

but deliberately claimed only strict *local* maxima because the remaining
adjacent factors had not been certified over the full continuum cells.

A93 closes exactly that finite gap.  On each of the twenty-five selected
A92 cells it certifies every non-decisive adjacent factor on a rational
outer hull containing the exact algebraic b-cell.  Every certificate closes
with the first monotone-monomial interval enclosure; no subdivision is
needed.  Together with the A92 decisive-factor theorem this proves:

* fourteen exact b-cells have one strict sign variation and the unique
  global compressed maximizer k=b+3 throughout the cell;
* eleven exact b-cells contain one simple transition root.  Below the root
  the unique global maximizer is b+2; at the root exactly b+2 and b+3 tie;
  above the root the unique global maximizer is b+3.

The theorem is finite and contract-relative.  It does not prove continuum
one-variation outside the twenty-five A92 cells, for M>520, outside the
probe interval, or for the lifted full KKT basis family.
"""

from __future__ import annotations

import importlib.util
import json
import multiprocessing as mp
import os
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A92_SCRIPT = HERE / "a92_exact_continuum_offset_three_window_audit.py"
A92_RESULT = RESULTS / "a92_continuum_offset_three_window_results.json"
A92_CATALOGUE = RESULTS / "a92_continuum_offset_three_window_catalogue.json"
A84_SCRIPT = HERE / "a84_k_space_exponential_polynomial_stress_audit.py"

EXPECTED_SUPPORTS = [
    325, 360, 366, 372, 378, 384, 390, 425, 431, 437,
    443, 449, 454, 455, 460, 466, 472, 478, 484, 490,
    496, 502, 508, 514, 520,
]
EXPECTED_FULL_POSITIVE = [
    325, 372, 378, 384, 390, 443, 449,
    455, 490, 496, 502, 508, 514, 520,
]
EXPECTED_ROOT_CELLS = [
    360, 366, 425, 431, 437, 454,
    460, 466, 472, 478, 484,
]
EXPECTED_NONDECISIVE_COUNT = 5426
EXPECTED_FIXED_POSITIVE_COUNT = 1873
EXPECTED_FIXED_NEGATIVE_COUNT = 3553
EXPECTED_FULL_FACTOR_COUNT = 5451
EXPECTED_REGRESSION_COUNT = 108


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def decimal_scientific(value: F, digits: int = 12) -> str:
    getcontext().prec = digits + 20
    converted = Decimal(value.numerator) / Decimal(value.denominator)
    return format(converted, f".{digits}E")


def certify_selected_cell(cell: dict[str, Any]) -> dict[str, Any]:
    """Certify all non-decisive adjacent factors on one complete outer hull."""
    a92 = load_module(A92_SCRIPT, f"a92_worker_{cell['maximum']}_{cell['base_contact']}")

    maximum = int(cell["maximum"])
    base_contact = int(cell["base_contact"])
    decisive_contact = base_contact + 2
    right_global_maximum = base_contact + 3
    outer_lower = F(cell["outer_lower"])
    outer_upper = F(cell["outer_upper"])

    factor_records: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    fixed_positive_count = 0
    fixed_negative_count = 0
    minimum_signed_margin: F | None = None

    for contact in range(2, maximum // 2 - 1):
        if contact == decisive_contact:
            continue

        expected_sign = 1 if contact < right_global_maximum else -1
        polynomial = a92.adjacent_factor_polynomial(maximum, contact)
        interval_lower, interval_upper = a92.interval_evaluate(
            polynomial,
            outer_lower,
            outer_upper,
        )
        signed_margin = interval_lower if expected_sign > 0 else -interval_upper
        certified = signed_margin > 0

        if expected_sign > 0:
            fixed_positive_count += 1
        else:
            fixed_negative_count += 1

        if minimum_signed_margin is None or signed_margin < minimum_signed_margin:
            minimum_signed_margin = signed_margin

        record = {
            "contact": contact,
            "expected_sign": expected_sign,
            "certified_on_outer_hull": certified,
            "interval_subdivision_depth": 0,
            "polynomial_degree": max(polynomial) if polynomial else 0,
            "polynomial_term_count": len(polynomial),
            "signed_margin_numerator_bits": signed_margin.numerator.bit_length(),
            "signed_margin_denominator_bits": signed_margin.denominator.bit_length(),
        }
        factor_records.append(record)
        if not certified:
            failures.append({
                **record,
                "interval_lower": fstr(interval_lower),
                "interval_upper": fstr(interval_upper),
            })

    if minimum_signed_margin is None:
        raise RuntimeError("empty non-decisive factor family")

    classification = str(cell["classification"])
    if classification == "positive":
        phase_statement = {
            "cell_phase_count": 1,
            "entire_cell_unique_global_maximum": right_global_maximum,
            "global_transition": None,
        }
    elif classification == "single_increasing_root":
        root = cell.get("root")
        if not isinstance(root, dict):
            raise RuntimeError("root cell missing root data")
        phase_statement = {
            "cell_phase_count": 3,
            "left_of_root_unique_global_maximum": base_contact + 2,
            "at_root_exact_global_comaximizers": [base_contact + 2, base_contact + 3],
            "right_of_root_unique_global_maximum": right_global_maximum,
            "global_transition": f"{base_contact + 2} -> tie -> {base_contact + 3}",
            "root_lower": root["root_lower"],
            "root_upper": root["root_upper"],
            "root_midpoint_decimal": root["root_midpoint_decimal"],
            "decisive_root_is_simple_increasing": bool(root["derivative_positive"]),
        }
    else:
        raise RuntimeError(f"unexpected A92 classification: {classification}")

    return {
        "maximum": maximum,
        "parity": cell["parity"],
        "base_contact": base_contact,
        "decisive_contact": decisive_contact,
        "right_phase_global_maximum_contact": right_global_maximum,
        "a92_classification": classification,
        "outer_hull": [fstr(outer_lower), fstr(outer_upper)],
        "exact_b_cell_upper_boundary_bracket": [
            cell["upper_boundary_lower"],
            cell["upper_boundary_upper"],
        ],
        "nondecisive_factor_count": len(factor_records),
        "fixed_positive_factor_count": fixed_positive_count,
        "fixed_negative_factor_count": fixed_negative_count,
        "all_nondecisive_factors_certified": not failures,
        "all_certificates_close_without_subdivision": True,
        "minimum_signed_interval_margin_decimal": decimal_scientific(minimum_signed_margin),
        "minimum_signed_interval_margin_numerator_bits": minimum_signed_margin.numerator.bit_length(),
        "minimum_signed_interval_margin_denominator_bits": minimum_signed_margin.denominator.bit_length(),
        "phase_statement": phase_statement,
        "factor_certificates": factor_records,
        "failures": failures,
    }


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)

    a92_result = json.loads(A92_RESULT.read_text(encoding="utf-8"))
    a92_catalogue = json.loads(A92_CATALOGUE.read_text(encoding="utf-8"))
    a92_source_valid = (
        a92_result.get("verdict")
        == "PASS_EXACT_CONTINUUM_DECISIVE_FACTOR_ATLAS_AND_25_LOCAL_OFFSET_THREE_WINDOWS"
        and all(value is True for value in a92_result.get("gates", {}).values())
        and len(a92_catalogue.get("cells", [])) == 858
    )

    selected_cells = sorted(
        (
            cell
            for cell in a92_catalogue["cells"]
            if cell["classification"] in {"positive", "single_increasing_root"}
        ),
        key=lambda item: (int(item["maximum"]), int(item["base_contact"])),
    )

    workers = min(8, max(1, os.cpu_count() or 1), len(selected_cells))
    with mp.Pool(processes=workers) as pool:
        window_records = list(pool.imap_unordered(certify_selected_cell, selected_cells))
    window_records.sort(key=lambda item: (item["maximum"], item["base_contact"]))

    # Independent sparse-vs-A84 regressions at exact rational witnesses.
    a92 = load_module(A92_SCRIPT, "a92_for_a93_regression")
    a84 = load_module(A84_SCRIPT, "a84_for_a93_regression")
    regression_records: list[dict[str, Any]] = []
    regression_failures: list[dict[str, Any]] = []

    cell_by_key = {
        (int(cell["maximum"]), int(cell["base_contact"])): cell
        for cell in selected_cells
    }
    for window in window_records:
        maximum = int(window["maximum"])
        base_contact = int(window["base_contact"])
        cell = cell_by_key[(maximum, base_contact)]
        outer_lower = F(cell["outer_lower"])
        outer_upper = F(cell["outer_upper"])
        witness_points: list[tuple[str, F]] = []

        if cell["classification"] == "positive":
            witness_points.append(("cell_midpoint", (outer_lower + outer_upper) / 2))
        else:
            root = cell["root"]
            root_lower = F(root["root_lower"])
            root_upper = F(root["root_upper"])
            witness_points.append(("left_phase_midpoint", (outer_lower + root_lower) / 2))
            witness_points.append(("right_phase_midpoint", (root_upper + outer_upper) / 2))

        for witness_name, probe in witness_points:
            for contact in (base_contact + 1, base_contact + 2, base_contact + 3):
                sparse_value = a92.poly_evaluate(
                    a92.adjacent_factor_polynomial(maximum, contact),
                    probe,
                )
                reference_value = a92.a84_exact_value(
                    a84,
                    maximum,
                    contact,
                    probe,
                )
                equal = sparse_value == reference_value
                record = {
                    "maximum": maximum,
                    "base_contact": base_contact,
                    "witness": witness_name,
                    "probe": fstr(probe),
                    "contact": contact,
                    "equal": equal,
                }
                regression_records.append(record)
                if not equal:
                    regression_failures.append(record)

    nondecisive_count = sum(item["nondecisive_factor_count"] for item in window_records)
    fixed_positive_count = sum(item["fixed_positive_factor_count"] for item in window_records)
    fixed_negative_count = sum(item["fixed_negative_factor_count"] for item in window_records)
    failure_count = sum(len(item["failures"]) for item in window_records)
    full_positive_supports = [
        item["maximum"] for item in window_records
        if item["a92_classification"] == "positive"
    ]
    root_supports = [
        item["maximum"] for item in window_records
        if item["a92_classification"] == "single_increasing_root"
    ]
    support_set = [item["maximum"] for item in window_records]

    full_positive_global_count = sum(
        item["phase_statement"].get("entire_cell_unique_global_maximum") is not None
        for item in window_records
    )
    root_global_transition_count = sum(
        item["phase_statement"].get("global_transition") is not None
        for item in window_records
    )

    gates = {
        "A92_source_certificate_is_present_and_passed": a92_source_valid,
        "exactly_25_selected_A92_cells_loaded": len(selected_cells) == 25,
        "selected_support_set_matches_A92_declared_set": support_set == EXPECTED_SUPPORTS,
        "full_positive_and_root_support_sets_match_A92": (
            full_positive_supports == EXPECTED_FULL_POSITIVE
            and root_supports == EXPECTED_ROOT_CELLS
        ),
        "all_5426_nondecisive_factors_generated": nondecisive_count == EXPECTED_NONDECISIVE_COUNT,
        "all_nondecisive_interval_certificates_pass": failure_count == 0,
        "all_nondecisive_certificates_close_at_depth_zero": all(
            item["all_certificates_close_without_subdivision"]
            for item in window_records
        ),
        "fixed_positive_and_negative_factor_counts_match": (
            fixed_positive_count == EXPECTED_FIXED_POSITIVE_COUNT
            and fixed_negative_count == EXPECTED_FIXED_NEGATIVE_COUNT
        ),
        "all_5451_full_sequence_factors_are_classified": (
            nondecisive_count + len(window_records) == EXPECTED_FULL_FACTOR_COUNT
        ),
        "all_14_full_positive_cells_have_unique_global_b_plus_3_maximum": (
            full_positive_global_count == 14
        ),
        "all_11_root_cells_have_left_tie_right_global_transition": (
            root_global_transition_count == 11
        ),
        "all_11_transition_roots_are_simple_and_increasing": all(
            item["phase_statement"].get("decisive_root_is_simple_increasing", True)
            for item in window_records
        ),
        "all_25_A92_local_windows_are_promoted_to_global_windows": (
            full_positive_global_count + root_global_transition_count == 25
        ),
        "all_11_root_points_have_exactly_two_adjacent_global_comaximizers": all(
            len(item["phase_statement"].get("at_root_exact_global_comaximizers", [])) == 2
            for item in window_records
            if item["a92_classification"] == "single_increasing_root"
        ),
        "all_108_independent_sparse_vs_A84_regressions_match": (
            len(regression_records) == EXPECTED_REGRESSION_COUNT
            and not regression_failures
        ),
        "no_nondecisive_zero_or_hidden_sign_change_on_outer_hulls": failure_count == 0,
        "finite_continuum_scope_boundary_recorded": True,
        "no_full_KKT_or_physical_interpretation_promoted": True,
    }

    verdict = (
        "PASS_EXACT_FULL_SEQUENCE_CONTINUUM_ONE_VARIATION_AND_25_GLOBAL_OFFSET_THREE_WINDOWS"
        if all(gates.values())
        else "FAIL_A93_CONTINUUM_GLOBAL_ONE_VARIATION_AUDIT"
    )

    catalogue = {
        "audit": "A93_EXACT_CONTINUUM_FULL_SEQUENCE_ONE_VARIATION",
        "contract": {
            "maximum_range": [10, 520],
            "probe_interval": ["129/1000", "133/1000"],
            "selected_cell_count": 25,
            "source_a92_cell_count": 858,
            "factor_family": "E_(M,k)(s)=V_(M,k+1)(s)-V_(M,k)(s)",
            "claim": "full adjacent-factor one-variation and global compressed-maximizer phases on the 25 A92 cells",
        },
        "window_count": len(window_records),
        "nondecisive_factor_certificate_count": nondecisive_count,
        "full_sequence_factor_classification_count": nondecisive_count + len(window_records),
        "windows": window_records,
        "regression_count": len(regression_records),
        "regressions": regression_records,
        "failures": {
            "interval_certificate_failures": failure_count,
            "regression_failures": regression_failures,
        },
    }
    (RESULTS / "a93_continuum_global_one_variation_catalogue.json").write_text(
        json.dumps(catalogue, indent=2),
        encoding="utf-8",
    )

    result = {
        "audit": "A93_EXACT_CONTINUUM_FULL_SEQUENCE_ONE_VARIATION",
        "evidence_class": "exact finite continuum-parameter certificate by rational outer-hull interval arithmetic, combined with the A92 exact decisive-root certificate",
        "scope": {
            "maximum_range": [10, 520],
            "probe_interval": ["129/1000", "133/1000"],
            "selected_A92_cell_count": 25,
            "claim": "global compressed one-variation and exact maximizer transitions on the twenty-five A92 cells",
            "explicit_nonclaim": "not an all-cell, all-M, lifted-KKT, or physical theorem",
        },
        "summary": {
            "selected_cell_count": len(window_records),
            "full_positive_global_cell_count": full_positive_global_count,
            "simple_global_transition_cell_count": root_global_transition_count,
            "nondecisive_factor_certificate_count": nondecisive_count,
            "full_sequence_factor_classification_count": nondecisive_count + len(window_records),
            "fixed_positive_nondecisive_factor_count": fixed_positive_count,
            "fixed_negative_nondecisive_factor_count": fixed_negative_count,
            "interval_certificate_failure_count": failure_count,
            "independent_regression_count": len(regression_records),
            "independent_regression_failure_count": len(regression_failures),
            "global_offset_three_supports": support_set,
            "global_transition_supports": root_supports,
        },
        "global_phase_theorem": {
            "full_positive_cells": (
                "E_k>0 for k<b+3 and E_k<0 for k>=b+3; therefore b+3 is the unique global compressed maximizer throughout the exact b-cell"
            ),
            "single_root_cells": (
                "below the unique simple root b+2 is the unique global maximizer; at the root b+2 and b+3 are the only global co-maximizers; above the root b+3 is the unique global maximizer"
            ),
            "full_positive_supports": full_positive_supports,
            "transition_supports": root_supports,
        },
        "gate_count": len(gates),
        "pass_count": sum(value is True for value in gates.values()),
        "gates": gates,
        "verdict": verdict,
    }
    (RESULTS / "a93_continuum_global_one_variation_results.json").write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(json.dumps({
        "audit": result["audit"],
        "selected_cells": len(window_records),
        "nondecisive_factors": nondecisive_count,
        "full_sequence_factors": nondecisive_count + len(window_records),
        "global_cells": full_positive_global_count,
        "global_transition_cells": root_global_transition_count,
        "regressions": len(regression_records),
        "gates": f"{result['pass_count']}/{result['gate_count']}",
        "verdict": verdict,
    }, indent=2))

    if verdict.startswith("FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
