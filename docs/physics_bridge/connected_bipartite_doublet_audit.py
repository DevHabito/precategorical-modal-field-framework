#!/usr/bin/env python3
"""Exhaustive connected-bipartite unique-coloring regression through n=6.

For every labeled simple graph on n=2,...,6:
- test connectedness;
- enumerate all binary colorings;
- if at least one proper coloring exists, assert exactly two exist and are
  global complements.

This reproduces the classical uniqueness of bipartition for connected
bipartite graphs.
"""

import itertools
import json


def connected(n, edges):
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)

    seen = {0}
    stack = [0]

    while stack:
        u = stack.pop()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)

    return len(seen) == n


def proper_binary_colorings(n, edges):
    result = []

    for coloring in itertools.product((0, 1), repeat=n):
        if all(coloring[u] != coloring[v] for u, v in edges):
            result.append(coloring)

    return result


counts = {}

for n in range(2, 7):
    possible_edges = [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
    ]

    connected_bipartite_count = 0

    for mask in range(1 << len(possible_edges)):
        edges = [
            possible_edges[k]
            for k in range(len(possible_edges))
            if (mask >> k) & 1
        ]

        if not connected(n, edges):
            continue

        colorings = proper_binary_colorings(n, edges)

        if not colorings:
            continue

        connected_bipartite_count += 1

        assert len(colorings) == 2
        assert tuple(1 - x for x in colorings[0]) == colorings[1]

    counts[str(n)] = connected_bipartite_count

assert counts == {
    "2": 1,
    "3": 3,
    "4": 19,
    "5": 195,
    "6": 3031,
}

result = {
    "audit": "CONNECTED_BIPARTITE_UNIQUE_DOUBLET_V1",
    "status": "PASS",
    "n_range": [2, 6],
    "connected_labeled_bipartite_counts": counts,
    "property_checked": (
        "every connected bipartite graph has exactly two proper binary "
        "colorings, related by global complement"
    ),
    "graphA_C4_bipartition": [[0, 3], [2, 4]],
    "nonclaims": [
        "Classical graph theorem regression; not a new combinatorial theorem.",
        "No physical temporal meaning is assigned to the bipartition."
    ]
}

print(json.dumps(result, indent=2))
