#!/usr/bin/env python3
"""A64: scale-normalized noise and boundary-pair stress atlas.

Exact theorem:
- sharp lower bound for L_mu from discrete convexity;
- dimensionless error epsilon = delta * ell_mu;
- direct-target ratio bound rho <= 1 + 2 delta.

Computational atlas:
- 240 contracts;
- 84 three-anchor designs per contract;
- all 20,160 designs ranked with HiGHS interior point;
- top candidates cross-checked with dual simplex;
- one exact rational tie certifies that boundary-pair uniqueness is false.

The atlas supports existence of a boundary-pair optimizer on the declared
integer catalogue. It is not a continuous-anchor theorem.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import a64_scale_normalized_boundary_pair_exact_helpers as helpers  # noqa: E402

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
TIE_TOLERANCE = 2e-9
CROSSCHECK_TOLERANCE = 1e-7


def solve_primal(
    maximum: int,
    mean: sp.Rational,
    target: int,
    epsilon: sp.Rational,
    design: tuple[int, int, int],
    method: str,
) -> float:
    objective, a_eq, b_eq, a_ub, b_ub = helpers.build_scaled_numeric_problem(
        maximum,
        mean,
        target,
        epsilon,
        design,
    )
    dimension = len(objective)
    result = linprog(
        -objective,
        A_ub=(a_ub if len(a_ub) else None),
        b_ub=(b_ub if len(b_ub) else None),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(0.0, 1.0)] * dimension,
        method=method,
        options={
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
            "ipm_optimality_tolerance": 1e-10,
        },
    )
    if not result.success:
        raise RuntimeError(
            f"{method} failed: M={maximum}, mean={mean}, target={target}, "
            f"epsilon={epsilon}, design={design}: {result.message}"
        )
    return float(-result.fun)


def main() -> None:
    lower_certificates = []
    lower_gates = []

    contracts = []
    design_solve_count = 0
    crosscheck_count = 0
    max_crosscheck_gap = 0.0

    for maximum in SUPPORT_MAXIMA:
        for fraction in MEAN_FRACTIONS:
            mean = sp.factor(maximum * fraction)

            for target in TARGET_EXPONENTS:
                certificate = helpers.lower_bound_certificate(
                    maximum,
                    mean,
                    target,
                )
                lower_certificates.append(
                    {
                        "maximum": maximum,
                        "mean_fraction": str(fraction),
                        "mean": str(mean),
                        "target_exponent": target,
                        **certificate,
                    }
                )
                lower_gates.extend(
                    [
                        certificate["all_residuals_nonnegative"],
                        certificate["affine_at_mean_equals_candidate"],
                    ]
                )

                ell = helpers.sharp_lower_bound(
                    maximum,
                    mean,
                    target,
                )
                catalogue = list(
                    range(target + 1, target + 1 + CATALOGUE_WIDTH)
                )
                designs = list(itertools.combinations(catalogue, 3))

                for delta in DELTA_LEVELS:
                    epsilon = sp.factor(delta * ell)
                    ranked = []

                    for design in designs:
                        value = solve_primal(
                            maximum,
                            mean,
                            target,
                            epsilon,
                            design,
                            "highs-ipm",
                        )
                        ranked.append((value, design))
                        design_solve_count += 1

                    ranked.sort()
                    minimum = ranked[0][0]

                    near = [
                        item
                        for item in ranked
                        if item[0] - minimum <= CROSSCHECK_TOLERANCE
                    ]

                    boundary_pair_candidates = [
                        item
                        for item in ranked
                        if item[1][0] == target + 1
                        and item[1][1] == target + 2
                    ]
                    best_boundary = min(boundary_pair_candidates)

                    crosscheck_set = {
                        ranked[0][1],
                        ranked[1][1],
                        best_boundary[1],
                        *[item[1] for item in near],
                    }

                    checked = {}
                    for design in sorted(crosscheck_set):
                        second = solve_primal(
                            maximum,
                            mean,
                            target,
                            epsilon,
                            design,
                            "highs-ds",
                        )
                        first = next(
                            value
                            for value, candidate
                            in ranked
                            if candidate == design
                        )
                        gap = abs(first - second)
                        max_crosscheck_gap = max(
                            max_crosscheck_gap,
                            gap,
                        )
                        crosscheck_count += 1
                        checked["-".join(map(str, design))] = {
                            "ipm": first,
                            "dual_simplex": second,
                            "gap": gap,
                        }

                    optimizer_designs = [
                        design
                        for value, design in ranked
                        if value - minimum <= TIE_TOLERANCE
                    ]

                    boundary_pair_exists = any(
                        design[0] == target + 1
                        and design[1] == target + 2
                        for design in optimizer_designs
                    )
                    all_first_boundary = all(
                        design[0] == target + 1
                        for design in optimizer_designs
                    )
                    all_have_pair = all(
                        design[0] == target + 1
                        and design[1] == target + 2
                        for design in optimizer_designs
                    )

                    contracts.append(
                        {
                            "maximum": maximum,
                            "mean_fraction": str(fraction),
                            "mean": str(mean),
                            "target_exponent": target,
                            "delta": str(delta),
                            "target_lower_bound": str(ell),
                            "epsilon_absolute": str(epsilon),
                            "winner": list(ranked[0][1]),
                            "winner_ratio": ranked[0][0],
                            "runner_up": list(ranked[1][1]),
                            "runner_ratio": ranked[1][0],
                            "optimizer_count": len(optimizer_designs),
                            "optimizer_designs": [
                                list(design)
                                for design in optimizer_designs
                            ],
                            "all_optimizers_first_boundary": bool(
                                all_first_boundary
                            ),
                            "boundary_pair_optimizer_exists": bool(
                                boundary_pair_exists
                            ),
                            "all_optimizers_have_boundary_pair": bool(
                                all_have_pair
                            ),
                            "crosschecks": checked,
                            "direct_target_ratio_upper_bound": str(
                                sp.factor(1 + 2 * delta)
                            ),
                            "direct_target_risk_upper_bound_decimal": str(
                                sp.N(
                                    sp.log(1 + 2 * delta)
                                    / (2 * sp.log(2)),
                                    40,
                                )
                            ),
                        }
                    )

    exact_tie_contract = {
        "maximum": 5,
        "mean": sp.Rational(5, 4),
        "target": 3,
        "delta": sp.Rational(1, 1875),
    }
    exact_tie_contract["epsilon"] = sp.factor(
        exact_tie_contract["delta"]
        * helpers.sharp_lower_bound(
            exact_tie_contract["maximum"],
            exact_tie_contract["mean"],
            exact_tie_contract["target"],
        )
    )

    tie_designs = [
        (4, 5, 7),
        (4, 7, 12),
    ]
    exact_tie_values = {}

    for design in tie_designs:
        primal = helpers.exact_primal_value(
            exact_tie_contract["maximum"],
            exact_tie_contract["mean"],
            exact_tie_contract["target"],
            exact_tie_contract["epsilon"],
            design,
        )
        dual = helpers.exact_dual_value(
            exact_tie_contract["maximum"],
            exact_tie_contract["mean"],
            exact_tie_contract["target"],
            exact_tie_contract["epsilon"],
            design,
        )
        exact_tie_values[
            "-".join(map(str, design))
        ] = {
            "primal": str(primal),
            "dual": str(dual),
            "primal_dual_equal": bool(primal == dual),
        }

    exact_tie_ratio_set = {
        value["primal"]
        for value in exact_tie_values.values()
    }
    exact_tie_pass = (
        len(exact_tie_ratio_set) == 1
        and all(
            value["primal_dual_equal"]
            for value in exact_tie_values.values()
        )
    )

    all_first_count = sum(
        item["all_optimizers_first_boundary"]
        for item in contracts
    )
    pair_exists_count = sum(
        item["boundary_pair_optimizer_exists"]
        for item in contracts
    )
    all_pair_count = sum(
        item["all_optimizers_have_boundary_pair"]
        for item in contracts
    )
    nonunique_count = sum(
        item["optimizer_count"] > 1
        for item in contracts
    )

    alignment = {}
    for delta in DELTA_LEVELS:
        groups = {}
        for item in contracts:
            if item["delta"] != str(delta):
                continue
            key = (
                item["maximum"],
                item["mean_fraction"],
            )
            groups.setdefault(key, []).append(item)

        aligned = 0
        for group in groups.values():
            offsets = {
                item["winner"][2]
                - item["target_exponent"]
                for item in group
            }
            aligned += int(len(offsets) == 1)

        alignment[str(delta)] = {
            "aligned": aligned,
            "total": len(groups),
            "fraction": aligned / len(groups),
        }

    fixed_absolute_alignment = None
    normalized_alignment = None

    if A63_RESULTS.exists():
        a63 = json.loads(
            A63_RESULTS.read_text(encoding="utf-8")
        )
        fixed_groups = {}
        for item in a63["contracts"]:
            if (
                item["epsilon"] == "1/10000"
                and item["target_exponent"] in [1, 2]
            ):
                key = (
                    item["maximum"],
                    item["mean_mode"],
                )
                fixed_groups.setdefault(key, []).append(item)

        fixed_aligned = sum(
            len(
                {
                    item["winner"][2]
                    - item["target_exponent"]
                    for item in group
                }
            )
            == 1
            for group in fixed_groups.values()
        )
        fixed_absolute_alignment = {
            "aligned": fixed_aligned,
            "total": len(fixed_groups),
        }

        normalized_groups = {}
        for item in contracts:
            if (
                item["maximum"] in [5, 6, 7, 8]
                and item["mean_fraction"] in ["2/5", "1/2"]
                and item["target_exponent"] in [1, 2]
                and item["delta"] == "1/1875"
            ):
                key = (
                    item["maximum"],
                    item["mean_fraction"],
                )
                normalized_groups.setdefault(key, []).append(item)

        normalized_aligned_count = sum(
            len(
                {
                    item["winner"][2]
                    - item["target_exponent"]
                    for item in group
                }
            )
            == 1
            for group in normalized_groups.values()
        )
        normalized_alignment = {
            "aligned": normalized_aligned_count,
            "total": len(normalized_groups),
        }

    expected_designs = (
        len(SUPPORT_MAXIMA)
        * len(MEAN_FRACTIONS)
        * len(TARGET_EXPONENTS)
        * len(DELTA_LEVELS)
        * math.comb(CATALOGUE_WIDTH, 3)
    )

    gates = {
        "all_sharp_lower_bound_certificates_pass": bool(
            all(lower_gates)
        ),
        "all_20160_designs_solved": bool(
            design_solve_count == expected_designs
        ),
        "top_candidates_crosschecked": bool(
            crosscheck_count >= 2 * len(contracts)
        ),
        "maximum_crosscheck_gap_below_1e_minus_7": bool(
            max_crosscheck_gap < 1e-7
        ),
        "every_optimizer_uses_first_boundary_anchor": bool(
            all_first_count == len(contracts)
        ),
        "boundary_pair_optimizer_exists_everywhere": bool(
            pair_exists_count == len(contracts)
        ),
        "exact_nonunique_counterexample_certified": bool(
            exact_tie_pass
        ),
        "strong_uniqueness_claim_rejected": bool(
            all_pair_count < len(contracts)
            and nonunique_count > 0
        ),
        "exact_data_translation_alignment_complete": bool(
            alignment["0"]["aligned"]
            == alignment["0"]["total"]
        ),
        "normalization_improves_A63_alignment": bool(
            fixed_absolute_alignment is not None
            and normalized_alignment is not None
            and (
                normalized_alignment["aligned"]
                / normalized_alignment["total"]
                >
                fixed_absolute_alignment["aligned"]
                / fixed_absolute_alignment["total"]
            )
        ),
    }

    verdict = (
        "PASS_SCALE_NORMALIZED_NOISE_AND_BOUNDARY_PAIR_STRESS_ATLAS"
        if all(gates.values())
        else "FAIL_A64_SCALE_NORMALIZED_BOUNDARY_AUDIT"
    )

    result = {
        "audit": "A64_SCALE_NORMALIZED_NOISE_AND_BOUNDARY_PAIR",
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
            "catalogue": "{mu+1,...,mu+9}",
            "budget": 3,
            "contract_count": len(contracts),
            "design_count": design_solve_count,
            "crosscheck_count": crosscheck_count,
        },
        "sharp_scale_theorem": {
            "lower_bound": (
                "ell_mu(M,m) is the affine interpolation of "
                "2^(-mu x) between floor(m) and ceil(m)"
            ),
            "noise_contract": "epsilon=delta*ell_mu(M,m)",
            "direct_target_ratio_bound": "rho<=1+2*delta",
            "direct_target_risk_bound": (
                "R_Q<=0.5*log2(1+2*delta)"
            ),
            "certificates": lower_certificates,
        },
        "atlas_summary": {
            "all_first_boundary_count": all_first_count,
            "boundary_pair_exists_count": pair_exists_count,
            "all_optimizers_have_pair_count": all_pair_count,
            "nonunique_contract_count": nonunique_count,
            "maximum_crosscheck_gap": max_crosscheck_gap,
            "translation_alignment_by_delta": alignment,
            "fixed_absolute_alignment_A63": fixed_absolute_alignment,
            "normalized_alignment_A63_grid": normalized_alignment,
            "correct_statement": (
                "Every optimal set in the declared atlas uses mu+1. "
                "Every contract admits at least one optimizer containing "
                "{mu+1,mu+2}. Exact ties show that mu+2 is not necessary "
                "in every optimizer."
            ),
        },
        "exact_tie_counterexample": {
            "maximum": 5,
            "mean": "5/4",
            "target_exponent": 3,
            "delta": "1/1875",
            "epsilon": str(exact_tie_contract["epsilon"]),
            "values": exact_tie_values,
            "interpretation": (
                "{4,5,7} and {4,7,12} have exactly the same minimax "
                "ratio. The boundary-pair design is optimal, but not unique."
            ),
        },
        "contracts": contracts,
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The scale-normalization statements are exact. The boundary "
            "conclusion is an exhaustive finite integer-catalogue stress "
            "test, not yet a continuous-anchor existence theorem."
        ),
    }

    output = HERE / "a64_scale_normalized_boundary_pair_results.json"
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "audit": result["audit"],
                "gate_count": len(gates),
                "pass_count": sum(gates.values()),
                "contract_count": len(contracts),
                "design_count": design_solve_count,
                "first_boundary": (
                    f"{all_first_count}/{len(contracts)}"
                ),
                "boundary_pair_exists": (
                    f"{pair_exists_count}/{len(contracts)}"
                ),
                "all_optimizers_have_pair": (
                    f"{all_pair_count}/{len(contracts)}"
                ),
                "nonunique_contracts": nonunique_count,
                "maximum_crosscheck_gap": max_crosscheck_gap,
                "failed_gates": [
                    name
                    for name, value in gates.items()
                    if not value
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
