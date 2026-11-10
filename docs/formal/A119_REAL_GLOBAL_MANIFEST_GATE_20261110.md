# A119: full real-parameter cell coverage — formal checkpoint

**Date:** 10 November 2026  
**Branch:** `research/a115-a119-uniform-remainder-20261110`  
**Mathematical object:** the explicit A119 critical-substitution rational expression for the reduced C2(k) family. This is *not* a theorem about the unrestricted F2/F3 optimum.

## Confirmed evidence

The rational-endpoint inclusion interpreter has a kernel-checked real-input soundness theorem in `A119RealIntervalEvaluator`. The exact expression tree is algebraically identified with `criticalXiHatReal` in `A119RealCritical`. All 35 explicit real-parameter box corollaries passed their individual `leanchecker` job in [run 42891947892](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42891947892), which finished **43/43 SUCCESS**. The corollaries are valid for *all real points in each closed box*. No floating-point interpolation or inference from density of rationals is involved.

A pilot in `PrecategoryFormal.A119RealManifest` implements elementary two-part and three-part closed-interval coverage over `Real` and uses existing box certificates to prove the entire even r=4 interval and the unsplit even r=8 interval. Its dedicated individual checker in [run 42908750117](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42908750117) completed with **SUCCESS**. This is a narrower fact than approval of the subsequent full manifest.

## Submitted finite-manifest theorem

`PrecategoryFormal.A119RealFullCells` contains 25 real-parameter full-cell theorems:

- even deficits r=4,...,12 (9 cells);
- odd deficits r=4,...,19 (16 cells).

For each such cell and the source window s in [129/1000,133/1000], the target enlarged alpha interval is

  [2(r+sigma), 21(r+1+sigma)/10],

with sigma=0 (even) or 1/2 (odd). The r=4 cells are covered by three closed subintervals, the r=5,6,7 cells by two closed halves, and the rest by a single complete box. Shared endpoints are explicitly retained.

`PrecategoryFormal.A119GlobalRealManifest` states one universally quantified result:

  if (parity=even and 4<=r<=12) or (parity=odd and 4<=r<=19),
  and s,alpha lie in the frozen source and enlarged critical cell,
  then criticalXiHatReal(s,alpha,parity,r)>0.

This is a **finite-contact** theorem. It does *not* establish that every actual critical point must have one of these 25 deficit/parity combinations. That separate A117/A119 large-deficit cutoff still requires formalization. The new modules also do not identify Xi-hat with the source-derived A118 second-order coefficient.

At the time of this note, the modules above were **submitted for Lean compilation and kernel replay**, not yet claimed successful. The relevant CI is [full-cell run 42909372248](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42909372248) and [single-manifest run 42909538752](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42909538752). Only promote these to PASS after verifying the specific module jobs at the exact source SHA. The new source is on the research branch; `main` is unchanged.

## Exact scientific boundary

This advances the rigor of a *particular rational sign certificate*. It is not a new universal law, a physical model, or a proof of a global moment-LP optimum. The unresolved source-to-coefficient derivation (A115–A118), uniform remainder bounds, and full-text prior-art comparison remain independent obligations. Do not present the interval certificate as a substitute for those arguments.

The current independent algebraic cross-check `a115_a119_independent_symbolic_bridge_2026-11-10.py`, executed in a standard Python/SymPy environment on 10 November 2026, again reported PASS for the Cramer's-rule adjacent-objective identity and for the even/odd source-to-published-A118 coefficient identities. This is **symbolic supporting evidence**, not a Lean kernel proof and not a bound for every omitted exponentially small remainder.

## Evidence-status ledger

- 35/35 rational box checks (Lean): PASS in earlier CI.
- 35/35 real box corollaries (Lean): PASS, 43/43 full workflow.
- Real two/three-way coverage pilot (Lean): PASS, dedicated module job.
- All 25 full real cells (Lean): PENDING CI.
- Single universally quantified real finite-manifest theorem (Lean): PENDING CI.
- Real-A118 critical substitution identity from an independently derived coefficient: NOT YET PROVED.
- Uniform A115–A118 finite-M error bounds and F3 global optimization: NOT PROVED.
- Historical originality: NOT CERTIFIED.
