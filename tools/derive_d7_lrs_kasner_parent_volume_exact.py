#!/usr/bin/env python3
"""Exact d=7 LRS-Kasner parent-volume directional-jet calibration.

Spacetime dimension:
    d = 7,
    n = 6 spatial dimensions.

LRS Kasner exponents:
    p_parallel = -2/3,
    p_perp     = +1/3
with p_perp repeated four times.

For w=mu^2, exact rational directional jets reconstruct

    c2(w)
      = (175 w^2 - 215 w + 28)/280,

    c4(w)
      = (12271875 w^4 - 31773000 w^3 + 26430775 w^2
         - 7600010 w + 505456)/9450000.

The normalized S^5 moments are

    <w^k> = (1/2)_k / (5/2)_k.

They give

    <c2> = 0,
    <c4> = 566/21384.

The physical normalization factor is (n+1)/2=3, hence

    V_Kasner^(6)/V_flat^(6)
      = 1 + (1981/42768) L^4 + O(L^6).

For this geometry,

    E^2 = 144/125,
    D^2 = 192/125,
    H^2 = 0,

and the corrected all-d ACD law gives exactly

    A_6 E^2 + C_6 D^2 = 1981/42768.

No floating-point fit or rational reconstruction is used.
"""

from __future__ import annotations

from collections import defaultdict
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
    return {degree: -value for degree, value in jet.items()}


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
                acc[degree] += left_value * right_value
    return clean(dict(acc))


def binomial_power(jet: Jet, exponent: sp.Rational) -> Jet:
    scalar = jet.get(0, sp.Integer(0))
    if scalar == 0:
        raise ValueError("formal binomial series requires nonzero scalar term")

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

    return scale(out, scalar**exponent)


def time_power(exponent: sp.Rational) -> Jet:
    return {
        degree:
            sp.binomial(exponent, degree) * u**degree
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
                sp.integrate(value, (u, lower, upper))
            for degree, value in jet.items()
        }
    )


def substitute_jet(
    jet: Jet,
    substitutions: dict[sp.Symbol, sp.Expr],
) -> Jet:
    return clean(
        {
            degree: value.subs(substitutions)
            for degree, value in jet.items()
        }
    )


def solve_cone_series(
    w: sp.Rational,
    lower: sp.Expr,
    upper: sp.Expr,
    prefix: str,
    flat_duration: sp.Expr,
) -> Jet:
    unknowns = sp.symbols(f"{prefix}1:{MAX_ORDER}")

    c: Jet = {
        0: w,
        1: unknowns[0],
        2: unknowns[1],
        3: unknowns[2],
        4: unknowns[3],
    }

    axial_power = time_power(sp.Rational(4, 3))
    transverse_power = time_power(sp.Rational(-2, 3))
    one = constant(1)

    def build(current_c: Jet) -> tuple[Jet, Jet]:
        energy_squared = add(
            multiply(current_c, axial_power),
            multiply(
                subtract(one, current_c),
                transverse_power,
            ),
        )

        inverse_energy = binomial_power(
            energy_squared,
            sp.Rational(-1, 2),
        )

        axial = integrate_u(
            multiply(axial_power, inverse_energy),
            lower,
            upper,
        )

        transverse = integrate_u(
            multiply(transverse_power, inverse_energy),
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
                multiply(transverse, transverse),
            ),
        )

        return direction_equation, axial

    solution: dict[sp.Symbol, sp.Expr] = {}

    for degree, unknown in enumerate(unknowns, start=1):
        current_c = substitute_jet(c, solution)
        equation, _ = build(current_c)

        coefficient = sp.factor(
            equation.get(degree, sp.Integer(0))
        )

        roots = sp.solve(
            sp.Eq(coefficient, 0),
            unknown,
            dict=False,
        )

        if len(roots) != 1:
            raise RuntimeError(
                f"expected one direction coefficient root at order {degree}"
            )

        solution[unknown] = sp.factor(roots[0])

    solved_c = substitute_jet(c, solution)
    _, axial = build(solved_c)

    return scale(
        multiply(
            binomial_power(
                scale(solved_c, 1 / w),
                sp.Rational(1, 2),
            ),
            axial,
        ),
        1 / flat_duration,
    )


def solve_edge(
    past_radius: Jet,
    future_radius: Jet,
) -> dict[int, sp.Expr]:
    unknowns = sp.symbols("y1:5")

    edge_trial = sum(
        unknowns[degree - 1] * L**degree
        for degree in range(1, 5)
    )

    difference = sum(
        (
            past_radius.get(degree, 0)
            - future_radius.get(degree, 0)
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

    for degree, unknown in enumerate(unknowns, start=1):
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

        solution[unknown] = sp.factor(roots[0])

    return {
        degree:
            sp.factor(
                unknowns[degree - 1].subs(solution)
            )
        for degree in range(1, 5)
    }


def directional_parent_coefficients(
    w: sp.Rational,
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    past_ratio = solve_cone_series(
        w=w,
        lower=-1,
        upper=Y,
        prefix="c",
        flat_duration=1 + Y,
    )

    future_ratio = solve_cone_series(
        w=w,
        lower=Y,
        upper=1,
        prefix="d",
        flat_duration=1 - Y,
    )

    past_radius = scale(
        past_ratio,
        1 + Y,
    )

    future_radius = scale(
        future_ratio,
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

    lapse = {0: sp.Integer(1), 1: Y}

    past_integrand = lapse
    future_integrand = lapse

    for _ in range(6):
        past_integrand = multiply(
            past_integrand,
            past_radius,
        )
        future_integrand = multiply(
            future_integrand,
            future_radius,
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
            - past_antiderivative.subs(
                Y,
                -1,
            )
            + future_antiderivative.subs(
                Y,
                1,
            )
            - future_antiderivative.subs(
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


def normalized_s5_average(polynomial: sp.Expr) -> sp.Expr:
    expanded = sp.Poly(
        sp.expand(polynomial),
        w_symbol,
    )

    total = sp.Integer(0)

    for (power,), coefficient in expanded.terms():
        moment = (
            sp.rf(sp.Rational(1, 2), power)
            /
            sp.rf(sp.Integer(3), power)
        )
        total += coefficient * moment

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
    ]

    training = []

    for w in training_w:
        flat, c2, c4 = directional_parent_coefficients(w)

        assert flat == sp.Rational(2, 7)

        training.append((w, c2, c4))

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
            [(w, c2) for w, c2, _ in training],
            w_symbol,
        )
    )

    c4_polynomial = sp.factor(
        sp.interpolate(
            [(w, c4) for w, _, c4 in training],
            w_symbol,
        )
    )

    # No all-d target polynomial is inserted here.
    # Five training directions determine a degree <= 4 candidate.
    # Three held-out rational directions must reproduce it exactly.
    assert sp.Poly(c2_polynomial, w_symbol).degree() <= 4
    assert sp.Poly(c4_polynomial, w_symbol).degree() <= 4

    for w in held_out_w:
        flat, c2, c4 = directional_parent_coefficients(w)

        assert flat == sp.Rational(2, 7)

        assert sp.simplify(
            c2_polynomial.subs(w_symbol, w) - c2
        ) == 0

        assert sp.simplify(
            c4_polynomial.subs(w_symbol, w) - c4
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

    average_c2 = normalized_s5_average(
        c2_polynomial
    )

    average_c4 = normalized_s5_average(
        c4_polynomial
    )

    assert average_c2 == 0
    assert average_c4 == sp.Rational(566, 21384)

    physical_l4 = sp.factor(
        sp.Rational(7, 2) * average_c4
    )

    assert physical_l4 == sp.Rational(1981, 42768)

    d = sp.Integer(7)
    n = sp.Integer(6)

    e2 = (
        4
        * (n - 2)**2
        * (n - 1)
        / n**3
    )

    d2 = (
        16
        * (n - 1)
        * (n - 2)
        / n**3
    )

    assert e2 == sp.Rational(40, 27)
    assert d2 == sp.Rational(40, 27)

    a7 = (
        d
        * (7 * d**2 + 44 * d + 58)
        / (
            180
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    c7 = -(
        d
        / (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    predicted = sp.factor(
        a7 * e2 + c7 * d2
    )

    assert predicted == sp.Rational(1981, 42768)
    assert sp.simplify(
        physical_l4 - predicted
    ) == 0

    print(
        {
            "c2_polynomial": str(c2_polynomial),
            "c4_polynomial": str(c4_polynomial),
            "average_c2": str(average_c2),
            "average_c4": str(average_c4),
            "physical_parent_L4": str(physical_l4),
            "E2": str(e2),
            "D2": str(d2),
            "all_d_prediction": str(predicted),
        }
    )

    print(
        "PASS: exact d=7 LRS-Kasner directional-jet calculation gives "
        "V/V_flat = 1 + (1981/42768)L^4 + O(L^6), exactly matching "
        "A_6 E^2 + C_6 D^2 from the corrected all-d ACD formula."
    )


if __name__ == "__main__":
    main()
