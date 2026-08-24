#!/usr/bin/env python3
"""A51 exact audit: target-exclusion distance law.

The first anchor is allowed on the full interval 1 <= alpha <= 3, with
s = 2^(-alpha).

Exact contract:
    {alpha, 3, 4} * log(2)

Noisy contract:
    {alpha, 3, infinity} * log(2)
    epsilon = 1/10000

The audit certifies:
- one exact distinct-anchor branch on (1,3);
- fourteen positive-noise primal-dual phases on [1,3];
- thirteen algebraic transitions;
- strict monotonic increase of risk in alpha;
- boundary optimum alpha = 1 + Delta;
- asymptotic connection to the direct-target theorem.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A48_RESULTS = HERE / "a48_target_inclusion_degeneracy_results.json"
A50_RESULTS = HERE / "a50_continuous_first_anchor_results.json"

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


ROW_ALPHA = [s**x for x in SUPPORT]
ROW3 = row_integer(3)
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
    lower_float = float(sp.N(lower, 60))
    upper_float = float(sp.N(upper, 60))
    candidate = sp.Rational(
        str((lower_float + upper_float) / 2)
    )
    if not bool(lower < candidate < upper):
        raise RuntimeError("Could not create interval sample")
    return candidate


def certify_nonnegative(
    expression: sp.Expr,
    lower: sp.Expr,
    upper: sp.Expr,
    *,
    strict: bool = False,
) -> dict[str, Any]:
    expression = sp.factor(expression)

    if expression == 0:
        return {
            "ok": not strict,
            "identically_zero": True,
        }

    numerator, denominator = sp.fraction(
        sp.cancel(expression)
    )

    numerator_polynomial = sp.Poly(
        numerator,
        s,
        domain=sp.QQ,
    )
    denominator_polynomial = sp.Poly(
        denominator,
        s,
        domain=sp.QQ,
    )

    numerator_roots = [
        root
        for root in numerator_polynomial.real_roots()
        if bool(lower < root < upper)
    ]
    denominator_roots = [
        root
        for root in denominator_polynomial.real_roots()
        if bool(lower < root < upper)
    ]

    midpoint = rational_midpoint(lower, upper)
    signs = [
        sp.sign(expression.subs(s, lower)),
        sp.sign(expression.subs(s, midpoint)),
        sp.sign(expression.subs(s, upper)),
    ]

    ok = (
        not numerator_roots
        and not denominator_roots
        and signs[0] >= 0
        and signs[1] > 0
        and signs[2] >= 0
    )

    if strict:
        ok = ok and signs[1] > 0

    return {
        "ok": bool(ok),
        "identically_zero": False,
        "signs": [str(sign) for sign in signs],
        "interior_numerator_root_count": len(numerator_roots),
        "interior_denominator_root_count": len(denominator_roots),
    }


EXACT = symbolic_certificate(
    [1, 3, 5],
    [0, 1, 2, 4],
    [ROW_ALPHA, ROW3, ROW4],
    [],
    exact=True,
)

EXACT_DUPLICATE = symbolic_certificate(
    [0, 1, 2, 5],
    [1, 3],
    [ROW3, ROW4],
    [],
    exact=True,
)

PHASE_SPECS = [
    ("M0", [2, 3, 5], [2, 3], [(0, 1)]),
    ("M1", [2, 3, 5], [0, 2, 3], [(0, 1), (2, -1)]),
    (
        "M2",
        [2, 3, 5],
        [0, 1, 2, 3],
        [(0, 1), (1, -1), (2, -1)],
    ),
    ("M3", [2, 3, 5], [1, 2, 3], [(0, 1), (1, -1)]),
    (
        "M4",
        [0, 2, 3, 5],
        [1, 2, 3],
        [(0, 1), (1, -1), (2, 1)],
    ),
    (
        "M5",
        [0, 2, 3, 5],
        [2, 3, 4],
        [(0, 1), (1, -1), (2, 1)],
    ),
    (
        "M6",
        [0, 1, 2, 3, 5],
        [2, 4],
        [(0, 1), (1, -1), (2, 1)],
    ),
    (
        "N1",
        [0, 1, 3, 5],
        [1, 2, 4],
        [(0, 1), (1, -1), (2, 1)],
    ),
    (
        "N2",
        [0, 2, 3, 5],
        [1, 2, 4],
        [(0, 1), (1, -1), (2, 1)],
    ),
    (
        "N3",
        [0, 2, 5],
        [1, 2, 3, 4],
        [(0, 1), (1, -1), (2, 1)],
    ),
    (
        "N4",
        [0, 1, 2, 5],
        [1, 2, 3],
        [(0, 1), (1, -1), (2, 1)],
    ),
    (
        "N4a",
        [0, 1, 2, 5],
        [1, 3],
        [(0, 1), (1, -1)],
    ),
    (
        "N5a",
        [1, 2, 5],
        [0, 1, 3],
        [(0, 1), (1, -1)],
    ),
    (
        "N5b",
        [1, 2, 5],
        [0, 1, 3],
        [(0, 1), (2, -1)],
    ),
]

PHASES = {
    name: symbolic_certificate(
        p_support,
        q_support,
        [ROW_ALPHA, ROW3, ROW_INFINITY],
        active,
        exact=False,
    )
    for name, p_support, q_support, active in PHASE_SPECS
}

UPPER_TRANSITION_POLYNOMIALS = [
    6000 * s**5 - 21750 * s**3 + 17625 * s**2 - 1874,
    (
        6000 * s**5
        - 25502 * s**3
        + 27005 * s**2
        - 7504 * s
        + 2
    ),
    (
        7056000 * s**5
        - 32307346 * s**3
        + 37550365 * s**2
        - 13458692 * s
        + 1160849
    ),
    (
        35247232 * s**5
        - 161397466 * s**3
        + 187604369 * s**2
        - 67252500 * s
        + 5807332
    ),
    (
        4412352 * s**4
        - 11614664 * s**3
        + 10285634 * s**2
        - 3377419 * s
        + 294832
    ),
    (
        17588416 * s**4
        - 46305000 * s**3
        + 41017906 * s**2
        - 13477563 * s
        + 1179328
    ),
    (
        2300416 * s**4
        - 6174000 * s**3
        + 5664406 * s**2
        - 2011563 * s
        + 223828
    ),
]

LOWER_TRANSITION_POLYNOMIALS = [
    (
        2300416 * s**4
        - 6174000 * s**3
        + 5664406 * s**2
        - 2011563 * s
        + 223828
    ),
    (
        2778888 * s**4
        - 4299425 * s**3
        + 1786055 * s
        - 268850
    ),
    (
        1307712 * s**4
        - 4299425 * s**2
        + 3369570 * s
        - 379425
    ),
    (
        11702144 * s**4
        - 38403750 * s**2
        + 30009165 * s
        - 3317800
    ),
    (
        1066112 * s**5
        - 3491250 * s**3
        + 2718052 * s**2
        - 292914 * s
        - 931
    ),
    (
        23507776 * s**5
        - 76817741 * s**3
        + 59583896 * s**2
        - 6253449 * s
        - 40964
    ),
]


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
            f"Expected one root in ({lower},{upper}), found {len(roots)}"
        )
    return roots[0]


UPPER_ROOTS = [
    unique_root(
        polynomial,
        sp.Rational(1, 4),
        sp.Rational(1, 2),
    )
    for polynomial in UPPER_TRANSITION_POLYNOMIALS
]

LOWER_ROOTS = [
    unique_root(
        polynomial,
        sp.Rational(1, 8),
        sp.Rational(1, 4),
    )
    for polynomial in LOWER_TRANSITION_POLYNOMIALS
]

ALL_ROOTS = UPPER_ROOTS + LOWER_ROOTS

(
    u0,
    u1,
    u2,
    u3,
    u4,
    u5,
    u6,
) = UPPER_ROOTS

(
    l0,
    l1,
    l2,
    l3,
    l4,
    l5,
) = LOWER_ROOTS

PHASE_INTERVALS = {
    "M0": (u0, sp.Rational(1, 2)),
    "M1": (u1, u0),
    "M2": (u2, u1),
    "M3": (u3, u2),
    "M4": (u4, u3),
    "M5": (u5, u4),
    "M6": (u6, u5),
    "N1": (l0, u6),
    "N2": (l1, l0),
    "N3": (l2, l1),
    "N4": (l3, l2),
    "N4a": (l4, l3),
    "N5a": (l5, l4),
    "N5b": (sp.Rational(1, 8), l5),
}

CONTINUITY_POLYNOMIALS = (
    UPPER_TRANSITION_POLYNOMIALS
    + LOWER_TRANSITION_POLYNOMIALS
)


def audit_exact() -> dict[str, Any]:
    expressions = [
        value
        for value in EXACT["p"] + EXACT["q"]
        if value != 0
    ]
    expressions.append(EXACT["scale"])
    expressions.extend(
        value
        for value in EXACT["reduced_costs"]
        if value != 0
    )

    sign_certificates = [
        certify_nonnegative(
            expression,
            sp.Rational(1, 8),
            sp.Rational(1, 2),
        )
        for expression in expressions
    ]

    derivative = sp.factor(sp.diff(EXACT["ratio"], s))

    return {
        "ratio": str(EXACT["ratio"]),
        "derivative": str(derivative),
        "direct_target_endpoint": str(
            EXACT["ratio"].subs(s, sp.Rational(1, 2))
        ),
        "distinct_duplicate_limit": str(
            EXACT["ratio"].subs(s, sp.Rational(1, 8))
        ),
        "actual_duplicate_ratio": str(EXACT_DUPLICATE["ratio"]),
        "gates": {
            "all_sign_certificates_pass": bool(
                all(item["ok"] for item in sign_certificates)
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
            "primal_dual_identity": bool(
                EXACT["ratio"] == EXACT["dual_objective"]
            ),
            "closed_formula": bool(
                sp.factor(
                    EXACT["ratio"]
                    - 5 * (392 * s + 779)
                    / (2 * (1043 * s + 1916))
                )
                == 0
            ),
            "derivative_negative": bool(
                derivative
                ==
                -sp.Rational(307125, 2)
                / (1043 * s + 1916) ** 2
            ),
            "direct_target_ratio_one": bool(
                EXACT["ratio"].subs(s, sp.Rational(1, 2))
                == 1
            ),
            "duplicate_ratio_exact": bool(
                EXACT_DUPLICATE["ratio"]
                == sp.Rational(3871, 3484)
            ),
            "duplicate_discontinuity": bool(
                EXACT_DUPLICATE["ratio"]
                != EXACT["ratio"].subs(
                    s,
                    sp.Rational(1, 8),
                )
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
        label: certify_nonnegative(
            expression,
            lower,
            upper,
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
        ] = certify_nonnegative(
            2 * EPSILON - difference,
            lower,
            upper,
        )

        inactive_results[
            f"observation_{observation_index}_lower"
        ] = certify_nonnegative(
            2 * EPSILON + difference,
            lower,
            upper,
        )

    derivative = sp.factor(
        sp.diff(certificate["ratio"], s)
    )
    derivative_certificate = certify_nonnegative(
        -derivative,
        lower,
        upper,
        strict=True,
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
                all(item["ok"] for item in sign_results.values())
            ),
            "all_inactive_constraints_pass": bool(
                all(
                    item["ok"]
                    for item in inactive_results.values()
                )
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
            "ratio_derivative_negative": bool(
                derivative_certificate["ok"]
            ),
        },
    }


def continuity_gates() -> dict[str, bool]:
    names = list(PHASES)
    gates = {}

    for left_name, right_name, polynomial in zip(
        names[:-1],
        names[1:],
        CONTINUITY_POLYNOMIALS,
    ):
        numerator = sp.fraction(
            sp.cancel(
                PHASES[left_name]["ratio"]
                - PHASES[right_name]["ratio"]
            )
        )[0]

        remainder = sp.rem(
            sp.Poly(numerator, s, domain=sp.QQ),
            sp.Poly(polynomial, s, domain=sp.QQ),
        )

        gates[
            f"{left_name}_to_{right_name}"
        ] = bool(remainder == 0)

    return gates


def main() -> None:
    if not A48_RESULTS.exists():
        raise FileNotFoundError(A48_RESULTS)
    if not A50_RESULTS.exists():
        raise FileNotFoundError(A50_RESULTS)

    a48 = json.loads(A48_RESULTS.read_text(encoding="utf-8"))
    a50 = json.loads(A50_RESULTS.read_text(encoding="utf-8"))

    exact_audit = audit_exact()

    phase_audits = {
        name: audit_phase(name, certificate)
        for name, certificate in PHASES.items()
    }

    continuity = continuity_gates()

    root_gates = {}
    for index, (
        polynomial,
        root,
    ) in enumerate(
        zip(CONTINUITY_POLYNOMIALS, ALL_ROOTS),
        start=1,
    ):
        lower = (
            sp.Rational(1, 4)
            if index <= 7
            else sp.Rational(1, 8)
        )
        upper = (
            sp.Rational(1, 2)
            if index <= 7
            else sp.Rational(1, 4)
        )

        root_gates[
            f"transition_{index}_unique_in_declared_half"
        ] = bool(
            sp.Poly(polynomial, s).count_roots(
                lower,
                upper,
            )
            == 1
        )

    root_order_gate = bool(
        sp.Rational(1, 2)
        > u0 > u1 > u2 > u3 > u4 > u5 > u6
        > l0 > l1 > l2 > l3 > l4 > l5
        > sp.Rational(1, 8)
    )

    M0 = PHASES["M0"]["ratio"]
    exact_alpha_derivative = sp.factor(
        -sp.log(2)
        * sp.Rational(1, 2)
        * sp.diff(EXACT["ratio"], s).subs(
            s,
            sp.Rational(1, 2),
        )
    )

    noisy_alpha_derivative = sp.factor(
        -sp.log(2)
        * sp.Rational(1, 2)
        * sp.diff(M0, s).subs(
            s,
            sp.Rational(1, 2),
        )
    )

    exact_risk_slope = sp.factor(
        exact_alpha_derivative
        / (2 * sp.log(2))
    )

    direct_noisy_ratio = sp.Rational(1877, 1875)

    noisy_risk_slope = sp.factor(
        (
            noisy_alpha_derivative
            / direct_noisy_ratio
        )
        / (2 * sp.log(2))
    )

    transition_table = []
    phase_names = list(PHASES)

    for index, root in enumerate(ALL_ROOTS, start=1):
        ratio = PHASES[
            phase_names[index - 1]
        ]["ratio"].subs(s, root)

        transition_table.append(
            {
                "transition": index,
                "s_decimal": str(sp.N(root, 35)),
                "alpha_decimal": str(
                    sp.N(-sp.log(root, 2), 35)
                ),
                "delta_decimal": str(
                    sp.N(-sp.log(root, 2) - 1, 35)
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
        value
        for audit in phase_audits.values()
        for value in audit["gates"].values()
    ]

    a50_phase_names = [
        "N1",
        "N2",
        "N3",
        "N4",
        "N4a",
        "N5a",
        "N5b",
    ]

    a50_consistency = all(
        phase_audits[name]["ratio"]
        == a50["noisy_phases"][name]["ratio"]
        for name in a50_phase_names
    )

    gates = {
        **root_gates,
        "transition_roots_strictly_ordered": root_order_gate,
        "exact_audit_pass": bool(
            all(exact_audit["gates"].values())
        ),
        "all_fourteen_phase_gates_pass": bool(
            all(all_phase_gates)
        ),
        "all_thirteen_transitions_continuous": bool(
            all(continuity.values())
        ),
        "exact_small_delta_ratio_slope": bool(
            exact_alpha_derivative
            == 21 * sp.log(2) / 1625
        ),
        "exact_small_delta_risk_slope": bool(
            exact_risk_slope == sp.Rational(21, 3250)
        ),
        "noisy_direct_limit_matches_A48": bool(
            M0.subs(s, sp.Rational(1, 2))
            == sp.Rational(
                a48["noisy_catalogue"]["included_ratio"]
            )
        ),
        "noisy_small_delta_ratio_slope": bool(
            noisy_alpha_derivative
            == 2 * sp.log(2) / 9375
        ),
        "noisy_small_delta_risk_slope": bool(
            noisy_risk_slope == sp.Rational(1, 9385)
        ),
        "A50_noisy_phases_reproduced": bool(
            a50_consistency
        ),
        "boundary_optimum_exact_for_all_delta_below_2": bool(
            exact_audit["gates"]["derivative_negative"]
        ),
        "boundary_optimum_noisy_for_all_delta": bool(
            all(
                audit["gates"]["ratio_derivative_negative"]
                for audit in phase_audits.values()
            )
        ),
    }

    verdict = (
        "PASS_TARGET_EXCLUSION_DISTANCE_BOUNDARY_LAW"
        if all(gates.values())
        else "FAIL_A51_TARGET_EXCLUSION_DISTANCE_AUDIT"
    )

    result = {
        "audit": "A51_TARGET_EXCLUSION_DISTANCE_LAW",
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "target_exponent": 1,
            "delta_domain": "(0,2]",
            "alpha_domain_for_delta": "[1+delta,3]",
            "exact_design": "{alpha,3,4}*log(2)",
            "noisy_design": "{alpha,3,infinity}*log(2)",
            "epsilon": str(EPSILON),
        },
        "exact_result": exact_audit,
        "noisy_phases": phase_audits,
        "transition_polynomials": [
            str(sp.factor(polynomial))
            for polynomial in CONTINUITY_POLYNOMIALS
        ],
        "transition_table": transition_table,
        "continuity": continuity,
        "small_delta": {
            "exact_ratio": (
                "1 + 21*log(2)/1625*delta + O(delta^2)"
            ),
            "exact_future_risk": (
                "21/3250*delta + O(delta^2)"
            ),
            "noisy_ratio": (
                "1877/1875 + 2*log(2)/9375*delta "
                "+ O(delta^2)"
            ),
            "noisy_future_risk": (
                "0.5*log2(1877/1875) "
                "+ delta/9385 + O(delta^2)"
            ),
        },
        "optimizer_law": {
            "exact_0_lt_delta_lt_2": "alpha*=1+delta",
            "exact_delta_eq_2": (
                "only alpha=3 is admissible; duplicate ratio 3871/3484"
            ),
            "noisy_0_lt_delta_le_2": "alpha*=1+delta",
        },
        "formal_results": [
            (
                "exact first-anchor optimum equals the lower "
                "exclusion boundary"
            ),
            (
                "exact risk vanishes linearly as delta goes to zero"
            ),
            (
                "fourteen positive-noise phases cover alpha in [1,3]"
            ),
            "thirteen ordered algebraic transitions",
            (
                "positive-noise optimum equals the lower exclusion "
                "boundary for every delta"
            ),
            (
                "positive-noise limit reproduces direct target measurement"
            ),
            (
                "exclusion distance is part of the information contract, "
                "not an inferred universal constant"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The theorem is exact only under the six-point support, "
            "exact mean, contract-specific fixed second and third "
            "observations, common absolute error, and direct future-Q "
            "risk. No experimental cost or empirical exclusion distance "
            "is inferred."
        ),
    }

    output_path = HERE / (
        "a51_target_exclusion_distance_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "phase_count": len(PHASES),
        "transition_count": len(ALL_ROOTS),
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "exact_optimizer": "alpha=1+delta",
        "noisy_optimizer": "alpha=1+delta",
        "verdict": verdict,
    }

    print(json.dumps(summary, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
