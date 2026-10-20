#!/usr/bin/env python3
"""Check small directed-graph edge toggles with an independent DFS oracle.

This is an exhaustive finite control, not an all-size mathematical proof.
"""

from __future__ import annotations


def directed_edges(vertices: int) -> list[tuple[int, int]]:
    return [
        (source, target)
        for source in range(vertices)
        for target in range(vertices)
        if source != target
    ]


def reachability_code(
    graph: int, vertices: int, edges: list[tuple[int, int]]
) -> tuple[int, ...]:
    outgoing = [[] for _ in range(vertices)]
    for bit, (source, target) in enumerate(edges):
        if graph & (1 << bit):
            outgoing[source].append(target)

    result = []
    for source in range(vertices):
        visited = {source}
        frontier = [source]
        while frontier:
            current = frontier.pop()
            for target in outgoing[current]:
                if target not in visited:
                    visited.add(target)
                    frontier.append(target)
        result.append(sum(1 << target for target in visited))
    return tuple(result)


def verify_graph_toggles(vertices: int, expected_changes: int) -> None:
    edges = directed_edges(vertices)
    codes = [
        reachability_code(graph, vertices, edges)
        for graph in range(1 << len(edges))
    ]

    changes = 0
    absent_edge_changes = 0
    for graph, before in enumerate(codes):
        for index, (source, target) in enumerate(edges):
            mask = 1 << index
            edge_present = bool(graph & mask)
            after = codes[graph ^ mask]
            changed = before != after
            changes += int(changed)
            if not edge_present:
                absent_edge_changes += int(changed)
                reachable_before = bool(before[source] & (1 << target))
                assert changed == (not reachable_before), (
                    vertices, graph, source, target
                )
            assert changed == (after != codes[(graph ^ mask) ^ mask])

    assert changes == 2 * absent_edge_changes
    assert changes == expected_changes, (vertices, changes, expected_changes)
    print(f"Graph toggle oracle PASS: n={vertices}; changed={changes}")


def verify_negative_controls() -> None:
    edges = directed_edges(3)
    edge_index = {edge: index for index, edge in enumerate(edges)}
    indirect = (1 << edge_index[(0, 2)]) | (1 << edge_index[(2, 1)])
    direct_edge = 1 << edge_index[(0, 1)]
    assert reachability_code(indirect, 3, edges) == reachability_code(
        indirect | direct_edge, 3, edges
    ), "Adding a redundant edge should not change reachability."
    assert reachability_code(0, 3, edges) != reachability_code(
        direct_edge, 3, edges
    ), "Adding the first edge should change reachability."
    print("Graph toggle oracle PASS: redundant-edge and reachability-change controls")


def main() -> None:
    verify_negative_controls()
    for vertices, expected_changes in ((2, 8), (3, 288), (4, 24576)):
        verify_graph_toggles(vertices, expected_changes)


if __name__ == "__main__":
    main()
