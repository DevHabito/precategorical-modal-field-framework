#!/usr/bin/env python3
"""Regression for the regular-curved null-joint coefficient.

The curved d>=4 theorem gives

    C_curved =
        2^m * omega_{d-2} / V_D^2
        * J_d
        * (a_m L_m)^2
        * Gamma(a_m)^2 / Gamma(2 a_m + 1),

where m=d/2 and

    J_d = int_Sigma chi^(m+1) dA.

For the unit flat Minkowski diamond:

    V_D = 2 S_{d-2} / [d(d-1)],
    chi = 2,
    Area(Sigma) = S_{d-2}.

This script checks that the curved formula exactly reproduces the independent
flat formula already used in the repository.

The numerical quadrature is a regression only; the algebraic equality is
shown in the theorem/audit documents.
"""

from __future__ import annotations

import argparse
import math

from scipy.integrate import quad
from scipy.special import gamma


def sphere_area(k: int) -> float:
    return (
        2.0
        * math.pi ** ((k + 1.0) / 2.0)
        / gamma((k + 1.0) / 2.0)
    )


def ball_volume(k: int) -> float:
    return (
        math.pi ** (k / 2.0)
        / gamma(k / 2.0 + 1.0)
    )


def one_side_L(d: int) -> float:
    m = d / 2.0
    a = 1.0 + 1.0 / m

    value, _ = quad(
        lambda t:
            ((1.0 + t) ** m - t**m) ** (-a),
        0.0,
        math.inf,
        epsabs=1.0e-12,
        epsrel=1.0e-12,
        limit=500,
    )

    return value / (m + 1.0)


def flat_reference_coefficient(d: int) -> float:
    m = d / 2.0
    a = 1.0 + 1.0 / m
    L = one_side_L(d)

    return (
        2.0 ** (d - 1)
        * d**2
        * (d - 1.0) ** 2
        / (d - 2.0)
        * sphere_area(d - 3)
        / sphere_area(d - 2)
        * (a * L) ** 2
        * gamma(a) ** 2
        / gamma(2.0 * a + 1.0)
    )


def curved_formula_on_flat_joint(d: int) -> float:
    m = d / 2.0
    a = 1.0 + 1.0 / m
    L = one_side_L(d)

    volume_diamond = (
        2.0
        * sphere_area(d - 2)
        / (d * (d - 1.0))
    )

    joint_optical = (
        2.0 ** (m + 1.0)
        * sphere_area(d - 2)
    )

    return (
        2.0**m
        * ball_volume(d - 2)
        / volume_diamond**2
        * joint_optical
        * (a * L) ** 2
        * gamma(a) ** 2
        / gamma(2.0 * a + 1.0)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=12)
    args = parser.parse_args()

    for d in range(4, args.max_d + 1):
        reference = flat_reference_coefficient(d)
        curved = curved_formula_on_flat_joint(d)

        if not math.isclose(
            reference,
            curved,
            rel_tol=1.0e-11,
            abs_tol=1.0e-12,
        ):
            raise AssertionError(
                {
                    "d": d,
                    "reference": reference,
                    "curved": curved,
                }
            )

        print(
            {
                "d": d,
                "flat_reference": reference,
                "curved_on_flat": curved,
                "ratio": curved / reference,
            }
        )

    d4 = curved_formula_on_flat_joint(4)

    if not math.isclose(
        d4,
        3.0 * math.pi,
        rel_tol=1.0e-11,
        abs_tol=1.0e-12,
    ):
        raise AssertionError(
            {
                "d4": d4,
                "3pi": 3.0 * math.pi,
            }
        )

    print(
        "PASS: curved joint formula reproduces the flat all-dimensional coefficient."
    )


if __name__ == "__main__":
    main()
