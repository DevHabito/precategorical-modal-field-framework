#!/usr/bin/env python3
"""Exact generic timelike-tip jets for transversely boosted d=5 LRS Kasner.

Metric:
    ds^2 = -dt^2 + t^(-1) dx^2 + t(dy_1^2+dy_2^2+dy_3^2).

Let P be the conserved transverse momentum and define

    a = P^2 = v^2/(1-v^2).

With proper time s centered at t(0)=1, y(0)=0, the geodesic equations are

    dt/ds = sqrt(1 + a/t),
    dy/ds = sqrt(a)/t.

This checker derives and verifies the generic Taylor jets through s^6.
It also specializes them to v=1/2, P^2=1/3, reproducing the exact
coefficients used in the boosted-volume calibration.

These jets are the analytic starting point for a future exact expansion of
the translated null-cone lens.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s = sp.symbols("s", real=True)
    a = sp.symbols("a", positive=True)

    gamma = sp.sqrt(1 + a)
    momentum = sp.sqrt(a)

    t = (
        1
        + gamma * s
        - a * s**2 / 4
        + a * gamma * s**3 / 6
        - a * (7 * a + 6) * s**4 / 48
        + a * gamma * (35 * a + 24) * s**5 / 240
        - a
        * (
            455 * a**2
            + 684 * a
            + 240
        )
        * s**6
        / 2880
    )

    y = (
        momentum * s
        - momentum * gamma * s**2 / 2
        + momentum * (5 * a + 4) * s**3 / 12
        - momentum
        * gamma
        * (5 * a + 3)
        * s**4
        / 12
        + momentum
        * (
            55 * a**2
            + 77 * a
            + 24
        )
        * s**5
        / 120
        - momentum
        * gamma
        * (
            385 * a**2
            + 462 * a
            + 120
        )
        * s**6
        / 720
    )

    dt_rhs = sp.sqrt(
        1 + a / t
    ).series(
        s,
        0,
        6,
    ).removeO()

    dy_rhs = (
        momentum / t
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

    assert sp.simplify(
        dt_residual
    ) == 0

    assert sp.simplify(
        dy_residual
    ) == 0

    L = sp.symbols("L", real=True)

    delta_t = sp.factor(
        t.subs(s, L)
        - t.subs(s, -L)
    )

    delta_y = sp.factor(
        y.subs(s, L)
        - y.subs(s, -L)
    )

    mean_t = sp.factor(
        (
            t.subs(s, L)
            + t.subs(s, -L)
        )
        / 2
    )

    expected_delta_t = (
        2 * gamma * L
        + a * gamma * L**3 / 3
        + a
        * gamma
        * (
            35 * a
            + 24
        )
        * L**5
        / 120
    )

    expected_delta_y = (
        2 * momentum * L
        + momentum
        * (
            5 * a
            + 4
        )
        * L**3
        / 6
        + momentum
        * (
            55 * a**2
            + 77 * a
            + 24
        )
        * L**5
        / 60
    )

    expected_mean_t = (
        1
        - a * L**2 / 4
        - a
        * (
            7 * a
            + 6
        )
        * L**4
        / 48
        - a
        * (
            455 * a**2
            + 684 * a
            + 240
        )
        * L**6
        / 2880
    )

    assert sp.simplify(
        delta_t
        - expected_delta_t
    ) == 0

    assert sp.simplify(
        delta_y
        - expected_delta_y
    ) == 0

    assert sp.simplify(
        mean_t
        - expected_mean_t
    ) == 0

    # Specialize to v=1/2, hence a=P^2=1/3.
    special = {
        a: sp.Rational(1, 3),
    }

    sqrt3 = sp.sqrt(3)

    expected_t_half = (
        1
        + 2 * sqrt3 * s / 3
        - s**2 / 12
        + sqrt3 * s**3 / 27
        - 25 * s**4 / 432
        + 107 * sqrt3 * s**5 / 3240
        - 4667 * s**6 / 77760
    )

    assert sp.simplify(
        t.subs(special)
        - expected_t_half
    ) == 0

    print(
        {
            "generic_t_series":
                str(t),
            "generic_y_series":
                str(y),
            "generic_tip_delta_t":
                str(delta_t),
            "generic_tip_delta_y":
                str(delta_y),
            "generic_tip_mean_t":
                str(mean_t),
            "v_half_t_series":
                str(t.subs(special)),
        }
    )

    print(
        "PASS: generic boosted d5 Kasner timelike-tip jets satisfy the "
        "geodesic ODEs and reproduce the v=1/2 specialization."
    )


if __name__ == "__main__":
    main()
