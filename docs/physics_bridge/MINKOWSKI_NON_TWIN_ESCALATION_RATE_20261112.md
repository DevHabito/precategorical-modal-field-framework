# Theorem: non-twin implication-escalation failures are subleading

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic quantitative refinement of implication-edge escalation  
**Physical status:** local forcing-defect hierarchy after causal-arrow erasure  
**Novelty status:** forcing classes are classical; the quantitative Minkowski rate is project-specific

## 1. Statement

Fix an integer spacetime dimension

\[
d\ge3.
\]

Let

\[
\beta_d
=
\min\left(
d,\,
2+\frac4d
\right).
\]

Let \(R_n\) count sampled comparable edges \(e\) satisfying all three conditions:

1. \(\Delta_d(e)<\delta_0\);
2. \(e\) has at least one sampled splitter;
3. no sampled splitter directly forces \(e\) to an edge \(e'\) with
   \[
   \Delta_d(e')>2\Delta_d(e).
   \]

Then, for sufficiently small fixed \(\delta_0\),

\[
\boxed{
\mathbb E[R_n]
=
O(
n^{1-\beta_d}
).
}
\]

Consequently,

### d = 3

\[
\boxed{
\mathbb E[R_n]
=
O(n^{-2}).
}
\]

### d >= 4

\[
\boxed{
\mathbb E[R_n]
=
O(n^{-1-4/d}).
}
\]

Thus every non-twin microscopic implication-escalation failure is lower order than the comparable true-twin scale.

## 2. Splitter geometry of one edge

For a comparable continuum edge

\[
e=\{x,y\},
\]

write

\[
\delta
=
\Delta_d(x,y)
=
\mu(A_x\triangle A_y).
\]

The splitter region of \(e\) is exactly

\[
A_x\triangle A_y.
\]

A sampled splitter \(z\) is comparable to exactly one endpoint.

Hence it directly forces \(e\) with one new edge:

\[
e_z=\{x,z\}
\]

or

\[
e_z=\{y,z\}.
\]

## 3. Constant-factor bad splitters

Call a splitter \(z\) **bad** when

\[
\Delta_d(e_z)\le2\delta.
\]

If \(z\) is comparable to \(x\), then

\[
z\in B_{2\delta}(x),
\]

and similarly for \(y\).

The uniform comparable-ball theorem gives

\[
\sup_u
\mu(B_t(u))
=
O(t^2).
\]

Therefore

\[
\boxed{
\mu(
\text{bad splitters of }e
)
\le
C_d\delta^2.
}
\]

The total splitter mass is exactly

\[
\delta.
\]

Thus, for sufficiently small fixed \(\delta_0\),

\[
0<\delta<\delta_0
\]

implies

\[
\boxed{
\mu(
\text{good splitters}
)
\ge
\frac{\delta}{2}.
}
\]

## 4. Conditional residual probability

Condition on a sampled comparable edge with disagreement \(\delta<\delta_0\).

Let

\[
b(\delta)
\le
C\delta^2
\]

be its bad-splitter mass and let

\[
g(\delta)
\ge
\frac{\delta}{2}
\]

be its good-splitter mass.

The event counted by \(R_n\) requires:

- no one of the remaining \(n-2\) sampled vertices falls in the good region;
- at least one falls in the bad region.

A union bound over the possible first bad sampled point gives

\[
\begin{aligned}
\Pr(
e\text{ counted by }R_n
\mid e
)
&\le
(n-2)b(\delta)
(1-g(\delta))^{n-3}\\
&\le
Cn\delta^2
e^{-cn\delta}.
\end{aligned}
\]

The zero-splitter event is excluded from \(R_n\).

That zero-splitter event is precisely the true-twin mechanism.

## 5. Integrating over sampled edges

The expected number of residual edges is bounded by

\[
\mathbb E[R_n]
\le
Cn^3
\int_0^{\delta_0}
\delta^2
e^{-cn\delta}
\,dF_d(\delta),
\]

where

\[
F_d(t)
=
\Pr(
X\sim Y,\,
\Delta_d(X,Y)\le t
).
\]

The all-dimensional edge-tail theorem gives

\[
F_d(t)
=
O(t^{\beta_d}).
\]

A Laplace-Stieltjes estimate yields

\[
\int_0^{\delta_0}
\delta^2
e^{-cn\delta}
\,dF_d(\delta)
=
O(
n^{-\beta_d-2}
).
\]

Hence

\[
\boxed{
\mathbb E[R_n]
=
O(
n^{1-\beta_d}
).
}
\]

## 6. Comparison with true twins

For \(d\ge4\),

\[
\Pr(T_n>0)
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
\]

The residual escalation rate is

\[
O(n^{-1-4/d}).
\]

Therefore

\[
\boxed{
\Pr(R_n>0)
=
o(
\Pr(T_n>0)
).
}
\]

For \(d=3\), true twins have expectation \(O(n^{-1})\), while residual escalation failures are \(O(n^{-2})\).

Thus the same one-power separation holds.

## 7. Simultaneous forcing consequence

Outside an event of probability

\[
O(
n^{1-\beta_d}
),
\]

every sampled low-disagreement edge satisfies one of two alternatives:

1. it has no sampled splitter and is therefore a comparable true-twin edge;
2. it directly forces an edge whose disagreement is more than twice as large.

If there are no true twins and no residual edges, repeated direct forcing sends every implication class from any low-disagreement edge to the fixed core

\[
\Delta_d\ge\delta_0.
\]

The number of constant-factor escalation steps from a disagreement \(\delta\) is finite and at most logarithmic in \(\delta_0/\delta\).

No additional probability union bound is needed because the residual-edge event was already defined simultaneously over every sampled low edge.

## 8. Quantitative frontier

For \(d\ge4\), after removing the true-twin event, every remaining local forcing defect is already

\[
O(n^{-1-4/d}).
\]

The matching upper bound

\[
1-p_d^{\mathrm{UPO}}(n)
\le
(K_d^{\mathrm{twin}}+o(1))
n^{-4/d}
\]

therefore cannot fail because of another microscopic implication-class mechanism.

Any competing contribution at order \(n^{-4/d}\) would have to come from a macroscopic or near-whole modular event.

Those are now the only quantitative regimes requiring sharper bounds.
