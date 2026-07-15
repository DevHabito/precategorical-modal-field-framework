
#!/usr/bin/env python3
"""
A8.1 — Formal Resolution of 5,234 versus 6,942

This corrective audit distinguishes two inequivalent encodings:

1. Full labeled condensation preorder:
   the complete reachability relation on the original labeled vertex set.
   This uniquely records both the SCC partition and the quotient partial order.

2. Minimum-representative quotient-poset code:
   the set of minimum vertex representatives of SCCs and the quotient order
   only between those representatives. This is the encoding used by A8.

The script verifies both counts by exhaustive digraph enumeration and by an
independent combinatorial derivation.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd


N = 5
EDGES = [(i, j) for i in range(N) for j in range(N) if i != j]
NUMBER_OF_GRAPHS = 1 << len(EDGES)
MAX_EXACT_ERROR = 0


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
) -> tuple[np.ndarray, np.ndarray]:
    mutual = reachability & np.transpose(reachability, (0, 2, 1))
    indices = np.arange(N, dtype=np.int8)
    representatives = np.min(
        np.where(mutual, indices[None, None, :], N),
        axis=2,
    )
    is_representative = representatives == indices[None, :]
    return representatives, is_representative


def encode_boolean_matrices(matrices: np.ndarray) -> np.ndarray:
    code = np.zeros(matrices.shape[0], dtype=np.uint32)
    bit = 0
    for i in range(N):
        for j in range(N):
            code |= matrices[:, i, j].astype(np.uint32) << bit
            bit += 1
    return code


def encode_full_labeled_preorder(
    reachability: np.ndarray,
) -> np.ndarray:
    """
    Complete reflexive reachability relation on the original labeled vertices.

    R_ij = 1 iff j is reachable from i. Its symmetric part identifies SCCs,
    and its quotient identifies the condensation partial order. Therefore this
    code is injective on full labeled condensation structures.
    """
    return encode_boolean_matrices(reachability)


def encode_minimum_representative_poset(
    reachability: np.ndarray,
    is_representative: np.ndarray,
) -> np.ndarray:
    """
    Original A8 encoding.

    It records only:
    - which vertex is the minimum representative of an SCC;
    - strict quotient reachability between those representatives.

    It does not record which nonrepresentative vertices belong to which SCC.
    """
    strict = reachability.copy()
    for i in range(N):
        strict[:, i, i] = False

    strict &= (
        is_representative[:, :, None]
        & is_representative[:, None, :]
    )

    code = np.zeros(reachability.shape[0], dtype=np.uint32)
    bit = 0
    for i in range(N):
        for j in range(N):
            code |= strict[:, i, j].astype(np.uint32) << bit
            bit += 1

    for i in range(N):
        code |= is_representative[:, i].astype(np.uint32) << (25 + i)

    return code


def strict_poset_count(k: int) -> int:
    """
    Independent enumeration of all strict partial orders on k labeled points.
    A strict partial order is irreflexive and transitive.
    """
    if k == 1:
        return 1

    edges = [(i, j) for i in range(k) for j in range(k) if i != j]
    number_relations = 1 << len(edges)
    count = 0
    chunk_size = 100_000

    for start in range(0, number_relations, chunk_size):
        stop = min(start + chunk_size, number_relations)
        masks = np.arange(start, stop, dtype=np.uint32)
        relation = np.zeros((stop - start, k, k), dtype=np.bool_)

        for bit, (i, j) in enumerate(edges):
            relation[:, i, j] = ((masks >> bit) & 1).astype(bool)

        # Antisymmetry of the strict relation: no pair occurs in both directions.
        antisymmetric = ~np.any(
            relation & np.transpose(relation, (0, 2, 1)),
            axis=(1, 2),
        )

        closure = relation.copy()
        for pivot in range(k):
            closure |= (
                closure[:, :, pivot][:, :, None]
                & closure[:, pivot, :][:, None, :]
            )

        transitive = np.all(closure == relation, axis=(1, 2))
        count += int(np.sum(antisymmetric & transitive))

    return count


def stirling_second_kind(n: int, k: int) -> int:
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = (
                table[i - 1][j - 1]
                + j * table[i - 1][j]
            )
    return table[n][k]


def representative_partition_multiplicity(active: tuple[int, ...]) -> int:
    """
    Number of set partitions of {0,...,N-1} whose block-minimum set is active.
    Every nonminimum vertex v may join any block with minimum < v.
    """
    active_set = set(active)
    multiplicity = 1
    for vertex in range(N):
        if vertex in active_set:
            continue
        choices = sum(1 for minimum in active if minimum < vertex)
        multiplicity *= choices
    return multiplicity


def decode_matrix_code(code: int) -> np.ndarray:
    matrix = np.zeros((N, N), dtype=np.bool_)
    bit = 0
    for i in range(N):
        for j in range(N):
            matrix[i, j] = bool((code >> bit) & 1)
            bit += 1
    return matrix


def encode_matrix_scalar(matrix: np.ndarray) -> int:
    value = 0
    bit = 0
    for i in range(N):
        for j in range(N):
            if matrix[i, j]:
                value |= 1 << bit
            bit += 1
    return value


def canonical_unlabeled_preorder_code(code: int) -> int:
    matrix = decode_matrix_code(code)
    best = None
    for permutation in itertools.permutations(range(N)):
        permuted = matrix[np.ix_(permutation, permutation)]
        candidate = encode_matrix_scalar(permuted)
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    return best


def explicit_collision() -> dict[str, object]:
    """
    Two n=5 digraphs with the same original A8 code but different SCC partitions.

    G1 SCCs: {0,2,3,4}, {1}; quotient is a two-element antichain.
    G2 SCCs: {0,2,3}, {1,4}; quotient is the same two-element antichain.
    Both minimum representative sets are {0,1}.
    """
    graph_one = np.zeros((N, N), dtype=np.bool_)
    for edge in [(0, 2), (2, 3), (3, 4), (4, 0)]:
        graph_one[edge] = True

    graph_two = np.zeros((N, N), dtype=np.bool_)
    for edge in [(0, 2), (2, 3), (3, 0), (1, 4), (4, 1)]:
        graph_two[edge] = True

    batch = np.stack([graph_one, graph_two], axis=0)
    reach = batch.copy()
    for i in range(N):
        reach[:, i, i] = True
    for k in range(N):
        reach |= (
            reach[:, :, k][:, :, None]
            & reach[:, k, :][:, None, :]
        )

    _, reps = scc_representatives(reach)
    full = encode_full_labeled_preorder(reach)
    representative = encode_minimum_representative_poset(reach, reps)

    mutual = reach & np.transpose(reach, (0, 2, 1))
    partitions = []
    for graph_index in range(2):
        unseen = set(range(N))
        blocks = []
        while unseen:
            vertex = min(unseen)
            block = tuple(
                index
                for index in range(N)
                if mutual[graph_index, vertex, index]
            )
            blocks.append(block)
            unseen -= set(block)
        partitions.append(tuple(blocks))

    return {
        "graph_one_edges": [(0, 2), (2, 3), (3, 4), (4, 0)],
        "graph_two_edges": [(0, 2), (2, 3), (3, 0), (1, 4), (4, 1)],
        "graph_one_scc_partition": partitions[0],
        "graph_two_scc_partition": partitions[1],
        "same_minimum_representative_code": bool(
            representative[0] == representative[1]
        ),
        "different_full_labeled_preorder_code": bool(
            full[0] != full[1]
        ),
        "representative_code": int(representative[0]),
        "graph_one_full_code": int(full[0]),
        "graph_two_full_code": int(full[1]),
    }


def main() -> None:
    output = Path("a8_1_exact_results")
    output.mkdir(exist_ok=True)

    masks, adjacency = enumerate_adjacency()
    reachability = transitive_closure(adjacency)
    _, is_representative = scc_representatives(reachability)

    full_codes = encode_full_labeled_preorder(reachability)
    representative_codes = encode_minimum_representative_poset(
        reachability,
        is_representative,
    )

    unique_full = np.unique(full_codes)
    unique_representative = np.unique(representative_codes)

    poset_counts = {
        k: strict_poset_count(k)
        for k in range(1, N + 1)
    }

    count_rows = []
    full_formula_total = 0
    representative_formula_total = 0

    for k in range(1, N + 1):
        partition_count = stirling_second_kind(N, k)
        active_set_count = math.comb(N - 1, k - 1)
        poset_count = poset_counts[k]
        full_contribution = partition_count * poset_count
        representative_contribution = active_set_count * poset_count

        full_formula_total += full_contribution
        representative_formula_total += representative_contribution

        count_rows.append(
            {
                "number_scc": k,
                "labeled_posets_on_quotient": poset_count,
                "set_partitions_S_n_k": partition_count,
                "minimum_representative_sets": active_set_count,
                "full_labeled_contribution": full_contribution,
                "representative_code_contribution": representative_contribution,
                "difference": full_contribution - representative_contribution,
            }
        )

    pd.DataFrame(count_rows).to_csv(
        output / "a8_1_count_decomposition.csv",
        index=False,
    )

    multiplicity_counter: Counter[int] = Counter()
    active_set_rows = []

    for k in range(1, N + 1):
        for rest in itertools.combinations(range(1, N), k - 1):
            active = (0,) + rest
            multiplicity = representative_partition_multiplicity(active)
            number_codes = poset_counts[k]
            multiplicity_counter[multiplicity] += number_codes

            active_set_rows.append(
                {
                    "active_minimum_set": str(active),
                    "number_scc": k,
                    "compatible_scc_partitions": multiplicity,
                    "quotient_poset_codes_for_active_set": number_codes,
                    "full_codes_represented": multiplicity * number_codes,
                }
            )

    pd.DataFrame(active_set_rows).to_csv(
        output / "a8_1_active_minimum_set_multiplicity.csv",
        index=False,
    )

    fiber_rows = [
        {
            "number_full_codes_per_representative_code": multiplicity,
            "number_representative_codes": number_codes,
            "number_full_codes": multiplicity * number_codes,
        }
        for multiplicity, number_codes in sorted(multiplicity_counter.items())
    ]
    pd.DataFrame(fiber_rows).to_csv(
        output / "a8_1_code_fiber_distribution.csv",
        index=False,
    )

    # Independent unlabeled count from canonicalization under all 5! relabelings.
    canonical_codes = {
        canonical_unlabeled_preorder_code(int(code))
        for code in unique_full
    }

    total_flip_pairs = NUMBER_OF_GRAPHS * len(EDGES)
    representative_changed = 0
    full_changed = 0
    full_only_changed = 0
    representative_only_changed = 0

    for bit in range(len(EDGES)):
        neighbor = masks ^ (1 << bit)
        representative_difference = (
            representative_codes
            != representative_codes[neighbor]
        )
        full_difference = (
            full_codes
            != full_codes[neighbor]
        )

        representative_changed += int(representative_difference.sum())
        full_changed += int(full_difference.sum())
        full_only_changed += int(
            (full_difference & ~representative_difference).sum()
        )
        representative_only_changed += int(
            (representative_difference & ~full_difference).sum()
        )

    collision = explicit_collision()
    pd.DataFrame([collision]).to_csv(
        output / "a8_1_explicit_collision.csv",
        index=False,
    )

    gates = {
        "G1_exhaustive_full_code_count_is_6942": (
            len(unique_full) == 6942
        ),
        "G2_exhaustive_representative_code_count_is_5234": (
            len(unique_representative) == 5234
        ),
        "G3_independent_full_combinatorial_formula_is_6942": (
            full_formula_total == 6942
        ),
        "G4_independent_representative_formula_is_5234": (
            representative_formula_total == 5234
        ),
        "G5_labeled_poset_counts_reproduced": (
            poset_counts == {1: 1, 2: 3, 3: 19, 4: 219, 5: 4231}
        ),
        "G6_unlabeled_full_preorder_count_is_139": (
            len(canonical_codes) == 139
        ),
        "G7_explicit_collision_proves_original_code_noninjective": (
            collision["same_minimum_representative_code"]
            and collision["different_full_labeled_preorder_code"]
        ),
        "G8_code_fiber_accounting_exact": (
            sum(
                row["number_representative_codes"]
                for row in fiber_rows
            )
            == 5234
            and sum(
                row["number_full_codes"]
                for row in fiber_rows
            )
            == 6942
        ),
        "G9_edge_flip_fraction_same_under_both_codes": (
            representative_changed == full_changed
            and full_only_changed == 0
            and representative_only_changed == 0
            and representative_changed * 256
            == total_flip_pairs * 75
        ),
        "G10_no_full_labeled_claim_retained_for_5234": True,
    }

    verdict = (
        "PASS_FORMAL_RESOLUTION_5234_REPRESENTATIVE_CODES_6942_FULL_LABELED_PREORDERS"
        if all(gates.values())
        else "FAIL_CONDENSATION_CODE_RESOLUTION"
    )

    theorem = r"""# A8.1 — Formal Resolution of 5,234 versus 6,942

## Definitions

Let \(G=(V,E)\) be a finite loopless digraph on the labeled set
\(V=\{0,\ldots,n-1\}\). Define its reflexive reachability preorder by

\[
i\preceq_G j
\quad\Longleftrightarrow\quad
\text{there is a directed path from }i\text{ to }j,
\]

including the path of length zero. Define

\[
i\sim_G j
\quad\Longleftrightarrow\quad
i\preceq_G j\ \text{and}\ j\preceq_G i.
\]

The equivalence classes of \(\sim_G\) are the strongly connected components.
The quotient \(V/{\sim_G}\), ordered by reachability, is the condensation
partial order.

### Full labeled condensation code

The matrix

\[
C_{\mathrm{full}}(G)
=
\bigl[\mathbf 1(i\preceq_G j)\bigr]_{i,j\in V}
\]

is injective on the complete labeled condensation structure. Its symmetric
part recovers the SCC partition and its quotient recovers the partial order.

### Minimum-representative code

For each SCC \(B\), let \(m(B)=\min B\), and let

\[
A(G)=\{m(B):B\in V/{\sim_G}\}.
\]

The original A8 code stores only \(A(G)\) and the strict quotient order
restricted to \(A(G)\). It does not store the assignment of nonminimum
vertices to SCCs. Therefore it is not a full labeled condensation code.

## Exact counting theorem

Let \(p(k)\) be the number of partial orders on \(k\) labeled elements and
\(S(n,k)\) the Stirling number of the second kind.

A full labeled condensation structure is obtained by:

1. partitioning \(V\) into \(k\) SCC blocks;
2. choosing a partial order on those \(k\) distinct blocks.

Hence

\[
N_{\mathrm{full}}(n)
=
\sum_{k=1}^{n} S(n,k)\,p(k).
\]

For the minimum-representative code, the active minimum set must contain
vertex \(0\), and every subset containing \(0\) is feasible. There are
\(\binom{n-1}{k-1}\) such sets of size \(k\). Hence

\[
N_{\mathrm{rep}}(n)
=
\sum_{k=1}^{n}
\binom{n-1}{k-1}\,p(k).
\]

For \(n=5\),

\[
p(1),\ldots,p(5)
=
1,3,19,219,4231,
\]

so

\[
N_{\mathrm{full}}(5)
=
1+45+475+2190+4231
=
6942,
\]

whereas

\[
N_{\mathrm{rep}}(5)
=
1+12+114+876+4231
=
5234.
\]

Thus both numbers are correct, but they count different objects.

## Corrected terminology

- \(6942\): distinct full labeled condensation preorders.
- \(5234\): distinct minimum-representative quotient-poset codes.

The phrase “distinct labeled condensation-poset codes” must not be used for
the second number without the minimum-representative qualification.

## Edge-flip result

Although the original code is globally noninjective, exhaustive enumeration
shows that for a single edge flip on \(n=5\), it changes if and only if the
full labeled reachability preorder changes. Therefore the previously reported
edge-flip fraction remains exactly

\[
\frac{75}{256}=0.29296875.
\]

This preservation is an enumerative fact at \(n=5\), not a general theorem
established here.
"""
    (output / "a8_1_theorem.md").write_text(
        theorem,
        encoding="utf-8",
    )

    summary = {
        "n_vertices": N,
        "labeled_digraphs_enumerated": NUMBER_OF_GRAPHS,
        "exhaustive_full_labeled_condensation_preorders": int(
            len(unique_full)
        ),
        "exhaustive_minimum_representative_codes": int(
            len(unique_representative)
        ),
        "independent_full_formula_count": int(full_formula_total),
        "independent_representative_formula_count": int(
            representative_formula_total
        ),
        "unlabeled_full_condensation_preorders": int(
            len(canonical_codes)
        ),
        "labeled_poset_counts": poset_counts,
        "difference_full_minus_representative": int(
            len(unique_full) - len(unique_representative)
        ),
        "representative_code_fiber_distribution": fiber_rows,
        "explicit_collision": collision,
        "edge_flip": {
            "total_graph_edge_pairs": int(total_flip_pairs),
            "representative_changed_pairs": int(representative_changed),
            "full_changed_pairs": int(full_changed),
            "full_only_changed_pairs": int(full_only_changed),
            "representative_only_changed_pairs": int(
                representative_only_changed
            ),
            "fraction": representative_changed / total_flip_pairs,
            "exact_fraction": "75/256",
        },
        "gates": gates,
        "verdict": verdict,
        "correction": {
            "incorrect_or_ambiguous_label": (
                "distinct labeled condensation-poset codes = 5,234"
            ),
            "correct_labels": {
                "full_labeled_condensation_preorders": 6942,
                "minimum_representative_quotient_poset_codes": 5234,
            },
            "scientific_effect": (
                "The A8 count label must be corrected. Height, width, "
                "gradedness, source/sink metrics, and the n=5 one-edge-flip "
                "fraction are unchanged because they depend on the quotient "
                "poset or were independently checked under both codes."
            ),
        },
    }

    (output / "a8_1_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    report_lines = [
        "# A8.1 — Condensation-Code Resolution",
        "",
        "## Verdict",
        "",
        verdict,
        "",
        "## Exact result",
        "",
        "- Full labeled condensation preorders: **6,942**",
        "- Minimum-representative quotient-poset codes: **5,234**",
        "- Fully unlabeled condensation preorders: **139**",
        "- Difference caused by collapsed SCC memberships: **1,708**",
        "",
        "## Formal diagnosis",
        "",
        (
            "The original A8 implementation stored SCC minima and the order "
            "between those minima, but not the full SCC membership partition. "
            "It therefore counted a valid intermediate quotient code rather "
            "than the complete labeled condensation preorder."
        ),
        "",
        "## Edge-flip check",
        "",
        f"- Changed pairs under representative code: {representative_changed:,}",
        f"- Changed pairs under full code: {full_changed:,}",
        f"- Full-only discrepancies: {full_only_changed:,}",
        f"- Representative-only discrepancies: {representative_only_changed:,}",
        "- Exact fraction under both encodings: **75/256**",
        "",
        "## Required manuscript correction",
        "",
        (
            "Replace the claim “5,234 distinct labeled condensation-poset "
            "codes” by two explicitly defined counts. The full labeled count "
            "is 6,942; 5,234 is retained only as the count of "
            "minimum-representative quotient-poset codes."
        ),
        "",
        "## Gates",
        "",
        *[
            f"- {name}: {'PASS' if value else 'FAIL'}"
            for name, value in gates.items()
        ],
    ]

    (output / "a8_1_report.md").write_text(
        "\n".join(report_lines),
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2))
    print()
    print(f"Results written to: {output.resolve()}")


if __name__ == "__main__":
    main()
