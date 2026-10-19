#!/usr/bin/env python3
"""Independent exact cross-checks for selected finite mathematical claims.

The implementations here do not import historical audit code. Passing these
checks does not certify novelty, unrestricted theorems, or physical relevance.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb


def count_partial_orders(vertex_count: int) -> int:
    """Enumerate antisymmetric relations and retain transitive ones."""
    pairs = list(combinations(range(vertex_count), 2))
    accepted = 0

    for orientations in product((-1, 0, 1), repeat=len(pairs)):
        rows = [1 << vertex for vertex in range(vertex_count)]
        for (source, target), orientation in zip(pairs, orientations):
            if orientation == 1:
                rows[source] |= 1 << target
            elif orientation == -1:
                rows[target] |= 1 << source

        is_transitive = all(
            not rows[source] & (1 << intermediate)
            or rows[intermediate] & ~rows[source] == 0
            for source in range(vertex_count)
            for intermediate in range(vertex_count)
        )
        accepted += is_transitive

    return accepted


def rooted_reachable_counts(maximum_vertices: int) -> list[int]:
    """Partition digraphs by their root's exact reachable vertex set."""
    counts = [0, 1]

    for vertex_count in range(2, maximum_vertices + 1):
        total_graphs = 2 ** (vertex_count * (vertex_count - 1))
        incomplete = sum(
            comb(vertex_count - 1, subset_size - 1)
            * counts[subset_size]
            * 2 ** ((vertex_count - subset_size) * (vertex_count - 1))
            for subset_size in range(1, vertex_count)
        )
        counts.append(total_graphs - incomplete)

    return counts


def nonreach_by_reachable_set(
    vertex_count: int, rooted_counts: list[int]
) -> int:
    """Count graphs whose root does not reach one designated other vertex."""
    return sum(
        comb(vertex_count - 2, subset_size - 1)
        * rooted_counts[subset_size]
        * 2 ** ((vertex_count - subset_size) * (vertex_count - 1))
        for subset_size in range(1, vertex_count)
    )


def nonreach_by_cut_inclusion_exclusion(vertex_count: int) -> int:
    """Compute nonreachability as a union of outgoing-closed cut events."""
    edges = [
        (source, target)
        for source in range(vertex_count)
        for target in range(vertex_count)
        if source != target
    ]
    cut_masks = []

    for selection in range(1 << (vertex_count - 2)):
        subset = {0}
        for offset, vertex in enumerate(range(2, vertex_count)):
            if selection & (1 << offset):
                subset.add(vertex)

        cut_mask = sum(
            1 << index
            for index, (source, target) in enumerate(edges)
            if source in subset and target not in subset
        )
        cut_masks.append(cut_mask)

    nonreachable_graphs = 0
    for selected_cuts in range(1, 1 << len(cut_masks)):
        absent_edges = 0
        for index, cut_mask in enumerate(cut_masks):
            if selected_cuts & (1 << index):
                absent_edges |= cut_mask

        admissible_graphs = 1 << (len(edges) - absent_edges.bit_count())
        sign = 1 if selected_cuts.bit_count() % 2 else -1
        nonreachable_graphs += sign * admissible_graphs

    return nonreachable_graphs


def verify_representative_code_count() -> None:
    poset_counts = [count_partial_orders(size) for size in range(1, 6)]
    expected_counts = [1, 3, 19, 219, 4231]
    assert poset_counts == expected_counts, poset_counts

    code_count = sum(
        comb(4, size - 1) * poset_counts[size - 1]
        for size in range(1, 6)
    )
    assert code_count == 5234, code_count
    print(f"MF-R008 PASS: labeled posets {poset_counts}; five-vertex codes {code_count}")


def verify_edge_toggle_probability() -> None:
    rooted_counts = rooted_reachable_counts(6)
    assert rooted_counts[:6] == [0, 1, 2, 32, 2432, 745472]

    expected_probabilities = {
        2: Fraction(1),
        3: Fraction(3, 4),
        4: Fraction(1, 2),
        5: Fraction(75, 256),
        6: Fraction(313, 2048),
    }
    for vertices, expected in expected_probabilities.items():
        root_count = nonreach_by_reachable_set(vertices, rooted_counts)
        cut_count = nonreach_by_cut_inclusion_exclusion(vertices)
        assert root_count == cut_count, (vertices, root_count, cut_count)

        graph_count = 2 ** (vertices * (vertices - 1))
        probability = Fraction(2 * root_count, graph_count)
        assert probability == expected, (vertices, probability, expected)
        print(f"MF-R011 PASS: n={vertices}; nonreach={cut_count}; P={probability}")


def verify_dynamic_nonclosure_witness() -> None:
    support = range(4)
    plus = (
        Fraction(9, 40), Fraction(7, 20),
        Fraction(1, 8), Fraction(3, 10),
    )
    minus = (
        Fraction(11, 40), Fraction(3, 20),
        Fraction(3, 8), Fraction(1, 5),
    )
    for weights in (plus, minus):
        assert sum(weights) == 1
        assert all(weight > 0 for weight in weights)
        assert sum(x * weight for x, weight in zip(support, weights)) == Fraction(3, 2)
        assert sum(
            weight * Fraction(1, 2**x)
            for x, weight in zip(support, weights)
        ) == Fraction(15, 32)

    # A + B*sqrt(2) is an exact representation of E[2^(-X/2)].
    def half_scale_moment(weights: tuple[Fraction, ...]) -> tuple[Fraction, Fraction]:
        return (weights[0] + weights[2] / 2, weights[1] / 2 + weights[3] / 4)

    assert half_scale_moment(plus) == (Fraction(23, 80), Fraction(1, 4))
    assert half_scale_moment(minus) == (Fraction(37, 80), Fraction(1, 8))
    # Their difference is (5*sqrt(2) - 7)/40 > 0.
    # Both sides are positive, so squaring gives the exact sign check.
    assert 5**2 * 2 > 7**2
    print("MF-R049 PASS: exact four-point dynamic nonclosure witness")


def main() -> None:
    verify_representative_code_count()
    verify_edge_toggle_probability()
    verify_dynamic_nonclosure_witness()


if __name__ == "__main__":
    main()
