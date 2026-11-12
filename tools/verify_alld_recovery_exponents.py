#!/usr/bin/env python3
"""Regression for exponent windows in the all-dimensional recovery proof.

For every integer d >= 3:
- r is the smallest power of two strictly greater than d/4;
- the near-whole proof needs r < d;
- it needs an exponent a with 1-1/r < a < 1-1/d;
- it needs gamma with r < gamma < d;
- the final low-degree layer needs 4r/d - 1 > 0;
- the edge-escalation proof needs beta_d > 2, where
      beta_d = min(d, 2 + 4/d).

This script checks those inequalities over a user-selected finite range.
The analytic proof of the inequalities is recorded in the audit document.
"""

from __future__ import annotations

import argparse


def smallest_power_two_above(x: float) -> int:
    r = 1
    while r <= x:
        r *= 2
    return r


def check_dimension(d: int) -> dict[str, float | int | bool]:
    if d < 3:
        raise ValueError("d must be >= 3")

    r = smallest_power_two_above(d / 4.0)
    lower_a = 1.0 - 1.0 / r
    upper_a = 1.0 - 1.0 / d
    gamma = 0.5 * (r + d)
    beta = min(float(d), 2.0 + 4.0 / d)

    checks = {
        "r_lt_d": r < d,
        "a_window_nonempty": lower_a < upper_a,
        "gamma_window": r < gamma < d,
        "final_tail_positive": 4.0 * r / d - 1.0 > 0.0,
        "edge_tail_above_two": beta > 2.0,
    }

    if not all(checks.values()):
        raise AssertionError({"d": d, "r": r, **checks})

    return {
        "d": d,
        "r": r,
        "lower_a": lower_a,
        "upper_a": upper_a,
        "gamma_example": gamma,
        "beta_d": beta,
        "final_tail_excess": 4.0 * r / d - 1.0,
        **checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=100)
    args = parser.parse_args()

    for d in range(3, args.max_d + 1):
        row = check_dimension(d)
        print(row)

    print(f"PASS: exponent windows verified for d=3..{args.max_d}")


if __name__ == "__main__":
    main()
