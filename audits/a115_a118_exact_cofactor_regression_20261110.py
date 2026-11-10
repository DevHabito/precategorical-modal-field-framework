#!/usr/bin/env python3
"""Independent exact finite-M regression for the A115 adjacent cofactor.

Standard library only. Computes original finite powers, then independently
reconstructs the zero-full-power auxiliary model and its explicit remainder.
A PASS is evidence for six finite inputs, not a uniform asymptotic theorem.
"""
from fractions import Fraction as Q

if not __debug__:
    raise RuntimeError("Do not disable assertions in the exact audit.")

BETA = Q(1, 8)
DELTA = Q(1, 1875)

def inspect_case(M, parity, s, alpha, r):
    assert M % 2 == parity and M >= 2
    h = M // 2
    k = h - r + 1
    assert 1 <= k <= h - 2
    tau = s * (1 + 2 * alpha / M)
    assert 0 < BETA < s < tau < 1
    u = tau ** h
    scale = lambda a: (1 + a) / 2 if parity else Q(1)
    L = lambda a: a - h * a ** h + (h - 1) * a ** (h + 1)
    assert L(tau) > 0

    def A(a):
        return (1 + a ** M) / 2

    def H(a, band_sign):
        C = L(a) / L(tau)
        D = scale(a) * a ** h - scale(tau) * u * C
        return A(a) - D + band_sign * 2 * DELTA * scale(tau) * u

    Hb, Hs = H(BETA, 1), H(s, -1)

    def E(j, include_full_powers):
        v = lambda a: a ** M if include_full_powers else Q(0)
        B = lambda a: a ** j - 1 + Q(j, M) * (1 - v(a))
        dB = lambda a: (a - 1) * a ** j + (1 - v(a)) / M
        At = (1 + v(tau)) / 2
        return ((At * B(BETA) - Hb * B(tau)) * dB(s)
                + (-At * dB(BETA) + Hb * dB(tau)) * B(s)
                + (-B(BETA) * dB(tau) + B(tau) * dB(BETA)) * Hs)

    # The exact finite comparison must use tau^-1, not a frozen factor 2.
    full = E(k, True) - E(k + 1, True) / tau
    auxiliary = E(k, False) - E(k + 1, False) / tau
    assert full != auxiliary, "Finite full-length power terms were silently dropped."
    assert full != E(k, True) - E(k + 1, True), "Missing tau^-1 went unnoticed."

    x, theta = Q(1, M), Q(k, M)
    K, W, T = BETA ** k / u, s ** k / u, tau ** k / u
    U, V = (Hb - Q(1, 2)) / u, (Hs - Q(1, 2)) / u
    core = (tau * T * (1 - s) * (tau - s) * W
            + 2 * tau * T * x * (1 - tau) * (U - V)
            + 2 * U * W * ((s - tau) * (s - 1) * (theta - 1)
                           + x * (s * s - 2 * s + tau)))
    beta_tail = (-tau * T * (BETA - 1) * (BETA - tau)
                 - 2 * V * ((theta - 1) * (BETA - 1) * (BETA - tau)
                            + x * (BETA * BETA - 2 * BETA + tau))
                 - W * (s - BETA) * (BETA * s - tau))
    cubic_tail = 2 * tau * T * (
        -K * V * (BETA - 1) * (BETA - tau)
        + U * W * (s - 1) * (s - tau))

    assert 2 * tau * auxiliary == (
        u * u * core + u * u * K * beta_tail + u ** 3 * cubic_tail
    ), "Exact cofactor polynomial cancellation failed."

    # Exact mixed finite-power cancellation, with arbitrary positive M-th
    # power values kept and u=0 used as a FORMAL polynomial specialization.
    vb, vs, vt = BETA ** M, s ** M, tau ** M
    def E_zero_u(j):
        B = lambda vv: -1 + Q(j, M) * (1 - vv)
        dB = lambda vv: x * (1 - vv)
        At = (1 + vt) / 2
        half = Q(1, 2)
        return ((At * B(vb) - half * B(vt)) * dB(vs)
                + (-At * dB(vb) + half * dB(vt)) * B(vs)
                + (-B(vb) * dB(vt) + B(vt) * dB(vb)) * half)
    assert 2 * (tau * E_zero_u(k) - E_zero_u(k + 1)) == (
        x * (tau - 1) * vt * (vs - vb)
    ), "Mixed full-power u=0 correction failed."

    assert u > 0 and K > 0 and T > 0
    return "+" if full > 0 else "-" if full < 0 else "zero"

CASES = (
    (60, 0, Q(129, 1000), Q(8), 4),
    (61, 1, Q(133, 1000), Q(9), 4),
    (200, 0, Q(131, 1000), Q(11), 7),
    (201, 1, Q(129, 1000), Q(16), 7),
    (521, 1, Q(129, 1000), Q(9), 12),
    (1000, 0, Q(133, 1000), Q(45), 19),
)

def main():
    for M, parity, s, alpha, r in CASES:
        sign = inspect_case(M, parity, s, alpha, r)
        print(f"PASS M={M}, parity={'odd' if parity else 'even'}, r={r}; "
              f"finite J sign={sign}")
    print("PASS 6/6 exact finite A115 cofactor reconstruction controls")
    print("PASS explicit beta-channel/cubic and mixed finite-M power identities")
    print("PASS negative controls: dropping full powers or tau^-1 changes J")
    print("NOT a uniform remainder bound, global F3 optimization, or Lean proof")

if __name__ == "__main__":
    main()
