# Consolidation 1.0 — canonical start page

**Status:** active repository reorganization; no mathematical claim is strengthened by this editorial layer.

**Literature scope check:** [Verified classical precedents and unresolved priority questions](../docs/novelty/CONSOLIDATION_CLASSICAL_LITERATURE_2026-10-19.md).

**A113 recovered primary source:** [23 exact checks replayed from CRC-verified original code, independent parity contact-envelope proof, and open universal majorant audit](A113_RECOVERED_CERTIFICATE_AND_CONTACT_ENVELOPES_2026-10-19.md).

**A113 independent small-left theorem:** [uniform rational proof for every M>=521, every source in the frozen interval and 2<=k<=29; middle/right/central sectors remain open](A113_SMALL_LEFT_UNIFORM_PROOF_2026-10-19.md).

**A113 finite A84 coefficient bounds (2026-10-20):** [formally certified beta/source/target affine and linear coefficients, constant channel and exact-coefficient identity pending isolated replay](A113_A84_COEFFICIENT_ENVELOPES_2026-10-20.md). The full A113 E-F remainder remains open.

**A113 bilinear coefficient checkpoint (2026-10-20):** [three actual A84 channel products with 3U/M caps, pinned Lean build/axiom trace and isolated checker PASS, independent exact regressions](A113_BILINEAR_COEFFICIENT_CHECKPOINT_2026-10-20.md). The global finite-M E-F error remains open.

**A113 target and moment slopes (2026-10-20):** [finite-M mass correction, nonnegative moment slopes, exact unit-over-M error, pinned Lean 26/26 including isolated leanchecker, plus independent Fraction replay](A113_TARGET_AND_MOMENT_ENVELOPES_2026-10-20.md).

**A113 kernel-checked H envelopes (2026-10-20):** [both plus/minus tolerance bounds, uniform beta/source theorems, pinned Lean axiom audit and isolated leanchecker pass](A113_H_ENVELOPES_FORMAL_CHECKPOINT_2026-10-20.md). The full finite-M E error remains open.

**A113 formal defect bound (2026-10-20):** [Lean proof of `|D_M(r)|<U_M/2` for all M>=521 and 0<=r<=1/6, with even/odd checker replay; H and full E error remain open](A113_DEFECT_SIGNS_FORMAL_CHECKPOINT_2026-10-20.md). [Earlier analytic derivation](A113_DEFECT_ENVELOPE_DERIVATION_2026-10-20.md).

**A113 finite parity channels (2026-10-20):** [exact even/odd D and opposite-sign H definitions, formal dyadic and denominator bounds, finite-error obligation still open](A113_FINITE_CHANNELS_LEAN_CHECKPOINT_2026-10-20.md).

**A113 new all-contact ideal-core bound (2026-10-20):** [exact recurrence, universally quantified Lean lower bound, independent rational regression, and explicitly open finite-M error analysis](A113_IDEAL_CORE_RECURRENCE_2026-10-20.md).

**A113 Lean 4 checkpoint:** [formal A83/A84 algebraic identity and explicit conditional positivity transport; all-k analytic envelopes remain to be formalized](A113_LEAN_FORMALIZATION_CHECKPOINT_2026-10-19.md).

**Critical reproducibility blocker:** [Three invalid historical ZIPs, three dated checksum mismatches, and the guarded recovery protocol](HISTORICAL_ZIP_INTEGRITY_FINDING_2026-10-19.md).

**A112 determinant and Q-ECT reviews:** [independent Schur orientation](C3_A112_DETERMINANT_REDERIVATION_2026-10-19.md) and [multiplicity-aware Q reduced-cost zero budget](C3_A112_Q_REDUCED_COST_ZERO_BUDGET_2026-10-19.md).

**C3 analytic-tail review:** [Frozen A110–A114 theorem scopes, exact counterexamples, independent LP oracle, open proof gates](C3_A110_A114_ADVERSARIAL_CHECKPOINT_2026-10-19.md).

**F3/MF-R049 formal proof:** [exact rational counterexample, centered exponential transport, and proof scope](F3_RATIONAL_NONCLOSURE_2026-10-19.md).

**Lean axiom trace:** [actual theorem-level dependencies from CI](LEAN_AXIOM_DEPENDENCIES_2026-10-19.md).

**Assurance checkpoint (2026-10-19):** [trust boundaries, independently reproduced finite claims, and stale SHA-256 indexes](ASSURANCE_CHECKPOINT_2026-10-19.md). This is a partial audit, not a completed independent peer review or a release certificate.

The purpose of Consolidation 1.0 is to make the project readable, independently checkable, and resistant to common-mode errors. The historical A-number sequence remains preserved as provenance, but it is no longer the preferred way to navigate the mathematics.

## Three strictly separated layers

### 1. Mathematical core

This layer contains only definitions, propositions, theorems, exact counterexamples, and explicitly scoped computational certificates. A statement belongs here only if its hypotheses and conclusion can be written without physical or ontological interpretation.

### 2. Verification and reproducibility

This layer contains executable audits, exact enumeration, Fraction/SymPy/interval certificates, regression tests, and future proof-assistant formalizations. A computational test is never promoted to a theorem merely because it passes.

### 3. Interpretation and historical programme

RZS, Modal Field language, physical motivation, speculative bridges, failed routes, and chronological A-number development belong here. They may motivate mathematics but are not premises of the mathematical core unless independently formalized.

## Canonical result groups under consolidation

The current cleanup reduces the public-facing mathematical programme to five candidate result groups:

1. **Finite combinatorics and encoding correction** — MF-R008/MF-R009/MF-R011.
2. **Exact dynamic non-closure** — MF-R049 and its explicit witness.
3. **Frozen exponential-moment optimization** — A112/A113, with A114 retained separately until its governance/audit status is normalized.
4. **Target-deformed central nesting and boundary layer** — A115–A119, to be rewritten as one self-contained theorem package.
5. **Fixed-interior rounding-phase staircase and resonance** — A120–A122, to be rewritten as one self-contained theorem package.

These groups are editorial targets, not novelty claims. Their novelty/priority status remains conservative until dedicated literature review is complete.

## Stop rule

No A123/A124/... research package should be added during Consolidation 1.0 unless it is required to repair a contradiction discovered during consolidation.

The work now is:

- minimize hypotheses;
- rewrite the strongest results self-containedly;
- trace every theorem to independent executable evidence where available;
- formalize selected claims in Lean 4;
- separate historical/speculative material from mathematical premises;
- prepare short external-review units instead of asking anyone to review the full archive.

## Navigation

- [`CORE_RESULTS_MAP.md`](CORE_RESULTS_MAP.md) — the reduced set of mathematical claims worth carrying forward.
- [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md) — status, evidence, open obligations, and forbidden overclaims.
- [`FORMALIZATION_PLAN.md`](FORMALIZATION_PLAN.md) — Lean 4 roadmap.
- [`INDEPENDENT_VERIFICATION_PROTOCOL.md`](INDEPENDENT_VERIFICATION_PROTOCOL.md) — blind rederivation, independent implementations, proof-kernel and external-check ladder.
- [`ARCHIVE_PLAN.md`](ARCHIVE_PLAN.md) — non-destructive migration from cumulative A39-* directories to tagged historical releases.

## Epistemic rule

A theorem proved from assumptions `H` establishes only `H -> conclusion`. It does not establish that nature satisfies `H`. Physical interpretation requires a separate operational and empirical bridge.
