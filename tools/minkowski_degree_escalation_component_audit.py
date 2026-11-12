#!/usr/bin/env python3
"""Degree-escalation audit for Minkowski causal comparability graphs.

The accompanying theorem proves that, for every fixed spacetime dimension d>=2,
all non-isolated vertices lie in a single connected component with probability
tending to one.

This script provides a finite-n diagnostic in d=4:
- number of connected components containing at least one edge;
- number of isolated vertices;
- violations of a chosen degree-escalation rule
      Q(y) > Q(x)^alpha
  among low-Q non-isolated vertices.

NumPy only.  The finite audit is not part of the analytic proof.
"""

from __future__ import annotations

import argparse
import numpy as np


def sprinkle_diamond(n: int, d: int, rng: np.random.Generator) -> np.ndarray:
    spatial_dim = d - 1

    abs_t = 1.0 - rng.random(n) ** (1.0 / d)
    t = abs_t * np.where(rng.random(n) < 0.5, -1.0, 1.0)

    direction = rng.normal(size=(n, spatial_dim))
    norm = np.linalg.norm(direction, axis=1)
    zero = norm == 0.0
    while np.any(zero):
        direction[zero] = rng.normal(size=(int(np.sum(zero)), spatial_dim))
        norm = np.linalg.norm(direction, axis=1)
        zero = norm == 0.0

    radius = (1.0 - abs_t) * rng.random(n) ** (1.0 / spatial_dim)
    spatial = direction / norm[:, None] * radius[:, None]

    return np.concatenate([t[:, None], spatial], axis=1)


def adjacency_matrix(points: np.ndarray) -> np.ndarray:
    t = points[:, 0]
    x = points[:, 1:]

    dt = t[:, None] - t[None, :]
    dx = x[:, None, :] - x[None, :, :]
    dr2 = np.sum(dx * dx, axis=2)

    adj = dt * dt > dr2
    np.fill_diagonal(adj, False)
    return adj


def q_d(points: np.ndarray, d: int) -> np.ndarray:
    t = points[:, 0]
    r2 = np.sum(points[:, 1:] ** 2, axis=1)

    past = np.maximum((1.0 + t) ** 2 - r2, 0.0)
    future = np.maximum((1.0 - t) ** 2 - r2, 0.0)

    power = d / 2.0
    return (past**power + future**power) / (2.0**d)


def component_sizes(adj: np.ndarray) -> list[int]:
    n = len(adj)
    seen = np.zeros(n, dtype=bool)
    sizes: list[int] = []

    for start in range(n):
        if seen[start]:
            continue

        stack = [start]
        seen[start] = True
        size = 0

        while stack:
            v = stack.pop()
            size += 1

            neighbours = np.flatnonzero(adj[v] & ~seen)
            seen[neighbours] = True
            stack.extend(int(x) for x in neighbours)

        sizes.append(size)

    return sorted(sizes, reverse=True)


def escalation_violations(
    adj: np.ndarray,
    q: np.ndarray,
    alpha: float,
    q0: float,
) -> int:
    bad = 0

    for i in range(len(adj)):
        qi = float(q[i])

        if qi >= q0 or not np.any(adj[i]):
            continue

        neighbours = np.flatnonzero(adj[i])

        if not np.any(q[neighbours] > qi**alpha):
            bad += 1

    return bad


def parse_int_list(text: str) -> list[int]:
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", type=int, default=4)
    parser.add_argument("--ns", default="64,128,256,512,1024")
    parser.add_argument("--reps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=20261112)
    parser.add_argument("--alpha", type=float, default=0.75)
    parser.add_argument("--q0", type=float, default=0.08)
    args = parser.parse_args()

    if not (0.5 < args.alpha < 1.0):
        raise ValueError("alpha must lie in (1/2,1) for the d=4 audit")

    for n in parse_int_list(args.ns):
        rng = np.random.default_rng(args.seed + 1009 * n)

        multiple_nontrivial = 0
        total_isolates = 0
        graphs_with_escalation_violation = 0
        total_escalation_violations = 0
        largest_second_nontrivial = 0

        for _ in range(args.reps):
            points = sprinkle_diamond(n, args.d, rng)
            adj = adjacency_matrix(points)
            q = q_d(points, args.d)

            sizes = component_sizes(adj)
            nontrivial = [size for size in sizes if size >= 2]

            if len(nontrivial) > 1:
                multiple_nontrivial += 1
                largest_second_nontrivial = max(
                    largest_second_nontrivial,
                    nontrivial[1],
                )

            total_isolates += sum(size == 1 for size in sizes)

            violations = escalation_violations(
                adj,
                q,
                args.alpha,
                args.q0,
            )
            total_escalation_violations += violations
            if violations:
                graphs_with_escalation_violation += 1

        print(
            {
                "d": args.d,
                "n": n,
                "reps": args.reps,
                "multiple_nontrivial_fraction": multiple_nontrivial / args.reps,
                "mean_isolates": total_isolates / args.reps,
                "graphs_with_escalation_violation_fraction":
                    graphs_with_escalation_violation / args.reps,
                "mean_escalation_violations":
                    total_escalation_violations / args.reps,
                "largest_second_nontrivial_component":
                    largest_second_nontrivial,
            }
        )


if __name__ == "__main__":
    main()
