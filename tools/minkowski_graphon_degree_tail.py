#!/usr/bin/env python3
"""Degree-tail and fixed-degree audit for Minkowski causal graphons.

Analytic results checked here:

    g_d(q) ~ C_d q^(4/d),

where

    C_d = d(d-1) Gamma(1+2/d)^2 / Gamma(1+4/d),

and, for each fixed graph degree j,

    E[D_j] ~ C_d (4/d) Gamma(j+4/d)/j! * n^(1-4/d).

In d=4 this becomes E[D_j] -> 3*pi for every fixed j.

SciPy quadrature is used only as a finite-n numerical regression.
"""

from __future__ import annotations

import argparse
import math

from scipy.integrate import dblquad


def tail_coefficient(d: int) -> float:
    return (
        d
        * (d - 1)
        * math.gamma(1.0 + 2.0 / d) ** 2
        / math.gamma(1.0 + 4.0 / d)
    )


def isolated_coefficient(d: int) -> float:
    return d * (d - 1) * math.gamma(1.0 + 2.0 / d) ** 2


def fixed_degree_coefficient(d: int, j: int) -> float:
    a = 4.0 / d
    return (
        tail_coefficient(d)
        * a
        * math.gamma(j + a)
        / math.factorial(j)
    )


def q_d(a: float, b: float, d: int) -> float:
    return (
        (a * (2.0 - b)) ** (d / 2.0)
        + (b * (2.0 - a)) ** (d / 2.0)
    ) / (2.0**d)


def density_ab(a: float, b: float, d: int) -> float:
    return (
        d
        * (d - 1)
        / 4.0
        * (1.0 - (a + b) / 2.0) ** (d - 2)
    )


def expected_degree_j(n: int, d: int, j: int) -> float:
    if j >= n:
        return 0.0

    prefactor = n * math.comb(n - 1, j)

    def integrand(b: float, a: float) -> float:
        q = q_d(a, b, d)
        return (
            density_ab(a, b, d)
            * q**j
            * (1.0 - q) ** (n - 1 - j)
        )

    value, _ = dblquad(
        integrand,
        0.0,
        2.0,
        lambda a: 0.0,
        lambda a: 2.0 - a,
        epsabs=1.0e-10,
        epsrel=1.0e-8,
    )
    return prefactor * value


def parse_int_list(text: str) -> list[int]:
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", type=int, default=4)
    parser.add_argument("--degrees", default="0,1,2,3")
    parser.add_argument("--ns", default="20,50,100,200")
    args = parser.parse_args()

    print(f"d={args.d}")
    print(f"C_d={tail_coefficient(args.d):.12f}")
    print(f"isolated coefficient={isolated_coefficient(args.d):.12f}")

    degrees = parse_int_list(args.degrees)
    for j in degrees:
        print(
            f"fixed-degree coefficient j={j}: "
            f"{fixed_degree_coefficient(args.d, j):.12f}"
        )

    for n in parse_int_list(args.ns):
        row = {"n": n}
        for j in degrees:
            row[f"E[D_{j}]"] = expected_degree_j(n, args.d, j)
        print(row)


if __name__ == "__main__":
    main()
