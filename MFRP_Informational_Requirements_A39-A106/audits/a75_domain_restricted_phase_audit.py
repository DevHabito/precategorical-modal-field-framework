#!/usr/bin/env python3
"""Domain-restricted exact phase runner for A75.

This runner reproduces the exact M=15 and M=16 phase audits while restricting
condition-root isolation to the declared first-anchor domain s in [1/8,1/4].
The restriction is mathematically exact because roots outside that domain
cannot affect any phase certificate.

The transition roots are still isolated by the original A67 transition
routine. Only the repeated condition-root cache is replaced.
"""

from __future__ import annotations

import importlib.util
import json
from functools import lru_cache
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"
A75_SPECS = HERE / "a75_exact_phase_generator.py"


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
        "a67_for_a75_domain_restricted",
    )
    specs = load_module(
        A75_SPECS,
        "a75_phase_specs",
    )

    @lru_cache(maxsize=None)
    def roots_in_declared_domain(
        polynomial_text: str,
    ):
        polynomial = sp.Poly(
            sp.sympify(polynomial_text),
            a67.S,
            domain=sp.QQ,
        )
        return tuple(
            (
                left,
                right,
                multiplicity,
            )
            for (
                left,
                right,
            ), multiplicity in sp.intervals(
                polynomial,
                eps=sp.Rational(
                    1,
                    10**10,
                ),
                inf=a67.DOMAIN_LOWER,
                sup=a67.DOMAIN_UPPER,
                fast=True,
            )
        )

    a67.roots_of_poly = (
        roots_in_declared_domain
    )

    summary = {}

    for maximum in [15, 16]:
        result = a67.audit_M(
            maximum,
            specs.SPECS[maximum],
        )

        output = HERE / (
            f"a75_exact_phases_M{maximum}.json"
        )
        output.write_text(
            json.dumps(
                result,
                indent=2,
            ),
            encoding="utf-8",
        )

        summary[str(maximum)] = {
            "phase_count": (
                result["phase_count"]
            ),
            "transition_count": (
                result["transition_count"]
            ),
            "gates": result["gates"],
            "verdict": result["verdict"],
            "output": output.name,
        }

    summary["root_cache"] = (
        roots_in_declared_domain
        .cache_info()
        ._asdict()
    )

    print(json.dumps(summary, indent=2))

    if not all(
        all(
            item["gates"].values()
        )
        for key, item
        in summary.items()
        if key in {"15", "16"}
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
