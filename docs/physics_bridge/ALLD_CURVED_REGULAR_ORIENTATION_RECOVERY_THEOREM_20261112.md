# Theorem: asymptotic orientation recovery in regular curved Lorentzian diamonds for every fixed d >= 3

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** assembled analytic theorem under explicit regular-diamond hypotheses  
**Physical status:** curved-spacetime extension of the arrow-erasure orientation-recovery law in all fixed dimensions above \(1+1\)  
**Novelty status:** targeted review did not locate an equivalent finite stochastic UPO theorem; absolute priority is not certified

## 1. Setting

Let

\[
(M^d,g)
\]

be a smooth time-oriented Lorentzian spacetime with fixed integer

\[
d\ge3.
\]

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval with normalized physical volume measure \(\mu\).

Sample

\[
X_1,\ldots,X_n
\]

iid from \(\mu\).

Let \(P_{g,n}\) be the induced chronological partial order and let \(G_{g,n}\) be the undirected comparability graph obtained after all arrows are erased.

Let

\[
p_{d,g}^{\mathrm{UPO}}(n)
\]

be the probability that \(G_{g,n}\) determines the sampled partial order up to one global reversal.

## 2. Regular-diamond hypotheses

Assume:

### R1. Temporal finite-diamond volume function

\[
\Phi(x)
=
\frac{
V(p,x)-V(x,q)
}{
V_D
}
\]

is \(C^1\) in the interior and has timelike differential.

### R2. Regular transverse null edge

The two null boundary sheets meet transversely along a compact smooth spacelike codimension-two edge \(E\).

The relevant null generators have no cut or conjugate points and admit uniform null-Fermi/double-null neighborhoods.

### R3. Penrose-scaled compactness

The thin-null endpoint families satisfy the compact-containment condition required by the Penrose-scaled Alexandrov-domain convergence theorem.

### R4. Regular tips

The one-sided future/past volume functions have nonzero temporal first variations at the tips and admit regular compact middle null bands free of cuts and conjugate points.

## 3. Small-disagreement exponent

Define

\[
F_{d,g}(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta_g(X,Y)\le\varepsilon
).
\]

Then

\[
\boxed{
F_{d,g}(\varepsilon)
\sim
C_{d,g}
\varepsilon^{\beta_d},
}
\]

with

\[
\boxed{
\beta_d
=
\begin{cases}
3,& d=3,\\[4pt]
2+\dfrac4d,& d\ge4.
\end{cases}
}
\]

## 4. d = 3 coefficient

In \(2+1\), the leading sector is the bulk.

Define

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi,d\Phi)
}.
\]

The dominated-convergence theorem gives

\[
\boxed{
C_{3,g}
=
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa(x)^{-3}
\,d\mu(x).
}
\]

The nonlinear null-joint core is

\[
O(\varepsilon^{10/3})
\]

and is subleading.

## 5. d >= 4 coefficient

For \(d\ge4\), the regular codimension-two null edge is leading.

Let

\[
m=\frac d2,
\qquad
a_m=1+\frac2d.
\]

The curved regular-joint theorem gives

\[
\boxed{
C_{d,g}
=
C_{d,g}^{\rm joint}
=
2
\int_E
\mathcal A_d(s)
\mathcal S_d(s)
\,dA_E(s),
}
\]

where

\[
\mathcal A_d(s)
\]

is the local causal-cap pair-density coefficient and

\[
\mathcal S_d(s)
=
(a_mL_m)^2
c_+(s)^{-a_m}
c_-(s)^{-a_m}
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}.
\]

The universal scalar integral is

\[
L_m
=
\frac1{m+1}
\int_0^\infty
\left[
(1+t)^m-t^m
\right]^{-(m+1)/m}
dt.
\]

The local coefficients \(c_\pm\) are determined by the Penrose-limit thin-null volumes.

## 6. True-twin first moment

Let \(T_n\) count comparable true-twin pairs.

Exactly,

\[
\mathbb E[T_n]
=
\binom n2
\int
(1-\delta)^{n-2}
\,dF_{d,g}(\delta).
\]

Therefore

\[
\boxed{
\mathbb E[T_n]
\sim
K_{d,g}
n^{2-\beta_d},
}
\]

where

\[
\boxed{
K_{d,g}
=
\frac12
C_{d,g}
\Gamma(\beta_d+1).
}
\]

Thus

\[
d=3:
\qquad
K_{3,g}
=
3C_{3,g}
=
\frac{
2\pi
}{
V_D
}
\int_D
\kappa^{-3}\,d\mu,
\]

and

\[
d\ge4:
\qquad
\mathbb E[T_n]
\sim
K_{d,g}n^{-4/d}.
\]

## 7. True-twin occurrence probability

The curved all-dimensional comparable-ball theorem gives

\[
\boxed{
\sup_x
\mu
\{
z:z\sim x,\,
\Delta(x,z)\le t
\}
=
O(t^2).
}
\]

For two disjoint candidate twin pairs,

\[
\mathbb E[
T_n(T_n-1)
]_{\rm disjoint}
=
O(
n^{4-2\beta_d}
).
\]

For overlapping pairs, the first pair costs

\[
O(t^{\beta_d}),
\]

and the third point costs

\[
O(t^2),
\]

so

\[
\mathbb E[
T_n(T_n-1)
]_{\rm overlap}
=
O(
n^{1-\beta_d}
).
\]

In every fixed \(d\ge3\),

\[
4-2\beta_d
<
2-\beta_d,
\]

and

\[
1-\beta_d
<
2-\beta_d.
\]

Hence

\[
\boxed{
\mathbb E[
T_n(T_n-1)
]
=
o(
\mathbb E[T_n]
).
}
\]

Therefore

\[
\boxed{
\Pr(T_n>0)
\sim
K_{d,g}
n^{2-\beta_d}.
}
\]

## 8. Low-degree geometry

The regular curved edge theorem gives

\[
\boxed{
g_{d,g}(q)
=
\Theta(q^{4/d}),
}
\]

and

\[
\boxed{
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2).
}
\]

These imply degree escalation exactly as in the flat proof.

Choose

\[
\alpha
\]

with

\[
\max\left(
\frac12,
1-\frac2d
\right)
<
\alpha
<
1.
\]

The expected number of nonisolated low-degree vertices whose sampled neighbors all remain below \(q^\alpha\) tends to zero.

Thus every nonisolated sampled vertex reaches a fixed positive-degree core.

## 9. Component structure

The positive-degree core is connected with high probability by a finite compact-cover/anchor argument in the connected causal diamond.

Therefore

\[
\boxed{
\Pr(
\text{more than one edge-containing component}
)
\to0.
}
\]

For the leading-rate analysis, use implication escalation instead.

## 10. Non-twin implication escalation

For an edge of disagreement \(\delta\), the bad splitters that only force an edge with disagreement at most \(2\delta\) have mass

\[
O(\delta^2)
\]

by the uniform comparable-ball theorem.

Separating the zero-splitter true-twin event gives

\[
\boxed{
\Pr(
\text{non-twin residual escalation failure}
)
=
O(
n^{1-\beta_d}
).
}
\]

This is always lower order than

\[
n^{2-\beta_d}.
\]

## 11. Core edges force linear structures

Outside true twins and residual escalation failures, every sampled edge reaches a fixed positive-disagreement core edge.

A core edge has \(\Theta(n)\) sampled splitters with exponentially high probability.

Thus every:

- edge-containing component;
- proper non-stable module containing an edge;

has linear size.

## 12. Graphon primeness and balanced modules

The causal-comparability graphon of a Lorentzian Alexandrov interval is prime under the regular causal assumptions.

Therefore for each fixed balance parameter \(\varepsilon>0\), balanced modules are separated from the causal graphon in cut distance.

The standard graphon sampling estimate gives

\[
\boxed{
\Pr(
\text{balanced linear module}
)
\le
\exp\left(
-\frac{n}{2\log n}
\right)
}
\]

for sufficiently large \(n\).

A diagonal choice handles the slowly shrinking balanced range.

## 13. Tip geometry and near-whole modules

The curved all-dimensional tip theorem gives

\[
\boxed{
\bar g_{d,g}(r)
=
\Theta(r^d),
}
\]

and a middle nonneighbor band satisfying

\[
\mu(B_x^{\rm mid})
\ge
cR(x)
\]

with intermediate graphon degree.

Therefore

\[
\boxed{
\Pr(
\text{near-whole module}
)
=
O(n^{1-d})
+
e^{-\Theta(n)}.
}
\]

For \(d=3\),

\[
n^{1-d}
=
n^{-2}
=
o(n^{-1}).
\]

For \(d\ge4\),

\[
n^{1-d}
=
o(n^{-4/d}).
\]

## 14. Multiple components without true twins

Outside true twins and residual escalation failures, every edge-containing component has linear size.

If two such components existed, either one would be a balanced graph module.

Hence

\[
\boxed{
\Pr(
\text{multiple edge components},
\ T_n=0
)
=
O(
n^{1-\beta_d}
)
+
\exp\left(
-\frac{n}{2\log n}
\right)
+
e^{-\Theta(n)}.
}
\]

This is lower order than the true-twin probability.

## 15. Internal UPO failure without true twins

Suppose there is a unique edge-containing component but it is not UPO.

The classical connected-UPO criterion gives a proper non-stable module \(M\).

An internal edge of \(M\) remains inside \(M\) under forcing.

Outside residual escalation failure, it reaches a core edge.

Thus

\[
|M|\ge cn.
\]

If its complement is also linear, \(M\) is a balanced module and is superpolynomially rare.

If its complement is sublinear, the near-whole theorem applies.

Therefore

\[
\boxed{
\Pr(
\text{internal UPO failure},
\ T_n=0
)
=
o(
n^{2-\beta_d}
).
}
\]

## 16. Main asymptotic law

Let \(\mathcal F_n\) be orientation-recovery failure.

True twins give the lower bound

\[
\Pr(\mathcal F_n)
\ge
\left[
K_{d,g}+o(1)
\right]
n^{2-\beta_d}.
\]

The failure decomposition gives the matching upper bound.

Hence

\[
\boxed{
1-p_{d,g}^{\mathrm{UPO}}(n)
\sim
K_{d,g}
n^{2-\beta_d}.
}
\]

Equivalently,

\[
\boxed{
1-p_{d,g}^{\mathrm{UPO}}(n)
\sim
\begin{cases}
K_{3,g}n^{-1},&d=3,\\[4pt]
K_{d,g}n^{-4/d},&d\ge4.
\end{cases}
}
\]

Comparable true twins are the unique leading obstruction.

## 17. Flat checks

For the unit flat \(2+1\) diamond,

\[
K_{3,\eta}
=
\frac{32\pi}{3}.
\]

For the unit flat \(3+1\) diamond,

\[
K_{4,\eta}
=
9\pi.
\]

For all \(d\ge4\), the edge integral reduces to the previously derived flat constant

\[
K_d^{\rm twin}.
\]

Thus the curved theorem contains the flat laws as special cases.

## 18. Interpretation

The recovery exponent is controlled by local Lorentzian boundary geometry:

### d = 3

Bulk volume-time gradient:

\[
\beta_3=3.
\]

### d >= 4

Codimension-two null edge:

\[
\beta_d
=
2+\frac4d.
\]

Curvature changes the coefficient through:

- the finite-diamond volume-time field;
- Penrose-limit data along null generators;
- edge geometry.

Under regularity, it does not change the leading exponent.

## 19. Scope

This theorem is conditional on the regular-diamond hypotheses.

It does not cover diamonds with:

- caustics;
- conjugate points on relevant generators;
- cut loci crossing the edge/tip regions;
- nonsmooth or nontransverse null-edge structure;
- degenerate finite-diamond volume-time gradients.

The local small-diamond theorem removes these assumptions automatically near strongly causal points.
