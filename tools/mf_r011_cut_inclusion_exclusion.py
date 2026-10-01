#!/usr/bin/env python3
"""Independent exact MF-R011 fixed-pair non-reachability checker.

This implementation deliberately does not use the rooted-reachable recurrence.
It counts the event s !-> t by inclusion-exclusion over directed cut events:

    A_S = "no directed edge leaves S",

for every S with s in S and t not in S.

All arithmetic is integer arithmetic.
"""

from __future__ import annotations

from fractions import Fraction


def directed_edges(n: int) -> list[tuple[int, int]]:
    return [(u, v) for u in range(n) for v in range(n) if u != v]


def cut_edge_mask(
    n: int,
    subset: frozenset[int],
    edge_index: dict[tuple[int, int], int],
) -> int:
    mask = 0
    for u in subset:
        for v in range(n):
            if v not in subset:
                mask |= 1 << edge_index[(u, v)]
    return mask


def separating_cut_masks(n: int, s: int = 0, t: int = 1) -> list[int]:
    if not (0 <= s < n and 0 <= t < n and s != t):
        raise ValueError("Require distinct s,t in range(n).")

    edges = directed_edges(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    free_vertices = [v for v in range(n) if v not in (s, t)]

    masks: list[int] = []
    for bits in range(1 << len(free_vertices)):
        subset = {s}
        for i, v in enumerate(free_vertices):
            if (bits >> i) & 1:
                subset.add(v)
        masks.append(cut_edge_mask(n, frozenset(subset), edge_index))
    return masks


def fixed_pair_nonreach_count(n: int, s: int = 0, t: int = 1) -> int:
    """Count loopless labeled digraphs with no directed path s -> t.

    Inclusion-exclusion is over all sets S containing s and excluding t.
    Event A_S says every edge from S to V\S is absent.

    For an intersection of cut events, every edge in the union of the
    corresponding directed cuts is forced absent; every other edge is free.
    """
    cuts = separating_cut_masks(n, s, t)
    number_of_edges = n * (n - 1)
    family_count = 1 << len(cuts)

    union_masks = [0] * family_count
    total = 0

    for family in range(1, family_count):
        least_bit = family & -family
        cut_index = least_bit.bit_length() - 1
        previous = family ^ least_bit
        union_masks[family] = union_masks[previous] | cuts[cut_index]

        forced_absent = union_masks[family].bit_count()
        intersection_size = 1 << (number_of_edges - forced_absent)

        if family.bit_count() & 1:
            total += intersection_size
        else:
            total -= intersection_size

    return total


def sensitivity_probability(n: int) -> Fraction:
    nonreach = fixed_pair_nonreach_count(n)
    graph_count = 1 << (n * (n - 1))
    return Fraction(2 * nonreach, graph_count)


def ordered_graph_edge_counts(n: int) -> tuple[int, int]:
    p = sensitivity_probability(n)
    total = n * (n - 1) * (1 << (n * (n - 1)))
    changed = total * p
    if changed.denominator != 1:
        raise ArithmeticError("Sensitive-pair count must be integral.")
    return changed.numerator, total


def main() -> None:
    for n in range(2, 7):
        nonreach = fixed_pair_nonreach_count(n)
        graph_count = 1 << (n * (n - 1))
        nonreach_probability = Fraction(nonreach, graph_count)
        p = sensitivity_probability(n)
        changed, total = ordered_graph_edge_counts(n)
        print(
            f"n={n} "
            f"nonreach={nonreach}/{graph_count}={nonreach_probability} "
            f"P={p} "
            f"sensitive={changed}/{total}"
        )


if __name__ == "__main__":
    main()
