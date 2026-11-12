# Lemma: uniform null index-form spectral gap on a compact conjugate-free generator family

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic compactness lemma  
**Purpose:** justify the uniform coercivity constant used in thin-null compact containment

## 1. Setting

Let

\[
\{\gamma_s\}_{s\in E}
\]

be a compact smooth family of future-directed null geodesic segments, with parameter

\[
s\in E,
\]

where \(E\) is compact.

Assume:

1. every \(\gamma_s\) lies in a regular null-Fermi tube;
2. the affine parameter interval is identified with
   \[
   [0,L_s];
   \]
3. the lengths \(L_s\) vary continuously and satisfy
   \[
   0<L_*\le L_s\le L^*<\infty;
   \]
4. no endpoint \(\gamma_s(L_s)\) is conjugate to \(\gamma_s(0)\);
5. no conjugate point occurs in the open segment.

Work in the transverse screen bundle of rank

\[
r=d-2.
\]

## 2. Dirichlet Jacobi operator

After choosing a smooth orthonormal screen frame along the family, the transverse Jacobi equation has the matrix form

\[
\ddot J
-
H_s(v)J
=
0
\]

with a continuous/smooth symmetric matrix profile

\[
H_s(v).
\]

The associated Dirichlet quadratic form is

\[
\boxed{
Q_s[w]
=
\int_0^{L_s}
\left(
|\dot w|^2
+
\langle H_s(v)w,w\rangle
\right)\,dv
}
\]

for

\[
w(0)=w(L_s)=0.
\]

The corresponding self-adjoint Dirichlet operator is

\[
\boxed{
\mathcal L_s
=
-\frac{d^2}{dv^2}
+
H_s(v).
}
\]

## 3. Pointwise positivity

For a null generator that remains on an achronal boundary before its first conjugate point, the null Morse-index theorem gives index zero.

Thus

\[
Q_s[w]\ge0
\]

for all Dirichlet screen variations.

If

\[
Q_s[w]=0
\]

for a nonzero \(w\), the basic index lemma implies that \(w\) is a Jacobi field with

\[
w(0)=w(L_s)=0.
\]

That would make the endpoints conjugate.

By assumption this does not occur.

Hence

\[
\boxed{
Q_s[w]>0
\qquad
(w\ne0).
}
\]

Equivalently, the lowest Dirichlet eigenvalue satisfies

\[
\boxed{
\lambda_1(s)>0.
}
\]

## 4. Put all operators on one fixed interval

Set

\[
v=L_s t,
\qquad
t\in[0,1].
\]

Then

\[
Q_s[w]
=
\frac1{L_s}
\int_0^1
|\partial_t\widetilde w|^2\,dt
+
L_s
\int_0^1
\langle
H_s(L_st)
\widetilde w,
\widetilde w
\rangle\,dt.
\]

Thus the rescaled Dirichlet operator on the fixed Hilbert space

\[
H_0^1([0,1];\mathbb R^r)
\]

has coefficients depending continuously on \(s\).

## 5. Continuity of the first eigenvalue

The Rayleigh quotient is

\[
\mathcal R_s[w]
=
\frac{
Q_s[w]
}{
\|w\|_{L^2}^2
}.
\]

Uniform boundedness of:

- \(L_s\);
- \(L_s^{-1}\);
- \(H_s\);

and uniform convergence of the coefficient matrices under \(s'\to s\) imply

\[
\mathcal R_{s'}[w]
\to
\mathcal R_s[w]
\]

uniformly on \(L^2\)-normalized sets with bounded \(H^1\) norm.

By the min-max principle,

\[
\boxed{
s\mapsto\lambda_1(s)
}
\]

is continuous.

Equivalent proofs follow from norm-resolvent continuity of regular matrix Sturm-Liouville operators.

## 6. Compactness gives a positive uniform gap

Because \(E\) is compact and

\[
\lambda_1(s)>0
\]

for every \(s\),

\[
\lambda_*
=
\min_{s\in E}
\lambda_1(s)
\]

exists.

Continuity gives

\[
\boxed{
\lambda_*>0.
}
\]

Therefore

\[
Q_s[w]
\ge
\lambda_*
\|w\|_{L^2}^2
\]

uniformly.

Combining with the derivative term in the quadratic form and a standard interpolation/Poincare estimate gives the stronger coercivity form

\[
\boxed{
Q_s[w]
\ge
c_*
\|w\|_{H^1}^2
}
\]

for one

\[
c_*>0
\]

independent of \(s\).

## 7. Why endpoint nonconjugacy matters

It is not enough to assume:

> no conjugate point occurs strictly before the endpoint.

If a sequence of endpoints approaches the first conjugate point, then

\[
\lambda_1(s_n)\to0
\]

is possible.

The exact constant-profile plane-wave diagnostic demonstrates this:

\[
\lambda_1(L)
=
\left(
\frac{\pi}{L}
\right)^2-\omega^2
\to0
\]

as

\[
L\uparrow\frac{\pi}{\omega}.
\]

Therefore the regular theorem needs the compact edge-generator family to stay uniformly on the conjugate-free side, including its endpoints.

For a smooth compact edge contained in a strictly convex normal neighborhood this is automatic.

## 8. Consequence for thin-null compact containment

The uniform gap is the missing compact-family input in

THIN_NULL_COMPACT_CONTAINMENT_LEMMA_20261112.md.

It makes the constants in

\[
|y|
\le
C\sqrt a
\]

and

\[
|u|
\le
Ca
\]

uniform along the entire compact edge.

Hence the Penrose-scaled domains fit inside one fixed compact set uniformly in the edge parameter.

## 9. Failure signal

If

\[
\inf_{s\in E}
\lambda_1(s)=0,
\]

then one of two things happens:

1. conjugacy is reached somewhere in the compact closure of the generator family; or
2. the family is not compact/regular enough for the continuity argument.

Thus loss of the uniform gap is itself a diagnostic of leaving the regular universality class.
