#!/usr/bin/env python3
"""A84 exact k-space exponential-polynomial reduction and finite stress audit.

A83 represented each adjacent objective difference by a seven-term polynomial
in the observation variable s. A84 changes coordinates: for fixed (M,s), the
same factor is an exponential polynomial in the discrete contact k.

The analytic identity has ten confluent exponential terms with nodes

    beta*s < beta*target < s*target < beta < s < target < 1,

and basis order

    (beta*s)^k, (beta*target)^k, (s*target)^k,
    beta^k, k beta^k, s^k, k s^k,
    target^k, k target^k, 1.

The finite exact stress covers M=10,...,300 at three rational probes
s in {129/1000, 131/1000, 133/1000}. It checks 21,607 adjacent pairs and
64,821 exact pair/probe signs. Every one of the 873 support/probe sign
sequences has exactly one positive-to-negative variation and therefore one
strict compressed maximizer.

The coefficient sign pattern in the declared confluent-node order is always

    + - + + - - + - + -,

which has seven variations. Therefore a direct variation-diminishing or
Descartes-type coefficient argument cannot, by itself, prove the observed
one-variation law: its raw bound is seven, not one. This is an obstruction to
that proof route, not a counterexample to finite unimodality.

The audit is exact at the three probes. Endpoint disagreements imply at least
one root inside the local interval, but A84 does not claim a complete interval
root atlas for M>80.
"""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"

F = Fraction
BETA = F(1, 8)
TARGET = F(1, 2)
LOCAL_LOWER = F(129, 1000)
PROBE = F(131, 1000)
LOCAL_UPPER = F(133, 1000)
PROBES = (
    ("local_lower", LOCAL_LOWER),
    ("probe", PROBE),
    ("local_upper", LOCAL_UPPER),
)
M_MIN = 10
M_MAX = 300
EXPECTED_COEFFICIENT_SIGNS = [1, -1, 1, 1, -1, -1, 1, -1, 1, -1]


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sign(value: F) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def normalized_epsilon(maximum: int) -> F:
    h = maximum // 2
    scale = 1875 if maximum % 2 == 0 else 2500
    return F(1, scale * 2**h)


def powers(value: F, maximum: int) -> list[F]:
    output = [F(1)] * (maximum + 1)
    for exponent in range(1, maximum + 1):
        output[exponent] = output[exponent - 1] * value
    return output


def d_value(maximum: int, value: F, value_powers: list[F]) -> F:
    h = maximum // 2
    u = F(1, 2**h)
    denominator = 1 - (h + 1) * u
    if maximum % 2 == 0:
        return (
            (-2 * u / denominator) * value
            + (1 + 2 * h * u / denominator) * value_powers[h]
            + (-2 * (h - 1) * u / denominator) * value_powers[h + 1]
        )
    return (
        (-F(3, 2) * u / denominator) * value
        + (F(1, 2) + F(3, 2) * h * u / denominator) * value_powers[h]
        + (F(1, 2) - F(3, 2) * (h - 1) * u / denominator)
        * value_powers[h + 1]
    )


def b_value(maximum: int, contact: int, value_powers: list[F]) -> F:
    return (
        value_powers[contact]
        - F(maximum - contact, maximum)
        - F(contact, maximum) * value_powers[maximum]
    )


def delta_b_value(maximum: int, contact: int, value_powers: list[F]) -> F:
    return (
        value_powers[contact + 1]
        - value_powers[contact]
        + F(1 - value_powers[maximum], maximum)
    )


def h_value(
    maximum: int,
    value: F,
    value_powers: list[F],
    epsilon: F,
) -> F:
    return (
        F(1 + value_powers[maximum], 2)
        - d_value(maximum, value, value_powers)
        - 2 * epsilon
    )


def adjacent_cofactors(
    maximum: int,
    contact: int,
    power_cache: dict[str, list[F]],
    h_beta: F,
) -> tuple[F, F, F]:
    beta_powers = power_cache["beta"]
    target_powers = power_cache["target"]
    b_beta = b_value(maximum, contact, beta_powers)
    b_target = b_value(maximum, contact, target_powers)
    delta_beta = delta_b_value(maximum, contact, beta_powers)
    delta_target = delta_b_value(maximum, contact, target_powers)
    a_target = F(1 + target_powers[maximum], 2)
    x = a_target * b_beta - h_beta * b_target
    y = -a_target * delta_beta + h_beta * delta_target
    w = -b_beta * delta_target + b_target * delta_beta
    return x, y, w


def seven_term_value(
    maximum: int,
    contact: int,
    probe_name: str,
    power_cache: dict[str, list[F]],
    h_probe: F,
    cofactors: tuple[F, F, F],
) -> F:
    x, y, w = cofactors
    probe_powers = power_cache[probe_name]
    return (
        x * delta_b_value(maximum, contact, probe_powers)
        + y * b_value(maximum, contact, probe_powers)
        + w * h_probe
    )


def k_space_coefficients(
    maximum: int,
    probe_value: F,
    power_cache: dict[str, list[F]],
    h_beta: F,
    h_probe: F,
) -> list[tuple[str, F]]:
    beta_powers = power_cache["beta"]
    target_powers = power_cache["target"]
    probe_powers = power_cache["current_probe"]
    a_beta = F(1 - beta_powers[maximum], maximum)
    a_target = F(1 - target_powers[maximum], maximum)
    a_probe = F(1 - probe_powers[maximum], maximum)
    capital_a = F(1 + target_powers[maximum], 2)

    c_beta_probe = capital_a * (probe_value - BETA)
    c_beta_target = h_probe * (BETA - TARGET)
    c_probe_target = h_beta * (TARGET - probe_value)

    c_k_beta = -(BETA - 1) * (capital_a * a_probe - h_probe * a_target)
    c_beta = (
        capital_a * a_probe
        + capital_a * BETA
        - capital_a
        - h_probe * a_target
        - h_probe * BETA
        + h_probe
    )

    c_k_target = (TARGET - 1) * (h_beta * a_probe - h_probe * a_beta)
    c_target = (
        -h_beta * a_probe
        - h_beta * TARGET
        + h_beta
        + h_probe * a_beta
        + h_probe * TARGET
        - h_probe
    )

    c_k_probe = (probe_value - 1) * (
        capital_a * a_beta - h_beta * a_target
    )
    c_probe = (
        -capital_a * a_beta
        - capital_a * probe_value
        + capital_a
        + h_beta * a_target
        + h_beta * probe_value
        - h_beta
    )

    c_constant = (
        -capital_a * a_probe
        + capital_a * a_beta
        + h_beta * a_probe
        - h_beta * a_target
        - h_probe * a_beta
        + h_probe * a_target
    )

    # Declared ascending node/confluent order:
    # beta*s, beta*target, s*target, beta, k*beta,
    # s, k*s, target, k*target, 1.
    return [
        ("(beta*s)^k", c_beta_probe),
        ("(beta*target)^k", c_beta_target),
        ("(s*target)^k", c_probe_target),
        ("beta^k", c_beta),
        ("k*beta^k", c_k_beta),
        ("s^k", c_probe),
        ("k*s^k", c_k_probe),
        ("target^k", c_target),
        ("k*target^k", c_k_target),
        ("1", c_constant),
    ]


def evaluate_k_space(
    coefficients: list[tuple[str, F]],
    contact: int,
    probe_value: F,
    power_cache: dict[str, list[F]],
) -> F:
    coefficient_map = dict(coefficients)
    beta_powers = power_cache["beta"]
    target_powers = power_cache["target"]
    probe_powers = power_cache["current_probe"]
    return (
        coefficient_map["(beta*s)^k"] * power_cache["beta_probe"][contact]
        + coefficient_map["(beta*target)^k"] * power_cache["beta_target"][contact]
        + coefficient_map["(s*target)^k"] * power_cache["probe_target"][contact]
        + coefficient_map["beta^k"] * beta_powers[contact]
        + coefficient_map["k*beta^k"] * contact * beta_powers[contact]
        + coefficient_map["s^k"] * probe_powers[contact]
        + coefficient_map["k*s^k"] * contact * probe_powers[contact]
        + coefficient_map["target^k"] * target_powers[contact]
        + coefficient_map["k*target^k"] * contact * target_powers[contact]
        + coefficient_map["1"]
    )


def symbolic_identity_gate() -> bool:
    """Verify the generic algebraic expansion once with independent symbols."""
    b, t, s = sp.symbols("b t s")
    bk, tk, sk, k = sp.symbols("B T S K")
    a_b, a_t, a_s = sp.symbols("a_b a_t a_s")
    capital_a, h_b, h_s = sp.symbols("A H_b H_s")

    b_b = bk - 1 + k * a_b
    b_t = tk - 1 + k * a_t
    b_s = sk - 1 + k * a_s
    delta_b = (b - 1) * bk + a_b
    delta_t = (t - 1) * tk + a_t
    delta_s = (s - 1) * sk + a_s

    x = capital_a * b_b - h_b * b_t
    y = -capital_a * delta_b + h_b * delta_t
    w = -b_b * delta_t + b_t * delta_b
    original = sp.expand(x * delta_s + y * b_s + w * h_s)

    expansion = (
        capital_a * (s - b) * bk * sk
        + h_s * (b - t) * bk * tk
        + h_b * (t - s) * tk * sk
        + (
            capital_a * a_s
            + capital_a * b
            - capital_a
            - h_s * a_t
            - h_s * b
            + h_s
        ) * bk
        - (b - 1) * (capital_a * a_s - h_s * a_t) * k * bk
        + (
            -capital_a * a_b
            - capital_a * s
            + capital_a
            + h_b * a_t
            + h_b * s
            - h_b
        ) * sk
        + (s - 1) * (capital_a * a_b - h_b * a_t) * k * sk
        + (
            -h_b * a_s
            - h_b * t
            + h_b
            + h_s * a_b
            + h_s * t
            - h_s
        ) * tk
        + (t - 1) * (h_b * a_s - h_s * a_b) * k * tk
        + (
            -capital_a * a_s
            + capital_a * a_b
            + h_b * a_s
            - h_b * a_t
            - h_s * a_b
            + h_s * a_t
        )
    )
    return sp.expand(original - expansion) == 0


def strict_single_variation(signs: list[int]) -> bool:
    transitions = sum(left != right for left, right in zip(signs, signs[1:]))
    return bool(
        signs
        and 0 not in signs
        and signs[0] == 1
        and signs[-1] == -1
        and transitions == 1
    )


def main() -> None:
    symbolic_identity_ok = symbolic_identity_gate()

    adjacent_pair_count = 0
    pair_probe_evaluation_count = 0
    coefficient_pattern_count = 0
    coefficient_variation_census: Counter[int] = Counter()
    strict_sequence_count = 0
    endpoint_crossings: list[dict[str, Any]] = []
    support_records: list[dict[str, Any]] = []
    probe_maximizers: list[tuple[int, int]] = []

    for maximum in range(M_MIN, M_MAX + 1):
        h = maximum // 2
        contacts = list(range(2, h))
        adjacent_contacts = contacts[:-1]
        adjacent_pair_count += len(adjacent_contacts)
        epsilon = normalized_epsilon(maximum)

        power_cache: dict[str, list[F]] = {
            "beta": powers(BETA, maximum),
            "target": powers(TARGET, maximum),
        }
        h_beta = (
            F(1 + power_cache["beta"][maximum], 2)
            - d_value(maximum, BETA, power_cache["beta"])
            + 2 * epsilon
        )

        sequences: dict[str, list[int]] = {}
        maximizers: dict[str, int] = {}
        transition_contacts: dict[str, int] = {}
        coefficient_patterns: dict[str, list[int]] = {}

        for probe_name, probe_value in PROBES:
            current_powers = powers(probe_value, maximum)
            power_cache[probe_name] = current_powers
            power_cache["current_probe"] = current_powers
            h_probe = h_value(
                maximum,
                probe_value,
                current_powers,
                epsilon,
            )
            k_coefficients = k_space_coefficients(
                maximum,
                probe_value,
                power_cache,
                h_beta,
                h_probe,
            )
            coefficient_signs = [sign(value) for _, value in k_coefficients]
            coefficient_patterns[probe_name] = coefficient_signs
            coefficient_variations = sum(
                left != right
                for left, right in zip(coefficient_signs, coefficient_signs[1:])
            )
            coefficient_variation_census[coefficient_variations] += 1
            coefficient_pattern_count += int(
                coefficient_signs == EXPECTED_COEFFICIENT_SIGNS
            )

            current_signs: list[int] = []
            for contact in adjacent_contacts:
                cofactors = adjacent_cofactors(
                    maximum,
                    contact,
                    power_cache,
                    h_beta,
                )
                seven_value = seven_term_value(
                    maximum,
                    contact,
                    probe_name,
                    power_cache,
                    h_probe,
                    cofactors,
                )
                pair_probe_evaluation_count += 1
                current_signs.append(sign(seven_value))

            sequences[probe_name] = current_signs
            is_strict = strict_single_variation(current_signs)
            strict_sequence_count += int(is_strict)
            if not is_strict:
                raise RuntimeError(
                    f"One-variation failure at M={maximum}, probe={probe_name}"
                )
            transition_index = next(
                index for index, value in enumerate(current_signs) if value < 0
            )
            maximizing_contact = adjacent_contacts[transition_index]
            transition_contacts[probe_name] = maximizing_contact
            maximizers[probe_name] = maximizing_contact

        probe_maximizers.append((maximum, maximizers["probe"]))

        lower_signs = sequences["local_lower"]
        upper_signs = sequences["local_upper"]
        differing_indices = [
            index
            for index, (left, right) in enumerate(zip(lower_signs, upper_signs))
            if left != right
        ]
        if len(differing_indices) > 1:
            raise RuntimeError(
                f"More than one endpoint-crossing adjacent factor at M={maximum}"
            )
        if differing_indices:
            index = differing_indices[0]
            endpoint_crossings.append({
                "maximum": maximum,
                "lower_contact": adjacent_contacts[index],
                "upper_contact": adjacent_contacts[index] + 1,
                "direction": [lower_signs[index], upper_signs[index]],
                "maximizer_at_local_lower": maximizers["local_lower"],
                "maximizer_at_local_upper": maximizers["local_upper"],
                "claim": "At least one root exists in the open interval by continuity; A84 does not count or isolate all roots.",
            })

        support_records.append({
            "maximum": maximum,
            "adjacent_pair_count": len(adjacent_contacts),
            "maximizing_contact": maximizers,
            "transition_contact": transition_contacts,
            "coefficient_sign_pattern": coefficient_patterns,
            "strict_single_variation": {
                name: strict_single_variation(sequences[name])
                for name, _ in PROBES
            },
            "endpoint_crossing_count": len(differing_indices),
        })

    # Compress the probe maximizer into consecutive support blocks.
    blocks: list[dict[str, int]] = []
    block_start, current_contact = probe_maximizers[0]
    previous_maximum = block_start
    for maximum, contact in probe_maximizers[1:]:
        if contact != current_contact:
            blocks.append({
                "maximum_start": block_start,
                "maximum_end": previous_maximum,
                "contact": current_contact,
                "length": previous_maximum - block_start + 1,
            })
            block_start = maximum
            current_contact = contact
        previous_maximum = maximum
    blocks.append({
        "maximum_start": block_start,
        "maximum_end": previous_maximum,
        "contact": current_contact,
        "length": previous_maximum - block_start + 1,
    })
    block_length_census = Counter(block["length"] for block in blocks)

    crossing_direction_census = Counter(
        tuple(record["direction"]) for record in endpoint_crossings
    )

    gates = {
        "generic_ten_term_k_space_identity_symbolic": symbolic_identity_ok,
        "adjacent_pair_count_exact": adjacent_pair_count == 21607,
        "pair_probe_evaluation_count_exact": pair_probe_evaluation_count == 64821,
        "all_coefficient_vectors_have_declared_sign_pattern": coefficient_pattern_count == 873,
        "all_coefficient_vectors_have_seven_sign_variations": coefficient_variation_census == Counter({7: 873}),
        "all_support_probe_sequences_have_one_sign_variation": strict_sequence_count == 873,
        "endpoint_crossing_factor_count_exact": len(endpoint_crossings) == 51,
        "endpoint_crossing_directions_exact": crossing_direction_census == Counter({(-1, 1): 50, (1, -1): 1}),
        "at_most_one_endpoint_crossing_factor_per_support": all(record["endpoint_crossing_count"] <= 1 for record in support_records),
        "probe_contact_block_count_exact": len(blocks) == 51,
        "probe_block_length_census_exact": block_length_census == Counter({6: 38, 5: 12, 3: 1}),
        "A83_scope_reproduced_inside_extended_range": all(
            record["strict_single_variation"][name]
            for record in support_records[:71]
            for name, _ in PROBES
        ),
        "variation_diminishing_raw_bound_is_not_one": all(
            variation == 7 for variation in coefficient_variation_census
        ),
        "scope_and_nonclaim_boundary_preserved": (
            M_MIN == 10
            and M_MAX == 300
            and LOCAL_LOWER == F(129, 1000)
            and PROBE == F(131, 1000)
            and LOCAL_UPPER == F(133, 1000)
        ),
    }

    summary = {
        "audit": "A84_K_SPACE_EXPONENTIAL_POLYNOMIAL_STRESS",
        "contract": {
            "maximum_range": [M_MIN, M_MAX],
            "adjacent_contact_rule": "2 <= k < floor(M/2)-1",
            "exact_probes": [
                {"name": name, "value": fstr(value)} for name, value in PROBES
            ],
            "beta": fstr(BETA),
            "target": fstr(TARGET),
        },
        "analytic_k_space_reduction": {
            "identity": "E_(M,k)(s) is a ten-term confluent exponential polynomial in k",
            "basis_order": [
                "(beta*s)^k",
                "(beta*target)^k",
                "(s*target)^k",
                "beta^k",
                "k*beta^k",
                "s^k",
                "k*s^k",
                "target^k",
                "k*target^k",
                "1",
            ],
            "node_order_on_declared_probe_set": "beta*s < beta*target < s*target < beta < s < target < 1",
            "coefficient_sign_pattern": EXPECTED_COEFFICIENT_SIGNS,
            "coefficient_sign_pattern_symbols": ["+", "-", "+", "+", "-", "-", "+", "-", "+", "-"],
            "coefficient_variation_count": 7,
            "interpretation": (
                "A direct generalized-Descartes or variation-diminishing argument based only on coefficient signs can permit up to seven zeros/sign changes. It does not prove the observed one-variation law."
            ),
        },
        "finite_exact_stress": {
            "support_count": M_MAX - M_MIN + 1,
            "adjacent_pair_count": adjacent_pair_count,
            "pair_probe_exact_evaluation_count": pair_probe_evaluation_count,
            "ten_term_identity_verification": "generic symbolic identity, independent of the finite scan",
            "support_probe_sequence_count": 873,
            "strict_single_variation_sequence_count": strict_sequence_count,
            "endpoint_crossing_factor_count": len(endpoint_crossings),
            "endpoint_crossing_direction_census": {
                f"{left}->{right}": count
                for (left, right), count in sorted(crossing_direction_census.items())
            },
            "probe_maximizer_block_count": len(blocks),
            "probe_block_length_census": {
                str(length): count
                for length, count in sorted(block_length_census.items())
            },
            "verdict": (
                "EXACT_ONE_SIGN_VARIATION_AT_THREE_RATIONAL_PROBES_THROUGH_M300"
            ),
        },
        "endpoint_crossings": endpoint_crossings,
        "probe_contact_blocks": blocks,
        "support_records": support_records,
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": (
            "PASS_K_SPACE_EXPONENTIAL_POLYNOMIAL_REDUCTION_AND_FINITE_ONE_VARIATION_STRESS"
            if all(gates.values())
            else "FAIL"
        ),
        "claim_boundary": [
            "The ten-term k-space formula is an exact algebraic identity under the reduced contract.",
            "The one-sign-variation theorem is finite and pointwise: 10<=M<=300 at exactly three rational s values.",
            "Endpoint sign disagreements prove existence of at least one interior root by continuity, not uniqueness or a complete interval atlas.",
            "The seven coefficient variations make the naive variation-diminishing route too weak; they do not disprove stronger structured inequalities.",
            "No all-M theorem, periodic contact law, asymptotic recurrence, or physical interpretation is inferred.",
        ],
    }

    compact_catalogue = {
        "audit": "A84_EXACT_PROBE_CONTACT_AND_ENDPOINT_CROSSING_CATALOGUE",
        "scope": summary["contract"],
        "probe_contact_blocks": blocks,
        "endpoint_crossings": endpoint_crossings,
        "support_records": support_records,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    result_path = RESULTS / "a84_k_space_exponential_polynomial_stress_results.json"
    catalogue_path = RESULTS / "a84_probe_contact_and_crossing_catalogue.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    catalogue_path.write_text(json.dumps(compact_catalogue, indent=2), encoding="utf-8")

    print(json.dumps({
        "audit": summary["audit"],
        "support_count": M_MAX - M_MIN + 1,
        "adjacent_pair_count": adjacent_pair_count,
        "pair_probe_evaluation_count": pair_probe_evaluation_count,
        "strict_sequence_count": strict_sequence_count,
        "endpoint_crossing_count": len(endpoint_crossings),
        "coefficient_variation_census": dict(coefficient_variation_census),
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
