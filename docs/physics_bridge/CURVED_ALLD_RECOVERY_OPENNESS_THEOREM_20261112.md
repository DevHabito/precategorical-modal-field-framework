# Theorem: openness of the regular curved orientation-recovery class in every fixed d >= 3

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** analytic stability theorem
**Physical status:** makes the regular curved all-dimensional recovery theorem stable under generic metric perturbations

## 1. Statement

Fix an integer

\[
d\ge3.
\]

Let \(g_0\) be a smooth time-oriented Lorentzian metric on a neighborhood of the closure of a relatively compact diamond

\[
D_0=I_{g_0}(p_0,q_0).
\]

Assume \(D_0\) satisfies the regular curved all-dimensional recovery hypotheses with strict margins:

1. smooth compact transverse joint;
2. no relevant null cut/conjugate degeneration;
3. uniform Penrose/null-Fermi tubes;
4. regular volume-null coordinates;
5. regular tangential causal cap;
6. nondegenerate temporal finite-diamond volume gradient in the bulk;
7. dominated bulk Taylor control;
8. nondegenerate temporal co-degree gradients at the tips;
9. regular noncaustic tip cones.

Then there exists a \(C^4\) neighborhood of \((g_0,p_0,q_0)\) such that every sufficiently close perturbed diamond remaining in the common regular neighborhood satisfies the same hypotheses.

Consequently, the full regular-curved orientation-recovery law is open under \(C^4\) perturbations.

## 2. Joint geometry

The reference null hypersurfaces intersect transversely along a compact codimension-two spacelike joint.

Transversality is a strict rank condition.

Null geodesic flow depends continuously on the metric and endpoints.

Therefore sufficiently small perturbations preserve:

- smoothness of the two null hypersurface pieces;
- compactness of the joint;
- spacelike character of the joint;
- transverse intersection.

## 3. Conjugate-point exclusion

The transverse Jacobi determinant along each relevant reference generator is nonzero before the joint.

The generator family is compact.

Hence the determinant has a uniform positive lower bound after a suitable normalization.

The Jacobi equation depends continuously on the metric curvature and initial data.

A sufficiently small \(C^2\) perturbation therefore preserves nonvanishing of the determinant.

Thus no conjugate point enters the relevant null segments.

## 4. Cut-free generator uniqueness

The reference null exponential maps are embeddings on compact parameter domains before the cut locus.

Compact injectivity and separation of distinct branches persist under sufficiently small perturbations.

Therefore the unique-generator/no-branching hypothesis is open.

## 5. Volume-null coordinate stability

For every fixed dimension define

\[
m=d/2,
\]

\[
a=
\mathcal V(p,\cdot)^{1/m},
\qquad
b=
\mathcal V(\cdot,q)^{1/m}.
\]

The Penrose-limit near-null volume law is

\[
\mathcal V(p,x_\delta)
=
\delta^m
[
C_\gamma+o(1)
].
\]

On a regular compact family of null generators,

\[
0<C_{\min}\le C_\gamma\le C_{\max}<\infty.
\]

The Penrose-Fermi expansion and causal-interval stability imply continuous dependence of \(C_\gamma\), the volume-null transverse derivatives, and the joint Jacobian on the metric.

Hence the regular coordinate bounds

\[
0<c_J
\le
J(a,b,\sigma)
\le
C_J
\]

persist.

## 6. Tangential causal cap stability

At the joint the double-null metric has the form

\[
g
=
2\chi\,da\,db
+
h_\Sigma
+
O(a+b).
\]

The leading timelike condition for a nearby pair is

\[
h_\Sigma(\zeta,\zeta)
<
2\chi AB.
\]

The positive quantities

\[
\chi,
\qquad
h_\Sigma
\]

vary continuously under metric perturbation.

Their eigenvalues remain bounded above and below on the compact joint.

Therefore the causal-cap comparison

\[
\operatorname{Vol}_{\sigma}
(\text{cap})
\asymp
(AB)^{(d-2)/2}
\]

persists uniformly.

## 7. Central small-interval control

For nearby comparable points in a regular double-null chart,

\[
\tau(x,y)^2
\le
C AB.
\]

The local Alexandrov-volume estimate gives

\[
\mathcal V(x,y)
\le
C'(AB)^{d/2}.
\]

The constants depend continuously on the metric on compact chart families.

Thus the absorption of the central interval into the endpoint-volume increments is stable.

## 8. Bulk volume-time stability

Define

\[
\Phi_g
=
\mathcal V_g(p,\cdot)
-
\mathcal V_g(\cdot,q).
\]

The finite-diamond volume-function stability lemma gives \(C^2\) convergence on regular compact bulk subsets.

Therefore a strict timelike margin for

\[
d\Phi_{g_0}
\]

persists.

The uniform quadratic Taylor remainder and the local cone-volume majorants also persist under a sufficiently small \(C^4\) perturbation.

For \(d=3\), the joint comparison preserves the integrable singularity of

\[
[-g^{-1}(d\Phi,d\Phi)]^{-3/2}.
\]

For \(d\ge4\), the bulk is subleading and only nondegeneracy is needed for the global comparable-ball estimate.

## 9. Tip data

The co-degree first derivative at a regular timelike tip is the first variation of the opposite large causal interval.

It is a null-boundary flux depending continuously on:

- the metric;
- endpoint;
- null geodesic flow;
- Jacobi fields.

Thus a nonzero timelike tip gradient remains nonzero and timelike.

The tip middle-band constants also persist because their construction depends on strict positive margins on a compact affine null band.

## 10. Graphon primeness

Causal-graphon primeness does not require perturbative stability.

It holds for every smooth regular Lorentzian diamond directly.

Therefore the macroscopic module part of the proof remains available throughout the perturbation neighborhood.

## 11. Leading coefficient continuity

### d = 3

The leading coefficient is

\[
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
\]

Regular bulk convergence plus uniform joint domination gives continuity.

### d >= 4

The leading coefficient is

\[
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
\]

The total volume, joint metric, joint area form, and \(\chi\) all vary continuously.

Hence \(K_{d,g}\) is continuous in the regular perturbation class.

## 12. Consequence

The regular curved recovery theorem is not a measure-zero geometric phenomenon.

It holds on an open set in the \(C^4\) topology of Lorentzian metrics.

This open set contains nonconformally-flat metrics in every dimension where conformal flatness is non-generic.

The local small-diamond theorem uses this openness with Minkowski space as the reference geometry.
