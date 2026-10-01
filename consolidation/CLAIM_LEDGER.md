# Consolidation 1.0 — canonical claim ledger

This ledger is the public-facing status table for claims selected for consolidation. Historical A-number packages remain the source of provenance and detailed derivations.

| Core ID | Claim family | Current status | Evidence class | Formalization target | Literature status | Main unresolved obligation |
|---|---|---|---|---|---|---|
| C1.1 | Minimum-representative quotient-poset count | PROVED; END-TO-END LEAN/KERNEL PASS | combinatorial proof + exact `native_decide` enumeration + literal-code equivalence + explicit digraph realization + module-sharded `leanchecker` replay | formalization complete for the declared MF-R008 code/count claim | novelty not certified | none for the declared counting theorem; novelty remains separate |
| C1.2 | Non-injectivity of representative code | PROVED; EXPLICIT WITNESS END-TO-END LEAN/KERNEL PASS | constructive counterexample + `ReflTransGen` SCC proof + direct graph-code computation + `leanchecker` | explicit witness complete; generic encoder library optional | novelty not material | none for the explicit witness; prove generic five-vertex bounded-reach completeness only before promoting the bounded evaluator as a reusable arbitrary-graph encoder |
| C1.3 | `P5=75/256` edge-toggle sensitivity of the full labeled reachability preorder | EXACT FINITE RESULT; END-TO-END LEAN/KERNEL PASS AT DECLARED `n=5` SCOPE | historical exhaustive enumeration + independent exact counting derivation + independent directed-cut inclusion-exclusion cross-check through `n=6` + independent Lean finite enumeration + semantic/ensemble/indicator bridges + module-sharded `leanchecker` replay | formalization complete for the declared exact `n=5` statistic and its semantic bridge; the general probability identity for arbitrary `n` is not claimed as Lean-formalized | fixed-pair random-digraph reachability and reachability-based edge influence have prior art; priority of the specific value `75/256` is not certified | no unresolved obligation for F2 at the declared `n=5` boundary; preserve corrected literature wording and explicit formal-scope boundary |
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

### C1.3 formal boundary — closed for F2

C1.3 now has an end-to-end Lean/kernel pass for the **declared exact `n=5` reachability-preorder sensitivity claim**. The observable is the full labeled reflexive-transitive reachability relation on the original vertices; this is a preorder. It should not be described loosely as only the condensation preorder/poset, because the formal observable retains the labeled vertex-level reachability relation before SCC quotienting.

The formal chain contains an independent Lean graph-mask enumeration for the exact `n=5` numerator, an independent relation-based Floyd–Warshall reference closure proved equivalent to `Relation.ReflTransGen`, an exhaustive bridge from the compact reachability code to that semantic reference over all `2^20` graph masks, a proof that the 20 mask coordinates are exactly the 20 directed non-loop edges, a proof that a coordinate toggle flips exactly that edge and preserves all others, and an indicator bridge proving each enumerator summand is exactly the event that the full mathematical reachability preorder changes.

At commit `83b45fed020e24f7f9ceba7ecd86220e9c2b8b08`, workflow `Lean formal verification` run `301` completed successfully: the pinned-toolchain `lake build`, proof-placeholder rejection, and every declared module-sharded bundled `leanchecker` replay passed.

A separate generic theorem proves that inserting one directed edge preserves the whole reflexive-transitive closure exactly when its target was already reachable from its source. This theorem has no finiteness, encoding, or probability assumptions. It formalizes the logical insertion criterion only; the probabilistic pairing factor `2` and label-symmetry step in

`P_n = 2 Pr(s not→ t) = 2(1 - gamma_{n,1/2})`

are established in the human-readable mathematical derivation but are **not** being promoted as an already kernel-checked general probability theorem for arbitrary `n`.

Outside the Lean path, the `n=5` value has an exact reachable-set counting derivation, and a pre-registered `n=6` target was independently reproduced by directed-cut inclusion-exclusion:

`B6 = 82051072`, `Pr(s not→ t) = 313/4096`, `P6 = 313/2048`, and `4923064320` sensitive ordered graph-edge pairs out of `32212254720`.

Those `n=6` checks strengthen reproducibility but do not enlarge the end-to-end formal claim beyond `n=5`.

F2/C1.3 is therefore closed at its declared finite scope. Any future generalization in `n`, asymptotic analysis, or general probability formalization is new work and must receive its own hypotheses, verification gate, and literature review.

## Freeze rule

During Consolidation 1.0, no new chronological research package is created merely to extend the sequence. New work is allowed only to repair a contradiction, close a formalization gap, or produce an independent verification of a selected core claim.
