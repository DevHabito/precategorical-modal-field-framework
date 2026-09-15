# Consolidation 1.0 — canonical start page

**Status:** active repository reorganization; no mathematical claim is strengthened by this editorial layer.

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
