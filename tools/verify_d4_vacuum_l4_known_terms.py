#!/usr/bin/env python3
"""Corrected exact bookkeeping for the known d=4 Ricci-flat L^4 terms.

Use the invariant physical-coefficient form

    K_4 ∝ V_D * A_E * chi^{-3} * F_+^{-3/2} * F_-^{-3/2},

where:
- V_D is the parent Alexandrov spacetime volume,
- A_E is the codimension-two edge area,
- chi = -g^{-1}(dS_+,dS_-) is the null-sheet cross normalization,
- F_± are dimensionless thin-null focusing factors.

Known pieces before chi:
1. edge area: +2/135 E^2
2. parent volume: +127/4725 E^2 + 1/105 B^2
3. thin focusing: -1/105 (E^2+B^2)

Thus

    known E^2 = 152/4725,
    known B^2 = 0.

The previous script incorrectly used the raw V_D^{-2} pair-density factor
without restoring the V_D^3 contained in normalized c_±^{-3/2}.
"""

from __future__ import annotations

from fractions import Fraction


def main() -> None:
    edge_e = Fraction(2, 135)
    edge_b = Fraction(0, 1)

    parent_e = Fraction(127, 4725)
    parent_b = Fraction(1, 105)

    thin_e = -Fraction(1, 105)
    thin_b = -Fraction(1, 105)

    known_e = edge_e + parent_e + thin_e
    known_b = edge_b + parent_b + thin_b

    print(
        {
            "edge_area_E2": str(edge_e),
            "edge_area_B2": str(edge_b),
            "parent_volume_E2": str(parent_e),
            "parent_volume_B2": str(parent_b),
            "thin_focusing_E2": str(thin_e),
            "thin_focusing_B2": str(thin_b),
            "known_total_E2": str(known_e),
            "known_total_B2": str(known_b),
            "known_total_E2_float": float(known_e),
            "known_total_B2_float": float(known_b),
        }
    )

    assert known_e == Fraction(152, 4725)
    assert known_b == 0

    print(
        "PASS: corrected d=4 known L^4 bookkeeping verified; "
        "remaining term is -3 <delta ln chi>."
    )


if __name__ == "__main__":
    main()
