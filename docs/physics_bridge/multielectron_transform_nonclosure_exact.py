#!/usr/bin/env python3
"""Exact witness audit for Bridge 1B.

This script checks the four-state algebraic witness used in the physical
transform-nonclosure note. It does not use experimental data.
"""

from fractions import Fraction as F
import json


def mean(p):
    return sum(F(n) * p[n] for n in range(len(p)))


def G(p, r):
    return sum(p[n] * (r ** n) for n in range(len(p)))


z = F(1, 2)
y = F(3, 4)
eps = F(1, 20)

v = [
    -z,
    2*z + 1,
    -z - 2,
    F(1),
]

base = [F(1,4)] * 4
p_plus = [base[i] + eps*v[i] for i in range(4)]
p_minus = [base[i] - eps*v[i] for i in range(4)]

assert all(x > 0 for x in p_plus)
assert all(x > 0 for x in p_minus)
assert sum(p_plus) == 1
assert sum(p_minus) == 1

assert mean(p_plus) == mean(p_minus) == F(3,2)
assert G(p_plus,z) == G(p_minus,z) == F(15,32)

gy_plus = G(p_plus,y)
gy_minus = G(p_minus,y)
assert gy_plus == F(219,320)
assert gy_minus == F(437,640)
assert gy_plus - gy_minus == F(1,640)

# Direct perturbation identities.
assert sum(v) == 0
assert sum(F(n)*v[n] for n in range(4)) == 0
assert sum(v[n]*(z**n) for n in range(4)) == 0
assert sum(v[n]*(y**n) for n in range(4)) == (y-1)**2*(y-z)

results = {
    "bridge": "MULTIELECTRON_TRANSFORM_NONCLOSURE_V1",
    "status": "PASS",
    "z": "1/2",
    "y": "3/4",
    "epsilon": "1/20",
    "p_plus": [str(x) for x in p_plus],
    "p_minus": [str(x) for x in p_minus],
    "mean_both": "3/2",
    "G_z_both": "15/32",
    "G_y_plus": "219/320",
    "G_y_minus": "437/640",
    "G_y_difference": "1/640",
    "nonclaims": [
        "This is an exact algebraic witness, not experimental data.",
        "The chosen rational z and y are not fitted to the published device parameters.",
        "No novelty claim is made for transform nonclosure in birth-death processes."
    ]
}

print(json.dumps(results, indent=2))
