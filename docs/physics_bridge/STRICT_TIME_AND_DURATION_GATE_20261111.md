# Strict temporal rank and duration — acyclicity and refinement gates

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** mathematical governance gate for any pregeometric time proposal  
**Novelty status:** DAG/topological-order and causal-set distance results are classical

## 1. Two problems that must not be conflated

A temporal construction has at least two logically distinct tasks.

### Ordering

Determine when one event/configuration can be said to precede another.

### Duration

Assign a quantitative interval between ordered events/configurations.

An acyclic order solves only the first problem.

A numerical graph statistic does not automatically solve the second.

## 2. Strict scalar rank requires acyclicity

Let

$$
G=(V,E)
$$

be a finite directed graph.

Suppose there exists a scalar function

$$
\tau:V\to\mathbb R
$$

such that

$$
u\to v
\quad\Longrightarrow\quad
\tau(u)<\tau(v).
$$

Then \(G\) cannot contain a directed cycle.

Indeed, a cycle

$$
v_0\to v_1\to\cdots\to v_k=v_0
$$

would imply

$$
\tau(v_0)
<
\tau(v_1)
<
\cdots
<
\tau(v_0),
$$

which is impossible.

Conversely, every finite DAG admits a topological ordering and therefore an injective integer rank that increases along every edge.

Thus

$$
\boxed{
\text{finite directed graph admits a strict edge-increasing rank}
\iff
\text{it is acyclic}.
}
$$

This is classical graph theory.

## 3. Consequence for reversible/cyclic primitive relations

If the primitive relation contains cycles representing physically meaningful reversible change, no single strict scalar time can increase along every primitive relation.

Any proposed construction must therefore do at least one of:

1. quotient cyclic sectors;
2. orient/remove some relations;
3. enlarge the state to include additional information;
4. abandon the requirement that the scalar be strictly increasing on every microscopic transition.

Each option changes the physical claim.

The change must be explicit.

## 4. SCC quotient is canonical but lossy

Strongly connected component condensation supplies a canonical acyclic quotient.

This solves the acyclicity problem mathematically.

But it identifies all states inside one mutually reachable sector.

The repository's formal C1 work already contains explicit graph-level non-injectivity evidence for quotient-type encodings.

Therefore:

$$
\boxed{
\text{acyclic macro-order can be obtained by losing micro-relational information}.
}
$$

That may be physically appropriate for an irreversible macro-description.

It is not a reconstruction of microscopic time.

## 5. Acyclic order still does not provide duration

Suppose the quotient contains

$$
A\prec B.
$$

One might propose that duration is the number of links or nodes along a path.

But consider two descriptions.

### Description 1

$$
A\to B.
$$

### Description 2

$$
A\to X\to B.
$$

After forgetting the refinement node \(X\), both express the same coarse reachability

$$
A\prec B.
$$

Yet their path lengths are different.

Therefore raw chain length depends on the chosen resolution.

Without an independent rule explaining what one primitive element represents physically, link count is not a physical duration.

## 6. Longest-path depth is not automatically a clock

A DAG can have multiple paths of different lengths between the same endpoints.

Choosing:

- shortest path;
- longest path;
- number of vertices in an interval;
- topological level

produces different numerical functions.

Graph theory alone does not select one as proper time.

A physical theory must provide the correspondence.

## 7. Causal-set benchmark

Causal-set theory provides an important benchmark.

Its programme combines:

$$
\boxed{
\text{order}+\text{number}
}
$$

to recover Lorentzian geometry under appropriate continuum correspondence.

For timelike-separated sprinkled events, longest-chain length has a statistical relation to continuum proper time in suitable high-density limits.

This works because the causal-set programme includes additional physical structure and assumptions:

- the partial order is interpreted causally;
- local finiteness supplies discreteness;
- element number corresponds statistically to spacetime volume;
- sprinkling density sets a scale;
- continuum approximation is tested.

The present repository does not yet have analogous ingredients.

Therefore it may not import

$$
\text{chain length}=\text{proper time}
$$

by analogy.

## 8. Refinement-invariance gate

Any candidate duration \(D(a,b)\) derived from primitive relational structure must state how it behaves under physically irrelevant refinement.

Possible acceptable behaviours include:

1. exact invariance;
2. convergence under a controlled refinement limit;
3. a known rescaling law with an independently fixed density/scale.

If arbitrary insertion of intermediate relational states changes the duration without a compensating rule, the candidate fails as a physical metric.

## 9. Multiple linear extensions are not multiple physical times

A partial order generally admits many topological sorts.

These linear extensions are bookkeeping choices unless a physical principle selects one.

Therefore:

$$
\boxed{
\text{topological index}
\neq
\text{derived physical time}
}
$$

without additional justification.

The partial order itself is the invariant object.

## 10. Formal kernel already available

The repository's explicit graphA contains a directed four-cycle.

A physical-bridge Lean module now states the finite core:

> no rational scalar rank can increase strictly along every graphA edge.

The same module also records that multiple distinct vertices in that cycle belong to one SCC and are therefore collapsed by the SCC quotient.

The formal proof certifies only this finite algebraic obstruction.

## 11. Relation to entropy clocks

Entropy or another monotone can provide an arrow or an internal clock on a restricted family of histories.

But reversible dynamics can continue while the monotone is constant, and fluctuations can complicate strict monotonicity.

Thus an entropy clock should be classified as:

$$
\boxed{
\text{state-dependent temporal parameterization under stated conditions}
}
$$

rather than automatically as the origin of all physical time.

Current 2026 literature continues to debate the distinction between entropy, irreversibility, temporal orientation, and time itself.

## 12. Current pregeometric status

The repository now has:

- rejected information degradation as universal time;
- rejected observational conditional independence as a unique direction generator;
- identified SCC condensation as a valid timeless macro-order construction;
- proved that cyclic primitive relations obstruct a strict scalar rank;
- identified duration as a separate unresolved problem.

The strongest allowed claim is therefore:

> a canonical acyclic macro-order can be extracted from a cyclic relation by quotienting mutual reachability, but no physical duration or universal microscopic time has been derived.

## 13. Next obligation

A serious next candidate must address reversible change.

It must explain either:

1. why reversible microscopic sectors should be quotiented before temporal structure is defined; or
2. how relational time can distinguish change inside a reversible sector without requiring a globally increasing scalar.

This is where relational-clock approaches become a more appropriate benchmark than thermodynamic monotones.
