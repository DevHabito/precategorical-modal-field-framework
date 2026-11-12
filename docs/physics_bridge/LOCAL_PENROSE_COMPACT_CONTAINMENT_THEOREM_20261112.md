# Theorem: automatic Penrose-scaled compact containment in sufficiently small convex diamonds

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic comparison theorem  
**Purpose:** remove the compact-containment assumption from the local small-diamond Penrose-Fermi argument

## 1. Setting

Let

\[
D=I(p,q)
\]

be a sufficiently small Alexandrov interval whose closure lies inside a causally convex convex-normal neighborhood.

Let

\[
\gamma:[0,L]\to M
\]

be one of the compact null generator segments from a tip to the codimension-two edge.

Choose a uniform null-Fermi tube around \(\gamma\) with coordinates

\[
(u,v,y^A),
\qquad
A=1,\ldots,d-2,
\]

such that the reference generator is

\[
u=0,
\qquad
y=0,
\]

and \(v\) is an affine parameter along the generator.

Consider a family of timelike endpoints \(x_a\) entering the diamond from the null face with inward optical depth

\[
a\downarrow0.
\]

## 2. Goal

Let

\[
I_a=I(p,x_a).
\]

Under the Penrose anisotropic scaling

\[
u=aU,
\qquad
y^A=\sqrt a\,Y^A,
\qquad
v=V,
\]

we prove that the rescaled intervals lie inside one fixed compact coordinate box:

\[
\boxed{
|U|\le C,
\qquad
|Y|\le C,
\qquad
V\in[V_-,V_+]
}
\]

for all sufficiently small \(a\).

Thus the compact-containment hypothesis of the scaled-domain convergence theorem is automatic in a sufficiently small regular diamond.

## 3. Uniform cone comparison

On the compact null-Fermi tube, the metric is smooth.

Shrink the tube if necessary.

There exist two smooth comparison Lorentzian metrics

\[
g_-
\prec
g
\prec
g_+
\]

whose cones are uniformly narrower/wider than those of \(g\), and whose coefficients in the chosen coordinates are uniformly equivalent to the constant double-null model

\[
\eta_0
=
-2\,du\,dv
+
\delta_{AB}dy^A dy^B.
\]

In particular, after fixed linear rescaling of the coordinates, every \(g\)-causal curve is \(g_+\)-causal and the \(g_+\)-cone obeys an inequality of the form

\[
\boxed{
|dy|^2
\le
C\,du\,dv
}
\]

for future causal displacements in the tube.

The constant \(C\) is independent of \(a\).

## 4. Endpoint coordinates

After a smooth coordinate normalization, the null endpoint has

\[
p=(0,0,0)
\]

and the nearly-null endpoint has the form

\[
x_a
=
(
a+O(a^2),
\,
L+O(a),
\,
O(a)
).
\]

A bounded transverse \(O(a)\) shift can be absorbed into the constants below.

The affine coordinate \(v\) remains in a fixed compact interval because the original generator segment is compact.

## 5. Comparison diamond in the wider metric

Let

\[
z=(u,v,y)
\in
I_g(p,x_a).
\]

Since

\[
g\prec g_+,
\]

we also have

\[
z\in
J_{g_+}^+(p)
\cap
J_{g_+}^-(x_a).
\]

The wider comparison cones imply

\[
0\le u\le Ca
\]

and

\[
V_-\le v\le V_+
\]

for fixed constants.

The future-cone inequality from \(p\) gives

\[
|y|^2
\le
Cuv.
\]

Since

\[
u=O(a),
\qquad
v=O(1),
\]

\[
|y|^2
\le
Ca.
\]

The past-cone inequality from \(x_a\) gives the complementary estimate

\[
|y-y_a|^2
\le
C(a-u)(L-v)
+
O(a^2),
\]

which is consistent with the same scale.

Hence

\[
\boxed{
|y|
\le
C\sqrt a.
}
\]

## 6. Rescaled bounds

Set

\[
U=\frac ua,
\qquad
Y=\frac y{\sqrt a},
\qquad
V=v.
\]

The preceding estimates give

\[
\boxed{
|U|\le C,
}
\]

\[
\boxed{
|Y|\le C,
}
\]

and

\[
\boxed{
V\in[V_-,V_+].
}
\]

Therefore every rescaled interval lies in one fixed compact subset of the null-Fermi coordinate domain.

## 7. Limiting endpoint relation

The Penrose-Fermi rescaled metrics converge smoothly on that compact set to the plane-wave limit

\[
g_{\rm PW}.
\]

The rescaled endpoints converge to finite points

\[
P_0,
\qquad
Q_0.
\]

Because \(x_a\) lies strictly inside the original null face for every \(a>0\), the rescaled inward displacement remains finite and positive.

The limiting pair is therefore timelike related in the plane-wave metric:

\[
\boxed{
P_0\ll_{g_{\rm PW}}Q_0.
}
\]

After shrinking the family if necessary, this relation has a uniform strict margin.

## 8. Consequence

The hypotheses of

PENROSE_SCALED_ALEXANDROV_DOMAIN_CONVERGENCE_20261112.md

are now derived from the local convex-diamond geometry rather than assumed.

Therefore the thin-null law

\[
V(p,x_a)
=
\mathcal C_\gamma
a^{d/2}
[1+o(1)]
\]

holds automatically along every regular generator family of a sufficiently small convex causal diamond.

## 9. Why the small-diamond assumption matters

For a large diamond, a thin interval can leave every single null-Fermi tube before returning to its endpoint, or encounter caustics/cut points.

Then the simple comparison box need not exist.

The theorem is local.

It does not claim compact containment for arbitrary long nearly-null intervals in a general spacetime.

## 10. Audit consequence

One of the four external-review priorities of the local all-dimensional theorem was whether Penrose-scaled compact containment really follows from small-diamond geometry.

The cone-comparison estimate above supplies the missing a priori bound:

\[
u=O(a),
\qquad
y=O(\sqrt a),
\qquad
v=O(1).
\]

The Penrose blow-up therefore cannot escape to infinity in the regular local theorem.
