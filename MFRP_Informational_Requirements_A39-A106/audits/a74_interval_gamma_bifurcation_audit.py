#!/usr/bin/env python3
"""A74 exact audit: interval-stable gamma bifurcation and M=14 extension.

Part I: symbolic gamma multiplier
---------------------------------
For the late-stage signature with

    P={0,3,4,M},
    Q={1,6,7},
    mean=M/2,
    active bands alpha+, beta-, gamma+,

write

    R=2^{-M},
    T=s^M,
    s=2^{-alpha}.

The gamma-plus multiplier is reconstructed by Cramer's rule as

    lambda_gamma_plus = N(M,R,T,s,epsilon) / D(M,R,T,s,epsilon).

The symbolic determinant formula is checked against independently built exact
LP dual branches for M=12 and M=13.

Part II: interval-stable support-size bifurcation
-------------------------------------------------
On the common exact rational interval

    s in [13/100, 33/250],

the same gamma-plus signature has:

    lambda_gamma_plus > 0 at M=12,
    lambda_gamma_plus < 0 at M=13.

There are no numerator or denominator roots in the interval.

On the complete exact M=13 phase-7 interval:
- the inherited gamma-plus multiplier remains strictly negative;
- the gamma-minus replacement remains strictly positive and globally KKT
  certified by the exact phase theorem.

Part III: M=14
--------------
M=14 is discovered numerically without importing the M=13 phase grammar,
then certified independently over seven exact algebraic phases. All 84
integer designs are ranked exactly. {2,3,4} remains the unique winner.

The result is exact for M=12,13,14. It is not an arbitrary-M theorem.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent

A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"
A72_M12 = HERE / "a72_exact_phases_M12.json"
A73_M13 = HERE / "a73_exact_phases_M13.json"
A74_M14 = HERE / "a74_exact_phases_M14.json"
A74_M14_CATALOGUE = HERE / "a74_exact_catalogue_M14.json"
A74_M14_DISCOVERY = HERE / "a74_M14_phase_discovery.json"
A73_RESULTS = HERE / "a73_complete_one_pivot_neighborhood_results.json"

S = sp.Symbol("s")
M_SYMBOL = sp.Symbol("M")
R_SYMBOL = sp.Symbol("R")
T_SYMBOL = sp.Symbol("T")
E_SYMBOL = sp.Symbol("epsilon")

COMMON_LOWER = sp.Rational(13, 100)
COMMON_UPPER = sp.Rational(33, 250)


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def exact_boundary(
    serialized: dict[str, Any],
) -> dict[str, Any]:
    return {
        "kind": serialized["kind"],
        "left": sp.Rational(serialized["left"]),
        "right": sp.Rational(serialized["right"]),
    }


def phase_contains_interval(
    phase: dict[str, Any],
    lower: sp.Rational,
    upper: sp.Rational,
) -> bool:
    phase_lower = sp.Rational(
        phase["s_lower"]["right"]
    )
    phase_upper = sp.Rational(
        phase["s_upper"]["left"]
    )
    return bool(
        phase_lower < lower
        and upper < phase_upper
    )


def condition_expression(
    branch: dict[str, Any],
    name: str,
) -> sp.Expr:
    return next(
        expression
        for current_name, expression
        in branch["conditions"]
        if current_name == name
    )


def symbolic_gamma_formula() -> dict[str, sp.Expr]:
    mean = M_SYMBOL / 2

    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [0, 3, 4, M_SYMBOL, 0, 0, 0, -mean],
        [0, 0, 0, 0, 1, 6, 7, -mean],
        [
            0,
            0,
            0,
            0,
            sp.Rational(1, 2),
            sp.Rational(1, 64),
            sp.Rational(1, 128),
            0,
        ],
        [
            1,
            S**3,
            S**4,
            T_SYMBOL,
            -S,
            -S**6,
            -S**7,
            -2 * E_SYMBOL,
        ],
        [
            -1,
            -sp.Rational(1, 512),
            -sp.Rational(1, 4096),
            -R_SYMBOL**3,
            sp.Rational(1, 8),
            sp.Rational(1, 2**18),
            sp.Rational(1, 2**21),
            -2 * E_SYMBOL,
        ],
        [
            1,
            sp.Rational(1, 4096),
            sp.Rational(1, 65536),
            R_SYMBOL**4,
            -sp.Rational(1, 16),
            -sp.Rational(1, 2**24),
            -sp.Rational(1, 2**28),
            -2 * E_SYMBOL,
        ],
    ]

    basis = sp.Matrix(rows)
    objective = sp.Matrix(
        [
            1,
            sp.Rational(1, 8),
            sp.Rational(1, 16),
            R_SYMBOL,
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
        "numerator": numerator,
        "denominator": denominator,
        "ratio": sp.cancel(
            numerator / denominator
        ),
    }


def specialized_formula(
    formula: dict[str, sp.Expr],
    maximum: int,
    epsilon: sp.Rational,
) -> sp.Expr:
    return sp.cancel(
        formula["ratio"].subs(
            {
                M_SYMBOL: maximum,
                R_SYMBOL: sp.Rational(
                    1,
                    2**maximum,
                ),
                T_SYMBOL: S**maximum,
                E_SYMBOL: epsilon,
            }
        )
    )


def signature_from_exact_phase(
    maximum: int,
    phase: dict[str, Any],
) -> dict[str, Any]:
    count = maximum + 1
    indices = phase["positive_indices"]

    return {
        "p_support": [
            index
            for index in indices
            if 0 <= index < count
        ],
        "q_support": [
            index - count
            for index in indices
            if count <= index < 2 * count
        ],
        "active_observations": (
            phase["active_observations"]
        ),
    }


def serialize_certificate(
    certificate: dict[str, Any],
) -> dict[str, Any]:
    output = {}

    for key, value in certificate.items():
        if isinstance(value, sp.Basic):
            output[key] = str(value)
        else:
            output[key] = value

    return output


def main() -> None:
    required = [
        A67_SCRIPT,
        A72_M12,
        A73_M13,
        A74_M14,
        A74_M14_CATALOGUE,
        A74_M14_DISCOVERY,
        A73_RESULTS,
    ]

    for path in required:
        if not path.exists():
            raise FileNotFoundError(path)

    a67 = load_module(
        A67_SCRIPT,
        "a67_for_a74",
    )

    m12 = json.loads(
        A72_M12.read_text(
            encoding="utf-8"
        )
    )
    m13 = json.loads(
        A73_M13.read_text(
            encoding="utf-8"
        )
    )
    m14 = json.loads(
        A74_M14.read_text(
            encoding="utf-8"
        )
    )
    catalogue_14 = json.loads(
        A74_M14_CATALOGUE.read_text(
            encoding="utf-8"
        )
    )
    discovery_14 = json.loads(
        A74_M14_DISCOVERY.read_text(
            encoding="utf-8"
        )
    )
    a73 = json.loads(
        A73_RESULTS.read_text(
            encoding="utf-8"
        )
    )

    formula = symbolic_gamma_formula()

    branch_m12_plus = a67.build_branch(
        12,
        sp.Rational(6),
        sp.Rational(1, 120000),
        4,
        (
            0,
            3,
            4,
            12,
            14,
            19,
            20,
            26,
        ),
        (
            ("alpha", 1),
            ("beta", -1),
            ("gamma", 1),
        ),
    )
    branch_m13_plus = a67.build_branch(
        13,
        sp.Rational(13, 2),
        sp.Rational(1, 160000),
        4,
        (
            0,
            3,
            4,
            13,
            15,
            20,
            21,
            28,
        ),
        (
            ("alpha", 1),
            ("beta", -1),
            ("gamma", 1),
        ),
    )
    branch_m13_minus = a67.build_branch(
        13,
        sp.Rational(13, 2),
        sp.Rational(1, 160000),
        4,
        (
            0,
            3,
            4,
            13,
            15,
            20,
            21,
            28,
        ),
        (
            ("alpha", 1),
            ("beta", -1),
            ("gamma", -1),
        ),
    )

    multiplier_m12 = condition_expression(
        branch_m12_plus,
        "active_dual_gamma_+1",
    )
    multiplier_m13_plus = condition_expression(
        branch_m13_plus,
        "active_dual_gamma_+1",
    )
    multiplier_m13_minus = condition_expression(
        branch_m13_minus,
        "active_dual_gamma_-1",
    )

    formula_m12 = specialized_formula(
        formula,
        12,
        sp.Rational(1, 120000),
    )
    formula_m13 = specialized_formula(
        formula,
        13,
        sp.Rational(1, 160000),
    )

    common_lower = {
        "kind": "rational",
        "left": COMMON_LOWER,
        "right": COMMON_LOWER,
    }
    common_upper = {
        "kind": "rational",
        "left": COMMON_UPPER,
        "right": COMMON_UPPER,
    }

    m12_phase = m12["phases"][3]
    m13_phase = m13["phases"][6]

    m13_lower = exact_boundary(
        m13_phase["s_lower"]
    )
    m13_upper = exact_boundary(
        m13_phase["s_upper"]
    )

    common_m12_positive = (
        a67.certify_positive(
            multiplier_m12,
            common_lower,
            common_upper,
        )
    )
    common_m13_plus_negative = (
        a67.certify_positive(
            -multiplier_m13_plus,
            common_lower,
            common_upper,
        )
    )
    common_m13_minus_positive = (
        a67.certify_positive(
            multiplier_m13_minus,
            common_lower,
            common_upper,
        )
    )

    full_m13_plus_negative = (
        a67.certify_positive(
            -multiplier_m13_plus,
            m13_lower,
            m13_upper,
        )
    )
    full_m13_minus_positive = (
        a67.certify_positive(
            multiplier_m13_minus,
            m13_lower,
            m13_upper,
        )
    )

    discovery_signatures = [
        {
            "p_support": phase["p_support"],
            "q_support": phase["q_support"],
            "active_observations": (
                phase["active_observations"]
            ),
        }
        for phase in discovery_14[
            "phases"
        ]
    ]
    exact_signatures = [
        signature_from_exact_phase(
            14,
            phase,
        )
        for phase in m14["phases"]
    ]

    m13_first_signature = (
        signature_from_exact_phase(
            13,
            m13["phases"][0],
        )
    )
    m14_first_signature = (
        exact_signatures[0]
    )

    winner_ratio = sp.Rational(
        catalogue_14["top"][0][
            "primal"
        ]
    )
    boundary_ratio = sp.Rational(
        m14["boundary_ratio"]
    )
    runner_ratio = sp.Rational(
        catalogue_14["top"][1][
            "primal"
        ]
    )

    gates = {
        "A73_previous_audit_passed": bool(
            all(
                a73["gates"].values()
            )
        ),
        "symbolic_Cramer_formula_matches_M12_branch": bool(
            sp.cancel(
                formula_m12
                - multiplier_m12
            )
            == 0
        ),
        "symbolic_Cramer_formula_matches_M13_branch": bool(
            sp.cancel(
                formula_m13
                - multiplier_m13_plus
            )
            == 0
        ),
        "common_interval_inside_exact_M12_and_M13_phases": bool(
            phase_contains_interval(
                m12_phase,
                COMMON_LOWER,
                COMMON_UPPER,
            )
            and phase_contains_interval(
                m13_phase,
                COMMON_LOWER,
                COMMON_UPPER,
            )
        ),
        "M12_gamma_plus_positive_on_common_interval": bool(
            common_m12_positive["ok"]
        ),
        "M13_gamma_plus_negative_on_common_interval": bool(
            common_m13_plus_negative[
                "ok"
            ]
        ),
        "M13_gamma_minus_positive_on_common_interval": bool(
            common_m13_minus_positive[
                "ok"
            ]
        ),
        "M13_gamma_plus_negative_on_complete_phase7_interval": bool(
            full_m13_plus_negative[
                "ok"
            ]
        ),
        "M13_gamma_minus_positive_on_complete_phase7_interval": bool(
            full_m13_minus_positive[
                "ok"
            ]
        ),
        "M14_discovery_and_exact_phase_signatures_match": bool(
            discovery_signatures
            == exact_signatures
        ),
        "M14_exact_global_phase_theorem_passed": bool(
            all(
                m14["gates"].values()
            )
        ),
        "M14_exact_catalogue_has_84_designs": bool(
            catalogue_14["count"]
            == 84
        ),
        "M14_unique_catalogue_winner_2_3_4": bool(
            catalogue_14["winner"]
            == [2, 3, 4]
            and runner_ratio
            > winner_ratio
        ),
        "M14_top_three_exact_primal_dual_values_match": bool(
            all(
                item["equal"]
                for item in catalogue_14[
                    "top"
                ]
            )
        ),
        "M14_catalogue_and_continuous_boundary_values_match": bool(
            winner_ratio
            == boundary_ratio
        ),
        "M14_does_not_copy_M13_phase_grammar": bool(
            m14["phase_count"]
            != m13["phase_count"]
            and m14_first_signature
            != m13_first_signature
        ),
    }

    verdict = (
        "PASS_INTERVAL_STABLE_GAMMA_BIFURCATION_AND_M14_EXTENSION"
        if all(
            gates.values()
        )
        else "FAIL_A74_INTERVAL_BIFURCATION_AUDIT"
    )

    result = {
        "audit": (
            "A74_INTERVAL_STABLE_GAMMA_BIFURCATION_AND_M14_EXTENSION"
        ),
        "symbolic_gamma_multiplier": {
            "signature": (
                "P={0,3,4,M}, Q={1,6,7}, "
                "active={alpha+,beta-,gamma+}"
            ),
            "variables": {
                "R": "2^(-M)",
                "T": "s^M",
                "s": "2^(-alpha)",
            },
            "formula": (
                "lambda_gamma_plus=N/D"
            ),
            "numerator": str(
                formula["numerator"]
            ),
            "denominator": str(
                formula["denominator"]
            ),
            "numerator_character_count": len(
                str(
                    formula[
                        "numerator"
                    ]
                )
            ),
            "denominator_character_count": len(
                str(
                    formula[
                        "denominator"
                    ]
                )
            ),
            "exact_specialization_checks": {
                "M12": gates[
                    "symbolic_Cramer_formula_matches_M12_branch"
                ],
                "M13": gates[
                    "symbolic_Cramer_formula_matches_M13_branch"
                ],
            },
        },
        "support_size_bifurcation": {
            "common_interval_s": {
                "lower": str(
                    COMMON_LOWER
                ),
                "upper": str(
                    COMMON_UPPER
                ),
                "alpha_lower_decimal": str(
                    sp.N(
                        -sp.log(
                            COMMON_UPPER,
                            2,
                        ),
                        50,
                    )
                ),
                "alpha_upper_decimal": str(
                    sp.N(
                        -sp.log(
                            COMMON_LOWER,
                            2,
                        ),
                        50,
                    )
                ),
            },
            "M12_gamma_plus": {
                "sign": "positive",
                "certificate": (
                    serialize_certificate(
                        common_m12_positive
                    )
                ),
            },
            "M13_gamma_plus": {
                "sign": "negative",
                "certificate": (
                    serialize_certificate(
                        common_m13_plus_negative
                    )
                ),
            },
            "M13_gamma_minus": {
                "sign": "positive",
                "certificate": (
                    serialize_certificate(
                        common_m13_minus_positive
                    )
                ),
            },
            "formal_statement": (
                "On one common exact s interval, the same gamma-plus "
                "contact signature changes dual orientation between the "
                "consecutive supports M=12 and M=13."
            ),
        },
        "M13_interval_stability": {
            "phase": 7,
            "phase_s_lower": (
                m13_phase["s_lower"]
            ),
            "phase_s_upper": (
                m13_phase["s_upper"]
            ),
            "gamma_plus_negative": (
                serialize_certificate(
                    full_m13_plus_negative
                )
            ),
            "gamma_minus_positive": (
                serialize_certificate(
                    full_m13_minus_positive
                )
            ),
            "formal_statement": (
                "The inherited gamma-plus multiplier is strictly "
                "negative throughout the complete exact M=13 phase-7 "
                "interval, while the selected gamma-minus multiplier "
                "is strictly positive throughout that interval."
            ),
        },
        "M14": {
            "discovery": discovery_14,
            "exact_phase_result": m14,
            "catalogue": catalogue_14,
            "phase_signatures": (
                exact_signatures
            ),
            "comparison_with_M13": {
                "M13_phase_count": (
                    m13["phase_count"]
                ),
                "M14_phase_count": (
                    m14["phase_count"]
                ),
                "M13_first_signature": (
                    m13_first_signature
                ),
                "M14_first_signature": (
                    m14_first_signature
                ),
            },
            "formal_result": (
                "M=14 has seven exact phases, six simple finite "
                "transitions, unique integer-catalogue winner "
                "{2,3,4}, and strictly increasing first-anchor "
                "risk on alpha in [2,3)."
            ),
        },
        "formal_results": [
            (
                "the gamma-plus dual multiplier has an exact symbolic "
                "Cramer formula for the shared M=12,13 contact family"
            ),
            (
                "the formula changes sign between M=12 and M=13 on "
                "one common exact continuous interval"
            ),
            (
                "the M=13 gamma sign selection is stable across the "
                "complete exact phase-7 interval, not only at one probe"
            ),
            (
                "M=14 was discovered independently and does not repeat "
                "the M=13 phase grammar"
            ),
            (
                "the global first-boundary theorem extends to M=14"
            ),
            (
                "the exact M=14 integer-catalogue winner remains "
                "{2,3,4}"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A74 proves an interval-stable bifurcation for the declared "
            "M=12,13 signature and a separate exact M=14 theorem. It "
            "does not prove a symbolic support-size threshold for every "
            "M or a universal gamma-sign rule."
        ),
    }

    output = HERE / (
        "a74_interval_gamma_bifurcation_results.json"
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
        "common_interval": result[
            "support_size_bifurcation"
        ]["common_interval_s"],
        "M12_gamma_plus": "positive",
        "M13_gamma_plus": "negative",
        "M13_gamma_minus": "positive",
        "M14_phase_count": (
            m14["phase_count"]
        ),
        "M14_transition_count": (
            m14["transition_count"]
        ),
        "M14_catalogue_winner": (
            catalogue_14["winner"]
        ),
        "M14_boundary_risk": (
            m14[
                "boundary_risk_decimal"
            ]
        ),
        "M14_coalescence_risk": (
            m14[
                "coalescence_risk_limit_decimal"
            ]
        ),
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
