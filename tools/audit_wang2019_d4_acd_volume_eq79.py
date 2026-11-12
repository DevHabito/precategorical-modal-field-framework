#!/usr/bin/env python3
"""Audit Wang (2019) Eq. (79) against its own Eqs. (74) and (76) in d=4.

Reference:
    Jinzhao Wang, "Geometry of small causal diamonds",
    Phys. Rev. D 100, 064020 (2019), arXiv:1904.01034.

The paper gives:
  - Eq. (74): the vacuum ACD null-cone boundary r^+(t,n),
  - Eq. (76): the Ricci-flat RNC volume density,
  - Eq. (75): the total volume as twice the upper-cone integral,
  - Eq. (79): the stated final closed form.

This checker directly integrates the published intermediate equations in d=4
for two algebraic Weyl representatives:

  1. purely electric: E = diag(2,-1,-1), B = 0,
  2. purely magnetic: E = 0, B = diag(2,-1,-1).

Rotational invariance then fixes the universal coefficients of E^2 and B^2.

Result from Eqs. (74)+(76):
    v_E = 17/630,
    v_B = 1/210.

The d=4 specialization of Eq. (79) instead states:
    v_E = 127/4725,
    v_B = 1/105.

Thus Eq. (79) is internally inconsistent with the preceding published
equations, assuming the transcription of Eqs. (74) and (76) used here.
"""

from __future__ import annotations

import itertools
import sympy as sp


mu, s, r = sp.symbols("mu s r", real=True)
eta = sp.diag(-1, 1, 1, 1)


def set_riemann_symmetries(C, a, b, c, d, value):
    entries = (
        (a, b, c, d, value),
        (b, a, c, d, -value),
        (a, b, d, c, -value),
        (b, a, d, c, value),
        (c, d, a, b, value),
        (d, c, a, b, -value),
        (c, d, b, a, -value),
        (d, c, b, a, value),
    )
    for i, j, k, l, v in entries:
        C[i, j, k, l] = sp.simplify(v)


def build_weyl(E: sp.Matrix, B: sp.Matrix):
    """Build a 4D vacuum Weyl tensor from symmetric trace-free E and B.

    Spatial indices are 0,1,2 internally and map to spacetime indices 1,2,3.
    We use
        C_{0i0j} = E_{ij},
        H_{ijk}=C_{0ijk}=epsilon_{jkl} B_{il},
        D_{ijkl}
          = delta_{ik}E_{jl}-delta_{il}E_{jk}
            -delta_{jk}E_{il}+delta_{jl}E_{ik}.
    """
    C = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)
    H = sp.MutableDenseNDimArray.zeros(3, 3, 3)
    delta = sp.eye(3)

    for i, j in itertools.product(range(3), repeat=2):
        if E[i, j] != 0:
            set_riemann_symmetries(
                C, 0, i + 1, 0, j + 1, E[i, j]
            )

    for i, j, k in itertools.product(range(3), repeat=3):
        value = sum(
            sp.LeviCivita(j, k, l) * B[i, l]
            for l in range(3)
        )
        H[i, j, k] = sp.simplify(value)
        if value != 0:
            set_riemann_symmetries(
                C, 0, i + 1, j + 1, k + 1, value
            )

    for i, j, k, l in itertools.product(range(3), repeat=4):
        value = (
            delta[i, k] * E[j, l]
            - delta[i, l] * E[j, k]
            - delta[j, k] * E[i, l]
            + delta[j, l] * E[i, k]
        )
        if value != 0:
            set_riemann_symmetries(
                C, i + 1, j + 1, k + 1, l + 1, value
            )

    # Vacuum trace check.
    for b, d in itertools.product(range(4), repeat=2):
        ricci = sum(
            eta[a, c] * C[a, b, c, d]
            for a, c in itertools.product(range(4), repeat=2)
        )
        assert sp.simplify(ricci) == 0

    return C, H


def volume_coefficient(E: sp.Matrix, B: sp.Matrix) -> sp.Expr:
    """Integrate Wang Eqs. (74) and (76) in d=4 with l=1."""
    C, H = build_weyl(E, B)

    # Axisymmetric representatives allow phi=0 without loss.
    n = [
        mu,
        sp.sqrt(1 - mu**2),
        sp.Integer(0),
    ]

    E_nn = sp.expand(
        sum(
            E[i, j] * n[i] * n[j]
            for i, j in itertools.product(range(3), repeat=2)
        )
    )

    E2_nn = sp.expand(
        sum(
            E[i, k] * E[k, j] * n[i] * n[j]
            for i, j, k in itertools.product(range(3), repeat=3)
        )
    )

    hh4 = sp.Integer(0)
    ee4 = sp.Integer(0)

    for i, j, l, k in itertools.product(range(3), repeat=4):
        hh = sum(
            H[i, m, j] * H[l, m, k]
            for m in range(3)
        )
        hh4 += hh * n[i] * n[j] * n[l] * n[k]
        ee4 += (
            E[i, j]
            * E[l, k]
            * n[i]
            * n[j]
            * n[l]
            * n[k]
        )

    # Eq. (74), upper cone, l=1.
    #
    # r^+ = (1-s) [1 + A + B + O(C^3)],
    # where A is linear and B quadratic in Weyl.
    A = E_nn / 6

    B_quad = (
        E_nn**2 / 24
        - s * E2_nn / 45
        + (1 - s) ** 2
        * (E2_nn + hh4 - ee4)
        / 90
    )

    # In d=4, integral_0^{r+} r^2 dr = (r+)^3/3.
    # The quadratic boundary contribution is
    # (1-s)^3 [B_quad + A^2].
    boundary = sp.expand(
        (1 - s) ** 3
        * (B_quad + A**2)
    )

    # Eq. (76):
    # sqrt(g) = 1 - Q(x)/180,
    # Q = C^gamma_mu^alpha_nu C_{gamma rho alpha sigma}
    #     x^mu x^nu x^rho x^sigma.
    X = [
        s,
        r * n[0],
        r * n[1],
        r * n[2],
    ]

    Q = sp.Integer(0)

    for gamma, alpha, m, nu, rho, sigma in itertools.product(
        range(4), repeat=6
    ):
        first = (
            eta[gamma, gamma]
            * eta[alpha, alpha]
            * C[gamma, m, alpha, nu]
        )
        second = C[gamma, rho, alpha, sigma]

        if first != 0 and second != 0:
            Q += (
                first
                * second
                * X[m]
                * X[nu]
                * X[rho]
                * X[sigma]
            )

    determinant = sp.integrate(
        -r**2 * sp.expand(Q) / 180,
        (r, 0, 1 - s),
    )

    upper_density = sp.expand(boundary + determinant)

    # Spherical average. Axisymmetry makes the normalized S^2 average
    # (1/2) integral_{-1}^{1} dmu.
    angular_average = sp.simplify(
        sp.integrate(
            upper_density,
            (mu, -1, 1),
        )
        / 2
    )

    # Eq. (75): double the upper cone.
    # V_flat(d=4,l=1)=2*pi/3.
    # The normalization reduces to a factor 12 after the normalized S^2 average.
    relative = sp.simplify(
        12
        * sp.integrate(
            angular_average,
            (s, 0, 1),
        )
    )

    return relative


def contribution_split(E: sp.Matrix, B: sp.Matrix) -> tuple[sp.Expr, sp.Expr]:
    """Return separately the moving-boundary and RNC-determinant pieces."""
    C, H = build_weyl(E, B)
    n = [mu, sp.sqrt(1 - mu**2), sp.Integer(0)]

    E_nn = sp.expand(sum(
        E[i, j] * n[i] * n[j]
        for i, j in itertools.product(range(3), repeat=2)
    ))
    E2_nn = sp.expand(sum(
        E[i, k] * E[k, j] * n[i] * n[j]
        for i, j, k in itertools.product(range(3), repeat=3)
    ))

    hh4 = sp.Integer(0)
    ee4 = sp.Integer(0)
    for i, j, l, k in itertools.product(range(3), repeat=4):
        hh = sum(H[i, m, j] * H[l, m, k] for m in range(3))
        hh4 += hh * n[i] * n[j] * n[l] * n[k]
        ee4 += E[i, j] * E[l, k] * n[i] * n[j] * n[l] * n[k]

    A = E_nn / 6
    B_quad = (
        E_nn**2 / 24
        - s * E2_nn / 45
        + (1 - s)**2 * (E2_nn + hh4 - ee4) / 90
    )
    boundary = sp.expand((1 - s)**3 * (B_quad + A**2))

    X = [s, r * n[0], r * n[1], r * n[2]]
    Q = sp.Integer(0)
    for gamma, alpha, m, nu, rho, sigma in itertools.product(range(4), repeat=6):
        first = eta[gamma, gamma] * eta[alpha, alpha] * C[gamma, m, alpha, nu]
        second = C[gamma, rho, alpha, sigma]
        if first != 0 and second != 0:
            Q += first * second * X[m] * X[nu] * X[rho] * X[sigma]

    determinant = sp.integrate(
        -r**2 * sp.expand(Q) / 180,
        (r, 0, 1 - s),
    )

    def normalized(piece: sp.Expr) -> sp.Expr:
        angular = sp.simplify(
            sp.integrate(piece, (mu, -1, 1)) / 2
        )
        return sp.simplify(
            12 * sp.integrate(angular, (s, 0, 1))
        )

    return normalized(boundary), normalized(determinant)


def norm2(M: sp.Matrix) -> sp.Expr:
    return sp.simplify(
        sum(
            M[i, j] ** 2
            for i, j in itertools.product(range(3), repeat=2)
        )
    )


def main() -> None:
    electric = sp.diag(2, -1, -1)
    magnetic = sp.diag(2, -1, -1)
    zero = sp.zeros(3)

    pure_electric_relative = volume_coefficient(
        electric,
        zero,
    )
    pure_magnetic_relative = volume_coefficient(
        zero,
        magnetic,
    )

    E2 = norm2(electric)
    B2 = norm2(magnetic)

    vE = sp.simplify(
        pure_electric_relative / E2
    )
    vB = sp.simplify(
        pure_magnetic_relative / B2
    )

    boundary_E, determinant_E = contribution_split(electric, zero)
    boundary_B, determinant_B = contribution_split(zero, magnetic)

    assert sp.simplify(boundary_E / E2) == sp.Rational(1, 36)
    assert sp.simplify(determinant_E / E2) == -sp.Rational(1, 1260)
    assert sp.simplify(boundary_B / B2) == sp.Rational(1, 225)
    assert sp.simplify(determinant_B / B2) == sp.Rational(1, 3150)

    assert E2 == 6
    assert B2 == 6

    assert pure_electric_relative == sp.Rational(17, 105)
    assert pure_magnetic_relative == sp.Rational(1, 35)

    assert vE == sp.Rational(17, 630)
    assert vB == sp.Rational(1, 210)

    # d=4 specialization of Wang Eq. (79).
    wang_vE = sp.Rational(127, 4725)
    wang_vB = sp.Rational(1, 105)

    delta_E = sp.simplify(vE - wang_vE)
    delta_B = sp.simplify(vB - wang_vB)

    assert delta_E == sp.Rational(1, 9450)
    assert delta_B == -sp.Rational(1, 210)

    # Type-N plane-wave check E^2=B^2=omega^4/2.
    # Correct coefficient of omega^4 L^4:
    type_n = sp.simplify((vE + vB) / 2)
    wang_type_n = sp.simplify((wang_vE + wang_vB) / 2)

    assert type_n == sp.Rational(1, 63)
    assert wang_type_n == sp.Rational(86, 9450)

    print(
        {
            "from_Eq74_Eq76_vE": str(vE),
            "from_Eq74_Eq76_vB": str(vB),
            "Wang_Eq79_vE": str(wang_vE),
            "Wang_Eq79_vB": str(wang_vB),
            "delta_vE": str(delta_E),
            "delta_vB": str(delta_B),
            "boundary_E2": str(sp.simplify(boundary_E / E2)),
            "determinant_E2": str(sp.simplify(determinant_E / E2)),
            "boundary_B2": str(sp.simplify(boundary_B / B2)),
            "determinant_B2": str(sp.simplify(determinant_B / B2)),
            "type_N_correct": str(type_n),
            "type_N_Eq79": str(wang_type_n),
        }
    )

    print(
        "PASS: Wang Eqs. (74)+(76) imply "
        "vE=17/630 and vB=1/210, not the d=4 specialization of Eq. (79)."
    )


if __name__ == "__main__":
    main()
