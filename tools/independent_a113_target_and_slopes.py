#!/usr/bin/env python3
"""Independent exact rational replay for the finite A113 target and slopes.

This script deliberately does not import historical A83/A84/A113 code
or the new Lean module. Samples guard implementation and arithmetic;
the universal real and integer quantifiers are established in Lean.
"""

from __future__ import annotations

from fractions import Fraction


BETA = Fraction(1, 8)
TAU = Fraction(1, 2)
SOURCES = (
    Fraction(129, 1000),
    Fraction(131, 1000),
    Fraction(133, 1000),
)
SIZES = (521, 522, 561, 661, 1024)


def check_size(size: int) -> int:
    if size < 521:
        raise AssertionError("Size outside certified domain.")

    half = size // 2
    unit = Fraction(1, 2**half)
    target_mass = (1 + TAU**size) / 2

    assert 0 < TAU**size <= unit
    assert target_mass - Fraction(1, 2) == TAU**size / 2
    assert abs(target_mass - Fraction(1, 2)) <= unit / 2
    assert Fraction(1, 2) <= target_mass <= 1

    checked = 0
    for node in (Fraction(0), BETA, *SOURCES, TAU):
        power = node**size
        slope = (1 - power) / size
        residual = slope - Fraction(1, size)

        assert 0 <= node <= TAU
        assert 0 <= power <= unit
        assert residual == -power / size
        assert 0 <= slope <= Fraction(1, size)
        assert abs(residual) <= unit / size

        if node <= Fraction(1, 6):
            assert power <= unit / 128
            assert abs(residual) <= unit / (128 * size)

        checked += 1

    return checked


def main() -> None:
    checks = sum(check_size(size) for size in SIZES)
    print("A113 target-mass and moment-slope exact rational replay: PASS")
    print(f"A113 sampled size/node pairs: {checks}")
    print("Scope: integer M>=521, real node in [0,1/2]")
    print("Finite rational sampling is not a proof of universal bounds.")


if __name__ == "__main__":
    main()
