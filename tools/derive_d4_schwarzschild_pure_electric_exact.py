#!/usr/bin/env python3
"""Exact weak-field Schwarzschild calibration of the d=4 vacuum response.

The calculation keeps terms through O(m^2 tau^4), where

    m   = M / r0,
    tau = T / r0.

It expands the Schwarzschild optical geodesic/Jacobi system as a formal
bivariate series, constructs the parent-volume and intrinsic edge factors,
performs the angular integrals exactly, and extracts the purely electric
vacuum coefficient a4.

No floating-point arithmetic is used in the coefficient derivation.
"""

from __future__ import annotations

from collections import defaultdict
import sympy as sp

MAX_M = 2
MAX_T = 6
mu, x = sp.symbols("mu x", real=True)

Poly = dict[tuple[int, int], sp.Expr]


def clean(poly: Poly) -> Poly:
    out: Poly = {}
    for (im, it), value in poly.items():
        if im <= MAX_M and it <= MAX_T and value != 0:
            value = sp.cancel(value)
            if value != 0:
                out[(im, it)] = value
    return out


def const(value: sp.Expr | int) -> Poly:
    return {(0, 0): sp.sympify(value)}


def m_monomial() -> Poly:
    return {(1, 0): sp.Integer(1)}


def add(left: Poly, right: Poly) -> Poly:
    acc: defaultdict[tuple[int, int], sp.Expr] = defaultdict(
        lambda: sp.Integer(0)
    )
    for key, value in left.items():
        acc[key] += value
    for key, value in right.items():
        acc[key] += value
    return clean(dict(acc))


def neg(poly: Poly) -> Poly:
    return {key: -value for key, value in poly.items()}


def sub(left: Poly, right: Poly) -> Poly:
    return add(left, neg(right))


def scale(poly: Poly, factor: sp.Expr | int) -> Poly:
    factor = sp.sympify(factor)
    return clean({key: factor * value for key, value in poly.items()})


def mul(left: Poly, right: Poly) -> Poly:
    acc: defaultdict[tuple[int, int], sp.Expr] = defaultdict(
        lambda: sp.Integer(0)
    )
    for (im, it), a in left.items():
        for (jm, jt), b in right.items():
            if im + jm <= MAX_M and it + jt <= MAX_T:
                acc[(im + jm, it + jt)] += a * b
    return clean(dict(acc))


def int_power(poly: Poly, power: int) -> Poly:
    out = const(1)
    for _ in range(power):
        out = mul(out, poly)
    return out


def inverse(poly: Poly) -> Poly:
    scalar = poly.get((0, 0), sp.Integer(0))
    if scalar == 0:
        raise ValueError("series has zero scalar constant")

    q = sub(scale(poly, 1 / scalar), const(1))
    out = const(1)
    term = const(1)

    for _ in range(1, MAX_M + MAX_T + 3):
        term = mul(term, neg(q))
        if not term:
            break
        out = add(out, term)

    return scale(out, 1 / scalar)


def binomial_power(poly: Poly, exponent: sp.Rational) -> Poly:
    scalar = poly.get((0, 0), sp.Integer(0))
    if scalar == 0:
        raise ValueError("series has zero scalar constant")

    q = sub(scale(poly, 1 / scalar), const(1))
    out = const(1)
    term = const(1)

    for order in range(1, MAX_M + MAX_T + 3):
        term = mul(term, q)
        if not term:
            break
        out = add(out, scale(term, sp.binomial(exponent, order)))

    return scale(out, scalar**exponent)


def s_coeff(poly: Poly, degree: int) -> list[sp.Expr]:
    return [
        poly.get((im, degree), sp.Integer(0))
        for im in range(MAX_M + 1)
    ]


def set_s_coeff(
    poly: Poly,
    degree: int,
    values: list[sp.Expr],
) -> Poly:
    out = dict(poly)
    for im, value in enumerate(values):
        if value != 0:
            out[(im, degree)] = sp.cancel(value)
    return clean(out)


def evaluate_scaled(poly: Poly, factor: sp.Expr) -> Poly:
    return clean(
        {
            (im, degree): sp.expand(value * factor**degree)
            for (im, degree), value in poly.items()
        }
    )


def divide_by_T(poly: Poly, power: int) -> Poly:
    out: Poly = {}
    for (im, degree), value in poly.items():
        if degree < power:
            if value != 0:
                raise ValueError(
                    "series is not divisible by requested T power"
                )
        else:
            out[(im, degree - power)] = value
    return clean(out)


def integrate_coefficients(
    poly: Poly,
    variable: sp.Symbol,
) -> Poly:
    out: Poly = {}
    for key, value in poly.items():
        integrated = sp.integrate(
            sp.expand(value),
            (variable, -1, 1),
        )
        if integrated != 0:
            out[key] = sp.simplify(integrated)
    return clean(out)


def integrate_unit_interval(poly: Poly) -> Poly:
    out: Poly = {}
    for key, value in poly.items():
        integrated = sp.integrate(
            sp.expand(value),
            (x, 0, 1),
        )
        if integrated != 0:
            out[key] = sp.simplify(integrated)
    return clean(out)


def build_optical_series() -> tuple[
    Poly,
    Poly,
    Poly,
    Poly,
    Poly,
]:
    """Return r(s), j_parallel, k_parallel, j_perp, k_perp."""
    one = const(1)
    m = m_monomial()

    ell2 = scale(
        inverse(sub(one, scale(m, 2))),
        1 - mu**2,
    )

    r = const(1)
    v = const(mu)
    j1: Poly = {}
    p1 = const(1)
    k1 = const(1)
    q1: Poly = {}
    j2: Poly = {}
    p2 = const(1)
    k2 = const(1)
    q2: Poly = {}

    states = [
        r,
        v,
        j1,
        p1,
        k1,
        q1,
        j2,
        p2,
        k2,
        q2,
    ]

    for degree in range(MAX_T):
        (
            r,
            v,
            j1,
            p1,
            k1,
            q1,
            j2,
            p2,
            k2,
            q2,
        ) = states

        r_inv = inverse(r)
        r_inv2 = mul(r_inv, r_inv)
        r_inv3 = mul(r_inv2, r_inv)
        r_inv4 = mul(r_inv2, r_inv2)

        a = sub(one, scale(mul(m, r_inv), 2))
        one_minus_3m_over_r = sub(
            one,
            scale(mul(m, r_inv), 3),
        )

        k_rad = mul(
            m,
            mul(
                sub(scale(m, 3), scale(r, 2)),
                r_inv4,
            ),
        )
        k_tan = mul(
            m,
            mul(
                sub(scale(r, 4), scale(m, 9)),
                r_inv4,
            ),
        )

        angular_speed2 = mul(
            ell2,
            mul(a, r_inv2),
        )
        k_perp = add(
            mul(mul(v, v), k_rad),
            mul(angular_speed2, k_tan),
        )

        rhs = [
            mul(a, v),
            mul(
                ell2,
                mul(
                    a,
                    mul(
                        one_minus_3m_over_r,
                        r_inv3,
                    ),
                ),
            ),
            p1,
            neg(mul(k_rad, j1)),
            q1,
            neg(mul(k_rad, k1)),
            p2,
            neg(mul(k_perp, j2)),
            q2,
            neg(mul(k_perp, k2)),
        ]

        next_states: list[Poly] = []
        for state, derivative in zip(states, rhs):
            values = [
                sp.cancel(
                    value / sp.Integer(degree + 1)
                )
                for value in s_coeff(
                    derivative,
                    degree,
                )
            ]
            next_states.append(
                set_s_coeff(
                    state,
                    degree + 1,
                    values,
                )
            )

        states = next_states

    (
        r,
        _v,
        j1,
        _p1,
        k1,
        _q1,
        j2,
        _p2,
        k2,
        _q2,
    ) = states

    return r, j1, k1, j2, k2


def derive() -> tuple[Poly, Poly, Poly]:
    one = const(1)
    m = m_monomial()

    r, j1, k1, j2, k2 = build_optical_series()

    a_s = sub(
        one,
        scale(mul(m, inverse(r)), 2),
    )

    a_x = evaluate_scaled(a_s, x)
    a_T = evaluate_scaled(a_s, sp.Integer(1))

    j1x = evaluate_scaled(j1, x)
    k1x = evaluate_scaled(k1, x)
    j2x = evaluate_scaled(j2, x)
    k2x = evaluate_scaled(k2, x)

    j1T = evaluate_scaled(j1, sp.Integer(1))
    k1T = evaluate_scaled(k1, sp.Integer(1))
    j2T = evaluate_scaled(j2, sp.Integer(1))
    k2T = evaluate_scaled(k2, sp.Integer(1))

    b1 = sub(
        mul(j1T, k1x),
        mul(k1T, j1x),
    )
    b2 = sub(
        mul(j2T, k2x),
        mul(k2T, j2x),
    )

    J1x = divide_by_T(j1x, 1)
    B1 = divide_by_T(b1, 1)
    J2x = divide_by_T(j2x, 1)
    B2 = divide_by_T(b2, 1)
    J1T = divide_by_T(j1T, 1)
    J2T = divide_by_T(j2T, 1)

    jacobi_ratio = mul(
        mul(
            mul(J1x, B1),
            mul(J2x, B2),
        ),
        inverse(mul(J1T, J2T)),
    )
    jacobi_ratio = scale(
        jacobi_ratio,
        1 / (x**2 * (1 - x) ** 2),
    )
    sqrt_ratio = binomial_power(
        jacobi_ratio,
        sp.Rational(1, 2),
    )

    a_x2 = mul(a_x, a_x)

    cbar = integrate_unit_interval(
        scale(
            mul(a_x2, sqrt_ratio),
            6 * x * (1 - x),
        )
    )

    parent_direction = integrate_unit_interval(
        scale(
            mul(a_x2, mul(J1x, J2x)),
            12 * (1 - x),
        )
    )

    edge_direction = mul(
        mul(
            int_power(a_T, 4),
            mul(J1T, J2T),
        ),
        int_power(inverse(cbar), 3),
    )

    vbar = scale(
        integrate_coefficients(
            parent_direction,
            mu,
        ),
        sp.Rational(1, 2),
    )
    ibar = scale(
        integrate_coefficients(
            edge_direction,
            mu,
        ),
        sp.Rational(1, 2),
    )
    kbar = mul(vbar, ibar)

    return vbar, ibar, kbar


def coefficient(
    poly: Poly,
    m_degree: int,
    t_degree: int,
) -> sp.Expr:
    return sp.simplify(
        poly.get(
            (m_degree, t_degree),
            sp.Integer(0),
        )
    )


def main() -> None:
    vbar, ibar, kbar = derive()

    expected_v_t4 = sp.Rational(17, 105)
    expected_i_t4 = sp.Rational(428, 1575)
    expected_k_t4 = sp.Rational(683, 1575)
    expected_a4 = sp.Rational(683, 9450)
    expected_b4 = sp.Rational(37, 1050)

    assert coefficient(vbar, 0, 0) == 1
    assert coefficient(vbar, 1, 0) == -4
    assert coefficient(vbar, 2, 0) == 4
    assert (
        coefficient(vbar, 2, 2)
        ==
        sp.Rational(2, 3)
    )
    assert coefficient(vbar, 2, 4) == expected_v_t4

    assert coefficient(ibar, 0, 0) == 1
    assert coefficient(ibar, 1, 0) == 4
    assert coefficient(ibar, 2, 0) == 12
    assert (
        coefficient(ibar, 2, 2)
        ==
        -sp.Rational(2, 3)
    )
    assert coefficient(ibar, 2, 4) == expected_i_t4

    assert coefficient(kbar, 1, 0) == 0
    assert coefficient(kbar, 2, 0) == 0
    assert coefficient(kbar, 2, 2) == 0
    assert coefficient(kbar, 2, 4) == expected_k_t4

    a4 = sp.simplify(expected_k_t4 / 6)
    b4 = sp.simplify(
        sp.Rational(508, 4725) - a4
    )

    assert a4 == expected_a4
    assert b4 == expected_b4

    print(
        {
            "Vbar_m2_tau2":
                str(coefficient(vbar, 2, 2)),
            "Vbar_m2_tau4":
                str(coefficient(vbar, 2, 4)),
            "Ibar_m2_tau2":
                str(coefficient(ibar, 2, 2)),
            "Ibar_m2_tau4":
                str(coefficient(ibar, 2, 4)),
            "Kratio_m2_tau4":
                str(coefficient(kbar, 2, 4)),
            "a4":
                str(a4),
            "b4_from_plane_wave_sum":
                str(b4),
        }
    )
    print(
        "PASS: exact Schwarzschild weak-field calibration "
        "gives a4 = 683/9450."
    )


if __name__ == "__main__":
    main()
