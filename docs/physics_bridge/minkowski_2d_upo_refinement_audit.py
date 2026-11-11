#!/usr/bin/env python3
"""Exact one-point refinement transitions for random 2D-order UPO status.

For a relative permutation pi of size n, a new independent point has an
equiprobable insertion rank in each of the two light-cone coordinate orders.
After fixing the first order to identity, this is represented by inserting a
new permutation value j at position i, with (i,j) uniform on
{0,...,n}^2.

All parent permutations are enumerated for n=2,...,6.
"""

import itertools
import json
import math
from fractions import Fraction


def edges(pi):
    n = len(pi)
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if pi[i] < pi[j]
    ]


def orientation(E, bits):
    return {
        (u, v) if bits[k] else (v, u)
        for k, (u, v) in enumerate(E)
    }


def transitive(O):
    for u, v in O:
        for v2, w in O:
            if v2 == v and (u, w) not in O:
                return False
    return True


def is_nontrivial_upo(pi):
    E = edges(pi)
    if not E:
        return False

    count = 0
    for bits in itertools.product((False, True), repeat=len(E)):
        if transitive(orientation(E, bits)):
            count += 1
            if count >= 3:
                return False

    return count == 2


def insert_relative_permutation(pi, position, value):
    updated = [
        x + (1 if x >= value else 0)
        for x in pi
    ]
    updated.insert(position, value)
    return tuple(updated)


status = {}
for n in range(2, 8):
    status[n] = {
        pi: is_nontrivial_upo(pi)
        for pi in itertools.permutations(range(n))
    }


summary = {}

for n in range(2, 7):
    counts = {
        "U_to_U": 0,
        "U_to_N": 0,
        "N_to_U": 0,
        "N_to_N": 0,
    }

    parent_count = {
        "U": 0,
        "N": 0,
    }

    upo_child_ranges = {
        "U": [],
        "N": [],
    }

    for pi, parent_upo in status[n].items():
        parent_key = "U" if parent_upo else "N"
        parent_count[parent_key] += 1
        upo_children = 0

        for position in range(n + 1):
            for value in range(n + 1):
                child = insert_relative_permutation(
                    pi,
                    position,
                    value,
                )
                child_upo = status[n + 1][child]

                if child_upo:
                    upo_children += 1

                transition = (
                    ("U" if parent_upo else "N")
                    + "_to_"
                    + ("U" if child_upo else "N")
                )
                counts[transition] += 1

        upo_child_ranges[parent_key].append(
            upo_children
        )

    denominator_u = (
        parent_count["U"] * (n + 1) ** 2
    )
    denominator_n = (
        parent_count["N"] * (n + 1) ** 2
    )

    p_u_given_u = Fraction(
        counts["U_to_U"],
        denominator_u,
    )
    p_u_given_n = Fraction(
        counts["N_to_U"],
        denominator_n,
    )

    summary[str(n)] = {
        "parent_size": n,
        "child_size": n + 1,
        "parent_counts": parent_count,
        "transition_counts": counts,
        "P_child_U_given_parent_U": str(
            p_u_given_u
        ),
        "P_child_U_given_parent_N": str(
            p_u_given_n
        ),
        "U_parent_upo_child_count_min": min(
            upo_child_ranges["U"]
        ),
        "U_parent_upo_child_count_max": max(
            upo_child_ranges["U"]
        ),
        "child_insertions_per_parent": (
            (n + 1) ** 2
        ),
    }


expected = {
    "2": ("2/3", "2/3", 6, 6),
    "3": ("9/16", "3/8", 9, 9),
    "4": ("8/15", "1/10", 12, 15),
    "5": ("32/57", "37/492", 15, 24),
    "6": ("146/231", "104/1295", 18, 35),
}

for n, values in expected.items():
    row = summary[n]
    assert (
        row["P_child_U_given_parent_U"],
        row["P_child_U_given_parent_N"],
        row["U_parent_upo_child_count_min"],
        row["U_parent_upo_child_count_max"],
    ) == values

result = {
    "audit": "MINKOWSKI_2D_UPO_REFINEMENT_V1",
    "status": "PASS",
    "parent_size_range": [2, 6],
    "summary": summary,
    "exact_conclusions": [
        "Nontrivial UPO status is not invariant under one-point random-2-order refinement.",
        "Both UPO-to-non-UPO and non-UPO-to-UPO transitions occur.",
        "From n=3 onward in the audited range, a UPO parent has a larger conditional UPO-child probability than a non-UPO parent.",
        "UPO-parent refinement robustness varies across individual permutations."
    ],
    "nonclaims": [
        "No asymptotic convergence is claimed.",
        "No continuum time-orientation result is established.",
        "UPO is treated only as a finite orientation-recovery diagnostic."
    ],
}

print(json.dumps(result, indent=2))
