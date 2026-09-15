# Consolidation 1.0 — canonical claim ledger

This ledger is the public-facing status table for claims selected for consolidation. Historical A-number packages remain the source of provenance and detailed derivations.

| Core ID | Claim family | Current status | Evidence class | Formalization target | Literature status | Main unresolved obligation |
|---|---|---|---|---|---|---|
| C1.1 | Minimum-representative quotient-poset count | PROVED | combinatorial proof + exact enumeration | Lean candidate 1 | novelty not certified | reconstruct minimal definitions and bijection in Lean |
| C1.2 | Non-injectivity of representative code | PROVED; ENCODING-LEVEL LEAN PILOT PASS | constructive counterexample + Lean kernel/leanchecker | graph-to-SCC bridge remains | novelty not material | formalize directed reachability/SCCs for the two explicit graph witnesses and derive the checked block maps |
| C1.3 | `P5=75/256` edge-toggle sensitivity | EXACT FINITE RESULT | exhaustive enumeration | Lean/native_decide candidate | apparently unreported; not certified | independent formal finite computation and OEIS/literature check |
| C2 | Fixed-score dynamic non-closure | PROVED | exact identity + four-point counterexample | Lean candidate 2 | novelty not certified | self-contained theorem independent of framework terminology |
| C3.1 | Frozen tail structural theorem | PROVED | analytic proof | later Lean/Isabelle candidate | novelty not certified | extract assumptions and remove historical dependencies |
| C3.2 | Frozen compressed one-variation | PROVED | analytic proof + exact regression | later formalization | novelty not certified | rewrite as standalone exponential-moment theorem |
| C3.3 | Lifted active-set selection | PROVED WITH GOVERNANCE CLEANUP REQUIRED | KKT/determinant proof + adversarial audits | defer | novelty not certified | normalize theorem headers and red-team/governance status before promotion |
| C4 | Target-deformed central nesting/boundary layer | PROVED WITH SCOPED COMPUTER-ASSISTED COMPONENTS | analytic proofs + exact counterexamples + interval certificates | defer until compressed | novelty not certified | compress A115–A119 into one theorem chain and independently rederive |
| C5 | Fixed-interior rounding staircase/resonance | PROVED WITH SCOPED COMPUTER-ASSISTED COMPONENTS | analytic proofs + exact hardening + interval certificate | defer until compressed | novelty not certified | compress A120–A122; isolate arithmetic realization question |

## Allowed evidence labels

- **PROVED** — deductive proof under explicit assumptions.
- **EXACT FINITE RESULT** — exhaustive finite computation in a declared finite ensemble.
- **CONSTRUCTIVE COUNTEREXAMPLE** — explicit witness refuting a universal statement.
- **COMPUTER-ASSISTED CERTIFICATE** — rigorous interval/exact arithmetic closes a finite or continuous sign obligation, with code and scope declared.
- **FINITE EVIDENCE** — regression, stress test, or sample; never sufficient by itself for theorem promotion.
- **OPEN** — not established.

## Mandatory separation

For every consolidated theorem, the final presentation must contain four independent boxes:

1. **Hypotheses.** Everything assumed.
2. **Conclusion.** Exactly what follows.
3. **Verification status.** Human-readable proof, exact computation, formal kernel, or combination.
4. **Nonclaims.** Stronger statements that do not follow.

## Promotion gate

A result cannot enter a short public manuscript as a central theorem until all of the following are true:

- the statement is independent of A-number chronology;
- definitions needed by the theorem fit in the same document or a minimal shared definitions file;
- every imported lemma is named and traced;
- failed stronger variants are recorded when materially relevant;
- executable evidence is reproducible from a clean environment where applicable;
- novelty wording matches the dedicated literature audit;
- physical interpretation is absent from the proof unless supplied as an explicit additional assumption.

## Formal-pilot scope rule

A Lean proof of an extracted substatement must be labeled by its actual formal boundary. C1.2 currently has a kernel-checked encoding-level theorem: two explicit valid minimum-block maps are distinct but share the historical representative code. It is **not yet** an end-to-end formal proof from the original directed graph definitions, because reachability and SCC extraction remain to be formalized.

## Freeze rule

During Consolidation 1.0, no new chronological research package is created merely to extend the sequence. New work is allowed only to repair a contradiction, close a formalization gap, or produce an independent verification of a selected core claim.
