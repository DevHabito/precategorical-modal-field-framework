#!/usr/bin/env python3
"""A78 exact rational-probe contact-selection audit.

This audit freezes the A77 rational probe

    s0 = 131/1000,  alpha0 = -log_2(s0),

and treats the interior P contact as a discrete structural variable.  For every
M=10,...,80 it exhaustively checks, in exact rational arithmetic, two declared
basis families:

    F3(M,k,sigma):
        P={0,k,k+1,M}, Q={1,h,h+1},
        active bands={alpha+, beta-, gamma_sigma};

    F2(M,k):
        P={0,k,M}, Q={1,h,h+1},
        active bands={alpha+, beta-}, gamma inactive;

where h=floor(M/2), 1<=k<=M-2 for F3, and 1<=k<=M-1 for F2.

Every candidate is tested against the *full* finite LP KKT system: positive
basic variables, positive active band multipliers, every nonbasic reduced cost,
and every inactive observation-band slack.  Therefore a strict pass certifies a
unique global basic optimum at the declared probe, not merely an optimum within
the candidate catalogue.

The result is finite and probe-specific.  It is not an interval theorem and is
not a theorem for arbitrary M.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE.parent / "results" if HERE.name == "audits" else HERE

S0 = sp.Rational(131, 1000)
M_MIN = 10
M_MAX = 80


@dataclass(frozen=True)
class BranchSpec:
    family: str
    maximum: int
    contact: int
    gamma_sign: int | None


def normalized_epsilon(maximum: int) -> sp.Rational:
    h = maximum // 2
    if maximum % 2 == 0:
        return sp.Rational(1, 1875 * 2**h)
    return sp.Rational(1, 2500 * 2**h)


def target_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2**x)


def beta_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (3 * x))


def gamma_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (4 * x))


def _classify_conditions(
    conditions: list[tuple[str, sp.Rational]],
) -> tuple[str, tuple[str, sp.Rational] | None]:
    for name, value in conditions:
        if value < 0:
            if name.startswith("basic_"):
                status = "primal_infeasible"
            elif name.startswith("active_dual_"):
                status = "active_dual_infeasible"
            elif name.startswith("reduced_cost_"):
                status = "reduced_cost_infeasible"
            elif name.startswith("inactive_slack_"):
                status = "inactive_slack_infeasible"
            else:
                status = "negative_condition"
            return status, (name, value)
        if value == 0:
            return "zero_condition", (name, value)
    return "pass", None


def _strict_pass_record(
    spec: BranchSpec,
    ratio: sp.Rational,
    conditions: list[tuple[str, sp.Rational]],
) -> dict[str, Any]:
    class_counts = {
        "basic": sum(name.startswith("basic_") for name, _ in conditions),
        "active_dual": sum(name.startswith("active_dual_") for name, _ in conditions),
        "reduced_cost": sum(name.startswith("reduced_cost_") for name, _ in conditions),
        "inactive_slack": sum(name.startswith("inactive_slack_") for name, _ in conditions),
    }
    return {
        "family": spec.family,
        "maximum": spec.maximum,
        "contact": spec.contact,
        "gamma_sign": spec.gamma_sign,
        "p_support": (
            [0, spec.contact, spec.contact + 1, spec.maximum]
            if spec.family == "three_band_adjacent"
            else [0, spec.contact, spec.maximum]
        ),
        "q_support": [
            1,
            spec.maximum // 2,
            spec.maximum // 2 + 1,
        ],
        "active_bands": (
            [
                ["alpha", 1],
                ["beta", -1],
                ["gamma", spec.gamma_sign],
            ]
            if spec.family == "three_band_adjacent"
            else [["alpha", 1], ["beta", -1]]
        ),
        "ratio_exact": str(ratio),
        "condition_count": len(conditions),
        "condition_class_counts": class_counts,
        "all_conditions_strictly_positive": True,
    }


def evaluate_three_band(
    maximum: int,
    contact: int,
    gamma_sign: int,
    *,
    collect_pass: bool = False,
) -> dict[str, Any]:
    spec = BranchSpec(
        "three_band_adjacent",
        maximum,
        contact,
        gamma_sign,
    )
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    p_points = [0, contact, contact + 1, maximum]
    q_points = [1, h, h + 1]

    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [*p_points, 0, 0, 0, -mean],
        [0, 0, 0, 0, *q_points, -mean],
        [
            0, 0, 0, 0,
            *[target_value(x) for x in q_points],
            0,
        ],
        [
            *[S0**x for x in p_points],
            *[-S0**x for x in q_points],
            -2 * epsilon,
        ],
        [
            *[-beta_value(x) for x in p_points],
            *[beta_value(x) for x in q_points],
            -2 * epsilon,
        ],
        [
            *[gamma_sign * gamma_value(x) for x in p_points],
            *[-gamma_sign * gamma_value(x) for x in q_points],
            -2 * epsilon,
        ],
    ]

    domain = sp.polys.matrices.DomainMatrix.from_Matrix(
        sp.Matrix(rows)
    ).to_field()
    try:
        inverse = domain.inv().to_Matrix()
    except Exception:
        return {"spec": spec, "status": "singular", "failure": None}

    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
    objective = sp.Matrix([
        *[target_value(x) for x in p_points],
        0, 0, 0, 0,
    ])
    basic = inverse * rhs
    dual = inverse.T * objective

    conditions: list[tuple[str, sp.Rational]] = []
    for index, x in enumerate(p_points):
        conditions.append((f"basic_p_{x}", basic[index]))
    for index, x in enumerate(q_points, start=4):
        conditions.append((f"basic_q_{x}", basic[index]))
    conditions.append(("basic_t", basic[7]))

    status, failure = _classify_conditions(conditions)
    if status != "pass":
        return {"spec": spec, "status": status, "failure": failure}

    active = [
        ("alpha", 1, dual[5]),
        ("beta", -1, dual[6]),
        ("gamma", gamma_sign, dual[7]),
    ]
    active_conditions = [
        (f"active_dual_{name}_{sign:+d}", value)
        for name, sign, value in active
    ]
    conditions.extend(active_conditions)
    status, failure = _classify_conditions(active_conditions)
    if status != "pass":
        return {"spec": spec, "status": status, "failure": failure}

    p_set = set(p_points)
    q_set = set(q_points)
    for x in range(maximum + 1):
        p_column = sp.Matrix([
            1, 0, x, 0, 0,
            S0**x,
            -beta_value(x),
            gamma_sign * gamma_value(x),
        ])
        q_column = sp.Matrix([
            0, 1, 0, x, target_value(x),
            -S0**x,
            beta_value(x),
            -gamma_sign * gamma_value(x),
        ])
        if x not in p_set:
            item = (
                f"reduced_cost_p_{x}",
                p_column.dot(dual) - target_value(x),
            )
            status, failure = _classify_conditions([item])
            if status != "pass":
                return {"spec": spec, "status": status, "failure": failure}
            conditions.append(item)
        if x not in q_set:
            item = (f"reduced_cost_q_{x}", q_column.dot(dual))
            status, failure = _classify_conditions([item])
            if status != "pass":
                return {"spec": spec, "status": status, "failure": failure}
            conditions.append(item)

    t_value = basic[7]
    alpha_difference = (
        sum(S0**x * basic[i] for i, x in enumerate(p_points))
        - sum(S0**x * basic[4 + i] for i, x in enumerate(q_points))
    )
    beta_difference = (
        sum(beta_value(x) * basic[i] for i, x in enumerate(p_points))
        - sum(
            beta_value(x) * basic[4 + i]
            for i, x in enumerate(q_points)
        )
    )
    gamma_difference = (
        sum(gamma_value(x) * basic[i] for i, x in enumerate(p_points))
        - sum(
            gamma_value(x) * basic[4 + i]
            for i, x in enumerate(q_points)
        )
    )
    inactive_conditions = [
        (
            "inactive_slack_alpha_-1",
            2 * epsilon * t_value + alpha_difference,
        ),
        (
            "inactive_slack_beta_+1",
            2 * epsilon * t_value - beta_difference,
        ),
        (
            f"inactive_slack_gamma_{-gamma_sign:+d}",
            2 * epsilon * t_value + gamma_sign * gamma_difference,
        ),
    ]
    conditions.extend(inactive_conditions)
    status, failure = _classify_conditions(inactive_conditions)
    if status != "pass":
        return {"spec": spec, "status": status, "failure": failure}

    ratio = sum(
        target_value(x) * basic[i]
        for i, x in enumerate(p_points)
    )
    record = (
        _strict_pass_record(spec, ratio, conditions)
        if collect_pass
        else None
    )
    return {
        "spec": spec,
        "status": "pass",
        "failure": None,
        "record": record,
    }


def evaluate_two_band(
    maximum: int,
    contact: int,
    *,
    collect_pass: bool = False,
) -> dict[str, Any]:
    spec = BranchSpec(
        "two_band_compressed",
        maximum,
        contact,
        None,
    )
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    p_points = [0, contact, maximum]
    q_points = [1, h, h + 1]

    rows = [
        [1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 1, 1, 1, -1],
        [*p_points, 0, 0, 0, -mean],
        [0, 0, 0, *q_points, -mean],
        [
            0, 0, 0,
            *[target_value(x) for x in q_points],
            0,
        ],
        [
            *[S0**x for x in p_points],
            *[-S0**x for x in q_points],
            -2 * epsilon,
        ],
        [
            *[-beta_value(x) for x in p_points],
            *[beta_value(x) for x in q_points],
            -2 * epsilon,
        ],
    ]

    domain = sp.polys.matrices.DomainMatrix.from_Matrix(
        sp.Matrix(rows)
    ).to_field()
    try:
        inverse = domain.inv().to_Matrix()
    except Exception:
        return {"spec": spec, "status": "singular", "failure": None}

    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0])
    objective = sp.Matrix([
        *[target_value(x) for x in p_points],
        0, 0, 0, 0,
    ])
    basic = inverse * rhs
    dual = inverse.T * objective

    conditions: list[tuple[str, sp.Rational]] = []
    for index, x in enumerate(p_points):
        conditions.append((f"basic_p_{x}", basic[index]))
    for index, x in enumerate(q_points, start=3):
        conditions.append((f"basic_q_{x}", basic[index]))
    conditions.append(("basic_t", basic[6]))

    status, failure = _classify_conditions(conditions)
    if status != "pass":
        return {"spec": spec, "status": status, "failure": failure}

    active_conditions = [
        ("active_dual_alpha_+1", dual[5]),
        ("active_dual_beta_-1", dual[6]),
    ]
    conditions.extend(active_conditions)
    status, failure = _classify_conditions(active_conditions)
    if status != "pass":
        return {"spec": spec, "status": status, "failure": failure}

    p_set = set(p_points)
    q_set = set(q_points)
    for x in range(maximum + 1):
        p_column = sp.Matrix([
            1, 0, x, 0, 0,
            S0**x,
            -beta_value(x),
        ])
        q_column = sp.Matrix([
            0, 1, 0, x, target_value(x),
            -S0**x,
            beta_value(x),
        ])
        if x not in p_set:
            item = (
                f"reduced_cost_p_{x}",
                p_column.dot(dual) - target_value(x),
            )
            status, failure = _classify_conditions([item])
            if status != "pass":
                return {"spec": spec, "status": status, "failure": failure}
            conditions.append(item)
        if x not in q_set:
            item = (f"reduced_cost_q_{x}", q_column.dot(dual))
            status, failure = _classify_conditions([item])
            if status != "pass":
                return {"spec": spec, "status": status, "failure": failure}
            conditions.append(item)

    t_value = basic[6]
    alpha_difference = (
        sum(S0**x * basic[i] for i, x in enumerate(p_points))
        - sum(S0**x * basic[3 + i] for i, x in enumerate(q_points))
    )
    beta_difference = (
        sum(beta_value(x) * basic[i] for i, x in enumerate(p_points))
        - sum(
            beta_value(x) * basic[3 + i]
            for i, x in enumerate(q_points)
        )
    )
    gamma_difference = (
        sum(gamma_value(x) * basic[i] for i, x in enumerate(p_points))
        - sum(
            gamma_value(x) * basic[3 + i]
            for i, x in enumerate(q_points)
        )
    )
    inactive_conditions = [
        (
            "inactive_slack_alpha_-1",
            2 * epsilon * t_value + alpha_difference,
        ),
        (
            "inactive_slack_beta_+1",
            2 * epsilon * t_value - beta_difference,
        ),
        (
            "inactive_slack_gamma_+1",
            2 * epsilon * t_value - gamma_difference,
        ),
        (
            "inactive_slack_gamma_-1",
            2 * epsilon * t_value + gamma_difference,
        ),
    ]
    conditions.extend(inactive_conditions)
    status, failure = _classify_conditions(inactive_conditions)
    if status != "pass":
        return {"spec": spec, "status": status, "failure": failure}

    ratio = sum(
        target_value(x) * basic[i]
        for i, x in enumerate(p_points)
    )
    record = (
        _strict_pass_record(spec, ratio, conditions)
        if collect_pass
        else None
    )
    return {
        "spec": spec,
        "status": "pass",
        "failure": None,
        "record": record,
    }


def _compact_runs(selected: list[dict[str, Any]]) -> list[dict[str, Any]]:
    runs: list[dict[str, Any]] = []
    start = selected[0]["maximum"]
    previous = start
    key = (
        selected[0]["family"],
        selected[0]["contact"],
    )
    for item in selected[1:]:
        current_key = (item["family"], item["contact"])
        if current_key != key or item["maximum"] != previous + 1:
            runs.append({
                "M_start": start,
                "M_end": previous,
                "family": key[0],
                "contact": key[1],
                "length": previous - start + 1,
            })
            start = item["maximum"]
            key = current_key
        previous = item["maximum"]
    runs.append({
        "M_start": start,
        "M_end": previous,
        "family": key[0],
        "contact": key[1],
        "length": previous - start + 1,
    })
    return runs


def main() -> None:
    status_counts = {
        "three_band_adjacent": {},
        "two_band_compressed": {},
    }
    catalogue: list[dict[str, Any]] = []
    selected: list[dict[str, Any]] = []

    def register(result: dict[str, Any]) -> None:
        spec: BranchSpec = result["spec"]
        family_counts = status_counts[spec.family]
        family_counts[result["status"]] = (
            family_counts.get(result["status"], 0) + 1
        )
        catalogue.append({
            "family": spec.family,
            "maximum": spec.maximum,
            "contact": spec.contact,
            "gamma_sign": spec.gamma_sign,
            "status": result["status"],
            "first_failure": (result["failure"][0] if result["failure"] else None),
        })

    for maximum in range(M_MIN, M_MAX + 1):
        pass_records: list[dict[str, Any]] = []

        for contact in range(1, maximum - 1):
            for gamma_sign in (-1, 1):
                result = evaluate_three_band(
                    maximum,
                    contact,
                    gamma_sign,
                    collect_pass=True,
                )
                register(result)
                if result["status"] == "pass":
                    pass_records.append(result["record"])

        for contact in range(1, maximum):
            result = evaluate_two_band(maximum, contact, collect_pass=True)
            register(result)
            if result["status"] == "pass":
                pass_records.append(result["record"])

        if len(pass_records) != 1:
            selected.append({
                "maximum": maximum,
                "selection_error": pass_records,
            })
            continue

        selected.append(pass_records[0])

    expected_branch_count = sum(
        2 * (maximum - 2) + (maximum - 1)
        for maximum in range(M_MIN, M_MAX + 1)
    )
    compressed_supports = [
        item["maximum"]
        for item in selected
        if item.get("family") == "two_band_compressed"
    ]
    negative_gamma_supports = [
        item["maximum"]
        for item in selected
        if item.get("gamma_sign") == -1
    ]
    contact_runs = _compact_runs(selected)

    a77_reproduction = {
        23: ("three_band_adjacent", 5, -1),
        24: ("three_band_adjacent", 6, 1),
        25: ("three_band_adjacent", 6, 1),
    }
    selected_lookup = {
        item["maximum"]: (
            item.get("family"),
            item.get("contact"),
            item.get("gamma_sign"),
        )
        for item in selected
        if "family" in item
    }

    compressed_transition_witnesses = []
    for maximum in compressed_supports:
        compressed = selected_lookup[maximum]
        k = int(compressed[1])
        left = evaluate_three_band(maximum, k - 1, 1)
        right = evaluate_three_band(maximum, k, -1)
        compressed_transition_witnesses.append({
            "maximum": maximum,
            "compressed_contact": k,
            "left_adjacent_family": {
                "contact": k - 1,
                "gamma_sign": 1,
                "status": left["status"],
                "first_failure": ({"name": left["failure"][0], "value": str(left["failure"][1])} if left["failure"] else None),
            },
            "right_adjacent_family": {
                "contact": k,
                "gamma_sign": -1,
                "status": right["status"],
                "first_failure": ({"name": right["failure"][0], "value": str(right["failure"][1])} if right["failure"] else None),
            },
        })

    all_selected_valid = all("family" in item for item in selected)
    zero_count = sum(
        1 for item in catalogue if item["status"] == "zero_condition"
    )
    singular_count = sum(
        1 for item in catalogue if item["status"] == "singular"
    )
    run_lengths = [
        item["length"]
        for item in contact_runs
        if item["family"] == "three_band_adjacent"
    ]

    gates = {
        "declared_branch_count_exact": (
            len(catalogue) == expected_branch_count == 9230
        ),
        "all_supports_have_one_strict_selection": (
            all_selected_valid and len(selected) == 71
        ),
        "no_singular_candidate_basis": singular_count == 0,
        "no_zero_condition_boundary_at_probe": zero_count == 0,
        "A77_M23_M25_sequence_reproduced": all(
            selected_lookup.get(maximum) == expected
            for maximum, expected in a77_reproduction.items()
        ),
        "exactly_three_gamma_inactive_compressions": (
            compressed_supports == [40, 57, 74]
        ),
        "all_other_supports_use_adjacent_three_band_family": (
            sum(
                item.get("family") == "three_band_adjacent"
                for item in selected
            ) == 68
        ),
        "compressed_transitions_are_forced_by_dual_failure": all(
            witness["left_adjacent_family"]["status"]
            == "active_dual_infeasible"
            and witness["right_adjacent_family"]["status"]
            == "active_dual_infeasible"
            for witness in compressed_transition_witnesses
        ),
        "contact_blocks_are_not_uniform_five_support_blocks": (
            len(set(run_lengths)) > 1
        ),
        "selected_conditions_are_strictly_positive": all(
            item.get("all_conditions_strictly_positive") is True
            for item in selected
        ),
        "negative_gamma_set_frozen": negative_gamma_supports == [
            13, 18, 23, 28, 29, 34,
            45, 51, 56, 62, 68,
        ],
        "finite_probe_scope_preserved": (
            M_MIN == 10 and M_MAX == 80 and S0 == sp.Rational(131, 1000)
        ),
    }

    summary = {
        "audit": "A78_EXACT_RATIONAL_PROBE_CONTACT_SELECTION",
        "contract": {
            "M_min": M_MIN,
            "M_max": M_MAX,
            "support": "{0,...,M}",
            "mean": "M/2",
            "target_exponent": 1,
            "s0": str(S0),
            "alpha0_decimal": f"{-math.log2(float(S0)):.15f}",
            "beta_exponent": 3,
            "gamma_exponent": 4,
            "epsilon_even": "1/(1875*2^(M/2))",
            "epsilon_odd": "1/(2500*2^floor(M/2))",
        },
        "candidate_families": {
            "three_band_adjacent": (
                "P={0,k,k+1,M}, Q={1,h,h+1}, "
                "active={alpha+,beta-,gamma±}"
            ),
            "two_band_compressed": (
                "P={0,k,M}, Q={1,h,h+1}, "
                "active={alpha+,beta-}, gamma inactive"
            ),
        },
        "branch_count": len(catalogue),
        "expected_branch_count": expected_branch_count,
        "status_counts": status_counts,
        "selected_support_count": len(selected),
        "three_band_selection_count": 68,
        "two_band_compression_count": 3,
        "compressed_supports": compressed_supports,
        "negative_gamma_supports": negative_gamma_supports,
        "contact_runs": contact_runs,
        "compressed_transition_witnesses": compressed_transition_witnesses,
        "selected": selected,
        "gates": gates,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": (
            "PASS_EXACT_RATIONAL_PROBE_CONTACT_SELECTION_AND_COMPRESSION_RESETS"
            if all(gates.values())
            else "FAIL"
        ),
        "claim_boundary": [
            "Exact only at s=s0=131/1000.",
            "Exact only for integer supports 10<=M<=80.",
            "No interval theorem is claimed.",
            "No all-M recurrence is claimed.",
            "No physical interpretation is inferred from the LP contact sequence.",
        ],
    }

    catalogue_output = {
        "audit": "A78_EXACT_RATIONAL_PROBE_BRANCH_CATALOGUE",
        "branch_count": len(catalogue),
        "catalogue": catalogue,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    result_path = OUTPUT_DIR / "a78_rational_probe_contact_selection_results.json"
    catalogue_path = OUTPUT_DIR / "a78_rational_probe_branch_catalogue.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    catalogue_path.write_text(
        json.dumps(catalogue_output, indent=2),
        encoding="utf-8",
    )

    print(json.dumps({
        "audit": summary["audit"],
        "branch_count": len(catalogue),
        "selected_support_count": len(selected),
        "compressed_supports": compressed_supports,
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "verdict": summary["verdict"],
        "result": result_path.name,
        "catalogue": catalogue_path.name,
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
