# Theorem: non-twin component ambiguity is second order in regular curved 2+1

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** analytic quantitative theorem under the regular curved \(2+1\) recovery hypotheses
**Physical status:** rate bound for disconnected edge-containing sectors after causal-arrow erasure

## 1. Statement

Let \(D=I(p,q)\) be a regular curved \(2+1\)-dimensional Lorentzian diamond satisfying the hypotheses of the curved small-edge, comparable-ball, and Lorentzian causal-graphon primeness theorems.

Let \(G_n\) be the sampled causal-comparability graph and let \(T_n\) count comparable true-twin pairs.

Let \(\mathcal C_n\) be the event that \(G_n\) has at least two connected components containing an edge.

Then

\[
\boxed{
\Pr(\mathcal C_n,\;T_n=0)
=
O(n^{-2})
+
\exp\!\left(-\frac{n}{2\log n}\right)
+
e^{-\Theta(n)}.
}
\]

Hence component ambiguity without a comparable true twin is \(o(n^{-1})\).

## 2. Curved small-edge inputs

The regular curved \(2+1\) edge tail is

\[
F_{3,g}(t)
=
\Pr(X\sim Y,\Delta_g(X,Y)\le t)
=
O(t^3).
\]

The uniform comparable-disagreement ball bound is

\[
\sup_x
\mu\{z:z\sim x,\Delta_g(x,z)\le t\}
=
O(t^2).
\]

These two estimates are the only local geometric inputs needed below.

## 3. Constant-factor residual escalation

Fix a sufficiently small \(\delta_0>0\).

For a comparable edge \(e=\{x,y\}\) with

\[
\delta=\Delta_g(e)<\delta_0,
\]

call a sampled splitter \(z\) bad if the directly forced new edge \(e_z\) satisfies

\[
\Delta_g(e_z)\le 2\delta.
\]

Every bad splitter lies in one of the two comparable balls

\[
B_{2\delta}(x)\cup B_{2\delta}(y).
\]

Therefore its continuum mass is

\[
O(\delta^2).
\]

The full splitter region has mass exactly \(\delta\).

For sufficiently small \(\delta_0\), the good-splitter mass is at least \(c\delta\).

Let \(R_n\) count sampled edges that

1. have \(0<\Delta_g(e)<\delta_0\);
2. have at least one sampled splitter;
3. have no sampled good splitter.

Conditioned on \(\Delta_g(e)=\delta\),

\[
\Pr(e\text{ counted by }R_n\mid e)
\le
Cn\delta^2e^{-cn\delta}.
\]

Thus

\[
\begin{aligned}
\mathbb E[R_n]
&\le
Cn^3
\int_0^{\delta_0}
\delta^2e^{-cn\delta}\,dF_{3,g}(\delta)\\
&=
O(n^{-2}).
\end{aligned}
\]

Hence

\[
\boxed{
\Pr(R_n>0)=O(n^{-2}).
}
\]

## 4. Every remaining edge reaches the core

Work on

\[
T_n=0
\]

and

\[
R_n=0.
\]

Take any sampled edge \(e\).

If

\[
\Delta_g(e)\ge\delta_0,
\]

it is already a core edge.

Otherwise, \(e\) is not a true twin, so it has a sampled splitter.

Since \(R_n=0\), one of its sampled splitters directly forces an edge \(e_1\) satisfying

\[
\Delta_g(e_1)>2\Delta_g(e).
\]

Repeat.

The disagreement increases by a factor greater than two at every low-disagreement step, so after finitely many steps the forcing chain reaches an edge \(e_*\) with

\[
\Delta_g(e_*)\ge\delta_0.
\]

Every forcing step shares a vertex with the previous edge, so the entire chain remains in the same connected component.

Therefore

\[
\boxed{
\text{every edge-containing component contains a core edge}
}
\]

outside the events \(T_n>0\) and \(R_n>0\).

## 5. Core edges force linear components

Condition on a sampled core edge \(e\).

Its splitter count is

\[
S_e\sim\operatorname{Binomial}(n-2,\Delta_g(e)),
\]

with mean at least

\[
\delta_0(n-2).
\]

There is a fixed \(c_0>0\) such that

\[
\Pr(S_e<c_0n)\le e^{-cn}.
\]

A union bound over at most \(\binom n2\) sampled edges gives

\[
\boxed{
S_e\ge c_0n
}
\]

simultaneously for every sampled core edge except with probability \(e^{-\Theta(n)}\).

Every sampled splitter is adjacent to exactly one endpoint of the core edge and therefore belongs to the same connected component.

Hence every edge-containing connected component has at least

\[
c_0n
\]

vertices.

## 6. Two edge-containing components imply a balanced module

If two edge-containing components exist, each has size at least

\[
c_0n.
\]

Choose one of them, \(C\).

Since another edge-containing component also contains at least \(c_0n\) vertices,

\[
c_0n
\le
|C|
\le
(1-c_0)n.
\]

Every connected component is a graph module, because every outside vertex is anticomplete to it.

Thus \(C\) is a \(c_0\)-balanced module.

## 7. Quantitative balanced-module exclusion in the curved graphon

The Lorentzian causal-comparability graphon is prime.

For fixed \(\varepsilon=c_0\), compactness of coloured graphons implies a positive cut-distance gap

\[
\rho_{g,c_0}>0
\]

between \(W_g\) and graphons carrying a homogeneous set of measure in

\[
[c_0,1-c_0].
\]

The graphon Second Sampling Lemma gives, for sufficiently large \(n\),

\[
\Pr\!\left(
\delta_\square(G(n,W_g),W_g)
>
\frac{22}{\sqrt{\log n}}
\right)
\le
\exp\!\left(
-\frac{n}{2\log n}
\right).
\]

Once

\[
22/\sqrt{\log n}<\rho_{g,c_0},
\]

a sampled \(c_0\)-balanced module is impossible on the sampling-good event.

Therefore

\[
\boxed{
\Pr(
\exists\ c_0\text{-balanced module}
)
\le
\exp\!\left(
-\frac{n}{2\log n}
\right).
}
\]

## 8. Conclusion

The event

\[
\{\mathcal C_n,\ T_n=0\}
\]

is contained in the union of

1. \(R_n>0\);
2. a core-edge splitter concentration failure;
3. a balanced-module sampling deviation.

Hence

\[
\boxed{
\Pr(\mathcal C_n,\;T_n=0)
=
O(n^{-2})
+
\exp\!\left(
-\frac{n}{2\log n}
\right)
+
e^{-\Theta(n)}.
}
\]

This is \(o(n^{-1})\).

Thus multiple edge-containing components cannot modify the leading curved \(2+1\) true-twin constant.
