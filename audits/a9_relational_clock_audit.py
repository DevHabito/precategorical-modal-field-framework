#!/usr/bin/env python3
"""
A9 — Relational Clock Audit

Exact audit over all loopless labeled digraphs on five vertices.

Starting from the SCC condensation poset, this program computes three
isomorphism-invariant ordinal clock candidates:

1. depth clock: longest chain ending at each SCC;
2. balance clock: |down-set| - |up-set|;
3. mean-extension clock: expected position under the uniform distribution
   over all linear extensions of the finite poset.

The program tests:
- strict monotonicity on comparable SCCs;
- uniqueness/injectivity of clock levels;
- disagreement between canonical candidates on incomparable SCCs;
- covariance under order reversal;
- sensitivity to a single edge flip in the underlying digraph.

These clocks are mathematical descriptors only. The script does not infer
physical duration, rate, causality, or a preferred arrow of time.
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
TOLERANCE = 1e-12


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


def normalize_clock(values: np.ndarray, active: list[int]) -> np.ndarray:
    result = np.full(N, np.nan, dtype=float)
    active_values = values[active].astype(float)

    if len(active) == 1:
        result[active[0]] = 0.5
        return result

    low = float(active_values.min())
    high = float(active_values.max())

    if abs(high - low) <= TOLERANCE:
        result[active] = 0.5
    else:
        result[active] = (active_values - low) / (high - low)

    return result


def topological_order(active: list[int], strict: np.ndarray) -> list[int]:
    indegree = {
        vertex: int(sum(strict[parent, vertex] for parent in active))
        for vertex in active
    }
    available = sorted(
        vertex for vertex in active if indegree[vertex] == 0
    )
    order: list[int] = []

    while available:
        vertex = available.pop(0)
        order.append(vertex)
        for child in active:
            if strict[vertex, child]:
                # Only cover status is not needed: decrement for every strict
                # predecessor would over-count. Recompute availability safely.
                pass

        remaining = [x for x in active if x not in order]
        for candidate in remaining:
            if (
                candidate not in available
                and all(
                    not strict[parent, candidate]
                    or parent in order
                    for parent in active
                )
            ):
                available.append(candidate)
        available.sort()

    if len(order) != len(active):
        raise RuntimeError("Condensation relation is not acyclic.")

    return order


def linear_extensions(
    active: list[int],
    strict: np.ndarray,
) -> list[tuple[int, ...]]:
    result: list[tuple[int, ...]] = []
    for permutation in itertools.permutations(active):
        position = {vertex: index for index, vertex in enumerate(permutation)}
        valid = True
        for i in active:
            for j in active:
                if strict[i, j] and position[i] >= position[j]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            result.append(permutation)
    return result


def poset_clocks(
    active: list[int],
    strict: np.ndarray,
) -> dict[str, np.ndarray | int | float | bool]:
    reflexive = strict.copy()
    for vertex in active:
        reflexive[vertex, vertex] = True

    down_count = np.zeros(N, dtype=float)
    up_count = np.zeros(N, dtype=float)
    for vertex in active:
        down_count[vertex] = sum(
            reflexive[other, vertex] for other in active
        )
        up_count[vertex] = sum(
            reflexive[vertex, other] for other in active
        )

    balance_raw = down_count - up_count

    order = topological_order(active, strict)
    depth_raw = np.zeros(N, dtype=float)
    for vertex in order:
        predecessors = [
            parent for parent in active if strict[parent, vertex]
        ]
        if predecessors:
            depth_raw[vertex] = 1.0 + max(
                depth_raw[parent] for parent in predecessors
            )

    extensions = linear_extensions(active, strict)
    expected_raw = np.zeros(N, dtype=float)
    for extension in extensions:
        for position, vertex in enumerate(extension):
            expected_raw[vertex] += position
    expected_raw /= len(extensions)

    clocks = {
        "depth": normalize_clock(depth_raw, active),
        "balance": normalize_clock(balance_raw, active),
        "mean_extension": normalize_clock(expected_raw, active),
    }

    strict_monotone = {}
    injective = {}
    level_count = {}

    for name, clock in clocks.items():
        strict_monotone[name] = all(
            not strict[i, j] or clock[i] < clock[j] - TOLERANCE
            for i in active
            for j in active
        )
        rounded = np.round(clock[active], 12)
        level_count[name] = int(len(np.unique(rounded)))
        injective[name] = level_count[name] == len(active)

    incomparable_pairs = []
    pair_disagreements = {
        ("depth", "balance"): 0,
        ("depth", "mean_extension"): 0,
        ("balance", "mean_extension"): 0,
    }
    pair_comparisons = 0

    for i, j in itertools.combinations(active, 2):
        if strict[i, j] or strict[j, i]:
            continue
        incomparable_pairs.append((i, j))
        pair_comparisons += 1

        for first, second in pair_disagreements:
            first_sign = np.sign(clocks[first][i] - clocks[first][j])
            second_sign = np.sign(clocks[second][i] - clocks[second][j])
            if first_sign != second_sign:
                pair_disagreements[(first, second)] += 1

    all_equal = all(
        np.allclose(
            clocks["depth"][active],
            clocks[name][active],
            atol=TOLERANCE,
            rtol=0,
        )
        for name in ("balance", "mean_extension")
    )

    return {
        **clocks,
        "number_extensions": len(extensions),
        "strict_depth": strict_monotone["depth"],
        "strict_balance": strict_monotone["balance"],
        "strict_mean_extension": strict_monotone["mean_extension"],
        "injective_depth": injective["depth"],
        "injective_balance": injective["balance"],
        "injective_mean_extension": injective["mean_extension"],
        "levels_depth": level_count["depth"],
        "levels_balance": level_count["balance"],
        "levels_mean_extension": level_count["mean_extension"],
        "incomparable_pairs": len(incomparable_pairs),
        "disagreement_depth_balance": pair_disagreements[
            ("depth", "balance")
        ],
        "disagreement_depth_mean_extension": pair_disagreements[
            ("depth", "mean_extension")
        ],
        "disagreement_balance_mean_extension": pair_disagreements[
            ("balance", "mean_extension")
        ],
        "pair_comparisons": pair_comparisons,
        "all_clocks_equal": all_equal,
    }


def transpose_masks(masks: np.ndarray) -> np.ndarray:
    result = np.zeros_like(masks)
    bit_lookup = {edge: bit for bit, edge in enumerate(EDGES)}

    for bit, (i, j) in enumerate(EDGES):
        target_bit = bit_lookup[(j, i)]
        result |= ((masks >> bit) & 1) << target_bit

    return result


def graph_clock_values(
    unique_clock: np.ndarray,
    inverse: np.ndarray,
    representatives: np.ndarray,
) -> np.ndarray:
    graph_clock_on_representatives = unique_clock[inverse]
    rows = np.arange(NUMBER_OF_GRAPHS)[:, None]
    return graph_clock_on_representatives[rows, representatives]


def main() -> None:
    output_directory = Path("a9_exact_results")
    output_directory.mkdir(exist_ok=True)

    masks, adjacency = enumerate_adjacency()
    reachability = transitive_closure(adjacency)
    representatives, is_representative, number_scc = scc_data(reachability)
    codes = encode_condensation_posets(reachability, is_representative)
    unique_codes, inverse = np.unique(codes, return_inverse=True)

    clock_names = ["depth", "balance", "mean_extension"]
    unique_clocks = {
        name: np.full((len(unique_codes), N), np.nan, dtype=float)
        for name in clock_names
    }

    rows = []
    first_disagreement_example = None

    for index, raw_code in enumerate(unique_codes):
        active, strict = decode_poset(int(raw_code))
        result = poset_clocks(active, strict)

        for name in clock_names:
            unique_clocks[name][index] = result[name]

        row = {
            "code": int(raw_code),
            "number_scc": len(active),
            "number_linear_extensions": result["number_extensions"],
            "strict_depth": result["strict_depth"],
            "strict_balance": result["strict_balance"],
            "strict_mean_extension": result["strict_mean_extension"],
            "injective_depth": result["injective_depth"],
            "injective_balance": result["injective_balance"],
            "injective_mean_extension": result[
                "injective_mean_extension"
            ],
            "levels_depth": result["levels_depth"],
            "levels_balance": result["levels_balance"],
            "levels_mean_extension": result[
                "levels_mean_extension"
            ],
            "incomparable_pairs": result["incomparable_pairs"],
            "disagreement_depth_balance": result[
                "disagreement_depth_balance"
            ],
            "disagreement_depth_mean_extension": result[
                "disagreement_depth_mean_extension"
            ],
            "disagreement_balance_mean_extension": result[
                "disagreement_balance_mean_extension"
            ],
            "all_clocks_equal": result["all_clocks_equal"],
        }
        rows.append(row)

        if (
            first_disagreement_example is None
            and not result["all_clocks_equal"]
            and len(active) >= 3
        ):
            first_disagreement_example = {
                "code": int(raw_code),
                "active_vertices": active,
                "strict_relation_matrix": strict.astype(int).tolist(),
                "depth_clock": result["depth"].tolist(),
                "balance_clock": result["balance"].tolist(),
                "mean_extension_clock": result[
                    "mean_extension"
                ].tolist(),
                "number_linear_extensions": result[
                    "number_extensions"
                ],
            }

    poset_frame = pd.DataFrame(rows)
    poset_frame.to_csv(
        output_directory / "a9_poset_clock_profiles.csv",
        index=False,
    )

    graph_clocks = {
        name: graph_clock_values(
            unique_clocks[name],
            inverse,
            representatives,
        )
        for name in clock_names
    }

    transposed = transpose_masks(masks)
    reversal_rows = []

    for name in clock_names:
        original = graph_clocks[name]
        reversed_clock = original[transposed]

        nontrivial = number_scc > 1
        reflected_error = np.max(
            np.abs(
                reversed_clock[nontrivial]
                - (1.0 - original[nontrivial])
            ),
            axis=1,
        )

        reversal_rows.append(
            {
                "clock": name,
                "fraction_exactly_reflected": float(
                    (reflected_error <= TOLERANCE).mean()
                ),
                "mean_max_reflection_error": float(
                    reflected_error.mean()
                ),
                "maximum_reflection_error": float(
                    reflected_error.max()
                ),
            }
        )

    pd.DataFrame(reversal_rows).to_csv(
        output_directory / "a9_reversal_audit.csv",
        index=False,
    )

    total_pairs = NUMBER_OF_GRAPHS * len(EDGES)
    perturbation_rows = []

    for name in clock_names:
        clock = graph_clocks[name]
        changed_graph_edge_pairs = 0
        total_absolute_change = 0.0
        total_max_change = 0.0

        for bit in range(len(EDGES)):
            neighbor = masks ^ (1 << bit)
            difference = np.abs(clock - clock[neighbor])
            maximum = difference.max(axis=1)

            changed_graph_edge_pairs += int(
                (maximum > TOLERANCE).sum()
            )
            total_absolute_change += float(difference.mean(axis=1).sum())
            total_max_change += float(maximum.sum())

        perturbation_rows.append(
            {
                "clock": name,
                "fraction_single_edge_flips_changing_clock": (
                    changed_graph_edge_pairs / total_pairs
                ),
                "mean_vertex_absolute_change": (
                    total_absolute_change / total_pairs
                ),
                "mean_graph_maximum_change": (
                    total_max_change / total_pairs
                ),
            }
        )

    pd.DataFrame(perturbation_rows).to_csv(
        output_directory / "a9_perturbation_audit.csv",
        index=False,
    )

    nontrivial_rows = poset_frame[poset_frame["number_scc"] > 1]
    incomparable_total = int(
        nontrivial_rows["incomparable_pairs"].sum()
    )

    summary = {
        "n_vertices": N,
        "labeled_digraphs": NUMBER_OF_GRAPHS,
        "unique_labeled_condensation_posets": int(len(unique_codes)),
        "nontrivial_unique_condensation_posets": int(
            (poset_frame["number_scc"] > 1).sum()
        ),
        "all_candidates_strict_on_comparable_pairs": {
            name: bool(
                poset_frame[f"strict_{name}"].all()
            )
            for name in clock_names
        },
        "fraction_nontrivial_posets_clock_injective": {
            name: float(
                nontrivial_rows[f"injective_{name}"].mean()
            )
            for name in clock_names
        },
        "fraction_nontrivial_posets_all_three_clocks_equal": float(
            nontrivial_rows["all_clocks_equal"].mean()
        ),
        "total_incomparable_pairs_across_unique_posets": (
            incomparable_total
        ),
        "fraction_incomparable_pairs_depth_balance_disagree": (
            float(
                nontrivial_rows[
                    "disagreement_depth_balance"
                ].sum()
                / incomparable_total
            )
            if incomparable_total
            else 0.0
        ),
        "fraction_incomparable_pairs_depth_mean_extension_disagree": (
            float(
                nontrivial_rows[
                    "disagreement_depth_mean_extension"
                ].sum()
                / incomparable_total
            )
            if incomparable_total
            else 0.0
        ),
        "fraction_incomparable_pairs_balance_mean_extension_disagree": (
            float(
                nontrivial_rows[
                    "disagreement_balance_mean_extension"
                ].sum()
                / incomparable_total
            )
            if incomparable_total
            else 0.0
        ),
        "reversal_audit": reversal_rows,
        "single_edge_perturbation_audit": perturbation_rows,
        "first_candidate_disagreement_example": (
            first_disagreement_example
        ),
    }

    (output_directory / "a9_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    report = f"""# A9 — Relational Clock Audit

## Exact scope

- Labeled loopless digraphs: {NUMBER_OF_GRAPHS:,}
- Vertices per digraph: {N}
- Distinct labeled SCC-condensation posets: {len(unique_codes):,}
- Nontrivial distinct condensation posets:
  {(poset_frame["number_scc"] > 1).sum():,}

## Clock candidates

1. Depth: longest-chain depth from minimal SCCs.
2. Balance: cardinality of principal down-set minus principal up-set.
3. Mean extension: expected position in the uniform distribution over all
   linear extensions.

All three are strict order-preserving functions on every comparable pair in
the exact enumeration.

## Interpretation limit

For any strictly increasing function f, f∘tau is another valid ordinal clock.
Therefore order alone fixes no duration, interval scale, or rate.

The reverse relation yields the dual poset. Balance and mean-extension clocks
reflect exactly under duality; the depth clock generally does not, because
depth from minima and depth from maxima need not be affinely equivalent.

## Scientific status

The candidates are canonical descriptors of a chosen orientation. They do
not select that orientation, are not unique on incomparable elements, are
not automatically compatible with coarse-graining, and are sensitive to
changes in the underlying relation. They are not physical clocks.
"""

    (output_directory / "a9_report.md").write_text(
        report,
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2))
    print()
    print(f"Results written to: {output_directory.resolve()}")


if __name__ == "__main__":
    main()
