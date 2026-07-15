#!/usr/bin/env python3
"""A5 — exact finite projective-family audit for loopless directed graphs.

State space: unlabeled finite directed graphs with no self-loops.
Sampling map: choose an m-subset uniformly and take the induced subgraph.

The script:
1. Enumerates isomorphism classes for n <= N_MAX exactly.
2. Constructs exact rational kernels K_{m<-n}.
3. Verifies composition/projectivity of kernels.
4. Computes rational ranks and affine image dimensions.
5. Reports finite-family polytope dimensions and exact-extensibility facts.

No Monte Carlo sampling or learned model is used.
"""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import sympy as sp

N_MAX = 4
OUT_DIR = Path('/mnt/data/a5_exact_results')
OUT_DIR.mkdir(parents=True, exist_ok=True)


def edge_list(n: int) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(n) if i != j]


def mask_to_adj(mask: int, n: int) -> np.ndarray:
    A = np.zeros((n, n), dtype=np.uint8)
    for bit, (i, j) in enumerate(edge_list(n)):
        A[i, j] = (mask >> bit) & 1
    return A


def adj_to_mask(A: np.ndarray) -> int:
    n = A.shape[0]
    mask = 0
    for bit, (i, j) in enumerate(edge_list(n)):
        if int(A[i, j]):
            mask |= 1 << bit
    return mask


def permuted_mask(mask: int, n: int, perm: Tuple[int, ...]) -> int:
    A = mask_to_adj(mask, n)
    # Relabel old vertex i to new vertex perm[i].
    B = np.zeros_like(A)
    for i in range(n):
        for j in range(n):
            B[perm[i], perm[j]] = A[i, j]
    return adj_to_mask(B)


def canonical_mask(mask: int, n: int) -> int:
    return min(permuted_mask(mask, n, p) for p in itertools.permutations(range(n)))


def enumerate_classes(n: int) -> Tuple[List[int], Dict[int, int], Dict[int, int]]:
    """Return representatives, canonical->index, and orbit multiplicities."""
    total = 1 << (n * (n - 1))
    multiplicity: Dict[int, int] = {}
    for mask in range(total):
        c = canonical_mask(mask, n)
        multiplicity[c] = multiplicity.get(c, 0) + 1
    reps = sorted(multiplicity)
    index = {c: i for i, c in enumerate(reps)}
    return reps, index, multiplicity


def induced_subgraph_mask(A: np.ndarray, subset: Tuple[int, ...]) -> int:
    B = A[np.ix_(subset, subset)]
    return adj_to_mask(B)


def kernel(
    n: int,
    m: int,
    classes: Dict[int, List[int]],
    class_index: Dict[int, Dict[int, int]],
) -> sp.Matrix:
    """Exact K_{m<-n}; rows m-classes, columns n-classes."""
    rows = len(classes[m])
    cols = len(classes[n])
    den = comb(n, m)
    data = [[sp.Rational(0) for _ in range(cols)] for _ in range(rows)]
    subsets = list(itertools.combinations(range(n), m))
    for c, rep in enumerate(classes[n]):
        A = mask_to_adj(rep, n)
        counts = [0] * rows
        for subset in subsets:
            sub = induced_subgraph_mask(A, subset)
            canon = canonical_mask(sub, m)
            counts[class_index[m][canon]] += 1
        for r, count in enumerate(counts):
            data[r][c] = sp.Rational(count, den)
    return sp.Matrix(data)


def adjacency_list(mask: int, n: int) -> List[List[int]]:
    return mask_to_adj(mask, n).astype(int).tolist()


def main() -> None:
    classes: Dict[int, List[int]] = {}
    indexes: Dict[int, Dict[int, int]] = {}
    multiplicities: Dict[int, Dict[int, int]] = {}

    for n in range(1, N_MAX + 1):
        reps, idx, mult = enumerate_classes(n)
        classes[n] = reps
        indexes[n] = idx
        multiplicities[n] = mult

    kernels: Dict[Tuple[int, int], sp.Matrix] = {}
    for n in range(2, N_MAX + 1):
        for m in range(1, n):
            kernels[(m, n)] = kernel(n, m, classes, indexes)

    # Exact composition checks.
    composition_checks = []
    for n in range(3, N_MAX + 1):
        for m in range(2, n):
            for ell in range(1, m):
                lhs = kernels[(ell, m)] * kernels[(m, n)]
                rhs = kernels[(ell, n)]
                composition_checks.append({
                    'ell': ell,
                    'm': m,
                    'n': n,
                    'exact': bool(lhs == rhs),
                })

    kernel_stats = []
    for (m, n), K in sorted(kernels.items()):
        rank = int(K.rank())
        distinct_cols = len({tuple(K[:, j]) for j in range(K.cols)})
        delta_extendible = []
        for r in range(K.rows):
            target = tuple(sp.Integer(1) if i == r else sp.Integer(0) for i in range(K.rows))
            if any(tuple(K[:, j]) == target for j in range(K.cols)):
                delta_extendible.append(r)
        kernel_stats.append({
            'm': m,
            'n': n,
            'rows_u_m': K.rows,
            'cols_u_n': K.cols,
            'rank': rank,
            'affine_image_dimension': rank - 1,
            'distinct_columns': distinct_cols,
            'pure_m_classes_extendible': len(delta_extendible),
            'pure_m_class_indices_extendible': delta_extendible,
        })

        # Save exact matrix as CSV-like rational strings.
        with (OUT_DIR / f'K_{m}_from_{n}.csv').open('w', encoding='utf-8') as f:
            for i in range(K.rows):
                f.write(','.join(str(K[i, j]) for j in range(K.cols)) + '\n')

    # Full projective-family dimension through each top N.
    family_dimensions = []
    for N in range(1, N_MAX + 1):
        uN = len(classes[N])
        # Lower marginals are uniquely determined by p_N, so graph of affine map.
        family_dimensions.append({
            'N': N,
            'u_N': uN,
            'simplex_dimension_top': uN - 1,
            'projective_family_polytope_dimension': uN - 1,
            'number_of_extreme_points': uN,
        })

    # Detailed pure 3-class extendibility to n=4, with representatives.
    K34 = kernels[(3, 4)]
    pure3 = []
    for r, rep3 in enumerate(classes[3]):
        witness_cols = [j for j in range(K34.cols) if tuple(K34[:, j]) == tuple(sp.Integer(1) if i == r else sp.Integer(0) for i in range(K34.rows))]
        pure3.append({
            'class_index': r,
            'representative_mask': rep3,
            'adjacency': adjacency_list(rep3, 3),
            'extendible_to_4_as_delta': bool(witness_cols),
            'number_of_4_class_witnesses': len(witness_cols),
            'first_witness_4_class_index': witness_cols[0] if witness_cols else None,
        })

    theorem_audit = {
        'statement': (
            'For a fixed top size N, the polytope of projective families '
            '(p_1,...,p_N) with induced-subgraph kernels is affinely '
            'isomorphic to the full simplex on unlabeled N-vertex classes.'
        ),
        'reason': (
            'p_N is unconstrained apart from being a probability vector, '
            'and every lower p_m is uniquely K_{m<-N} p_N.'
        ),
        'consequence': (
            'Finite projectivity alone does not select a measure; its '
            'dimension is u_N-1 and its extreme points are deterministic '
            'choices of an N-vertex isomorphism class.'
        ),
    }

    summary = {
        'model': 'loopless directed graphs; uniform induced-subset sampling',
        'N_max': N_MAX,
        'unlabeled_class_counts': {str(n): len(classes[n]) for n in classes},
        'composition_checks': composition_checks,
        'all_composition_checks_pass': all(x['exact'] for x in composition_checks),
        'kernel_stats': kernel_stats,
        'family_dimensions': family_dimensions,
        'theorem_audit': theorem_audit,
        'pure_3_class_extendibility_to_4': pure3,
    }

    (OUT_DIR / 'a5_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')

    # Human-readable report.
    lines = []
    lines.append('# A5 exact projective-family audit')
    lines.append('')
    lines.append('## Isomorphism-class counts')
    for n in range(1, N_MAX + 1):
        lines.append(f'- u_{n} = {len(classes[n])}')
    lines.append('')
    lines.append('## Kernel ranks')
    for s in kernel_stats:
        lines.append(
            f"- K_{{{s['m']}<-{s['n']}}}: shape {s['rows_u_m']}x{s['cols_u_n']}, "
            f"rank {s['rank']}, affine image dimension {s['affine_image_dimension']}, "
            f"distinct columns {s['distinct_columns']}, pure lower classes extendible "
            f"{s['pure_m_classes_extendible']}/{s['rows_u_m']}."
        )
    lines.append('')
    lines.append('## Finite projective-family dimensions')
    for d in family_dimensions:
        lines.append(
            f"- Through N={d['N']}: dimension {d['projective_family_polytope_dimension']} "
            f"with {d['number_of_extreme_points']} extreme points."
        )
    lines.append('')
    lines.append('## Exact verdict')
    lines.append(theorem_audit['consequence'])
    (OUT_DIR / 'a5_report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    print(json.dumps({
        'class_counts': summary['unlabeled_class_counts'],
        'all_composition_checks_pass': summary['all_composition_checks_pass'],
        'kernel_stats': kernel_stats,
        'family_dimensions': family_dimensions,
    }, indent=2))


if __name__ == '__main__':
    main()
