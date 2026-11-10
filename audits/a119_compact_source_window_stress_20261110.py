#!/usr/bin/env python3
"""Exact source-window stress for the fixed 35-box A119 interval manifest.

Only concerns the published rational Xi-hat expression. Failure of an
interval lower bound does NOT imply the mathematical function is negative.
"""
from fractions import Fraction as F
from a119_compact_35box_fraction_certificate_20261110 import I, calc

if not __debug__:
    raise RuntimeError("Python -O disables assertions")

def certificate_min(source):
    rows = []
    for parity, stop in (("even", 12), ("odd", 19)):
        sigma = F(0) if parity == "even" else F(1, 2)
        for r in range(4, stop + 1):
            lo = 2 * (r + sigma)
            hi = F(21, 10) * (r + 1 + sigma)
            cuts = (
                (F(0), F(1, 4), F(1, 2), F(1))
                if r == 4 else
                (F(0), F(1, 2), F(1))
                if r in (5, 6, 7) else
                (F(0), F(1))
            )
            for lower, upper in zip(cuts, cuts[1:]):
                alpha = I(lo + (hi-lo) * lower, lo + (hi-lo) * upper)
                bound = calc(source, alpha, parity, r).l
                rows.append((bound, parity, r, lower, upper))
    assert len(rows) == 35
    return min(rows, key=lambda row: row[0])

original = I(F(129, 1000), F(133, 1000))
wider = I(F(2577, 20000), F(2663, 20000))
too_wide = I(F(5153, 40000), F(5327, 40000))

if __name__ == "__main__":
    out0 = certificate_min(original)
    out1 = certificate_min(wider)
    out2 = certificate_min(too_wide)
    assert out0[0] > 0 and out1[0] > 0 and out2[0] < 0
    assert out1[0] == F(
        71236007338704140184291611230761656680237,
        24836358976702853398583841218100200880000000
    ), out1
    assert out1[1:] == ("even", 4, F(1,2), F(1))
    assert out2[1:] == ("even", 4, F(1,2), F(1))
    print("PASS original source window: all 35 boxes positive")
    print("PASS expanded source window [2577/20000, 2663/20000]")
    print("expanded worst lower bound:", out1[0])
    print("PASS negative interval-CERTIFICATION control on wider window")
    print("too-wide worst lower bound:", out2[0])
    print("NOT a counterexample to Xi positivity outside the original window")
    print("NOT an extension of the full A116-A119 theorem chain")
