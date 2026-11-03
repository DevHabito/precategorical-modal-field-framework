# A113 normalized H-channel gap — universal interval proof candidate

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03  
**Initial status:** submitted to the pinned Lean 4.33.1 build and full checker; **do not call verified before CI**.

## Proposed result

For every integer `M>=521` and real `s in [129/1000,133/1000]`, with the **original** parity-specific H definitions, `U=2^(-floor(M/2))` and `beta=1/8`, prove

    43/10000 < [H_M(s,false)-H_M(beta,true)]/U < 7/500.

The two new theorem names are `a113Delta_uniform_interval` and `a113H_sourceBeta_gap_uniform_interval`. They do **not** take a bound on Delta as an assumption.

## Why the proof is not ad hoc

The source-to-conclusion dependency chain is explicit:

1. `A113DeltaPreliminaries.lean` supplies `d>=999/1000`, the tiny high-power cap and the exact H gap algebra.
2. `A113DeltaPowerGaps.lean` supplies nonnegative, at-most-`10^-6` normalized differences for `s^h-beta^h`, `s^(h+1)-beta^(h+1)`, and `s^M-beta^M`.
3. Existing `A113DefectEnvelopes.lean` proves `hU/d<=1/3`. The fact `h>=1` implies `0<=((h-1)U/d)<=1/3`.
4. `A113DeltaScalarBudgets.lean` proves the strict rational Delta interval **from** the exact stated scalar budgets, without assuming the interval in those lemmas.
5. `A113DeltaParityIdentities.lean` identifies those scalar expressions with the actual finite-M source/beta H gap, separately for even and odd M.
6. The new `A113DeltaUniform.lean` composes these conclusions over **all admissible M and real s**, with no sampled-grid extrapolation.

The independent `Fraction` error-budget regression, including a deliberately inadequate denominator bound and a deliberately inadequate power bound as negative controls, already passed in GitHub Actions [41724713362](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41724713362). These exact rational checks support the arithmetic choices but do not replace the proposed formal proof.

## Formal acceptance

The new module is imported into the library and added to the full now-35-module `leanchecker` matrix. `AssuranceA113DeltaUniform.lean` prints the transitive axioms of both theorems. Successful Lean compilation, a checker replay and an axiom report must be seen at the **exact code SHA** before promoting this note to “verified.” A failure is retained as evidence; no hypothesis will be added simply to close a tactic.

## Remaining scientific obligations

Even if Delta is formally bounded, that **does not** prove the sign of the central two-step factor `J=E_(b+1)-2E_(b+2)`. The exact central channel identity has already been checked, but the threshold contact `b`, transformed channel remainders and the remote/middle sectors need their own uniform proofs. The original damaged A112/A113/A114 archive containers and the larger physical interpretation remain outside this theorem.

Existing literature on Tchebycheff systems and moment spaces predates this work, including Samuel Karlin and William J. Studden (1966), *Tchebycheff Systems: With Applications in Analysis and Statistics*. Sources and caveats are already recorded in `consolidation/C3_A110_A114_ADVERSARIAL_CHECKPOINT_2026-10-19.md`. No novelty or physical-law claim is made here.
