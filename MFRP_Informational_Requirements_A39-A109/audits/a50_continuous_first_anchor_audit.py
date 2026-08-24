#!/usr/bin/env python3
"""A50 exact audit: continuous release of the first excluded anchor.

Contracts
---------
Exact:
    D0(alpha) = {alpha, 3, 4} * log(2)
    2 <= alpha <= 3

Noisy:
    De(alpha) = {alpha, 3, infinity} * log(2)
    epsilon = 1/10000
    2 <= alpha <= 3

The script derives exact symbolic Charnes-Cooper primal-dual certificates,
isolates six algebraic noisy transitions, and certifies monotonicity.

The exact-data distinct-anchor result is valid on [2,3). The duplicated
endpoint alpha=3 is solved separately.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A43_RESULTS = HERE / "a43_direct_q_minimax_design_results.json"
A44_RESULTS = HERE / "a44_continuous_parameter_results.json"

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

    primal_matrix = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(len(rows))
        ]
    )

    if primal_matrix.rows != primal_matrix.cols:
        raise RuntimeError("Active system is not square")

    primal_solution = primal_matrix.inv() * sp.Matrix(rhs)

    z = [sp.Integer(0)] * 13
    for index, value in zip(
        positive_indices,
        primal_solution,
    ):
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
        [
            objective[index]
            for index in positive_indices
        ]
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
    p = [
        sp.factor(z[index] / scale)
        for index in range(6)
    ]
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
    lower_float = float(sp.N(lower, 50))
    upper_float = float(sp.N(upper, 50))
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

EXACT_ENDPOINT = symbolic_certificate(
    [0, 1, 2, 5],
    [1, 3],
    [ROW3, ROW4],
    [],
    exact=True,
)

NOISY_PHASES = {
    "N1": symbolic_certificate(
        [0, 1, 3, 5],
        [1, 2, 4],
        [ROW_ALPHA, ROW3, ROW_INFINITY],
        [(0, 1), (1, -1), (2, 1)],
        exact=False,
    ),
    "N2": symbolic_certificate(
        [0, 2, 3, 5],
        [1, 2, 4],
        [ROW_ALPHA, ROW3, ROW_INFINITY],
        [(0, 1), (1, -1), (2, 1)],
        exact=False,
    ),
    "N3": symbolic_certificate(
        [0, 2, 5],
        [1, 2, 3, 4],
        [ROW_ALPHA, ROW3, ROW_INFINITY],
        [(0, 1), (1, -1), (2, 1)],
        exact=False,
    ),
    "N4": symbolic_certificate(
        [0, 1, 2, 5],
        [1, 2, 3],
        [ROW_ALPHA, ROW3, ROW_INFINITY],
        [(0, 1), (1, -1), (2, 1)],
        exact=False,
    ),
    "N4a": symbolic_certificate(
        [0, 1, 2, 5],
        [1, 3],
        [ROW_ALPHA, ROW3, ROW_INFINITY],
        [(0, 1), (1, -1)],
        exact=False,
    ),
    "N5a": symbolic_certificate(
        [1, 2, 5],
        [0, 1, 3],
        [ROW_ALPHA, ROW3, ROW_INFINITY],
        [(0, 1), (1, -1)],
        exact=False,
    ),
    "N5b": symbolic_certificate(
        [1, 2, 5],
        [0, 1, 3],
        [ROW_ALPHA, ROW3, ROW_INFINITY],
        [(0, 1), (2, -1)],
        exact=False,
    ),
}

TRANSITION_POLYNOMIALS = [
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

TRANSITION_ROOTS = []
for polynomial in TRANSITION_POLYNOMIALS:
    roots = [
        root
        for root in sp.Poly(polynomial, s).real_roots()
        if bool(root > sp.Rational(1, 8))
        and bool(root < sp.Rational(1, 4))
    ]
    if len(roots) != 1:
        raise RuntimeError("Transition root is not unique")
    TRANSITION_ROOTS.append(roots[0])

s1, s2, s3, s4, s5, s6 = TRANSITION_ROOTS

PHASE_INTERVALS = {
    "N1": (s1, sp.Rational(1, 4)),
    "N2": (s2, s1),
    "N3": (s3, s2),
    "N4": (s4, s3),
    "N4a": (s5, s4),
    "N5a": (s6, s5),
    "N5b": (sp.Rational(1, 8), s6),
}


def audit_exact_certificate() -> dict[str, Any]:
    expressions = (
        [
            value
            for value in EXACT["p"] + EXACT["q"]
            if value != 0
        ]
        + [EXACT["scale"]]
        + [
            value
            for value in EXACT["reduced_costs"]
            if value != 0
        ]
    )

    sign_certificates = [
        certify_nonnegative(
            expression,
            sp.Rational(1, 8),
            sp.Rational(1, 4),
        )
        for expression in expressions
    ]

    observation_differences = [
        sp.factor(
            dot(values, EXACT["p"])
            - dot(values, EXACT["q"])
        )
        for values in [ROW_ALPHA, ROW3, ROW4]
    ]

    derivative = sp.factor(
        sp.diff(EXACT["ratio"], s)
    )

    return {
        "ratio": str(EXACT["ratio"]),
        "derivative": str(derivative),
        "distinct_limit_at_alpha_3": str(
            sp.factor(
                EXACT["ratio"].subs(
                    s,
                    sp.Rational(1, 8),
                )
            )
        ),
        "endpoint_ratio": str(EXACT_ENDPOINT["ratio"]),
        "gates": {
            "all_sign_certificates_pass": bool(
                all(
                    certificate["ok"]
                    for certificate in sign_certificates
                )
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
            "observations_match": bool(
                observation_differences == [0, 0, 0]
            ),
            "primal_dual_identity": bool(
                EXACT["ratio"]
                == EXACT["dual_objective"]
            ),
            "closed_ratio_formula": bool(
                sp.factor(
                    EXACT["ratio"]
                    -
                    5
                    * (392 * s + 779)
                    / (
                        2
                        * (1043 * s + 1916)
                    )
                )
                == 0
            ),
            "derivative_strictly_negative": bool(
                derivative
                ==
                -sp.Rational(307125, 2)
                / (1043 * s + 1916) ** 2
            ),
            "winner_ratio_at_alpha_2": bool(
                EXACT["ratio"].subs(
                    s,
                    sp.Rational(1, 4),
                )
                == sp.Rational(8770, 8707)
            ),
            "duplicated_endpoint_ratio": bool(
                EXACT_ENDPOINT["ratio"]
                == sp.Rational(3871, 3484)
            ),
            "endpoint_discontinuity": bool(
                EXACT_ENDPOINT["ratio"]
                != EXACT["ratio"].subs(
                    s,
                    sp.Rational(1, 8),
                )
            ),
        },
    }


def audit_noisy_phase(
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
                expressions.append(
                    (f"{prefix}{index}", value)
                )

    expressions.append(("scale", certificate["scale"]))

    for index, value in enumerate(
        certificate["dual"][5:]
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
        difference = sp.factor(
            dot(values, certificate["p"])
            - dot(values, certificate["q"])
        )

        if observation_index in active_observations:
            continue

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

    observation_differences = [
        sp.factor(
            dot(values, certificate["p"])
            - dot(values, certificate["q"])
        )
        for values in certificate["observation_rows"]
    ]

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
        "observation_differences": [
            str(value)
            for value in observation_differences
        ],
        "sign_expression_count": len(sign_results),
        "inactive_constraint_count": len(inactive_results),
        "gates": {
            "all_sign_certificates_pass": bool(
                all(
                    result["ok"]
                    for result in sign_results.values()
                )
            ),
            "all_inactive_constraints_pass": bool(
                all(
                    result["ok"]
                    for result in inactive_results.values()
                )
            ),
            "normalization": bool(
                sp.factor(sum(certificate["p"]) - 1)
                == 0
                and sp.factor(
                    sum(certificate["q"]) - 1
                )
                == 0
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
    names = list(NOISY_PHASES)
    gates = {}

    for index, (
        left_name,
        right_name,
        polynomial,
    ) in enumerate(
        zip(
            names[:-1],
            names[1:],
            TRANSITION_POLYNOMIALS,
        )
    ):
        numerator = sp.fraction(
            sp.cancel(
                NOISY_PHASES[left_name]["ratio"]
                -
                NOISY_PHASES[right_name]["ratio"]
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
    if not A43_RESULTS.exists():
        raise FileNotFoundError(A43_RESULTS)
    if not A44_RESULTS.exists():
        raise FileNotFoundError(A44_RESULTS)

    a43 = json.loads(
        A43_RESULTS.read_text(encoding="utf-8")
    )
    a44 = json.loads(
        A44_RESULTS.read_text(encoding="utf-8")
    )

    exact_audit = audit_exact_certificate()
    phase_audits = {
        name: audit_noisy_phase(name, certificate)
        for name, certificate in NOISY_PHASES.items()
    }
    continuity = continuity_gates()

    root_gates = {}
    for index, (
        polynomial,
        root,
    ) in enumerate(
        zip(
            TRANSITION_POLYNOMIALS,
            TRANSITION_ROOTS,
        ),
        start=1,
    ):
        root_gates[
            f"transition_{index}_unique_domain_root"
        ] = bool(
            sp.Poly(polynomial, s).count_roots(
                sp.Rational(1, 8),
                sp.Rational(1, 4),
            )
            == 1
        )

    root_order_gate = bool(
        sp.Rational(1, 4)
        > s1 > s2 > s3 > s4 > s5 > s6
        > sp.Rational(1, 8)
    )

    noisy_alpha_2_ratio = sp.factor(
        NOISY_PHASES["N1"]["ratio"].subs(
            s,
            sp.Rational(1, 4),
        )
    )
    noisy_alpha_3_ratio = sp.factor(
        NOISY_PHASES["N5b"]["ratio"].subs(
            s,
            sp.Rational(1, 8),
        )
    )

    transition_table = []
    phase_names = list(NOISY_PHASES)
    for index, root in enumerate(
        TRANSITION_ROOTS,
        start=1,
    ):
        ratio = NOISY_PHASES[
            phase_names[index - 1]
        ]["ratio"].subs(s, root)
        risk = (
            sp.log(ratio)
            / (2 * sp.log(2))
        )
        transition_table.append(
            {
                "transition": index,
                "root_object": str(root),
                "s_decimal": str(sp.N(root, 40)),
                "alpha_decimal": str(
                    sp.N(-sp.log(root, 2), 40)
                ),
                "future_risk_decimal": str(
                    sp.N(risk, 40)
                ),
            }
        )

    internal_phase_gates = [
        value
        for audit in phase_audits.values()
        for value in audit["gates"].values()
    ]

    gates = {
        **root_gates,
        "transition_roots_strictly_ordered": root_order_gate,
        "exact_audit_pass": bool(
            all(exact_audit["gates"].values())
        ),
        "all_noisy_phase_gates_pass": bool(
            all(internal_phase_gates)
        ),
        "all_noisy_transitions_continuous": bool(
            all(continuity.values())
        ),
        "exact_alpha_2_matches_A43": bool(
            exact_audit["gates"][
                "winner_ratio_at_alpha_2"
            ]
            and sp.Rational(
                a43["exact_data_contract"][
                    "winner_ratio_exact"
                ]
            )
            == sp.Rational(8770, 8707)
        ),
        "noisy_alpha_2_matches_A44": bool(
            noisy_alpha_2_ratio
            == sp.Rational(
                a44["noisy_compactified_result"][
                    "infinity_ratio"
                ]
            )
        ),
        "noisy_alpha_2_unique_lower_endpoint": bool(
            all(
                audit["gates"][
                    "ratio_derivative_negative"
                ]
                for audit in phase_audits.values()
            )
        ),
        "noisy_alpha_3_ratio_exact": bool(
            noisy_alpha_3_ratio
            == sp.Rational(
                202875104,
                179268705,
            )
        ),
    }

    verdict = (
        "PASS_CONTINUOUS_FIRST_ANCHOR_BOUNDARY_OPTIMALITY"
        if all(gates.values())
        else "FAIL_A50_FIRST_ANCHOR_AUDIT"
    )

    result = {
        "audit": (
            "A50_CONTINUOUS_FIRST_TARGET_EXCLUDING_ANCHOR"
        ),
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "target_exponent": 1,
            "alpha_domain": "[2,3]",
            "s_definition": "s=2^(-alpha)",
            "exact_design": "{alpha,3,4}*log(2)",
            "noisy_design": (
                "{alpha,3,infinity}*log(2)"
            ),
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
        "endpoints": {
            "exact_alpha_2_ratio": str(
                EXACT["ratio"].subs(
                    s,
                    sp.Rational(1, 4),
                )
            ),
            "exact_distinct_alpha_3_limit": str(
                EXACT["ratio"].subs(
                    s,
                    sp.Rational(1, 8),
                )
            ),
            "exact_duplicated_alpha_3_ratio": str(
                EXACT_ENDPOINT["ratio"]
            ),
            "noisy_alpha_2_ratio": str(
                noisy_alpha_2_ratio
            ),
            "noisy_alpha_2_future_risk": str(
                sp.N(
                    sp.log(noisy_alpha_2_ratio)
                    / (2 * sp.log(2)),
                    40,
                )
            ),
            "noisy_alpha_3_ratio": str(
                noisy_alpha_3_ratio
            ),
            "noisy_alpha_3_future_risk": str(
                sp.N(
                    sp.log(noisy_alpha_3_ratio)
                    / (2 * sp.log(2)),
                    40,
                )
            ),
        },
        "formal_results": [
            (
                "exact ratio strictly increases with alpha "
                "for distinct anchors"
            ),
            (
                "exact duplicated endpoint is discontinuous"
            ),
            (
                "seven exact noisy primal-dual phases "
                "cover [2,3]"
            ),
            "six unique algebraic transitions",
            (
                "noisy ratio is continuous and strictly "
                "increasing in alpha"
            ),
            (
                "alpha=2 is the unique minimizer in both "
                "controlled contracts"
            ),
            (
                "the optimum is a declared-domain boundary, "
                "not a universal physical constant"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The result is exact only for alpha in [2,3], "
            "the six-point support, exact mean, contract-specific "
            "third observations, common error, and direct future-Q "
            "risk. It does not cover anchors between the target "
            "exponent 1 and the declared lower boundary 2."
        ),
    }

    output_path = HERE / (
        "a50_continuous_first_anchor_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "transition_count": len(TRANSITION_ROOTS),
        "noisy_phase_count": len(NOISY_PHASES),
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "exact_winner_alpha": 2,
        "noisy_winner_alpha": 2,
        "verdict": verdict,
    }
    print(json.dumps(summary, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
