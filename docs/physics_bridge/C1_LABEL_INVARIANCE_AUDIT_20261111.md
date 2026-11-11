# C1 label-invariance audit for pregeometric use

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** scope correction separating canonical SCC structure from label-dependent encoding representatives

## 1. Why this audit is necessary

The repository's C1 formalization deliberately uses minimum-labeled representatives of strongly connected components.

That is legitimate for a finite encoding/counting scheme on a labeled ground set.

It must not be confused with a physically canonical element of the SCC.

A pregeometric theory cannot assign physical meaning to “the smallest vertex label” unless those labels themselves have independent physical meaning.

## 2. Canonical object

For a directed graph \(G\), mutual reachability defines an equivalence relation.

The set of equivalence classes

$$
V/{\sim}
$$

is canonical up to graph isomorphism.

The condensation relation between those classes is likewise canonical up to isomorphism.

If the original graph is relabeled, the SCC quotient is relabeled correspondingly but its abstract structure is unchanged.

This is the part that may enter a label-invariant physical discussion.

## 3. Encoding representative

The project-specific C1 code chooses, for each SCC, the minimum vertex label.

Schematically,

$$
\operatorname{rep}(C)=\min C.
$$

This choice depends on a total order of labels.

Under an arbitrary relabeling of the same abstract graph, the vertex selected as the minimum representative can change.

Therefore

$$
\boxed{
\text{minimum representative}
\neq
\text{intrinsic physical element of the SCC}.
}
$$

It is a coding convention.

## 4. Simple example

Take one three-vertex directed cycle.

All three vertices form one SCC.

With labels

$$
\{0,1,2\},
$$

the minimum representative is \(0\).

Relabel the same abstract cycle by a permutation exchanging \(0\) and \(2\).

The SCC remains the same abstract component, but the vertex carrying the minimum numerical label is now a different original vertex.

Nothing physical changed.

Only the encoding convention did.

## 5. Consequence for C1 claims

The C1 theorems remain valid for their declared labeled encoding.

This audit does not invalidate:

- the counting formula;
- the formal SCC bridge;
- the explicit code collision;
- the non-injectivity theorem.

It restricts physical reuse.

A pregeometric bridge may use:

- SCC equivalence classes;
- the abstract quotient order;
- isomorphism-invariant properties of the quotient.

It may not use the identity of a minimum-labeled representative as a physical datum without a separate justification.

## 6. Consequence for the SCC macro-order candidate

The correct candidate macro-order is

$$
[C]\prec[D]
$$

between SCC equivalence classes, defined by quotient reachability.

It is **not**

$$
\min(C)\prec\min(D)
$$

as a physical statement.

Representative labels can still implement the quotient computationally, but all physical conclusions must be invariant under changing the representative convention.

## 7. Required test

Any future pregeometric observable \(F(G)\) derived from C1-style data must pass:

$$
\boxed{
F(\sigma G)\cong F(G)
}
$$

for every graph relabeling/isomorphism \(\sigma\).

If the numerical value or physical conclusion changes only because vertex names changed, the candidate fails.

## 8. Relation to the symmetry-orientation gate

This audit and the automorphism no-go point in the same direction.

A physical temporal arrow cannot be hidden in:

- label order;
- representative choice;
- file ordering;
- enumeration order;
- arbitrary tie-breaking.

If an orientation survives only after such a choice, the asymmetry was inserted by the encoding rather than derived from the primitive relation.

## 9. Current classification

**C1 minimum-representative code:** valid mathematical encoding.

**SCC quotient/condensation:** canonical up to isomorphism and eligible for timeless structural analysis.

**Minimum representative as physical primitive:** rejected.

This distinction is mandatory in all later pregeometric work.
