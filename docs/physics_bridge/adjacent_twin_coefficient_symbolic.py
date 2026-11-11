#!/usr/bin/env python3
"""Symbolic checks for the adjacent-twin coefficient derivation.

This script verifies only exact algebra/integration steps.  It does not prove
the global small-D domination lemma needed for the asymptotic theorem.
"""

from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    s, z = sp.symbols(
        "s z",
        real=True,
    )

    x = s * (1 + z) / 2
    y = s * (1 - z) / 2

    h_original = (
        x**4
        + y**4
        + x * y * (
            4 - x**2 - y**2
        )
    )

    h_factored = (
        s**2
        / 4
        * (
            s**2 * z**4
            + 3 * s**2 * z**2
            - 4 * z**2
            + 4
        )
    )

    h_check = sp.expand(
        h_original - h_factored
    ) == 0

    a = z**2 * (z**2 + 3)
    b = 4 * (1 - z**2)

    # The d=3 transformed s-integrand is
    #   b / (a*s^2+b)^(3/2).
    # Its antiderivative is s/sqrt(a*s^2+b).
    primitive = (
        s
        / sp.sqrt(
            a * s**2 + b
        )
    )

    derivative_check = sp.simplify(
        sp.diff(
            primitive,
            s,
        )
        - b
        / (
            a * s**2 + b
        ) ** sp.Rational(3, 2)
    )

    # For -1 < z < 1, evaluating the primitive at s=2 gives
    # 1/(1+z^2).  The algebraic square identity below is the only
    # branch-sensitive step.
    endpoint_square_check = sp.expand(
        (
            z**4
            + 3 * z**2
            + 1
            - z**2
        )
        - (1 + z**2) ** 2
    ) == 0

    z_integral = sp.integrate(
        1 / (1 + z**2),
        (z, -1, 1),
    )

    u = sp.symbols(
        "u",
        positive=True,
    )

    gaussian_half_integral = (
        sp.integrate(
            sp.exp(-u**2),
            (u, 0, sp.oo),
        )
    )

    i1 = sp.simplify(
        gaussian_half_integral / 2
    )

    c3 = sp.simplify(
        sp.Rational(64, 3)
        * z_integral
    )

    c4 = sp.simplify(
        144 * i1**2
    )

    expected = {
        "d3_z_integral": sp.pi / 2,
        "d3_coefficient": 32 * sp.pi / 3,
        "d4_I1": sp.sqrt(sp.pi) / 4,
        "d4_coefficient": 9 * sp.pi,
    }

    checks = {
        "d3_H_factorization": h_check,
        "d3_s_antiderivative": (
            derivative_check == 0
        ),
        "d3_endpoint_square": (
            endpoint_square_check
        ),
        "d3_z_integral": (
            sp.simplify(
                z_integral
                - expected[
                    "d3_z_integral"
                ]
            )
            == 0
        ),
        "d3_coefficient": (
            sp.simplify(
                c3
                - expected[
                    "d3_coefficient"
                ]
            )
            == 0
        ),
        "d4_half_gaussian": (
            sp.simplify(
                i1
                - expected[
                    "d4_I1"
                ]
            )
            == 0
        ),
        "d4_coefficient": (
            sp.simplify(
                c4
                - expected[
                    "d4_coefficient"
                ]
            )
            == 0
        ),
    }

    result = {
        "audit": (
            "ADJACENT_TWIN_"
            "COEFFICIENT_SYMBOLIC_V1"
        ),
        "status": (
            "PASS"
            if all(checks.values())
            else "FAIL"
        ),
        "checks": checks,
        "values": {
            "d3_z_integral": str(
                z_integral
            ),
            "d3_coefficient": str(c3),
            "d4_I1": str(i1),
            "d4_coefficient": str(c4),
        },
        "nonclaim": (
            "These checks verify exact algebra "
            "and one-dimensional integrals only; "
            "they do not prove the global "
            "small-D asymptotic."
        ),
    }

    print(
        json.dumps(
            result,
            indent=2,
            sort_keys=True,
        )
    )

    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
