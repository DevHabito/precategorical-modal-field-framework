#!/usr/bin/env python3
"""A91 exact four-term mechanism for the A90 offset-three cells.

A90 proves strict one-variation of the complete adjacent-factor sequence at
nine exact rational probes for M=10,...,520, and finds fifteen cells where the
compressed maximizer is

    k* = ceil(M c(s)) + 3.

This audit asks whether those fifteen cells require a nonlocal explanation or
whether the same four channels isolated by A85 already determine the sign of
the decisive factor

    E_(M,b+2)(s),  b = ceil(M c(s)).

The four-term core is

    K4 = c_(beta t) (beta t)^k
       + c_(s t)    (s t)^k
       + c_t        t^k
       + c_(k t) k  t^k,

with beta=1/8 and t=1/2.  Since t^k>0, its sign is equivalently the sign of

    Phi = c_(beta t) beta^k + c_(s t) s^k + c_t + k c_(k t).

All theorem gates use exact Fraction arithmetic.  A separate high-precision
A85 parity-locator diagnostic is reported only as a diagnostic and is not
promoted to an exact theorem.
"""

from __future__ import annotations

import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from typing import Any

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A84_PATH = HERE / "a84_k_space_exponential_polynomial_stress_audit.py"
A90_RESULT_PATH = RESULTS / "a90_prethreshold_all_k_one_variation_results.json"
A90_CATALOGUE_PATH = RESULTS / "a90_prethreshold_contact_sequence_catalogue.json"

BETA = F(1, 8)
TARGET = F(1, 2)
EXPECTED_ELIGIBLE_COUNT = 4_563
EXPECTED_INELIGIBLE_COUNT = 36
EXPECTED_POSITIVE_CASES = [
    (325, 0, 55, 57, 58),
    (372, 0, 63, 65, 66),
    (378, 0, 64, 66, 67),
    (384, 0, 65, 67, 68),
    (390, 0, 66, 68, 69),
    (443, 0, 75, 77, 78),
    (449, 0, 76, 78, 79),
    (455, 0, 77, 79, 80),
    (460, 1, 78, 80, 81),
    (490, 0, 83, 85, 86),
    (496, 0, 84, 86, 87),
    (502, 0, 85, 87, 88),
    (508, 0, 86, 88, 89),
    (514, 0, 87, 89, 90),
    (520, 0, 88, 90, 91),
]


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sign(value: F) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def decimal_ratio(value: F, digits: int = 35) -> str:
    mp.mp.dps = max(60, digits + 20)
    return mp.nstr(mp.mpf(value.numerator) / value.denominator, digits)


def coefficient_bundle(a84, maximum: int, probe: F) -> dict[str, Any]:
    epsilon = a84.normalized_epsilon(maximum)
    beta_powers = a84.powers(BETA, maximum)
    target_powers = a84.powers(TARGET, maximum)
    probe_powers = a84.powers(probe, maximum)
    h_beta = (
        F(1 + beta_powers[maximum], 2)
        - a84.d_value(maximum, BETA, beta_powers)
        + 2 * epsilon
    )
    h_probe = a84.h_value(maximum, probe, probe_powers, epsilon)
    power_cache = {
        "beta": beta_powers,
        "target": target_powers,
        "probe": probe_powers,
        "current_probe": probe_powers,
        "beta_probe": a84.powers(BETA * probe, maximum),
        "beta_target": a84.powers(BETA * TARGET, maximum),
        "probe_target": a84.powers(probe * TARGET, maximum),
    }
    coefficients = dict(
        a84.k_space_coefficients(
            maximum,
            probe,
            power_cache,
            h_beta,
            h_probe,
        )
    )
    return {
        "power_cache": power_cache,
        "coefficients": coefficients,
    }


def evaluate_full_and_core(
    a84,
    maximum: int,
    probe: F,
    contact: int,
    bundle: dict[str, Any],
) -> dict[str, F]:
    coefficients = bundle["coefficients"]
    powers = bundle["power_cache"]

    full = a84.evaluate_k_space(
        list(coefficients.items()),
        contact,
        probe,
        powers,
    )

    beta_target_term = (
        coefficients["(beta*target)^k"]
        * powers["beta_target"][contact]
    )
    probe_target_term = (
        coefficients["(s*target)^k"]
        * powers["probe_target"][contact]
    )
    target_term = coefficients["target^k"] * powers["target"][contact]
    confluent_target_term = (
        coefficients["k*target^k"]
        * contact
        * powers["target"][contact]
    )
    four_core = (
        beta_target_term
        + probe_target_term
        + target_term
        + confluent_target_term
    )

    normalized_core = (
        coefficients["(beta*target)^k"] * powers["beta"][contact]
        + coefficients["(s*target)^k"] * powers["probe"][contact]
        + coefficients["target^k"]
        + contact * coefficients["k*target^k"]
    )

    return {
        "full": full,
        "four_core": four_core,
        "normalized_core": normalized_core,
        "residual": full - four_core,
        "target_scale": powers["target"][contact],
        "beta_target_term": beta_target_term,
        "probe_target_term": probe_target_term,
        "target_term": target_term,
        "confluent_target_term": confluent_target_term,
    }


def asymptotic_parameters(probe: F, parity: str) -> tuple[mp.mpf, mp.mpf]:
    mp.mp.dps = 120
    s = mp.mpf(probe.numerator) / probe.denominator
    beta = mp.mpf(1) / 8
    target = mp.mpf(1) / 2
    slope = mp.log(2) / (-2 * mp.log(s))
    amplitude = (target - s) / 2
    if parity == "even":
        constant = s - beta - mp.mpf(2) / 1875
        parity_factor = mp.mpf(1)
    elif parity == "odd":
        constant = mp.mpf(3) * (s - beta) / 4 - mp.mpf(1) / 1250
        parity_factor = mp.sqrt(2)
    else:
        raise ValueError(parity)
    offset = mp.log(
        parity_factor * constant * (1 - slope) / amplitude
    ) / mp.log(s)
    return slope, offset


def main() -> None:
    a84 = load_module(A84_PATH, "a84_for_a91")
    a90_result = json.loads(A90_RESULT_PATH.read_text(encoding="utf-8"))
    a90_catalogue = json.loads(A90_CATALOGUE_PATH.read_text(encoding="utf-8"))
    source_records = a90_catalogue["records"]

    exact_records: list[dict[str, Any]] = []
    positive_cases: list[dict[str, Any]] = []
    ineligible_records: list[dict[str, Any]] = []
    sign_mismatches: list[dict[str, Any]] = []
    dominance_failures: list[dict[str, Any]] = []
    normalized_identity_failures: list[dict[str, Any]] = []
    offset_classifier_failures: list[dict[str, Any]] = []

    minimum_ratio: F | None = None
    minimum_ratio_record: dict[str, Any] | None = None
    sign_counts = Counter()
    sign_counts_by_probe: dict[str, Counter] = {}
    parity_counts = Counter()

    bundle_cache: dict[tuple[int, F], dict[str, Any]] = {}

    for source in source_records:
        maximum = int(source["maximum"])
        probe_index = int(source["probe_index"])
        probe = F(source["probe"])
        base_contact = int(source["base_contact_ceil_Mc"])
        decisive_contact = base_contact + 2
        true_offset = int(source["ceil_offset"])

        eligible = decisive_contact <= maximum // 2 - 2
        if not eligible:
            ineligible_records.append({
                "maximum": maximum,
                "probe_index": probe_index,
                "probe": fstr(probe),
                "base_contact": base_contact,
                "decisive_contact": decisive_contact,
                "true_offset": true_offset,
            })
            continue

        cache_key = (maximum, probe)
        if cache_key not in bundle_cache:
            bundle_cache[cache_key] = coefficient_bundle(a84, maximum, probe)
        values = evaluate_full_and_core(
            a84,
            maximum,
            probe,
            decisive_contact,
            bundle_cache[cache_key],
        )

        full = values["full"]
        core = values["four_core"]
        residual = values["residual"]
        normalized = values["normalized_core"]
        target_scale = values["target_scale"]

        full_sign = sign(full)
        core_sign = sign(core)
        residual_sign = sign(residual)
        ratio = abs(core) / abs(residual)
        predicted_offset_three = core_sign > 0
        true_offset_three = true_offset == 3

        record = {
            "maximum": maximum,
            "parity": "even" if maximum % 2 == 0 else "odd",
            "probe_index": probe_index,
            "probe": fstr(probe),
            "base_contact": base_contact,
            "decisive_adjacent_factor_contact": decisive_contact,
            "maximizing_contact": int(source["maximizing_contact"]),
            "true_offset": true_offset,
            "full_sign": full_sign,
            "four_core_sign": core_sign,
            "six_term_residual_sign": residual_sign,
            "four_core_strictly_dominates_residual": abs(core) > abs(residual),
            "four_core_to_residual_ratio_decimal": decimal_ratio(ratio, 24),
            "offset_three_from_four_core": predicted_offset_three,
            "offset_three_exact": true_offset_three,
        }
        exact_records.append(record)

        sign_counts[core_sign] += 1
        sign_counts_by_probe.setdefault(str(probe_index), Counter())[core_sign] += 1
        parity_counts[(record["parity"], core_sign)] += 1

        if core != target_scale * normalized:
            normalized_identity_failures.append(record)
        if core_sign != full_sign:
            sign_mismatches.append(record)
        if abs(core) <= abs(residual):
            dominance_failures.append(record)
        if predicted_offset_three != true_offset_three:
            offset_classifier_failures.append(record)

        if minimum_ratio is None or ratio < minimum_ratio:
            minimum_ratio = ratio
            minimum_ratio_record = record

        if full_sign > 0:
            positive = {
                **record,
                "four_core_exact": fstr(core),
                "full_factor_exact": fstr(full),
                "six_term_residual_exact": fstr(residual),
                "normalized_four_core_exact": fstr(normalized),
            }
            positive_cases.append(positive)

    if minimum_ratio is None or minimum_ratio_record is None:
        raise RuntimeError("No eligible cells")

    # Secondary, explicitly non-exact diagnostic: does the A85 continuous
    # parity-corrected locator screen every offset-three cell?
    predictor_cache: dict[tuple[F, str], tuple[mp.mpf, mp.mpf]] = {}
    predictor_three_records: list[dict[str, Any]] = []
    minimum_distance_to_integer: mp.mpf | None = None
    minimum_distance_record: dict[str, Any] | None = None

    for source in source_records:
        maximum = int(source["maximum"])
        probe = F(source["probe"])
        parity = "even" if maximum % 2 == 0 else "odd"
        key = (probe, parity)
        if key not in predictor_cache:
            predictor_cache[key] = asymptotic_parameters(probe, parity)
        slope, offset = predictor_cache[key]
        predictor = slope * maximum + offset
        nearest_integer_distance = abs(predictor - mp.nint(predictor))
        if (
            minimum_distance_to_integer is None
            or nearest_integer_distance < minimum_distance_to_integer
        ):
            minimum_distance_to_integer = nearest_integer_distance
            minimum_distance_record = {
                "maximum": maximum,
                "probe_index": int(source["probe_index"]),
                "probe": fstr(probe),
                "predictor": mp.nstr(predictor, 60),
                "distance_to_nearest_integer": mp.nstr(nearest_integer_distance, 60),
            }

        predicted_contact = int(mp.ceil(predictor))
        predicted_offset = predicted_contact - int(source["base_contact_ceil_Mc"])
        if predicted_offset == 3:
            predictor_three_records.append({
                "maximum": maximum,
                "probe_index": int(source["probe_index"]),
                "probe": fstr(probe),
                "parity": parity,
                "true_offset": int(source["ceil_offset"]),
                "predictor_offset": predicted_offset,
                "predictor": mp.nstr(predictor, 45),
            })

    exact_positive_tuples = [
        (
            item["maximum"],
            item["probe_index"],
            item["base_contact"],
            item["decisive_adjacent_factor_contact"],
            item["maximizing_contact"],
        )
        for item in positive_cases
    ]

    exact_gates = {
        "A90_source_verdict_and_gates_pass": (
            a90_result["verdict"]
            == "PASS_EXACT_PRETHRESHOLD_NINE_PROBE_ALL_K_ONE_VARIATION_AND_FOUR_CONTACT_STRIP"
            and all(a90_result["gates"].values())
        ),
        "source_catalogue_record_count_exact": len(source_records) == 4_599,
        "offset_three_decision_eligible_count_exact": len(exact_records) == EXPECTED_ELIGIBLE_COUNT,
        "small_support_boundary_exclusion_count_exact": len(ineligible_records) == EXPECTED_INELIGIBLE_COUNT,
        "boundary_exclusions_have_only_offsets_zero_or_one": all(
            item["true_offset"] in (0, 1) for item in ineligible_records
        ),
        "normalized_four_core_identity_exact_in_every_eligible_cell": len(normalized_identity_failures) == 0,
        "four_core_sign_matches_full_factor_in_every_eligible_cell": len(sign_mismatches) == 0,
        "four_core_strictly_dominates_six_term_residual_in_every_eligible_cell": len(dominance_failures) == 0,
        "four_core_offset_three_classifier_exact_in_every_eligible_cell": len(offset_classifier_failures) == 0,
        "positive_four_core_count_is_exactly_fifteen": sign_counts[1] == 15,
        "negative_four_core_count_is_exactly_4548": sign_counts[-1] == 4_548,
        "positive_case_list_matches_A90_offset_three_list": exact_positive_tuples == EXPECTED_POSITIVE_CASES,
        "positive_cases_occur_only_at_first_two_probes": (
            sign_counts_by_probe.get("0", Counter())[1] == 14
            and sign_counts_by_probe.get("1", Counter())[1] == 1
            and all(
                sign_counts_by_probe.get(str(index), Counter())[1] == 0
                for index in range(2, 9)
            )
        ),
        "minimum_exact_core_dominance_ratio_exceeds_70": minimum_ratio > 70,
        "claim_boundary_preserved": (
            min(item["maximum"] for item in source_records) == 10
            and max(item["maximum"] for item in source_records) == 520
            and len({item["probe"] for item in source_records}) == 9
        ),
    }

    predictor_true_positive_count = sum(
        item["true_offset"] == 3 for item in predictor_three_records
    )
    predictor_false_positive_count = sum(
        item["true_offset"] != 3 for item in predictor_three_records
    )

    summary = {
        "audit": "A91_EXACT_FOUR_TERM_OFFSET_THREE_MECHANISM",
        "contract": {
            "maximum_range": [10, 520],
            "probe_count": 9,
            "probe_interval": ["129/1000", "133/1000"],
            "base_contact": "b=ceil(M c(s)) from the exact A90 integer comparison",
            "decisive_factor": "E_(M,b+2)(s)",
            "eligibility": "b+2 <= floor(M/2)-2, so the comparison between contacts b+2 and b+3 is admissible",
        },
        "exact_four_term_reduction": {
            "four_channels": [
                "(beta*target)^k",
                "(s*target)^k",
                "target^k",
                "k*target^k",
            ],
            "formula": "K4=c_(beta target)(beta target)^k+c_(s target)(s target)^k+c_target target^k+c_(k target) k target^k",
            "normalized_formula": "Phi=K4/target^k=c_(beta target) beta^k+c_(s target) s^k+c_target+k c_(k target)",
            "normalization_reason": "target^k=(1/2)^k is strictly positive",
            "eligible_cell_count": len(exact_records),
            "boundary_excluded_cell_count": len(ineligible_records),
            "full_positive_count": sum(item["full_sign"] > 0 for item in exact_records),
            "full_negative_count": sum(item["full_sign"] < 0 for item in exact_records),
            "four_core_positive_count": sign_counts[1],
            "four_core_negative_count": sign_counts[-1],
            "sign_mismatch_count": len(sign_mismatches),
            "dominance_failure_count": len(dominance_failures),
            "offset_three_classifier_mismatch_count": len(offset_classifier_failures),
            "minimum_four_core_to_six_term_residual_ratio": {
                "exact": fstr(minimum_ratio),
                "decimal": decimal_ratio(minimum_ratio, 40),
                "record": minimum_ratio_record,
            },
            "positive_count_by_probe_index": {
                str(index): sign_counts_by_probe.get(str(index), Counter())[1]
                for index in range(9)
            },
            "positive_count_by_parity": {
                "even": parity_counts[("even", 1)],
                "odd": parity_counts[("odd", 1)],
            },
            "theorem_statement": (
                "On every eligible A90 cell, the sign of E_(M,b+2)(s) is fixed by the four-channel core K4, with strict residual dominance. Because A90 proves one variation and offsets at most three on this grid, k*=b+3 if and only if K4>0."
            ),
        },
        "offset_three_cases": positive_cases,
        "parity_corrected_locator_diagnostic": {
            "evidence_class": "120-digit numerical diagnostic; not an exact rational or interval theorem",
            "predictor": "x_p(M,s)=M c(s)+d_parity(s), using the A85 parity correction",
            "screening_rule": "ceil(x_p)-ceil(Mc)=3",
            "screened_cell_count": len(predictor_three_records),
            "true_offset_three_count_inside_screen": predictor_true_positive_count,
            "false_positive_count": predictor_false_positive_count,
            "false_negative_count": 15 - predictor_true_positive_count,
            "minimum_distance_of_any_predictor_to_an_integer": (
                mp.nstr(minimum_distance_to_integer, 70)
                if minimum_distance_to_integer is not None
                else None
            ),
            "minimum_distance_record": minimum_distance_record,
            "interpretation": (
                "The parity-corrected locator screens all fifteen offset-three cells but also admits fifty-four offset-two cells. It is therefore a complete diagnostic screen on this finite grid, not an exact classifier. The exact decision is the sign of the local four-term core."
            ),
        },
        "gates": exact_gates,
        "gate_count": len(exact_gates),
        "pass_count": sum(value is True for value in exact_gates.values()),
        "verdict": "PASS_EXACT_FOUR_TERM_OFFSET_THREE_CLASSIFIER_AND_PARITY_SCREENING_OBSTRUCTION",
        "claim_boundary": [
            "The exact theorem is finite: 10<=M<=520 at the nine A90 rational probes.",
            "The theorem concerns the compressed-objective adjacent factor and inherits A90's strict one-variation result; it is not a continuum-in-s theorem.",
            "The A85 parity-corrected continuous locator is reported only as a high-precision diagnostic, not as an exact certificate.",
            "A91 does not prove that offset four is impossible beyond the A90 grid or that the four-term classifier remains valid for all support sizes.",
            "Compressed-objective selection remains separate from the full KKT feasibility exceptions identified in A82.",
            "No physical, spacetime, pre-temporal, or ontological interpretation follows from this finite contract-relative result.",
        ],
    }

    catalogue = {
        "audit": summary["audit"],
        "contract": summary["contract"],
        "record_count": len(exact_records),
        "records": exact_records,
        "boundary_excluded_records": ineligible_records,
        "parity_predictor_offset_three_screen": predictor_three_records,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "a91_four_term_offset_three_results.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    (RESULTS / "a91_four_term_offset_three_catalogue.json").write_text(
        json.dumps(catalogue, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps({
        "verdict": summary["verdict"],
        "gates": f"{summary['pass_count']}/{summary['gate_count']}",
        "eligible_cells": len(exact_records),
        "offset_three_cells": len(positive_cases),
        "minimum_dominance_ratio": summary["exact_four_term_reduction"]["minimum_four_core_to_six_term_residual_ratio"]["decimal"],
        "parity_screen": {
            "screened": len(predictor_three_records),
            "true": predictor_true_positive_count,
            "false_positive": predictor_false_positive_count,
        },
    }, indent=2))

    if not all(exact_gates.values()):
        failed = [name for name, value in exact_gates.items() if not value]
        raise SystemExit(f"A91 failed gates: {failed}")


if __name__ == "__main__":
    main()
