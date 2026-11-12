#!/usr/bin/env python3
"""Finite-n UPO audit for conformally weighted Minkowski sprinklings.

A positive conformal rescaling preserves the causal-comparability relation and
changes only the physical sprinkling density.

This script compares:
1. uniform Minkowski volume;
2. a de-Sitter-like conformal density Omega(t)^d with Omega=1/(3-t);
3. a symmetric smooth density Omega(t)^d with Omega=1+0.8 t^2.

The test is diagnostic only.  The theorem is analytic and applies to any
bounded positive density.

No external packages beyond NumPy are required.
"""

from __future__ import annotations

import argparse
import numpy as np


def sprinkle_uniform_diamond(
    n: int,
    d: int,
    rng: np.random.Generator,
) -> np.ndarray:
    spatial_dim = d - 1

    abs_t = 1.0 - rng.random(n) ** (1.0 / d)
    t = abs_t * np.where(
        rng.random(n) < 0.5,
        -1.0,
        1.0,
    )

    direction = rng.normal(size=(n, spatial_dim))
    direction /= np.linalg.norm(
        direction,
        axis=1,
    )[:, None]

    radius = (
        (1.0 - abs_t)
        * rng.random(n) ** (1.0 / spatial_dim)
    )

    spatial = direction * radius[:, None]

    return np.concatenate(
        [t[:, None], spatial],
        axis=1,
    )


def conformal_weight(
    points: np.ndarray,
    d: int,
    model: str,
) -> np.ndarray:
    t = points[:, 0]

    if model == "desitter_like":
        omega = 1.0 / (3.0 - t)
    elif model == "symmetric":
        omega = 1.0 + 0.8 * t * t
    else:
        raise ValueError(model)

    return omega**d


def weight_max(d: int, model: str) -> float:
    if model == "desitter_like":
        return (1.0 / 2.0) ** d
    if model == "symmetric":
        return 1.8**d
    raise ValueError(model)


def sprinkle_weighted_diamond(
    n: int,
    d: int,
    rng: np.random.Generator,
    model: str,
) -> np.ndarray:
    chunks: list[np.ndarray] = []
    total = 0
    wmax = weight_max(d, model)

    while total < n:
        batch = max(64, 3 * (n - total))

        points = sprinkle_uniform_diamond(
            batch,
            d,
            rng,
        )

        weights = conformal_weight(
            points,
            d,
            model,
        )

        accepted = points[
            rng.random(batch)
            <
            weights / wmax
        ]

        if len(accepted):
            chunks.append(accepted)
            total += len(accepted)

    return np.vstack(chunks)[:n]


def adjacency_bitsets(
    points: np.ndarray,
) -> list[int]:
    n = len(points)
    adj = [0] * n

    for i in range(n - 1):
        dt = (
            points[i + 1 :, 0]
            -
            points[i, 0]
        )

        dr2 = np.sum(
            (
                points[i + 1 :, 1 :]
                -
                points[i, 1 :]
            )
            ** 2,
            axis=1,
        )

        js = (
            np.nonzero(
                dt * dt > dr2
            )[0]
            +
            i
            +
            1
        )

        for j0 in js:
            j = int(j0)
            adj[i] |= 1 << j
            adj[j] |= 1 << i

    return adj


def connected_components(
    adj: list[int],
) -> list[list[int]]:
    n = len(adj)
    seen = 0
    result: list[list[int]] = []

    for start in range(n):
        bit = 1 << start

        if seen & bit:
            continue

        seen |= bit
        stack = [start]
        component: list[int] = []

        while stack:
            u = stack.pop()
            component.append(u)

            work = adj[u] & ~seen

            while work:
                next_bit = work & -work
                work -= next_bit

                v = (
                    next_bit.bit_length()
                    -
                    1
                )

                seen |= next_bit
                stack.append(v)

        result.append(component)

    return result


def component_is_upo(
    adj: list[int],
    component: list[int],
) -> bool:
    members = set(component)
    edges: list[tuple[int, int]] = []

    for u in component:
        work = adj[u]

        while work:
            bit = work & -work
            work -= bit
            v = bit.bit_length() - 1

            if u < v and v in members:
                edges.append((u, v))

    if not edges:
        return True

    parent = list(range(len(edges)))

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[
                parent[a]
            ]
            a = parent[a]
        return a

    def union(a: int, b: int) -> None:
        ra = find(a)
        rb = find(b)

        if ra != rb:
            parent[rb] = ra

    incident: dict[
        int,
        list[tuple[int, int]],
    ] = {
        u: []
        for u in component
    }

    for index, (u, v) in enumerate(edges):
        incident[u].append((index, v))
        incident[v].append((index, u))

    for u, edge_list in incident.items():
        del u

        for i in range(len(edge_list)):
            edge_i, endpoint_i = (
                edge_list[i]
            )

            for j in range(
                i + 1,
                len(edge_list),
            ):
                edge_j, endpoint_j = (
                    edge_list[j]
                )

                if (
                    (
                        adj[endpoint_i]
                        >>
                        endpoint_j
                    )
                    &
                    1
                ) == 0:
                    union(
                        edge_i,
                        edge_j,
                    )

    return (
        len(
            {
                find(i)
                for i
                in range(len(edges))
            }
        )
        ==
        1
    )


def orientation_recoverable(
    points: np.ndarray,
) -> bool:
    adj = adjacency_bitsets(points)

    components = connected_components(
        adj
    )

    nontrivial = [
        comp
        for comp in components
        if len(comp) > 1
    ]

    if len(nontrivial) != 1:
        return False

    return component_is_upo(
        adj,
        nontrivial[0],
    )


def parse_int_list(text: str) -> list[int]:
    return [
        int(part.strip())
        for part in text.split(",")
        if part.strip()
    ]


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--d",
        type=int,
        default=4,
    )

    parser.add_argument(
        "--ns",
        default="16,24,32,48",
    )

    parser.add_argument(
        "--reps",
        type=int,
        default=300,
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=20261112,
    )

    args = parser.parse_args()

    models = (
        "uniform",
        "desitter_like",
        "symmetric",
    )

    for n in parse_int_list(args.ns):
        for model_index, model in enumerate(
            models
        ):
            rng = np.random.default_rng(
                args.seed
                +
                1009 * n
                +
                100000 * model_index
            )

            recovered = 0

            for _ in range(args.reps):
                if model == "uniform":
                    points = (
                        sprinkle_uniform_diamond(
                            n,
                            args.d,
                            rng,
                        )
                    )
                else:
                    points = (
                        sprinkle_weighted_diamond(
                            n,
                            args.d,
                            rng,
                            model,
                        )
                    )

                recovered += (
                    orientation_recoverable(
                        points
                    )
                )

            print(
                {
                    "d": args.d,
                    "n": n,
                    "reps": args.reps,
                    "model": model,
                    "upo_fraction":
                        recovered
                        /
                        args.reps,
                }
            )


if __name__ == "__main__":
    main()
