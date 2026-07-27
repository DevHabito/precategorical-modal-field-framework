#!/usr/bin/env python3
"""A60 exact audit: general covariance matrix robust calibration theorem.

The A58 ratio is linear-fractional in the three calibration-error factors.
For any positive-definite covariance ellipsoid contained in [1,1.1]^3, the
exact robust maximum is one admissible quadratic root.

The audit verifies:
- exact general formula;
- positive definiteness and containment;
- KKT worst direction;
- ratio reproduction;
- Loewner monotonicity;
- covariance contribution diagnostics.

The script also writes a reusable covariance-input template.
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


def extract_linear_fractional(
    ratio: sp.Expr,
    variables: list[sp.Symbol],
) -> dict[str, Any]:
    numerator, denominator = sp.fraction(sp.cancel(ratio))

    n = [
        sp.diff(numerator, variable)
        for variable in variables
    ]
    d = [
        sp.diff(denominator, variable)
        for variable in variables
    ]

    n0 = sp.expand(
        numerator
        - sum(
            n[index] * variables[index]
            for index in range(len(variables))
        )
    )
    d0 = sp.expand(
        denominator
        - sum(
            d[index] * variables[index]
            for index in range(len(variables))
        )
    )

    exactly_linear = all(
        sp.diff(n[index], variable) == 0
        and sp.diff(d[index], variable) == 0
        for index in range(len(variables))
        for variable in variables
    )

    return {
        "n0": n0,
        "d0": d0,
        "n": n,
        "d": d,
        "exactly_linear": bool(exactly_linear),
    }


def exact_positive_definite(matrix: sp.Matrix) -> bool:
    return bool(
        matrix == matrix.T
        and matrix[:1, :1].det() > 0
        and matrix[:2, :2].det() > 0
        and matrix.det() > 0
    )


def mp_number(expression: sp.Expr, s: sp.Symbol, s_star: sp.Expr) -> mp.mpf:
    return mp.mpf(str(sp.N(expression.subs(s, s_star), 90)))


def robust_solution(
    name: str,
    covariance: sp.Matrix,
    centre: list[sp.Rational],
    coefficients: dict[str, Any],
    s: sp.Symbol,
    s_star: sp.Expr,
) -> dict[str, Any]:
    mp.mp.dps = 90

    positive_definite = exact_positive_definite(covariance)
    diagonal_containment = all(
        covariance[index, index] <= sp.Rational(1, 400)
        for index in range(3)
    )

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
    sigma_mp = mp.matrix(
        [
            [
                mp.mpf(str(sp.N(covariance[row, column], 90)))
                for column in range(3)
            ]
            for row in range(3)
        ]
    )

    a = n0 + sum(n[index] * centre_mp[index] for index in range(3))
    b = d0 + sum(d[index] * centre_mp[index] for index in range(3))

    def quadratic_form(left, matrix, right):
        return sum(
            left[index]
            * sum(
                matrix[index, other] * right[other]
                for other in range(3)
            )
            for index in range(3)
        )

    nn = quadratic_form(n, sigma_mp, n)
    dd = quadratic_form(d, sigma_mp, d)
    nd = quadratic_form(n, sigma_mp, d)

    coefficient_a = b**2 - dd
    coefficient_b = -2 * a * b + 2 * nd
    coefficient_c = a**2 - nn

    discriminant = coefficient_b**2 - 4 * coefficient_a * coefficient_c
    roots = [
        (-coefficient_b + mp.sqrt(discriminant)) / (2 * coefficient_a),
        (-coefficient_b - mp.sqrt(discriminant)) / (2 * coefficient_a),
    ]

    selected = None

    for candidate in roots:
        vector = [
            n[index] - candidate * d[index]
            for index in range(3)
        ]
        support_squared = quadratic_form(vector, sigma_mp, vector)
        support_residual = a - candidate * b + mp.sqrt(support_squared)
        branch = a - candidate * b

        if (
            abs(support_residual) < mp.mpf("1e-65")
            and branch <= 0
        ):
            selected = candidate
            selected_vector = vector
            selected_support_squared = support_squared
            break

    if selected is None:
        raise RuntimeError(f"No admissible root for {name}")

    displacement = [
        sum(
            sigma_mp[index, other] * selected_vector[other]
            for other in range(3)
        )
        / mp.sqrt(selected_support_squared)
        for index in range(3)
    ]

    worst = [
        centre_mp[index] + displacement[index]
        for index in range(3)
    ]

    numerator_worst = n0 + sum(
        n[index] * worst[index] for index in range(3)
    )
    denominator_worst = d0 + sum(
        d[index] * worst[index] for index in range(3)
    )
    reproduced = numerator_worst / denominator_worst

    inverse_sigma = sigma_mp**-1
    boundary_norm = quadratic_form(displacement, inverse_sigma, displacement)

    centre_ratio = a / b
    centre_risk = mp.log(centre_ratio, 2) / 2
    robust_risk = mp.log(selected, 2) / 2

    gradient = []
    for index in range(3):
        ratio_derivative = (
            n[index] * b - d[index] * a
        ) / b**2
        gradient.append(
            ratio_derivative
            / (2 * mp.log(2) * centre_ratio)
        )

    marginal_contributions = [
        gradient[index] ** 2 * sigma_mp[index, index]
        for index in range(3)
    ]
    pairwise_contributions = {
        "2_beta": (
            2 * gradient[0] * gradient[1] * sigma_mp[0, 1]
        ),
        "2_infinity": (
            2 * gradient[0] * gradient[2] * sigma_mp[0, 2]
        ),
        "beta_infinity": (
            2 * gradient[1] * gradient[2] * sigma_mp[1, 2]
        ),
    }
    local_variance = (
        sum(marginal_contributions)
        + sum(pairwise_contributions.values())
    )

    return {
        "name": name,
        "covariance": [
            [str(covariance[row, column]) for column in range(3)]
            for row in range(3)
        ],
        "positive_definite": positive_definite,
        "diagonal_containment": diagonal_containment,
        "quadratic_coefficients": {
            "A": mp.nstr(coefficient_a, 70),
            "B": mp.nstr(coefficient_b, 70),
            "C": mp.nstr(coefficient_c, 70),
        },
        "robust_ratio": mp.nstr(selected, 70),
        "robust_risk": mp.nstr(robust_risk, 70),
        "centre_risk": mp.nstr(centre_risk, 70),
        "excess_over_centre": mp.nstr(
            robust_risk - centre_risk,
            70,
        ),
        "worst_error_factors": [
            mp.nstr(value, 70)
            for value in worst
        ],
        "ellipsoid_boundary_norm": mp.nstr(boundary_norm, 70),
        "ratio_reproduction_residual": mp.nstr(
            reproduced - selected,
            70,
        ),
        "local_covariance_diagnostic": {
            "gradient": [
                mp.nstr(value, 60)
                for value in gradient
            ],
            "marginal_contributions": [
                mp.nstr(value, 60)
                for value in marginal_contributions
            ],
            "pairwise_contributions": {
                key: mp.nstr(value, 60)
                for key, value in pairwise_contributions.items()
            },
            "total_local_variance": mp.nstr(local_variance, 60),
        },
        "gates": {
            "positive_definite": positive_definite,
            "contained_in_A58_box": diagonal_containment,
            "admissible_root_reproduced": bool(
                abs(reproduced - selected) < mp.mpf("1e-60")
            ),
            "ellipsoid_boundary_exact": bool(
                abs(boundary_norm - 1) < mp.mpf("1e-60")
            ),
            "worst_point_inside_box": bool(
                all(
                    mp.mpf("1") <= value <= mp.mpf("1.1")
                    for value in worst
                )
            ),
            "denominator_positive_at_worst": bool(
                denominator_worst > 0
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

    a52 = load_module(A52_SCRIPT, "a52_for_a60")
    a58 = load_module(A58_SCRIPT, "a58_for_a60")

    a58_results = json.loads(
        A58_RESULTS.read_text(encoding="utf-8")
    )

    certificate = a58.build_certificate(a52)
    variables = [
        certificate["u2"],
        certificate["ub"],
        certificate["ui"],
    ]
    coefficients = extract_linear_fractional(
        certificate["ratio"],
        variables,
    )

    centre = [
        sp.Rational(21, 20),
        sp.Rational(21, 20),
        sp.Rational(21, 20),
    ]

    sigma_diagonal = sp.diag(
        sp.Rational(1, 400),
        sp.Rational(1, 625),
        sp.Rational(1, 2500),
    )

    sigma_positive = sp.Matrix(
        [
            [sp.Rational(1, 400), sp.Rational(1, 1000), sp.Rational(1, 5000)],
            [sp.Rational(1, 1000), sp.Rational(1, 625), sp.Rational(1, 5000)],
            [sp.Rational(1, 5000), sp.Rational(1, 5000), sp.Rational(1, 2500)],
        ]
    )

    sigma_mixed = sp.Matrix(
        [
            [sp.Rational(1, 400), -sp.Rational(1, 2000), -sp.Rational(1, 10000)],
            [-sp.Rational(1, 2000), sp.Rational(1, 625), sp.Rational(1, 12500)],
            [-sp.Rational(1, 10000), sp.Rational(1, 12500), sp.Rational(1, 2500)],
        ]
    )

    sigma_small = sp.diag(
        sp.Rational(9, 10000),
        sp.Rational(1, 1600),
        sp.Rational(9, 40000),
    )

    w = sp.Matrix(
        [
            sp.Rational(1, 50),
            sp.Rational(3, 200),
            sp.Rational(1, 100),
        ]
    )
    sigma_large = sigma_small + w * w.T

    matrices = {
        "unequal_independent": sigma_diagonal,
        "positive_pairwise": sigma_positive,
        "mixed_pairwise": sigma_mixed,
        "loewner_small": sigma_small,
        "loewner_large": sigma_large,
    }

    cases = [
        robust_solution(
            name,
            matrix,
            centre,
            coefficients,
            certificate["s"],
            a52.s_star,
        )
        for name, matrix in matrices.items()
    ]

    case_by_name = {
        case["name"]: case
        for case in cases
    }

    difference = sp.simplify(sigma_large - sigma_small)
    loewner_exact = bool(difference == w * w.T)
    loewner_nonzero = bool(any(value != 0 for value in difference))

    loewner_risk_order = bool(
        mp.mpf(
            case_by_name["loewner_large"]["robust_risk"]
        )
        >
        mp.mpf(
            case_by_name["loewner_small"]["robust_risk"]
        )
    )

    all_case_gates = [
        value
        for case in cases
        for value in case["gates"].values()
    ]

    gates = {
        "A58_complete_audit_passed": bool(
            all(a58_results["gates"].values())
        ),
        "ratio_exactly_linear_fractional": bool(
            coefficients["exactly_linear"]
        ),
        "all_covariance_case_gates_pass": bool(
            all(all_case_gates)
        ),
        "loewner_increment_is_exact_rank_one_PSD": bool(
            loewner_exact and loewner_nonzero
        ),
        "strict_loewner_risk_order_verified": loewner_risk_order,
        "positive_and_mixed_examples_share_marginals": bool(
            all(
                sigma_positive[index, index]
                == sigma_mixed[index, index]
                for index in range(3)
            )
        ),
        "positive_example_more_adversarial_than_mixed_example": bool(
            mp.mpf(
                case_by_name["positive_pairwise"]["robust_risk"]
            )
            >
            mp.mpf(
                case_by_name["mixed_pairwise"]["robust_risk"]
            )
        ),
    }

    verdict = (
        "PASS_GENERAL_COVARIANCE_MATRIX_ROBUST_CALIBRATION_THEOREM"
        if all(gates.values())
        else "FAIL_A60_GENERAL_COVARIANCE_AUDIT"
    )

    result = {
        "audit": "A60_GENERAL_COVARIANCE_MATRIX",
        "contract": {
            "design": "{2,beta-star,infinity}*log(2)",
            "centre": [str(value) for value in centre],
            "covariance_requirement": "Sigma positive definite",
            "containment_requirement": "Sigma_ii<=1/400",
            "certified_box": "[1,11/10]^3",
        },
        "general_theorem": {
            "ratio": "(n0+n^T u)/(d0+d^T u)",
            "quadratic": (
                "(b^2-d^T Sigma d)y^2"
                "+(-2ab+2n^T Sigma d)y"
                "+(a^2-n^T Sigma n)=0"
            ),
            "branch_condition": "a-yb<=0",
            "worst_direction": (
                "u*=ubar+Sigma(n-yd)"
                "/sqrt((n-yd)^T Sigma (n-yd))"
            ),
            "loewner_order": (
                "Sigma1<=Sigma2 implies robust_risk(Sigma1)"
                "<=robust_risk(Sigma2)"
            ),
        },
        "linear_fractional_coefficients": {
            "n0": str(coefficients["n0"]),
            "d0": str(coefficients["d0"]),
            "n": [str(value) for value in coefficients["n"]],
            "d": [str(value) for value in coefficients["d"]],
        },
        "cases": cases,
        "loewner_test": {
            "small_covariance": [
                [str(sigma_small[row, column]) for column in range(3)]
                for row in range(3)
            ],
            "increment_vector": [str(value) for value in w],
            "large_equals_small_plus_wwT": loewner_exact,
            "small_risk": case_by_name["loewner_small"]["robust_risk"],
            "large_risk": case_by_name["loewner_large"]["robust_risk"],
        },
        "formal_results": [
            "arbitrary unequal marginal scales are allowed",
            "all three pairwise correlations may differ",
            "the robust maximum is one admissible quadratic root",
            "the exact worst covariance direction is supplied",
            "robust risk is monotone in the Loewner order",
            "local variance and covariance contributions are reported",
            "a machine-readable covariance template is supplied",
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The theorem requires a positive-definite covariance "
            "ellipsoid contained in the A58 box. It does not estimate "
            "Sigma from data, model covariance-estimation uncertainty, "
            "or reoptimize beta-star."
        ),
    }

    output_path = HERE / "a60_general_covariance_matrix_results.json"
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    template = {
        "centre": [1.05, 1.05, 1.05],
        "covariance": [
            [0.0025, 0.0010, 0.0002],
            [0.0010, 0.0016, 0.0002],
            [0.0002, 0.0002, 0.0004],
        ],
        "requirements": {
            "symmetric": True,
            "positive_definite": True,
            "maximum_diagonal_entry": 0.0025,
            "channel_order": ["u2", "u_beta", "u_infinity"],
        },
    }

    template_path = HERE / "a60_covariance_input_template.json"
    template_path.write_text(
        json.dumps(template, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "risk_by_case": {
            case["name"]: case["robust_risk"]
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
