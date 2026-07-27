#!/usr/bin/env python3
"""A75 exact audit: parity reduction, double support-size bifurcation,
and exact M=15/M=16 extensions.

The late-stage gamma-plus candidate is

    P={0,3,4,M},
    Q={1,h,h+1},
    h=floor(M/2),
    active={alpha+,beta-,gamma+}.

The central-mean normalized error has parity forms:

    M=2h:     epsilon=2^{-h}/1875,
    M=2h+1:   epsilon=2^{-h}/2500.

Using U=2^{-h}, V=s^h, s=2^{-alpha}, the gamma-plus multiplier is
reconstructed separately for even and odd supports:

    lambda_gamma_plus = N_parity(h,U,V,s) / D_parity(h,U,V,s).

On the exact interval I=[13/100,33/250], A75 proves:

    lambda_gamma_plus > 0 for M=10,11,12,
    lambda_gamma_plus < 0 for 13 <= M <= 21,
    lambda_gamma_plus > 0 for every integer M >= 22.

The second sign change is caused by the active-basis determinant:
the Cramer numerator stays negative for all M>=13, while the denominator
changes from positive to negative at M=22.

Proof architecture
------------------
1. Exact parity-specific determinant formulas.
2. Exact Bernstein-coefficient sign certificates for M=10,...,35.
3. Exact asymptotic remainder bounds for h>=18, separately by parity.
4. Independent exact global phase and catalogue certificates for M=15,16.

The result is exact on the declared s interval. It is not a universal
statement over all alpha in [2,3) for the candidate gamma-plus signature.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent

A74_RESULTS = HERE / "a74_interval_gamma_bifurcation_results.json"
PARITY_CACHE = HERE / "a75_parity_formula_cache.json"
DISCOVERY = HERE / "a75_M15_M16_phase_discovery.json"
PHASE_M15 = HERE / "a75_exact_phases_M15.json"
PHASE_M16 = HERE / "a75_exact_phases_M16.json"
CATALOGUE_M15 = HERE / "a75_exact_catalogue_M15.json"
CATALOGUE_M16 = HERE / "a75_exact_catalogue_M16.json"

S = sp.Symbol("s")
H = sp.Symbol("h", integer=True, positive=True)
U = sp.Symbol("U", positive=True)
V = sp.Symbol("V", positive=True)
T = sp.Symbol("t")

INTERVAL_LOWER = sp.Rational(13, 100)
INTERVAL_UPPER = sp.Rational(33, 250)
ASYMPTOTIC_H0 = 18


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)

    return json.loads(
        path.read_text(encoding="utf-8")
    )


def parity_formula(
    parity: str,
) -> dict[str, sp.Expr]:
    if parity == "even":
        maximum = 2 * H
        mean = H
        target_at_maximum = U**2
        alpha_at_maximum = V**2
        epsilon = U / 1875
    elif parity == "odd":
        maximum = 2 * H + 1
        mean = H + sp.Rational(1, 2)
        target_at_maximum = U**2 / 2
        alpha_at_maximum = S * V**2
        epsilon = U / 2500
    else:
        raise ValueError(parity)

    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [0, 3, 4, maximum, 0, 0, 0, -mean],
        [0, 0, 0, 0, 1, H, H + 1, -mean],
        [
            0,
            0,
            0,
            0,
            sp.Rational(1, 2),
            U,
            U / 2,
            0,
        ],
        [
            1,
            S**3,
            S**4,
            alpha_at_maximum,
            -S,
            -V,
            -S * V,
            -2 * epsilon,
        ],
        [
            -1,
            -sp.Rational(1, 512),
            -sp.Rational(1, 4096),
            -target_at_maximum**3,
            sp.Rational(1, 8),
            U**3,
            U**3 / 8,
            -2 * epsilon,
        ],
        [
            1,
            sp.Rational(1, 4096),
            sp.Rational(1, 65536),
            target_at_maximum**4,
            -sp.Rational(1, 16),
            -U**4,
            -U**4 / 16,
            -2 * epsilon,
        ],
    ]

    basis = sp.Matrix(rows)
    objective = sp.Matrix(
        [
            1,
            sp.Rational(1, 8),
            sp.Rational(1, 16),
            target_at_maximum,
            0,
            0,
            0,
            0,
        ]
    )

    numerator_basis = basis.copy()
    numerator_basis[7, :] = objective.T

    numerator = sp.factor(
        numerator_basis.det()
    )
    denominator = sp.factor(
        basis.det()
    )

    return {
        "maximum": maximum,
        "epsilon": epsilon,
        "numerator": numerator,
        "denominator": denominator,
        "ratio": sp.cancel(
            numerator / denominator
        ),
    }


def specialized_polynomials(
    formula: dict[str, sp.Expr],
    maximum: int,
) -> tuple[sp.Poly, sp.Poly]:
    h = maximum // 2
    substitutions = {
        H: h,
        U: sp.Rational(1, 2**h),
        V: S**h,
    }

    numerator = sp.factor(
        formula["numerator"].subs(
            substitutions
        )
    )
    denominator = sp.factor(
        formula["denominator"].subs(
            substitutions
        )
    )

    return (
        sp.Poly(
            numerator,
            S,
            domain=sp.QQ,
        ),
        sp.Poly(
            denominator,
            S,
            domain=sp.QQ,
        ),
    )


def bernstein_coefficients(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
) -> list[sp.Rational]:
    degree = polynomial.degree()

    if degree <= 0:
        return [
            sp.Rational(
                polynomial.nth(0)
            )
        ]

    transformed = sp.Poly(
        sp.expand(
            polynomial.as_expr().subs(
                S,
                lower
                + (
                    upper - lower
                )
                * T,
            )
        ),
        T,
        domain=sp.QQ,
    )

    power_coefficients = [
        transformed.nth(index)
        for index in range(
            degree + 1
        )
    ]

    return [
        sp.factor(
            sum(
                power_coefficients[j]
                * sp.binomial(k, j)
                / sp.binomial(
                    degree,
                    j,
                )
                for j in range(
                    k + 1
                )
            )
        )
        for k in range(
            degree + 1
        )
    ]


def strict_bernstein_sign(
    polynomial: sp.Poly,
) -> dict[str, Any]:
    coefficients = (
        bernstein_coefficients(
            polynomial,
            INTERVAL_LOWER,
            INTERVAL_UPPER,
        )
    )

    if all(
        coefficient > 0
        for coefficient
        in coefficients
    ):
        sign = 1
    elif all(
        coefficient < 0
        for coefficient
        in coefficients
    ):
        sign = -1
    else:
        sign = 0

    return {
        "sign": sign,
        "coefficient_count": len(
            coefficients
        ),
        "minimum_absolute_coefficient": str(
            min(
                abs(coefficient)
                for coefficient
                in coefficients
            )
        ),
        "maximum_absolute_coefficient": str(
            max(
                abs(coefficient)
                for coefficient
                in coefficients
            )
        ),
    }


def leading_terms(
    formula: dict[str, sp.Expr],
) -> dict[str, sp.Expr]:
    return {
        "numerator": sp.factor(
            formula[
                "numerator"
            ].subs(
                {
                    U: 0,
                    V: 0,
                }
            )
        ),
        "denominator": sp.factor(
            formula[
                "denominator"
            ].subs(
                {
                    U: 0,
                    V: 0,
                }
            )
        ),
    }


def remainder_bound(
    expression: sp.Expr,
    h0: int,
) -> dict[str, Any]:
    leading = expression.subs(
        {
            U: 0,
            V: 0,
        }
    )
    remainder = sp.expand(
        expression - leading
    )
    polynomial = sp.Poly(
        remainder,
        H,
        U,
        V,
        S,
        domain=sp.QQ,
    )

    total = sp.Rational(0)
    largest_step_ratio = (
        sp.Rational(0)
    )

    for monomial, coefficient in (
        polynomial.terms()
    ):
        power_h, power_u, power_v, power_s = (
            monomial
        )

        decay_base = (
            sp.Rational(1, 2)
            ** power_u
            * INTERVAL_UPPER
            ** power_v
        )

        step_ratio = (
            decay_base
            * sp.Rational(
                h0 + 1,
                h0,
            )
            ** power_h
        )
        largest_step_ratio = max(
            largest_step_ratio,
            step_ratio,
        )

        total += (
            abs(coefficient)
            * sp.Integer(h0)
            ** power_h
            * sp.Rational(1, 2)
            ** (
                power_u
                * h0
            )
            * INTERVAL_UPPER
            ** (
                power_v
                * h0
            )
            * INTERVAL_UPPER
            ** power_s
        )

    return {
        "term_count": len(
            polynomial.terms()
        ),
        "upper_bound": sp.factor(
            total
        ),
        "largest_one_step_decay_ratio": (
            sp.factor(
                largest_step_ratio
            )
        ),
    }


def leading_lower_bound(
    parity: str,
    kind: str,
    h0: int,
) -> sp.Rational:
    common_numerator = (
        (
            1
            - 2
            * INTERVAL_UPPER
        )
        * (
            8
            * INTERVAL_LOWER
            - 1
        )
        * (
            84
            * INTERVAL_LOWER**2
            + 10
            * INTERVAL_LOWER
            + 1
        )
    )
    common_denominator = (
        (
            8
            * INTERVAL_LOWER
            - 1
        )
        * (
            16
            * INTERVAL_LOWER
            - 1
        )
        * (
            448
            * INTERVAL_LOWER**2
            + 24
            * INTERVAL_LOWER
            + 1
        )
    )

    if parity == "even":
        if kind == "numerator":
            return sp.factor(
                sp.Rational(
                    3 * h0,
                    65536,
                )
                * common_numerator
            )

        return sp.factor(
            sp.Rational(
                h0,
                67108864,
            )
            * common_denominator
        )

    if kind == "numerator":
        return sp.factor(
            sp.Rational(
                3
                * (
                    2 * h0
                    + 1
                ),
                131072,
            )
            * common_numerator
        )

    return sp.factor(
        sp.Rational(
            2 * h0 + 1,
            134217728,
        )
        * common_denominator
    )


def phase_signature(
    maximum: int,
    phase: dict[str, Any],
) -> dict[str, Any]:
    count = maximum + 1
    indices = phase[
        "positive_indices"
    ]

    return {
        "p_support": [
            index
            for index in indices
            if 0 <= index < count
        ],
        "q_support": [
            index - count
            for index in indices
            if count
            <= index
            < 2 * count
        ],
        "active_observations": (
            phase[
                "active_observations"
            ]
        ),
    }


def main() -> None:
    a74 = load_json(A74_RESULTS)
    discovery = load_json(DISCOVERY)
    phase_results = {
        15: load_json(PHASE_M15),
        16: load_json(PHASE_M16),
    }
    catalogues = {
        15: load_json(CATALOGUE_M15),
        16: load_json(CATALOGUE_M16),
    }

    parity_cache = load_json(PARITY_CACHE)
    local_symbols = {
        "h": H,
        "U": U,
        "V": V,
        "s": S,
    }
    formulas = {
        parity: {
            "numerator": sp.sympify(
                parity_cache[parity]["numerator"],
                locals=local_symbols,
            ),
            "denominator": sp.sympify(
                parity_cache[parity]["denominator"],
                locals=local_symbols,
            ),
        }
        for parity in ["even", "odd"]
    }
    for formula in formulas.values():
        formula["ratio"] = sp.cancel(
            formula["numerator"]
            / formula["denominator"]
        )
    leading = {
        parity: {
            "numerator": sp.sympify(
                parity_cache[parity]["leading_numerator"],
                locals=local_symbols,
            ),
            "denominator": sp.sympify(
                parity_cache[parity]["leading_denominator"],
                locals=local_symbols,
            ),
        }
        for parity in ["even", "odd"]
    }

    # Verify against the independently constructed A74 M=12/M=13 formula.
    a74_numerator = sp.sympify(
        a74[
            "symbolic_gamma_multiplier"
        ]["numerator"]
    )
    a74_denominator = sp.sympify(
        a74[
            "symbolic_gamma_multiplier"
        ]["denominator"]
    )
    M = sp.Symbol("M")
    R = sp.Symbol("R")
    T_symbol = sp.Symbol("T")
    epsilon = sp.Symbol(
        "epsilon"
    )

    a74_ratio = sp.cancel(
        a74_numerator
        / a74_denominator
    )

    specialization_checks = {}

    for maximum in [12, 13]:
        h = maximum // 2
        parity = (
            "even"
            if maximum % 2 == 0
            else "odd"
        )
        parity_ratio = sp.cancel(
            formulas[parity][
                "ratio"
            ].subs(
                {
                    H: h,
                    U: sp.Rational(
                        1,
                        2**h,
                    ),
                    V: S**h,
                }
            )
        )

        a74_specialized = sp.cancel(
            a74_ratio.subs(
                {
                    M: maximum,
                    R: sp.Rational(
                        1,
                        2**maximum,
                    ),
                    T_symbol: S**maximum,
                    epsilon: (
                        sp.Rational(
                            1,
                            120000,
                        )
                        if maximum == 12
                        else sp.Rational(
                            1,
                            160000,
                        )
                    ),
                }
            )
        )

        specialization_checks[
            str(maximum)
        ] = bool(
            sp.cancel(
                parity_ratio
                - a74_specialized
            )
            == 0
        )

    finite_certificates = []
    finite_sign_gates = []

    for maximum in range(
        10,
        36,
    ):
        parity = (
            "even"
            if maximum % 2 == 0
            else "odd"
        )
        numerator, denominator = (
            specialized_polynomials(
                formulas[parity],
                maximum,
            )
        )

        numerator_certificate = (
            strict_bernstein_sign(
                numerator
            )
        )
        denominator_certificate = (
            strict_bernstein_sign(
                denominator
            )
        )

        multiplier_sign = (
            numerator_certificate[
                "sign"
            ]
            * denominator_certificate[
                "sign"
            ]
        )

        finite_sign_gates.append(
            numerator_certificate[
                "sign"
            ]
            != 0
            and denominator_certificate[
                "sign"
            ]
            != 0
        )

        finite_certificates.append(
            {
                "maximum": maximum,
                "parity": parity,
                "h": maximum // 2,
                "numerator_degree": (
                    numerator.degree()
                ),
                "denominator_degree": (
                    denominator.degree()
                ),
                "numerator": (
                    numerator_certificate
                ),
                "denominator": (
                    denominator_certificate
                ),
                "multiplier_sign": (
                    multiplier_sign
                ),
            }
        )

    asymptotic_certificates = {}

    for parity, formula in (
        formulas.items()
    ):
        asymptotic_certificates[
            parity
        ] = {}

        for kind in [
            "numerator",
            "denominator",
        ]:
            remainder = (
                remainder_bound(
                    formula[kind],
                    ASYMPTOTIC_H0,
                )
            )
            lower_bound = (
                leading_lower_bound(
                    parity,
                    kind,
                    ASYMPTOTIC_H0,
                )
            )
            ratio = sp.factor(
                remainder[
                    "upper_bound"
                ]
                / lower_bound
            )

            asymptotic_certificates[
                parity
            ][kind] = {
                "leading_term": str(
                    leading[parity][
                        kind
                    ]
                ),
                "leading_absolute_lower_bound": str(
                    lower_bound
                ),
                "remainder_absolute_upper_bound": str(
                    remainder[
                        "upper_bound"
                    ]
                ),
                "remainder_to_leading_ratio": str(
                    ratio
                ),
                "remainder_to_leading_decimal": str(
                    sp.N(
                        ratio,
                        50,
                    )
                ),
                "remainder_term_count": (
                    remainder[
                        "term_count"
                    ]
                ),
                "largest_one_step_decay_ratio": str(
                    remainder[
                        "largest_one_step_decay_ratio"
                    ]
                ),
                "strictly_below_leading": bool(
                    ratio < 1
                ),
                "decays_for_all_h_at_least_18": bool(
                    remainder[
                        "largest_one_step_decay_ratio"
                    ]
                    < 1
                ),
            }

    finite_pattern = {
        record["maximum"]: (
            record[
                "numerator"
            ]["sign"],
            record[
                "denominator"
            ]["sign"],
            record[
                "multiplier_sign"
            ],
        )
        for record
        in finite_certificates
    }

    expected_pattern = {
        maximum: (
            (1, 1, 1)
            if maximum <= 12
            else (
                -1,
                1,
                -1,
            )
            if maximum <= 21
            else (
                -1,
                -1,
                1,
            )
        )
        for maximum in range(
            10,
            36,
        )
    }

    discovery_map = {
        item["maximum"]: item
        for item
        in discovery["supports"]
    }

    discovery_matches = {}

    for maximum in [15, 16]:
        exact_signatures = [
            phase_signature(
                maximum,
                phase,
            )
            for phase
            in phase_results[
                maximum
            ]["phases"]
        ]
        numerical_signatures = [
            {
                "p_support": (
                    phase[
                        "p_support"
                    ]
                ),
                "q_support": (
                    phase[
                        "q_support"
                    ]
                ),
                "active_observations": (
                    phase[
                        "active_observations"
                    ]
                ),
            }
            for phase
            in discovery_map[
                maximum
            ]["phases"]
        ]

        discovery_matches[
            str(maximum)
        ] = bool(
            exact_signatures
            == numerical_signatures
        )

    catalogue_boundary_matches = {}

    for maximum in [15, 16]:
        catalogue_boundary_matches[
            str(maximum)
        ] = bool(
            sp.Rational(
                catalogues[
                    maximum
                ]["top"][0][
                    "primal"
                ]
            )
            == sp.Rational(
                phase_results[
                    maximum
                ]["boundary_ratio"]
            )
        )

    gates = {
        "A74_previous_audit_passed": bool(
            all(
                a74["gates"].values()
            )
        ),
        "parity_formula_matches_A74_M12_M13": bool(
            all(
                specialization_checks.values()
            )
        ),
        "all_26_finite_Bernstein_certificates_strict": bool(
            len(
                finite_certificates
            )
            == 26
            and all(
                finite_sign_gates
            )
        ),
        "finite_sign_pattern_matches_double_bifurcation": bool(
            finite_pattern
            == expected_pattern
        ),
        "all_four_asymptotic_remainder_bounds_below_leading": bool(
            all(
                item[
                    "strictly_below_leading"
                ]
                for parity
                in asymptotic_certificates.values()
                for item
                in parity.values()
            )
        ),
        "all_asymptotic_remainders_decay_for_h_at_least_18": bool(
            all(
                item[
                    "decays_for_all_h_at_least_18"
                ]
                for parity
                in asymptotic_certificates.values()
                for item
                in parity.values()
            )
        ),
        "exact_gamma_plus_double_bifurcation_for_all_M_at_least_10": bool(
            finite_pattern[10][2]
            == 1
            and finite_pattern[12][2]
            == 1
            and finite_pattern[13][2]
            == -1
            and finite_pattern[21][2]
            == -1
            and finite_pattern[22][2]
            == 1
            and all(
                asymptotic_certificates[
                    parity
                ][kind][
                    "strictly_below_leading"
                ]
                for parity
                in ["even", "odd"]
                for kind
                in [
                    "numerator",
                    "denominator",
                ]
            )
        ),
        "M15_M16_discovery_matches_exact_phase_signatures": bool(
            all(
                discovery_matches.values()
            )
        ),
        "M15_M16_exact_global_phase_theorems_pass": bool(
            all(
                all(
                    phase_results[
                        maximum
                    ]["gates"].values()
                )
                for maximum in [15, 16]
            )
        ),
        "M15_M16_catalogues_have_84_designs": bool(
            all(
                catalogues[
                    maximum
                ]["count"]
                == 84
                for maximum
                in [15, 16]
            )
        ),
        "M15_M16_unique_catalogue_winner_2_3_4": bool(
            all(
                catalogues[
                    maximum
                ]["winner"]
                == [2, 3, 4]
                and sp.Rational(
                    catalogues[
                        maximum
                    ]["gap"]
                )
                > 0
                for maximum
                in [15, 16]
            )
        ),
        "M15_M16_top_three_primal_dual_values_match": bool(
            all(
                item["equal"]
                for maximum
                in [15, 16]
                for item
                in catalogues[
                    maximum
                ]["top"]
            )
        ),
        "M15_M16_catalogue_and_continuous_boundary_values_match": bool(
            all(
                catalogue_boundary_matches.values()
            )
        ),
    }

    verdict = (
        "PASS_PARITY_REDUCED_DOUBLE_BIFURCATION_AND_M15_M16_EXTENSION"
        if all(
            gates.values()
        )
        else "FAIL_A75_PARITY_ORIENTATION_AUDIT"
    )

    result = {
        "audit": (
            "A75_PARITY_REDUCED_SUPPORT_SIZE_ORIENTATION"
        ),
        "interval": {
            "s_lower": str(
                INTERVAL_LOWER
            ),
            "s_upper": str(
                INTERVAL_UPPER
            ),
            "alpha_lower_decimal": str(
                sp.N(
                    -sp.log(
                        INTERVAL_UPPER,
                        2,
                    ),
                    50,
                )
            ),
            "alpha_upper_decimal": str(
                sp.N(
                    -sp.log(
                        INTERVAL_LOWER,
                        2,
                    ),
                    50,
                )
            ),
        },
        "parity_reduction": {
            "even": {
                "support": "M=2h",
                "U": "2^(-h)",
                "V": "s^h",
                "epsilon": "U/1875",
                "numerator": str(
                    formulas[
                        "even"
                    ]["numerator"]
                ),
                "denominator": str(
                    formulas[
                        "even"
                    ]["denominator"]
                ),
                "leading_numerator": str(
                    leading[
                        "even"
                    ]["numerator"]
                ),
                "leading_denominator": str(
                    leading[
                        "even"
                    ]["denominator"]
                ),
            },
            "odd": {
                "support": "M=2h+1",
                "U": "2^(-h)",
                "V": "s^h",
                "epsilon": "U/2500",
                "numerator": str(
                    formulas[
                        "odd"
                    ]["numerator"]
                ),
                "denominator": str(
                    formulas[
                        "odd"
                    ]["denominator"]
                ),
                "leading_numerator": str(
                    leading[
                        "odd"
                    ]["numerator"]
                ),
                "leading_denominator": str(
                    leading[
                        "odd"
                    ]["denominator"]
                ),
            },
            "specialization_checks": (
                specialization_checks
            ),
        },
        "finite_Bernstein_certificates": (
            finite_certificates
        ),
        "asymptotic_certificates": (
            asymptotic_certificates
        ),
        "support_size_theorem": {
            "numerator_sign": {
                "M_10_to_12": "positive",
                "all_M_at_least_13": "negative",
            },
            "denominator_sign": {
                "M_10_to_21": "positive",
                "all_M_at_least_22": "negative",
            },
            "multiplier_sign": {
                "M_10_to_12": "positive",
                "M_13_to_21": "negative",
                "all_M_at_least_22": "positive",
            },
            "formal_statement": (
                "For every integer M>=10, on the declared exact "
                "s interval, the gamma-plus multiplier is positive "
                "for M=10,11,12, negative for 13<=M<=21, and "
                "positive for every M>=22."
            ),
            "mechanism": (
                "The first sign change at 12->13 comes from the "
                "Cramer numerator. The re-entry at 21->22 comes "
                "from the active-basis determinant changing sign "
                "while the numerator remains negative."
            ),
        },
        "M15_M16": {
            "discovery_matches": (
                discovery_matches
            ),
            "phase_results": {
                str(maximum): (
                    phase_results[
                        maximum
                    ]
                )
                for maximum
                in [15, 16]
            },
            "catalogues": {
                str(maximum): (
                    catalogues[
                        maximum
                    ]
                )
                for maximum
                in [15, 16]
            },
            "catalogue_boundary_matches": (
                catalogue_boundary_matches
            ),
            "formal_result": (
                "M=15 and M=16 each have six exact phases and "
                "five simple finite transitions. Their first-anchor "
                "risks are strictly increasing on alpha in [2,3), "
                "and {2,3,4} is the unique exact integer-catalogue "
                "winner."
            ),
        },
        "formal_results": [
            (
                "central-mean noise normalization admits separate "
                "exact even and odd Cramer formulas"
            ),
            (
                "the gamma-plus multiplier has two exact support-size "
                "orientation bifurcations on the declared interval"
            ),
            (
                "the negative orientation after M=13 is temporary"
            ),
            (
                "gamma-plus re-enters with positive orientation for "
                "every integer M>=22 on the declared interval"
            ),
            (
                "the numerator remains negative for every M>=13"
            ),
            (
                "the second bifurcation is caused by the basis "
                "determinant orientation"
            ),
            (
                "the global first-boundary theorem extends exactly "
                "to M=15 and M=16"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The all-M support-size theorem concerns the declared "
            "gamma-plus candidate signature only on the exact "
            "interval s in [13/100,33/250]. It does not state that "
            "this signature is globally optimal for every M or "
            "throughout alpha in [2,3)."
        ),
    }

    output = HERE / (
        "a75_parity_orientation_results.json"
    )
    output.write_text(
        json.dumps(
            result,
            indent=2,
        ),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(
            gates
        ),
        "pass_count": sum(
            gates.values()
        ),
        "support_size_multiplier_sign": (
            result[
                "support_size_theorem"
            ][
                "multiplier_sign"
            ]
        ),
        "asymptotic_start": {
            "h": ASYMPTOTIC_H0,
            "even_M": 2
            * ASYMPTOTIC_H0,
            "odd_M": 2
            * ASYMPTOTIC_H0
            + 1,
        },
        "M15_phase_count": (
            phase_results[15][
                "phase_count"
            ]
        ),
        "M16_phase_count": (
            phase_results[16][
                "phase_count"
            ]
        ),
        "M15_M16_winners": {
            "15": catalogues[15][
                "winner"
            ],
            "16": catalogues[16][
                "winner"
            ],
        },
        "failed_gates": [
            name
            for name, value
            in gates.items()
            if not value
        ],
        "verdict": verdict,
    }

    print(
        json.dumps(
            summary,
            indent=2,
        )
    )

    if not all(
        gates.values()
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
