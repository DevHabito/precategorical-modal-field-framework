# Exact diagnostic: conjugate-point breakdown of thin-null compact containment in a plane wave

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact model calculation  
**Purpose:** identify a genuine failure mechanism for the regular thin-null universality class  
**Literature boundary:** focusing and conjugate points in plane waves are classical; the project-specific point is their effect on the splitter-volume scaling used by arrow-erasure recovery

## 1. Model

Consider the \(2+1\)-dimensional constant-profile plane wave

\[
\boxed{
ds^2
=
2\,du\,dv
+
dy^2
-
\omega^2y^2\,dv^2,
}
\]

with

\[
\omega>0.
\]

The distinguished null geodesic is

\[
\gamma(v)=(0,v,0).
\]

Take endpoints

\[
P_a=(0,0,0),
\]

\[
Q_a=(-a,L,0),
\qquad
a>0.
\]

The parameter \(a\) measures inward timelike displacement from the exactly null endpoint configuration.

## 2. Causal action

Let a future causal curve from \(P_a\) to \(Q_a\) be parameterized by \(v\):

\[
c(v)
=
(u(v),v,y(v)).
\]

The causal inequality is

\[
2\dot u
+
\dot y^2
-
\omega^2y^2
\le0.
\]

Integrating from \(0\) to \(L\),

\[
2[u(L)-u(0)]
+
\int_0^L
(\dot y^2-\omega^2y^2)\,dv
\le0.
\]

Since

\[
u(L)-u(0)=-a,
\]

we obtain

\[
\boxed{
Q_L[y]
:=
\int_0^L
(\dot y^2-\omega^2y^2)\,dv
\le
2a.
}
\]

For the transverse endpoint conditions,

\[
y(0)=y(L)=0.
\]

Thus the geometry is controlled exactly by the Dirichlet index form

\[
Q_L.
\]

## 3. Spectrum

The Dirichlet eigenfunctions are

\[
e_k(v)
=
\sin\left(
\frac{k\pi v}{L}
\right),
\]

with eigenvalues

\[
\boxed{
\lambda_k(L)
=
\left(
\frac{k\pi}{L}
\right)^2
-
\omega^2.
}
\]

The first eigenvalue is

\[
\boxed{
\lambda_1(L)
=
\left(
\frac{\pi}{L}
\right)^2
-
\omega^2.
}
\]

The first conjugate point occurs at

\[
\boxed{
L_c
=
\frac{\pi}{\omega}.
}
\]

## 4. Before the first conjugate point

If

\[
L<L_c,
\]

then

\[
\lambda_1(L)>0.
\]

Poincare/spectral coercivity gives

\[
Q_L[y]
\ge
\lambda_1(L)
\int_0^L
y(v)^2\,dv.
\]

Together with

\[
Q_L[y]\le2a,
\]

this gives

\[
\int_0^L
y^2\,dv
\le
\frac{2a}{
\lambda_1(L)
}.
\]

The one-dimensional Sobolev estimate then gives

\[
\boxed{
\|y\|_\infty
\le
C(L,\omega)
\sqrt a.
}
\]

More explicitly, for the first mode

\[
y(v)
=
A
\sin\left(
\frac{\pi v}{L}
\right),
\]

\[
Q_L[y]
=
\frac L2
\lambda_1(L)
A^2.
\]

Therefore the causal inequality allows at most

\[
\boxed{
A^2
\le
\frac{
4a
}{
L\lambda_1(L)
}.
}
\]

Thus

\[
\boxed{
A_{\max}
\asymp
\sqrt{
\frac a{\lambda_1(L)}
}.
}
\]

For fixed \(L<L_c\), this is the ordinary

\[
\sqrt a
\]

Penrose transverse scaling.

## 5. Approach to the conjugate point

As

\[
L\uparrow L_c,
\]

\[
\lambda_1(L)\downarrow0.
\]

Hence the coefficient of the thin-null transverse width diverges:

\[
\boxed{
\frac{
A_{\max}
}{
\sqrt a
}
\asymp
\lambda_1(L)^{-1/2}
\to\infty.
}
\]

This gives a quantitative warning before the caustic is reached.

The regular thin-null coefficient is not uniform across a family whose first Jacobi eigenvalue approaches zero.

## 6. Exact conjugate threshold

Set

\[
L=L_c
=
\frac{\pi}{\omega}.
\]

Then

\[
\lambda_1(L_c)=0.
\]

The Jacobi mode

\[
\boxed{
y_A(v)
=
A\sin(\omega v)
}
\]

satisfies

\[
y_A(0)=y_A(L_c)=0
\]

and

\[
\boxed{
Q_{L_c}[y_A]=0
}
\]

for every amplitude

\[
A\in\mathbb R.
\]

Therefore the causal inequality

\[
Q_{L_c}[y]\le2a
\]

does not constrain \(A\).

## 7. Explicit causal curves of arbitrary transverse amplitude

Define

\[
y(v)
=
A\sin(\omega v).
\]

Choose

\[
\dot u(v)
=
-\frac12
\left(
\dot y^2-\omega^2y^2
\right)
-
\frac a{L_c}.
\]

Then

\[
2\dot u
+
\dot y^2
-
\omega^2y^2
=
-\frac{2a}{L_c}
<0.
\]

Thus the curve is strictly timelike.

Integrating,

\[
u(L_c)-u(0)
=
-\frac12Q_{L_c}[y]-a
=
-a.
\]

So it joins exactly

\[
P_a
\quad\text{to}\quad
Q_a.
\]

At the midpoint,

\[
v=\frac{L_c}{2},
\]

\[
y=A.
\]

Also,

\[
\int_0^{L_c/2}
(\dot y^2-\omega^2y^2)\,dv
=
0,
\]

so

\[
u(L_c/2)
=
-\frac a2.
\]

Therefore every point

\[
\boxed{
\left(
-\frac a2,\,
\frac{L_c}{2},\,
A
\right)
}
\]

lies on a timelike curve from \(P_a\) to \(Q_a\), for arbitrary \(A\).

Hence the causal diamond has an unbounded transverse midpoint section in the exact plane-wave model.

## 8. Consequence

At the first conjugate threshold,

\[
\boxed{
|y|=O(\sqrt a)
}
\]

is false.

Indeed there is no finite \(a\)-dependent transverse bound in the exact quadratic plane wave.

Thus Penrose-scaled compact containment fails maximally.

The regular theorem cannot be continued through a conjugate point by continuity.

## 9. After the first conjugate point

If

\[
L>L_c,
\]

then

\[
\lambda_1(L)<0.
\]

The index form has a negative direction.

Scaling the corresponding eigenfunction by an arbitrarily large amplitude makes

\[
Q_L[y]\to-\infty.
\]

The integrated causal inequality is then even easier to satisfy.

This is consistent with the well-known focusing/non-global-hyperbolicity phenomena of exact plane waves.

## 10. Causal-boundary interpretation

A conjugate point is not merely a regular point of the same null boundary with a worse coefficient.

At conjugacy the null exponential map loses rank, so the light cone develops a caustic and ceases to be an immersed smooth null hypersurface at that point.

Classical Lorentzian causality also implies that once a null generator has passed the relevant conjugate/cut threshold it cannot continue as an achronal generator of

\[
E^+(p)
=
J^+(p)\setminus I^+(p).
\]

At the first conjugate point itself one must distinguish carefully between the caustic point and the immediately post-caustic generator; in either case the **regular embedded-null-sheet hypothesis** used by the recovery theorem has failed.

Therefore the exact plane-wave calculation should be interpreted as:

\[
\boxed{
\text{conjugacy destroys the regular-edge model before one can simply assign it a new regular-edge coefficient.}
}
\]

A post-caustic theory must use the local singularity type of the wave front rather than the smooth double-null edge normal form.

Stable caustic types such as fold and cusp are classified by the established singularity theory of wave fronts.

No arrow-erasure exponent is claimed for those classes here.

## 10. Interpretation for the curved splitter program

The regular thin-null theorem uses

\[
V_{\rm thin}
\sim
\mathcal C_\gamma a^{d/2}
\]

with finite positive

\[
\mathcal C_\gamma.
\]

The plane-wave threshold shows that

\[
\mathcal C_\gamma
\]

can diverge as a conjugate point is approached.

At conjugacy the entire

\[
a^{d/2}
\]

scaling description can break down because the scaled causal domain is no longer compact.

Therefore:

\[
\boxed{
\text{conjugate points can change the thin-null universality class.}
}
\]

This is a demonstrated mechanism, not speculation.

## 11. Near-caustic double scaling

Before conjugacy,

\[
A_{\max}
\asymp
\sqrt{
\frac a{\lambda_1}
}.
\]

If a family of geometries/endpoints approaches conjugacy simultaneously with

\[
a\to0
\]

and

\[
\lambda_1
\sim
a^\gamma,
\]

then

\[
\boxed{
A_{\max}
\sim
a^{(1-\gamma)/2}.
}
\]

Thus the ordinary transverse exponent \(1/2\) is recovered only when

\[
\lambda_1
\]

stays bounded away from zero on the \(a\)-scale.

The regime

\[
\lambda_1\sim a^\gamma
\]

is a distinct near-caustic double-scaling problem.

No universal splitter exponent is claimed there.

## 12. Higher-dimensional implication

If \(r\) independent transverse Jacobi eigenvalues become small,

\[
\lambda_1,\ldots,\lambda_r\downarrow0,
\]

the quadratic thin-domain coefficient acquires factors schematically of the form

\[
\prod_{j=1}^r
\lambda_j^{-1/2}.
\]

This identifies the multiplicity of focusing as a candidate control parameter for the divergence of the regular thin-null coefficient.

At exact conjugacy, higher-order geometry beyond the quadratic Penrose plane wave is required to determine any replacement scaling law.

This final statement is a research direction, not a proved universal theorem.

## 13. Literature connection

Plane-wave focusing and the relation between conjugate points and causal structure are established in the general-relativity literature.

The exact constant-profile calculation above is elementary.

The project-specific conclusion is that the same conjugate-point threshold is precisely where the compactness assumption underlying the arrow-erasure thin-null asymptotic fails.
