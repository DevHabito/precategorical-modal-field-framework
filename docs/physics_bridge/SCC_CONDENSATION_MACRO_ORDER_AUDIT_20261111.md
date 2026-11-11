# SCC condensation as a pregeometric macro-order candidate

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** mathematically valid timeless order construction; insufficient as a universal physical time  
**Novelty status:** strongly connected components and condensation DAGs are classical; project relevance comes from the existing C1 lossy-encoding results

## 1. Motivation

The pregeometric anti-circularity gate rules out candidate temporal orders that already assume:

- external time labels;
- update numbers interpreted as time;
- Markov-step ordering;
- decay parameters;
- imposed causal direction.

A directed relational structure, however, can be given without assigning a scalar time.

If that structure contains cycles, no strictly increasing scalar time function can be assigned to every directed edge.

Strongly connected component condensation provides a canonical way to separate mutually reachable cyclic sectors from irreversible reachability between sectors.

## 2. Strong-connectivity equivalence

Let

$$
G=(V,E)
$$

be a directed graph.

Define

$$
u\sim v
$$

when \(u\) reaches \(v\) and \(v\) reaches \(u\).

Mutual reachability is an equivalence relation.

Its equivalence classes are the strongly connected components (SCCs).

No temporal label is needed to define this quotient.

## 3. Condensation graph

Let

$$
\mathcal C(G)
$$

have one node for each SCC.

For distinct components \(C_i,C_j\), place an edge

$$
C_i\to C_j
$$

when at least one original edge runs from a vertex of \(C_i\) to a vertex of \(C_j\).

A classical theorem gives

$$
\boxed{
\mathcal C(G)\text{ is a directed acyclic graph}.
}
$$

If a directed cycle existed between two or more SCCs, those components would be mutually reachable and therefore would not be distinct maximal SCCs.

## 4. Canonical partial order

Because the condensation is acyclic, reachability on its nodes defines a strict partial order.

Write

$$
C_i\prec C_j
$$

when there is a directed path from \(C_i\) to \(C_j\).

Thus an arbitrary finite directed relation has a canonical decomposition into:

- cyclic/mutually reachable sectors;
- an acyclic reachability order between those sectors.

This construction is invariant under relabeling of the original graph.

It therefore passes the most elementary anti-circularity and label-invariance checks.

## 5. Why this is not automatically physical time

The construction supplies an order on SCCs.

It does not supply:

- physical duration;
- a clock;
- Lorentzian causal structure;
- metric intervals;
- a unique total ordering of incomparable SCCs;
- dynamics inside one SCC.

The word “time” cannot be attached merely because a DAG exists.

## 6. Exact information loss

Condensation is highly non-injective.

Consider two graphs on three vertices.

### Graph A

A directed three-cycle:

$$
1\to2\to3\to1.
$$

### Graph B

Every pair is connected in both directions.

Both graphs are strongly connected.

Therefore

$$
\boxed{
\mathcal C(G_A)
=
\mathcal C(G_B)
=
\{\text{one component}\}.
}
$$

Yet their internal edge structures are different.

So the condensation cannot reconstruct the microscopic relational dynamics.

More generally, arbitrarily many non-isomorphic strongly connected graphs can map to the same one-node condensation.

## 7. Connection with C1

The repository's C1 programme already proved a closely related warning for its project-specific representative encoding:

> quotient-level order plus selected representatives does not determine the original relational structure.

The present physical audit gives that older mathematical result a concrete governance role.

If a proposed pregeometric time uses a quotient order, the repository already knows that:

$$
\boxed{
\text{macro-order does not determine micro-relation}.
}
$$

That information loss must be acknowledged rather than treated as a feature to be silently ignored.

## 8. The reversible-sector problem

Suppose an entire physical system lies in one strongly connected component.

Then

$$
\mathcal C(G)
$$

has one node.

The SCC macro-order contains no nontrivial progression at all.

Nevertheless the system can have rich reversible or cyclic dynamics internally.

Therefore SCC condensation cannot be a universal representation of physical time.

It can at most represent an order of **irreversible accessibility between recurrence classes**.

## 9. Topological order is not duration

Every finite DAG admits a topological ordering.

But topological orderings need not be unique.

If two SCCs are incomparable, either can appear first in a linear extension.

Therefore choosing one topological index and calling it time would add arbitrary information.

One may instead retain the partial order itself.

Even then, assigning a numerical duration requires additional structure.

For example, longest-path depth is a combinatorial statistic, not automatically proper time.

## 10. Comparison with causal sets

A finite DAG's transitive reachability relation is a finite partial order.

This resembles one ingredient of causal-set theory.

But causal-set theory gives the order a causal interpretation as part of its physical hypothesis.

The SCC construction by itself supplies only a mathematical partial order.

To use it physically, the project must explain why the primitive directed relation represents something whose asymmetric reachability corresponds to causal or temporal precedence.

Without that bridge, similarity to a causet is structural only.

## 11. A possible restricted interpretation

A defensible restricted interpretation is:

> SCC condensation separates mutually recoverable/recurrent relational sectors from one-way accessibility between sectors.

If a physical application independently justifies the directed relation as an accessibility or influence relation, the quotient can define a macroscopic irreversible order.

This would be an emergent **arrow between sectors**, not a derivation of all microscopic time.

## 12. Falsification criteria

The SCC route fails as a physical macro-order if:

1. the primitive edge relation has no operational meaning;
2. physically reversible states that must remain distinguishable are collapsed incorrectly;
3. observed transitions move against the proposed quotient order;
4. the quotient order depends on arbitrary preprocessing;
5. different physically relevant systems with the same condensation require different temporal predictions that the quotient cannot encode.

## 13. Current classification

### As a mathematical timeless order construction

**PASS.**

It is canonical, label-invariant, and acyclic after quotienting mutual reachability.

### As a universal physical time

**FAIL.**

It erases all internal cyclic dynamics and provides no duration.

### As a candidate macroscopic accessibility/irreversibility order

**OPEN.**

It may be useful if a future physical model independently supplies the meaning of the primitive directed relation.

## 14. Research consequence

The pregeometric programme now has a sharper fork.

Either:

1. derive a physically justified directed primitive relation whose SCC quotient carries meaningful irreversible order; or
2. find a construction that represents reversible change without collapsing it into one equivalence class.

The second problem is harder and is the one a universal account of time would ultimately have to address.
