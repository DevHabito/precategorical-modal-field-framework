# A113 Delta power gaps — Lean failure and exact rewrite repair

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03

## First observed failure

The proposed `A113DeltaPowerGaps.lean` module failed in [GitHub Actions 41725088460](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41725088460) at the pinned Lean 4.33.1 `lake build` step. The full-matrix run [41725088517](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41725088517) also failed in the build. Neither run reached successful axiom or checker verification for the new module.

The first job's exact source diagnostic was:

```text
PrecategoryFormal/A113DeltaPowerGaps.lean:45:48: unsolved goals
```

The proof attempted to change `node^size` to a product via `rw [hsplit,pow_add]` for `size=h+(size-h)`. Lean's unrestricted rewriting also changed nested occurrences of `size` within `a113HalfIndex size` on the right-hand side, producing a needlessly expanded, nonmatching term.

## Smallest repair

I separated the step into:

1. `congrArg (fun exponent : ℕ => node ^ exponent) hsplit`, establishing only the desired power equality;
2. `rw [pow_add]`, distributing the fixed sum on the next line.

No mathematical hypotheses, constants, domain, target inequality or upstream theorem was changed. This is a proof-script elaboration repair, not a redefinition. The first failed CI run remains recorded as **FAIL**.

## Next acceptance requirement

A new exact-head pinned Lean build, transitive `#print axioms` output for the five power-gap theorems, and dedicated/full `leanchecker` replay must pass before these statements are promoted. The strict universal Delta interval and central `J>0` remain unproved irrespective of whether this repair compiles.
