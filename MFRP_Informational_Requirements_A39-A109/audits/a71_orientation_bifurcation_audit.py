#!/usr/bin/env python3
"""A71 exact audit: orientation bifurcation and active-set protection at M=10.

The A70 weakest repeated signature is

    P={0,2,3,M}, Q={1,4,5},
    active bands alpha+, beta-, gamma-,
    gamma=4, mean=M/2.

A71 derives its Cramer numerator symbolically as a function of M,
R=2^{-M}, and epsilon. The orientation is negative at M=8 and M=9 but
positive at M=10. At M=10, the inherited active-basis determinant is
strictly negative on s in [1/8,1/4], so its alpha multiplier would be
strictly negative. The inherited phase is therefore dual-infeasible.

The optimizer changes active set. For the M=10 central-mean contract with
delta=1/1875 and fixed completion {alpha,3,4}, six exact algebraic phases
are certified. Every phase has positive derivative, and alpha=2 is the
unique global first-anchor optimum.

The integer catalogue {2,...,10} choose 3 is also ranked exactly over the
rationals. {2,3,4} is the unique winner.
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
A69_RESULTS = HERE / "a69_cramer_chebyshev_reduction_results.json"
A70_RESULTS = HERE / "a70_signed_q_schur_dominance_results.json"

S = sp.Symbol("s")
M_SYMBOL = sp.Symbol("M")
R_SYMBOL = sp.Symbol("R")
EPS_SYMBOL = sp.Symbol("epsilon")

M10_SPEC = {
    "mean": sp.Rational(5),
    "epsilon": sp.Rational(1, 60000),
    "gamma": 4,
    "phase_specs": [
        (
            (1, 4, 10, 11, 13, 16, 17, 22),
            (
                ("alpha", 1),
                ("beta", -1),
                ("gamma", 1),
            ),
        ),
        (
            (0, 1, 4, 10, 13, 16, 17, 22),
            (
                ("alpha", 1),
                ("beta", -1),
                ("gamma", 1),
            ),
        ),
        (
            (0, 4, 10, 12, 13, 16, 17, 22),
            (
                ("alpha", 1),
                ("beta", -1),
                ("gamma", 1),
            ),
        ),
        (
            (0, 3, 4, 10, 12, 16, 17, 22),
            (
                ("alpha", 1),
                ("beta", -1),
                ("gamma", 1),
            ),
        ),
        (
            (0, 3, 10, 12, 16, 17, 22),
            (
                ("alpha", 1),
                ("beta", -1),
            ),
        ),
        (
            (0, 3, 10, 12, 16, 17, 22),
            (
                ("alpha", 1),
                ("gamma", -1),
            ),
        ),
    ],
    "approx_alpha": [
        2.5624,
        2.6680,
        2.7684,
        2.9438,
        2.9475,
    ],
}


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def exact_catalogue_task(
    design: tuple[int, int, int],
) -> tuple[tuple[int, int, int], str]:
    helper = load_module(
        A64_HELPER,
        f"a64_worker_{design[0]}_{design[1]}_{design[2]}",
    )
    value = helper.exact_primal_value(
        10,
        sp.Rational(5),
        1,
        sp.Rational(1, 60000),
        design,
    )
    return design, str(value)


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

    return sp.factor(
        ell / 1875
    )


def weak_signature_symbolic_numerator() -> sp.Expr:
    """Cramer numerator for the inherited weak A70 signature."""
    p_points = [
        sp.Integer(0),
        sp.Integer(2),
        sp.Integer(3),
        M_SYMBOL,
    ]
    q_points = [
        sp.Integer(1),
        sp.Integer(4),
        sp.Integer(5),
    ]
    dimension = 8
    mean = M_SYMBOL / 2

    rows: list[list[sp.Expr]] = []

    rows.append(
        [1, 1, 1, 1, 0, 0, 0, -1]
    )
    rows.append(
        [0, 0, 0, 0, 1, 1, 1, -1]
    )
    rows.append(
        [
            *p_points,
            0,
            0,
            0,
            -mean,
        ]
    )
    rows.append(
        [
            0,
            0,
            0,
            0,
            *q_points,
            -mean,
        ]
    )

    rows.append(
        [
            0,
            0,
            0,
            0,
            *[
                sp.Rational(1, 2 ** int(x))
                for x in q_points
            ],
            0,
        ]
    )

    # Alpha row replaced by the target objective row.
    rows.append(
        [
            sp.Rational(1),
            sp.Rational(1, 4),
            sp.Rational(1, 8),
            R_SYMBOL,
            0,
            0,
            0,
            0,
        ]
    )

    # beta=3 negative band.
    rows.append(
        [
            -sp.Rational(1),
            -sp.Rational(1, 2 ** 6),
            -sp.Rational(1, 2 ** 9),
            -R_SYMBOL ** 3,
            sp.Rational(1, 2 ** 3),
            sp.Rational(1, 2 ** 12),
            sp.Rational(1, 2 ** 15),
            -2 * EPS_SYMBOL,
        ]
    )

    # gamma=4 negative band.
    rows.append(
        [
            -sp.Rational(1),
            -sp.Rational(1, 2 ** 8),
            -sp.Rational(1, 2 ** 12),
            -R_SYMBOL ** 4,
            sp.Rational(1, 2 ** 4),
            sp.Rational(1, 2 ** 16),
            sp.Rational(1, 2 ** 20),
            -2 * EPS_SYMBOL,
        ]
    )

    return sp.factor(
        sp.Matrix(rows).det()
    )


def weak_numerator_at(
    symbolic_numerator: sp.Expr,
    maximum: int,
) -> sp.Expr:
    return sp.factor(
        symbolic_numerator.subs(
            {
                M_SYMBOL: maximum,
                R_SYMBOL: sp.Rational(
                    1,
                    2 ** maximum,
                ),
                EPS_SYMBOL: normalized_epsilon(
                    maximum
                ),
            }
        )
    )


def inherited_m10_basis(
    a67,
) -> dict[str, Any]:
    maximum = 10
    count = maximum + 1
    positive_indices = (
        0,
        2,
        3,
        10,
        count + 1,
        count + 4,
        count + 5,
        2 * count,
    )
    active = (
        ("alpha", 1),
        ("beta", -1),
        ("gamma", -1),
    )

    branch = a67.build_branch(
        maximum,
        sp.Rational(5),
        sp.Rational(1, 60000),
        4,
        positive_indices,
        active,
    )

    # Reconstruct the active matrix determinant independently.
    support = list(range(maximum + 1))
    dimension = 2 * count + 1
    target = [
        sp.Rational(
            1,
            2 ** x,
        )
        for x in support
    ]

    rows: list[list[sp.Expr]] = []

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[index] = 1
    row[-1] = -1
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[count + index] = 1
    row[-1] = -1
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(support):
        row[index] = x
    row[-1] = -5
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(support):
        row[count + index] = x
    row[-1] = -5
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[count + index] = target[index]
    rows.append(row)

    exponent_map = {
        "alpha": None,
        "beta": 3,
        "gamma": 4,
    }

    for name, sign in active:
        exponent = exponent_map[name]
        values = [
            (
                S ** x
                if exponent is None
                else sp.Rational(
                    1,
                    2 ** (exponent * x),
                )
            )
            for x in support
        ]

        row = [sp.Integer(0)] * dimension
        for index in range(count):
            row[index] = sign * values[index]
            row[count + index] = -sign * values[index]
        row[-1] = -sp.Rational(1, 30000)
        rows.append(row)

    basis = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(8)
        ]
    )
    determinant = sp.factor(
        basis.det()
    )

    determinant_polynomial = sp.Poly(
        sp.fraction(
            sp.cancel(determinant)
        )[0],
        S,
        domain=sp.QQ,
    )

    roots = []
    for (left, right), multiplicity in sp.intervals(
        determinant_polynomial,
        eps=sp.Rational(1, 10 ** 14),
    ):
        if right < sp.Rational(1, 8):
            continue
        if left > sp.Rational(1, 4):
            continue
        roots.append(
            {
                "left": str(left),
                "right": str(right),
                "multiplicity": multiplicity,
            }
        )

    sample = sp.Rational(3, 16)
    determinant_sample = sp.factor(
        determinant.subs(
            S,
            sample,
        )
    )

    alpha_dual = next(
        expression
        for name, expression in branch[
            "conditions"
        ]
        if name == "active_dual_alpha_+1"
    )
    alpha_dual_sample = sp.factor(
        alpha_dual.subs(
            S,
            sample,
        )
    )

    return {
        "positive_indices": list(
            positive_indices
        ),
        "active_observations": [
            list(observation)
            for observation in active
        ],
        "basis_determinant": str(
            determinant
        ),
        "determinant_degree": (
            determinant_polynomial.degree()
        ),
        "determinant_roots_in_domain": roots,
        "determinant_sample": str(
            determinant_sample
        ),
        "determinant_negative_on_domain": bool(
            not roots
            and determinant_sample < 0
        ),
        "alpha_multiplier": str(
            alpha_dual
        ),
        "alpha_multiplier_sample": str(
            alpha_dual_sample
        ),
        "alpha_multiplier_negative_on_domain": bool(
            not roots
            and alpha_dual_sample < 0
        ),
    }


def phase_supports(
    maximum: int,
    phase: dict[str, Any],
) -> dict[str, Any]:
    count = maximum + 1
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
        "scale_basic": bool(
            2 * count in indices
        ),
    }


def main() -> None:
    for path in [
        A64_HELPER,
        A67_SCRIPT,
        A69_RESULTS,
        A70_RESULTS,
    ]:
        if not path.exists():
            raise FileNotFoundError(path)

    a64 = load_module(
        A64_HELPER,
        "a64_for_a71",
    )
    a67 = load_module(
        A67_SCRIPT,
        "a67_for_a71",
    )
    a69 = json.loads(
        A69_RESULTS.read_text(
            encoding="utf-8"
        )
    )
    a70 = json.loads(
        A70_RESULTS.read_text(
            encoding="utf-8"
        )
    )

    designs = list(
        itertools.combinations(
            range(2, 11),
            3,
        )
    )

    process_count = min(
        8,
        max(1, mp.cpu_count()),
    )

    with mp.Pool(
        process_count
    ) as pool:
        catalogue = list(
            pool.imap_unordered(
                exact_catalogue_task,
                designs,
                chunksize=1,
            )
        )

    catalogue.sort(
        key=lambda item: sp.Rational(
            item[1]
        )
    )

    winner_design = catalogue[0][0]
    runner_design = catalogue[1][0]
    winner_ratio = sp.Rational(
        catalogue[0][1]
    )
    runner_ratio = sp.Rational(
        catalogue[1][1]
    )

    winner_dual = a64.exact_dual_value(
        10,
        sp.Rational(5),
        1,
        sp.Rational(1, 60000),
        winner_design,
    )
    runner_dual = a64.exact_dual_value(
        10,
        sp.Rational(5),
        1,
        sp.Rational(1, 60000),
        runner_design,
    )

    m10 = a67.audit_M(
        10,
        M10_SPEC,
    )

    symbolic_weak = (
        weak_signature_symbolic_numerator()
    )
    weak_values = {
        str(maximum): str(
            weak_numerator_at(
                symbolic_weak,
                maximum,
            )
        )
        for maximum in range(
            8,
            17,
        )
    }
    weak_signs = {
        maximum: int(
            sp.sign(
                sp.Rational(
                    weak_values[
                        str(maximum)
                    ]
                )
            )
        )
        for maximum in range(
            8,
            17,
        )
    }

    inherited = inherited_m10_basis(
        a67
    )

    # Confirm exact agreement with A69 for the two audited occurrences.
    a69_m8 = next(
        record
        for record in a69[
            "phase_records"
        ]
        if record["maximum"] == 8
        and record["phase"] == 5
    )
    a69_m9 = next(
        record
        for record in a69[
            "phase_records"
        ]
        if record["maximum"] == 9
        and record["phase"] == 7
    )

    weak_m8 = sp.Rational(
        weak_values["8"]
    )
    weak_m9 = sp.Rational(
        weak_values["9"]
    )
    weak_m10 = sp.Rational(
        weak_values["10"]
    )

    actual_phase_records = []

    for phase in m10["phases"]:
        supports = phase_supports(
            10,
            phase,
        )
        alpha_condition = next(
            condition
            for condition in phase[
                "conditions"
            ]
            if condition["name"]
            == "active_dual_alpha_+1"
        )
        kappa_condition = next(
            condition
            for condition in phase[
                "conditions"
            ]
            if condition["name"]
            == "kappa"
        )

        actual_phase_records.append(
            {
                "phase": phase["phase"],
                **supports,
                "active_observations": (
                    phase[
                        "active_observations"
                    ]
                ),
                "alpha_multiplier_positive": bool(
                    alpha_condition["ok"]
                    and alpha_condition[
                        "sample_sign"
                    ]
                    > 0
                ),
                "derivative_positive": bool(
                    kappa_condition["ok"]
                    and kappa_condition[
                        "sample_sign"
                    ]
                    > 0
                ),
                "alpha_lower": (
                    phase["s_upper"][
                        "alpha_decimal"
                    ]
                ),
                "alpha_upper": (
                    phase["s_lower"][
                        "alpha_decimal"
                    ]
                ),
            }
        )

    gates = {
        "A70_dominance_audit_passed": bool(
            all(
                a70["gates"].values()
            )
        ),
        "all_84_M10_catalogue_designs_ranked_exactly": bool(
            len(catalogue) == 84
        ),
        "M10_catalogue_winner_unique_2_3_4": bool(
            winner_design
            == (2, 3, 4)
            and runner_ratio
            > winner_ratio
        ),
        "winner_and_runner_exact_primal_dual": bool(
            winner_ratio
            == winner_dual
            and runner_ratio
            == runner_dual
        ),
        "weak_signature_formula_reproduces_A69_M8_M9": bool(
            weak_m8
            == sp.factor(
                sp.sympify(
                    a69_m8[
                        "alpha_cramer_numerator"
                    ]
                ).subs(
                    EPS_SYMBOL,
                    sp.Rational(
                        a69_m8[
                            "declared_epsilon"
                        ]
                    ),
                )
            )
            and weak_m9
            == sp.factor(
                sp.sympify(
                    a69_m9[
                        "alpha_cramer_numerator"
                    ]
                ).subs(
                    EPS_SYMBOL,
                    sp.Rational(
                        a69_m9[
                            "declared_epsilon"
                        ]
                    ),
                )
            )
        ),
        "weak_signature_orientation_bifurcates_at_M10": bool(
            weak_m8 < 0
            and weak_m9 < 0
            and weak_m10 > 0
        ),
        "inherited_M10_basis_dual_infeasible_everywhere": bool(
            inherited[
                "determinant_negative_on_domain"
            ]
            and inherited[
                "alpha_multiplier_negative_on_domain"
            ]
        ),
        "M10_six_exact_phases_globally_certified": bool(
            m10["phase_count"] == 6
            and all(
                m10["gates"].values()
            )
        ),
        "positive_alpha_multiplier_and_derivative_all_M10_phases": bool(
            all(
                record[
                    "alpha_multiplier_positive"
                ]
                and record[
                    "derivative_positive"
                ]
                for record
                in actual_phase_records
            )
        ),
        "M10_boundary_is_unique_global_first_anchor_optimum": bool(
            sp.Rational(
                m10[
                    "coalescence_ratio_limit"
                ]
            )
            > sp.Rational(
                m10[
                    "boundary_ratio"
                ]
            )
        ),
    }

    verdict = (
        "PASS_ORIENTATION_BIFURCATION_AND_ACTIVE_SET_PROTECTION"
        if all(
            gates.values()
        )
        else "FAIL_A71_ACTIVE_SET_BIFURCATION_AUDIT"
    )

    result = {
        "audit": (
            "A71_ORIENTATION_BIFURCATION_AND_ACTIVE_SET_PROTECTION"
        ),
        "M10_contract": {
            "support": (
                "{0,...,10}"
            ),
            "mean": "5",
            "target_exponent": 1,
            "delta": "1/1875",
            "epsilon": "1/60000",
            "integer_catalogue": (
                "{2,...,10}"
            ),
            "budget": 3,
            "exact_design_count": 84,
            "winner": list(
                winner_design
            ),
            "winner_ratio": str(
                winner_ratio
            ),
            "winner_risk_decimal": str(
                sp.N(
                    sp.log(
                        winner_ratio
                    )
                    / (
                        2
                        * sp.log(2)
                    ),
                    50,
                )
            ),
            "runner_up": list(
                runner_design
            ),
            "runner_ratio": str(
                runner_ratio
            ),
            "exact_ratio_gap": str(
                sp.factor(
                    runner_ratio
                    - winner_ratio
                )
            ),
            "top_10_designs": [
                {
                    "design": list(
                        design
                    ),
                    "ratio": ratio,
                }
                for design, ratio
                in catalogue[:10]
            ],
        },
        "weak_signature": {
            "p_support": (
                "{0,2,3,M}"
            ),
            "q_support": (
                "{1,4,5}"
            ),
            "active_observations": [
                ["alpha", 1],
                ["beta", -1],
                ["gamma", -1],
            ],
            "gamma": 4,
            "mean": "M/2",
            "R_definition": (
                "R=2^(-M)"
            ),
            "symbolic_cramer_numerator": str(
                symbolic_weak
            ),
            "values_M8_to_M16": (
                weak_values
            ),
            "signs_M8_to_M16": {
                str(key): value
                for key, value
                in weak_signs.items()
            },
            "orientation_bifurcation": (
                "The numerator is negative at M=8,9 "
                "and positive from M=10 in the audited "
                "M=8,...,16 continuation."
            ),
        },
        "inherited_M10_basis": (
            inherited
        ),
        "active_set_protection": {
            "statement": (
                "The inherited M=8,9 weak signature would "
                "have a negative alpha multiplier at M=10. "
                "It is therefore excluded by dual feasibility. "
                "The M=10 optimizer changes contact pattern "
                "and retains alpha+ with positive multiplier."
            ),
            "phase_count": (
                m10["phase_count"]
            ),
            "transition_count": (
                m10[
                    "transition_count"
                ]
            ),
            "transitions": (
                m10["transitions"]
            ),
            "phases": (
                actual_phase_records
            ),
        },
        "M10_global_theorem": {
            "design": (
                "{alpha,3,4}"
            ),
            "alpha_domain": (
                "[2,3)"
            ),
            "boundary_ratio": (
                m10[
                    "boundary_ratio"
                ]
            ),
            "boundary_risk_decimal": (
                m10[
                    "boundary_risk_decimal"
                ]
            ),
            "coalescence_ratio_limit": (
                m10[
                    "coalescence_ratio_limit"
                ]
            ),
            "coalescence_risk_limit_decimal": (
                m10[
                    "coalescence_risk_limit_decimal"
                ]
            ),
            "theorem": (
                "The exact minimax ratio is continuous "
                "and strictly increasing for alpha in [2,3). "
                "Therefore alpha*=2 is the unique global "
                "first-anchor optimum."
            ),
            "exact_phase_result": (
                m10
            ),
        },
        "formal_results": [
            (
                "the A70 weakest repeated signature has an "
                "explicit symbolic arithmetic-grid Cramer numerator"
            ),
            (
                "that numerator changes orientation between "
                "M=9 and M=10"
            ),
            (
                "the inherited M=10 basis would have a negative "
                "alpha multiplier throughout the full first-anchor domain"
            ),
            (
                "dual feasibility therefore prevents continuation "
                "of the weak signature"
            ),
            (
                "the M=10 optimizer changes active contact pattern "
                "and retains a positive alpha multiplier in all six phases"
            ),
            (
                "the exact global first-boundary theorem extends "
                "to M=10 despite failure of the naive signature recurrence"
            ),
            (
                "the exact M=10 integer catalogue winner is {2,3,4}"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A71 is exact for the M=10 central-mean contract "
            "and for the declared symbolic continuation of one "
            "contact signature. It does not prove the boundary law "
            "for every M. It shows that a fixed-signature induction "
            "is false and that active-set selection can protect "
            "dual orientation at the first extrapolated support."
        ),
    }

    output = HERE / (
        "a71_orientation_bifurcation_results.json"
    )
    output.write_text(
        json.dumps(
            result,
            indent=2,
        ),
        encoding="utf-8",
    )

    summary = {
        "audit": result[
            "audit"
        ],
        "gate_count": len(
            gates
        ),
        "pass_count": sum(
            gates.values()
        ),
        "catalogue_winner": (
            result[
                "M10_contract"
            ]["winner"]
        ),
        "weak_signature_signs": {
            key: value
            for key, value
            in result[
                "weak_signature"
            ][
                "signs_M8_to_M16"
            ].items()
        },
        "M10_phase_count": (
            m10[
                "phase_count"
            ]
        ),
        "M10_transition_count": (
            m10[
                "transition_count"
            ]
        ),
        "M10_boundary_risk": (
            m10[
                "boundary_risk_decimal"
            ]
        ),
        "M10_coalescence_risk": (
            m10[
                "coalescence_risk_limit_decimal"
            ]
        ),
        "failed_gates": [
            name
            for name, value
            in gates.items()
            if not value
        ],
        "verdict": verdict,
    }

    print(
        json.dumps(
            summary,
            indent=2,
        )
    )

    if not all(
        gates.values()
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
