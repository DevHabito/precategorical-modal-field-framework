# Bipartite orientation doublet — depth-one limitation

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact structural limitation  
**Conclusion:** the canonical orientation induced by one bipartition is acyclic but has directed height at most one edge; it cannot by itself encode extended temporal succession

## 1. Why this limitation matters

The connected-bipartite theorem provides a genuine orientation class modulo global reversal.

For a connected bipartite graph

$$
V=A\sqcup B,
$$

orient every edge as

$$
A\to B.
$$

This gives a canonical orientation up to global reversal.

The construction is mathematically clean.

But its temporal expressive power is extremely limited.

## 2. No directed path of length two

Every oriented edge has the form

$$
a\to b,
\qquad
a\in A,\quad b\in B.
$$

A second directed edge beginning at \(b\) would require

$$
b\in A.
$$

But

$$
A\cap B=\varnothing.
$$

Therefore no configuration

$$
u\to v\to w
$$

exists.

Hence:

$$
\boxed{
\text{every directed path has at most one edge}.
}
$$

## 3. Consequences

The bipartite orientation supports:

- local source-versus-target distinction;
- a two-layer partial order;
- one global reversal pair.

It does **not** support:

- three or more successive temporal layers;
- a long causal chain;
- repeated internal updates;
- path-length duration;
- nontrivial transitive propagation through intermediate events.

Its transitivity is vacuous because there are no composable directed edges.

## 4. graphA example

For graphA's cycle component, choose

$$
A=\{0,3\},
\qquad
B=\{2,4\}.
$$

One orientation is

$$
0\to2,\quad
0\to4,\quad
3\to2,\quad
3\to4.
$$

There is no directed path of the form

$$
x\to y\to z.
$$

The reverse orientation has the same limitation.

Thus the intrinsic C4 doublet is a clean orientation axis but not an extended temporal order.

## 5. This is not a defect in the theorem

The bipartite construction was introduced to solve a narrower problem:

> can an unmarked symmetric finite structure determine an orientation class modulo reversal?

For graphA C4 the answer is yes.

The current limitation says only that:

$$
\boxed{
\text{orientation-class existence}
\not\Rightarrow
\text{rich causal depth}.
}
$$

This is analogous to the earlier separation between chirality and precedence.

## 6. New gate: compositional depth

Any candidate pregeometric order intended to model extended temporal succession must support a nontrivial composition structure.

At minimum, one should test whether there exist

$$
x_0\prec x_1\prec x_2.
$$

For macroscopic temporal recovery one needs much more:

- arbitrarily or parametrically long chains in growing systems;
- stable coarse-grained order;
- controlled scaling of chain depth;
- compatibility with local causal structure;
- no hidden labeling convention.

## 7. Height versus duration

Even long chains would still provide only ordinal depth.

A chain length

$$
L
$$

is not physical duration unless a refinement/calibration theorem relates it to an accepted clock or proper-time quantity.

Therefore the hierarchy becomes

$$
\boxed{
\text{orientation doublet}
\to
\text{nontrivial order depth}
\to
\text{causal recovery}
\to
\text{duration calibration}.
}
$$

## 8. Relation to causal sets

Causal-set theory illustrates why depth matters.

A causal set is not merely bipartite.

Its partial order can contain long chains, and in appropriate sprinkling regimes longest-chain statistics are related to continuum proper-time structure.

That established programme is a stronger benchmark than the current C4 doublet.

The repository should not call a two-layer orientation a causal set or a time geometry.

## 9. Relation to constructor/resource semantics

A two-layer source-target relation can still have legitimate non-temporal meaning:

- inputs versus outputs;
- reactants versus products;
- permitted source/target resource types;
- producer/consumer roles.

This reinforces the semantic caution.

The same mathematical two-layer order can represent many non-temporal structures.

## 10. Formal status

The Lean module PhysicalBridgeBipartiteOrientation proves the finite logical kernel:

- orientation from one side is irreflexive;
- no directed two-step path exists;
- transitivity therefore holds vacuously;
- asymmetry holds;
- complementing the side predicate gives the globally reversed orientation when adjacency is symmetric.

The module is submitted to CI and must not be promoted until the workflow passes.

## 11. Current verdict

**Intrinsic orientation doublet from graphA C4:** PASS.

**Nontrivial directed path of length two:** FAIL by theorem.

**Extended temporal succession:** NOT PROVIDED.

**Duration:** NOT PROVIDED.

**Usefulness:** retained as a minimal orientability precursor only.

## 12. Revised next mathematical question

The next structure must preserve the good part of the bipartite result—

$$
\text{canonical orientation modulo reversal}
$$

—while allowing nontrivial compositional depth.

The smallest new question is:

$$
\boxed{
\text{Can a non-temporal finite relational structure canonically determine
a unique reversal class of acyclic orders with chain length at least 2?}
}
$$

This is now the next finite target.
