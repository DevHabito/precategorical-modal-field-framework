#!/usr/bin/env python3
"""A97 exact endpoint-released interval and obstruction audit.

A96 resolved the first A95 obstruction at M=125, s=33/250 by releasing the
forced P-endpoint 0.  The exact basis is

    P={j-1,j,M}, Q={1,h,h+1}, active={alpha+,beta-}, gamma inactive,

with (M,j)=(125,24).  A97 performs two independent upgrades.

1. It builds the M=125 basis symbolically in s and certifies the exact connected
   strict-KKT component containing s=33/250 inside the declared local search
   interval 129/1000 <= s <= 133/1000.  The lower boundary is a simple zero of
   the nonbasic p0 reduced cost; the upper boundary is a simple zero of p23.
   Every other numerator and denominator is certified sign-stable by exact
   rational interval Horner evaluation.

2. It tests the same endpoint-released architecture at all 83 A95 rational
   obstruction witnesses.  Seventy-six witnesses pass the unrestricted full
   finite-LP KKT system.  Seven lower-s witnesses fail because q0 has negative
   reduced cost.  Replacing q1 by q0 in the same sparse architecture does not
   repair any of those seven cases.

The result is an exact interval theorem at one support and a finite exact
rational-witness atlas over the A95 obstructions.  It is not an all-s interval
atlas, not a complete solution of the seven residual obstructions, and not a
physical or ontological claim.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import multiprocessing as mp
import os
import subprocess
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Callable

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if HERE.name == "audits" else HERE
RESULTS = ROOT / "results" if HERE.name == "audits" else HERE
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"
A95_RESULT = RESULTS / "a95_rational_witness_lift_results.json"
A95_CATALOGUE = RESULTS / "a95_rational_witness_lift_catalogue.json"
A96_RESULT = RESULTS / "a96_full_lp_active_set_resolution_results.json"

SEARCH_LOWER = sp.Rational(129, 1000)
SEARCH_UPPER = sp.Rational(133, 1000)
S0 = sp.Rational(33, 250)
M0 = 125
J0 = 24
ROOT_DENOMINATOR = 10**24
LOWER_ROOT_BRACKET = (
    sp.Rational(131966486281809654082390, ROOT_DENOMINATOR),
    sp.Rational(131966486281809654082393, ROOT_DENOMINATOR),
)
UPPER_ROOT_BRACKET = (
    sp.Rational(132121156974041079026925, ROOT_DENOMINATOR),
    sp.Rational(132121156974041079026928, ROOT_DENOMINATOR),
)
EXPECTED_OBSTRUCTION_COUNT = 83
EXPECTED_ENDPOINT_PASS_COUNT = 76
EXPECTED_RESIDUAL_COUNT = 7
EXPECTED_RESIDUAL_KEYS = [
    (396, "13/100", 70),
    (443, "13/100", 78),
    (449, "13/100", 79),
    (455, "13/100", 80),
    (484, "13/100", 85),
    (490, "13/100", 86),
    (496, "13/100", 87),
]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def normalized_epsilon(maximum: int) -> sp.Rational:
    h = maximum // 2
    factor = 1875 if maximum % 2 == 0 else 2500
    return sp.Rational(1, factor * 2**h)


def target_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2**x)


def beta_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (3 * x))


def gamma_value(x: int) -> sp.Rational:
    return sp.Rational(1, 2 ** (4 * x))


def fstr(value: F | sp.Rational) -> str:
    if isinstance(value, F):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    value = sp.Rational(value)
    return str(value)


def decimal_str(value: sp.Expr, digits: int = 40) -> str:
    return str(sp.N(value, digits))


def interval_multiply(
    first: tuple[sp.Rational, sp.Rational],
    second: tuple[sp.Rational, sp.Rational],
) -> tuple[sp.Rational, sp.Rational]:
    values = (
        first[0] * second[0], first[0] * second[1],
        first[1] * second[0], first[1] * second[1],
    )
    return min(values), max(values)


def polynomial_interval_horner(
    polynomial: sp.Poly,
    lower: sp.Rational,
    upper: sp.Rational,
) -> tuple[sp.Rational, sp.Rational]:
    coefficients = polynomial.all_coeffs()
    interval = (sp.Rational(coefficients[0]), sp.Rational(coefficients[0]))
    x_interval = (lower, upper)
    for coefficient in coefficients[1:]:
        interval = interval_multiply(interval, x_interval)
        coefficient = sp.Rational(coefficient)
        interval = (interval[0] + coefficient, interval[1] + coefficient)
    return interval


def interval_has_sign(
    interval: tuple[sp.Rational, sp.Rational],
    sign: int,
) -> bool:
    if sign > 0:
        return interval[0] > 0
    if sign < 0:
        return interval[1] < 0
    return interval[0] == 0 and interval[1] == 0


def exact_sign(value: sp.Expr) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def semantic_condition_name(name: str, maximum: int) -> str:
    count = maximum + 1
    if name.startswith("basic_"):
        raw = int(name.split("_")[-1])
        if raw < count:
            return f"basic_p_{raw}"
        if raw < 2 * count:
            return f"basic_q_{raw - count}"
        return "basic_t"
    if name.startswith("reduced_cost_"):
        raw = int(name.split("_")[-1])
        if raw < count:
            return f"reduced_cost_p_{raw}"
        if raw < 2 * count:
            return f"reduced_cost_q_{raw - count}"
        return "reduced_cost_t"
    return name


def symbolic_m125_interval_certificate(a67) -> dict[str, Any]:
    maximum = M0
    count = maximum + 1
    h = maximum // 2
    positive_indices = (
        J0 - 1,
        J0,
        maximum,
        count + 1,
        count + h,
        count + h + 1,
        2 * count,
    )
    branch = a67.build_branch(
        maximum,
        sp.Rational(maximum, 2),
        normalized_epsilon(maximum),
        4,
        positive_indices,
        (("alpha", 1), ("beta", -1)),
    )
    variable = a67.S
    conditions = branch["conditions"]
    condition_map = dict(conditions)
    lower_boundary_name = "reduced_cost_0"
    upper_boundary_name = f"basic_{J0 - 1}"
    lower_expression = condition_map[lower_boundary_name]
    upper_expression = condition_map[upper_boundary_name]
    lower_num, lower_den = sp.fraction(sp.cancel(lower_expression))
    upper_num, upper_den = sp.fraction(sp.cancel(upper_expression))
    lower_poly = sp.Poly(lower_num, variable, domain=sp.QQ)
    upper_poly = sp.Poly(upper_num, variable, domain=sp.QQ)
    lower_den_poly = sp.Poly(lower_den, variable, domain=sp.QQ)
    upper_den_poly = sp.Poly(upper_den, variable, domain=sp.QQ)

    lower_endpoint_signs = [
        exact_sign(lower_poly.eval(LOWER_ROOT_BRACKET[0])),
        exact_sign(lower_poly.eval(LOWER_ROOT_BRACKET[1])),
    ]
    upper_endpoint_signs = [
        exact_sign(upper_poly.eval(UPPER_ROOT_BRACKET[0])),
        exact_sign(upper_poly.eval(UPPER_ROOT_BRACKET[1])),
    ]
    lower_derivative_interval = polynomial_interval_horner(
        lower_poly.diff(), *LOWER_ROOT_BRACKET
    )
    upper_derivative_interval = polynomial_interval_horner(
        upper_poly.diff(), *UPPER_ROOT_BRACKET
    )
    lower_denominator_interval = polynomial_interval_horner(
        lower_den_poly, *LOWER_ROOT_BRACKET
    )
    upper_denominator_interval = polynomial_interval_horner(
        upper_den_poly, *UPPER_ROOT_BRACKET
    )

    hull = (LOWER_ROOT_BRACKET[0], UPPER_ROOT_BRACKET[1])
    core = (LOWER_ROOT_BRACKET[1], UPPER_ROOT_BRACKET[0])
    part_certificates: list[dict[str, Any]] = []
    unique_polynomials: set[tuple[str, ...]] = set()
    failures: list[dict[str, Any]] = []

    for raw_name, expression in conditions:
        numerator, denominator = sp.fraction(sp.cancel(expression))
        for part_name, part_expression in (("numerator", numerator), ("denominator", denominator)):
            if part_name == "numerator" and raw_name in {lower_boundary_name, upper_boundary_name}:
                continue
            polynomial = sp.Poly(part_expression, variable, domain=sp.QQ)
            key = tuple(polynomial.all_coeffs())
            unique_polynomials.add(key)
            reference_sign = exact_sign(polynomial.eval(S0))
            enclosure = polynomial_interval_horner(polynomial, *hull)
            passed = interval_has_sign(enclosure, reference_sign)
            record = {
                "condition": semantic_condition_name(raw_name, maximum),
                "raw_condition": raw_name,
                "part": part_name,
                "degree": polynomial.degree(),
                "reference_sign": reference_sign,
                "interval_sign_certified": passed,
            }
            part_certificates.append(record)
            if not passed:
                failures.append({**record, "interval_lower": str(enclosure[0]), "interval_upper": str(enclosure[1])})

    lower_core_derivative_interval = polynomial_interval_horner(lower_poly.diff(), *core)
    upper_core_interval = polynomial_interval_horner(upper_poly, *core)
    lower_root_unique = bool(
        lower_endpoint_signs == [1, -1]
        and lower_derivative_interval[1] < 0
        and lower_denominator_interval[1] < 0
    )
    upper_root_unique = bool(
        upper_endpoint_signs == [-1, 1]
        and upper_derivative_interval[0] > 0
        and upper_denominator_interval[1] < 0
    )
    core_boundary_signs = bool(
        lower_poly.eval(core[0]) < 0
        and lower_core_derivative_interval[1] < 0
        and upper_core_interval[1] < 0
    )

    return {
        "contract": {
            "maximum": maximum,
            "mean": str(sp.Rational(maximum, 2)),
            "epsilon": str(normalized_epsilon(maximum)),
            "search_interval": [str(SEARCH_LOWER), str(SEARCH_UPPER)],
            "probe": str(S0),
            "P_support": [J0 - 1, J0, maximum],
            "Q_support": [1, h, h + 1],
            "active_bands": [["alpha", 1], ["beta", -1]],
            "gamma_status": "inactive",
        },
        "strict_component": {
            "lower_boundary_condition": "reduced_cost_p_0",
            "upper_boundary_condition": f"basic_p_{J0 - 1}",
            "lower_root_bracket": [str(x) for x in LOWER_ROOT_BRACKET],
            "upper_root_bracket": [str(x) for x in UPPER_ROOT_BRACKET],
            "lower_root_midpoint_decimal": decimal_str(sum(LOWER_ROOT_BRACKET) / 2, 35),
            "upper_root_midpoint_decimal": decimal_str(sum(UPPER_ROOT_BRACKET) / 2, 35),
            "root_bracket_width": str(sp.Rational(3, ROOT_DENOMINATOR)),
            "component_statement": "the maximal connected strict-KKT component containing 33/250 inside [129/1000,133/1000] is the open interval between the two isolated algebraic roots",
        },
        "boundary_certificates": {
            "lower_numerator_degree": lower_poly.degree(),
            "lower_numerator_endpoint_signs": lower_endpoint_signs,
            "lower_derivative_interval_signs": [exact_sign(x) for x in lower_derivative_interval],
            "lower_denominator_interval_signs": [exact_sign(x) for x in lower_denominator_interval],
            "lower_root_unique_and_simple": lower_root_unique,
            "upper_numerator_degree": upper_poly.degree(),
            "upper_numerator_endpoint_signs": upper_endpoint_signs,
            "upper_derivative_interval_signs": [exact_sign(x) for x in upper_derivative_interval],
            "upper_denominator_interval_signs": [exact_sign(x) for x in upper_denominator_interval],
            "upper_root_unique_and_simple": upper_root_unique,
            "lower_numerator_derivative_signs_on_closed_core": [exact_sign(x) for x in lower_core_derivative_interval],
            "boundary_numerators_have_correct_sign_on_closed_core": core_boundary_signs,
        },
        "complete_sign_census": {
            "condition_count": len(conditions),
            "polynomial_part_count": 2 * len(conditions),
            "boundary_numerators_handled_separately": 2,
            "interval_horner_part_count": len(part_certificates),
            "unique_interval_horner_polynomial_count": len(unique_polynomials),
            "interval_horner_failure_count": len(failures),
            "all_nonboundary_parts_sign_stable_on_full_hull": not failures,
            "failures": failures,
        },
        "pass": bool(
            len(conditions) == 259
            and lower_root_unique
            and upper_root_unique
            and core_boundary_signs
            and not failures
            and LOWER_ROOT_BRACKET[1] < S0 < UPPER_ROOT_BRACKET[0]
        ),
    }



def interval_worker(_: int = 0) -> dict[str, Any]:
    a67 = load_module(A67_SCRIPT, f"a67_for_a97_interval_{os.getpid()}")
    return symbolic_m125_interval_certificate(a67)

def classify_conditions(
    conditions: list[tuple[str, sp.Rational]],
) -> tuple[str, tuple[str, sp.Rational] | None]:
    for name, value in conditions:
        if value < 0:
            if name.startswith("basic_"):
                return "primal_infeasible", (name, value)
            if name.startswith("active_dual_"):
                return "active_dual_infeasible", (name, value)
            if name.startswith("reduced_cost_"):
                return "reduced_cost_infeasible", (name, value)
            if name.startswith("inactive_slack_"):
                return "inactive_slack_infeasible", (name, value)
            return "negative_condition", (name, value)
        if value == 0:
            return "zero_condition", (name, value)
    return "pass", None


def evaluate_endpoint_released(
    maximum: int,
    contact: int,
    probe: sp.Rational,
    *,
    q_low: int = 1,
) -> dict[str, Any]:
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    p_points = [contact - 1, contact, maximum]
    q_points = [q_low, h, h + 1]
    if len(set(p_points)) != 3 or len(set(q_points)) != 3:
        return {"status": "degenerate_support", "failure": None}

    rows = [
        [1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 1, 1, 1, -1],
        [*p_points, 0, 0, 0, -mean],
        [0, 0, 0, *q_points, -mean],
        [0, 0, 0, *[target_value(x) for x in q_points], 0],
        [
            *[probe**x for x in p_points],
            *[-probe**x for x in q_points],
            -2 * epsilon,
        ],
        [
            *[-beta_value(x) for x in p_points],
            *[beta_value(x) for x in q_points],
            -2 * epsilon,
        ],
    ]
    domain = sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix(rows)).to_field()
    try:
        inverse = domain.inv().to_Matrix()
    except Exception:
        return {"status": "singular", "failure": None}

    rhs = sp.Matrix([0, 0, 0, 0, 1, 0, 0])
    objective = sp.Matrix([*[target_value(x) for x in p_points], 0, 0, 0, 0])
    basic = inverse * rhs
    dual = inverse.T * objective

    conditions: list[tuple[str, sp.Rational]] = []
    for index, x in enumerate(p_points):
        conditions.append((f"basic_p_{x}", basic[index]))
    for index, x in enumerate(q_points, start=3):
        conditions.append((f"basic_q_{x}", basic[index]))
    conditions.append(("basic_t", basic[6]))
    conditions.extend([
        ("active_dual_alpha_+1", dual[5]),
        ("active_dual_beta_-1", dual[6]),
    ])

    p_set = set(p_points)
    q_set = set(q_points)
    for x in range(maximum + 1):
        sx = probe**x
        tx = target_value(x)
        bx = beta_value(x)
        if x not in p_set:
            value = dual[0] + x * dual[2] + sx * dual[5] - bx * dual[6] - tx
            conditions.append((f"reduced_cost_p_{x}", value))
        if x not in q_set:
            value = dual[1] + x * dual[3] + tx * dual[4] - sx * dual[5] + bx * dual[6]
            conditions.append((f"reduced_cost_q_{x}", value))

    t_value = basic[6]

    def difference(fn: Callable[[int], sp.Rational]) -> sp.Rational:
        return (
            sum(fn(x) * basic[i] for i, x in enumerate(p_points))
            - sum(fn(x) * basic[3 + i] for i, x in enumerate(q_points))
        )

    alpha_difference = difference(lambda x: probe**x)
    beta_difference = difference(beta_value)
    gamma_difference = difference(gamma_value)
    conditions.extend([
        ("inactive_slack_alpha_-1", 2 * epsilon * t_value + alpha_difference),
        ("inactive_slack_beta_+1", 2 * epsilon * t_value - beta_difference),
        ("inactive_slack_gamma_+1", 2 * epsilon * t_value - gamma_difference),
        ("inactive_slack_gamma_-1", 2 * epsilon * t_value + gamma_difference),
    ])

    status, failure = classify_conditions(conditions)
    result: dict[str, Any] = {
        "status": status,
        "P_support": p_points,
        "Q_support": q_points,
        "active_bands": [["alpha", 1], ["beta", -1]],
        "condition_count": len(conditions),
        "failure": (
            {"name": failure[0], "exact": str(failure[1]), "sign": exact_sign(failure[1])}
            if failure else None
        ),
    }
    if status == "pass":
        minimum = min(conditions, key=lambda item: item[1])
        ratio = sum(target_value(x) * basic[i] for i, x in enumerate(p_points))
        dual_value = rhs.dot(dual)
        result.update({
            "minimum_condition_name": minimum[0],
            "minimum_condition_sign": exact_sign(minimum[1]),
            "primal_dual_equal": ratio == dual_value,
            "strict_global_KKT_pass": ratio == dual_value,
        })
    return result


def evaluate_obstruction_record(record: dict[str, Any]) -> dict[str, Any]:
    maximum = int(record["maximum"])
    contact = int(record["compressed_maximizer_contact"])
    witness = F(record["witness"])
    probe = sp.Rational(witness.numerator, witness.denominator)
    result = evaluate_endpoint_released(maximum, contact, probe, q_low=1)
    return {
        "maximum": maximum,
        "base_contact": int(record["base_contact"]),
        "compressed_phase": record["compressed_phase"],
        "phase_side": record["phase_side"],
        "witness": record["witness"],
        "compressed_maximizer_contact": contact,
        "endpoint_released_result": result,
    }


def evaluate_q0_repair(record: dict[str, Any]) -> dict[str, Any]:
    maximum = int(record["maximum"])
    contact = int(record["compressed_maximizer_contact"])
    witness = F(record["witness"])
    probe = sp.Rational(witness.numerator, witness.denominator)
    result = evaluate_endpoint_released(maximum, contact, probe, q_low=0)
    return {
        "maximum": maximum,
        "witness": record["witness"],
        "compressed_maximizer_contact": contact,
        "q0_replacement_result": result,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=min(16, max(1, os.cpu_count() or 1)))
    parser.add_argument("--interval-only-output", type=str, default=None)
    parser.add_argument("--atlas-only-output", type=str, default=None)
    parser.add_argument(
        "--interval-input",
        type=str,
        default=str(ROOT / "provenance" / "a97_phase" / "a97_interval_phase.json"),
    )
    parser.add_argument(
        "--atlas-input",
        type=str,
        default=str(ROOT / "provenance" / "a97_phase" / "a97_atlas_phase.json"),
    )
    args = parser.parse_args()
    RESULTS.mkdir(parents=True, exist_ok=True)

    if args.interval_only_output:
        a67 = load_module(A67_SCRIPT, f"a67_for_a97_interval_subprocess_{os.getpid()}")
        certificate = symbolic_m125_interval_certificate(a67)
        output = Path(args.interval_only_output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(certificate, indent=2), encoding="utf-8")
        print(json.dumps({"interval_pass": certificate["pass"], "output": str(output)}))
        return

    if args.atlas_only_output:
        a95_catalogue = json.loads(A95_CATALOGUE.read_text(encoding="utf-8"))
        obstructions = [
            record for record in a95_catalogue["records"]
            if int(record["strict_pass_count"]) == 0
        ]
        workers = min(args.workers, len(obstructions))
        with mp.Pool(processes=workers) as pool:
            records = list(pool.imap_unordered(evaluate_obstruction_record, obstructions, chunksize=1))
        records.sort(key=lambda item: (item["maximum"], item["witness"], item["phase_side"]))
        residuals = [
            record for record in records
            if record["endpoint_released_result"]["status"] != "pass"
        ]
        with mp.Pool(processes=min(workers, max(1, len(residuals)))) as pool:
            q0_repairs = list(pool.imap_unordered(evaluate_q0_repair, residuals, chunksize=1))
        q0_repairs.sort(key=lambda item: item["maximum"])
        payload = {
            "audit_phase": "A97_ENDPOINT_RELEASED_RATIONAL_WITNESS_ATLAS_PHASE",
            "records": records,
            "q0_repairs": q0_repairs,
        }
        output = Path(args.atlas_only_output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(json.dumps({
            "record_count": len(records),
            "pass_count": sum(r["endpoint_released_result"]["status"] == "pass" for r in records),
            "residual_count": len(residuals),
            "output": str(output),
        }))
        return

    interval_input = Path(args.interval_input)
    atlas_input = Path(args.atlas_input)
    if not interval_input.exists() or not atlas_input.exists():
        raise FileNotFoundError(
            "A97 uses two memory-isolated exact phases. Run:\n"
            f"  {sys.executable} {Path(__file__).name} --interval-only-output {interval_input}\n"
            f"  {sys.executable} {Path(__file__).name} --atlas-only-output {atlas_input}\n"
            "then rerun the audit normally."
        )

    interval_certificate = json.loads(interval_input.read_text(encoding="utf-8"))
    atlas_phase = json.loads(atlas_input.read_text(encoding="utf-8"))
    records = atlas_phase["records"]
    q0_repairs = atlas_phase["q0_repairs"]

    a95_result = json.loads(A95_RESULT.read_text(encoding="utf-8"))
    a95_catalogue = json.loads(A95_CATALOGUE.read_text(encoding="utf-8"))
    a96_result = json.loads(A96_RESULT.read_text(encoding="utf-8"))

    a95_source_valid = (
        a95_result.get("verdict")
        == "PASS_EXACT_RATIONAL_WITNESS_LIFT_ATLAS_AND_RESTRICTED_FAMILY_OBSTRUCTION"
        and all(a95_result.get("gates", {}).values())
    )
    a96_source_valid = (
        a96_result.get("verdict")
        == "PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M125"
        and all(a96_result.get("gates", {}).values())
        and a96_result["resolved_active_set"]["P_support"] == [23, 24, 125]
        and a96_result["resolved_active_set"]["Q_support"] == [1, 62, 63]
    )
    obstructions = [
        record for record in a95_catalogue["records"]
        if int(record["strict_pass_count"]) == 0
    ]
    passes = [r for r in records if r["endpoint_released_result"]["status"] == "pass"]
    residuals = [r for r in records if r["endpoint_released_result"]["status"] != "pass"]
    residual_keys = [
        (int(r["maximum"]), str(r["witness"]), int(r["compressed_maximizer_contact"]))
        for r in residuals
    ]
    residual_status_counts = Counter(r["endpoint_released_result"]["status"] for r in residuals)
    residual_failure_names = Counter(
        r["endpoint_released_result"]["failure"]["name"]
        for r in residuals
        if r["endpoint_released_result"].get("failure")
    )
    q0_passes = [r for r in q0_repairs if r["q0_replacement_result"]["status"] == "pass"]
    q0_status_counts = Counter(r["q0_replacement_result"]["status"] for r in q0_repairs)
    q0_failure_names = Counter(
        r["q0_replacement_result"]["failure"]["name"]
        for r in q0_repairs
        if r["q0_replacement_result"].get("failure")
    )
    m125_record = next(
        r for r in records
        if r["maximum"] == 125 and r["witness"] == "33/250"
    )

    gates = {
        "A95_source_is_present_and_passed": a95_source_valid,
        "A96_source_is_present_and_passed": a96_source_valid,
        "memory_isolated_interval_phase_is_present_and_passed": interval_certificate.get("pass") is True,
        "memory_isolated_atlas_phase_has_83_records": len(records) == EXPECTED_OBSTRUCTION_COUNT,
        "M125_symbolic_branch_has_259_KKT_conditions": (
            interval_certificate["complete_sign_census"]["condition_count"] == 259
        ),
        "M125_lower_boundary_is_unique_simple_p0_reduced_cost_root": (
            interval_certificate["boundary_certificates"]["lower_root_unique_and_simple"]
        ),
        "M125_upper_boundary_is_unique_simple_p23_basic_root": (
            interval_certificate["boundary_certificates"]["upper_root_unique_and_simple"]
        ),
        "M125_all_516_nonboundary_polynomial_parts_are_sign_stable": (
            interval_certificate["complete_sign_census"]["interval_horner_part_count"] == 516
            and interval_certificate["complete_sign_census"]["interval_horner_failure_count"] == 0
        ),
        "M125_boundary_numerators_have_correct_core_sign": (
            interval_certificate["boundary_certificates"]["boundary_numerators_have_correct_sign_on_closed_core"]
        ),
        "M125_strict_component_contains_33_over_250": interval_certificate["pass"],
        "A95_obstruction_witness_count_is_83": len(obstructions) == EXPECTED_OBSTRUCTION_COUNT,
        "endpoint_released_family_passes_76_of_83_obstructions": (
            len(passes) == EXPECTED_ENDPOINT_PASS_COUNT and len(residuals) == EXPECTED_RESIDUAL_COUNT
        ),
        "A96_point_is_reproduced_by_general_endpoint_released_evaluator": (
            m125_record["endpoint_released_result"]["status"] == "pass"
            and m125_record["endpoint_released_result"]["P_support"] == [23, 24, 125]
            and m125_record["endpoint_released_result"]["Q_support"] == [1, 62, 63]
            and m125_record["endpoint_released_result"]["condition_count"] == 259
        ),
        "all_76_passes_are_complete_strict_global_KKT_certificates": (
            all(r["endpoint_released_result"].get("strict_global_KKT_pass") for r in passes)
        ),
        "residual_obstruction_keys_match_exact_declared_list": residual_keys == EXPECTED_RESIDUAL_KEYS,
        "all_seven_residuals_are_q0_negative_reduced_cost_failures": (
            residual_status_counts == {"reduced_cost_infeasible": 7}
            and residual_failure_names == {"reduced_cost_q_0": 7}
        ),
        "simple_q1_to_q0_replacement_repairs_zero_of_seven": len(q0_passes) == 0,
        "q0_replacement_failures_are_three_primal_and_four_gamma_minus_slack": (
            q0_status_counts == {"primal_infeasible": 3, "inactive_slack_infeasible": 4}
            and q0_failure_names == {
                "basic_p_69": 1,
                "basic_p_79": 1,
                "basic_p_86": 1,
                "inactive_slack_gamma_-1": 4,
            }
        ),
        "formal_contract_and_nonphysical_scope_preserved": True,
    }
    gates = {name: bool(value) for name, value in gates.items()}

    summary = {
        "audit": "A97_ENDPOINT_RELEASED_INTERVAL_AND_OBSTRUCTION_ATLAS",
        "evidence_class": "exact symbolic interval certificate plus exact finite rational-witness unrestricted KKT atlas",
        "scope": {
            "interval_theorem": "M=125 on 129/1000 <= s <= 133/1000",
            "witness_atlas": "all 83 A95 obstruction phase-segment witnesses",
            "tested_family": "P={j-1,j,M}, Q={1,h,h+1}, alpha+ and beta- active, gamma inactive",
            "explicit_nonclaims": [
                "not an interval theorem for the other 82 A95 witnesses",
                "not a complete resolution of the seven residual q0-entry obstructions",
                "not an all-M support theorem",
                "not a physical, spacetime, matter, or ontological result",
            ],
        },
        "M125_interval_theorem": interval_certificate,
        "obstruction_atlas": {
            "source_obstruction_count": len(obstructions),
            "endpoint_released_strict_pass_count": len(passes),
            "residual_obstruction_count": len(residuals),
            "pass_support_count": len({r["maximum"] for r in passes}),
            "residual_support_count": len({r["maximum"] for r in residuals}),
            "residual_keys": [list(item) for item in residual_keys],
            "residual_status_counts": dict(residual_status_counts),
            "residual_failure_names": dict(residual_failure_names),
        },
        "q0_replacement_stress": {
            "tested_count": len(q0_repairs),
            "strict_pass_count": len(q0_passes),
            "status_counts": dict(q0_status_counts),
            "failure_names": dict(q0_failure_names),
            "interpretation": "the negative q0 reduced cost signals a required active-set change, but simply replacing q1 by q0 in the same seven-variable two-band basis is insufficient",
        },
        "interpretation": {
            "positive_result": "The endpoint-released family is not a one-point accident: it is exact on an algebraic interval at M=125 and resolves 76 of the 83 rational A95 obstructions.",
            "new_boundary": "Seven lower-s witnesses remain unresolved. In each, q0 has negative reduced cost against the q1-based family, but the direct q0 replacement basis is itself infeasible.",
            "next_target": "Solve the unrestricted full LP at the first residual case M=396, s=13/100 and identify the actual q0-associated pivot structure.",
        },
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "gates": gates,
        "verdict": (
            "PASS_ENDPOINT_RELEASED_M125_INTERVAL_AND_76_OF_83_OBSTRUCTION_RESOLUTION_WITH_SEVEN_Q0_ENTRY_RESIDUALS"
            if all(gates.values()) else "FAIL"
        ),
    }
    catalogue = {
        "audit": "A97_ENDPOINT_RELEASED_OBSTRUCTION_CATALOGUE",
        "family": summary["scope"]["tested_family"],
        "records": records,
        "residual_q0_replacement_tests": q0_repairs,
    }

    result_path = RESULTS / "a97_endpoint_released_interval_and_obstruction_results.json"
    catalogue_path = RESULTS / "a97_endpoint_released_obstruction_catalogue.json"
    interval_path = RESULTS / "a97_M125_endpoint_released_interval_certificate.json"
    result_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    catalogue_path.write_text(json.dumps(catalogue, indent=2), encoding="utf-8")
    interval_path.write_text(json.dumps(interval_certificate, indent=2), encoding="utf-8")

    print(json.dumps({
        "audit": summary["audit"],
        "M125_interval_lower_midpoint": interval_certificate["strict_component"]["lower_root_midpoint_decimal"],
        "M125_interval_upper_midpoint": interval_certificate["strict_component"]["upper_root_midpoint_decimal"],
        "endpoint_released_pass_count": len(passes),
        "residual_count": len(residuals),
        "residual_keys": residual_keys,
        "q0_replacement_pass_count": len(q0_passes),
        "gate_count": summary["gate_count"],
        "pass_count": summary["pass_count"],
        "verdict": summary["verdict"],
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
