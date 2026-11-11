#!/usr/bin/env python3
"""Higher-dimensional Minkowski UPO pilot.

This script studies the information-loss experiment used by the repository:
1. condition on n points sampled uniformly in a flat Alexandrov interval;
2. keep only symmetric causal comparability;
3. compute the classical comparability-graph implication/color classes;
4. classify nonempty UPO graphs by k_Gamma == 1.

No permutation representation is used outside the exact 1+1 self-test.

The script also records the number of isolated vertices and compares its sample
mean with the analytic asymptotic

    E[I_n] ~ d(d-1) Gamma(1 + 2/d)^2 n^(1 - 4/d).

Only Python's standard library is required.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from collections import Counter
from statistics import fmean, median


EXACT_RANDOM_2_ORDER_UPO = {
    2: 1,
    3: 4,
    4: 12,
    5: 38,
    6: 165,
    7: 1042,
    8: 8464,
}


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, first: int, second: int) -> None:
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return

        if self.rank[root_first] < self.rank[root_second]:
            root_first, root_second = root_second, root_first

        self.parent[root_second] = root_first

        if self.rank[root_first] == self.rank[root_second]:
            self.rank[root_first] += 1


def permutation_edges(permutation: tuple[int, ...]) -> set[tuple[int, int]]:
    n = len(permutation)
    return {
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if permutation[i] < permutation[j]
    }


def implication_pair_count(
    n: int,
    edges: set[tuple[int, int]],
) -> int:
    """Return k_Gamma, the number of inverse implication-class pairs.

    On undirected edges this is the number of color/forcing classes generated
    by induced P3 constraints.  For a nonempty comparability graph,
    k_Gamma == 1 is equivalent to UPO.
    """
    if not edges:
        return 0

    edge_list = sorted(edges)
    adjacency = [set() for _ in range(n)]
    incident: list[list[tuple[int, int]]] = [[] for _ in range(n)]

    for edge_index, (u, v) in enumerate(edge_list):
        adjacency[u].add(v)
        adjacency[v].add(u)
        incident[u].append((edge_index, v))
        incident[v].append((edge_index, u))

    union_find = UnionFind(len(edge_list))

    for center in range(n):
        local = incident[center]

        for first_index in range(len(local)):
            first_edge, first_other = local[first_index]

            for second_index in range(first_index + 1, len(local)):
                second_edge, second_other = local[second_index]

                if second_other not in adjacency[first_other]:
                    union_find.union(first_edge, second_edge)

    return len({
        union_find.find(edge_index)
        for edge_index in range(len(edge_list))
    })


def graph_components(
    n: int,
    edges: set[tuple[int, int]],
) -> list[list[int]]:
    adjacency = [set() for _ in range(n)]

    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)

    seen = [False] * n
    components: list[list[int]] = []

    for start in range(n):
        if seen[start]:
            continue

        stack = [start]
        seen[start] = True
        component: list[int] = []

        while stack:
            vertex = stack.pop()
            component.append(vertex)

            for neighbor in adjacency[vertex]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    stack.append(neighbor)

        components.append(component)

    return components


def classify_graph(
    n: int,
    edges: set[tuple[int, int]],
) -> dict:
    components = graph_components(n, edges)
    k_gamma = implication_pair_count(n, edges)
    upo = bool(edges) and k_gamma == 1
    connected_upo = upo and len(components) == 1

    nontrivial_components = [
        component
        for component in components
        if len(component) > 1
    ]

    active_size = (
        len(nontrivial_components[0])
        if upo and len(nontrivial_components) == 1
        else 0
    )

    return {
        "k_gamma": k_gamma,
        "upo": upo,
        "connected_upo": connected_upo,
        "active_size": active_size,
        "component_count": len(components),
        "nontrivial_component_count": len(nontrivial_components),
        "isolated_vertices": sum(
            len(component) == 1
            for component in components
        ),
    }


def unit_direction(
    spatial_dimension: int,
    rng: random.Random,
) -> tuple[float, ...]:
    if spatial_dimension == 1:
        return (1.0 if rng.random() < 0.5 else -1.0,)

    while True:
        coordinates = [
            rng.gauss(0.0, 1.0)
            for _ in range(spatial_dimension)
        ]
        norm = math.sqrt(sum(value * value for value in coordinates))

        if norm > 0.0:
            return tuple(value / norm for value in coordinates)


def sprinkle_alexandrov_interval(
    n: int,
    dimension: int,
    rng: random.Random,
) -> list[tuple[float, tuple[float, ...]]]:
    """Uniform iid points in the diamond between (-1,0) and (1,0).

    dimension is spacetime dimension, so the spatial dimension is d-1.
    Conditioning a Poisson sprinkling on cardinality n gives this iid law.
    """
    spatial_dimension = dimension - 1
    points = []

    for _ in range(n):
        absolute_time = 1.0 - rng.random() ** (1.0 / dimension)
        time = (
            absolute_time
            if rng.random() < 0.5
            else -absolute_time
        )

        maximum_radius = 1.0 - absolute_time
        direction = unit_direction(spatial_dimension, rng)
        radius = (
            maximum_radius
            * rng.random() ** (1.0 / spatial_dimension)
        )

        spatial = tuple(
            radius * coordinate
            for coordinate in direction
        )

        points.append((time, spatial))

    return points


def causal_comparability_edges(
    points: list[tuple[float, tuple[float, ...]]],
) -> set[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()

    for i in range(len(points)):
        time_i, space_i = points[i]

        for j in range(i + 1, len(points)):
            time_j, space_j = points[j]
            delta_time = abs(time_j - time_i)
            spatial_square = sum(
                (left - right) ** 2
                for left, right in zip(space_i, space_j)
            )

            # Equality is a null relation and has probability zero here.
            if delta_time * delta_time > spatial_square:
                edges.add((i, j))

    return edges


def wilson_interval(
    successes: int,
    trials: int,
    z: float = 1.959963984540054,
) -> tuple[float, float]:
    p = successes / trials
    denominator = 1.0 + z * z / trials
    center = (
        p + z * z / (2.0 * trials)
    ) / denominator
    half_width = (
        z
        * math.sqrt(
            p * (1.0 - p) / trials
            + z * z / (4.0 * trials * trials)
        )
        / denominator
    )
    return center - half_width, center + half_width


def myrheim_meyer_ordering_fraction(dimension: int) -> float:
    d = dimension
    return (
        math.gamma(d + 1)
        * math.gamma(d / 2)
        / (2.0 * math.gamma(3.0 * d / 2.0))
    )


def isolated_vertex_asymptotic(dimension: int, n: int) -> float:
    d = dimension
    coefficient = (
        d
        * (d - 1)
        * math.gamma(1.0 + 2.0 / d) ** 2
    )
    return coefficient * n ** (1.0 - 4.0 / d)


def run_trial_block(
    dimension: int,
    n: int,
    trials: int,
    seed: int,
) -> dict:
    rng = random.Random(seed)

    upo_count = 0
    connected_upo_count = 0
    ordering_fractions: list[float] = []
    active_fractions: list[float] = []
    isolated_counts: list[int] = []
    k_histogram: Counter[int] = Counter()
    multiple_nontrivial_count = 0
    empty_count = 0

    for _ in range(trials):
        points = sprinkle_alexandrov_interval(
            n,
            dimension,
            rng,
        )
        edges = causal_comparability_edges(points)
        status = classify_graph(n, edges)

        ordering_fractions.append(
            len(edges) / math.comb(n, 2)
        )
        isolated_counts.append(
            status["isolated_vertices"]
        )
        k_histogram[status["k_gamma"]] += 1

        if not edges:
            empty_count += 1

        if status["nontrivial_component_count"] >= 2:
            multiple_nontrivial_count += 1

        if status["upo"]:
            upo_count += 1
            active_fractions.append(
                status["active_size"] / n
            )

        if status["connected_upo"]:
            connected_upo_count += 1

    return {
        "dimension": dimension,
        "n": n,
        "trials": trials,
        "seed": seed,
        "upo_count": upo_count,
        "p_upo": upo_count / trials,
        "p_upo_wilson95": wilson_interval(
            upo_count,
            trials,
        ),
        "connected_upo_count": connected_upo_count,
        "p_connected_upo": connected_upo_count / trials,
        "p_connected_upo_wilson95": wilson_interval(
            connected_upo_count,
            trials,
        ),
        "mean_ordering_fraction": fmean(ordering_fractions),
        "theoretical_ordering_fraction": (
            myrheim_meyer_ordering_fraction(dimension)
        ),
        "mean_active_fraction_given_upo": (
            fmean(active_fractions)
            if active_fractions
            else None
        ),
        "median_active_fraction_given_upo": (
            median(active_fractions)
            if active_fractions
            else None
        ),
        "mean_isolated_vertices": fmean(isolated_counts),
        "isolated_vertex_asymptotic": (
            isolated_vertex_asymptotic(
                dimension,
                n,
            )
        ),
        "p_multiple_nontrivial_components": (
            multiple_nontrivial_count / trials
        ),
        "p_empty": empty_count / trials,
        "k_gamma_histogram": {
            str(key): value
            for key, value in sorted(k_histogram.items())
        },
    }


def exact_random_2_order_self_test(max_n: int = 8) -> dict:
    observed = {}

    for n in range(2, max_n + 1):
        upo_count = 0

        for permutation in itertools.permutations(range(n)):
            edges = permutation_edges(permutation)

            if implication_pair_count(n, edges) == 1:
                upo_count += 1

        observed[n] = upo_count
        assert upo_count == EXACT_RANDOM_2_ORDER_UPO[n]

    return {
        "status": "PASS",
        "max_n": max_n,
        "observed": {
            str(key): value
            for key, value in observed.items()
        },
    }


def default_schedule() -> dict[int, int]:
    return {
        7: 5000,
        9: 5000,
        11: 5000,
        16: 5000,
        24: 3000,
        32: 1500,
        48: 750,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--self-test-only",
        action="store_true",
    )
    parser.add_argument(
        "--output",
        default=None,
    )
    args = parser.parse_args()

    result = {
        "audit": "MINKOWSKI_HIGHER_DIMENSIONAL_UPO_PILOT_V1",
        "self_test": exact_random_2_order_self_test(),
        "runs": [],
        "nonclaims": [
            "Monte Carlo trends are not asymptotic theorems.",
            "UPO recovery does not select future over past.",
            "Connected-UPO is a causal-support diagnostic, not a different logical recovery criterion.",
            "The isolated-vertex result concerns expectation only and does not by itself determine the limiting probability of graph connectedness.",
        ],
    }

    if not args.self_test_only:
        for dimension in (2, 3, 4):
            for n, trials in default_schedule().items():
                seed = 2026111100 + 1000 * dimension + n
                result["runs"].append(
                    run_trial_block(
                        dimension,
                        n,
                        trials,
                        seed,
                    )
                )

    encoded = json.dumps(
        result,
        indent=2,
        sort_keys=True,
    )

    if args.output:
        with open(
            args.output,
            "w",
            encoding="utf-8",
        ) as handle:
            handle.write(encoded)
            handle.write("\n")

    print(encoded)


if __name__ == "__main__":
    main()
