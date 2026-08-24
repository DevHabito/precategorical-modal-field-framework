#!/usr/bin/env python3
"""A77 parity audit for the actual M=19,... contact family.

Family
------
    P={0,5,6,M},
    Q={1,h,h+1}, h=floor(M/2),
    active={alpha+,beta-,gamma+}.

On I=[13/100,33/250], the exact gamma-plus Cramer orientation is:

    positive for M=19,20,21,22,
    negative for 23 <= M <= 34,
    positive for every integer M >= 35.

The first bifurcation is numerator-driven. The second is caused by the
basis determinant. Exact Bernstein certificates cover M=19,...,47.
Parity-specific asymptotic remainder bounds cover all h>=24:
M>=48 even and M>=49 odd.

This is a theorem about the fixed contact family, not a claim that this
family remains optimal after M=23.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A75_SCRIPT = HERE / "a75_parity_orientation_audit.py"
A76_RESULTS = HERE / "a76_interval_certificate_results.json"

S = sp.Symbol("s")
H = sp.Symbol("h", integer=True, positive=True)
U = sp.Symbol("U", positive=True)
V = sp.Symbol("V", positive=True)

LOWER = sp.Rational(13, 100)
UPPER = sp.Rational(33, 250)
ASYMPTOTIC_H0 = 24


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def parity_formula(parity: str) -> dict[str, sp.Expr]:
    if parity == "even":
        maximum = 2 * H
        mean = H
        target_max = U**2
        alpha_max = V**2
        epsilon = U / 1875
    elif parity == "odd":
        maximum = 2 * H + 1
        mean = H + sp.Rational(1, 2)
        target_max = U**2 / 2
        alpha_max = S * V**2
        epsilon = U / 2500
    else:
        raise ValueError(parity)

    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [0, 5, 6, maximum, 0, 0, 0, -mean],
        [0, 0, 0, 0, 1, H, H + 1, -mean],
        [
            0, 0, 0, 0,
            sp.Rational(1, 2), U, U / 2, 0,
        ],
        [
            1, S**5, S**6, alpha_max,
            -S, -V, -S * V, -2 * epsilon,
        ],
        [
            -1,
            -sp.Rational(1, 2**15),
            -sp.Rational(1, 2**18),
            -target_max**3,
            sp.Rational(1, 8),
            U**3,
            U**3 / 8,
            -2 * epsilon,
        ],
        [
            1,
            sp.Rational(1, 2**20),
            sp.Rational(1, 2**24),
            target_max**4,
            -sp.Rational(1, 16),
            -U**4,
            -U**4 / 16,
            -2 * epsilon,
        ],
    ]

    basis = sp.Matrix(rows)
    objective = sp.Matrix([
        1,
        sp.Rational(1, 32),
        sp.Rational(1, 64),
        target_max,
        0, 0, 0, 0,
    ])

    numerator_basis = basis.copy()
    numerator_basis[7, :] = objective.T

    numerator = sp.factor(numerator_basis.det())
    denominator = sp.factor(basis.det())

    return {
        "maximum": maximum,
        "epsilon": epsilon,
        "numerator": numerator,
        "denominator": denominator,
        "ratio": sp.cancel(numerator / denominator),
    }


def specialized_polynomials(
    formula: dict[str, sp.Expr],
    maximum: int,
) -> tuple[sp.Poly, sp.Poly]:
    h = maximum // 2
    substitutions = {
        H: h,
        U: sp.Rational(1, 2**h),
        V: S**h,
    }
    return (
        sp.Poly(
            sp.factor(formula["numerator"].subs(substitutions)),
            S,
            domain=sp.QQ,
        ),
        sp.Poly(
            sp.factor(formula["denominator"].subs(substitutions)),
            S,
            domain=sp.QQ,
        ),
    )


def leading_lower_bound(
    parity: str,
    kind: str,
    h0: int,
) -> sp.Rational:
    p_factor = (
        (1 - 2 * UPPER)
        * (8 * LOWER - 1)
        * (
            5456 * LOWER**4
            + 680 * LOWER**3
            + 84 * LOWER**2
            + 10 * LOWER
            + 1
        )
    )
    d_factor = (
        (8 * LOWER - 1)
        * (16 * LOWER - 1)
        * (
            126976 * LOWER**4
            + 7680 * LOWER**3
            + 448 * LOWER**2
            + 24 * LOWER
            + 1
        )
    )

    if parity == "even":
        if kind == "numerator":
            return sp.factor(
                sp.Rational(3 * h0, 2**24) * p_factor
            )
        return sp.factor(
            sp.Rational(h0, 2**40) * d_factor
        )

    if kind == "numerator":
        return sp.factor(
            sp.Rational(3 * (2 * h0 + 1), 2**25)
            * p_factor
        )
    return sp.factor(
        sp.Rational(2 * h0 + 1, 2**41)
        * d_factor
    )


def main() -> None:
    a75 = load_module(A75_SCRIPT, "a75_for_a77")
    a76 = json.loads(
        A76_RESULTS.read_text(encoding="utf-8")
    )

    formulas = {
        "even": parity_formula("even"),
        "odd": parity_formula("odd"),
    }

    leading = {
        parity: {
            kind: sp.factor(
                formula[key].subs({U: 0, V: 0})
            )
            for kind, key in [
                ("numerator", "numerator"),
                ("denominator", "denominator"),
            ]
        }
        for parity, formula in formulas.items()
    }

    finite = []
    finite_strict = []

    for maximum in range(19, 48):
        parity = "even" if maximum % 2 == 0 else "odd"
        numerator, denominator = specialized_polynomials(
            formulas[parity],
            maximum,
        )
        numerator_certificate = a75.strict_bernstein_sign(numerator)
        denominator_certificate = a75.strict_bernstein_sign(denominator)
        multiplier_sign = (
            numerator_certificate["sign"]
            * denominator_certificate["sign"]
        )

        finite_strict.append(
            numerator_certificate["sign"] != 0
            and denominator_certificate["sign"] != 0
        )
        finite.append({
            "maximum": maximum,
            "parity": parity,
            "numerator_degree": numerator.degree(),
            "denominator_degree": denominator.degree(),
            "numerator": numerator_certificate,
            "denominator": denominator_certificate,
            "multiplier_sign": multiplier_sign,
        })

    expected = {
        maximum: (
            (1, 1, 1)
            if maximum <= 22
            else (-1, 1, -1)
            if maximum <= 34
            else (-1, -1, 1)
        )
        for maximum in range(19, 48)
    }
    observed = {
        item["maximum"]: (
            item["numerator"]["sign"],
            item["denominator"]["sign"],
            item["multiplier_sign"],
        )
        for item in finite
    }

    asymptotic = {}
    asymptotic_gates = []

    for parity, formula in formulas.items():
        asymptotic[parity] = {}
        for kind, key in [
            ("numerator", "numerator"),
            ("denominator", "denominator"),
        ]:
            remainder = a75.remainder_bound(
                formula[key],
                ASYMPTOTIC_H0,
            )
            lower_bound = leading_lower_bound(
                parity,
                kind,
                ASYMPTOTIC_H0,
            )
            ratio = sp.factor(
                remainder["upper_bound"] / lower_bound
            )
            entry = {
                "leading_term": str(leading[parity][kind]),
                "leading_absolute_lower_bound": str(lower_bound),
                "remainder_absolute_upper_bound": str(
                    remainder["upper_bound"]
                ),
                "remainder_to_leading_ratio": str(ratio),
                "remainder_to_leading_decimal": str(
                    sp.N(ratio, 50)
                ),
                "remainder_term_count": remainder["term_count"],
                "largest_one_step_decay_ratio": str(
                    remainder["largest_one_step_decay_ratio"]
                ),
                "strictly_below_leading": bool(ratio < 1),
                "decays_for_all_h_at_least_24": bool(
                    remainder["largest_one_step_decay_ratio"] < 1
                ),
            }
            asymptotic[parity][kind] = entry
            asymptotic_gates.append(
                entry["strictly_below_leading"]
                and entry["decays_for_all_h_at_least_24"]
            )

    # Agreement with independently reconstructed A76 M=21,22,23 Cramer signs.
    a76_cramer = a76["actual_Cramer_certificates"]
    agreement = {
        str(maximum): bool(
            observed[maximum][0]
            == a76_cramer[str(maximum)][
                "numerator_certificate"
            ]["sign"]
            and observed[maximum][1]
            == a76_cramer[str(maximum)][
                "denominator_certificate"
            ]["sign"]
        )
        for maximum in [21, 22, 23]
    }

    gates = {
        "A76_interval_certificate_passed": bool(
            all(a76["gates"].values())
        ),
        "parity_formulas_agree_with_A76_M21_M23": bool(
            all(agreement.values())
        ),
        "all_29_finite_Bernstein_certificates_strict": bool(
            len(finite) == 29 and all(finite_strict)
        ),
        "finite_pattern_matches_two_bifurcations": bool(
            observed == expected
        ),
        "all_four_asymptotic_bounds_strict": bool(
            len(asymptotic_gates) == 4
            and all(asymptotic_gates)
        ),
        "gamma_plus_positive_for_M19_M22": bool(
            all(observed[m][2] == 1 for m in range(19, 23))
        ),
        "gamma_plus_negative_for_M23_M34": bool(
            all(observed[m][2] == -1 for m in range(23, 35))
        ),
        "gamma_plus_positive_for_every_M_at_least_35": bool(
            all(observed[m][2] == 1 for m in range(35, 48))
            and all(asymptotic_gates)
        ),
    }

    verdict = (
        "PASS_FIXED_ACTUAL_FAMILY_DOUBLE_BIFURCATION"
        if all(gates.values())
        else "FAIL_A77_FIXED_FAMILY_PARITY_AUDIT"
    )

    result = {
        "audit": "A77_FIXED_ACTUAL_FAMILY_PARITY_ORIENTATION",
        "interval": {
            "s_lower": str(LOWER),
            "s_upper": str(UPPER),
            "alpha_lower_decimal": str(
                sp.N(-sp.log(UPPER, 2), 50)
            ),
            "alpha_upper_decimal": str(
                sp.N(-sp.log(LOWER, 2), 50)
            ),
        },
        "family": (
            "P={0,5,6,M}, Q={1,floor(M/2),floor(M/2)+1}, "
            "active={alpha+,beta-,gamma+}"
        ),
        "parity_formulas": {
            parity: {
                "numerator": str(formula["numerator"]),
                "denominator": str(formula["denominator"]),
                "leading_numerator": str(
                    leading[parity]["numerator"]
                ),
                "leading_denominator": str(
                    leading[parity]["denominator"]
                ),
            }
            for parity, formula in formulas.items()
        },
        "finite_Bernstein_certificates": finite,
        "asymptotic_certificates": asymptotic,
        "support_size_theorem": {
            "numerator_sign": {
                "M19_M22": "positive",
                "all_M_at_least_23": "negative",
            },
            "denominator_sign": {
                "M19_M34": "positive",
                "all_M_at_least_35": "negative",
            },
            "multiplier_sign": {
                "M19_M22": "positive",
                "M23_M34": "negative",
                "all_M_at_least_35": "positive",
            },
            "formal_statement": (
                "For the fixed {5,6} contact family on the declared "
                "interval, gamma-plus is positive for M=19,...,22, "
                "negative for M=23,...,34, and positive for every "
                "integer M>=35."
            ),
            "mechanism": (
                "The 22->23 bifurcation is numerator-driven. "
                "The 34->35 re-entry is determinant-driven."
            ),
        },
        "agreement_with_A76": agreement,
        "gates": gates,
        "verdict": verdict,
        "boundary": (
            "This theorem concerns a fixed contact family. It does not "
            "assert that the family remains primal feasible or optimal "
            "after M=23."
        ),
    }

    output = HERE / "a77_fixed_family_parity_results.json"
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    cache = {
        "even": {
            "numerator": str(formulas["even"]["numerator"]),
            "denominator": str(formulas["even"]["denominator"]),
        },
        "odd": {
            "numerator": str(formulas["odd"]["numerator"]),
            "denominator": str(formulas["odd"]["denominator"]),
        },
    }
    (HERE / "a77_fixed_family_parity_formula_cache.json").write_text(
        json.dumps(cache, indent=2),
        encoding="utf-8",
    )

    print(json.dumps({
        "audit": result["audit"],
        "gate_count": len(gates),
        "pass_count": sum(gates.values()),
        "multiplier_sign": result[
            "support_size_theorem"
        ]["multiplier_sign"],
        "asymptotic_start": {
            "h": ASYMPTOTIC_H0,
            "even_M": 2 * ASYMPTOTIC_H0,
            "odd_M": 2 * ASYMPTOTIC_H0 + 1,
        },
        "failed_gates": [
            name for name, value in gates.items() if not value
        ],
        "verdict": verdict,
    }, indent=2))

    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
