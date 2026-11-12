#!/usr/bin/env python3
"""Pre-asymptotic audit of the all-dimensional Minkowski edge tail.

Two complementary checks are provided.

1. Direct iid pair Monte Carlo in the full Alexandrov interval estimates

       F_d(eps) = P(X~Y and Delta_d(X,Y) <= eps).

   In high dimension, accessible eps values can display effective slopes well
   below the asymptotic exponent because the null-joint scale is

       lambda = eps^(2/d),

   which shrinks very slowly when d is large.

2. The reduced one-side integral

       J_m(s) = int A^(m-1) 1[((alpha+A)^m-alpha^m)<=s] dA d alpha

   is evaluated deterministically.  It isolates the asymptotic joint scaling
   and converges rapidly to the theoretical exponent.

The script is a diagnostic only; the analytic theorem is in
MINKOWSKI_ALLD_EDGE_TAIL_THEOREM_20261112.md.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import quad


def sprinkle_diamond(n: int, d: int, rng: np.random.Generator) -> np.ndarray:
    spatial_dim = d - 1

    abs_t = 1.0 - rng.random(n) ** (1.0 / d)
    t = abs_t * np.where(rng.random(n) < 0.5, -1.0, 1.0)

    direction = rng.normal(size=(n, spatial_dim))
    direction /= np.linalg.norm(direction, axis=1)[:, None]

    radius = (1.0 - abs_t) * rng.random(n) ** (1.0 / spatial_dim)
    spatial = direction * radius[:, None]

    return np.concatenate([t[:, None], spatial], axis=1)


def tau2(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    dt = b[:, 0] - a[:, 0]
    dr2 = np.sum((b[:, 1:] - a[:, 1:]) ** 2, axis=1)
    return dt * dt - dr2


def comparable_delta(
    x0: np.ndarray,
    y0: np.ndarray,
    d: int,
) -> tuple[np.ndarray, np.ndarray]:
    swap = x0[:, 0] > y0[:, 0]

    x = x0.copy()
    y = y0.copy()
    x[swap] = y0[swap]
    y[swap] = x0[swap]

    p = np.zeros_like(x)
    q = np.zeros_like(x)
    p[:, 0] = -1.0
    q[:, 0] = 1.0

    py = np.maximum(tau2(p, y), 0.0)
    px = np.maximum(tau2(p, x), 0.0)
    xq = np.maximum(tau2(x, q), 0.0)
    yq = np.maximum(tau2(y, q), 0.0)
    xy = np.maximum(tau2(x, y), 0.0)

    m = d / 2.0

    delta = (
        py**m
        - px**m
        + xq**m
        - yq**m
        - 2.0 * xy**m
    ) / (2.0**d)

    return xy > 0.0, delta


def theoretical_beta(d: int) -> float:
    return min(float(d), 2.0 + 4.0 / d)


def estimate_full_tail(
    d: int,
    total_pairs: int,
    eps_values: list[float],
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed + d)
    counts = np.zeros(len(eps_values), dtype=np.int64)

    chunk = min(200_000, total_pairs)
    done = 0

    while done < total_pairs:
        n = min(chunk, total_pairs - done)

        x = sprinkle_diamond(n, d, rng)
        y = sprinkle_diamond(n, d, rng)
        causal, delta = comparable_delta(x, y, d)

        for i, eps in enumerate(eps_values):
            counts[i] += np.count_nonzero(
                causal & (delta <= eps)
            )

        done += n

    return counts / total_pairs, counts


def one_side_J(m: float, s: float, eta: float = 0.5) -> float:
    def integrand(alpha: float) -> float:
        amax = (alpha**m + s) ** (1.0 / m) - alpha
        return amax**m / m

    value, _ = quad(
        integrand,
        0.0,
        eta,
        epsabs=1.0e-13,
        epsrel=1.0e-10,
        limit=400,
    )
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", type=int, default=1_000_000)
    parser.add_argument("--seed", type=int, default=9876)
    args = parser.parse_args()

    grids = {
        3: [0.02, 0.025, 0.03, 0.04, 0.05, 0.07, 0.10],
        4: [0.01, 0.015, 0.02, 0.03, 0.04, 0.05, 0.07],
        5: [0.008, 0.012, 0.016, 0.024, 0.032, 0.045, 0.06],
        6: [0.006, 0.009, 0.012, 0.018, 0.025, 0.035, 0.05],
        8: [0.004, 0.006, 0.009, 0.013, 0.019, 0.028, 0.04],
    }

    for d, eps_values in grids.items():
        f, counts = estimate_full_tail(
            d,
            args.pairs,
            eps_values,
            args.seed,
        )

        beta = theoretical_beta(d)

        print(
            {
                "d": d,
                "beta_theory": beta,
                "joint_scale_at_min_eps":
                    eps_values[0] ** (2.0 / d),
            }
        )

        for eps, value, count in zip(eps_values, f, counts):
            print(
                {
                    "eps": eps,
                    "count": int(count),
                    "F": float(value),
                    "F_over_eps_beta":
                        float(value / eps**beta),
                }
            )

    print("Reduced one-side integral slopes")

    for d in (3, 4, 5, 6, 8):
        m = d / 2.0
        s_values = np.logspace(-8, -3, 11)
        j_values = np.array(
            [one_side_J(m, float(s)) for s in s_values]
        )

        local_slopes = np.diff(np.log(j_values)) / np.diff(
            np.log(s_values)
        )

        if m * (m - 1.0) < 1.0:
            expected = m
        else:
            expected = 1.0 + 1.0 / m

        print(
            {
                "d": d,
                "m": m,
                "expected_one_side_exponent": expected,
                "small_s_slope": float(local_slopes[0]),
                "next_slope": float(local_slopes[1]),
            }
        )


if __name__ == "__main__":
    main()
