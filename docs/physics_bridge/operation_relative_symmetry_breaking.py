#!/usr/bin/env python3
"""Exact operation-relative symmetry-breaking audit for cycle colorings."""

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
    automorphisms = list(dict.fromkeys(rotations + reflections))
    return automorphisms, rotations, reflections


def preserves(coloring, permutation):
    return all(
        coloring[i] == coloring[permutation[i]]
        for i in range(len(coloring))
    )


rows = []

for n in range(3, 9):
    aut, rotations, reflections = dihedral(n)

    for k in range(1, 4):
        pair_orienting = 0
        chirality_selecting = 0
        fully_distinguishing = 0

        for coloring in itertools.product(range(k), repeat=n):
            stabilizer = [p for p in aut if preserves(coloring, p)]

            pair_reversible = any(
                p[0] == 1 and p[1] == 0
                for p in stabilizer
            )
            reflection_survives = any(
                preserves(coloring, p)
                for p in reflections
            )

            if not pair_reversible:
                pair_orienting += 1
            if not reflection_survives:
                chirality_selecting += 1
            if len(stabilizer) == 1:
                fully_distinguishing += 1

        assert pair_orienting >= chirality_selecting
        assert chirality_selecting >= fully_distinguishing

        rows.append({
            "n": n,
            "alphabet": k,
            "coloring_count": k ** n,
            "pair_orienting_count": pair_orienting,
            "chirality_selecting_count": chirality_selecting,
            "fully_distinguishing_count": fully_distinguishing,
        })

c4_binary = next(
    row for row in rows
    if row["n"] == 4 and row["alphabet"] == 2
)
assert c4_binary["pair_orienting_count"] == 12
assert c4_binary["chirality_selecting_count"] == 0
assert c4_binary["fully_distinguishing_count"] == 0

result = {
    "audit": "OPERATION_RELATIVE_SYMMETRY_BREAKING_V1",
    "status": "PASS",
    "rows": rows,
    "c4_binary": c4_binary,
    "interpretation": [
        "A marked structure can orient a selected pair without selecting global cycle chirality.",
        "Cycle chirality can be selected while some non-reflection automorphism remains.",
        "Full distinguishing colorings are a stronger requirement than either task.",
        "The informational symmetry-breaking budget is operation-relative."
    ],
    "nonclaim": "Exact group-action enumeration only; marks are not assigned physical temporal meaning."
}

print(json.dumps(result, indent=2))
