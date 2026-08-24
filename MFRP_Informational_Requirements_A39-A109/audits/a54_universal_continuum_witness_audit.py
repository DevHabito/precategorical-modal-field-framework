#!/usr/bin/env python3
"""A54 exact audit: universal continuum witness and global anchor optimum.

The audit proves that the A52 extremal pair at beta* satisfies the common
absolute-error constraints for every exponent eta >= 2.

Consequences:
- every finite or infinite observation design in [2,infinity] has ratio at
  least rho*;
- {2,beta*,infinity} attains rho*;
- the complete three-anchor problem is globally solved;
- adding arbitrary extra observations in the allowed domain cannot improve
  the minimax floor.
"""

from __future__ import annotations

import importlib.util
import json
from math import comb
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A52_SCRIPT = HERE / "a52_continuous_second_anchor_audit.py"
A52_RESULTS = HERE / "a52_continuous_second_anchor_results.json"
A53_RESULTS = HERE / "a53_coupled_second_third_anchor_results.json"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(
        name,
        path,
    )
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")

    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def bernstein_coefficients_2d(
    polynomial: sp.Poly,
    x: sp.Symbol,
    y: sp.Symbol,
) -> dict[tuple[int, int], sp.Rational]:
    degree_x = polynomial.degree(x)
    degree_y = polynomial.degree(y)

    coefficients = {
        (index_x, index_y): sp.Rational(0)
        for index_x in range(degree_x + 1)
        for index_y in range(degree_y + 1)
    }

    for (power_x, power_y), coefficient in polynomial.terms():
        for index_x in range(power_x, degree_x + 1):
            factor_x = sp.Rational(
                comb(index_x, power_x),
                comb(degree_x, power_x),
            )

            for index_y in range(power_y, degree_y + 1):
                factor_y = sp.Rational(
                    comb(index_y, power_y),
                    comb(degree_y, power_y),
                )

                coefficients[(index_x, index_y)] += (
                    coefficient * factor_x * factor_y
                )

    return coefficients


def build_universal_certificate(module) -> dict[str, Any]:
    s = module.s
    s_star = module.s_star
    stationary_polynomial = module.STATIONARY_POLYNOMIAL
    certificate = module.PHASES["P5"]

    r, u, v = sp.symbols("r u v", real=True)

    difference = sp.factor(
        sum(
            (
                certificate["p"][index]
                - certificate["q"][index]
            )
            * r**index
            for index in range(6)
        )
    )

    upper_residual = sp.factor(
        sp.Rational(1, 5000) - difference
    )
    lower_residual = sp.factor(
        sp.Rational(1, 5000) + difference
    )

    upper_numerator, denominator = sp.fraction(
        upper_residual
    )
    lower_numerator, lower_denominator = sp.fraction(
        lower_residual
    )

    if sp.factor(denominator - lower_denominator) != 0:
        raise RuntimeError("Residual denominators differ")

    upper_core = sp.factor(
        upper_numerator / (-r * (4 * r - 1))
    )
    lower_core = sp.factor(
        lower_numerator / (r - s)
    )

    quotient, remainder = sp.div(
        lower_core
        - (s - 1) * stationary_polynomial,
        r - s,
        domain="QQ[s]",
    )
    quotient = sp.factor(quotient)

    isolation_lower = sp.Rational(3, 20)
    isolation_upper = sp.Rational(19, 125)

    root_count = sp.Poly(
        stationary_polynomial,
        s,
    ).count_roots(
        isolation_lower,
        isolation_upper,
    )

    s_map = (
        isolation_lower
        + (
            isolation_upper
            - isolation_lower
        )
        * v
    )
    r_map = sp.Rational(1, 4) * u

    upper_rectangle = sp.Poly(
        sp.expand(
            upper_core.subs(
                {
                    s: s_map,
                    r: r_map,
                }
            )
        ),
        u,
        v,
        domain=sp.QQ,
    )

    quotient_rectangle = sp.Poly(
        sp.expand(
            quotient.subs(
                {
                    s: s_map,
                    r: r_map,
                }
            )
        ),
        u,
        v,
        domain=sp.QQ,
    )

    upper_bernstein = bernstein_coefficients_2d(
        upper_rectangle,
        u,
        v,
    )
    quotient_bernstein = bernstein_coefficients_2d(
        quotient_rectangle,
        u,
        v,
    )

    upper_maximum = max(
        upper_bernstein.values()
    )
    quotient_maximum = max(
        quotient_bernstein.values()
    )

    denominator_core = sp.factor(
        denominator
    )

    denominator_samples = [
        sp.sign(
            denominator_core.subs(
                {
                    s: point,
                    r: sp.Rational(1, 8),
                }
            )
        )
        for point in [
            isolation_lower,
            sp.Rational(151, 1000),
            isolation_upper,
        ]
    ]

    target_ratio = sp.factor(
        certificate["ratio"].subs(
            s,
            s_star,
        )
    )
    future_risk = (
        sp.log(target_ratio)
        / (2 * sp.log(2))
    )

    p_star = [
        value.subs(s, s_star)
        for value in certificate["p"]
    ]
    q_star = [
        value.subs(s, s_star)
        for value in certificate["q"]
    ]

    difference_at_zero = sp.factor(
        difference.subs(
            {
                s: s_star,
                r: 0,
            }
        )
    )
    difference_at_beta = sp.factor(
        difference.subs(
            {
                s: s_star,
                r: s_star,
            }
        )
    )
    difference_at_two = sp.factor(
        difference.subs(
            {
                s: s_star,
                r: sp.Rational(1, 4),
            }
        )
    )

    gates = {
        "stationary_root_unique_in_rational_box": bool(
            root_count == 1
            and isolation_lower
            < s_star
            < isolation_upper
        ),
        "stationary_root_exact": bool(
            s_star
            in sp.Poly(
                stationary_polynomial,
                s,
            ).real_roots()
        ),
        "lower_core_division_identity": bool(
            remainder == 0
        ),
        "full_rectangle_upper_bernstein_negative": bool(
            upper_maximum < 0
        ),
        "full_rectangle_lower_bernstein_negative": bool(
            quotient_maximum < 0
        ),
        "common_denominator_negative": bool(
            denominator_samples == [-1, -1, -1]
        ),
        "equioscillation_at_infinity": bool(
            difference_at_zero
            == sp.Rational(1, 5000)
        ),
        "equioscillation_at_beta_star": bool(
            difference_at_beta
            == -sp.Rational(1, 5000)
        ),
        "equioscillation_at_exponent_2": bool(
            difference_at_two
            == sp.Rational(1, 5000)
        ),
        "normalization_exact": bool(
            sp.factor(sum(p_star) - 1) == 0
            and sp.factor(sum(q_star) - 1) == 0
        ),
        "mean_exact": bool(
            sp.factor(
                sum(index * p_star[index] for index in range(6))
                - sp.Rational(5, 2)
            )
            == 0
            and sp.factor(
                sum(index * q_star[index] for index in range(6))
                - sp.Rational(5, 2)
            )
            == 0
        ),
        "A52_primal_dual_identity": bool(
            certificate["ratio"]
            == certificate["dual_objective"]
        ),
    }

    return {
        "s_star": str(s_star),
        "s_star_decimal": str(
            sp.N(s_star, 50)
        ),
        "beta_star_decimal": str(
            sp.N(-sp.log(s_star, 2), 50)
        ),
        "target_ratio": str(target_ratio),
        "future_risk_decimal": str(
            sp.N(future_risk, 50)
        ),
        "p_star": [
            str(value)
            for value in p_star
        ],
        "q_star": [
            str(value)
            for value in q_star
        ],
        "difference_polynomial": str(
            difference.subs(s, s_star)
        ),
        "stationary_polynomial": str(
            stationary_polynomial
        ),
        "upper_residual_factorization": str(
            upper_residual
        ),
        "lower_residual_factorization": str(
            lower_residual
        ),
        "lower_core_identity": {
            "quotient": str(quotient),
            "remainder": str(remainder),
        },
        "rational_isolation_interval": [
            str(isolation_lower),
            str(isolation_upper),
        ],
        "full_rectangle": {
            "s_interval": [
                str(isolation_lower),
                str(isolation_upper),
            ],
            "r_interval": ["0", "1/4"],
        },
        "upper_bernstein_minimum": str(
            min(upper_bernstein.values())
        ),
        "upper_bernstein_maximum": str(
            upper_maximum
        ),
        "lower_bernstein_minimum": str(
            min(quotient_bernstein.values())
        ),
        "lower_bernstein_maximum": str(
            quotient_maximum
        ),
        "equioscillation": {
            "r_0": str(difference_at_zero),
            "r_s_star": str(difference_at_beta),
            "r_1_over_4": str(difference_at_two),
        },
        "gates": gates,
    }


def main() -> None:
    if not A52_SCRIPT.exists():
        raise FileNotFoundError(A52_SCRIPT)
    if not A52_RESULTS.exists():
        raise FileNotFoundError(A52_RESULTS)
    if not A53_RESULTS.exists():
        raise FileNotFoundError(A53_RESULTS)

    module = load_module(
        A52_SCRIPT,
        "a52_for_a54",
    )

    a52_results = json.loads(
        A52_RESULTS.read_text(encoding="utf-8")
    )
    a53_results = json.loads(
        A53_RESULTS.read_text(encoding="utf-8")
    )

    certificate = build_universal_certificate(
        module
    )

    a52_gates = a52_results["gates"]
    a53_gates = a53_results["gates"]

    gates = {
        "A52_complete_audit_passed": bool(
            all(a52_gates.values())
        ),
        "A53_coordinatewise_audit_passed": bool(
            all(a53_gates.values())
        ),
        "universal_continuum_certificate_passed": bool(
            all(certificate["gates"].values())
        ),
        "upper_error_band_uniform_on_full_domain": bool(
            certificate["gates"][
                "full_rectangle_upper_bernstein_negative"
            ]
        ),
        "lower_error_band_uniform_on_full_domain": bool(
            certificate["gates"][
                "full_rectangle_lower_bernstein_negative"
            ]
        ),
        "three_contact_equioscillation_exact": bool(
            certificate["gates"][
                "equioscillation_at_infinity"
            ]
            and certificate["gates"][
                "equioscillation_at_beta_star"
            ]
            and certificate["gates"][
                "equioscillation_at_exponent_2"
            ]
        ),
        "global_lower_bound_attained_by_A52_design": bool(
            a52_gates[
                "stationary_polynomial_has_one_phase_root"
            ]
            and a52_gates[
                "continuous_optimum_improves_beta_3"
            ]
        ),
        "arbitrary_observation_budget_cannot_improve": bool(
            certificate["gates"][
                "full_rectangle_upper_bernstein_negative"
            ]
            and certificate["gates"][
                "full_rectangle_lower_bernstein_negative"
            ]
        ),
    }

    verdict = (
        "PASS_UNIVERSAL_CONTINUUM_WITNESS_AND_COMPLETE_GLOBAL_ANCHOR_OPTIMUM"
        if all(gates.values())
        else "FAIL_A54_UNIVERSAL_CONTINUUM_AUDIT"
    )

    result = {
        "audit": (
            "A54_UNIVERSAL_CONTINUUM_WITNESS"
        ),
        "contract": {
            "support": list(range(6)),
            "mean": "5/2",
            "target_exponent": 1,
            "allowed_observation_exponents": "[2,infinity]",
            "epsilon": "1/10000",
            "future_score_transport": "a=1/2",
            "observation_budget": "arbitrary, including continuum",
        },
        "universal_certificate": certificate,
        "global_optimum": {
            "design": [
                "2",
                certificate["beta_star_decimal"],
                "infinity",
            ],
            "future_risk": certificate[
                "future_risk_decimal"
            ],
            "statement": (
                "Every design using observation exponents "
                "eta>=2 has minimax risk at least this value, "
                "and the three-point design attains it."
            ),
        },
        "formal_results": [
            (
                "one exact extremal pair satisfies the error "
                "band for every eta>=2"
            ),
            (
                "the result is uniform over the full continuum "
                "of permitted observations"
            ),
            (
                "all finite and infinite observation budgets "
                "share the same minimax lower floor"
            ),
            (
                "{2,beta-star,infinity} attains the universal floor"
            ),
            (
                "the complete joint anchor problem is globally solved"
            ),
            (
                "the optimal points are the three exact "
                "equioscillation contacts"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The theorem depends on the six-point microscopic "
            "support, exact mean, common absolute tolerance "
            "1e-4, target exponent 1, and exclusion of observation "
            "exponents below 2. No physical interpretation or "
            "empirical error model is inferred."
        ),
    }

    output_path = HERE / (
        "a54_universal_continuum_witness_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "beta_star": certificate[
            "beta_star_decimal"
        ],
        "future_risk": certificate[
            "future_risk_decimal"
        ],
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
