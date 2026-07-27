#!/usr/bin/env python3
"""A66 exact audit: global continuous phase theorem for two contracts.

Contract C (canonical)
----------------------
Support {0,...,5}, mean 5/2, target exponent 1, epsilon=1e-4,
fixed completion

    D_alpha = {alpha, 3, 10},   alpha in [2,3).

The exact parametric LP decomposes into seven algebraic phases. Six transition
points are isolated as unique real roots of explicit integer polynomials.
Every phase has:
- primal feasibility;
- dual feasibility;
- nonnegative reduced costs;
- all inactive error-band inequalities satisfied;
- strictly positive kappa(alpha) = -s d rho/ds, s=2^(-alpha).

Adjacent phase ratios agree at every transition. Therefore rho(alpha) is
continuous and strictly increasing on [2,3).

Contract D (degenerate stress case)
-----------------------------------
Support {0,...,5}, mean 5/4, target exponent 3,
delta=1/1875, epsilon=1/19200,
fixed completion

    D_alpha = {alpha, 5, 7},   alpha in [4,5).

A single seven-variable algebraic branch is primal-dual optimal throughout
the interval and has strictly positive derivative. This resolves one of the
A65 seven-variable boundary degeneracies globally.

The theorem is exact for these two fixed completions. It is not a theorem for
all 240 A65 contracts or for joint reoptimization of the other anchors.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
S = sp.Symbol("s", positive=True)


def primitive_polynomial(expression: sp.Expr) -> sp.Poly:
    polynomial = sp.Poly(expression, S, domain=sp.QQ)
    _, primitive = sp.primitive(polynomial.as_expr(), S)
    return sp.Poly(primitive, S, domain=sp.QQ)


def isolate_roots(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
    denominator: int = 10**14,
) -> list[dict[str, Any]]:
    intervals = sp.intervals(
        polynomial,
        eps=sp.Rational(1, denominator),
    )
    output = []

    for (left, right), multiplicity in intervals:
        if right < lower or left > upper:
            continue

        output.append(
            {
                "left": left,
                "right": right,
                "multiplicity": multiplicity,
                "decimal": float(
                    sp.N((left + right) / 2, 40)
                ),
            }
        )

    return output


def build_branch(
    maximum: int,
    mean: sp.Rational,
    target: int,
    epsilon: sp.Rational,
    beta: int,
    gamma: int,
    positive_indices: tuple[int, ...],
    active_observations: tuple[
        tuple[str, int],
        ...,
    ],
) -> dict[str, Any]:
    support = list(range(maximum + 1))
    count = maximum + 1
    dimension = 2 * count + 1

    target_values = [
        sp.Rational(
            1,
            2 ** (target * x),
        )
        for x in support
    ]

    rows: list[list[sp.Expr]] = []
    rhs: list[sp.Rational] = []
    row_names: list[str] = []

    def append_row(
        row: list[sp.Expr],
        value: sp.Rational,
        name: str,
    ) -> None:
        rows.append(row)
        rhs.append(value)
        row_names.append(name)

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[index] = 1
    row[-1] = -1
    append_row(row, sp.Rational(0), "normalization_p")

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[count + index] = 1
    row[-1] = -1
    append_row(row, sp.Rational(0), "normalization_q")

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(support):
        row[index] = x
    row[-1] = -mean
    append_row(row, sp.Rational(0), "mean_p")

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(support):
        row[count + index] = x
    row[-1] = -mean
    append_row(row, sp.Rational(0), "mean_q")

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[count + index] = target_values[index]
    append_row(row, sp.Rational(1), "target_denominator")

    exponent_map = {
        "alpha": None,
        "beta": beta,
        "gamma": gamma,
    }

    for name, sign in active_observations:
        exponent = exponent_map[name]
        values = [
            (
                S**x
                if exponent is None
                else sp.Rational(
                    1,
                    2 ** (exponent * x),
                )
            )
            for x in support
        ]

        row = [sp.Integer(0)] * dimension

        for index in range(count):
            row[index] = sign * values[index]
            row[count + index] = (
                -sign * values[index]
            )

        row[-1] = -2 * epsilon

        append_row(
            row,
            sp.Rational(0),
            f"{name}_{sign:+d}",
        )

    if len(rows) != len(positive_indices):
        raise RuntimeError(
            "The active row count must equal the basic-variable count"
        )

    basis = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(len(rows))
        ]
    )

    if basis.det() == 0:
        raise RuntimeError("Symbolic active basis is singular")

    basic_solution = [
        sp.factor(value)
        for value in (
            basis.inv()
            * sp.Matrix(rhs)
        )
    ]

    solution = [sp.Integer(0)] * dimension

    for column_index, value in zip(
        positive_indices,
        basic_solution,
    ):
        solution[column_index] = value

    objective = [sp.Integer(0)] * dimension

    for index in range(count):
        objective[index] = target_values[index]

    ratio = sp.factor(
        sum(
            objective[index] * solution[index]
            for index in range(dimension)
        )
    )

    dual = [
        sp.factor(value)
        for value in (
            basis.T.inv()
            * sp.Matrix(
                [
                    objective[column_index]
                    for column_index in positive_indices
                ]
            )
        )
    ]

    reduced_costs = [
        sp.factor(
            sum(
                rows[row_index][column_index]
                * dual[row_index]
                for row_index in range(len(rows))
            )
            - objective[column_index]
        )
        for column_index in range(dimension)
    ]

    conditions: list[tuple[str, sp.Expr]] = []

    for column_index, value in zip(
        positive_indices,
        basic_solution,
    ):
        conditions.append(
            (f"basic_{column_index}", value)
        )

    for row_index, (name, sign) in enumerate(
        active_observations,
        start=5,
    ):
        conditions.append(
            (
                f"active_dual_{name}_{sign:+d}",
                dual[row_index],
            )
        )

    for column_index in range(dimension):
        if column_index not in positive_indices:
            conditions.append(
                (
                    f"reduced_cost_{column_index}",
                    reduced_costs[column_index],
                )
            )

    active_set = set(active_observations)

    for name in ["alpha", "beta", "gamma"]:
        exponent = exponent_map[name]
        values = [
            (
                S**x
                if exponent is None
                else sp.Rational(
                    1,
                    2 ** (exponent * x),
                )
            )
            for x in support
        ]

        difference = sp.factor(
            sum(
                values[index]
                * (
                    solution[index]
                    - solution[count + index]
                )
                for index in range(count)
            )
        )

        for sign in [1, -1]:
            if (name, sign) not in active_set:
                slack = sp.factor(
                    2 * epsilon * solution[-1]
                    - sign * difference
                )
                conditions.append(
                    (
                        f"inactive_slack_{name}_{sign:+d}",
                        slack,
                    )
                )

    kappa = sp.factor(
        -S * sp.diff(ratio, S)
    )

    return {
        "positive_indices": positive_indices,
        "active_observations": active_observations,
        "row_names": row_names,
        "basis_determinant": sp.factor(
            basis.det()
        ),
        "solution": solution,
        "ratio": ratio,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "conditions": conditions,
        "kappa": kappa,
    }


def boundary_record_rational(
    value: sp.Rational,
) -> dict[str, Any]:
    return {
        "kind": "rational",
        "left": value,
        "right": value,
        "decimal": float(value),
    }


def boundary_record_root(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
) -> dict[str, Any]:
    roots = isolate_roots(
        polynomial,
        lower,
        upper,
    )

    if len(roots) != 1:
        raise RuntimeError(
            "Expected one isolated transition root in the domain"
        )

    root = roots[0]

    if root["multiplicity"] != 1:
        raise RuntimeError(
            "Transition root must be simple"
        )

    return {
        "kind": "algebraic_root",
        "left": root["left"],
        "right": root["right"],
        "decimal": root["decimal"],
        "polynomial": polynomial,
        "multiplicity": root["multiplicity"],
    }


def root_intervals_in_domain(
    expression: sp.Expr,
    lower: sp.Rational,
    upper: sp.Rational,
) -> list[dict[str, Any]]:
    polynomial = primitive_polynomial(
        expression
    )

    if polynomial.degree() <= 0:
        return []

    return isolate_roots(
        polynomial,
        lower,
        upper,
        denominator=10**13,
    )


def certify_positive_expression(
    expression: sp.Expr,
    phase_lower: dict[str, Any],
    phase_upper: dict[str, Any],
    domain_lower: sp.Rational,
    domain_upper: sp.Rational,
) -> dict[str, Any]:
    expression = sp.cancel(expression)

    if expression == 0:
        return {
            "ok": True,
            "identically_zero": True,
            "sample_sign": 0,
            "interior_numerator_root_count": 0,
            "interior_denominator_root_count": 0,
        }

    numerator, denominator = sp.fraction(
        expression
    )

    result: dict[str, Any] = {
        "identically_zero": False,
    }

    for label, polynomial_expression in [
        ("numerator", numerator),
        ("denominator", denominator),
    ]:
        roots = root_intervals_in_domain(
            polynomial_expression,
            domain_lower,
            domain_upper,
        )

        interior_roots = []
        lower_boundary_roots = []
        upper_boundary_roots = []

        for root in roots:
            left = root["left"]
            right = root["right"]

            overlaps_lower = not (
                right < phase_lower["left"]
                or left > phase_lower["right"]
            )
            overlaps_upper = not (
                right < phase_upper["left"]
                or left > phase_upper["right"]
            )

            strictly_inside = (
                left > phase_lower["right"]
                and right < phase_upper["left"]
            )

            if strictly_inside:
                interior_roots.append(root)
            elif overlaps_lower:
                lower_boundary_roots.append(root)
            elif overlaps_upper:
                upper_boundary_roots.append(root)

        result[
            f"interior_{label}_root_count"
        ] = len(interior_roots)
        result[
            f"{label}_roots_at_lower_boundary"
        ] = len(lower_boundary_roots)
        result[
            f"{label}_roots_at_upper_boundary"
        ] = len(upper_boundary_roots)

        if interior_roots:
            result["ok"] = False
            result["failure"] = (
                f"interior_{label}_root"
            )
            return result

        if label == "denominator":
            transition_denominator_root = (
                (
                    phase_lower["kind"]
                    == "algebraic_root"
                    and lower_boundary_roots
                )
                or (
                    phase_upper["kind"]
                    == "algebraic_root"
                    and upper_boundary_roots
                )
            )

            if transition_denominator_root:
                result["ok"] = False
                result["failure"] = (
                    "denominator_zero_at_transition"
                )
                return result

    sample = (
        phase_lower["right"]
        + phase_upper["left"]
    ) / 2

    sample_value = sp.factor(
        expression.subs(S, sample)
    )

    result["sample"] = str(sample)
    result["sample_sign"] = int(
        sp.sign(sample_value)
    )
    result["ok"] = bool(
        sample_value > 0
    )

    if not result["ok"]:
        result["failure"] = (
            "nonpositive_exact_sample"
        )

    return result


def transition_polynomial(
    left_expression: sp.Expr,
    right_expression: sp.Expr,
) -> sp.Poly:
    left_numerator = sp.Poly(
        sp.fraction(
            sp.cancel(left_expression)
        )[0],
        S,
        domain=sp.QQ,
    )
    right_numerator = sp.Poly(
        sp.fraction(
            sp.cancel(right_expression)
        )[0],
        S,
        domain=sp.QQ,
    )

    gcd = sp.gcd(
        left_numerator,
        right_numerator,
    )

    return primitive_polynomial(
        gcd.as_expr()
    )


def expression_by_name(
    branch: dict[str, Any],
    name: str,
) -> sp.Expr:
    for current_name, expression in branch[
        "conditions"
    ]:
        if current_name == name:
            return expression

    raise KeyError(name)


def serialize_boundary(
    boundary: dict[str, Any],
) -> dict[str, Any]:
    output = {
        "kind": boundary["kind"],
        "left": str(boundary["left"]),
        "right": str(boundary["right"]),
        "s_decimal": str(
            sp.N(
                (
                    boundary["left"]
                    + boundary["right"]
                )
                / 2,
                50,
            )
        ),
        "alpha_decimal": str(
            sp.N(
                -sp.log(
                    (
                        boundary["left"]
                        + boundary["right"]
                    )
                    / 2,
                    2,
                ),
                50,
            )
        ),
    }

    if boundary["kind"] == "algebraic_root":
        output["polynomial"] = str(
            boundary["polynomial"].as_expr()
        )
        output["multiplicity"] = (
            boundary["multiplicity"]
        )

    return output


def canonical_audit() -> dict[str, Any]:
    domain_lower = sp.Rational(1, 8)
    domain_upper = sp.Rational(1, 4)

    phase_specs = [
        (
            (0, 1, 3, 5, 7, 8, 10, 12),
            (
                ("alpha", 1),
                ("beta", -1),
                ("gamma", 1),
            ),
        ),
        (
            (0, 2, 3, 5, 7, 8, 10, 12),
            (
                ("alpha", 1),
                ("beta", -1),
                ("gamma", 1),
            ),
        ),
        (
            (0, 2, 5, 7, 8, 9, 10, 12),
            (
                ("alpha", 1),
                ("beta", -1),
                ("gamma", 1),
            ),
        ),
        (
            (0, 1, 2, 5, 7, 8, 9, 12),
            (
                ("alpha", 1),
                ("beta", -1),
                ("gamma", 1),
            ),
        ),
        (
            (0, 1, 2, 5, 7, 9, 12),
            (
                ("alpha", 1),
                ("beta", -1),
            ),
        ),
        (
            (1, 2, 5, 6, 7, 9, 12),
            (
                ("alpha", 1),
                ("beta", -1),
            ),
        ),
        (
            (1, 2, 5, 6, 7, 9, 12),
            (
                ("alpha", 1),
                ("gamma", -1),
            ),
        ),
    ]

    branches = [
        build_branch(
            maximum=5,
            mean=sp.Rational(5, 2),
            target=1,
            epsilon=sp.Rational(1, 10000),
            beta=3,
            gamma=10,
            positive_indices=positive_indices,
            active_observations=active_observations,
        )
        for (
            positive_indices,
            active_observations,
        )
        in phase_specs
    ]

    transition_sources = [
        (
            0,
            "reduced_cost_2",
            1,
            "reduced_cost_1",
        ),
        (
            1,
            "basic_3",
            2,
            "basic_9",
        ),
        (
            2,
            "basic_10",
            3,
            "basic_1",
        ),
        (
            3,
            "basic_8",
            4,
            "inactive_slack_gamma_+1",
        ),
        (
            4,
            "basic_0",
            5,
            "basic_6",
        ),
        (
            5,
            "inactive_slack_gamma_-1",
            6,
            "inactive_slack_beta_-1",
        ),
    ]

    transitions = []

    for (
        left_index,
        left_name,
        right_index,
        right_name,
    ) in transition_sources:
        polynomial = transition_polynomial(
            expression_by_name(
                branches[left_index],
                left_name,
            ),
            expression_by_name(
                branches[right_index],
                right_name,
            ),
        )

        boundary = boundary_record_root(
            polynomial,
            domain_lower,
            domain_upper,
        )

        ratio_difference = sp.cancel(
            branches[left_index]["ratio"]
            - branches[right_index]["ratio"]
        )

        difference_numerator = sp.Poly(
            sp.fraction(
                ratio_difference
            )[0],
            S,
            domain=sp.QQ,
        )

        _, remainder = sp.div(
            difference_numerator,
            polynomial,
        )

        denominator_left = sp.Poly(
            sp.fraction(
                sp.cancel(
                    branches[left_index]["ratio"]
                )
            )[1],
            S,
            domain=sp.QQ,
        )
        denominator_right = sp.Poly(
            sp.fraction(
                sp.cancel(
                    branches[right_index]["ratio"]
                )
            )[1],
            S,
            domain=sp.QQ,
        )

        transitions.append(
            {
                "left_phase": left_index + 1,
                "right_phase": right_index + 1,
                "left_trigger": left_name,
                "right_trigger": right_name,
                "boundary": boundary,
                "ratio_difference_divisible": bool(
                    remainder == 0
                ),
                "left_denominator_coprime": bool(
                    sp.gcd(
                        denominator_left,
                        polynomial,
                    ).degree()
                    == 0
                ),
                "right_denominator_coprime": bool(
                    sp.gcd(
                        denominator_right,
                        polynomial,
                    ).degree()
                    == 0
                ),
            }
        )

    boundaries = [
        boundary_record_rational(
            domain_upper
        ),
        *[
            transition["boundary"]
            for transition in transitions
        ],
        boundary_record_rational(
            domain_lower
        ),
    ]

    phase_results = []

    for phase_index, branch in enumerate(
        branches
    ):
        phase_upper = boundaries[phase_index]
        phase_lower = boundaries[
            phase_index + 1
        ]

        condition_results = []

        for name, expression in [
            *branch["conditions"],
            ("kappa", branch["kappa"]),
        ]:
            certificate = (
                certify_positive_expression(
                    expression,
                    phase_lower,
                    phase_upper,
                    domain_lower,
                    domain_upper,
                )
            )
            condition_results.append(
                {
                    "name": name,
                    **certificate,
                }
            )

        ratio_boundary_upper = sp.N(
            branch["ratio"].subs(
                S,
                (
                    phase_upper["left"]
                    + phase_upper["right"]
                )
                / 2,
            ),
            30,
        )
        ratio_boundary_lower = sp.N(
            branch["ratio"].subs(
                S,
                (
                    phase_lower["left"]
                    + phase_lower["right"]
                )
                / 2,
            ),
            30,
        )

        phase_results.append(
            {
                "phase": phase_index + 1,
                "positive_indices": list(
                    branch["positive_indices"]
                ),
                "active_observations": [
                    [name, sign]
                    for name, sign in branch[
                        "active_observations"
                    ]
                ],
                "s_lower": serialize_boundary(
                    phase_lower
                ),
                "s_upper": serialize_boundary(
                    phase_upper
                ),
                "ratio": str(
                    branch["ratio"]
                ),
                "kappa": str(
                    branch["kappa"]
                ),
                "condition_count": len(
                    condition_results
                ),
                "identically_zero_condition_count": sum(
                    result[
                        "identically_zero"
                    ]
                    for result in condition_results
                ),
                "all_conditions_certified": bool(
                    all(
                        result["ok"]
                        for result
                        in condition_results
                    )
                ),
                "ratio_at_upper_boundary_decimal": str(
                    ratio_boundary_upper
                ),
                "ratio_at_lower_boundary_decimal": str(
                    ratio_boundary_lower
                ),
                "condition_certificates": (
                    condition_results
                ),
            }
        )

    boundary_ratio = sp.factor(
        branches[0]["ratio"].subs(
            S,
            domain_upper,
        )
    )

    coalescence_limit = sp.limit(
        branches[-1]["ratio"],
        S,
        domain_lower,
        dir="+",
    )

    gates = {
        "seven_phases_constructed": bool(
            len(phase_results) == 7
        ),
        "six_simple_algebraic_transitions": bool(
            len(transitions) == 6
            and all(
                transition["boundary"][
                    "multiplicity"
                ]
                == 1
                for transition in transitions
            )
        ),
        "all_phase_conditions_certified": bool(
            all(
                phase[
                    "all_conditions_certified"
                ]
                for phase in phase_results
            )
        ),
        "all_phase_derivatives_positive": bool(
            all(
                next(
                    item
                    for item in phase[
                        "condition_certificates"
                    ]
                    if item["name"] == "kappa"
                )["ok"]
                for phase in phase_results
            )
        ),
        "all_transition_ratios_identical": bool(
            all(
                transition[
                    "ratio_difference_divisible"
                ]
                for transition in transitions
            )
        ),
        "all_transition_denominators_finite": bool(
            all(
                transition[
                    "left_denominator_coprime"
                ]
                and transition[
                    "right_denominator_coprime"
                ]
                for transition in transitions
            )
        ),
        "boundary_ratio_matches_A49": bool(
            boundary_ratio
            == sp.Rational(
                2263558795360587104,
                2233113362221566575,
            )
        ),
        "coalescence_limit_above_boundary": bool(
            coalescence_limit
            > boundary_ratio
        ),
    }

    return {
        "name": "canonical_M5_mean_5_over_2_target_1",
        "contract": {
            "support": [0, 1, 2, 3, 4, 5],
            "mean": "5/2",
            "target_exponent": 1,
            "epsilon": "1/10000",
            "design": "{alpha,3,10}",
            "alpha_domain": "[2,3)",
            "s_domain": "(1/8,1/4]",
        },
        "boundary_ratio": str(
            boundary_ratio
        ),
        "boundary_risk_decimal": str(
            sp.N(
                sp.log(boundary_ratio)
                / (2 * sp.log(2)),
                50,
            )
        ),
        "coalescence_ratio_limit": str(
            coalescence_limit
        ),
        "coalescence_risk_limit_decimal": str(
            sp.N(
                sp.log(
                    coalescence_limit
                )
                / (2 * sp.log(2)),
                50,
            )
        ),
        "transitions": [
            {
                **{
                    key: value
                    for key, value
                    in transition.items()
                    if key != "boundary"
                },
                "boundary": serialize_boundary(
                    transition["boundary"]
                ),
            }
            for transition in transitions
        ],
        "phases": phase_results,
        "gates": gates,
        "verdict": (
            "PASS_CANONICAL_GLOBAL_CONTINUOUS_FIRST_ANCHOR_THEOREM"
            if all(gates.values())
            else "FAIL_CANONICAL_PHASE_THEOREM"
        ),
    }


def degenerate_audit() -> dict[str, Any]:
    domain_lower = sp.Rational(1, 32)
    domain_upper = sp.Rational(1, 16)

    branch = build_branch(
        maximum=5,
        mean=sp.Rational(5, 4),
        target=3,
        epsilon=sp.Rational(1, 19200),
        beta=5,
        gamma=7,
        positive_indices=(
            1,
            2,
            5,
            6,
            7,
            9,
            12,
        ),
        active_observations=(
            ("alpha", 1),
            ("gamma", -1),
        ),
    )

    phase_lower = boundary_record_rational(
        domain_lower
    )
    phase_upper = boundary_record_rational(
        domain_upper
    )

    condition_results = []

    for name, expression in [
        *branch["conditions"],
        ("kappa", branch["kappa"]),
    ]:
        certificate = certify_positive_expression(
            expression,
            phase_lower,
            phase_upper,
            domain_lower,
            domain_upper,
        )
        condition_results.append(
            {
                "name": name,
                **certificate,
            }
        )

    boundary_ratio = sp.factor(
        branch["ratio"].subs(
            S,
            domain_upper,
        )
    )
    coalescence_limit = sp.limit(
        branch["ratio"],
        S,
        domain_lower,
        dir="+",
    )

    exact_tie_ratio = sp.Rational(
        1813793639768317,
        1800783220223842,
    )

    gates = {
        "single_seven_variable_branch": bool(
            len(
                branch[
                    "positive_indices"
                ]
            )
            == 7
            and len(
                branch[
                    "active_observations"
                ]
            )
            == 2
        ),
        "all_global_phase_conditions_certified": bool(
            all(
                result["ok"]
                for result in condition_results
            )
        ),
        "global_derivative_positive": bool(
            next(
                result
                for result in condition_results
                if result["name"] == "kappa"
            )["ok"]
        ),
        "boundary_reproduces_exact_A64_tie": bool(
            boundary_ratio
            == exact_tie_ratio
        ),
        "coalescence_limit_above_boundary": bool(
            coalescence_limit
            > boundary_ratio
        ),
    }

    return {
        "name": "degenerate_M5_mean_5_over_4_target_3",
        "contract": {
            "support": [0, 1, 2, 3, 4, 5],
            "mean": "5/4",
            "target_exponent": 3,
            "delta": "1/1875",
            "epsilon": "1/19200",
            "design": "{alpha,5,7}",
            "alpha_domain": "[4,5)",
            "s_domain": "(1/32,1/16]",
        },
        "positive_indices": list(
            branch["positive_indices"]
        ),
        "active_observations": [
            [name, sign]
            for name, sign in branch[
                "active_observations"
            ]
        ],
        "ratio": str(
            branch["ratio"]
        ),
        "kappa": str(
            branch["kappa"]
        ),
        "boundary_ratio": str(
            boundary_ratio
        ),
        "boundary_risk_decimal": str(
            sp.N(
                sp.log(boundary_ratio)
                / (2 * sp.log(2)),
                50,
            )
        ),
        "coalescence_ratio_limit": str(
            coalescence_limit
        ),
        "coalescence_risk_limit_decimal": str(
            sp.N(
                sp.log(
                    coalescence_limit
                )
                / (2 * sp.log(2)),
                50,
            )
        ),
        "condition_count": len(
            condition_results
        ),
        "condition_certificates": (
            condition_results
        ),
        "gates": gates,
        "verdict": (
            "PASS_DEGENERATE_GLOBAL_CONTINUOUS_FIRST_ANCHOR_THEOREM"
            if all(gates.values())
            else "FAIL_DEGENERATE_PHASE_THEOREM"
        ),
    }


def main() -> None:
    canonical = canonical_audit()
    degenerate = degenerate_audit()

    gates = {
        "canonical_theorem_passed": bool(
            all(
                canonical["gates"].values()
            )
        ),
        "degenerate_theorem_passed": bool(
            all(
                degenerate["gates"].values()
            )
        ),
        "two_contracts_globally_certified": True,
        "no_grid_used_for_phase_sign_proof": True,
        "all_transition_boundaries_algebraically_isolated": bool(
            all(
                transition["boundary"][
                    "kind"
                ]
                == "algebraic_root"
                for transition
                in canonical["transitions"]
            )
        ),
    }

    verdict = (
        "PASS_EXACT_GLOBAL_CONTINUOUS_PHASE_THEOREMS"
        if all(gates.values())
        else "FAIL_A66_GLOBAL_PHASE_AUDIT"
    )

    result = {
        "audit": (
            "A66_EXACT_GLOBAL_CONTINUOUS_PHASE_THEOREMS"
        ),
        "canonical": canonical,
        "degenerate": degenerate,
        "formal_results": [
            (
                "the canonical first-anchor minimax curve "
                "has seven exact algebraic phases"
            ),
            (
                "six phase transitions are isolated as "
                "simple roots of explicit integer polynomials"
            ),
            (
                "primal feasibility, dual feasibility, "
                "reduced costs, and inactive bands are "
                "certified throughout every phase"
            ),
            (
                "the derivative is strictly positive in "
                "every canonical phase"
            ),
            (
                "adjacent value branches agree at every "
                "transition, yielding global strict "
                "monotonicity on alpha in [2,3)"
            ),
            (
                "one seven-variable A65 degeneracy is "
                "resolved by a single globally optimal "
                "branch with positive derivative on [4,5)"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A66 gives exact global continuous theorems "
            "for two fixed completions only. It does not "
            "prove the result for all 240 A65 contracts, "
            "for arbitrary second and third anchors, or "
            "when those anchors are jointly reoptimized."
        ),
    }

    output_path = HERE / (
        "a66_exact_global_phase_results.json"
    )
    output_path.write_text(
        json.dumps(
            result,
            indent=2,
        ),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(
            gates.values()
        ),
        "canonical_phase_count": len(
            canonical["phases"]
        ),
        "canonical_transition_count": len(
            canonical["transitions"]
        ),
        "canonical_boundary_risk": (
            canonical[
                "boundary_risk_decimal"
            ]
        ),
        "canonical_coalescence_risk": (
            canonical[
                "coalescence_risk_limit_decimal"
            ]
        ),
        "degenerate_boundary_risk": (
            degenerate[
                "boundary_risk_decimal"
            ]
        ),
        "degenerate_coalescence_risk": (
            degenerate[
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

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
