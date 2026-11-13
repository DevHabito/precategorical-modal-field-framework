#!/usr/bin/env python3
"""Localize the +108 -> +116 electric discrepancy in Wang (2019) Eq. (79).

Starting point
--------------
Direct integration of the printed intermediate Eqs. (74), (76)--(78) gives
five independent electric-sector contributions to the relative ACD volume.

Put all five over

    D = 180 (d+1)(d+2)(d+3)(d+4).

Their numerator polynomials are

    P1 = 5(d+1)(d+2)(d+3)(d+4)
    P2 = -4(d+2)(d+3)(d+4)
    P3 = 2d(d-1)(d+3)(d+4)
    P4 = -24
    P5 = -3d(d+2).

They sum to

    d(d+2)(7d^2+44d+58)
      = d(7d^3+58d^2+146d+116).

The printed Eq. (79) would require instead

    d(7d^3+58d^2+146d+108),

i.e. a change of exactly

    -8d

at this common-numerator stage.

This script proves two things:

1. the exact five-term sum gives +116;
2. no dimension-independent multiplicative change in any subset of one,
   two, three, or four of the five isolated contributions can generate
   exactly -8d for every d.

Therefore the electric discrepancy does not have the same signature as the
hook-sector factor-of-two discrepancy.  The calculation does NOT prove the
historical source of the printed +108; it only rules out a broad class of
simple one/few-term multiplicative explanations.
"""

from __future__ import annotations

from itertools import combinations
import sympy as sp


def constant_rescaling_solution(
    polynomials: list[sp.Expr],
    target: sp.Expr,
    d: sp.Symbol,
) -> list[dict[sp.Symbol, sp.Expr]]:
    variables = sp.symbols(
        f"a0:{len(polynomials)}"
    )

    expression = (
        sum(
            variable * polynomial
            for variable, polynomial
            in zip(
                variables,
                polynomials,
            )
        )
        - target
    )

    equations = sp.Poly(
        sp.expand(expression),
        d,
    ).all_coeffs()

    return sp.solve(
        equations,
        variables,
        dict=True,
    )


def main() -> None:
    d = sp.symbols(
        "d",
        integer=True,
        positive=True,
    )

    terms = {
        "cone_Enn2_and_square":
            5
            * (d + 1)
            * (d + 2)
            * (d + 3)
            * (d + 4),

        "cone_E2nn_time":
            -4
            * (d + 2)
            * (d + 3)
            * (d + 4),

        "cone_final_electric":
            2
            * d
            * (d - 1)
            * (d + 3)
            * (d + 4),

        "density_t4":
            -24,

        "density_r4_electric":
            -3
            * d
            * (d + 2),
    }

    corrected_common = sp.factor(
        sum(
            terms.values()
        )
    )

    expected_corrected = (
        d
        * (d + 2)
        * (
            7 * d**2
            + 44 * d
            + 58
        )
    )

    assert sp.simplify(
        corrected_common
        - expected_corrected
    ) == 0

    corrected_final = sp.expand(
        corrected_common / d
    )

    assert sp.simplify(
        corrected_final
        - (
            7 * d**3
            + 58 * d**2
            + 146 * d
            + 116
        )
    ) == 0

    printed_final = (
        7 * d**3
        + 58 * d**2
        + 146 * d
        + 108
    )

    required_common_shift = sp.expand(
        d
        * (
            printed_final
            - corrected_final
        )
    )

    assert required_common_shift == -8 * d

    names = list(
        terms.keys()
    )

    polynomials = [
        terms[name]
        for name in names
    ]

    # Ask whether constant multiplicative errors in a strict subset of the
    # five isolated terms can generate exactly -8d for every dimension.
    subset_results: list[
        tuple[
            tuple[str, ...],
            list[
                dict[
                    sp.Symbol,
                    sp.Expr,
                ]
            ],
        ]
    ] = []

    for subset_size in range(
        1,
        len(polynomials),
    ):
        for indices in combinations(
            range(
                len(polynomials)
            ),
            subset_size,
        ):
            subset = [
                polynomials[index]
                for index in indices
            ]

            solutions = (
                constant_rescaling_solution(
                    subset,
                    -8 * d,
                    d,
                )
            )

            subset_names = tuple(
                names[index]
                for index in indices
            )

            subset_results.append(
                (
                    subset_names,
                    solutions,
                )
            )

            assert not solutions, (
                "unexpected strict-subset constant-rescaling explanation: "
                f"{subset_names} -> {solutions}"
            )

    # For reference, all five polynomials together do span -8d, but only by
    # coordinated changes across every contribution.  This is not interpreted
    # as a physical explanation; it is merely a linear-algebra control.
    all_five_solution = (
        constant_rescaling_solution(
            polynomials,
            -8 * d,
            d,
        )
    )

    assert all_five_solution

    print(
        {
            "common_numerator_terms": {
                name:
                    str(
                        sp.expand(
                            polynomial
                        )
                    )
                for name, polynomial
                in terms.items()
            },
            "corrected_common_numerator":
                str(
                    sp.expand(
                        corrected_common
                    )
                ),
            "corrected_final_electric_numerator":
                str(
                    corrected_final
                ),
            "printed_final_electric_numerator":
                str(
                    printed_final
                ),
            "required_common_shift":
                str(
                    required_common_shift
                ),
            "strict_subsets_with_constant_rescaling_solution":
                0,
            "all_five_control_solution":
                [
                    {
                        str(key): str(value)
                        for key, value
                        in solution.items()
                    }
                    for solution
                    in all_five_solution
                ],
        }
    )

    print(
        "PASS: +116 follows exactly from the five printed intermediate "
        "electric contributions, and the printed +108 cannot be generated "
        "by a dimension-independent multiplicative error in any strict "
        "subset of those five contributions."
    )


if __name__ == "__main__":
    main()
