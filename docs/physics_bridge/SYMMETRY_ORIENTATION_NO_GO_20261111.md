# Symmetry obstruction to deriving a canonical temporal orientation

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact structural no-go used as a pregeometric gate  
**Novelty status:** symmetry/automorphism reasoning is classical; no originality claim

## 1. The problem

Suppose a primitive timeless structure admits a symmetry that exchanges two candidate events or configurations.

Can a deterministic, label-invariant rule extract a strict direction between them from that structure alone?

In general, no.

This is the structural form of the requirement that an asymmetry cannot be produced canonically from perfectly symmetric input data without some additional symmetry-breaking ingredient.

## 2. Setup

Let

$$
\mathfrak P
$$

be a primitive structure.

Let

$$
\sigma:\mathfrak P\to\mathfrak P
$$

be an automorphism.

Suppose two elements satisfy

$$
\sigma(a)=b,
\qquad
\sigma(b)=a.
$$

Let a derived strict relation

$$
\prec_{\mathfrak P}
$$

be produced by a deterministic isomorphism-equivariant rule.

Equivariance requires

$$
x\prec_{\mathfrak P}y
\iff
\sigma(x)\prec_{\mathfrak P}\sigma(y).
$$

## 3. No-go theorem

Assume

$$
a\prec_{\mathfrak P}b.
$$

Applying equivariance gives

$$
\sigma(a)\prec_{\mathfrak P}\sigma(b).
$$

Therefore

$$
b\prec_{\mathfrak P}a.
$$

But a strict temporal/order relation is asymmetric:

$$
a\prec b
\Longrightarrow
\neg(b\prec a).
$$

Contradiction.

Hence

$$
\boxed{
\text{a swap symmetry forbids a canonical asymmetric orientation of the swapped pair}.
}
$$

## 4. General automorphism-orbit statement

Any derived structure obtained canonically from \(\mathfrak P\) must be invariant under

$$
\operatorname{Aut}(\mathfrak P).
$$

If one automorphism maps a proposed oriented pair

$$
(a,b)
$$

to its reverse

$$
(b,a),
$$

then no automorphism-invariant strict relation can contain that pair.

Thus the obstruction is not about two labels specifically.

It is about the automorphism orbit of the primitive data.

## 5. Consequence for time-direction proposals

A pregeometric proposal cannot obtain a unique arrow merely by:

- choosing the lower vertex label;
- selecting one arbitrary representative;
- choosing one topological sort;
- orienting a symmetric edge by implementation order;
- assigning a random but then unreported convention.

A physical orientation requires additional structure that distinguishes the alternatives.

Possible sources include:

- asymmetric boundary conditions;
- an asymmetric state;
- explicit symmetry breaking;
- spontaneous selection of a sector;
- an operationally meaningful asymmetric relation;
- a stochastic orientation with a declared probability law.

Each option is a separate physical hypothesis.

## 6. Spontaneous symmetry breaking does not remove the bookkeeping obligation

A symmetric law can admit asymmetric solutions.

This is not a contradiction.

But the asymmetric solution or sector becomes additional information.

If a project says that an arrow is selected spontaneously, it must specify:

1. the symmetric space of possibilities;
2. the mechanism or measure over sectors;
3. what observable distinguishes the selected sector;
4. whether opposite orientations are physically equivalent;
5. how the observed arrow becomes stable.

The direction is then not derivable from the symmetric relational structure alone.

## 7. Time-reversal benchmark

Fundamental dynamical laws are often approximately or exactly time-reversal invariant over the regime of interest.

This is why the arrow-of-time problem is normally separated from the existence of dynamical evolution.

A time-symmetric law can support histories related by reversal.

To select one macroscopic arrow, accounts typically invoke ingredients such as asymmetric boundary conditions, low-entropy initial conditions, cosmological structure, coarse graining, or symmetry breaking.

The repository should follow the same discipline.

## 8. Relation to Blackwell and causal-order audits

The previous timeless candidates failed for complementary reasons.

### Blackwell order

Reversible transformations can remain informationally equivalent.

### Observational causal orientation

Markov-equivalent DAGs can leave direction underdetermined.

### Symmetry obstruction

Even before statistics are considered, a primitive automorphism can make an orientation impossible to select canonically.

Together these results say:

$$
\boxed{
\text{direction requires genuine asymmetric information}.
}
$$

They do not say what that information must be.

## 9. Relation to SCC condensation

SCC condensation is canonical because it does not choose a direction inside a strongly connected symmetric/cyclic sector.

It collapses that sector instead.

This is mathematically consistent with the symmetry gate.

But the price is information loss.

Thus SCC condensation avoids an arbitrary orientation by refusing to manufacture one.

## 10. Relation to Page-Wootters

Relational evolution does not require a global arrow.

A clock can parameterize reversible conditional evolution.

Therefore the inability to canonically orient a symmetric primitive structure does not imply that no relational dynamics can exist.

It blocks only the extraction of a unique strict arrow from the symmetric data alone.

## 11. Formal kernel

The repository formalizes the smallest logical core separately:

if a strict relation is invariant under a transformation that swaps \(a\) and \(b\), then the relation cannot orient \(a\) toward \(b\).

The Lean theorem is intentionally generic and contains no physical interpretation.

## 12. Pregeometric gate

Before promoting any derived relation as a temporal orientation:

1. compute or characterize relevant automorphisms of the primitive structure;
2. test whether an automorphism reverses the proposed oriented pair/order;
3. if yes, identify the additional symmetry-breaking data;
4. declare whether that data are primitive, boundary, state-dependent, stochastic, or emergent;
5. do not hide the choice inside labels or implementation details.

## 13. Current conclusion

The origin-of-direction question has become sharper:

> What non-temporal asymmetric structure, if any, is physically justified strongly enough to break the reversal symmetries of the primitive model?

Until such a structure is identified, a canonical temporal arrow cannot be derived from a symmetric relational substrate.
