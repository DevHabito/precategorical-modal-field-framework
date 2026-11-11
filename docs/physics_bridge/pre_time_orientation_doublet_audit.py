#!/usr/bin/env python3
"""Exact finite pre-time-orientation doublet audit for marked cycles.

A coloring passes when the set of automorphism-invariant acyclic orientations
contains exactly two members and those members are global reverses.

This is a project-specific finite criterion inspired by, but not equivalent
to, Lorentzian time orientability.
"""

import itertools
import json


def dihedral(n):
    rotations = [
        tuple((i + k) % n for i in range(n))
        for k in range(n)
    ]
    reflections = [
        tuple((k - i) % n for i in range(n))
        for k in range(n)
    ]
    return list(dict.fromkeys(rotations + reflections))


def preserves_coloring(coloring, permutation):
    return all(
        coloring[i] == coloring[permutation[i]]
        for i in range(len(coloring))
    )


def directed_edges(n, bits):
    result = set()
    for i, clockwise in enumerate(bits):
        j = (i + 1) % n
        result.add((i, j) if clockwise else (j, i))
    return result


def orientation_invariant(edges, permutation):
    return {
        (permutation[u], permutation[v])
        for u, v in edges
    } == edges


def acyclic_cycle_orientation(bits):
    return not (all(bits) or not any(bits))


rows = []
examples = {}

for n in range(3, 9):
    automorphisms = dihedral(n)
    acyclic = [
        bits
        for bits in itertools.product((False, True), repeat=n)
        if acyclic_cycle_orientation(bits)
    ]

    for k in range(1, 4):
        doublet_count = 0
        sample_colorings = []

        for coloring in itertools.product(range(k), repeat=n):
            stabilizer = [
                p for p in automorphisms
                if preserves_coloring(coloring, p)
            ]

            valid = []
            for bits in acyclic:
                edges = directed_edges(n, bits)
                if all(
                    orientation_invariant(edges, p)
                    for p in stabilizer
                ):
                    valid.append(bits)

            if len(valid) == 2:
                reverse = tuple(not bit for bit in valid[0])
                if reverse == valid[1] or reverse == valid[0]:
                    assert reverse in valid
                    doublet_count += 1
                    if len(sample_colorings) < 8:
                        sample_colorings.append({
                            "coloring": list(coloring),
                            "orientations": [
                                [int(x) for x in bits]
                                for bits in valid
                            ],
                        })

        rows.append({
            "n": n,
            "alphabet": k,
            "coloring_count": k ** n,
            "unique_orientation_doublet_count": doublet_count,
        })
        examples[f"C{n}_k{k}"] = sample_colorings

c4_binary = next(
    row for row in rows
    if row["n"] == 4 and row["alphabet"] == 2
)

assert c4_binary["unique_orientation_doublet_count"] == 2

c4_examples = examples["C4_k2"]
assert {
    tuple(x["coloring"])
    for x in c4_examples
} == {
    (0, 1, 0, 1),
    (1, 0, 1, 0),
}

result = {
    "audit": "PRE_TIME_ORIENTATION_DOUBLET_V1",
    "status": "PASS",
    "rows": rows,
    "c4_binary": c4_binary,
    "c4_binary_examples": c4_examples,
    "interpretation": [
        "A marked finite structure can determine one acyclic orientation class modulo global reversal without choosing a polarity.",
        "The graphA C4 skeleton has exactly two binary colorings with this property: the complementary alternating bipartitions.",
        "The finite criterion is only structurally analogous to Lorentzian time orientability."
    ],
    "nonclaims": [
        "No Lorentzian metric, light cone, duration, dimension, or physical time is derived.",
        "The orientation doublet is a project-specific finite governance criterion, not a claimed new theorem of geometry."
    ]
}

print(json.dumps(result, indent=2))
