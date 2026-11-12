# Theorem: asymptotic causal-orientation recovery in every fixed Minkowski dimension d >= 3

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** assembled analytic theorem for every fixed integer spacetime dimension \(d\ge3\)  
**Physical status:** reconstruction theorem for a declared arrow-erasure experiment in flat finite Minkowski Alexandrov intervals  
**Novelty status:** targeted literature review located classical UPO/comparability theory, random dimension-two orders, causal-set reconstruction work, and graphon homogeneous-set theory, but no equivalent higher-dimensional Minkowski arrow-erasure orientation-recovery theorem. Absolute novelty and priority are not certified.

## 1. Model

Fix an integer spacetime dimension

\[
d\ge3.
\]

Let

\[
D_d
=
I(p,q)
\subset
\mathbb M^d
\]

be a fixed flat Alexandrov interval of finite positive volume.

Condition a Poisson sprinkling on cardinality \(n\), equivalently sample

\[
X_1,\ldots,X_n
\]

iid uniformly with respect to Minkowski volume in \(D_d\).

Let \(P_{d,n}\) be the induced causal partial order.

Erase every causal arrow and retain only the symmetric comparability relation

\[
i\sim j
\quad\Longleftrightarrow\quad
i\prec j
\text{ or }
j\prec i.
\]

Let

\[
G_{d,n}
\]

be the resulting undirected comparability graph.

Null equality has probability zero and does not affect the random finite model.

## 2. Orientation-recovery event

Call the sample orientation-recoverable when the nonempty comparability graph determines the original partial order up to one global duality:

\[
G_{d,n}
\longmapsto
\{
P_{d,n},
P_{d,n}^{\mathrm{op}}
\}.
\]

Equivalently, the unique edge-containing connected component is uniquely partially orderable and all other components are isolated vertices.

Let

\[
p_d^{\mathrm{UPO}}(n)
\]

denote the probability of this event.

## 3. Main theorem

For every fixed integer spacetime dimension

\[
d\ge3,
\]

\[
\boxed{
\lim_{n\to\infty}
p_d^{\mathrm{UPO}}(n)
=
1.
}
\]

Thus, in every fixed flat Minkowski dimension above \(1+1\), the arrow-erased causal comparability graph asymptotically retains enough information to reconstruct the directed causal partial order up to a single global reversal.

This is an orientation-reconstruction theorem.

It does not select which of the two orientations is the physical future.

## 4. Proof architecture

The theorem follows from five independently established project results.

### A. One edge-containing component

For every fixed

\[
d\ge2,
\]

\[
\boxed{
\Pr(
G_{d,n}
\text{ has more than one connected component containing an edge}
)
\to0.
}
\]

Therefore, with probability tending to one,

\[
G_{d,n}
=
C_{d,n}
\;\dot\cup\;
I_{d,n},
\]

where \(C_{d,n}\) is the unique nontrivial connected component and \(I_{d,n}\) is a set of isolated vertices.

The isolated vertices introduce no orientation choice.

### B. Classical connected-UPO criterion

For a connected comparability graph, the following are equivalent:

1. the graph is uniquely partially orderable;
2. there is one undirected forcing/color class of edges;
3. every proper nontrivial graph module is stable.

Therefore

\[
C_{d,n}
\]

fails UPO exactly when it contains a proper non-stable module.

### C. Every implication class reaches a positive-disagreement core

For a comparable continuum pair define

\[
\Delta_d(x,y)
=
\mu(A_x\triangle A_y),
\qquad
A_x=\{z:z\sim x\}.
\]

The all-dimensional small-edge theorem gives

\[
\boxed{
F_d(t)
:=
\Pr(
X\sim Y,\,
\Delta_d(X,Y)\le t
)
=
\Theta(t^{\beta_d}),
}
\]

where

\[
\boxed{
\beta_d
=
\min\left(
d,\,
2+\frac4d
\right).
}
\]

For every fixed integer

\[
d\ge3,
\]

\[
\beta_d>2.
\]

The uniform comparable-neighborhood estimate gives

\[
\boxed{
\sup_x
\mu\{
z:z\sim x,\ \Delta_d(x,z)\le t
\}
=
O(t^2).
}
\]

Choose

\[
\alpha\in(1/2,1).
\]

For an edge with disagreement \(\delta\), the mass of splitters that would lead only to another edge of disagreement at most \(\delta^\alpha\) is

\[
O(\delta^{2\alpha})
=
o(\delta).
\]

Thus every sufficiently small-disagreement edge has a good-splitter region of volume at least a fixed fraction of \(\delta\).

The expected number of sampled edges with no sampled good splitter is bounded by

\[
Cn^2
\int_0^{\delta_0}
e^{-cn\delta}
\,dF_d(\delta)
=
O(
n^{2-\beta_d}
).
\]

Because

\[
\beta_d>2,
\]

this tends to zero.

Hence there exists a fixed

\[
\delta_0(d)>0
\]

such that, with probability tending to one,

\[
\boxed{
\text{every implication class contains an edge }e
\text{ with }
\Delta_d(e)\ge\delta_0(d).
}
\]

### D. Every non-stable module is macroscopic

Let \(M\) be a non-stable module of \(C_{d,n}\).

Choose an internal edge \(e_0\subset M\).

A forcing step starting from an edge inside \(M\) cannot leave \(M\): an outside vertex of a module is adjacent either to every member of \(M\) or to none, and therefore cannot distinguish the endpoints of an internal edge.

Hence the entire implication class of \(e_0\) lies inside \(M\).

By the preceding step, that class contains a core edge

\[
e
\]

with

\[
\Delta_d(e)\ge\delta_0(d).
\]

Conditioned on \(e\), its number of sampled splitters is

\[
S_e
\sim
\operatorname{Binomial}
(n-2,\Delta_d(e)).
\]

Uniform Chernoff concentration over at most \(\binom n2\) sampled edges gives a fixed constant

\[
c_d>0
\]

such that, with probability tending to one,

\[
S_e\ge c_dn
\]

for every core edge.

Every module containing \(e\) must contain all splitters of \(e\).

Therefore

\[
\boxed{
|M|\ge c_dn
}
\]

for every non-stable module witnessing UPO failure.

Thus all sublinear and small-side module regimes are eliminated at once.

### E. No macroscopic proper non-stable module survives

There are two remaining possibilities.

#### E1. Balanced linear modules

The causal-comparability graphon

\[
W_d(x,y)
=
\mathbf1_{\{x\sim y\}}
\]

has no nontrivial weakly homogeneous measurable set for any fixed

\[
d\ge2.
\]

Therefore it is prime in the measurable homogeneous-set sense.

By graphon sampling convergence and finite-colour compactness, for every fixed

\[
\varepsilon\in(0,1/2),
\]

\[
\boxed{
\Pr(
\exists\text{ graph module }M:
\varepsilon n\le|M|\le(1-\varepsilon)n
)
\to0.
}
\]

Thus a surviving macroscopic non-stable module would have to occupy all but a sublinear complement.

#### E2. Near-whole modules

Let

\[
O=C_{d,n}\setminus M
\]

and write

\[
O=U\dot\cup N,
\]

where \(U\) is complete to \(M\) and \(N\) is anticomplete to \(M\).

Connectedness gives

\[
U\ne\varnothing.
\]

If

\[
|O|=sn=o(n),
\]

then:

- \(U\)-vertices have sampled co-degree \(O(sn+I_n)\);
- \(N\)-vertices have sampled degree \(O(sn)\).

The Minkowski degree tails are

\[
\boxed{
g_d(q)
=
O(q^{4/d})
}
\]

near the null joint and

\[
\boxed{
\bar g_d(r)
=
O(r^d)
}
\]

near the timelike tips.

The low-degree internal-neighbor estimate is

\[
\boxed{
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2).
}
\]

Let

\[
r_*=2^J
\]

be the smallest power of two satisfying

\[
r_*>\frac d4.
\]

Repeated use of the internal-neighbor estimate forces

\[
N
\]

through the nested degree layers

\[
S_{Cs},
\quad
S_{Cs^2},
\quad
S_{Cs^4},
\quad\ldots,\quad
S_{Cs^{r_*}}.
\]

At the final layer,

\[
\mathbb E
\#S_{Cs^{r_*}}^{\mathrm{sample}}
=
O(
n s^{4r_*/d}
)
=
o(ns)
\]

because

\[
\frac{4r_*}{d}>1.
\]

At the same time, the co-degree tail gives only

\[
o(ns)
\]

possible \(U\)-vertices.

Therefore

\[
|U|+|N|
=
o(ns),
\]

contradicting

\[
|O|=ns.
\]

The full dyadic/concentration argument is recorded in the all-dimensional near-whole theorem.

Hence near-whole proper non-stable modules also disappear.

## 5. Completion of the proof

Suppose \(G_{d,n}\) is not orientation-recoverable.

With probability tending to one there is exactly one edge-containing connected component

\[
C_{d,n}.
\]

If \(C_{d,n}\) is not UPO, it has a proper non-stable module \(M\).

The implication-edge theorem and splitter concentration imply

\[
|M|\ge c_dn.
\]

For every fixed \(\varepsilon>0\), graphon primeness eliminates

\[
c_dn\le|M|\le(1-\varepsilon)n.
\]

A standard diagonal choice of

\[
\varepsilon_n\downarrow0
\]

therefore reduces any residual failure event to

\[
|C_{d,n}\setminus M|
\le
\varepsilon_n n.
\]

The all-dimensional near-whole theorem eliminates that regime as well.

Thus

\[
\Pr(
C_{d,n}
\text{ is not UPO}
)
\to0.
\]

The isolated components carry no edges and hence no independent transitive-orientation choices.

Finally, \(G_{d,n}\) is nonempty with probability tending to one: choose fixed positive-volume open sets \(U,V\subset D_d\) such that every event in \(U\) is timelike before every event in \(V\). Both sets are occupied with probability tending to one.

Therefore

\[
\boxed{
p_d^{\mathrm{UPO}}(n)\to1
\qquad
\text{for every fixed integer }d\ge3.
}
\]

## 6. The dimension-two exception

For \(d=2\), corresponding to \(1+1\) Minkowski spacetime, the relative causal order is a random \(2\)-order.

The project independently derives

\[
\boxed{
p_2^{\mathrm{UPO}}(n)\to\frac1e.
}
\]

However, Peter Winkler's 1990 paper *Random orders of dimension 2* explicitly studies the limiting probability that a two-dimensional random order has a uniquely orientable comparability graph in the random-linear-order ensemble.

Therefore the dimension-two asymptotic unique-orientability problem is prior art.

The repository does not claim priority for the \(1/e\) result without direct full-text comparison to Winkler and adjacent literature.

The local geometric distinction is nevertheless clear:

\[
\beta_2=2,
\]

whereas

\[
\beta_d>2
\quad
(d\ge3).
\]

Thus \(d=2\) sits exactly at the microscopic edge-forcing threshold.

## 7. Mathematical dimension dichotomy

Under the declared fixed-diamond, conditioned-cardinality ensemble, the current results are:

\[
\boxed{
d=2:
\quad
p_2^{\mathrm{UPO}}(n)\to\frac1e,
}
\]

and

\[
\boxed{
d\ge3:
\quad
p_d^{\mathrm{UPO}}(n)\to1.
}
\]

The mechanism is not identical in all dimensions.

For example:

- \(d=3\): the small-disagreement edge tail is bulk-controlled,
  \[
  F_3(t)=\Theta(t^3);
  \]
- \(d=4\): the codimension-two null joint controls the leading tail,
  \[
  F_4(t)\sim3\pi t^3;
  \]
- \(d>4\): the joint exponent is
  \[
  2+\frac4d.
  \]

Despite these geometric differences, every fixed

\[
d\ge3
\]

lies strictly on the recoverable side of the threshold

\[
\beta=2.
\]

## 8. What this theorem means

The theorem states that after deleting all arrows from a high-density flat Minkowski causal set while retaining only which pairs are causally comparable, the original directed partial order is asymptotically recoverable up to one global reversal for every fixed dimension \(d\ge3\).

The information loss is therefore asymptotically reduced to

\[
\boxed{
P
\leftrightarrow
P^{\mathrm{op}}.
}
\]

The graph itself does not choose between those two possibilities.

## 9. What it does not mean

The theorem does **not** establish:

- a physically preferred future;
- the emergence of time from no temporal structure;
- proper-time reconstruction;
- metric scale reconstruction;
- curvature reconstruction;
- Lorentzian manifold reconstruction in general;
- stability under arbitrary boundaries;
- stability under curvature;
- dynamical laws;
- empirical confirmation of causal-set ontology.

It is a precise theorem about one information-loss/reconstruction experiment.

## 10. Literature boundary

The proof imports established tools from several literatures.

### Comparability graphs and UPO

- Martin Aigner and Geert Prins, **Uniquely Partially Orderable Graphs**, *Journal of the London Mathematical Society* s2-3 (1971), 260–266.
- W. T. Trotter Jr., John I. Moore Jr., and David P. Sumner, **The Dimension of a Comparability Graph**, *Proceedings of the American Mathematical Society* 60 (1976), 35–40.
- Rolf H. Möhring, **Almost all comparability graphs are UPO**, *Discrete Mathematics* 50 (1984), 63–70.
- Ross M. McConnell and Jeremy P. Spinrad, **Modular decomposition and transitive orientation**, *Discrete Mathematics* 201 (1999), 189–241.

### Random dimension-two orders

- Peter Winkler, **Random orders of dimension 2**, *Order* 7 (1990), 329–339. DOI: 10.1007/BF00383197.

### Graphons and homogeneous sets

- Hamed Hatami and Sergey Norin, **On the boundary of the region defined by homomorphism densities**, *Journal of Combinatorics* 10 (2019), 203–219.
- Standard graphon sampling/cut-distance convergence and finite-colour compactness results.

### Causal sets and Minkowski reconstruction

The causal-set literature contains extensive results on sprinklings, dimension estimation, embedding, interval reconstruction, manifoldlikeness, and recovery of continuum geometric information from the directed causal order.

The targeted review did not locate a result that begins with a Minkowski sprinkling, discards every causal arrow, retains only symmetric causal comparability, and proves asymptotic recovery of the original partial order up to global reversal in all fixed dimensions \(d\ge3\).

This is limited negative evidence only.

No absolute novelty or priority claim is made.

## 11. Repository dependency chain

The theorem depends on the following project documents:

1. MINKOWSKI_HIGHER_DIMENSIONAL_UPO_AND_ISOLATED_THRESHOLD_20261111.md
2. MINKOWSKI_GRAPHON_DEGREE_TAIL_20261112.md
3. MINKOWSKI_NONISOLATED_GIANT_THEOREM_20261112.md
4. MINKOWSKI_CAUSAL_GRAPHON_PRIME_THEOREM_20261112.md
5. MINKOWSKI_ALLD_EDGE_TAIL_THEOREM_20261112.md
6. MINKOWSKI_ALLD_NEAR_WHOLE_EXCLUSION_THEOREM_20261112.md

The dimension-specific \(d=3\) and \(d=4\) proofs remain useful independent checks rather than being deleted.

## 12. Next research frontier

The flat fixed-window orientation-recovery question is now closed for every fixed integer dimension.

The strongest next targets are:

1. determine the asymptotic convergence rate of
   \[
   1-p_d^{\mathrm{UPO}}(n)
   \]
   for \(d\ge3\);
2. identify the leading rare obstruction in each dimension;
3. replace the fixed Alexandrov interval by other causally convex windows;
4. perturb the argument to weakly curved Lorentzian manifolds;
5. determine which local geometric assumptions preserve graphon primeness and edge escalation;
6. separate boundary-driven effects from genuinely local continuum effects;
7. ask what extra information, if any, can select one orientation from
   \[
   \{P,P^{\mathrm{op}}\}.
   \]

The current theorem establishes asymptotic orientation recoverability, not the physical selection of an arrow of time.
