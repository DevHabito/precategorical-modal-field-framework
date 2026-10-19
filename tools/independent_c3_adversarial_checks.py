#!/usr/bin/env python3
"""Adversarial, exact C3 checks against the frozen A84/A112/A113 contracts.

No imported historical audit routines, floating-point signs, or fitted bounds.
Finite checks do not prove the M>=521 analytic-tail theorems.
"""

from __future__ import annotations

from fractions import Fraction as F


BETA = F(1, 8)
GAMMA = F(1, 16)
TARGET = F(1, 2)
S_LOWER = F(129, 1000)
S_UPPER = F(133, 1000)


def sign(value: F) -> int:
    return int(value > 0) - int(value < 0)


def exact_contact_threshold(size: int, source: F) -> int:
    """Smallest b with source^(2b) <= 2^(-size); no logarithm."""
    threshold = F(1, 2**size)
    lower, upper = 0, size
    while lower < upper:
        middle = (lower + upper) // 2
        if source ** (2 * middle) <= threshold:
            upper = middle
        else:
            lower = middle + 1
    b = lower
    assert b > 0 and source ** (2 * (b - 1)) > threshold
    assert source ** (2 * b) <= threshold
    return b


def tolerance(size: int) -> F:
    return F(1, (1875 if size % 2 == 0 else 2500) * 2 ** (size // 2))


def rational_solve(matrix: list[list[F]], right: list[F]) -> list[F]:
    """Gauss-Jordan elimination with exact fractions and explicit pivots."""
    dimension = len(right)
    if len(matrix) != dimension or any(len(row) != dimension for row in matrix):
        raise ValueError("Expected a square linear system.")
    rows = [[F(value) for value in row] + [F(rhs)]
            for row, rhs in zip(matrix, right)]

    for column in range(dimension):
        pivot = next(
            (row for row in range(column, dimension) if rows[row][column]),
            None,
        )
        if pivot is None:
            raise ArithmeticError("Singular declared compressed/KKT basis.")
        rows[column], rows[pivot] = rows[pivot], rows[column]
        lead = rows[column][column]
        rows[column] = [value / lead for value in rows[column]]
        for row in range(dimension):
            if row == column:
                continue
            factor = rows[row][column]
            if factor:
                rows[row] = [
                    value - factor * leading
                    for value, leading in zip(rows[row], rows[column])
                ]

    result = [row[-1] for row in rows]
    assert all(
        sum(F(value) * variable for value, variable in zip(row, result))
        == F(rhs)
        for row, rhs in zip(matrix, right)
    )
    return result


def compressed_value(size: int, source: F, contact: int) -> F:
    """Direct seven-equation compressed LP equality-basis objective."""
    middle = size // 2
    primal = (0, contact, size)
    target = (1, middle, middle + 1)
    mean = F(size, 2)
    epsilon = tolerance(size)
    matrix = [
        [1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 1, 1, 1, -1],
        [*primal, 0, 0, 0, -mean],
        [0, 0, 0, *target, -mean],
        [0, 0, 0, *(TARGET ** node for node in target), 0],
        [*(source ** node for node in primal),
         *(-source ** node for node in target), -2 * epsilon],
        [*(-BETA ** node for node in primal),
         *(BETA ** node for node in target), -2 * epsilon],
    ]
    solution = rational_solve(matrix, [0, 0, 0, 0, 1, 0, 0])
    return sum(solution[index] * TARGET ** node
               for index, node in enumerate(primal))


class ExactAdjacentFactor:
    """Separate cofactor reconstruction of A84's adjacent factor E_k."""

    def __init__(self, size: int, source: F) -> None:
        self.size = size
        self.source = source
        self.powers: dict[F, list[F]] = {}
        for base in (BETA, TARGET, source):
            values = [F(1)]
            for _ in range(size):
                values.append(values[-1] * base)
            self.powers[base] = values

        half = size // 2
        unit = F(1, 2**half)
        denominator = 1 - (half + 1) * unit

        def central_function(base: F) -> F:
            value = self.powers[base]
            if size % 2 == 0:
                return (
                    -2 * unit * base / denominator
                    + (1 + 2 * half * unit / denominator) * value[half]
                    - 2 * (half - 1) * unit * value[half + 1] / denominator
                )
            return (
                -F(3, 2) * unit * base / denominator
                + (F(1, 2) + F(3, 2) * half * unit / denominator) * value[half]
                + (F(1, 2) - F(3, 2) * (half - 1) * unit / denominator)
                * value[half + 1]
            )

        def average(base: F) -> F:
            return (1 + self.powers[base][size]) / 2

        self.beta_channel = (
            average(BETA) - central_function(BETA) + 2 * tolerance(size)
        )
        self.source_channel = (
            average(source) - central_function(source) - 2 * tolerance(size)
        )
        self.target_average = average(TARGET)

    def anchored(self, base: F, contact: int) -> F:
        values = self.powers[base]
        return (
            values[contact] - F(self.size - contact, self.size)
            - F(contact, self.size) * values[self.size]
        )

    def adjacent(self, base: F, contact: int) -> F:
        values = self.powers[base]
        return (
            (base - 1) * values[contact]
            + F(1 - values[self.size], self.size)
        )

    def value(self, contact: int) -> F:
        if not 2 <= contact < self.size // 2 - 1:
            raise ValueError("Contact is outside the A84 compressed contract.")
        bb = self.anchored(BETA, contact)
        bt = self.anchored(TARGET, contact)
        bs = self.anchored(self.source, contact)
        db = self.adjacent(BETA, contact)
        dt = self.adjacent(TARGET, contact)
        ds = self.adjacent(self.source, contact)
        x = self.target_average * bb - self.beta_channel * bt
        y = -self.target_average * db + self.beta_channel * dt
        z = -bb * dt + bt * db
        return x * ds + y * bs + z * self.source_channel


def gamma_plus_adjacent_signs(size: int, source: F, contact: int) -> tuple[int, int, int]:
    """Construct the full eight-variable gamma-plus KKT equality system."""
    half = size // 2
    primal = (0, contact, contact + 1, size)
    target = (1, half, half + 1)
    mean = F(size, 2)
    epsilon = tolerance(size)
    active = ((source, 1), (BETA, -1), (GAMMA, 1))

    matrix = [
        [1, 1, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 1, 1, 1, -1],
        [*primal, 0, 0, 0, -mean],
        [0, 0, 0, 0, *target, -mean],
        [0, 0, 0, 0, *(TARGET ** k for k in target), 0],
    ]
    for base, orientation in active:
        matrix.append([
            *(orientation * base**k for k in primal),
            *(-orientation * base**k for k in target),
            -2 * epsilon,
        ])
    rhs = [0, 0, 0, 0, 1, 0, 0, 0]
    objective = [*(TARGET**k for k in primal), 0, 0, 0, 0]
    primal_solution = rational_solve(matrix, rhs)
    dual_solution = rational_solve([list(row) for row in zip(*matrix)], objective)
    q2_column = [0, 1, 0, 2, TARGET**2] + [
        -orientation * base**2 for base, orientation in active
    ]
    q2_reduced = sum(F(x) * y for x, y in zip(q2_column, dual_solution))
    return (sign(primal_solution[primal.index(contact)]),
            sign(primal_solution[primal.index(contact + 1)]),
            sign(q2_reduced))


def verify_published_negative_controls() -> None:
    for size, source, expected_b in (
        (561, S_LOWER, 95),
        (661, S_LOWER, 112),
        (821, S_LOWER, 139),
        (886, S_LOWER, 150),
        (951, S_LOWER, 161),
        (2049, S_UPPER, 353),
    ):
        b = exact_contact_threshold(size, source)
        assert b == expected_b, (size, b, expected_b)
        oracle = ExactAdjacentFactor(size, source)
        assert oracle.value(b + 2) > 0 if size != 2049 else oracle.value(b + 2) < 0
        assert oracle.value(b + 3) < 0
        assert oracle.value(b + 1) - 2 * oracle.value(b + 2) > 0

        for offset in (0, 1, 2, 3):
            contact = b + offset
            direction = sign(
                compressed_value(size, source, contact + 1)
                - compressed_value(size, source, contact)
            )
            assert direction == sign(oracle.value(contact)), (size, contact)

        if size == 2049:
            assert oracle.value(b + 1) < 0
            assert oracle.value(b + 1) - oracle.value(b + 2) < 0
        if size in (821, 886, 951):
            assert 3 * (b + 2) - size // 2 >= 13

        print(f"C3 counterexample PASS: M={size}; s={source}; b={b}")

    # Contact localization by itself does NOT imply a positive Q2 reduced cost.
    size, source, contact = 600, S_UPPER, 106
    assert exact_contact_threshold(size, source) == 104
    assert gamma_plus_adjacent_signs(size, source, contact) == (1, -1, -1)
    print("A112 false stronger q2 implication rejected exactly at M=600")


def verify_finite_contact_sequences() -> None:
    for size, source in (
        (521, S_LOWER),
        (522, S_UPPER),
        (561, S_LOWER),
        (661, S_LOWER),
        (2049, S_UPPER),
    ):
        oracle = ExactAdjacentFactor(size, source)
        b = exact_contact_threshold(size, source)
        contacts = range(2, size // 2 - 1)
        values = [oracle.value(contact) for contact in contacts]
        assert all(value > 0 for contact, value in zip(contacts, values)
                   if contact <= b)
        assert all(value < 0 for contact, value in zip(contacts, values)
                   if contact >= b + 3)
        assert 0 < oracle.value(b + 1) - 2 * oracle.value(b + 2)
        signs = [sign(value) for value in values]
        assert 0 not in signs
        assert sum(left != right for left, right in zip(signs, signs[1:])) == 1
        print(f"C3 finite-sequence PASS: M={size}; {len(values)} admissible factors")


def main() -> None:
    verify_published_negative_controls()
    verify_finite_contact_sequences()


if __name__ == "__main__":
    main()
