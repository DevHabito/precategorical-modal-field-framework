#!/usr/bin/env python3
"""Exact minimal deep-UPO classification through n=5."""

import itertools
import json
from collections import deque


def edges(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def connected(n, E):
    adj = [[] for _ in range(n)]
    for u, v in E:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def orient(E, bits):
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


def longest_path(n, O):
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in O:
        adj[u].append(v)
        indeg[v] += 1
    q = deque(i for i, d in enumerate(indeg) if d == 0)
    dist = [0] * n
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in adj[u]:
            dist[v] = max(dist[v], dist[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    assert seen == n
    return max(dist)


def permutation_image(E, p):
    return {
        tuple(sorted((p[u], p[v])))
        for u, v in E
    }


def automorphism_count(n, E):
    target = {tuple(sorted(e)) for e in E}
    return sum(
        permutation_image(E, p) == target
        for p in itertools.permutations(range(n))
    )


def isomorphic(n, E1, E2):
    target = {tuple(sorted(e)) for e in E2}
    return any(
        permutation_image(E1, p) == target
        for p in itertools.permutations(range(n))
    )


BULL = {(0,1),(0,2),(1,2),(1,3),(2,4)}
HOUSE = {(0,1),(0,2),(1,3),(2,3),(2,4),(3,4)}

summary = {}
deep5 = []

for n in range(2, 6):
    pairs = edges(n)
    connected_count = 0
    upo_count = 0
    deep_count = 0
    depth_hist = {}

    for mask in range(1 << len(pairs)):
        E = [
            pairs[k]
            for k in range(len(pairs))
            if (mask >> k) & 1
        ]
        if not connected(n, E):
            continue
        connected_count += 1

        TO = []
        for bits in itertools.product((False, True), repeat=len(E)):
            O = orient(E, bits)
            if transitive(O):
                TO.append(O)

        if len(TO) != 2:
            continue

        upo_count += 1
        depth = longest_path(n, TO[0])
        depth_hist[str(depth)] = depth_hist.get(str(depth), 0) + 1

        if depth >= 2:
            deep_count += 1
            if n == 5:
                deep5.append(E)

    summary[str(n)] = {
        "connected_labeled_graphs": connected_count,
        "upo_graphs": upo_count,
        "upo_depth_at_least_2": deep_count,
        "depth_histogram": depth_hist,
    }

assert len(deep5) == 120

bull_count = sum(isomorphic(5, E, BULL) for E in deep5)
house_count = sum(isomorphic(5, E, HOUSE) for E in deep5)

assert bull_count == 60
assert house_count == 60
assert bull_count + house_count == len(deep5)
assert automorphism_count(5, list(BULL)) == 2
assert automorphism_count(5, list(HOUSE)) == 2

result = {
    "audit": "MINIMAL_DEEP_UPO_V1",
    "status": "PASS",
    "summary": summary,
    "minimal_depth_two_vertex_count": 5,
    "depth_two_unlabeled_types": {
        "bull": {
            "labeled_count": bull_count,
            "edge_count": len(BULL),
            "automorphism_count": 2,
            "degree_multiset": [1,1,2,3,3],
        },
        "house": {
            "labeled_count": house_count,
            "edge_count": len(HOUSE),
            "automorphism_count": 2,
            "degree_multiset": [2,2,2,3,3],
        },
    },
    "nonclaims": [
        "UPO theory is classical.",
        "The finite classification is a project control calculation, not a novelty claim.",
        "No physical temporal semantics follows from the UPO property."
    ],
}

print(json.dumps(result, indent=2))
