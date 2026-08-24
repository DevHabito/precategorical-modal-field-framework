#!/usr/bin/env python3
"""Generate the exact A74 integer-catalogue certificate for M=14.

All 84 three-anchor designs from {2,...,10} are solved over exact rational
arithmetic. The best three designs are independently checked by exact primal
and dual programmes.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import multiprocessing as mp
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
HELPER = HERE / "a64_scale_normalized_boundary_pair_exact_helpers.py"


def load_helper(name: str):
    specification = importlib.util.spec_from_file_location(name, HELPER)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Could not load {HELPER}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def normalized_epsilon(maximum: int) -> sp.Rational:
    mean = sp.Rational(maximum, 2)
    lower = int(sp.floor(mean))

    if mean == lower:
        lower_scale = sp.Rational(1, 2 ** lower)
    else:
        lower_scale = (
            sp.Rational(1, 2 ** lower)
            + sp.Rational(1, 2 ** (lower + 1))
        ) / 2

    return sp.factor(lower_scale / 1875)


def solve_task(
    arguments: tuple[int, tuple[int, int, int]],
) -> tuple[tuple[int, int, int], str]:
    maximum, design = arguments
    helper = load_helper(
        f"a74_catalogue_M{maximum}_{design[0]}_{design[1]}_{design[2]}"
    )
    value = helper.exact_primal_value(
        maximum,
        sp.Rational(maximum, 2),
        1,
        normalized_epsilon(maximum),
        design,
    )
    return design, str(value)


def main() -> None:
    maximum = 14
    designs = list(itertools.combinations(range(2, 11), 3))
    tasks = [(maximum, design) for design in designs]

    with mp.Pool(min(8, max(1, mp.cpu_count()))) as pool:
        values = list(
            pool.imap_unordered(
                solve_task,
                tasks,
                chunksize=1,
            )
        )

    values.sort(key=lambda item: sp.Rational(item[1]))

    helper = load_helper("a74_catalogue_dual_M14")
    top = []

    for design, primal_text in values[:3]:
        primal = sp.Rational(primal_text)
        dual = helper.exact_dual_value(
            maximum,
            sp.Rational(maximum, 2),
            1,
            normalized_epsilon(maximum),
            design,
        )
        top.append(
            {
                "design": list(design),
                "primal": str(primal),
                "dual": str(dual),
                "equal": bool(primal == dual),
                "risk_decimal": str(
                    sp.N(
                        sp.log(primal) / (2 * sp.log(2)),
                        50,
                    )
                ),
            }
        )

    result = {
        "M": maximum,
        "mean": str(sp.Rational(maximum, 2)),
        "epsilon": str(normalized_epsilon(maximum)),
        "count": len(values),
        "winner": list(values[0][0]),
        "runner_up": list(values[1][0]),
        "gap": str(
            sp.factor(
                sp.Rational(values[1][1])
                - sp.Rational(values[0][1])
            )
        ),
        "top": top,
    }

    output = HERE / "a74_exact_catalogue_M14.json"
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
