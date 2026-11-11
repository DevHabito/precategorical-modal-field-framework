# Comparability and UPO positioning for the orientation-torsor programme

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** prior-art correction and exact finite classification  
**Novelty status:** comparability graphs, transitive orientations, UPO graphs, modular decomposition, and automorphism actions on transitive orientations are established graph theory

## 1. Why this correction is necessary

The recent finite search introduced an orientation-class criterion for an undirected graph \(G\).

Given an acyclic orientation \(O\), the audit asked whether every graph automorphism sends \(O\) to either

$$
O
$$

or its global reverse

$$
O^{\mathrm{op}}.
$$

The diamond graph \(K_4-e\) supplied the first unmarked depth-two witness under that criterion.

Before treating this as a structural contribution, the criterion must be positioned against classical comparability-graph theory.

## 2. Classical transitive orientations

An undirected graph \(G=(V,E)\) is a comparability graph when its edges admit a transitive orientation.

A transitive orientation \(O\) satisfies:

if

$$
u\to v
\quad\text{and}\quad
v\to w,
$$

then

$$
\{u,w\}\in E
$$

and the edge is oriented

$$
u\to w.
$$

The resulting directed relation is a strict partial order whose comparability graph is exactly \(G\).

This theory predates the present project by decades.

## 3. Classical UPO graphs

Aigner and Prins introduced uniquely partially orderable (UPO) graphs.

A comparability graph is UPO when its compatible strict partial order is unique except for dualization.

Equivalently, in orientation language, it has exactly two transitive orientations:

$$
\boxed{
O,\quad O^{\mathrm{op}}.
}
$$

Möhring later proved asymptotic results showing that almost all comparability graphs are UPO.

Therefore the bare statement

> a graph has one transitive orientation up to reversal

is classical and must not be claimed as a project novelty.

## 4. Automorphisms act on transitive orientations

For a comparability graph \(G\), every

$$
g\in\operatorname{Aut}(G)
$$

maps a transitive orientation to another transitive orientation.

Thus

$$
\operatorname{Aut}(G)
$$

acts on the set

$$
\mathrm{TO}(G)
$$

of transitive orientations.

This action and its structural relation to modular decomposition are established comparability-graph theory.

The present project should therefore formulate its finite criterion as an application of this classical action, not as a newly discovered graph-theoretic framework.

## 5. Project criterion after correction

The project's current finite criterion is not UPO.

For a transitive orientation \(O\), define its duality class

$$
[O]_\pm
=
\{O,O^{\mathrm{op}}\}.
$$

Call this class Aut-stable for project bookkeeping when

$$
g(O)\in[O]_\pm
$$

for every

$$
g\in\operatorname{Aut}(G).
$$

Equivalently, \([O]_\pm\) is a fixed point of the induced automorphism action on

$$
\mathrm{TO}(G)/(\text{global reversal}).
$$

The project then asks whether exactly one such Aut-stable duality class exists.

This is a project-specific selection criterion assembled from classical ingredients.

No novelty claim is attached to the group action itself.

## 6. Exact difference from UPO

### UPO

$$
|\mathrm{TO}(G)|=2.
$$

There is only one duality class at all.

### Project Aut-stable criterion

There may be many transitive orientations and many duality classes.

The criterion requires only one duality class to be fixed by the full graph automorphism group.

Other duality classes may exist but be moved nontrivially by automorphisms.

Therefore:

$$
\boxed{
\text{UPO}
\Longrightarrow
\text{one Aut-stable duality class},
}
$$

but the converse need not hold.

The diamond graph is the smallest witness found here for the failure of the converse.

## 7. Diamond correction

The diamond graph

$$
K_4-e
$$

has six transitive orientations.

Therefore:

$$
\boxed{
K_4-e\text{ is not UPO}.
}
$$

Its six orientations form three reversal pairs.

Under the full four-element automorphism group:

- one reversal pair is preserved as a set;
- the other two reversal pairs are moved by some automorphisms.

The preserved pair is the depth-two orientation described in the earlier diamond audit:

$$
a\to x,\quad
a\to y,\quad
x\to b,\quad
y\to b,\quad
a\to b,
$$

together with its global reverse.

Thus the correct statement is:

> The diamond has one Aut-stable transitive-orientation duality class, even though it is not uniquely partially orderable.

## 8. Why the automorphism requirement matters

A transitive orientation can encode a partial order that depends on an arbitrary choice not respected by all symmetries of the original undirected structure.

The project is interested in structure that can be extracted equivariantly from unlabelled primitive data.

Requiring the duality class to be fixed under the automorphism action is therefore a governance condition for pregeometric reuse.

It is not a replacement for comparability theory.

## 9. Exact enumeration through n=5

The corrected audit enumerates every connected labeled simple graph for

$$
n=2,3,4,5.
$$

For every graph it computes:

- every transitive orientation;
- comparability status;
- UPO status;
- graph automorphisms;
- Aut-stable orientation duality classes;
- longest chain depth.

The exact summary is:

| n | connected | comparability | UPO | exactly one Aut-stable duality class | such class with depth >= 2 |
|---:|---:|---:|---:|---:|---:|
|2|1|1|1|1|0|
|3|4|4|3|3|0|
|4|38|38|19|25|6|
|5|728|716|315|340|145|

These are labeled-graph counts.

## 10. UPO depth versus Aut-stable depth

For \(n=4\), all 19 UPO graphs in the enumeration have longest directed chain depth 1.

The six additional deep Aut-stable cases are the six labeled diamonds.

For \(n=5\):

- UPO depth histogram:
  - depth 1: 195;
  - depth 2: 120.

- unique Aut-stable-class depth histogram:
  - depth 1: 195;
  - depth 2: 145.

Thus the automorphism-stable criterion includes, but is not identical to, the UPO class.

## 11. Transitivity matters

The earlier intrinsic-orientation-depth audit tested acyclicity, not full transitivity.

Acyclic orientation is weaker than transitive orientation.

Therefore its counts must not be compared directly with UPO counts.

The corrected audit adds the exact transitivity condition and should be the canonical source for any claim involving partial-order comparability.

The earlier acyclic audit remains useful only for the broader question of invariant DAG orientation.

## 12. Literature boundary

The following are classical and require attribution:

- comparability graphs;
- transitive orientations;
- implication classes;
- UPO graphs;
- uniqueness up to duality;
- modular-decomposition structure of transitive orientations;
- action of graph automorphisms on transitive orientations.

The present project currently contributes only a use-specific filter:

> among classical transitive orientation classes, retain those whose duality class is fixed by every automorphism of the primitive undirected graph.

Whether this criterion has appeared under another name requires a dedicated novelty search before any originality claim.

## 13. Physical boundary

Even an Aut-stable transitive orientation duality class is only a partial-order structure.

It does not provide:

- causal semantics;
- Lorentzian cones;
- duration;
- spacetime dimension;
- a physical mapping of vertices to events;
- empirical evidence.

The pregeometric interpretation remains separate from the graph-theoretic classification.

## 14. Current conclusion

The diamond result survives the literature correction, but in a narrower form.

It is not a new example of unique partial orderability.

It is a small exact witness separating:

$$
\boxed{
\text{UPO uniqueness}
}
$$

from

$$
\boxed{
\text{uniqueness of an automorphism-stable duality class}.
}
$$

The latter is the property currently relevant to the project's label-free extraction rule.

Its absolute mathematical novelty is not certified and should not be claimed.
