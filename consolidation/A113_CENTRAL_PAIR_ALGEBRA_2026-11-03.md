# A113 central-pair algebra: a new proof obligation

**Research author:** Felipe Gianini Romero
**Date:** 2026-11-03
**Status at proposal:** symbolic identity independently checked; new Lean source committed for CI, **not reported as checked until its own logs are inspected**.

## Where the work stands

The pinned [full-matrix Lean run 41720383464](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41720383464) passed the prior 29-module suite, including the new small-left result. Its log explicitly contains 29 individual `PASS PrecategoryFormal.*` lines, and the earlier finite-count `native_decide` dependencies remain visible in the complete axiom trace. The check was made at source commit `716cc322fb36af6cdb72072eb7bf3c9f6a782bb3`; successful CI at that commit does not automatically certify subsequent changes.

The next A113 mathematical obligation is not another small-left proof. The historical recovered source claims that the **central combination**

    J_(M,k)(s) = E_(M,k)(s) - 2 E_(M,k+1)(s)

is strictly positive at `k=b(M,s)+1`, with `b` defined by a logarithmic ceiling. The full inequality is not yet independently proven or formalized in this research branch. The original recovered certificate's 23 arithmetic/symbolic gates are reproducible but do not supply all continuous, uniform A83/A84 majorant-to-factor arguments. See `consolidation/A113_RECOVERED_CERTIFICATE_AND_CONTACT_ENVELOPES_2026-10-19.md` and `consolidation/C3_A110_A114_ADVERSARIAL_CHECKPOINT_2026-10-19.md`.

## First bridge: exact algebra, not a sign proof

I isolated a structural fact that the central argument needs. For an arbitrary real node `r`, real coefficients `c,d`, and natural index `k`,

    (c+kd)r^k - 2(c+(k+1)d)r^(k+1)
      = ((1-2r)(c+kd) - 2rd)r^k.

This is a polynomial identity once `r^(k+1)=r*r^k` is substituted. At the fixed target node `r=1/2`, the entire affine coefficient `c` cancels exactly:

    (c+kd)(1/2)^k - 2(c+(k+1)d)(1/2)^(k+1)
      = -d(1/2)^k.

Using `a113ActualFactor_eq_namedCoefficients`, the new Lean candidate `formal/lean/PrecategoryFormal/A113CentralPairIdentity.lean` expands the **actual finite-M** central combination into:

- three product channels multiplied by `1-2*node_product`;
- one beta affine-linear channel;
- one source affine-linear channel;
- the surviving negative target linear term `-d_target*(1/2)^k`;
- the negative constant channel.

This is the same exact parity-dependent `a113ActualFactor` as in the previous small-left proof; I did not introduce a favorable substitute or assume `J>0`. There are no parameter restrictions in the identity itself. The theorem must compile with the existing definitions; if it fails, the exact diagnostic is evidence.

## Independent symbolic check

`tools/research_2026_11_03/pmff_a113_central_pair_algebra.py` constructs the two adjacent seven-channel expansions independently with separate symbolic placeholders for all powers `r^k`. It replaces each `r^(k+1)` by `r*r^k`, subtracts the proposed transformed expression, and checks that the remainder is identically zero. It also checks the target-node affine cancellation and a deliberately altered-sign negative control. This algebraic test does not evaluate A113's analytic inequalities or prove a uniform positive sign.

## Formal acceptance gates

1. Compile the new module with pinned Lean 4.33.1 and the existing exact mathlib manifest.
2. Print axioms for all three named identity theorems and inspect transitive native axioms separately from `propext`, `Classical.choice`, and `Quot.sound`.
3. Replay the module with `leanchecker`, then replay all previously declared 29 modules (now a 30-module matrix).
4. Run the independent symbolic regression under pinned Python 3.13/SymPy 1.14.0.
5. Preserve every failure and do not move the new bridge into a “verified” category until the exact-head CI is green.

## What this does **not** establish

- It does **not** prove `J_(M,b+1)(s)>0`, or even a sign for arbitrary `J_(M,k)(s)`.
- It does **not** define or formalize the logarithmic contact threshold `b(M,s)`.
- It does **not** establish the remote-left, remote-right or global one-variation theorem.
- It does **not** repair the three malformed historical ZIP archives, clear all KKT cases, or establish any physical or astrophysical prediction.

**Next hard proof:** derive uniform bounds for the transformed seven-channel expression, including the target linear term and the parity-sensitive source/beta deviations, then formally connect those estimates to the exact ceiling threshold. A small finite sampling grid cannot replace this step.

## Existing mathematical literature

The zero-count and sign-variation tools used elsewhere in the A112–A114 programme are not new in general: Samuel Karlin and William J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics* (Interscience, 1966), precede this work. The project documents that bibliographic context in `consolidation/C3_A110_A114_ADVERSARIAL_CHECKPOINT_2026-10-19.md`. This particular adjacent-factor algebraic identity is elementary; I make no priority or novelty claim for it.
