#!/usr/bin/env python3
"""Exact symmetric-law/asymmetric-sector regression.

This is a finite stochastic sector-selection toy model, not a claim of
thermodynamic spontaneous symmetry breaking.
"""

from fractions import Fraction as F
import json

# State order: minus, neutral, plus
K = [
    [F(1),   F(0), F(0)],
    [F(1,2), F(0), F(1,2)],
    [F(0),   F(0), F(1)],
]

pi = [F(0), F(1), F(0)]
order_parameter = [F(-1), F(0), F(1)]


def step(p):
    return [
        sum(p[i] * K[i][j] for i in range(3))
        for j in range(3)
    ]


def reflect(p):
    return [p[2], p[1], p[0]]


def expectation(p, values):
    return sum(x * y for x, y in zip(p, values))


rows = []

for n in range(6):
    mean = expectation(pi, order_parameter)
    abs_mean = expectation(
        pi,
        [abs(x) for x in order_parameter],
    )

    assert reflect(pi) == pi
    assert mean == 0

    if n == 0:
        assert abs_mean == 0
    else:
        assert pi == [F(1,2), F(0), F(1,2)]
        assert abs_mean == 1

    rows.append({
        "n": n,
        "distribution": [str(x) for x in pi],
        "reflection_invariant": True,
        "mean_order_parameter": str(mean),
        "mean_absolute_order_parameter": str(abs_mean),
    })

    pi = step(pi)

result = {
    "audit": "SYMMETRIC_LAW_ASYMMETRIC_SECTOR_V1",
    "status": "PASS",
    "kernel": [[str(x) for x in row] for row in K],
    "rows": rows,
    "exact_conclusions": [
        "The ensemble distribution remains reflection invariant.",
        "The signed order-parameter expectation is exactly zero.",
        "After one update every realization lies in a nonzero-polarity absorbing sector.",
        "For n>=1 the mean absolute order parameter is exactly one."
    ],
    "nonclaims": [
        "This finite chain is not asserted to be thermodynamic spontaneous symmetry breaking.",
        "The update index already supplies dynamical succession.",
        "Sector polarity is not identified with temporal order."
    ]
}

print(json.dumps(result, indent=2))
