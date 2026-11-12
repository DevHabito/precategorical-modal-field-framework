#!/usr/bin/env python3
"""Exact random-Weyl stress audit for all-d ACD angular contractions.

The vacuum RNC volume-density calculation uses the tensor

    Q_{mu nu rho sigma}
      = C^gamma_{ mu }^alpha_{ nu }
        C_{gamma rho alpha sigma}.

After averaging over spatial directions n in spatial dimension N=d-1,
the claimed decomposition is

    <Q(x)>
      = E^2 t^4
        + (3 H^2 / N) t^2 r^2
        + [3 E^2 - 3 H^2 + (3/2) D^2]
          r^4 / [N(N+2)].

The null-boundary calculation also uses

    < H_i^m_j H_{l m k} n^i n^j n^l n^k >
      = (3/2 H^2) / [N(N+2)].

This script generates exact rational algebraic Weyl tensors by:
1. building algebraic Riemann tensors from Kulkarni--Nomizu products;
2. projecting out Ricci traces in Lorentz signature;
3. checking Weyl trace-freeness exactly;
4. verifying the angular contractions with Fraction arithmetic.

No floating-point arithmetic is used.
"""

from __future__ import annotations

from fractions import Fraction
import itertools
import random


Q = Fraction


def zeros4(d: int):
    return [
        [
            [
                [Q(0) for _ in range(d)]
                for _ in range(d)
            ]
            for _ in range(d)
        ]
        for _ in range(d)
    ]


def symmetric_matrix(d: int, rng: random.Random):
    a = [[Q(0) for _ in range(d)] for _ in range(d)]
    for i in range(d):
        for j in range(i, d):
            value = Q(rng.randint(-3, 3))
            a[i][j] = value
            a[j][i] = value
    return a


def kulkarni(a, b):
    d = len(a)
    out = zeros4(d)

    for i, j, k, l in itertools.product(
        range(d), repeat=4
    ):
        out[i][j][k][l] = (
            a[i][k] * b[j][l]
            + a[j][l] * b[i][k]
            - a[i][l] * b[j][k]
            - a[j][k] * b[i][l]
        )

    return out


def add4(left, right):
    d = len(left)
    out = zeros4(d)
    for i, j, k, l in itertools.product(
        range(d), repeat=4
    ):
        out[i][j][k][l] = (
            left[i][j][k][l]
            + right[i][j][k][l]
        )
    return out


def random_riemann(d: int, seed: int):
    rng = random.Random(seed)
    out = zeros4(d)

    for _ in range(3):
        a = symmetric_matrix(d, rng)
        b = symmetric_matrix(d, rng)
        out = add4(out, kulkarni(a, b))

    return out


def metric_sign(index: int) -> Q:
    return Q(-1 if index == 0 else 1)


def weyl_project(riemann):
    d = len(riemann)

    # Ricci R_bd = g^{ac} R_abcd.
    ricci = [[Q(0) for _ in range(d)] for _ in range(d)]

    for b, dd in itertools.product(range(d), repeat=2):
        ricci[b][dd] = sum(
            metric_sign(a)
            * riemann[a][b][a][dd]
            for a in range(d)
        )

    scalar = sum(
        metric_sign(b) * ricci[b][b]
        for b in range(d)
    )

    C = zeros4(d)

    for a, b, c, dd in itertools.product(
        range(d), repeat=4
    ):
        gac = metric_sign(a) if a == c else Q(0)
        gad = metric_sign(a) if a == dd else Q(0)
        gbc = metric_sign(b) if b == c else Q(0)
        gbd = metric_sign(b) if b == dd else Q(0)

        trace1 = (
            gac * ricci[dd][b]
            - gad * ricci[c][b]
            - gbc * ricci[dd][a]
            + gbd * ricci[c][a]
        )

        trace2 = (
            gac * gbd
            - gad * gbc
        )

        C[a][b][c][dd] = (
            riemann[a][b][c][dd]
            - trace1 / Q(d - 2)
            + scalar
            * trace2
            / Q((d - 1) * (d - 2))
        )

    # Exact Weyl trace check.
    for b, dd in itertools.product(range(d), repeat=2):
        contraction = sum(
            metric_sign(a) * C[a][b][a][dd]
            for a in range(d)
        )
        assert contraction == 0

    return C


def invariants(C):
    d = len(C)
    n = d - 1

    e2 = Q(0)
    h2 = Q(0)
    d2 = Q(0)

    for i, j in itertools.product(range(1, d), repeat=2):
        e2 += C[0][i][0][j] ** 2

    for i, j, k in itertools.product(range(1, d), repeat=3):
        h2 += C[0][i][j][k] ** 2

    for i, j, k, l in itertools.product(range(1, d), repeat=4):
        d2 += C[i][j][k][l] ** 2

    return n, e2, h2, d2


def q_tensor(C, mu, nu, rho, sigma):
    d = len(C)

    return sum(
        metric_sign(gamma)
        * metric_sign(alpha)
        * C[gamma][mu][alpha][nu]
        * C[gamma][rho][alpha][sigma]
        for gamma, alpha in itertools.product(
            range(d), repeat=2
        )
    )


def angular_q_coefficients(C):
    d = len(C)
    n = d - 1

    # t^4.
    t4 = q_tensor(C, 0, 0, 0, 0)

    # t^2 r^2: sum over the six positions of two time indices,
    # then use <n_i n_j> = delta_ij / n.
    t2r2 = Q(0)
    patterns = set(itertools.permutations((0, 0, 1, 2)))

    # Instead of symbolic i,j placeholders, explicitly sum six tensor
    # placements with equal spatial index from delta_ij.
    for i in range(1, d):
        t2r2 += (
            q_tensor(C, 0, 0, i, i)
            + q_tensor(C, 0, i, 0, i)
            + q_tensor(C, 0, i, i, 0)
            + q_tensor(C, i, 0, 0, i)
            + q_tensor(C, i, 0, i, 0)
            + q_tensor(C, i, i, 0, 0)
        ) / Q(n)

    # r^4:
    # <n_i n_j n_k n_l>
    #   = (delta_ij delta_kl + delta_ik delta_jl + delta_il delta_jk)
    #     / [n(n+2)].
    r4 = Q(0)

    for i, k in itertools.product(range(1, d), repeat=2):
        r4 += (
            q_tensor(C, i, i, k, k)
            + q_tensor(C, i, k, i, k)
            + q_tensor(C, i, k, k, i)
        ) / Q(n * (n + 2))

    return t4, t2r2, r4


def boundary_h_average(C):
    d = len(C)
    n = d - 1

    # H_{ijk}=C_{0ijk}.  Compute
    # H_i^m_j H_{lmk} averaged with the fourth spherical moment.
    #
    # Pairing delta_ij delta_lk.
    term1 = Q(0)
    # Pairing delta_il delta_jk.
    term2 = Q(0)
    # Pairing delta_ik delta_jl.
    term3 = Q(0)

    for i, l in itertools.product(range(1, d), repeat=2):
        # delta_ij, delta_lk => j=i, k=l
        term1 += sum(
            C[0][i][m][i]
            * C[0][l][m][l]
            for m in range(1, d)
        )

        # delta_il, delta_jk => l=i, k=j
        term2 += sum(
            C[0][i][m][j]
            * C[0][i][m][j]
            for m, j in itertools.product(
                range(1, d), repeat=2
            )
        ) if l == i else Q(0)

        # delta_ik, delta_jl => k=i, l=j
        term3 += sum(
            C[0][i][m][j]
            * C[0][j][m][i]
            for m, j in itertools.product(
                range(1, d), repeat=2
            )
        ) if l == i else Q(0)

    return (
        term1 + term2 + term3
    ) / Q(n * (n + 2))


def run_case(d: int, seed: int) -> None:
    C = weyl_project(
        random_riemann(d, seed)
    )

    n, e2, h2, d2 = invariants(C)

    # Avoid an accidentally trivial draw.
    assert e2 + h2 + d2 != 0

    t4, t2r2, r4 = angular_q_coefficients(C)

    assert t4 == e2
    assert t2r2 == Q(3, n) * h2
    assert r4 == (
        3 * e2
        - 3 * h2
        + Q(3, 2) * d2
    ) / Q(n * (n + 2))

    h_average = boundary_h_average(C)
    assert h_average == (
        Q(3, 2)
        * h2
        / Q(n * (n + 2))
    )

    print(
        {
            "d": d,
            "seed": seed,
            "E2": str(e2),
            "H2": str(h2),
            "D2": str(d2),
            "status": "PASS",
        }
    )


def main() -> None:
    for d in (4, 5, 6, 7):
        for seed in (11, 29, 47):
            run_case(d, seed)

    print(
        "PASS: exact random-Weyl stress audit verified the all-d "
        "angular contraction identities in d=4,5,6,7."
    )


if __name__ == "__main__":
    main()
