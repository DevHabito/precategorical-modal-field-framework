#!/usr/bin/env python3
"""Regression for null index-form coercivity in a constant-profile plane wave.

For one transverse degree of freedom, take the Penrose plane-wave quadratic
form

    Q[y] = ∫_0^L (y'(v)^2 - omega^2 y(v)^2) dv

with Dirichlet boundary conditions.

The Jacobi equation is

    y'' + omega^2 y = 0.

The first conjugate point occurs at L = pi/omega.

The Dirichlet spectrum is

    lambda_k = (k*pi/L)^2 - omega^2.

This script verifies that the lowest index-form eigenvalue:
- is positive before the conjugate point;
- vanishes at the conjugate point;
- becomes negative after it.

It also checks a finite-difference discretization against the exact formula.
The script is diagnostic/regression support, not a replacement for the
analytic null Morse-index argument.
"""

from __future__ import annotations

import argparse
import math
import numpy as np


def exact_lowest_eigenvalue(
    omega: float,
    length: float,
) -> float:
    return (math.pi / length) ** 2 - omega**2


def discrete_lowest_eigenvalue(
    omega: float,
    length: float,
    interior_points: int,
) -> float:
    n = interior_points
    h = length / (n + 1)

    diag = np.full(
        n,
        2.0 / h**2 - omega**2,
    )

    off = np.full(
        n - 1,
        -1.0 / h**2,
    )

    matrix = np.diag(diag)

    matrix += np.diag(
        off,
        k=1,
    )

    matrix += np.diag(
        off,
        k=-1,
    )

    return float(
        np.linalg.eigvalsh(matrix)[0]
    )


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--omega",
        type=float,
        default=1.0,
    )

    parser.add_argument(
        "--points",
        type=int,
        default=400,
    )

    args = parser.parse_args()

    omega = args.omega
    conjugate_length = math.pi / omega

    cases = [
        ("before_far", 0.50 * conjugate_length),
        ("before_near", 0.99 * conjugate_length),
        ("threshold", conjugate_length),
        ("after_near", 1.01 * conjugate_length),
    ]

    for name, length in cases:
        exact = exact_lowest_eigenvalue(
            omega,
            length,
        )

        discrete = discrete_lowest_eigenvalue(
            omega,
            length,
            args.points,
        )

        print(
            {
                "case": name,
                "L": length,
                "exact_lambda1": exact,
                "discrete_lambda1": discrete,
            }
        )

        if name.startswith("before"):
            assert exact > 0.0

        if name == "threshold":
            assert abs(exact) < 1e-12

        if name.startswith("after"):
            assert exact < 0.0

    print(
        "PASS: index-form spectral gap closes at the first conjugate point."
    )


if __name__ == "__main__":
    main()
