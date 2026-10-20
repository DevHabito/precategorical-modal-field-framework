# A113 Lean formalization checkpoint — algebra before analytic closure

**Date:** 2026-10-19  
**Review branch:** `audit/2026-10-19-trust-and-integrity`  
**Assurance status:** Lean source committed and CI wired. Do not report the new
module as checked until the pinned build, axiom trace and module-specific
`leanchecker` pass on the exact revision being described.

## Why this module exists

The A113 historical certificate was recovered and replayed, but replaying
a positive arithmetic margin does not certify the inequalities that bound the
original A84 factors. The clean-room small-left derivation in
[A113_SMALL_LEFT_UNIFORM_PROOF_2026-10-19.md](A113_SMALL_LEFT_UNIFORM_PROOF_2026-10-19.md)
addresses one sector, with several remaining formal obligations.

The new source
`formal/lean/PrecategoryFormal/A113SmallLeftBridge.lean`
is deliberately a smaller, proof-assistant-facing component. It has no
`sorry`, `admit`, `axiom`, `native_decide`, or result-specific
replacement of an unproved analytic premise.

## Declared theorems and exact interpretation

| Lean theorem | Mathematical content | Scope |
|---|---|---|
| `contactAdjacentFactor_eq_tenTermFactor` | A83 cofactor expression equals A84 ten-term expansion | Unconditional polynomial identity, every natural contact and arbitrary real parameters |
| `contactIdealCore_from_cofactors` | Equal half-moments and common slopes yield the ideal triple-product expression | Unconditional under precisely the displayed equal-moment substitutions |
| `contactIdealCore_one`, `contactIdealCore_two` | Exact low-contact ideal-core factorizations | Only contacts 1 and 2 |
| `contactIdealCore_one_pos`, `contactIdealCore_two_pos` | Positive low-contact comparison factors | Ordered positive nodes only |
| `contactSmallLeftRationalMargin` | A frozen rational lower bound exceeds `20 / 2^260` | Exact numeric inequality, no numerical approximation |
| `contactSmallLeftPositive_of_uniformBounds` | Core lower bound + remainder bound + unit bound imply positivity | Conditional order-theoretic statement |
| `contactA113SmallLeftPositive_of_analyticEnvelopes` | Same implication written for the actual A83 factor and frozen A113 parameter ranges | **Still conditional:** the main analytic estimates are explicit theorem inputs |

All mathematical assumptions appear as binders or theorem premises.
The unconditional A113 theorem

```text
For every integer M>=521, every real s in [129/1000,133/1000],
and every integer contact 2<=k<=29, E_(M,k)(s)>0
```

**is not yet an output of Lean**. In particular, the current Lean file
does not prove the uniform ideal-core lower bound for all `2<=k<=29`,
does not define the actual frozen `D_M` and `H_r` channels with their
even/odd cases, and does not derive the `|E-E0|<20U` remainder bound.

## Independent cross-check, not a substitute for Lean

A fresh symbolic expansion using independent formal polynomial symbols
found the cofactor-to-ten-term difference to be identically zero. It
also checked the low-contact core factorizations for `k=1,2`.
The separately implemented standard-library Python exact checker
`tools/independent_a113_small_left.py` reproduced its 60 rational
controls and rational envelope threshold gates.

These support the implementation as secondary evidence; they cannot
establish a Lean kernel result, a bound for all real sources, or a
complete A113 theorem.

## Formal audit gates

1. Import the new module into the Lean project root.
2. Run the frozen Lean 4.33.1 and mathlib build.
3. Run the proof-placeholder gate.
4. Run `#print axioms` on the symbolic identity, core identity,
   rational margin and conditional transport theorem. Inspect any
   native evaluation or additional trust dependencies.
5. Run the module-specific `leanchecker` job, not merely `lake build`.
6. Review the exact CI revision and separately check root SHA-256
   inventories after bot-generated index commits.

The surrounding `audit/**` PR also contains an intentionally failing
historical ZIP integrity gate. Its red result must not be suppressed.

## Next unclosed mathematical tasks

First formalize the homogeneous-symmetric-polynomial core identity for
arbitrary `k>=1` and derive its uniform lower bound for `2<=k<=29`.
Next formalize the even/odd `D_M(r)` and opposite-sign tolerance
adjustments in `H_beta` and `H_s`. Prove the monotone dyadic and
high-power envelopes analytically, then the affine coefficient and
constant-channel bounds. Only then may the current conditional
transport theorem be instantiated with proved premises to certify the
unconditional small-left sign law in Lean.

Even a successful small-left Lean certificate would leave the
middle-left, remote-right, central nesting, full lifted-KKT, archive
recovery and novelty/prior-art audit tasks open.
