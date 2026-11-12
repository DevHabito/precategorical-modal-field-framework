# Theorem: asymptotic causal-orientation recovery from arrow-erased 3+1 Minkowski sprinklings

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** assembled analytic theorem from independently established component, modular, graphon, and Lorentzian-geometric lemmas  
**Physical status:** reconstruction theorem for a declared information-loss experiment; not a theorem that physical time emerges  
**Novelty status:** targeted literature review did not locate an equivalent higher-dimensional arrow-erasure/UPO theorem for Minkowski sprinklings. Absolute novelty and priority are not certified.

## 1. Model

Let

\[
D
=
I((-1,\mathbf0),(1,\mathbf0))
\subset
\mathbb M^4
\]

be a fixed flat Alexandrov interval in \(3+1\)-dimensional Minkowski spacetime.

Condition on cardinality \(n\), and sample

\[
X_1,\ldots,X_n
\]

iid uniformly with respect to Minkowski volume in \(D\).

Let \(P_n\) be the causal partial order:

\[
i\prec j
\quad\Longleftrightarrow\quad
X_i
\text{ is strictly timelike before }
X_j.
\]

Null equality has probability zero, so replacing strict timelike relation by the usual causal relation does not change the finite random model almost surely.

Erase all arrows and retain only symmetric comparability:

\[
i\sim j
\quad\Longleftrightarrow\quad
i\prec j
\text{ or }
j\prec i.
\]

Let

\[
G_n
\]

be the resulting undirected comparability graph.

## 2. Recovery event

Call the sample **orientation-recoverable** when the nonempty graph \(G_n\) has exactly two transitive orientations, one the global reversal of the other.

Equivalently, the causal partial order is determined by symmetric comparability up to global duality:

\[
G_n
\longmapsto
\{P_n,P_n^{\mathrm{op}}\}.
\]

Isolated vertices carry no edges and therefore introduce no additional orientation choice.

Let

\[
p_4^{\mathrm{UPO}}(n)
\]

denote the probability of this event.

## 3. Main theorem

\[
\boxed{
\lim_{n\to\infty}
p_4^{\mathrm{UPO}}(n)
=
1.
}
\]

Thus, for a conditioned high-density sprinkling in a fixed flat \(3+1\) Alexandrov interval, erasing every causal arrow while retaining only which pairs are causally comparable loses asymptotically only one global binary choice:

\[
\boxed{
\text{future versus past}.
}
\]

This statement is about orientation recoverability.

It does not reconstruct a preferred time orientation, proper time, the metric scale, curvature, or a dynamical law.

## 4. Logical structure of the proof

The proof is assembled from five independently established results.

### 4.1 One nontrivial component

For every fixed Minkowski dimension \(d\ge2\),

\[
\Pr(
G_{d,n}
\text{ has more than one edge-containing component}
)
\to0.
\]

Therefore, in \(d=4\), with probability tending to one,

\[
G_n
=
C_n
\;\dot\cup\;
I_n,
\]

where \(C_n\) is the unique nontrivial connected component and \(I_n\) is a set of isolated vertices.

Moreover,

\[
\mathbb E[|I_n|]\to3\pi.
\]

The isolates are orientation-neutral.

### 4.2 Classical connected-UPO criterion

For a connected comparability graph, the following are equivalent:

1. it is uniquely partially orderable;
2. it has one forcing/color class;
3. every proper nontrivial module is stable.

Therefore \(C_n\) fails UPO exactly when it contains a proper non-stable module.

### 4.3 Edge escalation

For a comparable pair define the graphon-neighborhood disagreement

\[
\Delta(x,y)
=
\mu(A_x\triangle A_y),
\qquad
A_x=\{z:z\sim x\}.
\]

The \(d=4\) small-edge theorem gives

\[
\Pr(
X\sim Y,\,
\Delta(X,Y)\le t
)
\sim
3\pi t^3.
\]

A uniform comparable-ball estimate gives

\[
\sup_x
\mu
\{z:z\sim x,\ \Delta(x,z)\le t\}
=
O(t^2).
\]

Consequently, for some fixed

\[
\delta_0>0,
\]

with probability tending to one every implication class contains an edge \(e\) satisfying

\[
\Delta(e)\ge\delta_0.
\]

### 4.4 Core edges force macroscopic modules

For an edge \(e=\{x,y\}\), the continuum splitter region is

\[
A_x\triangle A_y.
\]

Conditioned on \(e\), the number of sampled splitters is

\[
\operatorname{Binomial}
(n-2,\Delta(e)).
\]

Uniform Chernoff concentration over all sampled core edges gives

\[
S_e\ge c_0n
\]

for a fixed \(c_0>0\) simultaneously for every

\[
\Delta(e)\ge\delta_0
\]

with probability tending to one.

Every graph module containing \(e\) must contain every splitter of \(e\).

Thus every non-stable module witnessing failure of UPO has

\[
\boxed{
|M|\ge c_0n.
}
\]

### 4.5 Large modules are impossible

There are two scales to exclude.

#### Balanced modules

The causal-comparability graphon

\[
W_4(x,y)=\mathbf1_{\{x\sim y\}}
\]

has no nontrivial weakly homogeneous measurable set.

Therefore, by finite-colour graphon compactness and sampling convergence, for every fixed

\[
\varepsilon>0,
\]

\[
\Pr(
\exists\text{ module }M:
\varepsilon n\le|M|\le(1-\varepsilon)n
)
\to0.
\]

Hence any residual non-stable module must be near-whole:

\[
|C_n\setminus M|=o(n).
\]

#### Near-whole modules

Write

\[
O=C_n\setminus M.
\]

Every vertex of \(O\) is either:

- complete to \(M\), forming a set \(U\);
- anticomplete to \(M\), forming a set \(N\).

Connectedness forces

\[
U\ne\varnothing.
\]

If

\[
|O|=sn=o(n),
\]

then the module condition implies:

- vertices of \(U\) have sampled co-degree \(O(sn)\);
- vertices of \(N\) have sampled degree \(O(sn)\).

The Minkowski boundary tails are asymmetric:

\[
\mu\{Q_4\le s\}
=
O(s),
\]

whereas

\[
\mu\{1-Q_4\le s\}
=
O(s^4).
\]

Moreover, low-degree internal sparsity gives

\[
\sup_{x:Q_4(x)\le as}
\mu(
A_x\cap\{Q_4\le as\}
)
=
O(s^2).
\]

Therefore a vertex of \(N\) with

\[
Q_4(x)\gg s^2
\]

would have \(\Theta(ns^2)\) sampled neighbors outside the low-degree layer.

All such neighbors would have to lie in \(U\).

But the total number of possible \(U\)-vertices is only

\[
O_p(ns^4).
\]

Hence all \(N\)-vertices must lie in the ultra-low layer

\[
Q_4=O(s^2).
\]

That layer contains only

\[
O_p(ns^2)
=
o(sn)
\]

sampled vertices.

Likewise

\[
|U|=o_p(sn).
\]

Thus

\[
|O|
=
|U|+|N|
=
o_p(|O|),
\]

a contradiction.

So near-whole proper non-stable modules also disappear.

## 5. Completion

Assume \(C_n\) is not UPO.

Then it contains a proper non-stable module \(M\).

By edge escalation and splitter concentration,

\[
|M|\ge c_0n.
\]

Balanced-module exclusion forces

\[
|C_n\setminus M|=o(n).
\]

Near-whole exclusion says that no such module exists with probability tending to one.

Therefore

\[
\boxed{
\Pr(
C_n\text{ is not UPO}
)
\to0.
}
\]

The component theorem gives one nontrivial component plus isolates.

Hence the whole nonempty comparability graph has exactly two transitive orientations, global reversals of one another.

Finally, \(G_n\) is nonempty with probability tending to one: choose two fixed positive-volume open subsets \(U,V\subset D\) such that every point of \(U\) is timelike before every point of \(V\).  Both are occupied with probability tending to one.

Therefore

\[
\boxed{
p_4^{\mathrm{UPO}}(n)\to1.
}
\]

## 6. Relation to the \(1+1\) case

The \(1+1\) random-\(2\)-order ensemble behaves differently.

The project independently derives

\[
p_2^{\mathrm{UPO}}(n)\to\frac1e.
\]

However, Peter Winkler's 1990 paper *Random orders of dimension 2* already studies limiting unique orientability in the sample space generated by pairs of random linear orders.

Therefore the \(1+1\) asymptotic problem is prior art, and this repository does not claim priority for the \(1/e\) result without comparison to the full paper.

The higher-dimensional \(3+1\) theorem above uses a different mechanism:

\[
\boxed{
\text{small-edge tail exponent }3>2
}
\]

plus Lorentzian boundary sparsity and graphon primeness.

No analogous conclusion is imported from the random-\(2\)-order literature.

## 7. What is genuinely dimension-specific

Several \(d=4\) structures enter the proof.

### Null-joint edge tail

\[
F_4(t)
\sim
3\pi t^3.
\]

### Low-degree tail

\[
g_4(q)
\sim
3\pi q.
\]

### Near-universal tail

\[
\bar g_4(r)
\sim
\frac{r^4}{16}.
\]

### Low-degree internal sparsity

\[
\sup_{x\in S_q}
\mu(A_x\cap S_q)
=
O(q^2).
\]

The final theorem is therefore currently proved for \(d=4\).

It should not yet be advertised as an all-\(d\ge3\) theorem.

The \(2+1\) case remains a separate target, even though its component problem is already easier because

\[
g_3(q)=o(q).
\]

## 8. Literature boundary

The proof imports established graph-theoretic and graphon machinery:

- UPO comparability graphs and forcing/color classes;
- modular decomposition and transitive orientation;
- weakly homogeneous sets in graphons;
- cut-distance convergence of \(G(n,W)\);
- compactness of finite-colour graphon limits;
- Chernoff and Laplace/Stieltjes concentration tools.

Relevant classical and modern sources include:

- Martin Aigner and Geert Prins, **Uniquely Partially Orderable Graphs**, *Journal of the London Mathematical Society* s2-3 (1971), 260–266.
- Rolf H. Möhring, **Almost all comparability graphs are UPO**, *Discrete Mathematics* 50 (1984), 63–70. DOI: 10.1016/0012-365X(84)90035-9.
- Ross M. McConnell and Jeremy P. Spinrad, **Modular decomposition and transitive orientation**, *Discrete Mathematics* 201 (1999), 189–241. DOI: 10.1016/S0012-365X(98)00319-7.
- Hamed Hatami and Sergey Norin, **On the boundary of the region defined by homomorphism densities**, *Journal of Combinatorics* 10 (2019), 203–219.
- Jan Hladký and Gopal Viswanathan, **Connectivity of Inhomogeneous Random Graphs II**, *Random Structures & Algorithms* 69 (2026), e70098. DOI: 10.1002/rsa.70098.
- Svante Janson, Tiffany Y. Y. Lo, Colin McDiarmid, Anda Skeja, and Fiona Skerman, **Graphon Colourings and Limits of Graph Partitions**, arXiv:2610.38599 (2026).

A targeted literature search did not locate a prior result that:

1. erases the orientation of a Minkowski sprinkling;
2. treats the remaining causal-comparability graph as the observation;
3. proves asymptotic reconstruction of the original causal order up to global reversal in \(3+1\).

This is limited negative evidence only.

Absolute novelty or priority is not certified.

## 9. Physical interpretation

The theorem says:

> in the declared high-density flat \(3+1\) sprinkling ensemble, symmetric causal connectibility asymptotically contains enough relational information to recover the directed causal partial order up to a single global reversal.

It does **not** say:

- that the universe is a causal set;
- that time fundamentally emerges from an undirected graph;
- that the future direction is selected;
- that metric scale or proper time is reconstructed;
- that curvature is reconstructed;
- that the result survives arbitrary spacetime boundaries or curved manifolds;
- that the result is experimentally established.

The mathematical statement is narrower and stronger for being narrow.

## 10. Next research frontier

The immediate next questions are no longer about whether the flat \(3+1\) theorem closes.

They are:

1. does the same asymptotic recovery hold in \(2+1\)?
2. what is the convergence rate of
   \[
   1-p_4^{\mathrm{UPO}}(n)?
   \]
3. which obstruction gives the leading finite-\(n\) correction?
4. does the theorem survive other finite windows?
5. how does curvature perturb the degree tails, null-joint scaling, and forcing geometry?
6. can a local version be proved for causally convex regions of curved Lorentzian manifolds?
7. what additional information is needed to choose one of the two global time orientations?

The flat \(3+1\) arrow-erasure recovery problem itself is now analytically closed under the stated assumptions.
