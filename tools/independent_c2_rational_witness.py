#!/usr/bin/env python3
"""Exact constructive MF-R049 control without historical audit imports.

This does not establish theorem novelty, nor does it use logarithm tolerances.
"""

from __future__ import annotations

from fractions import Fraction


PLUS = (Fraction(15, 64), Fraction(22, 64), Fraction(7, 64), Fraction(20, 64))
MINUS = (Fraction(17, 64), Fraction(10, 64), Fraction(25, 64), Fraction(12, 64))


def moment(weights: tuple[Fraction, ...], t: Fraction) -> Fraction:
    return sum(weight * t**index for index, weight in enumerate(weights))


def mean(weights: tuple[Fraction, ...]) -> Fraction:
    return sum(weight * index for index, weight in enumerate(weights))


def polynomial_difference(t: Fraction) -> Fraction:
    return Fraction(1, 8) * (t - 1) ** 2 * (t - Fraction(1, 4))


def main() -> None:
    for weights in (PLUS, MINUS):
        assert all(weight > 0 for weight in weights)
        assert sum(weights) == 1
        assert mean(weights) == Fraction(3, 2)
        assert moment(weights, Fraction(1, 4)) == Fraction(85, 256)

    for t in (
        Fraction(-3, 2), Fraction(0), Fraction(1, 8),
        Fraction(1, 4), Fraction(1, 2), Fraction(1),
        Fraction(5, 4), Fraction(7, 2),
    ):
        assert moment(PLUS, t) - moment(MINUS, t) == polynomial_difference(t)

    plus_rescaled = moment(PLUS, Fraction(1, 2))
    minus_rescaled = moment(MINUS, Fraction(1, 2))

    assert plus_rescaled == Fraction(121, 256)
    assert minus_rescaled == Fraction(119, 256)
    assert plus_rescaled - minus_rescaled == Fraction(1, 128)
    assert plus_rescaled > minus_rescaled > 0

    # The centered contraction sends q_k = k to q'_k = 3/4 + k/2.
    # For lambda=2*log(2), its exponential moment has the exact form
    #   exp(-3*lambda/4) * moment(weights, 1/2).
    # The common exponential factor is strictly positive; no numerical
    # approximation to the logarithm or exponential is required to infer
    # distinct next entropic scores.
    print("MF-R049 PASS: normalized positive weights with equal means")
    print("MF-R049 PASS: initial moments = 85/256 at t=1/4")
    print("MF-R049 PASS: rescaled moments = 121/256 and 119/256")
    print("MF-R049 PASS: exact difference = 1/128")
    print("MF-R049 PASS: polynomial identity and sign controls")


if __name__ == "__main__":
    main()
