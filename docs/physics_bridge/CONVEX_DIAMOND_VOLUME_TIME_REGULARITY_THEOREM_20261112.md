# Theorem: volume-time regularity on convex normal Lorentzian diamonds

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** literature-backed corollary specialized to finite convex diamonds  
**Physical status:** removes the independent volume-time regularity assumption for sufficiently regular convex diamonds  
**Literature basis:** direct specialization of Chruściel, Grant, and Minguzzi, *On differentiability of volume time functions*, Ann. Henri Poincaré 17 (2016), 2801–2824, DOI 10.1007/s00023-015-0448-3

## 1. Setting

Let

\[
(M^d,g)
\]

be a smooth time-oriented Lorentzian spacetime with

\[
d\ge2.
\]

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval whose closure lies inside a convex normal neighborhood \(U\).

Assume

\[
p\ll q.
\]

Use physical spacetime volume.

Define

\[
\tau_-(x)
=
\operatorname{Vol}(I(p,x)),
\]

and

\[
\tau_+(x)
=
\operatorname{Vol}(I(x,q)).
\]

Because \(D\) is causally convex,

\[
I_D^-(x)=I(p,x),
\]

and

\[
I_D^+(x)=I(x,q).
\]

Thus these are the past and future volume functions of the spacetime \(D\).

## 2. Statement

The functions

\[
\tau_-,
\qquad
\tau_+
\]

are \(C^1\) on \(D\).

Moreover,

\[
\nabla\tau_-
\]

is past-directed timelike and

\[
\nabla\tau_+
\]

is future-directed timelike.

Therefore

\[
\boxed{
\Phi(x)
=
\frac{
\tau_-(x)-\tau_+(x)
}{
V_D
}
}
\]

is \(C^1\) with past-directed timelike gradient throughout \(D\).

Equivalently,

\[
\boxed{
d\Phi
\text{ is a temporal covector field.}
}
\]

## 3. Direct reduction to the established volume-function theorem

View the open diamond

\[
D=I(p,q)
\]

as a spacetime in its own right.

Because \(D\) is a relatively compact causal diamond in the local convex setting, it is globally hyperbolic and has finite physical volume.

The constant weight

\[
\varphi\equiv1
\]

is smooth, strictly positive, and integrable on \(D\).

Chruściel, Grant, and Minguzzi prove \(C^1\) differentiability with timelike gradient for an appropriate class of positive smooth integrable Geroch volume functions on globally hyperbolic spacetimes.

Inside \(D\),

\[
I_D^-(x)=I(p,x),
\]

and

\[
I_D^+(x)=I(x,q).
\]

Therefore their past and future volume functions specialize exactly to

\[
\tau_-(x)=\operatorname{Vol}(I(p,x)),
\]

and

\[
\tau_+(x)=\operatorname{Vol}(I(x,q)).
\]

Thus the \(C^1\) temporal regularity used by the orientation-recovery theorem is not a new differentiability theorem of this project.

The remaining sections give a local geometric proof sketch because it is useful for understanding signs and for the later tip-shape calculation, but the regularity conclusion itself should be cited as a corollary of the established volume-function literature.

## 4. Why the convex-normal setting is simpler

Inside a convex normal neighborhood:

1. every two points are joined by a unique geodesic in \(U\);
2. the exponential map is nonsingular on the relevant star-shaped domains;
3. no null cut point or conjugate point occurs before leaving \(U\);
4. the null cone of an interior point is a smooth null hypersurface away from its vertex.

The general volume-function proof of Chruściel--Grant--Minguzzi has to remove a null cut locus of measure zero.

That complication is absent here.

## 5. Variation of the past volume

Fix

\[
x\in D
\]

and

\[
Z\in T_xM.
\]

Choose a smooth curve

\[
x(s)
\]

with

\[
x(0)=x,
\qquad
\dot x(0)=Z.
\]

The moving domain is

\[
I(p,x(s)).
\]

Its boundary consists of:

- a fixed piece on the future null boundary generated from \(p\);
- the moving past null cone of \(x(s)\).

Only the moving null-cone piece contributes to the first variation.

Let

\[
L(Z)
\]

be the Jacobi variation field on the null generators of the past cone induced by moving the vertex with velocity \(Z\).

The standard transport/Stokes argument gives

\[
\boxed{
Z(\tau_-)
=
\int_{E_D^-(x)}
i_{L(Z)}
d\operatorname{Vol}_g.
}
\]

Here

\[
E_D^-(x)
=
\partial I_D^-(x)\setminus\{x\}
\]

up to lower-dimensional boundary pieces.

## 6. Finiteness and continuity of the derivative

The closure of the diamond is compact in \(U\).

The null generators have uniformly finite affine length before meeting the fixed lower boundary.

The metric, Jacobi equation coefficients, and null hypersurface Jacobians are smooth.

Therefore:

- the variation field \(L(Z)\) depends continuously on \(x,Z\) and the null direction;
- the integrand is bounded by an integrable function on the compactified null-generator parameter space;
- the endpoint of each generator on the fixed diamond boundary varies continuously, with any exceptional tangencies confined to a lower-dimensional set.

Dominated convergence therefore gives continuity of

\[
(x,Z)
\longmapsto
Z(\tau_-).
\]

The derivative is linear in \(Z\).

Hence

\[
\boxed{
\tau_-\in C^1(D).
}
\]

The time-dual argument gives

\[
\boxed{
\tau_+\in C^1(D).
}
\]

## 7. Timelikeness of the past-volume gradient

Let

\[
Z
\]

be future-directed causal and nonzero.

On each past null generator from \(x\), the Jacobi first-variation contraction in the volume integral is nonnegative.

At the cone vertex its sign is governed by the scalar product between \(Z\) and the past-directed null generator tangent.

This scalar product is strictly positive except when \(Z\) is null and exactly aligned with that one generator.

In spacetime dimension at least two, the exceptional aligned generator has zero measure in the null-direction family.

Therefore

\[
\boxed{
Z(\tau_-)>0
}
\]

for every nonzero future-directed causal \(Z\).

A \(C^1\) covector that is strictly positive on the entire future causal cone has past-directed timelike metric dual.

Thus

\[
\boxed{
\nabla\tau_-
\text{ is past-directed timelike.}
}
\]

This is the finite-diamond analogue of the standard volume-time gradient argument.

## 8. Timelikeness of the future-volume gradient

By time reversal,

\[
Z(\tau_+)<0
\]

for every nonzero future-directed causal \(Z\).

Hence

\[
\boxed{
\nabla\tau_+
\text{ is future-directed timelike.}
}
\]

Equivalently,

\[
-\nabla\tau_+
\]

is past-directed timelike.

## 9. The finite-diamond volume difference

Define

\[
\Phi
=
\frac{
\tau_--\tau_+
}{
V_D
}.
\]

For every future-directed causal nonzero \(Z\),

\[
Z(\Phi)
=
\frac{
Z(\tau_-)-Z(\tau_+)
}{
V_D
}
>
0.
\]

Therefore

\[
\boxed{
\nabla\Phi
\text{ is past-directed timelike.}
}
\]

No cancellation can make it null: both terms contribute with the same sign to \(Z(\Phi)\).

Thus the primitive regularity assumption R1 of the curved recovery theorem is automatic on convex normal causal diamonds.

## 10. Relation to the literature

Chruściel, Grant, and Minguzzi derive the differentiability formula for weighted past/future volume functions by transporting causal pasts along Jacobi fields and applying Stokes' theorem.

They show that the resulting gradient is timelike or vanishing for nonnegative weights, and prove local anti-Lipschitz estimates for positive integrable weights.

The present finite-diamond proof uses the same local geometric mechanism with:

- physical weight equal to \(1\);
- finite total volume;
- a convex normal domain, eliminating internal null cut-locus complications;
- a fixed lower/upper diamond boundary whose velocity is zero in the shape derivative.

No novelty is claimed for the general volume-variation method.

The project-specific consequence is that the exact finite-diamond function governing arrow-erasure disagreement is automatically temporal in this local convex class.

## 11. Consequence for orientation recovery

For every convex normal causally convex diamond in \(2+1\), the bulk-disagreement theorem can define

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi,d\Phi)
}
\]

without separately assuming that \(d\Phi\) is timelike.

Thus one major primitive hypothesis of the curved orientation-recovery theorem is eliminated in the small-diamond regime.
