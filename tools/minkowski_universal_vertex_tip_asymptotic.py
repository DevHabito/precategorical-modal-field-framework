#!/usr/bin/env python3
"""Universal-vertex tip asymptotic in a Minkowski Alexandrov interval.

For an n-point iid sprinkling in M^d, a sampled event x is universal in the
unoriented comparability graph when all other n-1 events lie in its symmetric
causal-comparability region.

The exact expectation is

    E[U_n] = n E[Q_d(X)^(n-1)],

and the tip asymptotic derived in the accompanying note is

    E[U_n] ~ [2^d Gamma(d) / d^(d-1)] n^(1-d).

SciPy is used only for finite-n quadrature checks.
"""

from __future__ import annotations

import argparse
import math

from scipy.integrate import quad


def coefficient(d: int) -> float:
    return (2.0**d) * math.gamma(d) / (d ** (d - 1))


def q_tip_coordinates(s: float, rho: float, d: int) -> float:
    """Exact Q_d at t=-1+s, r=s*rho."""
    r = s * rho
    past_tau2 = s * s - r * r
    future_tau2 = (2.0 - s) ** 2 - r * r

    power = d / 2.0
    return (
        max(past_tau2, 0.0) ** power
        + max(future_tau2, 0.0) ** power
    ) / (2.0**d)


def expected_universal_vertices(n: int, d: int) -> float:
    """Exact two-tip integral, exploiting time-reflection symmetry."""
    prefactor = d * (d - 1) / 2.0

    def s_integrand(s: float) -> float:
        def rho_integrand(rho: float) -> float:
            q = q_tip_coordinates(s, rho, d)
            return (
                prefactor
                * s ** (d - 1)
                * rho ** (d - 2)
                * q ** (n - 1)
            )

        return quad(
            rho_integrand,
            0.0,
            1.0,
            epsabs=1.0e-13,
            epsrel=1.0e-10,
            limit=200,
        )[0]

    one_tip = quad(
        s_integrand,
        0.0,
        1.0,
        epsabs=1.0e-13,
        epsrel=1.0e-10,
        limit=300,
    )[0]

    return 2.0 * n * one_tip


def parse_int_list(text: str) -> list[int]:
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", type=int, default=4)
    parser.add_argument("--ns", default="10,20,50,100,200,500,1000")
    args = parser.parse_args()

    c = coefficient(args.d)
    print(f"d={args.d}")
    print(f"asymptotic coefficient={c:.12f}")

    for n in parse_int_list(args.ns):
        value = expected_universal_vertices(n, args.d)
        scaled = value * n ** (args.d - 1)
        print(
            f"n={n:>6d}  E[U_n]={value:.12e}  "
            f"n^(d-1)E[U_n]={scaled:.12f}"
        )


if __name__ == "__main__":
    main()
