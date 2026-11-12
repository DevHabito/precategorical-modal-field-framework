#!/usr/bin/env python3
"""Random algebraic-Weyl regression for the vacuum L^4 invariant basis.

The analytic theorem says:

- d=3 spacetime: Weyl vanishes identically;
- d=4 spacetime: the parity-even quadratic observer-dependent invariant
  space has rank 2;
- d>=5 spacetime: it has rank 3, represented by E^2, H^2, D^2.

This script generates random algebraic curvature tensors using sums of
Kulkarni-Nomizu products, projects them to Weyl tensors in Lorentz signature,
and checks:

1. Weyl trace-freeness and Bianchi symmetry;
2. spatial trace D -> E;
3. alternative H and D contractions reduce to the standard norms;
4. D^2 = 4 E^2 in d=4;
5. numerical rank of a redundant list of parity-even contractions:
      rank 2 in d=4,
      rank 3 in d>=5.

This is a regression only.  The invariant-basis proof is analytic.
"""

from __future__ import annotations

import argparse
import numpy as np


def kulkarni_nomizu(
    a: np.ndarray,
    b: np.ndarray,
) -> np.ndarray:
    d = a.shape[0]
    out = np.zeros(
        (d, d, d, d),
        dtype=float,
    )

    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):
                    out[i, j, k, l] = (
                        a[i, k] * b[j, l]
                        + a[j, l] * b[i, k]
                        - a[i, l] * b[j, k]
                        - a[j, k] * b[i, l]
                    )

    return out


def random_algebraic_riemann(
    d: int,
    rng: np.random.Generator,
    terms: int = 6,
) -> np.ndarray:
    r = np.zeros(
        (d, d, d, d),
        dtype=float,
    )

    for _ in range(terms):
        a = rng.normal(
            size=(d, d)
        )
        a = (a + a.T) / 2.0

        b = rng.normal(
            size=(d, d)
        )
        b = (b + b.T) / 2.0

        r += kulkarni_nomizu(
            a,
            b,
        )

    return r


def project_to_weyl(
    r: np.ndarray,
) -> np.ndarray:
    d = r.shape[0]

    g = np.diag(
        [-1.0]
        +
        [1.0] * (d - 1)
    )

    g_inv = g.copy()

    ric = np.einsum(
        "ac,abcd->bd",
        g_inv,
        r,
    )

    scalar = float(
        np.einsum(
            "bd,bd->",
            g_inv,
            ric,
        )
    )

    c = np.zeros_like(r)

    for a in range(d):
        for b in range(d):
            for cc in range(d):
                for dd in range(d):
                    ric_part = (
                        g[a, cc] * ric[dd, b]
                        - g[a, dd] * ric[cc, b]
                        - g[b, cc] * ric[dd, a]
                        + g[b, dd] * ric[cc, a]
                    ) / (d - 2)

                    scalar_part = (
                        scalar
                        * (
                            g[a, cc] * g[dd, b]
                            - g[a, dd] * g[cc, b]
                        )
                        /
                        (
                            (d - 1)
                            * (d - 2)
                        )
                    )

                    c[a, b, cc, dd] = (
                        r[a, b, cc, dd]
                        - ric_part
                        + scalar_part
                    )

    return c


def decompose(
    c: np.ndarray,
):
    e = c[
        0,
        1:,
        0,
        1:,
    ]

    h = c[
        0,
        1:,
        1:,
        1:,
    ]

    d_tensor = c[
        1:,
        1:,
        1:,
        1:,
    ]

    return e, h, d_tensor


def invariant_vector(
    c: np.ndarray,
) -> np.ndarray:
    e, h, d_tensor = decompose(c)
    n = e.shape[0]

    delta = np.eye(n)

    ric_d = np.einsum(
        "kl,kilj->ij",
        delta,
        d_tensor,
    )

    e2 = float(
        np.einsum(
            "ij,ij->",
            e,
            e,
        )
    )

    h2 = float(
        np.einsum(
            "ijk,ijk->",
            h,
            h,
        )
    )

    d2 = float(
        np.einsum(
            "ijkl,ijkl->",
            d_tensor,
            d_tensor,
        )
    )

    e_ric_d = float(
        np.einsum(
            "ij,ij->",
            e,
            ric_d,
        )
    )

    ric_d2 = float(
        np.einsum(
            "ij,ij->",
            ric_d,
            ric_d,
        )
    )

    d_alt = float(
        np.einsum(
            "ijkl,ikjl->",
            d_tensor,
            d_tensor,
        )
    )

    h_alt_1 = float(
        np.einsum(
            "ijk,jik->",
            h,
            h,
        )
    )

    h_alt_2 = float(
        np.einsum(
            "ijk,kij->",
            h,
            h,
        )
    )

    return np.array(
        [
            e2,
            h2,
            d2,
            e_ric_d,
            ric_d2,
            d_alt,
            h_alt_1,
            h_alt_2,
        ],
        dtype=float,
    )


def max_weyl_trace(
    c: np.ndarray,
) -> float:
    d = c.shape[0]
    g_inv = np.diag(
        [-1.0]
        +
        [1.0] * (d - 1)
    )

    trace = np.einsum(
        "ac,abcd->bd",
        g_inv,
        c,
    )

    return float(
        np.max(
            np.abs(trace)
        )
    )


def max_bianchi_error(
    c: np.ndarray,
) -> float:
    cyclic = (
        c
        +
        np.transpose(
            c,
            (0, 2, 3, 1),
        )
        +
        np.transpose(
            c,
            (0, 3, 1, 2),
        )
    )

    return float(
        np.max(
            np.abs(cyclic)
        )
    )


def sample_dimension(
    d: int,
    samples: int,
    rng: np.random.Generator,
) -> None:
    rows = []

    max_trace = 0.0
    max_bianchi = 0.0
    max_d_trace_error = 0.0

    for _ in range(samples):
        r = random_algebraic_riemann(
            d,
            rng,
        )

        c = project_to_weyl(r)

        max_trace = max(
            max_trace,
            max_weyl_trace(c),
        )

        max_bianchi = max(
            max_bianchi,
            max_bianchi_error(c),
        )

        e, _h, d_tensor = (
            decompose(c)
        )

        spatial_trace = np.einsum(
            "kl,kilj->ij",
            np.eye(d - 1),
            d_tensor,
        )

        max_d_trace_error = max(
            max_d_trace_error,
            float(
                np.max(
                    np.abs(
                        spatial_trace
                        -
                        e
                    )
                )
            ),
        )

        rows.append(
            invariant_vector(c)
        )

    matrix = np.vstack(rows)

    singular_values = (
        np.linalg.svd(
            matrix,
            compute_uv=False,
        )
    )

    scale = singular_values[0]

    rank = int(
        np.sum(
            singular_values
            >
            scale * 1e-10
        )
    )

    print(
        {
            "d": d,
            "rank": rank,
            "max_weyl_trace": max_trace,
            "max_bianchi_error":
                max_bianchi,
            "max_D_trace_minus_E":
                max_d_trace_error,
            "singular_values":
                singular_values.tolist(),
        }
    )

    assert max_trace < 1e-8
    assert max_bianchi < 1e-8
    assert max_d_trace_error < 1e-8

    # Check the universal redundant-contraction identities.
    e2 = matrix[:, 0]
    h2 = matrix[:, 1]
    d2 = matrix[:, 2]

    assert np.allclose(
        matrix[:, 3],
        e2,
        rtol=1e-9,
        atol=1e-9,
    )

    assert np.allclose(
        matrix[:, 4],
        e2,
        rtol=1e-9,
        atol=1e-9,
    )

    assert np.allclose(
        matrix[:, 5],
        0.5 * d2,
        rtol=1e-9,
        atol=1e-9,
    )

    assert np.allclose(
        matrix[:, 6],
        0.5 * h2,
        rtol=1e-9,
        atol=1e-9,
    )

    assert np.allclose(
        matrix[:, 7],
        -0.5 * h2,
        rtol=1e-9,
        atol=1e-9,
    )

    if d == 4:
        assert rank == 2

        assert np.allclose(
            d2,
            4.0 * e2,
            rtol=1e-9,
            atol=1e-9,
        )

    elif d >= 5:
        assert rank == 3


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dimensions",
        default="4,5,6,7",
    )

    parser.add_argument(
        "--samples",
        type=int,
        default=30,
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=20261112,
    )

    args = parser.parse_args()

    dimensions = [
        int(part.strip())
        for part
        in args.dimensions.split(",")
        if part.strip()
    ]

    rng = np.random.default_rng(
        args.seed
    )

    for d in dimensions:
        if d < 4:
            raise ValueError(
                "Use d>=4. In d=3 the Weyl tensor vanishes identically."
            )

        sample_dimension(
            d,
            args.samples,
            rng,
        )

    print(
        "PASS: random algebraic-Weyl contractions have rank 2 in d=4 and rank 3 for d>=5."
    )


if __name__ == "__main__":
    main()
