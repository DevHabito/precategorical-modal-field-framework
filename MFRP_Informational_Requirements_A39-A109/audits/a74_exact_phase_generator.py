#!/usr/bin/env python3
"""Generate the exact A74 continuous-phase certificate for M=14.

The phase sequence was first discovered numerically without importing the
M=13 grammar. This script certifies the declared sequence algebraically.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"


M14_SPEC = {
    "mean": sp.Rational(7),
    "epsilon": sp.Rational(1, 240000),
    "gamma": 4,
    "phase_specs": [
        (
            (1, 5, 14, 15, 17, 22, 23, 30),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 1, 5, 14, 17, 22, 23, 30),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 5, 14, 16, 17, 22, 23, 30),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 4, 5, 14, 16, 22, 23, 30),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 4, 14, 16, 22, 23, 30),
            (("alpha", 1), ("beta", -1)),
        ),
        (
            (0, 3, 4, 14, 16, 22, 23, 30),
            (("alpha", 1), ("beta", -1), ("gamma", -1)),
        ),
        (
            (0, 3, 14, 16, 22, 23, 30),
            (("alpha", 1), ("gamma", -1)),
        ),
    ],
    "approx_alpha": [
        2.6158,
        2.6850,
        2.7508,
        2.9371,
        2.9416,
        2.9849,
    ],
}


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main() -> None:
    a67 = load_module(A67_SCRIPT, "a67_for_a74_M14")
    result = a67.audit_M(14, M14_SPEC)

    output = HERE / "a74_exact_phases_M14.json"
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "maximum": 14,
                "phase_count": result["phase_count"],
                "transition_count": result["transition_count"],
                "boundary_risk": result["boundary_risk_decimal"],
                "coalescence_risk": result[
                    "coalescence_risk_limit_decimal"
                ],
                "gates": result["gates"],
                "verdict": result["verdict"],
            },
            indent=2,
        )
    )

    if not all(result["gates"].values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
