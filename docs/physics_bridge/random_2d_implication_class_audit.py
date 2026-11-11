#!/usr/bin/env python3
"""Exact implication-class ambiguity audit for random 2D orders, N<=8.

Uses the classical Golumbic forcing relation Gamma on directed versions of
undirected comparability edges. The transitive closure Gamma* gives implication
classes. For every nonempty comparability graph the classes are paired with
their inverses and k_Gamma = number_of_classes / 2.

The script also tracks k_Gamma under the exact one-point rank-insertion process.
"""

import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction


class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}
        self.rank = {x: 0 for x in items}

    def find(self, x):
        parent = self.parent[x]
        if parent != x:
            self.parent[x] = self.find(parent)
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


def comparability_edges(pi):
    n = len(pi)
    return {
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if pi[i] < pi[j]
    }


def implication_pair_count(n, undirected_edges):
    if not undirected_edges:
        return 0

    edge_set = {
        tuple(sorted(edge))
        for edge in undirected_edges
    }

    def adjacent(a, b):
        if a == b:
            return False
        return tuple(sorted((a, b))) in edge_set

    directed = []
    for u, v in sorted(edge_set):
        directed.append((u, v))
        directed.append((v, u))

    uf = UnionFind(directed)

    for index, first in enumerate(directed):
        a, b = first

        for second in directed[index + 1:]:
            c, d = second

            same_tail_forcing = (
                a == c
                and not adjacent(b, d)
            )
            same_head_forcing = (
                b == d
                and not adjacent(a, c)
            )

            if same_tail_forcing or same_head_forcing:
                uf.union(first, second)

    components = defaultdict(list)

    for edge in directed:
        components[
            uf.find(edge)
        ].append(edge)

    classes = list(
        components.values()
    )

    class_sets = {
        frozenset(component)
        for component in classes
    }

    for component in classes:
        inverse = frozenset(
            (v, u)
            for u, v in component
        )
        assert inverse in class_sets

    assert len(classes) % 2 == 0
    return len(classes) // 2


def insert_relative_permutation(
    pi,
    position,
    value,
):
    updated = [
        x + (1 if x >= value else 0)
        for x in pi
    ]
    updated.insert(position, value)
    return tuple(updated)


k_status = {}
distribution_summary = {}

for n in range(2, 9):
    statuses = {}
    histogram = Counter()
    empty_count = 0

    for pi in itertools.permutations(
        range(n)
    ):
        edges = comparability_edges(pi)

        if not edges:
            k = 0
            empty_count += 1
        else:
            k = implication_pair_count(
                n,
                edges,
            )
            histogram[k] += 1

        statuses[pi] = k

    k_status[n] = statuses

    nonempty_count = (
        math.factorial(n)
        - empty_count
    )

    mean = Fraction(
        sum(
            k * count
            for k, count
            in histogram.items()
        ),
        nonempty_count,
    )

    at_most_2 = Fraction(
        sum(
            count
            for k, count
            in histogram.items()
            if k <= 2
        ),
        nonempty_count,
    )

    at_most_3 = Fraction(
        sum(
            count
            for k, count
            in histogram.items()
            if k <= 3
        ),
        nonempty_count,
    )

    distribution_summary[str(n)] = {
        "permutations": math.factorial(n),
        "empty_antichain_count": empty_count,
        "nonempty_k_histogram": {
            str(k): count
            for k, count
            in sorted(
                histogram.items()
            )
        },
        "mean_k_given_nonempty": str(mean),
        "P_k_at_most_2_given_nonempty": (
            str(at_most_2)
        ),
        "P_k_at_most_3_given_nonempty": (
            str(at_most_3)
        ),
        "maximum_k": max(
            histogram
        ),
    }


refinement_summary = {}

for n in range(2, 8):
    transitions = Counter()
    total = 0
    unchanged = 0
    within_one = 0
    absolute_change_sum = 0

    for pi, parent_k in (
        k_status[n].items()
    ):
        for position in range(n + 1):
            for value in range(n + 1):
                child = (
                    insert_relative_permutation(
                        pi,
                        position,
                        value,
                    )
                )
                child_k = (
                    k_status[n + 1][child]
                )

                transitions[
                    (parent_k, child_k)
                ] += 1
                total += 1

                difference = abs(
                    child_k - parent_k
                )

                absolute_change_sum += (
                    difference
                )
                unchanged += (
                    difference == 0
                )
                within_one += (
                    difference <= 1
                )

    refinement_summary[str(n)] = {
        "parent_size": n,
        "child_size": n + 1,
        "transition_count": total,
        "P_k_unchanged": str(
            Fraction(
                unchanged,
                total,
            )
        ),
        "P_abs_change_at_most_1": str(
            Fraction(
                within_one,
                total,
            )
        ),
        "mean_absolute_change": str(
            Fraction(
                absolute_change_sum,
                total,
            )
        ),
    }


expected_n8 = {
    "1": 8464,
    "2": 12942,
    "3": 8568,
    "4": 4713,
    "5": 3006,
    "6": 693,
    "7": 1089,
    "8": 315,
    "9": 156,
    "10": 102,
    "11": 171,
    "12": 18,
    "13": 18,
    "15": 36,
    "16": 18,
    "21": 9,
    "28": 1,
}

assert (
    distribution_summary["8"][
        "nonempty_k_histogram"
    ]
    == expected_n8
)

assert (
    distribution_summary["8"][
        "mean_k_given_nonempty"
    ]
    == "114035/40319"
)

assert (
    refinement_summary["7"][
        "P_k_unchanged"
    ]
    == "859/1680"
)

assert (
    refinement_summary["7"][
        "P_abs_change_at_most_1"
    ]
    == "1929/2240"
)

assert (
    refinement_summary["7"][
        "mean_absolute_change"
    ]
    == "27413/40320"
)


result = {
    "audit": "RANDOM_2D_IMPLICATION_CLASS_AMBIGUITY_V1",
    "status": "PASS",
    "n_range": [2, 8],
    "distribution_summary": (
        distribution_summary
    ),
    "refinement_summary": (
        refinement_summary
    ),
    "interpretation": [
        "k_Gamma=1 reproduces the nontrivial UPO counts.",
        "k_Gamma is a forcing-block diagnostic, not the number of independent orientation bits.",
        "The graded count is not refinement invariant but usually changes by at most one under one-point refinement in the audited finite range."
    ],
    "nonclaims": [
        "No large-N limit is inferred.",
        "No physical entropy or time dimension is assigned to k_Gamma.",
        "Implication classes are classical comparability-graph structure."
    ],
}

print(
    json.dumps(
        result,
        indent=2,
    )
)
