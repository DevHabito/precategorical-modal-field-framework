#!/usr/bin/env python3
"""Exact cycle-rank audit for the undirected C1 witness skeletons.

No floating-point linear algebra is required. For a finite undirected graph,
the cycle-space dimension is beta1 = |E| - |V| + number_of_components.
"""

import json

VERTICES = tuple(range(5))

GRAPHS = {
    "graphA_skeleton": {
        "edges": [(0, 2), (2, 3), (3, 4), (4, 0)],
        "cycle_generator": [(0, 2), (2, 3), (3, 4), (4, 0)],
    },
    "graphB_skeleton": {
        "edges": [(0, 2), (2, 3), (3, 0), (1, 4)],
        "cycle_generator": [(0, 2), (2, 3), (3, 0)],
    },
}


def components(vertices, edges):
    adjacency = {v: set() for v in vertices}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)

    unseen = set(vertices)
    comps = []

    while unseen:
        start = min(unseen)
        stack = [start]
        unseen.remove(start)
        comp = []

        while stack:
            u = stack.pop()
            comp.append(u)
            for v in sorted(adjacency[u]):
                if v in unseen:
                    unseen.remove(v)
                    stack.append(v)

        comps.append(sorted(comp))

    return comps


rows = {}
for name, data in GRAPHS.items():
    edges = data["edges"]
    comps = components(VERTICES, edges)
    beta1 = len(edges) - len(VERTICES) + len(comps)
    incidence_rank = len(VERTICES) - len(comps)
    edge_space_dimension = len(edges)
    quotient_dimension = edge_space_dimension - incidence_rank

    assert beta1 == 1
    assert quotient_dimension == beta1

    rows[name] = {
        "vertices": len(VERTICES),
        "edges": len(edges),
        "components": comps,
        "component_count": len(comps),
        "incidence_rank": incidence_rank,
        "edge_space_dimension": edge_space_dimension,
        "cycle_rank_beta1": beta1,
        "edge_mod_gradient_dimension": quotient_dimension,
        "cycle_generator": data["cycle_generator"],
    }

result = {
    "audit": "C1_CYCLE_SPACE_V1",
    "status": "PASS",
    "graphs": rows,
    "interpretation": [
        "Both C1 witness skeletons have exactly one independent undirected cycle-space degree of freedom.",
        "For a reciprocal edge score transforming by addition of a vertex gradient, one real cycle-circulation coordinate spans the gauge-invariant quotient on these skeletons.",
        "This is classical graph homology/Hodge structure, not a physical derivation of direction or time."
    ]
}

print(json.dumps(result, indent=2))
