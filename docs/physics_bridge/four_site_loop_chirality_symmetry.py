#!/usr/bin/env python3
"""Symmetry regression for the four-site uniform-flux ring."""

import json
import math
import numpy as np

N = 4
PHASES = [math.pi / 3.0, math.pi / 2.0]


def ring_hamiltonian(phi):
    theta = phi / N
    h = np.zeros((N, N), dtype=complex)
    for j in range(N):
        k = (j + 1) % N
        h[j, k] = -np.exp(1j * theta)
        h[k, j] = -np.exp(-1j * theta)
    return h


translation = np.zeros((N, N), dtype=complex)
reflection = np.zeros((N, N), dtype=complex)

for j in range(N):
    translation[(j + 1) % N, j] = 1.0
    reflection[(-j) % N, j] = 1.0

cases = []

for phi in PHASES:
    h = ring_hamiltonian(phi)
    h_minus = ring_hamiltonian(-phi)

    rotation_commutator_error = float(
        np.linalg.norm(translation @ h - h @ translation)
    )
    reflection_flux_reversal_error = float(
        np.linalg.norm(
            reflection @ h @ reflection.conjugate().T - h_minus
        )
    )

    cases.append({
        "phi": phi,
        "rotation_commutator_error": rotation_commutator_error,
        "reflection_flux_reversal_error": reflection_flux_reversal_error,
    })

assert max(x["rotation_commutator_error"] for x in cases) < 1e-12
assert max(x["reflection_flux_reversal_error"] for x in cases) < 1e-12

result = {
    "audit": "FOUR_SITE_LOOP_CHIRALITY_NOT_ORDER_V1",
    "status": "PASS",
    "cases": cases,
    "interpretation": [
        "Uniform nonzero loop flux preserves cyclic translation symmetry.",
        "Reflection maps phi to -phi.",
        "Loop chirality therefore does not select a distinguished vertex or strict temporal order."
    ],
    "nonclaim": "Standard magnetic-ring symmetry regression; not evidence for emergent time."
}

print(json.dumps(result, indent=2))
