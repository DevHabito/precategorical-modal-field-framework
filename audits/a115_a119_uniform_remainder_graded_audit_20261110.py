#!/usr/bin/env python3
"""Exact polynomial cancellation audit of the reduced A115 adjacent factor.

This checks weighted polynomial identities. Analytic uniform bounds and Taylor
remainder are justified separately in the research note, not by these asserts.
Requires SymPy; the working-container run used SymPy 1.14.0.
"""
import sympy as S

x, q, u, s, tau, beta = S.symbols('x q u s tau beta', real=True)
U, V, W, T, K = S.symbols('U V W T K', real=True)
vb, vs, vt = S.symbols('vb vs vt', real=True)
A = {beta: (1 + vb) / 2, s: (1 + vs) / 2, tau: (1 + vt) / 2}
v = {beta: vb, s: vs, tau: vt}
Hbeta = S.Rational(1, 2) + u * U
Hs = S.Rational(1, 2) + u * V

def factor_E(q0, bk, sk, tk):
    power = {beta: bk, s: sk, tau: tk}
    B = {z: power[z] - 1 + q0 * (1 - v[z]) for z in (beta, s, tau)}
    dB = {z: (z - 1) * power[z] + x * (1 - v[z]) for z in (beta, s, tau)}
    return (
        (A[tau] * B[beta] - Hbeta * B[tau]) * dB[s]
        + (-A[tau] * dB[beta] + Hbeta * dB[tau]) * B[s]
        + (-B[beta] * dB[tau] + B[tau] * dB[beta]) * Hs
    )

# Exact model-level substitutions: beta^k=uK, s^k=uW, tau^k=uT,
# v_r=r^M, q=k/M and x=1/M.
J = S.expand(
    factor_E(q, u * K, u * W, u * T)
    - factor_E(q + x, u * beta * K, u * s * W, u * tau * T) / tau
)
polynomial = S.Poly(J, u, vb, vs, vt, domain="EX")
items = polynomial.terms()
weight = lambda exp: exp[0] + 2 * sum(exp[1:])
assert all(weight(exp) >= 2 for exp, coeff in items)

core = S.expand(
    sum(coeff * u ** exp[0] for exp, coeff in items
        if weight(exp) == 2 and exp[1:] == (0, 0, 0))
)
assert S.simplify(
    core / u ** 2
    - S.expand(J.subs({vb: 0, vs: 0, vt: 0})).coeff(u, 2)
) == 0

closed = (
    (1 - s) * (tau - s) * W / 2
    + x * (1 - tau) * (U - V)
    + U * (W / (T * tau)) * (
        (s - tau) * (s - 1) * (q - 1) + x * (s ** 2 - 2 * s + tau)
    )
)
assert S.cancel((core / (u ** 2 * T)).subs(K, 0) - closed) == 0
assert all(
    not (weight(exp) == 2 and exp[1:] != (0, 0, 0))
    for exp, coeff in items
)
remainder = S.Poly(S.expand(J - u ** 2 * T * closed),
                   u, vb, vs, vt, domain="EX")
for exp, coeff in remainder.terms():
    w = weight(exp)
    assert w >= 3 or (w == 2 and S.expand(coeff).subs(K, 0) == 0)

print("PASS exact J polynomial and weighted-degree cancellation")
print("PASS degree-2 dominant expression, all remaining terms suppressed")
print("Full monomial groups:", len(items))
print("Remainder monomial groups:", len(remainder.terms()))
print("NOT a proof of analytic bounds, LP optimality, novelty or Lean replay")
