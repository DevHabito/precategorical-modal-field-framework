#!/usr/bin/env python3
"""A56 exact audit: cost-regularized finite-cap policy.

The audit works on the certified A55 family

    D_Gamma = {2, beta*, Gamma}, Gamma >= 6.

It proves:
- strict risk improvement with Gamma;
- strict diminishing one-step returns;
- complete linear-cost threshold policy;
- logarithmic small-cost scaling.

No empirical or monetary value is assigned to the abstract unit cost.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A52_SCRIPT = HERE / "a52_continuous_second_anchor_audit.py"
A55_SCRIPT = HERE / "a55_finite_cap_implementability_audit.py"
A55_RESULTS = HERE / "a55_finite_cap_implementability_results.json"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")

    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main() -> None:
    if not A52_SCRIPT.exists():
        raise FileNotFoundError(A52_SCRIPT)
    if not A55_SCRIPT.exists():
        raise FileNotFoundError(A55_SCRIPT)
    if not A55_RESULTS.exists():
        raise FileNotFoundError(A55_RESULTS)

    a52 = load_module(A52_SCRIPT, "a52_for_a56")
    a55 = load_module(A55_SCRIPT, "a55_for_a56")

    a55_results = json.loads(
        A55_RESULTS.read_text(encoding="utf-8")
    )

    certificate = a55.build_bivariate_certificate(a52)

    s = certificate["s"]
    r = certificate["r"]
    ratio = sp.cancel(certificate["ratio"])
    s_star = a52.s_star

    s_lower = sp.Rational(3, 20)
    s_upper = sp.Rational(19, 125)
    r_lower = sp.Rational(0)
    r_upper = sp.Rational(1, 64)
    box = (s_lower, s_upper, r_lower, r_upper)

    ratio_derivative = sp.cancel(
        sp.diff(ratio, r)
    )

    risk_derivative_sign = (
        a55.certify_rational_sign_adaptive(
            ratio_derivative,
            1,
            s,
            r,
            box,
            max_depth=7,
        )
    )

    ratio_half = sp.cancel(
        ratio.subs(r, r / 2)
    )
    ratio_derivative_half = sp.cancel(
        sp.diff(ratio, r).subs(r, r / 2)
    )

    diminishing_expression = sp.cancel(
        sp.diff(ratio, r) / ratio
        -
        sp.Rational(1, 2)
        * ratio_derivative_half
        / ratio_half
    )

    diminishing_sign = (
        a55.certify_rational_sign_adaptive(
            diminishing_expression,
            1,
            s,
            r,
            box,
            max_depth=7,
        )
    )

    def risk_expression(gamma: int) -> sp.Expr:
        ratio_value = ratio.subs(
            {
                s: s_star,
                r: sp.Rational(1, 2**gamma),
            }
        )
        return (
            sp.log(ratio_value)
            / (2 * sp.log(2))
        )

    gamma_min = 6
    gamma_max = 30

    risk_table = []
    gain_expressions: dict[int, sp.Expr] = {}

    for gamma in range(gamma_min, gamma_max + 1):
        risk = risk_expression(gamma)

        row: dict[str, Any] = {
            "gamma": gamma,
            "risk_expression": str(risk),
            "risk_decimal": str(sp.N(risk, 50)),
        }

        if gamma < gamma_max:
            gain = sp.factor(
                risk
                - risk_expression(gamma + 1)
            )
            gain_expressions[gamma] = gain
            row["next_step_gain_expression"] = str(gain)
            row["next_step_gain_decimal"] = str(
                sp.N(gain, 50)
            )

        risk_table.append(row)

    finite_gain_positive = all(
        sp.N(gain, 80) > 0
        for gain in gain_expressions.values()
    )

    finite_gain_decreasing = all(
        sp.N(
            gain_expressions[gamma]
            - gain_expressions[gamma + 1],
            80,
        )
        > 0
        for gamma in range(gamma_min, gamma_max - 1)
    )

    kappa_q = sp.sympify(
        a55_results["asymptotic"][
            "risk_linear_coefficient"
        ]
    )

    asymptotic_ratios = []
    for gamma in [20, 24, 28, 30]:
        gain = gain_expressions.get(gamma)
        if gain is None:
            gain = sp.factor(
                risk_expression(gamma)
                - risk_expression(gamma + 1)
            )

        leading = (
            kappa_q
            * sp.Rational(1, 2 ** (gamma + 1))
        )

        asymptotic_ratios.append(
            {
                "gamma": gamma,
                "gain_decimal": str(sp.N(gain, 50)),
                "leading_decimal": str(sp.N(leading, 50)),
                "gain_over_leading": str(
                    sp.N(gain / leading, 50)
                ),
            }
        )

    example_costs = [
        sp.Rational(1, 10**5),
        sp.Rational(1, 10**6),
        sp.Rational(1, 10**7),
        sp.Rational(1, 10**8),
        sp.Rational(1, 10**9),
    ]

    example_policy = []

    for cost in example_costs:
        candidates = []

        for gamma in range(6, 41):
            objective = (
                risk_expression(gamma)
                + cost * gamma
            )
            candidates.append(
                (objective, gamma)
            )

        best_objective, best_gamma = min(
            candidates,
            key=lambda pair: float(
                sp.N(pair[0], 50)
            ),
        )

        example_policy.append(
            {
                "cost": str(cost),
                "cost_decimal": str(sp.N(cost, 20)),
                "selected_gamma": best_gamma,
                "risk_decimal": str(
                    sp.N(
                        risk_expression(best_gamma),
                        50,
                    )
                ),
                "total_objective_decimal": str(
                    sp.N(best_objective, 50)
                ),
            }
        )

    break_even_table = []

    for gamma in range(6, 21):
        gain = gain_expressions[gamma]
        break_even_table.append(
            {
                "upgrade": f"{gamma}->{gamma + 1}",
                "gamma": gamma,
                "break_even_cost_expression": str(gain),
                "break_even_cost_decimal": str(
                    sp.N(gain, 50)
                ),
            }
        )

    policy_gate = {
        sp.Rational(1, 10**5): 8,
        sp.Rational(1, 10**6): 11,
        sp.Rational(1, 10**7): 14,
        sp.Rational(1, 10**8): 17,
        sp.Rational(1, 10**9): 20,
    }

    example_policy_correct = all(
        next(
            item["selected_gamma"]
            for item in example_policy
            if item["cost"] == str(cost)
        )
        == expected
        for cost, expected in policy_gate.items()
    )

    a55_gates = a55_results["gates"]

    gates = {
        "A55_complete_audit_passed": bool(
            all(a55_gates.values())
        ),
        "risk_strictly_increases_with_r": bool(
            risk_derivative_sign["ok"]
        ),
        "one_step_gain_function_increases_with_r": bool(
            diminishing_sign["ok"]
        ),
        "finite_risks_strictly_decrease_with_gamma": bool(
            finite_gain_positive
        ),
        "finite_one_step_gains_strictly_decrease": bool(
            finite_gain_decreasing
        ),
        "linear_cost_examples_match_threshold_rule": bool(
            example_policy_correct
        ),
        "asymptotic_gain_ratio_converges_to_one": bool(
            abs(
                float(
                    asymptotic_ratios[-1][
                        "gain_over_leading"
                    ]
                )
                - 1.0
            )
            < 1e-6
        ),
    }

    verdict = (
        "PASS_COST_REGULARIZED_FINITE_CAP_POLICY_AND_DIMINISHING_RETURNS"
        if all(gates.values())
        else "FAIL_A56_COST_REGULARIZATION_AUDIT"
    )

    result = {
        "audit": "A56_COST_REGULARIZED_FINITE_CAP_POLICY",
        "contract": {
            "family": "{2,beta-star,Gamma}*log(2)",
            "gamma_domain": "integer Gamma>=6",
            "unit_cost": "c risk-units per one cap increment",
            "objective": "J_c(Gamma)=Q_Gamma+c*Gamma",
            "epsilon": "1/10000",
        },
        "derivative_certificates": {
            "risk_derivative_sign": risk_derivative_sign,
            "diminishing_returns_sign": diminishing_sign,
            "diminishing_rational_expression": str(
                diminishing_expression
            ),
        },
        "risk_table": risk_table,
        "break_even_table": break_even_table,
        "example_policy": example_policy,
        "asymptotic": {
            "kappa_Q": str(kappa_q),
            "gain_law": (
                "G_Gamma = kappa_Q*2^(-(Gamma+1)) "
                "+ O(4^(-Gamma))"
            ),
            "selected_cap_scale": (
                "Gamma_c approximately "
                "log2(kappa_Q/(2c))"
            ),
            "checks": asymptotic_ratios,
        },
        "decision_rule": {
            "high_cost": (
                "If c>G_6, Gamma=6 is unique."
            ),
            "interior": (
                "For n>=7, if G_n<c<G_(n-1), "
                "Gamma=n is unique."
            ),
            "ties": (
                "At c=G_n, n and n+1 tie."
            ),
            "zero_cost": (
                "At c=0, the compactified limit is recovered."
            ),
        },
        "formal_results": [
            "strict finite-cap risk improvement",
            "strict diminishing marginal returns",
            "complete integer linear-cost threshold policy",
            "all caps are Pareto efficient in the fixed family",
            "selected cap grows logarithmically as cost falls",
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The theorem applies to the fixed beta-star implementation "
            "family. The abstract cost c is not an empirical monetary, "
            "time, energy, or hardware cost, and beta is not jointly "
            "reoptimized under the cost objective."
        ),
    }

    output_path = HERE / (
        "a56_cost_regularized_finite_cap_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "example_policy": {
            item["cost_decimal"]: item["selected_gamma"]
            for item in example_policy
        },
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
