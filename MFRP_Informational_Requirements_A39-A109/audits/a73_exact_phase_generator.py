#!/usr/bin/env python3
"""Generate the exact A73 continuous-phase certificate for M=13."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"


M13_SPEC = {
    "mean": sp.Rational(13, 2),
    "epsilon": sp.Rational(1, 160000),
    "gamma": 4,
    "phase_specs": [
        (
            (1, 4, 13, 14, 16, 20, 21, 28),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (1, 4, 5, 13, 16, 20, 21, 28),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 4, 5, 13, 16, 20, 21, 28),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 4, 13, 15, 16, 20, 21, 28),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 4, 5, 13, 15, 20, 21, 28),
            (("alpha", 1), ("beta", -1), ("gamma", 1)),
        ),
        (
            (0, 4, 13, 15, 20, 21, 28),
            (("alpha", 1), ("beta", -1)),
        ),
        (
            (0, 3, 4, 13, 15, 20, 21, 28),
            (("alpha", 1), ("beta", -1), ("gamma", -1)),
        ),
        (
            (0, 3, 13, 15, 20, 21, 28),
            (("alpha", 1), ("gamma", -1)),
        ),
    ],
    "approx_alpha": [
        2.7825,
        2.7955,
        2.8715,
        2.9015,
        2.9095,
        2.9185,
        2.9785,
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
    a67 = load_module(A67_SCRIPT, "a67_for_a73_M13")
    result = a67.audit_M(13, M13_SPEC)

    output = HERE / "a73_exact_phases_M13.json"
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "maximum": 13,
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
