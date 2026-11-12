#!/usr/bin/env python3
"""Audit the curved null-edge coefficient.

Checks two things:

1. optical-gauge invariance under
       a' = lambda a,
       b' = mu b;

2. exact reduction of the curved edge formula to the previously derived
   flat Minkowski true-twin constant for d=4,...,10.

The script is a regression.  The accompanying audit contains the algebraic
cancellation proof.
"""

from __future__ import annotations

import math

import scipy.integrate as integrate
import scipy.special as special


def sphere_area(n: int) -> float:
    return 2.0 * math.pi ** ((n + 1) / 2.0) / special.gamma(
        (n + 1) / 2.0
    )


def ball_volume(n: int) -> float:
    return math.pi ** (n / 2.0) / special.gamma(n / 2.0 + 1.0)


def L_m(m: float) -> float:
    def integrand(t: float) -> float:
        return (
            (1.0 + t) ** m - t**m
        ) ** (-(m + 1.0) / m)

    value, _ = integrate.quad(
        integrand,
        0.0,
        math.inf,
        epsabs=1.0e-11,
        epsrel=1.0e-11,
        limit=500,
    )
    return value / (m + 1.0)


def flat_known_constant(d: int) -> float:
    m = d / 2.0
    a = 1.0 + 2.0 / d
    lm = L_m(m)

    return (
        2.0 ** (d - 2)
        * d**2
        * (d - 1) ** 2
        / (d - 2)
        * sphere_area(d - 3)
        / sphere_area(d - 2)
        * (
            a
            * lm
            * special.gamma(a)
        )
        ** 2
    )


def curved_formula_on_flat_diamond(d: int) -> float:
    m = d / 2.0
    a = 1.0 + 2.0 / d
    lm = L_m(m)

    v_diamond = (
        2.0
        * sphere_area(d - 2)
        / (d * (d - 1))
    )

    # For a=1-r+t, b=1-r-t at the flat null joint:
    # ds^2 = da db + dOmega^2, hence |Omega|^2 = 1/2
    # in the convention -2 Omega^2 da db.
    omega_null = 1.0 / math.sqrt(2.0)

    # Normalized endpoint interval volume:
    # V(p,x)/V_D ~ 2^{-d/2} a^{d/2}.
    c_plus = 2.0 ** (-m)
    c_minus = c_plus

    pair_density = (
        ball_volume(d - 2)
        * 2.0 ** (m - 1.0)
        * omega_null ** (d + 2)
        / v_diamond**2
    )

    scalar = (
        (a * lm) ** 2
        * c_plus ** (-a)
        * c_minus ** (-a)
        * special.gamma(a) ** 2
        / special.gamma(2.0 * a + 1.0)
    )

    edge_area = sphere_area(d - 2)

    c_edge = (
        2.0
        * edge_area
        * pair_density
        * scalar
    )

    beta = 2.0 + 4.0 / d

    return (
        0.5
        * c_edge
        * special.gamma(beta + 1.0)
    )


def gauge_multiplier(
    d: int,
    lambda_a: float,
    lambda_b: float,
) -> float:
    """Net multiplier of A_d*S_d under optical rescaling."""
    m = d / 2.0
    a = 1.0 + 1.0 / m

    # Omega'^2 = Omega^2/(lambda_a lambda_b)
    pair = (
        lambda_a
        * lambda_b
    ) ** (-(d + 2.0) / 2.0)

    # c_+' = c_+ lambda_a^{-m},
    # so c_+'^{-a} contributes lambda_a^{m a}.
    scalar = (
        lambda_a ** (m * a)
        * lambda_b ** (m * a)
    )

    return pair * scalar


def main() -> None:
    for d in range(4, 11):
        known = flat_known_constant(d)
        curved = curved_formula_on_flat_diamond(d)

        ratio = curved / known

        print(
            {
                "d": d,
                "known_flat_K": known,
                "curved_formula_flat_K": curved,
                "ratio": ratio,
            }
        )

        assert math.isclose(
            ratio,
            1.0,
            rel_tol=3.0e-9,
            abs_tol=3.0e-9,
        )

        for lambda_a, lambda_b in (
            (2.0, 3.0),
            (0.4, 1.7),
            (5.5, 0.2),
        ):
            multiplier = gauge_multiplier(
                d,
                lambda_a,
                lambda_b,
            )

            assert math.isclose(
                multiplier,
                1.0,
                rel_tol=2.0e-12,
                abs_tol=2.0e-12,
            )

    expected_d4 = 9.0 * math.pi
    actual_d4 = curved_formula_on_flat_diamond(4)

    assert math.isclose(
        actual_d4,
        expected_d4,
        rel_tol=2.0e-10,
        abs_tol=2.0e-10,
    )

    print(
        "PASS: optical-gauge invariance and flat constant reduction verified."
    )


if __name__ == "__main__":
    main()
