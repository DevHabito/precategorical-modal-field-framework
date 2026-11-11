#!/usr/bin/env python3
"""Exact rational audit for observable-selective closure.

This checks the three-state equal-mean counterexample and the scalar-transform
generator identity at a rational surrogate exp(-c)=1/2.
"""

from fractions import Fraction as F
import json

r = F(1, 2)  # r = exp(-c), so exp(c)=2
birth = F(3)
D = F(5, 7)

pA = [F(0), F(1), F(0)]
pB = [F(1,2), F(0), F(1,2)]

def mean(p):
    return sum(F(n) * p[n] for n in range(len(p)))

def g_minus_c(p):
    return sum(p[n] * (r ** (-n)) for n in range(len(p)))

assert mean(pA) == mean(pB) == 1
assert g_minus_c(pA) == 2
assert g_minus_c(pB) == F(5,2)

mean_dot_A = birth - D * g_minus_c(pA)
mean_dot_B = birth - D * g_minus_c(pB)

assert mean_dot_A == F(11,7)
assert mean_dot_B == F(17,14)
assert mean_dot_B - mean_dot_A == -F(5,14)

results = {
    "audit": "OBSERVABLE_SELECTIVE_CLOSURE_V1",
    "status": "PASS",
    "exp_minus_c": "1/2",
    "birth_rate": "3",
    "death_prefactor": "5/7",
    "pA": ["0", "1", "0"],
    "pB": ["1/2", "0", "1/2"],
    "mean_both": "1",
    "G_minus_c_A": "2",
    "G_minus_c_B": "5/2",
    "mean_derivative_A": "11/7",
    "mean_derivative_B": "17/14",
    "derivative_difference_B_minus_A": "-5/14",
    "nonclaim": "Exact algebraic audit only; not experimental evidence."
}
print(json.dumps(results, indent=2))
