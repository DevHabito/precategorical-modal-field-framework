#!/usr/bin/env python3
"""Exact rational consistency check for the stationary transform ladder.

This audit compares the stationary transform formula obtained from the
integer-shifted discrete Gaussian with the stationary triangular recurrence.
It does not use experimental data.
"""

from fractions import Fraction as F
import json

s = F(1, 2)          # s = exp(-a)
ratio = F(2, 3)      # ratio = Gamma0/GammaPlus

H = [F(1)]
checks = []

for k in range(1, 5):
    gaussian_formula = ratio ** k * s ** (-(k * k))
    recurrence_formula = ratio * s ** (-(2 * k - 1)) * H[k - 1]
    assert gaussian_formula == recurrence_formula
    H.append(gaussian_formula)
    checks.append({
        "k": k,
        "gaussian_formula": str(gaussian_formula),
        "triangular_recurrence": str(recurrence_formula),
        "equal": True,
    })

results = {
    "audit": "MULTIELECTRON_STATIONARY_TRANSFORM_CONSISTENCY_V1",
    "status": "PASS",
    "s_exp_minus_a": "1/2",
    "Gamma0_over_GammaPlus": "2/3",
    "checks": checks,
    "nonclaim": "Rational surrogate algebra check only; not experimental evidence."
}

print(json.dumps(results, indent=2))
