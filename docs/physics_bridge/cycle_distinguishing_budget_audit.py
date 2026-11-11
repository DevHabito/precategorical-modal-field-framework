#!/usr/bin/env python3
"""Exact distinguishing-coloring regression for cycle graphs.

Enumerates every k-coloring of C_n and every dihedral automorphism.
This reproduces the classical distinguishing-number benchmark and is used only
to calibrate how much added marked information is required to destroy the
symmetries of the C1 cycle skeletons.
"""

import itertools
import json


def dihedral_permutations(n):
    rotations = [
        tuple((i + k) % n for i in range(n))
        for k in range(n)
    ]
    reflections = [
        tuple((k - i) % n for i in range(n))
        for k in range(n)
    ]
    return list(dict.fromkeys(rotations + reflections))


def preserves(coloring, permutation):
    return all(
        coloring[i] == coloring[permutation[i]]
        for i in range(len(coloring))
    )


def count_distinguishing(n, k):
    automorphisms = dihedral_permutations(n)
    count = 0

    for coloring in itertools.product(range(k), repeat=n):
        stabilizer_size = sum(
            preserves(coloring, p)
            for p in automorphisms
        )
        if stabilizer_size == 1:
            count += 1

    return count


rows = []
for n in range(3, 11):
    counts = {
        str(k): count_distinguishing(n, k)
        for k in range(1, 5)
    }
    minimum = next(
        k for k in range(1, 5)
        if counts[str(k)] > 0
    )
    rows.append({
        "n": n,
        "distinguishing_counts": counts,
        "minimum_alphabet": minimum,
    })

expected = {
    n: (3 if n in {3, 4, 5} else 2)
    for n in range(3, 11)
}

assert all(
    row["minimum_alphabet"] == expected[row["n"]]
    for row in rows
)

result = {
    "audit": "CYCLE_DISTINGUISHING_BUDGET_V1",
    "status": "PASS",
    "rows": rows,
    "graphA_C4_binary_distinguishing_count": 0,
    "graphA_C4_ternary_distinguishing_count": 24,
    "classical_benchmark": "D(C_n)=3 for n=3,4,5 and 2 for n>=6",
    "nonclaim": "Exact finite reproduction of a classical distinguishing-number result; not a new graph theorem or physical direction mechanism."
}

print(json.dumps(result, indent=2))
