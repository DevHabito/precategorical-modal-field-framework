#!/usr/bin/env python3
"""Exact boundary-state symmetry-selection audit.

Uses Fraction arithmetic. The transition law is reflection symmetric while
left/right boundary preparations select opposite signs of the centered
relaxation mode.

This is not a derivation of time or a thermodynamic Past Hypothesis model.
"""

from fractions import Fraction as F
import json

K = [
    [F(3,4), F(1,4), F(0)],
    [F(1,4), F(1,2), F(1,4)],
    [F(0),   F(1,4), F(3,4)],
]

left = [F(1), F(0), F(0)]
right = [F(0), F(0), F(1)]
stationary = [F(1,3)] * 3
positions = [F(0), F(1), F(2)]


def step(p):
    return [
        sum(p[i] * K[i][j] for i in range(3))
        for j in range(3)
    ]


def reflect(p):
    return [p[2], p[1], p[0]]


def mean_x(p):
    return sum(p[i] * positions[i] for i in range(3))


# Exact structural checks.
assert all(sum(row) == 1 for row in K)
assert all(K[i][j] == K[j][i] for i in range(3) for j in range(3))
assert step(stationary) == stationary
assert reflect(step(left)) == step(reflect(left))
assert reflect(left) == right

rows = []
pL = left
pR = right

for n in range(13):
    expected_decay = F(3,4) ** n
    expected_L = F(1) - expected_decay
    expected_R = F(1) + expected_decay

    assert pR == reflect(pL)
    assert mean_x(pL) == expected_L
    assert mean_x(pR) == expected_R

    rows.append({
        "n": n,
        "left_distribution": [str(x) for x in pL],
        "right_distribution": [str(x) for x in pR],
        "left_mean_x": str(mean_x(pL)),
        "right_mean_x": str(mean_x(pR)),
        "centered_left": str(mean_x(pL) - 1),
        "centered_right": str(mean_x(pR) - 1),
    })

    pL = step(pL)
    pR = step(pR)

left1 = step(left)
right1 = step(right)
assert mean_x(left1) - mean_x(left) == F(1,4)
assert mean_x(right1) - mean_x(right) == F(-1,4)

result = {
    "audit": "BOUNDARY_STATE_ARROW_SELECTION_V1",
    "status": "PASS",
    "kernel": [[str(x) for x in row] for row in K],
    "stationary_distribution": [str(x) for x in stationary],
    "one_step_left_drift": "1/4",
    "one_step_right_drift": "-1/4",
    "exact_mode_factor": "3/4",
    "checked_steps": 12,
    "rows": rows,
    "nonclaims": [
        "Exact finite symmetry-selection regression only.",
        "The Markov step index is already temporal/update structure.",
        "No claim that the witness derives time or proves the cosmological Past Hypothesis."
    ]
}

print(json.dumps(result, indent=2))
