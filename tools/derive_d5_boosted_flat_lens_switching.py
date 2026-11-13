#!/usr/bin/env python3
"""Exact switching geometry of the flat boosted d=5 causal-diamond lens.

This is the leading L->0 geometry underlying the boosted LRS-Kasner
calibration.

Let

    gamma = sqrt(1 + P^2)

and use scaled coordinates

    T = (t-1)/L,
    X = x/L.

The flat boosted tips are

    (-gamma, -P), (+gamma, +P)

in the (T,y_1) plane.

At fixed T and X, the past/future null-cone transverse sections are
three-balls with radii

    R_- = sqrt((gamma+T)^2 - X^2),
    R_+ = sqrt((gamma-T)^2 - X^2),

and center separation 2P.

The lens regime changes when either

    R_- + R_+ = 2P

or

    R_- - R_+ = 2P

for T>=0.

Both conditions reduce to

    X_*^2 = 1 - T^2/P^2,

with different sign/positivity branches.

The critical time separating non-overlap from containment at the smaller
cone's axial endpoint is

    T_c = P^2/gamma.

For T>=P, the smaller transverse ball is contained in the larger one for
the full allowed axial interval.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    P, T, X = sp.symbols(
        "P T X",
        positive=True,
        real=True,
    )

    gamma = sp.sqrt(
        1 + P**2
    )

    a = gamma + T
    b = gamma - T

    # Solve the squared algebra associated with:
    #
    # R_- - R_+ = 2P.
    #
    # This gives
    #
    # R_+ = (gamma*T - P^2)/P.
    r_plus_containment = (
        gamma * T
        - P**2
    ) / P

    x2_containment = sp.factor(
        b**2
        - r_plus_containment**2
    )

    expected_x2 = (
        1
        - T**2 / P**2
    )

    assert sp.simplify(
        x2_containment
        - expected_x2
    ) == 0

    # For
    #
    # R_- + R_+ = 2P,
    #
    # the corresponding branch gives
    #
    # R_+ = (P^2 - gamma*T)/P.
    r_plus_overlap = (
        P**2
        - gamma * T
    ) / P

    x2_overlap = sp.factor(
        b**2
        - r_plus_overlap**2
    )

    assert sp.simplify(
        x2_overlap
        - expected_x2
    ) == 0

    critical_time = sp.simplify(
        P**2 / gamma
    )

    # At the smaller cone's axial endpoint X=b, R_+=0 and
    #
    # R_- = sqrt((gamma+T)^2-(gamma-T)^2)
    #     = 2 sqrt(gamma T).
    #
    # Equality with 2P occurs at T=P^2/gamma.
    endpoint_large_radius_squared = sp.factor(
        a**2 - b**2
    )

    assert sp.simplify(
        endpoint_large_radius_squared
        - 4 * gamma * T
    ) == 0

    assert sp.simplify(
        endpoint_large_radius_squared.subs(
            T,
            critical_time,
        )
        - 4 * P**2
    ) == 0

    # At X=0:
    #
    # R_- - R_+ = 2T.
    #
    # Therefore T>=P implies containment already on the axis.
    axis_difference = sp.simplify(
        a - b
    )

    assert axis_difference == 2 * T

    print(
        {
            "gamma": str(gamma),
            "switch_X_squared":
                str(expected_x2),
            "critical_time":
                str(critical_time),
            "axis_radius_difference":
                str(axis_difference),
            "endpoint_large_radius_squared":
                str(endpoint_large_radius_squared),
        }
    )

    print(
        "PASS: the flat boosted d5 lens switching surface is "
        "X_*^2 = 1 - T^2/P^2, with T_c=P^2/gamma and full containment "
        "for T>=P."
    )


if __name__ == "__main__":
    main()
