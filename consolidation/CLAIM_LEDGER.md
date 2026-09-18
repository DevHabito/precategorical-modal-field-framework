# Consolidation 1.0 — canonical claim ledger

This ledger is the public-facing status table for claims selected for consolidation. Historical A-number packages remain the source of provenance and detailed derivations.

| Core ID | Claim family | Current status | Evidence class | Formalization target | Literature status | Main unresolved obligation |
|---|---|---|---|---|---|---|
| C1.1 | Minimum-representative quotient-poset count | PROVED; END-TO-END LEAN/KERNEL PASS | combinatorial proof + exact `native_decide` enumeration + literal-code equivalence + explicit digraph realization + module-sharded `leanchecker` replay | formalization complete for the declared MF-R008 code/count claim | novelty not certified | none for the declared counting theorem; novelty remains separate |
| C1.2 | Non-injectivity of representative code | PROVED; EXPLICIT WITNESS END-TO-END LEAN/KERNEL PASS | constructive counterexample + `ReflTransGen` SCC proof + direct graph-code computation + `leanchecker` | explicit witness complete; generic encoder library optional | novelty not material | none for the explicit witness; prove generic five-vertex bounded-reach completeness only before promoting the bounded evaluator as a reusable arbitrary-graph encoder |
| C1.3 | `P5=75/256` edge-toggle sensitivity | EXACT FINITE RESULT; FORMALIZATION IN PROGRESS | independent exhaustive enumeration + semantic/pairing Lean chain under verification | direct semantic toggle predicate added; aggregate count still requires structural count proof and clean kernel replay | classical pivotality/Birnbaum structural-importance and random-digraph reachability framework; project-specific exact value; novelty not certified | prove the semantic aggregate count structurally without redundant brute force, obtain clean pinned `lake build` + `leanchecker`, and keep novelty audit synchronized |
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

A Lean proof of an extracted substatement must be labeled by its actual formal boundary.

C1.1 now has an end-to-end formalization of the **declared MF-R008 counting claim**. The formal chain proves the representative-set binomial factor, independently enumerates the labeled poset counts through the three-state antisymmetric encoding, proves the executable transitivity checker equivalent to mathematical transitivity, constructs the bijection to Boolean partial-order matrices, derives the fiber-sum cardinality from an explicit canonical code type, and proves that this coordinate model is equivalent to the literal published code `(S,P)` where `P` is a partial order on the actual representative set `S`. It also proves realizability: every such literal code has an explicit loopless directed-graph realization whose strongly connected components are exactly the fibers of the representative map, whose chosen representatives are the minimum labels of those SCCs, and whose quotient reachability order is exactly `P`. For five vertices the literal type has cardinality `5234`. The exact small-poset values use `native_decide`; they are therefore recorded as exact finite formal computation, not as a new analytic enumeration formula. The full Lean library build and a module-sharded bundled `leanchecker` replay pass.

C1.1 does **not** establish a novelty or priority claim, does not retain or count the discarded SCC memberships as part of the code, and does not make the representative code injective. Those are separate questions; the non-injectivity is C1.2.

C1.2 has an end-to-end kernel-checked theorem for the **explicit two-graph witness**: the original directed graphs are connected to mathematical reachability via `Relation.ReflTransGen`, their SCC minimum maps and antichain quotients are proved, and the direct graph encoder reproduces the historical collision code `100663296` for both distinct condensation structures.

This does not yet certify `ReachWithinBool 4` as a generic encoder component for every five-vertex directed graph. A reusable generic encoder would additionally require a completeness theorem reducing arbitrary five-vertex reachability to bounded paths. That stronger library statement is not needed for the explicit C1.2 counterexample and is not claimed.

C1.3 remains an **exact finite result under formalization**, not a kernel-complete theorem. The Lean branch now contains a Boolean predicate whose intended theorem is that it is true exactly when toggling a concrete non-loop edge changes the complete reflexive reachability preorder. The earlier fixed-edge cut checker has already been connected to semantic non-reachability, and the absent-edge count `153600` has exact finite certificates. The remaining count-level obligation is deliberately structural: connect the direct semantic full-ensemble object to the already certified absent-edge counts by a toggle-pair bijection and label symmetry (or an equivalent exact bijection proof), rather than paying for a second redundant brute-force scan of the full graph-edge ensemble.

Two attempted full CI builds were externally terminated by the hosted runner with a shutdown signal / exit code 143 while compiling the MF-R011 branch; no Lean theorem/type error was emitted before termination. These interrupted runs are neither passes nor mathematical failures and must not be used as evidence of kernel completion.

The C1.3 novelty boundary is also corrected. Fixed-edge pivotality is classical reliability/influence language: for the two-terminal system `φ_{a,b}(G)=1[a reaches b]`, the distinguished direct arc `a→b` has Birnbaum structural importance equal to the MF-R011 fixed-edge toggle probability. In the uniform `p=1/2` digraph this combines with classical random-digraph reachability to give `P_n = 2(1-γ_{n,1/2})`. Thus no novelty claim is made for the pivotality concept, the random-digraph reachability probability, or the initially-connected-digraph auxiliary sequence. The project-specific exact value and formal certificate remain valid research objects, with priority/novelty explicitly uncertified.

## Freeze rule

During Consolidation 1.0, no new chronological research package is created merely to extend the sequence. New work is allowed only to repair a contradiction, close a formalization gap, or produce an independent verification of a selected core claim.
