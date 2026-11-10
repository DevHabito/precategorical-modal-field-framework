#!/usr/bin/env python3
"""Exact rational A117 cell-entry and A119 tail-cutoff checks.

Finite calculations establish strict margins. The monotonic extension from
cutoff to infinity is an analytical argument in the accompanying note.
"""
from fractions import Fraction as F

if not __debug__:
    raise RuntimeError("Python -O disables assertions")

def negative_log_bracket(x, terms=80):
    assert 0 < x < 1
    a = (1 - x) / (1 + x)
    t, partial = a, F(0)
    for j in range(terms):
        partial += 2 * t / (2 * j + 1)
        t *= a * a
    rem = 2 * t / ((2 * terms + 1) * (1 - a * a))
    return partial, partial + rem

s0, s1 = F(129, 1000), F(133, 1000)
beta, delta = F(1, 8), F(1, 1875)
L_at_s1 = negative_log_bracket(s1)
L_at_s0 = negative_log_bracket(s0)
assert F(2) < L_at_s1[0]
assert L_at_s0[1] < F(21, 10)

Bmax = beta / s0 + 2 * delta
Cmax = 1 - beta / s1 - 4 * delta
assert 0 < Cmax < F(3, 50) and 0 < Bmax < 1
even_entry = -F(3, 50) + 8 * s0 ** 2 - F(42, 5) * s1 ** 4
odd_entry = (
    -F(567, 1000) * F(3, 50) + 9 * s0 ** 2 * F(359, 1000)
    - F(567, 1000) * F(9, 2) * F(21, 10)
    * s1 ** 4 * F(365, 1000)
)
assert even_entry > 0 and odd_entry > 0

even_tail = (
    -Cmax + 14 * 2 * s0 ** 3
    - 14 * F(21, 10) * Bmax * s1 ** 14
)
assert F(359, 1000) ** 2 < s0 and s1 < F(365, 1000) ** 2
odd_tail = (
    -F(567, 1000) * Cmax
    + F(43, 2) * 2 * s0 ** 3 * F(359, 1000)
    - F(567, 1000) * F(43, 2) * F(21, 10)
    * Bmax * s1 ** 21 * F(365, 1000)
)
even_decay_ratio = F(15, 14) * s1
odd_decay_ratio = F(45, 43) * s1
assert even_tail > 0 and odd_tail > 0
assert 0 < even_decay_ratio < 1 and 0 < odd_decay_ratio < 1

print("PASS: 2 < -log(s) < 21/10, source interval")
print("PASS: strict A117 cell-entry margins, even/odd")
print("PASS: exact A119 tail margins and geometric-decay ratios")
print("even entry:", even_entry)
print("odd entry:", odd_entry)
print("even tail:", even_tail)
print("odd tail:", odd_tail)
print("ratios:", even_decay_ratio, odd_decay_ratio)
print("NOT a replacement for full A119 Xi positivity or Lean")
