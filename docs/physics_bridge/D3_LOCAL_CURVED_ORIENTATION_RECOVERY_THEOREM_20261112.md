# Theorem: local curved 2+1 orientation recovery at strongly causal points

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** local analytic theorem assembled from the regular curved proof chain  
**Physical status:** removes the ad hoc regular-diamond assumptions for sufficiently small diamonds around strongly causal points  
**Novelty status:** local causal convexity and convex normal neighborhoods are classical; the orientation-recovery consequence is project-specific

## 1. Statement

Let

\[
(M^3,g)
\]

be a smooth time-oriented \(2+1\)-dimensional Lorentzian spacetime.

Let

\[
o\in M
\]

be a strongly causal point and let

\[
T\in T_oM
\]

be a future-directed unit timelike vector.

For sufficiently small

\[
L>0,
\]

define

\[
p_L=\exp_o(-LT),
\qquad
q_L=\exp_o(LT),
\]

and

\[
D_L=I(p_L,q_L).
\]

Then there exists

\[
L_0>0
\]

such that for every fixed

\[
0<L<L_0,
\]

the arrow-erased causal-comparability graph of \(n\) iid physical-volume samples from \(D_L\) satisfies

\[
\boxed{
p_{3,g,L}^{\mathrm{UPO}}(n)
\to1
}
\]

as

\[
n\to\infty.
\]

More sharply,

\[
\boxed{
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\sim
\frac{
K_{3,g}(D_L)
}{
n
},
}
\]

where

\[
\boxed{
K_{3,g}(D_L)
=
\frac{
2\pi
}{
V(D_L)
}
\int_{D_L}
\left[
-g^{-1}(d\Phi_L,d\Phi_L)
\right]^{-3/2}
d\mu_L,
}
\]

and

\[
\Phi_L(x)
=
\frac{
V(p_L,x)-V(x,q_L)
}{
V(D_L)
}.
\]

Thus the leading \(n^{-1}\) orientation-recovery law is locally valid in every smooth \(2+1\) spacetime at every strongly causal point.

## 2. Order of limits

The theorem has a precise order of limits.

First choose a fixed sufficiently small physical diamond

\[
D_L.
\]

Then let

\[
n\to\infty.
\]

The theorem is not a simultaneous statement with

\[
L=L_n\to0.
\]

No double scaling is required.

## 3. Existence of a convex causally convex neighborhood

Strong causality at \(o\) gives arbitrarily small causally convex neighborhoods.

Smooth Lorentzian geometry also gives arbitrarily small convex normal neighborhoods.

Choose a relatively compact open set

\[
U\ni o
\]

that is simultaneously:

- causally convex in the ambient spacetime;
- convex normal;
- globally hyperbolic as a local spacetime.

For sufficiently small \(L\),

\[
\overline{D_L}\subset U.
\]

Causal relations between points of \(D_L\) are therefore represented entirely inside \(U\).

## 4. No cut or conjugate points in the diamond

Because \(U\) is convex normal, every two points of \(U\) are connected by a unique geodesic in \(U\).

The exponential map is nonsingular on the relevant star-shaped domain.

Therefore the null generator segments forming the boundary of \(D_L\) have no cut or conjugate points before reaching the opposite boundary.

This supplies the regular-null-tube requirement.

## 5. Smooth transverse null edge

Inside \(U\), the two null boundary sheets are locally given by the world-function equations

\[
\sigma(p_L,x)=0,
\]

and

\[
\sigma(x,q_L)=0.
\]

Their differentials are the null covectors tangent to the unique null geodesics from \(p_L\) to \(x\) and from \(x\) to \(q_L\).

Suppose the two differentials were linearly dependent at an intersection point.

Then the two null generators would lie on the same null line through \(x\).

Their concatenation would make \(p_L\) and \(q_L\) null related.

But

\[
p_L\ll q_L.
\]

Contradiction.

Therefore the two null hypersurfaces meet transversely.

By the implicit-function theorem, their intersection is a smooth spacelike one-dimensional edge

\[
E_L.
\]

Because

\[
\overline{D_L}
\]

is compact, \(E_L\) is compact.

## 6. Uniform null-Fermi regularity

The generator families from \(p_L\) and \(q_L\) to the compact edge are compact.

They contain no cut or conjugate points.

Null-Fermi coordinate tubes therefore exist around each generator.

Compactness gives a finite subcover and uniform bounds on the corresponding metric and Jacobi coefficients.

Thus the regular Penrose-Fermi hypotheses used by the thin-null theorem hold uniformly along the edge.

## 7. Compactness of the Penrose-scaled thin intervals

Fix a compact generator family.

The metric in a sufficiently small null-Fermi tube is uniformly sandwiched between two nearby model cone structures.

For an endpoint with inward optical depth \(a\):

- the longitudinal inward coordinate is \(O(a)\);
- causal transverse separation is \(O(\sqrt a)\);
- affine position along the generator stays in the fixed compact generator interval.

After the Penrose scaling

\[
u=aU,
\qquad
y=\sqrt a\,Y,
\qquad
v=V,
\]

the corresponding rescaled causal intervals are therefore contained in one fixed compact coordinate set.

Their endpoints converge to a timelike-separated pair in the Penrose plane-wave limit.

Hence the compact-containment hypothesis of the scaled-domain convergence theorem is automatic in the sufficiently small convex diamond.

## 8. Thin-null endpoint law

The Penrose-Fermi volume theorem and the scaled-domain convergence theorem now give uniformly along the compact edge

\[
\boxed{
V(p_L,x)
=
c_+(s)a^{3/2}
[1+o(1)],
}
\]

and

\[
\boxed{
V(x,q_L)
=
c_-(s)b^{3/2}
[1+o(1)],
}
\]

with positive coefficients bounded above and below.

Thus the regular thin-null hypothesis is derived.

## 9. Double-null pair cap

The smooth transverse edge admits a regular double-null neighborhood.

In coordinates

\[
(a,b,s),
\]

the metric has nondegenerate leading form

\[
g
=
-2\Omega^2 da\,db
+
h\,ds^2
+
O(a+b),
\]

with

\[
\Omega,h>0.
\]

Hence nearby comparable pairs obey

\[
\boxed{
|\Delta s|
=
\Theta(\sqrt{AB}).
}
\]

Thus the curved pair-cap hypothesis is automatic.

## 10. Volume-time regularity is automatic

The dedicated convex-diamond volume-time theorem gives

\[
\tau_-(x)
=
V(p_L,x),
\]

\[
\tau_+(x)
=
V(x,q_L)
\]

of class \(C^1\) throughout the interior.

Their gradients have opposite time orientation:

\[
\nabla\tau_-
\text{ past-directed timelike},
\]

\[
\nabla\tau_+
\text{ future-directed timelike}.
\]

Therefore

\[
\boxed{
\Phi_L
=
\frac{\tau_--\tau_+}{V(D_L)}
}
\]

is \(C^1\) temporal.

Thus the remaining primitive volume-time assumption is removed.

## 11. Tip regularity

At \(p_L\), the first variation of

\[
x\mapsto V(x,q_L)
\]

is given by the null-cone volume variation formula.

Because the full regular cone contains a positive-measure family of null generators, the resulting derivative is a nonzero temporal covector.

The same holds at \(q_L\) by time reversal.

Choose a compact affine sub-band on each tip null cone, separated from:

- the tip;
- the joint edge.

There are no cut/conjugate points.

The degree function is continuous on the compact band and satisfies

\[
0<Q<1.
\]

Therefore

\[
0<q_-<Q<q_+<1
\]

uniformly after shrinking the band.

The Synge-world-function swept-volume theorem then supplies the required middle-band estimate.

Thus the regular-tip hypothesis is automatic.

## 12. Derived small-disagreement law

All hypotheses of the regular curved \(2+1\) matched theorem are now consequences of sufficiently small convex-diamond geometry.

Therefore

\[
\boxed{
F_{3,g,L}(\varepsilon)
\sim
C_{3,g}(D_L)
\varepsilon^3,
}
\]

where

\[
C_{3,g}(D_L)
=
\frac{
2\pi
}{
3V(D_L)
}
\int_{D_L}
\kappa_L(x)^{-3}
d\mu_L(x),
\]

and

\[
\kappa_L
=
\sqrt{
-g^{-1}(d\Phi_L,d\Phi_L)
}.
\]

## 13. Derived stochastic estimates

The same small diamond automatically satisfies:

\[
g_3(q)
=
\Theta(q^{4/3}),
\]

\[
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2),
\]

\[
\sup_x
\mu(B_t(x))
=
O(t^2),
\]

\[
\bar g_3(r)
=
\Theta(r^3),
\]

and the tip middle-band estimate.

The causal graphon is prime independently of flatness.

The dedicated curved component theorem gives one edge-containing component asymptotically and non-twin component ambiguity of order

\[
O(n^{-2})
+
\text{superpolynomial}.
\]

## 14. True twins dominate

The true-twin expectation satisfies

\[
\mathbb E[T_n]
\sim
K_{3,g}(D_L)n^{-1},
\]

with

\[
K_{3,g}(D_L)
=
3C_{3,g}(D_L).
\]

The second factorial moment is

\[
O(n^{-2}).
\]

All verified non-twin failure classes are

\[
O(n^{-2})
\]

or superpolynomially smaller.

Hence

\[
\boxed{
1-p_{3,g,L}^{\mathrm{UPO}}(n)
\sim
\frac{
K_{3,g}(D_L)
}{
n
}.
}
\]

## 15. Flat tangent limit

As

\[
L\downarrow0,
\]

the rescaled metric converges to the tangent Minkowski metric.

Accordingly,

\[
K_{3,g}(D_L)
\longrightarrow
\frac{32\pi}{3}
\]

after the standard unit-diamond normalization.

Thus the flat coefficient is the tangent-space limit of the curved intrinsic coefficient.

The theorem does not yet give the rate of this convergence in \(L\).

## 16. Scope

The theorem applies locally at strongly causal points.

In particular, it applies at every point of a globally hyperbolic spacetime.

It does not cover points lying in chronology/strong-causality violating regions.

It also makes no claim that a large Alexandrov interval containing caustics or cut loci satisfies the same law.

## 17. Scientific meaning

The \(n^{-1}\) recovery law in \(2+1\) is therefore not only a property of Minkowski space or of a specially chosen regular curved diamond.

It is a **local Lorentzian phenomenon** around every strongly causal point:

\[
\boxed{
\text{small curved causal diamond}
\Longrightarrow
\text{arrow-erased orientation recovery}
=
1-\frac{K(D)}n+o(n^{-1}).
}
\]

The geometry changes the coefficient.

The exponent and the dominance of comparable true twins survive.
