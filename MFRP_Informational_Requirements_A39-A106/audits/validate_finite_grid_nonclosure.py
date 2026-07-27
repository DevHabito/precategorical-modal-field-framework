#!/usr/bin/env python3
"""Exact dyadic witnesses for finite-grid nonclosure.

This script is a regression check for the analytic construction in
MFRP_next_step_finite_grid_nonclosure.md.  All tracked constraints are
verified with fractions.  Decimal arithmetic is used only to display the
nonzero omitted-transform and future-Q differences.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
from typing import Iterable, List


def multiply_polynomials(a: List[Fraction], b: List[Fraction]) -> List[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def evaluate_fraction_polynomial(coeffs: Iterable[Fraction], t: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(list(coeffs)):
        value = value * t + coefficient
    return value


def derivative_at_one(coeffs: Iterable[Fraction]) -> Fraction:
    return sum(Fraction(k) * coefficient for k, coefficient in enumerate(coeffs))


def fraction_to_decimal(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def decimal_polynomial(coeffs: Iterable[Fraction], t: Decimal) -> Decimal:
    value = Decimal(0)
    for coefficient in reversed(list(coeffs)):
        value = value * t + fraction_to_decimal(coefficient)
    return value


def laplace_decimal(probabilities: List[Fraction], t: Decimal) -> Decimal:
    value = Decimal(0)
    power = Decimal(1)
    for probability in probabilities:
        value += fraction_to_decimal(probability) * power
        power *= t
    return value


def decimal_ln(value: Decimal) -> Decimal:
    # Decimal.ln is available in current supported Python releases.
    try:
        return value.ln()
    except AttributeError:  # pragma: no cover - compatibility fallback
        import math

        return Decimal(str(math.log(float(value))))


def construct_witness(m: int) -> tuple[List[Fraction], Fraction, List[Fraction], List[Fraction]]:
    if m < 1:
        raise ValueError("m must be at least 1")

    # P_m(t) = (t-1)^2 product_{j=1}^m (t-2^{-j}), ascending coefficients.
    coeffs = [Fraction(1)]
    coeffs = multiply_polynomials(coeffs, [Fraction(-1), Fraction(1)])
    coeffs = multiply_polynomials(coeffs, [Fraction(-1), Fraction(1)])
    for j in range(1, m + 1):
        root = Fraction(1, 2**j)
        coeffs = multiply_polynomials(coeffs, [-root, Fraction(1)])

    uniform = Fraction(1, m + 3)
    max_abs = max(abs(value) for value in coeffs)
    epsilon = uniform / (2 * max_abs)

    p_plus = [uniform + epsilon * value for value in coeffs]
    p_minus = [uniform - epsilon * value for value in coeffs]
    return coeffs, epsilon, p_plus, p_minus


def verify_exact(m: int, coeffs: List[Fraction], p_plus: List[Fraction], p_minus: List[Fraction]) -> None:
    assert len(coeffs) == m + 3
    assert all(value > 0 for value in p_plus)
    assert all(value > 0 for value in p_minus)
    assert sum(p_plus) == Fraction(1)
    assert sum(p_minus) == Fraction(1)

    support = list(range(m + 3))
    mean_plus = sum(Fraction(x) * p for x, p in zip(support, p_plus))
    mean_minus = sum(Fraction(x) * p for x, p in zip(support, p_minus))
    assert mean_plus == mean_minus

    # Equivalent coefficient identities.
    assert evaluate_fraction_polynomial(coeffs, Fraction(1)) == 0
    assert derivative_at_one(coeffs) == 0

    for j in range(1, m + 1):
        t = Fraction(1, 2**j)
        assert evaluate_fraction_polynomial(coeffs, t) == 0
        l_plus = sum(p * (t**x) for x, p in zip(support, p_plus))
        l_minus = sum(p * (t**x) for x, p in zip(support, p_minus))
        assert l_plus == l_minus


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", type=int, default=2, help="number of tracked scores")
    parser.add_argument("--precision", type=int, default=80, help="decimal precision")
    args = parser.parse_args()

    coeffs, epsilon, p_plus, p_minus = construct_witness(args.m)
    verify_exact(args.m, coeffs, p_plus, p_minus)

    with localcontext() as ctx:
        ctx.prec = args.precision
        sqrt_two = Decimal(2).sqrt()
        t_missing = Decimal(1) / sqrt_two  # exp[-(log 2)/2]

        polynomial_at_missing = decimal_polynomial(coeffs, t_missing)
        l_plus_missing = laplace_decimal(p_plus, t_missing)
        l_minus_missing = laplace_decimal(p_minus, t_missing)
        delta_l = l_plus_missing - l_minus_missing

        log_two = decimal_ln(Decimal(2))
        lambda_missing = log_two / Decimal(2)
        q_plus_missing = -decimal_ln(l_plus_missing) / lambda_missing
        q_minus_missing = -decimal_ln(l_minus_missing) / lambda_missing

        # For a=1/2 and output lambda=log 2, the mean term cancels between witnesses.
        delta_future_q = (q_plus_missing - q_minus_missing) / Decimal(2)

    print(f"m = {args.m}")
    print("P_m coefficients (ascending):")
    print([str(value) for value in coeffs])
    print(f"epsilon = {epsilon}")
    print("p_plus =", [str(value) for value in p_plus])
    print("p_minus =", [str(value) for value in p_minus])
    print("exact tracked constraints: PASS")
    print("P_m(2^(-1/2)) ~=", polynomial_at_missing)
    print("L_plus(missing) - L_minus(missing) ~=", delta_l)
    print("future Q_log2 difference ~=", delta_future_q)

    if delta_l == 0 or delta_future_q == 0:
        raise RuntimeError("Unexpected zero omitted-transform or future-score difference")


if __name__ == "__main__":
    main()
