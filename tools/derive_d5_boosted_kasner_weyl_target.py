#!/usr/bin/env python3
"""Exact Weyl-invariant target for a transversely boosted d=5 LRS-Kasner observer.

Metric at t=1:
    ds^2 = -dt^2 + t^(-1) dx^2 + t (dy_1^2+dy_2^2+dy_3^2).

Comoving Kasner exponents:
    p_x = -1/2,
    p_y = +1/2.

The comoving frame is purely electric.  A Lorentz boost in one transverse
direction y_1 produces a nonzero hook/magnetic Weyl sector.

This checker constructs the full orthonormal-frame Weyl tensor from the
Kasner Riemann components, performs the exact Lorentz transformation, and
computes

    E^2 = C_{0i0j} C_{0i0j},
    H^2 = C_{0ijk} C_{0ijk},
    D^2 = C_{ijkl} C_{ijkl}.

For boost speed v,

    E^2 = (v^4 + 2v^2 + 3) / [4(1-v^2)^2],
    H^2 = 3v^2 / (1-v^2)^2,
    D^2 = (7v^4 + 2v^2 + 3) / [2(1-v^2)^2].

The corrected d=5 ACD volume law therefore predicts

    delta V / V_flat / L^4
      = (8v^4 + 24v^2 + 25)
        / [1152(1-v^2)^2].

This is a target for a future direct causal-volume calculation around the
boosted timelike geodesic.  The present script does not perform that volume
integration.
"""

from __future__ import annotations

import sympy as sp


def set_riemann_symmetries(
    tensor: sp.MutableDenseNDimArray,
    a: int,
    b: int,
    c: int,
    d: int,
    value: sp.Expr,
) -> None:
    for aa, bb, sign_ab in (
        (a, b, 1),
        (b, a, -1),
    ):
        for cc, dd, sign_cd in (
            (c, d, 1),
            (d, c, -1),
        ):
            tensor[aa, bb, cc, dd] = (
                sign_ab * sign_cd * value
            )
            tensor[cc, dd, aa, bb] = (
                sign_ab * sign_cd * value
            )


def main() -> None:
    v = sp.symbols("v", real=True)
    gamma = 1 / sp.sqrt(1 - v**2)

    # d=5 -> four spatial dimensions.
    n = 4
    dim = 5

    exponents = [
        -sp.Rational(1, 2),
        sp.Rational(1, 2),
        sp.Rational(1, 2),
        sp.Rational(1, 2),
    ]

    C = sp.MutableDenseNDimArray.zeros(
        dim,
        dim,
        dim,
        dim,
    )

    # In an orthonormal Kasner frame at t=1:
    #
    # C_{0i0i}=p_i(1-p_i),
    # C_{ijij}=p_i p_j,
    #
    # and Ricci=0, so Riemann=Weyl.
    for i in range(1, dim):
        p_i = exponents[i - 1]

        set_riemann_symmetries(
            C,
            0,
            i,
            0,
            i,
            p_i * (1 - p_i),
        )

    for i in range(1, dim):
        for j in range(i + 1, dim):
            set_riemann_symmetries(
                C,
                i,
                j,
                i,
                j,
                exponents[i - 1]
                * exponents[j - 1],
            )

    # Boost in transverse spatial direction index 2.
    Lambda = sp.eye(dim)

    Lambda[0, 0] = gamma
    Lambda[0, 2] = gamma * v
    Lambda[2, 0] = gamma * v
    Lambda[2, 2] = gamma

    def transformed(
        a: int,
        b: int,
        c: int,
        d: int,
    ) -> sp.Expr:
        result = sp.Integer(0)

        for A in range(dim):
            if Lambda[a, A] == 0:
                continue
            for B in range(dim):
                if Lambda[b, B] == 0:
                    continue
                for C_index in range(dim):
                    if Lambda[c, C_index] == 0:
                        continue
                    for D in range(dim):
                        if Lambda[d, D] == 0:
                            continue

                        result += (
                            Lambda[a, A]
                            * Lambda[b, B]
                            * Lambda[c, C_index]
                            * Lambda[d, D]
                            * C[A, B, C_index, D]
                        )

        return sp.simplify(result)

    e2 = sp.Integer(0)
    h2 = sp.Integer(0)
    d2 = sp.Integer(0)

    for i in range(1, dim):
        for j in range(1, dim):
            e2 += transformed(
                0,
                i,
                0,
                j,
            ) ** 2

            for k in range(1, dim):
                h2 += transformed(
                    0,
                    i,
                    j,
                    k,
                ) ** 2

                for ell in range(1, dim):
                    d2 += transformed(
                        i,
                        j,
                        k,
                        ell,
                    ) ** 2

    e2 = sp.factor(e2)
    h2 = sp.factor(h2)
    d2 = sp.factor(d2)

    expected_e2 = (
        v**4 + 2 * v**2 + 3
    ) / (
        4 * (1 - v**2) ** 2
    )

    expected_h2 = (
        3 * v**2
        / (1 - v**2) ** 2
    )

    expected_d2 = (
        7 * v**4
        + 2 * v**2
        + 3
    ) / (
        2 * (1 - v**2) ** 2
    )

    assert sp.simplify(
        e2 - expected_e2
    ) == 0

    assert sp.simplify(
        h2 - expected_h2
    ) == 0

    assert sp.simplify(
        d2 - expected_d2
    ) == 0

    # Corrected d=5 coefficients.
    a5 = sp.Rational(151, 5184)
    b5 = sp.Rational(11, 5184)
    c5 = -sp.Rational(1, 10368)

    predicted = sp.factor(
        a5 * e2
        + b5 * h2
        + c5 * d2
    )

    expected_predicted = (
        8 * v**4
        + 24 * v**2
        + 25
    ) / (
        1152 * (1 - v**2) ** 2
    )

    assert sp.simplify(
        predicted - expected_predicted
    ) == 0

    assert sp.simplify(
        predicted.subs(v, 0)
        - sp.Rational(25, 1152)
    ) == 0

    print(
        {
            "E2_boosted": str(e2),
            "H2_boosted": str(h2),
            "D2_boosted": str(d2),
            "predicted_d5_L4_coefficient":
                str(predicted),
            "comoving_limit":
                str(predicted.subs(v, 0)),
        }
    )

    print(
        "PASS: a transverse boost of d=5 LRS Kasner generates H^2 != 0 "
        "and provides a one-parameter independent target for the corrected "
        "all-d ACD volume law."
    )


if __name__ == "__main__":
    main()
