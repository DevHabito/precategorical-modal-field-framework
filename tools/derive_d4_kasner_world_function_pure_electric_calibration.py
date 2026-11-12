#!/usr/bin/env python3
"""Exact LRS-Kasner world-function calibration of the d=4 vacuum recovery law.

Metric
------
    ds^2 = -dt^2 + t^(-2/3) dx^2 + t^(4/3) (dy^2 + dz^2)

This is the nontrivial locally rotationally symmetric Kasner vacuum with
exponents (-1/3, 2/3, 2/3).  The comoving central line is geodesic, so tips

    p = (1-L, 0,0,0),  q = (1+L, 0,0,0)

form an exactly centered Alexandrov interval with half proper time L.

The script derives, with exact SymPy rational arithmetic:

1. null-cone radial series from conserved momenta;
2. the direction-dependent edge location;
3. the total parent volume through O(L^4) relative to flat;
4. the edge area density;
5. the raw Synge-world-function cross-normalization chi;
6. the local area * chi^(-3) edge integral;
7. the universal thin-null vacuum focusing term;
8. the resulting purely electric recovery coefficient a4.

No Schwarzschild optical geometry and no floating-point fitting are used.
"""

from __future__ import annotations

import sympy as sp


L, Y, u, w, mu = sp.symbols(
    "L Y u w mu",
    real=True,
)
C1, C2, C3, C4 = sp.symbols("C1 C2 C3 C4")
D1, D2, D3, D4 = sp.symbols("D1 D2 D3 D4")


def truncate(expr: sp.Expr, order: int = 5) -> sp.Expr:
    return sp.series(expr, L, 0, order).removeO().expand()


def null_integrands(c: sp.Expr) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return dt-affine, x and transverse coordinate integrands."""
    t = 1 + L * u
    energy2 = (
        c * t ** sp.Rational(2, 3)
        + (1 - c) * t ** sp.Rational(-4, 3)
    )
    inv_e = energy2 ** sp.Rational(-1, 2)
    f0 = truncate(inv_e)
    fx = truncate(t ** sp.Rational(2, 3) * inv_e)
    fp = truncate(t ** sp.Rational(-4, 3) * inv_e)
    return f0, fx, fp


def solve_direction_series(
    lower: sp.Expr,
    upper: sp.Expr,
    symbols: tuple[sp.Symbol, ...],
) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    """Solve the conserved-momentum direction parameter c(L).

    The target coordinate-space ray has squared axial direction cosine w.
    Overall momentum scale is fixed to one, so c=P_x^2 and 1-c=P_perp^2.
    """
    c = (
        w
        + symbols[0] * L
        + symbols[1] * L**2
        + symbols[2] * L**3
        + symbols[3] * L**4
    )
    f0, fx, fp = null_integrands(c)

    j0 = sp.integrate(f0, (u, lower, upper))
    jx = sp.integrate(fx, (u, lower, upper))
    jp = sp.integrate(fp, (u, lower, upper))

    # Direction equation with square roots eliminated.
    eq = truncate(
        c * (1 - w) * jx**2
        - w * (1 - c) * jp**2
    )

    solution: dict[sp.Symbol, sp.Expr] = {}
    for degree, symbol in enumerate(symbols, start=1):
        coefficient = sp.expand(eq.subs(solution)).coeff(L, degree)
        value = sp.solve(
            sp.Eq(coefficient, 0),
            symbol,
            dict=False,
        )[0]
        solution[symbol] = sp.factor(value)

    csol = truncate(c.subs(solution))
    j0sol = truncate(j0.subs(solution))
    jxsol = truncate(jx.subs(solution))
    return csol, j0sol, jxsol, sp.expand(eq.subs(solution))


def cone_radius_series(
    csol: sp.Expr,
    jxsol: sp.Expr,
    flat_duration: sp.Expr,
) -> sp.Expr:
    """Return rho/[L*flat_duration] for one null cone."""
    ratio = (
        sp.sqrt(csol / w)
        * jxsol
        / flat_duration
    )
    return truncate(ratio)


def average_mu(expr_w: sp.Expr) -> sp.Expr:
    return sp.simplify(
        sp.integrate(
            sp.expand(expr_w.subs(w, mu**2)),
            (mu, -1, 1),
        )
        / 2
    )


def main() -> None:
    # Past cone: t from 1-L to 1+LY.
    cm, j0m, jxm, _ = solve_direction_series(
        -1,
        Y,
        (C1, C2, C3, C4),
    )
    rm = cone_radius_series(
        cm,
        jxm,
        Y + 1,
    )

    # Future cone: integrate backward in time using positive interval Y -> 1.
    cp, j0p, jxp, _ = solve_direction_series(
        Y,
        1,
        (D1, D2, D3, D4),
    )
    rp = cone_radius_series(
        cp,
        jxp,
        1 - Y,
    )

    # Solve where the two coordinate-ray radii cross.
    y1, y2, y3, y4 = sp.symbols("y1 y2 y3 y4")
    yedge_trial = (
        y1 * L
        + y2 * L**2
        + y3 * L**3
        + y4 * L**4
    )

    radius_minus = (1 + Y) * rm
    radius_plus = (1 - Y) * rp
    crossing = truncate(
        (radius_minus - radius_plus).subs(
            Y,
            yedge_trial,
        ),
        6,
    )

    edge_solution: dict[sp.Symbol, sp.Expr] = {}
    for degree, symbol in enumerate(
        (y1, y2, y3, y4),
        start=1,
    ):
        coefficient = sp.expand(
            crossing.subs(edge_solution)
        ).coeff(L, degree)
        edge_solution[symbol] = sp.factor(
            sp.solve(
                sp.Eq(coefficient, 0),
                symbol,
                dict=False,
            )[0]
        )

    yedge = sp.expand(
        yedge_trial.subs(edge_solution)
    )

    assert edge_solution[y1] == w / 2 - sp.Rational(1, 3)
    assert edge_solution[y2] == 0
    assert edge_solution[y4] == 0

    expected_y3 = (
        216 * w**3
        - 477 * w**2
        + 324 * w
        - 56
    ) / 648
    assert sp.simplify(edge_solution[y3] - expected_y3) == 0

    # ------------------------------------------------------------------
    # Parent volume
    # ------------------------------------------------------------------
    # sqrt(det spatial metric) = t for this Kasner metric.
    past_integrand = truncate(
        (1 + L * Y)
        * (1 + Y) ** 3
        * rm**3
    )
    future_integrand = truncate(
        (1 + L * Y)
        * (1 - Y) ** 3
        * rp**3
    )

    directional_parent = sp.Integer(0)

    for degree in range(5):
        pk = sp.expand(past_integrand).coeff(L, degree)
        fk = sp.expand(future_integrand).coeff(L, degree)

        panti = sp.integrate(pk, Y)
        fanti = sp.integrate(fk, Y)

        boundary = (
            panti.subs(Y, yedge)
            - panti.subs(Y, -1)
            + fanti.subs(Y, 1)
            - fanti.subs(Y, yedge)
        )

        directional_parent += (
            L**degree
            * sp.series(
                boundary,
                L,
                0,
                5 - degree,
            ).removeO()
        )

    directional_parent = truncate(directional_parent)

    parent_ratio = sp.Integer(0)
    for degree in range(5):
        parent_ratio += (
            average_mu(
                sp.expand(directional_parent).coeff(
                    L,
                    degree,
                )
            )
            * L**degree
        )
    parent_ratio = sp.expand(parent_ratio)

    assert parent_ratio.coeff(L, 2) == 0
    assert parent_ratio.coeff(L, 3) == 0
    assert (
        parent_ratio.coeff(L, 4)
        ==
        sp.Rational(68, 8505)
    )

    # Kasner electric Weyl norm at t=1.
    e2 = sp.Rational(8, 27)

    parent_e2_coefficient = sp.simplify(
        parent_ratio.coeff(L, 4) / e2
    )
    assert (
        parent_e2_coefficient
        ==
        sp.Rational(17, 630)
    )

    # ------------------------------------------------------------------
    # Edge embedding and area density
    # ------------------------------------------------------------------
    edge_radius_over_l = truncate(
        radius_minus.subs(Y, yedge)
    )
    edge_time = truncate(1 + L * yedge)

    re_mu = edge_radius_over_l.subs(w, mu**2)
    te_mu = edge_time.subs(w, mu**2)
    rho = L * re_mu

    xcoord = rho * mu
    ycoord = rho * sp.sqrt(1 - mu**2)

    dt_dmu = sp.diff(te_mu, mu)
    dx_dmu = sp.diff(xcoord, mu)
    dy_dmu = sp.diff(ycoord, mu)

    q_mumu = (
        -dt_dmu**2
        + te_mu ** sp.Rational(-2, 3) * dx_dmu**2
        + te_mu ** sp.Rational(4, 3) * dy_dmu**2
    )
    q_phiphi = (
        te_mu ** sp.Rational(4, 3)
        * rho**2
        * (1 - mu**2)
    )

    area_density = truncate(
        sp.sqrt(
            truncate(q_mumu * q_phiphi / L**4, 6)
        ),
        6,
    )

    area2 = sp.factor(area_density.coeff(L, 2))
    area4 = sp.factor(area_density.coeff(L, 4))

    expected_area2 = (
        45 * mu**4
        - 48 * mu**2
        + 7
    ) / 27

    expected_area4 = (
        5103 * mu**8
        - 12663 * mu**6
        + 10467 * mu**4
        - 3117 * mu**2
        + 194
    ) / 1458

    assert sp.simplify(area2 - expected_area2) == 0
    assert sp.simplify(area4 - expected_area4) == 0
    assert sp.integrate(area2, (mu, -1, 1)) / 2 == 0

    area_e2_coefficient = sp.simplify(
        (
            sp.integrate(
                area4,
                (mu, -1, 1),
            )
            / 2
        )
        / e2
    )
    assert area_e2_coefficient == sp.Rational(2, 135)

    # ------------------------------------------------------------------
    # Raw world-function cross-normalization chi
    # ------------------------------------------------------------------
    cm_edge = truncate(cm.subs(Y, yedge))
    cp_edge = truncate(cp.subs(Y, yedge))

    lambda_minus = truncate(
        L * j0m.subs(Y, yedge),
        6,
    )
    lambda_plus = truncate(
        L * j0p.subs(Y, yedge),
        6,
    )

    tedge = edge_time

    em = truncate(
        sp.sqrt(
            cm_edge * tedge ** sp.Rational(2, 3)
            + (1 - cm_edge)
            * tedge ** sp.Rational(-4, 3)
        )
    )
    ep = truncate(
        sp.sqrt(
            cp_edge * tedge ** sp.Rational(2, 3)
            + (1 - cp_edge)
            * tedge ** sp.Rational(-4, 3)
        )
    )

    spatial_cross = truncate(
        tedge ** sp.Rational(2, 3)
        * sp.sqrt(cm_edge * cp_edge)
        + tedge ** sp.Rational(-4, 3)
        * sp.sqrt(
            (1 - cm_edge)
            * (1 - cp_edge)
        )
    )

    # d(2 sigma)=2 lambda p at a null endpoint.
    chi_ratio = truncate(
        (
            4
            * lambda_minus
            * lambda_plus
            * (em * ep + spatial_cross)
        )
        / (8 * L**2)
    )

    # For 0 <= w <= 1 simplify branch absolute values generated by sqrt.
    qlog = truncate(sp.log(chi_ratio))
    qlog = qlog.xreplace(
        {
            sp.Abs(w): w,
            sp.Abs(w - 1): 1 - w,
        }
    )
    qlog = sp.expand(qlog)

    q2 = sp.factor(qlog.coeff(L, 2))
    q4 = sp.factor(qlog.coeff(L, 4))

    expected_q2 = 2 * (3 * w - 1) / 27
    expected_q4 = (
        540 * w**3
        - 1467 * w**2
        + 1164 * w
        - 137
    ) / 3645

    assert sp.simplify(q2 - expected_q2) == 0
    assert sp.simplify(q4 - expected_q4) == 0

    # ------------------------------------------------------------------
    # Local intrinsic edge factor dA * chi^(-3)
    # ------------------------------------------------------------------
    q_mu = qlog.subs(w, mu**2)
    edge_cross_density = truncate(
        area_density * sp.exp(-3 * q_mu)
    )

    edge_cross_l2 = sp.simplify(
        sp.integrate(
            edge_cross_density.coeff(L, 2),
            (mu, -1, 1),
        )
        / 2
    )
    edge_cross_l4 = sp.simplify(
        sp.integrate(
            edge_cross_density.coeff(L, 4),
            (mu, -1, 1),
        )
        / 2
    )

    assert edge_cross_l2 == 0
    assert edge_cross_l4 == sp.Rational(296, 18225)

    edge_cross_e2_coefficient = sp.simplify(
        edge_cross_l4 / e2
    )
    assert (
        edge_cross_e2_coefficient
        ==
        sp.Rational(37, 675)
    )

    # ------------------------------------------------------------------
    # Thin-null focusing
    # ------------------------------------------------------------------
    # At t=1:
    #   E = diag(-4/9, 2/9, 2/9), B=0.
    #
    # The screen optical tidal norm for a null direction with mu=n_x is
    #
    #   H_AB H^AB = (8/9) (1-mu^2)^2.
    #
    # The universal d=4 thin-null coefficient is
    #
    #   F = 1 + L^4 H^2_screen / 504 + ...
    #
    # for each sheet.  Since the recovery integrand contains
    # F_-^(-3/2) F_+^(-3/2), the two-sheet local correction is
    # -H^2_screen L^4 / 168.
    screen_h2 = (
        sp.Rational(8, 9)
        * (1 - mu**2) ** 2
    )

    mean_screen_h2 = sp.simplify(
        sp.integrate(
            screen_h2,
            (mu, -1, 1),
        )
        / 2
    )

    assert mean_screen_h2 == sp.Rational(64, 135)
    assert sp.simplify(mean_screen_h2 / e2) == sp.Rational(8, 5)

    thin_e2_coefficient = sp.simplify(
        (-mean_screen_h2 / 168) / e2
    )
    assert thin_e2_coefficient == -sp.Rational(1, 105)

    # ------------------------------------------------------------------
    # Full purely electric recovery coefficient
    # ------------------------------------------------------------------
    a4 = sp.simplify(
        parent_e2_coefficient
        + edge_cross_e2_coefficient
        + thin_e2_coefficient
    )

    assert a4 == sp.Rational(683, 9450)

    # Independent symmetric-plane-wave calibration:
    plane_wave_sum = sp.Rational(508, 4725)
    b4 = sp.simplify(plane_wave_sum - a4)

    assert b4 == sp.Rational(37, 1050)

    print(
        {
            "parent_volume_E2": str(parent_e2_coefficient),
            "edge_area_E2": str(area_e2_coefficient),
            "edge_cross_E2": str(edge_cross_e2_coefficient),
            "thin_null_E2": str(thin_e2_coefficient),
            "a4_Kasner_world_function": str(a4),
            "b4_from_independent_plane_wave_sum": str(b4),
        }
    )

    print(
        "PASS: independent LRS-Kasner/world-function route gives "
        "a4 = 683/9450 and closes the d=4 vacuum coefficient pair."
    )


if __name__ == "__main__":
    main()
