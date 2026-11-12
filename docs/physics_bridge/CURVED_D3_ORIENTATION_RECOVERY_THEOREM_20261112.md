# Theorem: asymptotic causal-orientation recovery in a regular curved 2+1 Lorentzian diamond

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** assembled analytic theorem under explicit Lorentzian regularity hypotheses  
**Physical status:** first non-conformally-flat curved extension of the arrow-erasure recovery program  
**Novelty status:** targeted literature review did not locate an equivalent finite-sprinkling orientation-recovery theorem for curved Lorentzian diamonds; absolute priority is not certified

## 1. Model

Let

\[
(M,g)
\]

be a smooth time-oriented \(2+1\)-dimensional Lorentzian spacetime.

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval.

Condition on cardinality \(n\) and sample

\[
X_1,\ldots,X_n
\]

iid from normalized physical spacetime volume on \(D\).

Form the causal partial order and then erase all causal directions, retaining only symmetric timelike comparability.

Let

\[
G_{g,n}
\]

be the resulting undirected comparability graph.

Let

\[
p_{3,g}^{\mathrm{UPO}}(n)
\]

be the probability that the sampled causal partial order is determined by \(G_{g,n}\) up to global reversal.

## 2. Geometric regularity package

Assume the following.

### H1. Regular null joint

The joint

\[
\Sigma
=
\partial I^+(p)
\cap
\partial I^-(q)
\]

is a compact smooth spacelike one-manifold.

The two null boundaries meet transversely and the relevant generators reach the joint before any cut/conjugate degeneration.

### H2. Uniform regular Penrose tubes

The compact families of incoming and outgoing joint generators admit uniform null Fermi/Penrose expansions.

Consequently the volume-null coordinates

\[
a(x)
=
\mathcal V(p,x)^{2/3},
\]

\[
b(x)
=
\mathcal V(x,q)^{2/3}
\]

form a regular chart near \(\Sigma\), with bounded positive Jacobian and the causal-cap estimate

\[
|\Delta\sigma|
\le
C\sqrt{AB}.
\]

### H3. Temporal finite-diamond volume function

Define

\[
\Phi(x)
=
\mathcal V(p,x)
-
\mathcal V(x,q).
\]

Away from the joint, \(\Phi\) is \(C^2\) and

\[
d\Phi
\]

is timelike.

Set

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi,d\Phi)
}.
\]

Assume

\[
\kappa^{-3}
\in
L^1(D,\mu).
\]

### H4. Nondegenerate temporal tip gradients

The co-degree function

\[
R(x)
=
1-Q(x)
\]

extends \(C^2\)-regularly to the two timelike tips and has nonzero timelike differential there.

These assumptions are geometric.

No random-graph or UPO statement is included in them.

## 3. Continuum causal graphon

Define

\[
W_g(x,y)
=
\mathbf1_{\{x\ll y\text{ or }y\ll x\}}.
\]

The general Lorentzian causal-graphon primeness theorem gives

\[
\boxed{
W_g
\text{ is prime}.
}
\]

In particular it is a connected graphon.

No flatness assumption enters this result.

## 4. Low-degree tail

The regular volume-null chart gives the exact identity

\[
Q(x)
=
a^{3/2}
+
b^{3/2}.
\]

Therefore

\[
\boxed{
g_3(t)
=
\mu\{Q\le t\}
\sim
C_\Sigma t^{4/3}.
}
\]

Hence

\[
\boxed{
g_3(t)=o(t).
}
\]

## 5. Sample connectivity

A theorem of Hladký and Viswanathan characterizes connectivity of graphon samples.

If \(W\) is connected and

\[
g_W(t)=o(t),
\]

then

\[
G(n,W)
\]

is asymptotically almost surely connected.

Both hypotheses hold here.

Therefore

\[
\boxed{
\Pr(
G_{g,n}
\text{ is connected}
)
\to1.
}
\]

In fact, their theorem gives asymptotic \(K\)-connectivity for every fixed \(K\).

## 6. Small-disagreement edge tail

Define

\[
\Delta_g(x,y)
=
\mu(A_x\triangle A_y).
\]

The curved bulk volume-time theorem plus regular joint suppression give

\[
\boxed{
F_{3,g}(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta_g(X,Y)\le\varepsilon
)
\sim
C_g\varepsilon^3,
}
\]

where

\[
C_g
=
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa(x)^{-3}
\,d\mu(x).
\]

In particular,

\[
F_{3,g}(\varepsilon)
=
O(\varepsilon^3).
\]

## 7. Uniform comparable-disagreement balls

The curved comparable-ball theorem gives

\[
\boxed{
\sup_x
\mu\{
z:z\sim x,\,
\Delta_g(x,z)\le t
\}
=
O(t^2).
}
\]

This is the second local input needed for forcing escalation.

## 8. Implication-edge escalation

Fix

\[
\alpha\in(1/2,1).
\]

Let an edge \(e\) have disagreement

\[
\delta=\Delta_g(e).
\]

A splitter is bad if the forced new edge has disagreement at most

\[
\delta^\alpha.
\]

Every bad splitter lies in one of two comparable-disagreement balls of radius \(\delta^\alpha\).

Therefore the bad-splitter mass is

\[
O(
\delta^{2\alpha}
)
=
o(\delta).
\]

For sufficiently small fixed \(\delta_0\), every edge with

\[
0<\delta<\delta_0
\]

has a good-splitter region of mass at least \(c\delta\).

The probability that a sampled edge has no sampled good splitter is bounded by

\[
e^{-cn\delta}.
\]

Summing over all sampled edges,

\[
\mathbb E[Z_n]
\le
Cn^2
\int_0^{\delta_0}
e^{-cn\delta}
\,dF_{3,g}(\delta).
\]

Since

\[
F_{3,g}(\delta)
=
O(\delta^3),
\]

\[
\boxed{
\mathbb E[Z_n]
=
O(n^{-1})
\to0.
}
\]

Hence, with probability tending to one,

\[
\boxed{
\text{every implication class reaches an edge with }
\Delta_g\ge\delta_0.
}
\]

## 9. Core edges force linear modules

Condition on a sampled core edge

\[
e
\]

with

\[
\Delta_g(e)\ge\delta_0.
\]

The number of sampled splitters is

\[
S_e
\sim
\operatorname{Binomial}
(n-2,\Delta_g(e)).
\]

Uniform Chernoff concentration over all \(O(n^2)\) sampled edges gives a constant

\[
c_0>0
\]

such that, with probability tending to one,

\[
\boxed{
S_e\ge c_0n
}
\]

for every core edge.

Any graph module containing \(e\) must contain every splitter of \(e\).

Therefore every non-stable module witnessing UPO failure has size at least

\[
\boxed{
c_0n.
}
\]

## 10. Balanced modules disappear

Because the causal graphon is prime, standard coloured-graphon compactness implies that for every fixed

\[
\varepsilon>0,
\]

\[
\boxed{
\Pr\!\left(
\exists\text{ module }M:
\varepsilon n
\le
|M|
\le
(1-\varepsilon)n
\right)
\to0.
}
\]

Thus a surviving non-stable module must have sublinear complement.

## 11. Near-whole modules disappear

The regular curved geometry gives

\[
g_3(q)
=
O(q^{4/3}),
\]

\[
\bar g_3(r)
=
O(r^3),
\]

and

\[
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2).
\]

The curved near-whole theorem uses only these three estimates and concentration.

It gives

\[
\boxed{
\Pr\!\left(
\exists\text{ proper non-stable module }M:
n-|M|=o(n)
\right)
\to0
}
\]

in the deterministic-diagonal sense needed to combine with the balanced-module theorem.

## 12. Completion

With probability tending to one:

1. \(G_{g,n}\) is connected;
2. every implication class reaches the positive-disagreement core;
3. every non-stable module is linear in size;
4. no balanced linear non-stable module exists;
5. no near-whole non-stable module exists.

Suppose \(G_{g,n}\) were not UPO.

The classical connected-comparability-graph criterion would give a proper non-stable module.

Sections 9--11 exclude every possible size regime.

Therefore

\[
\boxed{
\Pr(
G_{g,n}
\text{ is not UPO}
)
\to0.
}
\]

Hence

\[
\boxed{
p_{3,g}^{\mathrm{UPO}}(n)
\longrightarrow
1.
}
\]

## 13. What is new relative to the conformal theorem

The conformal-weight theorem preserves the Minkowski causal relation exactly and changes only the sampling measure.

The present theorem allows the causal cones themselves to deform.

The spacetime need not be conformally flat.

The theorem is therefore a genuinely curved causal-structure extension, conditional on the explicit regularity package H1--H4.

## 14. Leading true-twin scale

The small-edge coefficient gives

\[
\mathbb E[T_n]
\sim
3C_g\,n^{-1}.
\]

The same second-moment argument as in flat \(2+1\) gives

\[
\boxed{
\Pr(T_n>0)
\sim
3C_g\,n^{-1}.
}
\]

Thus

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
\ge
\left(
3C_g+o(1)
\right)
n^{-1}.
}
\]

A matching upper bound is not yet proved for the full curved class because the current near-whole estimate is qualitative rather than \(o(n^{-1})\).

## 15. Literature boundary

The connectivity step uses:

**Jan Hladký and Gopal Viswanathan, "Connectivity of Inhomogeneous Random Graphs II," Random Structures & Algorithms 69 (2026), e70098, DOI 10.1002/rsa.70098.**

They prove that \(G(n,W)\) is a.a.s. connected exactly when \(W\) is connected and \(g_W(\alpha)=o(\alpha)\).

The Lorentzian graphon primeness, volume-null geometry, small-disagreement tail, and arrow-erasure UPO application are project-specific components.

A targeted search did not locate a previous curved-Lorentzian finite-sprinkling UPO theorem.

## 16. Current frontier

The qualitative curved \(2+1\) recovery problem is closed under H1--H4.

The next two tasks are:

1. remove or weaken the regularity hypotheses by proving them from standard null-geodesic conditions;
2. obtain a curved tip-clearance theorem strong enough to show
   \[
   1-p_{3,g}^{\mathrm{UPO}}(n)
   \sim
   3C_g\,n^{-1}.
   \]

The first-order coefficient is already identified; only the global upper-bound rate remains.
