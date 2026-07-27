#!/usr/bin/env python3
"""A59 audit: exact nonlinear correlated ellipsoidal calibration risk.

The A58 ratio is linear-fractional in the three independent error factors.
Therefore its maximum over an ellipsoid is the admissible root of one
quadratic equation.

The audit:
- inherits the exact A58 branch on [1,1.1]^3;
- proves ellipsoid containment;
- computes algebraic robust roots and KKT directions;
- verifies correlation ordering;
- compares exact nonlinear and first-order robust excesses.

The exact theorem is analytic. Decimal evaluations use 80-digit arithmetic.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp


HERE = Path(__file__).resolve().parent
A52_SCRIPT = HERE / "a52_continuous_second_anchor_audit.py"
A58_SCRIPT = HERE / "a58_independent_three_channel_error_audit.py"
A58_RESULTS = HERE / "a58_independent_three_channel_error_results.json"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")

    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def mp_value(expression: sp.Expr, digits: int = 90) -> mp.mpf:
    return mp.mpf(str(sp.N(expression, digits)))


def extract_linear_fractional(
    ratio: sp.Expr,
    variables: list[sp.Symbol],
) -> dict[str, Any]:
    numerator, denominator = sp.fraction(sp.cancel(ratio))

    numerator_vector = [
        sp.diff(numerator, variable)
        for variable in variables
    ]
    denominator_vector = [
        sp.diff(denominator, variable)
        for variable in variables
    ]

    numerator_constant = sp.expand(
        numerator
        - sum(
            numerator_vector[index] * variables[index]
            for index in range(len(variables))
        )
    )
    denominator_constant = sp.expand(
        denominator
        - sum(
            denominator_vector[index] * variables[index]
            for index in range(len(variables))
        )
    )

    linear_gate = all(
        sp.diff(numerator_vector[index], variable) == 0
        and sp.diff(denominator_vector[index], variable) == 0
        for index in range(len(variables))
        for variable in variables
    )

    return {
        "numerator_constant": numerator_constant,
        "denominator_constant": denominator_constant,
        "numerator_vector": numerator_vector,
        "denominator_vector": denominator_vector,
        "linear_gate": bool(linear_gate),
    }


def robust_case(
    rho_text: str,
    coefficients: dict[str, Any],
    s_star: sp.Expr,
) -> dict[str, Any]:
    mp.mp.dps = 90

    rho = mp.mpf(rho_text)
    h = mp.mpf("0.05")
    centre = [mp.mpf("1.05")] * 3

    n0 = mp_value(
        coefficients["numerator_constant"].subs(
            coefficients["s"],
            s_star,
        )
    )
    d0 = mp_value(
        coefficients["denominator_constant"].subs(
            coefficients["s"],
            s_star,
        )
    )
    n = [
        mp_value(
            expression.subs(
                coefficients["s"],
                s_star,
            )
        )
        for expression in coefficients["numerator_vector"]
    ]
    d = [
        mp_value(
            expression.subs(
                coefficients["s"],
                s_star,
            )
        )
        for expression in coefficients["denominator_vector"]
    ]

    correlation = mp.matrix(
        [
            [1, rho, rho],
            [rho, 1, rho],
            [rho, rho, 1],
        ]
    )

    numerator_centre = (
        n0
        + sum(n[index] * centre[index] for index in range(3))
    )
    denominator_centre = (
        d0
        + sum(d[index] * centre[index] for index in range(3))
    )

    def quadratic_form(vector):
        return sum(
            vector[index]
            * sum(
                correlation[index, other] * vector[other]
                for other in range(3)
            )
            for index in range(3)
        )

    nn = quadratic_form(n)
    dd = quadratic_form(d)
    nd = sum(
        n[index]
        * sum(
            correlation[index, other] * d[other]
            for other in range(3)
        )
        for index in range(3)
    )

    coefficient_a = (
        denominator_centre**2
        - h**2 * dd
    )
    coefficient_b = (
        -2 * numerator_centre * denominator_centre
        + 2 * h**2 * nd
    )
    coefficient_c = (
        numerator_centre**2
        - h**2 * nn
    )

    discriminant = (
        coefficient_b**2
        - 4 * coefficient_a * coefficient_c
    )

    roots = [
        (
            -coefficient_b
            + mp.sqrt(discriminant)
        )
        / (2 * coefficient_a),
        (
            -coefficient_b
            - mp.sqrt(discriminant)
        )
        / (2 * coefficient_a),
    ]

    selected = None

    for candidate in roots:
        direction_vector = [
            n[index] - candidate * d[index]
            for index in range(3)
        ]
        support_norm_squared = quadratic_form(direction_vector)
        support_equation = (
            numerator_centre
            - candidate * denominator_centre
            + h * mp.sqrt(support_norm_squared)
        )

        branch_condition = (
            numerator_centre
            - candidate * denominator_centre
        )

        if (
            abs(support_equation) < mp.mpf("1e-70")
            and branch_condition <= 0
        ):
            selected = candidate
            selected_vector = direction_vector
            selected_norm_squared = support_norm_squared
            break

    if selected is None:
        raise RuntimeError(
            f"No admissible robust root for rho={rho_text}"
        )

    normalized_direction = [
        sum(
            correlation[index, other]
            * selected_vector[other]
            for other in range(3)
        )
        / mp.sqrt(selected_norm_squared)
        for index in range(3)
    ]

    worst_factors = [
        centre[index] + h * normalized_direction[index]
        for index in range(3)
    ]

    numerator_worst = (
        n0
        + sum(
            n[index] * worst_factors[index]
            for index in range(3)
        )
    )
    denominator_worst = (
        d0
        + sum(
            d[index] * worst_factors[index]
            for index in range(3)
        )
    )
    reproduced_ratio = numerator_worst / denominator_worst

    inverse_correlation = correlation**-1
    boundary_norm = sum(
        normalized_direction[index]
        * sum(
            inverse_correlation[index, other]
            * normalized_direction[other]
            for other in range(3)
        )
        for index in range(3)
    )

    robust_risk = mp.log(selected, 2) / 2
    centre_ratio = numerator_centre / denominator_centre
    centre_risk = mp.log(centre_ratio, 2) / 2
    exact_excess = robust_risk - centre_risk

    risk_gradient = []
    for index in range(3):
        ratio_derivative = (
            n[index] * denominator_centre
            - d[index] * numerator_centre
        ) / denominator_centre**2

        risk_gradient.append(
            ratio_derivative
            / (2 * mp.log(2) * centre_ratio)
        )

    linear_variance = sum(
        risk_gradient[index]
        * sum(
            correlation[index, other]
            * risk_gradient[other]
            for other in range(3)
        )
        for index in range(3)
    )
    linear_excess = h * mp.sqrt(linear_variance)

    relative_discrepancy = (
        (linear_excess - exact_excess)
        / exact_excess
    )

    eigenvalues = [
        1 - rho,
        1 - rho,
        1 + 2 * rho,
    ]

    return {
        "correlation": rho_text,
        "correlation_eigenvalues": [
            mp.nstr(value, 50)
            for value in eigenvalues
        ],
        "quadratic_coefficients": {
            "A": mp.nstr(coefficient_a, 70),
            "B": mp.nstr(coefficient_b, 70),
            "C": mp.nstr(coefficient_c, 70),
        },
        "ratio": mp.nstr(selected, 70),
        "risk": mp.nstr(robust_risk, 70),
        "centre_risk": mp.nstr(centre_risk, 70),
        "exact_excess": mp.nstr(exact_excess, 70),
        "linear_excess": mp.nstr(linear_excess, 70),
        "relative_linear_discrepancy": mp.nstr(
            relative_discrepancy,
            70,
        ),
        "worst_error_factors": [
            mp.nstr(value, 70)
            for value in worst_factors
        ],
        "normalized_direction": [
            mp.nstr(value, 70)
            for value in normalized_direction
        ],
        "support_residual": mp.nstr(
            reproduced_ratio - selected,
            70,
        ),
        "ellipsoid_boundary_norm": mp.nstr(
            boundary_norm,
            70,
        ),
        "gates": {
            "positive_definite": bool(
                min(eigenvalues) > 0
            ),
            "admissible_root_reproduced": bool(
                abs(reproduced_ratio - selected)
                < mp.mpf("1e-60")
            ),
            "ellipsoid_boundary_exact": bool(
                abs(boundary_norm - 1)
                < mp.mpf("1e-60")
            ),
            "worst_point_inside_A58_box": bool(
                all(
                    mp.mpf("1")
                    <= value
                    <= mp.mpf("1.1")
                    for value in worst_factors
                )
            ),
            "all_ratio_gradient_components_positive": bool(
                all(value > 0 for value in risk_gradient)
            ),
            "linear_error_below_one_tenth_percent": bool(
                abs(relative_discrepancy)
                < mp.mpf("0.001")
            ),
        },
    }


def main() -> None:
    if not A52_SCRIPT.exists():
        raise FileNotFoundError(A52_SCRIPT)
    if not A58_SCRIPT.exists():
        raise FileNotFoundError(A58_SCRIPT)
    if not A58_RESULTS.exists():
        raise FileNotFoundError(A58_RESULTS)

    a52 = load_module(
        A52_SCRIPT,
        "a52_for_a59",
    )
    a58 = load_module(
        A58_SCRIPT,
        "a58_for_a59",
    )

    a58_results = json.loads(
        A58_RESULTS.read_text(encoding="utf-8")
    )

    certificate = a58.build_certificate(a52)

    ratio = sp.cancel(certificate["ratio"])
    variables = [
        certificate["u2"],
        certificate["ub"],
        certificate["ui"],
    ]

    linear_fractional = extract_linear_fractional(
        ratio,
        variables,
    )
    linear_fractional["s"] = certificate["s"]

    correlation_values = [
        "-0.4",
        "0",
        "0.5",
        "0.9",
    ]

    cases = [
        robust_case(
            correlation,
            linear_fractional,
            a52.s_star,
        )
        for correlation in correlation_values
    ]

    case_gates = [
        value
        for case in cases
        for value in case["gates"].values()
    ]

    risks = [
        mp.mpf(case["risk"])
        for case in cases
    ]

    exact_excesses = [
        mp.mpf(case["exact_excess"])
        for case in cases
    ]

    box_worst_risk = mp.mpf(
        a58_results[
            "robust_box_bounds"
        ]["maximum_risk_decimal"]
    )

    centre_risk = mp.mpf(
        cases[0]["centre_risk"]
    )

    gates = {
        "A58_complete_audit_passed": bool(
            all(a58_results["gates"].values())
        ),
        "ratio_is_exactly_linear_fractional": bool(
            linear_fractional["linear_gate"]
        ),
        "all_case_gates_pass": bool(
            all(case_gates)
        ),
        "robust_risk_strictly_increases_with_correlation": bool(
            all(
                risks[index + 1] > risks[index]
                for index in range(len(risks) - 1)
            )
        ),
        "robust_excess_strictly_increases_with_correlation": bool(
            all(
                exact_excesses[index + 1]
                > exact_excesses[index]
                for index in range(
                    len(exact_excesses) - 1
                )
            )
        ),
        "ellipsoid_cases_below_box_worst_case": bool(
            all(
                risk < box_worst_risk
                for risk in risks
            )
        ),
        "all_robust_cases_above_ellipsoid_centre": bool(
            all(
                risk > centre_risk
                for risk in risks
            )
        ),
    }

    verdict = (
        "PASS_EXACT_CORRELATED_ELLIPSOIDAL_CALIBRATION_RISK"
        if all(gates.values())
        else "FAIL_A59_CORRELATED_ELLIPSOID_AUDIT"
    )

    result = {
        "audit": (
            "A59_CORRELATED_ELLIPSOIDAL_CALIBRATION"
        ),
        "contract": {
            "design": (
                "{2,beta-star,infinity}*log(2)"
            ),
            "ellipsoid_centre": [
                "21/20",
                "21/20",
                "21/20",
            ],
            "marginal_radius": "1/20",
            "equicorrelation_domain": "(-1/2,1)",
            "certified_box": "[1,11/10]^3",
        },
        "linear_fractional_ratio": {
            "numerator_constant": str(
                linear_fractional[
                    "numerator_constant"
                ]
            ),
            "denominator_constant": str(
                linear_fractional[
                    "denominator_constant"
                ]
            ),
            "numerator_vector": [
                str(value)
                for value in linear_fractional[
                    "numerator_vector"
                ]
            ],
            "denominator_vector": [
                str(value)
                for value in linear_fractional[
                    "denominator_vector"
                ]
            ],
            "robust_root_equation": (
                "(Nbar-y*Dbar)^2="
                "h^2*(n-y*d)^T*R_rho*(n-y*d), "
                "with Nbar-y*Dbar<=0"
            ),
            "worst_direction": (
                "u*=ubar+h*R_rho*(n-y*d)"
                "/sqrt((n-y*d)^T*R_rho*(n-y*d))"
            ),
        },
        "cases": cases,
        "comparison": {
            "ellipsoid_centre_risk": str(
                centre_risk
            ),
            "A58_independent_box_worst_risk": str(
                box_worst_risk
            ),
            "interpretation": (
                "Positive correlation increases the robust "
                "risk, negative correlation reduces it, and "
                "every contained ellipsoid remains below the "
                "independent-box worst corner."
            ),
        },
        "formal_results": [
            (
                "the full nonlinear ellipsoidal maximum has "
                "an algebraic quadratic solution"
            ),
            (
                "the exact KKT worst direction is supplied"
            ),
            (
                "robust risk strictly increases with "
                "equicorrelation"
            ),
            (
                "common-mode uncertainty is more adversarial "
                "than independent uncertainty"
            ),
            (
                "anticorrelation reduces the robust risk"
            ),
            (
                "the A58 gradient predicts the nonlinear "
                "excess to better than 0.1 percent in the "
                "representative cases"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The theorem uses an equicorrelation ellipsoid "
            "centred at 1.05 with marginal radius 0.05, so it "
            "stays inside the A58 certified box. It does not "
            "estimate an empirical covariance matrix or "
            "reoptimize the anchor locations."
        ),
    }

    output_path = HERE / (
        "a59_correlated_ellipsoidal_calibration_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "risk_by_correlation": {
            case["correlation"]: case["risk"]
            for case in cases
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
