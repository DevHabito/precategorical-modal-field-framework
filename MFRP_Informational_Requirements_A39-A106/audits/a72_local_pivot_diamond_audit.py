#!/usr/bin/env python3
"""A72 exact audit: local pivot diamond and orientation-selected path.

Scope
-----
Central-mean contracts with target exponent 1, relative error delta=1/1875,
and fixed completion {alpha,3,4}, for M=10,11,12.

The M=10 theorem is inherited from A71. M=11 and M=12 are independently
audited over exact algebraic phases. Their complete integer catalogues
{2,...,10} choose 3 are ranked exactly over the rationals.

All three supports share the same first four phase signatures after writing

    h = floor(M/2).

The common terminal start and end signatures are

    S: P={0,3,4,M}, Q={1,h,h+1}, alpha+, beta-, gamma+
    T: P={0,3,M},   Q={1,h,h+1}, alpha+, gamma-

but two different exact intermediate routes occur:

    Route A (M=10,11):
      A: P={0,3,M}, Q={1,h,h+1}, alpha+, beta-

    Route B (M=12):
      B: P={0,3,4,M}, Q={1,h,h+1}, alpha+, beta-, gamma-

The cross-route candidates are excluded exactly on the competing
intermediate intervals:

- At M=11, Route B has lambda_gamma^- < 0 throughout the exact phase-5
  interval, hence is dual-infeasible.
- At M=12, Route A has a negative reduced cost for the missing P-state x=4
  throughout the exact phase-5 interval, hence is dual-infeasible.

This proves an exact local orientation-selection mechanism. It does not
enumerate every possible active basis, nor prove an arbitrary-M pivot law.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import multiprocessing as mp
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent

A64_HELPER = HERE / "a64_scale_normalized_boundary_pair_exact_helpers.py"
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"
A71_RESULTS = HERE / "a71_orientation_bifurcation_results.json"
CATALOGUE_FILES = {
    11: HERE / "a72_exact_catalogue_M11.json",
    12: HERE / "a72_exact_catalogue_M12.json",
}
PHASE_FILES = {
    11: HERE / "a72_exact_phases_M11.json",
    12: HERE / "a72_exact_phases_M12.json",
}


M11_SPEC = {
    "mean": sp.Rational(11, 2),
    "epsilon": sp.Rational(1, 80000),
    "gamma": 4,
    "phase_specs": [
        (
            (1, 4, 11, 12, 14, 17, 18, 24),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 1, 4, 11, 14, 17, 18, 24),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 4, 11, 13, 14, 17, 18, 24),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 3, 4, 11, 13, 17, 18, 24),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 3, 11, 13, 17, 18, 24),
            (("alpha", 1), ("beta", -1)),
        ),
        (
            (0, 3, 11, 13, 17, 18, 24),
            (("alpha", 1), ("gamma", -1)),
        ),
    ],
    "approx_alpha": [
        2.6825,
        2.7535,
        2.8255,
        2.9565,
        2.9595,
    ],
}


M12_SPEC = {
    "mean": sp.Rational(6),
    "epsilon": sp.Rational(1, 120000),
    "gamma": 4,
    "phase_specs": [
        (
            (1, 4, 12, 13, 15, 19, 20, 26),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 1, 4, 12, 15, 19, 20, 26),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 4, 12, 14, 15, 19, 20, 26),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 3, 4, 12, 14, 19, 20, 26),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 3, 4, 12, 14, 19, 20, 26),
            (("alpha", 1), ("beta", -1), ("gamma", -1)),
        ),
        (
            (0, 3, 12, 14, 19, 20, 26),
            (("alpha", 1), ("gamma", -1)),
        ),
    ],
    "approx_alpha": [
        2.7925,
        2.8365,
        2.8845,
        2.9605,
        2.9715,
    ],
}


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def normalized_epsilon(maximum: int) -> sp.Rational:
    mean = sp.Rational(maximum, 2)
    lower = int(sp.floor(mean))

    if mean == lower:
        ell = sp.Rational(1, 2 ** lower)
    else:
        ell = (
            sp.Rational(1, 2 ** lower)
            + sp.Rational(1, 2 ** (lower + 1))
        ) / 2

    return sp.factor(ell / 1875)


def exact_catalogue(maximum: int) -> dict[str, Any]:
    """Load the independently generated exact catalogue certificate.

    The companion script a72_exact_catalogue_generator.py recomputes all
    84 rational LP optima for one requested support maximum.
    """
    path = CATALOGUE_FILES[maximum]
    if not path.exists():
        raise FileNotFoundError(
            f"Missing exact catalogue certificate: {path}. "
            "Run a72_exact_catalogue_generator.py first."
        )

    raw = json.loads(path.read_text(encoding="utf-8"))
    top = raw["top"]

    return {
        "maximum": maximum,
        "design_count": raw["count"],
        "winner": top[0]["design"],
        "winner_ratio": top[0]["primal"],
        "runner_up": top[1]["design"],
        "runner_ratio": top[1]["primal"],
        "exact_gap": raw["gap"],
        "top_3": [
            {
                "design": item["design"],
                "primal": item["primal"],
                "dual": item["dual"],
                "primal_dual_equal": item["equal"],
                "risk_decimal": str(
                    sp.N(
                        sp.log(sp.Rational(item["primal"]))
                        / (2 * sp.log(2)),
                        50,
                    )
                ),
            }
            for item in top
        ],
        "certificate_file": path.name,
    }

def phase_signature(
    result: dict[str, Any],
    phase_number: int,
) -> dict[str, Any]:
    maximum = result["maximum"]
    count = maximum + 1
    phase = result["phases"][phase_number - 1]
    indices = phase["positive_indices"]

    return {
        "p_support": [
            index
            for index in indices
            if 0 <= index < count
        ],
        "q_support": [
            index - count
            for index in indices
            if count <= index < 2 * count
        ],
        "active_observations": (
            phase["active_observations"]
        ),
    }


def canonical_signature(
    maximum: int,
    stage: str,
) -> dict[str, Any]:
    h = maximum // 2

    definitions = {
        "phase_1": {
            "p_support": [1, 4, maximum],
            "q_support": [0, 2, h, h + 1],
            "active_observations": [
                ["alpha", 1],
                ["beta", -1],
                ["gamma", 1],
            ],
        },
        "phase_2": {
            "p_support": [0, 1, 4, maximum],
            "q_support": [2, h, h + 1],
            "active_observations": [
                ["alpha", 1],
                ["beta", -1],
                ["gamma", 1],
            ],
        },
        "phase_3": {
            "p_support": [0, 4, maximum],
            "q_support": [1, 2, h, h + 1],
            "active_observations": [
                ["alpha", 1],
                ["beta", -1],
                ["gamma", 1],
            ],
        },
        "S": {
            "p_support": [0, 3, 4, maximum],
            "q_support": [1, h, h + 1],
            "active_observations": [
                ["alpha", 1],
                ["beta", -1],
                ["gamma", 1],
            ],
        },
        "A": {
            "p_support": [0, 3, maximum],
            "q_support": [1, h, h + 1],
            "active_observations": [
                ["alpha", 1],
                ["beta", -1],
            ],
        },
        "B": {
            "p_support": [0, 3, 4, maximum],
            "q_support": [1, h, h + 1],
            "active_observations": [
                ["alpha", 1],
                ["beta", -1],
                ["gamma", -1],
            ],
        },
        "T": {
            "p_support": [0, 3, maximum],
            "q_support": [1, h, h + 1],
            "active_observations": [
                ["alpha", 1],
                ["gamma", -1],
            ],
        },
    }

    return definitions[stage]


def serialized_boundary_to_exact(
    boundary: dict[str, Any],
) -> dict[str, Any]:
    return {
        "kind": boundary["kind"],
        "left": sp.Rational(boundary["left"]),
        "right": sp.Rational(boundary["right"]),
    }


def negative_certificate(
    a67,
    result: dict[str, Any],
    phase_number: int,
    branch: dict[str, Any],
    condition_name: str,
) -> dict[str, Any]:
    phase = result["phases"][phase_number - 1]
    lower = serialized_boundary_to_exact(
        phase["s_lower"]
    )
    upper = serialized_boundary_to_exact(
        phase["s_upper"]
    )

    expression = next(
        expression
        for name, expression in branch["conditions"]
        if name == condition_name
    )
    certificate = a67.certify_positive(
        -expression,
        lower,
        upper,
    )

    return {
        "condition": condition_name,
        "negative_throughout_interval": bool(
            certificate["ok"]
            and certificate["sample_sign"] > 0
        ),
        "certificate": certificate,
        "expression": str(expression),
    }


def pivot_description(
    left: dict[str, Any],
    right: dict[str, Any],
) -> dict[str, Any]:
    left_p = set(left["p_support"])
    right_p = set(right["p_support"])
    left_q = set(left["q_support"])
    right_q = set(right["q_support"])
    left_a = {
        tuple(item)
        for item in left["active_observations"]
    }
    right_a = {
        tuple(item)
        for item in right["active_observations"]
    }

    return {
        "p_enter": sorted(right_p - left_p),
        "p_leave": sorted(left_p - right_p),
        "q_enter": sorted(right_q - left_q),
        "q_leave": sorted(left_q - right_q),
        "bands_activate": [
            list(item)
            for item in sorted(right_a - left_a)
        ],
        "bands_deactivate": [
            list(item)
            for item in sorted(left_a - right_a)
        ],
    }


def main() -> None:
    for path in [
        A64_HELPER,
        A67_SCRIPT,
        A71_RESULTS,
        CATALOGUE_FILES[11],
        CATALOGUE_FILES[12],
        PHASE_FILES[11],
        PHASE_FILES[12],
    ]:
        if not path.exists():
            raise FileNotFoundError(path)

    a67 = load_module(
        A67_SCRIPT,
        "a67_for_a72",
    )
    a71 = json.loads(
        A71_RESULTS.read_text(
            encoding="utf-8"
        )
    )

    m10 = a71[
        "M10_global_theorem"
    ]["exact_phase_result"]
    m11 = json.loads(PHASE_FILES[11].read_text(encoding="utf-8"))
    m12 = json.loads(PHASE_FILES[12].read_text(encoding="utf-8"))

    catalogue_11 = exact_catalogue(11)
    catalogue_12 = exact_catalogue(12)

    results_by_M = {
        10: m10,
        11: m11,
        12: m12,
    }

    common_prefix_checks = []
    terminal_checks = []

    for maximum, result in results_by_M.items():
        for phase_number, stage in [
            (1, "phase_1"),
            (2, "phase_2"),
            (3, "phase_3"),
            (4, "S"),
            (6, "T"),
        ]:
            common_prefix_checks.append(
                phase_signature(
                    result,
                    phase_number,
                )
                == canonical_signature(
                    maximum,
                    stage,
                )
            )

    terminal_checks.extend(
        [
            phase_signature(m10, 5)
            == canonical_signature(10, "A"),
            phase_signature(m11, 5)
            == canonical_signature(11, "A"),
            phase_signature(m12, 5)
            == canonical_signature(12, "B"),
        ]
    )

    cross_B_M11 = a67.build_branch(
        11,
        sp.Rational(11, 2),
        sp.Rational(1, 80000),
        4,
        (
            0,
            3,
            4,
            11,
            13,
            17,
            18,
            24,
        ),
        (
            ("alpha", 1),
            ("beta", -1),
            ("gamma", -1),
        ),
    )
    cross_A_M12 = a67.build_branch(
        12,
        sp.Rational(6),
        sp.Rational(1, 120000),
        4,
        (
            0,
            3,
            12,
            14,
            19,
            20,
            26,
        ),
        (
            ("alpha", 1),
            ("beta", -1),
        ),
    )

    reject_B_M11 = negative_certificate(
        a67,
        m11,
        5,
        cross_B_M11,
        "active_dual_gamma_-1",
    )
    reject_A_M12 = negative_certificate(
        a67,
        m12,
        5,
        cross_A_M12,
        "reduced_cost_4",
    )

    phase_sequences = {}
    pivot_sequences = {}

    for maximum, result in results_by_M.items():
        signatures = [
            phase_signature(
                result,
                phase_number,
            )
            for phase_number in range(
                1,
                result["phase_count"] + 1,
            )
        ]
        phase_sequences[str(maximum)] = signatures
        pivot_sequences[str(maximum)] = [
            pivot_description(
                signatures[index],
                signatures[index + 1],
            )
            for index in range(
                len(signatures) - 1
            )
        ]

    all_alpha_positive = all(
        ["alpha", 1]
        in phase["active_observations"]
        for result in results_by_M.values()
        for phase in result["phases"]
    )
    all_derivatives_positive = all(
        result["gates"][
            "all_phase_derivatives_positive"
        ]
        for result in results_by_M.values()
    )

    catalogues = {
        "11": catalogue_11,
        "12": catalogue_12,
    }

    gates = {
        "A71_M10_theorem_passed": bool(
            all(m10["gates"].values())
        ),
        "M11_exact_global_theorem_passed": bool(
            all(m11["gates"].values())
        ),
        "M12_exact_global_theorem_passed": bool(
            all(m12["gates"].values())
        ),
        "all_168_new_catalogue_designs_ranked_exactly": bool(
            catalogue_11["design_count"] == 84
            and catalogue_12["design_count"] == 84
        ),
        "M11_M12_unique_catalogue_winner_2_3_4": bool(
            catalogue_11["winner"] == [2, 3, 4]
            and catalogue_12["winner"] == [2, 3, 4]
            and sp.Rational(
                catalogue_11["runner_ratio"]
            )
            > sp.Rational(
                catalogue_11["winner_ratio"]
            )
            and sp.Rational(
                catalogue_12["runner_ratio"]
            )
            > sp.Rational(
                catalogue_12["winner_ratio"]
            )
        ),
        "top_catalogue_primal_dual_certificates_match": bool(
            all(
                item["primal_dual_equal"]
                for catalogue in catalogues.values()
                for item in catalogue["top_3"]
            )
        ),
        "common_first_four_and_final_signatures_M10_M12": bool(
            all(common_prefix_checks)
        ),
        "terminal_pivot_order_bifurcation_exact": bool(
            all(terminal_checks)
        ),
        "cross_route_B_rejected_at_M11_by_negative_dual": bool(
            reject_B_M11[
                "negative_throughout_interval"
            ]
        ),
        "cross_route_A_rejected_at_M12_by_negative_reduced_cost": bool(
            reject_A_M12[
                "negative_throughout_interval"
            ]
        ),
        "alpha_positive_band_active_all_18_phases": bool(
            all_alpha_positive
        ),
        "derivative_positive_all_18_phases": bool(
            all_derivatives_positive
        ),
    }

    verdict = (
        "PASS_EXACT_LOCAL_PIVOT_DIAMOND_AND_ORIENTATION_SELECTION"
        if all(gates.values())
        else "FAIL_A72_PIVOT_SELECTION_AUDIT"
    )

    result = {
        "audit": (
            "A72_LOCAL_PIVOT_DIAMOND_AND_ORIENTATION_SELECTION"
        ),
        "contract_family": {
            "support_maxima": [10, 11, 12],
            "support": "{0,...,M}",
            "mean": "M/2",
            "target_exponent": 1,
            "relative_error_delta": "1/1875",
            "fixed_completion": "{alpha,3,4}",
            "alpha_domain": "[2,3)",
        },
        "catalogues": catalogues,
        "global_theorems": {
            "10": m10,
            "11": m11,
            "12": m12,
        },
        "common_signature_grammar": {
            "h": "floor(M/2)",
            "phase_1": (
                "P={1,4,M}, Q={0,2,h,h+1}, "
                "active={alpha+,beta-,gamma+}"
            ),
            "phase_2": (
                "P={0,1,4,M}, Q={2,h,h+1}, "
                "active={alpha+,beta-,gamma+}"
            ),
            "phase_3": (
                "P={0,4,M}, Q={1,2,h,h+1}, "
                "active={alpha+,beta-,gamma+}"
            ),
            "S": (
                "P={0,3,4,M}, Q={1,h,h+1}, "
                "active={alpha+,beta-,gamma+}"
            ),
            "T": (
                "P={0,3,M}, Q={1,h,h+1}, "
                "active={alpha+,gamma-}"
            ),
        },
        "local_pivot_diamond": {
            "start_S": (
                "P={0,3,4,M}, Q={1,h,h+1}, "
                "active={alpha+,beta-,gamma+}"
            ),
            "intermediate_A": (
                "P={0,3,M}, Q={1,h,h+1}, "
                "active={alpha+,beta-}"
            ),
            "intermediate_B": (
                "P={0,3,4,M}, Q={1,h,h+1}, "
                "active={alpha+,beta-,gamma-}"
            ),
            "terminal_T": (
                "P={0,3,M}, Q={1,h,h+1}, "
                "active={alpha+,gamma-}"
            ),
            "observed_paths": {
                "M10": "S -> A -> T",
                "M11": "S -> A -> T",
                "M12": "S -> B -> T",
            },
            "cross_route_exclusions": {
                "M11_B": reject_B_M11,
                "M12_A": reject_A_M12,
            },
            "interpretation": (
                "The terminal pivot order is selected by exact "
                "primal-dual orientation. The alternative intermediate "
                "basis is infeasible throughout the competing exact "
                "phase-5 interval."
            ),
        },
        "phase_sequences": phase_sequences,
        "pivot_sequences": pivot_sequences,
        "formal_results": [
            (
                "M=11 and M=12 each have six exact algebraic phases "
                "and five simple finite transitions"
            ),
            (
                "the exact integer-catalogue winner remains {2,3,4} "
                "for M=11 and M=12"
            ),
            (
                "M=10,11,12 share the same first four and final "
                "normalized contact signatures"
            ),
            (
                "the terminal two-pivot order bifurcates at M=12"
            ),
            (
                "the unused M=11 Route-B intermediate is excluded by "
                "a negative gamma-minus dual multiplier"
            ),
            (
                "the unused M=12 Route-A intermediate is excluded by "
                "a negative reduced cost for the omitted P contact x=4"
            ),
            (
                "the positive alpha band and positive derivative persist "
                "through all 18 exact phases"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A72 proves an exact local selection law for the four "
            "terminal signatures observed at M=10,11,12. It does not "
            "enumerate every active basis, prove an oriented-matroid "
            "elimination axiom, or establish the pivot grammar for "
            "arbitrary support size."
        ),
    }

    output_path = HERE / (
        "a72_local_pivot_diamond_results.json"
    )
    output_path.write_text(
        json.dumps(
            result,
            indent=2,
        ),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "phase_counts": {
            str(maximum): result_M["phase_count"]
            for maximum, result_M
            in results_by_M.items()
        },
        "transition_counts": {
            str(maximum): result_M["transition_count"]
            for maximum, result_M
            in results_by_M.items()
        },
        "catalogue_winners": {
            key: value["winner"]
            for key, value in catalogues.items()
        },
        "observed_paths": result[
            "local_pivot_diamond"
        ]["observed_paths"],
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
