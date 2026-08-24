#!/usr/bin/env python3
"""A39 provisional audit: sharp omitted-transform and future-score bounds.

This script validates a concrete generalized-moment extremal problem arising
from the centered-contraction transport identity in MFRP-TR-2026-01.

It performs four logically separate tasks:
1. solves the lower and upper primal/dual contact systems at high precision;
2. certifies a unique solution in a 1e-30 box with the Krawczyk operator;
3. interval-verifies the endpoint/derivative signs used by the ECT argument;
4. reports rigorous intervals for the omitted Laplace value, Q_mu, and the
   next Q_log2 value.

The global envelope step uses the analytic fact that
    {1, x, exp(-mu*x), exp(-lambda*x), exp(-2*lambda*x)}
is an extended complete Chebyshev system on every finite interval when the
positive exponents are distinct. Hence a nonzero residual has at most four
zeros counting multiplicity. The script validates the contact multiplicities
and the robust signs; the ECT theorem itself is mathematical input, not a
numerical test.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, Sequence

import mpmath as mp

mp.mp.dps = 100
mp.iv.dps = 80
iv = mp.iv

LAMBDA_1 = mp.log(2)
LAMBDA_2 = 2 * LAMBDA_1
MU = LAMBDA_1 / 2
MEAN = mp.mpf(2)
S1 = mp.mpf(31) / 80
S2 = mp.mpf(341) / 1280
BOX_RADIUS = mp.mpf("1e-30")


def ivdeg(x: mp.mpf) -> object:
    s = mp.nstr(x, 120)
    return iv.mpf([s, s])


def ivbox(center: Sequence[mp.mpf], radius: mp.mpf) -> list[object]:
    return [
        iv.mpf([mp.nstr(c - radius, 120), mp.nstr(c + radius, 120)])
        for c in center
    ]


def izero() -> object:
    return iv.mpf([0, 0])


def point_inverse(matrix: Sequence[Sequence[mp.mpf]]) -> mp.matrix:
    return mp.inverse(mp.matrix(matrix))


def point_matvec(matrix: mp.matrix, vector: Sequence[mp.mpf]) -> list[mp.mpf]:
    return [
        sum(matrix[i, j] * vector[j] for j in range(len(vector)))
        for i in range(matrix.rows)
    ]


def point_interval_matmul(
    left: mp.matrix, right: Sequence[Sequence[object]]
) -> list[list[object]]:
    rows, inner, cols = left.rows, left.cols, len(right[0])
    out = [[izero() for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            value = izero()
            for k in range(inner):
                value += ivdeg(left[i, k]) * right[k][j]
            out[i][j] = value
    return out


def interval_matvec(
    matrix: Sequence[Sequence[object]], vector: Sequence[object]
) -> list[object]:
    out: list[object] = []
    for row in matrix:
        value = izero()
        for coefficient, item in zip(row, vector):
            value += coefficient * item
        out.append(value)
    return out


def krawczyk_certify(
    center: Sequence[mp.mpf],
    radius: mp.mpf,
    f_point: Callable[[Sequence[mp.mpf]], list[mp.mpf]],
    j_point: Callable[[Sequence[mp.mpf]], list[list[mp.mpf]]],
    j_interval: Callable[[Sequence[object]], list[list[object]]],
) -> tuple[bool, list[object]]:
    n = len(center)
    box = ivbox(center, radius)
    f_center = f_point(center)
    inverse = point_inverse(j_point(center))
    correction = point_matvec(inverse, f_center)
    base = [center[i] - correction[i] for i in range(n)]

    product = point_interval_matmul(inverse, j_interval(box))
    remainder = [
        [
            (ivdeg(1) if i == j else ivdeg(0)) - product[i][j]
            for j in range(n)
        ]
        for i in range(n)
    ]
    centered_box = [box[i] - ivdeg(center[i]) for i in range(n)]
    image_delta = interval_matvec(remainder, centered_box)
    image = [ivdeg(base[i]) + image_delta[i] for i in range(n)]

    strict_inclusion = True
    for candidate, original in zip(image, box):
        if not (
            mp.mpf(candidate.a) > mp.mpf(original.a)
            and mp.mpf(candidate.b) < mp.mpf(original.b)
        ):
            strict_inclusion = False
            break
    return strict_inclusion, image


# ---------------------------------------------------------------------------
# Lower-transform contact system
# Variables: x1, x2, w, y0, y1, y2, y3.
# The primal is w*delta_x1 + (1-w)*delta_x2.
# The dual lower envelope is h=y0+y1*x+y2*e^-lambda1*x+y3*e^-lambda2*x.
# Contact conditions: g-h and its derivative vanish at x1 and x2.
# ---------------------------------------------------------------------------


def lower_f(z: Sequence[mp.mpf]) -> list[mp.mpf]:
    x1, x2, w, y0, y1, y2, y3 = z
    e11, e12 = mp.exp(-LAMBDA_1 * x1), mp.exp(-LAMBDA_1 * x2)
    e21, e22 = mp.exp(-LAMBDA_2 * x1), mp.exp(-LAMBDA_2 * x2)
    em1, em2 = mp.exp(-MU * x1), mp.exp(-MU * x2)

    def residual(x: mp.mpf, em: mp.mpf, e1: mp.mpf, e2: mp.mpf) -> mp.mpf:
        return em - y0 - y1 * x - y2 * e1 - y3 * e2

    def derivative(em: mp.mpf, e1: mp.mpf, e2: mp.mpf) -> mp.mpf:
        return -MU * em - y1 + LAMBDA_1 * y2 * e1 + LAMBDA_2 * y3 * e2

    return [
        w * x1 + (1 - w) * x2 - MEAN,
        w * e11 + (1 - w) * e12 - S1,
        w * e21 + (1 - w) * e22 - S2,
        residual(x1, em1, e11, e21),
        derivative(em1, e11, e21),
        residual(x2, em2, e12, e22),
        derivative(em2, e12, e22),
    ]


def lower_j_point(z: Sequence[mp.mpf]) -> list[list[mp.mpf]]:
    x1, x2, w, _y0, y1, y2, y3 = z
    e11, e12 = mp.exp(-LAMBDA_1 * x1), mp.exp(-LAMBDA_1 * x2)
    e21, e22 = mp.exp(-LAMBDA_2 * x1), mp.exp(-LAMBDA_2 * x2)
    em1, em2 = mp.exp(-MU * x1), mp.exp(-MU * x2)
    rp1 = -MU * em1 - y1 + LAMBDA_1 * y2 * e11 + LAMBDA_2 * y3 * e21
    rp2 = -MU * em2 - y1 + LAMBDA_1 * y2 * e12 + LAMBDA_2 * y3 * e22
    rpp1 = MU**2 * em1 - LAMBDA_1**2 * y2 * e11 - LAMBDA_2**2 * y3 * e21
    rpp2 = MU**2 * em2 - LAMBDA_1**2 * y2 * e12 - LAMBDA_2**2 * y3 * e22
    return [
        [w, 1 - w, x1 - x2, 0, 0, 0, 0],
        [-LAMBDA_1 * w * e11, -LAMBDA_1 * (1 - w) * e12, e11 - e12, 0, 0, 0, 0],
        [-LAMBDA_2 * w * e21, -LAMBDA_2 * (1 - w) * e22, e21 - e22, 0, 0, 0, 0],
        [rp1, 0, 0, -1, -x1, -e11, -e21],
        [rpp1, 0, 0, 0, -1, LAMBDA_1 * e11, LAMBDA_2 * e21],
        [0, rp2, 0, -1, -x2, -e12, -e22],
        [0, rpp2, 0, 0, -1, LAMBDA_1 * e12, LAMBDA_2 * e22],
    ]


def lower_j_interval(z: Sequence[object]) -> list[list[object]]:
    x1, x2, w, _y0, y1, y2, y3 = z
    one, zero = ivdeg(1), ivdeg(0)
    l1, l2, mu = ivdeg(LAMBDA_1), ivdeg(LAMBDA_2), ivdeg(MU)
    e11, e12 = iv.exp(-l1 * x1), iv.exp(-l1 * x2)
    e21, e22 = iv.exp(-l2 * x1), iv.exp(-l2 * x2)
    em1, em2 = iv.exp(-mu * x1), iv.exp(-mu * x2)
    rp1 = -mu * em1 - y1 + l1 * y2 * e11 + l2 * y3 * e21
    rp2 = -mu * em2 - y1 + l1 * y2 * e12 + l2 * y3 * e22
    rpp1 = mu**2 * em1 - l1**2 * y2 * e11 - l2**2 * y3 * e21
    rpp2 = mu**2 * em2 - l1**2 * y2 * e12 - l2**2 * y3 * e22
    return [
        [w, one - w, x1 - x2, zero, zero, zero, zero],
        [-l1 * w * e11, -l1 * (one - w) * e12, e11 - e12, zero, zero, zero, zero],
        [-l2 * w * e21, -l2 * (one - w) * e22, e21 - e22, zero, zero, zero, zero],
        [rp1, zero, zero, -one, -x1, -e11, -e21],
        [rpp1, zero, zero, zero, -one, l1 * e11, l2 * e21],
        [zero, rp2, zero, -one, -x2, -e12, -e22],
        [zero, rpp2, zero, zero, -one, l1 * e12, l2 * e22],
    ]


# ---------------------------------------------------------------------------
# Upper-transform contact system
# Variables: x, w0, w1, w4, y0, y1, y2, y3.
# The primal is w0*delta_0 + w1*delta_x + w4*delta_4.
# The dual upper envelope contacts g at 0, x (tangentially), and 4.
# ---------------------------------------------------------------------------


def upper_f(z: Sequence[mp.mpf]) -> list[mp.mpf]:
    x, w0, w1, w4, y0, y1, y2, y3 = z
    e1, e2, em = mp.exp(-LAMBDA_1 * x), mp.exp(-LAMBDA_2 * x), mp.exp(-MU * x)
    return [
        w0 + w1 + w4 - 1,
        w1 * x + 4 * w4 - MEAN,
        w0 + w1 * e1 + w4 * mp.exp(-4 * LAMBDA_1) - S1,
        w0 + w1 * e2 + w4 * mp.exp(-4 * LAMBDA_2) - S2,
        y0 + y2 + y3 - 1,
        y0 + y1 * x + y2 * e1 + y3 * e2 - em,
        y1 - LAMBDA_1 * y2 * e1 - LAMBDA_2 * y3 * e2 + MU * em,
        y0 + 4 * y1 + y2 * mp.exp(-4 * LAMBDA_1) + y3 * mp.exp(-4 * LAMBDA_2) - mp.exp(-4 * MU),
    ]


def upper_j_point(z: Sequence[mp.mpf]) -> list[list[mp.mpf]]:
    x, _w0, w1, _w4, _y0, y1, y2, y3 = z
    e1, e2, em = mp.exp(-LAMBDA_1 * x), mp.exp(-LAMBDA_2 * x), mp.exp(-MU * x)
    dp = y1 - LAMBDA_1 * y2 * e1 - LAMBDA_2 * y3 * e2 + MU * em
    dpp = LAMBDA_1**2 * y2 * e1 + LAMBDA_2**2 * y3 * e2 - MU**2 * em
    return [
        [0, 1, 1, 1, 0, 0, 0, 0],
        [w1, 0, x, 4, 0, 0, 0, 0],
        [-LAMBDA_1 * w1 * e1, 1, e1, mp.exp(-4 * LAMBDA_1), 0, 0, 0, 0],
        [-LAMBDA_2 * w1 * e2, 1, e2, mp.exp(-4 * LAMBDA_2), 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [dp, 0, 0, 0, 1, x, e1, e2],
        [dpp, 0, 0, 0, 0, 1, -LAMBDA_1 * e1, -LAMBDA_2 * e2],
        [0, 0, 0, 0, 1, 4, mp.exp(-4 * LAMBDA_1), mp.exp(-4 * LAMBDA_2)],
    ]


def upper_j_interval(z: Sequence[object]) -> list[list[object]]:
    x, _w0, w1, _w4, _y0, y1, y2, y3 = z
    one, zero = ivdeg(1), ivdeg(0)
    l1, l2, mu = ivdeg(LAMBDA_1), ivdeg(LAMBDA_2), ivdeg(MU)
    e1, e2, em = iv.exp(-l1 * x), iv.exp(-l2 * x), iv.exp(-mu * x)
    dp = y1 - l1 * y2 * e1 - l2 * y3 * e2 + mu * em
    dpp = l1**2 * y2 * e1 + l2**2 * y3 * e2 - mu**2 * em
    e14, e24 = iv.exp(-4 * l1), iv.exp(-4 * l2)
    return [
        [zero, one, one, one, zero, zero, zero, zero],
        [w1, zero, x, ivdeg(4), zero, zero, zero, zero],
        [-l1 * w1 * e1, one, e1, e14, zero, zero, zero, zero],
        [-l2 * w1 * e2, one, e2, e24, zero, zero, zero, zero],
        [zero, zero, zero, zero, one, zero, one, one],
        [dp, zero, zero, zero, one, x, e1, e2],
        [dpp, zero, zero, zero, zero, one, -l1 * e1, -l2 * e2],
        [zero, zero, zero, zero, one, ivdeg(4), e14, e24],
    ]


def solve_centers() -> tuple[list[mp.mpf], list[mp.mpf]]:
    lower_guess = (
        mp.mpf("0.2817737193"), mp.mpf("3.0552051995"), mp.mpf("0.3804691795"),
        mp.mpf("0.4773495998"), mp.mpf("-0.06801424452"),
        mp.mpf("0.6591415481"), mp.mpf("-0.1380646609"),
    )
    upper_guess = (
        mp.mpf("1.7066204386"), mp.mpf("0.2193160394"),
        mp.mpf("0.4895551793"), mp.mpf("0.2911287813"),
        mp.mpf("0.4626977607"), mp.mpf("-0.06401298676"),
        mp.mpf("0.7040912970"), mp.mpf("-0.1667890577"),
    )

    lower_root = mp.findroot(
        lambda x1, x2, w, y0, y1, y2, y3: tuple(lower_f((x1, x2, w, y0, y1, y2, y3))),
        lower_guess, tol=mp.mpf("1e-75"), maxsteps=100,
    )
    upper_root = mp.findroot(
        lambda x, w0, w1, w4, y0, y1, y2, y3: tuple(upper_f((x, w0, w1, w4, y0, y1, y2, y3))),
        upper_guess, tol=mp.mpf("1e-75"), maxsteps=100,
    )
    return [mp.mpf(v) for v in lower_root], [mp.mpf(v) for v in upper_root]


def lower_residual_at(x: mp.mpf, box: Sequence[object]) -> object:
    _x1, _x2, _w, y0, y1, y2, y3 = box
    xx = ivdeg(x)
    return (
        iv.exp(-ivdeg(MU) * xx) - y0 - y1 * xx
        - y2 * iv.exp(-ivdeg(LAMBDA_1) * xx)
        - y3 * iv.exp(-ivdeg(LAMBDA_2) * xx)
    )


def upper_derivative_at(x: mp.mpf, box: Sequence[object]) -> object:
    _xc, _w0, _w1, _w4, _y0, y1, y2, y3 = box
    xx = ivdeg(x)
    return (
        y1 - ivdeg(LAMBDA_1) * y2 * iv.exp(-ivdeg(LAMBDA_1) * xx)
        - ivdeg(LAMBDA_2) * y3 * iv.exp(-ivdeg(LAMBDA_2) * xx)
        + ivdeg(MU) * iv.exp(-ivdeg(MU) * xx)
    )


def interval_pair(value: object, digits: int = 55) -> list[str]:
    return [mp.nstr(mp.mpf(value.a), digits), mp.nstr(mp.mpf(value.b), digits)]


def point_strings(values: Sequence[mp.mpf], digits: int = 55) -> list[str]:
    return [mp.nstr(value, digits) for value in values]


def main() -> None:
    lower_center, upper_center = solve_centers()
    lower_ok, lower_box = krawczyk_certify(
        lower_center, BOX_RADIUS, lower_f, lower_j_point, lower_j_interval
    )
    upper_ok, upper_box = krawczyk_certify(
        upper_center, BOX_RADIUS, upper_f, upper_j_point, upper_j_interval
    )

    lower_r0 = lower_residual_at(mp.mpf(0), lower_box)
    lower_r4 = lower_residual_at(mp.mpf(4), lower_box)
    upper_dp0 = upper_derivative_at(mp.mpf(0), upper_box)
    upper_dp4 = upper_derivative_at(mp.mpf(4), upper_box)

    x1, x2, w, *_ = lower_box
    lower_laplace = (
        w * iv.exp(-ivdeg(MU) * x1)
        + (ivdeg(1) - w) * iv.exp(-ivdeg(MU) * x2)
    )
    x, w0, w1, w4, *_ = upper_box
    upper_laplace = (
        w0 + w1 * iv.exp(-ivdeg(MU) * x)
        + w4 * iv.exp(-ivdeg(MU) * ivdeg(4))
    )

    # Since Q=-log(L)/mu is decreasing in L:
    q_lower = -iv.log(upper_laplace) / ivdeg(MU)
    q_upper = -iv.log(lower_laplace) / ivdeg(MU)
    future_lower = ivdeg(1) + ivdeg(mp.mpf("0.5")) * q_lower
    future_upper = ivdeg(1) + ivdeg(mp.mpf("0.5")) * q_upper

    gates = {
        "G1_lower_contact_root_krawczyk_unique": lower_ok,
        "G2_upper_contact_root_krawczyk_unique": upper_ok,
        "G3_lower_residual_positive_at_0": mp.mpf(lower_r0.a) > 0,
        "G4_lower_residual_positive_at_4": mp.mpf(lower_r4.a) > 0,
        "G5_upper_residual_derivative_positive_at_0": mp.mpf(upper_dp0.a) > 0,
        "G6_upper_residual_derivative_negative_at_4": mp.mpf(upper_dp4.b) < 0,
        "G7_lower_primal_atoms_inside_support": (
            mp.mpf(lower_box[0].a) > 0 and mp.mpf(lower_box[1].b) < 4
        ),
        "G8_lower_weights_positive": (
            mp.mpf(lower_box[2].a) > 0 and mp.mpf(lower_box[2].b) < 1
        ),
        "G9_upper_atoms_and_weights_admissible": (
            mp.mpf(upper_box[0].a) > 0 and mp.mpf(upper_box[0].b) < 4
            and all(mp.mpf(upper_box[i].a) > 0 for i in (1, 2, 3))
        ),
        "G10_all_numeric_certificate_gates_pass": False,
    }
    gates["G10_all_numeric_certificate_gates_pass"] = all(
        value for key, value in gates.items() if key != "G10_all_numeric_certificate_gates_pass"
    )

    result = {
        "audit": "A39_PROVISIONAL_SHARP_PREDICTION_INTERVAL",
        "support_contract": ["0", "4"],
        "observed_constraints": {
            "mean": "2",
            "L_log2": "31/80",
            "L_2log2": "341/1280",
        },
        "omitted_parameter": "(log 2)/2",
        "contraction": "1/2",
        "box_radius": mp.nstr(BOX_RADIUS, 8),
        "lower_contact_solution_center": point_strings(lower_center),
        "upper_contact_solution_center": point_strings(upper_center),
        "sign_certificates": {
            "lower_residual_at_0": interval_pair(lower_r0),
            "lower_residual_at_4": interval_pair(lower_r4),
            "upper_residual_derivative_at_0": interval_pair(upper_dp0),
            "upper_residual_derivative_at_4": interval_pair(upper_dp4),
        },
        "sharp_intervals": {
            "L_mu_min": interval_pair(lower_laplace),
            "L_mu_max": interval_pair(upper_laplace),
            "Q_mu_min": interval_pair(q_lower),
            "Q_mu_max": interval_pair(q_upper),
            "next_Q_log2_min": interval_pair(future_lower),
            "next_Q_log2_max": interval_pair(future_upper),
        },
        "analytic_global_step": (
            "The five-function exponential-polynomial system is ECT. "
            "The lower residual has two certified double contacts and positive endpoint signs; "
            "the upper residual has endpoint contacts plus one certified double interior contact "
            "and the certified endpoint derivative signs. Therefore the dual envelopes have "
            "the required global inequalities on [0,4]."
        ),
        "gates": gates,
        "verdict": (
            "PASS_SHARP_OMITTED_TRANSFORM_AND_FUTURE_SCORE_INTERVAL"
            if gates["G10_all_numeric_certificate_gates_pass"]
            else "FAIL_NUMERIC_CERTIFICATE"
        ),
        "boundary": (
            "This is a mathematical bound conditional on bounded support and the supplied moments. "
            "It does not establish a physical q-scale, a physical contraction, or an empirical model."
        ),
    }

    output = Path(__file__).with_name("a39_sharp_prediction_interval_results.json")
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"\nWrote {output}")

    if not gates["G10_all_numeric_certificate_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
