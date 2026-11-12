#!/usr/bin/env python3
"""Full d=4 audit of Wang (2019) Eqs. (74), (76) and (79).

The published Eq. (74) gives the abridged ACD null-cone boundary.
The published Eq. (76) gives the quadratic-vacuum RNC volume density.
This checker integrates those two equations directly in four dimensions.

No exact-spacetime calibration is used as input.

Result
------
Pure electric:
    cone       =  1/36   E^2 L^4
    density    = -1/1260 E^2 L^4
    total      = 17/630  E^2 L^4

Pure magnetic:
    cone       =  1/225  B^2 L^4
    density    =  1/3150 B^2 L^4
    total      =  1/210  B^2 L^4

Therefore Eqs. (74)+(76) imply

    V/V0 = 1 + L^4[(17/630)E^2 + (1/210)B^2] + ...

whereas the d=4 specialization of the printed Eq. (79) is

    V/V0 = 1 + L^4[(127/4725)E^2 + (1/105)B^2] + ...

The discrepancies are exactly

    Delta v_E = +1/9450,
    Delta v_B = -1/210.

Conventions follow Wang:
    E_ij = C_0i0j,
    H_ijk = C_0ijk,
    B_ij = (1/2) epsilon_jkl H_i^{kl},
    H^2 = 2 B^2 in d=4,
    D^2 = 4 E^2 in d=4.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    t, r = sp.symbols("t r", nonnegative=True, real=True)

    # ---------------------------------------------------------------
    # Pure-electric boundary contribution from Eq. (74)
    # ---------------------------------------------------------------
    #
    # S^2 STF moments:
    #   <E_nn^2>      = 2 E^2 / 15
    #   <(E^2)_nn>    = E^2 / 3
    #
    # For r_+=(1-t)(1+a1+a2):
    #   a1 = E_nn/6
    #   a2 = E_nn^2/24
    #        - t (E^2)_nn/45
    #        + (1-t)^2[(E^2)_nn-E_nn^2]/90.
    e_local = (
        sp.Rational(2, 15) / 24
        + sp.Rational(2, 15) / 36
        - t * sp.Rational(1, 3) / 45
        + (1 - t) ** 2
        * (
            sp.Rational(1, 3)
            - sp.Rational(2, 15)
        )
        / 90
    )

    e_cone = sp.simplify(
        12
        * sp.integrate(
            (1 - t) ** 3 * e_local,
            (t, 0, 1),
        )
    )

    assert e_cone == sp.Rational(1, 36)

    # ---------------------------------------------------------------
    # Pure-electric density contribution from Eq. (76)
    # ---------------------------------------------------------------
    #
    # Angular average of the tensorial quartic contraction:
    #
    #   <Q_E>/E^2 = (3 r^4 + 5 t^4)/5,
    #
    # with sqrt|g| = 1 - Q/180.
    q_e = (
        3 * r**4 + 5 * t**4
    ) / 5

    e_density = sp.simplify(
        -sp.Rational(1, 15)
        * sp.integrate(
            sp.integrate(
                r**2 * q_e,
                (r, 0, 1 - t),
            ),
            (t, 0, 1),
        )
    )

    assert e_density == -sp.Rational(1, 1260)

    v_e = sp.simplify(
        e_cone + e_density
    )

    assert v_e == sp.Rational(17, 630)

    # ---------------------------------------------------------------
    # Pure-magnetic boundary contribution from Eq. (74)
    # ---------------------------------------------------------------
    #
    # The PDF notation is H_i{}^m{}_j H_lmk.
    #
    # In d=4,
    #   H_ijk = epsilon_jkq B_iq,
    # and the S^2 average gives
    #
    #   < n^i n^j n^l n^k
    #     H_i{}^m{}_j H_lmk >
    #       = B^2 / 5.
    #
    # Hence
    #   <a2_B> = (1-t)^2 B^2 / 450.
    b_local = (1 - t) ** 2 / 450

    b_cone = sp.simplify(
        12
        * sp.integrate(
            (1 - t) ** 3 * b_local,
            (t, 0, 1),
        )
    )

    assert b_cone == sp.Rational(1, 225)

    # ---------------------------------------------------------------
    # Pure-magnetic density contribution from Eq. (76)
    # ---------------------------------------------------------------
    #
    # Angular average:
    #
    #   <Q_B>/B^2
    #     = (2/5) r^2 (5 t^2 - r^2).
    q_b = (
        sp.Rational(2, 5)
        * r**2
        * (5 * t**2 - r**2)
    )

    b_density = sp.simplify(
        -sp.Rational(1, 15)
        * sp.integrate(
            sp.integrate(
                r**2 * q_b,
                (r, 0, 1 - t),
            ),
            (t, 0, 1),
        )
    )

    assert b_density == sp.Rational(1, 3150)

    v_b = sp.simplify(
        b_cone + b_density
    )

    assert v_b == sp.Rational(1, 210)

    # ---------------------------------------------------------------
    # Compare to the printed Eq. (79)
    # ---------------------------------------------------------------
    eq79_e = sp.Rational(127, 4725)
    eq79_b = sp.Rational(1, 105)

    delta_e = sp.simplify(v_e - eq79_e)
    delta_b = sp.simplify(v_b - eq79_b)

    assert delta_e == sp.Rational(1, 9450)
    assert delta_b == -sp.Rational(1, 210)

    print(
        {
            "Eq74_cone_E2": str(e_cone),
            "Eq76_density_E2": str(e_density),
            "Eq74_plus_Eq76_vE": str(v_e),
            "Eq79_vE": str(eq79_e),
            "Delta_vE": str(delta_e),
            "Eq74_cone_B2": str(b_cone),
            "Eq76_density_B2": str(b_density),
            "Eq74_plus_Eq76_vB": str(v_b),
            "Eq79_vB": str(eq79_b),
            "Delta_vB": str(delta_b),
        }
    )

    print(
        "PASS: direct d=4 integration of Wang Eqs. (74)+(76) gives "
        "v_E=17/630 and v_B=1/210, not the coefficients printed in Eq. (79)."
    )


if __name__ == "__main__":
    main()
