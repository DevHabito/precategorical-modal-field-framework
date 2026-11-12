# Lemma: automatic compact containment of thin-null Alexandrov intervals via the null index form

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic causal-geometric lemma  
**Purpose:** remove compact containment as an independent hypothesis in the Penrose-scaled thin-null theorem  
**Audit note:** this version replaces an earlier Gronwall-only argument that did not adequately control the sign-indefinite plane-wave curvature term

## 1. Setting

Let

\[
\gamma:[0,L]\to(M,g)
\]

be a compact future null geodesic segment.

Assume:

1. \(\gamma\) is contained in a regular null-Fermi tube;
2. there is no point conjugate to \(\gamma(0)\) along \(\gamma|_{(0,L]}\);
3. the relevant generator family is compact and stays uniformly away from conjugacy, so the transverse index forms have a uniform positive spectral gap;
4. the nearly null endpoint family has inward optical scale \(a\downarrow0\).

Use null-Fermi coordinates

\[
(u,v,y^A),
\qquad
A=1,\ldots,d-2,
\]

adapted to \(\gamma\), with

\[
\gamma(v)=(0,v,0).
\]

The endpoint family has the natural scaling

\[
P_a=(O(a),\,0,\,O(\sqrt a)),
\]

\[
Q_a=(O(a),\,L,\,O(\sqrt a)).
\]

The claim is that the whole Alexandrov interval satisfies the same transverse scaling.

## 2. Penrose-Fermi leading metric

The null-Fermi expansion of Blau, Frank, and Weiss has leading plane-wave form

\[
g_{\rm PW}
=
2\,du\,dv
+
\delta_{AB}\,dy^A dy^B
+
H_{AB}(v)y^Ay^B\,dv^2,
\]

up to a conventional sign absorbed into \(H\).

The full metric in a sufficiently small tube is

\[
g
=
g_{\rm PW}
+
\mathcal R,
\]

where \(\mathcal R\) is higher order in the transverse Fermi variables and is controlled uniformly on the compact generator family.

The important point is that

\[
H_{AB}(v)y^Ay^B
\]

is a genuine quadratic curvature term.

Its sign cannot be controlled merely by shrinking the tube.

## 3. The transverse null index form

For a transverse path

\[
y:[0,L]\to\mathbb R^{d-2},
\]

define the plane-wave quadratic form

\[
\boxed{
Q_\gamma[y]
=
\int_0^L
\left(
|\dot y|^2
+
\langle H(v)y,y\rangle
\right)\,dv.
}
\]

With the displayed metric convention, the corresponding transverse Jacobi equation is

\[
\boxed{
\ddot J-H(v)J=0.
}
\]

A nonzero solution satisfying

\[
J(0)=J(L)=0
\]

is precisely a transverse Jacobi field producing conjugacy of the endpoints along the null generator.

Thus loss of invertibility of the Dirichlet Jacobi operator is the conjugate-point threshold.

## 4. Coercivity away from conjugacy

Assume there is no conjugate point on \((0,L]\).

Then the Dirichlet Jacobi operator has trivial kernel.

For the generator segment lying on the regular achronal null boundary, the null Morse-index theorem gives nonnegative index and no negative direction before the first conjugate point.

Hence the quadratic form is strictly positive on nonzero

\[
H_0^1([0,L];\mathbb R^{d-2})
\]

variations.

Because the interval is compact, strict positivity yields a spectral gap:

\[
\boxed{
Q_\gamma[w]
\ge
c_\gamma
\|w\|_{H^1}^2
}
\]

for every

\[
w(0)=w(L)=0,
\]

with

\[
c_\gamma>0.
\]

For a compact family of generators uniformly separated from conjugacy, continuity of the Jacobi operator gives

\[
\boxed{
c_\gamma\ge c_*>0
}
\]

uniformly.

This is the key estimate.

## 5. Nonzero endpoint data

A causal curve joining the nearly null endpoints need not have zero transverse endpoint values.

Let

\[
j_a
\]

be the unique Jacobi field satisfying the endpoint data

\[
j_a(0)=y(P_a),
\qquad
j_a(L)=y(Q_a).
\]

Nonconjugacy gives existence and uniqueness.

Smooth dependence of the Dirichlet Jacobi problem on its endpoint data gives

\[
\boxed{
\|j_a\|_{H^1}
+
\|j_a\|_\infty
=
O(\sqrt a).
}
\]

Write

\[
y=j_a+w,
\qquad
w(0)=w(L)=0.
\]

Because \(j_a\) solves the Jacobi equation, the index-form cross term vanishes:

\[
Q_\gamma[j_a,w]=0.
\]

Therefore

\[
\boxed{
Q_\gamma[y]
=
Q_\gamma[j_a]
+
Q_\gamma[w].
}
\]

Since \(j_a=O(\sqrt a)\),

\[
Q_\gamma[j_a]=O(a).
\]

## 6. Causal inequality in the plane-wave model

Parameterize a future causal curve by the monotone null coordinate \(v\).

The plane-wave causal condition gives, up to the chosen signature convention,

\[
2\dot u
+
|\dot y|^2
+
\langle H(v)y,y\rangle
\le0.
\]

Integrating from \(0\) to \(L\),

\[
Q_\gamma[y]
\le
C|\Delta u|.
\]

The endpoint configuration has

\[
|\Delta u|=O(a).
\]

Hence

\[
Q_\gamma[y]
=
O(a).
\]

Using the Jacobi decomposition,

\[
Q_\gamma[w]
=
O(a).
\]

Coercivity gives

\[
\boxed{
\|w\|_{H^1}^2
=
O(a).
}
\]

The one-dimensional Sobolev estimate then yields

\[
\boxed{
\|w\|_\infty
=
O(\sqrt a).
}
\]

Adding back \(j_a\),

\[
\boxed{
\sup_v|y(v)|
=
O(\sqrt a).
}
\]

Thus the desired transverse scale is enforced by the null index form.

## 7. Stability for the full null-Fermi metric

The physical metric differs from the plane-wave quadratic model by higher-order Fermi terms.

Use a first-exit bootstrap inside a fixed sufficiently small null-Fermi tube.

On the portion before first exit, the remainder contribution to the integrated causal inequality satisfies

\[
|\operatorname{Rem}[y,u]|
\le
\epsilon(\rho)
\|w\|_{H^1}^2
+
C_\rho a,
\]

where

\[
\epsilon(\rho)\to0
\]

as the tube radius

\[
\rho\to0.
\]

Choose the tube so small that

\[
\epsilon(\rho)
<
\frac{c_*}{2}.
\]

Then the remainder can be absorbed into the uniform index-form gap:

\[
\frac{c_*}{2}
\|w\|_{H^1}^2
\le
Ca.
\]

Therefore the full metric still gives

\[
\boxed{
|y|
\le
C\sqrt a.
}
\]

This is the place where shrinking the tube is legitimately used: it controls only the **higher-order remainder**, not the sign-indefinite quadratic curvature term.

## 8. Bound on the conjugate null coordinate

Return to the causal inequality.

Once

\[
|y|=O(\sqrt a),
\qquad
\int|\dot y|^2\,dv=O(a),
\]

all quadratic plane-wave terms and higher-order Fermi terms have integral \(O(a)\).

Integrating the \(u\)-equation from either endpoint therefore gives

\[
\boxed{
|u(v)|
\le
Ca
}
\]

along the entire causal curve.

The affine coordinate \(v\) is monotone and remains between the endpoint values up to the \(O(a)\) endpoint normalization.

Hence

\[
\boxed{
v\in[-Ca,L+Ca].
}
\]

## 9. First-exit contradiction

Assume a causal curve in

\[
I(P_a,Q_a)
\]

first exits the chosen regular tube.

Before first exit the estimates above hold:

\[
|y|\le C\sqrt a,
\qquad
|u|\le Ca.
\]

For sufficiently small \(a\), both are strictly smaller than the fixed tube radius.

The monotone \(v\)-coordinate also remains in the longitudinal tube interval.

This contradicts first exit.

Therefore every causal curve joining the endpoints remains in the regular tube.

In particular, every point of the Alexandrov interval obeys

\[
\boxed{
|u|\le Ca,
\qquad
|y|\le C\sqrt a,
\qquad
v\in[-Ca,L+Ca].
}
\]

## 10. Penrose-scaled compact containment

Under

\[
U=\frac ua,
\qquad
Y=\frac y{\sqrt a},
\qquad
V=v,
\]

the bounds become

\[
|U|\le C,
\qquad
|Y|\le C,
\qquad
V\in[-1,L+1]
\]

for all sufficiently small \(a\).

Hence the rescaled Alexandrov intervals lie in one fixed compact set.

The compact-containment hypothesis in

PENROSE_SCALED_ALEXANDROV_DOMAIN_CONVERGENCE_20261112.md

is therefore derived rather than assumed.

## 11. Why conjugate points are a genuine failure mechanism

If the endpoint reaches a conjugate point, the Dirichlet Jacobi operator develops a nontrivial kernel.

Then

\[
c_\gamma\to0.
\]

The estimate

\[
Q_\gamma[w]
\ge
c_\gamma\|w\|_{H^1}^2
\]

loses coercivity.

At the exact conjugate threshold, a nonzero transverse Jacobi field can have

\[
Q_\gamma[w]=0.
\]

Therefore the causal inequality can no longer force

\[
|y|=O(\sqrt a).
\]

This identifies a precise geometric route by which the thin-null universality class can change.

Caustics are therefore structural, not merely technical exclusions.

## 12. Literature boundary

Blau, Frank, and Weiss provide the null-Fermi/Penrose metric expansion.

The relation between conjugate points, Jacobi fields, and the null index form is classical Lorentzian Morse-index theory.

The project-specific statement is the use of index-form coercivity to prove compact containment of the nearly-null Alexandrov interval at the exact

\[
u=O(a),
\qquad
y=O(\sqrt a)
\]

Penrose scaling.

## 13. Consequence

The corrected logical chain is

\[
\boxed{
\text{regular conjugate-free null generator}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{uniform null index-form gap}
}
\]

\[
\Downarrow
\]

\[
\boxed{
u=O(a),\quad y=O(\sqrt a)
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{Penrose-scaled compact containment}
}
\]

\[
\Downarrow
\]

\[
\boxed{
V_{\rm thin}
\sim
\mathcal C_\gamma a^{d/2}.
}
\]

This replaces the weaker Gronwall-only argument of the earlier draft.
