#!/usr/bin/env python3
"""
A3 — Exact Conditional Null Validation
Campo Modal Pré-Categorial / RZS research program

Enumerates all loopless directed graphs on n=5 labeled vertices,
computes the residual/contrast quotient profile T(A), groups graphs
by exact labeled in/out-degree fibers, and evaluates selected controls
under two exact conditional null measures:

1. Uniform over labeled realizations in the degree fiber.
2. Uniform over orbits under the stabilizer of the degree vector.

No Monte Carlo sampling is used.
"""

from __future__ import annotations

import csv
import itertools
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np


N_VERTICES = 5
EDGES = [
    (i, j)
    for i in range(N_VERTICES)
    for j in range(N_VERTICES)
    if i != j
]
N_GRAPHS = 1 << len(EDGES)


def masks_to_adj(masks: np.ndarray) -> np.ndarray:
    masks = np.asarray(masks, dtype=np.uint32)
    arr = np.zeros(
        (len(masks), N_VERTICES, N_VERTICES),
        dtype=np.uint8,
    )
    for bit, (i, j) in enumerate(EDGES):
        arr[:, i, j] = ((masks >> bit) & 1).astype(np.uint8)
    return arr


def mask_from_adj(adjacency: np.ndarray) -> int:
    value = 0
    for bit, (i, j) in enumerate(EDGES):
        if adjacency[i, j]:
            value |= 1 << bit
    return value


def aggregation_partitions() -> list[np.ndarray]:
    """All unlabeled 2+3 partitions of five vertices."""
    result: list[np.ndarray] = []
    for pair in itertools.combinations(range(N_VERTICES), 2):
        block_zero = set(pair)
        labels = np.array(
            [0 if i in block_zero else 1 for i in range(N_VERTICES)],
            dtype=np.int8,
        )
        result.append(labels)
    return result


PARTITIONS = aggregation_partitions()
PARTITION_DATA = []
for labels in PARTITIONS:
    membership = np.zeros((N_VERTICES, 2), dtype=float)
    membership[np.arange(N_VERTICES), labels] = 1.0
    projection = (
        membership
        @ np.linalg.inv(membership.T @ membership)
        @ membership.T
    )
    homogeneous = np.ones((N_VERTICES, N_VERTICES)) / N_VERTICES
    PARTITION_DATA.append(
        (labels, membership, projection, homogeneous)
    )


def vectorized_profile(
    adjacency_batch: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute T(A)=(r*, c*) for a batch.

    Lower r* is better. If r* ties, higher c* is better.
    Squared normalized norms are used, avoiding unnecessary square roots.
    """
    batch_size = adjacency_batch.shape[0]
    best_r = np.full(batch_size, np.inf)
    best_c = np.full(batch_size, -np.inf)

    adjacency = adjacency_batch.astype(float)
    transpose = np.transpose(adjacency, (0, 2, 1))

    for _, membership, projection, homogeneous in PARTITION_DATA:
        outgoing = adjacency @ membership
        incoming = transpose @ membership

        fitted_out = np.einsum(
            "ij,bjk->bik", projection, outgoing
        )
        fitted_in = np.einsum(
            "ij,bjk->bik", projection, incoming
        )
        global_out = np.einsum(
            "ij,bjk->bik", homogeneous, outgoing
        )
        global_in = np.einsum(
            "ij,bjk->bik", homogeneous, incoming
        )

        denominator_out = np.sum(outgoing * outgoing, axis=(1, 2))
        denominator_in = np.sum(incoming * incoming, axis=(1, 2))

        residual_out = np.sum(
            (outgoing - fitted_out) ** 2,
            axis=(1, 2),
        )
        residual_in = np.sum(
            (incoming - fitted_in) ** 2,
            axis=(1, 2),
        )
        contrast_out = np.sum(
            (fitted_out - global_out) ** 2,
            axis=(1, 2),
        )
        contrast_in = np.sum(
            (fitted_in - global_in) ** 2,
            axis=(1, 2),
        )

        r_out = np.divide(
            residual_out,
            denominator_out,
            out=np.zeros_like(residual_out),
            where=denominator_out != 0,
        )
        r_in = np.divide(
            residual_in,
            denominator_in,
            out=np.zeros_like(residual_in),
            where=denominator_in != 0,
        )
        c_out = np.divide(
            contrast_out,
            denominator_out,
            out=np.zeros_like(contrast_out),
            where=denominator_out != 0,
        )
        c_in = np.divide(
            contrast_in,
            denominator_in,
            out=np.zeros_like(contrast_in),
            where=denominator_in != 0,
        )

        residual = np.maximum(r_out, r_in)
        contrast = np.minimum(c_out, c_in)

        better = (
            (residual < best_r - 1e-14)
            | (
                (np.abs(residual - best_r) <= 1e-14)
                & (contrast > best_c + 1e-14)
            )
        )
        best_r[better] = residual[better]
        best_c[better] = contrast[better]

    return best_r, best_c


def scalar_profile(adjacency: np.ndarray) -> tuple[float, float]:
    r, c = vectorized_profile(adjacency[None, :, :])
    return float(r[0]), float(c[0])


def degree_code(adjacency_batch: np.ndarray) -> np.ndarray:
    out_degree = adjacency_batch.sum(axis=2).astype(np.int64)
    in_degree = adjacency_batch.sum(axis=1).astype(np.int64)
    digits = np.concatenate([out_degree, in_degree], axis=1)
    powers = np.array([5**i for i in range(10)], dtype=np.int64)
    return (digits * powers).sum(axis=1)


def decode_degree_code(code: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    digits = []
    remainder = int(code)
    for _ in range(10):
        digits.append(remainder % 5)
        remainder //= 5
    return tuple(digits[:5]), tuple(digits[5:])


def lex_better_or_equal(
    candidate: tuple[float, float],
    observed: tuple[float, float],
    tolerance: float = 1e-12,
) -> bool:
    r, c = candidate
    observed_r, observed_c = observed
    return (
        r < observed_r - tolerance
        or (
            abs(r - observed_r) <= tolerance
            and c >= observed_c - tolerance
        )
    )


PERMUTATIONS = list(itertools.permutations(range(N_VERTICES)))


def degree_stabilizer(
    out_degree: tuple[int, ...],
    in_degree: tuple[int, ...],
) -> list[tuple[int, ...]]:
    degree_pairs = list(zip(out_degree, in_degree))
    return [
        permutation
        for permutation in PERMUTATIONS
        if all(
            degree_pairs[permutation[i]] == degree_pairs[i]
            for i in range(N_VERTICES)
        )
    ]


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    adjacency = masks_to_adj(np.array([mask], dtype=np.uint32))[0]
    permuted = adjacency[np.ix_(permutation, permutation)]
    return mask_from_adj(permuted)


def orbit_representatives(
    masks: list[int],
    out_degree: tuple[int, ...],
    in_degree: tuple[int, ...],
) -> list[int]:
    stabilizer = degree_stabilizer(out_degree, in_degree)
    mask_set = set(masks)
    seen: set[int] = set()
    representatives: list[int] = []

    for mask in masks:
        if mask in seen:
            continue
        orbit = {
            permute_mask(mask, permutation)
            for permutation in stabilizer
        }
        orbit &= mask_set
        seen |= orbit
        representatives.append(min(orbit))
    return representatives


def enumerate_all() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    residual = np.empty(N_GRAPHS, dtype=np.float64)
    contrast = np.empty(N_GRAPHS, dtype=np.float64)
    degrees = np.empty(N_GRAPHS, dtype=np.int64)

    chunk_size = 50_000
    for start in range(0, N_GRAPHS, chunk_size):
        stop = min(start + chunk_size, N_GRAPHS)
        masks = np.arange(start, stop, dtype=np.uint32)
        adjacency = masks_to_adj(masks)
        batch_r, batch_c = vectorized_profile(adjacency)
        residual[start:stop] = batch_r
        contrast[start:stop] = batch_c
        degrees[start:stop] = degree_code(adjacency)

    return residual, contrast, degrees


def control_graphs() -> dict[str, np.ndarray]:
    graphs: dict[str, np.ndarray] = {}

    directed_cycle = np.zeros((5, 5), dtype=np.uint8)
    for i in range(5):
        directed_cycle[i, (i + 1) % 5] = 1
    graphs["directed_C5"] = directed_cycle

    disjoint_cycles = np.zeros((5, 5), dtype=np.uint8)
    disjoint_cycles[0, 1] = disjoint_cycles[1, 0] = 1
    disjoint_cycles[2, 3] = 1
    disjoint_cycles[3, 4] = 1
    disjoint_cycles[4, 2] = 1
    graphs["C2_plus_C3"] = disjoint_cycles

    directed_path = np.zeros((5, 5), dtype=np.uint8)
    for i in range(4):
        directed_path[i, i + 1] = 1
    graphs["directed_path5"] = directed_path

    circulant = np.zeros((5, 5), dtype=np.uint8)
    for i in range(5):
        circulant[i, (i + 1) % 5] = 1
        circulant[i, (i + 2) % 5] = 1
    graphs["circulant_5_12"] = circulant

    bidirectional_cycle = np.zeros((5, 5), dtype=np.uint8)
    for i in range(5):
        bidirectional_cycle[i, (i + 1) % 5] = 1
        bidirectional_cycle[i, (i - 1) % 5] = 1
    graphs["bidirectional_C5"] = bidirectional_cycle

    complement_cycle = np.ones((5, 5), dtype=np.uint8)
    np.fill_diagonal(complement_cycle, 0)
    for i in range(5):
        complement_cycle[i, (i + 1) % 5] = 0
    graphs["complement_directed_C5"] = complement_cycle

    return graphs


def main() -> None:
    output_directory = Path("a3_exact_results")
    output_directory.mkdir(exist_ok=True)

    residual, contrast, degree_codes = enumerate_all()

    order = np.argsort(degree_codes)
    sorted_codes = degree_codes[order]
    sorted_r = np.round(residual[order], 12)
    sorted_c = np.round(contrast[order], 12)

    unique_codes, starts, counts = np.unique(
        sorted_codes,
        return_index=True,
        return_counts=True,
    )

    multiple_mask = counts > 1
    fibers_with_multiple = int(np.sum(multiple_mask))
    fibers_with_residual_variation = 0
    fibers_with_profile_variation = 0

    for start, count in zip(
        starts[multiple_mask],
        counts[multiple_mask],
    ):
        fiber_r = sorted_r[start : start + count]
        fiber_c = sorted_c[start : start + count]

        if len(np.unique(fiber_r)) > 1:
            fibers_with_residual_variation += 1

        pairs = np.stack([fiber_r, fiber_c], axis=1)
        if len(np.unique(pairs, axis=0)) > 1:
            fibers_with_profile_variation += 1

    summary = {
        "n_vertices": N_VERTICES,
        "number_of_possible_edges": len(EDGES),
        "number_of_labeled_graphs": N_GRAPHS,
        "number_of_labeled_degree_fibers": int(len(unique_codes)),
        "fibers_with_more_than_one_graph": fibers_with_multiple,
        "fibers_with_residual_variation": fibers_with_residual_variation,
        "fibers_with_full_profile_variation": fibers_with_profile_variation,
        "largest_fiber_size": int(np.max(counts)),
        "median_nontrivial_fiber_size": float(
            np.median(counts[multiple_mask])
        ),
    }

    with (output_directory / "a3_summary.json").open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(summary, file, indent=2)

    controls = control_graphs()
    control_rows = []

    for name, adjacency in controls.items():
        out_degree = tuple(adjacency.sum(axis=1).tolist())
        in_degree = tuple(adjacency.sum(axis=0).tolist())
        code = int(
            degree_code(adjacency[None, :, :])[0]
        )

        fiber_masks = np.flatnonzero(degree_codes == code).tolist()
        observed = scalar_profile(adjacency)

        fiber_profiles = [
            scalar_profile(
                masks_to_adj(
                    np.array([mask], dtype=np.uint32)
                )[0]
            )
            for mask in fiber_masks
        ]

        labeled_p = (
            sum(
                lex_better_or_equal(profile, observed)
                for profile in fiber_profiles
            )
            / len(fiber_profiles)
        )

        representatives = orbit_representatives(
            fiber_masks,
            out_degree,
            in_degree,
        )
        orbit_profiles = [
            scalar_profile(
                masks_to_adj(
                    np.array([mask], dtype=np.uint32)
                )[0]
            )
            for mask in representatives
        ]
        orbit_p = (
            sum(
                lex_better_or_equal(profile, observed)
                for profile in orbit_profiles
            )
            / len(orbit_profiles)
        )

        control_rows.append(
            {
                "control": name,
                "out_degree": str(out_degree),
                "in_degree": str(in_degree),
                "r_star_squared": observed[0],
                "c_star_squared": observed[1],
                "labeled_fiber_size": len(fiber_masks),
                "exact_labeled_p": labeled_p,
                "orbit_count": len(representatives),
                "exact_orbit_p": orbit_p,
            }
        )

    with (output_directory / "a3_control_tests.csv").open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=list(control_rows[0]),
        )
        writer.writeheader()
        writer.writerows(control_rows)

    print(json.dumps(summary, indent=2))
    print()
    for row in control_rows:
        print(row)


if __name__ == "__main__":
    main()
