#!/usr/bin/env python3
"""Exact invariant-acyclic-orientation audit for marked cycles."""

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
    # A simple undirected cycle contains a directed cycle exactly when all
    # edges are coherently clockwise or all coherently counterclockwise.
    return not (all(bits) or not any(bits))


rows = []

for n in range(3, 9):
    automorphisms = dihedral(n)
    acyclic_orientations = [
        bits
        for bits in itertools.product((False, True), repeat=n)
        if acyclic_cycle_orientation(bits)
    ]

    for k in range(1, 4):
        admissible_coloring_count = 0
        total_invariant_acyclic_orientations = 0

        for coloring in itertools.product(range(k), repeat=n):
            stabilizer = [
                p for p in automorphisms
                if preserves_coloring(coloring, p)
            ]

            valid = []
            for bits in acyclic_orientations:
                edges = directed_edges(n, bits)
                if all(
                    orientation_invariant(edges, p)
                    for p in stabilizer
                ):
                    valid.append(bits)

            if valid:
                admissible_coloring_count += 1
                total_invariant_acyclic_orientations += len(valid)

                # Global reversal must remain valid.
                for bits in valid:
                    reverse = tuple(not b for b in bits)
                    assert reverse in valid

        rows.append({
            "n": n,
            "alphabet": k,
            "coloring_count": k ** n,
            "colorings_with_invariant_acyclic_orientation": admissible_coloring_count,
            "total_invariant_acyclic_orientations": total_invariant_acyclic_orientations,
        })

c4_binary = next(
    r for r in rows
    if r["n"] == 4 and r["alphabet"] == 2
)

assert c4_binary["colorings_with_invariant_acyclic_orientation"] == 10

result = {
    "audit": "MARKED_CYCLE_ORIENTABILITY_V1",
    "status": "PASS",
    "rows": rows,
    "c4_binary": c4_binary,
    "global_reversal_pairing_checked": True,
    "interpretation": [
        "Marked structures can admit an automorphism-invariant acyclic orientation without being fully distinguishing.",
        "Every invariant acyclic orientation is accompanied by its globally reversed invariant acyclic orientation.",
        "Static orientability therefore does not by itself supply physical polarity."
    ],
    "nonclaim": "Exact finite combinatorics only; no temporal meaning is assigned."
}

print(json.dumps(result, indent=2))
