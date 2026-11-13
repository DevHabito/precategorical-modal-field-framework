#!/usr/bin/env python3
"""Verify C^1 matching of the three-ball lens volume at regime switches.

For two three-balls with radii R>=r and center separation d, the partial-lens
volume is

    V = pi (R+r-d)^2
        [d^2 + 2d(R+r) - 3(R-r)^2]
        / (12d).

There are two switching surfaces:

1. non-overlap:
       d = R+r;

2. containment:
       d = R-r.

This checker proves that the physical piecewise volume is C^1 at both
surfaces: the mismatch starts quadratically in the signed gap.

This fact is useful for perturbative boosted-diamond calculations because a
small displacement of the switching surface contributes only at cubic order
in the displacement.
"""

from __future__ import annotations

import sympy as sp


def lens_volume(
    R: sp.Expr,
    r: sp.Expr,
    d: sp.Expr,
) -> sp.Expr:
    return (
        sp.pi
        * (R + r - d) ** 2
        * (
            d**2
            + 2 * d * (R + r)
            - 3 * (R - r) ** 2
        )
        / (12 * d)
    )


def main() -> None:
    R, r, g, h = sp.symbols(
        "R r g h",
        positive=True,
    )

    # Non-overlap boundary:
    #
    # d = R+r-g, g -> 0+.
    nonoverlap = sp.series(
        lens_volume(
            R,
            r,
            R + r - g,
        ),
        g,
        0,
        4,
    ).removeO().expand()

    nonoverlap_quadratic = sp.simplify(
        nonoverlap.coeff(g, 2)
    )

    assert sp.simplify(
        nonoverlap_quadratic
        - sp.pi * R * r / (R + r)
    ) == 0

    assert sp.simplify(
        nonoverlap.subs(g, 0)
    ) == 0

    assert sp.simplify(
        sp.diff(
            nonoverlap,
            g,
        ).subs(
            g,
            0,
        )
    ) == 0

    # Containment boundary:
    #
    # d = R-r+h, h -> 0+.
    small_ball = (
        4
        * sp.pi
        * r**3
        / 3
    )

    containment_difference = sp.series(
        lens_volume(
            R,
            r,
            R - r + h,
        )
        - small_ball,
        h,
        0,
        4,
    ).removeO().expand()

    containment_quadratic = sp.simplify(
        containment_difference.coeff(
            h,
            2,
        )
    )

    assert sp.simplify(
        containment_quadratic
        + sp.pi * R * r / (R - r)
    ) == 0

    assert sp.simplify(
        containment_difference.subs(
            h,
            0,
        )
    ) == 0

    assert sp.simplify(
        sp.diff(
            containment_difference,
            h,
        ).subs(
            h,
            0,
        )
    ) == 0

    print(
        {
            "nonoverlap_leading_mismatch":
                "pi*R*r/(R+r) * g^2",
            "containment_leading_mismatch":
                "-pi*R*r/(R-r) * h^2",
        }
    )

    print(
        "PASS: three-ball intersection volume is C^1 across both "
        "non-overlap/lens and lens/containment switching surfaces."
    )


if __name__ == "__main__":
    main()
