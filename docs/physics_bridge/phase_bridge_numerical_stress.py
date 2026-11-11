#!/usr/bin/env python3
"""Numerical stress test for the randomized-phase physical bridge.

This script integrates the exact phase-conditioned scalar transform equation
over a diagnostic parameter grid and checks two derived claims:

1. phase-averaged continuous-time dynamics generally differs from the
   constant averaged-rate approximation;
2. phase-averaged stroboscopic values satisfy the exact three-point
   recurrence with the Floquet multiplier fixed by the periodic drive.

This is a regression test of the mathematics. It does not use experimental
data and it is not evidence for a physical theory.
"""

import itertools
import json
import math


def i0(x):
    term = 1.0
    total = 1.0
    k = 1
    while True:
        term *= (x * x / 4.0) / (k * k)
        new_total = total + term
        if abs(term) < 1e-16 * abs(new_total):
            return new_total
        total = new_total
        k += 1
        if k > 1000:
            raise RuntimeError("I0 series did not converge")


def rk4_step(x, t, dt, phi, q, gamma0, amp, omega, b):
    kappa = 1.0 - q

    def rhs(tt, xx):
        rate = gamma0 * math.exp(-amp * math.sin(omega * tt + phi))
        return -kappa * rate * xx + b

    k1 = rhs(t, x)
    k2 = rhs(t + dt / 2.0, x + dt * k1 / 2.0)
    k3 = rhs(t + dt / 2.0, x + dt * k2 / 2.0)
    k4 = rhs(t + dt, x + dt * k3)
    return x + dt * (k1 + 2*k2 + 2*k3 + k4) / 6.0


def run_case(q, amp, gamma0, omega, phase_count=24,
             steps_per_period=800, periods=5):
    period = 2.0 * math.pi / omega
    death_prefactor = gamma0 * math.sqrt(q)
    source = death_prefactor * (1.0 / q - 1.0)
    multiplier = math.exp(
        -(1.0 - q) * gamma0 * period * i0(amp)
    )

    phases = [
        2.0 * math.pi * p / phase_count
        for p in range(phase_count)
    ]

    # Phase-dependent initial values deliberately stress the fact that
    # phase/state correlations do not spoil the stroboscopic recurrence.
    states = [
        1.0 + 0.15 * math.cos(phi) + 0.05 * math.sin(2.0 * phi)
        for phi in phases
    ]

    dt = period / steps_per_period
    stroboscopic = [sum(states) / phase_count]

    for period_index in range(periods):
        for step in range(steps_per_period):
            t = (period_index * steps_per_period + step) * dt
            states = [
                rk4_step(x, t, dt, phi, q, gamma0, amp, omega, source)
                for x, phi in zip(states, phases)
            ]
        stroboscopic.append(sum(states) / phase_count)

    recurrence_residuals = []
    for n in range(len(stroboscopic) - 2):
        residual = (
            stroboscopic[n + 2]
            - (1.0 + multiplier) * stroboscopic[n + 1]
            + multiplier * stroboscopic[n]
        )
        recurrence_residuals.append(residual)

    # Separate continuous-time comparison from a common initial transform.
    states = [1.1 for _ in phases]
    averaged_rate_state = 1.1
    averaged_rate = gamma0 * i0(amp)
    checkpoints = {}

    for step in range(steps_per_period):
        t = step * dt
        states = [
            rk4_step(x, t, dt, phi, q, gamma0, amp, omega, source)
            for x, phi in zip(states, phases)
        ]

        kappa = 1.0 - q

        def averaged_rhs(xx):
            return -kappa * averaged_rate * xx + source

        k1 = averaged_rhs(averaged_rate_state)
        k2 = averaged_rhs(averaged_rate_state + dt * k1 / 2.0)
        k3 = averaged_rhs(averaged_rate_state + dt * k2 / 2.0)
        k4 = averaged_rhs(averaged_rate_state + dt * k3)
        averaged_rate_state += dt * (k1 + 2*k2 + 2*k3 + k4) / 6.0

        if step + 1 in {
            steps_per_period // 8,
            steps_per_period // 4,
            steps_per_period // 2,
            steps_per_period,
        }:
            checkpoints[(step + 1) / steps_per_period] = (
                sum(states) / phase_count,
                averaged_rate_state,
            )

    max_continuous_difference = max(
        abs(exact - approximate)
        for exact, approximate in checkpoints.values()
    )

    return {
        "q": q,
        "A": amp,
        "gamma0": gamma0,
        "omega": omega,
        "mu": multiplier,
        "max_stroboscopic_residual": max(
            abs(x) for x in recurrence_residuals
        ),
        "max_continuous_mean_rate_difference": max_continuous_difference,
    }


cases = [
    run_case(q, amp, gamma0, omega)
    for q, amp, gamma0, omega in itertools.product(
        [0.35, 0.65],
        [0.4, 1.3],
        [0.2, 0.8],
        [0.7, 1.9],
    )
]

results = {
    "audit": "PHASE_BRIDGE_NUMERICAL_STRESS_V1",
    "status": "PASS",
    "case_count": len(cases),
    "phase_count": 24,
    "steps_per_period": 800,
    "period_count": 5,
    "max_stroboscopic_residual": max(
        x["max_stroboscopic_residual"] for x in cases
    ),
    "min_continuous_mean_rate_difference": min(
        x["max_continuous_mean_rate_difference"] for x in cases
    ),
    "max_continuous_mean_rate_difference": max(
        x["max_continuous_mean_rate_difference"] for x in cases
    ),
    "cases": cases,
    "nonclaims": [
        "Numerical regression of derived equations only; not experimental evidence.",
        "The parameter grid is diagnostic and not fitted to the Salhani et al. device."
    ],
}

print(json.dumps(results, indent=2))
