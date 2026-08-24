#!/usr/bin/env python3
"""Numerically discover the M=14 active-phase sequence without importing M=13.

This is a discovery aid, not the exact proof. The exact certification is
performed independently by a74_exact_phase_generator.py.

The scan solves the normalized Charnes-Cooper LP on a uniform alpha grid,
extracts positive P/Q supports and active observation bands, and records
stable signature changes.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
A65_SCRIPT = HERE / "a65_continuous_first_anchor_audit.py"

MAXIMUM = 14
MEAN = 7.0
EPSILON = 1.0 / 240000.0
GRID_COUNT = 1000
POSITIVE_TOLERANCE = 1e-9
SLACK_TOLERANCE = 1e-7


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def signature(a65, alpha: float) -> dict:
    detail = a65.solve_continuous_ratio(
        MAXIMUM,
        MEAN,
        1,
        EPSILON,
        (alpha, 3.0, 4.0),
        "highs-ds",
        True,
    )

    solution = detail["result"].x
    count = MAXIMUM + 1

    p_support = [
        index
        for index in range(count)
        if solution[index] > POSITIVE_TOLERANCE
    ]
    q_support = [
        index
        for index in range(count)
        if solution[count + index] > POSITIVE_TOLERANCE
    ]

    slacks = (
        detail["inequality_rhs"]
        - detail["inequality_rows"].dot(solution)
    )

    active = []

    for (exponent, sign), slack in zip(
        detail["inequality_labels"],
        slacks,
    ):
        if slack < SLACK_TOLERANCE:
            if abs(exponent - alpha) < 1e-8:
                name = "alpha"
            elif abs(exponent - 3.0) < 1e-8:
                name = "beta"
            else:
                name = "gamma"

            active.append([name, int(sign)])

    return {
        "p_support": p_support,
        "q_support": q_support,
        "active_observations": active,
        "ratio": detail["ratio"],
    }


def main() -> None:
    a65 = load_module(A65_SCRIPT, "a65_for_a74_discovery")

    alphas = np.linspace(
        2.0,
        2.999,
        GRID_COUNT,
    )

    phases = []
    previous_key = None

    for alpha in alphas:
        current = signature(a65, float(alpha))
        key = (
            tuple(current["p_support"]),
            tuple(current["q_support"]),
            tuple(
                tuple(item)
                for item in current[
                    "active_observations"
                ]
            ),
        )

        if key != previous_key:
            phases.append(
                {
                    "approx_alpha_start": float(alpha),
                    **current,
                }
            )
            previous_key = key

    result = {
        "audit": "A74_M14_NUMERICAL_PHASE_DISCOVERY",
        "role": (
            "Discovery only. The exact theorem is generated independently "
            "by a74_exact_phase_generator.py."
        ),
        "contract": {
            "maximum": MAXIMUM,
            "mean": MEAN,
            "target_exponent": 1,
            "epsilon": "1/240000",
            "design": "{alpha,3,4}",
            "alpha_grid": "[2,2.999]",
            "grid_count": GRID_COUNT,
        },
        "phase_count": len(phases),
        "phases": phases,
    }

    output = HERE / "a74_M14_phase_discovery.json"
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "phase_count": len(phases),
                "phase_starts": [
                    phase["approx_alpha_start"]
                    for phase in phases
                ],
                "output": output.name,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
