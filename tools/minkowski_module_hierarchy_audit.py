#!/usr/bin/env python3
"""Fixed-size module hierarchy audit for Minkowski comparability graphs.

Measures two obstruction families in arrow-erased causal-set comparability graphs:

1. true-twin pairs (size-two non-stable modules);
2. induced-P3 graph modules (minimal size-three non-stable modules without
   a true-twin pair).

The script uses only NumPy and deterministic seeds.  It is intended as a
reproducible finite-n audit, not as an asymptotic proof.
"""

from __future__ import annotations

import argparse
import math
from collections import defaultdict

import numpy as np


def sprinkle_diamond(n: int, d: int, rng: np.random.Generator) -> np.ndarray:
    spatial_dim = d - 1
    abs_t = 1.0 - rng.random(n) ** (1.0 / d)
    signs = np.where(rng.random(n) < 0.5, -1.0, 1.0)
    t = abs_t * signs

    directions = rng.normal(size=(n, spatial_dim))
    norms = np.linalg.norm(directions, axis=1)
    zero = norms == 0.0
    while np.any(zero):
        directions[zero] = rng.normal(size=(int(np.sum(zero)), spatial_dim))
        norms = np.linalg.norm(directions, axis=1)
        zero = norms == 0.0

    radii = (1.0 - abs_t) * rng.random(n) ** (1.0 / spatial_dim)
    spatial = directions / norms[:, None] * radii[:, None]
    return np.concatenate([t[:, None], spatial], axis=1)


def adjacency_masks(points: np.ndarray) -> list[int]:
    n = len(points)
    masks = [0] * n

    for i in range(n):
        dt = points[i + 1 :, 0] - points[i, 0]
        dr2 = np.sum((points[i + 1 :, 1 :] - points[i, 1 :]) ** 2, axis=1)
        causal = dt * dt > dr2
        for j in np.nonzero(causal)[0] + i + 1:
            jj = int(j)
            masks[i] |= 1 << jj
            masks[jj] |= 1 << i

    return masks


def true_twin_count(adj: list[int]) -> int:
    """Adjacent twins are exactly equal closed-neighborhood masks."""
    groups: dict[int, int] = defaultdict(int)
    for i, mask in enumerate(adj):
        groups[mask | (1 << i)] += 1
    return sum(k * (k - 1) // 2 for k in groups.values())


def p3_module_count(adj: list[int]) -> int:
    """Count induced-P3 graph modules.

    In an induced P3 module, the two leaves are false twins, hence have
    identical open-neighborhood masks.  For each false-twin leaf pair, test
    whether a common neighbor can serve as the center while matching the same
    exterior adjacency signature.
    """
    n = len(adj)
    full = (1 << n) - 1

    false_twin_groups: dict[int, list[int]] = defaultdict(list)
    for i, mask in enumerate(adj):
        false_twin_groups[mask].append(i)

    count = 0

    for leaf_mask, leaves in false_twin_groups.items():
        if len(leaves) < 2:
            continue

        centers = [z for z in range(n) if (leaf_mask >> z) & 1]

        for a in range(len(leaves) - 1):
            x = leaves[a]
            for b in range(a + 1, len(leaves)):
                y = leaves[b]

                for z in centers:
                    module_mask = (1 << x) | (1 << y) | (1 << z)
                    outside = full ^ module_mask

                    if ((adj[z] ^ leaf_mask) & outside) == 0:
                        count += 1

    return count


def run_cell(d: int, n: int, reps: int, seed: int) -> dict[str, float | int]:
    rng = np.random.default_rng(seed)

    twin_values = np.empty(reps, dtype=np.int64)
    p3_values = np.empty(reps, dtype=np.int64)

    for r in range(reps):
        points = sprinkle_diamond(n, d, rng)
        adj = adjacency_masks(points)
        twin_values[r] = true_twin_count(adj)
        p3_values[r] = p3_module_count(adj)

    def summary(values: np.ndarray, prefix: str) -> dict[str, float]:
        mean = float(np.mean(values))
        variance = float(np.var(values, ddof=1)) if len(values) > 1 else 0.0
        se = math.sqrt(variance / len(values)) if len(values) > 1 else 0.0
        return {
            f"{prefix}_mean": mean,
            f"{prefix}_se": se,
            f"{prefix}_prob_nonzero": float(np.mean(values > 0)),
        }

    row: dict[str, float | int] = {
        "d": d,
        "n": n,
        "reps": reps,
        "seed": seed,
    }
    row.update(summary(twin_values, "true_twin"))
    row.update(summary(p3_values, "p3_module"))
    row["n_times_true_twin_mean"] = n * float(np.mean(twin_values))
    row["n2_times_p3_mean"] = n * n * float(np.mean(p3_values))
    return row


def parse_int_list(text: str) -> list[int]:
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dims", default="4")
    parser.add_argument("--ns", default="24,32,48,64,96,128")
    parser.add_argument("--reps", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=20261118)
    args = parser.parse_args()

    for d in parse_int_list(args.dims):
        for n in parse_int_list(args.ns):
            cell_seed = args.seed + 1000003 * d + 1009 * n
            print(run_cell(d, n, args.reps, cell_seed))


if __name__ == "__main__":
    main()
