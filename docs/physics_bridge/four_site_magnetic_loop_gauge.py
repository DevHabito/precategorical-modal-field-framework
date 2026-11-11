#!/usr/bin/env python3
"""Four-site magnetic-flux ring gauge regression.

Classical tight-binding/Peierls benchmark only. This script verifies that local
phase gauge changes leave the Hamiltonian spectrum unchanged while the
gauge-invariant loop phase can alter the spectrum.
"""

import json
import math
import numpy as np


N = 4
J = 1.0
CHI = np.array([0.3, -0.7, 1.1, -0.2], dtype=float)
PHASES = [0.0, math.pi / 3.0, math.pi / 2.0, math.pi]


def ring_hamiltonian(loop_phase, chi=None):
    theta = np.full(N, loop_phase / N, dtype=float)

    if chi is not None:
        theta = theta + chi - np.roll(chi, -1)

    h = np.zeros((N, N), dtype=complex)

    for j in range(N):
        k = (j + 1) % N
        h[j, k] = -J * np.exp(1j * theta[j])
        h[k, j] = -J * np.exp(-1j * theta[j])

    return h, theta


cases = []

for phase in PHASES:
    h0, theta0 = ring_hamiltonian(phase)
    hg, thetag = ring_hamiltonian(phase, CHI)

    u = np.diag(np.exp(1j * CHI))
    expected = u @ h0 @ u.conjugate().T

    eig0 = np.linalg.eigvalsh(h0)
    eigg = np.linalg.eigvalsh(hg)

    cases.append({
        "loop_phase": phase,
        "base_phase_sum": float(theta0.sum()),
        "gauge_phase_sum": float(thetag.sum()),
        "unitary_conjugation_error": float(np.linalg.norm(hg - expected)),
        "maximum_spectrum_error": float(np.max(np.abs(eig0 - eigg))),
        "spectrum": [float(x) for x in eig0],
    })

assert max(x["unitary_conjugation_error"] for x in cases) < 1e-12
assert max(x["maximum_spectrum_error"] for x in cases) < 1e-12

result = {
    "audit": "FOUR_SITE_MAGNETIC_LOOP_GAUGE_V1",
    "status": "PASS",
    "site_count": N,
    "J": J,
    "gauge_vector": [float(x) for x in CHI],
    "cases": cases,
    "maximum_unitary_conjugation_error": max(
        x["unitary_conjugation_error"] for x in cases
    ),
    "maximum_spectrum_error": max(
        x["maximum_spectrum_error"] for x in cases
    ),
    "nonclaims": [
        "Classical tight-binding/Peierls gauge regression only.",
        "No identification between the repository q field and electromagnetic vector potential.",
        "No claim that magnetic holonomy is time or explains the origin of time."
    ],
}

print(json.dumps(result, indent=2))
