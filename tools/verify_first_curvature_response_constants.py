#!/usr/bin/env python3
"""Regression for the first curvature response constants A_d and B_d.

For d>=4, the structural theorem gives

    K_d(L) = K0 + L^2 (A_d R + B_d R_TT) + o(L^2).

Two conformal perturbations of flat space are used:

    omega = eps * t^2
    omega = eps * r^2

The causal diamond is unchanged up to an irrelevant first-order global
dilation, so the response of K can be computed from the weighted null-edge
formula.

The script numerically evaluates the line and diamond averages and checks the
closed formulas

    A_d/K0 = - d(d+6) / [4(d-1)(d+1)(d+2)]

    B_d/K0 = (d^2+2d-4) / [4(d-1)(d+1)].
"""

from __future__ import annotations

import math

import scipy.integrate as integrate
import scipy.special as special


def line_average_x2(d: int) -> float:
    m = d / 2.0

    def weight(v: float) -> float:
        return (v * (2.0 - v)) ** (m - 1.0)

    denominator, _ = integrate.quad(
        weight,
        0.0,
        2.0,
        epsabs=1.0e-12,
        epsrel=1.0e-12,
    )

    numerator, _ = integrate.quad(
        lambda v: weight(v) * (v / 2.0) ** 2,
        0.0,
        2.0,
        epsabs=1.0e-12,
        epsrel=1.0e-12,
    )

    return numerator / denominator


def diamond_t2_average(d: int) -> float:
    # Exact value, retained as a function for clarity.
    return 2.0 / ((d + 1.0) * (d + 2.0))


def diamond_r2_average(d: int) -> float:
    return (
        d
        * (d - 1.0)
        / ((d + 1.0) * (d + 2.0))
    )


def conformal_log_responses(d: int) -> tuple[float, float]:
    line = line_average_x2(d)

    avg_t = diamond_t2_average(d)
    avg_r = diamond_r2_average(d)

    # General response:
    # d ln K / d eps =
    # 2d f_edge
    # -(d+2)(fbar_plus+fbar_minus)
    # +4 <f>_D.
    #
    # For both t^2 and r^2, the two null-generator line averages
    # equal 'line' by v <-> 2-v symmetry.
    c_t = (
        -(d + 2.0) * 2.0 * line
        + 4.0 * avg_t
    )

    c_r = (
        2.0 * d
        -(d + 2.0) * 2.0 * line
        + 4.0 * avg_r
    )

    return c_t, c_r


def solve_a_b_over_k(d: int) -> tuple[float, float]:
    c_t, c_r = conformal_log_responses(d)

    # Curvature convention:
    # R^rho_{ sigma mu nu}
    # = d_mu Gamma^rho_{nu sigma} - d_nu Gamma^rho_{mu sigma} + ...
    #
    # omega=eps t^2:
    # R/eps = 4(d-1), RTT/eps = -2(d-1)
    #
    # omega=eps r^2:
    # R/eps = -4(d-1)^2, RTT/eps = 2(d-1)
    u = c_t / (2.0 * (d - 1.0))
    v = c_r / (2.0 * (d - 1.0))

    a_over_k = -(u + v) / (2.0 * (d - 2.0))
    b_over_k = 2.0 * a_over_k - u

    return a_over_k, b_over_k


def closed_a_over_k(d: int) -> float:
    return (
        -d
        * (d + 6.0)
        / (
            4.0
            * (d - 1.0)
            * (d + 1.0)
            * (d + 2.0)
        )
    )


def closed_b_over_k(d: int) -> float:
    return (
        d**2
        + 2.0 * d
        - 4.0
    ) / (
        4.0
        * (d - 1.0)
        * (d + 1.0)
    )


def main() -> None:
    for d in range(4, 13):
        line = line_average_x2(d)
        exact_line = (
            d + 2.0
        ) / (
            4.0 * (d + 1.0)
        )

        assert math.isclose(
            line,
            exact_line,
            rel_tol=2.0e-11,
            abs_tol=2.0e-11,
        )

        a_num, b_num = solve_a_b_over_k(d)
        a_closed = closed_a_over_k(d)
        b_closed = closed_b_over_k(d)

        print(
            {
                "d": d,
                "line_average": line,
                "A_over_K_numeric": a_num,
                "A_over_K_closed": a_closed,
                "B_over_K_numeric": b_num,
                "B_over_K_closed": b_closed,
            }
        )

        assert math.isclose(
            a_num,
            a_closed,
            rel_tol=2.0e-10,
            abs_tol=2.0e-10,
        )

        assert math.isclose(
            b_num,
            b_closed,
            rel_tol=2.0e-10,
            abs_tol=2.0e-10,
        )

    # d=4 explicit ratios.
    assert math.isclose(
        closed_a_over_k(4),
        -1.0 / 9.0,
        rel_tol=1.0e-14,
    )

    assert math.isclose(
        closed_b_over_k(4),
        1.0 / 3.0,
        rel_tol=1.0e-14,
    )

    print(
        "PASS: first curvature-response constants verified for d=4..12."
    )


if __name__ == "__main__":
    main()
