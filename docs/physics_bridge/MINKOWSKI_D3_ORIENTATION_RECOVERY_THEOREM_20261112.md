# Theorem: asymptotic causal-orientation recovery from arrow-erased 2+1 Minkowski sprinklings

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** assembled analytic theorem  
**Physical status:** reconstruction theorem for a declared arrow-erasure experiment in flat \(2+1\) Minkowski spacetime  
**Novelty status:** targeted literature review did not locate an equivalent higher-dimensional arrow-erasure/UPO theorem for Minkowski sprinklings; absolute priority is not certified

## 1. Model

Let

\[
D\subset\mathbb M^3
\]

be a fixed flat Alexandrov interval.

Condition on cardinality \(n\), sprinkle

\[
X_1,\ldots,X_n
\]

iid uniformly, form the causal partial order \(P_n\), and erase every arrow while retaining only symmetric causal comparability.

Let \(G_n\) be the resulting comparability graph.

Let

\[
p_3^{\mathrm{UPO}}(n)
\]

be the probability that \(G_n\) determines \(P_n\) up to global reversal.

## 2. Main theorem

\[
\boxed{
\lim_{n\to\infty}
p_3^{\mathrm{UPO}}(n)
=
1.
}
\]

Thus, in the declared \(2+1\)-dimensional flat sprinkling ensemble, symmetric causal comparability asymptotically determines the directed causal order up to one global duality.

## 3. Component structure

The general non-isolated giant theorem gives

\[
\Pr(
G_n
\text{ has more than one edge-containing component}
)
\to0.
\]

In fact the \(d=3\) low-degree tail satisfies

\[
g_3(q)=\Theta(q^{4/3})=o(q),
\]

so the general graphon connectivity theorem of Hladký and Viswanathan also places this dimension in the supercritical fixed-\(K\)-connectivity regime.

Moreover,

\[
\mathbb E[I_n]
=
\Theta(n^{-1/3}),
\]

so

\[
\Pr(I_n>0)\to0.
\]

Thus \(G_n\) is connected with probability tending to one.

## 4. Internal UPO criterion

For a connected comparability graph,

\[
G
\text{ is UPO}
\]

if and only if it contains no proper non-stable module.

Equivalently, all edges belong to one transitive-orientation forcing/color class.

Therefore it remains to eliminate internal non-stable modules.

## 5. Edge escalation

The \(d=3\) small-disagreement theorem gives

\[
\boxed{
F_3(t)
=
\Pr(
X\sim Y,\,
\Delta(X,Y)\le t
)
=
\Theta(t^3).
}
\]

The uniform comparable metric-ball bound is

\[
\sup_x
\mu\{z:z\sim x,\ \Delta(x,z)\le t\}
=
O(t^2).
\]

Fix

\[
\alpha\in(1/2,1).
\]

The bad-splitter mass of an edge of disagreement \(\delta\) is

\[
O(\delta^{2\alpha})
=
o(\delta).
\]

Consequently, the expected number of sampled low-disagreement edges that fail to force an edge of strictly larger disagreement is

\[
O(n^{-1}).
\]

Hence, with probability tending to one, every implication class reaches a fixed core

\[
\Delta(e)\ge\delta_0>0.
\]

## 6. Core edges force linear modules

For a core edge \(e\),

\[
S_e
\sim
\operatorname{Binomial}(n-2,\Delta(e))
\]

counts its sampled splitters.

Uniform Chernoff concentration over all sampled core edges yields

\[
S_e\ge c_0n
\]

for a fixed \(c_0>0\) with probability tending to one.

Every module containing \(e\) must contain all splitters of \(e\).

Therefore every non-stable module witnessing failure of UPO has

\[
|M|\ge c_0n.
\]

## 7. Balanced modules are excluded

The Minkowski causal-comparability graphon is prime in every fixed spacetime dimension.

Thus, for every fixed

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

So any residual non-stable module must be near-whole:

\[
|C_n\setminus M|=o(n).
\]

## 8. Near-whole modules are excluded

Let

\[
O=C_n\setminus M
\]

and split it into:

\[
U
=
\{\text{vertices complete to }M\},
\]

\[
N
=
\{\text{vertices anticomplete to }M\}.
\]

Connectedness gives

\[
U\ne\varnothing.
\]

If

\[
|O|=sn=o(n),
\]

then:

- \(U\)-vertices have sampled co-degree \(O(sn)\);
- \(N\)-vertices have sampled degree \(O(sn)\).

The \(d=3\) boundary tails are

\[
g_3(s)=O(s^{4/3})
\]

and

\[
\bar g_3(s)=O(s^3).
\]

The low-degree internal-sparsity estimate is

\[
\mu(A_x\cap S_s)=O(s^2).
\]

These imply:

\[
|U|=O_p(ns^{5/2})=o(ns),
\]

while all \(N\)-vertices are forced into

\[
Q_3=O(s^2).
\]

The number of such ultra-low vertices is

\[
O_p(ns^{8/3})
=
o(ns).
\]

Therefore

\[
|O|
=
|U|+|N|
=
o_p(|O|),
\]

a contradiction.

Thus no near-whole proper non-stable module survives.

## 9. Completion

Assume \(G_n\) is not UPO.

With probability tending to one it is connected.

Then it has a proper non-stable module \(M\).

Edge escalation and splitter concentration force

\[
|M|\ge c_0n.
\]

Graphon primeness excludes the balanced regime.

Near-whole exclusion eliminates the only remaining regime.

Therefore

\[
\Pr(
G_n\text{ is not UPO}
)
\to0.
\]

Hence

\[
\boxed{
p_3^{\mathrm{UPO}}(n)\to1.
}
\]

## 10. Comparison with \(1+1\) and \(3+1\)

The current flat-Minkowski results form the following pattern.

### \(1+1\)

The random-\(2\)-order ensemble has a nontrivial limiting recoverability probability:

\[
p_2^{\mathrm{UPO}}(n)\to\frac1e.
\]

The asymptotic unique-orientability problem itself is prior art through Winkler's work on random dimension-two orders; the repository does not claim priority for that question.

### \(2+1\)

\[
\boxed{
p_3^{\mathrm{UPO}}(n)\to1.
}
\]

The small-edge tail is bulk-controlled:

\[
F_3(t)=\Theta(t^3).
\]

### \(3+1\)

\[
\boxed{
p_4^{\mathrm{UPO}}(n)\to1.
}
\]

The small-edge tail is controlled by the codimension-two null joint:

\[
F_4(t)\sim3\pi t^3.
\]

Thus \(2+1\) and \(3+1\) share the same orientation-recovery limit while reaching it through different Lorentzian geometries.

## 11. What is not yet proved

The repository does not yet contain an all-dimensional theorem

\[
p_d^{\mathrm{UPO}}(n)\to1
\qquad
\forall d\ge3.
\]

The natural candidate small-edge exponent is

\[
\beta_d
=
\min\left(
d,\,
2+\frac4d
\right),
\]

which is strictly greater than \(2\) for every finite integer

\[
d\ge3.
\]

This strongly suggests an all-dimensional extension, but the required uniform edge-tail and near-whole estimates should be written and audited in general dimension before that statement is promoted.

## 12. Physical boundary

The theorem concerns a fixed flat finite Alexandrov interval conditioned on cardinality \(n\).

It does not select a future direction.

It does not establish metric reconstruction, curvature reconstruction, dynamics, or empirical emergence of time.

It states only that, under arrow erasure, the directed causal partial order is asymptotically recoverable from symmetric comparability up to global reversal.
