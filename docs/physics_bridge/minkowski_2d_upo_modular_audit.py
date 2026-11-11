#!/usr/bin/env python3
"""Exact modular UPO classification for finite random 2-orders, N<=9.

Uses the classical connected UPO characterization:
a connected comparability graph is UPO iff every nontrivial module/partitive
set is stable.

For a disconnected graph, exactly one component may contain edges if the full
graph is to have exactly two transitive orientations; isolated vertices do not
add orientation freedom.

No Monte Carlo sampling is used.
"""

import itertools
import json
import math
from collections import Counter
from fractions import Fraction


def adjacency_masks(pi):
    n = len(pi)
    adj = [0] * n
    edge_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if pi[i] < pi[j]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
                edge_count += 1

    return adj, edge_count


def component_masks(n, adj):
    unseen = (1 << n) - 1
    result = []

    while unseen:
        bit = unseen & -unseen
        start = bit.bit_length() - 1
        unseen ^= bit
        stack = [start]
        comp = 0

        while stack:
            u = stack.pop()
            comp |= 1 << u
            neighbors = adj[u] & unseen

            while neighbors:
                b = neighbors & -neighbors
                v = b.bit_length() - 1
                neighbors ^= b
                unseen ^= b
                stack.append(v)

        result.append(comp)

    return result


def has_nonstable_module(component, adj):
    vertices = [
        i
        for i in range(len(adj))
        if (component >> i) & 1
    ]

    subset = (component - 1) & component
    while subset:
        size = subset.bit_count()
        if 2 <= size < len(vertices):
            # Skip stable subsets immediately.
            if any(adj[u] & subset for u in vertices if (subset >> u) & 1):
                outside = component & ~subset
                valid = True

                while outside:
                    bit = outside & -outside
                    x = bit.bit_length() - 1
                    outside ^= bit

                    count = (adj[x] & subset).bit_count()
                    if count not in (0, size):
                        valid = False
                        break

                if valid:
                    return True

        subset = (subset - 1) & component

    return False


def minimum_nonstable_module_size(component, adj):
    vertices = [
        i
        for i in range(len(adj))
        if (component >> i) & 1
    ]

    for size in range(2, len(vertices)):
        for chosen in itertools.combinations(vertices, size):
            module = sum(1 << x for x in chosen)

            # Stable sets contain no internal edge.
            if not any(adj[u] & module for u in chosen):
                continue

            outside = component & ~module
            valid = True

            while outside:
                bit = outside & -outside
                x = bit.bit_length() - 1
                outside ^= bit

                count = (adj[x] & module).bit_count()
                if count not in (0, size):
                    valid = False
                    break

            if valid:
                return size

    return None


summary = {}

for n in range(2, 10):
    categories = Counter()
    minimum_bad_module_histogram = Counter()

    for pi in itertools.permutations(range(n)):
        adj, edge_count = adjacency_masks(pi)

        if edge_count == 0:
            categories["empty_antichain"] += 1
            continue

        components = component_masks(n, adj)
        nontrivial = [
            comp
            for comp in components
            if comp.bit_count() >= 2
        ]

        if len(nontrivial) >= 2:
            categories["multiple_nontrivial_components"] += 1
            continue

        if n <= 8:
            bad_size = minimum_nonstable_module_size(
                nontrivial[0],
                adj,
            )
            has_bad_module = bad_size is not None
        else:
            bad_size = None
            has_bad_module = has_nonstable_module(
                nontrivial[0],
                adj,
            )

        if not has_bad_module:
            categories["upo_recoverable"] += 1
        else:
            categories["internal_module_ambiguity"] += 1
            if bad_size is not None:
                minimum_bad_module_histogram[str(bad_size)] += 1

    total = math.factorial(n)
    upo = categories["upo_recoverable"]
    recovery = Fraction(upo, total)

    summary[str(n)] = {
        "permutations": total,
        "upo_recoverable": upo,
        "internal_module_ambiguity": (
            categories["internal_module_ambiguity"]
        ),
        "multiple_nontrivial_components": (
            categories["multiple_nontrivial_components"]
        ),
        "empty_antichain": categories["empty_antichain"],
        "recovery_fraction": str(recovery),
        "recovery_decimal": float(recovery),
        "minimum_bad_module_size_histogram": (
            dict(sorted(minimum_bad_module_histogram.items()))
            if n <= 8
            else None
        ),
    }

expected_upo = {
    "2": 1,
    "3": 4,
    "4": 12,
    "5": 38,
    "6": 165,
    "7": 1042,
    "8": 8464,
    "9": 80020,
}

for n, expected in expected_upo.items():
    assert summary[n]["upo_recoverable"] == expected
    assert (
        summary[n]["upo_recoverable"]
        + summary[n]["internal_module_ambiguity"]
        + summary[n]["multiple_nontrivial_components"]
        + summary[n]["empty_antichain"]
        == summary[n]["permutations"]
    )

# Regression against the previous direct-orientation enumeration.
for n, expected in {
    "2": "1/2",
    "3": "2/3",
    "4": "1/2",
    "5": "19/60",
    "6": "11/48",
    "7": "521/2520",
}.items():
    assert summary[n]["recovery_fraction"] == expected

assert summary["8"]["recovery_fraction"] == "529/2520"
assert summary["9"]["recovery_fraction"] == "4001/18144"

result = {
    "audit": "MINKOWSKI_2D_UPO_MODULAR_V1",
    "status": "PASS",
    "n_range": [2, 9],
    "summary": summary,
    "exact_conclusions": [
        "The classical modular UPO criterion exactly reproduces the previous direct-orientation UPO counts through N=7.",
        "Exact enumeration extends the random-2-order recovery statistic to N=8 and N=9.",
        "The finite recovery fraction is not monotone: it rises at N=8 and again at N=9.",
        "Internal non-stable modules are the dominant failure mode in the audited range.",
        "Minimum bad-module sizes were exhaustively classified through N=8; N=9 was classified for UPO/failure type without the extra minimum-size pass."
    ],
    "nonclaims": [
        "No asymptotic limit is inferred from N<=9.",
        "The UPO/module characterization is classical graph theory.",
        "The standard causal-set primitive remains the directed partial order.",
        "No claim is made that physical causal sets generically permit orientation recovery from symmetric connectibility."
    ]
}

print(json.dumps(result, indent=2))
