#!/usr/bin/env python3
"""Exact rational audits of constants in A115 finite-power tail bounds.

This checks arithmetic gates, not the analytic inequalities or Lean lemmas.
Requires only Python's standard library; never use python -O.
"""
from fractions import Fraction as F

if not __debug__:
    raise RuntimeError("Assertions were disabled.")

BETA = F(1, 8)
S_MIN, S_MAX = F(129, 1000), F(133, 1000)
DELTA = F(1, 1875)
RHO = F(99, 100)
X_MAX = F(1, 1000)
ALPHA_MAX = F(45)
H = 8 ** 18

def main():
    # Frozen collision and positivity range for every M >= 1000.
    tau_max = S_MAX * (1 + 2 * ALPHA_MAX * X_MAX)
    assert BETA < S_MIN < tau_max < F(3, 20)
    assert 2 * ALPHA_MAX * X_MAX <= F(9, 100)
    assert F(3, 20) < RHO ** 2
    assert F(125, 129) < RHO ** 2
    assert F(2, 5) / RHO < F(1, 2)

    # Central-response bound: |U|,|V| < 3 using L_h(tau)>=7*tau/10.
    assert F(10, 7) + 2 * DELTA + 1 + F(1, 2) < 3

    # Elementary normalization bounds: 1/(2*tau*T) < 4, T >= 1.
    assert F(1, 2 * S_MIN) < 4
    assert H >= 1

    # Coefficient consequences of 0 <= x <= 1/1000, 0 <= q <= 1,
    # 0 <= v_a <= u^2 <= 1, and |K|,|W|,|T| <= H, |U|,|V| <= 3.
    assert 18 * H + 2 * X_MAX * H + 24 * X_MAX < 19 * H
    assert H * H + (24 + 12 * X_MAX) * H < 26 * H * H

    # The final geometric coefficient explicitly absorbs x and u^2 <= u.
    final = 4 * F(100, 99) * (2 * X_MAX + 19 * H + 26 * H * H)
    assert final < 200 * H * H
    print("PASS exact rational source/target and central-response constant gates")
    print("PASS bounds for C0, C1, C2 and normalized geometric coefficient")
    print("H=8^18 =", H)
    print("C_full=200*H^2 =", 200 * H * H)
    print("NOT a Lean proof or a test of every analytic inequality")

if __name__ == "__main__":
    main()
