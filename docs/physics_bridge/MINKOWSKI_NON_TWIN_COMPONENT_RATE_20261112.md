# Theorem: non-twin component ambiguity is subleading

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic quantitative component theorem  
**Physical status:** rate bound for multiple edge-containing components after causal-arrow erasure  
**Novelty status:** graph components and modules are classical; the quantitative Minkowski bound combines project-specific edge escalation with graphon sampling separation

## 1. Statement

Fix an integer spacetime dimension

\[
d\ge3.
\]

Let \(T_n\) be the number of comparable true-twin pairs.

Let \(\mathcal C_n\) be the event that the sampled comparability graph has at least two connected components containing an edge.

Then

\[
\boxed{
\Pr(
\mathcal C_n,\,
T_n=0
)
=
O(
n^{1-\beta_d}
)
+
\exp\!\left(
-\frac{n}{2\log n}
\right)
+
e^{-\Theta(n)},
}
\]

where

\[
\beta_d
=
\min\left(
d,\,
2+\frac4d
\right).
\]

For every fixed

\[
d\ge4,
\]

\[
\boxed{
\Pr(
\mathcal C_n,\,
T_n=0
)
=
O(
n^{-1-4/d}
)
+
\exp\!\left(
-\frac{n}{2\log n}
\right).
}
\]

Thus non-twin component ambiguity is

\[
o(n^{-4/d}).
\]

## 2. Residual escalation event

Let \(R_n\) be the number of low-disagreement edges that:

1. have at least one sampled splitter;
2. have no sampled splitter forcing an edge whose disagreement is more than twice as large.

The quantitative escalation theorem gives

\[
\boxed{
\mathbb E[R_n]
=
O(
n^{1-\beta_d}
).
}
\]

Hence

\[
\Pr(R_n>0)
=
O(
n^{1-\beta_d}
).
\]

Work outside this event and outside the true-twin event.

## 3. Every edge reaches the core

Take any sampled edge

\[
e.
\]

If its disagreement is already at least the fixed threshold

\[
\delta_0,
\]

it is a core edge.

Otherwise, since \(e\) is not a true twin, it has at least one sampled splitter.

Because \(R_n=0\), it directly forces an edge \(e_1\) satisfying

\[
\Delta(e_1)>2\Delta(e).
\]

Repeat.

The disagreement strictly increases by a factor greater than two at every low-disagreement step.

Therefore, after finitely many forcing steps, the implication class reaches an edge

\[
e_*
\]

with

\[
\Delta(e_*)\ge\delta_0.
\]

All forcing steps remain inside the connected component of the starting edge, because each new edge shares a vertex with the previous one.

Thus:

\[
\boxed{
\text{every edge-containing component contains a core edge.}
}
\]

## 4. Core edges force linear components

Let

\[
e=\{x,y\}
\]

be a core edge.

Its continuum splitter volume satisfies

\[
\Delta(e)\ge\delta_0.
\]

Among the other \(n-2\) sample points, the number of splitters is

\[
S_e
\sim
\operatorname{Binomial}
(n-2,\Delta(e)).
\]

Every splitter is adjacent to exactly one endpoint of \(e\).

Therefore every sampled splitter lies in the same connected component as \(e\).

A Chernoff bound gives a constant

\[
c_0=c_0(d,\delta_0)>0
\]

such that

\[
\Pr(
S_e<c_0n
)
\le
e^{-c n}.
\]

There are at most

\[
\binom n2
\]

sampled edges.

Hence, except with probability

\[
e^{-\Theta(n)},
\]

every core edge simultaneously belongs to a connected component of size at least

\[
\boxed{
c_0n.
}
\]

## 5. Two nontrivial components imply a balanced module

Suppose there are at least two edge-containing components.

On the good event above, each has size at least

\[
c_0n.
\]

Choose one such component \(C\).

Because another component has at least \(c_0n\) vertices,

\[
|C|
\le
(1-c_0)n.
\]

Thus

\[
c_0n
\le
|C|
\le
(1-c_0)n.
\]

Every connected component is a graph module: every outside vertex is anticomplete to it.

Therefore \(C\) is a balanced module.

## 6. Quantitative balanced-module exclusion

The balanced-module rate theorem gives

\[
\Pr(
\exists\text{ module }M:
c_0n\le|M|\le(1-c_0)n
)
\le
\exp\!\left(
-\frac{n}{2\log n}
\right)
\]

for all sufficiently large \(n\).

Thus, outside:

- the residual escalation event;
- the exponentially small core-concentration failure;
- the superpolynomial balanced-module event;

there cannot be two edge-containing components.

This proves

\[
\boxed{
\Pr(
\mathcal C_n,\,
T_n=0
)
=
O(
n^{1-\beta_d}
)
+
\exp\!\left(
-\frac{n}{2\log n}
\right)
+
e^{-\Theta(n)}.
}
\]

## 7. d >= 4 consequence

For

\[
d\ge4,
\]

\[
\beta_d
=
2+\frac4d.
\]

Hence

\[
n^{1-\beta_d}
=
n^{-1-4/d}.
\]

The comparable true-twin occurrence probability is

\[
\Pr(T_n>0)
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
\]

Therefore

\[
\boxed{
\Pr(
\mathcal C_n,\,
T_n=0
)
=
o(
\Pr(T_n>0)
).
}
\]

Multiple-component ambiguity cannot alter the leading true-twin constant.

## 8. Quantitative inventory

For fixed \(d\ge4\), the currently verified non-twin failure mechanisms satisfy:

### Fixed-size non-twin modules

\[
O(n^{-1-4/d}).
\]

### Residual low-edge forcing failures

\[
O(n^{-1-4/d}).
\]

### Multiple edge-containing components without true twins

\[
O(n^{-1-4/d})
+
\text{superpolynomial}.
\]

### Balanced macroscopic modules

\[
\exp\!\left(
-\frac{n}{2\log n}
\right).
\]

### Near-whole modules

\[
O(n^{1-d}).
\]

Every item is

\[
o(n^{-4/d}).
\]

Thus the quantitative proof chain now has no remaining non-twin component obstruction at the candidate leading scale.
