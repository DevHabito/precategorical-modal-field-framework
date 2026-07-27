#!/usr/bin/env python3
"""A68 exact audit: dual envelopes and first-channel value.

This audit uses the already certified A67 phase sign records and independently
solves the five channel-removal problems in exact primal and dual rational LP
form.

Exact results:
- all 33 A67 phases use the positive alpha band;
- the Charnes-Cooper scale and the positive alpha multiplier are strictly
  positive in every phase;
- hence d rho / d epsilon_alpha = 2 t lambda_alpha^+ > 0;
- deleting alpha gives exactly the alpha->3- coalescence value;
- deletion strictly worsens risk for M=5,...,9.

The analytic dual-envelope theorem is general for this LP formulation. The
positivity and removal conclusions are exact for the five A67 family members.
"""

from __future__ import annotations

import concurrent.futures
import json
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.solvers.simplex import lpmax, lpmin


HERE = Path(__file__).resolve().parent
A67_RESULTS = HERE / "a67_central_mean_support_family_results.json"

FAMILY = {
    5: (sp.Rational(5, 2), sp.Rational(1, 10000), 10),
    6: (sp.Rational(3), sp.Rational(1, 15000), 5),
    7: (sp.Rational(7, 2), sp.Rational(1, 20000), 4),
    8: (sp.Rational(4), sp.Rational(1, 30000), 4),
    9: (sp.Rational(9, 2), sp.Rational(1, 40000), 4),
}


def build_two_anchor_primal(
    maximum: int,
    mean: sp.Rational,
    epsilon: sp.Rational,
    design: tuple[int, int],
) -> tuple[sp.Expr, list[sp.Rel]]:
    support = list(range(maximum + 1))
    count = maximum + 1

    p = sp.symbols(f"p0:{count}")
    q = sp.symbols(f"q0:{count}")
    scale = sp.Symbol("scale")
    variables = list(p) + list(q) + [scale]

    target = [sp.Rational(1, 2 ** x) for x in support]
    objective = sum(target[index] * p[index] for index in range(count))

    constraints: list[sp.Rel] = [
        sp.Eq(sum(p), scale),
        sp.Eq(sum(q), scale),
        sp.Eq(
            sum(support[index] * p[index] for index in range(count)),
            mean * scale,
        ),
        sp.Eq(
            sum(support[index] * q[index] for index in range(count)),
            mean * scale,
        ),
        sp.Eq(
            sum(target[index] * q[index] for index in range(count)),
            1,
        ),
    ]
    constraints.extend(variable >= 0 for variable in variables)

    for exponent in design:
        values = [
            sp.Rational(1, 2 ** (exponent * x))
            for x in support
        ]
        difference = sum(
            values[index] * (p[index] - q[index])
            for index in range(count)
        )
        constraints.extend(
            [
                difference <= 2 * epsilon * scale,
                -difference <= 2 * epsilon * scale,
            ]
        )

    return objective, constraints


def solve_two_anchor_primal(
    maximum: int,
    mean: sp.Rational,
    epsilon: sp.Rational,
    design: tuple[int, int],
) -> sp.Expr:
    objective, constraints = build_two_anchor_primal(
        maximum,
        mean,
        epsilon,
        design,
    )
    value, _ = lpmax(objective, constraints)
    return sp.factor(value)


def solve_two_anchor_dual(
    maximum: int,
    mean: sp.Rational,
    epsilon: sp.Rational,
    design: tuple[int, int],
) -> sp.Expr:
    support = list(range(maximum + 1))
    count = maximum + 1
    dimension = 2 * count + 1
    target = [sp.Rational(1, 2 ** x) for x in support]

    equality_rows: list[list[sp.Rational]] = []
    equality_rhs: list[sp.Rational] = []

    row = [sp.Rational(0)] * dimension
    for index in range(count):
        row[index] = 1
    row[-1] = -1
    equality_rows.append(row)
    equality_rhs.append(0)

    row = [sp.Rational(0)] * dimension
    for index in range(count):
        row[count + index] = 1
    row[-1] = -1
    equality_rows.append(row)
    equality_rhs.append(0)

    row = [sp.Rational(0)] * dimension
    for index, x in enumerate(support):
        row[index] = x
    row[-1] = -mean
    equality_rows.append(row)
    equality_rhs.append(0)

    row = [sp.Rational(0)] * dimension
    for index, x in enumerate(support):
        row[count + index] = x
    row[-1] = -mean
    equality_rows.append(row)
    equality_rhs.append(0)

    row = [sp.Rational(0)] * dimension
    for index in range(count):
        row[count + index] = target[index]
    equality_rows.append(row)
    equality_rhs.append(1)

    inequality_rows: list[list[sp.Rational]] = []
    inequality_rhs: list[sp.Rational] = []

    for exponent in design:
        values = [
            sp.Rational(1, 2 ** (exponent * x))
            for x in support
        ]
        difference = [sp.Rational(0)] * dimension
        for index in range(count):
            difference[index] = values[index]
            difference[count + index] = -values[index]

        positive = list(difference)
        positive[-1] = -2 * epsilon
        inequality_rows.append(positive)
        inequality_rhs.append(0)

        negative = [-value for value in difference]
        negative[-1] = -2 * epsilon
        inequality_rows.append(negative)
        inequality_rhs.append(0)

    objective = [sp.Rational(0)] * dimension
    for index in range(count):
        objective[index] = target[index]

    equality_count = len(equality_rows)
    inequality_count = len(inequality_rows)

    y_plus = sp.symbols(f"yp0:{equality_count}")
    y_minus = sp.symbols(f"ym0:{equality_count}")
    multipliers = sp.symbols(f"z0:{inequality_count}")

    variables = list(y_plus) + list(y_minus) + list(multipliers)
    dual_objective = sum(
        equality_rhs[index] * (y_plus[index] - y_minus[index])
        for index in range(equality_count)
    )
    dual_objective += sum(
        inequality_rhs[index] * multipliers[index]
        for index in range(inequality_count)
    )

    constraints: list[sp.Rel] = [variable >= 0 for variable in variables]

    for column in range(dimension):
        expression = sum(
            equality_rows[row_index][column]
            * (y_plus[row_index] - y_minus[row_index])
            for row_index in range(equality_count)
        )
        expression += sum(
            inequality_rows[row_index][column] * multipliers[row_index]
            for row_index in range(inequality_count)
        )
        constraints.append(expression >= objective[column])

    value, _ = lpmin(dual_objective, constraints)
    return sp.factor(value)


def solve_removal_case(maximum: int) -> dict[str, Any]:
    mean, epsilon, gamma = FAMILY[maximum]
    design = (3, gamma)
    primal = solve_two_anchor_primal(maximum, mean, epsilon, design)
    dual = solve_two_anchor_dual(maximum, mean, epsilon, design)
    return {
        "maximum": maximum,
        "mean": str(mean),
        "epsilon": str(epsilon),
        "remaining_design": list(design),
        "primal_ratio": str(primal),
        "dual_ratio": str(dual),
        "primal_dual_equal": bool(primal == dual),
    }


def main() -> None:
    if not A67_RESULTS.exists():
        raise FileNotFoundError(A67_RESULTS)

    a67 = json.loads(A67_RESULTS.read_text(encoding="utf-8"))

    activity = {
        "alpha_positive": 0,
        "alpha_negative": 0,
        "alpha_inactive": 0,
        "beta_positive": 0,
        "beta_negative": 0,
        "beta_inactive": 0,
        "gamma_positive": 0,
        "gamma_negative": 0,
        "gamma_inactive": 0,
    }
    phase_signs = []

    for support in a67["supports"]:
        maximum = support["maximum"]
        scale_name = f"basic_{2 * (maximum + 1)}"

        for phase in support["phases"]:
            active = {tuple(item) for item in phase["active_observations"]}
            conditions = {item["name"]: item for item in phase["conditions"]}

            for channel in ["alpha", "beta", "gamma"]:
                if (channel, 1) in active:
                    activity[f"{channel}_positive"] += 1
                elif (channel, -1) in active:
                    activity[f"{channel}_negative"] += 1
                else:
                    activity[f"{channel}_inactive"] += 1

            scale_positive = bool(
                conditions[scale_name]["ok"]
                and conditions[scale_name]["sample_sign"] > 0
            )
            alpha_positive = bool(
                conditions["active_dual_alpha_+1"]["ok"]
                and conditions["active_dual_alpha_+1"]["sample_sign"] > 0
            )

            phase_signs.append(
                {
                    "maximum": maximum,
                    "phase": phase["phase"],
                    "active_observations": phase["active_observations"],
                    "scale_positive": scale_positive,
                    "alpha_multiplier_positive": alpha_positive,
                    "ratio_tolerance_derivative_positive": bool(
                        scale_positive and alpha_positive
                    ),
                }
            )

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        removal_raw = list(executor.map(solve_removal_case, FAMILY.keys()))

    removal_by_M = {item["maximum"]: item for item in removal_raw}
    removal_results = []

    for support in a67["supports"]:
        maximum = support["maximum"]
        removal = removal_by_M[maximum]
        boundary = sp.Rational(support["boundary_ratio"])
        coalescence = sp.Rational(support["coalescence_ratio_limit"])
        removed = sp.Rational(removal["primal_ratio"])

        boundary_risk = sp.log(boundary) / (2 * sp.log(2))
        removed_risk = sp.log(removed) / (2 * sp.log(2))

        removal_results.append(
            {
                **removal,
                "full_boundary_ratio": str(boundary),
                "coalescence_ratio": str(coalescence),
                "removal_equals_coalescence": bool(removed == coalescence),
                "removal_strictly_worse": bool(removed > boundary),
                "full_boundary_risk_decimal": str(sp.N(boundary_risk, 50)),
                "removed_risk_decimal": str(sp.N(removed_risk, 50)),
                "absolute_risk_premium_decimal": str(
                    sp.N(removed_risk - boundary_risk, 50)
                ),
                "relative_risk_premium_percent": str(
                    sp.N(100 * (removed_risk / boundary_risk - 1), 50)
                ),
                "risk_multiplier": str(
                    sp.N(removed_risk / boundary_risk, 50)
                ),
            }
        )

    gates = {
        "A67_family_theorem_passed": bool(all(a67["gates"].values())),
        "positive_alpha_band_active_all_33_phases": bool(
            activity["alpha_positive"] == 33
            and activity["alpha_negative"] == 0
            and activity["alpha_inactive"] == 0
        ),
        "all_33_scale_and_alpha_multipliers_positive": bool(
            all(
                item["scale_positive"]
                and item["alpha_multiplier_positive"]
                for item in phase_signs
            )
        ),
        "beta_and_gamma_can_be_inactive": bool(
            activity["beta_inactive"] > 0
            and activity["gamma_inactive"] > 0
        ),
        "all_five_removal_primal_dual_certificates_exact": bool(
            all(item["primal_dual_equal"] for item in removal_results)
        ),
        "all_five_removal_values_equal_coalescence": bool(
            all(item["removal_equals_coalescence"] for item in removal_results)
        ),
        "all_five_removals_strictly_worsen_risk": bool(
            all(item["removal_strictly_worse"] for item in removal_results)
        ),
    }

    verdict = (
        "PASS_DUAL_ENVELOPE_AND_EXACT_FIRST_CHANNEL_VALUE"
        if all(gates.values())
        else "FAIL_A68_DUAL_CHANNEL_VALUE_AUDIT"
    )

    result = {
        "audit": "A68_DUAL_ENVELOPE_AND_FIRST_CHANNEL_VALUE",
        "dual_envelope_theorem": {
            "upper": (
                "A+Cx+sum_j w_j phi_j(x) >= phi_mu(x)"
            ),
            "lower": (
                "(-B-Dx+sum_j w_j phi_j(x))/rho <= phi_mu(x)"
            ),
            "shared_coefficients": "w_j=lambda_j^+-lambda_j^-",
            "contacts": (
                "Upper equality on active P support; lower equality on active Q support"
            ),
            "scalar_noise_budget": (
                "-A-B-mC-mD >= 2 sum_j epsilon_j(lambda_j^++lambda_j^-)"
            ),
        },
        "parametric_value_theorem": {
            "ratio_derivative": (
                "partial rho_star / partial epsilon_alpha = 2 t_star lambda_alpha^+"
            ),
            "Q_derivative": (
                "partial Q_star / partial epsilon_alpha = "
                "t_star lambda_alpha^+ /(ln(2) rho_star)"
            ),
            "conclusion": (
                "t_star>0 and lambda_alpha^+>0 in all 33 phases, so loosening "
                "the first-channel tolerance strictly worsens the optimum locally."
            ),
        },
        "phase_activity_counts": activity,
        "phase_sign_certificates": phase_signs,
        "channel_removal_theorem": {
            "statement": (
                "For M=5,...,9, deleting alpha and retaining {3,gamma_M} "
                "has exactly the same minimax value as lim_{alpha->3-}."
            ),
            "results": removal_results,
        },
        "formal_results": [
            "The minimax dual is an affine-exponential envelope sandwich.",
            "The positive alpha multiplier is exact in every A67 phase.",
            "First-channel tolerance has strictly positive marginal cost in every phase.",
            "Beta and gamma can become locally redundant; alpha does not in this family.",
            "Deleting alpha exactly equals the coalescence limit.",
            "Deleting alpha strictly worsens risk for all five supports.",
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A68 is exact for the five A67 family members and their fixed completions. "
            "It does not prove positive alpha shadow price for arbitrary supports, means, "
            "targets, or completions."
        ),
    }

    output = HERE / "a68_dual_envelope_channel_value_results.json"
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(
        json.dumps(
            {
                "audit": result["audit"],
                "gate_count": len(gates),
                "pass_count": sum(gates.values()),
                "phase_activity_counts": activity,
                "risk_multipliers": {
                    str(item["maximum"]): item["risk_multiplier"]
                    for item in removal_results
                },
                "failed_gates": [
                    name for name, value in gates.items() if not value
                ],
                "verdict": verdict,
            },
            indent=2,
        )
    )

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
