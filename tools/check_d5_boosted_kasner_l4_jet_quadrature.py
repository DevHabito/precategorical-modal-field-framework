#!/usr/bin/env python3
"""Perturbative L^4 quadrature for the v=1/2 boosted d=5 Kasner ACD.

This is not a finite-L extrapolation.

The code propagates truncated Taylor jets in the diamond half-size L through:

1. exact proper-time-centered tip jets;
2. exact null-geodesic first-integral density jets;
3. the moving past/future cone matching condition;
4. the moving lens/empty or lens/containment switch;
5. the exact moving time-regime boundaries T1(L), T2(L);
6. the exact three-ball lens formula;
7. Gaussian quadrature of the coefficient functions themselves.

For the five-dimensional LRS-Kasner metric

    ds^2 = -dt^2 + t^(-1) dx^2 + t dy_perp^2

with midpoint transverse speed v=1/2, the corrected vacuum ACD law predicts

    c4 = 7/144.

The Ricci-flat L^2 coefficient must vanish.

The script checks both statements numerically at the coefficient level.
No finite-L volume is evaluated.
"""

from __future__ import annotations

import math
import numpy as np
from numpy.polynomial.legendre import leggauss


ORDER = 6


def const(value: float) -> np.ndarray:
    out = np.zeros(ORDER)
    out[0] = value
    return out


def scale(a: np.ndarray, value: float) -> np.ndarray:
    return a * value


def mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.zeros(ORDER)

    for i in range(ORDER):
        for j in range(ORDER - i):
            out[i + j] += a[i] * b[j]

    return out


def inv(a: np.ndarray) -> np.ndarray:
    out = np.zeros(ORDER)
    out[0] = 1.0 / a[0]

    for n in range(1, ORDER):
        out[n] = -sum(
            a[k] * out[n - k]
            for k in range(1, n + 1)
        ) / a[0]

    return out


def div(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return mul(
        a,
        inv(b),
    )


def sqrt_jet(a: np.ndarray) -> np.ndarray:
    if a[0] <= 0.0:
        raise ValueError(
            "sqrt jet requires a positive scalar term"
        )

    out = np.zeros(ORDER)
    out[0] = math.sqrt(a[0])

    for n in range(1, ORDER):
        quadratic = sum(
            out[k] * out[n - k]
            for k in range(1, n)
        )

        out[n] = (
            a[n]
            - quadratic
        ) / (
            2.0 * out[0]
        )

    return out


def power(a: np.ndarray, exponent: int) -> np.ndarray:
    out = const(1.0)

    for _ in range(exponent):
        out = mul(
            out,
            a,
        )

    return out


def divide_by_L(a: np.ndarray) -> np.ndarray:
    out = np.zeros(ORDER)
    out[: ORDER - 1] = a[1:]
    return out


def polynomial(
    coefficients: list[float],
    argument: np.ndarray,
) -> np.ndarray:
    out = np.zeros(ORDER)
    current = const(1.0)

    for coefficient in coefficients:
        out += scale(
            current,
            coefficient,
        )

        current = mul(
            current,
            argument,
        )

    return out


def derivative_coefficients(
    coefficients: list[float],
) -> list[float]:
    return [
        degree * coefficients[degree]
        for degree
        in range(
            1,
            len(coefficients),
        )
    ]


AXIAL_DENSITY = [
    [1.0],
    [1.5, -1.0],
    [3.0 / 8.0, -2.0, 1.5],
    [
        -1.0 / 16.0,
        -9.0 / 8.0,
        15.0 / 4.0,
        -5.0 / 2.0,
    ],
    [
        3.0 / 128.0,
        -1.0 / 8.0,
        51.0 / 16.0,
        -15.0 / 2.0,
        35.0 / 8.0,
    ],
]


TRANSVERSE_DENSITY = [
    [1.0],
    [-0.5, -1.0],
    [3.0 / 8.0, 0.0, 1.5],
    [
        -5.0 / 16.0,
        -1.0 / 8.0,
        3.0 / 4.0,
        -5.0 / 2.0,
    ],
    [
        35.0 / 128.0,
        1.0 / 8.0,
        3.0 / 16.0,
        -5.0 / 2.0,
        35.0 / 8.0,
    ],
]


SQRT3 = math.sqrt(3.0)

GAMMA = 2.0 / SQRT3
MOMENTUM = 1.0 / SQRT3

TIP_MINUS = np.asarray(
    [
        0.0,
        -2.0 * SQRT3 / 3.0,
        -1.0 / 12.0,
        -SQRT3 / 27.0,
        -25.0 / 432.0,
        -107.0 * SQRT3 / 3240.0,
    ]
)

TIP_PLUS = np.asarray(
    [
        0.0,
        2.0 * SQRT3 / 3.0,
        -1.0 / 12.0,
        SQRT3 / 27.0,
        -25.0 / 432.0,
        107.0 * SQRT3 / 3240.0,
    ]
)

TIP_MID = (
    TIP_PLUS
    + TIP_MINUS
) / 2.0

TRANSVERSE_SEPARATION = np.asarray(
    [
        2.0 / SQRT3,
        0.0,
        17.0 * SQRT3 / 54.0,
        0.0,
        251.0 * SQRT3 / 810.0,
        0.0,
    ]
)

TIP_HALF_TIME = np.asarray(
    [
        2.0 * SQRT3 / 3.0,
        0.0,
        SQRT3 / 27.0,
        0.0,
        107.0 * SQRT3 / 3240.0,
        0.0,
    ]
)

# Exact moving time-regime boundaries derived independently in
#
# tools/derive_d5_boosted_kasner_lens_time_switch_jets.py.
TIME_SWITCH_1 = np.asarray(
    [
        SQRT3 / 6.0,
        1.0 / 16.0,
        61.0 * SQRT3 / 432.0,
        -367.0 / 2304.0,
        25949.0 * SQRT3 / 207360.0,
        0.0,
    ]
)

TIME_SWITCH_2 = np.asarray(
    [
        SQRT3 / 3.0,
        -1.0 / 4.0,
        19.0 * SQRT3 / 216.0,
        -7.0 / 72.0,
        3937.0 * SQRT3 / 51840.0,
        0.0,
    ]
)

L_JET = np.asarray(
    [
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ]
)


def slice_u(
    T: np.ndarray,
) -> np.ndarray:
    return (
        TIP_MID
        + mul(
            L_JET,
            T,
        )
    )


def scaled_integral(
    c: np.ndarray,
    lower: np.ndarray,
    upper: np.ndarray,
    *,
    transverse: bool,
) -> np.ndarray:
    density = (
        TRANSVERSE_DENSITY
        if transverse
        else AXIAL_DENSITY
    )

    total = np.zeros(ORDER)

    for degree, coefficients in enumerate(
        density
    ):
        coefficient = polynomial(
            coefficients,
            c,
        )

        difference = (
            power(
                upper,
                degree + 1,
            )
            -
            power(
                lower,
                degree + 1,
            )
        )

        total += scale(
            mul(
                coefficient,
                difference,
            ),
            1.0 / (degree + 1),
        )

    return divide_by_L(
        total
    )


def scaled_axial_derivative(
    c: np.ndarray,
    lower: np.ndarray,
    upper: np.ndarray,
) -> np.ndarray:
    total = np.zeros(ORDER)

    for degree, coefficients in enumerate(
        AXIAL_DENSITY
    ):
        derivative = derivative_coefficients(
            coefficients
        )

        if derivative:
            coefficient = polynomial(
                derivative,
                c,
            )
        else:
            coefficient = np.zeros(
                ORDER
            )

        difference = (
            power(
                upper,
                degree + 1,
            )
            -
            power(
                lower,
                degree + 1,
            )
        )

        total += scale(
            mul(
                coefficient,
                difference,
            ),
            1.0 / (degree + 1),
        )

    return divide_by_L(
        total
    )


def cone_profile(
    c: np.ndarray,
    lower: np.ndarray,
    upper: np.ndarray,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    axial = scaled_integral(
        c,
        lower,
        upper,
        transverse=False,
    )

    transverse = scaled_integral(
        c,
        lower,
        upper,
        transverse=True,
    )

    x = mul(
        sqrt_jet(c),
        axial,
    )

    radius = mul(
        sqrt_jet(
            const(1.0)
            - c
        ),
        transverse,
    )

    return (
        x,
        radius,
        axial,
    )


def solve_past_parameter(
    x_target: np.ndarray,
    T: np.ndarray,
    scalar_guess: float,
) -> np.ndarray:
    coefficients = np.zeros(
        ORDER
    )

    coefficients[0] = scalar_guess

    upper = slice_u(
        T
    )

    for order in range(
        1,
        5,
    ):
        base = coefficients.copy()
        base[order] = 0.0

        residual_base = (
            cone_profile(
                base,
                TIP_MINUS,
                upper,
            )[0]
            - x_target
        )

        trial = base.copy()
        trial[order] = 1.0

        residual_trial = (
            cone_profile(
                trial,
                TIP_MINUS,
                upper,
            )[0]
            - x_target
        )

        slope = (
            residual_trial[order]
            - residual_base[order]
        )

        coefficients[order] = (
            -residual_base[order]
            / slope
        )

    return coefficients


def geometry_at_future_parameter(
    T: np.ndarray,
    s: np.ndarray,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    c = power(
        s,
        2,
    )

    lower = slice_u(
        T
    )

    x_future, radius_future, axial = (
        cone_profile(
            c,
            lower,
            TIP_PLUS,
        )
    )

    axial_c = scaled_axial_derivative(
        c,
        lower,
        TIP_PLUS,
    )

    dx_ds = (
        axial
        + scale(
            mul(
                power(
                    s,
                    2,
                ),
                axial_c,
            ),
            2.0,
        )
    )

    scalar_past_parameter = (
        x_future[0]
        / (
            GAMMA
            + T[0]
        )
    ) ** 2

    past_parameter = solve_past_parameter(
        x_future,
        T,
        scalar_past_parameter,
    )

    radius_past = cone_profile(
        past_parameter,
        TIP_MINUS,
        lower,
    )[1]

    return (
        radius_past,
        radius_future,
        dx_ds,
    )


def lens_volume(
    radius_past: np.ndarray,
    radius_future: np.ndarray,
) -> np.ndarray:
    separation = TRANSVERSE_SEPARATION

    gap = (
        radius_past
        + radius_future
        - separation
    )

    bracket = (
        power(
            separation,
            2,
        )
        + scale(
            mul(
                separation,
                radius_past
                + radius_future,
            ),
            2.0,
        )
        - scale(
            power(
                radius_past
                - radius_future,
                2,
            ),
            3.0,
        )
    )

    return scale(
        div(
            mul(
                power(
                    gap,
                    2,
                ),
                bracket,
            ),
            separation,
        ),
        math.pi / 12.0,
    )


def contained_volume(
    radius_future: np.ndarray,
) -> np.ndarray:
    return scale(
        power(
            radius_future,
            3,
        ),
        4.0 * math.pi / 3.0,
    )


def solve_switch_parameter(
    T: np.ndarray,
    *,
    containment: bool,
) -> np.ndarray:
    T0 = T[0]

    scalar = math.sqrt(
        max(
            0.0,
            (
                1.0
                - 3.0 * T0 * T0
            )
            / (
                GAMMA
                - T0
            ) ** 2,
        )
    )

    coefficients = np.zeros(
        ORDER
    )

    coefficients[0] = scalar

    for order in range(
        1,
        5,
    ):
        base = coefficients.copy()
        base[order] = 0.0

        radius_past, radius_future, _ = (
            geometry_at_future_parameter(
                T,
                base,
            )
        )

        residual_base = (
            radius_past
            - radius_future
            - TRANSVERSE_SEPARATION
            if containment
            else
            radius_past
            + radius_future
            - TRANSVERSE_SEPARATION
        )

        trial = base.copy()
        trial[order] = 1.0

        (
            trial_past,
            trial_future,
            _,
        ) = geometry_at_future_parameter(
            T,
            trial,
        )

        residual_trial = (
            trial_past
            - trial_future
            - TRANSVERSE_SEPARATION
            if containment
            else
            trial_past
            + trial_future
            - TRANSVERSE_SEPARATION
        )

        slope = (
            residual_trial[order]
            - residual_base[order]
        )

        coefficients[order] = (
            -residual_base[order]
            / slope
        )

    return coefficients


def gaussian_jet_integral(
    function,
    order: int,
) -> np.ndarray:
    nodes, weights = leggauss(
        order
    )

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

        total += (
            0.5
            * weight
            * function(
                z
            )
        )

    return total


def spatial_section(
    T: np.ndarray,
    regime: int,
    *,
    spatial_order: int,
) -> np.ndarray:
    if regime == 1:
        switch = solve_switch_parameter(
            T,
            containment=False,
        )

        def lens_integrand(
            z: float,
        ) -> np.ndarray:
            s = scale(
                switch,
                z,
            )

            (
                radius_past,
                radius_future,
                dx_ds,
            ) = geometry_at_future_parameter(
                T,
                s,
            )

            return mul(
                lens_volume(
                    radius_past,
                    radius_future,
                ),
                mul(
                    dx_ds,
                    switch,
                ),
            )

        section = gaussian_jet_integral(
            lens_integrand,
            spatial_order,
        )

    elif regime == 2:
        switch = solve_switch_parameter(
            T,
            containment=True,
        )

        remainder = (
            const(1.0)
            - switch
        )

        def lens_integrand(
            z: float,
        ) -> np.ndarray:
            s = scale(
                switch,
                z,
            )

            (
                radius_past,
                radius_future,
                dx_ds,
            ) = geometry_at_future_parameter(
                T,
                s,
            )

            return mul(
                lens_volume(
                    radius_past,
                    radius_future,
                ),
                mul(
                    dx_ds,
                    switch,
                ),
            )

        def containment_integrand(
            z: float,
        ) -> np.ndarray:
            s = (
                switch
                + scale(
                    remainder,
                    z,
                )
            )

            (
                _,
                radius_future,
                dx_ds,
            ) = geometry_at_future_parameter(
                T,
                s,
            )

            return mul(
                contained_volume(
                    radius_future
                ),
                mul(
                    dx_ds,
                    remainder,
                ),
            )

        section = (
            gaussian_jet_integral(
                lens_integrand,
                spatial_order,
            )
            +
            gaussian_jet_integral(
                containment_integrand,
                spatial_order,
            )
        )

    elif regime == 3:

        def containment_integrand(
            z: float,
        ) -> np.ndarray:
            s = const(
                z
            )

            (
                _,
                radius_future,
                dx_ds,
            ) = geometry_at_future_parameter(
                T,
                s,
            )

            return mul(
                contained_volume(
                    radius_future,
                ),
                dx_ds,
            )

        section = gaussian_jet_integral(
            containment_integrand,
            spatial_order,
        )

    else:
        raise ValueError(
            "invalid regime"
        )

    # x -> -x symmetry.
    return scale(
        section,
        2.0,
    )


def positive_half_integral(
    *,
    time_order: int,
    spatial_order: int,
) -> np.ndarray:
    intervals = (
        (
            const(0.0),
            TIME_SWITCH_1,
            1,
        ),
        (
            TIME_SWITCH_1,
            TIME_SWITCH_2,
            2,
        ),
        (
            TIME_SWITCH_2,
            TIP_HALF_TIME,
            3,
        ),
    )

    nodes, weights = leggauss(
        time_order
    )

    total = np.zeros(
        ORDER
    )

    for lower, upper, regime in intervals:
        width = (
            upper
            - lower
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

            physical_density = (
                const(1.0)
                + slice_u(
                    T
                )
            )

            integrand = mul(
                mul(
                    physical_density,
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


def main() -> None:
    # These orders are high enough to put the coefficient-level quadrature
    # well below the declared 1e-5 tolerance while keeping CI runtime modest.
    time_order = 14
    spatial_order = 16

    positive = positive_half_integral(
        time_order=time_order,
        spatial_order=spatial_order,
    )

    # The negative half is obtained by L -> -L under tip exchange.
    # Therefore the full even coefficients are twice the positive-half ones,
    # and the factor of two cancels in the relative ratios below.
    relative_L2 = (
        positive[2]
        / positive[0]
    )

    relative_L4 = (
        positive[4]
        / positive[0]
    )

    target_L4 = (
        7.0 / 144.0
    )

    flat_half = (
        math.pi**2 / 10.0
    )

    print(
        {
            "time_order": time_order,
            "spatial_order": spatial_order,
            "flat_half_measured":
                positive[0],
            "flat_half_exact":
                flat_half,
            "relative_L2":
                relative_L2,
            "relative_L4":
                relative_L4,
            "target_L4":
                target_L4,
            "L4_difference":
                relative_L4
                - target_L4,
        }
    )

    assert abs(
        positive[0]
        - flat_half
    ) < 1.0e-6

    assert abs(
        relative_L2
    ) < 2.0e-6

    assert abs(
        relative_L4
        - target_L4
    ) < 1.0e-5

    print(
        "PASS: direct perturbative jet quadrature gives vanishing L^2 "
        "vacuum response and c4=7/144 for the v=1/2 boosted d5 Kasner "
        "diamond within the declared coefficient-level tolerance."
    )


if __name__ == "__main__":
    main()
