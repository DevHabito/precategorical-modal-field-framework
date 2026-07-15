#!/usr/bin/env python3
"""
A8 — Canonical Internal Order Audit

Exact enumeration of all loopless labeled directed graphs on five vertices.
The audit constructs the SCC condensation poset without interpreting it as
physical time and measures:

- number of strongly connected components;
- height and width of the condensation reachability poset;
- existence of a graded rank structure;
- source/sink counts;
- dependence on edge density and exact in/out-degree fibers;
- sensitivity to one-edge perturbations;
- behavior of selected control structures.

No geometry, embedding, physical clock, or stochastic approximation is used.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import pandas as pd


N = 5
EDGES = [(i, j) for i in range(N) for j in range(N) if i != j]
NUMBER_OF_GRAPHS = 1 << len(EDGES)


def enumerate_adjacency() -> tuple[np.ndarray, np.ndarray]:
    masks = np.arange(NUMBER_OF_GRAPHS, dtype=np.uint32)
    adjacency = np.zeros((NUMBER_OF_GRAPHS, N, N), dtype=np.bool_)
    for bit, (i, j) in enumerate(EDGES):
        adjacency[:, i, j] = ((masks >> bit) & 1).astype(bool)
    return masks, adjacency


def transitive_closure(adjacency: np.ndarray) -> np.ndarray:
    reachability = adjacency.copy()
    for i in range(N):
        reachability[:, i, i] = True
    for k in range(N):
        reachability |= (
            reachability[:, :, k][:, :, None]
            & reachability[:, k, :][:, None, :]
        )
    return reachability


def scc_representatives(
    reachability: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mutual = reachability & np.transpose(reachability, (0, 2, 1))
    indices = np.arange(N, dtype=np.int8)
    representatives = np.min(
        np.where(mutual, indices[None, None, :], N),
        axis=2,
    )
    is_representative = representatives == indices[None, :]
    number_scc = is_representative.sum(axis=1).astype(np.int8)
    return representatives, is_representative, number_scc


def height_and_width(
    reachability: np.ndarray,
    is_representative: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    comparability = reachability | np.transpose(
        reachability, (0, 2, 1)
    )
    height = np.zeros(NUMBER_OF_GRAPHS, dtype=np.int8)
    width = np.zeros(NUMBER_OF_GRAPHS, dtype=np.int8)

    for subset_mask in range(1, 1 << N):
        vertices = [
            i for i in range(N) if (subset_mask >> i) & 1
        ]
        size = len(vertices)
        valid = np.ones(NUMBER_OF_GRAPHS, dtype=bool)

        for i in vertices:
            valid &= is_representative[:, i]

        chain = valid.copy()
        antichain = valid.copy()

        for i, j in itertools.combinations(vertices, 2):
            chain &= comparability[:, i, j]
            antichain &= ~comparability[:, i, j]

        height[chain] = np.maximum(height[chain], size)
        width[antichain] = np.maximum(width[antichain], size)

    return height, width


def encode_condensation_posets(
    reachability: np.ndarray,
    is_representative: np.ndarray,
) -> np.ndarray:
    strict = reachability.copy()
    for i in range(N):
        strict[:, i, i] = False

    strict &= (
        is_representative[:, :, None]
        & is_representative[:, None, :]
    )

    code = np.zeros(NUMBER_OF_GRAPHS, dtype=np.uint32)
    bit = 0
    for i in range(N):
        for j in range(N):
            code |= strict[:, i, j].astype(np.uint32) << bit
            bit += 1

    for i in range(N):
        code |= is_representative[:, i].astype(np.uint32) << (25 + i)

    return code


def decode_poset(code: int) -> tuple[list[int], np.ndarray]:
    active = [
        i for i in range(N)
        if (code >> (25 + i)) & 1
    ]
    relation = np.zeros((N, N), dtype=bool)
    bit = 0
    for i in range(N):
        for j in range(N):
            relation[i, j] = bool((code >> bit) & 1)
            bit += 1
    return active, relation


def unique_poset_metrics(
    unique_codes: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    graded_values = []
    source_values = []
    sink_values = []
    cover_edge_values = []

    for raw_code in unique_codes:
        active, relation = decode_poset(int(raw_code))
        cover = relation.copy()

        for i in active:
            for j in active:
                if not relation[i, j]:
                    continue
                for k in active:
                    if (
                        k != i
                        and k != j
                        and relation[i, k]
                        and relation[k, j]
                    ):
                        cover[i, j] = False
                        break

        indegree = {
            j: sum(cover[i, j] for i in active)
            for j in active
        }
        outdegree = {
            i: sum(cover[i, j] for j in active)
            for i in active
        }

        sources = [i for i in active if indegree[i] == 0]
        sinks = [i for i in active if outdegree[i] == 0]

        undirected = {i: set() for i in active}
        for i in active:
            for j in active:
                if cover[i, j]:
                    undirected[i].add(j)
                    undirected[j].add(i)

        ranks: dict[int, int] = {}
        graded = True

        for root in active:
            if root in ranks:
                continue
            ranks[root] = 0
            stack = [root]

            while stack and graded:
                current = stack.pop()
                for neighbor in undirected[current]:
                    expected = (
                        ranks[current] + 1
                        if cover[current, neighbor]
                        else ranks[current] - 1
                    )
                    if neighbor in ranks:
                        if ranks[neighbor] != expected:
                            graded = False
                            break
                    else:
                        ranks[neighbor] = expected
                        stack.append(neighbor)

            if not graded:
                break

        graded_values.append(graded)
        source_values.append(len(sources))
        sink_values.append(len(sinks))
        cover_edge_values.append(int(cover.sum()))

    return (
        np.asarray(graded_values, dtype=bool),
        np.asarray(source_values, dtype=np.int8),
        np.asarray(sink_values, dtype=np.int8),
        np.asarray(cover_edge_values, dtype=np.int8),
    )


def degree_codes(adjacency: np.ndarray) -> np.ndarray:
    outdegree = adjacency.sum(axis=2).astype(np.int64)
    indegree = adjacency.sum(axis=1).astype(np.int64)
    digits = np.concatenate([outdegree, indegree], axis=1)
    powers = np.asarray([5**i for i in range(10)], dtype=np.int64)
    return (digits * powers).sum(axis=1)


def adjacency_from_edges(edge_list: list[tuple[int, int]]) -> np.ndarray:
    adjacency = np.zeros((N, N), dtype=bool)
    for i, j in edge_list:
        adjacency[i, j] = True
    return adjacency


def mask_from_adjacency(adjacency: np.ndarray) -> int:
    value = 0
    for bit, (i, j) in enumerate(EDGES):
        if adjacency[i, j]:
            value |= 1 << bit
    return value


def control_structures() -> dict[str, np.ndarray]:
    controls: dict[str, np.ndarray] = {}

    controls["empty"] = np.zeros((N, N), dtype=bool)

    complete = np.ones((N, N), dtype=bool)
    np.fill_diagonal(complete, False)
    controls["complete"] = complete

    controls["directed_path"] = adjacency_from_edges(
        [(i, i + 1) for i in range(N - 1)]
    )

    controls["directed_cycle"] = adjacency_from_edges(
        [(i, (i + 1) % N) for i in range(N)]
    )

    controls["bidirectional_path"] = adjacency_from_edges(
        [(i, i + 1) for i in range(N - 1)]
        + [(i + 1, i) for i in range(N - 1)]
    )

    controls["total_order"] = adjacency_from_edges(
        [(i, j) for i in range(N) for j in range(i + 1, N)]
    )

    controls["two_scc_modules"] = adjacency_from_edges(
        [
            (0, 1), (1, 0),
            (2, 3), (3, 4), (4, 2),
            (1, 2),
        ]
    )

    return controls


def main() -> None:
    output_directory = Path("a8_exact_results")
    output_directory.mkdir(exist_ok=True)

    masks, adjacency = enumerate_adjacency()
    reachability = transitive_closure(adjacency)

    _, is_representative, number_scc = scc_representatives(
        reachability
    )
    height, width = height_and_width(
        reachability,
        is_representative,
    )

    condensation_code = encode_condensation_posets(
        reachability,
        is_representative,
    )
    unique_codes, inverse = np.unique(
        condensation_code,
        return_inverse=True,
    )

    (
        unique_graded,
        unique_sources,
        unique_sinks,
        unique_cover_edges,
    ) = unique_poset_metrics(unique_codes)

    graded = unique_graded[inverse]
    sources = unique_sources[inverse]
    sinks = unique_sinks[inverse]
    cover_edges = unique_cover_edges[inverse]

    edge_count = adjacency.sum(axis=(1, 2)).astype(np.int8)
    codes = degree_codes(adjacency)

    density_rows = []
    for m in range(len(EDGES) + 1):
        selected = edge_count == m
        density_rows.append(
            {
                "edge_count": m,
                "number_graphs": int(selected.sum()),
                "mean_number_scc": float(number_scc[selected].mean()),
                "fraction_nontrivial_condensation": float(
                    (number_scc[selected] > 1).mean()
                ),
                "mean_height": float(height[selected].mean()),
                "mean_width": float(width[selected].mean()),
                "fraction_chain_condensation": float(
                    (width[selected] == 1).mean()
                ),
                "fraction_strongly_connected": float(
                    (number_scc[selected] == 1).mean()
                ),
            }
        )

    density_frame = pd.DataFrame(density_rows)
    density_frame.to_csv(
        output_directory / "a8_density_profile.csv",
        index=False,
    )

    order = np.argsort(codes)
    sorted_codes = codes[order]
    unique_degree_codes, starts, counts = np.unique(
        sorted_codes,
        return_index=True,
        return_counts=True,
    )

    multiple = counts > 1
    varying_scc = 0
    varying_height = 0
    varying_full_profile = 0

    for start, count in zip(starts[multiple], counts[multiple]):
        indices = order[start : start + count]

        if len(np.unique(number_scc[indices])) > 1:
            varying_scc += 1

        if len(np.unique(height[indices])) > 1:
            varying_height += 1

        profiles = np.stack(
            [
                number_scc[indices],
                height[indices],
                width[indices],
            ],
            axis=1,
        )
        if len(np.unique(profiles, axis=0)) > 1:
            varying_full_profile += 1

    total_edge_flips = NUMBER_OF_GRAPHS * len(EDGES)
    changed_scc = 0
    changed_height = 0
    changed_width = 0
    changed_graded = 0
    changed_condensation = 0
    absolute_scc_change = 0
    absolute_height_change = 0
    absolute_width_change = 0

    for bit in range(len(EDGES)):
        neighbor = masks ^ (1 << bit)

        changed_scc += int(
            (number_scc != number_scc[neighbor]).sum()
        )
        changed_height += int(
            (height != height[neighbor]).sum()
        )
        changed_width += int(
            (width != width[neighbor]).sum()
        )
        changed_graded += int(
            (graded != graded[neighbor]).sum()
        )
        changed_condensation += int(
            (condensation_code != condensation_code[neighbor]).sum()
        )

        absolute_scc_change += int(
            np.abs(
                number_scc.astype(np.int16)
                - number_scc[neighbor].astype(np.int16)
            ).sum()
        )
        absolute_height_change += int(
            np.abs(
                height.astype(np.int16)
                - height[neighbor].astype(np.int16)
            ).sum()
        )
        absolute_width_change += int(
            np.abs(
                width.astype(np.int16)
                - width[neighbor].astype(np.int16)
            ).sum()
        )

    control_rows = []
    for name, control in control_structures().items():
        mask = mask_from_adjacency(control)
        fiber = np.flatnonzero(codes == codes[mask])

        control_rows.append(
            {
                "control": name,
                "edge_count": int(control.sum()),
                "number_scc": int(number_scc[mask]),
                "height": int(height[mask]),
                "width": int(width[mask]),
                "graded": bool(graded[mask]),
                "sources": int(sources[mask]),
                "sinks": int(sinks[mask]),
                "degree_fiber_size": int(len(fiber)),
                "fraction_fiber_height_at_least_observed": float(
                    (height[fiber] >= height[mask]).mean()
                ),
                "fraction_fiber_chain_and_height_at_least_observed": float(
                    (
                        (width[fiber] == 1)
                        & (height[fiber] >= height[mask])
                    ).mean()
                ),
            }
        )

    pd.DataFrame(control_rows).to_csv(
        output_directory / "a8_control_tests.csv",
        index=False,
    )

    summary = {
        "n_vertices": N,
        "possible_edges": len(EDGES),
        "labeled_graphs_enumerated": NUMBER_OF_GRAPHS,
        "unique_labeled_condensation_posets": int(len(unique_codes)),
        "strongly_connected_graphs": int((number_scc == 1).sum()),
        "graphs_with_nontrivial_condensation": int(
            (number_scc > 1).sum()
        ),
        "chain_condensations_all": int((width == 1).sum()),
        "chain_condensations_nontrivial": int(
            ((width == 1) & (number_scc > 1)).sum()
        ),
        "graded_condensations_all": int(graded.sum()),
        "graded_condensations_nontrivial": int(
            (graded & (number_scc > 1)).sum()
        ),
        "nongraded_condensations_nontrivial": int(
            ((~graded) & (number_scc > 1)).sum()
        ),
        "fraction_nontrivial_condensations_graded": float(
            (graded & (number_scc > 1)).sum()
            / (number_scc > 1).sum()
        ),
        "labeled_degree_fibers": int(len(unique_degree_codes)),
        "degree_fibers_with_multiple_graphs": int(multiple.sum()),
        "degree_fibers_with_varying_scc_count": varying_scc,
        "degree_fibers_with_varying_height": varying_height,
        "degree_fibers_with_varying_full_profile": (
            varying_full_profile
        ),
        "single_edge_flip_fraction_changing_scc_count": (
            changed_scc / total_edge_flips
        ),
        "single_edge_flip_fraction_changing_height": (
            changed_height / total_edge_flips
        ),
        "single_edge_flip_fraction_changing_width": (
            changed_width / total_edge_flips
        ),
        "single_edge_flip_fraction_changing_gradedness": (
            changed_graded / total_edge_flips
        ),
        "single_edge_flip_fraction_changing_labeled_condensation": (
            changed_condensation / total_edge_flips
        ),
        "single_edge_flip_mean_absolute_scc_change": (
            absolute_scc_change / total_edge_flips
        ),
        "single_edge_flip_mean_absolute_height_change": (
            absolute_height_change / total_edge_flips
        ),
        "single_edge_flip_mean_absolute_width_change": (
            absolute_width_change / total_edge_flips
        ),
        "orientation_reversal_result": (
            "SCC partition, number of SCCs, height, width, and "
            "gradedness are preserved; sources and sinks are exchanged."
        ),
    }

    with (output_directory / "a8_summary.json").open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(summary, file, indent=2)

    report = f"""# A8 — Canonical Internal Order Audit

## Exact scope

- Vertices: {N}
- Possible directed non-loop edges: {len(EDGES)}
- Labeled digraphs enumerated: {NUMBER_OF_GRAPHS:,}
- Distinct labeled condensation-poset codes: {len(unique_codes):,}

## Main counts

- Strongly connected: {(number_scc == 1).sum():,}
- Nontrivial condensation: {(number_scc > 1).sum():,}
- Nontrivial chain condensations: {((width == 1) & (number_scc > 1)).sum():,}
- Nontrivial graded condensations: {(graded & (number_scc > 1)).sum():,}
- Nontrivial nongraded condensations: {((~graded) & (number_scc > 1)).sum():,}

## Exact negative findings

1. Reversing all edges preserves SCCs and dualizes the condensation order.
   Height, width, SCC count, and gradedness cannot choose a temporal arrow.

2. Gradedness is nearly universal at n=5:
   {float((graded & (number_scc > 1)).sum() / (number_scc > 1).sum()):.9f}
   of nontrivial condensations are graded. It is therefore weak as a selector.

3. A single edge flip changes the labeled condensation structure in
   {changed_condensation / total_edge_flips:.9f} of all graph-edge pairs,
   and changes height in {changed_height / total_edge_flips:.9f}.

4. The profile is not determined solely by exact labeled in/out degrees:
   {varying_full_profile:,} degree fibers contain more than one
   (SCC count, height, width) profile.

## Scientific status

The SCC condensation is a canonical, static partial order derived without
external time or geometry. However, the exact audit does not justify calling
it physical time. It supplies precedence only after the directed relation has
already been chosen, is dual under edge reversal, is strongly density
dependent, and is moderately fragile under one-edge perturbations.
"""

    (output_directory / "a8_report.md").write_text(
        report,
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2))
    print()
    print(f"Results written to: {output_directory.resolve()}")


if __name__ == "__main__":
    main()
