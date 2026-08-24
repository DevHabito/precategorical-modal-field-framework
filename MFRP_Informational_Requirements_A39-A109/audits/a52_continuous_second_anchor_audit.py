#!/usr/bin/env python3
"""A52 exact audit: continuous release of the second anchor.

Exact contract:
    {2, beta, 4} * log(2)
    2 <= beta <= 4

Noisy contract:
    {2, beta, infinity} * log(2)
    epsilon = 1/10000
    2 <= beta <= 4

The audit derives:
- one exact distinct-anchor primal-dual branch;
- duplicate endpoint certificates;
- eight noisy primal-dual phases;
- seven algebraic transitions;
- one unique noisy interior minimizer.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A44_RESULTS = HERE / "a44_continuous_parameter_results.json"
A49_RESULTS = HERE / (
    "a49_expanded_target_excluding_anchor_catalogue_results.json"
)

SUPPORT = list(range(6))
TARGET = [sp.Rational(1, 2**x) for x in SUPPORT]
MEAN = sp.Rational(5, 2)
EPSILON = sp.Rational(1, 10000)

s = sp.symbols("s", real=True)


def row_integer(exponent: int) -> list[sp.Rational]:
    return [
        sp.Rational(1, 2 ** (exponent * x))
        for x in SUPPORT
    ]


ROW2 = row_integer(2)
ROW_BETA = [s**x for x in SUPPORT]
ROW4 = row_integer(4)
ROW_INFINITY = [
    sp.Integer(1),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
]


def dot(
    values: list[sp.Expr],
    weights: list[sp.Expr],
) -> sp.Expr:
    return sp.factor(
        sum(
            values[index] * weights[index]
            for index in range(6)
        )
    )


def symbolic_certificate(
    p_support: list[int],
    q_support: list[int],
    observation_rows: list[list[sp.Expr]],
    active_constraints: list[tuple[int, int]],
    *,
    exact: bool,
) -> dict[str, Any]:
    rows: list[list[sp.Expr]] = []
    rhs: list[sp.Expr] = []

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[index] = 1
    current[12] = -1
    rows.append(current)
    rhs.append(0)

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[6 + index] = 1
    current[12] = -1
    rows.append(current)
    rhs.append(0)

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[index] = index
    current[12] = -MEAN
    rows.append(current)
    rhs.append(0)

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[6 + index] = index
    current[12] = -MEAN
    rows.append(current)
    rhs.append(0)

    current = [sp.Integer(0)] * 13
    for index in range(6):
        current[6 + index] = TARGET[index]
    rows.append(current)
    rhs.append(1)

    equality_count = 5

    if exact:
        for values in observation_rows:
            current = [sp.Integer(0)] * 13
            for index in range(6):
                current[index] = values[index]
                current[6 + index] = -values[index]
            rows.append(current)
            rhs.append(0)
    else:
        for observation_index, sign in active_constraints:
            values = observation_rows[observation_index]
            current = [sp.Integer(0)] * 13
            for index in range(6):
                current[index] = sign * values[index]
                current[6 + index] = -sign * values[index]
            current[12] = -2 * EPSILON
            rows.append(current)
            rhs.append(0)

    positive_indices = (
        p_support
        + [6 + index for index in q_support]
        + [12]
    )

    matrix = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(len(rows))
        ]
    )

    if matrix.rows != matrix.cols:
        raise RuntimeError("Active system is not square")

    solution = matrix.inv() * sp.Matrix(rhs)

    z = [sp.Integer(0)] * 13
    for index, value in zip(positive_indices, solution):
        z[index] = sp.factor(value)

    objective = [sp.Integer(0)] * 13
    for index in range(6):
        objective[index] = TARGET[index]

    ratio = sp.factor(
        sum(
            objective[index] * z[index]
            for index in range(13)
        )
    )

    dual_matrix = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for row_index in range(len(rows))
            ]
            for column_index in positive_indices
        ]
    )

    dual_solution = dual_matrix.inv() * sp.Matrix(
        [objective[index] for index in positive_indices]
    )
    dual = [sp.factor(value) for value in dual_solution]

    reduced_costs = [
        sp.factor(
            sum(
                rows[row_index][column_index]
                * dual[row_index]
                for row_index in range(len(rows))
            )
            - objective[column_index]
        )
        for column_index in range(13)
    ]

    scale = z[12]
    p = [sp.factor(z[index] / scale) for index in range(6)]
    q = [
        sp.factor(z[6 + index] / scale)
        for index in range(6)
    ]

    dual_objective = sp.factor(
        sum(
            rhs[index] * dual[index]
            for index in range(len(rows))
        )
    )

    return {
        "p_support": p_support,
        "q_support": q_support,
        "observation_rows": observation_rows,
        "active_constraints": active_constraints,
        "exact": exact,
        "equality_count": equality_count,
        "z": z,
        "scale": scale,
        "p": p,
        "q": q,
        "ratio": ratio,
        "dual": dual,
        "reduced_costs": reduced_costs,
        "dual_objective": dual_objective,
    }


def rational_midpoint(
    lower: sp.Expr,
    upper: sp.Expr,
) -> sp.Rational:
    candidate = sp.Rational(
        str(
            (
                float(sp.N(lower, 60))
                + float(sp.N(upper, 60))
            )
            / 2
        )
    )
    if not bool(lower < candidate < upper):
        raise RuntimeError("Could not construct midpoint")
    return candidate


def certify_sign_open(
    expression: sp.Expr,
    lower: sp.Expr,
    upper: sp.Expr,
    desired_sign: int,
) -> dict[str, Any]:
    expression = sp.factor(expression)

    if expression == 0:
        return {
            "ok": desired_sign == 0,
            "identically_zero": True,
        }

    numerator, denominator = sp.fraction(
        sp.cancel(expression)
    )

    numerator_roots = [
        root
        for root in sp.Poly(
            numerator,
            s,
            domain=sp.QQ,
        ).real_roots()
        if bool(lower < root < upper)
    ]

    denominator_roots = [
        root
        for root in sp.Poly(
            denominator,
            s,
            domain=sp.QQ,
        ).real_roots()
        if bool(lower < root < upper)
    ]

    midpoint = rational_midpoint(lower, upper)
    sample_sign = int(
        sp.sign(expression.subs(s, midpoint))
    )

    return {
        "ok": bool(
            not numerator_roots
            and not denominator_roots
            and sample_sign == desired_sign
        ),
        "identically_zero": False,
        "sample_sign": sample_sign,
        "numerator_root_count": len(numerator_roots),
        "denominator_root_count": len(denominator_roots),
    }


EXACT = symbolic_certificate(
    [1, 3, 5],
    [0, 1, 2, 4],
    [ROW2, ROW_BETA, ROW4],
    [],
    exact=True,
)

EXACT_DUPLICATE = symbolic_certificate(
    [0, 1, 2, 5],
    [1, 3],
    [ROW2, ROW4],
    [],
    exact=True,
)

PHASES = {
    "P0": symbolic_certificate(
        [1, 2, 5],
        [0, 1, 3],
        [ROW2, ROW_BETA, ROW_INFINITY],
        [(0, 1), (2, -1)],
        exact=False,
    ),
    "P0a": symbolic_certificate(
        [1, 2, 5],
        [0, 1, 3],
        [ROW2, ROW_BETA, ROW_INFINITY],
        [(0, 1), (1, -1)],
        exact=False,
    ),
    "P0b": symbolic_certificate(
        [0, 1, 2, 5],
        [1, 3],
        [ROW2, ROW_BETA, ROW_INFINITY],
        [(0, 1), (1, -1)],
        exact=False,
    ),
    "P1": symbolic_certificate(
        [0, 1, 2, 5],
        [1, 2, 3],
        [ROW2, ROW_BETA, ROW_INFINITY],
        [(0, 1), (1, -1), (2, 1)],
        exact=False,
    ),
    "P2": symbolic_certificate(
        [0, 2, 3, 5],
        [1, 2, 3],
        [ROW2, ROW_BETA, ROW_INFINITY],
        [(0, 1), (1, -1), (2, 1)],
        exact=False,
    ),
    "P3": symbolic_certificate(
        [0, 2, 5],
        [1, 2, 3, 4],
        [ROW2, ROW_BETA, ROW_INFINITY],
        [(0, 1), (1, -1), (2, 1)],
        exact=False,
    ),
    "P4": symbolic_certificate(
        [0, 2, 3, 5],
        [1, 2, 4],
        [ROW2, ROW_BETA, ROW_INFINITY],
        [(0, 1), (1, -1), (2, 1)],
        exact=False,
    ),
    "P5": symbolic_certificate(
        [0, 1, 3, 5],
        [1, 2, 4],
        [ROW2, ROW_BETA, ROW_INFINITY],
        [(0, 1), (1, -1), (2, 1)],
        exact=False,
    ),
}

TRANSITION_POLYNOMIALS = [
    (
        1083344 * s**4
        - 3848013 * s**2
        + 3361624 * s
        - 595929
    ),
    (
        541024 * s**5
        - 1923750 * s**3
        + 1683404 * s**2
        - 300678 * s
        + 513
    ),
    (
        540448 * s**5
        - 1923750 * s**3
        + 1686221 * s**2
        - 303432 * s
        + 1026
    ),
    (
        60048 * s**5
        - 213697 * s**3
        + 187274 * s**2
        - 33697 * s
        + 144
    ),
    (
        270144 * s**5
        - 741976 * s**4
        + 706918 * s**3
        - 268529 * s**2
        + 33488 * s
        - 90
    ),
    (
        135108 * s**5
        - 213697 * s**4
        + 100821 * s**2
        - 22394 * s
        + 324
    ),
    (
        72736 * s**5
        - 198000 * s**4
        + 186070 * s**3
        - 69183 * s**2
        + 8476 * s
        - 198
    ),
]

STATIONARY_POLYNOMIAL = (
    1079248 * s**7
    - 3781400 * s**6
    + 4931589 * s**5
    - 2900539 * s**4
    + 734375 * s**3
    - 70149 * s**2
    + 4896 * s
    - 504
)


def unique_root(
    polynomial: sp.Expr,
    lower: sp.Rational,
    upper: sp.Rational,
) -> sp.Expr:
    roots = [
        root
        for root in sp.Poly(polynomial, s).real_roots()
        if bool(root > lower)
        and bool(root < upper)
    ]

    if len(roots) != 1:
        raise RuntimeError(
            f"Expected one root, found {len(roots)}"
        )

    return roots[0]


TRANSITION_ROOTS = [
    unique_root(
        polynomial,
        sp.Rational(1, 16),
        sp.Rational(1, 4),
    )
    for polynomial in TRANSITION_POLYNOMIALS
]

s0, s1, s2, s3, s4, s5, s6 = TRANSITION_ROOTS

PHASE_INTERVALS = {
    "P0": (s0, sp.Rational(1, 4)),
    "P0a": (s1, s0),
    "P0b": (s2, s1),
    "P1": (s3, s2),
    "P2": (s4, s3),
    "P3": (s5, s4),
    "P4": (s6, s5),
    "P5": (sp.Rational(1, 16), s6),
}

s_star = unique_root(
    STATIONARY_POLYNOMIAL,
    sp.Rational(1, 16),
    s6,
)


def audit_exact() -> dict[str, Any]:
    sign_expressions = [
        value
        for value in EXACT["p"] + EXACT["q"]
        if value != 0
    ]
    sign_expressions.append(EXACT["scale"])
    sign_expressions.extend(
        value
        for value in EXACT["reduced_costs"]
        if value != 0
    )

    sign_results = [
        certify_sign_open(
            expression,
            sp.Rational(1, 16),
            sp.Rational(1, 4),
            1,
        )
        for expression in sign_expressions
    ]

    derivative = sp.factor(sp.diff(EXACT["ratio"], s))

    observation_differences = [
        sp.factor(
            dot(values, EXACT["p"])
            - dot(values, EXACT["q"])
        )
        for values in [ROW2, ROW_BETA, ROW4]
    ]

    return {
        "ratio": str(EXACT["ratio"]),
        "derivative": str(derivative),
        "lower_distinct_limit": str(
            EXACT["ratio"].subs(s, sp.Rational(1, 4))
        ),
        "upper_distinct_limit": str(
            EXACT["ratio"].subs(s, sp.Rational(1, 16))
        ),
        "duplicate_endpoint_ratio": str(
            EXACT_DUPLICATE["ratio"]
        ),
        "gates": {
            "all_sign_certificates_pass": bool(
                all(result["ok"] for result in sign_results)
            ),
            "normalization": bool(
                sp.factor(sum(EXACT["p"]) - 1) == 0
                and sp.factor(sum(EXACT["q"]) - 1) == 0
            ),
            "mean": bool(
                dot(
                    [sp.Integer(x) for x in SUPPORT],
                    EXACT["p"],
                )
                == MEAN
                and dot(
                    [sp.Integer(x) for x in SUPPORT],
                    EXACT["q"],
                )
                == MEAN
            ),
            "observations_exact": bool(
                observation_differences == [0, 0, 0]
            ),
            "primal_dual_identity": bool(
                EXACT["ratio"] == EXACT["dual_objective"]
            ),
            "closed_formula": bool(
                sp.factor(
                    EXACT["ratio"]
                    -
                    (1036 * s + 2063)
                    / (2 * (539 * s + 1021))
                )
                == 0
            ),
            "derivative_negative": bool(
                derivative
                ==
                -sp.Rational(54201, 2)
                / (539 * s + 1021) ** 2
            ),
            "lower_infimum_exact": bool(
                EXACT["ratio"].subs(s, sp.Rational(1, 4))
                == sp.Rational(1548, 1541)
            ),
            "beta_3_reproduces_A43": bool(
                EXACT["ratio"].subs(s, sp.Rational(1, 8))
                == sp.Rational(8770, 8707)
            ),
            "upper_limit_exact": bool(
                EXACT["ratio"].subs(s, sp.Rational(1, 16))
                == sp.Rational(5674, 5625)
            ),
            "duplicate_ratio_exact": bool(
                EXACT_DUPLICATE["ratio"]
                == sp.Rational(2033, 1898)
            ),
            "both_endpoint_discontinuities": bool(
                EXACT_DUPLICATE["ratio"]
                != EXACT["ratio"].subs(s, sp.Rational(1, 4))
                and EXACT_DUPLICATE["ratio"]
                != EXACT["ratio"].subs(s, sp.Rational(1, 16))
            ),
        },
    }


def audit_phase(
    name: str,
    certificate: dict[str, Any],
) -> dict[str, Any]:
    lower, upper = PHASE_INTERVALS[name]

    expressions: list[tuple[str, sp.Expr]] = []

    for prefix, values in [
        ("p", certificate["p"]),
        ("q", certificate["q"]),
    ]:
        for index, value in enumerate(values):
            if value != 0:
                expressions.append((f"{prefix}{index}", value))

    expressions.append(("scale", certificate["scale"]))

    for index, value in enumerate(
        certificate["dual"][certificate["equality_count"]:]
    ):
        expressions.append((f"dual_{index}", value))

    for index, value in enumerate(
        certificate["reduced_costs"]
    ):
        if value != 0:
            expressions.append(
                (f"reduced_cost_{index}", value)
            )

    sign_results = {
        label: certify_sign_open(
            expression,
            lower,
            upper,
            1,
        )
        for label, expression in expressions
    }

    active_observations = {
        observation_index
        for observation_index, _ in certificate[
            "active_constraints"
        ]
    }

    inactive_results = {}
    for observation_index, values in enumerate(
        certificate["observation_rows"]
    ):
        if observation_index in active_observations:
            continue

        difference = sp.factor(
            dot(values, certificate["p"])
            - dot(values, certificate["q"])
        )

        inactive_results[
            f"observation_{observation_index}_upper"
        ] = certify_sign_open(
            2 * EPSILON - difference,
            lower,
            upper,
            1,
        )

        inactive_results[
            f"observation_{observation_index}_lower"
        ] = certify_sign_open(
            2 * EPSILON + difference,
            lower,
            upper,
            1,
        )

    active_difference_gates = []
    for observation_index, sign in certificate[
        "active_constraints"
    ]:
        values = certificate["observation_rows"][
            observation_index
        ]
        difference = sp.factor(
            dot(values, certificate["p"])
            - dot(values, certificate["q"])
        )
        active_difference_gates.append(
            difference == sign * 2 * EPSILON
        )

    derivative = sp.factor(
        sp.diff(certificate["ratio"], s)
    )

    return {
        "support_p": certificate["p_support"],
        "support_q": certificate["q_support"],
        "active_constraints": certificate[
            "active_constraints"
        ],
        "ratio": str(certificate["ratio"]),
        "derivative": str(derivative),
        "sign_expression_count": len(sign_results),
        "inactive_constraint_count": len(inactive_results),
        "gates": {
            "all_sign_certificates_pass": bool(
                all(result["ok"] for result in sign_results.values())
            ),
            "all_inactive_constraints_pass": bool(
                all(
                    result["ok"]
                    for result in inactive_results.values()
                )
            ),
            "all_active_constraints_exact": bool(
                all(active_difference_gates)
            ),
            "normalization": bool(
                sp.factor(sum(certificate["p"]) - 1) == 0
                and sp.factor(sum(certificate["q"]) - 1) == 0
            ),
            "mean": bool(
                dot(
                    [sp.Integer(x) for x in SUPPORT],
                    certificate["p"],
                )
                == MEAN
                and dot(
                    [sp.Integer(x) for x in SUPPORT],
                    certificate["q"],
                )
                == MEAN
            ),
            "primal_dual_identity": bool(
                certificate["ratio"]
                == certificate["dual_objective"]
            ),
        },
    }


def continuity_gates() -> dict[str, bool]:
    names = list(PHASES)
    gates = {}

    for left, right, polynomial in zip(
        names[:-1],
        names[1:],
        TRANSITION_POLYNOMIALS,
    ):
        numerator = sp.fraction(
            sp.cancel(
                PHASES[left]["ratio"]
                - PHASES[right]["ratio"]
            )
        )[0]

        remainder = sp.rem(
            sp.Poly(numerator, s, domain=sp.QQ),
            sp.Poly(polynomial, s, domain=sp.QQ),
        )

        gates[f"{left}_to_{right}"] = bool(remainder == 0)

    return gates


def main() -> None:
    if not A44_RESULTS.exists():
        raise FileNotFoundError(A44_RESULTS)
    if not A49_RESULTS.exists():
        raise FileNotFoundError(A49_RESULTS)

    a44 = json.loads(A44_RESULTS.read_text(encoding="utf-8"))
    a49 = json.loads(A49_RESULTS.read_text(encoding="utf-8"))

    exact_audit = audit_exact()

    phase_audits = {
        name: audit_phase(name, certificate)
        for name, certificate in PHASES.items()
    }

    continuity = continuity_gates()

    transition_root_gates = {
        f"transition_{index}_unique":
        bool(
            sp.Poly(polynomial, s).count_roots(
                sp.Rational(1, 16),
                sp.Rational(1, 4),
            )
            == 1
        )
        for index, polynomial in enumerate(
            TRANSITION_POLYNOMIALS
        )
    }

    transition_order_gate = bool(
        sp.Rational(1, 4)
        > s0 > s1 > s2 > s3 > s4 > s5 > s6
        > sp.Rational(1, 16)
    )

    phase_derivatives = {
        name: sp.factor(
            sp.diff(certificate["ratio"], s)
        )
        for name, certificate in PHASES.items()
    }

    decreasing_beta_gates = {
        name: certify_sign_open(
            derivative,
            *PHASE_INTERVALS[name],
            1,
        )["ok"]
        for name, derivative in phase_derivatives.items()
        if name in {
            "P0a",
            "P0b",
            "P1",
            "P2",
            "P3",
            "P4",
        }
    }

    plateau_gate = bool(
        phase_derivatives["P0"] == 0
    )

    stationary_roots_in_phase = [
        root
        for root in sp.Poly(
            STATIONARY_POLYNOMIAL,
            s,
        ).real_roots()
        if bool(root > sp.Rational(1, 16))
        and bool(root < s6)
    ]

    stationary_unique_gate = bool(
        len(stationary_roots_in_phase) == 1
        and stationary_roots_in_phase[0] == s_star
    )

    stationary_left_sign = certify_sign_open(
        phase_derivatives["P5"],
        sp.Rational(1, 16),
        s_star,
        -1,
    )
    stationary_right_sign = certify_sign_open(
        phase_derivatives["P5"],
        s_star,
        s6,
        1,
    )

    beta_star = -sp.log(s_star, 2)
    ratio_star = PHASES["P5"]["ratio"].subs(s, s_star)
    risk_star = sp.log(ratio_star) / (2 * sp.log(2))

    ratio_beta3 = PHASES["P5"]["ratio"].subs(
        s,
        sp.Rational(1, 8),
    )
    risk_beta3 = (
        sp.log(ratio_beta3)
        / (2 * sp.log(2))
    )

    improvement_percent = sp.N(
        100 * (1 - risk_star / risk_beta3),
        40,
    )

    transition_table = []
    phase_names = list(PHASES)

    for index, root in enumerate(
        TRANSITION_ROOTS,
        start=1,
    ):
        ratio = PHASES[
            phase_names[index - 1]
        ]["ratio"].subs(s, root)

        transition_table.append(
            {
                "transition": index,
                "s_decimal": str(sp.N(root, 35)),
                "beta_decimal": str(
                    sp.N(-sp.log(root, 2), 35)
                ),
                "future_risk_decimal": str(
                    sp.N(
                        sp.log(ratio)
                        / (2 * sp.log(2)),
                        35,
                    )
                ),
            }
        )

    all_phase_gates = [
        gate
        for audit in phase_audits.values()
        for gate in audit["gates"].values()
    ]

    a44_ratio = sp.Rational(
        a44["noisy_compactified_result"]["infinity_ratio"]
    )

    a49_exact_ratio = sp.Rational(
        a49["exact_contract"]["winner_ratio_exact"]
    )

    gates = {
        **transition_root_gates,
        "transition_roots_strictly_ordered": transition_order_gate,
        "exact_audit_pass": bool(
            all(exact_audit["gates"].values())
        ),
        "all_noisy_phase_gates_pass": bool(
            all(all_phase_gates)
        ),
        "all_noisy_transitions_continuous": bool(
            all(continuity.values())
        ),
        "initial_noisy_phase_is_plateau": plateau_gate,
        "prestationary_noisy_phases_decrease_with_beta": bool(
            all(decreasing_beta_gates.values())
        ),
        "stationary_polynomial_has_one_phase_root": (
            stationary_unique_gate
        ),
        "P5_derivative_negative_below_s_star": bool(
            stationary_left_sign["ok"]
        ),
        "P5_derivative_positive_above_s_star": bool(
            stationary_right_sign["ok"]
        ),
        "beta_3_noisy_value_matches_A44": bool(
            ratio_beta3 == a44_ratio
        ),
        "beta_3_exact_value_matches_A49": bool(
            EXACT["ratio"].subs(s, sp.Rational(1, 8))
            == a49_exact_ratio
        ),
        "continuous_optimum_improves_beta_3": bool(
            risk_star < risk_beta3
        ),
    }

    verdict = (
        "PASS_CONTINUOUS_SECOND_ANCHOR_INTERIOR_OPTIMUM"
        if all(gates.values())
        else "FAIL_A52_SECOND_ANCHOR_AUDIT"
    )

    result = {
        "audit": "A52_CONTINUOUS_SECOND_ANCHOR",
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "target_exponent": 1,
            "beta_domain": "[2,4]",
            "s_definition": "s=2^(-beta)",
            "exact_design": "{2,beta,4}*log(2)",
            "noisy_design": "{2,beta,infinity}*log(2)",
            "epsilon": str(EPSILON),
        },
        "exact_result": exact_audit,
        "noisy_phases": phase_audits,
        "transition_polynomials": [
            str(sp.factor(polynomial))
            for polynomial in TRANSITION_POLYNOMIALS
        ],
        "transition_table": transition_table,
        "continuity": continuity,
        "stationary_result": {
            "polynomial": str(STATIONARY_POLYNOMIAL),
            "s_star_object": str(s_star),
            "s_star_decimal": str(sp.N(s_star, 40)),
            "beta_star_decimal": str(sp.N(beta_star, 40)),
            "ratio_star_object": str(ratio_star),
            "future_risk_star_decimal": str(
                sp.N(risk_star, 40)
            ),
            "beta_3_ratio": str(ratio_beta3),
            "beta_3_future_risk": str(
                sp.N(risk_beta3, 40)
            ),
            "improvement_over_beta_3_percent": str(
                improvement_percent
            ),
        },
        "formal_results": [
            (
                "exact distinct-anchor ratio increases "
                "strictly with beta"
            ),
            (
                "exact infimum occurs at unattained "
                "coalescence beta->2+"
            ),
            (
                "both exact duplicated endpoints are "
                "discontinuous"
            ),
            (
                "eight exact noisy primal-dual phases "
                "cover [2,4]"
            ),
            "seven ordered algebraic transitions",
            (
                "one unique noisy stationary point exists"
            ),
            (
                "the stationary point is the unique global "
                "noisy minimizer"
            ),
            (
                "the second anchor has a genuine noisy "
                "interior optimum"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The result is exact only for beta in [2,4], "
            "the six-point support, exact mean, fixed first "
            "anchor 2, contract-specific third observations, "
            "common error, and direct future-Q risk. The "
            "finite-gamma=10 continuous-beta problem is not "
            "solved here."
        ),
    }

    output_path = HERE / (
        "a52_continuous_second_anchor_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "phase_count": len(PHASES),
        "transition_count": len(TRANSITION_ROOTS),
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "beta_star": str(sp.N(beta_star, 20)),
        "risk_star": str(sp.N(risk_star, 20)),
        "failed_gates": [
            name for name, value in gates.items() if not value
        ],
        "verdict": verdict,
    }

    print(json.dumps(summary, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
