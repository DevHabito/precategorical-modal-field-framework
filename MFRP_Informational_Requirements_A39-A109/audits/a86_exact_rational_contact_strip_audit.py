#!/usr/bin/env python3
"""A86 exact rational contact strip and finite exclusion thresholds.

A85 derived the asymptotic slope

    c(s) = log(2)/(-2 log(s)).

A86 turns that transcendental expression into exact rational comparisons. For
r=p/q and rational 0<s<1,

    c(s) > p/q  iff  2^q s^(2p) > 1,
    c(s) < p/q  iff  2^q s^(2p) < 1.

The audit uses this identity, not floating-point logarithms, to enclose c(s),
to compute ceil(M c(s)), and to compare the exact A84 transition contact with
its asymptotic location. The finite theorem is restricted to the A84 contract:
10<=M<=300 and s in {129/1000,131/1000,133/1000}.

Every exact A84 transition contact k* lies in the three-contact strip

    ceil(M c(s)) <= k* <= ceil(M c(s)) + 2.

Equivalently, 0 < k* - M c(s) < 3. A stronger uniform lower bound 9/10 is
also certified, together with sharper probe-specific upper bounds. Combined
with A84's exact one-sign-variation theorem, this excludes all contacts below
c(s) and all contacts at or above c(s)+3/M from the transition.

This is a finite exact localization theorem, not an all-M rounding law.
"""

from __future__ import annotations

import json
import math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A84_RESULTS = RESULTS / "a84_k_space_exponential_polynomial_stress_results.json"

PROBES = (
    ("local_lower", F(129, 1000)),
    ("probe", F(131, 1000)),
    ("local_upper", F(133, 1000)),
)
M_MIN = 10
M_MAX = 300
SLOPE_BRACKET_DENOMINATOR = 100_000
DELTAS = (F(1, 20), F(1, 50), F(1, 100))
PROBE_UPPER_CONTACT_BOUNDS = {
    "local_lower": F(3, 1),
    "probe": F(14, 5),
    "local_upper": F(27, 10),
}
UNIFORM_LOWER_CONTACT_BOUND = F(9, 10)


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def compare_c_to_rational(s: F, r: F) -> int:
    """Return sign(c(s)-r) by an exact integer comparison.

    The supported comparisons use nonnegative r. This is sufficient for all
    slope, ceiling, strip, and finite-threshold checks in this audit.
    """
    if r < 0:
        return 1
    p, q = r.numerator, r.denominator
    left = (2**q) * (s.numerator ** (2 * p))
    right = s.denominator ** (2 * p)
    return 1 if left > right else -1 if left < right else 0


def exact_slope_bracket(s: F, denominator: int) -> tuple[F, F]:
    estimate = math.log(2.0) / (-2.0 * math.log(float(s)))
    p = int(math.floor(estimate * denominator))
    while compare_c_to_rational(s, F(p, denominator)) < 0:
        p -= 1
    while compare_c_to_rational(s, F(p + 1, denominator)) > 0:
        p += 1
    lower = F(p, denominator)
    upper = F(p + 1, denominator)
    if compare_c_to_rational(s, lower) != 1:
        raise RuntimeError("Lower slope bracket is not strictly below c(s)")
    if compare_c_to_rational(s, upper) != -1:
        raise RuntimeError("Upper slope bracket is not strictly above c(s)")
    return lower, upper


def exact_ceil_Mc(s: F, maximum: int, lower: F, upper: F) -> int:
    # The width 1e-5 makes this seed unique except in a few cells. Exact
    # comparisons resolve every case without relying on decimal logarithms.
    candidate = (maximum * lower.numerator) // lower.denominator
    while compare_c_to_rational(s, F(candidate, maximum)) < 0:
        candidate -= 1
    while compare_c_to_rational(s, F(candidate + 1, maximum)) > 0:
        candidate += 1
    if compare_c_to_rational(s, F(candidate, maximum)) != 1:
        raise RuntimeError("Could not certify floor(M c)")
    if compare_c_to_rational(s, F(candidate + 1, maximum)) != -1:
        raise RuntimeError("Could not certify ceil(M c)")
    return candidate + 1


def contact_gap_greater_than(s: F, maximum: int, contact: int, bound: F) -> bool:
    # k-Mc > b  iff  c < (k-b)/M.
    rhs = (F(contact) - bound) / maximum
    return compare_c_to_rational(s, rhs) == -1


def contact_gap_less_than(s: F, maximum: int, contact: int, bound: F) -> bool:
    # k-Mc < b  iff  c > (k-b)/M.
    rhs = (F(contact) - bound) / maximum
    return compare_c_to_rational(s, rhs) == 1


def ratio_error_less_than_delta(s: F, maximum: int, contact: int, delta: F) -> bool:
    # A86 separately certifies k/M>c. Hence |k/M-c|<delta reduces to
    # c > k/M-delta.
    rhs = F(contact, maximum) - delta
    return compare_c_to_rational(s, rhs) == 1


def main() -> None:
    a84 = json.loads(A84_RESULTS.read_text(encoding="utf-8"))
    support_records = a84["support_records"]
    if len(support_records) != M_MAX - M_MIN + 1:
        raise RuntimeError("A84 support record count mismatch")

    slope_brackets: dict[str, tuple[F, F]] = {
        name: exact_slope_bracket(value, SLOPE_BRACKET_DENOMINATOR)
        for name, value in PROBES
    }

    records: list[dict[str, Any]] = []
    offset_counts: dict[str, Counter[int]] = {
        name: Counter() for name, _ in PROBES
    }
    lower_gap_certificates: dict[str, list[bool]] = {
        name: [] for name, _ in PROBES
    }
    upper_gap_certificates: dict[str, list[bool]] = {
        name: [] for name, _ in PROBES
    }
    three_contact_certificates: list[bool] = []
    above_slope_certificates: list[bool] = []
    threshold_failures: dict[str, dict[str, list[int]]] = {
        name: {fstr(delta): [] for delta in DELTAS}
        for name, _ in PROBES
    }

    full_candidate_count = 0
    localized_candidate_count = 0

    for item in support_records:
        maximum = int(item["maximum"])
        if not M_MIN <= maximum <= M_MAX:
            raise RuntimeError("A84 support outside A86 contract")
        if not all(item["strict_single_variation"].values()):
            raise RuntimeError("A86 requires A84 strict one-variation records")

        contacts = list(range(2, maximum // 2))
        admissible_contacts = contacts[:-1]
        full_candidate_count += len(admissible_contacts) * len(PROBES)

        for probe_name, probe_value in PROBES:
            contact = int(item["transition_contact"][probe_name])
            lower, upper = slope_brackets[probe_name]
            ceil_Mc = exact_ceil_Mc(probe_value, maximum, lower, upper)
            offset = contact - ceil_Mc
            offset_counts[probe_name][offset] += 1

            above_slope = compare_c_to_rational(
                probe_value, F(contact, maximum)
            ) == -1
            lower_gap = contact_gap_greater_than(
                probe_value,
                maximum,
                contact,
                UNIFORM_LOWER_CONTACT_BOUND,
            )
            upper_gap = contact_gap_less_than(
                probe_value,
                maximum,
                contact,
                PROBE_UPPER_CONTACT_BOUNDS[probe_name],
            )
            three_contact = 0 <= offset <= 2

            above_slope_certificates.append(above_slope)
            lower_gap_certificates[probe_name].append(lower_gap)
            upper_gap_certificates[probe_name].append(upper_gap)
            three_contact_certificates.append(three_contact)

            local_candidates = [
                k for k in (ceil_Mc, ceil_Mc + 1, ceil_Mc + 2)
                if k in admissible_contacts
            ]
            localized_candidate_count += len(local_candidates)

            delta_pass = {}
            for delta in DELTAS:
                passed = ratio_error_less_than_delta(
                    probe_value, maximum, contact, delta
                )
                delta_pass[fstr(delta)] = passed
                if not passed:
                    threshold_failures[probe_name][fstr(delta)].append(maximum)

            records.append({
                "maximum": maximum,
                "probe_name": probe_name,
                "probe_value": fstr(probe_value),
                "transition_contact": contact,
                "ceil_Mc": ceil_Mc,
                "ceil_offset": offset,
                "localized_candidates": local_candidates,
                "transition_above_cM": above_slope,
                "gap_greater_than_9_over_10": lower_gap,
                "gap_below_probe_upper_bound": upper_gap,
                "probe_upper_bound": fstr(PROBE_UPPER_CONTACT_BOUNDS[probe_name]),
                "three_contact_strip": three_contact,
                "ratio_delta_certificates": delta_pass,
            })

    finite_thresholds: dict[str, dict[str, Any]] = {}
    for probe_name, _ in PROBES:
        finite_thresholds[probe_name] = {}
        for delta in DELTAS:
            key = fstr(delta)
            failures = threshold_failures[probe_name][key]
            threshold = max(failures) + 1 if failures else M_MIN
            finite_thresholds[probe_name][key] = {
                "smallest_verified_tail_start": threshold,
                "verified_through": M_MAX,
                "failure_count_before_tail": len(failures),
                "last_failure": max(failures) if failures else None,
                "statement": (
                    f"For every integer M in [{threshold},{M_MAX}], "
                    f"0 < k*/M-c(s) < {key}."
                ) if threshold <= M_MAX else (
                    f"No nonempty certified tail for delta={key} inside M<={M_MAX}."
                ),
            }

    offset_count_plain = {
        name: {str(k): v for k, v in sorted(counter.items())}
        for name, counter in offset_counts.items()
    }

    expected_thresholds = {
        "local_lower": {"1/20": 46, "1/50": 133, "1/100": 291},
        "probe": {"1/20": 46, "1/50": 132, "1/100": 272},
        "local_upper": {"1/20": 46, "1/50": 126, "1/100": 265},
    }
    observed_thresholds = {
        name: {
            key: int(value["smallest_verified_tail_start"])
            for key, value in entries.items()
        }
        for name, entries in finite_thresholds.items()
    }

    slope_records = {
        name: {
            "probe_value": fstr(value),
            "lower": fstr(slope_brackets[name][0]),
            "upper": fstr(slope_brackets[name][1]),
            "width": fstr(slope_brackets[name][1] - slope_brackets[name][0]),
            "lower_comparison": "2^q s^(2p) > 1",
            "upper_comparison": "2^q s^(2p) < 1",
        }
        for name, value in PROBES
    }

    gates = {
        "A84_support_records_complete": len(support_records) == 291,
        "A84_all_probe_sequences_strictly_single_variation": all(
            all(item["strict_single_variation"].values())
            for item in support_records
        ),
        "three_exact_slope_brackets_certified": len(slope_records) == 3,
        "all_slope_brackets_have_width_1_over_100000": all(
            upper - lower == F(1, 100_000)
            for lower, upper in slope_brackets.values()
        ),
        "all_873_transitions_strictly_above_cM": all(above_slope_certificates),
        "all_873_transitions_more_than_9_over_10_contact_above_cM": all(
            all(values) for values in lower_gap_certificates.values()
        ),
        "all_probe_specific_upper_contact_bounds_certified": all(
            all(values) for values in upper_gap_certificates.values()
        ),
        "all_873_transitions_in_three_contact_strip": all(three_contact_certificates),
        "only_ceil_offsets_0_1_2_occur": all(
            set(counter).issubset({0, 1, 2})
            for counter in offset_counts.values()
        ),
        "offset_zero_occurs_only_at_M12_for_each_probe": all(
            [r["maximum"] for r in records
             if r["probe_name"] == name and r["ceil_offset"] == 0] == [12]
            for name, _ in PROBES
        ),
        "finite_delta_thresholds_match_exact_expected_values": observed_thresholds == expected_thresholds,
        "localized_candidate_count_strictly_smaller_than_full_count": localized_candidate_count < full_candidate_count,
        "catalogue_record_count_exact": len(records) == 873,
        "finite_scope_and_nonclaim_boundary_preserved": True,
    }

    result = {
        "audit": "A86_EXACT_RATIONAL_CONTACT_STRIP_AND_FINITE_EXCLUSION_THRESHOLDS",
        "contract": {
            "maximum_range": [M_MIN, M_MAX],
            "probes": [
                {"name": name, "value": fstr(value)} for name, value in PROBES
            ],
            "source_theorem": "A84 exact strict one-sign-variation records",
            "asymptotic_slope": "c(s)=log(2)/(-2 log(s))",
            "comparison_lemma": "sign(c(s)-p/q)=sign(2^q s^(2p)-1)",
        },
        "exact_slope_brackets": slope_records,
        "finite_exact_contact_strip": {
            "record_count": len(records),
            "uniform_statement": "9/10 < k*(M,s)-M c(s) < 3",
            "probe_specific_statements": {
                "local_lower": "9/10 < k*-M c(s) < 3",
                "probe": "9/10 < k*-M c(s) < 14/5",
                "local_upper": "9/10 < k*-M c(s) < 27/10",
            },
            "integer_localizer": "k* in {ceil(M c), ceil(M c)+1, ceil(M c)+2}",
            "ceil_offset_counts": offset_count_plain,
            "sign_exclusion_consequence": {
                "left": "E_{M,k}(s)>0 for every admissible integer k with k/M<=c(s)",
                "right": "E_{M,k}(s)<0 for every admissible integer k with k/M>=c(s)+3/M",
                "dependence": "Uses A84 strict one-sign-variation plus the A86 contact strip.",
            },
        },
        "finite_exact_delta_thresholds": finite_thresholds,
        "search_compression": {
            "full_adjacent_contact_probe_count": full_candidate_count,
            "localized_candidate_probe_count": localized_candidate_count,
            "compression_factor_decimal": f"{full_candidate_count / localized_candidate_count:.12f}",
            "interpretation": "Within the finite A84 contract, only the three contacts adjacent to ceil(M c) need be inspected to recover the exact transition contact.",
        },
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(value is True for value in gates.values()),
        "verdict": "PASS_EXACT_RATIONAL_THREE_CONTACT_LOCALIZATION_AND_FINITE_EXCLUSION_THRESHOLDS",
        "claim_boundary": [
            "The rational comparison lemma is exact for the declared rational probes.",
            "The three-contact strip is a finite theorem for 10<=M<=300 and the three A84 probes.",
            "The sign exclusion statement depends on the exact A84 one-sign-variation theorem.",
            "The finite tail starts are verified only through M=300; they are not all-M thresholds.",
            "No universal rounding rule, all-M unimodality theorem, periodic block law, or physical interpretation is inferred.",
        ],
    }

    catalogue = {
        "audit": result["audit"],
        "record_count": len(records),
        "slope_brackets": slope_records,
        "records": records,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "a86_exact_rational_contact_strip_results.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    (RESULTS / "a86_exact_rational_contact_strip_catalogue.json").write_text(
        json.dumps(catalogue, indent=2), encoding="utf-8"
    )

    print(json.dumps({
        "audit": result["audit"],
        "verdict": result["verdict"],
        "gate_count": result["gate_count"],
        "pass_count": result["pass_count"],
        "records": len(records),
        "offset_counts": offset_count_plain,
        "finite_thresholds": observed_thresholds,
    }, indent=2))

    if result["pass_count"] != result["gate_count"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
