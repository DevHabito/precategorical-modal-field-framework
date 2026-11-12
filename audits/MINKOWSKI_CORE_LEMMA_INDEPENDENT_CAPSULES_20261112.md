# Independent proof capsules for the Minkowski orientation-recovery program

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** adversarial proof decomposition  
**Purpose:** isolate the four nonclassical lemmas on which the recovery theorem materially depends

## 1. Why this file exists

The repository now contains a long chain of results.

A long chain can hide accidental circularity even when each individual document looks plausible.

This file rewrites the four project-specific geometric inputs as independent proof capsules.

Each capsule contains:

1. the exact statement actually needed later;
2. the minimum imported facts;
3. a proof route that does not use any later recovery theorem;
4. the point at which an external reviewer should try hardest to break the argument.

No UPO conclusion is used inside these capsules.

---

# Capsule A: small-disagreement edge tail

## A.1 Statement

For the uniform flat Alexandrov interval in fixed integer spacetime dimension \(d\ge2\),

\[
F_d(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta_d(X,Y)\le\varepsilon
)
\]

satisfies

\[
\boxed{
F_d(\varepsilon)
=
\Theta(
\varepsilon^{\beta_d}
),
}
\]

with

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

For \(d\ge4\), the null joint gives the leading sector.

For \(d=3\), the bulk gives the leading sector.

## A.2 Imported facts

Only the following are imported:

- the exact flat Alexandrov-volume formula;
- spherical-coordinate volume measure;
- elementary Lorentzian causality;
- standard asymptotic integration.

No graph theory is used.

## A.3 Exact starting identity

For \(x\prec y\),

\[
\Delta_d(x,y)
=
\frac{
\tau(p,y)^d-\tau(p,x)^d
+
\tau(x,q)^d-\tau(y,q)^d
-
2\tau(x,y)^d
}{
2^d
}.
\]

This is exact.

## A.4 Bulk sector

Away from the codimension-two null joint, the first derivative of \(\Delta_d\) with respect to a small timelike displacement is nonzero.

Therefore

\[
\Delta_d
\asymp
|h|
\]

in every compact bulk chart.

The available displacement volume is \(d\)-dimensional.

Hence

\[
F_d^{\mathrm{bulk}}(\varepsilon)
=
\Theta(\varepsilon^d)
\]

at the scaling level.

For \(d=3\), the global coefficient can be integrated exactly and gives

\[
F_3(\varepsilon)
\sim
\frac{32\pi}{9}
\varepsilon^3.
\]

## A.5 Joint sector

Use null-waist coordinates

\[
a=1-r+t,
\qquad
b=1-r-t.
\]

For an ordered comparable pair, write

\[
a_x=\alpha,
\qquad
b_y=\beta,
\]

\[
A=a_y-a_x\ge0,
\qquad
B=b_x-b_y\ge0.
\]

Set

\[
m=\frac d2.
\]

The leading disagreement is equivalent, up to positive constants, to

\[
g_m(\alpha,A)
+
g_m(\beta,B),
\]

where

\[
g_m(u,v)
=
(u+v)^m-u^m.
\]

The pair measure contains the angular factor

\[
(AB)^{m-1}.
\]

The one-side integral is

\[
J_m(s)
=
\int
A^{m-1}
\mathbf1_{
\{g_m(\alpha,A)\le s\}
}
\,dA\,d\alpha.
\]

For \(m(m-1)>1\),

\[
J_m(s)
=
\Theta(
s^{1+1/m}
).
\]

For the integer-dimensional matching case \(d=3\),

\[
J_{3/2}(s)
=
\Theta(
s^{3/2}
).
\]

Squaring the one-side scale yields the joint exponent.

## A.6 Failure point to attack

The most important external-review target is the claim that all non-joint charts have a uniform nonzero first-order response and that the joint chart exhausts every possible degeneration of the gradient.

A hidden boundary sector with a weaker response would change \(\beta_d\).

The pre-asymptotic audit in high dimension was designed specifically to search for such a sector and did not find one.

---

# Capsule B: uniform comparable-ball bound

## B.1 Statement

For every fixed integer \(d\ge2\),

\[
B_t(x)
=
\{
z:z\sim x,\,
\Delta_d(x,z)\le t
\}
\]

satisfies

\[
\boxed{
\sup_x
\mu(B_t(x))
=
O(t^2).
}
\]

## B.2 Imported facts

Only:

- exact degree function \(Q_d(x)\);
- the inequality
  \[
  |Q_d(x)-Q_d(z)|
  \le
  \Delta_d(x,z);
  \]
- the low-degree internal-sparsity estimate;
- the local joint coordinates from Capsule A.

No forcing or UPO theorem is used.

## B.3 Low-degree case

If

\[
Q_d(x)\le Ct
\]

and

\[
\Delta_d(x,z)\le t,
\]

then

\[
Q_d(z)\le C't.
\]

Therefore both endpoints lie in a low-degree layer.

Internal sparsity gives

\[
\mu(
A_x\cap S_{C't}
)
=
O(t^2).
\]

## B.4 Joint transition

If \(Q_d(x)>Ct\) but \(x\) remains near the joint, let \(a,b\) be its null depths.

The disagreement bound gives one-side maximal increments

\[
L_t(a),
\qquad
L_t(b).
\]

The conditional causal volume is bounded by

\[
C
L_t(a)^m
L_t(b)^m.
\]

The one-side estimate is

\[
L_t(u)^m
\le
C
\begin{cases}
t, & u^m\le Ct,\\[4pt]
t^m u^{-m(m-1)}, & u^m>Ct.
\end{cases}
\]

Since at least one of \(a^m,b^m\) exceeds a constant multiple of \(t\), the product is always \(O(t^2)\).

## B.5 Bulk case

Away from the joint,

\[
\Delta_d(x,z)
\asymp
|z-x|,
\]

so the local comparable volume is

\[
O(t^d)
\le
O(t^2).
\]

## B.6 Failure point to attack

The key point is **uniformity in \(x\)** across the crossover between low-degree, one-sided null-face, two-sided joint, and bulk charts.

A proof valid only for each fixed \(x\) is not enough for the later union bounds.

---

# Capsule C: causal-graphon primeness

## C.1 Statement

Let

\[
W_d(x,y)
=
\mathbf1_{\{x\sim y\}}
\]

on a flat Minkowski Alexandrov interval with normalized volume measure.

There is no measurable set \(S\) with

\[
0<\mu(S)<1
\]

such that almost every outside point is adjacent either to almost every point of \(S\) or to almost none of \(S\).

Equivalently,

\[
\boxed{
W_d
\text{ is prime in the weakly homogeneous graphon sense.}
}
\]

## C.2 Imported facts

Only:

- Fubini's theorem;
- Lebesgue density points;
- openness of strict timelike and strict spacelike relations;
- elementary connectivity of the interior chronological future/past.

No finite random graph theorem is used.

## C.3 Splitter consequence

Weak homogeneity implies that for almost every pair

\[
x,y\in S,
\]

\[
\mu(
(A_x\triangle A_y)\setminus S
)
=
0.
\]

Thus almost every splitter of almost every pair of \(S\)-points also lies in \(S\).

## C.4 A positive-measure homogeneous set contains an edge

A positive-measure set has an interior density point.

Every small neighborhood of an interior event contains a positive-volume timelike cone sector.

Hence \(S\) contains a Fubini-good timelike pair.

## C.5 Continuum forcing connectivity

For fixed \(x\), all points of

\[
I^+(x)\cap D^\circ
\]

can be linked by a finite chain of spacelike steps staying in \(I^+(x)\).

Each step produces a direct \(P_3\)-forcing move between two timelike edges sharing \(x\).

Using a common future or common past point, any two interior timelike edges are connected by a finite forcing path.

All inequalities can be chosen strict, so the path is robust under perturbation.

## C.6 Propagation inside S

Start from a Fubini-good timelike edge in \(S\).

At each robust forcing step, the required splitter neighborhood has positive measure.

The weak-homogeneity consequence says almost every point in that splitter neighborhood lies in \(S\).

Inductively, the forcing path can be realized with all auxiliary vertices in \(S\), while preserving the Fubini-good property needed for the next step.

## C.7 Contradiction

Choose an interior density point of the complement.

Continuum forcing connectivity produces a robust path ending at an edge incident to that complement point.

The final robust splitter neighborhood must lie in \(S\) up to a null set.

That contradicts complement density at the endpoint.

Hence a positive-measure homogeneous set must have full measure.

## C.8 Failure point to attack

The delicate point is the interaction between:

- "almost every pair";
- finite forcing paths;
- repeated choice of Fubini-good auxiliary points.

A reviewer should verify that the full-measure sets can be intersected at every finite step without silently requiring a single null set that works uniformly for uncountably many paths.

The proof only needs one finite path at a time.

---

# Capsule D: tip middle-band lemma

## D.1 Statement

For every fixed \(d\ge3\), there exist constants

\[
r_0,c_0,q_-,q_+>0,
\qquad
q_+<1,
\]

such that if

\[
R(x)
=
1-Q_d(x)
\le r_0,
\]

then the nonneighbor set of \(x\) contains a measurable region

\[
B_x^{\mathrm{mid}}
\]

with

\[
\boxed{
\mu(B_x^{\mathrm{mid}})
\ge
c_0R(x),
}
\]

and

\[
\boxed{
q_-
\le
Q_d(z)
\le
q_+
\quad
\forall z\in B_x^{\mathrm{mid}}.
}
\]

## D.2 Imported facts

Only:

- the exact flat degree function;
- spherical-coordinate volume measure;
- elementary spacelike-separation algebra.

No module theorem is used.

## D.3 Explicit construction

Near the past tip, write

\[
x
=
(-1+s,s\rho e_1),
\qquad
0\le\rho\le1.
\]

Then

\[
R(x)
=
\frac d2s+O(s^2)
\]

uniformly in \(\rho\).

Choose a fixed time band

\[
\tau\in[\tau_0,\tau_1]
\Subset(0,1),
\]

a radial inward thickness

\[
h\in[s/4,s/3],
\]

and directions satisfying

\[
e_1\cdot\omega\le0.
\]

Set

\[
z
=
(-1+\tau,(\tau-h)\omega).
\]

## D.4 Spacelike margin

A direct calculation gives

\[
|\mathbf z-\mathbf x|^2
-
(t_z-t_x)^2
=
c(\tau,\rho,\omega)s
+
O(s^2),
\]

where the linear coefficient is uniformly positive over the chosen parameter ranges.

Thus

\[
z\not\sim x
\]

uniformly for sufficiently small \(s\).

## D.5 Volume and degree

The radial thickness is \(\Theta(s)\), while the time and angular windows have fixed positive measure.

Therefore

\[
\mu(B_x^{\mathrm{mid}})
=
\Theta(s)
=
\Theta(R(x)).
\]

As \(s\to0\), the band approaches a compact portion of the null face.

There

\[
Q_d(z)
=
(1-\tau)^{d/2},
\]

which is uniformly bounded away from zero and one.

## D.6 Failure point to attack

The dangerous case is

\[
\rho\to1,
\]

where the tip point itself approaches the null boundary.

The spacelike margin must remain uniformly positive in this limit.

The explicit formula and the repository grid regression both check this endpoint.

---

# 6. Dependency audit

The four capsules are logically ordered only through their geometric primitives.

They do not depend on:

- UPO recovery;
- the asymptotic error law;
- the module hierarchy;
- the component theorem.

The later stochastic proof uses them as inputs.

The dependence direction is therefore:

\[
\boxed{
\text{Lorentzian geometry}
\longrightarrow
\text{Capsules A--D}
\longrightarrow
\text{probability / graph theory}
\longrightarrow
\text{orientation recovery}.
}
\]

No reverse arrow is required.

# 7. External-review recommendation

Before publication, an independent reviewer should be asked to attack the capsules in this order:

1. Capsule A: search for a missing small-\(\Delta\) boundary sector;
2. Capsule B: test uniformity of the \(O(t^2)\) crossover;
3. Capsule C: audit the almost-everywhere forcing propagation;
4. Capsule D: audit the \(\rho\to1\) tip-boundary limit.

If all four survive, most of the remaining recovery proof is standard probabilistic or graph-theoretic assembly.
