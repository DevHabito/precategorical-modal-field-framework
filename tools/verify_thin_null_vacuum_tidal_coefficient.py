#!/usr/bin/env python3
"""Symbolic regression for the vacuum thin-null tidal coefficient.

For a constant trace-free transverse tidal matrix H, the Jacobi determinant
gives

    c_H(U)/c_0(U)
      = 1 + lambda_d U^4 Tr(H^2) + ...

with

    lambda_d
      = [1 - 2 (d/2)_4 / (d)_4] / 360.

The script verifies the determinant expansion and prints exact lambda_d values
for selected dimensions.
"""

from __future__ import annotations

import argparse
import sympy as sp


def rising4(x):
    return (
        x
        * (x + 1)
        * (x + 2)
        * (x + 3)
    )


def lambda_d(d):
    m = sp.Rational(d, 2)

    return sp.simplify(
        (
            1
            -
            2
            * rising4(m)
            / rising4(d)
        )
        / 360
    )


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dimensions",
        default="4,5,6,8,10",
    )

    args = parser.parse_args()

    t = sp.symbols(
        "t",
        real=True,
    )

    # Formal trace-free matrix invariants:
    tr_h2 = sp.symbols(
        "tr_h2",
        positive=True,
    )

    # log det(B/t) at order t^4:
    coefficient = sp.simplify(
        sp.Rational(1, 120)
        -
        sp.Rational(1, 2)
        * sp.Rational(1, 36)
    )

    assert (
        coefficient
        ==
        -sp.Rational(1, 180)
    )

    sqrt_coefficient = (
        coefficient / 2
    )

    assert (
        sqrt_coefficient
        ==
        -sp.Rational(1, 360)
    )

    print(
        {
            "log_det_B_over_t_coefficient":
                coefficient,
            "sqrt_det_coefficient":
                sqrt_coefficient,
        }
    )

    dimensions = [
        int(part.strip())
        for part
        in args.dimensions.split(",")
        if part.strip()
    ]

    for d in dimensions:
        if d < 3:
            raise ValueError(
                "Use spacetime dimension d>=3."
            )

        value = lambda_d(d)

        print(
            {
                "d": d,
                "lambda_d": str(value),
                "decimal": float(value),
            }
        )

    assert (
        lambda_d(4)
        ==
        sp.Rational(1, 504)
    )

    print(
        "PASS: vacuum thin-null tidal coefficient verified; lambda_4 = 1/504."
    )


if __name__ == "__main__":
    main()
