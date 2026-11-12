# Lemma: stability of finite-diamond causal-volume functions in a regular null-geodesic regime

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** analytic parameter-stability lemma under no-cut/no-caustic hypotheses
**Purpose:** establish openness of the curved \(2+1\) recovery hypotheses

## 1. Setting

Let \(U\) be a relatively compact coordinate neighborhood in a smooth manifold.

Let

\[
g_s,
\qquad
|s|<s_0,
\]

be a \(C^4\)-continuous family of smooth time-oriented Lorentzian metrics on a neighborhood of \(\overline U\).

Let

\[
p_s,\ q_s
\]

depend \(C^2\)-smoothly on \(s\), with

\[
p_s\ll_{g_s}q_s.
\]

Assume there is a compact set \(K\Subset U\) such that, for all sufficiently small \(s\):

1. the relevant portions of the future null cone of \(p_s\) and past null cone of \(q_s\) are smooth embedded null hypersurfaces in \(U\);
2. their null generators are unique and contain no cut or conjugate point before leaving \(U\);
3. their intersections with the compact sets considered below stay uniformly separated from the cone vertices and the cut loci.

Define

\[
V_s^-(x)
=
\operatorname{Vol}_{g_s}
\left(
I_{g_s}(p_s,x)
\right),
\]

and

\[
V_s^+(x)
=
\operatorname{Vol}_{g_s}
\left(
I_{g_s}(x,q_s)
\right).
\]

## 2. Claim

On every compact subset \(K_0\Subset U\) satisfying the regularity conditions above,

\[
\boxed{
(s,x)
\longmapsto
V_s^\pm(x)
}
\]

is \(C^2\) in \(x\) and continuous in \(s\) as a \(C^2(K_0)\)-valued map.

In particular,

\[
\boxed{
V_s^\pm
\to
V_0^\pm
\quad
\text{in }C^2(K_0)
}
\]

as

\[
s\to0.
\]

The same conclusion holds after normalization by the total diamond volume, provided that volume remains bounded away from zero.

## 3. Smooth dependence of null geodesics

The geodesic equation is a smooth ordinary differential equation whose coefficients depend on the metric and its first derivatives.

A \(C^4\)-continuous metric family therefore gives smooth dependence, on compact affine-parameter intervals, of:

- geodesics;
- tangent vectors;
- first variations with respect to initial direction;
- Jacobi fields.

The no-conjugate-point assumption says the transverse Jacobi determinant does not vanish.

Compactness strengthens this to a uniform bound away from zero.

Therefore the null exponential maps from \(p_s\) and \(q_s\) form smooth parameterized embeddings on the relevant generator families.

## 4. Smooth parameterization of the moving null boundary

Consider, for example, the past null boundary of a variable point \(x\).

In the no-cut/no-caustic regime, it is parameterized by the null exponential map

\[
(\lambda,\theta)
\longmapsto
\exp_x^{g_s}
\left(
-\lambda k_{s,x,\theta}
\right),
\]

where \(\theta\) labels normalized past-null directions.

The parameterization depends smoothly on

\[
(s,x,\lambda,\theta).
\]

The same holds for the fixed future null boundary of \(p_s\).

Their transverse intersection points depend smoothly on parameters by the implicit-function theorem whenever the hypersurfaces meet transversely.

Thus a causal interval can be decomposed into finitely many coordinate charts whose moving boundaries are smooth functions of \((s,x)\).

## 5. Differentiation of the moving-domain volume

The physical volume form

\[
d\operatorname{Vol}_{g_s}
\]

depends \(C^3\)-continuously on \(s\).

For a smoothly moving domain \(\Omega(s,x)\), the first variation is given by the transport formula

\[
\frac{d}{d\tau}
\int_{\Omega(\tau)}
\omega_\tau
=
\int_{\Omega(\tau)}
\frac{d\omega_\tau}{d\tau}
+
\int_{\partial\Omega(\tau)}
\iota_{V_\tau}\omega_\tau.
\]

In the present fixed-metric \(x\)-derivative, only the moving null-boundary flux term appears.

The velocity field of that null boundary is a Jacobi field because it comes from differentiating the null geodesic flow with respect to its endpoint.

All objects in the boundary integral depend continuously on \((s,x)\).

Differentiating once more uses derivatives of Jacobi fields and of the volume density, which remain continuous under the stated \(C^4\) regularity.

Therefore the interval-volume functions are \(C^2\) on the regular compact set.

## 6. Relation to established volume-function differentiability

The structure above is the finite-diamond, no-cut-locus version of the differentiability mechanism used in the literature on Geroch volume functions.

Chruściel, Grant, and Minguzzi establish differentiability of classes of volume time functions by differentiating the moving chronological sets.

García-Heveling's 2026 treatment makes the moving-boundary interpretation explicit: the derivative is a flux integral over the null boundary, whose velocity is obtained from Jacobi fields.

The present lemma uses the simpler setting in which all relevant null generators are unique and remain before the cut locus.

## 7. Temporal-gradient stability

Let

\[
\Phi_s(x)
=
\frac{
V_s^-(x)-V_s^+(x)
}{
V_s(p_s,q_s)
}.
\]

Suppose that on a compact \(K_0\),

\[
d\Phi_0
\]

is timelike and satisfies the strict margin

\[
-g_0^{-1}(d\Phi_0,d\Phi_0)
\ge
c_0^2>0.
\]

The \(C^1\) convergence of \(\Phi_s\) and \(C^0\) convergence of the inverse metrics imply

\[
-g_s^{-1}(d\Phi_s,d\Phi_s)
\ge
\frac{c_0^2}{2}
\]

for sufficiently small \(s\).

Thus temporality is an open property on every regular compact subset.

## 8. Tip-gradient stability

At a timelike tip, the first variation of the small interval attached to the tip vanishes in \(2+1\), while the variation of the opposite large interval is a smooth null-boundary flux.

Hence the co-degree differential at the tip depends continuously on the metric family.

If it is timelike and nonzero for \(s=0\), it remains timelike and nonzero for sufficiently small \(s\).

## 9. Joint-data stability

The same ODE/Jacobi-field dependence implies continuity of:

- null-generator affine lengths;
- transverse Jacobi determinants;
- Penrose-limit tidal profiles;
- the positive near-null interval-volume coefficients \(C_\gamma\).

If the reference family has no conjugate point and has a transverse smooth joint, compactness gives uniform positive margins.

Therefore:

- no-caustic regularity;
- transverse joint intersection;
- volume-null Jacobian bounds;
- causal-cap constants

persist under sufficiently small \(C^4\) metric perturbations.

## 10. Consequence

The geometric ingredients H1--H5 of the regular curved \(2+1\) recovery theorem are open under sufficiently small \(C^4\) perturbations of a reference regular diamond, provided the endpoints vary continuously and the perturbed diamonds remain in the common regular neighborhood.

The only additional analytic condition requiring separate control is the global integrability/dominated-exhaustion condition for

\[
\kappa^{-3}.
\]

In the reference Minkowski diamond that singularity is integrable and its joint asymptotic is controlled by volume-null coordinates.

The same local comparison persists under the regular joint perturbation, so integrability is stable as well.

Thus the full regular-recovery package is open.

## 11. Scope

This is a local parameter-stability statement.

It does not assert smooth dependence through:

- null cut loci;
- caustics;
- changes of joint topology;
- degenerating causal diamonds.

Those are deliberately excluded by the hypotheses.
