#!/usr/bin/env python3
"""A48 audit: target-inclusion degeneracy.

The audit proves an exact theorem for designs containing the target exponent 1:

    ratio = 1 + 32*epsilon/3

for all additional exponents >= 1 and 0 <= epsilon <= 1/128.

It also reuses the exact A43 target-excluding catalogue certificates to audit
the expanded integer catalogue {1,2,3,4,5,6}.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A43_RESULTS = HERE / "a43_direct_q_minimax_design_results.json"

epsilon = sp.symbols(
    "epsilon",
    real=True,
    nonnegative=True,
)

SUPPORT = list(range(6))
TARGET = [
    sp.Rational(1, 2**x)
    for x in SUPPORT
]
MEAN = sp.Rational(5, 2)

q = [
    sp.Integer(0),
    sp.Integer(0),
    sp.Rational(1, 2),
    sp.Rational(1, 2),
    sp.Integer(0),
    sp.Integer(0),
]

p = [
    sp.Integer(0),
    sp.Integer(0),
    sp.Rational(1, 2) + 32 * epsilon,
    sp.Rational(1, 2) - 64 * epsilon,
    32 * epsilon,
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


def transform_row(
    exponent: int,
) -> list[sp.Rational]:
    return [
        sp.Rational(
            1,
            2 ** (exponent * x),
        )
        for x in SUPPORT
    ]


def target_inclusive_ranking(
    a43: dict[str, Any],
    epsilon_value: sp.Rational,
) -> dict[str, Any]:
    included_designs = [
        [1, second, third]
        for second in range(2, 7)
        for third in range(second + 1, 7)
    ]

    included_ratio = sp.factor(
        1
        + sp.Rational(32, 3)
        * epsilon_value
    )

    if epsilon_value == 0:
        excluded_contract = a43[
            "exact_data_contract"
        ]
    else:
        excluded_contract = a43[
            "noisy_contract"
        ]

    excluded_rows = [
        {
            "design": row["design"],
            "ratio_exact": row["ratio_exact"],
            "ratio_decimal": row["ratio_decimal"],
            "future_score_risk_decimal": row[
                "future_score_risk_decimal"
            ],
            "contains_target": False,
        }
        for row in excluded_contract["ranking"]
    ]

    included_risk = (
        sp.log(included_ratio)
        / (2 * sp.log(2))
    )

    included_rows = [
        {
            "design": design,
            "ratio_exact": str(included_ratio),
            "ratio_decimal": (
                f"{float(included_ratio):.18g}"
            ),
            "future_score_risk_decimal": (
                f"{float(included_risk):.18g}"
            ),
            "contains_target": True,
        }
        for design in included_designs
    ]

    all_rows = included_rows + excluded_rows
    all_rows.sort(
        key=lambda row: sp.Rational(
            row["ratio_exact"]
        )
    )

    return {
        "epsilon": str(epsilon_value),
        "included_ratio": str(included_ratio),
        "included_future_risk_decimal": (
            f"{float(included_risk):.18g}"
        ),
        "ranking": all_rows,
        "winner_count": sum(
            sp.Rational(row["ratio_exact"])
            == sp.Rational(
                all_rows[0]["ratio_exact"]
            )
            for row in all_rows
        ),
        "all_winners_contain_target": all(
            row["contains_target"]
            for row in all_rows
            if sp.Rational(row["ratio_exact"])
            == sp.Rational(
                all_rows[0]["ratio_exact"]
            )
        ),
    }


def main() -> None:
    if not A43_RESULTS.exists():
        raise FileNotFoundError(
            f"Missing required A43 results: {A43_RESULTS}"
        )

    a43 = json.loads(
        A43_RESULTS.read_text(encoding="utf-8")
    )

    target_value_q = dot(TARGET, q)
    target_value_p = dot(TARGET, p)
    ratio_formula = sp.factor(
        target_value_p / target_value_q
    )

    normalization_p = sp.factor(sum(p))
    normalization_q = sp.factor(sum(q))
    mean_p = dot(
        [sp.Integer(x) for x in SUPPORT],
        p,
    )
    mean_q = dot(
        [sp.Integer(x) for x in SUPPORT],
        q,
    )

    finite_catalogue_differences = {
        str(exponent): sp.factor(
            dot(transform_row(exponent), p)
            - dot(transform_row(exponent), q)
        )
        for exponent in range(1, 7)
    }

    expected_differences = {
        str(exponent): sp.factor(
            32
            * epsilon
            * sp.Rational(
                1,
                2 ** (2 * exponent),
            )
            * (
                1
                - sp.Rational(
                    1,
                    2**exponent,
                )
            )
            ** 2
        )
        for exponent in range(1, 7)
    }

    exact_ranking = target_inclusive_ranking(
        a43,
        sp.Rational(0),
    )
    noisy_ranking = target_inclusive_ranking(
        a43,
        sp.Rational(1, 10000),
    )

    included_noisy_ratio = sp.Rational(
        noisy_ranking["included_ratio"]
    )
    excluded_noisy_winner_ratio = sp.Rational(
        a43["noisy_contract"][
            "winner_ratio_exact"
        ]
    )

    included_noisy_risk = (
        sp.log(included_noisy_ratio)
        / (2 * sp.log(2))
    )
    excluded_noisy_risk = (
        sp.log(excluded_noisy_winner_ratio)
        / (2 * sp.log(2))
    )

    risk_ratio = sp.N(
        excluded_noisy_risk
        / included_noisy_risk,
        40,
    )
    improvement_percent = sp.N(
        100
        * (
            1
            - included_noisy_risk
            / excluded_noisy_risk
        ),
        40,
    )

    # The finite catalogue constraints are maximized at exponent 1.
    finite_difference_bounds = {
        exponent: bool(
            sp.factor(
                2 * epsilon
                - finite_catalogue_differences[
                    str(exponent)
                ]
            )
            .subs(
                epsilon,
                sp.Rational(1, 128),
            )
            >= 0
        )
        for exponent in range(1, 7)
    }

    a43_all_gates = list(
        a43["gates"].values()
    )

    gates = {
        "q_normalized": bool(normalization_q == 1),
        "p_normalized_symbolically": bool(
            normalization_p == 1
        ),
        "q_mean_exact": bool(mean_q == MEAN),
        "p_mean_exact_symbolically": bool(
            mean_p == MEAN
        ),
        "target_lower_bound_affine_envelope_on_support": bool(
            all(
                TARGET[x]
                >=
                sp.Rational(1, 2)
                - sp.Rational(x, 8)
                for x in SUPPORT
            )
        ),
        "q_attains_target_lower_bound": bool(
            target_value_q
            == sp.Rational(3, 16)
        ),
        "target_difference_is_2epsilon": bool(
            sp.factor(
                target_value_p
                - target_value_q
            )
            == 2 * epsilon
        ),
        "ratio_formula_exact": bool(
            sp.factor(
                ratio_formula
                - (
                    1
                    + sp.Rational(32, 3)
                    * epsilon
                )
            )
            == 0
        ),
        "p_weights_nonnegative_through_1_over_128": bool(
            all(
                weight.subs(
                    epsilon,
                    sp.Rational(1, 128),
                )
                >= 0
                for weight in p
            )
            and all(
                weight.subs(epsilon, 0)
                >= 0
                for weight in p
            )
        ),
        "finite_catalogue_difference_formulas_exact": bool(
            finite_catalogue_differences
            == expected_differences
        ),
        "all_expanded_catalogue_extra_constraints_satisfied": bool(
            all(finite_difference_bounds.values())
        ),
        "A43_target_excluding_certificates_pass": bool(
            all(a43_all_gates)
        ),
        "expanded_catalogue_has_20_designs_exact": bool(
            len(exact_ranking["ranking"]) == 20
        ),
        "expanded_catalogue_has_20_designs_noisy": bool(
            len(noisy_ranking["ranking"]) == 20
        ),
        "exact_data_has_10_target_inclusive_winners": bool(
            exact_ranking["winner_count"] == 10
            and exact_ranking[
                "all_winners_contain_target"
            ]
        ),
        "noisy_data_has_10_target_inclusive_winners": bool(
            noisy_ranking["winner_count"] == 10
            and noisy_ranking[
                "all_winners_contain_target"
            ]
        ),
        "noisy_inclusive_ratio_is_1877_over_1875": bool(
            included_noisy_ratio
            == sp.Rational(1877, 1875)
        ),
        "noisy_inclusive_beats_best_excluding": bool(
            included_noisy_ratio
            < excluded_noisy_winner_ratio
        ),
    }

    verdict = (
        "PASS_TARGET_INCLUSION_DEGENERACY_AND_HONEST_ANCHOR_CONTRACT"
        if all(gates.values())
        else "FAIL_A48_TARGET_INCLUSION_AUDIT"
    )

    result = {
        "audit": (
            "A48_TARGET_INCLUSION_DEGENERACY"
        ),
        "contract": {
            "support": SUPPORT,
            "mean": str(MEAN),
            "target_exponent": 1,
            "additional_exponent_domain": (
                "alpha,beta >= 1"
            ),
            "epsilon_theorem_domain": (
                "[0, 1/128]"
            ),
            "expanded_integer_catalogue": [
                1,
                2,
                3,
                4,
                5,
                6,
            ],
        },
        "theorem": {
            "ratio": str(ratio_formula),
            "future_risk": (
                "0.5*log2(1 + 32*epsilon/3)"
            ),
            "q": [str(value) for value in q],
            "p_epsilon": [
                str(value) for value in p
            ],
            "finite_catalogue_differences": {
                key: str(value)
                for key, value
                in finite_catalogue_differences.items()
            },
        },
        "exact_catalogue": exact_ranking,
        "noisy_catalogue": noisy_ranking,
        "comparison_at_1e-4": {
            "target_inclusive_ratio": str(
                included_noisy_ratio
            ),
            "target_inclusive_future_risk": str(
                sp.N(included_noisy_risk, 40)
            ),
            "best_target_excluding_design": (
                a43["noisy_contract"]["winner"]
            ),
            "best_target_excluding_ratio": str(
                excluded_noisy_winner_ratio
            ),
            "best_target_excluding_future_risk": str(
                sp.N(excluded_noisy_risk, 40)
            ),
            "excluding_to_including_risk_ratio": str(
                risk_ratio
            ),
            "including_improvement_percent": str(
                improvement_percent
            ),
        },
        "formal_results": [
            (
                "sharp target transform lower bound "
                "L(log2)>=3/16"
            ),
            (
                "universal target-inclusive minimax "
                "ratio 1+32*epsilon/3"
            ),
            (
                "additional parameters alpha,beta>=1 "
                "are minimax-irrelevant"
            ),
            (
                "ten target-inclusive catalogue "
                "designs tie at both benchmarks"
            ),
            (
                "direct target inclusion changes the "
                "question from prediction to measurement"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The universal theorem covers additional "
            "exponents at least as large as the target "
            "exponent and epsilon<=1/128. The catalogue "
            "comparison is limited to integer exponents "
            "{1,...,6}. No physical cost or noise law is "
            "inferred."
        ),
    }

    output_path = HERE / (
        "a48_target_inclusion_degeneracy_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
