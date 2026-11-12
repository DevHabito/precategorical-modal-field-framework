# Lemma: world-function proof of C1 finite-diamond volume regularity

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic local proof lemma  
**Purpose:** provide a self-contained differentiability proof for constant-weight finite Alexandrov volumes in a strictly convex normal setting

## 1. Setting

Let

\[
C
\]

be a strictly convex normal neighborhood in a smooth time-oriented Lorentzian spacetime.

Let

\[
p\ll q
\]

with

\[
\overline{D}
\subset C,
\qquad
D=I(p,q).
\]

For

\[
x\in D,
\]

define

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

Because all relevant point pairs lie in \(C\), Synge's world function

\[
\sigma(y,x)
\]

is smooth off the diagonal on the full two-point domain used below.

## 2. Distributional representation

Choose a smooth coordinate chart containing \(\overline D\), with physical volume density

\[
d\operatorname{Vol}_g(y)
=
\rho(y)\,d^dy.
\]

Inside the convex normal domain, chronological relation is characterized by the sign of the world function plus the fixed time orientation.

Thus, after restricting to the time-oriented component,

\[
\tau_-(x)
=
\int_C
H[-\sigma(p,y)]
H[-\sigma(y,x)]
\chi_{p\prec y\prec x}
\rho(y)\,d^dy.
\]

The orientation factor is locally constant away from the null boundary and introduces no additional moving hypersurface.

## 3. Differentiation formula

Let

\[
Z\in T_xM.
\]

After the temporal-selector observation above, differentiate only the moving null Heaviside factor.

Formally,

\[
D_x H[-\sigma(y,x)][Z]
=
-\delta(\sigma(y,x))
D_x\sigma(y,x)[Z].
\]

Using an auxiliary smooth Riemannian metric \(h\) and the coarea formula gives

\[
\boxed{
D\tau_-(x)[Z]
=
-
\int_{\mathcal N_x^-}
\frac{
D_x\sigma(y,x)[Z]
}{
|\nabla_y^h\sigma(y,x)|_h
}
\rho(y)\,
dS_h(y),
}
\]

where

\[
\mathcal N_x^-
=
\partial I^-(x)\cap I^+(p)
\]

up to the codimension-two intersection with \(\partial I^+(p)\).

This formula is independent of the auxiliary Riemannian metric because it is simply the invariant hypersurface shape derivative written in coarea form.

## 4. Regularity away from the cone vertex

For

\[
y\ne x
\]

on the regular null cone,

\[
d_y\sigma(y,x)\ne0.
\]

Hence the integrand is smooth jointly in:

- \(x\);
- \(y\);
- \(Z\);

as long as \(y\) remains away from the cone vertex and from the transverse edge.

The moving null hypersurface depends smoothly on \(x\) by the implicit-function theorem.

## 5. Behavior near the cone vertex

Use normal coordinates centered at \(x\).

For a null generator,

\[
y=\exp_x(-r k),
\]

with \(r\downarrow0\) and \(k\) a normalized past-directed null direction.

The endpoint derivative satisfies

\[
D_x\sigma(y,x)[Z]
=
r\,g_x(k,Z)
+
O(r^2).
\]

Also,

\[
|\nabla_y^h\sigma(y,x)|_h
=
r\,c_h(k)
+
O(r^2),
\]

with

\[
c_h(k)>0.
\]

Therefore the quotient

\[
\frac{
D_x\sigma(y,x)[Z]
}{
|\nabla_y^h\sigma(y,x)|_h
}
\]

remains uniformly bounded as \(r\to0\).

The null-cone surface measure behaves as

\[
r^{d-2}\,dr\,d\theta.
\]

Hence the vertex contribution is integrable for every

\[
d\ge2.
\]

Moreover, the integral over

\[
0<r<\epsilon
\]

tends uniformly to zero with \(\epsilon\).

Thus the cone vertex creates no differentiability singularity.

## 6. Behavior at the codimension-two cutoff

The integration surface is truncated where the past null cone of \(x\) meets the fixed future null boundary of \(p\).

Inside a strictly convex normal diamond these two null hypersurfaces meet transversely.

Therefore, in local coordinates near their intersection, the moving integration domain has a smooth codimension-two boundary.

The boundary displacement under \(x\)-variation is smooth.

A codimension-two moving boundary produces no additional first-order bulk term in the hypersurface integral; its effect is already contained in the smooth variation of the integration surface.

Uniform transversality gives uniform local bounds.

## 7. Continuity of the derivative

Split the null cone into:

1. a small vertex neighborhood;
2. finitely many regular compact cone charts;
3. finitely many transverse edge charts.

The vertex piece is uniformly negligible.

On every regular/edge chart, the integrand and parameterized surface depend continuously on \(x\) and \(Z\), with a uniform integrable bound.

Dominated convergence therefore gives continuity of

\[
(x,Z)
\mapsto
D\tau_-(x)[Z].
\]

Linearity in \(Z\) is immediate from the formula.

Hence

\[
\boxed{
\tau_-\in C^1(D).
}
\]

Time reversal gives

\[
\boxed{
\tau_+\in C^1(D).
}
\]

## 8. Strict positivity on the future causal cone

Let

\[
Z
\]

be future-directed causal and nonzero.

On the past null cone of \(x\), write

\[
y=\exp_x(-r k),
\]

where \(k\) is future-directed null at \(x\).

For signature \((-+\cdots+)\),

\[
g_x(k,Z)\le0,
\]

with equality only when both \(k\) and \(Z\) are null and parallel.

Hence

\[
D_x\sigma(y,x)[Z]
\le0.
\]

For almost every null direction,

\[
D_x\sigma(y,x)[Z]<0.
\]

The remaining factors in the shape-derivative integral are positive.

Therefore

\[
\boxed{
D\tau_-(x)[Z]>0
}
\]

for every nonzero future-directed causal \(Z\).

Thus the metric dual of \(d\tau_-\) is past-directed timelike.

## 9. Future-volume sign

By the time-reversed argument,

\[
\boxed{
D\tau_+(x)[Z]<0
}
\]

for every nonzero future-directed causal \(Z\).

Thus the metric dual of \(d\tau_+\) is future-directed timelike.

## 10. Finite-diamond volume-time function

Define

\[
\Phi(x)
=
\frac{
\tau_-(x)-\tau_+(x)
}{
V_D
}.
\]

For every nonzero future-directed causal \(Z\),

\[
D\Phi(x)[Z]
=
\frac{
D\tau_-(x)[Z]
-
D\tau_+(x)[Z]
}{
V_D
}
>0.
\]

Therefore

\[
\boxed{
\Phi\in C^1(D)
}
\]

and

\[
\boxed{
d\Phi
\text{ is temporal everywhere in }D.
}
\]

## 11. Relation to Chrusciel-Grant-Minguzzi

Chrusciel, Grant, and Minguzzi develop a closely related null-cone variation formula for weighted Geroch volume functions.

Their differentiability theorem applies to a controlled class of weights and does **not** imply differentiability for constant weight on every bounded globally hyperbolic subspacetime.

They explicitly exhibit a bounded Minkowski-subspacetime counterexample for weight \(1\) with a non-smooth causal boundary.

The present lemma avoids that pathology by imposing:

- strict convex-normal containment;
- no null cut/conjugate locus;
- smooth null boundary sheets;
- transverse codimension-two intersection.

Thus the literature supplies the established variation mechanism, while the finite convex-diamond \(C^1\) conclusion is proved here from the stronger local geometry.

## 12. Consequence

The local curved orientation-recovery theorem does not need to assume volume-time regularity separately.

For sufficiently small diamonds contained in the nested strongly-causal/strictly-convex local construction,

\[
\boxed{
\Phi\in C^1
\quad\text{and}\quad
d\Phi\text{ temporal}
}
\]

follow from the geometry.
