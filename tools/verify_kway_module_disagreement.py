#!/usr/bin/env python3
"""Finite-bit regression for k-way graphon disagreement identities.

For a binary adjacency signature b=(b_1,...,b_k) seen from one outside point,
let m=sum b_i.  The point is a splitter iff 0<m<k.

The exact pointwise identity is
    sum_{i<j} 1[b_i != b_j] = m(k-m).

Therefore, after integrating over the graphon domain,
    (k-1) Delta_k <= sum_{i<j} Delta_ij
                    <= floor(k^2/4) Delta_k.

For any tree T on [k], a binary signature is nonconstant iff at least one
tree edge crosses from 0 to 1, giving
    D_k = union_{ij in T} (A_i triangle A_j).

This script exhaustively checks the finite binary identities for small k.
"""

from __future__ import annotations

import argparse
import itertools
import math


def path_tree(k: int) -> list[tuple[int, int]]:
    return [(i, i + 1) for i in range(k - 1)]


def star_tree(k: int) -> list[tuple[int, int]]:
    return [(0, i) for i in range(1, k)]


def check_k(k: int) -> None:
    lower = k - 1
    upper = (k * k) // 4

    for bits in itertools.product((0, 1), repeat=k):
        m = sum(bits)
        splitter = 0 < m < k

        pair_disagreements = sum(
            bits[i] != bits[j]
            for i in range(k)
            for j in range(i + 1, k)
        )

        assert pair_disagreements == m * (k - m)

        if splitter:
            assert lower <= pair_disagreements <= upper
        else:
            assert pair_disagreements == 0

        for tree in (path_tree(k), star_tree(k)):
            tree_crossing = any(bits[i] != bits[j] for i, j in tree)
            assert tree_crossing == splitter

    print(
        {
            "k": k,
            "binary_signatures_checked": 2**k,
            "lower_factor": lower,
            "upper_factor": upper,
            "status": "PASS",
        }
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-k", type=int, default=12)
    args = parser.parse_args()

    for k in range(2, args.max_k + 1):
        check_k(k)


if __name__ == "__main__":
    main()
