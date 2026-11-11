#!/usr/bin/env python3
"""Exact Aigner-Prins sufficient-condition coverage for random 2D UPO orders.

AP2:
  at most one nontrivial connected component and triangle-free.

AP5:
  graph connected, complement connected, complement has no induced K1,3.

UPO status is computed through classical implication classes:
nonempty graph is UPO iff it has one inverse implication-class pair.
"""

import itertools
import json
import math
from collections import defaultdict


class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(
                self.parent[x]
            )
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.parent[b] = a


def comparability_edges(pi):
    n = len(pi)
    return {
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if pi[i] < pi[j]
    }


def components(n, edges):
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)

    unseen = set(range(n))
    result = []

    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        component = []

        while stack:
            u = stack.pop()
            component.append(u)
            for v in adjacency[u]:
                if v in unseen:
                    unseen.remove(v)
                    stack.append(v)

        result.append(component)

    return result


def connected(n, edges):
    return len(components(n, edges)) == 1


def triangle_free(n, edges):
    E = set(edges)

    for a, b, c in itertools.combinations(
        range(n),
        3,
    ):
        if (
            tuple(sorted((a, b))) in E
            and tuple(sorted((a, c))) in E
            and tuple(sorted((b, c))) in E
        ):
            return False

    return True


def complement(n, edges):
    E = set(edges)
    return {
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if (i, j) not in E
    }


def induced_claw_exists(n, edges):
    E = set(edges)

    def adjacent(a, b):
        return tuple(sorted((a, b))) in E

    for center in range(n):
        neighbors = [
            v
            for v in range(n)
            if (
                v != center
                and adjacent(center, v)
            )
        ]

        for leaves in itertools.combinations(
            neighbors,
            3,
        ):
            if all(
                not adjacent(a, b)
                for a, b
                in itertools.combinations(
                    leaves,
                    2,
                )
            ):
                return True

    return False


def implication_pair_count(n, edges):
    if not edges:
        return 0

    E = {
        tuple(sorted(edge))
        for edge in edges
    }

    def adjacent(a, b):
        if a == b:
            return False
        return tuple(sorted((a, b))) in E

    directed = []
    for u, v in sorted(E):
        directed.extend(
            [(u, v), (v, u)]
        )

    uf = UnionFind(directed)

    for index, (a, b) in enumerate(
        directed
    ):
        for c, d in directed[
            index + 1:
        ]:
            if (
                a == c
                and not adjacent(b, d)
            ) or (
                b == d
                and not adjacent(a, c)
            ):
                uf.union(
                    (a, b),
                    (c, d),
                )

    classes = defaultdict(list)

    for edge in directed:
        classes[
            uf.find(edge)
        ].append(edge)

    assert len(classes) % 2 == 0
    return len(classes) // 2


def AP2(n, edges):
    nontrivial_components = sum(
        len(component) > 1
        for component
        in components(n, edges)
    )

    return (
        nontrivial_components <= 1
        and triangle_free(n, edges)
    )


def AP5(n, edges):
    comp = complement(n, edges)

    return (
        connected(n, edges)
        and connected(n, comp)
        and not induced_claw_exists(
            n,
            comp,
        )
    )


summary = {}

for n in range(2, 9):
    upo = 0
    ap2 = 0
    ap5 = 0
    both = 0
    union = 0

    for pi in itertools.permutations(
        range(n)
    ):
        edges = comparability_edges(pi)

        if (
            not edges
            or implication_pair_count(
                n,
                edges,
            ) != 1
        ):
            continue

        upo += 1

        condition2 = AP2(n, edges)
        condition5 = AP5(n, edges)

        ap2 += condition2
        ap5 += condition5
        both += (
            condition2 and condition5
        )
        union += (
            condition2 or condition5
        )

    summary[str(n)] = {
        "upo": upo,
        "AP2": ap2,
        "AP5": ap5,
        "both": both,
        "AP2_or_AP5": union,
    }


expected = {
    "2": [1, 1, 0, 0, 1],
    "3": [4, 4, 0, 0, 4],
    "4": [12, 12, 2, 2, 12],
    "5": [38, 34, 14, 10, 38],
    "6": [165, 98, 67, 37, 128],
    "7": [1042, 294, 269, 126, 437],
    "8": [8464, 919, 977, 422, 1474],
}

for n, values in expected.items():
    row = summary[n]
    assert [
        row["upo"],
        row["AP2"],
        row["AP5"],
        row["both"],
        row["AP2_or_AP5"],
    ] == values


result = {
    "audit": "AIGNER_PRINS_RANDOM_2D_COVERAGE_V1",
    "status": "PASS",
    "n_range": [2, 8],
    "summary": summary,
    "nonclaims": [
        "AP2 and AP5 are classical sufficient conditions, not project results.",
        "Failure of these sufficient conditions does not imply failure of UPO.",
        "No asymptotic conclusion is inferred."
    ],
}

print(
    json.dumps(
        result,
        indent=2,
    )
)
