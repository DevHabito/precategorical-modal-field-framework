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

`PrecategoryFormal/LiteralRepresentativeCode.lean` closes the carrier-level gap. It transports partial orders across the canonical increasing bijection `Fin k ≃ S`, proves the canonical coordinate code equivalent to the literal published code `(S,P)` where `P` lives on the actual representative set `S`, and proves

`Nat.card (LiteralRepresentativeCode 4) = 5234`.

`PrecategoryFormal/RepresentativeRealization.lean` closes the realizability gap. For every literal code `(S,P)` it constructs an explicit loopless directed graph and proves:

- graph reachability is exactly the order `P` lifted through the representative map;
- mutual reachability is equivalent to equality of representatives, so the SCCs are exactly the representative fibers;
- every selected representative is fixed by the representative map and is the minimum label in its SCC;
- reachability between the selected representatives is exactly `P`.

Thus the counted literal code space is not merely an abstract candidate superset: every counted `(S,P)` pair has a directed-graph realization with the declared SCC-minimum and quotient-order semantics.

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

**MF-R008 declared counting theorem, including literal-code realizability: END-TO-END LEAN/KERNEL PASS.**

**MF-R009 explicit witness: END-TO-END LEAN/KERNEL PASS.**

The repository CI uses pinned Lean `v4.33.1` / mathlib `v4.33.1`, rejects `sorry`/`admit` proof placeholders, and runs a complete `lake build`. The bundled `leanchecker` is then run separately for every project module. The checker stage is intentionally sharded across CI runners: this changes only scheduling, not the replay obligation, and prevents runner lifetime limits from masking the independent kernel replay.

The MF-R008 small-poset values are exact finite computations discharged with Lean `native_decide`; they are not presented as a new analytic formula for the poset-count sequence.

## Deliberate nonclaims

The MF-R008 formalization proves the declared representative-code counting theorem and the realizability of every counted literal code. It does **not** retain or count discarded SCC membership assignments as part of the code, make the representative code injective, establish novelty/priority, or imply anything physical.

For MF-R009, `ReachWithinBool 4` is used as an executable bounded-path evaluator for the two concrete five-vertex witnesses. We have proved its equivalence with the corresponding bounded proposition and proved bounded certificates sound for mathematical reachability.

We have **not** yet proved the reusable general theorem that every `Relation.ReflTransGen` path in every five-vertex directed graph can always be reduced to a path of length at most four. Therefore `witnessGraphRepresentativeCode4` is not yet promoted as a verified generic encoder for arbitrary five-vertex graphs.

This limitation does not weaken the explicit MF-R009 witness theorem: the exact SCC partitions, minimum representatives, absence of cross-SCC reachability, quotient antichain structure, and the two direct code values are all independently established for the two concrete graphs.

## Build

```bash
cd formal/lean
lake build
```

The committed `lake-manifest.json` pins the resolved dependency revisions used by CI.


## Physical bridge finite witnesses — END-TO-END LEAN/KERNEL PASS

Two deliberately small algebraic witnesses from the physics-facing bridge are now formalized.

### Transform non-closure witness

PrecategoryFormal/PhysicalBridgeTransformWitness.lean proves with exact rational arithmetic that the two four-state distributions used in the multi-electron bridge have:

- normalization one;
- the same mean \(3/2\);
- the same transform value \(15/32\) at the diagnostic point \(z=1/2\);
- different shifted-transform values \(219/320\) and \(437/640\);
- exact gap \(1/640\).

The file contains no experimental assumption. It certifies only the finite algebraic counterexample.

### Mean non-autonomy witness

PrecategoryFormal/PhysicalBridgeObservableWitness.lean proves the rational surrogate used to audit mean nonclosure:

- two three-state distributions have the same mean \(1\);
- their diagnostic \(G_{-c}\) values are \(2\) and \(5/2\);
- under the same rational birth/death coefficients their mean derivatives are \(11/7\) and \(17/14\);
- the exact derivative gap is \(-5/14\).

Again, this is a finite algebraic theorem, not a formalization of the experimental master equation.

### Verification status

GitHub Actions run 733 completed successfully after the modules were added to the sharded replay matrix.

The run includes:

- pinned Lean/mathlib build;
- proof-placeholder rejection;
- leanchecker replay for PrecategoryFormal.PhysicalBridgeTransformWitness;
- leanchecker replay for PrecategoryFormal.PhysicalBridgeObservableWitness.

The formal result does **not** certify the physical mapping, the Salhani et al. rate law, empirical adequacy, or novelty.


### Marginal-closure kernels — END-TO-END LEAN/KERNEL PASS

PrecategoryFormal/PhysicalBridgeMarginalClosure.lean formalizes three algebraic statements:

- the exact derivative gap produced by swapping two equal-weight hidden-context states;
- the fact that universal equal-weight two-context scalar closure forces equal multiplicative coefficients;
- the exact three-point recurrence for the average of two affine maps with a common multiplier.

GitHub Actions run 737 completed successfully with the pinned build and independent leanchecker replay for this module.

Scope boundary: the Lean file proves only rational algebraic kernels. It does not formalize Mori-Zwanzig, lumpability, the experimental systems, hidden-phase Fourier analysis, or the matrix-polynomial theorem.
