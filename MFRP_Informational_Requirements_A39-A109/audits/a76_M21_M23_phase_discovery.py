#!/usr/bin/env python3
"""Independent numerical phase discovery for M=21,22,23.

This file is a discovery aid only. It does not provide the exact proof.
The exact interval theorem and one-pivot classifications are produced by
a76_active_reentry_audit.py.

The scan uses a dense alpha grid, solves the normalized Charnes-Cooper LP,
and records stable positive-support and active-band signatures.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
A65_SCRIPT = HERE / "a65_continuous_first_anchor_audit.py"

GRID_COUNT = 1600
POSITIVE_TOLERANCE = 1e-13
SLACK_TOLERANCE = 1e-5


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def normalized_epsilon(maximum: int) -> float:
    h = maximum // 2

    if maximum % 2 == 0:
        return 1.0 / (1875.0 * 2.0**h)

    return 1.0 / (2500.0 * 2.0**h)


def solve_signature(a65, maximum: int, alpha: float) -> dict:
    detail = a65.solve_continuous_ratio(
        maximum,
        maximum / 2.0,
        1,
        normalized_epsilon(maximum),
        (alpha, 3.0, 4.0),
        "highs-ds",
        True,
    )

    solution = detail["result"].x
    count = maximum + 1

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


def discover(a65, maximum: int) -> dict:
    alphas = np.linspace(
        2.0,
        2.999,
        GRID_COUNT,
    )

    phases = []
    previous_key = None

    for alpha in alphas:
        current = solve_signature(
            a65,
            maximum,
            float(alpha),
        )
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

    return {
        "maximum": maximum,
        "mean": maximum / 2.0,
        "epsilon": str(
            normalized_epsilon(maximum)
        ),
        "phase_count": len(phases),
        "phases": phases,
    }


def main() -> None:
    a65 = load_module(
        A65_SCRIPT,
        "a65_for_a76_discovery",
    )

    results = {
        "audit": (
            "A76_M21_M23_NUMERICAL_PHASE_DISCOVERY"
        ),
        "role": (
            "Discovery only. Exact interval and KKT results are "
            "provided by a76_active_reentry_audit.py."
        ),
        "grid_count": GRID_COUNT,
        "supports": [
            discover(a65, maximum)
            for maximum in [21, 22, 23]
        ],
    }

    output = HERE / (
        "a76_M21_M23_phase_discovery.json"
    )
    output.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "phase_counts": {
                    str(item["maximum"]): (
                        item["phase_count"]
                    )
                    for item in results["supports"]
                },
                "phase_starts": {
                    str(item["maximum"]): [
                        phase[
                            "approx_alpha_start"
                        ]
                        for phase in item["phases"]
                    ]
                    for item in results["supports"]
                },
                "output": output.name,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
