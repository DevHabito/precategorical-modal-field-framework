#!/usr/bin/env python3
"""Diagnostic decomposition of the boosted d=5 L^4 jet integral by lens regime.

This script imports the coefficient-level jet machinery from

    check_d5_boosted_kasner_l4_jet_quadrature.py

and reports the positive-time contribution of each moving regime separately.

It is diagnostic only:
- no exact value is imposed for regimes I or II;
- nsimplify output, when shown, is a conjectural recognition aid;
- the exactly known regime-III result is used as a control.

The purpose is to identify tractable closed forms for the two remaining
partial-lens integrals.
"""

from __future__ import annotations

import math
import sympy as sp

from check_d5_boosted_kasner_l4_jet_quadrature import (
    ORDER,
    TIME_SWITCH_1,
    TIME_SWITCH_2,
    TIP_HALF_TIME,
    const,
    leggauss,
    mul,
    scale,
    slice_u,
    spatial_section,
)


def integrate_regime(
    lower,
    upper,
    regime: int,
    *,
    time_order: int,
    spatial_order: int,
):
    nodes, weights = leggauss(
        time_order
    )

    width = (
        upper
        - lower
    )

    total = [0.0] * ORDER

    import numpy as np

    total = np.zeros(
        ORDER
    )

    for node, weight in zip(
        nodes,
        weights,
    ):
        z = (
            node
            + 1.0
        ) / 2.0

        T = (
            lower
            + scale(
                width,
                z,
            )
        )

        section = spatial_section(
            T,
            regime,
            spatial_order=spatial_order,
        )

        density = (
            const(1.0)
            + slice_u(
                T
            )
        )

        integrand = mul(
            mul(
                density,
                section,
            ),
            width,
        )

        total += (
            0.5
            * weight
            * integrand
        )

    return total


def recognize(
    value: float,
):
    normalized = (
        sp.Float(
            value,
            18,
        )
        / sp.pi**2
    )

    return sp.nsimplify(
        normalized,
        [
            sp.sqrt(3),
        ],
        tolerance=sp.Float(
            "1e-10"
        ),
        full=True,
    )


def main() -> None:
    time_order = 26
    spatial_order = 28

    regimes = [
        (
            "I_lens_to_empty",
            const(0.0),
            TIME_SWITCH_1,
            1,
        ),
        (
            "II_lens_to_containment",
            TIME_SWITCH_1,
            TIME_SWITCH_2,
            2,
        ),
        (
            "III_full_containment",
            TIME_SWITCH_2,
            TIP_HALF_TIME,
            3,
        ),
    ]

    results = {}

    for (
        name,
        lower,
        upper,
        regime,
    ) in regimes:
        value = integrate_regime(
            lower,
            upper,
            regime,
            time_order=time_order,
            spatial_order=spatial_order,
        )

        results[name] = value

        print(
            {
                "regime": name,
                "coefficients": [
                    float(x)
                    for x in value
                ],
                "L4_over_pi2": float(
                    value[4]
                    / math.pi**2
                ),
                "L4_recognition_candidate":
                    str(
                        recognize(
                            float(
                                value[4]
                            )
                        )
                    ),
            }
        )

    total = sum(
        results.values()
    )

    print(
        {
            "total_coefficients": [
                float(x)
                for x in total
            ],
            "total_relative_L2":
                float(
                    total[2]
                    / total[0]
                ),
            "total_relative_L4":
                float(
                    total[4]
                    / total[0]
                ),
            "target_relative_L4":
                7.0 / 144.0,
        }
    )

    # Exact control for regime III, already proved symbolically.
    exact_regime3_l4 = (
        sp.Rational(
            9199,
            8957952,
        )
        * sp.sqrt(3)
        * sp.pi**2
    )

    regime3_error = (
        results[
            "III_full_containment"
        ][4]
        - float(
            sp.N(
                exact_regime3_l4,
                18,
            )
        )
    )

    print(
        {
            "regime3_exact_L4":
                str(
                    exact_regime3_l4
                ),
            "regime3_L4_error":
                float(
                    regime3_error
                ),
        }
    )

    assert abs(
        regime3_error
    ) < 2.0e-8

    assert abs(
        total[2]
        / total[0]
    ) < 2.0e-6

    assert abs(
        total[4]
        / total[0]
        - 7.0 / 144.0
    ) < 2.0e-6

    print(
        "PASS: regime decomposition reproduces the exact contained-tail "
        "control and the full coefficient-level boosted result."
    )


if __name__ == "__main__":
    main()
