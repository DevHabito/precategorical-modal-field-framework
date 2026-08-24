# Reproducibility and Claim Boundaries

## Reproducibility layers

### Layer 1 — Stored-result integrity

`tools/verify_results.py` checks that every registered result file parses, all top-level gates are true, all verdicts begin with `PASS`, all expected figures exist, and all Python files compile.

### Layer 2 — Figure reconstruction

`tools/generate_english_figures.py` reconstructs the legacy generated English figures from the JSON result records.

### Layer 3 — Audit replay

`tools/materialize_runtime.py` reconstructs the original flat working directory. `tools/run_all_audits.py` executes a chosen audit interval and stores logs.

### Layer 4 — Independent mathematical inspection

Every result JSON includes the audit contract, gates, verdict, and boundaries. Exact audits record rational values, polynomial identities, roots or isolating intervals, phase structures, or primal–dual certificates as applicable.

## Interpretation of a PASS verdict

A PASS verdict means that all encoded gates passed for the declared audit contract. It is not a peer-review decision and is not evidence outside that contract.

## Known non-universal results

The repository deliberately preserves the following negative or limiting results:

- finite observations do not generally identify an omitted transform when the hidden distribution has enough degrees of freedom;
- the far/compactified third anchor is contract-dependent outside the original six-state example;
- the boundary pair need not be unique because exact ties exist;
- order-only total positivity does not determine the coupled Cramer numerator sign;
- individual q-Schur positivity does not remove cancellation in the full numerator;
- a fixed active signature changes orientation between M=9 and M=10;
- the M=10 optimizer changes active set rather than continuing the invalid signature;
- the adjacent contact family is not universally persistent even at the A78 rational probe: gamma-inactive compression is selected at M=40,57,74;
- A78 is exact only at one rational probe and only for M=10,...,80;
- A79 upgrades only the three A78 compression supports to exact local algebraic intervals and does not establish an all-M compression law.

## Statistical limitation

A62's inflation factors are empirical and model-conditional. They are not universal finite-sample confidence constants. Heavy-tailed data reduce contract availability even after calibrated coverage improves.

## Physical limitation

The programme is informational/mathematical. It does not assign a physical metric, spacetime interpretation, measurement kernel, or physical unit to the transform parameters.
- A80 proves a finite local atlas only for A78-selected contacts, `10<=M<=80`, and `129/1000<=s<=133/1000`; it does not establish an all-M recurrence or a physical compression law.

- A81 derives exact reduced boundary formulas, but its positivity theorem is finite to `10<=M<=80`, `2<=k<floor(M/2)`, and `129/1000<=s<=133/1000`; it does not select `k(M)` for arbitrary support size.
- A82 proves a strict adjacent-contact locator only at `s=131/1000` for `10<=M<=80`. Its two local roots are certified inside isolating brackets, but same endpoint signs are not treated as a complete root-free certificate. The algebraic compressed maximizer also has eight exact primal-feasibility exceptions, so the predicted full branch still requires a KKT check.

## A84 exact finite stress

A84 uses exact Python `Fraction` arithmetic at three rational probes for `10 <= M <= 300`, plus one generic SymPy identity check. Endpoint disagreements are not promoted to a complete root atlas. See `REPRODUCIBILITY_A84.md`.
## A85 dominant-balance and asymptotic localization

A85 combines exact rational transition-bracket comparisons with an analytic parity expansion. The four-term dominance statement is exact only at the two factors bracketing each A84 maximizer, and it has an explicit small-support counterexample at `M=12`. The parity-offset `within one contact` check uses high-precision logarithms and is classified as numerical. See `REPRODUCIBILITY_A85.md`.


## A86 exact rational contact strip

A86 does not use floating-point logarithms in theorem gates. Every comparison with `c(s)=log(2)/(-2 log(s))` is reduced to the exact integer comparison `2^q s^(2p)` versus `1`. The finite three-contact strip is restricted to the A84 support/probe contract and depends on A84's exact one-sign-variation result. See `REPRODUCIBILITY_A86.md`.

## A87 exact secant-residual classifier

A87 uses exact rational arithmetic for the full, four-term, and eight-term local secant residuals. The theorem is finite to the A84/A86 contract. Local positivity of `E_b-E_{b+1}` is not promoted to global monotonicity; the complete finite census explicitly contains 40,483 negative global drops. See `REPRODUCIBILITY_A87.md`.



## A88 exact nine-term secant reduction

A88 derives the exact nine-term transform of the A87 local secant, checks 8,019 exact cells through `M=900` on nine rational probes, and certifies strict four-term-core dominance. The parity-phase leading-limit margins are exact rational lower bounds, but no explicit uniform finite remainder threshold is claimed. See `REPRODUCIBILITY_A88.md`.

## A93 exact continuum full-sequence one-variation

A93 reuses the committed A92 algebraic cell/root certificate and recomputes all 5,426 non-decisive adjacent factors using exact `Fraction` arithmetic. Every sign closes on a rational outer hull without subdivision. The theorem is restricted to the twenty-five A92 selected cells and does not certify the other 833 cells, supports above `M=520`, lifted KKT feasibility, or physical interpretation. See `REPRODUCIBILITY_A93.md`.

## A94 exact continuum all-cell one-variation

A94 reuses the committed A92 algebraic-cell certificate and reconstructs every non-decisive adjacent factor with exact rational arithmetic. Direct outer-hull enclosures settle 119,984 factors; adaptive interval and derivative/convexity certificates settle the remaining 4,972. The theorem is restricted to the 858 A92 cells and the compressed objective. See `REPRODUCIBILITY_A94.md`.

## A96 exact unrestricted full-LP resolution

A96 uses a high-precision simplex run only for active-set discovery. The theorem audit independently reconstructs the candidate in SymPy exact rational arithmetic and checks all 246 nonbasic atom reduced costs, all inactive observation slacks, exact primal feasibility, and exact primal–dual equality. See `REPRODUCIBILITY_A96.md`.
## A97 endpoint-released interval and obstruction atlas

A97 separates the symbolic M=125 interval certificate from the 83-witness exact KKT atlas to avoid retaining both large exact-arithmetic workloads in one process. Both phases are deterministic and seed-free. The final assembly checks the committed phase outputs and reproduces 19/19 gates. See `REPRODUCIBILITY_A97.md` and `RUNBOOK_A97.md`.

## A101 exact gamma-active interval and residual closure

A101 uses an exact Sherman–Morrison rank-one row update because only the active alpha row depends on `s`. The M443 theorem certifies one seven-term common denominator, two simple algebraic boundary roots, and 893 nonboundary condition numerators by integer-only interval arithmetic. The M449, M484, and M490 certificates use exact rational matrix inversion and complete unused-atom reduced-cost checks. The 83-witness closure is pointwise and is not promoted to a continuum lifted-KKT theorem. See `REPRODUCIBILITY_A101.md`.
## A102 complete exact rational-witness lift atlas

A102 is a finite database-closure theorem. It freezes the 1,063 A95 phase-segment keys, validates one exact source KKT certificate per key, pins 18 source inputs by SHA-256, and independently replays all 83 post-A95 resolutions plus a deterministic stratified sample of 100 natural lifts. The complete source census contains 676,847 exact KKT conditions. The result is pointwise and is not promoted to a continuum lifted-KKT theorem. See `REPRODUCIBILITY_A102.md`.
## A103 exact endpoint-released continuum segment atlas

A103 uses an exact Sherman–Morrison rank-one alpha-row update around `s=1/8` to represent every KKT quantity for the 76 endpoint-released witnesses as a sparse rational function of `s`. It certifies 55,020 oriented numerator/denominator sign obligations, isolates 55 locally unique simple algebraic boundaries, and records exact negative outside counterexamples. The theorem concerns the A95 rational inner source segments only: 25 are covered completely and 51 contain proper strict components. It is not an all-cell or all-witness continuum theorem. See `REPRODUCIBILITY_A103.md`.
## A104 exact exceptional q0/q1 continuum segment atlas

A104 uses exact Sherman–Morrison alpha-row updates for the three gamma-inactive and four gamma-minus-active q0/q1 architectures. It certifies 6,496 oriented numerator/denominator sign obligations, isolates 25 sign-changing candidate roots, and proves by exact rational bracket inequalities which 14 roots are nearest to the seven witnesses. Every selected boundary has a derivative-certified simple isolating bracket, every nonselected KKT condition stays positive on the complete boundary hull, and exact negative rational counterexamples are stored beyond both boundaries of every component. The theorem concerns only the seven A95 rational source segments routed to exceptional architectures by A102. See `REPRODUCIBILITY_A104.md`.


## A105

A105 stores forty memory-isolated exact rational-function KKT records. Every selected root is locally simple, all competing brackets are ordered by exact rational inequalities, and every boundary has an exact negative outside counterexample. See `REPRODUCIBILITY_A105.md`.


## A106

A106 stores eighteen exact legacy gamma-minus rational-function KKT records. It adds an independent direct matrix inversion regression for every one of the 2,410 witness conditions, exact root ordering, complete hull certification, and exact negative outside counterexamples. See `REPRODUCIBILITY_A106.md`.
