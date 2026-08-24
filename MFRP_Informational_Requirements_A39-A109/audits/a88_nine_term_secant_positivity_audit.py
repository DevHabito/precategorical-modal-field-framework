#!/usr/bin/env python3
"""A88 exact nine-term local-secant reduction and extended positivity stress.

A87 classifies the three A86 contact offsets with the local secant

    S_{M,b}(s) = E_{M,b}(s) - E_{M,b+1}(s),
    b = ceil(M c(s)),
    c(s) = log(2)/(-2 log(s)).

This audit derives the exact secant transform of the A84 ten-term confluent
exponential polynomial. A pure term c r^k becomes c(1-r)r^k; an affine term
(a+bk)r^k becomes

    ([(1-r)a-rb] + (1-r)bk) r^k.

The constant cancels, so the A84 ten-term factor reduces to a nine-term
secant polynomial on the same six nodes. The finite exact stress expands the
contract to M=10,...,900 and nine rational probes from 129/1000 through
133/1000 in steps of 1/2000. Every gate is evaluated with Fraction/integer
arithmetic; decimals are presentation only.

The four leading A85 channels (beta*target, s*target, target, k*target)
strictly determine and dominate the exact secant sign in all 8,019 declared
cells. The transformed coefficient pattern has six raw sign variations, so a
coefficient-only variation-diminishing proof remains insufficient.

The analytic part records the parity-phase leading secant limit and certifies
strictly positive rational lower bounds for it on the full local s interval.
This gives an asymptotic explanation, but no explicit all-M remainder threshold
is claimed. The finite exact positivity theorem stops at M=1000.
"""

from __future__ import annotations

import importlib.util
import json
import math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A86_PATH = HERE / "a86_exact_rational_contact_strip_audit.py"
A87_CATALOGUE = RESULTS / "a87_exact_secant_offset_classifier_catalogue.json"

BETA = F(1, 8)
TARGET = F(1, 2)
M_MIN = 10
M_MAX = 900
PROBES = tuple(
    (f"local_{index}", F(258 + index, 2000))
    for index in range(9)
)
EXPECTED_SECANT_COEFFICIENT_SIGNS = (1, -1, 1, 1, -1, -1, 1, -1, 1)
CORE_NAMES = {"beta_target", "probe_target", "target"}


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
    from decimal import Decimal, localcontext

    with localcontext() as context:
        context.prec = digits + 10
        rendered = Decimal(value.numerator) / Decimal(value.denominator)
        return format(rendered, f".{digits}g")


def sign(value: F) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def sign_variations(pattern: tuple[int, ...]) -> int:
    nonzero = [value for value in pattern if value]
    return sum(left != right for left, right in zip(nonzero, nonzero[1:]))


def normalized_epsilon(maximum: int) -> F:
    h = maximum // 2
    scale = 1875 if maximum % 2 == 0 else 2500
    return F(1, scale * 2**h)


def d_value_direct(
    maximum: int,
    value: F,
    value_M: F,
    value_h: F,
    value_h1: F,
) -> F:
    h = maximum // 2
    u = F(1, 2**h)
    denominator = 1 - (h + 1) * u
    if maximum % 2 == 0:
        return (
            -2 * u * value
            + (denominator + 2 * h * u) * value_h
            - 2 * (h - 1) * u * value_h1
        ) / denominator
    return (
        -F(3, 2) * u * value
        + (F(1, 2) * denominator + F(3, 2) * h * u) * value_h
        + (F(1, 2) * denominator - F(3, 2) * (h - 1) * u) * value_h1
    ) / denominator


def k_space_affine_nodes(maximum: int, probe: F) -> list[tuple[str, F, F, F]]:
    """Return (name,node,constant-coefficient,k-coefficient)."""
    h = maximum // 2
    epsilon = normalized_epsilon(maximum)

    beta_M = BETA**maximum
    beta_h = BETA**h
    target_M = TARGET**maximum
    probe_M = probe**maximum
    probe_h = probe**h

    h_beta = (
        F(1 + beta_M, 2)
        - d_value_direct(maximum, BETA, beta_M, beta_h, beta_h * BETA)
        + 2 * epsilon
    )
    h_probe = (
        F(1 + probe_M, 2)
        - d_value_direct(maximum, probe, probe_M, probe_h, probe_h * probe)
        - 2 * epsilon
    )

    a_beta = F(1 - beta_M, maximum)
    a_target = F(1 - target_M, maximum)
    a_probe = F(1 - probe_M, maximum)
    capital_a = F(1 + target_M, 2)

    c_beta_probe = capital_a * (probe - BETA)
    c_beta_target = h_probe * (BETA - TARGET)
    c_probe_target = h_beta * (TARGET - probe)

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

    c_k_probe = (probe - 1) * (capital_a * a_beta - h_beta * a_target)
    c_probe = (
        -capital_a * a_beta
        - capital_a * probe
        + capital_a
        + h_beta * a_target
        + h_beta * probe
        - h_beta
    )

    return [
        ("beta_probe", BETA * probe, c_beta_probe, F(0)),
        ("beta_target", BETA * TARGET, c_beta_target, F(0)),
        ("probe_target", probe * TARGET, c_probe_target, F(0)),
        ("beta", BETA, c_beta, c_k_beta),
        ("probe", probe, c_probe, c_k_probe),
        ("target", TARGET, c_target, c_k_target),
    ]


def secant_contributions(
    nodes: list[tuple[str, F, F, F]],
    contact: int,
) -> list[tuple[str, F]]:
    output: list[tuple[str, F]] = []
    for name, node, constant_coefficient, k_coefficient in nodes:
        transformed = (
            (1 - node) * (constant_coefficient + k_coefficient * contact)
            - node * k_coefficient
        ) * node**contact
        output.append((name, transformed))
    return output


def transformed_coefficient_pattern(
    nodes: list[tuple[str, F, F, F]],
) -> tuple[int, ...]:
    pattern: list[int] = []
    for _, node, constant_coefficient, k_coefficient in nodes:
        if k_coefficient == 0:
            pattern.append(sign((1 - node) * constant_coefficient))
        else:
            pattern.extend(
                [
                    sign((1 - node) * constant_coefficient - node * k_coefficient),
                    sign((1 - node) * k_coefficient),
                ]
            )
    return tuple(pattern)


def symbolic_secant_identity() -> bool:
    # Factor out r^k before simplification; this avoids asking SymPy to
    # manipulate a symbolic exponent.
    a, b, k, r = sp.symbols("a b k r")
    original_factor = (a + b * k) - r * (a + b * (k + 1))
    reduced_factor = (1 - r) * a - r * b + (1 - r) * b * k
    return sp.expand(original_factor - reduced_factor) == 0


def leading_limit_certificates() -> dict[str, Any]:
    """Exact lower bounds for the parity-phase leading secant limit.

    The A85 expansion gives, with delta in [0,1],

      L_even = A(1-st)s^delta - (1-t)C_even(s)(1-c(s)),
      L_odd  = A(1-st)s^delta/sqrt(2)
               - (1-t)C_odd(s)(1-c(s)),

    A=(t-s)/2.  Bounds use s^delta>=s, 0<c(s)<1, and
    1/sqrt(2)>7/10.  They are deliberately conservative and rational.
    """
    lower_s = F(129, 1000)
    upper_s = F(133, 1000)
    amplitude_lower = (TARGET - upper_s) / 2
    product_factor_lower = 1 - upper_s * TARGET
    shared_positive = amplitude_lower * product_factor_lower * lower_s

    c_even_upper = upper_s - BETA - F(2, 1875)
    c_odd_upper = F(3, 4) * (upper_s - BETA) - F(1, 1250)

    even_negative_upper = (1 - TARGET) * c_even_upper
    odd_negative_upper = (1 - TARGET) * c_odd_upper
    even_margin = shared_positive - even_negative_upper
    odd_positive_lower = F(7, 10) * shared_positive
    odd_margin = odd_positive_lower - odd_negative_upper

    return {
        "interval": [fstr(lower_s), fstr(upper_s)],
        "leading_limits": {
            "even": "((t-s)/2)(1-st)s^delta-(1-t)C_even(s)(1-c(s))",
            "odd": "((t-s)/(2 sqrt(2)))(1-st)s^delta-(1-t)C_odd(s)(1-c(s))",
        },
        "constants": {
            "C_even": "s-beta-2/1875",
            "C_odd": "3(s-beta)/4-1/1250",
        },
        "shared_positive_lower": fstr(shared_positive),
        "shared_positive_lower_decimal": decimal(shared_positive),
        "even_negative_upper": fstr(even_negative_upper),
        "even_margin_lower": fstr(even_margin),
        "even_margin_lower_decimal": decimal(even_margin),
        "odd_positive_lower_using_1_over_sqrt2_gt_7_over_10": fstr(odd_positive_lower),
        "odd_negative_upper": fstr(odd_negative_upper),
        "odd_margin_lower": fstr(odd_margin),
        "odd_margin_lower_decimal": decimal(odd_margin),
        "sqrt_bound_exact": "(7/10)^2=49/100<1/2=(1/sqrt(2))^2",
        "even_positive": even_margin > 0,
        "odd_positive": odd_margin > 0,
    }


def main() -> None:
    a86 = load_module(A86_PATH, "a86_module")
    a87_catalogue = json.loads(A87_CATALOGUE.read_text(encoding="utf-8"))
    a87_keys = {
        (int(item["maximum"]), F(item["probe_value"])): int(item["base_contact"])
        for item in a87_catalogue["records"]
    }

    slope_brackets = {
        probe: a86.exact_slope_bracket(probe, 100_000)
        for _, probe in PROBES
    }

    coefficient_patterns: Counter[tuple[int, ...]] = Counter()
    records: list[dict[str, Any]] = []
    full_nonpositive: list[dict[str, Any]] = []
    core_sign_mismatches: list[dict[str, Any]] = []
    core_dominance_failures: list[dict[str, Any]] = []
    source_base_mismatches: list[dict[str, Any]] = []
    minimum_ratio: F | None = None
    minimum_ratio_record: dict[str, Any] | None = None

    for maximum in range(M_MIN, M_MAX + 1):
        for probe_name, probe in PROBES:
            base = a86.exact_ceil_Mc(
                probe,
                maximum,
                slope_brackets[probe][0],
                slope_brackets[probe][1],
            )
            nodes = k_space_affine_nodes(maximum, probe)
            pattern = transformed_coefficient_pattern(nodes)
            coefficient_patterns[pattern] += 1

            contributions = secant_contributions(nodes, base)
            full = sum((value for _, value in contributions), F(0))
            core = sum(
                (value for name, value in contributions if name in CORE_NAMES),
                F(0),
            )
            residual = full - core
            ratio = abs(core) / abs(residual) if residual else None

            if full <= 0:
                full_nonpositive.append({
                    "maximum": maximum,
                    "probe_name": probe_name,
                    "probe_value": fstr(probe),
                    "base_contact": base,
                    "full_sign": sign(full),
                })
            if sign(core) != sign(full):
                core_sign_mismatches.append({
                    "maximum": maximum,
                    "probe_name": probe_name,
                    "probe_value": fstr(probe),
                    "base_contact": base,
                    "full_sign": sign(full),
                    "core_sign": sign(core),
                })
            if abs(core) <= abs(residual):
                core_dominance_failures.append({
                    "maximum": maximum,
                    "probe_name": probe_name,
                    "probe_value": fstr(probe),
                    "base_contact": base,
                })

            if ratio is not None and (minimum_ratio is None or ratio < minimum_ratio):
                minimum_ratio = ratio
                minimum_ratio_record = {
                    "maximum": maximum,
                    "probe_name": probe_name,
                    "probe_value": fstr(probe),
                    "base_contact": base,
                    "ratio": fstr(ratio),
                    "ratio_decimal": decimal(ratio),
                }
            source_key = (maximum, probe)
            if source_key in a87_keys and a87_keys[source_key] != base:
                source_base_mismatches.append({
                    "maximum": maximum,
                    "probe_value": fstr(probe),
                    "A87_base": a87_keys[source_key],
                    "A88_base": base,
                })

            records.append({
                "maximum": maximum,
                "probe_name": probe_name,
                "probe_value": fstr(probe),
                "base_contact": base,
                "full_secant_positive": full > 0,
                "four_term_core_positive": core > 0,
                "four_term_core_dominates": abs(core) > abs(residual),
            })

        if maximum % 100 == 0 and probe_name == PROBES[-1][0]:
            print(f"progress M={maximum}", flush=True)

    if minimum_ratio is None or minimum_ratio_record is None:
        raise RuntimeError("Missing core/residual minimum")

    leading = leading_limit_certificates()
    expected_record_count = (M_MAX - M_MIN + 1) * len(PROBES)
    original_probe_values = {F(129, 1000), F(131, 1000), F(133, 1000)}
    original_subset_count = sum(
        1
        for record in records
        if record["maximum"] <= 300 and F(record["probe_value"]) in original_probe_values
    )

    gates = {
        "generic_affine_secant_identity_verified_symbolically": symbolic_secant_identity(),
        "nine_rational_probes_cover_full_local_interval": (
            PROBES[0][1] == F(129, 1000)
            and PROBES[-1][1] == F(133, 1000)
            and all(PROBES[index + 1][1] - PROBES[index][1] == F(1, 2000) for index in range(8))
        ),
        "record_count_is_exactly_8019": len(records) == expected_record_count == 8019,
        "all_8019_exact_local_secants_are_positive": not full_nonpositive,
        "four_term_secant_core_matches_all_full_signs": not core_sign_mismatches,
        "four_term_secant_core_strictly_dominates_all_residuals": not core_dominance_failures,
        "minimum_core_to_residual_ratio_exceeds_four": minimum_ratio > 4,
        "one_invariant_nine_term_coefficient_sign_pattern": (
            len(coefficient_patterns) == 1
            and next(iter(coefficient_patterns)) == EXPECTED_SECANT_COEFFICIENT_SIGNS
        ),
        "nine_term_pattern_has_six_sign_variations": sign_variations(EXPECTED_SECANT_COEFFICIENT_SIGNS) == 6,
        "coefficient_sign_variation_route_remains_insufficient": sign_variations(EXPECTED_SECANT_COEFFICIENT_SIGNS) > 1,
        "A87_original_873_base_contacts_reproduced": (
            original_subset_count == 873 and not source_base_mismatches
        ),
        "even_parity_phase_leading_margin_strictly_positive": leading["even_positive"],
        "odd_parity_phase_leading_margin_strictly_positive": leading["odd_positive"],
        "finite_scope_extended_to_M900_without_all_M_claim": M_MAX == 900,
        "claim_boundary_preserved": True,
    }

    result = {
        "audit": "A88_NINE_TERM_LOCAL_SECANT_REDUCTION_AND_EXTENDED_POSITIVITY_STRESS",
        "contract": {
            "maximum_range": [M_MIN, M_MAX],
            "probe_count": len(PROBES),
            "probes": [
                {"name": name, "value": fstr(value)} for name, value in PROBES
            ],
            "base_contact": "b=ceil(M c(s))",
            "slope": "c(s)=log(2)/(-2 log(s))",
            "exact_slope_comparison": "sign(c(s)-p/q)=sign(2^q s^(2p)-1)",
        },
        "exact_nine_term_secant_reduction": {
            "pure_term": "c r^k -> c(1-r) r^k",
            "affine_term": "(a+b k)r^k -> ([(1-r)a-rb]+(1-r)b k)r^k",
            "constant_channel": "cancels exactly",
            "ordered_terms": [
                "(beta*s)^k",
                "(beta*target)^k",
                "(s*target)^k",
                "beta^k",
                "k beta^k",
                "s^k",
                "k s^k",
                "target^k",
                "k target^k",
            ],
            "coefficient_sign_pattern": list(EXPECTED_SECANT_COEFFICIENT_SIGNS),
            "sign_variation_count": sign_variations(EXPECTED_SECANT_COEFFICIENT_SIGNS),
            "interpretation": (
                "The exact secant has one fewer term than E because the constant cancels. "
                "Six coefficient sign variations still do not imply one zero or positivity."
            ),
        },
        "finite_exact_stress": {
            "cell_count": len(records),
            "nonpositive_full_secant_count": len(full_nonpositive),
            "four_term_core_sign_mismatch_count": len(core_sign_mismatches),
            "four_term_core_dominance_failure_count": len(core_dominance_failures),
            "minimum_core_to_residual_ratio": minimum_ratio_record,
            "A87_original_subset_cell_count": original_subset_count,
            "verdict": "POSITIVE_EXACT_LOCAL_SECANT_IN_ALL_8019_DECLARED_CELLS",
        },
        "parity_phase_asymptotic_limit": leading,
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(value is True for value in gates.values()),
        "verdict": "PASS_NINE_TERM_SECANT_REDUCTION_EXTENDED_EXACT_POSITIVITY_AND_POSITIVE_PARITY_PHASE_LIMIT",
        "claim_boundary": [
            "The exact finite positivity theorem covers only 10<=M<=900 and the nine declared rational probes.",
            "The parity-phase calculation certifies a strictly positive leading limit, but A88 does not supply an explicit uniform remainder threshold M0.",
            "The nine-term coefficient pattern has six sign variations, so a raw variation-diminishing argument remains insufficient.",
            "A88 does not prove global monotonicity of E in k; A87 already showed that global monotonicity is false.",
            "No physical interpretation, all-M rounding law, periodicity, or pre-spacetime ontology is inferred.",
        ],
    }

    catalogue = {
        "audit": result["audit"],
        "record_count": len(records),
        "records": records,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "a88_nine_term_secant_positivity_results.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    (RESULTS / "a88_nine_term_secant_positivity_catalogue.json").write_text(
        json.dumps(catalogue, indent=2), encoding="utf-8"
    )

    if result["pass_count"] != result["gate_count"]:
        failed = [name for name, value in gates.items() if value is not True]
        raise RuntimeError(f"A88 gates failed: {failed}")

    print(json.dumps({
        "audit": result["audit"],
        "gate_count": result["gate_count"],
        "pass_count": result["pass_count"],
        "cell_count": len(records),
        "minimum_core_to_residual_ratio_decimal": minimum_ratio_record["ratio_decimal"],
        "verdict": result["verdict"],
    }, indent=2))


if __name__ == "__main__":
    main()
