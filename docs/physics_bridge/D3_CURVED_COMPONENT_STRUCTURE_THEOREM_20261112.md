# Theorem: component structure and non-twin component rate in regular curved 2+1 diamonds

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic stochastic theorem under the regular curved \(2+1\) geometric estimates  
**Physical status:** dedicated curved proof of the one-nontrivial-component property and its non-twin quantitative refinement

## 1. Setting

Let

\[
D=I(p,q)
\]

be a regular curved \(2+1\) Alexandrov interval satisfying the hypotheses of the curved low-degree, comparable-ball, small-disagreement, and graphon-prime theorems.

Let

\[
G_n
\]

be the undirected causal-comparability graph of \(n\) iid physical-volume samples.

Write

\[
Q(x)=\mu(A_x)
\]

for the continuum graphon degree.

Assume the established curved estimates

\[
\boxed{
g(q)
:=
\mu\{Q\le q\}
\le
Cq^{4/3},
}
\]

and

\[
\boxed{
\sup_{x\in S_t}
\mu(A_x\cap S_t)
\le
Ct^2,
}
\]

where

\[
S_t=\{Q\le t\}.
\]

## 2. Qualitative statement

\[
\boxed{
\Pr(
G_n
\text{ has more than one connected component containing an edge}
)
\to0.
}
\]

Equivalently, with probability tending to one, all nonisolated sampled vertices lie in one connected component.

## 3. Degree-escalation parameter

Choose

\[
\alpha\in(1/2,1).
\]

For a sampled point \(x\) with continuum degree

\[
Q(x)=q<q_0,
\]

put

\[
t=q^\alpha.
\]

Since \(q<t\),

\[
x\in S_t.
\]

Internal sparsity gives

\[
h(x)
:=
\mu(A_x\cap S_{q^\alpha})
\le
Cq^{2\alpha}.
\]

Because

\[
2\alpha>1,
\]

choose \(q_0\) so small that

\[
h(x)\le\frac q2.
\]

## 4. Bad low-degree vertices

Call \(x\) bad when:

1. \(Q(x)=q<q_0\);
2. \(x\) has at least one sampled neighbor;
3. every sampled neighbor \(y\) has
   \[
   Q(y)\le q^\alpha.
   \]

Conditioned on \(x\),

\[
\begin{aligned}
\Pr(x\text{ bad}\mid x)
&=
(1-q+h)^{n-1}
-
(1-q)^{n-1}\\
&\le
Cnq^{2\alpha}e^{-cnq}.
\end{aligned}
\]

Let \(B_n\) be the number of bad sampled vertices.

Then

\[
\mathbb E[B_n]
\le
Cn^2
\int_0^{q_0}
q^{2\alpha}
e^{-cnq}
\,dg(q).
\]

Using

\[
g(q)\le Cq^{4/3},
\]

the Laplace-Stieltjes estimate gives

\[
\mathbb E[B_n]
=
O(
n^{2-2\alpha-4/3}
)
=
O(
n^{2/3-2\alpha}
).
\]

Since

\[
\alpha>1/2,
\]

\[
2/3-2\alpha<-\frac13.
\]

Therefore

\[
\boxed{
\Pr(B_n>0)\to0.
}
\]

## 5. Every nonisolated low-degree vertex reaches the core

Work on

\[
B_n=0.
\]

Let \(v_0\) be a nonisolated sampled vertex with

\[
Q(v_0)<q_0.
\]

Because it is not bad, it has a sampled neighbor \(v_1\) satisfying

\[
Q(v_1)>Q(v_0)^\alpha>Q(v_0).
\]

If \(Q(v_1)<q_0\), repeat.

This gives a finite graph path

\[
v_0\sim v_1\sim\cdots
\]

with strictly increasing continuum degree until the path reaches

\[
K_{q_0}
=
\{Q\ge q_0\}.
\]

Hence every nonisolated low-degree sampled vertex is connected to the sampled macroscopic-degree core.

## 6. Connectivity of the core

The degree function \(Q\) is continuous on the regular compact diamond interior and extends continuously away from the null-edge singular set relevant to \(Q=0\).

The set

\[
K_{q_0}
\]

is compact and separated from the low-degree null edge.

For each

\[
x\in K_{q_0},
\]

there exists:

- a neighborhood \(U_x\);
- a positive-volume anchor set \(B_x\);

such that every point of \(U_x\) is timelike comparable to every point of \(B_x\).

Choose the anchors inside finitely many overlapping chronological regions forming a connected finite chain through the diamond.

Compactness gives a finite subcover

\[
U_1,\ldots,U_m
\]

and positive-measure anchors

\[
B_1,\ldots,B_m.
\]

The probability that any fixed \(B_i\) is empty is exponentially small.

By a finite union bound, with probability

\[
1-e^{-\Theta(n)},
\]

all anchors are occupied.

Their prescribed chronological overlaps connect all sampled core vertices into one graph component.

Therefore every nonisolated sampled vertex lies in one component with probability tending to one.

This proves

\[
\boxed{
\Pr(
\text{more than one edge-containing component}
)
\to0.
}
\]

## 7. Quantitative non-twin refinement

Let \(T_n\) count comparable true-twin pairs.

Let \(R_n\) be the residual implication-escalation count: low-disagreement sampled edges that have at least one splitter but no splitter forcing an edge with more than twice the disagreement.

The curved small-edge tail is

\[
F(t)=\Theta(t^3),
\]

and the curved uniform comparable-ball estimate is

\[
O(t^2).
\]

The non-twin escalation calculation therefore gives

\[
\boxed{
\Pr(R_n>0)
=
O(n^{-2}).
}
\]

Work on

\[
T_n=0,
\qquad
R_n=0.
\]

## 8. Every edge-containing component reaches a core edge

Take any sampled edge \(e\).

If

\[
\Delta(e)\ge\delta_0,
\]

it is already a core edge.

Otherwise \(e\) is not a true twin, so it has at least one sampled splitter.

Since \(R_n=0\), there is a directly forced edge \(e_1\) satisfying

\[
\Delta(e_1)>2\Delta(e).
\]

Repeat.

The disagreement doubles at each low-edge step, so after finitely many steps the implication class reaches an edge

\[
e_*
\]

with

\[
\Delta(e_*)\ge\delta_0.
\]

Each direct forcing step shares a sampled vertex with the previous edge.

Hence the full forcing chain stays inside the connected component of the original edge.

Therefore

\[
\boxed{
\text{every edge-containing component contains a core edge.}
}
\]

## 9. Core edges force linear component size

For a core edge \(e\),

\[
\Delta(e)\ge\delta_0.
\]

Its sampled splitter count is

\[
S_e
\sim
\operatorname{Binomial}
(n-2,\Delta(e)).
\]

Every splitter is connected to one endpoint of \(e\), hence belongs to the same graph component.

Choose

\[
c_0<\delta_0/2.
\]

Chernoff gives

\[
\Pr(
S_e<c_0n
)
\le
e^{-cn}.
\]

There are at most \(n^2/2\) sampled edges, so uniformly over all core edges,

\[
\boxed{
S_e\ge c_0n
}
\]

outside an \(e^{-\Theta(n)}\) event.

Thus every edge-containing component has size at least

\[
c_0n
\]

outside the true-twin/residual events.

## 10. Two edge-containing components imply a balanced module

Suppose there are at least two edge-containing components.

Each has size at least

\[
c_0n.
\]

Choose one component \(C\).

Then

\[
c_0n
\le
|C|
\le
(1-c_0)n.
\]

Every connected component is a graph module because every outside vertex is anticomplete to it.

Hence \(C\) is a balanced module.

## 11. Curved graphon primeness excludes balanced components

The Lorentzian causal-comparability graphon on \(D\) is prime.

For the fixed balance parameter \(c_0\), the graphon is separated by positive cut distance from the class of graphons possessing a homogeneous set of measure in

\[
[c_0,1-c_0].
\]

The standard Second Sampling Lemma therefore gives, for sufficiently large \(n\),

\[
\Pr(
\text{balanced module of this size exists}
)
\le
\exp\left(
-\frac{n}{2\log n}
\right).
\]

Thus

\[
\boxed{
\Pr(
\text{at least two edge-containing components},
\ T_n=0
)
=
O(n^{-2})
+
\exp\left(
-\frac{n}{2\log n}
\right)
+
e^{-\Theta(n)}.
}
\]

In particular,

\[
\boxed{
\Pr(
\text{component ambiguity without true twins}
)
=
o(n^{-1}).
}
\]

## 12. Role in the curved recovery law

The leading curved true-twin occurrence probability is

\[
\Pr(T_n>0)
\sim
K_{3,g}n^{-1}.
\]

The present theorem proves that disconnected nontrivial components contribute only

\[
O(n^{-2})
+
\text{superpolynomial}.
\]

Therefore component ambiguity cannot modify the leading curved recovery constant.

## 13. Dependency list

This proof uses only the already separated curved inputs:

1. low-degree tail
   \[
   g(q)=O(q^{4/3});
   \]
2. internal low-degree sparsity
   \[
   O(t^2);
   \]
3. small-edge tail
   \[
   \Theta(t^3);
   \]
4. uniform comparable-ball
   \[
   O(t^2);
   \]
5. Lorentzian causal-graphon primeness;
6. standard concentration and graphon sampling.

No step invokes the final curved orientation-recovery theorem.

Thus the earlier documentation gap is closed without circularity.
