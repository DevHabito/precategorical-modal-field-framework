#!/usr/bin/env python3
"""Standalone rational reconstruction of the four-point nonclosure witness.

No project imports, symbolic algebra packages, tolerances, or random samples.
Passing this script does not constitute Lean verification or external review.
"""

from fractions import Fraction
from itertools import product

F = Fraction
ZERO = F(0)
ONE = F(1)
SUPPORT = (0, 1, 2, 3)
BASE = (F(1, 4),) * 4


def moment(weights: tuple[Fraction, ...], t: Fraction) -> Fraction:
    return sum((weight * t**index for index, weight in enumerate(weights)), ZERO)


def mean(weights: tuple[Fraction, ...]) -> Fraction:
    return sum((index * weight for index, weight in enumerate(weights)), ZERO)


def cubic_kernel(t0: Fraction) -> tuple[Fraction, ...]:
    """Coefficients of (t-1)^2(t-t0) in ascending degree."""
    return (-t0, ONE + 2 * t0, -(2 + t0), ONE)


def pair(t0: Fraction) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    assert ZERO < t0 < ONE
    delta = cubic_kernel(t0)
    return (
        tuple(b + d / 16 for b, d in zip(BASE, delta)),
        tuple(b - d / 16 for b, d in zip(BASE, delta)),
    )


def determinant_three(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    """Direct Leibniz formula for 3x3 matrices, independent of SymPy."""
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def verify_pair(t0: Fraction, t1: Fraction) -> None:
    left, right = pair(t0)
    assert left != right
    assert all(w > ZERO for w in (*left, *right))
    assert sum(left, ZERO) == sum(right, ZERO) == ONE
    assert mean(left) == mean(right) == F(3, 2)
    assert moment(left, t0) == moment(right, t0)
    assert moment(left, ONE) == moment(right, ONE)
    assert (
        moment(left, t1) - moment(right, t1)
        == (t1 - ONE)**2 * (t1 - t0) / 8
    )
    if t1 != t0 and t1 != ONE:
        assert moment(left, t1) != moment(right, t1)
    else:
        assert moment(left, t1) == moment(right, t1)


def main() -> None:
    t0, t1 = F(1, 4), F(1, 2)
    left, right = pair(t0)
    assert left == tuple(F(v, 64) for v in (15, 22, 7, 20))
    assert right == tuple(F(v, 64) for v in (17, 10, 25, 12))
    verify_pair(t0, t1)
    assert moment(left, t0) == moment(right, t0) == F(85, 256)
    assert moment(left, t1) == F(121, 256)
    assert moment(right, t1) == F(119, 256)
    assert moment(left, t1) - moment(right, t1) == F(1, 128)

    # The mass, mean and t0-moment constraints have rank three.
    rows = (
        (ONE, ONE, ONE),
        (ZERO, ONE, F(2)),
        (ONE, t0, t0**2),
    )
    assert determinant_three(rows) == (t0 - ONE)**2 != ZERO
    kernel = cubic_kernel(t0)
    assert sum(kernel, ZERO) == ZERO
    assert mean(kernel) == ZERO
    assert moment(kernel, t0) == ZERO

    grid = (F(1, 8), F(1, 4), F(1, 2), F(3, 4), F(7, 8))
    cases = 0
    for initial, updated in product(grid, repeat=2):
        verify_pair(initial, updated)
        cases += 1
    assert cases == 25

    # Adversarial controls: no contradiction at t1=t0 or at t1=1.
    assert moment(left, t0) == moment(right, t0)
    assert moment(left, ONE) == moment(right, ONE)
    # Perturb one pair while preserving total mass: mean and moment fail.
    perturbed = (left[0] + F(1, 64), left[1] - F(1, 64), *left[2:])
    assert sum(perturbed, ZERO) == ONE
    assert mean(perturbed) != mean(right)
    assert moment(perturbed, t0) != moment(right, t0)
    print("MF-R049/F3: standalone Fraction witness PASS")
    print("Fixed support: 0,1,2,3; lambda=2*log(2); scale=1/2")
    print("Initial t0=1/4: Mplus=Mminus=85/256")
    print("After contraction t1=1/2: Mplus=121/256; Mminus=119/256")
    print("Exact moment separation: 1/128")
    print("Constraint rank=3 (nonzero minor), kernel dimension=1")
    print(f"Generalized construction: {cases} rational parameter pairs PASS")
    print("Equality cases and mass-preserving perturbation controls PASS")
    print("Scope: algebra and rational arithmetic; no log/exp kernel or human review")


if __name__ == "__main__":
    main()
