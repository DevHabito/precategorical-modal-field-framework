#!/usr/bin/env python3
"""All-dimensional pure-spatial-Weyl calibration of the vacuum recovery law.

For d >= 5 choose an ultrastatic Ricci-flat spacetime

    g = -dt^2 + h,

where the (d-1)-dimensional Riemannian metric h is Ricci flat and non-flat.
Relative to T=partial_t,

    E = 0,
    H = 0,
    D = Riem(h).

Thus the vacuum recovery response

    K_d/K_d^Mink
      = 1 + L^4[a_d E^2+b_d H^2+c_d D^2] + o(L^4)

isolates c_d.

The derivation combines:
1. the classical Ricci-flat small-geodesic-ball coefficient;
2. the induced geodesic-sphere area coefficient;
3. the universal thin-null Jacobi determinant correction;
4. the exact ultrastatic cross-normalization g^{-1}(d alpha,d beta)=2.

It gives

    c_d =
      -(3 d^3 + 32 d^2 + 68 d + 48)
      /
      [192 (d-1)(d+1)^2(d+3)(d+4)].
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    d = sp.symbols(
        "d",
        integer=True,
        positive=True,
    )

    N = d - 1
    m = d / 2

    # ---------------------------------------------------------------
    # 1. Parent Alexandrov volume from Riemannian geodesic balls
    # ---------------------------------------------------------------
    #
    # Gray--Vanhecke small-ball expansion in N-dimensional Ricci-flat h:
    #
    # Vol_h(B_r)/Vol_flat(B_r)
    #   = 1 - D^2 r^4/[120 (N+2)(N+4)] + ...
    #
    # The ultrastatic diamond is
    #
    # V_D = 2 int_0^L Vol_h(B_r) dr.
    #
    # Therefore its relative D^2 L^4 coefficient is:
    parent_volume = sp.factor(
        -d
        /
        (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    # The intrinsic recovery coefficient contains V_D^(2/m)=V_D^(4/d).
    parent_recovery = sp.factor(
        sp.Rational(4, 1)
        / d
        * parent_volume
    )

    expected_parent_recovery = (
        -1
        /
        (
            30
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    assert sp.simplify(
        parent_recovery
        - expected_parent_recovery
    ) == 0

    # ---------------------------------------------------------------
    # 2. Geodesic-sphere edge area
    # ---------------------------------------------------------------
    #
    # Differentiate the small-ball volume:
    #
    # Area_h(S_L)/Area_flat(S_L)
    #   = 1 - D^2 L^4/[120 N(N+2)] + ...
    edge_area = sp.factor(
        -1
        /
        (
            120
            * N
            * (N + 2)
        )
    )

    expected_edge_area = (
        -1
        /
        (
            120
            * (d - 1)
            * (d + 1)
        )
    )

    assert sp.simplify(
        edge_area
        - expected_edge_area
    ) == 0

    # ---------------------------------------------------------------
    # 3. Angular average of the null/spatial tidal square
    # ---------------------------------------------------------------
    #
    # For a unit spatial radial direction n, define the screen tidal matrix
    #
    # Q_AB(n) = D_{A n B n}.
    #
    # Ricci-flatness gives tr Q=0.  The standard S^(N-1) fourth moment and
    # algebraic Riemann symmetries give
    #
    # <tr Q^2> = 3 D^2/[2 N(N+2)].
    tidal_average = sp.factor(
        sp.Rational(3, 2)
        /
        (
            N
            * (N + 2)
        )
    )

    # Universal thin-null coefficient:
    #
    # c_Q(L)/c_0(L)
    #   = 1 + lambda_d L^4 tr(Q^2) + ...
    lambda_d = sp.factor(
        sp.Rational(1, 360)
        * (
            1
            -
            2
            * sp.rf(m, 4)
            / sp.rf(d, 4)
        )
    )

    expected_lambda = (
        d
        * (7 * d + 22)
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

    # On the centered ultrastatic edge c_+=c_-=c_Q and the recovery
    # integrand carries
    #
    # [c_+ c_-]^(-(m+1)/m)
    #   = c_Q^(-2(m+1)/m).
    thin_recovery = sp.factor(
        -2
        * (m + 1)
        / m
        * lambda_d
        * tidal_average
    )

    expected_thin = (
        -(d + 2)
        * (7 * d + 22)
        /
        (
            960
            * (d - 1)
            * (d + 1)**2
            * (d + 3)
        )
    )

    assert sp.simplify(
        thin_recovery - expected_thin
    ) == 0

    # ---------------------------------------------------------------
    # 4. Cross-normalization
    # ---------------------------------------------------------------
    #
    # With r the Riemannian distance from the center,
    #
    # alpha = t + L - r,
    # beta  = L - t - r.
    #
    # In g=-dt^2+h,
    #
    # g^{-1}(d alpha,d beta)=2
    #
    # exactly wherever r is smooth.  Hence there is no independent
    # geometric cross-angle correction.
    cross_recovery = sp.Integer(0)

    c_d = sp.factor(
        parent_recovery
        + edge_area
        + thin_recovery
        + cross_recovery
    )

    expected_c = (
        -(
            3 * d**3
            + 32 * d**2
            + 68 * d
            + 48
        )
        /
        (
            192
            * (d - 1)
            * (d + 1)**2
            * (d + 3)
            * (d + 4)
        )
    )

    assert sp.simplify(
        c_d - expected_c
    ) == 0

    # Concrete regressions.
    assert c_d.subs(d, 5) == -sp.Rational(
        521,
        663552,
    )

    assert c_d.subs(d, 6) == -sp.Rational(
        47,
        88200,
    )

    print(
        {
            "parent_volume_D2":
                str(parent_volume),
            "parent_recovery_D2":
                str(parent_recovery),
            "edge_area_D2":
                str(edge_area),
            "mean_screen_tidal_square_over_D2":
                str(tidal_average),
            "thin_recovery_D2":
                str(thin_recovery),
            "cross_recovery_D2":
                str(cross_recovery),
            "c_d":
                str(c_d),
            "d5_c5":
                str(c_d.subs(d, 5)),
            "d6_c6":
                str(c_d.subs(d, 6)),
        }
    )

    print(
        "PASS: ultrastatic Ricci-flat calibration isolates the all-d "
        "pure-spatial-Weyl recovery coefficient c_d."
    )


if __name__ == "__main__":
    main()
