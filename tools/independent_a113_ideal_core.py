#!/usr/bin/env python3
"""Independent exact regression for the A113 ideal-core recurrence.

The core does not depend on M. Avoid multiplying reported test counts
by unrelated M values. These pointwise checks supplement, not replace,
the universally quantified Lean proof.
"""

from fractions import Fraction


BETA = Fraction(1, 8)
TARGET = Fraction(1, 2)
SOURCES = (
    Fraction(129, 1000),
    Fraction(131, 1000),
    Fraction(133, 1000),
)
CONTACTS = range(1, 30)


def ideal_core(contact: int, source: Fraction) -> Fraction:
    return (
        (source - BETA) * (BETA * source) ** contact
        + (BETA - TARGET) * (BETA * TARGET) ** contact
        + (TARGET - source) * (source * TARGET) ** contact
    ) / 2


def vandermonde_base(source: Fraction) -> Fraction:
    return (source - BETA) * (TARGET - BETA) * (TARGET - source) / 2


def main() -> None:
    checked = 0
    baseline = (
        (Fraction(129, 1000) - BETA)
        * (TARGET - BETA)
        * (TARGET - Fraction(133, 1000))
        * (Fraction(129, 2000) ** 28)
        / 2
    )
    assert baseline > 20 / Fraction(2**260)

    for source in SOURCES:
        constant = vandermonde_base(source)
        assert constant > 0
        assert ideal_core(0, source) == 0
        assert ideal_core(1, source) == constant

        for k in CONTACTS:
            current = ideal_core(k, source)
            successor = ideal_core(k + 1, source)
            correction = (
                (source - BETA)
                * (TARGET - BETA)
                * (
                    TARGET * (BETA * TARGET) ** k
                    - source * (BETA * source) ** k
                )
                / 2
            )
            assert successor == source * TARGET * current + correction
            assert correction > 0
            assert current >= constant * (source * TARGET) ** (k - 1)
            assert current >= baseline
            checked += 1

    # The strict sign requires ordered, distinct nodes.
    assert ideal_core(1, BETA) == 0
    assert ideal_core(1, TARGET) == 0

    print(f"A113 ideal-core exact recurrence: PASS ({checked} distinct source/contact pairs)")
    print("A113 ideal-core uniform rational regression: PASS")
    print("A113 boundary controls (equal nodes): PASS")
    print("This finite regression does not prove any quantified theorem.")


if __name__ == "__main__":
    main()
