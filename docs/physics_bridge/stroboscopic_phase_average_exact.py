#!/usr/bin/env python3
"""Exact algebraic audit for phase-averaged stroboscopic recurrences.

This checks the algebraic mechanism with rational phase-specific affine/lower-
triangular monodromy maps that share the same diagonal multipliers. It does not
reproduce the sinusoidal integral or experimental data.
"""

from fractions import Fraction as F
import json

mu1 = F(2, 3)
mu2 = F(1, 4)

# Three phase sectors. The first-level intercepts differ by phase.
C1 = [F(1, 7), F(2, 7), F(4, 7)]

# 3x3 lower-triangular augmented monodromy matrices for (H0,H1,H2).
# Diagonal is common: 1, mu1, mu2. Off-diagonal entries vary by phase.
M = [
    [
        [F(1), F(0), F(0)],
        [C1[0], mu1, F(0)],
        [F(2, 11), F(1, 5), mu2],
    ],
    [
        [F(1), F(0), F(0)],
        [C1[1], mu1, F(0)],
        [F(3, 11), F(2, 5), mu2],
    ],
    [
        [F(1), F(0), F(0)],
        [C1[2], mu1, F(0)],
        [F(5, 11), F(3, 5), mu2],
    ],
]

X = [
    [F(1), F(1, 3), F(2, 5)],
    [F(1), F(1, 2), F(1, 5)],
    [F(1), F(2, 3), F(3, 5)],
]


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(3)) for i in range(3)]


def avg(values):
    return sum(values, F(0)) / len(values)


history = []
for n in range(7):
    history.append([
        avg([X[p][j] for p in range(3)])
        for j in range(3)
    ])
    X = [matvec(M[p], X[p]) for p in range(3)]

# H1: characteristic roots 1, mu1.
for n in range(5):
    h0 = history[n][1]
    h1 = history[n + 1][1]
    h2 = history[n + 2][1]
    assert h2 - (1 + mu1) * h1 + mu1 * h0 == 0

# H2: characteristic roots 1, mu1, mu2.
s1 = 1 + mu1 + mu2
s2 = mu1 + mu2 + mu1 * mu2
s3 = mu1 * mu2
for n in range(4):
    x0 = history[n][2]
    x1 = history[n + 1][2]
    x2 = history[n + 2][2]
    x3 = history[n + 3][2]
    assert x3 - s1 * x2 + s2 * x1 - s3 * x0 == 0

results = {
    "audit": "PHASE_AVERAGED_STROBOSCOPIC_CLOSURE_V1",
    "status": "PASS",
    "mu1": str(mu1),
    "mu2": str(mu2),
    "phase_count": 3,
    "H1_three_point_recurrence": True,
    "H2_four_point_recurrence": True,
    "nonclaim": "Algebraic monodromy regression only; not experimental evidence."
}
print(json.dumps(results, indent=2))
