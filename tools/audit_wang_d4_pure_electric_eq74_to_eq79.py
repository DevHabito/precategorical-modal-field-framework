#!/usr/bin/env python3
"""Audit Wang (2019) Eq. (74)+(76) against Eq. (79) in d=4, B=0.

This checker uses only the published pure-electric specialization of the
abridged null-cone boundary (Eq. 74), the tensorial RNC volume-density
correction (Eq. 76), and standard S^2 STF moments.

It does NOT use:
- the exact Kasner volume,
- the symmetric plane-wave volume,
- the repository's candidate corrected coefficient.

Result:
    Eq. (74) + Eq. (76)  ->  v_E = 17/630
while the d=4 specialization of published Eq. (79) gives
    v_E = 127/4725.

The exact difference is 1/9450.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    t, r = sp.symbols("t r", real=True, nonnegative=True)
    E2 = sp.symbols("E2", positive=True)

    # For a symmetric trace-free E_ij on S^2:
    #
    # <E_nn^2> = 2 E^2 / 15,
    # <(E^2)_nn> = E^2 / 3.
    enn_sq_avg = sp.Rational(2, 15) * E2
    e2nn_avg = sp.Rational(1, 3) * E2

    # Eq. (74), d=4, B=0, L=1:
    #
    # r_+(t,n) = (1-t) [1 + a1 + a2],
    #
    # a1 = E_nn/6,
    #
    # a2 = E_nn^2/24
    #      - t (E^2)_nn/45
    #      + (1-t)^2 [(E^2)_nn - E_nn^2]/90.
    #
    # Expanding r_+^3 through quadratic curvature produces
    # a2 + a1^2 in the normalized boundary correction.
    a1_sq_avg = enn_sq_avg / 36

    a2_avg = (
        enn_sq_avg / 24
        - t * e2nn_avg / 45
        + (1 - t) ** 2
        * (e2nn_avg - enn_sq_avg)
        / 90
    )

    local_boundary_avg = sp.simplify(
        (a2_avg + a1_sq_avg) / E2
    )

    assert local_boundary_avg == (
        6 * t**2 - 32 * t + 31
    ) / 2700

    # The doubled upper-cone integral, divided by
    # V0 = 2*pi/3 for L=1, gives the factor 12.
    cone_coefficient = sp.simplify(
        12
        * sp.integrate(
            (1 - t) ** 3
            * local_boundary_avg,
            (t, 0, 1),
        )
    )

    assert cone_coefficient == sp.Rational(1, 36)

    # Eq. (76), specialized to a four-dimensional pure-electric Weyl field,
    # has angular average
    #
    # <Q>/E^2 = (3 r^4 + 5 t^4)/5
    #
    # in
    #
    # sqrt(|g|) = 1 - Q/180 + ...
    q_avg_per_e2 = (
        3 * r**4 + 5 * t**4
    ) / 5

    density_integral = sp.integrate(
        sp.integrate(
            r**2 * q_avg_per_e2,
            (r, 0, 1 - t),
        ),
        (t, 0, 1),
    )

    assert density_integral == sp.Rational(1, 84)

    # Again normalize the doubled upper half by V0:
    # 12 * (-1/180) = -1/15.
    density_coefficient = sp.simplify(
        -sp.Rational(1, 15)
        * density_integral
    )

    assert density_coefficient == -sp.Rational(1, 1260)

    from_74_76 = sp.simplify(
        cone_coefficient
        + density_coefficient
    )

    assert from_74_76 == sp.Rational(17, 630)

    # d=4 specialization of Wang Eq. (79), using H=0 and D^2=4E^2.
    published_79 = sp.Rational(127, 4725)

    difference = sp.simplify(
        from_74_76 - published_79
    )

    assert difference == sp.Rational(1, 9450)

    print(
        {
            "Eq74_cone_E2": str(cone_coefficient),
            "Eq76_density_E2": str(density_coefficient),
            "Eq74_plus_Eq76_E2": str(from_74_76),
            "Eq79_published_E2": str(published_79),
            "difference": str(difference),
        }
    )

    print(
        "PASS: in d=4 pure electric vacuum, the published Eq. (74)+(76) "
        "integrate to 17/630, not the 127/4725 stated in Eq. (79)."
    )


if __name__ == "__main__":
    main()
