# A113 Delta — parity identity candidates

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03  
**Status:** submitted for exact-head Lean compilation and proof checking; no success presumed.

The historical A113 gap is

    Delta(M,s) = (H_M(s,false)-H_M(1/8,true))/U_M.

The two strict scalar interval lemmas introduced in `A113DeltaScalarBudgets.lean` are valid only when their symbols represent the **actual** finite-M H channel terms, not arbitrary favorable substitutes. I have therefore introduced transparent helper definitions in `A113DeltaParityIdentities.lean` for the normalized full power `P`, half power `Q`, next-half power `R`, and coefficients `X=hU/d`, `Y=(h-1)U/d`.

The proposed theorems `a113Delta_even_formula` and `a113Delta_odd_formula` expand the original parity-dependent defect definitions **exactly**. Both preserve the source/beta sign orientation and the negative four-epsilon contribution. Their targets are identities for all real sources, at their respective parities, under `M>=521`. Neither theorem assumes or concludes any sign.

The Python regression independently checked these identities at 21 exact rational points (both parities and both source endpoints), but that alone is not evidence that the proposed Lean code elaborates. The new module requires the pinned Lean 4.33.1 full build, transitive axiom output and a now-34-module `leanchecker` replay.

The next separate obligation, **only after these identities are certified**, is to combine them with the source-to-PQR uniform bounds and the two scalar interval lemmas to produce the desired unconditioned (with respect to Delta) interval:

    43/10000 < Delta(M,s) < 7/500

for every `M>=521` and every real `s in [129/1000,133/1000]`. Even a successful Delta theorem would not by itself prove `J>0`, all-tail A113 one-variation, lifted KKT optimality, or physical claims.

The classical literature relevant to related moment-system and extended-Chebyshev arguments remains documented with author dates and source references in `consolidation/C3_A110_A114_ADVERSARIAL_CHECKPOINT_2026-10-19.md`. The present identities are elementary algebra, not an originality assertion.
