# A113 small-left — pinned Lean proof and independent checks

**Research author:** Felipe Gianini Romero  
**Date of verification:** 2026-11-03  
**Mathematical scope:** frozen A113 small-left sector only  
**Lean source revision checked:** `368c8c3dbb8bf7e870fade556ccdb348fdf9c8e1`  
**Lean execution:** [GitHub Actions 41718046660](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41718046660), attempt 1, **SUCCESS**.

## Why this checkpoint matters

I returned to the last unproved implication in the isolated A113 small-left chain. Earlier Lean modules established the exact coefficient identity, finite-size envelopes, and a positive lower bound on the ideal factor. The remaining task was to combine those results without taking the desired remainder inequality as a hypothesis.

That task is now formally completed for the domain below. I keep the first failed build, its one-line correction, the later successful run, the exact arithmetic tests, and the remaining limitations separate. None of these results is an argument about physical spacetime.

## Precise statements

The frozen source contract is:

- natural `size = M >= 521`;
- natural `2 <= k <= 29`;
- real `129/1000 <= source = s <= 133/1000`;
- `beta = 1/8`, `tau = 1/2`;
- `U_M = (1/2)^(floor(M/2))`, with the historical parity-sensitive H-channel definitions.

The new imported Lean module is `formal/lean/PrecategoryFormal/A113SmallLeftClosure.lean`. The source definitions of `a113ActualFactor` and `contactIdealCore` come from the previously audited A113 modules; they were not replaced by favorable stand-ins.

The new theorem

`PrecategoryFormal.a113ActualFactor_abs_error_lt_twenty_units`

proves, at that domain:

```text
|a113ActualFactor M k s - contactIdealCore k (1/8) (1/2) s|
  < 20 * a113Unit M.
```

The new theorem

`PrecategoryFormal.a113ActualFactor_smallLeft_pos`

proves:

```text
0 < a113ActualFactor M k s.
```

These are statements for every admissible integer M/k and every real s in the stated closed interval, **not** extrapolations from finite sample points. The mathematical mechanism is the seven-term exact A84 difference decomposition, the already proved channel and coefficient bounds, and the strict rational comparison:

```text
|E-F| < (18 + (9*k + 6)/M)*U
      <= (18 + 267/521)*U
       = (9645/521)*U
       < 20*U.
```

The existing uniform ideal-core lower bound exceeds `20*2^(-260)`, and the finite-M unit satisfies `U <= 2^(-260)`; hence the actual factor is positive.

## Failed attempt and minimal repair

The first exact source run [41714981951](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41714981951) concluded **FAILURE** in `lake build`:

```text
PrecategoryFormal/A113SmallLeftClosure.lean:198:10:
No goals to be solved
```

The source had a redundant `rfl` after a `rw` that had already closed the equality. The correction removed only that single line; no mathematical definition, theorem statement, assumption, constant, or upstream lemma changed. The original failure remains recorded at `consolidation/A113_LEAN_FIRST_BUILD_FAILURE_2026-11-03.md`. The failed run did not reach the axiom or checker stages.

## Observed formal verification

I inspected the completed job and its raw GitHub Actions log for [run 41718046660](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41718046660). At exact revision `368c8c3dbb8bf7e870fade556ccdb348fdf9c8e1`:

- pinned Lean `v4.33.1` and the committed mathlib manifest were used;
- the forbidden `sorry`/`admit` check passed;
- `lake build` reported **8,736 jobs built successfully**;
- `lake env lean AssuranceA113SmallLeftClosure.lean` completed;
- `lake env leanchecker PrecategoryFormal.A113SmallLeftClosure` completed successfully.

The printed transitive axioms for **both** newly proved theorems are exactly:

```text
[propext, Classical.choice, Quot.sound]
```

The output did **not** list native-computation axioms or `sorryAx` for either theorem. This does not erase the separately documented native-evaluation trust dependencies of some *other* finite-count theorems in the repository. The established Lean logical axioms remain disclosed, and proof-checker success does not establish originality, empirical content, or soundness of an external interpretation.

A source-level scan of the eleven direct A113-module files in the imported chain found no active declarations of new axioms, `sorry`, `admit`, `native_decide`, `unsafe`, or `opaque`. This supplementary textual inspection is not a replacement for the actual transitive axiom report.

## Exact Python regression and CI

I reran the three previously saved scripts locally under Python 3.13.5 and SymPy 1.14.0. Each completed without assertion failure. They check the F3 rational witness, A83/A84 symbolic identity, controlled sign mutation, selected exact rational envelopes, and all 28 integer contacts on a four-M/three-source grid.

A separate [GitHub Actions run 41718919204](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41718919204) concluded **SUCCESS** using Python 3.13.16 and SymPy 1.14.0. Its raw log records successful symbolic, negative-control, 60-case, and **336-case** rational checks. The 60 configurations are a subset of the 336 configurations, and the extended script reuses local functions; these are not 396 independent samples or a universal proof.

## Integrity status

The root tracked-file SHA-256 inventory was regenerated and checked by [run 41719565391](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41719565391), which reported **3,623 tracked regular files**, a successful manifest check and a passing repository validator. The bot committed only `MANIFEST.csv` and `SHA256SUMS.txt` at `bb122901b1b2ccfce9a4d016b66af42c323c747e`.

These indexes describe stored bytes; they do **not** establish that the three previously reported malformed historical ZIP archives are valid. That independent integrity finding stays unresolved. New documentation and workflow files added after the index commit require another root-index refresh before merge.

## What remains open

1. Run the **entire** established Lean module-checker suite after including the new module. The successful root `lake build` and the new module's checker do not substitute for that separate regression.
2. Conduct independent human review of the A83/A84 mathematical definitions and the proof of every imported analytic bound, including the parity-specific signs.
3. Address the middle-left, remote-right and central portions of A113 individually; small-left positivity is not a global compressed one-variation theorem.
4. Keep A112-G, A112-B, lifted A114/KKT status, and historical reproducibility defects within their independently documented boundaries.
5. Refresh the exact final branch's root indexes and preserve archived failure evidence.
6. Perform theorem-by-theorem literature/priority review before claiming novelty. Relevant background sources and their verified bibliographic metadata are in `docs/novelty/VERIFIED_CONTEXT_2026-11-03.md`.
7. Do not infer physical time, distance, matter, gravitation or astrophysical predictions from a finite-dimensional mathematical statement.

**Status statement:** the two scoped A113 small-left theorems passed pinned Lean build, selected transitive-axiom inspection and dedicated `leanchecker`. Independent full-matrix regression and external scientific review remain open. The larger A113 programme is not complete.
