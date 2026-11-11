#!/usr/bin/env python3
"""Exact UPO recovery audit for finite random 2D orders, N<=7.

After fixing one random total order to the identity, the relative second order
is a uniform permutation. The product order is:
    i <_P j iff i<j and pi[i]<pi[j].

The script forgets orientation, enumerates all transitive orientations of the
comparability graph (stopping after the third when only UPO status is needed),
and records exact nontrivial UPO recovery counts.

No Monte Carlo sampling is used.
"""

import itertools
import json
import math
from collections import deque
from fractions import Fraction


def graph_edges(pi):
    n = len(pi)
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if pi[i] < pi[j]
    ]


def orientation(edges, bits):
    return {
        (u, v) if bits[k] else (v, u)
        for k, (u, v) in enumerate(edges)
    }


def transitive(oriented):
    for u, v in oriented:
        for v2, w in oriented:
            if v2 == v and (u, w) not in oriented:
                return False
    return True


def transitive_orientation_count_up_to_three(edges):
    count = 0
    witness = None

    for bits in itertools.product((False, True), repeat=len(edges)):
        oriented = orientation(edges, bits)
        if not transitive(oriented):
            continue
        count += 1
        if witness is None:
            witness = oriented
        if count >= 3:
            return count, witness

    return count, witness


def longest_path(n, oriented):
    adjacency = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in oriented:
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

for n in range(2, 8):
    upo_count = 0
    selfdual_empty_count = 0
    depth_histogram = {}

    for pi in itertools.permutations(range(n)):
        edges = graph_edges(pi)

        if not edges:
            selfdual_empty_count += 1
            continue

        count, witness = transitive_orientation_count_up_to_three(edges)

        if count == 2:
            upo_count += 1
            depth = longest_path(n, witness)
            key = str(depth)
            depth_histogram[key] = depth_histogram.get(key, 0) + 1

    total = math.factorial(n)
    fraction = Fraction(upo_count, total)

    summary[str(n)] = {
        "permutations": total,
        "nontrivial_upo": upo_count,
        "selfdual_empty_antichain": selfdual_empty_count,
        "nontrivial_upo_fraction": str(fraction),
        "nontrivial_upo_decimal": float(fraction),
        "upo_depth_histogram": depth_histogram,
    }

expected = {
    "2": (1, "1/2"),
    "3": (4, "2/3"),
    "4": (12, "1/2"),
    "5": (38, "19/60"),
    "6": (165, "11/48"),
    "7": (1042, "521/2520"),
}

for n, (count, fraction) in expected.items():
    assert summary[n]["nontrivial_upo"] == count
    assert summary[n]["nontrivial_upo_fraction"] == fraction
    assert summary[n]["selfdual_empty_antichain"] == 1

result = {
    "audit": "MINKOWSKI_2D_UPO_RECOVERY_V1",
    "status": "PASS",
    "n_range": [2, 7],
    "summary": summary,
    "controls": {
        "identity_permutation": (
            "total chain; comparability graph K_n; n! transitive orientations"
        ),
        "reverse_permutation": (
            "antichain; empty comparability graph; one self-dual empty orientation"
        ),
    },
    "nonclaims": [
        "No asymptotic conclusion is inferred from N<=7.",
        "The standard causal-set primitive is the directed partial order, not the unoriented comparability graph.",
        "No claim is made that physical causal sets are generically UPO.",
        "No exact prior for this combined UPO/random-2-order recovery statistic was located in the targeted search; priority is not certified."
    ],
}

print(json.dumps(result, indent=2))
