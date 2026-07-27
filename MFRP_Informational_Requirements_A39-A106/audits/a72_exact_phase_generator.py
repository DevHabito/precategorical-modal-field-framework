#!/usr/bin/env python3
"""Generate one exact A72 continuous-phase certificate.

Usage
-----
python a72_exact_phase_generator.py 11
python a72_exact_phase_generator.py 12

The script imports the declared A72 phase specification and runs the exact
A67 algebraic phase auditor for the selected support maximum.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
A67_SCRIPT = HERE / "a67_central_mean_support_family_audit.py"
A72_SCRIPT = HERE / "a72_local_pivot_diamond_audit.py"


def load_module(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage: python a72_exact_phase_generator.py <M>"
        )

    maximum = int(sys.argv[1])

    if maximum not in {11, 12}:
        raise SystemExit("A72 phase certificates are defined for M=11 or M=12.")

    a67 = load_module(A67_SCRIPT, f"a67_phase_M{maximum}")
    a72 = load_module(A72_SCRIPT, f"a72_specs_M{maximum}")

    specification = (
        a72.M11_SPEC
        if maximum == 11
        else a72.M12_SPEC
    )
    result = a67.audit_M(maximum, specification)

    output = HERE / f"a72_exact_phases_M{maximum}.json"
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "maximum": maximum,
                "phase_count": result["phase_count"],
                "transition_count": result["transition_count"],
                "gates": result["gates"],
                "verdict": result["verdict"],
                "output": output.name,
            },
            indent=2,
        )
    )

    if not all(result["gates"].values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
