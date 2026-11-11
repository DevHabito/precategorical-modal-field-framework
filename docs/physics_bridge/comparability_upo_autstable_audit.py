#!/usr/bin/env python3
"""Exact comparability/UPO/Aut-stable orientation audit through n=5."""

import itertools
import json
from collections import deque

def edge_list(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]

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
        image = {tuple(sorted((p[u], p[v]))) for u, v in edge_set}
        if image == edge_set:
            result.append(p)
    return result

def oriented_edges(edges, bits):
    return {(u, v) if bits[k] else (v, u) for k, (u, v) in enumerate(edges)}

def reverse(orientation):
    return {(v, u) for u, v in orientation}

def apply_automorphism(orientation, p):
    return {(p[u], p[v]) for u, v in orientation}

def reversal_class_key(orientation):
    first = tuple(sorted(orientation))
    second = tuple(sorted(reverse(orientation)))
    return min(first, second), max(first, second)

def is_transitive_orientation(orientation):
    for u, v in orientation:
        for v2, w in orientation:
            if v2 == v and (u, w) not in orientation:
                return False
    return True

def longest_path(n, orientation):
    adjacency = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in orientation:
        adjacency[u].append(v)
        indegree[v] += 1
    queue = deque(i for i, d in enumerate(indegree) if d == 0)
    distance = [0] * n
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in adjacency[u]:
            distance[v] = max(distance[v], distance[u] + 1)
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    assert visited == n
    return max(distance)

summary = {}
diamond_records = []

for n in range(2, 6):
    pairs = edge_list(n)
    connected_count = 0
    comparability_count = 0
    upo_count = 0
    unique_autstable_count = 0
    unique_autstable_deep_count = 0
    transitive_orientation_histogram = {}
    autstable_class_histogram = {}
    upo_depth_histogram = {}
    unique_autstable_depth_histogram = {}

    for mask in range(1 << len(pairs)):
        edges = [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1]
        if not connected(n, edges):
            continue
        connected_count += 1

        transitive = []
        for bits in itertools.product((False, True), repeat=len(edges)):
            orientation = oriented_edges(edges, bits)
            if is_transitive_orientation(orientation):
                transitive.append(orientation)

        if not transitive:
            continue

        comparability_count += 1
        key = str(len(transitive))
        transitive_orientation_histogram[key] = (
            transitive_orientation_histogram.get(key, 0) + 1
        )

        if len(transitive) == 2:
            assert transitive[1] == reverse(transitive[0])
            upo_count += 1
            depth = longest_path(n, transitive[0])
            key = str(depth)
            upo_depth_histogram[key] = upo_depth_histogram.get(key, 0) + 1

        autos = automorphisms(n, edges)
        autstable = {}

        for orientation in transitive:
            opposite = reverse(orientation)
            if all(
                apply_automorphism(orientation, p) in (orientation, opposite)
                for p in autos
            ):
                autstable[reversal_class_key(orientation)] = orientation

        key = str(len(autstable))
        autstable_class_histogram[key] = (
            autstable_class_histogram.get(key, 0) + 1
        )

        if len(autstable) != 1:
            continue

        unique_autstable_count += 1
        orientation = next(iter(autstable.values()))
        depth = longest_path(n, orientation)
        key = str(depth)
        unique_autstable_depth_histogram[key] = (
            unique_autstable_depth_histogram.get(key, 0) + 1
        )

        if depth >= 2:
            unique_autstable_deep_count += 1
            if n == 4:
                diamond_records.append({
                    "edges": [list(edge) for edge in edges],
                    "transitive_orientation_count": len(transitive),
                    "automorphism_count": len(autos),
                    "autstable_duality_class_count": len(autstable),
                    "depth": depth,
                    "orientation": [list(edge) for edge in sorted(orientation)],
                })

    summary[str(n)] = {
        "connected_labeled_graphs": connected_count,
        "comparability_graphs": comparability_count,
        "upo_graphs": upo_count,
        "exactly_one_autstable_duality_class": unique_autstable_count,
        "unique_autstable_class_depth_at_least_2": unique_autstable_deep_count,
        "transitive_orientation_count_histogram": transitive_orientation_histogram,
        "autstable_class_count_histogram": autstable_class_histogram,
        "upo_depth_histogram": upo_depth_histogram,
        "unique_autstable_depth_histogram": unique_autstable_depth_histogram,
    }

expected_core = {
    "2": (1, 1, 1, 1, 0),
    "3": (4, 4, 3, 3, 0),
    "4": (38, 38, 19, 25, 6),
    "5": (728, 716, 315, 340, 145),
}

for n, expected in expected_core.items():
    row = summary[n]
    observed = (
        row["connected_labeled_graphs"],
        row["comparability_graphs"],
        row["upo_graphs"],
        row["exactly_one_autstable_duality_class"],
        row["unique_autstable_class_depth_at_least_2"],
    )
    assert observed == expected

assert len(diamond_records) == 6
assert all(
    record["transitive_orientation_count"] == 6
    and record["automorphism_count"] == 4
    and record["autstable_duality_class_count"] == 1
    and record["depth"] == 2
    for record in diamond_records
)

result = {
    "audit": "COMPARABILITY_UPO_AUTSTABLE_V1",
    "status": "PASS",
    "n_range": [2, 5],
    "summary": summary,
    "n4_deep_autstable_records": diamond_records,
    "exact_conclusions": [
        "UPO and the project Aut-stable-duality criterion are not equivalent.",
        "Every UPO graph in the audited connected finite range has exactly one Aut-stable duality class.",
        "The diamond K4-e is not UPO: it has six transitive orientations.",
        "Each labeled diamond has exactly one transitive duality class fixed by the full graph automorphism action and that class has depth two."
    ],
    "nonclaims": [
        "Comparability graphs and UPO theory are classical.",
        "Automorphism actions on transitive orientations are classical structure.",
        "No mathematical novelty is claimed for the project selection criterion without a dedicated novelty audit.",
        "No physical causal interpretation follows from these finite graph counts."
    ]
}

print(json.dumps(result, indent=2))
