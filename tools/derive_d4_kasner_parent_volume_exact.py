#!/usr/bin/env python3
"""Exact d=4 LRS-Kasner parent-volume series with explicit truncated algebra.

This replaces the fragile global SymPy-series assembly used by the older
full Kasner checker.

Metric:
    ds^2 = -dt^2 + t^(-2/3) dx^2 + t^(4/3)(dy^2+dz^2)

Centered tips:
    p=(1-L,0,0,0), q=(1+L,0,0,0).

The calculation keeps an explicit coefficient list in L through L^4.
No expression containing a formal L-series is substituted into another
expression and then re-expanded globally.

The normalized directional time integral is derived as

    <I_dir>
      = 1/2 + (34/8505) L^4 + O(L^6),

so the physical volume ratio is

    V/V_flat
      = 2 <I_dir>
      = 1 + (68/8505) L^4 + O(L^6).

At the midpoint E^2=8/27, hence

    (68/8505)/(8/27) = 17/630.

The script also verifies the direction-dependent edge series.
"""

from __future__ import annotations

import sympy as sp


ORDER = 4

Y, u, w, mu = sp.symbols(
    "Y u w mu",
    real=True,
)


def const(value):
    return [sp.sympify(value)] + [
        sp.Integer(0)
        for _ in range(ORDER)
    ]


def add(a, b):
    return [
        sp.expand(a[i] + b[i])
        for i in range(ORDER + 1)
    ]


def sub(a, b):
    return [
        sp.expand(a[i] - b[i])
        for i in range(ORDER + 1)
    ]


def scale(a, factor):
    return [
        sp.expand(factor * value)
        for value in a
    ]


def mul(a, b):
    return [
        sp.expand(
            sum(
                a[j] * b[i - j]
                for j in range(i + 1)
            )
        )
        for i in range(ORDER + 1)
    ]


def int_power(a, exponent: int):
    out = const(1)

    for _ in range(exponent):
        out = mul(out, a)

    return out


def shift(a, amount: int):
    return (
        [sp.Integer(0)] * amount
        + a[: ORDER + 1 - amount]
    )


def binomial_one_plus(delta, exponent):
    """Return (1+delta)^exponent for delta[0]=0."""
    assert sp.simplify(delta[0]) == 0

    out = const(1)
    term = const(1)

    for degree in range(1, ORDER + 1):
        term = mul(term, delta)

        out = add(
            out,
            scale(
                term,
                sp.binomial(
                    exponent,
                    degree,
                ),
            ),
        )

    return out


def t_power(exponent):
    """Series of (1+L*u)^exponent."""
    return [
        sp.binomial(exponent, degree)
        * u**degree
        for degree in range(ORDER + 1)
    ]


def integrate_u(series, lower, upper):
    return [
        sp.integrate(
            coefficient,
            (u, lower, upper),
        )
        for coefficient in series
    ]


def solve_direction_series(lower, upper, prefix):
    """Solve c(L)=P_x^2 coefficient-by-coefficient."""
    unknowns = sp.symbols(
        " ".join(
            f"{prefix}{degree}"
            for degree in range(1, ORDER + 1)
        )
    )

    c = [w, *unknowns]

    plus = t_power(
        sp.Rational(2, 3)
    )
    minus = t_power(
        sp.Rational(-4, 3)
    )

    energy2 = add(
        mul(c, plus),
        mul(
            sub(
                const(1),
                c,
            ),
            minus,
        ),
    )

    delta = list(energy2)
    delta[0] = sp.simplify(
        delta[0] - 1
    )

    inv_energy = binomial_one_plus(
        delta,
        sp.Rational(-1, 2),
    )

    jx = integrate_u(
        mul(
            plus,
            inv_energy,
        ),
        lower,
        upper,
    )

    jp = integrate_u(
        mul(
            minus,
            inv_energy,
        ),
        lower,
        upper,
    )

    direction_equation = sub(
        scale(
            mul(
                c,
                mul(jx, jx),
            ),
            1 - w,
        ),
        scale(
            mul(
                sub(
                    const(1),
                    c,
                ),
                mul(jp, jp),
            ),
            w,
        ),
    )

    solution = {}

    for degree, unknown in enumerate(
        unknowns,
        start=1,
    ):
        coefficient = sp.expand(
            direction_equation[degree].subs(
                solution
            )
        )

        value = sp.solve(
            sp.Eq(
                coefficient,
                0,
            ),
            unknown,
            dict=False,
        )[0]

        solution[unknown] = sp.factor(
            value
        )

    def substitute(series):
        return [
            sp.factor(
                coefficient.subs(
                    solution
                )
            )
            for coefficient in series
        ]

    return (
        substitute(c),
        substitute(jx),
    )


def sqrt_c_over_w(c):
    delta = [
        sp.Integer(0)
    ] + [
        sp.factor(
            c[degree] / w
        )
        for degree in range(
            1,
            ORDER + 1,
        )
    ]

    return binomial_one_plus(
        delta,
        sp.Rational(1, 2),
    )


def compose_in_Y(coefficients, y_series):
    """Compose sum L^k f_k(Y) with Y=y_series(L), y_series[0]=0."""
    assert sp.simplify(y_series[0]) == 0

    out = const(0)

    for l_degree, function in enumerate(
        coefficients
    ):
        power = const(1)

        for derivative_order in range(
            ORDER - l_degree + 1
        ):
            coefficient = (
                sp.diff(
                    function,
                    Y,
                    derivative_order,
                ).subs(
                    Y,
                    0,
                )
                /
                sp.factorial(
                    derivative_order
                )
            )

            out = add(
                out,
                shift(
                    scale(
                        power,
                        coefficient,
                    ),
                    l_degree,
                ),
            )

            power = mul(
                power,
                y_series,
            )

    return [
        sp.expand(value)
        for value in out
    ]


def average_over_sphere(function_of_w):
    return sp.simplify(
        sp.integrate(
            sp.expand(
                function_of_w.subs(
                    w,
                    mu**2,
                )
            ),
            (mu, -1, 1),
        )
        / 2
    )


def main() -> None:
    c_minus, jx_minus = solve_direction_series(
        -1,
        Y,
        "cm",
    )

    c_plus, jx_plus = solve_direction_series(
        Y,
        1,
        "cp",
    )

    r_minus = scale(
        mul(
            sqrt_c_over_w(
                c_minus
            ),
            jx_minus,
        ),
        1 / (1 + Y),
    )

    r_plus = scale(
        mul(
            sqrt_c_over_w(
                c_plus
            ),
            jx_plus,
        ),
        1 / (1 - Y),
    )

    radius_minus = [
        sp.expand(
            (1 + Y) * value
        )
        for value in r_minus
    ]

    radius_plus = [
        sp.expand(
            (1 - Y) * value
        )
        for value in r_plus
    ]

    radius_difference = sub(
        radius_minus,
        radius_plus,
    )

    y_unknowns = sp.symbols(
        "y1 y2 y3 y4"
    )

    y_series = [
        sp.Integer(0),
        *y_unknowns,
    ]

    crossing = compose_in_Y(
        radius_difference,
        y_series,
    )

    edge_solution = {}

    for degree, unknown in enumerate(
        y_unknowns,
        start=1,
    ):
        coefficient = sp.expand(
            crossing[degree].subs(
                edge_solution
            )
        )

        value = sp.solve(
            sp.Eq(
                coefficient,
                0,
            ),
            unknown,
            dict=False,
        )[0]

        edge_solution[unknown] = (
            sp.factor(value)
        )

    assert sp.simplify(
        edge_solution[y_unknowns[0]]
        -
        (
            w / 2
            -
            sp.Rational(1, 3)
        )
    ) == 0

    assert sp.simplify(
        edge_solution[y_unknowns[1]]
    ) == 0

    assert sp.simplify(
        edge_solution[y_unknowns[3]]
    ) == 0

    expected_y3 = (
        216 * w**3
        - 477 * w**2
        + 324 * w
        - 56
    ) / 648

    assert sp.simplify(
        edge_solution[y_unknowns[2]]
        - expected_y3
    ) == 0

    y_edge = [
        value.subs(
            edge_solution
        )
        for value in y_series
    ]

    # Physical volume:
    # sqrt(det g_spatial)=t=1+L*Y.
    past_integrand = mul(
        [
            sp.Integer(1),
            Y,
            sp.Integer(0),
            sp.Integer(0),
            sp.Integer(0),
        ],
        int_power(
            r_minus,
            3,
        ),
    )

    past_integrand = [
        sp.expand(
            (1 + Y) ** 3
            * coefficient
        )
        for coefficient
        in past_integrand
    ]

    future_integrand = mul(
        [
            sp.Integer(1),
            Y,
            sp.Integer(0),
            sp.Integer(0),
            sp.Integer(0),
        ],
        int_power(
            r_plus,
            3,
        ),
    )

    future_integrand = [
        sp.expand(
            (1 - Y) ** 3
            * coefficient
        )
        for coefficient
        in future_integrand
    ]

    past_antiderivative = [
        sp.integrate(
            coefficient,
            Y,
        )
        for coefficient
        in past_integrand
    ]

    future_antiderivative = [
        sp.integrate(
            coefficient,
            Y,
        )
        for coefficient
        in future_integrand
    ]

    past_at_edge = compose_in_Y(
        past_antiderivative,
        y_edge,
    )

    future_at_edge = compose_in_Y(
        future_antiderivative,
        y_edge,
    )

    directional_integral = []

    for degree in range(
        ORDER + 1
    ):
        directional_integral.append(
            sp.simplify(
                past_at_edge[degree]
                -
                past_antiderivative[
                    degree
                ].subs(
                    Y,
                    -1,
                )
                +
                future_antiderivative[
                    degree
                ].subs(
                    Y,
                    1,
                )
                -
                future_at_edge[degree]
            )
        )

    expected_directional_l2 = (
        7
        * (
            45 * w**2
            - 57 * w
            + 10
        )
        / 540
    )

    expected_directional_l4 = (
        56133 * w**4
        - 152334 * w**3
        + 138393 * w**2
        - 46632 * w
        + 3608
    ) / 54432

    assert (
        directional_integral[0]
        ==
        sp.Rational(1, 2)
    )

    assert directional_integral[1] == 0
    assert directional_integral[3] == 0

    assert sp.simplify(
        directional_integral[2]
        -
        expected_directional_l2
    ) == 0

    assert sp.simplify(
        directional_integral[4]
        -
        expected_directional_l4
    ) == 0

    angular_average = [
        average_over_sphere(
            coefficient
        )
        for coefficient
        in directional_integral
    ]

    assert angular_average[0] == sp.Rational(
        1,
        2,
    )

    assert angular_average[1] == 0
    assert angular_average[2] == 0
    assert angular_average[3] == 0

    assert (
        angular_average[4]
        ==
        sp.Rational(
            34,
            8505,
        )
    )

    # V/V_flat = 2 * normalized S^2 average of the directional integral.
    physical_l4 = sp.simplify(
        2 * angular_average[4]
    )

    assert physical_l4 == sp.Rational(
        68,
        8505,
    )

    e2 = sp.Rational(
        8,
        27,
    )

    electric_coefficient = (
        sp.simplify(
            physical_l4 / e2
        )
    )

    assert (
        electric_coefficient
        ==
        sp.Rational(
            17,
            630,
        )
    )

    print(
        {
            "raw_flat_directional_average":
                str(angular_average[0]),
            "raw_L4_directional_average":
                str(angular_average[4]),
            "physical_V_over_Vflat_L4":
                str(physical_l4),
            "E2":
                str(e2),
            "pure_electric_volume_coefficient":
                str(electric_coefficient),
        }
    )

    print(
        "PASS: exact truncated-series Kasner parent volume gives "
        "V/V_flat = 1 + (68/8505)L^4 + O(L^6), "
        "equivalently (17/630)E^2 L^4."
    )


if __name__ == "__main__":
    main()
