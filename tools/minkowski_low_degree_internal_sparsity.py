#!/usr/bin/env python3
"""Low-degree internal-sparsity audit for the d=4 Minkowski causal graphon.

Analytic target:
    mu(S_q) = Theta(q)
    int_{S_q x S_q} W = O(q^3)

where S_q = {x : Q_4(x) <= q}.

The script estimates the two quantities by iid pair sampling and reports
g(q)/q and e(q)/q^3.  It is a numerical regression only; the accompanying
note contains the geometric proof of the orders.
"""

from __future__ import annotations

import argparse
import numpy as np


def sprinkle(n: int, rng: np.random.Generator) -> np.ndarray:
    d = 4
    spatial_dim = 3

    abs_t = 1.0 - rng.random(n) ** (1.0 / d)
    t = abs_t * np.where(rng.random(n) < 0.5, -1.0, 1.0)

    direction = rng.normal(size=(n, spatial_dim))
    norm = np.linalg.norm(direction, axis=1)
    radius = (1.0 - abs_t) * rng.random(n) ** (1.0 / spatial_dim)
    spatial = direction / norm[:, None] * radius[:, None]

    return np.concatenate([t[:, None], spatial], axis=1)


def q4(points: np.ndarray) -> np.ndarray:
    t = points[:, 0]
    r2 = np.sum(points[:, 1:] ** 2, axis=1)
    past = (1.0 + t) ** 2 - r2
    future = (1.0 - t) ** 2 - r2
    return (past**2 + future**2) / 16.0


def comparable(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    dt = y[:, 0] - x[:, 0]
    dr2 = np.sum((y[:, 1:] - x[:, 1:]) ** 2, axis=1)
    return dt * dt > dr2


def parse_float_list(text: str) -> list[float]:
    return [float(x.strip()) for x in text.split(",") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", type=int, default=2_000_000)
    parser.add_argument("--seed", type=int, default=20261112)
    parser.add_argument("--qs", default="0.02,0.03,0.05,0.08")
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    x = sprinkle(args.pairs, rng)
    y = sprinkle(args.pairs, rng)

    qx = q4(x)
    qy = q4(y)
    edge = comparable(x, y)

    for q in parse_float_list(args.qs):
        sx = qx <= q
        sy = qy <= q

        g = float(np.mean(np.concatenate([qx, qy]) <= q))
        e = float(np.mean(edge & sx & sy))

        print(
            {
                "q": q,
                "g": g,
                "g_over_q": g / q,
                "edge_mass": e,
                "edge_mass_over_q3": e / (q**3),
                "conditional_edge_density": e / (g * g) if g > 0 else float("nan"),
            }
        )


if __name__ == "__main__":
    main()
