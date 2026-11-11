#!/usr/bin/env python3
"""Exhaustive intrinsic orientation-class audit for connected graphs n<=5.

A reversal class [O] = {O, O^op} is automorphism-canonical when every graph
automorphism maps O either to O or to O^op.

A graph passes uniqueness when exactly one such acyclic reversal class exists.
The audit also records the longest directed-path length in that class.
"""

import itertools
import json
from collections import deque


def edge_list(n):
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
    ]


def edges_from_mask(n, mask):
    pairs = edge_list(n)
    return [
        pairs[k]
        for k in range(len(pairs))
        if (mask >> k) & 1
    ]


def connected(n, edges):
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)

    seen = {0}
    stack = [0]

    while stack:
        u = stack.pop()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)

    return len(seen) == n


def automorphisms(n, edges):
    edge_set = {tuple(sorted(e)) for e in edges}
    result = []

    for p in itertools.permutations(range(n)):
        image = {
            tuple(sorted((p[u], p[v])))
            for u, v in edge_set
        }
        if image == edge_set:
            result.append(p)

    return result


def oriented_edges(edges, bits):
    return {
        (u, v) if bits[k] else (v, u)
        for k, (u, v) in enumerate(edges)
    }


def reverse(orientation):
    return {
        (v, u)
        for u, v in orientation
    }


def apply_automorphism(orientation, p):
    return {
        (p[u], p[v])
        for u, v in orientation
    }


def acyclic(n, orientation):
    adjacency = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in orientation:
        adjacency[u].append(v)
        indegree[v] += 1

    queue = deque(
        i for i, degree in enumerate(indegree)
        if degree == 0
    )
    visited = 0

    while queue:
        u = queue.popleft()
        visited += 1
        for v in adjacency[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return visited == n


def longest_directed_path(n, orientation):
    adjacency = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in orientation:
        adjacency[u].append(v)
        indegree[v] += 1

    queue = deque(
        i for i, degree in enumerate(indegree)
        if degree == 0
    )
    distance = [0] * n

    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            distance[v] = max(
                distance[v],
                distance[u] + 1,
            )
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return max(distance)


def orientation_key(orientation):
    return tuple(sorted(orientation))


def reversal_class_key(orientation):
    first = orientation_key(orientation)
    second = orientation_key(reverse(orientation))
    return tuple(sorted((first, second)))


summary = {}
diamond_examples = []

for n in range(2, 6):
    connected_count = 0
    unique_class_count = 0
    deep_unique_count = 0
    depth_histogram = {}

    for mask in range(1 << len(edge_list(n))):
        edges = edges_from_mask(n, mask)

        if not connected(n, edges):
            continue

        connected_count += 1
        autos = automorphisms(n, edges)
        canonical_classes = {}

        for bits in itertools.product(
            (False, True),
            repeat=len(edges),
        ):
            orientation = oriented_edges(
                edges,
                bits,
            )

            if not acyclic(n, orientation):
                continue

            reversed_orientation = reverse(
                orientation
            )

            if all(
                apply_automorphism(
                    orientation,
                    p,
                )
                in (
                    orientation,
                    reversed_orientation,
                )
                for p in autos
            ):
                canonical_classes[
                    reversal_class_key(
                        orientation
                    )
                ] = orientation

        if len(canonical_classes) != 1:
            continue

        unique_class_count += 1
        orientation = next(
            iter(canonical_classes.values())
        )
        depth = longest_directed_path(
            n,
            orientation,
        )
        depth_histogram[str(depth)] = (
            depth_histogram.get(
                str(depth),
                0,
            )
            + 1
        )

        if depth >= 2:
            deep_unique_count += 1

            if n == 4:
                diamond_examples.append({
                    "edges": [list(e) for e in edges],
                    "automorphism_count": len(autos),
                    "depth": depth,
                    "orientation": [
                        list(e)
                        for e in sorted(
                            orientation
                        )
                    ],
                })

    summary[str(n)] = {
        "connected_labeled_graphs": connected_count,
        "unique_canonical_reversal_class": unique_class_count,
        "unique_class_depth_at_least_2": deep_unique_count,
        "depth_histogram": depth_histogram,
    }

assert summary == {
    "2": {
        "connected_labeled_graphs": 1,
        "unique_canonical_reversal_class": 1,
        "unique_class_depth_at_least_2": 0,
        "depth_histogram": {"1": 1},
    },
    "3": {
        "connected_labeled_graphs": 4,
        "unique_canonical_reversal_class": 0,
        "unique_class_depth_at_least_2": 0,
        "depth_histogram": {},
    },
    "4": {
        "connected_labeled_graphs": 38,
        "unique_canonical_reversal_class": 13,
        "unique_class_depth_at_least_2": 6,
        "depth_histogram": {"1": 7, "2": 6},
    },
    "5": {
        "connected_labeled_graphs": 728,
        "unique_canonical_reversal_class": 30,
        "unique_class_depth_at_least_2": 25,
        "depth_histogram": {"1": 5, "2": 25},
    },
}

assert len(diamond_examples) == 6
assert all(
    len(example["edges"]) == 5
    for example in diamond_examples
)

result = {
    "audit": "INTRINSIC_ORIENTATION_DEPTH_V1",
    "status": "PASS",
    "n_range": [2, 5],
    "summary": summary,
    "minimal_deep_witness": "diamond graph K4-e",
    "labeled_diamond_witness_count": len(
        diamond_examples
    ),
    "diamond_examples": diamond_examples,
    "nonclaims": [
        "The automorphism-canonical reversal-class criterion is project-specific terminology.",
        "No physical causal or temporal interpretation follows from the finite graph result.",
        "No novelty claim is made for elementary properties of the diamond graph."
    ]
}

print(json.dumps(result, indent=2))
