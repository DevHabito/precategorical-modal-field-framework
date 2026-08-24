#!/usr/bin/env python3
"""A69 audit: Cramer reduction, orientation margins, and TP obstruction.

General fixed-basis theorem
---------------------------
Let B(s, epsilon) be an active Charnes-Cooper basis in which only the
positive alpha observation row depends on s=2^(-alpha). The corresponding
dual multiplier is

    lambda_alpha(s, epsilon)
      = Delta_alpha(epsilon) / Delta(s, epsilon),

where Delta=det B and Delta_alpha is obtained by replacing the alpha row of
B by the basic objective row.

Then:

1. Delta_alpha is independent of s.
2. Delta_alpha is affine in epsilon (degree at most one), because epsilon
   appears only in the single scale column.
3. At fixed epsilon with Delta_alpha != 0, lambda_alpha cannot change sign
   on a connected nonsingular region of the same active basis.

A67 family audit
----------------
The theorem is evaluated on all 33 exact A67 phases. Exact orientation,
contact-signature compression, noise-flip margins, and full-domain
determinant roots are recorded.

Obstruction theorem
-------------------
A same-order rational counterexample shows that contact order and abstract
Chebyshev/total-positivity structure alone do not fix the Cramer numerator
sign once the upper/lower envelopes are coupled by the mean and scale row.

Therefore an arbitrary-node oriented-matroid proof is false. A future
structural theorem must exploit additional arithmetic-grid structure.
"""

from __future__ import annotations

import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"
A67_RESULTS = HERE / "a67_central_mean_support_family_results.json"

S = sp.Symbol("s")
E = sp.Symbol("epsilon")


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def build_active_basis(
    maximum: int,
    mean: sp.Rational,
    gamma: int,
    positive_indices: tuple[int, ...],
    active_observations: tuple[tuple[str, int], ...],
) -> tuple[sp.Matrix, sp.Matrix, int]:
    support = list(range(maximum + 1))
    count = maximum + 1
    dimension = 2 * count + 1

    target = [
        sp.Rational(1, 2 ** x)
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
    row[-1] = -mean
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(support):
        row[count + index] = x
    row[-1] = -mean
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index in range(count):
        row[count + index] = target[index]
    rows.append(row)

    exponent_map = {
        "alpha": None,
        "beta": 3,
        "gamma": gamma,
    }

    for name, sign in active_observations:
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
        row[-1] = -2 * E
        rows.append(row)

    if len(rows) != len(positive_indices):
        raise RuntimeError("Active row/basic-variable count mismatch")

    basis = sp.Matrix(
        [
            [
                rows[row_index][column_index]
                for column_index in positive_indices
            ]
            for row_index in range(len(rows))
        ]
    )

    objective = [sp.Integer(0)] * dimension
    for index in range(count):
        objective[index] = target[index]

    basic_objective = sp.Matrix(
        [
            objective[column_index]
            for column_index in positive_indices
        ]
    )

    alpha_row_index = (
        5
        + list(active_observations).index(
            ("alpha", 1)
        )
    )

    return basis, basic_objective, alpha_row_index


def contact_signature(
    maximum: int,
    positive_indices: tuple[int, ...],
    active_observations: tuple[tuple[str, int], ...],
) -> dict[str, Any]:
    count = maximum + 1
    p_support = tuple(
        index
        for index in positive_indices
        if 0 <= index < count
    )
    q_support = tuple(
        index - count
        for index in positive_indices
        if count <= index < 2 * count
    )

    union = sorted(
        set(p_support)
        | set(q_support)
    )
    labels = tuple(
        (
            "B"
            if x in p_support and x in q_support
            else "P"
            if x in p_support
            else "Q"
        )
        for x in union
    )

    return {
        "p_support": p_support,
        "q_support": q_support,
        "labels": labels,
        "active_observations": active_observations,
        "p_count": len(p_support),
        "q_count": len(q_support),
        "key": (
            labels,
            active_observations,
            len(p_support),
            len(q_support),
        ),
    }


def roots_in_full_domain(
    expression: sp.Expr,
) -> list[dict[str, Any]]:
    numerator = sp.Poly(
        sp.fraction(
            sp.cancel(expression)
        )[0],
        S,
        domain=sp.QQ,
    )

    if numerator.degree() <= 0:
        return []

    roots = []
    for (left, right), multiplicity in sp.intervals(
        numerator,
        eps=sp.Rational(1, 10**12),
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
                "decimal": str(
                    sp.N(
                        (left + right) / 2,
                        40,
                    )
                ),
            }
        )
    return roots


def arbitrary_contact_numerator(
    points: tuple[int, ...],
) -> sp.Expr:
    """Exact numerator for one fixed contact-order signature.

    Signature:
        labels = P, B, Q, P, Q, P
        active bands = alpha+, beta-, gamma+
        target exponent=1, beta=3, gamma=10
        epsilon=0
        mean=(min+max)/2
    """
    labels = (
        "P",
        "B",
        "Q",
        "P",
        "Q",
        "P",
    )

    p_points = []
    q_points = []

    for x, label in zip(points, labels):
        if label in ("P", "B"):
            p_points.append(sp.Rational(x))
        if label in ("Q", "B"):
            q_points.append(sp.Rational(x))

    p_count = len(p_points)
    q_count = len(q_points)
    dimension = p_count + q_count + 1
    mean = sp.Rational(
        points[0] + points[-1],
        2,
    )

    rows: list[list[sp.Expr]] = []

    row = [sp.Integer(0)] * dimension
    for index in range(p_count):
        row[index] = 1
    row[-1] = -1
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index in range(q_count):
        row[p_count + index] = 1
    row[-1] = -1
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(p_points):
        row[index] = x
    row[-1] = -mean
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(q_points):
        row[p_count + index] = x
    row[-1] = -mean
    rows.append(row)

    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(q_points):
        row[p_count + index] = 2 ** (-x)
    rows.append(row)

    # Cramer replacement of the alpha row by the objective row.
    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(p_points):
        row[index] = 2 ** (-x)
    rows.append(row)

    # beta negative.
    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(p_points):
        row[index] = -2 ** (-3 * x)
    for index, x in enumerate(q_points):
        row[p_count + index] = 2 ** (-3 * x)
    rows.append(row)

    # gamma positive.
    row = [sp.Integer(0)] * dimension
    for index, x in enumerate(p_points):
        row[index] = 2 ** (-10 * x)
    for index, x in enumerate(q_points):
        row[p_count + index] = -2 ** (-10 * x)
    rows.append(row)

    return sp.factor(
        sp.Matrix(rows).det()
    )


def main() -> None:
    if not A67_SCRIPT.exists():
        raise FileNotFoundError(A67_SCRIPT)
    if not A67_RESULTS.exists():
        raise FileNotFoundError(A67_RESULTS)

    a67 = load_module(
        A67_SCRIPT,
        "a67_for_a69",
    )
    a67_results = json.loads(
        A67_RESULTS.read_text(
            encoding="utf-8"
        )
    )

    phase_records = []
    signature_records: dict[
        tuple[Any, ...],
        list[dict[str, Any]],
    ] = defaultdict(list)

    cramer_gates = []
    independence_gates = []
    affine_gates = []
    sign_match_gates = []
    phase_nonsingularity_gates = []

    finite_flip_margins = []
    full_domain_root_phase_count = 0
    full_domain_root_total = 0

    for support_result in a67_results["supports"]:
        maximum = support_result["maximum"]
        configuration = a67.FAMILY[maximum]

        for phase_result, phase_spec in zip(
            support_result["phases"],
            configuration["phase_specs"],
        ):
            positive_indices, active_observations = phase_spec

            basis, basic_objective, alpha_row_index = build_active_basis(
                maximum,
                configuration["mean"],
                configuration["gamma"],
                positive_indices,
                active_observations,
            )

            determinant = sp.factor(
                basis.det()
            )

            numerator_basis = basis.copy()
            numerator_basis[
                alpha_row_index,
                :,
            ] = basic_objective.T

            numerator = sp.factor(
                numerator_basis.det()
            )

            dual = basis.T.inv() * basic_objective
            alpha_multiplier = sp.cancel(
                dual[alpha_row_index]
            )

            cramer_ratio = sp.cancel(
                numerator
                / determinant
            )

            cramer_equal = bool(
                sp.cancel(
                    alpha_multiplier
                    - cramer_ratio
                )
                == 0
            )
            cramer_gates.append(
                cramer_equal
            )

            numerator_s_degree = sp.Poly(
                numerator,
                S,
                domain=sp.QQ[E],
            ).degree()

            numerator_epsilon_poly = sp.Poly(
                numerator,
                E,
                domain=sp.QQ[S],
            )
            numerator_epsilon_degree = (
                numerator_epsilon_poly.degree()
            )

            independence_gates.append(
                numerator_s_degree == 0
            )
            affine_gates.append(
                numerator_epsilon_degree <= 1
            )

            numerator_constant = sp.factor(
                numerator_epsilon_poly.nth(0)
            )
            numerator_slope = (
                sp.factor(
                    numerator_epsilon_poly.nth(1)
                )
                if numerator_epsilon_degree >= 1
                else sp.Integer(0)
            )

            declared_epsilon = (
                configuration["epsilon"]
            )
            declared_numerator = sp.factor(
                numerator.subs(
                    E,
                    declared_epsilon,
                )
            )
            declared_determinant = sp.factor(
                determinant.subs(
                    E,
                    declared_epsilon,
                )
            )

            midpoint = (
                sp.Rational(
                    phase_result[
                        "s_lower"
                    ]["right"]
                )
                + sp.Rational(
                    phase_result[
                        "s_upper"
                    ]["left"]
                )
            ) / 2

            numerator_sign = int(
                sp.sign(
                    declared_numerator
                )
            )
            determinant_sign = int(
                sp.sign(
                    declared_determinant.subs(
                        S,
                        midpoint,
                    )
                )
            )

            sign_match = bool(
                numerator_sign
                == determinant_sign
                and numerator_sign != 0
            )
            sign_match_gates.append(
                sign_match
            )

            alpha_condition = next(
                condition
                for condition
                in phase_result["conditions"]
                if condition["name"]
                == "active_dual_alpha_+1"
            )
            phase_nonsingularity_gates.append(
                bool(
                    alpha_condition["ok"]
                    and alpha_condition[
                        "sample_sign"
                    ]
                    > 0
                )
            )

            positive_flip_threshold = None
            flip_margin = None

            if numerator_slope != 0:
                root = sp.factor(
                    -numerator_constant
                    / numerator_slope
                )

                if root > 0:
                    positive_flip_threshold = root
                    flip_margin = sp.factor(
                        root
                        / declared_epsilon
                    )
                    finite_flip_margins.append(
                        (
                            flip_margin,
                            maximum,
                            phase_result["phase"],
                        )
                    )

            roots = roots_in_full_domain(
                declared_determinant
            )
            if roots:
                full_domain_root_phase_count += 1
                full_domain_root_total += len(
                    roots
                )

            signature = contact_signature(
                maximum,
                positive_indices,
                active_observations,
            )

            record = {
                "maximum": maximum,
                "phase": phase_result["phase"],
                "positive_indices": list(
                    positive_indices
                ),
                "p_support": list(
                    signature["p_support"]
                ),
                "q_support": list(
                    signature["q_support"]
                ),
                "contact_labels": list(
                    signature["labels"]
                ),
                "active_observations": [
                    list(observation)
                    for observation
                    in active_observations
                ],
                "basis_determinant": str(
                    determinant
                ),
                "alpha_cramer_numerator": str(
                    numerator
                ),
                "numerator_constant": str(
                    numerator_constant
                ),
                "numerator_epsilon_slope": str(
                    numerator_slope
                ),
                "numerator_s_degree": (
                    numerator_s_degree
                ),
                "numerator_epsilon_degree": (
                    numerator_epsilon_degree
                ),
                "declared_epsilon": str(
                    declared_epsilon
                ),
                "declared_numerator_sign": (
                    numerator_sign
                ),
                "declared_determinant_sign": (
                    determinant_sign
                ),
                "signs_match": sign_match,
                "positive_flip_threshold": (
                    str(
                        positive_flip_threshold
                    )
                    if positive_flip_threshold
                    is not None
                    else None
                ),
                "flip_margin_multiple": (
                    str(
                        sp.N(
                            flip_margin,
                            50,
                        )
                    )
                    if flip_margin is not None
                    else None
                ),
                "full_domain_determinant_roots": (
                    roots
                ),
                "cramer_identity_exact": (
                    cramer_equal
                ),
            }

            phase_records.append(
                record
            )
            signature_records[
                signature["key"]
            ].append(record)

    signature_summary = []
    repeated_signature_sign_gates = []

    for signature_key, records in signature_records.items():
        signs = {
            record[
                "declared_numerator_sign"
            ]
            for record in records
        }
        consistent = len(signs) == 1

        if len(records) > 1:
            repeated_signature_sign_gates.append(
                consistent
            )

        labels, active, p_count, q_count = signature_key

        signature_summary.append(
            {
                "contact_labels": list(
                    labels
                ),
                "active_observations": [
                    list(observation)
                    for observation in active
                ],
                "p_count": p_count,
                "q_count": q_count,
                "instance_count": len(
                    records
                ),
                "numerator_signs": sorted(
                    signs
                ),
                "sign_consistent_within_A67": (
                    consistent
                ),
                "instances": [
                    {
                        "maximum": record[
                            "maximum"
                        ],
                        "phase": record[
                            "phase"
                        ],
                    }
                    for record in records
                ],
            }
        )

    uniform_points = (
        0,
        1,
        2,
        3,
        4,
        5,
    )
    stretched_points = (
        0,
        1,
        2,
        3,
        4,
        9,
    )

    uniform_counterexample_value = arbitrary_contact_numerator(
        uniform_points
    )
    stretched_counterexample_value = arbitrary_contact_numerator(
        stretched_points
    )

    counterexample_gate = bool(
        uniform_counterexample_value > 0
        and stretched_counterexample_value < 0
    )

    finite_flip_margins.sort(
        key=lambda item: item[0]
    )

    minimum_flip_margin = (
        finite_flip_margins[0]
        if finite_flip_margins
        else None
    )

    numerator_positive_count = sum(
        record[
            "declared_numerator_sign"
        ]
        > 0
        for record in phase_records
    )
    numerator_negative_count = sum(
        record[
            "declared_numerator_sign"
        ]
        < 0
        for record in phase_records
    )

    signature_size_distribution = Counter(
        len(records)
        for records in signature_records.values()
    )

    gates = {
        "A67_family_theorem_passed": bool(
            all(
                a67_results["gates"].values()
            )
        ),
        "all_33_cramer_identities_exact": bool(
            len(cramer_gates) == 33
            and all(cramer_gates)
        ),
        "all_33_numerators_independent_of_alpha": bool(
            len(independence_gates)
            == 33
            and all(
                independence_gates
            )
        ),
        "all_33_numerators_affine_in_epsilon": bool(
            len(affine_gates) == 33
            and all(affine_gates)
        ),
        "all_33_declared_numerator_and_basis_signs_match": bool(
            len(sign_match_gates)
            == 33
            and all(sign_match_gates)
        ),
        "all_33_alpha_multipliers_positive_on_certified_phases": bool(
            len(
                phase_nonsingularity_gates
            )
            == 33
            and all(
                phase_nonsingularity_gates
            )
        ),
        "minimum_finite_numerator_flip_margin_above_100": bool(
            minimum_flip_margin
            is not None
            and minimum_flip_margin[0]
            > 100
        ),
        "repeated_A67_contact_signatures_have_consistent_orientation": bool(
            repeated_signature_sign_gates
            and all(
                repeated_signature_sign_gates
            )
        ),
        "same_order_exact_counterexample_rejects_order_only_theorem": bool(
            counterexample_gate
        ),
        "full_domain_basis_roots_show_phase_partition_is_necessary": bool(
            full_domain_root_phase_count
            == 17
            and full_domain_root_total
            >= 17
        ),
    }

    verdict = (
        "PASS_CRAMER_REDUCTION_WITH_TOTAL_POSITIVITY_OBSTRUCTION"
        if all(gates.values())
        else "FAIL_A69_CRAMER_ORIENTATION_AUDIT"
    )

    result = {
        "audit": (
            "A69_CRAMER_CHEBYSHEV_REDUCTION"
        ),
        "general_fixed_basis_theorem": {
            "cramer_formula": (
                "lambda_alpha(s,epsilon)="
                "Delta_alpha(epsilon)/Delta(s,epsilon)"
            ),
            "alpha_independence": (
                "Delta_alpha is independent of s because "
                "the only s-dependent row is replaced by "
                "the objective row."
            ),
            "epsilon_affinity": (
                "Delta_alpha has degree at most one in "
                "epsilon because epsilon occurs only in "
                "the single scale column."
            ),
            "no_internal_sign_flip": (
                "At fixed epsilon with nonzero Delta_alpha, "
                "the alpha multiplier cannot change sign on "
                "a connected region where the active basis "
                "determinant is nonzero."
            ),
        },
        "family_summary": {
            "phase_count": len(
                phase_records
            ),
            "unique_contact_signature_count": len(
                signature_records
            ),
            "repeated_contact_signature_count": sum(
                len(records) > 1
                for records
                in signature_records.values()
            ),
            "signature_size_distribution": {
                str(size): count
                for size, count
                in sorted(
                    signature_size_distribution.items()
                )
            },
            "positive_numerator_count": (
                numerator_positive_count
            ),
            "negative_numerator_count": (
                numerator_negative_count
            ),
            "finite_positive_flip_threshold_count": len(
                finite_flip_margins
            ),
            "minimum_flip_margin": {
                "multiple": str(
                    sp.N(
                        minimum_flip_margin[0],
                        50,
                    )
                ),
                "maximum": (
                    minimum_flip_margin[1]
                ),
                "phase": (
                    minimum_flip_margin[2]
                ),
            },
            "basis_with_roots_in_full_alpha_domain": (
                full_domain_root_phase_count
            ),
            "full_domain_basis_root_count": (
                full_domain_root_total
            ),
            "interpretation": (
                "The numerator orientation is highly robust "
                "inside the A67 arithmetic-grid family, but "
                "the basis determinant orientation is phase "
                "dependent."
            ),
        },
        "contact_signatures": (
            signature_summary
        ),
        "phase_records": (
            phase_records
        ),
        "order_only_counterexample": {
            "contact_labels": [
                "P",
                "B",
                "Q",
                "P",
                "Q",
                "P",
            ],
            "active_observations": [
                ["alpha", 1],
                ["beta", -1],
                ["gamma", 1],
            ],
            "target_exponent": 1,
            "beta_exponent": 3,
            "gamma_exponent": 10,
            "epsilon": 0,
            "mean_rule": (
                "(minimum contact + maximum contact)/2"
            ),
            "uniform_contacts": list(
                uniform_points
            ),
            "uniform_numerator": str(
                uniform_counterexample_value
            ),
            "uniform_sign": int(
                sp.sign(
                    uniform_counterexample_value
                )
            ),
            "stretched_contacts": list(
                stretched_points
            ),
            "stretched_numerator": str(
                stretched_counterexample_value
            ),
            "stretched_sign": int(
                sp.sign(
                    stretched_counterexample_value
                )
            ),
            "conclusion": (
                "The same contact order and active-band signs "
                "can produce opposite Cramer-numerator signs. "
                "Order-only total positivity is insufficient "
                "for the coupled dual-envelope matrix."
            ),
        },
        "formal_results": [
            (
                "the alpha Cramer numerator is exactly "
                "independent of alpha in every fixed active basis"
            ),
            (
                "the numerator is affine in the common tolerance"
            ),
            (
                "within a nonsingular basis phase the alpha "
                "multiplier has no internal zero"
            ),
            (
                "the 33 A67 numerator orientations have at least "
                "a 102.44-fold declared-noise margin before any "
                "possible numerator sign reversal"
            ),
            (
                "18 contact-order signatures compress the 33 "
                "phases and all repeated signatures agree inside "
                "the arithmetic-grid family"
            ),
            (
                "an exact same-order counterexample proves that "
                "abstract contact order alone cannot determine "
                "the sign"
            ),
            (
                "17 active bases have determinant roots somewhere "
                "in the full alpha domain, so the phase partition "
                "cannot be discarded"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A69 does not prove alpha-multiplier positivity for "
            "arbitrary supports. It proves a general fixed-basis "
            "Cramer reduction, audits its exact arithmetic-grid "
            "orientation on A67, and rejects the stronger "
            "order-only total-positivity conjecture."
        ),
    }

    output_path = HERE / (
        "a69_cramer_chebyshev_reduction_results.json"
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
        "gate_count": len(
            gates
        ),
        "pass_count": sum(
            gates.values()
        ),
        "phase_count": len(
            phase_records
        ),
        "unique_contact_signatures": len(
            signature_records
        ),
        "minimum_flip_margin": (
            result["family_summary"][
                "minimum_flip_margin"
            ]
        ),
        "full_domain_basis_root_phases": (
            full_domain_root_phase_count
        ),
        "counterexample_signs": [
            result[
                "order_only_counterexample"
            ]["uniform_sign"],
            result[
                "order_only_counterexample"
            ]["stretched_sign"],
        ],
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

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
