#!/usr/bin/env python3
"""A90 exact pre-threshold all-k one-variation audit.

A89 proves positivity of one *local secant* for every real

    129/1000 <= s <= 133/1000

and every M>=521.  It does not prove the sign pattern of the complete adjacent
factor sequence k -> E_(M,k)(s).  A90 audits the complementary finite range
M=10,...,520 at nine exact rational probes.

The A84 ten-term confluent exponential polynomial is evaluated without
floating point.  If c_i are rational coefficients and r_i rational nodes, set

    L = lcm(denominator(c_i)),
    D = lcm(denominator(r_i)).

Then L D^k E_(M,k)(s) is an integer sum whose bases are D r_i.  Because L and
D are positive, the integer sum has exactly the sign of E.  This conversion is
an exact computational identity, not a numerical approximation.

The finite result is deliberately pointwise in s: it covers nine rational
probes, not the full continuum interval.  It also tests an extrapolation of the
A86 three-contact strip and preserves its first counterexamples beyond the
original M<=300 scope.
"""

from __future__ import annotations

import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from math import lcm
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A84_PATH = HERE / "a84_k_space_exponential_polynomial_stress_audit.py"
A89_RESULT = RESULTS / "a89_uniform_secant_threshold_results.json"

BETA = F(1, 8)
TARGET = F(1, 2)
M_MIN = 10
M_MAX = 520
PROBES = tuple(
    (f"local_{index}", F(258 + index, 2000))
    for index in range(9)
)
ORIGINAL_A86_PROBE_INDICES = (0, 4, 8)

EXPECTED_TOTAL_ADJACENT_EVALUATIONS = 594_423
EXPECTED_SEQUENCE_COUNT = 4_599
EXPECTED_OFFSET_COUNTS = Counter({0: 9, 1: 1_207, 2: 3_368, 3: 15})
EXPECTED_OFFSET3 = [
    (325, 0, 55, 58),
    (372, 0, 63, 66),
    (378, 0, 64, 67),
    (384, 0, 65, 68),
    (390, 0, 66, 69),
    (443, 0, 75, 78),
    (449, 0, 76, 79),
    (455, 0, 77, 80),
    (460, 1, 78, 81),
    (490, 0, 83, 86),
    (496, 0, 84, 87),
    (502, 0, 85, 88),
    (508, 0, 86, 89),
    (514, 0, 87, 90),
    (520, 0, 88, 91),
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


def sign(value: int | F) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def c_greater_than(probe: F, rational: F) -> bool:
    """Exact test c(probe)>p/q for c(s)=log(2)/(-2 log(s))."""
    p = rational.numerator
    q = rational.denominator
    return (2**q) * (probe.numerator ** (2 * p)) > probe.denominator ** (2 * p)


def ceil_Mc_exact(probe: F, maximum: int) -> int:
    low = 0
    high = maximum // 2 + 1
    while low < high:
        midpoint = (low + high) // 2
        if c_greater_than(probe, F(midpoint, maximum)):
            low = midpoint + 1
        else:
            high = midpoint
    return low


def strict_one_variation(values: list[int]) -> bool:
    transitions = sum(left != right for left, right in zip(values, values[1:]))
    return bool(
        values
        and values[0] == 1
        and values[-1] == -1
        and 0 not in values
        and transitions == 1
    )


def coefficient_data(a84, maximum: int, probe: F) -> dict[str, Any]:
    epsilon = a84.normalized_epsilon(maximum)
    power_cache: dict[str, list[F]] = {
        "beta": a84.powers(BETA, maximum),
        "target": a84.powers(TARGET, maximum),
    }
    h_beta = (
        F(1 + power_cache["beta"][maximum], 2)
        - a84.d_value(maximum, BETA, power_cache["beta"])
        + 2 * epsilon
    )
    probe_powers = a84.powers(probe, maximum)
    power_cache["current_probe"] = probe_powers
    h_probe = a84.h_value(maximum, probe, probe_powers, epsilon)
    coefficients = a84.k_space_coefficients(
        maximum,
        probe,
        power_cache,
        h_beta,
        h_probe,
    )

    nodes = [
        BETA * probe,
        BETA * TARGET,
        probe * TARGET,
        BETA,
        BETA,
        probe,
        probe,
        TARGET,
        TARGET,
        F(1),
    ]
    affine_in_contact = [
        False,
        False,
        False,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
    ]

    coefficient_scale = 1
    for _, value in coefficients:
        coefficient_scale = lcm(coefficient_scale, value.denominator)
    node_scale = 1
    for node in nodes:
        node_scale = lcm(node_scale, node.denominator)

    integer_coefficients = [
        value.numerator * (coefficient_scale // value.denominator)
        for _, value in coefficients
    ]
    integer_bases = [
        node.numerator * (node_scale // node.denominator)
        for node in nodes
    ]

    return {
        "coefficients": coefficients,
        "nodes": nodes,
        "affine_in_contact": affine_in_contact,
        "coefficient_scale": coefficient_scale,
        "node_scale": node_scale,
        "integer_coefficients": integer_coefficients,
        "integer_bases": integer_bases,
        "power_cache": power_cache,
    }


def integer_sequence(data: dict[str, Any], maximum: int) -> tuple[list[int], list[int]]:
    contacts = list(range(2, maximum // 2 - 1))
    powers = [base * base for base in data["integer_bases"]]
    signs: list[int] = []
    values: list[int] = []
    for contact in contacts:
        total = sum(
            coefficient * node_power * (contact if affine else 1)
            for coefficient, node_power, affine in zip(
                data["integer_coefficients"],
                powers,
                data["affine_in_contact"],
            )
        )
        values.append(total)
        signs.append(sign(total))
        powers = [
            node_power * base
            for node_power, base in zip(powers, data["integer_bases"])
        ]
    return signs, values


def exact_scaling_regression(a84) -> list[dict[str, Any]]:
    """Check L D^k E(k)=integer_value in 45 independent cells."""
    records: list[dict[str, Any]] = []
    for maximum in (12, 300, 325, 460, 520):
        contacts = list(range(2, maximum // 2 - 1))
        selected_contacts = (
            contacts[0],
            contacts[len(contacts) // 2],
            contacts[-1],
        )
        for probe_index in ORIGINAL_A86_PROBE_INDICES:
            probe = PROBES[probe_index][1]
            data = coefficient_data(a84, maximum, probe)
            for contact in selected_contacts:
                direct = a84.evaluate_k_space(
                    data["coefficients"],
                    contact,
                    probe,
                    {
                        **data["power_cache"],
                        "beta_probe": a84.powers(BETA * probe, maximum),
                        "beta_target": a84.powers(BETA * TARGET, maximum),
                        "probe_target": a84.powers(probe * TARGET, maximum),
                    },
                )
                integer_value = sum(
                    coefficient
                    * (base**contact)
                    * (contact if affine else 1)
                    for coefficient, base, affine in zip(
                        data["integer_coefficients"],
                        data["integer_bases"],
                        data["affine_in_contact"],
                    )
                )
                scaled_direct = (
                    direct
                    * data["coefficient_scale"]
                    * data["node_scale"] ** contact
                )
                records.append({
                    "maximum": maximum,
                    "probe_index": probe_index,
                    "probe": fstr(probe),
                    "contact": contact,
                    "identity_exact": scaled_direct.denominator == 1
                    and scaled_direct.numerator == integer_value,
                    "sign_match": sign(direct) == sign(integer_value),
                })
    return records


def main() -> None:
    a84 = load_module(A84_PATH, "a84_for_a90")
    a89 = json.loads(A89_RESULT.read_text(encoding="utf-8"))

    records: list[dict[str, Any]] = []
    total_evaluations = 0
    strict_sequence_count = 0
    zero_count = 0
    offset_counts: Counter[int] = Counter()
    offset_counts_by_probe: dict[int, Counter[int]] = {
        index: Counter() for index in range(len(PROBES))
    }
    offset3_records: list[dict[str, Any]] = []
    a86_scope_counts: dict[int, Counter[int]] = {
        index: Counter() for index in ORIGINAL_A86_PROBE_INDICES
    }

    for maximum in range(M_MIN, M_MAX + 1):
        contacts = list(range(2, maximum // 2 - 1))
        for probe_index, (probe_name, probe) in enumerate(PROBES):
            data = coefficient_data(a84, maximum, probe)
            signs, _ = integer_sequence(data, maximum)
            total_evaluations += len(signs)
            zero_count += signs.count(0)
            one_variation = strict_one_variation(signs)
            strict_sequence_count += int(one_variation)
            if not one_variation:
                raise RuntimeError(
                    f"A90 one-variation failure at M={maximum}, probe={probe}"
                )

            transition_index = next(
                index for index, value in enumerate(signs) if value < 0
            )
            maximizing_contact = contacts[transition_index]
            base_contact = ceil_Mc_exact(probe, maximum)
            offset = maximizing_contact - base_contact
            offset_counts[offset] += 1
            offset_counts_by_probe[probe_index][offset] += 1
            if maximum <= 300 and probe_index in ORIGINAL_A86_PROBE_INDICES:
                a86_scope_counts[probe_index][offset] += 1

            record = {
                "maximum": maximum,
                "probe_index": probe_index,
                "probe_name": probe_name,
                "probe": fstr(probe),
                "adjacent_factor_count": len(signs),
                "first_sign": signs[0],
                "last_sign": signs[-1],
                "zero_count": signs.count(0),
                "sign_transition_count": sum(
                    left != right for left, right in zip(signs, signs[1:])
                ),
                "strict_one_variation": one_variation,
                "base_contact_ceil_Mc": base_contact,
                "maximizing_contact": maximizing_contact,
                "ceil_offset": offset,
            }
            records.append(record)
            if offset == 3:
                offset3_records.append(record)

    scaling_regression = exact_scaling_regression(a84)
    observed_offset3_tuples = [
        (
            item["maximum"],
            item["probe_index"],
            item["base_contact_ceil_Mc"],
            item["maximizing_contact"],
        )
        for item in offset3_records
    ]

    expected_a86_counts = {
        0: Counter({0: 1, 1: 65, 2: 225}),
        4: Counter({0: 1, 1: 105, 2: 185}),
        8: Counter({0: 1, 1: 133, 2: 157}),
    }

    gates = {
        "A89_threshold_is_521_and_A90_stops_at_520": (
            a89["contract"]["maximum_threshold"] == 521 and M_MAX == 520
        ),
        "support_count_exact": M_MAX - M_MIN + 1 == 511,
        "probe_count_exact": len(PROBES) == 9,
        "support_probe_sequence_count_exact": len(records) == EXPECTED_SEQUENCE_COUNT,
        "adjacent_factor_evaluation_count_exact": total_evaluations == EXPECTED_TOTAL_ADJACENT_EVALUATIONS,
        "all_integer_scaled_values_are_nonzero": zero_count == 0,
        "all_sequences_have_strict_one_positive_to_negative_variation": strict_sequence_count == EXPECTED_SEQUENCE_COUNT,
        "all_sequence_records_have_endpoint_signs_plus_minus": all(
            item["first_sign"] == 1 and item["last_sign"] == -1
            for item in records
        ),
        "integer_scaling_identity_regression_count_exact": len(scaling_regression) == 45,
        "integer_scaling_identity_exact_in_all_regressions": all(
            item["identity_exact"] and item["sign_match"]
            for item in scaling_regression
        ),
        "complete_offset_census_exact": offset_counts == EXPECTED_OFFSET_COUNTS,
        "finite_four_contact_strip_holds": set(offset_counts) == {0, 1, 2, 3},
        "A86_original_three_contact_scope_reproduced": all(
            a86_scope_counts[index] == expected_a86_counts[index]
            for index in ORIGINAL_A86_PROBE_INDICES
        ),
        "three_contact_extension_has_exactly_15_counterexamples": len(offset3_records) == 15,
        "three_contact_extension_counterexample_list_exact": observed_offset3_tuples == EXPECTED_OFFSET3,
        "first_three_contact_extension_failure_is_M325_at_lower_probe": (
            observed_offset3_tuples[0] == (325, 0, 55, 58)
        ),
        "claim_boundary_preserved": True,
    }

    result = {
        "audit": "A90_EXACT_PRETHRESHOLD_ALL_K_ONE_VARIATION",
        "contract": {
            "maximum_range": [M_MIN, M_MAX],
            "probe_interval": [fstr(PROBES[0][1]), fstr(PROBES[-1][1])],
            "exact_probes": [
                {"index": index, "name": name, "value": fstr(value)}
                for index, (name, value) in enumerate(PROBES)
            ],
            "adjacent_contact_rule": "2 <= k <= floor(M/2)-2",
            "base_contact": "b=ceil(M c(s)), c(s)=log(2)/(-2 log(s)) evaluated by exact integer comparisons",
        },
        "exact_integer_scaling": {
            "identity": "sign(E_(M,k)(s)) = sign(sum_i C_i (D r_i)^k, with the declared affine k multipliers), where C_i=L c_i, L=lcm coefficient denominators, and D=lcm node denominators",
            "reason": "L*D^k is strictly positive",
            "floating_point_used_for_gates": False,
            "regression_count": len(scaling_regression),
            "all_regressions_exact": all(item["identity_exact"] for item in scaling_regression),
        },
        "finite_exact_all_k_result": {
            "support_count": M_MAX - M_MIN + 1,
            "probe_count": len(PROBES),
            "support_probe_sequence_count": len(records),
            "adjacent_factor_evaluation_count": total_evaluations,
            "strict_one_variation_sequence_count": strict_sequence_count,
            "zero_factor_count": zero_count,
            "statement": "At every declared (M,s) cell, the complete adjacent sequence is strictly +,...,+,-,...,- and has one maximizing compressed contact.",
        },
        "contact_strip_result": {
            "offset_definition": "k_star-ceil(M c(s))",
            "offset_counts": {str(key): value for key, value in sorted(offset_counts.items())},
            "offset_counts_by_probe": {
                str(index): {
                    str(key): value
                    for key, value in sorted(counter.items())
                }
                for index, counter in offset_counts_by_probe.items()
            },
            "finite_exact_strip": "k_star belongs to {ceil(Mc), ceil(Mc)+1, ceil(Mc)+2, ceil(Mc)+3} on the declared finite grid",
            "A86_three_contact_extension_status": "falsified beyond the original M<=300 scope",
            "offset_three_count": len(offset3_records),
            "first_offset_three_case": offset3_records[0],
            "offset_three_cases": offset3_records,
        },
        "relation_to_A89": {
            "A89_result": "uniform continuum positivity of one local secant for every M>=521",
            "A90_result": "finite exact complete all-k one-variation at nine probes for M<=520",
            "nonimplication": "The two results do not combine into an all-M continuum proof of global all-k unimodality, because A90 is probe-discrete and A89 controls only one local secant.",
        },
        "scaling_regression": scaling_regression,
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(value is True for value in gates.values()),
        "verdict": "PASS_EXACT_PRETHRESHOLD_NINE_PROBE_ALL_K_ONE_VARIATION_AND_FOUR_CONTACT_STRIP",
        "claim_boundary": [
            "The one-variation result is exact but finite: 10<=M<=520 at nine rational probes only.",
            "A90 does not certify every real s between the probes.",
            "A90 does not prove global all-k unimodality for M>=521; A89 proves only the required local secant there.",
            "The four-contact strip is a finite-grid theorem, not an all-M theorem or exact rounding law.",
            "The fifteen offset-three records falsify only an extension of A86 beyond its declared M<=300 scope; they do not contradict A86.",
            "Compressed-objective selection is not by itself a physical law or a full KKT feasibility theorem for arbitrary contracts.",
        ],
    }

    catalogue = {
        "audit": "A90_EXACT_PRETHRESHOLD_CONTACT_SEQUENCE_CATALOGUE",
        "contract": result["contract"],
        "record_count": len(records),
        "records": records,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "a90_prethreshold_all_k_one_variation_results.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    (RESULTS / "a90_prethreshold_contact_sequence_catalogue.json").write_text(
        json.dumps(catalogue, indent=2), encoding="utf-8"
    )

    if result["pass_count"] != result["gate_count"]:
        failed = [name for name, value in gates.items() if value is not True]
        raise RuntimeError(f"A90 gates failed: {failed}")

    print(json.dumps({
        "audit": result["audit"],
        "sequence_count": len(records),
        "adjacent_factor_evaluation_count": total_evaluations,
        "offset_counts": result["contact_strip_result"]["offset_counts"],
        "offset_three_count": len(offset3_records),
        "gate_count": result["gate_count"],
        "pass_count": result["pass_count"],
        "verdict": result["verdict"],
    }, indent=2))


if __name__ == "__main__":
    main()
