#!/usr/bin/env python3
"""A81 exact reduced boundary system and ordered-root theorem.

A80 established 142 six-term Cramer boundary polynomials for the 71 contacts
selected by A78. A81 derives those six terms from a two-variable reduction of
the compressed branch instead of recomputing an 8x8 determinant for every
coefficient.

The reduction is analytic under the declared central-mean contract. The
finite computational part:

1. reconstructs all 142 committed A80 boundary polynomials exactly;
2. verifies the reduced variables and gamma slacks against the full symbolic
   compressed branch;
3. certifies positivity of the t-numerator T(s) and basis determinant Delta(s)
   on I=[129/1000,133/1000] for every admissible pair
   10<=M<=80, 2<=k<floor(M/2), not only the selected contacts;
4. proves a positive boundary-gap identity for all selected contacts; and
5. derives the A80 root classification from endpoint signs alone once strict
   monotonicity and the positive gap are known.

The all-(M,k) formulas are algebraic identities. The positivity and root-order
claims remain finite and local to the declared M and s domains.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
A80_SCRIPT = HERE / "a80_local_compression_window_atlas_audit.py"
A78_RESULT = RESULTS / "a78_rational_probe_contact_selection_results.json"
A80_RESULT = RESULTS / "a80_local_compression_window_atlas_results.json"
A80_CATALOGUE = RESULTS / "a80_boundary_polynomial_catalogue.json"

S = sp.Symbol("s")
LOCAL_LOWER = sp.Rational(129, 1000)
LOCAL_UPPER = sp.Rational(133, 1000)
BETA = sp.Rational(1, 8)
GAMMA = sp.Rational(1, 16)
FULL_BRANCH_WITNESSES = {(10, 3), (15, 4), (20, 5), (40, 9), (57, 12), (64, 13), (74, 15), (80, 16)}


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


def normalized_epsilon(maximum: int) -> sp.Rational:
    h = maximum // 2
    scale = 1875 if maximum % 2 == 0 else 2500
    return sp.Rational(1, scale * 2**h)


def add_scaled(
    target: dict[int, sp.Rational],
    source: dict[int, sp.Rational],
    scale: sp.Rational,
) -> None:
    for exponent, coefficient in source.items():
        target[exponent] = sp.cancel(
            target.get(exponent, sp.Rational(0)) + scale * coefficient
        )


def evaluate_coefficients(
    coefficients: dict[int, sp.Rational],
    value: sp.Rational | sp.Symbol,
) -> sp.Expr:
    return sp.cancel(sum(
        coefficient * value**exponent
        for exponent, coefficient in coefficients.items()
    ))


def interval_enclosure(
    coefficients: dict[int, sp.Rational],
    lower: sp.Rational,
    upper: sp.Rational,
    *,
    derivative: bool = False,
) -> tuple[sp.Rational, sp.Rational]:
    enclosure_lower = sp.Rational(0)
    enclosure_upper = sp.Rational(0)
    for exponent, coefficient in coefficients.items():
        if derivative:
            if exponent == 0:
                continue
            coefficient *= exponent
            exponent -= 1
        power_lower = lower**exponent
        power_upper = upper**exponent
        if coefficient >= 0:
            enclosure_lower += coefficient * power_lower
            enclosure_upper += coefficient * power_upper
        else:
            enclosure_lower += coefficient * power_upper
            enclosure_upper += coefficient * power_lower
    return sp.factor(enclosure_lower), sp.factor(enclosure_upper)


def primitive_integer_polynomial(
    coefficients: dict[int, sp.Rational],
) -> sp.Poly:
    expression = evaluate_coefficients(coefficients, S)
    polynomial = sp.Poly(expression, S, domain=sp.QQ)
    _, integer_polynomial = polynomial.clear_denoms(convert=True)
    _, primitive_expression = sp.primitive(integer_polynomial.as_expr(), S)
    primitive = sp.Poly(primitive_expression, S, domain=sp.ZZ)
    if primitive.LC() < 0:
        primitive = -primitive
    return primitive


def coefficient_hash(polynomial: sp.Poly) -> str:
    canonical = json.dumps(
        [str(value) for value in polynomial.all_coeffs()],
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def polynomial_from_catalogue(item: dict[str, Any]) -> sp.Poly:
    coefficient_map = {
        int(exponent): sp.Integer(value)
        for exponent, value in item["polynomial"][
            "nonzero_coefficients_by_exponent"
        ].items()
    }
    return sp.Poly(evaluate_coefficients(coefficient_map, S), S, domain=sp.ZZ)


def reduced_coefficient_blocks(
    maximum: int,
    contact: int,
) -> dict[str, Any]:
    """Return the exact P/Q transform blocks for arbitrary admissible (M,k)."""
    h = maximum // 2
    epsilon = normalized_epsilon(maximum)
    u = sp.Rational(1, 2**h)
    d = sp.cancel(1 - (h + 1) * u)

    # P_r = A_r t + B_r z, z=p_k.
    B = {
        0: -sp.Rational(maximum - contact, maximum),
        contact: sp.Rational(1),
        maximum: -sp.Rational(contact, maximum),
    }

    # Q_r = C_r + D_r t after solving normalization, mean, and target.
    C = {
        1: sp.cancel(2 / d),
        h: sp.cancel(-2 * h / d),
        h + 1: sp.cancel(2 * (h - 1) / d),
    }
    if maximum % 2 == 0:
        D = {
            1: sp.cancel(-2 * u / d),
            h: sp.cancel(1 + 2 * h * u / d),
            h + 1: sp.cancel(-2 * (h - 1) * u / d),
        }
        q_weights = {
            "q1": "2(1-U t)/d",
            "qh": "t-h q1",
            "qh1": "(h-1) q1",
        }
    else:
        D = {
            1: sp.cancel(-sp.Rational(3, 2) * u / d),
            h: sp.cancel(sp.Rational(1, 2) + sp.Rational(3, 2) * h * u / d),
            h + 1: sp.cancel(
                sp.Rational(1, 2)
                - sp.Rational(3, 2) * (h - 1) * u / d
            ),
        }
        q_weights = {
            "q1": "(2-3 U t/2)/d",
            "qh": "t/2-h q1",
            "qh1": "t/2+(h-1) q1",
        }

    # H_s=A_s-D_s-2 epsilon is the alpha+ coefficient of t.
    H = {
        0: sp.Rational(1, 2) - 2 * epsilon,
        maximum: sp.Rational(1, 2),
    }
    for exponent, coefficient in D.items():
        H[exponent] = -coefficient

    expected_exponents = {maximum, h + 1, h, contact, 1, 0}
    if set(B) | set(C) | set(H) != expected_exponents:
        raise RuntimeError("Unexpected exponent collision in reduced blocks")

    return {
        "maximum": maximum,
        "contact": contact,
        "h": h,
        "epsilon": epsilon,
        "u": u,
        "d": d,
        "B": B,
        "C": C,
        "D": D,
        "H": H,
        "q_weight_formula": q_weights,
        "expected_exponents": expected_exponents,
    }


def reduced_system(maximum: int, contact: int) -> dict[str, Any]:
    blocks = reduced_coefficient_blocks(maximum, contact)
    epsilon = blocks["epsilon"]
    B = blocks["B"]
    C = blocks["C"]
    D = blocks["D"]
    H = blocks["H"]

    B_beta = evaluate_coefficients(B, BETA)
    C_beta = evaluate_coefficients(C, BETA)
    A_beta = sp.cancel((1 + BETA**maximum) / 2)
    D_beta = evaluate_coefficients(D, BETA)
    H_beta = sp.cancel(A_beta - D_beta + 2 * epsilon)

    determinant_coefficients: dict[int, sp.Rational] = {}
    add_scaled(determinant_coefficients, B, H_beta)
    add_scaled(determinant_coefficients, H, -B_beta)

    z_numerator_coefficients: dict[int, sp.Rational] = {}
    add_scaled(z_numerator_coefficients, C, H_beta)
    add_scaled(z_numerator_coefficients, H, -C_beta)

    t_numerator_coefficients: dict[int, sp.Rational] = {}
    add_scaled(t_numerator_coefficients, B, C_beta)
    add_scaled(t_numerator_coefficients, C, -B_beta)

    B_gamma = evaluate_coefficients(B, GAMMA)
    C_gamma = evaluate_coefficients(C, GAMMA)
    A_gamma = sp.cancel((1 + GAMMA**maximum) / 2)
    D_gamma = evaluate_coefficients(D, GAMMA)
    G_gamma = sp.cancel(A_gamma - D_gamma)

    boundary: dict[str, dict[str, Any]] = {}
    # delta=+1 is lower/gamma-, delta=-1 is upper/gamma+ oriented
    # so both boundary polynomials are increasing in the selected family.
    for label, delta in (("lower", 1), ("upper", -1)):
        q_delta = sp.cancel(G_gamma + 2 * delta * epsilon)
        X = sp.cancel(q_delta * C_beta - C_gamma * H_beta)
        Y = sp.cancel(B_gamma * H_beta - q_delta * B_beta)
        Z = sp.cancel(C_gamma * B_beta - B_gamma * C_beta)
        coefficients: dict[int, sp.Rational] = {}
        add_scaled(coefficients, B, X)
        add_scaled(coefficients, C, Y)
        add_scaled(coefficients, H, Z)
        coefficients = {
            exponent: sp.cancel(coefficient)
            for exponent, coefficient in coefficients.items()
        }
        boundary[label] = {
            "delta": delta,
            "X": X,
            "Y": Y,
            "Z": Z,
            "coefficients": coefficients,
        }

    return {
        **blocks,
        "B_beta": B_beta,
        "C_beta": C_beta,
        "H_beta": H_beta,
        "B_gamma": B_gamma,
        "C_gamma": C_gamma,
        "G_gamma": G_gamma,
        "determinant_coefficients": determinant_coefficients,
        "z_numerator_coefficients": z_numerator_coefficients,
        "t_numerator_coefficients": t_numerator_coefficients,
        "boundary": boundary,
    }

def sign_at(
    coefficients: dict[int, sp.Rational],
    point: sp.Rational,
) -> int:
    return int(sp.sign(evaluate_coefficients(coefficients, point)))


def main() -> None:
    for required in (A80_SCRIPT, A78_RESULT, A80_RESULT, A80_CATALOGUE):
        if not required.exists():
            raise FileNotFoundError(required)

    a80 = load_module(A80_SCRIPT, "a80_for_a81")
    a78_data = json.loads(A78_RESULT.read_text(encoding="utf-8"))
    a80_data = json.loads(A80_RESULT.read_text(encoding="utf-8"))
    catalogue_data = json.loads(A80_CATALOGUE.read_text(encoding="utf-8"))

    selected = [
        (int(item["maximum"]), int(item["contact"]))
        for item in a78_data["selected"]
    ]
    catalogue_lookup = {
        (int(item["maximum"]), item["boundary"]): item
        for item in catalogue_data["polynomials"]
    }

    selected_records: list[dict[str, Any]] = []
    formula_reconstruction_failures: list[dict[str, Any]] = []
    full_branch_identity_failures: list[dict[str, Any]] = []
    normalization_failures: list[dict[str, Any]] = []
    normalization_asymmetries: list[dict[str, Any]] = []
    gap_identity_failures: list[dict[str, Any]] = []
    selected_derivative_failures: list[dict[str, Any]] = []
    selected_sparsity_failures: list[dict[str, Any]] = []
    endpoint_classification: dict[str, list[int]] = {
        "complete_ordered_pair": [],
        "upper_only": [],
        "lower_only": [],
        "none": [],
        "other": [],
    }

    for maximum, contact in selected:
        system = reduced_system(maximum, contact)
        expected = system["expected_exponents"]
        formula_polynomials: dict[str, sp.Poly] = {}
        normalizations: dict[str, sp.Rational] = {}
        derivative_records: dict[str, dict[str, str]] = {}
        endpoint_signs: dict[str, list[int]] = {}

        for boundary in ("lower", "upper"):
            coefficients = system["boundary"][boundary]["coefficients"]
            primitive = primitive_integer_polynomial(coefficients)
            formula_polynomials[boundary] = primitive
            catalogue_item = catalogue_lookup[(maximum, boundary)]
            committed = polynomial_from_catalogue(catalogue_item)
            if primitive != committed:
                formula_reconstruction_failures.append({
                    "maximum": maximum,
                    "contact": contact,
                    "boundary": boundary,
                    "formula_hash": coefficient_hash(primitive),
                    "committed_hash": coefficient_hash(committed),
                })

            raw_coefficients = system["boundary"][boundary]["coefficients"]
            normalization = sp.cancel(
                raw_coefficients[maximum] / committed.LC()
            )
            coefficient_scale_match = all(
                sp.cancel(
                    raw_coefficients.get(exponent, sp.Rational(0))
                    - normalization * committed.nth(exponent)
                ) == 0
                for exponent in range(committed.degree() + 1)
            )
            if not coefficient_scale_match:
                normalization_failures.append({
                    "maximum": maximum,
                    "boundary": boundary,
                    "failure": "coefficient scaling mismatch",
                })
            normalizations[boundary] = sp.Rational(normalization)

            if (
                set(coefficients) != expected
                or any(value == 0 for value in coefficients.values())
            ):
                selected_sparsity_failures.append({
                    "maximum": maximum,
                    "contact": contact,
                    "boundary": boundary,
                    "observed_exponents": sorted(coefficients),
                })

            derivative_lower, derivative_upper = interval_enclosure(
                coefficients,
                LOCAL_LOWER,
                LOCAL_UPPER,
                derivative=True,
            )
            derivative_records[boundary] = {
                "lower": str(derivative_lower),
                "upper": str(derivative_upper),
            }
            if derivative_lower <= 0:
                selected_derivative_failures.append({
                    "maximum": maximum,
                    "contact": contact,
                    "boundary": boundary,
                    "derivative_lower": str(derivative_lower),
                })
            endpoint_signs[boundary] = [
                sign_at(coefficients, LOCAL_LOWER),
                sign_at(coefficients, LOCAL_UPPER),
            ]

        if not (
            normalizations["lower"] > 0
            and normalizations["upper"] > 0
        ):
            normalization_failures.append({
                "maximum": maximum,
                "contact": contact,
                "lower": str(normalizations["lower"]),
                "upper": str(normalizations["upper"]),
            })
        if normalizations["lower"] != normalizations["upper"]:
            normalization_asymmetries.append({
                "maximum": maximum,
                "contact": contact,
                "lower": str(normalizations["lower"]),
                "upper": str(normalizations["upper"]),
                "lower_over_upper": str(sp.cancel(
                    normalizations["lower"] / normalizations["upper"]
                )),
            })

        lower_coefficients = system["boundary"]["lower"]["coefficients"]
        upper_coefficients = system["boundary"]["upper"]["coefficients"]
        gap_coefficients = {
            exponent: sp.cancel(
                lower_coefficients.get(exponent, sp.Rational(0))
                - upper_coefficients.get(exponent, sp.Rational(0))
            )
            for exponent in system["expected_exponents"]
        }
        expected_gap_coefficients = {
            exponent: sp.cancel(
                4 * system["epsilon"]
                * system["t_numerator_coefficients"].get(
                    exponent, sp.Rational(0)
                )
            )
            for exponent in system["expected_exponents"]
        }
        if gap_coefficients != expected_gap_coefficients:
            gap_identity_failures.append({
                "maximum": maximum,
                "contact": contact,
            })

        identities: dict[str, bool] | None = None
        if (maximum, contact) in FULL_BRANCH_WITNESSES:
            lower_expression = evaluate_coefficients(lower_coefficients, S)
            upper_expression = evaluate_coefficients(upper_coefficients, S)
            determinant_expression = evaluate_coefficients(
                system["determinant_coefficients"], S
            )
            branch = a80.build_compressed_symbolic_branch(maximum, contact)
            condition_map = dict(branch["conditions"])
            identities = {
                "basic_p_contact": sp.cancel(
                    condition_map[f"basic_p_{contact}"]
                    - evaluate_coefficients(
                        system["z_numerator_coefficients"], S
                    ) / determinant_expression
                ) == 0,
                "basic_t": sp.cancel(
                    condition_map["basic_t"]
                    - evaluate_coefficients(
                        system["t_numerator_coefficients"], S
                    ) / determinant_expression
                ) == 0,
                "gamma_minus_slack": sp.cancel(
                    condition_map["inactive_slack_gamma_-1"]
                    - lower_expression / determinant_expression
                ) == 0,
                "gamma_plus_slack": sp.cancel(
                    condition_map["inactive_slack_gamma_+1"]
                    + upper_expression / determinant_expression
                ) == 0,
            }
            if not all(identities.values()):
                full_branch_identity_failures.append({
                    "maximum": maximum,
                    "contact": contact,
                    "identities": identities,
                })

        lower_signs = endpoint_signs["lower"]
        upper_signs = endpoint_signs["upper"]
        if lower_signs == [-1, 1] and upper_signs == [-1, 1]:
            root_class = "complete_ordered_pair"
        elif lower_signs == [1, 1] and upper_signs == [-1, 1]:
            root_class = "upper_only"
        elif lower_signs == [-1, 1] and upper_signs == [1, 1]:
            root_class = "lower_only"
        elif lower_signs == [1, 1] and upper_signs == [1, 1]:
            root_class = "none"
        else:
            root_class = "other"
        endpoint_classification[root_class].append(maximum)

        selected_records.append({
            "maximum": maximum,
            "contact": contact,
            "parity": "even" if maximum % 2 == 0 else "odd",
            "h": system["h"],
            "positive_primitive_normalizations": {
                "lower": str(normalizations["lower"]),
                "upper": str(normalizations["upper"]),
                "lower_over_upper": str(sp.cancel(
                    normalizations["lower"] / normalizations["upper"]
                )),
            },
            "full_branch_identities": identities,
            "boundary_hashes": {
                boundary: coefficient_hash(formula_polynomials[boundary])
                for boundary in ("lower", "upper")
            },
            "cofactor_coefficients": {
                boundary: {
                    "X": str(system["boundary"][boundary]["X"]),
                    "Y": str(system["boundary"][boundary]["Y"]),
                    "Z": str(system["boundary"][boundary]["Z"]),
                    "six_coefficients": {
                        str(exponent): str(coefficient)
                        for exponent, coefficient in sorted(
                            system["boundary"][boundary]["coefficients"].items(),
                            reverse=True,
                        )
                    },
                }
                for boundary in ("lower", "upper")
            },
            "derivative_intervals": derivative_records,
            "endpoint_signs": endpoint_signs,
            "endpoint_root_class": root_class,
        })

    # Exhaustive finite family: every admissible contact, not just A78 selected.
    all_contact_certificates: list[dict[str, Any]] = []
    family_sparsity_failures: list[dict[str, Any]] = []
    t_positivity_failures: list[dict[str, Any]] = []
    determinant_positivity_failures: list[dict[str, Any]] = []
    family_pair_count = 0

    for maximum in range(10, 81):
        h = maximum // 2
        for contact in range(2, h):
            family_pair_count += 1
            system = reduced_system(maximum, contact)
            expected = system["expected_exponents"]
            for boundary in ("lower", "upper"):
                coefficients = system["boundary"][boundary]["coefficients"]
                if (
                    set(coefficients) != expected
                    or any(value == 0 for value in coefficients.values())
                ):
                    family_sparsity_failures.append({
                        "maximum": maximum,
                        "contact": contact,
                        "boundary": boundary,
                    })

            t_coefficients = system["t_numerator_coefficients"]
            determinant_coefficients = system["determinant_coefficients"]
            t_interval = interval_enclosure(
                t_coefficients,
                LOCAL_LOWER,
                LOCAL_UPPER,
            )
            determinant_interval = interval_enclosure(
                determinant_coefficients,
                LOCAL_LOWER,
                LOCAL_UPPER,
            )
            if t_interval[0] <= 0:
                t_positivity_failures.append({
                    "maximum": maximum,
                    "contact": contact,
                    "interval": [str(t_interval[0]), str(t_interval[1])],
                })
            if determinant_interval[0] <= 0:
                determinant_positivity_failures.append({
                    "maximum": maximum,
                    "contact": contact,
                    "interval": [
                        str(determinant_interval[0]),
                        str(determinant_interval[1]),
                    ],
                })

            all_contact_certificates.append({
                "maximum": maximum,
                "contact": contact,
                "t_numerator_interval": [
                    str(t_interval[0]), str(t_interval[1])
                ],
                "determinant_interval": [
                    str(determinant_interval[0]),
                    str(determinant_interval[1])
                ],
                "positive_boundary_gap": bool(t_interval[0] > 0),
                "positive_scaled_mass_t": bool(
                    t_interval[0] > 0 and determinant_interval[0] > 0
                ),
            })

    expected_complete = list(a80_data["compression_window_supports"])
    expected_counts = a80_data["root_class_counts"]
    observed_counts = {
        "complete_ordered_pair": len(endpoint_classification["complete_ordered_pair"]),
        "upper_only": len(endpoint_classification["upper_only"]),
        "lower_only": len(endpoint_classification["lower_only"]),
        "none": len(endpoint_classification["none"]),
        "other": len(endpoint_classification["other"]),
    }

    gates = {
        "all_Mk_formula_has_exact_six_distinct_nonzero_coefficients": (
            family_pair_count == 1438 and not family_sparsity_failures
        ),
        "all_142_A80_boundary_polynomials_reconstructed_exactly": (
            not formula_reconstruction_failures
        ),
        "all_selected_primitive_normalizations_are_positive_and_exact": (
            not normalization_failures
        ),
        "primitive_content_asymmetries_exactly_classified": (
            [item["maximum"] for item in normalization_asymmetries]
            == [34, 64, 69, 77]
            and [item["lower_over_upper"] for item in normalization_asymmetries]
            == ["29", "13", "1/19", "11"]
        ),
        "reduced_z_t_and_gamma_slacks_equal_full_symbolic_branch_on_declared_witnesses": (
            not full_branch_identity_failures
        ),
        "exact_boundary_gap_identity_Flower_minus_Fupper_equals_4epsilonT": (
            not gap_identity_failures
        ),
        "T_positive_on_local_interval_for_all_1438_admissible_pairs": (
            not t_positivity_failures
        ),
        "Delta_positive_on_local_interval_for_all_1438_admissible_pairs": (
            not determinant_positivity_failures
        ),
        "all_selected_lower_and_upper_boundaries_strictly_increasing": (
            not selected_derivative_failures
        ),
        "selected_formula_sparsity_exact": not selected_sparsity_failures,
        "positive_gap_excludes_reversed_selected_root_pairs": (
            not t_positivity_failures
            and not selected_derivative_failures
            and not endpoint_classification["lower_only"]
        ),
        "endpoint_only_classification_reproduces_20_complete_pairs": (
            endpoint_classification["complete_ordered_pair"] == expected_complete
        ),
        "endpoint_only_classification_reproduces_three_upper_only_cases": (
            endpoint_classification["upper_only"] == [20, 36, 64]
        ),
        "endpoint_only_classification_reproduces_48_no_root_cases": (
            observed_counts["none"] == 48
        ),
        "no_lower_only_or_unclassified_selected_case": (
            observed_counts["lower_only"] == 0
            and observed_counts["other"] == 0
        ),
        "A80_root_class_counts_reproduced_exactly": (
            observed_counts["complete_ordered_pair"]
            == int(expected_counts["complete_ordered_pair"])
            and observed_counts["upper_only"]
            == int(expected_counts["upper_only"])
            and observed_counts["lower_only"]
            == int(expected_counts.get("lower_only", 0))
            and observed_counts["none"] == int(expected_counts["none"])
        ),
        "declared_full_branch_witness_set_complete": (
            sum(item["full_branch_identities"] is not None for item in selected_records)
            == len(FULL_BRANCH_WITNESSES)
            and all(
                item["full_branch_identities"] is None
                or all(item["full_branch_identities"].values())
                for item in selected_records
            )
        ),
    }

    result = {
        "audit": "A81_REDUCED_TWO_VARIABLE_BOUNDARY_SYSTEM",
        "contract": {
            "maximum_range": [10, 80],
            "admissible_contact_rule": "2 <= k < floor(M/2)",
            "selected_contact_count": len(selected),
            "full_branch_witnesses": [list(item) for item in sorted(FULL_BRANCH_WITNESSES)],
            "all_admissible_pair_count": family_pair_count,
            "local_interval": [str(LOCAL_LOWER), str(LOCAL_UPPER)],
            "beta": str(BETA),
            "gamma": str(GAMMA),
        },
        "analytic_reduction": {
            "P_transform": "P_r=A_r t+B_r z, z=p_k",
            "A_r": "(1+r^M)/2",
            "B_r": "r^k-(M-k)/M-(k/M)r^M",
            "Q_transform": "Q_r=C_r+D_r t",
            "W_r": "r-h r^h+(h-1)r^(h+1)",
            "d": "1-(h+1)2^(-h)",
            "C_r": "2 W_r/d",
            "D_r_even": "r^h-2^(1-h)W_r/d",
            "D_r_odd": "(r^h+r^(h+1))/2-3*2^(-h)W_r/(2d)",
            "alpha_t_coefficient": "H_s=A_s-D_s-2 epsilon",
            "beta_t_coefficient": "H_beta=A_beta-D_beta+2 epsilon",
            "two_by_two_system": [
                "B_s z+H_s t=C_s",
                "B_beta z+H_beta t=C_beta",
            ],
            "solutions": {
                "Delta": "B_s H_beta-B_beta H_s",
                "z": "(C_s H_beta-C_beta H_s)/Delta",
                "t": "(B_s C_beta-B_beta C_s)/Delta",
            },
            "boundary_formula": (
                "F_delta(s)=X_delta B_s+Y_delta C_s+Z H_s; "
                "delta=+1 lower, delta=-1 upper"
            ),
            "cofactor_constants": {
                "q_delta": "G_gamma+2 delta epsilon",
                "X_delta": "q_delta C_beta-C_gamma H_beta",
                "Y_delta": "B_gamma H_beta-q_delta B_beta",
                "Z": "C_gamma B_beta-B_gamma C_beta",
                "G_gamma": "A_gamma-D_gamma",
            },
            "six_coefficients": {
                "c_k": "X_delta",
                "c_M": "-(k/M)X_delta+Z/2",
                "c_0": "-((M-k)/M)X_delta+(1/2-2epsilon)Z",
                "c_1": "Y_delta C_1+Z H_1",
                "c_h": "Y_delta C_h+Z H_h",
                "c_h1": "Y_delta C_(h+1)+Z H_(h+1)",
            },
            "gap_identity": "F_lower-F_upper=4 epsilon T, T=B_s C_beta-B_beta C_s",
        },
        "finite_family_certificate": {
            "admissible_pair_count": family_pair_count,
            "boundary_formula_count": 2 * family_pair_count,
            "T_positive_count": family_pair_count - len(t_positivity_failures),
            "Delta_positive_count": (
                family_pair_count - len(determinant_positivity_failures)
            ),
            "sparsity_failure_count": len(family_sparsity_failures),
            "T_failures": t_positivity_failures,
            "Delta_failures": determinant_positivity_failures,
        },
        "primitive_normalization_result": {
            "all_positive": not normalization_failures,
            "asymmetry_count": len(normalization_asymmetries),
            "asymmetry_supports": [
                item["maximum"] for item in normalization_asymmetries
            ],
            "asymmetries": normalization_asymmetries,
            "interpretation": (
                "The raw reduced lower/upper formulas obey the exact gap "
                "identity. Primitive integer reduction can divide the two "
                "polynomials by different contents, so the identity must not "
                "be applied after independent primitive normalization."
            ),
        },
        "selected_contact_theorem": {
            "selected_contact_count": len(selected),
            "reconstructed_boundary_count": 2 * len(selected),
            "endpoint_classification": endpoint_classification,
            "root_class_counts": observed_counts,
            "logical_consequence": (
                "On the selected family, both boundaries are strictly "
                "increasing and F_lower>F_upper throughout I. Therefore a "
                "lower-only or reversed ordered pair is impossible. A "
                "complete pair is detected by F_lower(I_lower)<0 and "
                "F_upper(I_upper)>0; an upper-only case has F_lower positive "
                "throughout while F_upper crosses once."
            ),
        },
        "selected_records": selected_records,
        "failure_catalogue": {
            "formula_reconstruction": formula_reconstruction_failures,
            "normalization_failures": normalization_failures,
            "primitive_content_asymmetries": normalization_asymmetries,
            "full_branch_identities": full_branch_identity_failures,
            "gap_identity": gap_identity_failures,
            "selected_derivative": selected_derivative_failures,
            "selected_sparsity": selected_sparsity_failures,
            "family_sparsity": family_sparsity_failures,
        },
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(value is True for value in gates.values()),
        "verdict": (
            "PASS_REDUCED_BOUNDARY_SYSTEM_AND_ORDERED_ROOT_THEOREM"
            if all(gates.values())
            else "FAIL_REDUCED_BOUNDARY_SYSTEM"
        ),
        "claim_boundary": [
            "The reduced coefficient formulas are exact algebraic identities under the declared support and band contract.",
            "The positivity theorem is finite: 10<=M<=80, 2<=k<floor(M/2), and 129/1000<=s<=133/1000.",
            "Strict boundary monotonicity and endpoint-only root classification are certified for the 71 A78-selected contacts, not every admissible k.",
            "Independent primitive normalization changes the relative integer content at M=34,64,69,77; the gap identity is an identity of the raw reduced formulas before that normalization.",
            "The result does not derive a periodic support law, a selected-contact formula for arbitrary M, or any physical interpretation.",
        ],
    }

    certificate_payload = {
        "audit": "A81_ALL_CONTACT_POSITIVE_T_AND_DELTA_CERTIFICATES",
        "interval": [str(LOCAL_LOWER), str(LOCAL_UPPER)],
        "pair_count": family_pair_count,
        "certificates": all_contact_certificates,
        "all_T_positive": not t_positivity_failures,
        "all_Delta_positive": not determinant_positivity_failures,
    }

    formula_payload = {
        "audit": "A81_SELECTED_CONTACT_CLOSED_COEFFICIENT_FORMULAS",
        "record_count": len(selected_records),
        "records": selected_records,
    }

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "a81_reduced_boundary_system_results.json").write_text(
        json.dumps(result, indent=2, sort_keys=False),
        encoding="utf-8",
    )
    (RESULTS / "a81_all_contact_positive_gap_certificates.json").write_text(
        json.dumps(certificate_payload, indent=2, sort_keys=False),
        encoding="utf-8",
    )
    (RESULTS / "a81_selected_contact_coefficient_formulas.json").write_text(
        json.dumps(formula_payload, indent=2, sort_keys=False),
        encoding="utf-8",
    )

    print(json.dumps({
        "audit": result["audit"],
        "selected_contacts": len(selected),
        "all_admissible_pairs": family_pair_count,
        "reconstructed_boundaries": 2 * len(selected),
        "root_class_counts": observed_counts,
        "gate_count": result["gate_count"],
        "pass_count": result["pass_count"],
        "verdict": result["verdict"],
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
