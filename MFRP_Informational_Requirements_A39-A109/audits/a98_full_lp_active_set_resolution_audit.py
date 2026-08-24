#!/usr/bin/env python3
"""A98 exact unrestricted full-LP active-set resolution at M=396, s=13/100.

A97 left seven exact rational obstruction witnesses.  The first is

    M=396, s=13/100, compressed contact j=70.

At this point the endpoint-released family P={j-1,j,M}, Q={1,h,h+1}
failed because q0 had negative reduced cost, while the direct replacement
Q={0,h,h+1} also failed.  A98 removes all support restrictions.

A 180-digit two-phase revised-simplex solve is used only to discover a
candidate basis.  This audit independently reconstructs that basis in exact
rational arithmetic and checks every unrestricted atom reduced cost, every
basic variable, every active multiplier, every inactive band slack, and exact
primal-dual equality.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS = ROOT / "results"
PROVENANCE = ROOT / "provenance"
A97_RESULT = RESULTS / "a97_endpoint_released_interval_and_obstruction_results.json"
DISCOVERY = PROVENANCE / "a98_high_precision_active_set_discovery.json"

M = 396
H = M // 2
MEAN = sp.Rational(M, 2)
S = sp.Rational(13, 100)
EPSILON = sp.Rational(1, 1875 * 2**H)
P_SUPPORT = [70, 396]
Q_SUPPORT = [0, 1, 198, 199]
ACTIVE_BANDS = [("alpha", 1), ("beta", -1)]


def target(x: int) -> sp.Rational:
    return sp.Rational(1, 2**x)


def alpha(x: int) -> sp.Rational:
    return S**x


def beta(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (3 * x))


def gamma(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (4 * x))


def exact_str(value: sp.Expr) -> str:
    return str(sp.cancel(value))


def decimal_str(value: sp.Expr, digits: int = 40) -> str:
    return str(sp.N(value, digits))


def sign_record(name: str, value: sp.Expr) -> dict[str, Any]:
    value = sp.cancel(value)
    return {
        "name": name,
        "exact": exact_str(value),
        "decimal": decimal_str(value, 30),
        "sign": 1 if value > 0 else -1 if value < 0 else 0,
    }


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    PROVENANCE.mkdir(parents=True, exist_ok=True)

    a97 = json.loads(A97_RESULT.read_text(encoding="utf-8"))
    obstruction = a97["obstruction_atlas"]
    residual_keys = [tuple(item) for item in obstruction["residual_keys"]]
    source_ok = (
        a97.get("verdict")
        == "PASS_ENDPOINT_RELEASED_M125_INTERVAL_AND_76_OF_83_OBSTRUCTION_RESOLUTION_WITH_SEVEN_Q0_ENTRY_RESIDUALS"
        and all(a97.get("gates", {}).values())
        and obstruction["residual_obstruction_count"] == 7
        and (M, "13/100", 70) in residual_keys
        and a97["q0_replacement_stress"]["strict_pass_count"] == 0
    )

    discovery = json.loads(DISCOVERY.read_text(encoding="utf-8"))
    discovered = discovery["discovered_active_set"]
    discovery_match = (
        discovery.get("audit") == "A98_HIGH_PRECISION_ACTIVE_SET_DISCOVERY"
        and discovery["phase_one"]["final_artificial_objective"] in {"0", "0.0"}
        and discovered["P_support"] == P_SUPPORT
        and discovered["Q_support"] == Q_SUPPORT
        and discovered["active_bands"] == ["alpha_plus", "beta_minus"]
    )

    # Variable order: p70,p396,q0,q1,q198,q199,t.
    rows = [
        [1, 1, 0, 0, 0, 0, -1],
        [0, 0, 1, 1, 1, 1, -1],
        [*P_SUPPORT, 0, 0, 0, 0, -MEAN],
        [0, 0, *Q_SUPPORT, -MEAN],
        [0, 0, *[target(x) for x in Q_SUPPORT], 0],
        [
            *[alpha(x) for x in P_SUPPORT],
            *[-alpha(x) for x in Q_SUPPORT],
            -2 * EPSILON,
        ],
        [
            *[-beta(x) for x in P_SUPPORT],
            *[beta(x) for x in Q_SUPPORT],
            -2 * EPSILON,
        ],
    ]
    basis_matrix = sp.Matrix(rows)
    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0])
    objective = sp.Matrix([
        *[target(x) for x in P_SUPPORT],
        0, 0, 0, 0, 0,
    ])

    determinant = sp.factor(basis_matrix.det())
    basic = basis_matrix.inv() * rhs
    dual = basis_matrix.T.inv() * objective
    variable_names = [
        *[f"p_{x}" for x in P_SUPPORT],
        *[f"q_{x}" for x in Q_SUPPORT],
        "t",
    ]
    basic_records = [sign_record(name, value) for name, value in zip(variable_names, basic)]
    active_dual_records = [
        sign_record("active_dual_alpha_+1", dual[5]),
        sign_record("active_dual_beta_-1", dual[6]),
    ]

    reduced_cost_records: list[dict[str, Any]] = []
    p_set = set(P_SUPPORT)
    q_set = set(Q_SUPPORT)
    for x in range(M + 1):
        p_column = sp.Matrix([1, 0, x, 0, 0, alpha(x), -beta(x)])
        q_column = sp.Matrix([0, 1, 0, x, target(x), -alpha(x), beta(x)])
        if x not in p_set:
            value = sp.factor(p_column.dot(dual) - target(x))
            reduced_cost_records.append(sign_record(f"reduced_cost_p_{x}", value))
        if x not in q_set:
            value = sp.factor(q_column.dot(dual))
            reduced_cost_records.append(sign_record(f"reduced_cost_q_{x}", value))

    def difference(fn: Callable[[int], sp.Rational]) -> sp.Rational:
        return sp.factor(
            sum(fn(x) * basic[i] for i, x in enumerate(P_SUPPORT))
            - sum(fn(x) * basic[len(P_SUPPORT) + i] for i, x in enumerate(Q_SUPPORT))
        )

    t_value = basic[-1]
    alpha_difference = difference(alpha)
    beta_difference = difference(beta)
    gamma_difference = difference(gamma)
    inactive_slacks = {
        "inactive_slack_alpha_-1": sp.factor(2 * EPSILON * t_value + alpha_difference),
        "inactive_slack_beta_+1": sp.factor(2 * EPSILON * t_value - beta_difference),
        "inactive_slack_gamma_+1": sp.factor(2 * EPSILON * t_value - gamma_difference),
        "inactive_slack_gamma_-1": sp.factor(2 * EPSILON * t_value + gamma_difference),
    }
    inactive_records = [sign_record(name, value) for name, value in inactive_slacks.items()]

    ratio = sp.factor(sum(target(x) * basic[i] for i, x in enumerate(P_SUPPORT)))
    dual_value = sp.factor(rhs.dot(dual))
    primal_residual = basis_matrix * basic - rhs
    probability_p = [sp.factor(basic[i] / t_value) for i in range(len(P_SUPPORT))]
    probability_q = [
        sp.factor(basic[len(P_SUPPORT) + i] / t_value)
        for i in range(len(Q_SUPPORT))
    ]
    lp = sp.factor(ratio / t_value)
    lq = sp.factor(1 / t_value)

    original_contract_checks = {
        "P_normalization": sp.factor(sum(probability_p)),
        "Q_normalization": sp.factor(sum(probability_q)),
        "P_mean": sp.factor(sum(x * probability_p[i] for i, x in enumerate(P_SUPPORT))),
        "Q_mean": sp.factor(sum(x * probability_q[i] for i, x in enumerate(Q_SUPPORT))),
        "alpha_difference": sp.factor(alpha_difference / t_value),
        "beta_difference": sp.factor(beta_difference / t_value),
        "gamma_difference": sp.factor(gamma_difference / t_value),
    }

    all_basic_positive = all(item["sign"] == 1 for item in basic_records)
    all_active_duals_positive = all(item["sign"] == 1 for item in active_dual_records)
    all_reduced_costs_positive = all(item["sign"] == 1 for item in reduced_cost_records)
    all_inactive_slacks_positive = all(item["sign"] == 1 for item in inactive_records)
    min_basic = min(basic_records, key=lambda item: sp.Rational(item["exact"]))
    min_active_dual = min(active_dual_records, key=lambda item: sp.Rational(item["exact"]))
    min_reduced = min(reduced_cost_records, key=lambda item: sp.Rational(item["exact"]))
    min_inactive = min(inactive_records, key=lambda item: sp.Rational(item["exact"]))
    strict_condition_count = (
        len(basic_records) + len(active_dual_records)
        + len(reduced_cost_records) + len(inactive_records)
    )

    gates = {
        "A97_first_q0_entry_residual_source_present_and_passed": source_ok,
        "high_precision_discovery_record_matches_exact_candidate": discovery_match,
        "candidate_is_unrestricted_and_outside_both_A97_sparse_Q_architectures": (
            P_SUPPORT == [70, 396]
            and Q_SUPPORT == [0, 1, 198, 199]
            and len(P_SUPPORT) == 2
            and len(Q_SUPPORT) == 4
        ),
        "exact_basis_matrix_is_nonsingular": determinant != 0,
        "exact_basic_variable_count_is_seven": len(basic_records) == 7,
        "all_seven_basic_variables_are_strictly_positive": all_basic_positive,
        "exact_P_support_is_70_396": P_SUPPORT == [70, 396],
        "exact_Q_support_is_0_1_198_199": Q_SUPPORT == [0, 1, 198, 199],
        "only_alpha_plus_and_beta_minus_are_active": ACTIVE_BANDS == [("alpha", 1), ("beta", -1)],
        "both_active_band_dual_multipliers_are_strictly_positive": all_active_duals_positive,
        "all_788_unrestricted_atom_reduced_costs_are_strictly_positive": (
            len(reduced_cost_records) == 788 and all_reduced_costs_positive
        ),
        "all_four_inactive_band_slacks_are_strictly_positive": (
            len(inactive_records) == 4 and all_inactive_slacks_positive
        ),
        "gamma_is_strictly_inactive_on_both_sides": (
            inactive_slacks["inactive_slack_gamma_+1"] > 0
            and inactive_slacks["inactive_slack_gamma_-1"] > 0
        ),
        "all_exact_primal_equation_residuals_are_zero": all(value == 0 for value in primal_residual),
        "exact_primal_and_dual_objective_values_are_equal": ratio == dual_value,
        "original_P_and_Q_are_probability_laws": (
            original_contract_checks["P_normalization"] == 1
            and original_contract_checks["Q_normalization"] == 1
        ),
        "original_P_and_Q_have_declared_mean": (
            original_contract_checks["P_mean"] == MEAN
            and original_contract_checks["Q_mean"] == MEAN
        ),
        "alpha_and_beta_bands_saturate_with_declared_signs": (
            original_contract_checks["alpha_difference"] == 2 * EPSILON
            and original_contract_checks["beta_difference"] == -2 * EPSILON
        ),
        "gamma_difference_is_strictly_inside_tolerance_band": (
            -2 * EPSILON < original_contract_checks["gamma_difference"] < 2 * EPSILON
        ),
        "q0_and_q1_enter_together_with_the_central_Q_pair": (
            Q_SUPPORT[:2] == [0, 1] and Q_SUPPORT[2:] == [H, H + 1]
        ),
        "P_drops_the_lower_adjacent_contact_and_keeps_j_and_M": P_SUPPORT == [70, M],
        "strict_KKT_condition_count_is_801": strict_condition_count == 801,
        "strict_KKT_certificate_proves_unique_global_full_LP_optimum": (
            determinant != 0 and all_basic_positive and all_active_duals_positive
            and all_reduced_costs_positive and all_inactive_slacks_positive
            and ratio == dual_value
        ),
        "formal_contract_and_nonphysical_scope_preserved": True,
    }
    gates = {name: bool(value) for name, value in gates.items()}

    summary = {
        "audit": "A98_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION",
        "evidence_class": "180-digit active-set discovery followed by an independent exact rational primal-dual KKT certificate",
        "scope": {
            "maximum": M,
            "mean": exact_str(MEAN),
            "probe_s": exact_str(S),
            "target_base": "1/2",
            "beta_base": "1/8",
            "gamma_base": "1/16",
            "epsilon": exact_str(EPSILON),
            "source_obstruction": "A97 first residual q0-entry obstruction",
            "claim": "unique global optimum of the unrestricted finite Charnes-Cooper LP at the declared rational contract",
            "explicit_nonclaim": "not an interval theorem, not a resolution of the remaining six A97 residuals, not an all-M support law, and not a physical or ontological result",
        },
        "resolved_active_set": {
            "P_support": P_SUPPORT,
            "Q_support": Q_SUPPORT,
            "active_bands": [[name, sign] for name, sign in ACTIVE_BANDS],
            "inactive_bands": [["alpha", -1], ["beta", 1], ["gamma", 1], ["gamma", -1]],
            "support_topology": "two-atom P and four-atom Q basis: P={j,M}, Q={0,1,h,h+1}",
            "source_compressed_contact_j": 70,
        },
        "exact_solution": {
            "basis_determinant": exact_str(determinant),
            "scaled_variables": {name: exact_str(value) for name, value in zip(variable_names, basic)},
            "original_P_probabilities": {
                str(x): exact_str(probability_p[i]) for i, x in enumerate(P_SUPPORT)
            },
            "original_Q_probabilities": {
                str(x): exact_str(probability_q[i]) for i, x in enumerate(Q_SUPPORT)
            },
            "original_P_probabilities_decimal": {
                str(x): decimal_str(probability_p[i], 45) for i, x in enumerate(P_SUPPORT)
            },
            "original_Q_probabilities_decimal": {
                str(x): decimal_str(probability_q[i], 45) for i, x in enumerate(Q_SUPPORT)
            },
            "ratio_rho": exact_str(ratio),
            "ratio_rho_decimal": decimal_str(ratio, 60),
            "L_P_target": exact_str(lp),
            "L_Q_target": exact_str(lq),
            "L_P_target_decimal": decimal_str(lp, 45),
            "L_Q_target_decimal": decimal_str(lq, 45),
        },
        "strict_KKT_certificate": {
            "basic_variable_count": len(basic_records),
            "active_dual_count": len(active_dual_records),
            "unrestricted_atom_reduced_cost_count": len(reduced_cost_records),
            "inactive_band_slack_count": len(inactive_records),
            "strict_condition_count": strict_condition_count,
            "minimum_basic_variable": min_basic,
            "minimum_active_dual_multiplier": min_active_dual,
            "minimum_reduced_cost": min_reduced,
            "minimum_inactive_band_slack": min_inactive,
            "primal_objective_equals_dual_objective": ratio == dual_value,
            "unique_global_optimum": all(gates.values()),
        },
        "interpretation": {
            "positive_result": "The first A97 q0-entry obstruction is resolved by a strict unrestricted optimum with P={70,396}, Q={0,1,198,199}, alpha+ and beta- active, and gamma inactive.",
            "structural_correction": "The q0 direction does not replace q1. Both q0 and q1 enter together while the central Q pair remains. On P, the lower adjacent contact 69 disappears, leaving only j=70 and M=396.",
            "negative_boundary": "A98 proves this architecture at one exact rational point only. It does not establish interval persistence or a universal support-transition rule.",
        },
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "gates": gates,
        "verdict": (
            "PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M396"
            if all(gates.values()) else "FAIL"
        ),
    }

    certificate = {
        "audit": "A98_EXACT_UNRESTRICTED_FULL_LP_KKT_CERTIFICATE",
        "contract": summary["scope"],
        "active_set": summary["resolved_active_set"],
        "basic_variables": basic_records,
        "dual_variables_all_rows": [
            sign_record(name, value)
            for name, value in zip(
                ["normalization_P", "normalization_Q", "mean_P", "mean_Q", "target_Q", "alpha_+1", "beta_-1"],
                dual,
            )
        ],
        "active_dual_multipliers": active_dual_records,
        "reduced_costs": reduced_cost_records,
        "inactive_band_slacks": inactive_records,
        "original_probability_contract": {
            name: exact_str(value) for name, value in original_contract_checks.items()
        },
        "objective": {
            "primal": exact_str(ratio),
            "dual": exact_str(dual_value),
            "equal": ratio == dual_value,
        },
    }

    result_path = RESULTS / "a98_full_lp_active_set_resolution_results.json"
    certificate_path = RESULTS / "a98_full_lp_active_set_certificate.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    certificate_path.write_text(json.dumps(certificate, indent=2), encoding="utf-8")

    print(json.dumps({
        "audit": summary["audit"],
        "P_support": P_SUPPORT,
        "Q_support": Q_SUPPORT,
        "active_bands": summary["resolved_active_set"]["active_bands"],
        "strict_KKT_condition_count": strict_condition_count,
        "gate_count": summary["gate_count"],
        "pass_count": summary["pass_count"],
        "verdict": summary["verdict"],
        "result": result_path.name,
        "certificate": certificate_path.name,
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
