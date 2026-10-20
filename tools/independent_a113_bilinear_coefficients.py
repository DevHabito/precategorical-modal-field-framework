#!/usr/bin/env python3
"""Exact independent A113 A84 coefficient and factor regression.

Uses stdlib fractions and fresh formulas, without importing historical
certificate code or Lean definitions. The finite samples do not prove
uniform claims over all integers, real sources or contact indices.
"""

from __future__ import annotations

from fractions import Fraction


BETA = Fraction(1, 8)
TARGET = Fraction(1, 2)
SOURCES = (
    Fraction(129, 1000),
    Fraction(131, 1000),
    Fraction(133, 1000),
)
SIZES = (521, 522, 561, 661, 1024, 2049)
CONTACTS = (2, 3, 7, 15, 29)


class ExactFiniteChannels:
    """Historical parity-dependent channels with integer-rational arithmetic."""

    def __init__(self, size: int) -> None:
        if size < 521:
            raise ValueError("Size is outside the declared A113 contract.")
        self.size = size
        self.half = size // 2
        self.unit = Fraction(1, 2**self.half)
        self.denominator = 1 - (self.half + 1) * self.unit
        self.epsilon = self.unit / (1875 if size % 2 == 0 else 2500)
        self.target_mass = (1 + TARGET**size) / 2

    def defect(self, node: Fraction) -> Fraction:
        h = self.half
        unit = self.unit
        denominator = self.denominator
        if self.size % 2 == 0:
            return (
                -2 * unit * node / denominator
                + (1 + 2 * h * unit / denominator) * node**h
                - 2 * (h - 1) * unit * node ** (h + 1) / denominator
            )
        return (
            -Fraction(3, 2) * unit * node / denominator
            + (Fraction(1, 2) + Fraction(3, 2) * h * unit / denominator)
            * node**h
            + (
                Fraction(1, 2)
                - Fraction(3, 2) * (h - 1) * unit / denominator
            )
            * node ** (h + 1)
        )

    def channel(self, node: Fraction, beta: bool) -> Fraction:
        correction = 2 * self.epsilon if beta else -2 * self.epsilon
        return (1 + node**self.size) / 2 - self.defect(node) + correction

    def slope(self, node: Fraction) -> Fraction:
        return (1 - node**self.size) / self.size


def ideal_core(contact: int, source: Fraction) -> Fraction:
    return Fraction(1, 2) * (
        (source - BETA) * (BETA * source) ** contact
        + (BETA - TARGET) * (BETA * TARGET) ** contact
        + (TARGET - source) * (source * TARGET) ** contact
    )


def check_case(size: int, source: Fraction) -> int:
    model = ExactFiniteChannels(size)
    unit = model.unit
    target_mass = model.target_mass
    beta_h = model.channel(BETA, beta=True)
    source_h = model.channel(source, beta=False)
    beta_slope = model.slope(BETA)
    source_slope = model.slope(source)
    target_slope = model.slope(TARGET)

    beta_bilinear = target_mass * source_slope - source_h * target_slope
    source_bilinear = target_mass * beta_slope - beta_h * target_slope
    target_bilinear = beta_h * source_slope - source_h * beta_slope
    for value in (beta_bilinear, source_bilinear, target_bilinear):
        assert abs(value) <= 3 * unit / size

    beta_affine = beta_bilinear + (BETA - 1) * (target_mass - source_h)
    source_affine = -source_bilinear + (1 - source) * (target_mass - beta_h)
    target_affine = -target_bilinear + (1 - TARGET) * (beta_h - source_h)
    for value in (beta_affine, source_affine, target_affine):
        assert abs(value) < 5 * unit

    beta_linear = (1 - BETA) * beta_bilinear
    source_linear = (source - 1) * source_bilinear
    target_linear = (TARGET - 1) * target_bilinear
    for value in (beta_linear, source_linear, target_linear):
        assert abs(value) <= 3 * unit / size

    constant = (
        (beta_h - target_mass) * source_slope
        + (target_mass - source_h) * beta_slope
        + (source_h - beta_h) * target_slope
    )
    assert abs(constant) <= 6 * unit / size

    for contact in CONTACTS:
        actual = (
            target_mass * (source - BETA) * (BETA * source) ** contact
            + source_h * (BETA - TARGET) * (BETA * TARGET) ** contact
            + beta_h * (TARGET - source) * (source * TARGET) ** contact
            + (beta_affine + contact * beta_linear) * BETA**contact
            + (source_affine + contact * source_linear) * source**contact
            + (target_affine + contact * target_linear) * TARGET**contact
            + constant
        )
        # Independent A83 cofactor route: do not reuse named A84 coefficients.
        def mass(node: Fraction) -> Fraction:
            return node**contact - 1 + contact * model.slope(node)

        def mass_difference(node: Fraction) -> Fraction:
            return (node - 1) * node**contact + model.slope(node)

        beta_mass = mass(BETA)
        target_mass_at_contact = mass(TARGET)
        source_mass = mass(source)
        beta_diff = mass_difference(BETA)
        target_diff = mass_difference(TARGET)
        source_diff = mass_difference(source)

        cofactor_x = target_mass * beta_mass - beta_h * target_mass_at_contact
        cofactor_y = -target_mass * beta_diff + beta_h * target_diff
        cofactor_w = -beta_mass * target_diff + target_mass_at_contact * beta_diff
        actual_from_cofactors = (
            cofactor_x * source_diff
            + cofactor_y * source_mass
            + cofactor_w * source_h
        )
        assert actual_from_cofactors == actual
        assert abs(actual - ideal_core(contact, source)) < 20 * unit

    return len(CONTACTS)


def main() -> None:
    checked = sum(check_case(size, source) for size in SIZES for source in SOURCES)
    assert checked == len(SIZES) * len(SOURCES) * len(CONTACTS)
    print("A113 independent A84 coefficient/factor rational regression: PASS")
    print(f"Size/source pairs: {len(SIZES) * len(SOURCES)}")
    print(f"Contact factor comparisons: {checked}")
    print(f"Independent A83 cofactor-to-A84 identity controls: {checked}")
    print("Bilinear/affine/linear/constant cases: 54/54/54/18")
    print("Finite controls are not a universal real/integer theorem.")


if __name__ == "__main__":
    main()
