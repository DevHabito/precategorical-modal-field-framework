#!/usr/bin/env python3
"""Regression for the first curvature-response constants in d=3.

The bulk-dominated d=3 recovery coefficient is

    K_3 = 3 C_3,

and for a conformal perturbation g_eps = exp(2 eps f) eta the causal kernel is
unchanged while the normalized sprinkling density changes.

For f=t^2 and f=r^2, the exact first variation reduces in endpoint-distance
coordinates to two convergent integrals over

    0 < s < 2,  -1 < w < 1.

This script evaluates those integrals with tensor-product Gauss-Legendre
quadrature and solves for A_3 and B_3 in

    K_3(L)
      = K_3^Mink
        + L^2 (A_3 R + B_3 R_TT)
        + o(L^2).

The numerical values are a regression.  The theorem records the exact integral
representation and does not claim an elementary closed form.
"""

from __future__ import annotations

import math

import numpy as np
from numpy.polynomial.legendre import leggauss


def response_integrals(order: int) -> tuple[float, float]:
    nodes, weights = leggauss(order)

    w = nodes[:, None]
    s = (nodes + 1.0)[None, :]

    quadrature_weight = (
        weights[:, None]
        * weights[None, :]
    )

    dpoly = (
        s**2 * w**4
        + 3.0 * s**2 * w**2
        - 4.0 * w**2
        + 4.0
    )

    base = (
        (256.0 / 9.0)
        * (1.0 - w**2)
        / dpoly**1.5
    )

    n_t = (
        35.0 * s**6 * w**6
        + 105.0 * s**6 * w**4
        + 60.0 * s**4 * w**6
        + 1020.0 * s**4 * w**4
        + 1000.0 * s**4 * w**2
        - 1312.0 * s**2 * w**4
        - 1776.0 * s**2 * w**2
        + 720.0 * s**2
        + 4288.0 * w**2
        - 4288.0
    )

    n_r = (
        35.0 * s**6 * w**6
        + 105.0 * s**6 * w**4
        - 260.0 * s**4 * w**6
        - 1860.0 * s**4 * w**4
        - 920.0 * s**4 * w**2
        + 2784.0 * s**2 * w**4
        + 2832.0 * s**2 * w**2
        - 1840.0 * s**2
        - 6976.0 * w**2
        + 6976.0
    )

    ratio_t = (
        3.0
        * n_t
        / (1280.0 * dpoly)
    )

    ratio_r = (
        3.0
        * n_r
        / (1280.0 * dpoly)
    )

    delta_c_t = float(
        np.sum(
            quadrature_weight
            * base
            * ratio_t
        )
    )

    delta_c_r = float(
        np.sum(
            quadrature_weight
            * base
            * ratio_r
        )
    )

    return delta_c_t, delta_c_r


def curvature_constants(
    delta_c_t: float,
    delta_c_r: float,
) -> tuple[float, float, float, float]:
    c0 = 32.0 * math.pi / 9.0
    k0 = 3.0 * c0

    c_t = delta_c_t / c0
    c_r = delta_c_r / c0

    # d=3 conformal test curvatures:
    #
    # f=t^2:
    #   R/eps = 8
    #   R_TT/eps = -4
    #
    # f=r^2:
    #   R/eps = -16
    #   R_TT/eps = 4
    #
    # Therefore
    #   8 a - 4 b = c_t
    #  -16 a + 4 b = c_r
    # with a=A_3/K0, b=B_3/K0.
    a_over_k = -(c_t + c_r) / 8.0
    b_over_k = 2.0 * a_over_k - c_t / 4.0

    return (
        a_over_k,
        b_over_k,
        k0 * a_over_k,
        k0 * b_over_k,
    )


def main() -> None:
    previous = None

    for order in (100, 200, 400, 800):
        delta_c_t, delta_c_r = response_integrals(order)

        (
            a_over_k,
            b_over_k,
            a3,
            b3,
        ) = curvature_constants(
            delta_c_t,
            delta_c_r,
        )

        print(
            {
                "order": order,
                "delta_C_t": delta_c_t,
                "delta_C_r": delta_c_r,
                "A3_over_K3": a_over_k,
                "B3_over_K3": b_over_k,
                "A3": a3,
                "B3": b3,
            }
        )

        current = np.array(
            [
                delta_c_t,
                delta_c_r,
                a_over_k,
                b_over_k,
                a3,
                b3,
            ],
            dtype=float,
        )

        if previous is not None and order == 800:
            if not np.allclose(
                current,
                previous,
                rtol=2.0e-8,
                atol=2.0e-8,
            ):
                raise AssertionError(
                    "Gauss-Legendre sequence did not stabilize."
                )

        previous = current

    print(
        "PASS: d=3 curvature-response quadrature stabilized."
    )


if __name__ == "__main__":
    main()
