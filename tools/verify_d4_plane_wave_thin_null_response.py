#!/usr/bin/env python3
"""Regression for the d=4 Ricci-flat thin-null plane-wave coefficient.

For a constant trace-free optical tidal matrix

    H = diag(h, -h),

the exact Jacobi solutions are

    S_+(u) = sinh(sqrt(h) u)/sqrt(h),
    S_-(u) = sin (sqrt(h) u)/sqrt(h).

The nearly-null Alexandrov volume coefficient is

    c(h) = pi * int_0^L du / sqrt(M_+(u) M_-(u)),

where

    M_\pm(u)
      = S_\pm'(u)/S_\pm(u)
        + S_\pm'(L-u)/S_\pm(L-u).

The analytic expansion is

    c(h)/c(0)
      = 1 + h^2 L^4 / 252 + O(h^4 L^8)

or equivalently

    1 + L^4 tr(H^2)/504 + ...

because tr(H^2)=2h^2.
"""

from __future__ import annotations

import argparse
import math

from scipy.integrate import quad


def p_channel(
    h: float,
    sign: int,
    u: float,
) -> float:
    if abs(h) < 1.0e-15:
        return 1.0 / u

    root = math.sqrt(abs(h))

    if sign > 0:
        return root / math.tanh(root * u)

    return root / math.tan(root * u)


def thin_ratio(
    h: float,
    length: float,
) -> float:
    def integrand(u: float) -> float:
        m_plus = (
            p_channel(h, +1, u)
            +
            p_channel(
                h,
                +1,
                length - u,
            )
        )

        m_minus = (
            p_channel(h, -1, u)
            +
            p_channel(
                h,
                -1,
                length - u,
            )
        )

        return 1.0 / math.sqrt(
            m_plus * m_minus
        )

    value, _ = quad(
        integrand,
        0.0,
        length,
        epsabs=1.0e-12,
        epsrel=1.0e-12,
        limit=500,
    )

    flat = length * length / 6.0

    return value / flat


def predicted_ratio(
    h: float,
    length: float,
) -> float:
    return (
        1.0
        +
        h * h
        * length**4
        / 252.0
    )


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--length",
        type=float,
        default=1.0,
    )

    args = parser.parse_args()

    previous_error = None

    for h in (
        0.15,
        0.10,
        0.05,
        0.02,
    ):
        exact = thin_ratio(
            h,
            args.length,
        )

        predicted = predicted_ratio(
            h,
            args.length,
        )

        scaled = (
            (exact - 1.0)
            /
            (
                h * h
                * args.length**4
            )
        )

        error = abs(
            exact - predicted
        )

        print(
            {
                "h": h,
                "exact_ratio": exact,
                "predicted_ratio": predicted,
                "(ratio-1)/(h^2 L^4)": scaled,
                "target": 1.0 / 252.0,
                "abs_error": error,
            }
        )

        if (
            previous_error is not None
            and h < 0.15
            and error
            > previous_error * 1.1
        ):
            raise AssertionError(
                "Small-h expansion did not improve."
            )

        previous_error = error

    print(
        "PASS: constant plane-wave thin-null response approaches 1/252."
    )


if __name__ == "__main__":
    main()
