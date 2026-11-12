#!/usr/bin/env python3
"""Null-joint scaling audit for comparable-twin obstructions in M^4.

This script validates the analytic constants for the d=4 null-joint sector:

    F_4(epsilon) joint contribution: 3*pi*epsilon^3
    E[T_n] joint contribution:       9*pi/n

The first constants are analytic.  The optional importance sampler checks the
slow finite-n approach of the exact kernel to the limiting 9*pi coefficient.

The script does not claim that the null-joint contribution is the entire
asymptotic until the complementary bulk/null-face sectors are bounded.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def analytic_constants() -> dict[str, float]:
    # In d=4, m=d/2=2.
    #
    # One-side leading variable:
    #   g(alpha,A) = (alpha+A)^2-alpha^2 = 2 alpha A + A^2.
    #
    # Under A d(alpha) dA, changing variables (alpha,A)->(g,A)
    # gives density w(g)=sqrt(g)/2.
    #
    # H=(g1+g2)/4. Therefore
    #
    # J_step = int_{H<=1} A B d(alpha)dA d(beta)dB = 2*pi/3
    # J_lap  = int exp(-H) A B d(alpha)dA d(beta)dB = 4*pi.
    #
    # The oriented-pair angular/radial coefficient at the joint is K=9/4.
    # F counts both time orientations, so C_F=2*K*J_step=3*pi.
    # In E[T_n], the factor 2 cancels the 1/2 from binom(n,2), giving
    # C_T=K*J_lap=9*pi.
    k_oriented = 9.0 / 4.0
    j_step = 2.0 * math.pi / 3.0
    j_laplace = 4.0 * math.pi

    return {
        "K_oriented": k_oriented,
        "J_step": j_step,
        "J_laplace": j_laplace,
        "F4_joint_tail_coefficient": 2.0 * k_oriented * j_step,
        "ET_joint_coefficient": k_oriented * j_laplace,
    }


def sample_limiting_laplace(
    samples: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Sample from the normalized limiting d=4 Laplace measure.

    With g_i distributed as Gamma(shape=3/2, scale=4), the transformed
    density is proportional to

        A B exp[-(g1+g2)/4] d(alpha)dA d(beta)dB.

    Conditional on g, A is uniform on [0,sqrt(g)] and
    alpha=(g-A^2)/(2A).
    """
    rng = np.random.default_rng(seed)

    g1 = rng.gamma(shape=1.5, scale=4.0, size=samples)
    g2 = rng.gamma(shape=1.5, scale=4.0, size=samples)

    a_inc = np.maximum(rng.random(samples) * np.sqrt(g1), 1.0e-15)
    b_inc = np.maximum(rng.random(samples) * np.sqrt(g2), 1.0e-15)

    alpha = (g1 - a_inc * a_inc) / (2.0 * a_inc)
    beta = (g2 - b_inc * b_inc) / (2.0 * b_inc)

    # In d=4 the relative solid-angle measure inside the causal cap is
    # uniform in u = 2 r_x r_y (1-cos(theta)) / (A B).
    u = rng.random(samples)
    h = (g1 + g2) / 4.0

    return alpha, beta, a_inc, b_inc, u, h


def exact_scaled_delta(
    n: int,
    alpha: np.ndarray,
    beta: np.ndarray,
    a_inc: np.ndarray,
    b_inc: np.ndarray,
    u: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate exact d=4 Delta after the null-joint n^{-1/2} scaling."""
    lam = n ** -0.5

    ax = lam * alpha
    by = lam * beta
    ay = ax + lam * a_inc
    bx = by + lam * b_inc

    rx = 1.0 - 0.5 * (ax + bx)
    ry = 1.0 - 0.5 * (ay + by)

    valid = (
        (rx > 0.0)
        & (ry > 0.0)
        & (ax >= 0.0)
        & (by >= 0.0)
        & (ax + bx <= 2.0)
        & (ay + by <= 2.0)
    )

    px = ax * (2.0 - bx)
    py = ay * (2.0 - by)
    xq = bx * (2.0 - ax)
    yq = by * (2.0 - ay)

    # The cap coordinate u makes the pair proper-time square exact:
    # tau(x,y)^2 = A B (1-u), with physical A,B already scaled by lam.
    xy = (lam * a_inc) * (lam * b_inc) * (1.0 - u)

    delta = (py**2 - px**2 + xq**2 - yq**2 - 2.0 * xy**2) / 16.0

    return delta, rx * ry, valid


def importance_estimate_n_et(
    n: int,
    alpha: np.ndarray,
    beta: np.ndarray,
    a_inc: np.ndarray,
    b_inc: np.ndarray,
    u: np.ndarray,
    h: np.ndarray,
) -> tuple[float, float]:
    """Estimate the null-joint contribution to n*E[T_n]."""
    delta, rr, valid = exact_scaled_delta(n, alpha, beta, a_inc, b_inc, u)

    ok = valid & (delta >= 0.0) & (delta < 1.0)
    log_ratio = np.full(delta.shape, -np.inf)
    log_ratio[ok] = (n - 2) * np.log1p(-delta[ok]) + h[ok]

    ratio = np.zeros(delta.shape)
    ratio[ok] = np.exp(np.clip(log_ratio[ok], -745.0, 50.0))

    weighted = rr * ratio

    # Normalizing integral of the limiting Laplace measure is 4*pi.
    # K=9/4.  The exact binomial correction contributes (n-1)/n.
    factor = ((n - 1.0) / n) * (9.0 / 4.0) * (4.0 * math.pi)

    estimate = factor * float(np.mean(weighted))
    stderr = factor * float(np.std(weighted, ddof=1) / math.sqrt(len(weighted)))
    return estimate, stderr


def parse_int_list(text: str) -> list[int]:
    return [int(part.strip()) for part in text.split(",") if part.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=500_000)
    parser.add_argument("--seed", type=int, default=20261111)
    parser.add_argument(
        "--ns",
        default="100,300,1000,3000,10000,30000,100000",
        help="Comma-separated n values for the importance-sampling check.",
    )
    args = parser.parse_args()

    constants = analytic_constants()
    print("Analytic constants")
    for key, value in constants.items():
        print(f"{key}: {value:.12f}")

    alpha, beta, a_inc, b_inc, u, h = sample_limiting_laplace(
        args.samples, args.seed
    )

    print("\nImportance-sampling finite-n check")
    for n in parse_int_list(args.ns):
        estimate, stderr = importance_estimate_n_et(
            n, alpha, beta, a_inc, b_inc, u, h
        )
        print(
            f"n={n:>7d}  n*E[T_n]_joint={estimate:.8f}  "
            f"MC_SE={stderr:.8f}  target={9.0 * math.pi:.8f}"
        )


if __name__ == "__main__":
    main()
