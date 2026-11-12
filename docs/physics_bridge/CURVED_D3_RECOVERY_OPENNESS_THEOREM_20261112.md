# Theorem: openness of the regular curved 2+1 orientation-recovery class

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** analytic stability theorem
**Physical status:** shows that the curved recovery theorem applies to an open set of genuinely nonconformal Lorentzian metrics

## 1. Statement

Let \(g_0\) be a smooth time-oriented Lorentzian metric on a neighborhood \(U\) of the closure of a relatively compact causal diamond

\[
D_0=I_{g_0}(p_0,q_0).
\]

Assume \(D_0\) satisfies the regular curved \(2+1\) recovery hypotheses H1--H5 with strict geometric margins:

1. smooth transverse compact null joint;
2. no relevant cut or conjugate point;
3. uniform regular Penrose/null-Fermi tubes;
4. regular volume-null chart and causal-cap estimate;
5. \(C^2\) temporal finite-diamond volume function in the bulk with dominated Taylor control;
6. integrable \(\kappa^{-3}\);
7. nondegenerate temporal tip gradients;
8. regular noncaustic tip cones.

Then there is a \(C^4\) neighborhood \(\mathcal U\) of \(g_0\), together with neighborhoods of \(p_0,q_0\), such that every triple

\[
(g,p,q)
\]

sufficiently close to

\[
(g_0,p_0,q_0)
\]

and whose diamond remains inside \(U\) also satisfies H1--H5.

Consequently,

\[
\boxed{
p_{3,g}^{\mathrm{UPO}}(n)\to1
}
\]

and

\[
\boxed{
1-p_{3,g}^{\mathrm{UPO}}(n)
\sim
\frac{\mathcal K(D_g,g)}{n},
}
\]

where

\[
\mathcal K(D_g,g)
=
\frac{2\pi}{V_{D_g}}
\int_{D_g}
\left[
-g^{-1}(d\Phi_g,d\Phi_g)
\right]^{-3/2}
\,d\mu_g.
\]

Thus the regular curved recovery property is open in the metric topology.

## 2. Joint transversality is open

At the reference metric, the two smooth null hypersurfaces

\[
\partial I_{g_0}^+(p_0),
\qquad
\partial I_{g_0}^-(q_0)
\]

meet transversely along the compact joint.

Transversality is a strict rank condition.

The geodesic flow and null exponential maps depend continuously on the metric and endpoints in the \(C^1\) topology induced by a \(C^2\) metric topology.

Therefore, after a sufficiently small perturbation:

- both null hypersurfaces remain smooth in the chosen tube;
- their intersection remains a smooth compact one-manifold;
- the intersection remains transverse.

## 3. Absence of conjugate points is open on a compact family

Along each reference null generator, the transverse Jacobi determinant is nonzero before the joint.

The generator family is compact.

Therefore its absolute determinant has a positive lower bound on every compact affine-parameter interval separated from the cone vertex.

Jacobi equations depend continuously on the metric, curvature, and initial conditions.

A sufficiently small \(C^2\) perturbation preserves the nonvanishing lower bound.

Thus no conjugate point is created in the relevant generator segments.

The same argument applies to the tip cones used by the middle-band theorem.

## 4. Cut-free uniqueness is stable in the chosen tube

At the reference metric, the relevant null generators are unique and the null exponential maps are embedded on compact parameter domains.

Compactness gives a positive separation between distinct branches.

Small \(C^2\) perturbations preserve injectivity on a slightly smaller common tube.

Thus the no-cut/no-branching condition persists.

## 5. Penrose and null-Fermi data vary continuously

The Penrose-limit plane-wave profile is determined by the curvature components

\[
R_{uiuj}
\]

along a parallel-propagated frame on each null generator.

A \(C^4\) perturbation of the metric gives continuous perturbations of:

- curvature;
- parallel frames;
- geodesics;
- Jacobi fields;
- the plane-wave profile;
- the first Penrose-Fermi correction.

Hence the uniform Penrose-tube constants and the positive near-null interval-volume coefficients vary continuously.

The volume-null coordinate regularity theorem then preserves:

\[
0<c_J\le J(a,b,\sigma)\le C_J,
\]

and

\[
|\Delta\sigma|
\le
C\sqrt{AB}.
\]

## 6. Stability of finite-diamond volume functions

The finite-diamond volume-function stability lemma gives, on every regular compact bulk set,

\[
V_g^\pm
\to
V_{g_0}^\pm
\]

in \(C^2\) as the metric and endpoints converge.

After normalizing by total diamond volume,

\[
\Phi_g
=
\mathcal V_g(p,\cdot)
-
\mathcal V_g(\cdot,q)
\]

converges in \(C^2\) on those compact sets.

If the reference differential \(d\Phi_{g_0}\) has a strict timelike margin there, then \(d\Phi_g\) remains timelike.

Thus the bulk temporal-gradient hypothesis is open.

## 7. Dominated bulk expansion is stable

On each compact bulk chart, the Taylor coefficients of

\[
\Delta_g(x,\exp_x h)
\]

depend continuously on \(g\).

The reference quadratic remainder has a uniform bound.

A sufficiently small \(C^4\) metric perturbation preserves a common quadratic majorant.

Near the joint, the bulk Taylor expansion is not used; the volume-null joint estimates give a common integrable comparison.

Therefore the compact-exhaustion dominated-convergence condition used in the small-edge theorem remains valid.

## 8. Integrability of the inverse volume-time gradient

Away from the joint, \(\kappa_g\) remains bounded below on compact sets.

Near the joint, the regular volume-null coordinate comparison gives the same local power behavior as in the reference metric, up to bounded positive multiplicative factors.

Hence the singularity of

\[
\kappa_g^{-3}
\]

is uniformly dominated by an integrable reference function.

Therefore

\[
\boxed{
\kappa_g^{-3}\in L^1(D_g,\mu_g)
}
\]

persists under sufficiently small perturbations.

## 9. Tip-gradient openness

The co-degree function

\[
R_g=1-Q_g
\]

has first derivative at a regular tip given by the null-boundary flux of the opposite large causal interval.

The finite-volume stability lemma and smooth dependence of the null geodesic flow imply continuous dependence of this differential on \(g,p,q\).

If the reference tip differential is timelike and nonzero, the perturbed differential remains timelike and nonzero.

## 10. Tip middle-band openness

The middle-band proof depends on:

- a compact smooth family of null generators;
- positivity of the Jacobi/focusing density \(H(\lambda,\theta)\);
- a fixed affine band separated from the tip and joint;
- continuum graphon degree on that band bounded away from zero and one.

All four properties have strict positive margins in the reference geometry and depend continuously on the metric.

Therefore the middle-band constants

\[
c_0,
\qquad
q_-,
\qquad
q_+
\]

remain valid after a sufficiently small perturbation, possibly with weaker numerical values.

## 11. Continuity of the leading error coefficient

Under the same regular perturbations,

\[
\mathcal K(D_g,g)
=
\frac{2\pi}{V_{D_g}}
\int_{D_g}
\kappa_g^{-3}
\,d\mu_g
\]

depends continuously on \(g,p,q\).

The proof uses:

1. convergence of total diamond volume;
2. \(C^1\) convergence of \(\Phi_g\) on compact bulk exhaustions;
3. uniform integrable domination near the joint.

Thus

\[
\boxed{
\mathcal K(D_g,g)
\to
\mathcal K(D_{g_0},g_0)
}
\]

under a regular perturbation.

## 12. Nonconformal metrics occur in every neighborhood of Minkowski

In \(2+1\), conformal flatness is equivalent to vanishing Cotton tensor.

The Cotton tensor depends on finitely many derivatives of the metric.

There are arbitrarily small \(C^4\) perturbations of Minkowski space with nonzero Cotton tensor.

Therefore the open recovery neighborhood around a Minkowski diamond contains genuinely nonconformally-flat metrics.

This is not merely a conformal-weight corollary.

## 13. Consequence

The regular curved \(2+1\) theorem applies to an open set of Lorentzian metrics around every regular reference diamond satisfying H1--H5.

In particular, it applies to an open \(C^4\) neighborhood of the unit Minkowski diamond.

The next document gives an explicit nonconformal family inside this neighborhood.
