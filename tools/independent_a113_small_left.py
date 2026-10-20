#!/usr/bin/env python3
"""Independent exact audit of the uniform A113 small-left sign lemma.

The mathematical uniform proof is recorded in the companion checkpoint.
Finite rational controls test the reconstruction but do not establish the
universal quantifiers. No historical A113 certificate module is imported.
"""

from __future__ import annotations

from fractions import Fraction


BETA = Fraction(1, 8)
TARGET = Fraction(1, 2)
SOURCE_MIN = Fraction(129, 1000)
SOURCE_MAX = Fraction(133, 1000)
MIN_SIZE = 521
MAX_SMALL_CONTACT = 29


def require(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


def target_epsilon(size: int) -> Fraction:
    denominator = 1875 if size % 2 == 0 else 2500
    return Fraction(1, denominator * 2 ** (size // 2))


def source_d(size: int, node: Fraction) -> Fraction:
    h = size // 2
    unit = Fraction(1, 2**h)
    denominator = 1 - (h + 1) * unit
    if size % 2 == 0:
        return (
            -2 * unit * node / denominator
            + (1 + 2 * h * unit / denominator) * node**h
            - 2 * (h - 1) * unit * node ** (h + 1) / denominator
        )
    return (
        -Fraction(3, 2) * unit * node / denominator
        + (Fraction(1, 2) + Fraction(3, 2) * h * unit / denominator)
        * node**h
        + (Fraction(1, 2) - Fraction(3, 2) * (h - 1) * unit / denominator)
        * node ** (h + 1)
    )


def adjusted_h(size: int, node: Fraction, *, beta_channel: bool) -> Fraction:
    tolerance = 2 * target_epsilon(size)
    adjustment = tolerance if beta_channel else -tolerance
    return (1 + node**size) / 2 - source_d(size, node) + adjustment


def moment_slope(size: int, node: Fraction) -> Fraction:
    return (1 - node**size) / size


def adjacent_factor_from_cofactors(size: int, k: int, source: Fraction) -> Fraction:
    target_mass = (1 + TARGET**size) / 2
    h_beta = adjusted_h(size, BETA, beta_channel=True)
    h_source = adjusted_h(size, source, beta_channel=False)

    def mass(node: Fraction) -> Fraction:
        return node**k - 1 + k * moment_slope(size, node)

    def mass_delta(node: Fraction) -> Fraction:
        return (node - 1) * node**k + moment_slope(size, node)

    x = target_mass * mass(BETA) - h_beta * mass(TARGET)
    y = -target_mass * mass_delta(BETA) + h_beta * mass_delta(TARGET)
    w = -mass(BETA) * mass_delta(TARGET) + mass(TARGET) * mass_delta(BETA)
    return x * mass_delta(source) + y * mass(source) + w * h_source


def adjacent_factor_from_ten_terms(size: int, k: int, source: Fraction) -> Fraction:
    target_mass = (1 + TARGET**size) / 2
    h_beta = adjusted_h(size, BETA, beta_channel=True)
    h_source = adjusted_h(size, source, beta_channel=False)
    a_beta = moment_slope(size, BETA)
    a_source = moment_slope(size, source)
    a_target = moment_slope(size, TARGET)

    beta_affine = (
        target_mass * a_source - h_source * a_target
        + (BETA - 1) * (target_mass - h_source)
    )
    beta_slope = (1 - BETA) * (target_mass * a_source - h_source * a_target)
    source_affine = (
        -target_mass * a_beta + h_beta * a_target
        + (1 - source) * (target_mass - h_beta)
    )
    source_slope = (source - 1) * (target_mass * a_beta - h_beta * a_target)
    target_affine = (
        -h_beta * a_source + h_source * a_beta
        + (1 - TARGET) * (h_beta - h_source)
    )
    target_slope = (TARGET - 1) * (h_beta * a_source - h_source * a_beta)
    constant = (
        (h_beta - target_mass) * a_source
        + (target_mass - h_source) * a_beta
        + (h_source - h_beta) * a_target
    )
    return (
        target_mass * (source - BETA) * (BETA * source) ** k
        + h_source * (BETA - TARGET) * (BETA * TARGET) ** k
        + h_beta * (TARGET - source) * (source * TARGET) ** k
        + (beta_affine + k * beta_slope) * BETA**k
        + (source_affine + k * source_slope) * source**k
        + (target_affine + k * target_slope) * TARGET**k
        + constant
    )


def complete_homogeneous_degree(degree: int, nodes: tuple[Fraction, ...]) -> Fraction:
    values = [Fraction(1)] + [Fraction(0)] * degree
    for node in nodes:
        for exponent in range(1, degree + 1):
            values[exponent] += node * values[exponent - 1]
    return values[degree]


def zero_unit_core(contact: int, source: Fraction) -> Fraction:
    nodes = (BETA * source, BETA * TARGET, source * TARGET)
    return (
        Fraction(1, 2)
        * (source - BETA)
        * (TARGET - BETA)
        * (TARGET - source)
        * complete_homogeneous_degree(contact - 1, nodes)
    )


def verify_uniform_rational_thresholds() -> None:
    h = MIN_SIZE // 2
    unit = Fraction(1, 2**h)
    require((h + 1) * unit < Fraction(1, 4), "Denominator gate failed")
    require(h * unit < Fraction(1, 4), "Linear exponent gate failed")
    require(SOURCE_MAX < Fraction(1, 6), "Source cap failed")
    require(Fraction(1, 3) ** h < Fraction(1, 1000), "Exponential cap failed")
    require(Fraction(1, 18) ** h < Fraction(1, 1000), "High power cap failed")

    even_d_bound = Fraction(4, 9) + Fraction(16, 9) / 1000
    odd_d_bound = Fraction(1, 3) + Fraction(7, 6) / 1000
    require(even_d_bound < Fraction(1, 2), "Even D upper bound failed")
    require(odd_d_bound < Fraction(1, 2), "Odd D upper bound failed")
    require(
        Fraction(1, 2) + Fraction(1, 2000) + Fraction(2, 1875) < 1,
        "Uniform H envelope failed",
    )

    perturbation_coefficient = 18 + Fraction(9 * MAX_SMALL_CONTACT + 6, MIN_SIZE)
    require(perturbation_coefficient < 20, "Perturbation cap failed")
    core_lower = (
        Fraction(1, 2)
        * (SOURCE_MIN - BETA)
        * (TARGET - BETA)
        * (TARGET - SOURCE_MAX)
        * (SOURCE_MIN * TARGET) ** (MAX_SMALL_CONTACT - 1)
    )
    require(core_lower > 20 * unit, "Positive core does not dominate error")


def verify_independent_finite_controls() -> int:
    tested = 0
    for size in (521, 522, 561, 661):
        unit = Fraction(1, 2 ** (size // 2))
        for source in (SOURCE_MIN, Fraction(131, 1000), SOURCE_MAX):
            for node, beta_channel in ((BETA, True), (source, False)):
                require(abs(source_d(size, node)) < unit / 2, "D replay failed")
                require(
                    abs(adjusted_h(size, node, beta_channel=beta_channel) - Fraction(1, 2))
                    < unit,
                    "H replay failed",
                )
            for k in (2, 3, 7, 15, MAX_SMALL_CONTACT):
                direct = adjacent_factor_from_cofactors(size, k, source)
                expanded = adjacent_factor_from_ten_terms(size, k, source)
                baseline = zero_unit_core(k, source)
                require(direct == expanded, "A83/A84 exact identity mismatch")
                require(direct > 0, "Small-left sign failure")
                require(abs(direct - baseline) < 20 * unit, "Error bound failure")
                tested += 1
    return tested


def main() -> None:
    verify_uniform_rational_thresholds()
    tested = verify_independent_finite_controls()
    print("A113 small-left universal rational thresholds: PASS")
    print("A113 small-left analytic certificate: E_k >= core - 20*U > 0")
    print(f"A113 small-left independent exact finite controls: {tested} PASS")
    print("Scope: M>=521, 129/1000<=s<=133/1000, 2<=k<=29 only")
    print("No full A113, lifted KKT, or physical theorem is certified here")


if __name__ == "__main__":
    main()
