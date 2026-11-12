#!/usr/bin/env python3
"""Higher-dimensional Minkowski UPO obstruction audit.

Standard-library-only reproducible experiment for:
- uniform sprinklings in a flat Alexandrov interval,
- comparability-graph implication/color classes,
- UPO classification,
- comparable twin-pair obstruction statistics,
- Myrheim-Meyer ordering-fraction calibration.

This script does not infer an asymptotic limit from finite Monte Carlo data.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
import random
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass
class DSU:
    parent: list[int]
    rank: list[int]

    @classmethod
    def make(cls, n: int) -> "DSU":
        return cls(list(range(n)), [0] * n)

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


def sprinkle_diamond(n: int, d: int, rng: random.Random) -> list[tuple[float, ...]]:
    """Sample n iid points uniformly from the diamond I((-1,0),(1,0)) in M^d."""
    if d < 2:
        raise ValueError("d must be a spacetime dimension >= 2")
    spatial_dim = d - 1
    points: list[tuple[float, ...]] = []

    for _ in range(n):
        # Spatial section volume at t is proportional to (1-|t|)^(d-1).
        # Therefore |t| = 1 - U^(1/d).
        abs_t = 1.0 - rng.random() ** (1.0 / d)
        t = abs_t if rng.random() < 0.5 else -abs_t
        r_max = 1.0 - abs_t

        direction = [rng.gauss(0.0, 1.0) for _ in range(spatial_dim)]
        norm = math.sqrt(sum(x * x for x in direction))
        while norm == 0.0:
            direction = [rng.gauss(0.0, 1.0) for _ in range(spatial_dim)]
            norm = math.sqrt(sum(x * x for x in direction))

        radius = r_max * rng.random() ** (1.0 / spatial_dim)
        spatial = tuple(radius * x / norm for x in direction)
        points.append((t, *spatial))

    return points


def comparability_masks(points: Sequence[tuple[float, ...]]) -> tuple[list[int], int]:
    """Return bit-mask adjacency and the number of comparable unordered pairs."""
    n = len(points)
    adj = [0] * n
    relations = 0

    for i in range(n):
        ti = points[i][0]
        xi = points[i][1:]
        for j in range(i + 1, n):
            tj = points[j][0]
            xj = points[j][1:]
            dt2 = (tj - ti) ** 2
            dr2 = sum((a - b) ** 2 for a, b in zip(xi, xj))
            if dt2 > dr2:  # null equality has measure zero
                adj[i] |= 1 << j
                adj[j] |= 1 << i
                relations += 1

    return adj, relations


def graph_from_relative_permutation(p: Sequence[int]) -> list[int]:
    """Comparability graph of the 2-order defined by identity intersect p."""
    n = len(p)
    adj = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] < p[j]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return adj


def color_classes(adj: Sequence[int]) -> list[list[tuple[int, int]]]:
    """Compute undirected color classes induced by Gallai forcing.

    Two incident edges are joined when their non-shared endpoints are nonadjacent.
    For a comparability graph, one nonempty color class is equivalent to UPO.
    """
    n = len(adj)
    edges: list[tuple[int, int]] = []
    edge_index: dict[tuple[int, int], int] = {}

    for i in range(n):
        for j in range(i + 1, n):
            if (adj[i] >> j) & 1:
                edge_index[(i, j)] = len(edges)
                edges.append((i, j))

    if not edges:
        return []

    dsu = DSU.make(len(edges))

    for v in range(n):
        neighbours = [u for u in range(n) if (adj[v] >> u) & 1]
        for a in range(len(neighbours)):
            u = neighbours[a]
            for b in range(a + 1, len(neighbours)):
                w = neighbours[b]
                if not ((adj[u] >> w) & 1):
                    e1 = edge_index[tuple(sorted((v, u)))]
                    e2 = edge_index[tuple(sorted((v, w)))]
                    dsu.union(e1, e2)

    groups: dict[int, list[tuple[int, int]]] = {}
    for idx, edge in enumerate(edges):
        groups.setdefault(dsu.find(idx), []).append(edge)
    return list(groups.values())


def comparable_twin_pairs(adj: Sequence[int]) -> list[tuple[int, int]]:
    """Return adjacent twin pairs, i.e. size-two non-stable modules."""
    n = len(adj)
    pairs: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if not ((adj[i] >> j) & 1):
                continue
            outside_i = adj[i] & ~(1 << j)
            outside_j = adj[j] & ~(1 << i)
            if outside_i == outside_j:
                pairs.append((i, j))
    return pairs


def point_comparable_volume_fraction(point: Sequence[float], d: int) -> float:
    """Exact Q_d(x): volume fraction of the diamond comparable to x."""
    t = point[0]
    r2 = sum(x * x for x in point[1:])
    future = max(0.0, (1.0 - t) ** 2 - r2)
    past = max(0.0, (1.0 + t) ** 2 - r2)
    return (future ** (d / 2.0) + past ** (d / 2.0)) / (2.0 ** d)


def myrheim_meyer_ordering_fraction(d: int) -> float:
    return (
        math.gamma(d + 1.0)
        * math.gamma(d / 2.0)
        / (2.0 * math.gamma(3.0 * d / 2.0))
    )


def exact_regression(max_n: int = 7) -> dict[int, int]:
    expected = {2: 1, 3: 4, 4: 12, 5: 38, 6: 165, 7: 1042}
    observed: dict[int, int] = {}

    for n in range(2, max_n + 1):
        count = 0
        for p in itertools.permutations(range(n)):
            classes = color_classes(graph_from_relative_permutation(p))
            if len(classes) == 1:
                count += 1
        observed[n] = count
        if n in expected and count != expected[n]:
            raise AssertionError(
                f"UPO regression failed at n={n}: got {count}, expected {expected[n]}"
            )

    return observed


def monte_carlo_row(d: int, n: int, reps: int, seed: int) -> dict[str, float | int]:
    rng = random.Random(seed)
    upo = 0
    empty = 0
    failures = 0
    failures_with_twins = 0
    total_twins = 0
    ordering_sum = 0.0
    twin_q_sum = 0.0
    twin_q_count = 0
    k_gamma = Counter()

    for _ in range(reps):
        points = sprinkle_diamond(n, d, rng)
        adj, relations = comparability_masks(points)
        classes = color_classes(adj)
        k = len(classes)
        k_gamma[k] += 1

        ordering_sum += relations / math.comb(n, 2)

        if k == 0:
            empty += 1
            continue
        if k == 1:
            upo += 1
            continue

        failures += 1
        twins = comparable_twin_pairs(adj)
        total_twins += len(twins)
        if twins:
            failures_with_twins += 1
            for i, j in twins:
                twin_q_sum += 0.5 * (
                    point_comparable_volume_fraction(points[i], d)
                    + point_comparable_volume_fraction(points[j], d)
                )
                twin_q_count += 1

    return {
        "d": d,
        "n": n,
        "reps": reps,
        "seed": seed,
        "upo_fraction": upo / reps,
        "empty_fraction": empty / reps,
        "nonupo_nonempty_fraction": failures / reps,
        "failure_with_twin_fraction": (
            failures_with_twins / failures if failures else 0.0
        ),
        "mean_twin_pairs": total_twins / reps,
        "mean_ordering_fraction": ordering_sum / reps,
        "theory_ordering_fraction": myrheim_meyer_ordering_fraction(d),
        "mean_twin_Q": twin_q_sum / twin_q_count if twin_q_count else float("nan"),
        "k_gamma_1_fraction": k_gamma[1] / reps,
        "k_gamma_2_fraction": k_gamma[2] / reps,
        "k_gamma_ge3_fraction": sum(v for k, v in k_gamma.items() if k >= 3) / reps,
    }


def parse_int_list(text: str) -> list[int]:
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dims", default="3,4")
    parser.add_argument("--ns", default="7,9,11,16,24,32,48")
    parser.add_argument("--reps", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20261113)
    parser.add_argument("--csv", default="")
    parser.add_argument("--skip-regression", action="store_true")
    args = parser.parse_args()

    if not args.skip_regression:
        print("Exact 1+1 permutation regression:", exact_regression())

    dims = parse_int_list(args.dims)
    ns = parse_int_list(args.ns)
    rows: list[dict[str, float | int]] = []

    for d in dims:
        for n in ns:
            # Derive a deterministic independent seed for every cell.
            cell_seed = args.seed + 1000003 * d + 1009 * n
            row = monte_carlo_row(d, n, args.reps, cell_seed)
            rows.append(row)
            print(row)

    if args.csv:
        out = Path(args.csv)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
