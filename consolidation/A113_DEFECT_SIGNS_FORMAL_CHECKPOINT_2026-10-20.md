# A113 defect signs — parity-complete Lean checkpoint

**Date:** 2026-10-20  
**Review branch:** `audit/2026-10-19-trust-and-integrity`  
**Status:** the theorem source has been committed for pinned Lean compilation and separate module-level `leanchecker` replay. Use the exact GitHub Actions run to determine whether it passed; the existence of this document is not certification.

## Claim and exact historical parameters

For all integers `M>=521` and all real nodes `0<=r<=1/6`, let
`h=floor(M/2)`, `U=(1/2)^h`, and `d=1-(h+1)U`. Use exactly the historical parity-dependent `D_M(r)` formulas in `A113FiniteChannels.lean`.

The new module `formal/lean/PrecategoryFormal/A113DefectSigns.lean`
formalizes the parity-specific triangle inequalities and combines them by cases on `M % 2`. Its intended conclusion is

```text
|D_M(r)| < U/2.
```

This includes the frozen beta node `1/8` and the complete source interval `[129/1000,133/1000]`; it is not a finite sample.

## Quantitative derivation

The previously independently replayed Lean module proves:

```text
0 < U; d >= 3/4;
r^h <= U/128; r^(h+1) <= U/768;
h*U/d <= 1/3.
```

The elementary ordered-ring inequality `(h-1)*U/d<=1/3` follows because `h>=1` and `U/d>0`.

For **even M**, the three absolute contributions to the defect are bounded by

```text
2*U*r/d                 <= (4/9)*U,
(1+2*h*U/d)*r^h         <= (5/384)*U,
2*(h-1)*U*r^(h+1)/d    <= (1/1152)*U.
```

Their sum is exactly `11/24*U < U/2`.

For **odd M**, the correction `1/2-(3/2)*(h-1)*U/d` lies in `[0,1/2]`. Therefore the three contributions are bounded by

```text
(3/2)*U*r/d                            <= (1/3)*U,
(1/2+(3/2)*h*U/d)*r^h                  <= U/128,
(1/2-(3/2)*(h-1)*U/d)*r^(h+1)       <= U/1536.
```

Their sum is `175/512*U < U/2`. All constants are rational, not decimal approximations.

The proof is decomposed into real-algebra helper lemmas and corresponding universal theorems for the actual `a113EvenDefect`, `a113OddDefect`, and parity selector `a113Defect`. No `sorry`, `admit`, `native_decide`, or assumption of the target sign is permitted.

## Assurance and remaining work

The complete final theorem is conditional only on `M>=521` and `0<=r<=1/6`, once the pinned build and `leanchecker` finish successfully. Prior algebraic, dyadic and high-power dependencies were checked independently.

A successful kernel replay of this statement would still **not** prove the final A113 small-left positivity result. The next obligations are the finite-size H-channel deviations, the target and moment-slope envelopes, and the ten-term actual-minus-ideal factor bound `|E_(M,k)(s)-F_k(s)|<20U`. The middle/right/central sectors and damaged historical ZIP archives remain unresolved.
