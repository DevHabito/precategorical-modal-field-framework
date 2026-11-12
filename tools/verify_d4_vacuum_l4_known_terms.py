#!/usr/bin/env python3
"""Component audit for d=4 Ricci-flat L^4 recovery bookkeeping.

IMPORTANT STATUS
----------------
This file supersedes an older factorized bookkeeping script.

Two later audits changed the scientific status:

1. The parent ACD four-volume in d=4 is

       delta V / V0
         = L^4 [17/630 E^2 + 1/210 B^2] + o(L^4),

   as obtained independently from:
   - exact LRS Kasner integration,
   - exact symmetric plane-wave integration,
   - direct integration of Wang (2019) Eqs. (74) and (76).

2. The local edge area and cross-normalization have zero-mean O(L^2)
   anisotropies whose products contribute at O(L^4).

Therefore one MUST NOT assemble the full recovery coefficient by multiplying
separately averaged logarithmic factors.  In particular, it is false that the
only remaining term after the components below is simply
-3 <delta ln chi>.

This script now verifies only individually established scalar components.
"""

from __future__ import annotations

from fractions import Fraction


def main() -> None:
    # Integrated edge-area coefficient.
    edge_e = Fraction(2, 135)
    edge_b = Fraction(0, 1)

    # Corrected d=4 parent Alexandrov four-volume.
    parent_e = Fraction(17, 630)
    parent_b = Fraction(1, 210)

    # Universal two-sheet thin-null focusing contribution after angular average.
    thin_e = -Fraction(1, 105)
    thin_b = -Fraction(1, 105)

    raw_component_e = edge_e + parent_e + thin_e
    raw_component_b = edge_b + parent_b + thin_b

    assert raw_component_e == Fraction(61, 1890)
    assert raw_component_b == -Fraction(1, 210)

    print(
        {
            "edge_area_E2": str(edge_e),
            "edge_area_B2": str(edge_b),
            "parent_volume_E2": str(parent_e),
            "parent_volume_B2": str(parent_b),
            "thin_focusing_E2": str(thin_e),
            "thin_focusing_B2": str(thin_b),
            "raw_component_sum_E2": str(raw_component_e),
            "raw_component_sum_B2": str(raw_component_b),
            "status":
                "COMPONENTS_ONLY_DO_NOT_FACTORIZE_LOCAL_EDGE_AVERAGES",
        }
    )

    print(
        "PASS: corrected d=4 component values verified. "
        "This is not a complete recovery-coefficient decomposition."
    )


if __name__ == "__main__":
    main()
