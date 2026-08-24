#!/usr/bin/env python3
"""A41 audit: robust interval-valued exponential data.

This audit validates two layers:

1. Reuse of the A39 certified continuous-support dual envelopes. The exact
   Krawczyk certificates are recomputed and converted into rigorous noisy-data
   outer bounds by the weighted l1 error penalty.

2. A fully exact finite-support parametric linear programme on support
   {0,1,2,3,4,5}. Rational primal and dual certificates prove sharp affine
   omitted-transform bounds for a common tolerance epsilon up to an exact
   breakpoint.

The general compactness, monotonicity, zero-noise convergence, and robust-dual
theorems are proved in the accompanying note. They are mathematical inputs,
not numerical claims.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
A39_PATH = HERE / "a39_sharp_prediction_interval_audit.py"

mp.mp.dps = 100
mp.iv.dps = 80
iv = mp.iv


def load_a39() -> Any:
    spec = importlib.util.spec_from_file_location("a39_module", A39_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load A39 audit module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def interval_pair(value: object, digits: int = 45) -> list[str]:
    return [
        mp.nstr(mp.mpf(value.a), digits),
        mp.nstr(mp.mpf(value.b), digits),
    ]


def interval_abs_upper(value: object) -> mp.mpf:
    return max(abs(mp.mpf(value.a)), abs(mp.mpf(value.b)))


def continuous_support_reuse() -> dict[str, Any]:
    a39 = load_a39()
    lower_center, upper_center = a39.solve_centers()
    lower_ok, lower_box = a39.krawczyk_certify(
        lower_center,
        a39.BOX_RADIUS,
        a39.lower_f,
        a39.lower_j_point,
        a39.lower_j_interval,
    )
    upper_ok, upper_box = a39.krawczyk_certify(
        upper_center,
        a39.BOX_RADIUS,
        a39.upper_f,
        a39.upper_j_point,
        a39.upper_j_interval,
    )

    lower_r0 = a39.lower_residual_at(mp.mpf(0), lower_box)
    lower_r4 = a39.lower_residual_at(mp.mpf(4), lower_box)
    upper_dp0 = a39.upper_derivative_at(mp.mpf(0), upper_box)
    upper_dp4 = a39.upper_derivative_at(mp.mpf(4), upper_box)

    x1, x2, w, *_ = lower_box
    exact_lower = (
        w * iv.exp(-a39.ivdeg(a39.MU) * x1)
        + (a39.ivdeg(1) - w) * iv.exp(-a39.ivdeg(a39.MU) * x2)
    )

    x, w0, w1, w4, *_ = upper_box
    exact_upper = (
        w0
        + w1 * iv.exp(-a39.ivdeg(a39.MU) * x)
        + w4 * iv.exp(-a39.ivdeg(a39.MU) * a39.ivdeg(4))
    )

    # Variables:
    # lower: x1,x2,w,y0,y_mean,y_L1,y_L2
    # upper: x,w0,w1,w4,y0,y_mean,y_L1,y_L2
    lower_penalty = interval_abs_upper(lower_box[5]) + interval_abs_upper(lower_box[6])
    upper_penalty = interval_abs_upper(upper_box[6]) + interval_abs_upper(upper_box[7])

    epsilons = [
        mp.mpf("0"),
        mp.mpf("1e-6"),
        mp.mpf("1e-5"),
        mp.mpf("1e-4"),
        mp.mpf("1e-3"),
    ]
    table = []
    support_floor = mp.exp(-4 * a39.MU)

    exact_lower_safe = mp.mpf(exact_lower.a)
    exact_upper_safe = mp.mpf(exact_upper.b)

    for eps in epsilons:
        noisy_lower = max(
            support_floor,
            exact_lower_safe - lower_penalty * eps,
        )
        noisy_upper = min(
            mp.mpf(1),
            exact_upper_safe + upper_penalty * eps,
        )
        q_lower = -mp.log(noisy_upper) / a39.MU
        q_upper = -mp.log(noisy_lower) / a39.MU
        future_lower = mp.mpf(1) + mp.mpf("0.5") * q_lower
        future_upper = mp.mpf(1) + mp.mpf("0.5") * q_upper

        table.append(
            {
                "epsilon": mp.nstr(eps, 12),
                "certified_L_lower": mp.nstr(noisy_lower, 40),
                "certified_L_upper": mp.nstr(noisy_upper, 40),
                "certified_future_lower": mp.nstr(future_lower, 40),
                "certified_future_upper": mp.nstr(future_upper, 40),
                "certified_future_width": mp.nstr(
                    future_upper - future_lower, 40
                ),
            }
        )

    gates = {
        "A39_lower_krawczyk_recomputed": bool(lower_ok),
        "A39_upper_krawczyk_recomputed": bool(upper_ok),
        "A39_lower_global_sign_inputs_recomputed": (
            mp.mpf(lower_r0.a) > 0 and mp.mpf(lower_r4.a) > 0
        ),
        "A39_upper_global_sign_inputs_recomputed": (
            mp.mpf(upper_dp0.a) > 0 and mp.mpf(upper_dp4.b) < 0
        ),
        "lower_penalty_positive": lower_penalty > 0,
        "upper_penalty_positive": upper_penalty > 0,
        "noisy_intervals_nested_in_epsilon": all(
            mp.mpf(table[i]["certified_L_lower"])
            >= mp.mpf(table[i + 1]["certified_L_lower"])
            and mp.mpf(table[i]["certified_L_upper"])
            <= mp.mpf(table[i + 1]["certified_L_upper"])
            for i in range(len(table) - 1)
        ),
    }

    return {
        "exact_L_interval": {
            "lower": interval_pair(exact_lower),
            "upper": interval_pair(exact_upper),
        },
        "transform_only_penalty_coefficients": {
            "lower": mp.nstr(lower_penalty, 55),
            "upper": mp.nstr(upper_penalty, 55),
        },
        "table": table,
        "gates": gates,
    }


def exact_finite_support_layer() -> dict[str, Any]:
    epsilon = sp.symbols("epsilon", nonnegative=True)
    support = list(range(6))

    one = [sp.Integer(1) for _ in support]
    mean_row = [sp.Integer(x) for x in support]
    r2 = [sp.Rational(1, 2 ** (2 * x)) for x in support]
    r3 = [sp.Rational(1, 2 ** (3 * x)) for x in support]
    r4 = [sp.Rational(1, 2 ** (4 * x)) for x in support]
    target = [sp.Rational(1, 2**x) for x in support]

    mean_value = sp.Rational(5, 2)
    b2 = sp.Rational(455, 2048)
    b3 = sp.Rational(12483, 65536)
    b4 = sp.Rational(372827, 2097152)

    basis_rows = [one, mean_row, r2, r3, r4]

    lower_dual = [
        sp.Rational(3427, 25935),
        -sp.Rational(31, 1482),
        sp.Rational(8876, 2223),
        -sp.Rational(11456, 1729),
        sp.Rational(2048, 585),
    ]
    upper_dual = [
        sp.Rational(3287, 20475),
        -sp.Rational(31, 1170),
        sp.Rational(1204, 351),
        -sp.Rational(480, 91),
        sp.Rational(23552, 8775),
    ]

    def envelope_values(coefficients: list[sp.Rational]) -> list[sp.Rational]:
        return [
            sp.factor(
                sum(coefficients[j] * basis_rows[j][i] for j in range(5))
            )
            for i in support
        ]

    lower_h = envelope_values(lower_dual)
    upper_h = envelope_values(upper_dual)
    lower_residual = [
        sp.factor(target[i] - lower_h[i]) for i in support
    ]
    upper_residual = [
        sp.factor(target[i] - upper_h[i]) for i in support
    ]

    lower_penalty = sp.factor(
        abs(lower_dual[2]) + abs(lower_dual[3]) + abs(lower_dual[4])
    )
    upper_penalty = sp.factor(
        abs(upper_dual[2]) + abs(upper_dual[3]) + abs(upper_dual[4])
    )

    central_lower = sp.Rational(5173, 15808)
    central_upper = sp.Rational(3283, 9984)
    lower_formula = sp.factor(central_lower - lower_penalty * epsilon)
    upper_formula = sp.factor(central_upper + upper_penalty * epsilon)
    width_formula = sp.factor(upper_formula - lower_formula)

    # Lower primal: p3=0 and transform constraints at (-,+,-) endpoints.
    lower_matrix = sp.Matrix([one, mean_row, r2, r3, r4, [0, 0, 0, 1, 0, 0]])
    lower_rhs = sp.Matrix(
        [
            1,
            mean_value,
            b2 - epsilon,
            b3 + epsilon,
            b4 - epsilon,
            0,
        ]
    )
    p_lower = [sp.factor(v) for v in lower_matrix.inv() * lower_rhs]

    # Upper primal: p4=0 and transform constraints at (+,-,+) endpoints.
    upper_matrix = sp.Matrix([one, mean_row, r2, r3, r4, [0, 0, 0, 0, 1, 0]])
    upper_rhs = sp.Matrix(
        [
            1,
            mean_value,
            b2 + epsilon,
            b3 - epsilon,
            b4 + epsilon,
            0,
        ]
    )
    p_upper = [sp.factor(v) for v in upper_matrix.inv() * upper_rhs]

    lower_objective = sp.factor(
        sum(target[i] * p_lower[i] for i in support)
    )
    upper_objective = sp.factor(
        sum(target[i] * p_upper[i] for i in support)
    )

    epsilon_star = sp.Rational(437325, 2210299904)

    def eval_vector(vector: list[sp.Expr], at: sp.Rational) -> list[sp.Rational]:
        return [sp.factor(item.subs(epsilon, at)) for item in vector]

    lower_at_zero = eval_vector(p_lower, sp.Rational(0))
    lower_at_star = eval_vector(p_lower, epsilon_star)
    upper_at_zero = eval_vector(p_upper, sp.Rational(0))
    upper_at_star = eval_vector(p_upper, epsilon_star)

    # Exact constraint verification.
    def dot(row: list[sp.Rational], weights: list[sp.Expr]) -> sp.Expr:
        return sp.factor(sum(row[i] * weights[i] for i in support))

    lower_constraints = {
        "normalization": dot(one, p_lower),
        "mean": dot(mean_row, p_lower),
        "L_2log2": dot(r2, p_lower),
        "L_3log2": dot(r3, p_lower),
        "L_4log2": dot(r4, p_lower),
    }
    upper_constraints = {
        "normalization": dot(one, p_upper),
        "mean": dot(mean_row, p_upper),
        "L_2log2": dot(r2, p_upper),
        "L_3log2": dot(r3, p_upper),
        "L_4log2": dot(r4, p_upper),
    }

    selected_eps = [
        sp.Rational(0),
        sp.Rational(1, 10**6),
        sp.Rational(1, 10**5),
        sp.Rational(1, 10**4),
    ]
    table = []
    for eps in selected_eps:
        lmin = sp.N(lower_formula.subs(epsilon, eps), 70)
        lmax = sp.N(upper_formula.subs(epsilon, eps), 70)
        lmin_mp = mp.mpf(str(lmin))
        lmax_mp = mp.mpf(str(lmax))
        q_lower = -mp.log(lmax_mp, 2)
        q_upper = -mp.log(lmin_mp, 2)
        future_lower = mp.mpf("1.25") + mp.mpf("0.5") * q_lower
        future_upper = mp.mpf("1.25") + mp.mpf("0.5") * q_upper
        table.append(
            {
                "epsilon": str(eps),
                "sharp_L_lower": str(sp.factor(lower_formula.subs(epsilon, eps))),
                "sharp_L_upper": str(sp.factor(upper_formula.subs(epsilon, eps))),
                "sharp_future_lower": mp.nstr(future_lower, 40),
                "sharp_future_upper": mp.nstr(future_upper, 40),
                "sharp_future_width": mp.nstr(
                    future_upper - future_lower, 40
                ),
            }
        )

    gates = {
        "lower_envelope_is_below_target_on_declared_support": all(
            residual >= 0 for residual in lower_residual
        ),
        "lower_envelope_has_exact_positive_slack_only_at_x3": (
            lower_residual
            == [
                0,
                0,
                0,
                sp.Rational(21, 3952),
                0,
                0,
            ]
        ),
        "upper_envelope_is_above_target_on_declared_support": all(
            residual <= 0 for residual in upper_residual
        ),
        "upper_envelope_has_exact_negative_slack_only_at_x4": (
            upper_residual
            == [
                0,
                0,
                0,
                0,
                -sp.Rational(7, 1664),
                0,
            ]
        ),
        "lower_penalty_exact": lower_penalty == sp.Rational(366188, 25935),
        "upper_penalty_exact": upper_penalty == sp.Rational(233188, 20475),
        "primal_lower_equals_dual_formula_symbolically": (
            sp.simplify(lower_objective - lower_formula) == 0
        ),
        "primal_upper_equals_dual_formula_symbolically": (
            sp.simplify(upper_objective - upper_formula) == 0
        ),
        "lower_primal_constraints_exact": (
            sp.simplify(lower_constraints["normalization"] - 1) == 0
            and sp.simplify(lower_constraints["mean"] - mean_value) == 0
            and sp.simplify(lower_constraints["L_2log2"] - (b2 - epsilon)) == 0
            and sp.simplify(lower_constraints["L_3log2"] - (b3 + epsilon)) == 0
            and sp.simplify(lower_constraints["L_4log2"] - (b4 - epsilon)) == 0
        ),
        "upper_primal_constraints_exact": (
            sp.simplify(upper_constraints["normalization"] - 1) == 0
            and sp.simplify(upper_constraints["mean"] - mean_value) == 0
            and sp.simplify(upper_constraints["L_2log2"] - (b2 + epsilon)) == 0
            and sp.simplify(upper_constraints["L_3log2"] - (b3 - epsilon)) == 0
            and sp.simplify(upper_constraints["L_4log2"] - (b4 + epsilon)) == 0
        ),
        "lower_weights_nonnegative_on_certified_interval": (
            all(v >= 0 for v in lower_at_zero)
            and all(v >= 0 for v in lower_at_star)
        ),
        "upper_weights_nonnegative_on_certified_interval": (
            all(v >= 0 for v in upper_at_zero)
            and all(v >= 0 for v in upper_at_star)
        ),
        "breakpoint_is_lower_p5_zero": (
            sp.factor(p_lower[5].subs(epsilon, epsilon_star)) == 0
        ),
        "width_decomposition_exact": (
            sp.simplify(
                width_formula
                - sp.Rational(301, 189696)
                - sp.Rational(9923392, 389025) * epsilon
            ) == 0
        ),
    }

    return {
        "support": support,
        "mean_exact": str(mean_value),
        "observed_centers": {
            "L_2log2": str(b2),
            "L_3log2": str(b3),
            "L_4log2": str(b4),
        },
        "target": "L_log2",
        "epsilon_star": {
            "exact": str(epsilon_star),
            "decimal": mp.nstr(
                mp.mpf(epsilon_star.p) / mp.mpf(epsilon_star.q), 40
            ),
        },
        "dual_certificates": {
            "lower_coefficients": [str(v) for v in lower_dual],
            "lower_target_minus_envelope": [str(v) for v in lower_residual],
            "upper_coefficients": [str(v) for v in upper_dual],
            "upper_target_minus_envelope": [str(v) for v in upper_residual],
        },
        "sharp_formulas": {
            "L_lower": str(lower_formula),
            "L_upper": str(upper_formula),
            "L_width": str(width_formula),
            "structural_width": str(sp.Rational(301, 189696)),
            "observational_width_slope": str(
                sp.Rational(9923392, 389025)
            ),
        },
        "primal_extremizers": {
            "lower_weights": [str(v) for v in p_lower],
            "upper_weights": [str(v) for v in p_upper],
        },
        "table": table,
        "gates": gates,
    }


def main() -> None:
    continuous = continuous_support_reuse()
    finite = exact_finite_support_layer()

    all_gates = {
        **{
            f"continuous::{key}": value
            for key, value in continuous["gates"].items()
        },
        **{
            f"finite::{key}": value
            for key, value in finite["gates"].items()
        },
    }

    verdict = (
        "PASS_ROBUST_DUAL_STABILITY_WITH_EXACT_STRUCTURAL_NOISE_DECOMPOSITION"
        if all(all_gates.values())
        else "FAIL_A41_AUDIT"
    )

    result = {
        "audit": "A41_PROVISIONAL_ROBUST_INTERVAL_DATA",
        "general_results_proved_in_note": [
            "compact noisy feasible classes attain sharp continuous-observable extrema",
            "interval widths are monotone in observational tolerances",
            "zero-noise limits converge to the exact finite-grid interval",
            "dual envelopes incur the support-function penalty of the declared error set",
            "finite-grid structural ambiguity is distinct from observational enlargement",
            "no strong inverse stability for the full measure is possible on a nonidentifying finite grid",
        ],
        "continuous_support_A39_reuse": continuous,
        "exact_finite_support_stress_test": finite,
        "gates": all_gates,
        "verdict": verdict,
        "boundary": (
            "The continuous-support noisy bounds reuse certified A39 envelopes and are "
            "rigorous outer bounds, not claimed sharp for positive tolerance. The six-point "
            "support result is sharp only under the explicitly declared finite-support, exact-mean, "
            "common-absolute-tolerance contract and only up to the certified breakpoint. "
            "No physical noise law, support, mark, or contraction is inferred."
        ),
    }

    output_path = HERE / "a41_robust_interval_data_results.json"
    output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

    if not all(all_gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
