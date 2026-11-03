# A113 central-pair identity — pinned Lean replay and finite Delta audit

**Research author:** Felipe Gianini Romero  
**Date:** 2026-11-03  
**Formal revision examined:** `5c40b71a514049d6719c3b7aeb09a8497ad147b7`  
**Lean:** [GitHub Actions run 41721969228](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41721969228), **SUCCESS**.  
**Exact Python:** [run 41721969226](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41721969226), **SUCCESS**; subsequent [run 41722823626](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41722823626), **SUCCESS** with additional finite Delta tests.

## Why I chose this step

The previously verified A113 small-left positivity result controls the finite-M factor only for `2<=k<=29`. The original A113 archive also claims signs for larger contacts and the central nesting inequality `J=E_(b+1)-2E_(b+2)>0`, where `b` depends on a logarithmic ceiling. Those more general sign claims were not established by the small-left proof.

I isolated a necessary **algebraic** identity before tackling another uniform analytic inequality. The central-pair expression in the historical certificate is prone to a misleading shortcut at the target node `tau=1/2`: the affine coefficient cancels there, but the linear coefficient does **not** disappear. The new formal module makes that surviving term explicit.

## Formal statements and evidence

The file `formal/lean/PrecategoryFormal/A113CentralPairIdentity.lean` defines **no new physical quantities** and proves three theorems:

1. `a113AffineDoubleStep`: the general two-step affine-power identity for arbitrary real coefficients and node, at every natural contact.
2. `a113HalfTargetAffineDoubleStep`: substitution `node=1/2` yields precisely the negative linear-coefficient term.
3. `a113ActualFactorCentralPair_eq_expansion`: the exact parity-sensitive `a113ActualFactor M k s - 2*a113ActualFactor M (k+1) s` equals the transformed seven-channel expansion, with the surviving negative target linear term and negative constant term. No positivity assumption is used.

I inspected the actual Actions log for exact code SHA `5c40b71a514049d6719c3b7aeb09a8497ad147b7`:

- the complete pinned Lean 4.33.1/mathlib build reported **8,737 jobs successful**;
- the proof-placeholder rejection gate passed;
- the axiom audit printed **exactly** `[propext, Classical.choice, Quot.sound]` for **all three** new statements;
- the full `leanchecker` loop emitted **30 named PASS lines**, including all 29 previously checked modules and `PrecategoryFormal.A113CentralPairIdentity`;
- the execution finished with overall `success`.

These statements depend on Lean's disclosed logical axioms but contain **no native-computation axiom in their printed transitive dependencies**. Other finite-enumeration theorems in the repository still have their separately documented `native_decide` dependencies. A full matrix pass does not change those older assurance labels.

## Independent symbolic implementation

`tools/research_2026_11_03/pmff_a113_central_pair_algebra.py` represents the seven channels by independent symbolic coefficients and k-th power variables. The k+1 powers are constructed by multiplication by their own bases. The script checks the complete expansion, the half-target cancellation, and a deliberate target-linear sign mutation. The exact Python workflow [41721969226](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41721969226) ran those gates successfully.

This is an independent algebraic representation of the formal identity, **not a second independent Lean kernel proof**.

## Next one-sided analytic bound: Delta

I separately reopened `A113FiniteChannels.lean` to inspect the odd/even defect formulas and the opposite beta/source epsilon adjustments. The historical central argument relies on

    Delta_M(s) = (H_M(s,false)-H_M(1/8,true)) / U_M

remaining strictly between `43/10000` and `7/500`. Its existing universal absolute H-error bound is insufficient by itself to establish this narrow positive difference.

The standalone source `tools/research_2026_11_03/pmff_a113_delta_channels.py` directly evaluates these original formulas with `Fraction`, verifies an independently expanded parity formula, checks the strict rational inequalities in **21 finite M/s cases**, and rejects a flipped tolerance-sign convention. I inspected the actual successful [CI run 41722823626](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41722823626) and its printed 21-case pass. Details and exact formulas are in [A113 delta channel audit](A113_DELTA_CHANNEL_AUDIT_2026-11-03.md).

**This Delta interval remains a conjectured universal analytic obligation here, not a Lean theorem.** A pointwise PASS, however exact, cannot prove all real s and all integer M.

## Open gates

- Derive in Lean uniform parity-sensitive upper and lower Delta bounds from actual finite-M functions, without introducing the desired inequality as an assumption.
- Verify the remaining middle-left and right-remote channel majorants and the central `J>0` inequality at the true logarithmic threshold `b`.
- Reconstruct the original A83 compressed-LP objective orientation independently wherever a global maximizer is asserted.
- Review the full A112/A114 lifted-KKT maps and their boundary cases independently.
- Keep the three historically invalid ZIPs, their original manifests, and the explicit red integrity gate unchanged.
- Perform independent theorem-by-theorem classical literature review before claiming novelty; the existing provenance list includes Samuel Karlin and William J. Studden (1966), *Tchebycheff Systems*, among other primary references.

**Status:** central-pair *algebraic bridge* is Lean verified and regression checked. Central *sign* and global A113 theorem are **not** verified. This is mathematical research only, not a physical or astrophysical theory validation.
