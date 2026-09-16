# Lean formalization — Consolidation 1.0 finite combinatorics

This directory is the proof-kernel track for the first Consolidation 1.0 claims. It currently contains end-to-end formal work for **MF-R008 / C1.1** and the explicit witness form of **MF-R009 / C1.2**.

## MF-R008 / C1.1 — representative-code count

The formal chain is deliberately split into independent modules.

`PrecategoryFormal/RepresentativeCount.lean` proves the representative-set combinatorics. For the `(m+1)`-label ground set, the `k`-element representative sets containing label `0` have cardinality

`Nat.choose m (k - 1)`.

It then derives the shifted-binomial fiber identity rather than defining the final theorem by the desired closed form.

`PrecategoryFormal/PosetEnumeration.lean` gives an independent finite enumeration of labeled posets. Each unordered pair has exactly three states — incomparable, lower-to-upper, or upper-to-lower — so antisymmetry is built into the candidate space. On five labels there are exactly `3^10 = 59049` candidates before the transitivity filter. Lean `native_decide` verifies

`p(1),…,p(5) = 1,3,19,219,4231`.

`PrecategoryFormal/PosetSemantics.lean` proves that the decoded relation is reflexive and antisymmetric and that the executable Boolean transitivity checker is equivalent to mathematical transitivity.

`PrecategoryFormal/PosetBijection.lean` constructs an exact equivalence between accepted three-state encodings and Boolean partial-order matrices on `Fin n`.

`PrecategoryFormal/PosetCountBridge.lean` identifies the executable count with the cardinality of the partial-order type and derives the verified five-vertex fiber count `5234`.

`PrecategoryFormal/RepresentativeCodeType.lean` defines an explicit canonical code type, so the fiber-sum formula is a theorem about a finite type rather than a stipulated definition.

`PrecategoryFormal/LiteralRepresentativeCode.lean` closes the final carrier-level gap. It transports partial orders across the canonical increasing bijection `Fin k ≃ S`, proves the canonical coordinate code equivalent to the literal published code `(S,P)` where `P` lives on the actual representative set `S`, and proves

`Nat.card (LiteralRepresentativeCode 4) = 5234`.

No historical Python count is imported into Lean as an axiom.

## MF-R009 / C1.2 — explicit non-injectivity witness

`PrecategoryFormal/RepresentativeCode.lean` formalizes the encoding-level collision:

- a five-vertex minimum-block representation;
- the two explicit A8.1 witness partitions;
- validity of both minimum-representative maps;
- exact historical representative code `100663296` for both witnesses;
- inequality of the two full block assignments;
- non-injectivity of the historical representative-code map.

`PrecategoryFormal/GraphSCCBridge.lean` closes the explicit graph-to-code bridge:

- the two original A8.1 directed graphs are defined by their edge relations;
- directed reachability is defined mathematically as `Relation.ReflTransGen` of the edge relation;
- SCC equivalence is mutual reachability;
- finite path certificates are proved sound for mathematical reachability;
- for each witness graph, mutual reachability is proved equivalent to equality of the proposed SCC minimum map;
- each representative is proved to lie in its SCC and to have minimum vertex label there;
- the quotient of the two SCCs is proved to be an antichain;
- a direct executable reconstruction of the historical A8 representative code reproduces `100663296` for each original graph;
- the direct graph code agrees with the already checked abstract condensation code on both witnesses.

The final theorem `mf_r009_graph_level_code_collision` therefore establishes the explicit MF-R009 counterexample end to end from the two original directed graphs through SCC semantics to the historical code collision.

## Verification status

**MF-R008 declared counting theorem: END-TO-END LEAN/KERNEL PASS.**

**MF-R009 explicit witness: END-TO-END LEAN/KERNEL PASS.**

The repository CI uses pinned Lean `v4.33.1` / mathlib `v4.33.1`, rejects `sorry`/`admit` proof placeholders, and runs a complete `lake build`. The bundled `leanchecker` is then run separately for every project module. The checker stage is intentionally sharded across CI runners: this changes only scheduling, not the replay obligation, and prevents runner lifetime limits from masking the independent kernel replay.

The MF-R008 small-poset values are exact finite computations discharged with Lean `native_decide`; they are not presented as a new analytic formula for the poset-count sequence.

## Deliberate nonclaims

The MF-R008 formalization proves the declared representative-code counting theorem. It does **not** count full SCC memberships, make the representative code injective, establish novelty/priority, or imply anything physical.

For MF-R009, `ReachWithinBool 4` is used as an executable bounded-path evaluator for the two concrete five-vertex witnesses. We have proved its equivalence with the corresponding bounded proposition and proved bounded certificates sound for mathematical reachability.

We have **not** yet proved the reusable general theorem that every `Relation.ReflTransGen` path in every five-vertex directed graph can always be reduced to a path of length at most four. Therefore `witnessGraphRepresentativeCode4` is not yet promoted as a verified generic encoder for arbitrary five-vertex graphs.

This limitation does not weaken the explicit MF-R009 witness theorem: the exact SCC partitions, minimum representatives, absence of cross-SCC reachability, quotient antichain structure, and the two direct code values are all independently established for the two concrete graphs.

## Build

```bash
cd formal/lean
lake build
```

The committed `lake-manifest.json` pins the resolved dependency revisions used by CI.
