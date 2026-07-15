#!/usr/bin/env python3
"""
A10 — Internal Duration Audit

Exact enumeration over all loopless labeled digraphs on five vertices.
Each graph is reduced to the partial order of its strongly connected
components. Three order-derived duration candidates are audited:

1. L(x,y): longest-chain length between comparable SCCs.
2. V(x,y): interval cardinality |[x,y]| - 1.
3. R(x,y): rank difference, where a genuine rank function exists.

Tests:
- positivity and isomorphism invariance by construction;
- superadditivity and exact additivity on x<y<z;
- equivalence of rank difference and longest-chain length in graded posets;
- dependence on density and exact degree fibers;
- sensitivity of duration signatures to one-edge perturbations;
- behavior on selected controls.

No candidate is interpreted as physical proper time without a separate
continuum correspondence and operational clock construction.
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


def scc_data(
    reachability: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mutual = reachability & np.transpose(reachability, (0, 2, 1))
    labels = np.arange(N, dtype=np.int8)
    representatives = np.min(
        np.where(mutual, labels[None, None, :], N),
        axis=2,
    )
    is_representative = representatives == labels[None, :]
    number_scc = is_representative.sum(axis=1).astype(np.int8)
    return representatives, is_representative, number_scc


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
    active = [i for i in range(N) if (code >> (25 + i)) & 1]
    strict = np.zeros((N, N), dtype=bool)

    bit = 0
    for i in range(N):
        for j in range(N):
            strict[i, j] = bool((code >> bit) & 1)
            bit += 1

    return active, strict


def cover_relation(active: list[int], strict: np.ndarray) -> np.ndarray:
    cover = strict.copy()
    for i in active:
        for j in active:
            if not strict[i, j]:
                continue
            if any(
                k != i
                and k != j
                and strict[i, k]
                and strict[k, j]
                for k in active
            ):
                cover[i, j] = False
    return cover


def topological_order(active: list[int], strict: np.ndarray) -> list[int]:
    remaining = set(active)
    order: list[int] = []

    while remaining:
        minima = sorted(
            vertex
            for vertex in remaining
            if not any(
                parent in remaining and strict[parent, vertex]
                for parent in remaining
            )
        )
        if not minima:
            raise RuntimeError("Strict relation is not acyclic.")
        order.extend(minima)
        remaining.difference_update(minima)

    return order


def rank_function(
    active: list[int],
    cover: np.ndarray,
    order: list[int],
) -> tuple[bool, np.ndarray]:
    rank = np.full(N, np.nan, dtype=float)
    graded = True

    for vertex in order:
        predecessors = [
            parent for parent in active if cover[parent, vertex]
        ]
        if not predecessors:
            rank[vertex] = 0.0
            continue

        candidate_ranks = {
            rank[parent] + 1.0 for parent in predecessors
        }
        if len(candidate_ranks) != 1:
            graded = False
            break
        rank[vertex] = candidate_ranks.pop()

    return graded, rank


def unit_cover_potential(
    active: list[int],
    cover: np.ndarray,
) -> tuple[bool, np.ndarray]:
    """
    Test existence of an integer potential increasing by one on every cover.

    Unlike the standard rank normalization, distinct minimal elements are
    not forced to have the same value. This is the exact path-independence
    condition for unit cover increments.
    """
    potential = np.full(N, np.nan, dtype=float)
    undirected = {vertex: set() for vertex in active}

    for i in active:
        for j in active:
            if cover[i, j]:
                undirected[i].add(j)
                undirected[j].add(i)

    assigned: dict[int, int] = {}
    consistent = True

    for root in active:
        if root in assigned:
            continue
        assigned[root] = 0
        stack = [root]

        while stack and consistent:
            current = stack.pop()
            for neighbor in undirected[current]:
                expected = (
                    assigned[current] + 1
                    if cover[current, neighbor]
                    else assigned[current] - 1
                )
                if neighbor in assigned:
                    if assigned[neighbor] != expected:
                        consistent = False
                        break
                else:
                    assigned[neighbor] = expected
                    stack.append(neighbor)

        if not consistent:
            break

    if consistent:
        for vertex, value in assigned.items():
            potential[vertex] = float(value)

    return consistent, potential


def longest_chain_distances(
    active: list[int],
    strict: np.ndarray,
    order: list[int],
) -> np.ndarray:
    distance = np.full((N, N), -1, dtype=np.int8)
    for vertex in active:
        distance[vertex, vertex] = 0

    position = {vertex: index for index, vertex in enumerate(order)}

    for source in active:
        for target in order[position[source] + 1 :]:
            if not strict[source, target]:
                continue
            predecessors = [
                middle
                for middle in active
                if (
                    middle != target
                    and (middle == source or strict[source, middle])
                    and strict[middle, target]
                    and distance[source, middle] >= 0
                )
            ]
            if predecessors:
                distance[source, target] = 1 + max(
                    distance[source, middle]
                    for middle in predecessors
                )
            else:
                distance[source, target] = 1

    return distance


def interval_volume(
    active: list[int],
    strict: np.ndarray,
) -> np.ndarray:
    reflexive = strict.copy()
    for vertex in active:
        reflexive[vertex, vertex] = True

    volume = np.full((N, N), -1, dtype=np.int8)

    for source in active:
        for target in active:
            if source == target:
                volume[source, target] = 0
                continue
            if not strict[source, target]:
                continue

            interval_size = sum(
                reflexive[source, middle]
                and reflexive[middle, target]
                for middle in active
            )
            volume[source, target] = interval_size - 1

    return volume


def poset_duration_metrics(
    active: list[int],
    strict: np.ndarray,
) -> dict[str, object]:
    cover = cover_relation(active, strict)
    order = topological_order(active, strict)
    standard_ranked, rank = rank_function(active, cover, order)
    cover_potential_exists, cover_potential = unit_cover_potential(
        active, cover
    )
    longest = longest_chain_distances(active, strict, order)
    volume = interval_volume(active, strict)

    comparable_pairs = [
        (i, j)
        for i in active
        for j in active
        if strict[i, j]
    ]

    triples = [
        (i, j, k)
        for i in active
        for j in active
        for k in active
        if strict[i, j] and strict[j, k]
    ]

    longest_defects = []
    volume_defects = []

    for i, j, k in triples:
        longest_defects.append(
            int(longest[i, k] - longest[i, j] - longest[j, k])
        )
        volume_defects.append(
            int(volume[i, k] - volume[i, j] - volume[j, k])
        )

    longest_additive = all(defect == 0 for defect in longest_defects)
    volume_additive = all(defect == 0 for defect in volume_defects)

    rank_matches_longest = True
    if standard_ranked:
        rank_matches_longest = all(
            int(rank[j] - rank[i]) == int(longest[i, j])
            for i, j in comparable_pairs
        )

    cover_potential_matches_longest = True
    if cover_potential_exists:
        cover_potential_matches_longest = all(
            int(cover_potential[j] - cover_potential[i])
            == int(longest[i, j])
            for i, j in comparable_pairs
        )

    longest_histogram = [
        sum(longest[i, j] == length for i, j in comparable_pairs)
        for length in range(1, N)
    ]
    volume_histogram = [
        sum(volume[i, j] == value for i, j in comparable_pairs)
        for value in range(1, N)
    ]

    return {
        "standard_ranked": standard_ranked,
        "cover_potential_exists": cover_potential_exists,
        "rank": rank,
        "cover_potential": cover_potential,
        "longest": longest,
        "volume": volume,
        "number_comparable_pairs": len(comparable_pairs),
        "number_comparable_triples": len(triples),
        "longest_defects": longest_defects,
        "volume_defects": volume_defects,
        "longest_additive_all_triples": longest_additive,
        "volume_additive_all_triples": volume_additive,
        "rank_matches_longest": rank_matches_longest,
        "cover_potential_matches_longest": (
            cover_potential_matches_longest
        ),
        "longest_histogram": longest_histogram,
        "volume_histogram": volume_histogram,
        "maximum_longest_duration": (
            max(
                [longest[i, j] for i, j in comparable_pairs],
                default=0,
            )
        ),
        "maximum_interval_duration": (
            max(
                [volume[i, j] for i, j in comparable_pairs],
                default=0,
            )
        ),
        "pair_equal_longest_volume": sum(
            longest[i, j] == volume[i, j]
            for i, j in comparable_pairs
        ),
    }


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

    controls["total_order"] = adjacency_from_edges(
        [(i, j) for i in range(N) for j in range(i + 1, N)]
    )

    controls["diamond"] = adjacency_from_edges(
        [(0, 1), (0, 2), (1, 3), (2, 3)]
    )

    controls["unequal_branches"] = adjacency_from_edges(
        [(0, 1), (1, 4), (0, 2), (2, 3), (3, 4)]
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
    output_directory = Path("a10_exact_results")
    output_directory.mkdir(exist_ok=True)

    masks, adjacency = enumerate_adjacency()
    reachability = transitive_closure(adjacency)
    _, is_representative, number_scc = scc_data(reachability)
    codes = encode_condensation_posets(reachability, is_representative)
    unique_codes, inverse = np.unique(codes, return_inverse=True)

    rows = []
    signature_to_id: dict[tuple[int, ...], int] = {}
    unique_signature_ids = np.empty(len(unique_codes), dtype=np.int32)
    unique_max_longest = np.zeros(len(unique_codes), dtype=np.int8)
    unique_max_volume = np.zeros(len(unique_codes), dtype=np.int8)
    unique_standard_ranked = np.zeros(len(unique_codes), dtype=bool)
    unique_cover_potential = np.zeros(len(unique_codes), dtype=bool)

    total_triples = 0
    total_longest_additive_triples = 0
    total_volume_additive_triples = 0
    total_longest_defect = 0
    total_volume_defect = 0
    total_pairs = 0
    total_pairs_equal = 0

    for index, raw_code in enumerate(unique_codes):
        active, strict = decode_poset(int(raw_code))
        result = poset_duration_metrics(active, strict)

        longest_defects = result["longest_defects"]
        volume_defects = result["volume_defects"]

        total_triples += len(longest_defects)
        total_longest_additive_triples += sum(
            defect == 0 for defect in longest_defects
        )
        total_volume_additive_triples += sum(
            defect == 0 for defect in volume_defects
        )
        total_longest_defect += sum(longest_defects)
        total_volume_defect += sum(volume_defects)

        total_pairs += result["number_comparable_pairs"]
        total_pairs_equal += result["pair_equal_longest_volume"]

        signature = tuple(
            result["longest_histogram"]
            + result["volume_histogram"]
            + [
                int(result["standard_ranked"]),
                int(result["cover_potential_exists"]),
            ]
        )
        if signature not in signature_to_id:
            signature_to_id[signature] = len(signature_to_id)
        unique_signature_ids[index] = signature_to_id[signature]
        unique_max_longest[index] = result["maximum_longest_duration"]
        unique_max_volume[index] = result["maximum_interval_duration"]
        unique_standard_ranked[index] = result["standard_ranked"]
        unique_cover_potential[index] = result[
            "cover_potential_exists"
        ]

        rows.append(
            {
                "code": int(raw_code),
                "number_scc": len(active),
                "standard_ranked": bool(
                    result["standard_ranked"]
                ),
                "cover_potential_exists": bool(
                    result["cover_potential_exists"]
                ),
                "number_comparable_pairs": result[
                    "number_comparable_pairs"
                ],
                "number_comparable_triples": result[
                    "number_comparable_triples"
                ],
                "longest_additive_all_triples": result[
                    "longest_additive_all_triples"
                ],
                "volume_additive_all_triples": result[
                    "volume_additive_all_triples"
                ],
                "rank_matches_longest": result[
                    "rank_matches_longest"
                ],
                "cover_potential_matches_longest": result[
                    "cover_potential_matches_longest"
                ],
                "maximum_longest_duration": result[
                    "maximum_longest_duration"
                ],
                "maximum_interval_duration": result[
                    "maximum_interval_duration"
                ],
                "mean_longest_defect": (
                    float(np.mean(longest_defects))
                    if longest_defects
                    else 0.0
                ),
                "mean_volume_defect": (
                    float(np.mean(volume_defects))
                    if volume_defects
                    else 0.0
                ),
                "longest_histogram": str(
                    result["longest_histogram"]
                ),
                "volume_histogram": str(
                    result["volume_histogram"]
                ),
            }
        )

    poset_frame = pd.DataFrame(rows)
    poset_frame.to_csv(
        output_directory / "a10_poset_duration_profiles.csv",
        index=False,
    )

    graph_signature = unique_signature_ids[inverse]
    graph_max_longest = unique_max_longest[inverse]
    graph_max_volume = unique_max_volume[inverse]
    graph_standard_ranked = unique_standard_ranked[inverse]
    graph_cover_potential = unique_cover_potential[inverse]
    edge_count = adjacency.sum(axis=(1, 2)).astype(np.int8)

    density_rows = []
    for m in range(len(EDGES) + 1):
        selected = edge_count == m
        density_rows.append(
            {
                "edge_count": m,
                "number_graphs": int(selected.sum()),
                "mean_max_longest_duration": float(
                    graph_max_longest[selected].mean()
                ),
                "mean_max_interval_duration": float(
                    graph_max_volume[selected].mean()
                ),
                "fraction_standard_ranked": float(
                    graph_standard_ranked[selected].mean()
                ),
                "fraction_cover_potential": float(
                    graph_cover_potential[selected].mean()
                ),
                "fraction_nontrivial_duration": float(
                    (graph_max_longest[selected] > 0).mean()
                ),
            }
        )

    pd.DataFrame(density_rows).to_csv(
        output_directory / "a10_density_profile.csv",
        index=False,
    )

    codes_by_degree = degree_codes(adjacency)
    order = np.argsort(codes_by_degree)
    sorted_degree_codes = codes_by_degree[order]
    _, starts, counts = np.unique(
        sorted_degree_codes,
        return_index=True,
        return_counts=True,
    )

    multiple = counts > 1
    fibers_varying_signature = 0
    fibers_varying_max_longest = 0
    fibers_varying_standard_ranked = 0
    fibers_varying_cover_potential = 0

    for start, count in zip(starts[multiple], counts[multiple]):
        indices = order[start : start + count]
        fibers_varying_signature += (
            len(np.unique(graph_signature[indices])) > 1
        )
        fibers_varying_max_longest += (
            len(np.unique(graph_max_longest[indices])) > 1
        )
        fibers_varying_standard_ranked += (
            len(np.unique(graph_standard_ranked[indices])) > 1
        )
        fibers_varying_cover_potential += (
            len(np.unique(graph_cover_potential[indices])) > 1
        )

    total_edge_flips = NUMBER_OF_GRAPHS * len(EDGES)
    changed_signature = 0
    changed_max_longest = 0
    changed_max_volume = 0
    changed_standard_ranked = 0
    changed_cover_potential = 0

    for bit in range(len(EDGES)):
        neighbor = masks ^ (1 << bit)
        changed_signature += int(
            (graph_signature != graph_signature[neighbor]).sum()
        )
        changed_max_longest += int(
            (graph_max_longest != graph_max_longest[neighbor]).sum()
        )
        changed_max_volume += int(
            (graph_max_volume != graph_max_volume[neighbor]).sum()
        )
        changed_standard_ranked += int(
            (
                graph_standard_ranked
                != graph_standard_ranked[neighbor]
            ).sum()
        )
        changed_cover_potential += int(
            (
                graph_cover_potential
                != graph_cover_potential[neighbor]
            ).sum()
        )

    control_rows = []
    controls = control_structures()

    for name, control in controls.items():
        mask = mask_from_adjacency(control)
        poset_index = inverse[mask]
        row = poset_frame.iloc[poset_index].to_dict()
        row.update(
            {
                "control": name,
                "edge_count": int(control.sum()),
            }
        )
        control_rows.append(row)

    pd.DataFrame(control_rows).to_csv(
        output_directory / "a10_control_tests.csv",
        index=False,
    )

    nontrivial_posets = poset_frame[
        poset_frame["number_scc"] > 1
    ]

    summary = {
        "n_vertices": N,
        "labeled_digraphs": NUMBER_OF_GRAPHS,
        "unique_labeled_condensation_posets": int(len(unique_codes)),
        "nontrivial_unique_condensation_posets": int(
            len(nontrivial_posets)
        ),
        "fraction_nontrivial_posets_standard_ranked": float(
            nontrivial_posets["standard_ranked"].mean()
        ),
        "fraction_nontrivial_posets_cover_potential_exists": float(
            nontrivial_posets["cover_potential_exists"].mean()
        ),
        "fraction_nontrivial_posets_longest_additive_all_triples": float(
            nontrivial_posets[
                "longest_additive_all_triples"
            ].mean()
        ),
        "fraction_nontrivial_posets_volume_additive_all_triples": float(
            nontrivial_posets[
                "volume_additive_all_triples"
            ].mean()
        ),
        "fraction_all_comparable_triples_longest_additive": (
            total_longest_additive_triples / total_triples
            if total_triples
            else 1.0
        ),
        "fraction_all_comparable_triples_volume_additive": (
            total_volume_additive_triples / total_triples
            if total_triples
            else 1.0
        ),
        "mean_longest_superadditivity_defect": (
            total_longest_defect / total_triples
            if total_triples
            else 0.0
        ),
        "mean_volume_superadditivity_defect": (
            total_volume_defect / total_triples
            if total_triples
            else 0.0
        ),
        "fraction_comparable_pairs_longest_equals_interval": (
            total_pairs_equal / total_pairs
            if total_pairs
            else 1.0
        ),
        "all_standard_ranked_posets_rank_matches_longest": bool(
            poset_frame.loc[
                poset_frame["standard_ranked"],
                "rank_matches_longest",
            ].all()
        ),
        "all_cover_potential_posets_match_longest": bool(
            poset_frame.loc[
                poset_frame["cover_potential_exists"],
                "cover_potential_matches_longest",
            ].all()
        ),
        "degree_fibers_with_multiple_graphs": int(multiple.sum()),
        "degree_fibers_varying_duration_signature": int(
            fibers_varying_signature
        ),
        "degree_fibers_varying_max_longest_duration": int(
            fibers_varying_max_longest
        ),
        "degree_fibers_varying_standard_rankedness": int(
            fibers_varying_standard_ranked
        ),
        "degree_fibers_varying_cover_potential": int(
            fibers_varying_cover_potential
        ),
        "single_edge_flip_fraction_changing_duration_signature": (
            changed_signature / total_edge_flips
        ),
        "single_edge_flip_fraction_changing_max_longest_duration": (
            changed_max_longest / total_edge_flips
        ),
        "single_edge_flip_fraction_changing_max_interval_duration": (
            changed_max_volume / total_edge_flips
        ),
        "single_edge_flip_fraction_changing_standard_rankedness": (
            changed_standard_ranked / total_edge_flips
        ),
        "single_edge_flip_fraction_changing_cover_potential": (
            changed_cover_potential / total_edge_flips
        ),
        "coarse_graining_counterexample": {
            "fine_chain": "a<b<c<d",
            "partition": "{a,b}|{c}|{d}",
            "quotient_chain": "A<B<C",
            "max_fine_longest_between_A_B": 2,
            "quotient_longest_A_B": 1,
            "max_fine_longest_between_A_C": 3,
            "quotient_longest_A_C": 2,
            "ratios": ["1/2", "2/3"],
            "conclusion": (
                "No single multiplicative scale preserves both durations."
            ),
        },
    }

    (output_directory / "a10_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    report = f"""# A10 — Internal Duration Audit

## Exact scope

- Labeled loopless digraphs: {NUMBER_OF_GRAPHS:,}
- Vertices: {N}
- Distinct labeled SCC-condensation posets: {len(unique_codes):,}

## Candidates

- L(x,y): longest-chain length.
- V(x,y): interval cardinality minus one.
- R(x,y): rank difference under the standard normalization in which all
  minimal elements have rank zero.
- P(x,y): difference of an integer cover potential, if one exists, without
  forcing distinct minimal elements to share a value.

## Exact algebra

For x<y<z:

L(x,z) >= L(x,y)+L(y,z)

because chains through y can be concatenated.

V(x,z) >= V(x,y)+V(y,z)

because [x,y] union [y,z] is contained in [x,z], with intersection {{y}}.

When the standard rank exists, its difference is additive and equals
longest-chain length on every comparable pair. The same is true for an
integer unit-cover potential. These are distinct existence conditions:
standard rank fixes every minimal element at zero, whereas the weaker cover
potential only demands path-independent unit increments. Neither creates a
new duration beyond longest-chain length in the sector where it exists.

## Interpretation limit

Longest-chain length approximates proper time only in special causal-set
ensembles with a demonstrated manifold correspondence and a dimension-
dependent calibration. This audit supplies neither of those assumptions.
Interval cardinality is a volume-like count, not duration by itself.

## Coarse-graining obstruction

For a<b<c<d and the partition {{a,b}}|{{c}}|{{d}}, the quotient is A<B<C.
Using maximal fine longest-chain separations between fibers gives ratios
1/2 for A-B and 2/3 for A-C. No single scale factor preserves both.
"""

    (output_directory / "a10_report.md").write_text(
        report,
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2))
    print()
    print(f"Results written to: {output_directory.resolve()}")


if __name__ == "__main__":
    main()
