#!/usr/bin/env python3
"""Exact directional-jet repair of the d=4 LRS-Kasner parent volume.

Why this checker exists
-----------------------
The older fully symbolic Kasner series kept the angular variable w=mu^2
inside every square root and series operation.  That route became fragile
and produced a normalization alarm.

This checker avoids the global multivariate expansion.  For each exact
rational direction w it builds a univariate formal power series in L,
solves the null-geodesic direction equation coefficient by coefficient,
solves the cone-crossing location, and extracts the directional parent-volume
coefficients.

Five rational directions reconstruct the quartic L^4 angular polynomial.
Two additional rational directions are held out and must agree exactly.

The reconstructed coefficients are

    c2(w) =
        7 (45 w^2 - 57 w + 10) / 540,

    c4(w) =
        (56133 w^4 - 152334 w^3 + 138393 w^2
         - 46632 w + 3608) / 54432.

With w=mu^2 and normalized S^2 average

    <w^k> = 1/(2k+1),

one obtains

    <c2> = 0,
    <c4> = 34/8505.

The directional time/angular integral has flat value 1/2, so the physical
ratio V/V_flat is twice the normalized angular average:

    V_Kasner / V_flat
      = 1 + (68/8505) L^4 + O(L^6).

Since E^2=8/27 at the midpoint,

    v_E = (68/8505)/(8/27) = 17/630.

All arithmetic used to reconstruct and test the angular polynomial is exact.
No floating-point rational reconstruction is used.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import sympy as sp


MAX_ORDER = 5

L, Y, u = sp.symbols("L Y u", real=True)
w_symbol = sp.symbols("w", real=True)

Jet = dict[int, sp.Expr]


def clean(jet: Jet) -> Jet:
    out: Jet = {}

    for degree, value in jet.items():
        if degree <= MAX_ORDER and value != 0:
            value = sp.cancel(value)
            if value != 0:
                out[degree] = value

    return out


def constant(value: sp.Expr | int) -> Jet:
    return {0: sp.sympify(value)}


def add(left: Jet, right: Jet) -> Jet:
    acc: defaultdict[int, sp.Expr] = defaultdict(
        lambda: sp.Integer(0)
    )

    for degree, value in left.items():
        acc[degree] += value

    for degree, value in right.items():
        acc[degree] += value

    return clean(dict(acc))


def negate(jet: Jet) -> Jet:
    return {
        degree: -value
        for degree, value in jet.items()
    }


def subtract(left: Jet, right: Jet) -> Jet:
    return add(left, negate(right))


def scale(jet: Jet, factor: sp.Expr | int) -> Jet:
    factor = sp.sympify(factor)

    return clean(
        {
            degree: factor * value
            for degree, value in jet.items()
        }
    )


def multiply(left: Jet, right: Jet) -> Jet:
    acc: defaultdict[int, sp.Expr] = defaultdict(
        lambda: sp.Integer(0)
    )

    for left_degree, left_value in left.items():
        for right_degree, right_value in right.items():
            degree = left_degree + right_degree

            if degree <= MAX_ORDER:
                acc[degree] += (
                    left_value
                    * right_value
                )

    return clean(dict(acc))


def binomial_power(
    jet: Jet,
    exponent: sp.Rational,
) -> Jet:
    scalar = jet.get(0, sp.Integer(0))

    if scalar == 0:
        raise ValueError(
            "formal binomial series requires nonzero scalar term"
        )

    q = subtract(
        scale(jet, 1 / scalar),
        constant(1),
    )

    out = constant(1)
    term = constant(1)

    for order in range(1, MAX_ORDER + 2):
        term = multiply(term, q)

        if not term:
            break

        out = add(
            out,
            scale(
                term,
                sp.binomial(exponent, order),
            ),
        )

    return scale(
        out,
        scalar**exponent,
    )


def time_power(exponent: sp.Rational) -> Jet:
    """Return the L-jet of (1+L*u)^exponent."""
    return {
        degree:
            sp.binomial(exponent, degree)
            * u**degree
        for degree in range(MAX_ORDER + 1)
    }


def integrate_u(
    jet: Jet,
    lower: sp.Expr,
    upper: sp.Expr,
) -> Jet:
    return clean(
        {
            degree:
                sp.integrate(
                    value,
                    (u, lower, upper),
                )
            for degree, value in jet.items()
        }
    )


def substitute_jet(
    jet: Jet,
    substitutions: dict[sp.Symbol, sp.Expr],
) -> Jet:
    return clean(
        {
            degree:
                value.subs(substitutions)
            for degree, value in jet.items()
        }
    )


@dataclass(frozen=True)
class ConeSeries:
    direction_parameter: Jet
    axial_integral: Jet
    radius_ratio: Jet


def solve_cone_series(
    w: sp.Rational,
    lower: sp.Expr,
    upper: sp.Expr,
    prefix: str,
    flat_duration: sp.Expr,
) -> ConeSeries:
    """Solve one exact null-cone radial series for fixed rational w."""
    unknowns = sp.symbols(
        f"{prefix}1:{MAX_ORDER}"
    )

    c: Jet = {
        0: w,
        1: unknowns[0],
        2: unknowns[1],
        3: unknowns[2],
        4: unknowns[3],
    }

    t23 = time_power(sp.Rational(2, 3))
    tm43 = time_power(sp.Rational(-4, 3))
    one = constant(1)

    def build(
        current_c: Jet,
    ) -> tuple[Jet, Jet]:
        energy_squared = add(
            multiply(current_c, t23),
            multiply(
                subtract(one, current_c),
                tm43,
            ),
        )

        inverse_energy = binomial_power(
            energy_squared,
            sp.Rational(-1, 2),
        )

        axial = integrate_u(
            multiply(t23, inverse_energy),
            lower,
            upper,
        )

        transverse = integrate_u(
            multiply(tm43, inverse_energy),
            lower,
            upper,
        )

        direction_equation = subtract(
            multiply(
                scale(current_c, 1 - w),
                multiply(axial, axial),
            ),
            multiply(
                scale(
                    subtract(one, current_c),
                    w,
                ),
                multiply(
                    transverse,
                    transverse,
                ),
            ),
        )

        return direction_equation, axial

    solution: dict[sp.Symbol, sp.Expr] = {}

    for degree, unknown in enumerate(
        unknowns,
        start=1,
    ):
        current_c = substitute_jet(
            c,
            solution,
        )

        equation, _ = build(current_c)

        coefficient = sp.factor(
            equation.get(
                degree,
                sp.Integer(0),
            )
        )

        roots = sp.solve(
            sp.Eq(coefficient, 0),
            unknown,
            dict=False,
        )

        if len(roots) != 1:
            raise RuntimeError(
                f"expected one coefficient root at order {degree}"
            )

        solution[unknown] = sp.factor(
            roots[0]
        )

    solved_c = substitute_jet(
        c,
        solution,
    )

    _, axial = build(solved_c)

    radius_ratio = scale(
        multiply(
            binomial_power(
                scale(solved_c, 1 / w),
                sp.Rational(1, 2),
            ),
            axial,
        ),
        1 / flat_duration,
    )

    return ConeSeries(
        direction_parameter=solved_c,
        axial_integral=axial,
        radius_ratio=radius_ratio,
    )


def solve_edge(
    past_radius: Jet,
    future_radius: Jet,
) -> dict[int, sp.Expr]:
    """Return Y_edge = sum y_k L^k through k=4."""
    unknowns = sp.symbols("y1:5")

    edge_trial = sum(
        unknowns[degree - 1] * L**degree
        for degree in range(1, 5)
    )

    difference = sum(
        (
            past_radius.get(degree, 0)
            -
            future_radius.get(degree, 0)
        )
        * L**degree
        for degree in range(MAX_ORDER + 1)
    )

    expanded = sp.series(
        difference.subs(Y, edge_trial),
        L,
        0,
        6,
    ).removeO().expand()

    solution: dict[sp.Symbol, sp.Expr] = {}

    for degree, unknown in enumerate(
        unknowns,
        start=1,
    ):
        coefficient = sp.expand(
            expanded.subs(solution)
        ).coeff(L, degree)

        roots = sp.solve(
            sp.Eq(coefficient, 0),
            unknown,
            dict=False,
        )

        if len(roots) != 1:
            raise RuntimeError(
                f"expected one edge root at order {degree}"
            )

        solution[unknown] = sp.factor(
            roots[0]
        )

    return {
        degree:
            sp.factor(
                unknowns[degree - 1]
                .subs(solution)
            )
        for degree in range(1, 5)
    }


def directional_parent_coefficients(
    w: sp.Rational,
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return flat, L^2 and L^4 coefficients for one rational direction."""
    past = solve_cone_series(
        w=w,
        lower=-1,
        upper=Y,
        prefix="c",
        flat_duration=1 + Y,
    )

    future = solve_cone_series(
        w=w,
        lower=Y,
        upper=1,
        prefix="d",
        flat_duration=1 - Y,
    )

    past_radius = scale(
        past.radius_ratio,
        1 + Y,
    )

    future_radius = scale(
        future.radius_ratio,
        1 - Y,
    )

    edge = solve_edge(
        past_radius,
        future_radius,
    )

    edge_expression = sum(
        value * L**degree
        for degree, value in edge.items()
    )

    lapse = {
        0: sp.Integer(1),
        1: Y,
    }

    past_integrand = multiply(
        lapse,
        multiply(
            multiply(
                past_radius,
                past_radius,
            ),
            past_radius,
        ),
    )

    future_integrand = multiply(
        lapse,
        multiply(
            multiply(
                future_radius,
                future_radius,
            ),
            future_radius,
        ),
    )

    parent = sp.Integer(0)

    for degree in range(5):
        past_antiderivative = sp.integrate(
            past_integrand.get(
                degree,
                sp.Integer(0),
            ),
            Y,
        )

        future_antiderivative = sp.integrate(
            future_integrand.get(
                degree,
                sp.Integer(0),
            ),
            Y,
        )

        moving_boundary = (
            past_antiderivative.subs(
                Y,
                edge_expression,
            )
            -
            past_antiderivative.subs(
                Y,
                -1,
            )
            +
            future_antiderivative.subs(
                Y,
                1,
            )
            -
            future_antiderivative.subs(
                Y,
                edge_expression,
            )
        )

        parent += (
            L**degree
            * sp.series(
                moving_boundary,
                L,
                0,
                5 - degree,
            ).removeO()
        )

    parent = sp.series(
        parent,
        L,
        0,
        5,
    ).removeO().expand()

    return (
        sp.factor(parent.coeff(L, 0)),
        sp.factor(parent.coeff(L, 2)),
        sp.factor(parent.coeff(L, 4)),
    )


def normalized_sphere_average(
    polynomial: sp.Expr,
) -> sp.Expr:
    """Average polynomial(w) over S^2 with w=mu^2."""
    expanded = sp.Poly(
        sp.expand(polynomial),
        w_symbol,
    )

    total = sp.Integer(0)

    for (power,), coefficient in expanded.terms():
        total += (
            coefficient
            / sp.Integer(2 * power + 1)
        )

    return sp.factor(total)


def main() -> None:
    training_w = [
        sp.Rational(1, 16),
        sp.Rational(1, 9),
        sp.Rational(1, 4),
        sp.Rational(1, 2),
        sp.Rational(4, 9),
    ]

    held_out_w = [
        sp.Rational(9, 16),
        sp.Rational(3, 4),
        sp.Rational(2, 3),
        sp.Rational(5, 6),
    ]

    training = []

    for w in training_w:
        flat, c2, c4 = (
            directional_parent_coefficients(w)
        )

        assert flat == sp.Rational(1, 2)

        training.append(
            (w, c2, c4)
        )

        print(
            {
                "w": str(w),
                "flat": str(flat),
                "c2": str(c2),
                "c4": str(c4),
                "role": "training",
            }
        )

    c2_polynomial = sp.factor(
        sp.interpolate(
            [
                (w, c2)
                for w, c2, _ in training
            ],
            w_symbol,
        )
    )

    c4_polynomial = sp.factor(
        sp.interpolate(
            [
                (w, c4)
                for w, _, c4 in training
            ],
            w_symbol,
        )
    )

    expected_c2 = (
        7
        * (
            45 * w_symbol**2
            - 57 * w_symbol
            + 10
        )
        / 540
    )

    expected_c4 = (
        56133 * w_symbol**4
        - 152334 * w_symbol**3
        + 138393 * w_symbol**2
        - 46632 * w_symbol
        + 3608
    ) / 54432

    assert sp.simplify(
        c2_polynomial - expected_c2
    ) == 0

    assert sp.simplify(
        c4_polynomial - expected_c4
    ) == 0

    for w in held_out_w:
        flat, c2, c4 = (
            directional_parent_coefficients(w)
        )

        assert flat == sp.Rational(1, 2)

        assert sp.simplify(
            c2_polynomial.subs(
                w_symbol,
                w,
            )
            - c2
        ) == 0

        assert sp.simplify(
            c4_polynomial.subs(
                w_symbol,
                w,
            )
            - c4
        ) == 0

        print(
            {
                "w": str(w),
                "flat": str(flat),
                "c2": str(c2),
                "c4": str(c4),
                "role": "held_out",
            }
        )

    average_c2 = normalized_sphere_average(
        c2_polynomial
    )

    average_c4 = normalized_sphere_average(
        c4_polynomial
    )

    assert average_c2 == 0
    assert average_c4 == sp.Rational(
        34,
        8505,
    )

    physical_l4 = sp.factor(
        2 * average_c4
    )

    assert physical_l4 == sp.Rational(
        68,
        8505,
    )

    e2 = sp.Rational(8, 27)

    v_e = sp.factor(
        physical_l4 / e2
    )

    assert v_e == sp.Rational(
        17,
        630,
    )

    print(
        {
            "c2_polynomial":
                str(c2_polynomial),
            "c4_polynomial":
                str(c4_polynomial),
            "average_c2":
                str(average_c2),
            "average_c4":
                str(average_c4),
            "physical_parent_L4":
                str(physical_l4),
            "pure_electric_volume_coefficient":
                str(v_e),
        }
    )

    print(
        "PASS: exact directional-jet reconstruction gives "
        "V_Kasner/V_flat = 1 + (68/8505)L^4 + O(L^6), "
        "hence v_E=17/630."
    )


if __name__ == "__main__":
    main()
