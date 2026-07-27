#!/usr/bin/env python3
"""Generate exact integer-catalogue certificates for M=15 and M=16.

All 84 three-anchor designs from {2,...,10} are solved over exact rational
arithmetic for each support. The best three are independently checked using
exact primal and dual programmes.
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
    h = maximum // 2

    if maximum % 2 == 0:
        return sp.Rational(
            1,
            1875 * 2**h,
        )

    return sp.Rational(
        1,
        2500 * 2**h,
    )


def solve_task(
    arguments: tuple[int, tuple[int, int, int]],
) -> tuple[int, tuple[int, int, int], str]:
    maximum, design = arguments
    helper = load_helper(
        f"a75_catalogue_M{maximum}_"
        f"{design[0]}_{design[1]}_{design[2]}"
    )
    value = helper.exact_primal_value(
        maximum,
        sp.Rational(maximum, 2),
        1,
        normalized_epsilon(maximum),
        design,
    )
    return maximum, design, str(value)


def solve_catalogue(maximum: int) -> dict:
    designs = list(
        itertools.combinations(
            range(2, 11),
            3,
        )
    )
    tasks = [
        (maximum, design)
        for design in designs
    ]

    with mp.Pool(
        min(8, max(1, mp.cpu_count()))
    ) as pool:
        values = list(
            pool.imap_unordered(
                solve_task,
                tasks,
                chunksize=1,
            )
        )

    ranked = [
        (design, sp.Rational(value))
        for _, design, value in values
    ]
    ranked.sort(key=lambda item: item[1])

    helper = load_helper(
        f"a75_catalogue_dual_M{maximum}"
    )
    top = []

    for design, primal in ranked[:3]:
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
                "equal": bool(
                    primal == dual
                ),
                "risk_decimal": str(
                    sp.N(
                        sp.log(primal)
                        / (2 * sp.log(2)),
                        50,
                    )
                ),
            }
        )

    return {
        "M": maximum,
        "mean": str(
            sp.Rational(maximum, 2)
        ),
        "epsilon": str(
            normalized_epsilon(maximum)
        ),
        "count": len(ranked),
        "winner": list(ranked[0][0]),
        "runner_up": list(ranked[1][0]),
        "gap": str(
            sp.factor(
                ranked[1][1]
                - ranked[0][1]
            )
        ),
        "top": top,
    }


def main() -> None:
    results = {}

    for maximum in [15, 16]:
        result = solve_catalogue(maximum)
        output = HERE / (
            f"a75_exact_catalogue_M{maximum}.json"
        )
        output.write_text(
            json.dumps(result, indent=2),
            encoding="utf-8",
        )
        results[str(maximum)] = result

    print(
        json.dumps(
            {
                maximum: {
                    "count": result["count"],
                    "winner": result["winner"],
                    "runner_up": (
                        result["runner_up"]
                    ),
                    "gap": result["gap"],
                    "top_primal_dual_equal": all(
                        item["equal"]
                        for item in result["top"]
                    ),
                }
                for maximum, result
                in results.items()
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
