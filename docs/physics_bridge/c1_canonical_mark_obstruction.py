#!/usr/bin/env python3
"""Exact automorphism-orbit and invariant-mark audit for the C1 skeletons."""

import itertools
import json

V = tuple(range(5))

GRAPHS = {
    "graphA": {(0, 2), (2, 3), (3, 4), (4, 0)},
    "graphB": {(0, 2), (2, 3), (3, 0), (1, 4)},
}


def canonical_edges(edges):
    return {tuple(sorted(e)) for e in edges}


def automorphisms(edges):
    edge_set = canonical_edges(edges)
    result = []

    for p in itertools.permutations(V):
        image = {
            tuple(sorted((p[u], p[v])))
            for u, v in edge_set
        }
        if image == edge_set:
            result.append(p)

    return result


def orbits(autos):
    unseen = set(V)
    result = []

    while unseen:
        start = min(unseen)
        orbit = {p[start] for p in autos}
        result.append(sorted(orbit))
        unseen -= orbit

    return result


def invariant_colorings(autos, alphabet):
    result = []

    for coloring in itertools.product(range(alphabet), repeat=len(V)):
        invariant = all(
            all(
                coloring[p[v]] == coloring[v]
                for v in V
            )
            for p in autos
        )
        if invariant:
            result.append(list(coloring))

    return result


rows = {}

for name, edges in GRAPHS.items():
    autos = automorphisms(edges)
    orbit_list = orbits(autos)
    binary = invariant_colorings(autos, 2)

    assert len(autos) == (8 if name == "graphA" else 12)
    assert len(binary) == 4

    rows[name] = {
        "automorphism_count": len(autos),
        "vertex_orbits": orbit_list,
        "binary_coloring_count": 2 ** len(V),
        "fully_automorphism_invariant_binary_colorings": binary,
        "invariant_binary_coloring_count": len(binary),
    }

assert rows["graphA"]["vertex_orbits"] == [[0, 2, 3, 4], [1]]
assert rows["graphB"]["vertex_orbits"] == [[0, 2, 3], [1, 4]]

graphA_alternating = {
    (0, 1, 0, 1),  # cycle order 0,2,3,4
    (1, 0, 1, 0),
}

for coloring in rows["graphA"]["fully_automorphism_invariant_binary_colorings"]:
    cycle_pattern = (
        coloring[0],
        coloring[2],
        coloring[3],
        coloring[4],
    )
    assert cycle_pattern not in graphA_alternating

result = {
    "audit": "C1_CANONICAL_MARK_OBSTRUCTION_V1",
    "status": "PASS",
    "graphs": rows,
    "exact_conclusions": [
        "Canonical isomorphism-invariant vertex marks are constant on automorphism orbits.",
        "All four graphA cycle vertices lie in one automorphism orbit.",
        "No fully automorphism-invariant binary mark on graphA yields the alternating cycle pattern required by the audited orientation doublet.",
        "The graphB triangle vertices form one orbit and the isolated-edge endpoints form another."
    ],
    "nonclaims": [
        "This does not forbid an independently supplied physical mark.",
        "No physical origin for such a mark is established."
    ]
}

print(json.dumps(result, indent=2))
