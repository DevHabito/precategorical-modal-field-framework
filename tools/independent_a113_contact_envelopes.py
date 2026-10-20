#!/usr/bin/env python3
"""Independent exact checks of universal A113 contact-envelope constants.

The *proof* of the uniform conclusions uses monotonicity and integer
ceiling/parity algebra, documented separately. This script validates the
rational endpoint premises and probes representative instances. It does
not substitute sampled M,s pairs for universal quantification.
"""

from __future__ import annotations

from fractions import Fraction


SOURCE_MIN = Fraction(129, 1000)
SOURCE_MAX = Fraction(133, 1000)
LOWER_C = Fraction(16923, 100000)
UPPER_C = Fraction(17180, 100000)
MIN_SIZE = 521
BETA = Fraction(1, 8)


def rational_log_contact_bound(source: Fraction, bound: Fraction) -> int:
    """Sign(c(source)-bound) exactly, via 2^q * source^(2p) vs 1."""
    numerator = bound.numerator
    denominator = bound.denominator
    quantity = 2**denominator * source.numerator ** (2 * numerator)
    threshold = source.denominator ** (2 * numerator)
    return (quantity > threshold) - (quantity < threshold)


def contact_ceil(size: int, source: Fraction) -> int:
    """The exact integer b satisfying s^(2b) <= 2^-M < s^(2(b-1))."""
    target = Fraction(1, 2**size)
    low, high = 0, size
    while low < high:
        midpoint = (low + high) // 2
        if source ** (2 * midpoint) <= target:
            high = midpoint
        else:
            low = midpoint + 1
    return low


def main() -> None:
    assert rational_log_contact_bound(SOURCE_MIN, LOWER_C) == 1
    assert rational_log_contact_bound(SOURCE_MAX, UPPER_C) == -1
    assert MIN_SIZE * LOWER_C > 88
    assert MIN_SIZE * (Fraction(1, 2) - 3 * LOWER_C) < -4
    assert (
        Fraction(MIN_SIZE - 1, 2) - 5 - (MIN_SIZE * UPPER_C + 1)
    ) > 0
    assert Fraction(1, 2) > Fraction(49, 100)  # 1/sqrt(2) > 7/10.

    tested = 0
    for size in (521, 522, 561, 661, 821, 1000, 2049, 4097):
        h = size // 2
        unit = Fraction(1, 2**h)
        for source in (SOURCE_MIN, Fraction(131, 1000), SOURCE_MAX):
            b = contact_ceil(size, source)
            assert b >= 89
            assert b + 3 <= h - 2
            ratio = source**b / unit
            assert Fraction(7, 10) * source < ratio <= 1
            beta_ratio = BETA**b / unit
            assert beta_ratio <= Fraction(1, 32)
            assert source ** (2 * b) <= Fraction(1, 2**size)
            assert source ** (2 * (b - 1)) > Fraction(1, 2**size)
            tested += 1

    print("A113 contact envelope PASS: exact rational endpoint log-bracketing")
    print("A113 contact envelope PASS: uniform inequality gates at M >= 521")
    print(
        "A113 contact envelope PASS: exact b, s^b/U and beta^b/U "
        f"for {tested} independently selected finite controls"
    )


if __name__ == "__main__":
    main()
