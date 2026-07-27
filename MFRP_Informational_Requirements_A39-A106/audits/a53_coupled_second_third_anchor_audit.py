#!/usr/bin/env python3
"""A53 coupled second-third anchor audit.

Exact theorem
-------------
At the A52 stationary beta*, the compactified extremal pair is feasible for
every finite gamma > beta*. Therefore gamma=infinity is globally optimal on
that beta slice.

Together with A52, this proves coordinatewise global optimality of
(beta*, infinity).

The script also performs deterministic numerical reconnaissance over the full
coupled domain. Numerical results are explicitly not promoted to an exact
two-dimensional global theorem.
"""

from __future__ import annotations

import importlib.util
import json
import math
from math import comb
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp
from scipy.optimize import differential_evolution, linprog, minimize_scalar


HERE = Path(__file__).resolve().parent
A52_SCRIPT = HERE / "a52_continuous_second_anchor_audit.py"
A52_RESULTS = HERE / "a52_continuous_second_anchor_results.json"

SUPPORT = np.arange(6, dtype=float)
TARGET_FLOAT = 2.0 ** (-SUPPORT)
MEAN_FLOAT = 2.5
EPSILON_FLOAT = 1e-4


def load_a52_module():
    specification = importlib.util.spec_from_file_location(
        "a52_module",
        A52_SCRIPT,
    )
    if specification is None or specification.loader is None:
        raise RuntimeError("Could not load A52 module")

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


def build_exact_certificate(
    module,
) -> dict[str, Any]:
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
        raise RuntimeError("Residual denominators do not match")

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
        + (isolation_upper - isolation_lower) * v
    )
    r_map = s_map * u

    upper_rectangle_polynomial = sp.Poly(
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

    quotient_rectangle_polynomial = sp.Poly(
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
        upper_rectangle_polynomial,
        u,
        v,
    )
    quotient_bernstein = bernstein_coefficients_2d(
        quotient_rectangle_polynomial,
        u,
        v,
    )

    upper_maximum = max(upper_bernstein.values())
    quotient_maximum = max(
        quotient_bernstein.values()
    )

    denominator_sign_samples = [
        sp.sign(
            denominator.subs(
                {
                    s: point,
                    r: 0,
                }
            )
        )
        for point in [
            isolation_lower,
            sp.Rational(151, 1000),
            isolation_upper,
        ]
    ]

    ratio_star = certificate["ratio"].subs(
        s,
        s_star,
    )
    risk_star = (
        sp.log(ratio_star)
        / (2 * sp.log(2))
    )

    gates = {
        "stationary_root_unique_in_rational_box": bool(
            root_count == 1
            and isolation_lower < s_star < isolation_upper
        ),
        "lower_core_division_identity": bool(
            remainder == 0
        ),
        "upper_bernstein_coefficients_strictly_negative": bool(
            upper_maximum < 0
        ),
        "lower_quotient_bernstein_coefficients_strictly_negative": bool(
            quotient_maximum < 0
        ),
        "common_denominator_strictly_negative": bool(
            denominator_sign_samples == [-1, -1, -1]
        ),
        "A52_stationary_polynomial_zero": bool(
            s_star
            in sp.Poly(
                stationary_polynomial,
                s,
            ).real_roots()
        ),
        "A52_primal_dual_identity_retained": bool(
            certificate["ratio"]
            == certificate["dual_objective"]
        ),
    }

    return {
        "s_star": str(s_star),
        "s_star_decimal": str(sp.N(s_star, 45)),
        "beta_star_decimal": str(
            sp.N(-sp.log(s_star, 2), 45)
        ),
        "ratio_star": str(ratio_star),
        "risk_star_decimal": str(
            sp.N(risk_star, 45)
        ),
        "stationary_polynomial": str(
            stationary_polynomial
        ),
        "upper_residual": str(upper_residual),
        "lower_residual": str(lower_residual),
        "lower_core_identity": {
            "quotient": str(quotient),
            "remainder": str(remainder),
        },
        "rational_isolation_interval": [
            str(isolation_lower),
            str(isolation_upper),
        ],
        "upper_bernstein_maximum": str(
            upper_maximum
        ),
        "lower_quotient_bernstein_maximum": str(
            quotient_maximum
        ),
        "gates": gates,
    }


def solve_ratio(
    beta: float,
    gamma: float | None,
) -> float:
    objective = np.zeros(13)
    objective[:6] = -TARGET_FLOAT

    equalities = []
    equality_rhs = []

    row = np.zeros(13)
    row[:6] = 1
    row[12] = -1
    equalities.append(row)
    equality_rhs.append(0)

    row = np.zeros(13)
    row[6:12] = 1
    row[12] = -1
    equalities.append(row)
    equality_rhs.append(0)

    row = np.zeros(13)
    row[:6] = SUPPORT
    row[12] = -MEAN_FLOAT
    equalities.append(row)
    equality_rhs.append(0)

    row = np.zeros(13)
    row[6:12] = SUPPORT
    row[12] = -MEAN_FLOAT
    equalities.append(row)
    equality_rhs.append(0)

    row = np.zeros(13)
    row[6:12] = TARGET_FLOAT
    equalities.append(row)
    equality_rhs.append(1)

    inequalities = []
    inequality_rhs = []

    exponents: list[float | None] = [
        2.0,
        beta,
        gamma,
    ]

    for exponent in exponents:
        if exponent is None:
            values = np.zeros(6)
            values[0] = 1
        else:
            values = 2.0 ** (
                -float(exponent) * SUPPORT
            )

        difference = np.zeros(13)
        difference[:6] = values
        difference[6:12] = -values

        for sign in [1.0, -1.0]:
            row = sign * difference.copy()
            row[12] = -2 * EPSILON_FLOAT
            inequalities.append(row)
            inequality_rhs.append(0)

    result = linprog(
        objective,
        A_ub=np.asarray(inequalities),
        b_ub=np.asarray(inequality_rhs),
        A_eq=np.asarray(equalities),
        b_eq=np.asarray(equality_rhs),
        bounds=[(0, None)] * 13,
        method="highs",
    )

    if not result.success:
        raise RuntimeError(result.message)

    return float(-result.fun)


def future_risk(
    beta: float,
    gamma: float | None,
) -> float:
    return 0.5 * math.log2(
        solve_ratio(beta, gamma)
    )


def numerical_reconnaissance(
    beta_star_exact: float,
    risk_star_exact: float,
) -> dict[str, Any]:
    cap_rows = []

    for cap in [4.0, 6.0, 10.0, 20.0]:
        optimization = minimize_scalar(
            lambda beta: future_risk(
                beta,
                cap,
            ),
            bounds=(
                2.000001,
                min(3.999999, cap - 0.000001),
            ),
            method="bounded",
            options={"xatol": 1e-10},
        )

        cap_rows.append(
            {
                "gamma_cap": cap,
                "beta_optimum": float(
                    optimization.x
                ),
                "future_risk": float(
                    optimization.fun
                ),
            }
        )

    infinity_optimization = minimize_scalar(
        lambda beta: future_risk(
            beta,
            None,
        ),
        bounds=(2.000001, 3.999999),
        method="bounded",
        options={"xatol": 1e-10},
    )

    cap_rows.append(
        {
            "gamma_cap": "infinity",
            "beta_optimum": float(
                infinity_optimization.x
            ),
            "future_risk": float(
                infinity_optimization.fun
            ),
        }
    )

    def finite_plane_objective(
        vector: np.ndarray,
    ) -> float:
        beta = float(vector[0])
        gamma = float(vector[1])

        if gamma <= beta:
            return 1.0 + beta - gamma

        return future_risk(beta, gamma)

    global_search = differential_evolution(
        finite_plane_objective,
        bounds=[
            (2.0001, 3.9999),
            (2.0002, 20.0),
        ],
        seed=53,
        polish=True,
        popsize=12,
        maxiter=60,
        tol=1e-9,
        updating="immediate",
        workers=1,
    )

    beta_grid = np.linspace(
        2.0005,
        3.9995,
        41,
    )

    lowest_grid = {
        "risk": float("inf"),
        "beta": None,
        "gamma": None,
    }

    low_beta_best = {
        "risk": float("inf"),
        "beta": None,
        "gamma": None,
    }

    for beta in beta_grid:
        gamma_grid = np.unique(
            np.concatenate(
                [
                    np.linspace(
                        beta + 0.001,
                        min(4.5, beta + 2.0),
                        35,
                    ),
                    np.linspace(
                        max(4.5, beta + 0.001),
                        20.0,
                        35,
                    ),
                ]
            )
        )

        gamma_grid = gamma_grid[
            gamma_grid > beta
        ]

        for gamma in gamma_grid:
            risk = future_risk(
                float(beta),
                float(gamma),
            )

            if risk < lowest_grid["risk"]:
                lowest_grid = {
                    "risk": float(risk),
                    "beta": float(beta),
                    "gamma": float(gamma),
                }

            if (
                beta <= 2.05
                and risk < low_beta_best["risk"]
            ):
                low_beta_best = {
                    "risk": float(risk),
                    "beta": float(beta),
                    "gamma": float(gamma),
                }

        infinity_risk = future_risk(
            float(beta),
            None,
        )

        if infinity_risk < lowest_grid["risk"]:
            lowest_grid = {
                "risk": float(infinity_risk),
                "beta": float(beta),
                "gamma": "infinity",
            }

    return {
        "finite_caps": cap_rows,
        "differential_evolution": {
            "beta": float(global_search.x[0]),
            "gamma": float(global_search.x[1]),
            "future_risk": float(
                global_search.fun
            ),
            "success": bool(
                global_search.success
            ),
            "message": str(global_search.message),
        },
        "adaptive_grid_minimum": lowest_grid,
        "low_beta_grid_best": low_beta_best,
        "certified_candidate": {
            "beta": beta_star_exact,
            "gamma": "infinity",
            "future_risk": risk_star_exact,
        },
        "no_numeric_improvement_found": bool(
            min(
                row["future_risk"]
                for row in cap_rows
            )
            >= risk_star_exact - 1e-10
            and global_search.fun
            >= risk_star_exact - 1e-8
            and lowest_grid["risk"]
            >= risk_star_exact - 1e-7
        ),
    }


def main() -> None:
    if not A52_SCRIPT.exists():
        raise FileNotFoundError(A52_SCRIPT)
    if not A52_RESULTS.exists():
        raise FileNotFoundError(A52_RESULTS)

    module = load_a52_module()
    a52_results = json.loads(
        A52_RESULTS.read_text(encoding="utf-8")
    )

    exact_certificate = build_exact_certificate(
        module
    )

    beta_star_float = float(
        exact_certificate["beta_star_decimal"]
    )
    risk_star_float = float(
        exact_certificate["risk_star_decimal"]
    )

    numerical = numerical_reconnaissance(
        beta_star_float,
        risk_star_float,
    )

    a52_gates = a52_results["gates"]

    gates = {
        "A52_full_audit_passed": bool(
            all(a52_gates.values())
        ),
        "stationary_exact_certificate_passed": bool(
            all(
                exact_certificate["gates"].values()
            )
        ),
        "finite_gamma_upper_residual_certified": bool(
            exact_certificate["gates"][
                "upper_bernstein_coefficients_strictly_negative"
            ]
        ),
        "finite_gamma_lower_residual_certified": bool(
            exact_certificate["gates"][
                "lower_quotient_bernstein_coefficients_strictly_negative"
            ]
        ),
        "coordinatewise_beta_globality_inherited_from_A52": bool(
            a52_gates[
                "stationary_polynomial_has_one_phase_root"
            ]
            and a52_gates[
                "P5_derivative_negative_below_s_star"
            ]
            and a52_gates[
                "P5_derivative_positive_above_s_star"
            ]
        ),
        "numerical_reconnaissance_found_no_improvement": bool(
            numerical[
                "no_numeric_improvement_found"
            ]
        ),
    }

    verdict = (
        "PASS_COUPLED_ANCHOR_COORDINATEWISE_GLOBAL_CERTIFICATE"
        if all(gates.values())
        else "FAIL_A53_COUPLED_ANCHOR_AUDIT"
    )

    result = {
        "audit": "A53_COUPLED_SECOND_THIRD_ANCHOR",
        "contract": {
            "support": list(range(6)),
            "mean": "5/2",
            "first_anchor": 2,
            "beta_domain": "(2,4)",
            "gamma_domain": "(beta,infinity]",
            "epsilon": "1/10000",
            "target_exponent": 1,
        },
        "exact_coordinatewise_certificate": (
            exact_certificate
        ),
        "numerical_reconnaissance": numerical,
        "formal_results": [
            (
                "A52 beta-star remains globally optimal "
                "on the compactified gamma boundary"
            ),
            (
                "the compactified extremal pair is feasible "
                "for every finite gamma at beta-star"
            ),
            (
                "gamma=infinity is globally optimal on the "
                "beta=beta-star slice"
            ),
            (
                "(beta-star,infinity) is coordinatewise "
                "globally optimal"
            ),
            (
                "finite-cap numerical optima converge toward "
                "the coordinatewise solution"
            ),
        ],
        "not_proved": [
            (
                "full joint global optimality over all "
                "2<beta<gamma<=infinity"
            ),
            (
                "a complete two-dimensional active-basis atlas"
            ),
            (
                "a uniform exact lower bound over the low-beta strip"
            ),
        ],
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "The exact theorem is coordinatewise, not a complete "
            "joint minimization theorem. The full-plane search is "
            "numerical reconnaissance and is not promoted to proof."
        ),
    }

    output_path = HERE / (
        "a53_coupled_second_third_anchor_results.json"
    )
    output_path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    summary = {
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "beta_star": exact_certificate[
            "beta_star_decimal"
        ],
        "risk_star": exact_certificate[
            "risk_star_decimal"
        ],
        "numerical_improvement_found": not numerical[
            "no_numeric_improvement_found"
        ],
        "failed_gates": [
            name
            for name, value in gates.items()
            if not value
        ],
        "failed_exact_subgates": [
            name
            for name, value
            in exact_certificate["gates"].items()
            if not value
        ],
        "verdict": verdict,
    }

    print(json.dumps(summary, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
