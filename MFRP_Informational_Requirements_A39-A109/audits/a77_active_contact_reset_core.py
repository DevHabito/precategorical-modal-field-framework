#!/usr/bin/env python3
"""Shared exact helpers for A77 active contact reset."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

import sympy as sp


HERE = Path(__file__).resolve().parent
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"

S0 = sp.Rational(131, 1000)
LOWER = sp.Rational(13, 100)
UPPER = sp.Rational(33, 250)
T = sp.Symbol("t")


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def normalized_epsilon(maximum: int) -> sp.Rational:
    h = maximum // 2
    if maximum % 2 == 0:
        return sp.Rational(1, 1875 * 2**h)
    return sp.Rational(1, 2500 * 2**h)


def positive_indices(
    maximum: int,
    contact: int,
) -> tuple[int, ...]:
    count = maximum + 1
    h = maximum // 2
    return (
        0,
        contact,
        contact + 1,
        maximum,
        count + 1,
        count + h,
        count + h + 1,
        2 * count,
    )


def selected_contact(maximum: int) -> int:
    if maximum == 23:
        return 5
    if maximum in {24, 25}:
        return 6
    raise ValueError(maximum)


def selected_gamma_sign(maximum: int) -> int:
    if maximum == 23:
        return -1
    if maximum in {24, 25}:
        return 1
    raise ValueError(maximum)


def signature(
    maximum: int,
    contact: int | None = None,
    gamma_sign: int | None = None,
) -> dict[str, Any]:
    h = maximum // 2
    if contact is None:
        contact = selected_contact(maximum)
    if gamma_sign is None:
        gamma_sign = selected_gamma_sign(maximum)

    return {
        "p_support": [0, contact, contact + 1, maximum],
        "q_support": [1, h, h + 1],
        "active_observations": [
            ["alpha", 1],
            ["beta", -1],
            ["gamma", gamma_sign],
        ],
    }


def build_branch(
    a67,
    maximum: int,
    contact: int,
    gamma_sign: int,
):
    return a67.build_branch(
        maximum,
        sp.Rational(maximum, 2),
        normalized_epsilon(maximum),
        4,
        positive_indices(maximum, contact),
        (
            ("alpha", 1),
            ("beta", -1),
            ("gamma", gamma_sign),
        ),
    )


def condition_expression(
    branch: dict[str, Any],
    name: str,
) -> sp.Expr:
    return next(
        expression
        for current_name, expression in branch["conditions"]
        if current_name == name
    )


def bernstein_coefficients(
    polynomial: sp.Poly,
) -> list[sp.Rational]:
    degree = polynomial.degree()
    if degree <= 0:
        return [sp.Rational(polynomial.nth(0))]

    variable = polynomial.gens[0]
    transformed = sp.Poly(
        sp.expand(
            polynomial.as_expr().subs(
                variable,
                LOWER + (UPPER - LOWER) * T,
            )
        ),
        T,
        domain=sp.QQ,
    )
    power = [
        transformed.nth(index)
        for index in range(degree + 1)
    ]
    return [
        sp.factor(
            sum(
                power[j]
                * sp.binomial(k, j)
                / sp.binomial(degree, j)
                for j in range(k + 1)
            )
        )
        for k in range(degree + 1)
    ]


def polynomial_sign(
    expression: sp.Expr,
    variable: sp.Symbol,
) -> dict[str, Any]:
    polynomial = sp.Poly(
        expression,
        variable,
        domain=sp.QQ,
    )
    coefficients = bernstein_coefficients(polynomial)

    if all(value > 0 for value in coefficients):
        sign = 1
    elif all(value < 0 for value in coefficients):
        sign = -1
    else:
        sign = 0

    return {
        "sign": sign,
        "degree": polynomial.degree(),
        "coefficient_count": len(coefficients),
        "minimum_absolute_coefficient": str(
            min(abs(value) for value in coefficients)
        ),
        "maximum_absolute_coefficient": str(
            max(abs(value) for value in coefficients)
        ),
    }


def rational_sign(
    expression: sp.Expr,
    variable: sp.Symbol,
) -> dict[str, Any]:
    numerator, denominator = sp.fraction(sp.cancel(expression))
    numerator_certificate = polynomial_sign(numerator, variable)
    denominator_certificate = polynomial_sign(denominator, variable)
    return {
        "sign": (
            numerator_certificate["sign"]
            * denominator_certificate["sign"]
        ),
        "numerator": numerator_certificate,
        "denominator": denominator_certificate,
    }


def gamma_plus_determinants(
    maximum: int,
    contact: int,
) -> dict[str, sp.Expr]:
    h = maximum // 2
    mean = sp.Rational(maximum, 2)
    epsilon = normalized_epsilon(maximum)
    p_points = [0, contact, contact + 1, maximum]
    q_points = [1, h, h + 1]
    variable = sp.Symbol("s")

    def target(x: int) -> sp.Rational:
        return sp.Rational(1, 2**x)

    def beta(x: int) -> sp.Rational:
        return sp.Rational(1, 2 ** (3 * x))

    def gamma(x: int) -> sp.Rational:
        return sp.Rational(1, 2 ** (4 * x))

    rows = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [*p_points, 0, 0, 0, -mean],
        [0, 0, 0, 0, *q_points, -mean],
        [
            0, 0, 0, 0,
            *[target(x) for x in q_points],
            0,
        ],
        [
            *[variable**x for x in p_points],
            *[-variable**x for x in q_points],
            -2 * epsilon,
        ],
        [
            *[-beta(x) for x in p_points],
            *[beta(x) for x in q_points],
            -2 * epsilon,
        ],
        [
            *[gamma(x) for x in p_points],
            *[-gamma(x) for x in q_points],
            -2 * epsilon,
        ],
    ]
    basis = sp.Matrix(rows)
    objective = sp.Matrix([
        *[target(x) for x in p_points],
        0, 0, 0, 0,
    ])
    numerator_basis = basis.copy()
    numerator_basis[7, :] = objective.T

    return {
        "variable": variable,
        "numerator": sp.factor(numerator_basis.det()),
        "denominator": sp.factor(basis.det()),
    }


def generate_neighbors(maximum: int) -> list[dict[str, Any]]:
    reference = signature(maximum)
    p_reference = set(reference["p_support"])
    q_reference = set(reference["q_support"])
    active_reference = tuple(
        tuple(item)
        for item in reference["active_observations"]
    )

    candidates: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()

    def add(
        kind: str,
        detail: Any,
        p_support: set[int],
        q_support: set[int],
        active_observations: tuple[tuple[str, int], ...],
        is_reference: bool = False,
    ) -> None:
        key = (
            tuple(sorted(p_support)),
            tuple(sorted(q_support)),
            active_observations,
        )
        if key in seen:
            return
        seen.add(key)
        candidates.append({
            "kind": kind,
            "detail": detail,
            "p_support": sorted(p_support),
            "q_support": sorted(q_support),
            "active_observations": [
                list(item) for item in active_observations
            ],
            "is_reference": is_reference,
        })

    add(
        "reference",
        None,
        p_reference,
        q_reference,
        active_reference,
        is_reference=True,
    )

    for leaving in sorted(p_reference):
        for entering in range(maximum + 1):
            if entering not in p_reference:
                add(
                    "p_contact_exchange",
                    {"leaving": leaving, "entering": entering},
                    (p_reference - {leaving}) | {entering},
                    q_reference,
                    active_reference,
                )

    for leaving in sorted(q_reference):
        for entering in range(maximum + 1):
            if entering not in q_reference:
                add(
                    "q_contact_exchange",
                    {"leaving": leaving, "entering": entering},
                    p_reference,
                    (q_reference - {leaving}) | {entering},
                    active_reference,
                )

    for channel in ["beta", "gamma"]:
        flipped = tuple(
            (
                name,
                -sign if name == channel else sign,
            )
            for name, sign in active_reference
        )
        add(
            "completion_band_sign_flip",
            {"channel": channel},
            p_reference,
            q_reference,
            flipped,
        )

    for channel in ["beta", "gamma"]:
        deactivated = tuple(
            item
            for item in active_reference
            if item[0] != channel
        )
        for leaving in sorted(p_reference):
            add(
                "deactivate_band_remove_p_contact",
                {"channel": channel, "leaving": leaving},
                p_reference - {leaving},
                q_reference,
                deactivated,
            )
        for leaving in sorted(q_reference):
            add(
                "deactivate_band_remove_q_contact",
                {"channel": channel, "leaving": leaving},
                p_reference,
                q_reference - {leaving},
                deactivated,
            )

    return candidates
