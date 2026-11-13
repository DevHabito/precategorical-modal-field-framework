#!/usr/bin/env python3
"""Exact d=5 LRS-Kasner parent-volume directional-jet calibration.

Spacetime dimension:
    d = 5,
    n = d - 1 = 4 spatial dimensions.

LRS Kasner exponents:
    p_parallel = -1/2,
    p_perp     = +1/2
with p_perp repeated three times.

Metric:
    ds^2 = -dt^2 + t^(-1) dx^2 + t (dy_1^2+dy_2^2+dy_3^2).

Centered tips:
    p=(1-L,0), q=(1+L,0).

The calculation uses exact rational arithmetic direction by direction.
It reconstructs the L^2 and L^4 directional polynomials from rational
training directions and verifies them on held-out rational directions.

For w = mu^2, where mu is the axial direction cosine,

    c2(w)
      = 4(16 w^2 - 20 w + 3)/105,

    c4(w)
      = (26560 w^4 - 70336 w^3 + 61059 w^2
         - 19080 w + 1377)/22680.

The normalized S^3 moments are

    <w^k> = (1/2)_k / (2)_k.

They give

    <c2> = 0,
    <c4> = 5/576.

The physical volume ratio has normalization factor (n+1)/2 = 5/2, hence

    V_Kasner^(5)/V_flat^(5)
      = 1 + (25/1152) L^4 + O(L^6).

For this LRS Kasner geometry,

    E^2 = 3/4,
    D^2 = 3/2,
    H^2 = 0.

The corrected all-d ACD coefficients give exactly

    A_5 E^2 + C_5 D^2 = 25/1152.

No floating-point fitting or rational reconstruction is used.
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

    # -2 p_parallel = +1, -2 p_perp = -1.
    axial_power = time_power(sp.Integer(1))
    transverse_power = time_power(sp.Integer(-1))
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

    return radius_ratio


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

    # sqrt(det g_spatial)=t because sum_i p_i=1.
    lapse = {0: sp.Integer(1), 1: Y}

    # Four spatial dimensions -> radial power rho^4.
    past_integrand = lapse
    future_integrand = lapse

    for _ in range(4):
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


def normalized_s3_average(polynomial: sp.Expr) -> sp.Expr:
    """Average polynomial(w) over S^3, w=mu^2."""
    expanded = sp.Poly(
        sp.expand(polynomial),
        w_symbol,
    )

    total = sp.Integer(0)

    for (power,), coefficient in expanded.terms():
        moment = (
            sp.rf(sp.Rational(1, 2), power)
            /
            sp.rf(sp.Integer(2), power)
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

        assert flat == sp.Rational(2, 5)

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

    expected_c2 = (
        4
        * (
            16 * w_symbol**2
            - 20 * w_symbol
            + 3
        )
        / 105
    )

    expected_c4 = (
        26560 * w_symbol**4
        - 70336 * w_symbol**3
        + 61059 * w_symbol**2
        - 19080 * w_symbol
        + 1377
    ) / 22680

    assert sp.simplify(
        c2_polynomial - expected_c2
    ) == 0

    assert sp.simplify(
        c4_polynomial - expected_c4
    ) == 0

    for w in held_out_w:
        flat, c2, c4 = directional_parent_coefficients(w)

        assert flat == sp.Rational(2, 5)

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

    average_c2 = normalized_s3_average(
        c2_polynomial
    )

    average_c4 = normalized_s3_average(
        c4_polynomial
    )

    assert average_c2 == 0
    assert average_c4 == sp.Rational(5, 576)

    # General flat normalization for n=4:
    # V/V_flat = (n+1)/2 * <I_dir> = 5/2 * <I_dir>.
    physical_l4 = sp.factor(
        sp.Rational(5, 2) * average_c4
    )

    assert physical_l4 == sp.Rational(25, 1152)

    d = sp.Integer(5)
    n = sp.Integer(4)

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

    assert e2 == sp.Rational(3, 4)
    assert d2 == sp.Rational(3, 2)

    a5 = (
        d
        * (7 * d**2 + 44 * d + 58)
        / (
            180
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    c5 = -(
        d
        / (
            120
            * (d + 1)
            * (d + 3)
            * (d + 4)
        )
    )

    predicted = sp.factor(
        a5 * e2 + c5 * d2
    )

    assert predicted == sp.Rational(25, 1152)
    assert sp.simplify(physical_l4 - predicted) == 0

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
        "PASS: exact d=5 LRS-Kasner directional-jet calculation gives "
        "V/V_flat = 1 + (25/1152)L^4 + O(L^6), exactly matching "
        "A_5 E^2 + C_5 D^2 from the corrected all-d ACD formula."
    )


if __name__ == "__main__":
    main()
