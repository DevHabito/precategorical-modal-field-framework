# A22 — Primitive Admissibility Criterion

## Symmetry-breaking criterion

Let `R` be the relational observation and let `G` act on latent
representatives while preserving `R`. Let `Z` be an added primitive.

If the conditional marked law is invariant,

`Law(Z | x) = Law(Z | g.x)`

for every relevant latent state `x` and transformation `g`, then the marked
observations `(R,Z)` have the same law. No estimator based on them can
distinguish the representatives.

Conversely, if for some measurable event `A`

`P(Z in A | x) != P(Z in A | g.x)`,

then the one-sample marked laws differ. In principle, repeated iid marked
observations can distinguish them whenever the resulting distributions are
statistically identifiable.

## Redundancy classes

- A primitive measurable from `R` is redundant.
- Model-independent noise can enlarge the sample space but cannot identify
  the latent representative.
- Rank or ordinal marks remain invariant under strictly increasing
  transformations.
- A numerical mark whose calibration is allowed to transform covariantly may
  also remain invariant.

## Minimal alphabet

A one-symbol mark is constant and cannot change a probability law. A binary
mark is therefore the smallest nontrivial alphabet. A Bernoulli mark with
different success probabilities in two models is sufficient for asymptotic
statistical separation.

This is minimal only in alphabet cardinality. It says nothing about physical
naturalness, locality, units, or whether the required calibration exists.
