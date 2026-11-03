#!/usr/bin/env python3
"""Exact rational budget for the proposed A113 universal Delta bound.

This checks scalar consequences of explicitly stated *uniform premises*.
It does NOT establish those premises in Lean or prove the full Delta theorem.
"""

from fractions import Fraction as F

BETA = F(1, 8)
LOWER_SOURCE = F(129, 1000)
UPPER_SOURCE = F(133, 1000)
MIN_DELTA = F(43, 10000)
MAX_DELTA = F(7, 500)
DENOMINATOR_FLOOR = F(999, 1000)
HIGH_POWER_CAP = F(1, 1000000)

assert 3**14 > 1000000
assert F(16, 2**15) < F(1, 1000)
assert BETA < LOWER_SOURCE < UPPER_SOURCE < F(1, 6)

# Under d >= 999/1000, d <= 1, 0 <= hU/d <= 1/3,
# 0 <= (h-1)U/d <= 1/3, and each normalized power difference
# Q=(s^h-beta^h)/U, R=(s^(h+1)-beta^(h+1))/U <= 10^-6,
# P=(s^M-beta^M)/(2U) <= 0.5*10^-6:
even_lower = (
    2 * (LOWER_SOURCE-BETA) - F(4, 1875)
    - F(5, 3) * HIGH_POWER_CAP
)
even_upper = (
    2 * (UPPER_SOURCE-BETA) / DENOMINATOR_FLOOR
    - F(4, 1875)
    + (F(1, 2) + F(2, 3)) * HIGH_POWER_CAP
)
odd_lower = (
    F(3, 2) * (LOWER_SOURCE-BETA) - F(4, 2500)
    - (F(1, 1) + F(1, 2)) * HIGH_POWER_CAP
)
odd_upper = (
    F(3, 2) * (UPPER_SOURCE-BETA) / DENOMINATOR_FLOOR
    - F(4, 2500)
    + F(1, 2) * HIGH_POWER_CAP
)
assert MIN_DELTA < even_lower < even_upper < MAX_DELTA
assert MIN_DELTA < odd_lower < odd_upper < MAX_DELTA

# Negative controls: the earlier 3/4 denominator cap is inadequate
# for the even upper claim; allowing a much looser Q destroys the odd
# lower margin. The regression must detect these insufficient budgets.
old_even_upper = (
    2 * (UPPER_SOURCE-BETA) / F(3, 4)
    - F(4, 1875)
    + (F(1, 2) + F(2, 3)) * HIGH_POWER_CAP
)
loose_odd_lower = (
    F(3, 2) * (LOWER_SOURCE-BETA) - F(4, 2500)
    - (F(1) + F(1, 2))*F(1, 1000)
)
assert old_even_upper > MAX_DELTA
assert loose_odd_lower < MIN_DELTA

print("A113 exact rational Delta error-budget gates: PASS")
for name, value, margin in (
    ("even lower", even_lower, even_lower - MIN_DELTA),
    ("even upper", even_upper, MAX_DELTA - even_upper),
    ("odd lower", odd_lower, odd_lower - MIN_DELTA),
    ("odd upper", odd_upper, MAX_DELTA - odd_upper),
):
    print(f"{name}: bound={value}; strictly positive margin={margin}")
print("Two deliberately inadequate-bound negative controls: PASS")
print("SCOPE: conditional rational consequences; full Lean hypotheses open")
