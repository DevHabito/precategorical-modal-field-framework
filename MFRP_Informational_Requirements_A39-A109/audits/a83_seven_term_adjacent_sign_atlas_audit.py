#!/usr/bin/env python3
"""A83 exact seven-term adjacent-difference factorization and local sign atlas.

A82 proved strict unimodality of the compressed objective at the rational
probe s0=131/1000, but its adjacent objective differences were represented as
cross-products of degree 2M. A83 derives a sparse factorization

    numerator(V_{M,k+1}-V_{M,k}) = Z_M(s) E_{M,k}(s),

where Z_M is the common positive interior-mass numerator and E_{M,k} has
exactly seven monomials with exponents

    {M, h+1, h, k+1, k, 1, 0},  h=floor(M/2).

The finite audit covers 10<=M<=80 and 2<=k<h-1 on
I=[129/1000,133/1000]. It certifies a complete local sign atlas for all 1,367
adjacent differences: 1,365 are sign-definite on I and exactly two have one
simple root. Consequently the compressed objective is strictly unimodal for
every support away from those roots, with a two-contact plateau at each root.

A83 also tests, rather than assumes, a discrete-concavity explanation. That
route fails beyond M=15: among 1,296 exact second differences at s0, 1,141 are
positive and 155 are negative. The correct finite mechanism is one sign
variation in the adjacent-difference sequence, not global discrete concavity.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A80_SCRIPT = HERE / "a80_local_compression_window_atlas_audit.py"
A81_SCRIPT = HERE / "a81_reduced_boundary_system_audit.py"
A82_SCRIPT = HERE / "a82_adjacent_contact_locator_audit.py"
A82_RESULT = RESULTS / "a82_adjacent_contact_locator_results.json"

S = sp.Symbol("s")
S0 = sp.Rational(131, 1000)
LOCAL_LOWER = sp.Rational(129, 1000)
LOCAL_UPPER = sp.Rational(133, 1000)
BETA = sp.Rational(1, 8)
TARGET = sp.Rational(1, 2)
M_MIN = 10
M_MAX = 80
BISECTION_STEPS = 100
EXPECTED_FEASIBILITY_EXCEPTIONS = [23, 28, 34, 45, 51, 56, 62, 68]
EXPECTED_CROSSINGS = {
    (28, 6): (1, -1),
    (79, 15): (-1, 1),
}


@dataclass(frozen=True)
class RootBracket:
    lower: sp.Rational
    upper: sp.Rational

    @property
    def midpoint(self) -> sp.Rational:
        return (self.lower + self.upper) / 2


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


def normalize_coefficients(
    coefficients: dict[int, sp.Rational],
) -> dict[int, sp.Rational]:
    return {
        int(exponent): sp.cancel(coefficient)
        for exponent, coefficient in coefficients.items()
        if coefficient != 0
    }


def add_scaled(
    target: dict[int, sp.Rational],
    source: dict[int, sp.Rational],
    scale: sp.Rational,
) -> None:
    for exponent, coefficient in source.items():
        target[exponent] = sp.cancel(
            target.get(exponent, sp.Rational(0)) + scale * coefficient
        )
    for exponent in [key for key, value in target.items() if value == 0]:
        del target[exponent]


def multiply_coefficients(
    left: dict[int, sp.Rational],
    right: dict[int, sp.Rational],
) -> dict[int, sp.Rational]:
    output: dict[int, sp.Rational] = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            output[exponent] = sp.cancel(
                output.get(exponent, sp.Rational(0))
                + left_coefficient * right_coefficient
            )
    return normalize_coefficients(output)


def evaluate_coefficients(
    coefficients: dict[int, sp.Rational],
    point: sp.Rational | sp.Symbol,
) -> sp.Expr:
    return sp.cancel(sum(
        coefficient * point**exponent
        for exponent, coefficient in coefficients.items()
    ))


def sign_preserving_integer_polynomial(
    coefficients: dict[int, sp.Rational],
) -> sp.Poly:
    rational = sp.Poly(evaluate_coefficients(coefficients, S), S, domain=sp.QQ)
    _, integer_polynomial = rational.clear_denoms(convert=True)
    content, primitive_expression = sp.primitive(integer_polynomial.as_expr(), S)
    if content < 0:
        primitive_expression = -primitive_expression
    return sp.Poly(primitive_expression, S, domain=sp.ZZ)


def coefficient_hash(polynomial: sp.Poly) -> str:
    canonical = json.dumps(
        [str(value) for value in polynomial.all_coeffs()],
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def polynomial_record(polynomial: sp.Poly) -> dict[str, Any]:
    nonzero = {
        str(exponents[0]): str(coefficient)
        for exponents, coefficient in polynomial.terms()
        if coefficient != 0
    }
    return {
        "degree": polynomial.degree(),
        "term_count": len(nonzero),
        "nonzero_coefficients_by_exponent": nonzero,
        "coefficient_sha256": coefficient_hash(polynomial),
    }


def exact_bisection_root(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
) -> RootBracket:
    lower_sign = int(sp.sign(polynomial.eval(lower)))
    upper_sign = int(sp.sign(polynomial.eval(upper)))
    if lower_sign == 0 or upper_sign == 0 or lower_sign == upper_sign:
        raise RuntimeError("Bisection requires opposite nonzero endpoint signs")
    for _ in range(BISECTION_STEPS):
        midpoint = (lower + upper) / 2
        midpoint_sign = int(sp.sign(polynomial.eval(midpoint)))
        if midpoint_sign == 0:
            return RootBracket(midpoint, midpoint)
        if midpoint_sign == lower_sign:
            lower = midpoint
        else:
            upper = midpoint
    return RootBracket(lower, upper)


def bracket_record(bracket: RootBracket) -> dict[str, Any]:
    return {
        "lower": str(bracket.lower),
        "upper": str(bracket.upper),
        "width": str(bracket.upper - bracket.lower),
        "midpoint_decimal": f"{float(bracket.midpoint):.18f}",
    }


def adjacent_sparse_factor(a81, maximum: int, contact: int) -> dict[str, Any]:
    """Return E_{M,k}=X deltaB+Y B+W H and its exact seven coefficients."""
    system = a81.reduced_system(maximum, contact)
    B = system["B"]
    H = system["H"]
    H_beta = system["H_beta"]

    delta_B = {
        contact + 1: sp.Rational(1),
        contact: sp.Rational(-1),
        0: sp.Rational(1, maximum),
        maximum: sp.Rational(-1, maximum),
    }
    B_beta = evaluate_coefficients(B, BETA)
    B_target = evaluate_coefficients(B, TARGET)
    delta_beta = evaluate_coefficients(delta_B, BETA)
    delta_target = evaluate_coefficients(delta_B, TARGET)
    A_target = sp.cancel((1 + TARGET**maximum) / 2)

    X = sp.cancel(A_target * B_beta - H_beta * B_target)
    Y = sp.cancel(-A_target * delta_beta + H_beta * delta_target)
    W = sp.cancel(-B_beta * delta_target + B_target * delta_beta)

    coefficients: dict[int, sp.Rational] = {}
    add_scaled(coefficients, delta_B, X)
    add_scaled(coefficients, B, Y)
    add_scaled(coefficients, H, W)
    coefficients = normalize_coefficients(coefficients)

    expected_exponents = {
        maximum,
        maximum // 2 + 1,
        maximum // 2,
        contact + 1,
        contact,
        1,
        0,
    }
    explicit_coefficients = {
        maximum: sp.cancel(-X / maximum - sp.Rational(contact, maximum) * Y + W / 2),
        maximum // 2 + 1: sp.cancel(W * H[maximum // 2 + 1]),
        maximum // 2: sp.cancel(W * H[maximum // 2]),
        contact + 1: X,
        contact: sp.cancel(-X + Y),
        1: sp.cancel(W * H[1]),
        0: sp.cancel(
            X / maximum
            - sp.Rational(maximum - contact, maximum) * Y
            + W * H[0]
        ),
    }
    explicit_coefficients = normalize_coefficients(explicit_coefficients)

    return {
        "system": system,
        "delta_B": delta_B,
        "X": X,
        "Y": Y,
        "W": W,
        "coefficients": coefficients,
        "explicit_coefficients": explicit_coefficients,
        "expected_exponents": expected_exponents,
    }


def main() -> None:
    for required in (A80_SCRIPT, A81_SCRIPT, A82_SCRIPT, A82_RESULT):
        if not required.exists():
            raise FileNotFoundError(required)

    a80 = load_module(A80_SCRIPT, "a80_for_a83")
    a81 = load_module(A81_SCRIPT, "a81_for_a83")
    a82 = load_module(A82_SCRIPT, "a82_for_a83")
    a82_data = json.loads(A82_RESULT.read_text(encoding="utf-8"))

    sparse_records: list[dict[str, Any]] = []
    support_records: list[dict[str, Any]] = []
    root_records: list[dict[str, Any]] = []

    adjacent_count = 0
    exact_factorization_count = 0
    exact_explicit_formula_count = 0
    exact_seven_term_count = 0
    common_z_positive_count = 0
    fixed_sign_count = 0
    crossing_count = 0
    complete_root_atlas_count = 0
    lower_unimodal_count = 0
    probe_unimodal_count = 0
    upper_unimodal_count = 0
    second_difference_positive_count = 0
    second_difference_negative_count = 0
    second_difference_zero_count = 0
    fully_discrete_concave_supports: list[int] = []

    for maximum in range(M_MIN, M_MAX + 1):
        h = maximum // 2
        contacts = list(range(2, h))
        adjacent_contacts = contacts[:-1]

        # Z_M is contact-independent. Certify its positive sign once per M.
        common_system = a81.reduced_system(maximum, contacts[0])
        z_coefficients = common_system["z_numerator_coefficients"]
        z_polynomial = sp.Poly(
            evaluate_coefficients(z_coefficients, S), S, domain=sp.QQ
        )
        z_certificate = a80.certify_polynomial_fixed_sign(
            z_polynomial, LOCAL_LOWER, LOCAL_UPPER, maximum_depth=16
        )
        common_z_positive = bool(
            z_certificate["pass"] and z_certificate["sign"] == 1
        )
        common_z_positive_count += int(common_z_positive)

        endpoint_sign_sequences: dict[str, list[int]] = {
            "local_lower": [],
            "s0": [],
            "local_upper": [],
        }
        endpoint_values: dict[str, list[sp.Rational]] = {
            "local_lower": [],
            "s0": [],
            "local_upper": [],
        }
        for point_name, point in (
            ("local_lower", LOCAL_LOWER),
            ("s0", S0),
            ("local_upper", LOCAL_UPPER),
        ):
            endpoint_values[point_name] = [
                a82.reduced_point_values(maximum, contact, point)["value"]
                for contact in contacts
            ]

        for contact in adjacent_contacts:
            adjacent_count += 1
            lower_parts = a82.objective_parts(a81, maximum, contact)
            upper_parts = a82.objective_parts(a81, maximum, contact + 1)
            cross_coefficients = a82.adjacent_difference_coefficients(
                lower_parts, upper_parts
            )
            factor = adjacent_sparse_factor(a81, maximum, contact)
            reconstructed = multiply_coefficients(
                z_coefficients, factor["coefficients"]
            )
            factorization_ok = reconstructed == normalize_coefficients(cross_coefficients)
            exact_factorization_count += int(factorization_ok)

            explicit_ok = factor["coefficients"] == factor["explicit_coefficients"]
            exact_explicit_formula_count += int(explicit_ok)
            seven_term_ok = bool(
                len(factor["coefficients"]) == 7
                and set(factor["coefficients"]) == factor["expected_exponents"]
                and all(value != 0 for value in factor["coefficients"].values())
            )
            exact_seven_term_count += int(seven_term_ok)

            sign_polynomial = sp.Poly(
                evaluate_coefficients(factor["coefficients"], S),
                S,
                domain=sp.QQ,
            )
            endpoint_signs = {
                "local_lower": int(sp.sign(sign_polynomial.eval(LOCAL_LOWER))),
                "s0": int(sp.sign(sign_polynomial.eval(S0))),
                "local_upper": int(sp.sign(sign_polynomial.eval(LOCAL_UPPER))),
            }
            for point_name in endpoint_sign_sequences:
                endpoint_sign_sequences[point_name].append(endpoint_signs[point_name])

            primitive = sign_preserving_integer_polynomial(factor["coefficients"])
            root_class: str
            certificate: dict[str, Any]
            if endpoint_signs["local_lower"] == endpoint_signs["local_upper"]:
                fixed_certificate = a80.certify_polynomial_fixed_sign(
                    sign_polynomial,
                    LOCAL_LOWER,
                    LOCAL_UPPER,
                    maximum_depth=16,
                )
                fixed_ok = bool(
                    fixed_certificate["pass"]
                    and fixed_certificate["sign"]
                    == endpoint_signs["local_lower"]
                )
                fixed_sign_count += int(fixed_ok)
                complete_root_atlas_count += int(fixed_ok)
                root_class = "sign_definite_no_root"
                certificate = {
                    "fixed_sign": fixed_certificate,
                    "complete_on_interval": fixed_ok,
                }
            else:
                crossing_count += 1
                bracket = exact_bisection_root(
                    sign_polynomial, LOCAL_LOWER, LOCAL_UPPER
                )
                # Use a wider rational monotonicity neighborhood around the
                # isolated root. Certifying fixed sign on intervals that end
                # within 2^-100 of a root is needlessly ill-conditioned for
                # interval Horner bounds; the wider neighborhood gives an
                # exact one-root proof without that numerical pathology.
                neighborhood_radius = sp.Rational(1, 10000)
                neighborhood_lower = bracket.midpoint - neighborhood_radius
                neighborhood_upper = bracket.midpoint + neighborhood_radius
                if not (LOCAL_LOWER < neighborhood_lower < bracket.lower):
                    raise RuntimeError("Invalid lower monotonicity neighborhood")
                if not (bracket.upper < neighborhood_upper < LOCAL_UPPER):
                    raise RuntimeError("Invalid upper monotonicity neighborhood")
                derivative_certificate = a80.certify_polynomial_fixed_sign(
                    sign_polynomial.diff(),
                    neighborhood_lower,
                    neighborhood_upper,
                    maximum_depth=16,
                )
                left_certificate = a80.certify_polynomial_fixed_sign(
                    sign_polynomial,
                    LOCAL_LOWER,
                    neighborhood_lower,
                    maximum_depth=18,
                )
                right_certificate = a80.certify_polynomial_fixed_sign(
                    sign_polynomial,
                    neighborhood_upper,
                    LOCAL_UPPER,
                    maximum_depth=18,
                )
                neighborhood_endpoint_signs = (
                    int(sp.sign(sign_polynomial.eval(neighborhood_lower))),
                    int(sp.sign(sign_polynomial.eval(neighborhood_upper))),
                )
                complete = bool(
                    derivative_certificate["pass"]
                    and derivative_certificate["sign"] != 0
                    and neighborhood_endpoint_signs[0]
                    == endpoint_signs["local_lower"]
                    and neighborhood_endpoint_signs[1]
                    == endpoint_signs["local_upper"]
                    and left_certificate["pass"]
                    and right_certificate["pass"]
                    and left_certificate["sign"] == endpoint_signs["local_lower"]
                    and right_certificate["sign"] == endpoint_signs["local_upper"]
                )
                complete_root_atlas_count += int(complete)
                root_class = "one_simple_root"
                certificate = {
                    "root_bracket": bracket_record(bracket),
                    "monotonicity_neighborhood": {
                        "lower": str(neighborhood_lower),
                        "upper": str(neighborhood_upper),
                        "endpoint_signs": list(neighborhood_endpoint_signs),
                    },
                    "derivative_nonzero_on_monotonicity_neighborhood": derivative_certificate,
                    "left_fixed_sign": left_certificate,
                    "right_fixed_sign": right_certificate,
                    "complete_on_interval": complete,
                }
                root_records.append({
                    "maximum": maximum,
                    "lower_contact": contact,
                    "upper_contact": contact + 1,
                    "endpoint_signs": endpoint_signs,
                    "root_bracket": bracket_record(bracket),
                    "polynomial": polynomial_record(primitive),
                    "certificate": certificate,
                })

            sparse_records.append({
                "maximum": maximum,
                "lower_contact": contact,
                "upper_contact": contact + 1,
                "expected_exponents": sorted(factor["expected_exponents"], reverse=True),
                "cofactors": {
                    "X": str(factor["X"]),
                    "Y": str(factor["Y"]),
                    "W": str(factor["W"]),
                },
                "polynomial": polynomial_record(primitive),
                "endpoint_signs": endpoint_signs,
                "root_class": root_class,
                "certificate": certificate,
                "exact_factorization_reconstructed": factorization_ok,
                "explicit_seven_coefficient_formula_reconstructed": explicit_ok,
            })

        def strict_single_variation(signs: list[int]) -> bool:
            transitions = sum(
                signs[index] != signs[index + 1]
                for index in range(len(signs) - 1)
            )
            return bool(
                signs
                and 0 not in signs
                and signs[0] == 1
                and signs[-1] == -1
                and transitions == 1
            )

        lower_unimodal = strict_single_variation(
            endpoint_sign_sequences["local_lower"]
        )
        probe_unimodal = strict_single_variation(endpoint_sign_sequences["s0"])
        upper_unimodal = strict_single_variation(
            endpoint_sign_sequences["local_upper"]
        )
        lower_unimodal_count += int(lower_unimodal)
        probe_unimodal_count += int(probe_unimodal)
        upper_unimodal_count += int(upper_unimodal)

        # Test the stronger discrete-concavity route at the exact probe.
        probe_values = endpoint_values["s0"]
        first_differences = [
            sp.cancel(probe_values[index + 1] - probe_values[index])
            for index in range(len(probe_values) - 1)
        ]
        second_differences = [
            sp.cancel(first_differences[index + 1] - first_differences[index])
            for index in range(len(first_differences) - 1)
        ]
        second_signs = [int(sp.sign(value)) for value in second_differences]
        current_positive = second_signs.count(1)
        current_negative = second_signs.count(-1)
        current_zero = second_signs.count(0)
        second_difference_positive_count += current_positive
        second_difference_negative_count += current_negative
        second_difference_zero_count += current_zero
        if current_positive == 0 and current_zero == 0:
            fully_discrete_concave_supports.append(maximum)

        def maximizing_contact(values: list[sp.Rational]) -> int:
            index = max(range(len(values)), key=lambda position: values[position])
            return contacts[index]

        support_records.append({
            "maximum": maximum,
            "adjacent_count": len(adjacent_contacts),
            "common_z_positive_on_local_interval": common_z_positive,
            "sign_sequences": endpoint_sign_sequences,
            "strict_unimodality": {
                "local_lower": lower_unimodal,
                "s0": probe_unimodal,
                "local_upper": upper_unimodal,
            },
            "maximizing_contact": {
                point_name: maximizing_contact(values)
                for point_name, values in endpoint_values.items()
            },
            "probe_second_difference_census": {
                "negative": current_negative,
                "positive": current_positive,
                "zero": current_zero,
                "strictly_discrete_concave": current_positive == 0 and current_zero == 0,
            },
        })

    root_pairs = [
        (record["maximum"], record["lower_contact"])
        for record in root_records
    ]
    root_signs = {
        (record["maximum"], record["lower_contact"]): (
            record["endpoint_signs"]["local_lower"],
            record["endpoint_signs"]["local_upper"],
        )
        for record in root_records
    }
    root_records_sorted = sorted(
        root_records,
        key=lambda item: sp.Rational(item["root_bracket"]["lower"]),
    )

    # A82's eight feasibility exceptions remain; the sparse sign law locates
    # the algebraic maximizer but does not replace full KKT feasibility.
    a82_exceptions = [
        int(item["maximum"])
        for item in a82_data["probe_theorem"][
            "compressed_maximizer_primal_feasibility_exceptions"
        ]
    ]

    gates = {
        "adjacent_pair_count_exact": adjacent_count == 1367,
        "all_cross_numerators_factor_exactly": exact_factorization_count == adjacent_count,
        "all_explicit_seven_coefficient_formulas_match": exact_explicit_formula_count == adjacent_count,
        "all_sparse_factors_have_exactly_seven_nonzero_terms": exact_seven_term_count == adjacent_count,
        "all_common_interior_mass_numerators_positive_on_local_interval": common_z_positive_count == 71,
        "complete_local_root_atlas_covers_every_adjacent_factor": complete_root_atlas_count == adjacent_count,
        "sign_definite_factor_count_exact": fixed_sign_count == 1365,
        "simple_root_factor_count_exact": crossing_count == 2,
        "exact_crossing_pairs_and_directions": (
            root_pairs == list(EXPECTED_CROSSINGS)
            and root_signs == EXPECTED_CROSSINGS
        ),
        "crossing_roots_ordered_M79_before_M28": (
            len(root_records_sorted) == 2
            and root_records_sorted[0]["maximum"] == 79
            and root_records_sorted[1]["maximum"] == 28
        ),
        "strict_unimodality_at_both_interval_endpoints_and_probe": (
            lower_unimodal_count == 71
            and probe_unimodal_count == 71
            and upper_unimodal_count == 71
        ),
        "probe_second_difference_census_exact": (
            second_difference_positive_count == 1141
            and second_difference_negative_count == 155
            and second_difference_zero_count == 0
        ),
        "global_discrete_concavity_rejected_beyond_M15": fully_discrete_concave_supports == [10, 11, 12, 13, 14, 15],
        "A82_primal_feasibility_exceptions_preserved": a82_exceptions == EXPECTED_FEASIBILITY_EXCEPTIONS,
        "scope_and_nonclaim_boundary_preserved": (
            M_MIN == 10
            and M_MAX == 80
            and LOCAL_LOWER == sp.Rational(129, 1000)
            and LOCAL_UPPER == sp.Rational(133, 1000)
            and S0 == sp.Rational(131, 1000)
        ),
    }

    summary = {
        "audit": "A83_SEVEN_TERM_ADJACENT_DIFFERENCE_SIGN_ATLAS",
        "contract": {
            "maximum_range": [M_MIN, M_MAX],
            "adjacent_contact_rule": "2 <= k < floor(M/2)-1",
            "local_interval": [str(LOCAL_LOWER), str(LOCAL_UPPER)],
            "probe": str(S0),
            "beta": str(BETA),
            "target": str(TARGET),
        },
        "analytic_factorization": {
            "identity": "numerator(V_(M,k+1)-V_(M,k)) = Z_M(s) E_(M,k)(s)",
            "common_factor": "Z_M(s)=C_s H_beta-C_beta H_s, the contact-independent interior-mass numerator",
            "sparse_factor": "E_(M,k)=X_(M,k) deltaB_(M,k)+Y_(M,k) B_(M,k)+W_(M,k) H_M",
            "cofactors": {
                "X": "A_target B_k(beta)-H_beta B_k(target)",
                "Y": "-A_target deltaB_k(beta)+H_beta deltaB_k(target)",
                "W": "-B_k(beta) deltaB_k(target)+B_k(target) deltaB_k(beta)",
            },
            "B_formula": "B_k(r)=r^k-1+(k/M)(1-r^M)",
            "deltaB_formula": "deltaB_k(r)=B_(k+1)(r)-B_k(r)=r^(k+1)-r^k+(1-r^M)/M",
            "seven_exponents": "{M,h+1,h,k+1,k,1,0}",
            "seven_coefficients": {
                "e_(k+1)": "X",
                "e_k": "-X+Y",
                "e_M": "-X/M-(k/M)Y+W/2",
                "e_(h+1)": "W H_(h+1)",
                "e_h": "W H_h",
                "e_1": "W H_1",
                "e_0": "X/M-((M-k)/M)Y+W(1/2-2 epsilon)",
            },
            "finite_reconstruction_count": exact_factorization_count,
        },
        "complete_local_sign_atlas": {
            "adjacent_factor_count": adjacent_count,
            "sign_definite_no_root_count": fixed_sign_count,
            "one_simple_root_count": crossing_count,
            "root_records": root_records_sorted,
            "strict_unimodal_support_count": {
                "local_lower": lower_unimodal_count,
                "s0": probe_unimodal_count,
                "local_upper": upper_unimodal_count,
            },
            "phase_consequence": (
                "For every s in the local interval except the two certified algebraic roots, each support has exactly one sign variation in k and therefore one strict compressed maximizer. At a root the corresponding support has one two-contact plateau."
            ),
        },
        "discrete_concavity_test": {
            "probe_second_difference_count": (
                second_difference_positive_count
                + second_difference_negative_count
                + second_difference_zero_count
            ),
            "positive": second_difference_positive_count,
            "negative": second_difference_negative_count,
            "zero": second_difference_zero_count,
            "fully_strictly_concave_supports": fully_discrete_concave_supports,
            "verdict": (
                "REJECT_GLOBAL_DISCRETE_CONCAVITY: strict unimodality is supported by a one-sign-variation law, not by all second differences being negative."
            ),
        },
        "feasibility_boundary": {
            "A82_compressed_maximizer_primal_exceptions": a82_exceptions,
            "interpretation": (
                "The sparse adjacent sign atlas locates the algebraic compressed maximizer. It does not remove the full KKT feasibility requirement, because the eight A82 exceptions remain exact."
            ),
        },
        "support_records": support_records,
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": (
            "PASS_SEVEN_TERM_ADJACENT_DIFFERENCE_FACTORIZATION_AND_COMPLETE_LOCAL_SIGN_ATLAS"
            if all(gates.values())
            else "FAIL"
        ),
        "claim_boundary": [
            "The sparse factorization is an algebraic identity under the declared reduced contract.",
            "The positivity and complete sign-atlas theorem are finite and local: 10<=M<=80 and 129/1000<=s<=133/1000.",
            "Strict unimodality at the two algebraic roots is replaced by an adjacent two-contact plateau.",
            "Global discrete concavity is explicitly rejected; it is not used as a proof device.",
            "The eight A82 primal-feasibility exceptions remain and require full KKT validation of the lifted branch.",
            "No all-M recurrence, asymptotic contact law, or physical interpretation is inferred.",
        ],
    }

    catalogue = {
        "audit": "A83_SEVEN_TERM_ADJACENT_FACTOR_CATALOGUE",
        "polynomial_count": len(sparse_records),
        "scope": summary["contract"],
        "records": sparse_records,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    result_path = RESULTS / "a83_seven_term_adjacent_sign_atlas_results.json"
    catalogue_path = RESULTS / "a83_seven_term_adjacent_factor_catalogue.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    catalogue_path.write_text(json.dumps(catalogue, indent=2), encoding="utf-8")

    print(json.dumps({
        "audit": summary["audit"],
        "adjacent_factor_count": adjacent_count,
        "sign_definite_count": fixed_sign_count,
        "simple_root_count": crossing_count,
        "second_difference_census": {
            "positive": second_difference_positive_count,
            "negative": second_difference_negative_count,
            "zero": second_difference_zero_count,
        },
        "fully_discrete_concave_supports": fully_discrete_concave_supports,
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
