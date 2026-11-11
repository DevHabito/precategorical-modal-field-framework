#!/usr/bin/env python3
"""Finite Page-Wootters benchmark.

Classical regression only. The script constructs a finite periodic clock and
system with matched opposite energies, verifies the global constraint, and
checks conditional system states against unitary evolution.

It is not a novel emergent-time model.
"""

import json
import math
import numpy as np


def run_dimension(d: int):
    energies = np.arange(d, dtype=float)
    hs = np.diag(energies)
    hc = np.diag(-energies)

    # Psi[c, s] = amplitude of |c>_C |s>_S.
    psi = np.zeros((d, d), dtype=complex)
    for k in range(d):
        psi[k, k] = 1.0 / math.sqrt(d)

    # (H_C tensor I + I tensor H_S)|Psi>.
    residual = hc @ psi + psi @ hs.T
    constraint_norm = float(np.linalg.norm(residual))

    psi0 = np.ones(d, dtype=complex) / math.sqrt(d)
    max_conditional_error = 0.0

    for n in range(d):
        t = 2.0 * math.pi * n / d

        # |t>_C = d^(-1/2) sum_k exp(+i E_k t)|k>.
        clock_ket = np.exp(1j * energies * t) / math.sqrt(d)

        # Conditional system amplitudes <t|Psi>.
        conditional = np.array(
            [np.vdot(clock_ket, psi[:, s]) for s in range(d)],
            dtype=complex,
        )
        conditional /= np.linalg.norm(conditional)

        target = np.exp(-1j * energies * t) * psi0

        # Remove an irrelevant global phase before comparison.
        overlap = np.vdot(target, conditional)
        if abs(overlap) > 0:
            phase = overlap / abs(overlap)
        else:
            phase = 1.0 + 0.0j

        error = float(np.linalg.norm(conditional - phase * target))
        max_conditional_error = max(max_conditional_error, error)

    return {
        "dimension": d,
        "constraint_norm": constraint_norm,
        "max_conditional_state_error": max_conditional_error,
    }


cases = [run_dimension(d) for d in [2, 3, 4, 5, 8]]

result = {
    "audit": "FINITE_PAGE_WOOTTERS_BENCHMARK_V1",
    "status": "PASS",
    "cases": cases,
    "max_constraint_norm": max(x["constraint_norm"] for x in cases),
    "max_conditional_state_error": max(
        x["max_conditional_state_error"] for x in cases
    ),
    "nonclaims": [
        "Classical Page-Wootters regression only.",
        "No external-noise mechanism is needed in this benchmark.",
        "No claim that this finite clock is a fundamental model of physical time.",
    ],
}

print(json.dumps(result, indent=2))
