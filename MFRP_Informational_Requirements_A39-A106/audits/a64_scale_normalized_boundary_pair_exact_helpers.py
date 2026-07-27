#!/usr/bin/env python3
"""A64 audit: scale-normalized noise and boundary-pair stress atlas.

Exact theorem layer
-------------------
For X supported on {0,...,M} with known mean m and target exponent mu>0,

    L_mu(P) = E[2^(-mu X)]

has the sharp lower bound given by the linear interpolation of 2^(-mu x)
between floor(m) and ceil(m). This defines the dimensionless noise contract

    epsilon_abs = delta * ell_mu(M,m).

Direct target ambiguity is then bounded by the scale-free ratio 1+2 delta.

Atlas layer
-----------
The three-anchor integer catalogue {mu+1,...,mu+9} is exhaustively audited
over 240 contracts:

- M in {5,6,7,8,9};
- mean/M in {1/4,1/3,2/5,1/2};
- mu in {1,2,3};
- delta in {0,1/7500,1/1875,1/750}.

Every design is solved independently by:
- a scaled primal LP;
- its explicit scaled dual LP.

Critical ties are recomputed with exact rational SymPy primal and dual LPs.

Logical goal
------------
Test the strongest statement compatible with the data:

    At least one minimax-optimal design contains
    {mu+1, mu+2}.

The audit explicitly tests and rejects the stronger uniqueness claim when
exact ties occur.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp
from scipy.optimize import linprog
from sympy.solvers.simplex import lpmax, lpmin


HERE = Path(__file__).resolve().parent
A63_RESULTS = HERE / "a63_structural_generalization_results.json"

SUPPORT_MAXIMA = [5, 6, 7, 8, 9]
MEAN_FRACTIONS = [
    sp.Rational(1, 4),
    sp.Rational(1, 3),
    sp.Rational(2, 5),
    sp.Rational(1, 2),
]
TARGET_EXPONENTS = [1, 2, 3]
DELTA_LEVELS = [
    sp.Rational(0),
    sp.Rational(1, 7500),
    sp.Rational(1, 1875),
    sp.Rational(1, 750),
]
CATALOGUE_WIDTH = 9
NUMERICAL_TIE_TOLERANCE = 2e-9


def sharp_lower_bound(
    maximum: int,
    mean: sp.Rational,
    exponent: int,
) -> sp.Rational:
    lower = int(sp.floor(mean))

    if mean == lower:
        return sp.Rational(
            1,
            2 ** (exponent * lower),
        )

    upper = lower + 1
    return sp.factor(
        (upper - mean)
        * sp.Rational(
            1,
            2 ** (exponent * lower),
        )
        + (mean - lower)
        * sp.Rational(
            1,
            2 ** (exponent * upper),
        )
    )


def lower_bound_certificate(
    maximum: int,
    mean: sp.Rational,
    exponent: int,
) -> dict[str, Any]:
    lower = int(sp.floor(mean))
    upper = lower if mean == lower else lower + 1

    if lower == upper:
        slope = (
            sp.Rational(
                1,
                2 ** (exponent * (lower + 1)),
            )
            - sp.Rational(
                1,
                2 ** (exponent * lower),
            )
        )
        intercept = (
            sp.Rational(
                1,
                2 ** (exponent * lower),
            )
            - slope * lower
        )
    else:
        value_lower = sp.Rational(
            1,
            2 ** (exponent * lower),
        )
        value_upper = sp.Rational(
            1,
            2 ** (exponent * upper),
        )
        slope = value_upper - value_lower
        intercept = value_lower - slope * lower

    residuals = []
    for x in range(maximum + 1):
        function_value = sp.Rational(
            1,
            2 ** (exponent * x),
        )
        affine_value = intercept + slope * x
        residuals.append(
            sp.factor(
                function_value - affine_value
            )
        )

    candidate = sharp_lower_bound(
        maximum,
        mean,
        exponent,
    )
    affine_at_mean = sp.factor(
        intercept + slope * mean
    )

    return {
        "lower_integer": lower,
        "upper_integer": upper,
        "slope": str(slope),
        "intercept": str(intercept),
        "residuals": [
            str(value)
            for value in residuals
        ],
        "all_residuals_nonnegative": bool(
            all(value >= 0 for value in residuals)
        ),
        "affine_at_mean_equals_candidate": bool(
            affine_at_mean == candidate
        ),
        "candidate": str(candidate),
    }


def transform_values(
    maximum: int,
    exponent: int,
) -> np.ndarray:
    support = np.arange(maximum + 1, dtype=float)
    return 2.0 ** (-exponent * support)


def build_scaled_numeric_problem(
    maximum: int,
    mean: sp.Rational,
    target_exponent: int,
    epsilon: sp.Rational,
    design: tuple[int, int, int],
):
    support = np.arange(maximum + 1, dtype=float)
    count = maximum + 1
    dimension = 2 * count + 1

    target_lower = float(
        sharp_lower_bound(
            maximum,
            mean,
            target_exponent,
        )
    )
    target = (
        transform_values(
            maximum,
            target_exponent,
        )
        / target_lower
    )

    objective = np.zeros(dimension)
    objective[:count] = target

    equality_rows = []
    equality_rhs = []

    row = np.zeros(dimension)
    row[:count] = 1.0
    row[-1] = -1.0
    equality_rows.append(row)
    equality_rhs.append(0.0)

    row = np.zeros(dimension)
    row[count:2 * count] = 1.0
    row[-1] = -1.0
    equality_rows.append(row)
    equality_rhs.append(0.0)

    row = np.zeros(dimension)
    row[:count] = support / maximum
    row[-1] = -float(mean) / maximum
    equality_rows.append(row)
    equality_rhs.append(0.0)

    row = np.zeros(dimension)
    row[count:2 * count] = support / maximum
    row[-1] = -float(mean) / maximum
    equality_rows.append(row)
    equality_rhs.append(0.0)

    row = np.zeros(dimension)
    row[count:2 * count] = target
    equality_rows.append(row)
    equality_rhs.append(1.0)

    inequality_rows = []
    inequality_rhs = []

    for exponent in design:
        observation_lower = float(
            sharp_lower_bound(
                maximum,
                mean,
                exponent,
            )
        )
        values = (
            transform_values(
                maximum,
                exponent,
            )
            / observation_lower
        )
        tolerance = (
            2.0
            * float(epsilon)
            / observation_lower
        )

        difference = np.zeros(dimension)
        difference[:count] = values
        difference[count:2 * count] = -values

        if epsilon == 0:
            equality_rows.append(difference)
            equality_rhs.append(0.0)
        else:
            positive = difference.copy()
            positive[-1] = -tolerance
            inequality_rows.append(positive)
            inequality_rhs.append(0.0)

            negative = -difference
            negative[-1] = -tolerance
            inequality_rows.append(negative)
            inequality_rhs.append(0.0)

    return (
        objective,
        np.asarray(equality_rows),
        np.asarray(equality_rhs),
        (
            np.asarray(inequality_rows)
            if inequality_rows
            else np.empty((0, dimension))
        ),
        (
            np.asarray(inequality_rhs)
            if inequality_rhs
            else np.empty(0)
        ),
    )


def numerical_primal_dual(
    maximum: int,
    mean: sp.Rational,
    target_exponent: int,
    epsilon: sp.Rational,
    design: tuple[int, int, int],
) -> tuple[float, float]:
    (
        objective,
        a_eq,
        b_eq,
        a_ub,
        b_ub,
    ) = build_scaled_numeric_problem(
        maximum,
        mean,
        target_exponent,
        epsilon,
        design,
    )

    dimension = len(objective)
    variable_bounds = (
        [(0.0, 1.0)] * (dimension - 1)
        + [(0.0, 1.0)]
    )

    primal = linprog(
        -objective,
        A_ub=(a_ub if len(a_ub) else None),
        b_ub=(b_ub if len(b_ub) else None),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=variable_bounds,
        method="highs-ipm",
        options={
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
            "ipm_optimality_tolerance": 1e-10,
        },
    )
    if not primal.success:
        raise RuntimeError(
            f"Primal failed: M={maximum}, mean={mean}, "
            f"target={target_exponent}, epsilon={epsilon}, "
            f"design={design}: {primal.message}"
        )

    equality_count = len(b_eq)
    inequality_count = len(b_ub)

    dual_objective = np.concatenate(
        [b_eq, b_ub]
    )
    dual_constraint_matrix = np.hstack(
        [
            a_eq.T,
            (
                a_ub.T
                if inequality_count
                else np.empty((dimension, 0))
            ),
        ]
    )

    dual = linprog(
        dual_objective,
        A_ub=-dual_constraint_matrix,
        b_ub=-objective,
        bounds=(
            [(None, None)] * equality_count
            + [(0.0, None)] * inequality_count
        ),
        method="highs-ipm",
        options={
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
            "ipm_optimality_tolerance": 1e-10,
        },
    )
    if not dual.success:
        raise RuntimeError(
            f"Dual failed: M={maximum}, mean={mean}, "
            f"target={target_exponent}, epsilon={epsilon}, "
            f"design={design}: {dual.message}"
        )

    return float(-primal.fun), float(dual.fun)


def build_exact_primal(
    maximum: int,
    mean: sp.Rational,
    target_exponent: int,
    epsilon: sp.Rational,
    design: tuple[int, int, int],
):
    support = list(range(maximum + 1))
    count = maximum + 1

    target = [
        sp.Rational(
            1,
            2 ** (target_exponent * x),
        )
        for x in support
    ]

    yp = sp.symbols(f"yp0:{count}")
    yq = sp.symbols(f"yq0:{count}")
    scale = sp.Symbol("scale")
    variables = list(yp) + list(yq) + [scale]

    objective = sum(
        target[index] * yp[index]
        for index in range(count)
    )

    constraints: list[sp.Rel] = [
        sp.Eq(sum(yp), scale),
        sp.Eq(sum(yq), scale),
        sp.Eq(
            sum(
                support[index] * yp[index]
                for index in range(count)
            ),
            mean * scale,
        ),
        sp.Eq(
            sum(
                support[index] * yq[index]
                for index in range(count)
            ),
            mean * scale,
        ),
        sp.Eq(
            sum(
                target[index] * yq[index]
                for index in range(count)
            ),
            1,
        ),
    ]
    constraints.extend(
        variable >= 0
        for variable in variables
    )

    for exponent in design:
        values = [
            sp.Rational(
                1,
                2 ** (exponent * x),
            )
            for x in support
        ]
        difference = sum(
            values[index]
            * (yp[index] - yq[index])
            for index in range(count)
        )

        if epsilon == 0:
            constraints.append(
                sp.Eq(difference, 0)
            )
        else:
            constraints.extend(
                [
                    difference
                    <= 2 * epsilon * scale,
                    -difference
                    <= 2 * epsilon * scale,
                ]
            )

    return objective, constraints


def exact_primal_value(
    maximum: int,
    mean: sp.Rational,
    target_exponent: int,
    epsilon: sp.Rational,
    design: tuple[int, int, int],
) -> sp.Expr:
    objective, constraints = build_exact_primal(
        maximum,
        mean,
        target_exponent,
        epsilon,
        design,
    )
    value, _ = lpmax(
        objective,
        constraints,
    )
    return sp.factor(value)


def exact_dual_value(
    maximum: int,
    mean: sp.Rational,
    target_exponent: int,
    epsilon: sp.Rational,
    design: tuple[int, int, int],
) -> sp.Expr:
    support = list(range(maximum + 1))
    count = maximum + 1
    dimension = 2 * count + 1

    target = [
        sp.Rational(
            1,
            2 ** (target_exponent * x),
        )
        for x in support
    ]

    a_eq: list[list[sp.Rational]] = []
    b_eq: list[sp.Rational] = []

    row = [sp.Rational(0)] * dimension
    for index in range(count):
        row[index] = 1
    row[-1] = -1
    a_eq.append(row)
    b_eq.append(0)

    row = [sp.Rational(0)] * dimension
    for index in range(count):
        row[count + index] = 1
    row[-1] = -1
    a_eq.append(row)
    b_eq.append(0)

    row = [sp.Rational(0)] * dimension
    for index, x in enumerate(support):
        row[index] = x
    row[-1] = -mean
    a_eq.append(row)
    b_eq.append(0)

    row = [sp.Rational(0)] * dimension
    for index, x in enumerate(support):
        row[count + index] = x
    row[-1] = -mean
    a_eq.append(row)
    b_eq.append(0)

    row = [sp.Rational(0)] * dimension
    for index in range(count):
        row[count + index] = target[index]
    a_eq.append(row)
    b_eq.append(1)

    a_ub: list[list[sp.Rational]] = []
    b_ub: list[sp.Rational] = []

    for exponent in design:
        values = [
            sp.Rational(
                1,
                2 ** (exponent * x),
            )
            for x in support
        ]
        difference = [sp.Rational(0)] * dimension

        for index in range(count):
            difference[index] = values[index]
            difference[count + index] = -values[index]

        if epsilon == 0:
            a_eq.append(difference)
            b_eq.append(0)
        else:
            positive = list(difference)
            positive[-1] = -2 * epsilon
            a_ub.append(positive)
            b_ub.append(0)

            negative = [-value for value in difference]
            negative[-1] = -2 * epsilon
            a_ub.append(negative)
            b_ub.append(0)

    objective = [sp.Rational(0)] * dimension
    for index in range(count):
        objective[index] = target[index]

    equality_count = len(a_eq)
    inequality_count = len(a_ub)

    y_plus = sp.symbols(
        f"dual_plus0:{equality_count}"
    )
    y_minus = sp.symbols(
        f"dual_minus0:{equality_count}"
    )
    inequality = (
        sp.symbols(
            f"dual_ineq0:{inequality_count}"
        )
        if inequality_count
        else ()
    )

    variables = (
        list(y_plus)
        + list(y_minus)
        + list(inequality)
    )

    dual_objective = sum(
        b_eq[index]
        * (y_plus[index] - y_minus[index])
        for index in range(equality_count)
    )
    dual_objective += sum(
        b_ub[index] * inequality[index]
        for index in range(inequality_count)
    )

    constraints: list[sp.Rel] = [
        variable >= 0
        for variable in variables
    ]

    for column in range(dimension):
        expression = sum(
            a_eq[row][column]
            * (y_plus[row] - y_minus[row])
            for row in range(equality_count)
        )
        expression += sum(
            a_ub[row][column]
            * inequality[row]
            for row in range(inequality_count)
        )
        constraints.append(
            expression >= objective[column]
        )

    value, _ = lpmin(
        dual_objective,
        constraints,
    )
    return sp.factor(value)


def main() -> None:
    lower_bound_certificates = []
    lower_bound_gates = []

    contracts = []
    maximum_primal_dual_gap = 0.0
    total_designs = 0

    for maximum in SUPPORT_MAXIMA:
        for fraction in MEAN_FRACTIONS:
            mean = sp.factor(
                maximum * fraction
            )

            for target in TARGET_EXPONENTS:
                certificate = lower_bound_certificate(
                    maximum,
                    mean,
                    target,
                )
                lower_bound_certificates.append(
                    {
                        "maximum": maximum,
                        "mean_fraction": str(fraction),
                        "mean": str(mean),
                        "target_exponent": target,
                        **certificate,
                    }
                )
                lower_bound_gates.extend(
                    [
                        certificate[
                            "all_residuals_nonnegative"
                        ],
                        certificate[
                            "affine_at_mean_equals_candidate"
                        ],
                    ]
                )

                target_lower = sharp_lower_bound(
                    maximum,
                    mean,
                    target,
                )

                catalogue = list(
                    range(
                        target + 1,
                        target + 1 + CATALOGUE_WIDTH,
                    )
                )
                designs = list(
                    itertools.combinations(
                        catalogue,
                        3,
                    )
                )

                for delta in DELTA_LEVELS:
                    epsilon = sp.factor(
                        delta * target_lower
                    )
                    candidates = []

                    for design in designs:
                        primal, dual = numerical_primal_dual(
                            maximum,
                            mean,
                            target,
                            epsilon,
                            design,
                        )
                        gap = abs(primal - dual)
                        maximum_primal_dual_gap = max(
                            maximum_primal_dual_gap,
                            gap,
                        )
                        total_designs += 1

                        candidates.append(
                            {
                                "design": list(design),
                                "primal_ratio": primal,
                                "dual_ratio": dual,
                                "consensus_ratio": (
                                    0.5 * (primal + dual)
                                ),
                                "primal_dual_gap": gap,
                            }
                        )

                    candidates.sort(
                        key=lambda item: item[
                            "consensus_ratio"
                        ]
                    )

                    minimum = candidates[0][
                        "consensus_ratio"
                    ]
                    numerical_optimizers = [
                        item
                        for item in candidates
                        if (
                            item["consensus_ratio"]
                            - minimum
                            <= NUMERICAL_TIE_TOLERANCE
                        )
                    ]

                    boundary_first = target + 1
                    boundary_second = target + 2

                    all_optimizers_first_boundary = all(
                        item["design"][0]
                        == boundary_first
                        for item in numerical_optimizers
                    )
                    boundary_pair_exists = any(
                        item["design"][0]
                        == boundary_first
                        and item["design"][1]
                        == boundary_second
                        for item in numerical_optimizers
                    )
                    all_optimizers_have_pair = all(
                        item["design"][0]
                        == boundary_first
                        and item["design"][1]
                        == boundary_second
                        for item in numerical_optimizers
                    )

                    contracts.append(
                        {
                            "maximum": maximum,
                            "mean_fraction": str(
                                fraction
                            ),
                            "mean": str(mean),
                            "target_exponent": target,
                            "delta": str(delta),
                            "target_lower_bound": str(
                                target_lower
                            ),
                            "epsilon_absolute": str(
                                epsilon
                            ),
                            "winner_numerical": (
                                candidates[0]["design"]
                            ),
                            "winner_ratio_numerical": (
                                candidates[0][
                                    "consensus_ratio"
                                ]
                            ),
                            "runner_numerical": (
                                candidates[1]["design"]
                            ),
                            "runner_ratio_numerical": (
                                candidates[1][
                                    "consensus_ratio"
                                ]
                            ),
                            "numerical_optimizer_count": len(
                                numerical_optimizers
                            ),
                            "numerical_optimizers": [
                                item["design"]
                                for item in numerical_optimizers
                            ],
                            "all_optimizers_first_boundary": bool(
                                all_optimizers_first_boundary
                            ),
                            "boundary_pair_optimizer_exists": bool(
                                boundary_pair_exists
                            ),
                            "all_optimizers_have_boundary_pair": bool(
                                all_optimizers_have_pair
                            ),
                            "maximum_design_primal_dual_gap": max(
                                item["primal_dual_gap"]
                                for item in candidates
                            ),
                            "direct_target_ratio_upper_bound": str(
                                sp.factor(
                                    1 + 2 * delta
                                )
                            ),
                            "direct_target_risk_upper_bound_decimal": str(
                                sp.N(
                                    sp.log(
                                        1 + 2 * delta
                                    )
                                    / (2 * sp.log(2)),
                                    40,
                                )
                            ),
                        }
                    )

    critical_contracts = [
        item
        for item in contracts
        if (
            item["numerical_optimizer_count"] > 1
            or not item[
                "all_optimizers_have_boundary_pair"
            ]
        )
    ]

    exact_critical_results = []
    exact_critical_gates = []

    for item in critical_contracts:
        maximum = item["maximum"]
        mean = sp.Rational(item["mean"])
        target = item["target_exponent"]
        epsilon = sp.Rational(
            item["epsilon_absolute"]
        )

        exact_values = {}
        for design_list in item[
            "numerical_optimizers"
        ]:
            design = tuple(design_list)
            primal = exact_primal_value(
                maximum,
                mean,
                target,
                epsilon,
                design,
            )
            dual = exact_dual_value(
                maximum,
                mean,
                target,
                epsilon,
                design,
            )
            exact_values[
                "-".join(
                    str(value)
                    for value in design
                )
            ] = {
                "primal": str(primal),
                "dual": str(dual),
                "primal_dual_equal": bool(
                    primal == dual
                ),
            }
            exact_critical_gates.append(
                primal == dual
            )

        distinct_values = {
            values["primal"]
            for values in exact_values.values()
        }
        exact_tie = len(distinct_values) == 1

        boundary_pair_designs = [
            key
            for key in exact_values
            if [
                int(value)
                for value in key.split("-")
            ][:2]
            == [target + 1, target + 2]
        ]

        exact_critical_gates.extend(
            [
                exact_tie,
                bool(boundary_pair_designs),
            ]
        )

        exact_critical_results.append(
            {
                "maximum": maximum,
                "mean_fraction": item[
                    "mean_fraction"
                ],
                "mean": item["mean"],
                "target_exponent": target,
                "delta": item["delta"],
                "epsilon_absolute": item[
                    "epsilon_absolute"
                ],
                "exact_values": exact_values,
                "all_exact_values_equal": bool(
                    exact_tie
                ),
                "boundary_pair_designs_in_tie": (
                    boundary_pair_designs
                ),
            }
        )

    all_first_boundary_count = sum(
        item["all_optimizers_first_boundary"]
        for item in contracts
    )
    boundary_pair_exists_count = sum(
        item["boundary_pair_optimizer_exists"]
        for item in contracts
    )
    all_pair_count = sum(
        item[
            "all_optimizers_have_boundary_pair"
        ]
        for item in contracts
    )
    nonunique_count = sum(
        item["numerical_optimizer_count"] > 1
        for item in contracts
    )

    translation_groups = {}
    for item in contracts:
        key = (
            item["maximum"],
            item["mean_fraction"],
            item["delta"],
        )
        translation_groups.setdefault(
            key,
            [],
        ).append(item)

    translation_alignment = {}
    for delta in DELTA_LEVELS:
        selected_groups = [
            group
            for key, group in translation_groups.items()
            if key[2] == str(delta)
        ]
        aligned = 0

        for group in selected_groups:
            offsets = {
                item["winner_numerical"][2]
                - item["target_exponent"]
                for item in group
            }
            if len(offsets) == 1:
                aligned += 1

        translation_alignment[str(delta)] = {
            "aligned_group_count": aligned,
            "group_count": len(
                selected_groups
            ),
            "alignment_fraction": (
                aligned
                / len(selected_groups)
            ),
        }

    fixed_absolute_alignment = None
    normalized_alignment_on_A63_grid = None

    if A63_RESULTS.exists():
        a63 = json.loads(
            A63_RESULTS.read_text(
                encoding="utf-8"
            )
        )

        a63_noisy = [
            item
            for item in a63["contracts"]
            if (
                item["epsilon"] == "1/10000"
                and item["target_exponent"]
                in [1, 2]
            )
        ]

        fixed_groups = {}
        for item in a63_noisy:
            key = (
                item["maximum"],
                item["mean_mode"],
            )
            fixed_groups.setdefault(
                key,
                [],
            ).append(item)

        fixed_aligned = 0
        for group in fixed_groups.values():
            offsets = {
                item["winner"][2]
                - item["target_exponent"]
                for item in group
            }
            if len(offsets) == 1:
                fixed_aligned += 1

        fixed_absolute_alignment = {
            "aligned": fixed_aligned,
            "total": len(fixed_groups),
        }

        normalized_groups = {}
        for item in contracts:
            if (
                item["maximum"]
                in [5, 6, 7, 8]
                and item["mean_fraction"]
                in ["2/5", "1/2"]
                and item["target_exponent"]
                in [1, 2]
                and item["delta"] == "1/1875"
            ):
                key = (
                    item["maximum"],
                    item["mean_fraction"],
                )
                normalized_groups.setdefault(
                    key,
                    [],
                ).append(item)

        normalized_aligned = 0
        for group in normalized_groups.values():
            offsets = {
                item["winner_numerical"][2]
                - item["target_exponent"]
                for item in group
            }
            if len(offsets) == 1:
                normalized_aligned += 1

        normalized_alignment_on_A63_grid = {
            "aligned": normalized_aligned,
            "total": len(
                normalized_groups
            ),
        }

    gates = {
        "all_sharp_lower_bound_certificates_pass": bool(
            all(lower_bound_gates)
        ),
        "all_catalogue_designs_solved_primal_and_dual": bool(
            total_designs
            == (
                len(SUPPORT_MAXIMA)
                * len(MEAN_FRACTIONS)
                * len(TARGET_EXPONENTS)
                * len(DELTA_LEVELS)
                * math.comb(
                    CATALOGUE_WIDTH,
                    3,
                )
            )
        ),
        "maximum_primal_dual_gap_below_1e_minus_7": bool(
            maximum_primal_dual_gap
            < 1e-7
        ),
        "every_optimizer_uses_first_boundary_anchor": bool(
            all_first_boundary_count
            == len(contracts)
        ),
        "boundary_pair_optimizer_exists_in_every_contract": bool(
            boundary_pair_exists_count
            == len(contracts)
        ),
        "critical_numerical_ties_exactly_certified": bool(
            all(exact_critical_gates)
        ),
        "strong_uniqueness_claim_rejected": bool(
            all_pair_count
            < len(contracts)
            and nonunique_count > 0
        ),
        "exact_target_translation_alignment_complete": bool(
            translation_alignment["0"][
                "aligned_group_count"
            ]
            == translation_alignment["0"][
                "group_count"
            ]
        ),
        "normalized_noise_improves_A63_target_alignment": bool(
            fixed_absolute_alignment is not None
            and normalized_alignment_on_A63_grid
            is not None
            and (
                normalized_alignment_on_A63_grid[
                    "aligned"
                ]
                / normalized_alignment_on_A63_grid[
                    "total"
                ]
                >
                fixed_absolute_alignment[
                    "aligned"
                ]
                / fixed_absolute_alignment[
                    "total"
                ]
            )
        ),
    }

    verdict = (
        "PASS_SCALE_NORMALIZED_NOISE_AND_BOUNDARY_PAIR_EXISTENCE_ATLAS"
        if all(gates.values())
        else "FAIL_A64_NORMALIZED_NOISE_BOUNDARY_AUDIT"
    )

    result = {
        "audit": (
            "A64_SCALE_NORMALIZED_NOISE_AND_BOUNDARY_PAIR"
        ),
        "configuration": {
            "support_maxima": SUPPORT_MAXIMA,
            "mean_fractions": [
                str(value)
                for value in MEAN_FRACTIONS
            ],
            "target_exponents": TARGET_EXPONENTS,
            "delta_levels": [
                str(value)
                for value in DELTA_LEVELS
            ],
            "catalogue_rule": (
                "{mu+1,...,mu+9}"
            ),
            "budget": 3,
            "contract_count": len(contracts),
            "designs_per_contract": math.comb(
                CATALOGUE_WIDTH,
                3,
            ),
            "primal_dual_design_count": (
                total_designs
            ),
            "numerical_tie_tolerance": (
                NUMERICAL_TIE_TOLERANCE
            ),
        },
        "sharp_scale_theorem": {
            "lower_bound": (
                "ell_mu(M,m) is the linear interpolation "
                "of 2^(-mu x) between floor(m) and ceil(m)"
            ),
            "noise_contract": (
                "epsilon_abs=delta*ell_mu(M,m)"
            ),
            "direct_target_ratio_bound": (
                "rho_direct<=1+2*delta"
            ),
            "direct_target_risk_bound": (
                "R_direct^Q<=0.5*log2(1+2*delta)"
            ),
            "certificates": (
                lower_bound_certificates
            ),
        },
        "atlas_summary": {
            "contract_count": len(contracts),
            "all_optimizers_first_boundary_count": (
                all_first_boundary_count
            ),
            "boundary_pair_optimizer_exists_count": (
                boundary_pair_exists_count
            ),
            "all_optimizers_have_boundary_pair_count": (
                all_pair_count
            ),
            "nonunique_contract_count": (
                nonunique_count
            ),
            "critical_contract_count": len(
                critical_contracts
            ),
            "maximum_primal_dual_gap": (
                maximum_primal_dual_gap
            ),
            "target_translation_alignment_by_delta": (
                translation_alignment
            ),
            "fixed_absolute_alignment_on_A63_grid": (
                fixed_absolute_alignment
            ),
            "normalized_alignment_on_A63_grid": (
                normalized_alignment_on_A63_grid
            ),
            "correct_boundary_statement": (
                "Within the declared atlas, every optimal "
                "set uses mu+1, and every contract admits "
                "at least one optimum containing "
                "{mu+1,mu+2}. The second anchor is not "
                "necessary in every optimizer because "
                "exact degeneracies occur."
            ),
        },
        "critical_exact_ties": (
            exact_critical_results
        ),
        "contracts": contracts,
        "formal_results": [
            (
                "a sharp target-scale lower bound defines "
                "dimensionless error across different target "
                "exponents and means"
            ),
            (
                "the direct-target ambiguity bound becomes "
                "scale free"
            ),
            (
                "the first boundary anchor appears in every "
                "numerically optimal design in all 240 contracts"
            ),
            (
                "at least one boundary-pair optimizer exists "
                "in every contract"
            ),
            (
                "the stronger unique-boundary-pair claim is "
                "false because exact tied optima exist"
            ),
            (
                "target normalization improves, but does not "
                "perfectly enforce, target-shift alignment"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The sharp lower-bound and direct-target scaling "
            "statements are exact theorems. The boundary-pair "
            "result is an exhaustive integer-catalogue atlas "
            "over the declared compact domain, not yet a "
            "continuous-anchor existence theorem. Exact ties "
            "show that a uniqueness theorem would be false "
            "without extra assumptions."
        ),
    }

    output_path = HERE / (
        "a64_scale_normalized_boundary_pair_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "contract_count": len(contracts),
        "primal_dual_design_count": (
            total_designs
        ),
        "first_boundary_all_optimizers": (
            f"{all_first_boundary_count}/{len(contracts)}"
        ),
        "boundary_pair_exists": (
            f"{boundary_pair_exists_count}/{len(contracts)}"
        ),
        "all_optimizers_have_pair": (
            f"{all_pair_count}/{len(contracts)}"
        ),
        "nonunique_contracts": nonunique_count,
        "critical_contracts": len(
            critical_contracts
        ),
        "maximum_primal_dual_gap": (
            maximum_primal_dual_gap
        ),
        "failed_gates": [
            name
            for name, value in gates.items()
            if not value
        ],
        "verdict": verdict,
    }

    print(json.dumps(summary, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
