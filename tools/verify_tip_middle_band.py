#!/usr/bin/env python3
"""Regression for the timelike-tip middle-band lemma.

The analytic lemma used in the near-whole-module rate theorem states that,
for a point x sufficiently close to a timelike tip, a fixed positive fraction
of its nonneighbor volume lies in a null-face band whose graphon degree stays
uniformly away from 0 and 1.

This script checks the explicit geometric construction over a finite grid in
d=3,...,max_d.  It is a numerical regression only; the proof is analytic.
"""

from __future__ import annotations

import argparse
import math
import numpy as np


def q_d(t: float, r: float, d: int) -> float:
    past = max((1.0 + t) ** 2 - r * r, 0.0)
    future = max((1.0 - t) ** 2 - r * r, 0.0)
    return (past ** (d / 2.0) + future ** (d / 2.0)) / (2.0**d)


def spacelike_margin(
    s: float,
    rho: float,
    tau: float,
    h: float,
    cosine: float,
) -> float:
    """Return |dz|^2-dt^2 for the explicit past-tip construction."""
    rz = tau - h
    rx = s * rho

    spatial_sq = (
        rz * rz
        + rx * rx
        - 2.0 * rz * rx * cosine
    )
    time_sq = (tau - s) ** 2
    return spatial_sq - time_sq


def check_dimension(d: int) -> dict[str, float | int]:
    s_values = [0.10, 0.05, 0.02, 0.01, 0.005, 0.001]
    rho_values = np.linspace(0.0, 1.0, 41)
    tau_values = np.linspace(1.0 / 3.0, 1.0 / 2.0, 21)
    h_fractions = np.linspace(1.0 / 4.0, 1.0 / 3.0, 13)
    cosine_values = np.linspace(-1.0, 0.0, 21)

    min_margin_over_s = math.inf
    min_r_over_s = math.inf
    max_r_over_s = 0.0
    min_q_band = math.inf
    max_q_band = 0.0

    for s in s_values:
        for rho in rho_values:
            qx = q_d(-1.0 + s, s * rho, d)
            co_degree = 1.0 - qx

            min_r_over_s = min(min_r_over_s, co_degree / s)
            max_r_over_s = max(max_r_over_s, co_degree / s)

            for tau in tau_values:
                for h_fraction in h_fractions:
                    h = s * h_fraction
                    qz = q_d(-1.0 + tau, tau - h, d)

                    min_q_band = min(min_q_band, qz)
                    max_q_band = max(max_q_band, qz)

                    for cosine in cosine_values:
                        margin = spacelike_margin(
                            s,
                            rho,
                            tau,
                            h,
                            cosine,
                        )
                        min_margin_over_s = min(
                            min_margin_over_s,
                            margin / s,
                        )

    if min_margin_over_s <= 0.0:
        raise AssertionError(
            f"middle-band construction lost spacelike margin in d={d}"
        )

    if not (0.0 < min_q_band < max_q_band < 1.0):
        raise AssertionError(
            f"middle-band graphon degrees not uniformly intermediate in d={d}"
        )

    return {
        "d": d,
        "min_margin_over_s": min_margin_over_s,
        "min_co_degree_over_s": min_r_over_s,
        "max_co_degree_over_s": max_r_over_s,
        "min_middle_Q": min_q_band,
        "max_middle_Q": max_q_band,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=12)
    args = parser.parse_args()

    for d in range(3, args.max_d + 1):
        print(check_dimension(d))

    print(
        f"PASS: middle-band regression verified for d=3..{args.max_d}"
    )


if __name__ == "__main__":
    main()
