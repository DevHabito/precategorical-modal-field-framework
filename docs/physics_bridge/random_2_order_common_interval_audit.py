#!/usr/bin/env python3
"""Independent common-interval regression for random-2-order UPO recovery.

For each relative permutation through N=9:
1. build the increasing-pair comparability graph;
2. require exactly one nontrivial connected component;
3. restrict and renormalize the relative permutation to that component;
4. reject if any proper common interval is not decreasing.

The expected UPO counts are compared with the independent modular audit.
"""

import itertools
import json
import math
from fractions import Fraction


def adjacency(pi):
    n = len(pi)
    result = [set() for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if pi[i] < pi[j]:
                result[i].add(j)
                result[j].add(i)

    return result


def components(adj):
    unseen = set(range(len(adj)))
    result = []

    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        comp = []

        while stack:
            u = stack.pop()
            comp.append(u)

            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v)
                    stack.append(v)

        result.append(sorted(comp))

    return result


def induced_relative_permutation(pi, vertices):
    vertices = sorted(vertices)
    values = [pi[v] for v in vertices]
    rank = {
        value: index
        for index, value in enumerate(sorted(values))
    }
    return tuple(rank[value] for value in values)


def has_non_decreasing_proper_common_interval(pi):
    n = len(pi)

    for left in range(n):
        minimum = maximum = pi[left]
        values = []

        for right in range(left, n):
            value = pi[right]
            values.append(value)
            minimum = min(minimum, value)
            maximum = max(maximum, value)
            size = right - left + 1

            if not (2 <= size < n):
                continue

            if maximum - minimum + 1 != size:
                continue

            decreasing = all(
                values[i] > values[j]
                for i in range(size)
                for j in range(i + 1, size)
            )

            if not decreasing:
                return True

    return False


def recoverable(pi):
    adj = adjacency(pi)

    if not any(adj):
        return False

    nontrivial = [
        comp
        for comp in components(adj)
        if len(comp) >= 2
    ]

    if len(nontrivial) != 1:
        return False

    induced = induced_relative_permutation(
        pi,
        nontrivial[0],
    )

    return not has_non_decreasing_proper_common_interval(
        induced
    )


expected = {
    2: 1,
    3: 4,
    4: 12,
    5: 38,
    6: 165,
    7: 1042,
    8: 8464,
    9: 80020,
}

summary = {}

for n in range(2, 10):
    count = sum(
        recoverable(pi)
        for pi in itertools.permutations(range(n))
    )

    assert count == expected[n]

    fraction = Fraction(count, math.factorial(n))

    summary[str(n)] = {
        "permutations": math.factorial(n),
        "recoverable": count,
        "fraction": str(fraction),
        "decimal": float(fraction),
    }

result = {
    "audit": "RANDOM_2_ORDER_COMMON_INTERVAL_V1",
    "status": "PASS",
    "n_range": [2, 9],
    "summary": summary,
    "comparison": {
        "independent_modular_audit": "exact match through N=9",
        "discrepancy_count": 0,
    },
    "nonclaims": [
        "The graph/module and common-interval theories are classical.",
        "No asymptotic formula is claimed.",
        "No physical causal interpretation follows from the permutation characterization alone."
    ],
}

print(json.dumps(result, indent=2))
