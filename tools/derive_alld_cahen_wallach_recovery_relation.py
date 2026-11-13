#!/usr/bin/env python3
"""All-dimensional symmetric-plane-wave calibration of the recovery coefficient.

For a centered small Ricci-flat Cahen--Wallach diamond in spacetime dimension
d >= 4, write the vacuum recovery response as

    K_d / K_d^Mink
      = 1 + L^4 [a_d E^2 + b_d H^2 + c_d D^2] + o(L^4).

For a symmetric plane wave with constant trace-free transverse profile P,

    T2 = tr(P^2),
    E^2 = T2/4,
    H^2 = T2/2,
    D^2 = T2.

The exact volume-null edge functional gives

    a_d/4 + b_d/2 + c_d = rho_d,

where

    rho_d =
      (21 d^4 + 138 d^3 + 196 d^2 - 200 d - 288)
      /
      (1152 (d-1) (d+1)^2 (d+3)).

The symbolic part derives rho_d from:
- the exact thin-null Jacobi determinant coefficient;
- the coarea reduction of the joint;
- the spherical quadratic-form average;
- the flat Beta(d/2-1,d/2-1) longitudinal weight.

The numerical part evaluates the unexpanded exact plane-wave functional for
two-eigenvalue trace-free profiles in d=4..7.  For d>4, averaging P and -P
removes the cubic invariant tr(P^3), isolating the quadratic coefficient.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
import sympy as sp
from scipy.special import roots_jacobi


def symbolic_relation() -> sp.Expr:
    d = sp.symbols("d", positive=True)
    m = d / 2

    # Universal thin-null / plane-wave parent-volume coefficient:
    # c_P(U)/c_0(U) = 1 + lambda_d U^4 tr(P^2) + ...
    lambda_d = sp.factor(
        sp.Rational(1, 360)
        * (
            1
            - 2
            * sp.rf(m, 4)
            / sp.rf(d, 4)
        )
    )

    expected_lambda = (
        d * (7 * d + 22)
        /
        (
            2880
            * (d + 1)
            * (d + 3)
        )
    )

    assert sp.simplify(
        lambda_d - expected_lambda
    ) == 0

    # Let x=u/U, q=x(1-x).
    #
    # S/s0 = I + A P + C P^2 + ...
    # A = U^2 q/3,
    # C = -U^4 q(1-3q)/45.
    #
    # After coarea, the joint angular factor is
    #
    # det(S)^(-1/2) <(y^T S y)^(-m)>.
    #
    # Its quadratic correction, averaged over the flat longitudinal
    # Beta(m-1,m-1) weight, is:
    edge_angular = sp.factor(
        sp.Rational(1, 180)
        +
        m * (3 - m)
        /
        (
            360
            * (2 * m - 1)
            * (2 * m + 1)
        )
    )

    expected_edge = (
        7 * d**2 + 6 * d - 8
    ) / (
        1440 * (d**2 - 1)
    )

    assert sp.simplify(
        edge_angular - expected_edge
    ) == 0

    # The normalized subinterval-volume factors contribute
    #
    # [c(U)/c0(U)]^(2/m)
    # [c(u)c(U-u)/(c0(u)c0(U-u))]^(-(m+1)/m).
    #
    # Under x ~ Beta(m-1,m-1),
    #
    # <x^4+(1-x)^4>
    #   = (m+1)(m+2) / [2(2m-1)(2m+1)].
    fourth_moment_sum = (
        (m + 1) * (m + 2)
        /
        (
            2
            * (2 * m - 1)
            * (2 * m + 1)
        )
    )

    volume_null = sp.factor(
        lambda_d
        * (
            2 / m
            -
            (m + 1) / m
            * fourth_moment_sum
        )
    )

    # Coefficient of U^4 tr(P^2).
    kappa_u = sp.factor(
        edge_angular + volume_null
    )

    expected_kappa_u = (
        21 * d**4
        + 138 * d**3
        + 196 * d**2
        - 200 * d
        - 288
    ) / (
        4608
        * (d - 1)
        * (d + 1)**2
        * (d + 3)
    )

    assert sp.simplify(
        kappa_u - expected_kappa_u
    ) == 0

    # U=sqrt(2)L, hence U^4=4L^4.
    rho_d = sp.factor(
        4 * kappa_u
    )

    expected_rho = (
        21 * d**4
        + 138 * d**3
        + 196 * d**2
        - 200 * d
        - 288
    ) / (
        1152
        * (d - 1)
        * (d + 1)**2
        * (d + 3)
    )

    assert sp.simplify(
        rho_d - expected_rho
    ) == 0

    # d=4 regression.  In four dimensions,
    # physical E^2 and B^2 are both T2/4 for the symmetric wave, so
    # a4+b4 = 4 rho_4.
    rho4 = sp.factor(
        rho_d.subs(d, 4)
    )

    assert rho4 == sp.Rational(
        127,
        4725,
    )

    assert 4 * rho4 == sp.Rational(
        508,
        4725,
    )

    print(
        {
            "lambda_d": str(sp.factor(lambda_d)),
            "edge_angular_U4_T2":
                str(sp.factor(edge_angular)),
            "volume_null_U4_T2":
                str(sp.factor(volume_null)),
            "kappa_U4_T2":
                str(kappa_u),
            "rho_L4_invariant_combination":
                str(rho_d),
            "d4_rho":
                str(rho4),
            "d4_a4_plus_b4":
                str(4 * rho4),
        }
    )

    return rho_d


def beta_nodes(
    a: float,
    b: float,
    order: int,
) -> tuple[np.ndarray, np.ndarray]:
    z, weights = roots_jacobi(
        order,
        b - 1.0,
        a - 1.0,
    )

    x = (z + 1.0) / 2.0
    weights = weights / np.sum(weights)

    return x, weights


def jacobi_channel(
    h: float,
    t: float,
) -> float:
    if abs(t) < 1e-15:
        return 0.0

    scale = abs(h) * t * t

    if scale < 1e-10:
        return (
            t
            * (
                1.0
                + h * t * t / 6.0
                + h * h * t**4 / 120.0
                + h**3 * t**6 / 5040.0
            )
        )

    if h > 0.0:
        q = math.sqrt(h)
        return math.sinh(q * t) / q

    q = math.sqrt(-h)
    return math.sin(q * t) / q


def exact_ratio(
    d: int,
    epsilon: float,
    order: int,
) -> float:
    n = d - 2
    m = d / 2.0

    # Two-eigenvalue trace-free profile:
    # one eigenvalue epsilon and n-1 equal eigenvalues -epsilon/(n-1).
    profile = np.array(
        [epsilon]
        +
        [-epsilon / (n - 1)] * (n - 1),
        dtype=float,
    )

    inner_x, inner_w = beta_nodes(
        m,
        m,
        order,
    )

    outer_x, outer_w = beta_nodes(
        m - 1.0,
        m - 1.0,
        order,
    )

    # If X is the squared projection onto the distinguished eigendirection,
    # then X ~ Beta(1/2,(n-1)/2).
    angular_x, angular_w = beta_nodes(
        0.5,
        (n - 1) / 2.0,
        order,
    )

    def det_ratio(t: float) -> float:
        if abs(t) < 1e-15:
            return 1.0

        value = 1.0

        for h in profile:
            value *= (
                jacobi_channel(h, t)
                / t
            )

        return value

    def thin_ratio(r: float) -> float:
        if abs(r) < 1e-15:
            return 1.0

        average = 0.0

        for x, weight in zip(
            inner_x,
            inner_w,
        ):
            average += (
                weight
                * math.sqrt(
                    det_ratio(r * x)
                    * det_ratio(
                        r * (1.0 - x)
                    )
                )
            )

        return average / math.sqrt(
            det_ratio(r)
        )

    p = (m + 1.0) / m
    integral = 0.0

    for x, weight in zip(
        outer_x,
        outer_w,
    ):
        u = x
        w = 1.0 - x

        s_tilde = []

        for h in profile:
            s = (
                jacobi_channel(h, 1.0)
                /
                (
                    jacobi_channel(h, u)
                    * jacobi_channel(h, w)
                )
            )

            s_tilde.append(
                s * u * w
            )

        s_tilde = np.asarray(
            s_tilde,
            dtype=float,
        )

        determinant_factor = (
            np.prod(s_tilde)
            ** (-0.5)
        )

        # All non-distinguished eigenvalues are equal.
        quadratic = (
            angular_x * s_tilde[0]
            +
            (1.0 - angular_x)
            * s_tilde[1]
        )

        angular_factor = (
            determinant_factor
            * float(
                np.sum(
                    angular_w
                    * quadratic ** (-m)
                )
            )
        )

        integral += (
            weight
            * thin_ratio(u) ** (-p)
            * thin_ratio(w) ** (-p)
            * angular_factor
        )

    return (
        thin_ratio(1.0) ** (2.0 / m)
        * integral
    )


def numerical_regression(
    rho_symbolic: sp.Expr,
    order: int,
) -> None:
    d_symbol = next(
        symbol
        for symbol in rho_symbolic.free_symbols
        if symbol.name == "d"
    )

    for d in range(4, 8):
        predicted_rho = float(
            rho_symbolic.subs(
                d_symbol,
                d,
            )
        )

        # rho is the coefficient of L^4 T2.
        # With U=1, L=1/sqrt(2), so the exact ratio coefficient per T2
        # is rho/4.
        predicted_u = (
            predicted_rho / 4.0
        )

        epsilon_values = (
            0.10,
            0.05,
            0.025,
        )

        errors = []

        for epsilon in epsilon_values:
            plus = exact_ratio(
                d,
                epsilon,
                order,
            )

            minus = exact_ratio(
                d,
                -epsilon,
                order,
            )

            n = d - 2

            t2 = (
                epsilon**2
                * n
                / (n - 1)
            )

            # Symmetrizing P -> -P removes the cubic invariant.
            measured = (
                (
                    (plus - 1.0)
                    +
                    (minus - 1.0)
                )
                / 2.0
                / t2
            )

            error = abs(
                measured
                - predicted_u
            )

            errors.append(error)

            print(
                {
                    "d": d,
                    "epsilon": epsilon,
                    "measured_U4_T2":
                        measured,
                    "predicted_U4_T2":
                        predicted_u,
                    "absolute_error":
                        error,
                }
            )

        assert errors[-1] < errors[0]
        assert errors[-1] < 1e-6


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--order",
        type=int,
        default=70,
    )

    parser.add_argument(
        "--skip-numerical",
        action="store_true",
    )

    args = parser.parse_args()

    rho = symbolic_relation()

    if not args.skip_numerical:
        numerical_regression(
            rho,
            args.order,
        )

    print(
        "PASS: all-d Cahen--Wallach recovery relation derived; "
        "d=4 exact regression and d=4..7 unexpanded numerical checks pass."
    )


if __name__ == "__main__":
    main()
