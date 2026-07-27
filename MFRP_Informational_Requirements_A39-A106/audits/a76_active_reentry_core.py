#!/usr/bin/env python3
"""A76 exact audit: candidate orientation versus actual active-set selection.

Question
--------
A75 proved that the old candidate signature

    C_M:
      P={0,3,4,M},
      Q={1,h,h+1},
      active={alpha+,beta-,gamma+}

has a positive gamma-plus multiplier again for every M>=22 on

    I=[13/100,33/250].

Does that orientation re-entry cause a real re-entry in the globally optimal
active set?

Answer
------
No, not at M=22.

The actual optimal signature on I uses different contacts:

    A_M:
      P={0,5,6,M},
      Q={1,h,h+1}.

Its exact active-band sequence is:

    M=21: gamma+
    M=22: gamma+
    M=23: gamma-

Thus gamma-plus is already active at M=21, so no active re-entry occurs at
M=22. A real actual-family sign flip occurs at M=23.

Proof layers
------------
1. Exact Bernstein sign certificates for every primal-dual KKT condition of
   the selected branches on the complete interval I.
2. Exact negative certificates for the opposite gamma sign on I.
3. Exact Cramer numerator/determinant orientation for the actual family.
4. Exact proof that the old A75 candidate remains primal-infeasible at M=22
   and M=23 despite its positive gamma-plus multiplier.
5. Complete classification, at s0=131/1000, of all 456 neighbors in the
   declared one-pivot neighborhood of the actual signatures.

The full-alpha phase atlas is numerical discovery only. The interval theorem
and one-pivot classifications are exact rational results.
"""

from __future__ import annotations

import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent

A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"
A73_SCRIPT = HERE / "a73_complete_one_pivot_neighborhood_audit.py"
A75_RESULTS = HERE / "a75_parity_orientation_results.json"
DISCOVERY = HERE / "a76_M21_M23_phase_discovery.json"

S0 = sp.Rational(131, 1000)
INTERVAL_LOWER = sp.Rational(13, 100)
INTERVAL_UPPER = sp.Rational(33, 250)

T = sp.Symbol("t")


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)

    return json.loads(
        path.read_text(encoding="utf-8")
    )


def normalized_epsilon(maximum: int) -> sp.Rational:
    h = maximum // 2

    if maximum % 2 == 0:
        return sp.Rational(
            1,
            1875 * 2**h,
        )

    return sp.Rational(
        1,
        2500 * 2**h,
    )


def bernstein_coefficients(
    polynomial: sp.Poly,
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
                polynomial.gens[0],
                INTERVAL_LOWER
                + (
                    INTERVAL_UPPER
                    - INTERVAL_LOWER
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


def polynomial_sign(
    polynomial_expression: sp.Expr,
    variable: sp.Symbol,
) -> dict[str, Any]:
    polynomial = sp.Poly(
        polynomial_expression,
        variable,
        domain=sp.QQ,
    )
    coefficients = bernstein_coefficients(
        polynomial
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
        "degree": polynomial.degree(),
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


def rational_sign(
    expression: sp.Expr,
    variable: sp.Symbol,
) -> dict[str, Any]:
    numerator, denominator = sp.fraction(
        sp.cancel(expression)
    )

    numerator_certificate = polynomial_sign(
        numerator,
        variable,
    )
    denominator_certificate = polynomial_sign(
        denominator,
        variable,
    )

    return {
        "sign": (
            numerator_certificate["sign"]
            * denominator_certificate["sign"]
        ),
        "numerator": (
            numerator_certificate
        ),
        "denominator": (
            denominator_certificate
        ),
    }


def actual_positive_indices(
    maximum: int,
) -> tuple[int, ...]:
    count = maximum + 1
    h = maximum // 2

    return (
        0,
        5,
        6,
        maximum,
        count + 1,
        count + h,
        count + h + 1,
        2 * count,
    )


def old_candidate_indices(
    maximum: int,
) -> tuple[int, ...]:
    count = maximum + 1
    h = maximum // 2

    return (
        0,
        3,
        4,
        maximum,
        count + 1,
        count + h,
        count + h + 1,
        2 * count,
    )


def actual_active_observations(
    maximum: int,
) -> tuple[tuple[str, int], ...]:
    gamma_sign = (
        1
        if maximum in {21, 22}
        else -1
    )

    return (
        ("alpha", 1),
        ("beta", -1),
        ("gamma", gamma_sign),
    )


def build_branch(
    a67,
    maximum: int,
    positive_indices: tuple[int, ...],
    active_observations: tuple[
        tuple[str, int],
        ...,
    ],
):
    return a67.build_branch(
        maximum,
        sp.Rational(maximum, 2),
        normalized_epsilon(maximum),
        4,
        positive_indices,
        active_observations,
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


def actual_gamma_determinants(
    maximum: int,
) -> dict[str, sp.Expr]:
    h = maximum // 2
    epsilon = normalized_epsilon(
        maximum
    )
    mean = sp.Rational(
        maximum,
        2,
    )

    p_points = [
        0,
        5,
        6,
        maximum,
    ]
    q_points = [
        1,
        h,
        h + 1,
    ]

    target = lambda x: sp.Rational(
        1,
        2**x,
    )
    beta = lambda x: sp.Rational(
        1,
        2 ** (3 * x),
    )
    gamma = lambda x: sp.Rational(
        1,
        2 ** (4 * x),
    )

    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [
            *p_points,
            0,
            0,
            0,
            -mean,
        ],
        [
            0,
            0,
            0,
            0,
            *q_points,
            -mean,
        ],
        [
            0,
            0,
            0,
            0,
            *[
                target(x)
                for x in q_points
            ],
            0,
        ],
        [
            *[
                sp.Symbol("s") ** x
                for x in p_points
            ],
            *[
                -sp.Symbol("s") ** x
                for x in q_points
            ],
            -2 * epsilon,
        ],
        [
            *[
                -beta(x)
                for x in p_points
            ],
            *[
                beta(x)
                for x in q_points
            ],
            -2 * epsilon,
        ],
        [
            *[
                gamma(x)
                for x in p_points
            ],
            *[
                -gamma(x)
                for x in q_points
            ],
            -2 * epsilon,
        ],
    ]

    variable = sp.Symbol("s")
    basis = sp.Matrix(rows)
    objective = sp.Matrix(
        [
            *[
                target(x)
                for x in p_points
            ],
            0,
            0,
            0,
            0,
        ]
    )

    numerator_basis = basis.copy()
    numerator_basis[7, :] = (
        objective.T
    )

    return {
        "variable": variable,
        "numerator": sp.factor(
            numerator_basis.det()
        ),
        "denominator": sp.factor(
            basis.det()
        ),
    }


def actual_signature(
    maximum: int,
) -> dict[str, Any]:
    h = maximum // 2
    gamma_sign = (
        1
        if maximum in {21, 22}
        else -1
    )

    return {
        "p_support": [
            0,
            5,
            6,
            maximum,
        ],
        "q_support": [
            1,
            h,
            h + 1,
        ],
        "active_observations": [
            ["alpha", 1],
            ["beta", -1],
            ["gamma", gamma_sign],
        ],
    }


def generate_neighbors(
    maximum: int,
) -> list[dict[str, Any]]:
    h = maximum // 2
    p_reference = {
        0,
        5,
        6,
        maximum,
    }
    q_reference = {
        1,
        h,
        h + 1,
    }
    active_reference = tuple(
        tuple(item)
        for item
        in actual_signature(maximum)[
            "active_observations"
        ]
    )

    candidates = []
    seen = set()

    def add(
        kind: str,
        detail: Any,
        p_support: set[int],
        q_support: set[int],
        active_observations: tuple[
            tuple[str, int],
            ...,
        ],
        is_reference: bool = False,
    ) -> None:
        key = (
            tuple(sorted(p_support)),
            tuple(sorted(q_support)),
            tuple(active_observations),
        )

        if key in seen:
            return

        seen.add(key)
        candidates.append(
            {
                "kind": kind,
                "detail": detail,
                "p_support": sorted(
                    p_support
                ),
                "q_support": sorted(
                    q_support
                ),
                "active_observations": [
                    list(item)
                    for item
                    in active_observations
                ],
                "is_reference": (
                    is_reference
                ),
            }
        )

    add(
        "reference",
        None,
        p_reference,
        q_reference,
        active_reference,
        is_reference=True,
    )

    for leaving in sorted(
        p_reference
    ):
        for entering in range(
            maximum + 1
        ):
            if entering not in p_reference:
                add(
                    "p_contact_exchange",
                    {
                        "leaving": leaving,
                        "entering": entering,
                    },
                    (
                        p_reference
                        - {leaving}
                    )
                    | {entering},
                    q_reference,
                    active_reference,
                )

    for leaving in sorted(
        q_reference
    ):
        for entering in range(
            maximum + 1
        ):
            if entering not in q_reference:
                add(
                    "q_contact_exchange",
                    {
                        "leaving": leaving,
                        "entering": entering,
                    },
                    p_reference,
                    (
                        q_reference
                        - {leaving}
                    )
                    | {entering},
                    active_reference,
                )

    for channel in [
        "beta",
        "gamma",
    ]:
        flipped = tuple(
            (
                name,
                (
                    -sign
                    if name == channel
                    else sign
                ),
            )
            for name, sign
            in active_reference
        )
        add(
            "completion_band_sign_flip",
            {"channel": channel},
            p_reference,
            q_reference,
            flipped,
        )

    for channel in [
        "beta",
        "gamma",
    ]:
        deactivated = tuple(
            item
            for item
            in active_reference
            if item[0] != channel
        )

        for leaving in sorted(
            p_reference
        ):
            add(
                (
                    "deactivate_band_"
                    "remove_p_contact"
                ),
                {
                    "channel": channel,
                    "leaving": leaving,
                },
                p_reference
                - {leaving},
                q_reference,
                deactivated,
            )

        for leaving in sorted(
            q_reference
        ):
            add(
                (
                    "deactivate_band_"
                    "remove_q_contact"
                ),
                {
                    "channel": channel,
                    "leaving": leaving,
                },
                p_reference,
                q_reference
                - {leaving},
                deactivated,
            )

    return candidates


def discovery_signature_at_probe(
    support_result: dict[str, Any],
    alpha_probe: float,
) -> dict[str, Any]:
    selected = support_result[
        "phases"
    ][0]

    for phase in support_result[
        "phases"
    ]:
        if (
            phase[
                "approx_alpha_start"
            ]
            <= alpha_probe
        ):
            selected = phase
        else:
            break

    return {
        "p_support": selected[
            "p_support"
        ],
        "q_support": selected[
            "q_support"
        ],
        "active_observations": (
            selected[
                "active_observations"
            ]
        ),
    }


def main() -> None:
    a67 = load_module(
        A67_SCRIPT,
        "a67_for_a76",
    )
    a73 = load_module(
        A73_SCRIPT,
        "a73_for_a76",
    )
    a73.S0 = S0

    a75 = load_json(
        A75_RESULTS
    )
    discovery = load_json(
        DISCOVERY
    )

    discovery_map = {
        item["maximum"]: item
        for item
        in discovery["supports"]
    }

    alpha_probe = float(
        sp.N(
            -sp.log(
                S0,
                2,
            ),
            30,
        )
    )

    selected_branches = {}
    selected_interval_certificates = {}
    opposite_sign_certificates = {}
    cramer_certificates = {}
    old_candidate_certificates = {}

    total_condition_count = 0
    condition_gates = []
    opposite_sign_gates = []
    cramer_gates = []

    for maximum in [
        21,
        22,
        23,
    ]:
        active = (
            actual_active_observations(
                maximum
            )
        )
        selected_branch = build_branch(
            a67,
            maximum,
            actual_positive_indices(
                maximum
            ),
            active,
        )
        selected_branches[
            maximum
        ] = selected_branch

        conditions = []

        for name, expression in (
            selected_branch[
                "conditions"
            ]
        ):
            certificate = rational_sign(
                expression,
                a67.S,
            )
            conditions.append(
                {
                    "name": name,
                    "certificate": (
                        certificate
                    ),
                }
            )
            condition_gates.append(
                certificate["sign"]
                == 1
            )

        total_condition_count += len(
            conditions
        )
        selected_interval_certificates[
            str(maximum)
        ] = {
            "signature": (
                actual_signature(
                    maximum
                )
            ),
            "condition_count": len(
                conditions
            ),
            "all_conditions_positive": bool(
                all(
                    item[
                        "certificate"
                    ]["sign"]
                    == 1
                    for item in conditions
                )
            ),
            "conditions": conditions,
            "ratio_at_probe": str(
                sp.factor(
                    selected_branch[
                        "ratio"
                    ].subs(
                        a67.S,
                        S0,
                    )
                )
            ),
            "risk_at_probe_decimal": str(
                sp.N(
                    sp.log(
                        selected_branch[
                            "ratio"
                        ].subs(
                            a67.S,
                            S0,
                        )
                    )
                    / (
                        2
                        * sp.log(2)
                    ),
                    50,
                )
            ),
        }

        opposite_gamma_sign = (
            -active[-1][1]
        )
        opposite_branch = build_branch(
            a67,
            maximum,
            actual_positive_indices(
                maximum
            ),
            (
                ("alpha", 1),
                ("beta", -1),
                (
                    "gamma",
                    opposite_gamma_sign,
                ),
            ),
        )
        condition_name = (
            "active_dual_gamma_"
            + (
                "+1"
                if opposite_gamma_sign
                > 0
                else "-1"
            )
        )
        opposite_multiplier = (
            condition_expression(
                opposite_branch,
                condition_name,
            )
        )
        opposite_certificate = (
            rational_sign(
                opposite_multiplier,
                a67.S,
            )
        )
        opposite_sign_gates.append(
            opposite_certificate[
                "sign"
            ]
            == -1
        )
        opposite_sign_certificates[
            str(maximum)
        ] = {
            "opposite_gamma_sign": (
                opposite_gamma_sign
            ),
            "multiplier_name": (
                condition_name
            ),
            "multiplier": str(
                opposite_multiplier
            ),
            "certificate": (
                opposite_certificate
            ),
            "value_at_probe": str(
                sp.factor(
                    opposite_multiplier.subs(
                        a67.S,
                        S0,
                    )
                )
            ),
        }

        determinants = (
            actual_gamma_determinants(
                maximum
            )
        )
        numerator_certificate = (
            polynomial_sign(
                determinants[
                    "numerator"
                ],
                determinants[
                    "variable"
                ],
            )
        )
        denominator_certificate = (
            polynomial_sign(
                determinants[
                    "denominator"
                ],
                determinants[
                    "variable"
                ],
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
        expected_plus_sign = (
            1
            if maximum
            in {21, 22}
            else -1
        )
        cramer_gates.append(
            multiplier_sign
            == expected_plus_sign
        )
        cramer_certificates[
            str(maximum)
        ] = {
            "gamma_plus_numerator": str(
                determinants[
                    "numerator"
                ]
            ),
            "gamma_plus_denominator": str(
                determinants[
                    "denominator"
                ]
            ),
            "numerator_certificate": (
                numerator_certificate
            ),
            "denominator_certificate": (
                denominator_certificate
            ),
            "gamma_plus_multiplier_sign": (
                multiplier_sign
            ),
        }

    # The old A75 candidate becomes positively oriented at M=22 and M=23,
    # but it is still primal-infeasible.
    finite_a75 = {
        record["maximum"]: record
        for record in a75[
            "finite_Bernstein_certificates"
        ]
    }

    for maximum in [
        22,
        23,
    ]:
        old_branch = build_branch(
            a67,
            maximum,
            old_candidate_indices(
                maximum
            ),
            (
                ("alpha", 1),
                ("beta", -1),
                ("gamma", 1),
            ),
        )
        negative_basic = (
            condition_expression(
                old_branch,
                "basic_4",
            )
        )
        basic_certificate = (
            rational_sign(
                negative_basic,
                a67.S,
            )
        )

        old_candidate_certificates[
            str(maximum)
        ] = {
            "A75_gamma_plus_multiplier_sign": (
                finite_a75[
                    maximum
                ][
                    "multiplier_sign"
                ]
            ),
            "basic_4": str(
                negative_basic
            ),
            "basic_4_certificate": (
                basic_certificate
            ),
            "basic_4_value_at_probe": str(
                sp.factor(
                    negative_basic.subs(
                        a67.S,
                        S0,
                    )
                )
            ),
            "conclusion": (
                "Positive multiplier orientation does not "
                "restore primal feasibility."
            ),
        }

    # Complete declared one-pivot neighborhood at the exact probe.
    candidate_records = []
    support_summaries = {}
    combined_neighbor_counts = (
        Counter()
    )
    combined_reference_counts = (
        Counter()
    )
    pivot_type_counts = defaultdict(
        Counter
    )

    for maximum in [
        21,
        22,
        23,
    ]:
        candidates = generate_neighbors(
            maximum
        )
        counts_neighbors = Counter()
        counts_all = Counter()
        strict_optima = []

        for candidate_index, candidate in enumerate(
            candidates,
            start=1,
        ):
            evaluation = (
                a73.exact_basis_evaluation(
                    maximum,
                    candidate,
                )
            )
            compact_failure = {
                "negative_basic": (
                    evaluation.get("negative_basic", [])[:1]
                ),
                "negative_active_dual": (
                    evaluation.get("negative_active_dual", [])[:1]
                ),
                "negative_reduced_cost": (
                    evaluation.get("negative_reduced_cost", [])[:1]
                ),
                "negative_inactive_slack": (
                    evaluation.get("negative_inactive_slack", [])[:1]
                ),
            }
            record = {
                "maximum": maximum,
                "candidate_index": candidate_index,
                **candidate,
                "classification": evaluation["classification"],
                "strict_local_optimum": evaluation[
                    "strict_local_optimum"
                ],
                "negative_counts": evaluation.get(
                    "negative_counts",
                    {},
                ),
                "first_failure": compact_failure,
            }
            candidate_records.append(record)

            classification = (
                evaluation[
                    "classification"
                ]
            )
            counts_all[
                classification
            ] += 1
            combined_reference_counts[
                classification
            ] += 1

            if not candidate[
                "is_reference"
            ]:
                counts_neighbors[
                    classification
                ] += 1
                combined_neighbor_counts[
                    classification
                ] += 1
                pivot_type_counts[
                    candidate["kind"]
                ][classification] += 1

            if evaluation[
                "strict_local_optimum"
            ]:
                strict_optima.append(
                    {
                        "candidate_index": (
                            candidate_index
                        ),
                        "kind": candidate[
                            "kind"
                        ],
                        "detail": candidate[
                            "detail"
                        ],
                        "p_support": candidate[
                            "p_support"
                        ],
                        "q_support": candidate[
                            "q_support"
                        ],
                        "active_observations": (
                            candidate[
                                "active_observations"
                            ]
                        ),
                    }
                )

        support_summaries[
            str(maximum)
        ] = {
            "candidate_count_including_reference": len(
                candidates
            ),
            "single_pivot_neighbor_count": (
                len(candidates)
                - 1
            ),
            "classification_counts_including_reference": dict(
                counts_all
            ),
            "classification_counts_neighbors": dict(
                counts_neighbors
            ),
            "strict_local_optima": (
                strict_optima
            ),
        }

    discovery_checks = {}

    for maximum in [
        21,
        22,
        23,
    ]:
        observed = (
            discovery_signature_at_probe(
                discovery_map[
                    maximum
                ],
                alpha_probe,
            )
        )
        expected = actual_signature(
            maximum
        )
        discovery_checks[
            str(maximum)
        ] = {
            "observed": observed,
            "expected": expected,
            "matches": bool(
                observed == expected
            ),
        }

    gates = {
        "A75_previous_audit_passed": bool(
            all(
                a75["gates"].values()
            )
        ),
        "numerical_discovery_has_seven_phases_each": bool(
            all(
                discovery_map[
                    maximum
                ]["phase_count"]
                == 7
                for maximum
                in [21, 22, 23]
            )
        ),
        "discovery_signature_at_probe_matches_exact_branch": bool(
            all(
                item["matches"]
                for item
                in discovery_checks.values()
            )
        ),
        "all_159_selected_branch_KKT_conditions_positive_on_interval": bool(
            total_condition_count
            == 159
            and all(
                condition_gates
            )
        ),
        "opposite_gamma_sign_multiplier_negative_for_all_three_supports": bool(
            len(
                opposite_sign_gates
            )
            == 3
            and all(
                opposite_sign_gates
            )
        ),
        "actual_gamma_plus_Cramer_orientation_is_plus_plus_minus": bool(
            len(
                cramer_gates
            )
            == 3
            and all(
                cramer_gates
            )
        ),
        "actual_M21_M22_gamma_plus_and_M23_gamma_minus_selected": bool(
            all(
                selected_interval_certificates[
                    str(maximum)
                ][
                    "all_conditions_positive"
                ]
                for maximum
                in [21, 22, 23]
            )
        ),
        "A75_old_candidate_positive_at_M22_M23_but_primal_infeasible": bool(
            all(
                old_candidate_certificates[
                    str(maximum)
                ][
                    "A75_gamma_plus_multiplier_sign"
                ]
                == 1
                and old_candidate_certificates[
                    str(maximum)
                ][
                    "basic_4_certificate"
                ]["sign"]
                == -1
                for maximum
                in [22, 23]
            )
        ),
        "all_456_declared_one_pivot_neighbors_enumerated": bool(
            sum(
                summary[
                    "single_pivot_neighbor_count"
                ]
                for summary
                in support_summaries.values()
            )
            == 456
        ),
        "all_459_reference_and_neighbor_bases_nonsingular_and_classified": bool(
            len(
                candidate_records
            )
            == 459
            and not any(
                record[
                    "classification"
                ]
                in {
                    "rank_mismatch",
                    "singular",
                }
                for record
                in candidate_records
            )
        ),
        "each_actual_reference_is_unique_strict_local_optimum": bool(
            all(
                len(
                    support_summaries[
                        str(maximum)
                    ][
                        "strict_local_optima"
                    ]
                )
                == 1
                and support_summaries[
                    str(maximum)
                ][
                    "strict_local_optima"
                ][0]["kind"]
                == "reference"
                for maximum
                in [21, 22, 23]
            )
        ),
        "no_declared_neighbor_is_locally_optimal": bool(
            combined_neighbor_counts.get(
                "locally_optimal",
                0,
            )
            == 0
        ),
        "combined_neighbor_failure_counts_match": bool(
            dict(
                combined_neighbor_counts
            )
            == {
                "primal_infeasible": 329,
                "active_dual_multiplier_infeasible": 55,
                "reduced_cost_infeasible": 68,
                "inactive_observation_slack_infeasible": 4,
            }
        ),
    }

    verdict = (
        "PASS_NO_ACTIVE_REENTRY_AT_M22_AND_ACTUAL_SIGN_FLIP_AT_M23"
        if all(
            gates.values()
        )
        else "FAIL_A76_ACTIVE_REENTRY_AUDIT"
    )

    result = {
        "audit": (
            "A76_CANDIDATE_ORIENTATION_VERSUS_ACTUAL_ACTIVE_SET"
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
            "probe_s": str(
                S0
            ),
            "probe_alpha_decimal": str(
                sp.N(
                    -sp.log(
                        S0,
                        2,
                    ),
                    50,
                )
            ),
        },
        "candidate_versus_actual": {
            "A75_old_candidate": (
                "P={0,3,4,M}, "
                "Q={1,floor(M/2),floor(M/2)+1}"
            ),
            "actual_family": (
                "P={0,5,6,M}, "
                "Q={1,floor(M/2),floor(M/2)+1}"
            ),
            "A75_candidate_gamma_plus_signs": {
                "21": finite_a75[
                    21
                ][
                    "multiplier_sign"
                ],
                "22": finite_a75[
                    22
                ][
                    "multiplier_sign"
                ],
                "23": finite_a75[
                    23
                ][
                    "multiplier_sign"
                ],
            },
            "actual_selected_gamma_signs": {
                "21": 1,
                "22": 1,
                "23": -1,
            },
            "formal_statement": (
                "The A75 orientation re-entry at M=22 is not an "
                "active-set re-entry. The actual optimizer already "
                "uses gamma-plus at M=21 and M=22, then flips to "
                "gamma-minus at M=23."
            ),
        },
        "selected_interval_certificates": (
            selected_interval_certificates
        ),
        "opposite_sign_certificates": (
            opposite_sign_certificates
        ),
        "actual_Cramer_certificates": (
            cramer_certificates
        ),
        "old_candidate_primal_infeasibility": (
            old_candidate_certificates
        ),
        "discovery_checks": (
            discovery_checks
        ),
        "declared_one_pivot_neighborhood": {
            "moves": [
                "exchange one P contact",
                "exchange one Q contact",
                "flip beta or gamma active-band sign",
                (
                    "deactivate beta or gamma while one active "
                    "P or Q contact leaves the reduced basis"
                ),
            ],
            "excluded_moves": [
                "scale-variable exchange",
                "alpha sign flip or deactivation",
                "two-contact exchange",
                "combined contact and sign exchange",
                "complete LP-basis enumeration",
            ],
            "neighbor_counts": {
                "21": 145,
                "22": 152,
                "23": 159,
                "total": 456,
            },
            "support_summaries": (
                support_summaries
            ),
            "combined_neighbor_classification_counts": dict(
                combined_neighbor_counts
            ),
            "pivot_type_classification_counts": {
                kind: dict(counts)
                for kind, counts
                in pivot_type_counts.items()
            },
        },
        "candidate_records": (
            candidate_records
        ),
        "numerical_phase_discovery": (
            discovery
        ),
        "formal_results": [
            (
                "the old candidate orientation re-entry at M=22 "
                "does not correspond to active-set re-entry"
            ),
            (
                "the actual optimal contact family is different "
                "from the A75 candidate family"
            ),
            (
                "all 159 exact KKT conditions of the selected "
                "M=21,22,23 branches are positive on the full "
                "declared interval"
            ),
            (
                "the opposite gamma sign has a strictly negative "
                "active multiplier in every support"
            ),
            (
                "the actual gamma-plus Cramer numerator changes "
                "sign between M=22 and M=23 while the determinant "
                "stays positive"
            ),
            (
                "the old M=22 and M=23 A75 candidate remains "
                "primal-infeasible despite positive gamma-plus "
                "orientation"
            ),
            (
                "all 456 declared one-pivot neighbors are rejected "
                "and each actual reference is the unique strict "
                "local optimum at the exact probe"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A76 is exact on the declared interval and exact at the "
            "one-pivot probe. The seven-phase full-alpha atlases are "
            "numerical discovery artifacts, not complete algebraic "
            "global phase theorems for M=21,22,23."
        ),
    }

    output = HERE / (
        "a76_active_reentry_results.json"
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
        "candidate_gamma_plus_signs": (
            result[
                "candidate_versus_actual"
            ][
                "A75_candidate_gamma_plus_signs"
            ]
        ),
        "actual_selected_gamma_signs": (
            result[
                "candidate_versus_actual"
            ][
                "actual_selected_gamma_signs"
            ]
        ),
        "selected_condition_counts": {
            maximum: item[
                "condition_count"
            ]
            for maximum, item
            in selected_interval_certificates.items()
        },
        "neighbor_counts": result[
            "declared_one_pivot_neighborhood"
        ]["neighbor_counts"],
        "neighbor_failure_counts": result[
            "declared_one_pivot_neighborhood"
        ][
            "combined_neighbor_classification_counts"
        ],
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
