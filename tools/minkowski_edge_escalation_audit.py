#!/usr/bin/env python3
"""Edge-escalation audit for d=4 Minkowski comparability graphs.

For an edge e={x,y}, Delta(e) is the continuum measure of its splitter region.
A sampled splitter z directly forces e with one of the edges {x,z} or {y,z}.

For alpha in (1/2,1), this audit asks whether every low-Delta sampled edge has
a splitter leading to a forced edge e' with

    Delta(e') > Delta(e)^alpha.

The accompanying analytic note proves that the probability of any violation
tends to zero in d=4.  This script is a finite-n diagnostic only.
"""

from __future__ import annotations

import argparse
import numpy as np


def sprinkle_diamond(n: int, rng: np.random.Generator) -> np.ndarray:
    d = 4
    abs_t = 1.0 - rng.random(n) ** 0.25
    t = abs_t * np.where(rng.random(n) < 0.5, -1.0, 1.0)

    direction = rng.normal(size=(n, 3))
    norm = np.linalg.norm(direction, axis=1)
    radius = (1.0 - abs_t) * rng.random(n) ** (1.0 / 3.0)
    spatial = direction / norm[:, None] * radius[:, None]

    return np.concatenate([t[:, None], spatial], axis=1)


def adjacency_masks(points: np.ndarray) -> list[int]:
    n = len(points)
    adj = [0] * n

    for i in range(n):
        dt = points[i + 1 :, 0] - points[i, 0]
        dr2 = np.sum((points[i + 1 :, 1 :] - points[i, 1 :]) ** 2, axis=1)
        for j0 in np.nonzero(dt * dt > dr2)[0] + i + 1:
            j = int(j0)
            adj[i] |= 1 << j
            adj[j] |= 1 << i

    return adj


def tau2(a: np.ndarray, b: np.ndarray) -> float:
    return float((b[0] - a[0]) ** 2 - np.sum((b[1:] - a[1:]) ** 2))


def delta_pair(points: np.ndarray, i: int, j: int) -> float:
    x = points[i].copy()
    y = points[j].copy()

    if x[0] > y[0]:
        x, y = y, x

    p = np.array([-1.0, 0.0, 0.0, 0.0])
    q = np.array([1.0, 0.0, 0.0, 0.0])

    py = max(tau2(p, y), 0.0)
    px = max(tau2(p, x), 0.0)
    xq = max(tau2(x, q), 0.0)
    yq = max(tau2(y, q), 0.0)
    xy = max(tau2(x, y), 0.0)

    return (py**2 - px**2 + xq**2 - yq**2 - 2.0 * xy**2) / 16.0


def edge_delta_table(
    points: np.ndarray,
    adj: list[int],
) -> dict[tuple[int, int], float]:
    n = len(adj)
    table: dict[tuple[int, int], float] = {}

    for i in range(n):
        work = adj[i] & ~((1 << (i + 1)) - 1)
        while work:
            bit = work & -work
            work -= bit
            j = bit.bit_length() - 1
            table[(i, j)] = delta_pair(points, i, j)

    return table


def audit_graph(
    points: np.ndarray,
    alpha: float,
    delta0: float,
) -> tuple[int, int, int]:
    adj = adjacency_masks(points)
    delta = edge_delta_table(points, adj)

    low_edges = 0
    violations = 0
    zero_splitter_violations = 0

    for (x, y), dxy in delta.items():
        if dxy >= delta0:
            continue

        low_edges += 1
        target = dxy**alpha

        splitters = (adj[x] ^ adj[y]) & ~((1 << x) | (1 << y))
        work = splitters
        escalates = False

        while work:
            bit = work & -work
            work -= bit
            z = bit.bit_length() - 1

            if (adj[x] >> z) & 1:
                forced_edge = tuple(sorted((x, z)))
            else:
                forced_edge = tuple(sorted((y, z)))

            if delta[forced_edge] > target:
                escalates = True
                break

        if not escalates:
            violations += 1
            if splitters == 0:
                zero_splitter_violations += 1

    return low_edges, violations, zero_splitter_violations


def parse_int_list(text: str) -> list[int]:
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ns", default="64,128,256")
    parser.add_argument("--reps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=20261112)
    parser.add_argument("--alpha", type=float, default=0.75)
    parser.add_argument("--delta0", type=float, default=0.08)
    args = parser.parse_args()

    if not (0.5 < args.alpha < 1.0):
        raise ValueError("alpha must lie in (1/2,1)")

    for n in parse_int_list(args.ns):
        rng = np.random.default_rng(args.seed + 1009 * n)

        total_low_edges = 0
        total_violations = 0
        total_zero_splitter = 0
        graphs_with_violation = 0

        for _ in range(args.reps):
            points = sprinkle_diamond(n, rng)
            low, bad, zero = audit_graph(points, args.alpha, args.delta0)

            total_low_edges += low
            total_violations += bad
            total_zero_splitter += zero
            if bad:
                graphs_with_violation += 1

        print(
            {
                "n": n,
                "reps": args.reps,
                "low_edges": total_low_edges,
                "violations": total_violations,
                "zero_splitter_violations": total_zero_splitter,
                "graphs_with_violation_fraction":
                    graphs_with_violation / args.reps,
            }
        )


if __name__ == "__main__":
    main()
