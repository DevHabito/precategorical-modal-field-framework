#!/usr/bin/env python3
"""Exact rational constants for a Mathlib-compatible A118 Taylor proof.

Use log cubic remainder z^4/(1-z) instead of the sharper alternating
z^4/4. Verifies that the originally published enormous final source
constant remains sufficient; does NOT prove analytic Mathlib lemmas.
"""
from fractions import Fraction as F
if not __debug__:
    raise RuntimeError("Python assertions must be enabled")

A_MAX=45
SHIFT_MAX=F(37,2)
Z_MAX=F(9,100)
X_MAX=F(1,1000)
ETA=A_MAX**2+2*SHIFT_MAX*A_MAX
B_MAG=F(4,3)*A_MAX**3+2*SHIFT_MAX*A_MAX**2
R_LOG=(F(8)*A_MAX**4)/(1-Z_MAX)+F(8,3)*SHIFT_MAX*A_MAX**3
assert ETA==3690 and B_MAG==196425
assert R_LOG<41_000_000
assert ETA+B_MAG*X_MAX+41_000_000*X_MAX**2 <4000
assert B_MAG+41_000_000*X_MAX<238_000
assert 4000+ETA==7690
EXP_REM=F(55,6)*4000**3
QUADRATIC_DIFF=F(238000*7690,2)
assert EXP_REM+QUADRATIC_DIFF+41_000_000 <590_000_000_000
LIN_REM=B_MAG+F(ETA**2,2)+590_000_000_000*X_MAX
assert LIN_REM<600_000_000
H=8**18
assert (46*H+768)*600_000_000<500_000_000_000*H
assert 510_000_000_000*H + 750*H*H*(12*99**3) < 100_000_000_000*H*H
print("PASS rational log cubic bound using z^4/(1-z)")
print("PASS |f-linear-jet| < 600000000*x^2 for both exponent ranges")
print("PASS original final C=10^11*(8^18)^2 remains sufficient")
print("Analytic series theorem still requires a kernel-replayed Lean module")
