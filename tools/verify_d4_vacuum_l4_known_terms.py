#!/usr/bin/env python3
"""Exact bookkeeping for the known d=4 Ricci-flat L^4 recovery terms.

Known pieces:
1. Alexandrov edge area from Wang (2019);
2. Alexandrov total spacetime volume from Wang (2019);
3. the two thin-null endpoint coefficients from the plane-wave Jacobi lemma.

The remaining unknown contribution is the gauge-invariant double-null
cross-normalization factor Omega.

All arithmetic is exact with fractions.
"""

from __future__ import annotations

from fractions import Fraction


def main() -> None:
    edge_e = Fraction(2, 135)
    edge_b = Fraction(0, 1)

    volume_e = Fraction(127, 4725)
    volume_b = Fraction(1, 105)

    # K contains V_D^{-2}.
    parent_e = -2 * volume_e
    parent_b = -2 * volume_b

    # Two thin-null coefficients together, multiplied by -3/2.
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
            "thin_null_E2": str(thin_e),
            "thin_null_B2": str(thin_b),
            "known_total_E2": str(known_e),
            "known_total_B2": str(known_b),
            "known_total_E2_float": float(known_e),
            "known_total_B2_float": float(known_b),
        }
    )

    assert known_e == -Fraction(229, 4725)
    assert known_b == -Fraction(1, 35)

    # Wang's d=4 identities:
    # D^2 = 4 E^2, H^2 = 2 B^2.
    #
    # ACD volume:
    # relative E coefficient = 127/4725
    # relative B coefficient = 1/105.
    #
    # ACD edge area:
    # relative E coefficient = 2/135
    # relative B coefficient = 0.
    print("PASS: exact d=4 known L^4 bookkeeping verified.")


if __name__ == "__main__":
    main()
