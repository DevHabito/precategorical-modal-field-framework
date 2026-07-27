#!/usr/bin/env python3
"""Generate exact continuous-phase certificates for M=15 and M=16.

The declared phase sequences come from the independent numerical discovery
artifact a75_M15_M16_phase_discovery.json. Each support is then certified
by the exact A67 algebraic phase auditor.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"


SPECS = {
    15: {
        "mean": sp.Rational(15, 2),
        "epsilon": sp.Rational(1, 320000),
        "gamma": 4,
        "phase_specs": [
            (
                (1, 5, 15, 16, 18, 23, 24, 32),
                (("alpha", 1), ("beta", -1), ("gamma", 1)),
            ),
            (
                (0, 1, 5, 15, 18, 23, 24, 32),
                (("alpha", 1), ("beta", -1), ("gamma", 1)),
            ),
            (
                (0, 5, 15, 17, 18, 23, 24, 32),
                (("alpha", 1), ("beta", -1), ("gamma", 1)),
            ),
            (
                (0, 4, 5, 15, 17, 23, 24, 32),
                (("alpha", 1), ("beta", -1), ("gamma", 1)),
            ),
            (
                (0, 4, 15, 17, 23, 24, 32),
                (("alpha", 1), ("beta", -1)),
            ),
            (
                (0, 4, 15, 17, 23, 24, 32),
                (("alpha", 1), ("gamma", -1)),
            ),
        ],
        "approx_alpha": [
            2.6905,
            2.7435,
            2.7975,
            2.9515,
            2.9535,
        ],
    },
    16: {
        "mean": sp.Rational(8),
        "epsilon": sp.Rational(1, 480000),
        "gamma": 4,
        "phase_specs": [
            (
                (1, 5, 16, 17, 19, 25, 26, 34),
                (("alpha", 1), ("beta", -1), ("gamma", 1)),
            ),
            (
                (0, 1, 5, 16, 19, 25, 26, 34),
                (("alpha", 1), ("beta", -1), ("gamma", 1)),
            ),
            (
                (0, 5, 16, 18, 19, 25, 26, 34),
                (("alpha", 1), ("beta", -1), ("gamma", 1)),
            ),
            (
                (0, 4, 5, 16, 18, 25, 26, 34),
                (("alpha", 1), ("beta", -1), ("gamma", 1)),
            ),
            (
                (0, 4, 16, 18, 25, 26, 34),
                (("alpha", 1), ("beta", -1)),
            ),
            (
                (0, 4, 16, 18, 25, 26, 34),
                (("alpha", 1), ("gamma", -1)),
            ),
        ],
        "approx_alpha": [
            2.7775,
            2.8135,
            2.8525,
            2.9665,
            2.9675,
        ],
    },
}


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main() -> None:
    a67 = load_module(
        A67_SCRIPT,
        "a67_for_a75_exact_phases",
    )

    summary = {}

    for maximum in [15, 16]:
        result = a67.audit_M(
            maximum,
            SPECS[maximum],
        )

        output = HERE / (
            f"a75_exact_phases_M{maximum}.json"
        )
        output.write_text(
            json.dumps(result, indent=2),
            encoding="utf-8",
        )

        summary[str(maximum)] = {
            "phase_count": (
                result["phase_count"]
            ),
            "transition_count": (
                result["transition_count"]
            ),
            "boundary_risk": (
                result[
                    "boundary_risk_decimal"
                ]
            ),
            "coalescence_risk": (
                result[
                    "coalescence_risk_limit_decimal"
                ]
            ),
            "gates": result["gates"],
            "verdict": result["verdict"],
            "output": output.name,
        }

    print(json.dumps(summary, indent=2))

    if not all(
        all(item["gates"].values())
        for item in summary.values()
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
