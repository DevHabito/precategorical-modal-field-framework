#!/usr/bin/env python3
"""Independently implement A119's published rational interval sign certificates.

This checks the displayed critical-substitution formula and cutoff bounds.
It does not independently prove the upstream A115-A118 analytic identities.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class RationalInterval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("The lower interval endpoint exceeds the upper endpoint.")

    def __add__(self, other: object) -> RationalInterval:
        right = as_interval(other)
        return RationalInterval(self.lower + right.lower, self.upper + right.upper)

    __radd__ = __add__

    def __neg__(self) -> RationalInterval:
        return RationalInterval(-self.upper, -self.lower)

    def __sub__(self, other: object) -> RationalInterval:
        return self + (-as_interval(other))

    def __rsub__(self, other: object) -> RationalInterval:
        return as_interval(other) - self

    def __mul__(self, other: object) -> RationalInterval:
        right = as_interval(other)
        products = (
            self.lower * right.lower,
            self.lower * right.upper,
            self.upper * right.lower,
            self.upper * right.upper,
        )
        return RationalInterval(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> RationalInterval:
        right = as_interval(other)
        if right.lower <= 0 <= right.upper:
            raise ZeroDivisionError("An interval denominator contains zero.")
        reciprocal = RationalInterval(1 / right.upper, 1 / right.lower)
        return self * reciprocal

    def __rtruediv__(self, other: object) -> RationalInterval:
        return as_interval(other) / self

    def __pow__(self, exponent: int) -> RationalInterval:
        if exponent < 0:
            return as_interval(1) / self ** (-exponent)
        if exponent == 0:
            return as_interval(1)
        if self.lower < 0:
            raise ValueError("This audit only takes powers of positive intervals.")
        return RationalInterval(self.lower**exponent, self.upper**exponent)


def as_interval(value: object) -> RationalInterval:
    if isinstance(value, RationalInterval):
        return value
    if isinstance(value, (int, Fraction)):
        exact = Fraction(value)
        return RationalInterval(exact, exact)
    raise TypeError(f"Unsupported interval operand: {type(value).__name__}")


def critical_second_order_bound(
    source: RationalInterval,
    alpha: RationalInterval,
    odd_parity: bool,
    deficit: int,
) -> RationalInterval:
    """Evaluate A118 Xi after A119's exact critical substitution."""
    beta = Fraction(1, 8)
    delta = Fraction(1, 1875)
    parity_shift = Fraction(1, 2) if odd_parity else Fraction(0)
    parity_mass = (1 + source) / 2 if odd_parity else as_interval(1)

    b_value = beta / source + 2 * delta
    c_value = 1 - beta / source - 4 * delta
    a_value = parity_mass * (1 - b_value)
    d_value = source ** (2 - deficit) - parity_mass * b_value
    critical_exponential = parity_mass * c_value / (
        a_value + alpha * d_value
    )

    source_sum = 1 - critical_exponential - 2 * delta
    target_sum = 1 - 2 * delta
    eta_h = alpha**2 + 2 * parity_shift * alpha
    eta_k = alpha**2 + 2 * alpha * (parity_shift + deficit - 1)

    beta_first = (
        2 * parity_shift * alpha * source * b_value
        - 2 * parity_mass * alpha * beta / source
    )
    source_first = (
        2 * parity_shift * alpha * source * target_sum
        - 2 * parity_mass * alpha
        - parity_mass * critical_exponential * eta_h
    )
    source_bracket = 2 * alpha * (
        1 + (1 - source) * (alpha + 2 - parity_shift - deficit)
    )

    main_term = (
        (1 - source) * alpha * source ** (2 - deficit)
        * critical_exponential * eta_h
    )
    source_term = critical_exponential * (
        parity_mass * b_value * source_bracket
        - (1 - source) * (alpha + 1)
        * (beta_first + parity_mass * b_value * eta_k)
    )
    target_term = (
        (1 - source) * (beta_first - source_first)
        - 2 * alpha * source * parity_mass * (b_value - source_sum)
    )
    return main_term + source_term + target_term


def validate_log_enclosure() -> None:
    """Certify 2 < -log(s) < 21/10 on the source interval."""
    def exponential_partial(value: Fraction, degree: int) -> tuple[Fraction, Fraction]:
        term = Fraction(1)
        total = term
        for index in range(1, degree + 1):
            term = term * value / index
            total += term
        return total, term

    lower_exp, _ = exponential_partial(Fraction(21, 10), 12)
    upper_partial, final_term = exponential_partial(Fraction(2), 15)
    first_omitted = final_term * 2 / 16
    upper_exp = upper_partial + first_omitted / (1 - Fraction(2, 17))

    # Term ratios beyond degree 15 are at most 2/17, giving a
    # rigorous geometric-series upper bound on the exponential tail.
    assert upper_exp < Fraction(1000, 133)
    assert lower_exp > Fraction(1000, 129)
    print("A119 logarithm enclosure PASS: 2 < -log(s) < 21/10")


def validate_cutoff_bounds() -> None:
    lower_source = Fraction(129, 1000)
    upper_source = Fraction(133, 1000)
    upper_c = 1 - Fraction(1, 8) / upper_source - Fraction(4, 1875)
    upper_b = Fraction(1, 8) / lower_source + Fraction(2, 1875)
    upper_log = Fraction(21, 10)

    even_deficit = 13
    even_n = even_deficit + 1
    even_lower_bound = (
        -upper_c + 2 * even_n * lower_source**3
        - even_n * upper_log * upper_b * upper_source**even_n
    )
    assert even_lower_bound > 0
    assert Fraction(even_n + 1, even_n) * upper_source < 1

    odd_n = Fraction(43, 2)
    upper_odd_mass = Fraction(567, 1000)
    odd_lower_bound = (
        -upper_odd_mass * upper_c
        + odd_n * 2 * lower_source**3 * Fraction(359, 1000)
        - upper_odd_mass * odd_n * upper_log * upper_b
        * upper_source**21 * Fraction(365, 1000)
    )
    assert odd_lower_bound > 0
    assert Fraction(45, 43) * upper_source < 1
    print("A119 cutoff bounds PASS: no possible critical cells for even r>=13, odd r>=20")


def validate_interval_cover(odd_parity: bool) -> None:
    source_min = Fraction(129, 1000)
    source_max = Fraction(133, 1000)
    parity_shift = Fraction(1, 2) if odd_parity else Fraction(0)
    final_deficit = 20 if odd_parity else 13
    subdivisions = 16
    worst_lower: Fraction | None = None
    checked_boxes = 0

    for deficit in range(4, final_deficit):
        alpha_min = 2 * (deficit + parity_shift)
        alpha_max = Fraction(21, 10) * (deficit + 1 + parity_shift)
        for source_index in range(subdivisions):
            source = RationalInterval(
                source_min + (source_max - source_min) * source_index / subdivisions,
                source_min + (source_max - source_min) * (source_index + 1) / subdivisions,
            )
            for alpha_index in range(subdivisions):
                alpha = RationalInterval(
                    alpha_min + (alpha_max - alpha_min) * alpha_index / subdivisions,
                    alpha_min + (alpha_max - alpha_min) * (alpha_index + 1) / subdivisions,
                )
                enclosure = critical_second_order_bound(
                    source, alpha, odd_parity, deficit
                )
                if enclosure.lower <= 0:
                    raise AssertionError(
                        (odd_parity, deficit, source_index, alpha_index, enclosure)
                    )
                checked_boxes += 1
                if worst_lower is None or enclosure.lower < worst_lower:
                    worst_lower = enclosure.lower

    expected_boxes = 4096 if odd_parity else 2304
    assert checked_boxes == expected_boxes
    assert worst_lower is not None and worst_lower > 0
    parity = "odd" if odd_parity else "even"
    print(f"A119 {parity} PASS: {checked_boxes} exact interval boxes; minimum={worst_lower}")


def main() -> None:
    validate_log_enclosure()
    validate_cutoff_bounds()
    validate_interval_cover(False)
    validate_interval_cover(True)


if __name__ == "__main__":
    main()
