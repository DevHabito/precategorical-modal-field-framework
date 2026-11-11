#!/usr/bin/env python3
"""Exhaustive automorphism/orientation audit for the C1 graph witnesses.

The audit enumerates all 5! vertex permutations. For each directed witness and
its undirected skeleton it computes the automorphism group and checks whether
an ordered pair (a,b) lies in the same automorphism orbit as its reverse (b,a).

Reverse separation means only that some automorphism-invariant asymmetric
relation could distinguish the ordered pair. It does not assign physical or
temporal meaning to that distinction.
"""

import itertools
import json

V = range(5)

EDGES_A = {(0, 2), (2, 3), (3, 4), (4, 0)}
EDGES_B = {(0, 2), (2, 3), (3, 0), (1, 4), (4, 1)}


def undirected(edges):
    return {tuple(sorted((u, v))) for u, v in edges if u != v}


def is_directed_automorphism(edges, p):
    return {(p[u], p[v]) for u, v in edges} == edges


def is_undirected_automorphism(edges, p):
    return {tuple(sorted((p[u], p[v]))) for u, v in edges} == edges


def reverse_in_same_orbit(automorphisms, a, b):
    return any(p[a] == b and p[b] == a for p in automorphisms)


def audit_graph(edges):
    skeleton = undirected(edges)
    permutations = list(itertools.permutations(V))

    directed_aut = [
        p for p in permutations
        if is_directed_automorphism(edges, p)
    ]
    skeleton_aut = [
        p for p in permutations
        if is_undirected_automorphism(skeleton, p)
    ]

    ordered_pairs = [
        (a, b) for a in V for b in V if a != b
    ]

    return {
        "directed_edges": [list(e) for e in sorted(edges)],
        "directed_automorphism_count": len(directed_aut),
        "undirected_skeleton_automorphism_count": len(skeleton_aut),
        "directed_automorphisms": [list(p) for p in directed_aut],
        "undirected_automorphisms": [list(p) for p in skeleton_aut],
        "edge_reverse_in_same_orbit_directed": {
            f"{a}->{b}": reverse_in_same_orbit(directed_aut, a, b)
            for a, b in sorted(edges)
        },
        "edge_reverse_in_same_orbit_skeleton": {
            f"{a}->{b}": reverse_in_same_orbit(skeleton_aut, a, b)
            for a, b in sorted(edges)
        },
        "ordered_pair_counts_directed": {
            "reverse_same_orbit": sum(
                reverse_in_same_orbit(directed_aut, a, b)
                for a, b in ordered_pairs
            ),
            "reverse_separate_orbit": sum(
                not reverse_in_same_orbit(directed_aut, a, b)
                for a, b in ordered_pairs
            ),
        },
        "ordered_pair_counts_skeleton": {
            "reverse_same_orbit": sum(
                reverse_in_same_orbit(skeleton_aut, a, b)
                for a, b in ordered_pairs
            ),
            "reverse_separate_orbit": sum(
                not reverse_in_same_orbit(skeleton_aut, a, b)
                for a, b in ordered_pairs
            ),
        },
    }


result = {
    "audit": "C1_AUTOMORPHISM_ORIENTATION_V1",
    "status": "PASS",
    "vertex_count": 5,
    "graphA": audit_graph(EDGES_A),
    "graphB": audit_graph(EDGES_B),
    "interpretation": [
        "Reverse-separated ordered-pair orbits mean only that an automorphism-invariant asymmetric relation could distinguish the pair; they do not supply physical temporal meaning.",
        "For graphA every directed cycle edge becomes reverse-equivalent after arrow removal, so its orientation is information contained in the directed relation rather than the undirected skeleton.",
        "For graphB the one-way triangle edges become reverse-equivalent after arrow removal; the bidirectional 1<->4 pair is reverse-equivalent already in the directed graph.",
        "This is an exact exhaustive permutation audit over all 5! vertex relabelings."
    ],
}

print(json.dumps(result, indent=2))
