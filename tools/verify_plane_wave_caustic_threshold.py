#!/usr/bin/env python3
"""Exact caustic-threshold regression for a constant-profile plane wave.

Metric:
    ds^2 = 2 du dv + dy^2 - omega^2 y^2 dv^2.

For endpoints
    P=(0,0,0), Q=(-a,L,0),
the transverse causal action is
    Q[y] = integral (y'^2 - omega^2 y^2) dv <= 2a.

The first Dirichlet mode has eigenvalue
    lambda1 = (pi/L)^2 - omega^2.

Checks:
1. before conjugacy, A_max ~ sqrt(a/lambda1);
2. at L=pi/omega, y=A sin(omega v) has exactly zero action
   for every amplitude A;
3. after conjugacy, the first-mode action is negative and scales
   to -infinity with amplitude.

This is an exact diagnostic of the breakdown of uniform thin-null
compact containment at a conjugate point.
"""

from __future__ import annotations

import argparse
import math


def lambda1(
    omega: float,
    length: float,
) -> float:
    return (math.pi / length) ** 2 - omega**2


def first_mode_action(
    amplitude: float,
    omega: float,
    length: float,
) -> float:
    lam = lambda1(
        omega,
        length,
    )

    return (
        0.5
        * length
        * lam
        * amplitude**2
    )


def max_amplitude_before_caustic(
    a: float,
    omega: float,
    length: float,
) -> float:
    lam = lambda1(
        omega,
        length,
    )

    if lam <= 0:
        return math.inf

    return math.sqrt(
        4.0
        * a
        /
        (length * lam)
    )


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--omega",
        type=float,
        default=1.0,
    )

    parser.add_argument(
        "--a",
        type=float,
        default=1e-6,
    )

    args = parser.parse_args()

    omega = args.omega
    a = args.a

    critical = math.pi / omega

    before = 0.99 * critical
    threshold = critical
    after = 1.01 * critical

    lam_before = lambda1(
        omega,
        before,
    )

    lam_threshold = lambda1(
        omega,
        threshold,
    )

    lam_after = lambda1(
        omega,
        after,
    )

    assert lam_before > 0.0
    assert abs(lam_threshold) < 1e-12
    assert lam_after < 0.0

    amax = max_amplitude_before_caustic(
        a,
        omega,
        before,
    )

    scaled_width = amax / math.sqrt(a)

    print(
        {
            "regime": "before",
            "L": before,
            "lambda1": lam_before,
            "Amax": amax,
            "Amax_over_sqrt_a": scaled_width,
        }
    )

    for amplitude in (
        1.0,
        10.0,
        1e3,
    ):
        action = first_mode_action(
            amplitude,
            omega,
            threshold,
        )

        print(
            {
                "regime": "threshold",
                "amplitude": amplitude,
                "action": action,
            }
        )

        assert abs(action) < 1e-8

    for amplitude in (
        1.0,
        10.0,
        100.0,
    ):
        action = first_mode_action(
            amplitude,
            omega,
            after,
        )

        print(
            {
                "regime": "after",
                "amplitude": amplitude,
                "action": action,
            }
        )

        assert action < 0.0

    print(
        "PASS: compact-containment coercivity fails exactly at conjugacy."
    )


if __name__ == "__main__":
    main()
