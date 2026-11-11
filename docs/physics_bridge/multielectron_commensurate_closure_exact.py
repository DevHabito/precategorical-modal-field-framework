#!/usr/bin/env python3
"""Exact audit of the commensurate transform closure ladder.

This is a regression check of the analytic generator identity. It uses only
rational arithmetic and does not use experimental data.
"""

from fractions import Fraction as F
import json


r = F(1, 2)  # r = exp(-c)
birth = F(3)
death_prefactor = F(5, 7)

p = [F(1, 10), F(2, 10), F(3, 10), F(4, 10)]
assert sum(p) == 1


def G(j: int) -> F:
    return sum(p[n] * r ** (j * n) for n in range(len(p)))


def direct_generator_derivative(j: int) -> F:
    total = F(0)
    for n, pn in enumerate(p):
        f_n = r ** (j * n)
        f_birth = r ** (j * (n + 1))
        f_death = r ** (j * (n - 1))
        death_n = death_prefactor * r ** (-n)
        total += pn * (
            birth * (f_birth - f_n)
            + death_n * (f_death - f_n)
        )
    return total


def ladder_derivative(j: int) -> F:
    return (
        birth * (r ** j - 1) * G(j)
        + death_prefactor * (r ** (-j) - 1) * G(j - 1)
    )


checks = []
for j in range(1, 5):
    direct = direct_generator_derivative(j)
    ladder = ladder_derivative(j)
    assert direct == ladder
    checks.append({
        "j": j,
        "G_j": str(G(j)),
        "G_j_minus_1": str(G(j - 1)),
        "direct_derivative": str(direct),
        "ladder_derivative": str(ladder),
        "equal": True,
    })

assert G(0) == 1

results = {
    "audit": "MULTIELECTRON_COMMENSURATE_CLOSURE_LADDER_V1",
    "status": "PASS",
    "r": "1/2",
    "birth_rate": "3",
    "death_prefactor": "5/7",
    "distribution": [str(x) for x in p],
    "G_0": "1",
    "checks": checks,
    "interpretation": [
        "j=1 closes on G_1 and the normalization G_0=1.",
        "j=m depends only on G_m and G_(m-1), so the ordered vector G_1,...,G_m is triangular and closed.",
        "The audit checks the analytic identity only; it is not experimental evidence."
    ]
}

print(json.dumps(results, indent=2))
