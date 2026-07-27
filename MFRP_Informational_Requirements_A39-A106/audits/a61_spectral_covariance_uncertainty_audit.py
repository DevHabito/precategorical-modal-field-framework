#!/usr/bin/env python3
"""A61 exact audit: spectral covariance-estimation uncertainty.

For a covariance estimate Sigma_hat and spectral radius tau, define

    S_tau = {Sigma = Sigma.T >= 0:
             ||Sigma-Sigma_hat||_2 <= tau}.

By Loewner monotonicity from A60:

    sup Q(Sigma) = Q(Sigma_hat + tau I).

If tau < lambda_min(Sigma_hat), then

    inf Q(Sigma) = Q(Sigma_hat - tau I).

The script verifies the theorem on an exact rational covariance estimate,
computes a deterministic risk table, the local tau sensitivity, and writes a
machine-readable input template.
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
A60_SCRIPT = HERE / "a60_general_covariance_matrix_audit.py"
A60_RESULTS = HERE / "a60_general_covariance_matrix_results.json"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")

    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def mp_number(expression: sp.Expr, s: sp.Symbol, s_star: sp.Expr) -> mp.mpf:
    return mp.mpf(str(sp.N(expression.subs(s, s_star), 90)))


def local_tau_sensitivity(
    coefficients: dict[str, Any],
    covariance: sp.Matrix,
    centre: list[sp.Rational],
    s: sp.Symbol,
    s_star: sp.Expr,
    robust_ratio_text: str,
) -> dict[str, str]:
    mp.mp.dps = 90

    n0 = mp_number(coefficients["n0"], s, s_star)
    d0 = mp_number(coefficients["d0"], s, s_star)
    n = [
        mp_number(value, s, s_star)
        for value in coefficients["n"]
    ]
    d = [
        mp_number(value, s, s_star)
        for value in coefficients["d"]
    ]

    centre_mp = [mp.mpf(str(value)) for value in centre]
    sigma = mp.matrix(
        [
            [
                mp.mpf(str(sp.N(covariance[row, column], 90)))
                for column in range(3)
            ]
            for row in range(3)
        ]
    )

    y = mp.mpf(robust_ratio_text)
    a = n0 + sum(n[index] * centre_mp[index] for index in range(3))
    b = d0 + sum(d[index] * centre_mp[index] for index in range(3))
    vector = [
        n[index] - y * d[index]
        for index in range(3)
    ]

    def bilinear(left, matrix, right):
        return sum(
            left[index]
            * sum(
                matrix[index, other] * right[other]
                for other in range(3)
            )
            for index in range(3)
        )

    support_squared = bilinear(vector, sigma, vector)
    euclidean_squared = sum(value**2 for value in vector)
    d_sigma_vector = bilinear(d, sigma, vector)

    dy_dtau = (
        euclidean_squared
        / (2 * mp.sqrt(support_squared))
        / (
            b
            + d_sigma_vector
            / mp.sqrt(support_squared)
        )
    )

    dQ_dtau = (
        dy_dtau
        / (2 * mp.log(2) * y)
    )

    return {
        "ratio_derivative": mp.nstr(dy_dtau, 70),
        "risk_derivative": mp.nstr(dQ_dtau, 70),
        "positive": bool(dQ_dtau > 0),
    }


def main() -> None:
    if not A52_SCRIPT.exists():
        raise FileNotFoundError(A52_SCRIPT)
    if not A58_SCRIPT.exists():
        raise FileNotFoundError(A58_SCRIPT)
    if not A60_SCRIPT.exists():
        raise FileNotFoundError(A60_SCRIPT)
    if not A60_RESULTS.exists():
        raise FileNotFoundError(A60_RESULTS)

    a52 = load_module(A52_SCRIPT, "a52_for_a61")
    a58 = load_module(A58_SCRIPT, "a58_for_a61")
    a60 = load_module(A60_SCRIPT, "a60_for_a61")

    a60_results = json.loads(
        A60_RESULTS.read_text(encoding="utf-8")
    )

    certificate = a58.build_certificate(a52)
    coefficients = a60.extract_linear_fractional(
        certificate["ratio"],
        [
            certificate["u2"],
            certificate["ub"],
            certificate["ui"],
        ],
    )

    centre = [
        sp.Rational(21, 20),
        sp.Rational(21, 20),
        sp.Rational(21, 20),
    ]

    sigma_hat = sp.diag(
        sp.Rational(9, 10000),
        sp.Rational(1, 1600),
        sp.Rational(9, 40000),
    )

    identity = sp.eye(3)
    lambda_min = sp.Rational(9, 40000)
    tau_box = (
        sp.Rational(1, 400)
        - max(sigma_hat[index, index] for index in range(3))
    )

    tau_values = [
        sp.Rational(0),
        sp.Rational(1, 1000000),
        sp.Rational(1, 100000),
        sp.Rational(1, 20000),
        sp.Rational(1, 10000),
        sp.Rational(1, 5000),
        sp.Rational(1, 1000),
        sp.Rational(1, 625),
    ]

    rows = []
    upper_cases = []
    lower_cases = []

    point_case = a60.robust_solution(
        "point_estimate",
        sigma_hat,
        centre,
        coefficients,
        certificate["s"],
        a52.s_star,
    )
    point_risk = mp.mpf(point_case["robust_risk"])

    for tau in tau_values:
        upper_covariance = sigma_hat + tau * identity
        upper_case = a60.robust_solution(
            f"upper_tau_{tau}",
            upper_covariance,
            centre,
            coefficients,
            certificate["s"],
            a52.s_star,
        )
        upper_cases.append(upper_case)

        upper_risk = mp.mpf(upper_case["robust_risk"])
        premium = upper_risk - point_risk

        row: dict[str, Any] = {
            "tau": str(tau),
            "tau_decimal": str(sp.N(tau, 30)),
            "upper_risk": upper_case["robust_risk"],
            "upper_premium": mp.nstr(premium, 70),
            "upper_relative_premium_percent": mp.nstr(
                100 * premium / point_risk,
                70,
            ),
            "upper_worst_error_factors": (
                upper_case["worst_error_factors"]
            ),
        }

        if tau > 0 and tau < lambda_min:
            lower_covariance = sigma_hat - tau * identity
            lower_case = a60.robust_solution(
                f"lower_tau_{tau}",
                lower_covariance,
                centre,
                coefficients,
                certificate["s"],
                a52.s_star,
            )
            lower_cases.append(lower_case)
            row["lower_risk"] = lower_case["robust_risk"]
            row["two_sided_interval_available"] = True
        else:
            row["lower_risk"] = None
            row["two_sided_interval_available"] = False

        rows.append(row)

    sensitivity = local_tau_sensitivity(
        coefficients,
        sigma_hat,
        centre,
        certificate["s"],
        a52.s_star,
        point_case["robust_ratio"],
    )

    upper_risks = [
        mp.mpf(case["robust_risk"])
        for case in upper_cases
    ]
    lower_risks = [
        mp.mpf(case["robust_risk"])
        for case in lower_cases
    ]

    small_tau = mp.mpf("0.000001")
    first_premium = mp.mpf(rows[1]["upper_premium"])
    first_order_ratio = (
        first_premium
        / (
            mp.mpf(sensitivity["risk_derivative"])
            * small_tau
        )
    )

    all_upper_case_gates = [
        value
        for case in upper_cases
        for value in case["gates"].values()
    ]
    all_lower_case_gates = [
        value
        for case in lower_cases
        for value in case["gates"].values()
    ]

    gates = {
        "A60_complete_audit_passed": bool(
            all(a60_results["gates"].values())
        ),
        "nominal_covariance_positive_definite": bool(
            a60.exact_positive_definite(sigma_hat)
        ),
        "spectral_containment_radius_exact": bool(
            tau_box == sp.Rational(1, 625)
        ),
        "all_upper_endpoint_cases_pass": bool(
            all(all_upper_case_gates)
        ),
        "all_lower_endpoint_cases_pass": bool(
            all(all_lower_case_gates)
        ),
        "upper_risk_strictly_increases_with_tau": bool(
            all(
                upper_risks[index + 1] > upper_risks[index]
                for index in range(len(upper_risks) - 1)
            )
        ),
        "lower_risk_strictly_decreases_with_tau": bool(
            all(
                lower_risks[index + 1] < lower_risks[index]
                for index in range(len(lower_risks) - 1)
            )
        ),
        "local_tau_sensitivity_positive": bool(
            sensitivity["positive"]
        ),
        "small_tau_first_order_check": bool(
            abs(first_order_ratio - 1)
            < mp.mpf("0.001")
        ),
        "all_upper_covariances_inside_A58_box": bool(
            all(
                sigma_hat[index, index] + tau_box
                <= sp.Rational(1, 400)
                for index in range(3)
            )
        ),
    }

    verdict = (
        "PASS_SPECTRAL_COVARIANCE_ESTIMATION_UNCERTAINTY"
        if all(gates.values())
        else "FAIL_A61_SPECTRAL_COVARIANCE_AUDIT"
    )

    result = {
        "audit": "A61_SPECTRAL_COVARIANCE_ESTIMATION_UNCERTAINTY",
        "contract": {
            "design": "{2,beta-star,infinity}*log(2)",
            "centre": [str(value) for value in centre],
            "covariance_estimate": [
                [str(sigma_hat[row, column]) for column in range(3)]
                for row in range(3)
            ],
            "spectral_set": (
                "Sigma symmetric PSD and "
                "||Sigma-Sigma_hat||_2<=tau"
            ),
            "lambda_min_sigma_hat": str(lambda_min),
            "maximum_certified_tau": str(tau_box),
        },
        "theorem": {
            "upper_exact": (
                "sup Q(Sigma)=Q(Sigma_hat+tau I)"
            ),
            "lower_exact": (
                "inf Q(Sigma)=Q(Sigma_hat-tau I) "
                "when tau<lambda_min(Sigma_hat)"
            ),
            "loewner_envelope": (
                "Sigma_hat-tau I <= Sigma <= "
                "Sigma_hat+tau I"
            ),
            "quadratic_coefficients": {
                "A_tau": (
                    "b^2-d^T Sigma_hat d-"
                    "tau*||d||^2"
                ),
                "B_tau": (
                    "-2ab+2n^T Sigma_hat d+"
                    "2tau*n^T d"
                ),
                "C_tau": (
                    "a^2-n^T Sigma_hat n-"
                    "tau*||n||^2"
                ),
            },
        },
        "point_estimate": point_case,
        "tau_sensitivity": sensitivity,
        "small_tau_first_order_ratio": mp.nstr(
            first_order_ratio,
            70,
        ),
        "risk_table": rows,
        "formal_results": [
            (
                "the exact worst covariance in the spectral "
                "ball is Sigma_hat+tau I"
            ),
            (
                "the exact best covariance is Sigma_hat-tau I "
                "while it remains positive definite"
            ),
            (
                "the covariance-estimation premium is algebraic"
            ),
            (
                "the premium increases monotonically with tau"
            ),
            (
                "the local spectral-radius sensitivity is supplied"
            ),
            (
                "a machine-readable covariance-confidence-set "
                "template is supplied"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "A61 is deterministic. It assumes tau has already "
            "been certified by an external covariance-estimation "
            "procedure and does not assign a confidence level or "
            "derive tau from sample size."
        ),
    }

    output_path = HERE / (
        "a61_spectral_covariance_uncertainty_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    template = {
        "centre": [1.05, 1.05, 1.05],
        "covariance_estimate": [
            [0.0009, 0.0, 0.0],
            [0.0, 0.000625, 0.0],
            [0.0, 0.0, 0.000225],
        ],
        "spectral_radius_tau": 0.0001,
        "requirements": {
            "covariance_estimate_symmetric": True,
            "covariance_estimate_positive_definite": True,
            "maximum_diagonal_after_inflation": 0.0025,
            "channel_order": ["u2", "u_beta", "u_infinity"],
        },
    }

    template_path = HERE / (
        "a61_covariance_confidence_set_template.json"
    )
    template_path.write_text(
        json.dumps(template, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "point_risk": point_case["robust_risk"],
        "risk_tau_1e_minus_4": next(
            row["upper_risk"]
            for row in rows
            if row["tau"] == "1/10000"
        ),
        "risk_derivative_at_zero": (
            sensitivity["risk_derivative"]
        ),
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
