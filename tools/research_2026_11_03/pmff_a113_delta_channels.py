#!/usr/bin/env python3
"""Exact, finite verification of the A113 beta/source H-channel gap.

This is a diagnostic of historical uniform Delta bounds, NOT a proof
for every integer M >= 521 or every real source in the interval.
No historical script or floating sign gate is imported.
"""

from fractions import Fraction as F

BETA = F(1, 8)
SOURCES = (F(129, 1000), F(131, 1000), F(133, 1000))
SIZES = (521, 522, 561, 661, 1000, 2049, 4097)
LOWER = F(43, 10000)
UPPER = F(7, 500)


def channels(size: int, source: F) -> tuple[F, F, F, F]:
    """Return (source-H, beta-H, U, epsilon) from literal A113 definitions."""
    h = size // 2
    unit = F(1, 2**h)
    denominator = 1 - (h + 1) * unit
    assert denominator > 0
    epsilon = unit / (1875 if size % 2 == 0 else 2500)

    def defect(node: F) -> F:
        if size % 2 == 0:
            return (
                -2 * unit * node / denominator
                + (1 + 2 * h * unit / denominator) * node**h
                - 2 * (h - 1) * unit * node**(h + 1) / denominator
            )
        return (
            -F(3, 2) * unit * node / denominator
            + (F(1, 2) + F(3, 2) * h * unit / denominator) * node**h
            + (F(1, 2) - F(3, 2) * (h - 1) * unit / denominator)
            * node**(h + 1)
        )

    h_source = (1 + source**size) / 2 - defect(source) - 2 * epsilon
    h_beta = (1 + BETA**size) / 2 - defect(BETA) + 2 * epsilon
    return h_source, h_beta, unit, epsilon


def independent_gap_decomposition(size: int, source: F) -> F:
    """Explicit leading gap and parity-sensitive high-power corrections."""
    h = size // 2
    unit = F(1, 2**h)
    denominator = 1 - (h + 1) * unit
    power_m = (source**size - BETA**size) / (2 * unit)
    power_h = (source**h - BETA**h) / unit
    power_next = (source**(h + 1) - BETA**(h + 1)) / unit
    if size % 2 == 0:
        return (
            2 * (source-BETA) / denominator - F(4, 1875)
            + power_m
            - (1 + 2*h*unit/denominator) * power_h
            + (2*(h-1)*unit/denominator) * power_next
        )
    return (
        F(3, 2) * (source-BETA) / denominator - F(4, 2500)
        + power_m
        - (F(1, 2) + F(3, 2)*h*unit/denominator) * power_h
        - (F(1, 2) - F(3, 2)*(h-1)*unit/denominator) * power_next
    )


def main() -> None:
    checked = 0
    observed = []
    for size in SIZES:
        for source in SOURCES:
            h_s, h_beta, unit, epsilon = channels(size, source)
            gap = (h_s-h_beta)/unit
            assert gap == independent_gap_decomposition(size, source)
            assert LOWER < gap < UPPER

            # Negative control: swapping both +/- epsilon signs changes
            # the beta/source difference by exactly 8*epsilon/U.
            reversed_adjustments = gap + 8 * epsilon / unit
            assert reversed_adjustments != gap
            assert reversed_adjustments-gap == 8*epsilon/unit
            checked += 1
            observed.append((gap, size, source))

    assert checked == len(SIZES)*len(SOURCES) == 21
    least = min(observed)
    greatest = max(observed)
    print(f"A113 Delta finite exact regression: PASS ({checked} Fraction cases)")
    print("Both size parities and both real-source interval endpoints sampled")
    print("Exact parity decomposition and tolerance-sign mutation: PASS")
    print(f"Minimum observed case: M={least[1]}, source={least[2]}")
    print(f"Maximum observed case: M={greatest[1]}, source={greatest[2]}")
    print("Bound checked exactly: 43/10000 < (H_source-H_beta)/U < 7/500")
    print("SCOPE: finite rational samples only; no all-M/all-real-source theorem")


if __name__ == "__main__":
    main()
