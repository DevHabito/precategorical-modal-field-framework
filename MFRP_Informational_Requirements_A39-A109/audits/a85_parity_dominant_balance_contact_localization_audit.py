#!/usr/bin/env python3
"""A85 parity-resolved dominant balance and asymptotic contact localization.

A84 proved exact one-sign-variation at three rational probes through M=300,
but the ten-term k-space representation had seven raw coefficient sign
variations. A85 asks a narrower structural question: which terms actually
control the sign at the observed adjacent-contact transition?

The exact ten-term factor is split into:

    four-term core = (beta*target)^k + (s*target)^k
                     + target^k + k*target^k,

with the appropriate exact coefficients, plus a six-term residual. At the two
adjacent factors bracketing every A84 maximizer, exact rational arithmetic is
used to compare the core, residual, and full factor.

A second eight-term core drops only the fastest product node (beta*s)^k and the
constant term. It is included as a finite exact fallback when the four-term
balance is not yet dominant at very small support.

The analytic part derives parity-specific leading coefficients. For fixed
beta=1/8, target=1/2, normalized epsilon, and fixed s in the declared local
interval, write h=floor(M/2), u=2^{-h}. Then

    c_{k target} = C_p(s) u / M + o(u/M),
    c_target     = -(M-2) C_p(s) u / M + o(u),

where

    C_even(s) = s-beta-2/1875,
    C_odd(s)  = 3(s-beta)/4-1/1250.

After division by target^k, the positive (s*target)^k channel balances the
negative target-affine channel. The exponential rate equality gives

    k/M -> c(s) = log(2)/(-2 log(s)).

This is an asymptotic localization statement, not an all-M proof of unique
unimodality. The finite offset diagnostic is evaluated with 80-digit mpmath
arithmetic and is explicitly classified as numerical, while every dominance
and sign comparison is exact rational arithmetic.
"""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A84_PATH = HERE / "a84_k_space_exponential_polynomial_stress_audit.py"
A84_RESULT_PATH = RESULTS / "a84_k_space_exponential_polynomial_stress_results.json"

F = Fraction
M_MIN = 10
M_MAX = 300
ASYMPTOTIC_DIAGNOSTIC_MINIMUM = 13


def load_a84():
    specification = importlib.util.spec_from_file_location("a84_module", A84_PATH)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {A84_PATH}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpstr(value: mp.mpf, digits: int = 40) -> str:
    return mp.nstr(value, digits)


def sign(value: F) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def ratio_decimal(value: F, digits: int = 40) -> str:
    mp.mp.dps = max(80, digits + 20)
    return mpstr(mp.mpf(value.numerator) / value.denominator, digits)


def symbolic_parity_leading_gate() -> dict[str, bool]:
    """Verify the leading parity coefficients independently with SymPy."""
    u, maximum, k, s, beta = sp.symbols("u M k s beta", positive=True)
    target = sp.Rational(1, 2)

    c_even = s - beta - sp.Rational(2, 1875)
    c_odd = sp.Rational(3, 4) * (s - beta) - sp.Rational(1, 1250)

    checks: dict[str, bool] = {}
    for parity, h_beta_1, h_s_1, expected in (
        (
            "even",
            2 * beta + sp.Rational(2, 1875),
            2 * s - sp.Rational(2, 1875),
            c_even,
        ),
        (
            "odd",
            sp.Rational(3, 2) * beta + sp.Rational(2, 2500),
            sp.Rational(3, 2) * s - sp.Rational(2, 2500),
            c_odd,
        ),
    ):
        h_beta = sp.Rational(1, 2) + u * h_beta_1
        h_s = sp.Rational(1, 2) + u * h_s_1
        a = 1 / maximum

        c_k_target = sp.expand((target - 1) * (h_beta * a - h_s * a))
        c_target = sp.expand(
            -h_beta * a
            - h_beta * target
            + h_beta
            + h_s * a
            + h_s * target
            - h_s
        )

        checks[f"{parity}_H_difference"] = (
            sp.simplify(h_s_1 - h_beta_1 - 2 * expected) == 0
        )
        checks[f"{parity}_k_target_leading"] = (
            sp.simplify(c_k_target - u * expected / maximum) == 0
        )
        checks[f"{parity}_target_leading"] = (
            sp.simplify(c_target + (maximum - 2) * u * expected / maximum) == 0
        )

    return checks


def term_vector(
    a84,
    maximum: int,
    contact: int,
    probe_value: F,
    coefficient_map: dict[str, F],
    power_cache: dict[str, list[F]],
) -> list[F]:
    return [
        coefficient_map["(beta*s)^k"] * power_cache["beta_probe"][contact],
        coefficient_map["(beta*target)^k"] * power_cache["beta_target"][contact],
        coefficient_map["(s*target)^k"] * power_cache["probe_target"][contact],
        coefficient_map["beta^k"] * power_cache["beta"][contact],
        coefficient_map["k*beta^k"] * contact * power_cache["beta"][contact],
        coefficient_map["s^k"] * power_cache["probe"][contact],
        coefficient_map["k*s^k"] * contact * power_cache["probe"][contact],
        coefficient_map["target^k"] * power_cache["target"][contact],
        coefficient_map["k*target^k"] * contact * power_cache["target"][contact],
        coefficient_map["1"],
    ]


def asymptotic_parameters(
    probe_value: F,
    parity: str,
) -> dict[str, mp.mpf]:
    mp.mp.dps = 100
    s = mp.mpf(probe_value.numerator) / probe_value.denominator
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
    return {
        "slope": slope,
        "amplitude": amplitude,
        "constant": constant,
        "offset": offset,
    }


def main() -> None:
    a84 = load_a84()
    a84_results = json.loads(A84_RESULT_PATH.read_text(encoding="utf-8"))
    support_records = {
        int(record["maximum"]): record
        for record in a84_results["support_records"]
    }

    symbolic_checks = symbolic_parity_leading_gate()

    exact_evaluation_count = 0
    four_term_sign_mismatches: list[dict[str, Any]] = []
    four_term_dominance_failures: list[dict[str, Any]] = []
    eight_term_sign_mismatches: list[dict[str, Any]] = []
    eight_term_dominance_failures: list[dict[str, Any]] = []

    minimum_four_ratio: F | None = None
    minimum_four_record: dict[str, Any] | None = None
    minimum_four_ratio_m13: F | None = None
    minimum_four_record_m13: dict[str, Any] | None = None
    minimum_eight_ratio: F | None = None
    minimum_eight_record: dict[str, Any] | None = None

    transition_records: list[dict[str, Any]] = []

    for maximum in range(M_MIN, M_MAX + 1):
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
                "probe": probe_powers,
                "current_probe": probe_powers,
                "beta_probe": a84.powers(a84.BETA * probe_value, maximum),
                "beta_target": a84.powers(a84.BETA * a84.TARGET, maximum),
                "probe_target": a84.powers(probe_value * a84.TARGET, maximum),
            }
            h_probe = a84.h_value(
                maximum,
                probe_value,
                probe_powers,
                epsilon,
            )
            coefficient_map = dict(
                a84.k_space_coefficients(
                    maximum,
                    probe_value,
                    power_cache,
                    h_beta,
                    h_probe,
                )
            )

            maximizing_contact = int(
                support_records[maximum]["maximizing_contact"][probe_name]
            )
            local_contacts = sorted({maximizing_contact - 1, maximizing_contact})
            local_record = {
                "maximum": maximum,
                "probe_name": probe_name,
                "probe_value": fstr(probe_value),
                "maximizing_contact": maximizing_contact,
                "bracketing_factors": [],
            }

            for contact in local_contacts:
                if not (2 <= contact < maximum // 2 - 1):
                    continue
                terms = term_vector(
                    a84,
                    maximum,
                    contact,
                    probe_value,
                    coefficient_map,
                    power_cache,
                )
                full = sum(terms, F(0))
                four_core = terms[1] + terms[2] + terms[7] + terms[8]
                four_residual = full - four_core
                eight_core = sum(terms[1:9], F(0))
                eight_residual = terms[0] + terms[9]

                exact_evaluation_count += 1
                four_ratio = abs(four_core) / abs(four_residual)
                eight_ratio = abs(eight_core) / abs(eight_residual)

                record = {
                    "maximum": maximum,
                    "probe_name": probe_name,
                    "probe_value": fstr(probe_value),
                    "contact": contact,
                    "full_sign": sign(full),
                    "four_core_sign": sign(four_core),
                    "eight_core_sign": sign(eight_core),
                    "four_core_to_residual_ratio": ratio_decimal(four_ratio, 30),
                    "eight_core_to_residual_ratio": ratio_decimal(eight_ratio, 30),
                }
                local_record["bracketing_factors"].append(record)

                if sign(four_core) != sign(full):
                    four_term_sign_mismatches.append(record)
                if abs(four_core) <= abs(four_residual):
                    four_term_dominance_failures.append(record)
                if sign(eight_core) != sign(full):
                    eight_term_sign_mismatches.append(record)
                if abs(eight_core) <= abs(eight_residual):
                    eight_term_dominance_failures.append(record)

                if minimum_four_ratio is None or four_ratio < minimum_four_ratio:
                    minimum_four_ratio = four_ratio
                    minimum_four_record = record
                if maximum >= 13 and (
                    minimum_four_ratio_m13 is None
                    or four_ratio < minimum_four_ratio_m13
                ):
                    minimum_four_ratio_m13 = four_ratio
                    minimum_four_record_m13 = record
                if minimum_eight_ratio is None or eight_ratio < minimum_eight_ratio:
                    minimum_eight_ratio = eight_ratio
                    minimum_eight_record = record

            transition_records.append(local_record)

    # High-precision diagnostic for the parity-corrected asymptotic location.
    # This is deliberately not called an exact certificate.
    predictor_records: list[dict[str, Any]] = []
    predictor_count = 0
    predictor_within_one_count = 0
    worst_by_probe: dict[str, dict[str, Any]] = {}

    for probe_name, probe_value in a84.PROBES:
        even_parameters = asymptotic_parameters(probe_value, "even")
        odd_parameters = asymptotic_parameters(probe_value, "odd")
        worst: dict[str, Any] | None = None

        for maximum in range(ASYMPTOTIC_DIAGNOSTIC_MINIMUM, M_MAX + 1):
            parameters = even_parameters if maximum % 2 == 0 else odd_parameters
            predicted = (
                parameters["slope"] * maximum + parameters["offset"]
            )
            selected = int(
                support_records[maximum]["maximizing_contact"][probe_name]
            )
            signed_error = mp.mpf(selected) - predicted
            absolute_error = abs(signed_error)
            predictor_count += 1
            predictor_within_one_count += int(absolute_error < 1)

            candidate = {
                "maximum": maximum,
                "probe_name": probe_name,
                "selected_contact": selected,
                "predicted_continuous_contact": mpstr(predicted, 35),
                "signed_error": mpstr(signed_error, 35),
                "absolute_error": mpstr(absolute_error, 35),
                "parity": "even" if maximum % 2 == 0 else "odd",
            }
            if worst is None or absolute_error > mp.mpf(worst["absolute_error"]):
                worst = candidate

        if worst is None:
            raise RuntimeError("No predictor records")
        worst_by_probe[probe_name] = worst
        predictor_records.append({
            "probe_name": probe_name,
            "probe_value": fstr(probe_value),
            "slope": mpstr(even_parameters["slope"], 40),
            "even_leading_constant": mpstr(even_parameters["constant"], 40),
            "odd_leading_constant": mpstr(odd_parameters["constant"], 40),
            "even_offset": mpstr(even_parameters["offset"], 40),
            "odd_offset": mpstr(odd_parameters["offset"], 40),
            "worst_error_M13_M300": worst,
        })

    if minimum_four_ratio is None or minimum_four_ratio_m13 is None or minimum_eight_ratio is None:
        raise RuntimeError("Missing dominance minima")

    gates = {
        "all_symbolic_parity_leading_coefficients_verified": all(symbolic_checks.values()),
        "transition_bracket_evaluation_count_exact": exact_evaluation_count == 1746,
        "four_term_core_has_exactly_one_sign_mismatch": (
            len(four_term_sign_mismatches) == 1
            and four_term_sign_mismatches[0]["maximum"] == 12
            and four_term_sign_mismatches[0]["probe_name"] == "local_lower"
            and four_term_sign_mismatches[0]["contact"] == 3
        ),
        "four_term_core_has_exactly_two_dominance_failures": (
            len(four_term_dominance_failures) == 2
            and {(item["maximum"], item["probe_name"], item["contact"])
                 for item in four_term_dominance_failures}
            == {(12, "local_lower", 3), (12, "probe", 3)}
        ),
        "four_term_core_dominates_all_transition_brackets_from_M13": minimum_four_ratio_m13 > 1,
        "eight_term_core_matches_every_full_sign": len(eight_term_sign_mismatches) == 0,
        "eight_term_core_strictly_dominates_every_transition_bracket": (
            len(eight_term_dominance_failures) == 0 and minimum_eight_ratio > 1
        ),
        "asymptotic_leading_constants_positive_on_all_three_probes": all(
            mp.mpf(record["even_leading_constant"]) > 0
            and mp.mpf(record["odd_leading_constant"]) > 0
            for record in predictor_records
        ),
        "parity_corrected_predictor_count_exact": predictor_count == 864,
        "parity_corrected_predictor_within_one_contact_for_M13_M300": predictor_within_one_count == 864,
        "A84_maximizer_records_complete": len(support_records) == 291,
        "scope_and_nonclaim_boundary_preserved": (
            M_MIN == 10
            and M_MAX == 300
            and ASYMPTOTIC_DIAGNOSTIC_MINIMUM == 13
            and tuple(value for _, value in a84.PROBES)
            == (F(129, 1000), F(131, 1000), F(133, 1000))
        ),
    }

    summary = {
        "audit": "A85_PARITY_DOMINANT_BALANCE_AND_ASYMPTOTIC_CONTACT_LOCALIZATION",
        "contract": {
            "maximum_range": [M_MIN, M_MAX],
            "exact_transition_bracket_probes": [
                {"name": name, "value": fstr(value)} for name, value in a84.PROBES
            ],
            "beta": fstr(a84.BETA),
            "target": fstr(a84.TARGET),
            "epsilon": "parity-normalized A67-A84 contract",
            "transition_contacts": "the two adjacent factors k*-1 and k* bracketing each A84 compressed maximizer",
        },
        "analytic_result": {
            "four_term_core": [
                "(beta*target)^k",
                "(s*target)^k",
                "target^k",
                "k*target^k",
            ],
            "parity_leading_constants": {
                "even": "C_even(s)=s-beta-2/1875",
                "odd": "C_odd(s)=3(s-beta)/4-1/1250",
            },
            "leading_target_coefficients": [
                "c_(k target)=C_p(s) 2^{-floor(M/2)}/M + o(2^{-floor(M/2)}/M)",
                "c_target=-(M-2) C_p(s) 2^{-floor(M/2)}/M + o(2^{-floor(M/2)})",
            ],
            "asymptotic_slope": "c(s)=log(2)/(-2 log(s))",
            "asymptotic_statement": (
                "For fixed s with positive parity constant, factors sampled at k/M below c(s) are eventually positive and factors sampled above c(s) are eventually negative. Any asymptotic sign-transition sequence therefore satisfies k/M -> c(s)."
            ),
            "parity_offset_formula": {
                "even": "d_even=log(C_even(s)(1-c(s))/((1/2-s)/2))/log(s)",
                "odd": "d_odd=log(sqrt(2) C_odd(s)(1-c(s))/((1/2-s)/2))/log(s)",
            },
            "symbolic_checks": symbolic_checks,
        },
        "finite_exact_transition_balance": {
            "exact_evaluation_count": exact_evaluation_count,
            "four_term_sign_mismatch_count": len(four_term_sign_mismatches),
            "four_term_sign_mismatches": four_term_sign_mismatches,
            "four_term_dominance_failure_count": len(four_term_dominance_failures),
            "four_term_dominance_failures": four_term_dominance_failures,
            "minimum_four_core_to_residual_ratio_all_M": {
                "exact": fstr(minimum_four_ratio),
                "decimal": ratio_decimal(minimum_four_ratio, 40),
                "record": minimum_four_record,
            },
            "minimum_four_core_to_residual_ratio_M13_M300": {
                "exact": fstr(minimum_four_ratio_m13),
                "decimal": ratio_decimal(minimum_four_ratio_m13, 40),
                "record": minimum_four_record_m13,
            },
            "eight_term_sign_mismatch_count": len(eight_term_sign_mismatches),
            "eight_term_dominance_failure_count": len(eight_term_dominance_failures),
            "minimum_eight_core_to_residual_ratio": {
                "exact": fstr(minimum_eight_ratio),
                "decimal": ratio_decimal(minimum_eight_ratio, 40),
                "record": minimum_eight_record,
            },
            "verdict": (
                "FOUR_TERM_CORE_EXACT_FROM_M13_AT_ALL_A84_TRANSITION_BRACKETS_WITH_ONE_SMALL_SUPPORT_COUNTEREXAMPLE; EIGHT_TERM_FALLBACK_EXACT_EVERYWHERE"
            ),
        },
        "high_precision_asymptotic_diagnostic": {
            "evidence_class": "80-digit numerical diagnostic, not an interval or rational theorem",
            "minimum_M": ASYMPTOTIC_DIAGNOSTIC_MINIMUM,
            "maximum_M": M_MAX,
            "record_count": predictor_count,
            "within_one_contact_count": predictor_within_one_count,
            "probe_parameters": predictor_records,
            "interpretation": (
                "The parity-corrected continuous predictor stays within one integer contact of every exact A84 maximizer for M=13,...,300 at all three probes. This supports the derived asymptotic balance but is not used as a proof of the all-M statement."
            ),
        },
        "transition_records": transition_records,
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": (
            "PASS_PARITY_DOMINANT_BALANCE_AND_ASYMPTOTIC_CONTACT_LOCALIZATION"
            if all(gates.values())
            else "FAIL"
        ),
        "claim_boundary": [
            "The parity-leading expansion and asymptotic slope are analytic statements under the declared reduced contract.",
            "The exact four-term dominance theorem is finite and local to the two factors bracketing the A84 maximizer; it is not asserted for every adjacent contact.",
            "M=12 supplies an explicit counterexample to universal four-term dominance from the smallest audited supports.",
            "The eight-term fallback is exact at all 1,746 audited transition-bracket factors but is a finite certificate, not an asymptotic theorem.",
            "The offset-within-one result uses high-precision numerical logarithms and is reported as a diagnostic, not a formal interval certificate.",
            "No unique all-M unimodality theorem, periodic block law, physical interpretation, or claim beyond the declared model is inferred.",
        ],
    }

    compact = {
        "audit": "A85_TRANSITION_DOMINANT_BALANCE_CATALOGUE",
        "contract": summary["contract"],
        "transition_records": transition_records,
        "four_term_failures": {
            "sign": four_term_sign_mismatches,
            "dominance": four_term_dominance_failures,
        },
        "predictor_parameters": predictor_records,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "a85_parity_dominant_balance_contact_localization_results.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    (RESULTS / "a85_transition_dominant_balance_catalogue.json").write_text(
        json.dumps(compact, indent=2), encoding="utf-8"
    )

    print(json.dumps({
        "verdict": summary["verdict"],
        "gate_count": summary["gate_count"],
        "pass_count": summary["pass_count"],
        "exact_transition_evaluations": exact_evaluation_count,
        "four_term_sign_mismatches": len(four_term_sign_mismatches),
        "four_term_dominance_failures": len(four_term_dominance_failures),
        "eight_term_sign_mismatches": len(eight_term_sign_mismatches),
        "predictor_within_one": f"{predictor_within_one_count}/{predictor_count}",
    }, indent=2))


if __name__ == "__main__":
    main()
