#!/usr/bin/env python3
"""Infer the d=4 vacuum ACD volume coefficient pair from two exact geometries.

Assumption
----------
For a centered Ricci-flat 3+1 Alexandrov interval, the parity-even L^4 scalar
basis is

    delta V / V0 = L^4 (v_E E^2 + v_B B^2) + o(L^4).

Exact calibrations
------------------
1. LRS Kasner:
       B^2 = 0,
       delta V / V0 = (17/630) E^2 L^4.
   Hence v_E = 17/630.

2. Symmetric Cahen-Wallach plane wave:
       E^2 = B^2 = omega^4/2,
       delta V / V0 = (1/63) omega^4 L^4.
   Hence (v_E + v_B)/2 = 1/63.

This script solves the two equations exactly and compares them to the d=4
specialization of Wang (2019), Eq. (79).
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    v_e = sp.Rational(17, 630)

    # Type-N plane wave:
    # (v_E + v_B) * omega^4/2 = omega^4/63.
    v_sum = sp.Rational(2, 63)
    v_b = sp.simplify(v_sum - v_e)

    assert v_b == sp.Rational(1, 210)

    wang_e = sp.Rational(127, 4725)
    wang_b = sp.Rational(1, 105)

    delta_e = sp.simplify(v_e - wang_e)
    delta_b = sp.simplify(v_b - wang_b)

    assert delta_e == sp.Rational(1, 9450)
    assert delta_b == -sp.Rational(1, 210)

    print(
        {
            "candidate_vE": str(v_e),
            "candidate_vB": str(v_b),
            "wang_vE": str(wang_e),
            "wang_vB": str(wang_b),
            "delta_vE": str(delta_e),
            "delta_vB": str(delta_b),
        }
    )

    print(
        "PASS: two exact geometries imply "
        "v_E = 17/630 and v_B = 1/210 "
        "under the d=4 vacuum {E^2,B^2} basis assumption."
    )


if __name__ == "__main__":
    main()
