# Theorem: all non-isolated vertices form one component in fixed-dimensional Minkowski sprinklings

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem + finite-n audit  
**Physical status:** component structure of arrow-erased Minkowski causal-set comparability graphs  
**Novelty status:** the graphon and concentration tools are classical; no equivalent all-non-isolated-one-component theorem for this Minkowski causal graphon family was located in the targeted review

## 1. Statement

Fix a spacetime dimension

\[
d\ge2.
\]

Let

\[
X_1,\ldots,X_n
\]

be iid uniform points in a flat Alexandrov interval

\[
D=I((-1,\mathbf0),(1,\mathbf0))
\subset\mathbb M^d.
\]

Form the undirected comparability graph

\[
G_{d,n}
\]

by joining \(i\) and \(j\) exactly when the sampled events \(X_i,X_j\) are causally comparable.

Then

\[
\boxed{
\Pr\!\left(
G_{d,n}
\text{ has more than one connected component containing an edge}
\right)
\longrightarrow0.
}
\]

Equivalently,

\[
\boxed{
\text{with probability tending to one, all non-isolated vertices lie in one component.}
}
\]

Thus asymptotically the graph has the form

\[
\boxed{
\text{one nontrivial component}
+
\text{isolated vertices}.
}
\]

The number of isolated vertices may vanish, remain tight, or diverge sublinearly depending on \(d\).

## 2. Graphon degree

Let

\[
W_d(x,y)=\mathbf1_{\{x\sim y\}}
\]

be the causal-comparability graphon, and define

\[
Q_d(x)
=
\int_D W_d(x,y)\,d\mu(y).
\]

The degree-tail theorem gives

\[
g_d(q)
:=
\mu\{x:Q_d(x)\le q\}
\sim
C_dq^{4/d},
\]

where

\[
C_d
=
d(d-1)
\frac{
\Gamma(1+2/d)^2
}{
\Gamma(1+4/d)
}.
\]

In particular, for sufficiently small \(q\),

\[
g_d(q)\le Cq^{4/d}.
\]

## 3. Low-degree-to-low-degree neighbor bound

For \(t>0\), define

\[
S_t
=
\{x:Q_d(x)\le t\}.
\]

There is a constant \(C_d'\) such that, for sufficiently small \(t\),

\[
\boxed{
\sup_{x\in S_t}
\mu(A_x\cap S_t)
\le
C_d't^2.
}
\]

Here

\[
A_x=\{y:y\sim x\}.
\]

### Geometric proof

The low-degree tail is concentrated near the codimension-two null joint.

For

\[
x,y\in S_t,
\]

their null-depth coordinates satisfy

\[
a,b=O(t^{2/d}).
\]

Therefore the available two-coordinate area for \(y\) is

\[
O(t^{4/d}).
\]

If \(x\) and \(y\) are comparable, their relative angular cap satisfies

\[
1-\cos\theta
=
O(t^{4/d}).
\]

The relative angular sphere has dimension

\[
d-2.
\]

Hence the cap measure is

\[
O\!\left(
t^{2(d-2)/d}
\right).
\]

Multiplying the null-coordinate and angular factors gives

\[
t^{4/d}
t^{2(d-2)/d}
=
t^2.
\]

The normalized density is bounded in the joint chart, so

\[
\mu(A_x\cap S_t)
=
O(t^2)
\]

uniformly.

For \(d=2\), the angular factor is absent and the same \(t^2\) order follows directly from the two null coordinates.

## 4. Degree escalation

Choose a number

\[
\alpha
\]

satisfying

\[
\boxed{
\max\!\left(
\frac12,
1-\frac2d
\right)
<
\alpha
<
1.
}
\]

Let a sampled vertex have continuum degree

\[
Q_d(x)=q.
\]

For \(q<q_0\), where \(q_0\) is sufficiently small, set

\[
t=q^\alpha.
\]

Since \(q<t\), we have \(x\in S_t\), and therefore

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

we may choose \(q_0\) small enough that

\[
h(x)\le\frac q2.
\]

## 5. A bad low-degree vertex

Call \(x\) **bad** if:

1. \(Q_d(x)=q<q_0\);
2. it has at least one sampled neighbor;
3. every sampled neighbor \(y\) satisfies
   \[
   Q_d(y)\le q^\alpha.
   \]

Conditioned on \(x\), the low-neighbor mass is \(h(x)\), while the total neighbor mass is \(q\).

Hence

\[
\begin{aligned}
\Pr(x\text{ bad}\mid x)
&=
(1-q+h)^{n-1}
-
(1-q)^{n-1}\\
&\le
(n-1)h
(1-q+h)^{n-2}\\
&\le
Cnq^{2\alpha}e^{-cnq}.
\end{aligned}
\]

## 6. Expected number of bad vertices

Let \(B_n\) be the number of bad sampled vertices.

Then

\[
\mathbb E[B_n]
\le
Cn^2
\int_0^{q_0}
q^{2\alpha}
e^{-cnq}
\,dg_d(q).
\]

Using

\[
g_d(q)\le Cq^{4/d},
\]

a standard Stieltjes/Laplace estimate gives

\[
\int_0^{q_0}
q^{2\alpha}
e^{-cnq}
\,dg_d(q)
=
O\!\left(
n^{-2\alpha-4/d}
\right).
\]

Therefore

\[
\boxed{
\mathbb E[B_n]
=
O\!\left(
n^{2-2\alpha-4/d}
\right).
}
\]

By the choice of \(\alpha\),

\[
2-2\alpha-\frac4d<0.
\]

Hence

\[
\boxed{
\mathbb E[B_n]\to0.
}
\]

Markov's inequality gives

\[
\boxed{
\Pr(B_n>0)\to0.
}
\]

For every fixed \(\eta>0\), choosing \(\alpha\) sufficiently close to \(1\) gives the quantitative form

\[
\Pr(B_n>0)
=
O\!\left(
n^{-4/d+\eta}
\right).
\]

## 7. Every non-isolated low-degree vertex reaches the core

Work on the event

\[
B_n=0.
\]

Let \(v\) be a non-isolated sampled vertex with

\[
Q_d(v)<q_0.
\]

Because \(v\) is not bad, it has a neighbor \(v_1\) with

\[
Q_d(v_1)
>
Q_d(v)^\alpha
>
Q_d(v).
\]

If

\[
Q_d(v_1)<q_0,
\]

apply the same argument to \(v_1\).

This creates a path

\[
v=v_0\sim v_1\sim v_2\sim\cdots
\]

with strictly increasing continuum degrees.

The finite graph contains only \(n\) vertices, so the path cannot continue forever without entering

\[
K_{q_0}
=
\{x:Q_d(x)\ge q_0\}.
\]

Thus every non-isolated low-degree sampled vertex is connected to a sampled vertex in the core \(K_{q_0}\).

## 8. Connectivity of the macroscopic-degree core

It remains to show that all sampled vertices in

\[
K_{q_0}
\]

belong to one component with probability tending to one.

The set \(K_{q_0}\) is compact and is disjoint from the null joint.

Every point \(x\in K_{q_0}\) is timelike related to at least one of the two Alexandrov endpoints.

Choose two sufficiently small fixed neighborhoods:

\[
P
\]

near the past tip and

\[
F
\]

near the future tip such that:

1. every point of \(P\cup F\) lies in \(K_{q_0}\);
2. every point of \(P\) is timelike before every point of \(F\).

For each \(x\in K_{q_0}\), openness of the timelike relation gives:

- a neighborhood \(U_x\) of \(x\);
- and a positive-measure anchor set
  \[
  B_x\subset P
  \quad\text{or}\quad
  B_x\subset F
  \]
  such that every point of \(U_x\) is comparable to every point of \(B_x\).

Compactness of \(K_{q_0}\) gives a finite subcover

\[
U_1,\ldots,U_m
\]

with positive-measure anchor sets

\[
B_1,\ldots,B_m.
\]

With probability

\[
1-e^{-\Theta(n)},
\]

the sample contains at least one point in every \(B_i\), and at least one point in both master regions \(P\) and \(F\).

Because

\[
P\prec F,
\]

all sampled anchor sets are connected through the two tip regions.

Every sampled core vertex lies in some \(U_i\) and therefore has an edge to the corresponding sampled anchor.

Hence the sampled core is contained in one connected component with probability tending to one.

## 9. Completion of the proof

With probability tending to one:

1. there are no bad low-degree vertices;
2. every non-isolated low-degree vertex reaches the core by an increasing-\(Q_d\) path;
3. all core vertices lie in one connected component.

Therefore every non-isolated sampled vertex lies in the same connected component.

Thus

\[
\boxed{
\Pr(
\text{more than one edge-containing component}
)
\to0.
}
\]

## 10. Consequence for 3+1 Minkowski spacetime

For \(d=4\),

\[
g_4(q)\sim3\pi q
\]

and

\[
\mathbb E[I_n]\to3\pi.
\]

So isolated vertices remain a genuine finite-probability phenomenon.

Nevertheless,

\[
\boxed{
\Pr(
\text{a second nontrivial component exists}
)
\to0.
}
\]

Thus the critical \(3+1\) graph asymptotically consists of:

\[
\boxed{
\text{one giant edge-containing component}
+
\text{isolated vertices only}.
}
\]

The isolated vertices do not create independent orientation choices.

## 11. Relation to the Hladký–Viswanathan critical regime

Hladký and Viswanathan prove that a connected graphon \(W\) yields an asymptotically connected graph \(G(n,W)\) exactly when

\[
g_W(q)=o(q).
\]

They explicitly identify the finite-positive regime

\[
\frac{g_W(q)}q\to\beta\in(0,\infty)
\]

as critical and leave a stronger relation between minimum degree and connectivity as Conjecture 14.

For \(d=4\),

\[
\frac{g_4(q)}q\to3\pi.
\]

The theorem above proves the \(K=1\) content of that conjectural picture for this specific critical graphon:

\[
\boxed{
\Pr(
\delta(G_{4,n})\ge1
\text{ and }
G_{4,n}\text{ disconnected}
)
\to0.
}
\]

The proof uses additional Lorentzian geometry,

\[
\mu(A_x\cap S_t)=O(t^2),
\]

which is not available for a general critical graphon.

## 12. Consequence for UPO recovery

The general UPO criterion for a nonempty comparability graph requires:

1. exactly one edge-containing connected component;
2. all other components isolated;
3. the unique nontrivial component is internally UPO.

The present theorem establishes conditions 1 and 2 asymptotically for every fixed Minkowski dimension.

Therefore the higher-dimensional orientation-recovery problem reduces asymptotically to a purely internal question:

\[
\boxed{
\text{Does the unique giant comparability component contain a proper non-stable module?}
}
\]

In \(d=4\), the known leading internal obstructions satisfy

\[
\mathbb E[T_n]
\sim
\frac{9\pi}{n}
\]

for true twins and

\[
\mathbb E[M_{3,n}]
=
\Theta(n^{-2})
\]

for induced-\(P_3\) modules.

The remaining frontier is now entirely the arbitrary-size internal modular-closure problem.

## 13. Finite-n diagnostic

The repository tool

tools/minkowski_degree_escalation_component_audit.py

checks the component structure and degree-escalation rule directly.

An independent session audit in \(d=4\) gave the following fractions of samples containing at least two nontrivial components:

| \(n\) | samples | fraction |
|---:|---:|---:|
|64|1200|0.1050|
|128|800|0.05375|
|256|400|0.03250|
|512|180|0.03333|
|1024|70|0.01429|

The second nontrivial component never exceeded size \(4\) in these runs and was size \(2\) at the two largest tested \(n\).

These data are diagnostic only.

The asymptotic theorem is analytic.

## 14. Literature boundary

The graphon model, graphon degree function, Chernoff/Laplace bounds, and compactness arguments are standard tools.

Relevant general literature includes:

- Svante Janson, **Connectedness in graph limits**, *European Journal of Combinatorics* 29 (2008), 1195–1211.
- Jan Hladký and Gopal Viswanathan, **Connectivity of Inhomogeneous Random Graphs II**, *Random Structures & Algorithms* 69 (2026), e70098, DOI 10.1002/rsa.70098.
- Mathew D. Penrose, **Inhomogeneous random graphs, isolated vertices, and Poisson approximation**, *Journal of Applied Probability* 55 (2018), 112–136, DOI 10.1017/jpr.2018.9.

No source located in the targeted review states the Minkowski-specific low-neighbor estimate

\[
\mu(A_x\cap S_t)=O(t^2)
\]

together with the degree-escalation consequence that every non-isolated vertex belongs asymptotically to one component.

This remains limited negative evidence only.
