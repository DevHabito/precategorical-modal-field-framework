#!/usr/bin/env python3
"""Exact symmetric plane-wave calibration of the d=4 vacuum L^4 response.

For the Ricci-flat symmetric plane wave

    ds^2 = -2 du dv + dx_1^2 + dx_2^2
            + H_ij x^i x^j du^2,

with
    H = diag(-omega^2, +omega^2),

consider a centered timelike diamond on the central geodesic, strictly before
the first conjugate phase.

Define
    z = omega U,
where U is the null-phase separation of the two tips.

The exact d=4 volume-null joint formula reduces to

    K_PW/K_Mink
      = F(z)/72 * integral_0^1
          (a_z+b_z)
          / [(a_z b_z)^2 [x(1-x)]^3
             [F(zx)F(z(1-x))]^(3/2)] dx,

where

    a_z(x) = z sin z / [sin(zx) sin(z(1-x))],
    b_z(x) = z sinh z / [sinh(zx) sinh(z(1-x))],

and

    F(z) = integral_0^1 [a_z(x)b_z(x)]^(-1/2) dx.

The symbolic expansion gives

    K_PW/K_Mink
      = 1 + (127/9450) z^4 + O(z^8).

For the central observer,
    E^2 = B^2 = omega^4/2,
and U = sqrt(2) L, where L is the proper-time half-size of the centered
diamond. Therefore

    a_4 + b_4 = 508/4725

in

    K_4/(9*pi)
      = 1 + L^4 [a_4 E^2 + b_4 B^2] + o(L^4).

The script performs both the symbolic expansion and an independent numerical
quadrature of the exact formula.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import math

import numpy as np
import sympy as sp


def symbolic_coefficient() -> sp.Rational:
    x, z = sp.symbols(
        "x z",
        positive=True,
        real=True,
    )

    a_exact = (
        z
        * sp.sin(z)
        /
        (
            sp.sin(z * x)
            * sp.sin(z * (1 - x))
        )
    )

    b_exact = (
        z
        * sp.sinh(z)
        /
        (
            sp.sinh(z * x)
            * sp.sinh(z * (1 - x))
        )
    )

    a = sp.series(
        a_exact,
        z,
        0,
        6,
    ).removeO()

    b = sp.series(
        b_exact,
        z,
        0,
        6,
    ).removeO()

    f_integrand = sp.series(
        1 / sp.sqrt(a * b),
        z,
        0,
        6,
    ).removeO()

    # On 0<x<1, SymPy's |x(x-1)| is x(1-x).
    f_integrand = f_integrand.replace(
        lambda e:
            isinstance(e, sp.Abs),
        lambda e:
            x * (1 - x),
    )

    f_series = sp.simplify(
        sp.integrate(
            f_integrand,
            (x, 0, 1),
        )
    )

    expected_f = (
        sp.Rational(1, 6)
        * (
            1
            +
            z**4
            / 252
        )
    )

    assert (
        sp.simplify(
            f_series - expected_f
        )
        ==
        0
    )

    def f_truncated(arg):
        return (
            sp.Rational(1, 6)
            * (
                1
                +
                arg**4 / 252
            )
        )

    inner = (
        (a + b)
        /
        (
            (a * b) ** 2
            * (x * (1 - x)) ** 3
            * (
                f_truncated(z * x)
                * f_truncated(
                    z * (1 - x)
                )
            )
            ** sp.Rational(3, 2)
        )
    )

    inner_series = sp.series(
        inner,
        z,
        0,
        6,
    ).removeO()

    inner_integral = sp.simplify(
        sp.integrate(
            inner_series,
            (x, 0, 1),
        )
    )

    ratio = sp.series(
        expected_f
        * inner_integral
        / 72,
        z,
        0,
        6,
    ).removeO()

    coefficient = sp.simplify(
        sp.expand(ratio).coeff(
            z,
            4,
        )
    )

    assert (
        coefficient
        ==
        sp.Rational(
            127,
            9450,
        )
    )

    return coefficient


def gauss_nodes(
    n: int,
) -> tuple[np.ndarray, np.ndarray]:
    nodes, weights = (
        np.polynomial.legendre.leggauss(
            n
        )
    )

    return (
        (nodes + 1.0) / 2.0,
        weights / 2.0,
    )


def sinc(
    x: np.ndarray,
) -> np.ndarray:
    return np.sinc(
        x / np.pi
    )


def sinhc(
    x: np.ndarray,
) -> np.ndarray:
    x = np.asarray(
        x,
        dtype=float,
    )

    out = np.ones_like(x)

    mask = (
        np.abs(x)
        >
        1e-7
    )

    out[mask] = (
        np.sinh(x[mask])
        /
        x[mask]
    )

    small = x[~mask]

    out[~mask] = (
        1.0
        +
        small**2 / 6.0
        +
        small**4 / 120.0
        +
        small**6 / 5040.0
    )

    return out


def f_values(
    z_values: np.ndarray,
    order: int,
) -> np.ndarray:
    z_values = np.atleast_1d(
        np.asarray(
            z_values,
            dtype=float,
        )
    )

    x, weights = gauss_nodes(
        order
    )

    z = z_values[:, None]
    xx = x[None, :]

    a = (
        sinc(z)
        /
        (
            xx
            * (1.0 - xx)
            * sinc(z * xx)
            * sinc(
                z * (1.0 - xx)
            )
        )
    )

    b = (
        sinhc(z)
        /
        (
            xx
            * (1.0 - xx)
            * sinhc(z * xx)
            * sinhc(
                z * (1.0 - xx)
            )
        )
    )

    values = 1.0 / np.sqrt(
        a * b
    )

    return values @ weights


def exact_ratio(
    z: float,
    order: int,
) -> float:
    x, weights = gauss_nodes(
        order
    )

    fz = float(
        f_values(
            np.array([z]),
            order,
        )[0]
    )

    fx = f_values(
        z * x,
        order,
    )

    f1x = f_values(
        z * (1.0 - x),
        order,
    )

    a = (
        sinc(
            np.array([z])
        )[0]
        /
        (
            x
            * (1.0 - x)
            * sinc(z * x)
            * sinc(
                z * (1.0 - x)
            )
        )
    )

    b = (
        sinhc(
            np.array([z])
        )[0]
        /
        (
            x
            * (1.0 - x)
            * sinhc(z * x)
            * sinhc(
                z * (1.0 - x)
            )
        )
    )

    integrand = (
        (a + b)
        /
        (
            (a * b) ** 2
            * (
                x
                * (1.0 - x)
            )
            ** 3
            * (
                fx * f1x
            )
            ** 1.5
        )
    )

    integral = float(
        np.sum(
            weights
            * integrand
        )
    )

    return (
        fz
        * integral
        / 72.0
    )


def parse_floats(
    text: str,
) -> list[float]:
    return [
        float(part.strip())
        for part
        in text.split(",")
        if part.strip()
    ]


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--z-values",
        default="0.3,0.2,0.1,0.05",
    )

    parser.add_argument(
        "--order",
        type=int,
        default=250,
    )

    args = parser.parse_args()

    coefficient = (
        symbolic_coefficient()
    )

    coefficient_float = float(
        coefficient
    )

    print(
        {
            "symbolic_z4_coefficient":
                str(coefficient),
            "decimal":
                coefficient_float,
        }
    )

    errors = []

    for z in parse_floats(
        args.z_values
    ):
        ratio = exact_ratio(
            z,
            args.order,
        )

        measured = (
            ratio - 1.0
        ) / z**4

        error = abs(
            measured
            -
            coefficient_float
        )

        errors.append(error)

        print(
            {
                "z": z,
                "K_ratio": ratio,
                "measured_z4_coefficient":
                    measured,
                "absolute_error":
                    error,
            }
        )

    if len(errors) >= 2:
        assert errors[-1] < errors[0]

    a_plus_b = (
        8 * coefficient
    )

    assert (
        a_plus_b
        ==
        sp.Rational(
            508,
            4725,
        )
    )

    print(
        {
            "a4_plus_b4":
                str(a_plus_b),
            "decimal":
                float(a_plus_b),
        }
    )

    print(
        "PASS: exact plane-wave calibration gives a4+b4 = 508/4725."
    )


if __name__ == "__main__":
    main()
