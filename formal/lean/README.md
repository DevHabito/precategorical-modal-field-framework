# Lean formalization — MF-R009 explicit witness

This directory is the proof-kernel track for Consolidation 1.0.

## Current verified scope

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

No Python result is imported into Lean as an axiom.

## Verification status

**MF-R009 explicit witness: END-TO-END LEAN/KERNEL PASS.**

The repository CI checks the Lean source with pinned Lean `v4.33.1` / mathlib `v4.33.1`, rejects `sorry`/`admit` proof placeholders, runs `lake build`, and then runs the bundled `leanchecker` from the active Lean toolchain.

## Deliberate nonclaim

`ReachWithinBool 4` is used as an executable bounded-path evaluator for these concrete five-vertex witnesses. We have proved its equivalence with the corresponding bounded proposition and proved bounded certificates sound for mathematical reachability.

We have **not** yet proved the reusable general theorem that every `Relation.ReflTransGen` path in every five-vertex directed graph can always be reduced to a path of length at most four. Therefore `witnessGraphRepresentativeCode4` is not yet promoted as a verified generic encoder for arbitrary five-vertex graphs.

This limitation does not weaken the explicit MF-R009 witness theorem: the exact SCC partitions, minimum representatives, absence of cross-SCC reachability, quotient antichain structure, and the two direct code values are all independently established for the two concrete graphs.

## Build

```bash
cd formal/lean
lake build
```

The committed `lake-manifest.json` pins the resolved dependency revisions used by CI.
