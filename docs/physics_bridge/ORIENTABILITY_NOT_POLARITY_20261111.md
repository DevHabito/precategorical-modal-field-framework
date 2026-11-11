# Orientability is not polarity

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite symmetry audit + structural governance result  
**Novelty status:** graph orientations and automorphism stabilizers are classical; project role is to separate the existence of an invariant orientation from a physically selected direction

## 1. The new distinction

The recent symmetry audits separated:

- local pair orientation;
- cycle chirality;
- full distinguishing labels.

There is one further distinction that matters more for pregeometry:

$$
\boxed{
\text{an orientation can be symmetry-compatible without being physically selected}.
}
$$

Call these two questions:

1. **orientability:** does the marked structure permit an invariant acyclic orientation?
2. **polarity:** what selects one orientation rather than its global reverse?

They are not the same problem.

## 2. Invariant acyclic orientation

Let \(G\) be an undirected graph with marking \(\ell\).

Let

$$
H=\operatorname{Aut}(G,\ell)
$$

be the mark-preserving automorphism group.

An orientation \(O\) of every edge is \(H\)-invariant if every \(h\in H\) maps oriented edges to oriented edges with the same direction.

If the resulting digraph is acyclic, \(O\) supplies a partial-order candidate compatible with all remaining marked symmetries.

This is already stronger than local pair orientability.

## 3. Exact cycle audit

For each coloring of

$$
C_n,\qquad n=3,\ldots,8,
$$

with alphabets \(k=1,2,3\), the repository exhaustively enumerates all \(2^n\) edge orientations and asks whether at least one is:

- invariant under the coloring stabilizer;
- acyclic.

The number of colorings admitting at least one such orientation is:

| \(n\) | \(k=1\) | \(k=2\) | \(k=3\) |
|---:|---:|---:|---:|
|3|0|0|6|
|4|0|10|66|
|5|0|0|120|
|6|0|44|654|
|7|0|28|1638|
|8|0|202|6258|

## 4. GraphA C4 result

For the unmarked square:

$$
0/1
$$

colorings admit an invariant acyclic orientation.

With a binary vertex mark:

$$
\boxed{
10/16
}
$$

colorings admit at least one invariant acyclic orientation.

This is substantially weaker than full distinguishability:

- only 0 binary C4 colorings are fully distinguishing;
- yet 10 allow a symmetry-compatible acyclic orientation.

Therefore full graph rigidity is not required for an acyclic macro-order candidate.

## 5. Why some residual symmetry is harmless

A remaining automorphism can exchange branches or incomparable elements while preserving an oriented partial order.

Such a symmetry need not reverse any directed edge.

Therefore:

$$
\boxed{
\text{nontrivial automorphism group}
\not\Rightarrow
\text{no invariant partial order}.
}
$$

This is important because a physical order need not assign unique names to every event.

## 6. Global reversal degeneracy

Now comes the stronger obstruction.

Given any orientation \(O\), define its global reverse

$$
O^{\mathrm{op}}
$$

by reversing every edge.

If \(O\) is invariant under \(H\), then \(O^{\mathrm{op}}\) is also invariant under \(H\).

If \(O\) is acyclic, then \(O^{\mathrm{op}}\) is also acyclic.

Therefore the static marked graph alone does not prefer

$$
O
$$

over

$$
O^{\mathrm{op}}.
$$

So even when the automorphism obstruction has been removed,

$$
\boxed{
\text{orientability does not provide polarity}.
}
$$

## 7. Why this is not contradicted by scalar marks

Suppose a real scalar mark \(\varphi\) is supplied and all adjacent values differ.

One may define

$$
u\to v
\quad\Longleftrightarrow\quad
\varphi(u)<\varphi(v).
$$

This selects one orientation.

But the direction “lower to higher” is part of the rule.

The opposite rule

$$
u\to v
\quad\Longleftrightarrow\quad
\varphi(u)>\varphi(v)
$$

is equally well defined mathematically.

The static scalar values alone do not say which polarity has causal or temporal meaning.

A physical law or operational semantics must select the sign convention.

## 8. Examples of genuine polarity semantics

Established physics can provide polarity through additional meaning.

### Intervention and response

If changing a controllable mechanism at \(A\) changes outcome statistics at \(B\), the operational roles “intervention” and “response” provide an asymmetric semantic distinction.

### Boundary condition

A special preparation can select one relaxation sector rather than its reflected partner.

### Thermodynamic constitutive law

Given an already temporal dynamical framework, entropy production or dissipation can select an effective arrow.

### External field

A signed magnetic flux selects loop chirality, but the magnetic-ring bridge shows that chirality still need not produce vertex precedence.

Each case uses more than an untyped static mark.

## 9. Consequence for the primitive relation

A future pregeometric proposal needs to distinguish:

### Asymmetric data

Enough information to distinguish alternatives.

### Orientability

Enough structure to admit an invariant directed partial-order candidate.

### Polarity

A physical rule that tells which of reversed candidate directions has the intended causal/temporal semantics.

### Duration

A separate metric/clock calibration.

Skipping polarity risks hiding the desired arrow in a convention such as “increasing q means future.”

## 10. Exact computational boundary

The cycle audit is finite and exhaustive.

It proves only combinatorial existence of invariant acyclic orientations for the enumerated marked cycles.

It does not select one physical orientation and does not assign time semantics.

## 11. Current conclusion

The direction-source problem is now more precisely split:

$$
\boxed{
\text{symmetry breaking}
\to
\text{orientability}
\to
\text{polarity}
\to
\text{physical order}
\to
\text{duration}.
}
$$

The current repository has exact results for the first two stages on selected finite models.

The first stage not supplied by pure graph symmetry is now **polarity**.

That is the next foundational target.
