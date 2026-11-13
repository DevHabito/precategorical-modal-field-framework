#!/usr/bin/env python3
"""Exact-geometry discriminator between corrected and printed ACD laws.

The purpose is not to re-integrate Wang's intermediate equations.

Instead, compare two competing coefficient laws against independent Ricci-flat
geometries whose small-diamond parent volumes are known from separate
calculations:

1. symmetric Cahen--Wallach plane waves in arbitrary d;
2. LRS Kasner in d=4,5,6.

The corrected law agrees with every exact geometry below.
The printed Eq. (79) differs by a nonzero rational amount.

This makes the discrepancy physically testable and separates the geometry
checks from the algebraic re-integration of the paper.
"""

from __future__ import annotations

import sympy as sp


def corrected_coefficients(
    d: sp.Expr,
) -> tuple[
    sp.Expr,
    sp.Expr,
    sp.Expr,
]:
    A = (
        d
        * (
            7 * d**2
            + 44 * d
            + 58
        )
        / (
            180
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    B = (
        d
        * (d + 6)
        / (
            60
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    C = -(
        d
        / (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    return (
        sp.factor(A),
        sp.factor(B),
        sp.factor(C),
    )


def printed_coefficients(
    d: sp.Expr,
) -> tuple[
    sp.Expr,
    sp.Expr,
    sp.Expr,
]:
    A = (
        d
        * (
            7 * d**3
            + 58 * d**2
            + 146 * d
            + 108
        )
        / (
            180
            * (d + 1)
            * (d + 2)
            * (d + 3)
            * (d + 4)
        )
    )

    B = (
        d
        * (d + 6)
        / (
            30
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    C = -(
        d
        / (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    return (
        sp.factor(A),
        sp.factor(B),
        sp.factor(C),
    )


def lrs_kasner_invariants(
    d: sp.Expr,
) -> tuple[
    sp.Expr,
    sp.Expr,
    sp.Expr,
]:
    E2 = (
        4
        * (d - 3) ** 2
        * (d - 2)
        / (d - 1) ** 3
    )

    H2 = sp.Integer(0)

    D2 = (
        16
        * (d - 3)
        * (d - 2)
        / (d - 1) ** 3
    )

    return (
        sp.factor(E2),
        H2,
        sp.factor(D2),
    )


def main() -> None:
    d = sp.symbols(
        "d",
        integer=True,
        positive=True,
    )

    (
        A_corr,
        B_corr,
        C_corr,
    ) = corrected_coefficients(d)

    (
        A_print,
        B_print,
        C_print,
    ) = printed_coefficients(d)

    # ------------------------------------------------------------
    # Exact Cahen--Wallach plane wave.
    # ------------------------------------------------------------

    plane_wave_exact = (
        d
        * (7 * d + 22)
        / (
            720
            * (d + 1)
            * (d + 3)
        )
    )

    plane_wave_corr = sp.factor(
        A_corr / 4
        + B_corr / 2
        + C_corr
    )

    plane_wave_print = sp.factor(
        A_print / 4
        + B_print / 2
        + C_print
    )

    assert sp.simplify(
        plane_wave_corr
        - plane_wave_exact
    ) == 0

    plane_wave_print_minus_exact = (
        sp.factor(
            plane_wave_print
            - plane_wave_exact
        )
    )

    expected_plane_wave_error = (
        d
        * (
            3 * d**2
            + 24 * d
            + 32
        )
        / (
            360
            * (d + 1)
            * (d + 2)
            * (d + 3)
            * (d + 4)
        )
    )

    assert sp.simplify(
        plane_wave_print_minus_exact
        - expected_plane_wave_error
    ) == 0

    # ------------------------------------------------------------
    # LRS Kasner.
    # ------------------------------------------------------------

    (
        E2,
        H2,
        D2,
    ) = lrs_kasner_invariants(d)

    kasner_corr = sp.factor(
        A_corr * E2
        + B_corr * H2
        + C_corr * D2
    )

    kasner_print = sp.factor(
        A_print * E2
        + B_print * H2
        + C_print * D2
    )

    kasner_corr_minus_print = (
        sp.factor(
            kasner_corr
            - kasner_print
        )
    )

    expected_kasner_gap = (
        8
        * d
        * (d - 3) ** 2
        * (d - 2)
        / (
            45
            * (d - 1) ** 3
            * (d + 1)
            * (d + 2)
            * (d + 3)
            * (d + 4)
        )
    )

    assert sp.simplify(
        kasner_corr_minus_print
        - expected_kasner_gap
    ) == 0

    exact_kasner = {
        4: sp.Rational(
            68,
            8505,
        ),
        5: sp.Rational(
            25,
            1152,
        ),
        6: sp.Rational(
            2288,
            65625,
        ),
    }

    rows = []

    for dimension, exact in (
        exact_kasner.items()
    ):
        corrected = sp.factor(
            kasner_corr.subs(
                d,
                dimension,
            )
        )

        printed = sp.factor(
            kasner_print.subs(
                d,
                dimension,
            )
        )

        assert corrected == exact
        assert printed != exact

        rows.append(
            {
                "d": dimension,
                "exact": str(exact),
                "corrected": str(corrected),
                "printed": str(printed),
                "exact_minus_printed": str(
                    sp.factor(
                        exact
                        - printed
                    )
                ),
            }
        )

    assert rows[0][
        "exact_minus_printed"
    ] == "4/127575"

    assert rows[1][
        "exact_minus_printed"
    ] == "1/18144"

    assert rows[2][
        "exact_minus_printed"
    ] == "4/65625"

    print(
        {
            "plane_wave_exact_combination":
                str(
                    sp.factor(
                        plane_wave_exact
                    )
                ),
            "plane_wave_printed_minus_exact":
                str(
                    plane_wave_print_minus_exact
                ),
            "kasner_corrected_minus_printed_general":
                str(
                    kasner_corr_minus_print
                ),
            "kasner_exact_rows":
                rows,
        }
    )

    print(
        "PASS: independent exact Cahen-Wallach and LRS-Kasner geometries "
        "select the corrected ACD law and reject the printed Eq. (79) "
        "along the tested invariant directions."
    )


if __name__ == "__main__":
    main()
