# Theorem: leading orientation-recovery error in regular curved Lorentzian diamonds for every fixed d >= 3

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** assembled analytic theorem under regular joint, bulk, and tip hypotheses
**Physical status:** all-dimensional curved extension of the arrow-erasure orientation-recovery law
**Novelty status:** targeted literature review did not locate an equivalent finite-sprinkling UPO law for curved Lorentzian diamonds; absolute novelty and priority are not certified

## 1. Model

Fix an integer spacetime dimension

\[
d\ge3.
\]

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth time-oriented Lorentzian spacetime.

Sample

\[
X_1,\ldots,X_n
\]

iid from normalized physical spacetime volume on \(D\).

Erase every causal arrow while retaining the symmetric timelike-comparability relation.

Let

\[
p_{d,g}^{\mathrm{UPO}}(n)
\]

be the probability that the sampled causal partial order is recoverable from that undirected comparability graph up to global reversal.

## 2. Regular geometric hypotheses

Assume:

1. the joint
   \[
   \Sigma=
   \partial I^+(p)\cap\partial I^-(q)
   \]
   is smooth, compact, spacelike, and transverse;
2. the relevant incoming and outgoing null generators have no cut or conjugate degeneration;
3. uniform regular Penrose/null-Fermi tubes exist;
4. the volume-null coordinates
   \[
   a=\mathcal V(p,\cdot)^{2/d},
   \qquad
   b=\mathcal V(\cdot,q)^{2/d}
   \]
   form a regular double-null chart near the joint;
5. the finite-diamond volume function
   \[
   \Phi=
   \mathcal V(p,\cdot)-\mathcal V(\cdot,q)
   \]
   is \(C^2\) with nondegenerate timelike differential on regular bulk charts, with the dominated Taylor control required by the bulk small-disagreement expansion;
6. the co-degree gradients at the timelike tips are nonzero and timelike;
7. the tip null cones are regular and noncaustic so the middle-band clearance theorem applies.

For \(d=3\), additionally require the integrability of

\[
[-g^{-1}(d\Phi,d\Phi)]^{-3/2}.
\]

These are geometric assumptions only.

## 3. Lorentzian causal graphon primeness

Define

\[
W_g(x,y)
=
\mathbf1_{\{x\sim y\}}.
\]

The general Lorentzian causal-graphon theorem gives

\[
\boxed{
W_g
\text{ is prime}.
}
\]

Therefore no nontrivial weakly homogeneous measurable block exists in the continuum causal graphon.

This part of the proof is independent of dimension and curvature.

## 4. Boundary exponents

The regular curved boundary-geometry theorem gives

\[
\boxed{
g_d(q)
=
\Theta(q^{4/d}),
}
\]

\[
\boxed{
\sup_{x\in S_q}
\mu(A_x\cap S_q)
=
O(q^2),
}
\]

\[
\boxed{
\sup_x
\mu\{z:z\sim x,\Delta_g(x,z)\le t\}
=
O(t^2),
}
\]

and

\[
\boxed{
\bar g_d(r)
=
\Theta(r^d).
}
\]

These are the same exponents as in the flat model.

## 5. Small-disagreement edge tail

There are two regimes.

### d = 3

The bulk volume-time theorem and curved joint suppression give

\[
\boxed{
F_{3,g}(\varepsilon)
\sim
C_{3,g}
\varepsilon^3,
}
\]

with

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
\left[
-g^{-1}(d\Phi,d\Phi)
\right]^{-3/2}
\,d\mu.
}
\]

### d >= 4

The regular curved null-joint theorem gives

\[
\boxed{
F_{d,g}(\varepsilon)
\sim
C_{d,g}^{\mathrm{joint}}
\varepsilon^{2+4/d}.
}
\]

Set

\[
m=\frac d2,
\qquad
a_m=1+\frac1m.
\]

In volume-null coordinates, write the joint metric as

\[
g=
2\chi(\sigma)\,da\,db
+
h_\Sigma
+
O(a+b).
\]

Define

\[
\mathcal J_d(D,g)
=
\int_\Sigma
\chi^{m+1}
\,dA_\Sigma.
\]

Also define

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

Then

\[
\boxed{
C_{d,g}^{\mathrm{joint}}
=
\frac{
2^m
\omega_{d-2}
}{
V_D^2
}
\mathcal J_d(D,g)
(a_mL_m)^2
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}.
}
\]

Thus the universal small-edge exponent is

\[
\boxed{
\beta_d
=
\begin{cases}
3, & d=3,\\[4pt]
2+\dfrac4d, & d\ge4.
\end{cases}
}
\]

In every fixed dimension

\[
d\ge3,
\]

\[
\boxed{
\beta_d>2.
}
\]

## 6. True-twin first moment

Let \(T_n\) be the number of adjacent true-twin pairs.

The exact expectation identity is

\[
\mathbb E[T_n]
=
\binom n2
\int_0^1
(1-\delta)^{n-2}
\,dF_{d,g}(\delta).
\]

### d = 3

\[
\boxed{
\mathbb E[T_n]
\sim
K_{3,g}
n^{-1},
}
\]

where

\[
\boxed{
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
[-g^{-1}(d\Phi,d\Phi)]^{-3/2}
\,d\mu.
}
\]

### d >= 4

\[
\boxed{
\mathbb E[T_n]
\sim
K_{d,g}
n^{-4/d},
}
\]

where

\[
\boxed{
K_{d,g}
=
\frac{
2^{m-1}
\omega_{d-2}
}{
V_D^2
}
\mathcal J_d(D,g)
\left[
a_mL_m
\Gamma(a_m)
\right]^2.
}
\]

## 7. True-twin occurrence probability

The factorial second moment is lower order.

### Disjoint pairs

Since

\[
F_{d,g}(t)=O(t^{\beta_d}),
\]

the disjoint contribution is

\[
O(
n^{4-2\beta_d}
).
\]

### Overlapping pairs

The first pair costs

\[
O(t^{\beta_d}),
\]

and the third vertex lies in a comparable-disagreement ball of mass

\[
O(t^2).
\]

Hence the overlap tail is

\[
O(t^{\beta_d+2}),
\]

and the overlap factorial moment is

\[
O(
n^{1-\beta_d}
).
\]

Both are \(o(n^{2-\beta_d})\), the first-moment scale.

Therefore

\[
\boxed{
\Pr(T_n>0)
\sim
\mathbb E[T_n].
}
\]

## 8. Residual local forcing is one power lower

For a low-disagreement edge of size \(\delta\), the mass of splitters leading only to a forced edge with disagreement at most \(2\delta\) is

\[
O(\delta^2).
\]

Conditioned on having at least one splitter but no good splitter, the edge contributes at most

\[
Cn\delta^2e^{-cn\delta}.
\]

Integrating against \(F_{d,g}\) gives

\[
\boxed{
\Pr(R_n>0)
=
O(
n^{1-\beta_d}
).
}
\]

Thus:

- \(d=3\):
  \[
  O(n^{-2});
  \]
- \(d\ge4\):
  \[
  O(n^{-1-4/d}).
  \]

This is smaller than the true-twin scale by one factor \(n^{-1}\).

## 9. Every non-twin edge reaches a positive-disagreement core

On

\[
T_n=0
\]

and

\[
R_n=0,
\]

every low-disagreement edge directly forces an edge with more than twice its disagreement.

Repeated forcing reaches a fixed threshold

\[
\Delta_g(e)\ge\delta_0>0.
\]

The forcing chain stays inside the original connected component and inside every module containing the starting edge.

## 10. Core edges force linear size

A core edge has splitter count

\[
S_e
\sim
\operatorname{Binomial}
(n-2,\Delta_g(e)).
\]

Uniform Chernoff concentration gives a fixed

\[
c_0>0
\]

such that every sampled core edge has at least

\[
c_0n
\]

splitters except with probability \(e^{-\Theta(n)}\).

Therefore:

- every edge-containing component has linear size;
- every non-stable module containing an edge has linear size.

## 11. Multiple nontrivial components are subleading

If two edge-containing components exist outside the local residual event, both have size at least

\[
c_0n.
\]

Each connected component is a module.

Hence one is a balanced module.

Primeness of the continuum graphon gives a positive cut-distance gap from graphons with a fixed balanced homogeneous set.

The Second Sampling Lemma therefore gives a superpolynomial balanced-module bound.

Thus

\[
\boxed{
\Pr(
\text{multiple edge-containing components},
\ T_n=0
)
=
O(n^{1-\beta_d})
+
\exp\!\left(
-\frac{n}{2\log n}
\right)
+
e^{-\Theta(n)}.
}
\]

## 12. Balanced internal modules are superpolynomial

The same graphon-prime cut-distance argument gives, for every fixed \(\varepsilon>0\),

\[
\Pr(
\exists M:
\varepsilon n
\le
|M|
\le
(1-\varepsilon)n
)
\le
\exp\!\left(
-\frac{n}{2\log n}
\right)
\]

for sufficiently large \(n\).

A deterministic diagonal sequence

\[
\varepsilon_n\downarrow0
\]

extends this control to every module whose two sides remain at least

\[
\varepsilon_n n.
\]

## 13. Near-whole modules are subleading

After excluding multiple edge-containing components, a proper near-whole module requires a complete external vertex.

The regular tip middle-band theorem gives a nonneighbor region of measure at least

\[
cR(x)
\]

containing only intermediate-degree continuum vertices.

The probability that the remaining sample completely misses that middle band is at most

\[
e^{-cnR(x)}.
\]

Using

\[
\bar g_d(r)=O(r^d),
\]

the expected number of tip-clear candidates is

\[
O(n^{1-d}).
\]

Therefore

\[
\boxed{
\Pr(
\text{near-whole proper non-stable module}
)
=
O(n^{1-d})
+
e^{-\Theta(n)}.
}
\]

For every fixed

\[
d\ge3,
\]

this is lower order than the true-twin scale.

## 14. Failure-class exhaustion

Let \(\mathcal F_n\) be the orientation-recovery failure event.

Outside the true-twin event, every failure lies in the union of:

1. residual local forcing;
2. multiple edge-containing components;
3. a balanced internal non-stable module;
4. a near-whole internal non-stable module;
5. exponentially rare splitter-concentration or empty-graph events.

All are lower order than the true-twin occurrence probability.

Hence

\[
\boxed{
\Pr(\mathcal F_n)
\sim
\Pr(T_n>0).
}
\]

## 15. Main curved error law

### d = 3

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
K_{3,g}
n^{-1},
}
\]

with

\[
\boxed{
K_{3,g}
=
\frac{
2\pi
}{
V_D
}
\int_D
[-g^{-1}(d\Phi,d\Phi)]^{-3/2}
\,d\mu.
}
\]

### d >= 4

\[
\boxed{
1-p_{d,g}^{\mathrm{UPO}}(n)
\sim
K_{d,g}
n^{-4/d},
}
\]

with

\[
\boxed{
K_{d,g}
=
\frac{
2^{d/2-1}
\omega_{d-2}
}{
V_D^2
}
\left(
\int_\Sigma
\chi^{d/2+1}
\,dA_\Sigma
\right)
\left[
\left(
1+\frac2d
\right)
L_{d/2}
\Gamma\left(
1+\frac2d
\right)
\right]^2.
}
\]

In every fixed dimension

\[
d\ge3,
\]

\[
\boxed{
p_{d,g}^{\mathrm{UPO}}(n)\to1.
}
\]

## 16. Flat regression

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

For every flat fixed \(d\ge4\), the curved joint formula reduces algebraically to the previously derived Minkowski constant

\[
K_d^{\mathrm{twin}}.
\]

Thus the curved theorem contains the full flat theorem as a special case.

## 17. Physical interpretation

The leading defect remains a comparable true-twin pair.

What changes under regular curvature is the geometric source of its coefficient.

### d = 3

The coefficient is a bulk volume-time functional:

\[
\int_D
[-g^{-1}(d\Phi,d\Phi)]^{-3/2}
\,d\mu.
\]

### d >= 4

The coefficient is a codimension-two joint optical functional:

\[
\int_\Sigma
\chi^{d/2+1}
\,dA_\Sigma.
\]

Thus curvature enters the reconstruction error through two different geometric channels on opposite sides of the \(d=4\) transition.

## 18. Limitations

The theorem is for regular curved diamonds.

It does not cover:

- null caustics;
- cut-locus branching;
- nonsmooth or self-intersecting joints;
- degenerate volume-time gradients;
- degenerate tip gradients.

In such geometries the exponent itself may change.

## 19. Next frontier

The strongest next questions are:

1. prove that sufficiently small diamonds in every smooth \(d\ge4\) spacetime satisfy the regular hypotheses, extending the local-universality theorem beyond \(2+1\);
2. derive the first curvature correction to the local flat coefficients;
3. understand whether caustics define new universality classes for the small-disagreement exponent.
