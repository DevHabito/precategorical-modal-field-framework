#!/usr/bin/env python3
"""Exact finite audit for the first Markov thermal physical-bridge pilot.

Only Python's standard library is used. All promoted finite equalities use
fractions.Fraction. Floating-point arithmetic is not used for sign or equality
decisions.
"""

from fractions import Fraction
import json
import math


def fs(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


# Three-state reversible CTMC.
# Units: beta = ln 2, candidate potential q = (0,1,2).
q = [0, 1, 2]
W = [
    [Fraction(0), Fraction(4), Fraction(1)],
    [Fraction(8), Fraction(0), Fraction(3)],
    [Fraction(4), Fraction(6), Fraction(0)],
]
pi_eq = [Fraction(4, 7), Fraction(2, 7), Fraction(1, 7)]


# Row-convention generator.
Q = []
for i in range(3):
    outgoing = sum(W[i][j] for j in range(3) if j != i)
    Q.append([
        -outgoing if i == j else W[i][j]
        for j in range(3)
    ])


stationarity = [
    sum(pi_eq[i] * Q[i][j] for i in range(3))
    for j in range(3)
]
assert stationarity == [Fraction(0), Fraction(0), Fraction(0)]


detailed_balance = {}
for i in range(3):
    for j in range(i + 1, 3):
        left = pi_eq[i] * W[i][j]
        right = pi_eq[j] * W[j][i]
        assert left == right
        detailed_balance[f"{i}-{j}"] = {
            "pi_i_w_ij": fs(left),
            "pi_j_w_ji": fs(right),
            "equal": True,
        }


ratio_checks = {}
for i, j in [(0, 1), (1, 2), (0, 2)]:
    ratio = W[i][j] / W[j][i]
    target = Fraction(1, 2 ** (q[j] - q[i]))
    assert ratio == target
    ratio_checks[f"{i}->{j}"] = {
        "rate_ratio": fs(ratio),
        "target_ratio": fs(target),
        "matches_q_difference": True,
        "q_difference": q[j] - q[i],
    }


cycle_forward = W[0][1] * W[1][2] * W[2][0]
cycle_reverse = W[1][0] * W[2][1] * W[0][2]
assert cycle_forward == cycle_reverse == 48


# Break one directed rate. The cycle condition must fail.
W_ne = [row[:] for row in W]
W_ne[0][2] = Fraction(2)
cycle_forward_ne = W_ne[0][1] * W_ne[1][2] * W_ne[2][0]
cycle_reverse_ne = W_ne[1][0] * W_ne[2][1] * W_ne[0][2]
assert cycle_forward_ne == 48
assert cycle_reverse_ne == 96
assert cycle_forward_ne != cycle_reverse_ne


# Coarse-graining A={0,1}, B={2}.
rate_0_to_B = W[0][2]
rate_1_to_B = W[1][2]
assert rate_0_to_B == 1
assert rate_1_to_B == 3

rho_eq_A = [
    pi_eq[0] / (pi_eq[0] + pi_eq[1]),
    pi_eq[1] / (pi_eq[0] + pi_eq[1]),
]
assert rho_eq_A == [Fraction(2, 3), Fraction(1, 3)]

rate_A_to_B_eq = rho_eq_A[0] * rate_0_to_B + rho_eq_A[1] * rate_1_to_B
assert rate_A_to_B_eq == Fraction(5, 3)


# Two energy/degeneracy representations with identical canonical weights.
E_A = [0, 1, 2]
mu_A = [1, 1, 1]
E_B = [1, 1, 2]
mu_B = [2, 1, 1]

weights_A = [Fraction(mu_A[i], 2 ** E_A[i]) for i in range(3)]
weights_B = [Fraction(mu_B[i], 2 ** E_B[i]) for i in range(3)]
assert weights_A == weights_B == [Fraction(1), Fraction(1, 2), Fraction(1, 4)]

F_A = [E_A[i] - int(math.log2(mu_A[i])) for i in range(3)]
F_B = [E_B[i] - int(math.log2(mu_B[i])) for i in range(3)]
assert F_A == F_B == [0, 1, 2]


results = {
    "pilot": "MARKOV_THERMAL_PHYSICAL_BRIDGE_V1",
    "date": "2026-11-11",
    "scope": "Exact finite diagnostic model; not an empirical validation of the framework.",
    "equilibrium_model": {
        "beta": "ln 2",
        "q": q,
        "off_diagonal_rates": [[fs(x) for x in row] for row in W],
        "stationary_distribution": [fs(x) for x in pi_eq],
        "stationarity_vector_piQ": [fs(x) for x in stationarity],
        "detailed_balance": detailed_balance,
        "rate_ratio_checks": ratio_checks,
        "cycle_product_forward": fs(cycle_forward),
        "cycle_product_reverse": fs(cycle_reverse),
        "kolmogorov_cycle_condition": True,
    },
    "nonequilibrium_perturbation": {
        "changed_rate": "W[0][2]: 1 -> 2",
        "cycle_product_forward": fs(cycle_forward_ne),
        "cycle_product_reverse": fs(cycle_reverse_ne),
        "kolmogorov_cycle_condition": False,
        "conclusion": "No single scalar state potential q can reproduce all three rate ratios after the perturbation.",
    },
    "coarse_graining": {
        "partition": {"A": [0, 1], "B": [2]},
        "A_to_B_rate_if_current_microstate_0": fs(rate_0_to_B),
        "A_to_B_rate_if_current_microstate_1": fs(rate_1_to_B),
        "equilibrium_conditional_occupancy_inside_A": [fs(x) for x in rho_eq_A],
        "equilibrium_weighted_A_to_B_rate": fs(rate_A_to_B_eq),
        "conclusion": "K and the partition alone do not determine the macro A->B rate away from a declared source occupancy or lumpability condition.",
    },
    "energy_degeneracy_reparameterization": {
        "representation_A": {
            "E": E_A,
            "mu": mu_A,
            "weights": [fs(x) for x in weights_A],
        },
        "representation_B": {
            "E": E_B,
            "mu": mu_B,
            "weights": [fs(x) for x in weights_B],
        },
        "same_equilibrium_weights": True,
        "effective_free_energy_in_log2_units_A": F_A,
        "effective_free_energy_in_log2_units_B": F_B,
        "conclusion": "Equilibrium weights identify the effective combination E-log2(mu), not E and mu separately.",
    },
    "status": "PASS",
    "nonclaims": [
        "This toy model is not experimental evidence.",
        "The reconstruction of q from K is classical detailed-balance structure, not a new theorem.",
        "The occupancy dependence of coarse-graining is classical and does not establish a new physical field pi.",
        "No spacetime, gravity, quantum, or pregeometric interpretation is inferred.",
    ],
}

print(json.dumps(results, indent=2))
