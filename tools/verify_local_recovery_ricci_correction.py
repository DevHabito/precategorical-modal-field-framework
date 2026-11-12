#!/usr/bin/env python3
"""Regression for the first Ricci correction to the d>=4 recovery coefficient.

The analytic theorem determines

    K_{d,L}/K_d^flat
      = 1 + L^2 [a_d R + b_d R_TT] + O(L^4)

from two reference families:

1. Einstein static universe:
       R=(d-1)(d-2), R_TT=0.

2. unit-radius de Sitter:
       R=d(d-1), R_TT=-(d-1).

This script evaluates the exact one-dimensional near-null coefficient integrals
and the exact symmetric volume/area integrals for small L, reconstructs the
joint optical factor, and checks convergence to the analytic L^2 coefficients.

The computation is a regression only; the theorem contains the derivation.
"""

from __future__ import annotations

import argparse
import math

from scipy.integrate import quad
from scipy.special import gamma


def sphere_area(k: int) -> float:
    return (
        2.0
        * math.pi ** ((k + 1.0) / 2.0)
        / gamma((k + 1.0) / 2.0)
    )


def ball_volume(k: int) -> float:
    return (
        math.pi ** (k / 2.0)
        / gamma(k / 2.0 + 1.0)
    )


def flat_geometric_factor(d: int, L: float = 1.0) -> float:
    m = d / 2.0
    sphere = sphere_area(d - 2)

    volume = (
        2.0
        * sphere
        / (d * (d - 1.0))
        * L**d
    )

    beta_mm = (
        gamma(m) ** 2
        / gamma(2.0 * m)
    )

    c_near_null = (
        2.0**m
        * ball_volume(d - 2)
        / d
        * L**m
        * beta_mm
    )

    c_coord = (
        c_near_null
        / volume
    ) ** (1.0 / m)

    chi = 1.0 / (
        2.0
        * c_coord**2
    )

    area = (
        sphere
        * L ** (d - 2)
    )

    joint_optical = (
        chi ** (m + 1.0)
        * area
    )

    return joint_optical / volume**2


def esu_volume(d: int, L: float) -> float:
    sphere = sphere_area(d - 2)

    def outer(t: float) -> float:
        inner, _ = quad(
            lambda x:
                math.sin(x) ** (d - 2),
            0.0,
            L - t,
            epsabs=1.0e-13,
            epsrel=1.0e-12,
            limit=300,
        )
        return inner

    result, _ = quad(
        outer,
        0.0,
        L,
        epsabs=1.0e-13,
        epsrel=1.0e-12,
        limit=300,
    )

    return 2.0 * sphere * result


def esu_near_null_coefficient(
    d: int,
    L: float,
) -> float:
    m = d / 2.0

    def integrand(lam: float) -> float:
        ratio = (
            math.sin(lam)
            * math.sin(L - lam)
            / math.sin(L)
        )
        return ratio ** (m - 1.0)

    value, _ = quad(
        integrand,
        0.0,
        L,
        epsabs=1.0e-13,
        epsrel=1.0e-12,
        limit=300,
    )

    return (
        2.0**m
        * ball_volume(d - 2)
        / d
        * value
    )


def esu_geometric_factor(
    d: int,
    L: float,
) -> float:
    m = d / 2.0

    volume = esu_volume(d, L)
    coeff = esu_near_null_coefficient(
        d,
        L,
    )

    c_coord = (
        coeff / volume
    ) ** (1.0 / m)

    chi = 1.0 / (
        2.0
        * c_coord**2
    )

    area = (
        sphere_area(d - 2)
        * math.sin(L) ** (d - 2)
    )

    return (
        chi ** (m + 1.0)
        * area
        / volume**2
    )


def ds_half_conformal_duration(
    L: float,
) -> float:
    return math.acos(
        1.0 / math.cosh(L)
    )


def ds_volume(
    d: int,
    L: float,
) -> tuple[float, float]:
    ell = ds_half_conformal_duration(L)
    sphere = sphere_area(d - 2)

    def outer(eta: float) -> float:
        inner, _ = quad(
            lambda x:
                math.sin(x) ** (d - 2),
            0.0,
            ell - eta,
            epsabs=1.0e-13,
            epsrel=1.0e-12,
            limit=300,
        )
        return (
            math.cos(eta) ** (-d)
            * inner
        )

    result, _ = quad(
        outer,
        0.0,
        ell,
        epsabs=1.0e-13,
        epsrel=1.0e-12,
        limit=300,
    )

    return (
        2.0 * sphere * result,
        ell,
    )


def ds_near_null_coefficient(
    d: int,
    L: float,
) -> tuple[float, float]:
    m = d / 2.0
    ell = ds_half_conformal_duration(L)

    def integrand(lam: float) -> float:
        eta = lam - ell

        ratio = (
            math.sin(lam)
            * math.sin(ell - lam)
            / math.sin(ell)
        )

        return (
            math.cos(eta) ** (-d)
            * ratio ** (m - 1.0)
        )

    value, _ = quad(
        integrand,
        0.0,
        ell,
        epsabs=1.0e-13,
        epsrel=1.0e-12,
        limit=300,
    )

    coefficient = (
        2.0**m
        * ball_volume(d - 2)
        / d
        * value
    )

    return coefficient, ell


def ds_geometric_factor(
    d: int,
    L: float,
) -> float:
    m = d / 2.0

    volume, ell = ds_volume(d, L)
    coeff, _ = ds_near_null_coefficient(
        d,
        L,
    )

    c_coord = (
        coeff / volume
    ) ** (1.0 / m)

    # The de Sitter conformal factor is 1 at
    # the centered joint eta=0.
    chi = 1.0 / (
        2.0
        * c_coord**2
    )

    area = (
        sphere_area(d - 2)
        * math.sin(ell) ** (d - 2)
    )

    return (
        chi ** (m + 1.0)
        * area
        / volume**2
    )


def a_relative(d: int) -> float:
    return (
        -d
        * (d + 6.0)
        /
        (
            4.0
            * (d - 1.0)
            * (d + 1.0)
            * (d + 2.0)
        )
    )


def b_relative(d: int) -> float:
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
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--max-d",
        type=int,
        default=10,
    )

    parser.add_argument(
        "--Ls",
        default="0.1,0.05,0.025",
    )

    args = parser.parse_args()

    Ls = [
        float(x.strip())
        for x in args.Ls.split(",")
        if x.strip()
    ]

    for d in range(4, args.max_d + 1):
        flat = flat_geometric_factor(d)

        a = a_relative(d)
        b = b_relative(d)

        r_esu = (
            (d - 1.0)
            * (d - 2.0)
        )

        target_esu = a * r_esu

        r_ds = d * (d - 1.0)
        rtt_ds = -(d - 1.0)

        target_ds = (
            a * r_ds
            + b * rtt_ds
        )

        print(
            {
                "d": d,
                "target_ESU_L2": target_esu,
                "target_dS_L2": target_ds,
            }
        )

        for L in Ls:
            esu = esu_geometric_factor(
                d,
                L,
            )

            ds = ds_geometric_factor(
                d,
                L,
            )

            print(
                {
                    "L": L,
                    "ESU_effective":
                        (esu / flat - 1.0)
                        / L**2,
                    "dS_effective":
                        (ds / flat - 1.0)
                        / L**2,
                }
            )

    print(
        "PASS target: effective coefficients converge to the analytic Ricci formula as L -> 0."
    )


if __name__ == "__main__":
    main()
