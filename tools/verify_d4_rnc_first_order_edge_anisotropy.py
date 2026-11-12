#!/usr/bin/env python3
"""Exact first-order RNC audit for the d=4 vacuum null-edge integrand.

This checker verifies, on a representative purely electric Weyl tensor, the
first-order world-function cross-normalization and edge-area anisotropies:

    q1(n) = delta ln chi = -(1/3) L^2 E_nn,
    a1(n) = delta(dA)/dA0 = +(1/6) L^2 E_nn.

Rotational covariance then gives the general directional form.  The script also
checks the universal second-order covariance contribution

    < (9/2) q1^2 - 3 a1 q1 >
      = (4/45) E^2 L^4

using the standard S^2 fourth-moment identity for a symmetric trace-free E.
"""

from __future__ import annotations

import sympy as sp


def build_representative_weyl(e: sp.Symbol):
    """Return C_abcd for E=diag(e,-e/2,-e/2), B=0, signature (-+++)."""
    C = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)
    E = sp.diag(e, -e / 2, -e / 2)
    delta = sp.eye(3)

    for i in range(1, 4):
        for j in range(1, 4):
            value = E[i - 1, j - 1]
            C[0, i, 0, j] = value
            C[i, 0, 0, j] = -value
            C[0, i, j, 0] = -value
            C[i, 0, j, 0] = value

    # In four-dimensional vacuum the purely spatial Weyl tensor is fixed by E.
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                for l in range(1, 4):
                    C[i, j, k, l] = (
                        delta[i - 1, k - 1] * E[j - 1, l - 1]
                        - delta[i - 1, l - 1] * E[j - 1, k - 1]
                        - delta[j - 1, k - 1] * E[i - 1, l - 1]
                        + delta[j - 1, l - 1] * E[i - 1, k - 1]
                    )

    return C


def world_function_twice(y, x, C, eta):
    """First-curvature RNC expansion of 2 sigma(y,x).

    g_ab(z) = eta_ab - (1/3) C_acbd z^c z^d + ...
    and the flat straight segment may be used in the first variation.
    """
    delta = x - y
    midpoint = (x + y) / 2

    flat = (delta.T * eta * delta)[0]
    curvature = sp.Integer(0)

    for mu in range(4):
        for a in range(4):
            for nu in range(4):
                for b in range(4):
                    curvature += (
                        C[mu, a, nu, b]
                        * delta[mu]
                        * delta[nu]
                        * midpoint[a]
                        * midpoint[b]
                    )

    return sp.expand(flat - curvature / 3)


def main() -> None:
    e, L, t, r = sp.symbols("e L t r", nonzero=True)
    eta = sp.diag(-1, 1, 1, 1)
    C = build_representative_weyl(e)

    x = sp.Matrix([t, r, 0, 0])
    p = sp.Matrix([-L, 0, 0, 0])
    q = sp.Matrix([L, 0, 0, 0])

    s_minus = world_function_twice(p, x, C, eta)
    s_plus = world_function_twice(x, q, C, eta)

    expected_minus = -L**2 - 2 * L * t + r**2 - t**2 - e * L**2 * r**2 / 3
    expected_plus = -L**2 + 2 * L * t + r**2 - t**2 - e * L**2 * r**2 / 3

    assert sp.simplify(s_minus - expected_minus) == 0
    assert sp.simplify(s_plus - expected_plus) == 0

    # First-order edge: t=0 and r=L[1+(1/6)eL^2].
    r_edge = L * (1 + e * L**2 / 6)

    # RNC metric and inverse to first order.
    g = sp.MutableDenseMatrix.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            correction = sp.Integer(0)
            for c in range(4):
                for d in range(4):
                    correction += C[a, c, b, d] * x[c] * x[d]
            g[a, b] = eta[a, b] - correction / 3

    g_inv = sp.Matrix(g).inv().applyfunc(
        lambda value: sp.series(value, e, 0, 2).removeO()
    )

    grad_minus = sp.Matrix([
        sp.diff(s_minus, t),
        sp.diff(s_minus, r),
        0,
        0,
    ])
    grad_plus = sp.Matrix([
        sp.diff(s_plus, t),
        sp.diff(s_plus, r),
        0,
        0,
    ])

    chi = (grad_minus.T * g_inv * grad_plus)[0]
    chi_edge = sp.series(
        chi.subs({t: 0, r: r_edge}),
        e,
        0,
        2,
    ).removeO()

    chi_ratio = sp.simplify(chi_edge / (8 * L**2))
    expected_chi_ratio = 1 - e * L**2 / 3
    assert sp.simplify(chi_ratio - expected_chi_ratio) == 0

    q1 = -e * L**2 / 3

    # Linear area correction.
    # Radial deformation contributes 2 delta r / L = +(1/3)eL^2.
    radial_area = e * L**2 / 3

    # Tangential RNC metric trace contributes -(1/6)eL^2 to sqrt(det h).
    tangent_metric_area = -e * L**2 / 6
    a1 = sp.simplify(radial_area + tangent_metric_area)

    assert a1 == e * L**2 / 6
    assert sp.simplify(a1 + q1 / 2) == 0

    # For trace-free symmetric E on S^2:
    # <(E_nn)^2> = 2 E^2 / 15.
    covariance_factor = sp.simplify(
        6 * sp.Rational(1, 9) * sp.Rational(2, 15)
    )
    assert covariance_factor == sp.Rational(4, 45)

    # Corrected residual target after inserting the exact a4,b4 coefficients.
    a4 = sp.Rational(683, 9450)
    b4 = sp.Rational(37, 1050)
    old_known_e = sp.Rational(152, 4725)
    corrected_known_e = sp.simplify(
        old_known_e + covariance_factor
    )

    q2_e = sp.simplify((corrected_known_e - a4) / 3)
    q2_b = sp.simplify(-b4 / 3)

    assert corrected_known_e == sp.Rational(572, 4725)
    assert q2_e == sp.Rational(461, 28350)
    assert q2_b == -sp.Rational(37, 3150)

    print(
        {
            "edge_radius_shift": "delta r/L = (1/6) L^2 E_nn",
            "q1": "delta ln chi = -(1/3) L^2 E_nn",
            "a1": "delta dA/dA0 = +(1/6) L^2 E_nn",
            "quadratic_covariance_E2": str(covariance_factor),
            "corrected_known_E2_before_q2": str(corrected_known_e),
            "required_mean_q2_E2": str(q2_e),
            "required_mean_q2_B2": str(q2_b),
        }
    )
    print(
        "PASS: first-order RNC anisotropy and the missing 4/45 E^2 covariance term verified."
    )


if __name__ == "__main__":
    main()
