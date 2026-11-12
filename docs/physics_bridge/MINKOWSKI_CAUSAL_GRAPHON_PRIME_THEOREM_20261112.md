# Theorem: primeness of the Minkowski causal graphon and exclusion of balanced modules

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic continuum theorem + graphon-limit transfer theorem  
**Physical status:** internal modular structure of arrow-erased Minkowski causal sets  
**Novelty status:** weakly homogeneous graphon sets and coloured-graphon compactness are established; no equivalent primeness/exclusion theorem for the Minkowski causal-comparability graphon was located in the targeted review

## 1. Statement

Fix a spacetime dimension

\[
d\ge2.
\]

Let

\[
D=I((-1,\mathbf0),(1,\mathbf0))
\subset\mathbb M^d
\]

with normalized volume measure \(\mu\), and define the random-free causal-comparability graphon

\[
W_d(x,y)
=
\mathbf1_{\{x\sim y\}}.
\]

Then \(W_d\) has no nontrivial weakly homogeneous measurable set.

Equivalently:

\[
\boxed{
W_d
\text{ is prime in the measurable homogeneous-set sense.}
}
\]

As a finite-sample consequence, for every fixed

\[
\varepsilon\in(0,1/2),
\]

if \(G_{d,n}\) is the comparability graph of \(n\) iid uniform sprinkled events, then

\[
\boxed{
\Pr\!\left(
\exists\text{ graph module }M:
\varepsilon n\le |M|\le(1-\varepsilon)n
\right)
\longrightarrow0.
}
\]

The statement concerns modules of the full sampled graph.  In the UPO application, modularity is ultimately applied inside the unique nontrivial component; the distinction matters because isolated vertices can make that entire component a benign module of the full graph.

## 2. Weakly homogeneous sets

A measurable set

\[
S\subseteq D
\]

of positive measure is weakly homogeneous when there exists a measurable function

\[
e:D\setminus S\to\{0,1\}
\]

such that

\[
W_d(z,x)=e(z)
\]

for almost every pair

\[
(z,x)\in(D\setminus S)\times S.
\]

Thus almost every outside event is comparable either to almost every point of \(S\) or to almost none of \(S\).

This is the graphon analogue of a graph module/homogeneous set.

## 3. Pairwise splitter consequence

For

\[
x,y\in D,
\]

write

\[
A_x=\{z:z\sim x\}.
\]

If \(S\) is weakly homogeneous, Fubini's theorem gives a full-measure subset of pairs

\[
(x,y)\in S\times S
\]

for which

\[
\boxed{
\mu\!\left(
(A_x\triangle A_y)\setminus S
\right)
=
0.
}
\]

Indeed, an outside point in

\[
A_x\triangle A_y
\]

would distinguish \(x\) and \(y\), violating homogeneity.

Thus, for almost every pair of points of \(S\), almost every continuum splitter also lies in \(S\).

## 4. A positive-measure set contains a timelike pair

Let

\[
\mu(S)>0.
\]

Choose an interior Lebesgue-density point

\[
x\in S.
\]

Every sufficiently small neighborhood of \(x\) contains a positive-volume open timelike cone sector.

Since \(x\) is a density point, that timelike sector intersects \(S\) in positive measure.

Therefore \(S\) contains a strictly timelike pair

\[
x\ll y
\]

that may also be chosen from the full-measure Fubini-good pair set of the previous section.

Hence a positive-measure weakly homogeneous set contains a genuine continuum edge whose splitter region lies in \(S\) almost everywhere.

## 5. Continuum forcing relation

Two timelike edges

\[
xy,\qquad xz
\]

directly force one another when

\[
y
\]

and

\[
z
\]

are spacelike separated.

Then \(y\) and \(z\) are mutual splitters relative to the two edge endpoints, exactly as in classical transitive-orientation forcing.

The continuum timelike-edge forcing graph is connected.

### Fixed-endpoint spacelike chains

Fix an interior point \(x\).

The open set

\[
I^+(x)\cap D^\circ
\]

is path connected.

Any sufficiently small displacement in Minkowski space can be decomposed into two spacelike displacements.

Refining a polygonal path inside the open set therefore gives a finite chain

\[
y=y_0,y_1,\ldots,y_m=z
\]

such that every

\[
y_i,y_{i+1}
\]

is spacelike separated while every \(y_i\) remains strictly to the future of \(x\).

Thus all timelike edges

\[
xy_i
\]

belong to one continuum forcing class.

The time-reversed statement holds in \(I^-(x)\).

### Arbitrary timelike edges

Take two interior timelike edges

\[
(x,y),
\qquad
(x',y').
\]

Choose an interior event

\[
z\in I^+(x)\cap I^+(x').
\]

Such a point exists, for example sufficiently near the future tip while remaining in the interior.

Use fixed-endpoint spacelike chains to connect

\[
(x,y)
\longrightarrow
(x,z),
\]

then

\[
(x,z)
\longrightarrow
(x',z),
\]

and finally

\[
(x',z)
\longrightarrow
(x',y').
\]

Therefore all interior timelike edges lie in one continuum forcing class.

## 6. Robust forcing propagation inside a homogeneous set

The forcing paths above use only strict timelike and strict spacelike inequalities.

They are therefore robust under sufficiently small perturbations of their auxiliary points.

Start from the Fubini-good timelike edge

\[
x_0y_0
\subset S.
\]

At each direct forcing step, the next auxiliary point lies in an open positive-measure splitter neighborhood.

Because the current edge endpoints belong to \(S\) and are chosen from the Fubini-good set, almost every point of that splitter neighborhood lies in \(S\).

The next point can therefore be chosen:

1. inside \(S\);
2. inside the required robust splitter neighborhood;
3. inside the full-measure set needed to continue the Fubini argument.

Inductively, every finite robust continuum forcing path can be realized with all of its vertices in \(S\), up to null sets.

## 7. No nontrivial weakly homogeneous set

Suppose, for contradiction,

\[
0<\mu(S)<1.
\]

Since the complement has positive measure, choose an interior density point

\[
w\in D\setminus S.
\]

Choose a timelike partner \(v\) of \(w\) and a robust continuum forcing path from the initial edge \(x_0y_0\subset S\) to the edge \(vw\).

At the final step, robustness gives an open neighborhood

\[
U\ni w
\]

all of whose points are splitters of an edge whose two endpoints have already been propagated into \(S\).

The splitter consequence of weak homogeneity implies

\[
\mu(U\setminus S)=0.
\]

But \(w\) is a density point of \(D\setminus S\), so every sufficiently small neighborhood of \(w\) has positive complement measure.

This is a contradiction.

Hence

\[
\boxed{
\mu(S)=1.
}
\]

Together with the trivial null case, the causal graphon has no nontrivial weakly homogeneous measurable set.

## 8. Finite balanced modules

Fix

\[
\varepsilon\in(0,1/2).
\]

Suppose the balanced-module conclusion were false.

Then there would exist a subsequence \(n_j\to\infty\) and graph realizations

\[
G_{n_j}\sim G(n_j,W_d)
\]

such that:

1. the uncoloured graphons of \(G_{n_j}\) converge to \(W_d\);
2. each \(G_{n_j}\) has a module \(M_j\) with
   \[
   \varepsilon n_j
   \le
   |M_j|
   \le
   (1-\varepsilon)n_j.
   \]

The first condition can be imposed because \(G(n,W_d)\to W_d\) in cut distance with probability tending to one.

Colour the vertices of \(M_j\) red and all remaining vertices blue.

## 9. The coloured splitter density is zero

Because \(M_j\) is a module, there is no ordered triple

\[
(x,y,z)
\]

with:

- \(x,y\) red;
- \(z\) blue;
- \(z\) adjacent to exactly one of \(x,y\).

Thus the density of the corresponding coloured splitter pattern is exactly zero for every \(j\).

Finite-colour graphon compactness yields a convergent coloured subsequence.

The red mass in the limit lies in

\[
[\varepsilon,1-\varepsilon].
\]

The underlying uncoloured graphon remains equivalent to \(W_d\).

The limiting colouring may be mixed, so write its red weight as

\[
f:D\to[0,1],
\qquad
\int_D f\,d\mu
\in
[\varepsilon,1-\varepsilon].
\]

The coloured counting lemma transfers the zero splitter density to

\[
\int
f(x)f(y)(1-f(z))
\,
\mathbf1_{
\{W_d(z,x)\ne W_d(z,y)\}
}
\,
d\mu(x)d\mu(y)d\mu(z)
=
0.
\]

## 10. A mixed zero-splitter colouring creates a homogeneous set

Set

\[
R=\{x:f(x)>0\}.
\]

Since

\[
\int f>0,
\]

\[
\mu(R)>0.
\]

For almost every \(z\) with

\[
f(z)<1,
\]

the zero integral implies that

\[
W_d(z,x)
\]

is constant for almost every \(x\in R\).

If

\[
\mu(R)<1,
\]

then every point outside \(R\) has \(f(z)=0<1\), so \(R\) is a nontrivial weakly homogeneous set.

This contradicts the primeness theorem.

If instead

\[
\mu(R)=1,
\]

then because

\[
\int f\le1-\varepsilon,
\]

the set

\[
\{z:f(z)<1\}
\]

has positive measure.

For almost every such \(z\), the row

\[
W_d(z,\cdot)
\]

would be constant almost everywhere on all of \(D\).

That is impossible for an interior Minkowski event, whose causal-comparability degree satisfies

\[
0<Q_d(z)<1
\]

almost everywhere.

Thus the mixed case is impossible as well.

The assumed balanced modules therefore cannot exist.

Hence

\[
\boxed{
\Pr\!\left(
\exists M:
\varepsilon n\le|M|\le(1-\varepsilon)n
\right)
\to0.
}
\]

## 11. Relation to existing graphon theory

Hatami and Norin define weakly homogeneous graphon sets and show that they are the graphon counterpart of homogeneous sets/modules in finite graphs.

Recent work of Janson, Lo, McDiarmid, Skeja, and Skerman develops compactness and convergence theory for pure and mixed finite graphon colourings.  In particular, it provides the natural framework for passing graph partitions to graphon limits.

The present proof uses those established tools.

The project-specific content is:

1. proving that the Minkowski causal-comparability graphon is prime;
2. identifying continuum transitive-orientation forcing as the mechanism behind that primeness;
3. applying the result to eliminate balanced finite modules in arrow-erased Minkowski sprinklings.

## 12. What this does not yet exclude

The theorem excludes modules whose size and complement are both linear in \(n\).

It does not by itself exclude:

\[
|M|=o(n)
\]

or

\[
n-|M|=o(n).
\]

For \(d=4\), the small-side regime already has strong independent control:

\[
\Pr(
2\le|M|\le n^{1/2-\eta}
)
\to0
\]

for every fixed \(\eta>0\), and implication-edge escalation forces every remaining orientation class to reach a fixed positive-disagreement edge core.

The remaining possible obstruction at the time of this note was a near-whole internal module whose complement is sublinear.

That regime was subsequently excluded in

\[
\texttt{MINKOWSKI\_D4\_NEAR\_WHOLE\_EXCLUSION\_THEOREM\_20261112.md}.
\]

The assembled consequence is the full \(3+1\) orientation-recovery theorem

\[
p_4^{\mathrm{UPO}}(n)\to1.
\]
