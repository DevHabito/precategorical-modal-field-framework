#!/usr/bin/env python3
"""Exact symmetric stochastic sector-selection audit.

States:
    0 = neutral
    + = positive sector
    - = negative sector

The law is exactly invariant under + <-> -.
Every trajectory selects a sign after one step, while the ensemble remains
exactly symmetric.

Fraction arithmetic only.
"""

from fractions import Fraction as F
import json

K = [
    [F(0), F(1, 2), F(1, 2)],
    [F(0), F(1),    F(0)],
    [F(0), F(0),    F(1)],
]

pi0 = [F(1), F(0), F(0)]


def step(p):
    return [
        sum(p[i] * K[i][j] for i in range(3))
        for j in range(3)
    ]


def flip(p):
    return [p[0], p[2], p[1]]


def odd_polarity(p):
    return p[1] - p[2]


def selected_mass(p):
    return p[1] + p[2]


# Kernel equivariance under + <-> -.
perm = [0, 2, 1]
for i in range(3):
    for j in range(3):
        assert K[perm[i]][perm[j]] == K[i][j]

rows = []
p = pi0

for n in range(9):
    assert p == flip(p)
    assert odd_polarity(p) == 0

    if n == 0:
        assert selected_mass(p) == 0
    else:
        assert p == [F(0), F(1, 2), F(1, 2)]
        assert selected_mass(p) == 1

    rows.append({
        "n": n,
        "distribution": [str(x) for x in p],
        "odd_polarity": str(odd_polarity(p)),
        "selected_sector_mass": str(selected_mass(p)),
    })

    p = step(p)

# Explicit trajectory probabilities.
trajectory_probabilities = {
    "0,+,+,+,...": "1/2",
    "0,-,-,-,...": "1/2",
}

result = {
    "audit": "SYMMETRIC_STOCHASTIC_SECTOR_SELECTION_V1",
    "status": "PASS",
    "kernel": [[str(x) for x in row] for row in K],
    "symmetry": "swap + and -; fix 0",
    "rows": rows,
    "trajectory_probabilities": trajectory_probabilities,
    "exact_conclusions": [
        "The ensemble distribution is symmetry-invariant at every checked step.",
        "The reversal-odd ensemble polarity is exactly zero.",
        "All probability mass leaves the neutral state after one update.",
        "Each individual trajectory remains in one selected sector thereafter.",
        "The two opposite realized sectors have equal probability."
    ],
    "nonclaims": [
        "This finite witness is not a new theorem about thermodynamic spontaneous symmetry breaking.",
        "No physical temporal interpretation is assigned to the + and - sectors.",
        "The update index is already supplied and is not derived."
    ]
}

print(json.dumps(result, indent=2))
