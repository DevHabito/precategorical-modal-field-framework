# Bipartite orientation-doublet theorem — canonical orientation class without scalar polarity

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** classical graph theorem + project-specific orientation-doublet corollary  
**Novelty status:** connected bipartition uniqueness is classical; the pre-time-orientation interpretation is project-specific and not claimed as new graph theory

## 1. The correction

The graphA cycle component does not need an externally chosen alternating scalar mark.

Its alternating two-color structure is already intrinsic **up to global color swap** because the cycle is connected and bipartite.

This provides a cleaner derivation of the orientation doublet.

## 2. Classical theorem

Let

$$
G=(V,E)
$$

be a connected bipartite graph with at least one edge.

If

$$
V=A\sqcup B
$$

and

$$
V=A'\sqcup B'
$$

are two bipartitions, then either

$$
A=A',\qquad B=B',
$$

or

$$
A=B',\qquad B=A'.
$$

Therefore the unordered bipartition

$$
\boxed{
\{A,B\}
}
$$

is canonical.

Equivalently, a connected bipartite graph has exactly two proper binary colorings, related by global color complement.

## 3. Proof by path parity

Fix one vertex

$$
v_0.
$$

Because the graph is connected, every vertex \(v\) is joined to \(v_0\) by a path.

In a bipartite graph every path from \(v_0\) to \(v\) has the same parity; otherwise two paths of opposite parity would form an odd cycle.

Thus vertices split into:

$$
A=
\{v:d(v_0,v)\equiv0\pmod2\},
$$

and

$$
B=
\{v:d(v_0,v)\equiv1\pmod2\}.
$$

Choosing \(v_0\) in the opposite part swaps \(A\) and \(B\).

No third bipartition exists.

## 4. Orientation-doublet corollary

Given the canonical unordered bipartition

$$
\{A,B\},
$$

define

$$
O_{A\to B}
$$

by orienting every undirected edge from its endpoint in \(A\) toward its endpoint in \(B\).

Because every edge joins opposite parts, the resulting digraph has no directed path of length two:

a vertex in \(B\) has no outgoing edges in this orientation.

Therefore it is acyclic.

Swapping the two parts gives

$$
O_{B\to A}
=
O_{A\to B}^{\mathrm{op}}.
$$

Thus the graph canonically determines the unordered pair

$$
\boxed{
[O]_\pm
=
\{
O_{A\to B},
O_{B\to A}
\}.
}
$$

This is an exact orientation doublet.

## 5. No scalar polarity is chosen

The graph does not canonically say which bipartition class is called \(A\) and which is called \(B\).

Therefore it does not choose

$$
A\to B
$$

over

$$
B\to A.
$$

The doublet is canonical even though neither polarity is.

This is precisely the distinction needed by Direction V2.

## 6. graphA

The connected nontrivial graphA skeleton is

$$
C_4
$$

with vertices in cycle order

$$
0-2-3-4-0.
$$

Its canonical unordered bipartition is

$$
\boxed{
\big\{
\{0,3\},
\{2,4\}
\big\}.
}
$$

The two induced orientations are:

### Orientation 1

$$
0\to2,\quad
3\to2,\quad
3\to4,\quad
0\to4.
$$

### Orientation 2

the global reverse.

This is exactly the doublet previously found by exhaustive binary-color enumeration.

The isolated vertex \(1\) is not part of this connected orientation-bearing component.

## 7. Why this does not contradict the automorphism orbit result

The four C4 vertices form one orbit under the full dihedral automorphism group.

Therefore no pointwise invariant scalar can assign one fixed numerical value to \(\{0,3\}\) and another to \(\{2,4\}\).

But an automorphism may exchange the two bipartition classes.

The unordered object

$$
\{
\{0,3\},
\{2,4\}
\}
$$

is preserved as a set.

Thus:

$$
\boxed{
\text{pointwise invariant scalar}
\neq
\text{equivariant unordered two-fold structure}.
}
$$

This is the key correction.

## 8. \(\mathbb Z_2\)-torsor interpretation

The two proper two-colorings are exchanged freely and transitively by global color complement.

Likewise the two induced orientations are exchanged freely and transitively by global reversal.

Therefore the orientation class naturally carries a

$$
\mathbb Z_2
$$

torsor structure.

There is no distinguished identity element/polarity.

## 9. Exact computational regression

The repository exhaustively enumerates every labeled simple graph for

$$
n=2,3,4,5,6.
$$

For each graph it tests:

1. connectedness;
2. existence of a proper binary coloring;
3. number of proper binary colorings.

For every connected bipartite graph found, the exact number of proper binary colorings is 2.

The numbers of connected labeled bipartite graphs encountered are:

| n | count |
|---:|---:|
|2|1|
|3|3|
|4|19|
|5|195|
|6|3031|

Every case satisfies uniqueness up to complement.

This is a computational regression of a classical theorem, not evidence of novelty.

## 10. New interpretation of graphA

The previous status

> graphA needs an independently supplied alternating mark to produce the doublet

was too strong.

The corrected status is:

> graphA's connected C4 skeleton intrinsically supplies an **unlabeled bipartition** and therefore an orientation doublet; it does not supply a preferred polarity.

This is a substantive improvement.

## 11. Physical boundary

Bipartiteness is purely combinatorial.

A canonical bipartition does not explain why its two classes correspond to anything temporal.

The classes might represent:

- two sublattices;
- parity sectors;
- particle types;
- input/output types;
- another relational distinction.

Therefore:

$$
\boxed{
\text{intrinsic orientation doublet}
\not\Rightarrow
\text{physical time orientation}.
}
$$

A physical bridge must explain why this particular two-fold structure maps to causal/time orientation.

## 12. Relation to Lorentzian time orientability

The structural analogy is now sharper.

### Connected bipartite graph

A unique two-coloring class modulo color swap.

### Connected time-orientable Lorentzian manifold

Two global time orientations related by reversal.

Both structures provide a canonical two-fold orientation class without intrinsically naming one side positive.

The analogy ends there.

No Lorentzian metric, cone bundle, dimensionality, or causal speed structure is derived from bipartiteness.

## 13. New mathematical target

The graphA example suggests broadening the search from scalar marks to **canonical two-fold structures**.

Candidate mechanisms include:

- unique bipartitions;
- double covers;
- parity classes;
- orientation bundles;
- other \(\mathbb Z_2\)-torsors determined functorially by the primitive structure.

This is more general and less ad hoc than inventing a scalar score.

## 14. Current verdict

**Does graphA C4 canonically determine an orientation doublet?**  
YES.

**Does it canonically choose one polarity?**  
NO.

**Was the previous scalar-mark no-go wrong?**  
NO; its earlier physical conclusion was overextended.

**Does bipartiteness derive physical temporal orientation?**  
NO.

**Is orientation-class emergence from the bare C4 now established mathematically?**  
YES, at the combinatorial level.

## 15. Revised frontier

The next question is no longer:

> what extra mark produces graphA's orientation doublet?

For graphA C4, no extra mark is needed.

The next question is:

$$
\boxed{
\text{what physical principle could make an intrinsically derived
two-fold relational orientation class correspond to time orientation?}
}
$$

That is a much cleaner bridge problem.
