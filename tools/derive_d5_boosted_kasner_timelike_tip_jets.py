#!/usr/bin/env python3
"""Exact timelike-tip jets for the d=5 transversely boosted LRS-Kasner test.

Metric:
    ds^2 = -dt^2 + t^(-1) dx^2 + t(dy_1^2+dy_2^2+dy_3^2).

Choose midpoint t=1 and local orthonormal transverse speed v=1/2.
Then

    gamma = 2/sqrt(3),
    P = gamma v = 1/sqrt(3),

where P is the conserved y_1 momentum.

The central timelike geodesic obeys

    dt/ds = sqrt(1 + P^2/t),
    dy/ds = P/t,

with proper time s and t(0)=1, y(0)=0.

This checker derives exact Taylor jets through s^6 and verifies the geodesic
ODEs coefficient by coefficient.  These jets are the starting point for a
future exact boosted-cone lens expansion.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s = sp.symbols("s", real=True)
    sqrt3 = sp.sqrt(3)
    P = 1 / sqrt3

    t = (
        1
        + 2 * sqrt3 * s / 3
        - s**2 / 12
        + sqrt3 * s**3 / 27
        - 25 * s**4 / 432
        + 107 * sqrt3 * s**5 / 3240
        - 4667 * s**6 / 77760
    )

    y = (
        sqrt3 * s / 3
        - s**2 / 3
        + 17 * sqrt3 * s**3 / 108
        - 7 * s**4 / 27
        + 251 * sqrt3 * s**5 / 1620
        - 2851 * s**6 / 9720
    )

    dt_rhs = sp.sqrt(
        1 + P**2 / t
    ).series(
        s,
        0,
        6,
    ).removeO()

    dy_rhs = (
        P / t
    ).series(
        s,
        0,
        6,
    ).removeO()

    dt_residual = sp.series(
        sp.diff(t, s) - dt_rhs,
        s,
        0,
        6,
    ).removeO().expand()

    dy_residual = sp.series(
        sp.diff(y, s) - dy_rhs,
        s,
        0,
        6,
    ).removeO().expand()

    assert dt_residual == 0
    assert dy_residual == 0

    L = sp.symbols("L", real=True)

    t_plus = sp.expand(
        t.subs(s, L)
    )

    t_minus = sp.expand(
        t.subs(s, -L)
    )

    y_plus = sp.expand(
        y.subs(s, L)
    )

    y_minus = sp.expand(
        y.subs(s, -L)
    )

    delta_t = sp.factor(
        t_plus - t_minus
    )

    delta_y = sp.factor(
        y_plus - y_minus
    )

    mean_t = sp.factor(
        (t_plus + t_minus) / 2
    )

    expected_delta_t = (
        4 * sqrt3 * L / 3
        + 2 * sqrt3 * L**3 / 27
        + 107 * sqrt3 * L**5 / 1620
    )

    expected_delta_y = (
        2 * sqrt3 * L / 3
        + 17 * sqrt3 * L**3 / 54
        + 251 * sqrt3 * L**5 / 810
    )

    expected_mean_t = (
        1
        - L**2 / 12
        - 25 * L**4 / 432
        - 4667 * L**6 / 77760
    )

    assert sp.simplify(
        delta_t - expected_delta_t
    ) == 0

    assert sp.simplify(
        delta_y - expected_delta_y
    ) == 0

    assert sp.simplify(
        mean_t - expected_mean_t
    ) == 0

    print(
        {
            "v": "1/2",
            "P": "1/sqrt(3)",
            "t_series": str(t),
            "y_series": str(y),
            "tip_delta_t": str(delta_t),
            "tip_delta_y": str(delta_y),
            "tip_mean_t": str(mean_t),
        }
    )

    print(
        "PASS: exact boosted d5 Kasner timelike-tip jets satisfy the "
        "geodesic ODEs through the retained order."
    )


if __name__ == "__main__":
    main()
