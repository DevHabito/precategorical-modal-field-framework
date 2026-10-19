#!/usr/bin/env python3
"""Independent exact determinant/Schur orientation controls for A112/A114.

The source-independent seven-row equality system is rebuilt from the
P/Q supports and band equations. No historical determinant routines are
imported. Finite controls are not a uniform-tail analytic certificate.
"""

from __future__ import annotations

from fractions import Fraction as F


BETA = F(1, 8)
GAMMA = F(1, 16)
TARGET = F(1, 2)
CONTROLS = (
    (521, F(129, 1000), 91),
    (522, F(131, 1000), 91),
    (561, F(53, 400), 98),
    (600, F(133, 1000), 106),
    (821, F(129, 1000), 141),
    (561, F(13277, 100000), 99),
    (1000, F(129, 1000), 171),
)


def determinant(matrix: list[list[F]]) -> F:
    """Exact row-elimination determinant, including row-swap orientation."""
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("The determinant requires a square matrix.")
    rows = [[F(value) for value in row] for row in matrix]
    answer = F(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if rows[row][column]),
            None,
        )
        if pivot is None:
            return F(0)
        if pivot != column:
            rows[pivot], rows[column] = rows[column], rows[pivot]
            answer = -answer
        scale = rows[column][column]
        answer *= scale
        for row in range(column + 1, size):
            ratio = rows[row][column] / scale
            if ratio:
                for index in range(column + 1, size):
                    rows[row][index] -= ratio * rows[column][index]
                rows[row][column] = F(0)
    return answer


def exact_solve(matrix: list[list[F]], rhs: list[F]) -> list[F]:
    """Independent Gauss-Jordan source-independent affine-branch solve."""
    size = len(rhs)
    if len(matrix) != size or any(len(row) != size for row in matrix):
        raise ValueError("Expected a square system.")
    rows = [[F(value) for value in matrix[index]] + [F(rhs[index])]
            for index in range(size)]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if rows[row][column]),
            None,
        )
        if pivot is None:
            raise ArithmeticError("Singular source-independent block.")
        rows[pivot], rows[column] = rows[column], rows[pivot]
        lead = rows[column][column]
        rows[column] = [value / lead for value in rows[column]]
        for row in range(size):
            if row != column:
                ratio = rows[row][column]
                if ratio:
                    rows[row] = [
                        value - ratio * pivot_value
                        for value, pivot_value in zip(rows[row], rows[column])
                    ]
    result = [row[-1] for row in rows]
    assert all(
        sum(F(value) * x for value, x in zip(matrix[index], result))
        == F(rhs[index])
        for index in range(size)
    )
    return result


def exact_threshold(size: int, source: F) -> int:
    threshold = F(1, 2**size)
    lower, upper = 0, size
    while lower < upper:
        middle = (lower + upper) // 2
        if source ** (2 * middle) <= threshold:
            upper = middle
        else:
            lower = middle + 1
    return lower


def orientation_control(size: int, source: F, contact: int) -> None:
    half = size // 2
    assert contact in (exact_threshold(size, source) + 1,
                       exact_threshold(size, source) + 2)
    assert F(129, 1000) <= source <= F(133, 1000)
    p_nodes = (0, contact, contact + 1, size)
    q_nodes = (1, half, half + 1)
    mean = F(size, 2)
    epsilon = F(1, (1875 if size % 2 == 0 else 2500) * 2**half)

    # Seven source-independent equalities, variables P4,Q3,t.
    source_free = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [*p_nodes, 0, 0, 0, -mean],
        [0, 0, 0, 0, *q_nodes, -mean],
        [0, 0, 0, 0, *(TARGET**node for node in q_nodes), 0],
        [*(-BETA**node for node in p_nodes),
         *(BETA**node for node in q_nodes), -2 * epsilon],
        [*(GAMMA**node for node in p_nodes),
         *(-GAMMA**node for node in q_nodes), -2 * epsilon],
    ]
    alpha_row = [
        *(source**node for node in p_nodes),
        *(-source**node for node in q_nodes),
        -2 * epsilon,
    ]
    # The original eight-row order is essential for determinant orientation.
    full_basis = source_free[:5] + [alpha_row] + source_free[5:]

    # Each non-t basic variable is affine in t after the seven-row solve.
    free_columns = [row[:-1] for row in source_free]
    branch_slope = exact_solve(
        free_columns, [-row[-1] for row in source_free]
    )
    source_slope = (
        sum(x * y for x, y in zip(alpha_row[:-1], branch_slope))
        + alpha_row[-1]
    )

    p_interpolation = [
        [F(1)] * 4,
        [F(node, size) for node in p_nodes],
        [BETA**node for node in p_nodes],
        [GAMMA**node for node in p_nodes],
    ]
    q_moment = [
        [F(1)] * 3,
        [F(node) for node in q_nodes],
        [TARGET**node for node in q_nodes],
    ]
    p_det = determinant(p_interpolation)
    q_det = determinant(q_moment)
    full_det = determinant(full_basis)
    unit = F(1, 2**half)
    predicted_q_det = (1 - (half + 1) * unit) / 2

    assert q_det == predicted_q_det > 0
    assert p_det < 0
    assert source_slope < 0
    assert full_det == size * p_det * q_det * source_slope
    assert full_det > 0

    print(
        f"A112 determinant PASS: M={size}, j={contact}; "
        "det(P)<0, det(Q)>0, A(s)<0, det(B8)>0; "
        "exact Schur factorization"
    )


STRICT_GAMMA_PLUS_CONTROLS = (
    (522, F(131, 1000), 91),
    (561, F(53, 400), 98),
    (561, F(13277, 100000), 99),
)


def verify_q_reduced_cost_checkpoints() -> None:
    """Check Q checkpoint orientation against every unused integer atom.

    The analytic six-function Chebyshev zero-budget argument is separate.
    This is an exact finite falsification control of the full LP dual signs.
    """
    for size, source, contact in STRICT_GAMMA_PLUS_CONTROLS:
        h = size // 2
        p_nodes = (0, contact, contact + 1, size)
        q_nodes = (1, h, h + 1)
        mean = F(size, 2)
        epsilon = F(1, (1875 if size % 2 == 0 else 2500) * 2**h)
        active = ((source, 1), (BETA, -1), (GAMMA, 1))
        rows = [
            [1, 1, 1, 1, 0, 0, 0, -1],
            [0, 0, 0, 0, 1, 1, 1, -1],
            [*p_nodes, 0, 0, 0, -mean],
            [0, 0, 0, 0, *q_nodes, -mean],
            [0, 0, 0, 0, *(TARGET**node for node in q_nodes), 0],
        ]
        for base, orientation in active:
            rows.append([
                *(orientation * base**node for node in p_nodes),
                *(-orientation * base**node for node in q_nodes),
                -2 * epsilon,
            ])
        rhs = [0, 0, 0, 0, 1, 0, 0, 0]
        objective = [
            *(TARGET**node for node in p_nodes),
            0, 0, 0, 0,
        ]
        primal = exact_solve(rows, rhs)
        dual = exact_solve([list(row) for row in zip(*rows)], objective)
        assert all(value > 0 for value in primal)
        assert all(value > 0 for value in dual[5:])

        def q_reduced_cost(node: int) -> F:
            column = [0, 1, 0, node, TARGET**node] + [
                -orientation * base**node for base, orientation in active
            ]
            return sum(F(x) * y for x, y in zip(column, dual))

        assert all(q_reduced_cost(node) == 0 for node in q_nodes)
        checkpoints = (0, 2, h - 1, h + 2, size)
        assert all(q_reduced_cost(node) > 0 for node in checkpoints)
        assert all(
            q_reduced_cost(node) > 0
            for node in range(size + 1)
            if node not in set(q_nodes)
        )
        print(
            f"A112 Q ECT controls PASS: M={size}, j={contact}; "
            "all five checkpoints and every nonbasic integer Q cost >0"
        )


def main() -> None:
    for size, source, contact in CONTROLS:
        orientation_control(size, source, contact)
    verify_q_reduced_cost_checkpoints()


if __name__ == "__main__":
    main()
