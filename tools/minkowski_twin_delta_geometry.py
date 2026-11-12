#!/usr/bin/env python3
"""Pair-geometry audit for comparable-twin obstructions in Minkowski diamonds.

Samples iid pairs from a flat Alexandrov interval, evaluates the exact
comparability-neighborhood disagreement volume Delta(x,y), and estimates
the small-Delta distribution F_d(epsilon).

Requires NumPy. No asymptotic theorem is inferred from fitted slopes.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def sprinkle_pairs(count: int, d: int, seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    return sprinkle(count, d, rng), sprinkle(count, d, rng)


def sprinkle(count: int, d: int, rng: np.random.Generator) -> np.ndarray:
    if d < 2:
        raise ValueError("d must be >= 2")
    spatial_dim = d - 1

    abs_t = 1.0 - rng.random(count) ** (1.0 / d)
    signs = np.where(rng.random(count) < 0.5, -1.0, 1.0)
    t = abs_t * signs

    directions = rng.normal(size=(count, spatial_dim))
    norms = np.linalg.norm(directions, axis=1)
    zero = norms == 0.0
    while np.any(zero):
        directions[zero] = rng.normal(size=(int(np.sum(zero)), spatial_dim))
        norms = np.linalg.norm(directions, axis=1)
        zero = norms == 0.0

    radii = (1.0 - abs_t) * rng.random(count) ** (1.0 / spatial_dim)
    spatial = directions / norms[:, None] * radii[:, None]
    return np.concatenate([t[:, None], spatial], axis=1)


def proper_time_squared(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    dt = b[:, 0] - a[:, 0]
    dr2 = np.sum((b[:, 1:] - a[:, 1:]) ** 2, axis=1)
    return dt * dt - dr2


def orient_comparable_pairs(
    x: np.ndarray, y: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    tau2 = proper_time_squared(x, y)
    causal = tau2 > 0.0

    xo = x.copy()
    yo = y.copy()
    swap = causal & (y[:, 0] < x[:, 0])
    xo[swap] = y[swap]
    yo[swap] = x[swap]
    return xo, yo, causal


def endpoint_tau2(point: np.ndarray, past: bool) -> np.ndarray:
    r2 = np.sum(point[:, 1:] ** 2, axis=1)
    if past:
        return (point[:, 0] + 1.0) ** 2 - r2
    return (1.0 - point[:, 0]) ** 2 - r2


def delta_exact(x: np.ndarray, y: np.ndarray, d: int) -> np.ndarray:
    """Exact Delta for already time-oriented comparable pairs x prec y."""
    px = np.maximum(endpoint_tau2(x, past=True), 0.0)
    py = np.maximum(endpoint_tau2(y, past=True), 0.0)
    xq = np.maximum(endpoint_tau2(x, past=False), 0.0)
    yq = np.maximum(endpoint_tau2(y, past=False), 0.0)
    xy = np.maximum(proper_time_squared(x, y), 0.0)

    power = d / 2.0
    return (
        py**power
        - px**power
        + xq**power
        - yq**power
        - 2.0 * xy**power
    ) / (2.0**d)


def point_q(point: np.ndarray, d: int) -> np.ndarray:
    p = np.maximum(endpoint_tau2(point, past=True), 0.0)
    f = np.maximum(endpoint_tau2(point, past=False), 0.0)
    power = d / 2.0
    return (p**power + f**power) / (2.0**d)


def parse_float_list(text: str) -> list[float]:
    return [float(x.strip()) for x in text.split(",") if x.strip()]


def parse_int_list(text: str) -> list[int]:
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def fit_log_slope(eps: np.ndarray, f: np.ndarray) -> float:
    mask = (eps > 0.0) & (f > 0.0)
    if int(np.sum(mask)) < 2:
        return float("nan")
    return float(np.polyfit(np.log(eps[mask]), np.log(f[mask]), 1)[0])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dims", default="3,4")
    parser.add_argument("--pairs", type=int, default=1000000)
    parser.add_argument("--seed", type=int, default=20261116)
    parser.add_argument("--eps", default="0.02,0.03,0.04,0.05,0.07,0.1")
    parser.add_argument("--q-min", default="0,0.03,0.06,0.1")
    parser.add_argument("--csv", default="")
    args = parser.parse_args()

    eps_values = np.asarray(parse_float_list(args.eps), dtype=float)
    qmins = parse_float_list(args.q_min)
    dims = parse_int_list(args.dims)
    rows: list[dict[str, float | int]] = []

    for d in dims:
        x, y = sprinkle_pairs(args.pairs, d, args.seed + 1000003 * d)
        xo, yo, causal = orient_comparable_pairs(x, y)
        xc = xo[causal]
        yc = yo[causal]

        delta = delta_exact(xc, yc, d)
        qmean = 0.5 * (point_q(xc, d) + point_q(yc, d))
        causal_fraction = len(delta) / args.pairs

        if np.any(delta < -1e-10):
            raise AssertionError("Delta became negative beyond floating-point tolerance")

        print(
            {
                "d": d,
                "pairs": args.pairs,
                "causal_fraction": causal_fraction,
                "min_delta": float(np.min(delta)) if len(delta) else float("nan"),
            }
        )

        for qmin in qmins:
            fs = []
            for epsilon in eps_values:
                # Unconditional pair measure F_d(epsilon), with optional bulk cut.
                probability = float(
                    np.mean((delta <= epsilon) & (qmean >= qmin))
                    * causal_fraction
                )
                fs.append(probability)
                rows.append(
                    {
                        "d": d,
                        "pairs": args.pairs,
                        "q_min": qmin,
                        "epsilon": float(epsilon),
                        "F": probability,
                    }
                )

            slope = fit_log_slope(eps_values, np.asarray(fs))
            print({"d": d, "q_min": qmin, "log_log_slope": slope, "F": fs})

    if args.csv:
        path = Path(args.csv)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle, fieldnames=["d", "pairs", "q_min", "epsilon", "F"]
            )
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
