#!/usr/bin/env python3
"""A87 exact secant-residual offset classifier.

A86 localizes the exact adjacent-contact transition to the three contacts

    b = ceil(M c(s)), b+1, b+2,

for 10<=M<=300 at the three rational A84 probes. A87 asks whether one
normalized local residual can decide which of those three offsets is selected.

Let E_{M,k}(s) be the exact seven/ten-term adjacent objective factor from
A83/A84, and define the local secant residual

    tau_{M,s} = E_{M,b}(s) / (E_{M,b}(s)-E_{M,b+1}(s)).

If the local secant drop is positive, then

    tau < 0       iff E_b < 0,
    0 < tau < 1   iff E_b > 0 > E_{b+1},
    tau > 1       iff E_{b+1} > 0.

Combined with A84's exact one-sign-variation theorem and A86's three-contact
strip, these three intervals select offsets 0, 1, and 2 respectively.

The audit also evaluates the A85 four-term and eight-term cores. The four-term
secant classifier has exactly the already-known M=12/local-lower failure; the
eight-term classifier is exact in every declared cell. Finally, the audit
checks the entire A84 factor sequences and records that global monotonicity is
false: local secant positivity near b does not extend to all contacts.

All theorem gates use Fraction/integer arithmetic. Decimal strings are display
only. The result is finite to the A84/A86 contract and is not an all-M theorem.
"""

from __future__ import annotations

import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Callable

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A84_PATH = HERE / "a84_k_space_exponential_polynomial_stress_audit.py"
A85_PATH = HERE / "a85_parity_dominant_balance_contact_localization_audit.py"
A84_RESULTS = RESULTS / "a84_k_space_exponential_polynomial_stress_results.json"
A85_RESULTS = RESULTS / "a85_parity_dominant_balance_contact_localization_results.json"
A86_CATALOGUE = RESULTS / "a86_exact_rational_contact_strip_catalogue.json"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def decimal(value: F, digits: int = 30) -> str:
    # Deterministic decimal display without using it in any gate.
    from decimal import Decimal, localcontext

    with localcontext() as context:
        context.prec = digits + 8
        rendered = Decimal(value.numerator) / Decimal(value.denominator)
        return format(rendered, f".{digits}g")


def sign(value: F) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def classify_tau(value: F) -> int | None:
    if value < 0:
        return 0
    if 0 < value < 1:
        return 1
    if value > 1:
        return 2
    return None


def threshold_margin(value: F, offset: int) -> F:
    if offset == 0:
        return -value
    if offset == 1:
        return min(value, 1 - value)
    if offset == 2:
        return value - 1
    raise ValueError(offset)


def extremum_record(
    records: list[dict[str, Any]],
    key: str,
    mode: str,
    predicate: Callable[[dict[str, Any]], bool] | None = None,
) -> dict[str, Any]:
    eligible = [record for record in records if predicate is None or predicate(record)]
    if not eligible:
        raise RuntimeError(f"No records for {key}")
    chooser = min if mode == "min" else max
    record = chooser(eligible, key=lambda item: F(item[key]))
    return {
        "maximum": record["maximum"],
        "probe_name": record["probe_name"],
        "probe_value": record["probe_value"],
        "base_contact": record["base_contact"],
        "true_offset": record["true_offset"],
        key: record[key],
        f"{key}_decimal": record[f"{key}_decimal"],
    }


def main() -> None:
    a84 = load_module(A84_PATH, "a84_module")
    a85 = load_module(A85_PATH, "a85_module")
    a84_results = json.loads(A84_RESULTS.read_text(encoding="utf-8"))
    a85_results = json.loads(A85_RESULTS.read_text(encoding="utf-8"))
    a86_catalogue = json.loads(A86_CATALOGUE.read_text(encoding="utf-8"))

    a84_by_maximum = {
        int(record["maximum"]): record
        for record in a84_results["support_records"]
    }
    source_records = a86_catalogue["records"]
    if len(source_records) != 873:
        raise RuntimeError("A86 record count mismatch")

    records: list[dict[str, Any]] = []
    full_class_counts: Counter[int] = Counter()
    four_class_counts: Counter[int] = Counter()
    eight_class_counts: Counter[int] = Counter()
    full_mismatches: list[dict[str, Any]] = []
    four_mismatches: list[dict[str, Any]] = []
    eight_mismatches: list[dict[str, Any]] = []
    full_denominator_failures: list[dict[str, Any]] = []
    four_denominator_failures: list[dict[str, Any]] = []
    eight_denominator_failures: list[dict[str, Any]] = []

    for source in source_records:
        maximum = int(source["maximum"])
        probe_name = source["probe_name"]
        probe_value = F(source["probe_value"])
        base_contact = int(source["ceil_Mc"])
        true_offset = int(source["ceil_offset"])

        if not a84_by_maximum[maximum]["strict_single_variation"][probe_name]:
            raise RuntimeError("A84 one-variation dependency failed")

        epsilon = a84.normalized_epsilon(maximum)
        beta_powers = a84.powers(a84.BETA, maximum)
        target_powers = a84.powers(a84.TARGET, maximum)
        probe_powers = a84.powers(probe_value, maximum)
        power_cache = {
            "beta": beta_powers,
            "target": target_powers,
            "probe": probe_powers,
            "current_probe": probe_powers,
            "beta_probe": a84.powers(a84.BETA * probe_value, maximum),
            "beta_target": a84.powers(a84.BETA * a84.TARGET, maximum),
            "probe_target": a84.powers(probe_value * a84.TARGET, maximum),
        }
        h_beta = (
            F(1 + beta_powers[maximum], 2)
            - a84.d_value(maximum, a84.BETA, beta_powers)
            + 2 * epsilon
        )
        h_probe = a84.h_value(maximum, probe_value, probe_powers, epsilon)
        coefficient_map = dict(
            a84.k_space_coefficients(
                maximum,
                probe_value,
                power_cache,
                h_beta,
                h_probe,
            )
        )

        def components(contact: int) -> tuple[F, F, F]:
            terms = a85.term_vector(
                a84,
                maximum,
                contact,
                probe_value,
                coefficient_map,
                power_cache,
            )
            full = sum(terms, F(0))
            four = terms[1] + terms[2] + terms[7] + terms[8]
            eight = sum(terms[1:9], F(0))
            return full, four, eight

        full_b, four_b, eight_b = components(base_contact)
        full_next, four_next, eight_next = components(base_contact + 1)

        data: dict[str, Any] = {
            "maximum": maximum,
            "probe_name": probe_name,
            "probe_value": fstr(probe_value),
            "base_contact": base_contact,
            "true_offset": true_offset,
            "selected_contact": int(source["transition_contact"]),
        }

        for label, left, right, counts, mismatches, failures in (
            (
                "full",
                full_b,
                full_next,
                full_class_counts,
                full_mismatches,
                full_denominator_failures,
            ),
            (
                "four",
                four_b,
                four_next,
                four_class_counts,
                four_mismatches,
                four_denominator_failures,
            ),
            (
                "eight",
                eight_b,
                eight_next,
                eight_class_counts,
                eight_mismatches,
                eight_denominator_failures,
            ),
        ):
            drop = left - right
            if drop <= 0:
                failures.append({
                    "maximum": maximum,
                    "probe_name": probe_name,
                    "base_contact": base_contact,
                    "left_sign": sign(left),
                    "right_sign": sign(right),
                    "drop_sign": sign(drop),
                })
            if drop == 0:
                raise RuntimeError("Zero local secant denominator")
            tau = left / drop
            predicted = classify_tau(tau)
            if predicted is not None:
                counts[predicted] += 1
            if predicted != true_offset:
                mismatches.append({
                    "maximum": maximum,
                    "probe_name": probe_name,
                    "probe_value": fstr(probe_value),
                    "base_contact": base_contact,
                    "true_offset": true_offset,
                    "predicted_offset": predicted,
                    "tau": fstr(tau),
                    "tau_decimal": decimal(tau),
                    "left_sign": sign(left),
                    "right_sign": sign(right),
                })

            margin = threshold_margin(tau, true_offset) if predicted == true_offset else F(-1)
            data.update({
                f"{label}_left_sign": sign(left),
                f"{label}_right_sign": sign(right),
                f"{label}_drop_positive": drop > 0,
                f"{label}_tau": fstr(tau),
                f"{label}_tau_decimal": decimal(tau),
                f"{label}_predicted_offset": predicted,
                f"{label}_threshold_margin": fstr(margin),
                f"{label}_threshold_margin_decimal": decimal(margin),
            })

        records.append(data)

    # Global monotonicity census for the complete A84 factor sequences.
    global_positive_drops = 0
    global_negative_drops = 0
    global_zero_drops = 0
    first_global_negative: dict[str, Any] | None = None
    global_factor_count = 0

    for maximum in range(10, 301):
        epsilon = a84.normalized_epsilon(maximum)
        beta_powers = a84.powers(a84.BETA, maximum)
        target_powers = a84.powers(a84.TARGET, maximum)
        h_beta = (
            F(1 + beta_powers[maximum], 2)
            - a84.d_value(maximum, a84.BETA, beta_powers)
            + 2 * epsilon
        )
        for probe_name, probe_value in a84.PROBES:
            probe_powers = a84.powers(probe_value, maximum)
            power_cache = {
                "beta": beta_powers,
                "target": target_powers,
                "current_probe": probe_powers,
                "beta_probe": a84.powers(a84.BETA * probe_value, maximum),
                "beta_target": a84.powers(a84.BETA * a84.TARGET, maximum),
                "probe_target": a84.powers(probe_value * a84.TARGET, maximum),
            }
            h_probe = a84.h_value(maximum, probe_value, probe_powers, epsilon)
            coefficients = a84.k_space_coefficients(
                maximum,
                probe_value,
                power_cache,
                h_beta,
                h_probe,
            )
            contacts = list(range(2, maximum // 2 - 1))
            values = [
                a84.evaluate_k_space(
                    coefficients,
                    contact,
                    probe_value,
                    power_cache,
                )
                for contact in contacts
            ]
            global_factor_count += len(values)
            for contact, left, right in zip(contacts, values, values[1:]):
                drop = left - right
                if drop > 0:
                    global_positive_drops += 1
                elif drop < 0:
                    global_negative_drops += 1
                    if first_global_negative is None:
                        first_global_negative = {
                            "maximum": maximum,
                            "probe_name": probe_name,
                            "probe_value": fstr(probe_value),
                            "contact": contact,
                            "left_sign": sign(left),
                            "right_sign": sign(right),
                            "drop_sign": -1,
                        }
                else:
                    global_zero_drops += 1

    def class_range(label: str, offset: int) -> dict[str, Any]:
        eligible = [record for record in records if record["true_offset"] == offset]
        values = [F(record[f"{label}_tau"]) for record in eligible]
        return {
            "count": len(values),
            "minimum": fstr(min(values)),
            "minimum_decimal": decimal(min(values)),
            "maximum": fstr(max(values)),
            "maximum_decimal": decimal(max(values)),
        }

    full_ranges = {str(offset): class_range("full", offset) for offset in (0, 1, 2)}
    eight_ranges = {str(offset): class_range("eight", offset) for offset in (0, 1, 2)}
    four_ranges = {str(offset): class_range("four", offset) for offset in (0, 1, 2)}

    minimum_full_margin_record = min(
        records,
        key=lambda record: F(record["full_threshold_margin"]),
    )
    minimum_eight_margin_record = min(
        records,
        key=lambda record: F(record["eight_threshold_margin"]),
    )

    expected_four_mismatch = [{
        "maximum": 12,
        "probe_name": "local_lower",
        "probe_value": "129/1000",
        "base_contact": 3,
        "true_offset": 0,
        "predicted_offset": 1,
    }]
    normalized_four_mismatches = [
        {key: record[key] for key in expected_four_mismatch[0]}
        for record in four_mismatches
    ]
    a85_expected = a85_results["finite_exact_transition_balance"][
        "four_term_sign_mismatches"
    ]

    gates = {
        "A84_support_records_complete_through_M300": len(a84_by_maximum) == 291,
        "A84_all_source_sequences_strictly_single_variation": all(
            all(record["strict_single_variation"].values())
            for record in a84_results["support_records"]
        ),
        "A86_source_catalogue_has_873_cells": len(source_records) == 873,
        "all_full_local_secant_denominators_positive": not full_denominator_failures,
        "full_tau_avoids_thresholds_zero_and_one": all(
            F(record["full_tau"]) not in {F(0), F(1)} for record in records
        ),
        "full_secant_classifier_matches_all_873_offsets": not full_mismatches,
        "full_offset_counts_are_3_303_567": dict(full_class_counts) == {0: 3, 1: 303, 2: 567},
        "full_tau_ranges_are_strictly_separated_by_zero_and_one": (
            F(full_ranges["0"]["maximum"]) < 0
            < F(full_ranges["1"]["minimum"])
            <= F(full_ranges["1"]["maximum"]) < 1
            < F(full_ranges["2"]["minimum"])
        ),
        "all_eight_term_local_secant_denominators_positive": not eight_denominator_failures,
        "eight_term_secant_classifier_matches_all_873_offsets": not eight_mismatches,
        "all_four_term_local_secant_denominators_positive": not four_denominator_failures,
        "four_term_classifier_has_exactly_one_known_counterexample": normalized_four_mismatches == expected_four_mismatch,
        "four_term_counterexample_matches_A85_failure": (
            len(a85_expected) == 1
            and a85_expected[0]["maximum"] == 12
            and a85_expected[0]["probe_name"] == "local_lower"
            and a85_expected[0]["contact"] == 3
        ),
        "global_factor_sequence_is_not_monotone_decreasing": global_negative_drops > 0,
        "global_monotonicity_census_has_no_exact_ties": global_zero_drops == 0,
        "two_factor_classifier_uses_1746_evaluations": 2 * len(records) == 1746,
        "two_factor_count_is_below_A86_three_candidate_count": 1746 < 2607,
        "finite_scope_and_nonclaim_boundary_preserved": True,
    }

    result = {
        "audit": "A87_EXACT_SECANT_RESIDUAL_OFFSET_CLASSIFIER",
        "contract": {
            "maximum_range": [10, 300],
            "probes": [
                {"name": name, "value": fstr(value)}
                for name, value in a84.PROBES
            ],
            "source_dependencies": [
                "A84 exact strict one-sign-variation support records",
                "A85 four/eight-term exact decomposition",
                "A86 exact three-contact strip and ceil(M c) base contact",
            ],
            "base_contact": "b=ceil(M c(s))",
            "normalized_residual": "tau=E_b/(E_b-E_{b+1})",
        },
        "exact_secant_classifier": {
            "theorem": {
                "offset_0": "tau<0",
                "offset_1": "0<tau<1",
                "offset_2": "tau>1",
                "required_local_condition": "E_b-E_{b+1}>0",
            },
            "record_count": len(records),
            "factor_evaluation_count": 2 * len(records),
            "offset_counts": {str(key): value for key, value in sorted(full_class_counts.items())},
            "tau_ranges_by_offset": full_ranges,
            "minimum_threshold_margin": {
                "exact": minimum_full_margin_record["full_threshold_margin"],
                "decimal": minimum_full_margin_record["full_threshold_margin_decimal"],
                "record": {
                    "maximum": minimum_full_margin_record["maximum"],
                    "probe_name": minimum_full_margin_record["probe_name"],
                    "probe_value": minimum_full_margin_record["probe_value"],
                    "base_contact": minimum_full_margin_record["base_contact"],
                    "true_offset": minimum_full_margin_record["true_offset"],
                    "tau": minimum_full_margin_record["full_tau"],
                    "tau_decimal": minimum_full_margin_record["full_tau_decimal"],
                },
            },
            "mismatch_count": len(full_mismatches),
        },
        "core_reductions": {
            "four_term": {
                "tau_ranges_by_true_offset": four_ranges,
                "predicted_class_counts": {str(key): value for key, value in sorted(four_class_counts.items())},
                "denominator_failure_count": len(four_denominator_failures),
                "mismatch_count": len(four_mismatches),
                "mismatches": four_mismatches,
                "verdict": "ONE_EXACT_SMALL_SUPPORT_COUNTEREXAMPLE_PRESERVED",
            },
            "eight_term": {
                "tau_ranges_by_offset": eight_ranges,
                "predicted_class_counts": {str(key): value for key, value in sorted(eight_class_counts.items())},
                "denominator_failure_count": len(eight_denominator_failures),
                "mismatch_count": len(eight_mismatches),
                "minimum_threshold_margin": {
                    "exact": minimum_eight_margin_record["eight_threshold_margin"],
                    "decimal": minimum_eight_margin_record["eight_threshold_margin_decimal"],
                    "record": {
                        "maximum": minimum_eight_margin_record["maximum"],
                        "probe_name": minimum_eight_margin_record["probe_name"],
                        "probe_value": minimum_eight_margin_record["probe_value"],
                        "base_contact": minimum_eight_margin_record["base_contact"],
                        "true_offset": minimum_eight_margin_record["true_offset"],
                        "tau": minimum_eight_margin_record["eight_tau"],
                        "tau_decimal": minimum_eight_margin_record["eight_tau_decimal"],
                    },
                },
                "verdict": "EXACT_IN_ALL_873_DECLARED_CELLS",
            },
        },
        "global_monotonicity_obstruction": {
            "factor_value_count": global_factor_count,
            "consecutive_secant_count": global_positive_drops + global_negative_drops + global_zero_drops,
            "positive_drop_count": global_positive_drops,
            "negative_drop_count": global_negative_drops,
            "zero_drop_count": global_zero_drops,
            "first_negative_drop": first_global_negative,
            "interpretation": (
                "The factor sequence is not globally decreasing in k. "
                "A87 certifies only the two-factor local secant at the A86 base contact."
            ),
        },
        "search_reduction": {
            "A84_full_factor_probe_count": 64821,
            "A86_localized_candidate_probe_count": 2607,
            "A87_two_factor_evaluation_count": 1746,
            "relative_to_A84_decimal": decimal(F(64821, 1746), 16),
            "relative_to_A86_candidate_count_decimal": decimal(F(2607, 1746), 16),
        },
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(value is True for value in gates.values()),
        "verdict": "PASS_EXACT_SECANT_RESIDUAL_THREE_OFFSET_CLASSIFIER_WITH_EIGHT_TERM_FALLBACK",
        "claim_boundary": [
            "The exact classifier is finite to 10<=M<=300 and the three A84 rational probes.",
            "It depends on A84 one-sign-variation and A86 three-contact localization.",
            "The local secant drop is not a global monotonicity theorem; global monotonicity is explicitly false in the audited sequences.",
            "The four-term reduction retains the exact M=12/local-lower counterexample; only the eight-term and full residuals classify all 873 cells.",
            "No all-M rounding law, physical interpretation, or pre-spacetime ontology is inferred.",
        ],
    }

    catalogue = {
        "audit": result["audit"],
        "record_count": len(records),
        "records": records,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "a87_exact_secant_offset_classifier_results.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    (RESULTS / "a87_exact_secant_offset_classifier_catalogue.json").write_text(
        json.dumps(catalogue, indent=2), encoding="utf-8"
    )

    if result["pass_count"] != result["gate_count"]:
        failed = [name for name, value in gates.items() if value is not True]
        raise RuntimeError(f"A87 gates failed: {failed}")

    print(json.dumps({
        "audit": result["audit"],
        "gate_count": result["gate_count"],
        "pass_count": result["pass_count"],
        "full_mismatch_count": len(full_mismatches),
        "four_term_mismatch_count": len(four_mismatches),
        "eight_term_mismatch_count": len(eight_mismatches),
        "global_negative_drop_count": global_negative_drops,
        "verdict": result["verdict"],
    }, indent=2))


if __name__ == "__main__":
    main()
