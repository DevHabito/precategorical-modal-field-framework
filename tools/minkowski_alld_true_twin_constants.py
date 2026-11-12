#!/usr/bin/env python3
"""Constants for the d>=4 comparable true-twin asymptotic.

For spacetime dimension d>=4, m=d/2 and

    F_d(epsilon) ~ C_edge(d) epsilon^(2+4/d),

with C_edge expressed through the convergent one-side integral

    L_m = 1/(m+1) int_0^infty
          ((1+t)^m - t^m)^(-(m+1)/m) dt.

Consequently

    E[T_n] ~ K_twin(d) n^(-4/d).

The script evaluates L_m and the two constants numerically.
For d=4 it recovers C_edge=3*pi and K_twin=9*pi.
"""

from __future__ import annotations

import argparse
import math

from scipy.integrate import quad
from scipy.special import gamma


def sphere_area(k: int) -> float:
    return 2.0 * math.pi ** ((k + 1.0) / 2.0) / gamma((k + 1.0) / 2.0)


def one_side_L(d: int) -> float:
    if d < 4:
        raise ValueError("The convergent joint integral used here requires d>=4.")

    m = d / 2.0
    a = (m + 1.0) / m

    def integrand(t: float) -> float:
        return ((1.0 + t) ** m - t**m) ** (-a)

    value, _ = quad(
        integrand,
        0.0,
        math.inf,
        epsabs=1.0e-12,
        epsrel=1.0e-12,
        limit=500,
    )
    return value / (m + 1.0)


def constants(d: int) -> dict[str, float | int]:
    if d < 4:
        raise ValueError("d must be >= 4")

    m = d / 2.0
    a = 1.0 + 1.0 / m
    beta = 2.0 * a
    L = one_side_L(d)

    c_single = d * (d - 1.0) / 4.0
    sphere_ratio = sphere_area(d - 3) / sphere_area(d - 2)

    angular_time_factor = (
        c_single**2
        * sphere_ratio
        / (m - 1.0)
    )

    scalar_step_factor = (
        (a * L) ** 2
        * 2.0 ** (d + 2)
        * gamma(a) ** 2
        / gamma(2.0 * a + 1.0)
    )

    c_edge = angular_time_factor * scalar_step_factor

    k_twin = (
        2.0 ** (d - 2)
        * d**2
        * (d - 1.0) ** 2
        / (d - 2.0)
        * sphere_ratio
        * (a * L * gamma(a)) ** 2
    )

    # Equivalent Laplace-transfer expression.
    k_twin_check = c_edge * gamma(beta + 1.0) / 2.0

    if not math.isclose(k_twin, k_twin_check, rel_tol=1.0e-10, abs_tol=1.0e-12):
        raise AssertionError((k_twin, k_twin_check))

    return {
        "d": d,
        "m": m,
        "beta": beta,
        "L_m": L,
        "C_edge": c_edge,
        "K_twin": k_twin,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-d", type=int, default=4)
    parser.add_argument("--max-d", type=int, default=10)
    args = parser.parse_args()

    for d in range(args.min_d, args.max_d + 1):
        row = constants(d)
        print(row)

    d4 = constants(4)
    assert math.isclose(d4["C_edge"], 3.0 * math.pi, rel_tol=1.0e-10)
    assert math.isclose(d4["K_twin"], 9.0 * math.pi, rel_tol=1.0e-10)
    print("PASS: d=4 recovers C_edge=3*pi and K_twin=9*pi")


if __name__ == "__main__":
    main()
