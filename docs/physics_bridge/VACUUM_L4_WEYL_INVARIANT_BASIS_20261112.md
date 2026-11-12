# Theorem: invariant basis for the first vacuum response of centered recovery coefficients

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic invariant-theory theorem  
**Scope:** centered sufficiently small regular causal diamonds in a Ricci-flat neighborhood  
**Purpose:** classify the complete parity-even \(L^4\) curvature basis before any coefficient calculation  
**Literature boundary:** the \(E/H/D\) decomposition and the vacuum identities are established; the application to the arrow-erasure coefficient \(K\) is project-specific

## 1. Setting

Let

\[
(M^d,g)
\]

be Ricci flat in a neighborhood of a point \(o\),

\[
R_{\mu\nu}=0,
\]

and let

\[
T^\mu
\]

be a unit timelike vector at \(o\).

Consider the centered small diamond

\[
D_L
=
I(
\exp_o(-LT),
\exp_o(LT)
).
\]

Let

\[
K_{d,g}(D_L)
\]

be the leading orientation-recovery error coefficient.

The centered-diamond parity theorem already gives

\[
K_{d,g}(D_L)
=
K_d^{\rm Mink}
+
O(L^4)
\]

in vacuum.

We now classify the complete scalar basis available at order \(L^4\).

## 2. Electric/magnetic/spatial Weyl decomposition

Choose an orthonormal frame adapted to

\[
T=e_0.
\]

Spatial indices are

\[
i,j,k,\ldots=1,\ldots,n,
\qquad
n=d-1.
\]

Define

\[
\boxed{
E_{ij}
=
C_{0i0j},
}
\]

\[
\boxed{
H_{ijk}
=
C_{0ijk},
}
\]

and

\[
\boxed{
D_{ijkl}
=
C_{ijkl}.
}
\]

The algebraic Weyl symmetries imply:

\[
E_{ij}=E_{ji},
\qquad
E^i{}_i=0,
\]

\[
H_{ijk}
=
-H_{ikj},
\]

\[
H_{ijk}
+
H_{jki}
+
H_{kij}
=
0,
\]

and

\[
H^i{}_{ji}=0.
\]

The purely spatial tensor \(D\) has the ordinary algebraic Riemann symmetries.

Full Weyl trace-freeness gives

\[
\boxed{
\delta^{kl}
D_{kilj}
=
E_{ij}.
}
\]

## 3. Spatial curvature decomposition of D

For spatial dimension

\[
n\ge3,
\]

decompose \(D\) as an \(n\)-dimensional algebraic curvature tensor.

Its spatial Ricci tensor is

\[
\operatorname{Ric}^{(D)}_{ij}
=
E_{ij},
\]

and its spatial scalar curvature vanishes because

\[
E^i{}_i=0.
\]

Therefore

\[
\boxed{
D_{ijkl}
=
W^{(s)}_{ijkl}
+
\frac1{n-2}
\left(
\delta_{ik}E_{jl}
-
\delta_{il}E_{jk}
-
\delta_{jk}E_{il}
+
\delta_{jl}E_{ik}
\right),
}
\]

where

\[
W^{(s)}
\]

is the trace-free spatial Weyl part.

Orthogonality of the standard Riemann decomposition gives

\[
\boxed{
D^2
=
(W^{(s)})^2
+
\frac4{n-2}E^2.
}
\]

Thus \(D^2\) contains the independent norm of the spatial Weyl piece plus a fixed electric trace contribution.

For \(n=3\), the spatial Weyl tensor vanishes identically, hence

\[
\boxed{
D^2=4E^2
\qquad
(d=4).
}
\]

## 4. Alternative contractions do not create new invariants

The algebraic Bianchi identity gives

\[
D_{ijkl}
+
D_{iklj}
+
D_{iljk}
=
0.
\]

Consequently,

\[
\boxed{
D_{ijkl}D^{ikjl}
=
\frac12D^2.
}
\]

The mixed electric-spatial contraction is

\[
\boxed{
E^{ij}
D^k{}_{ikj}
=
E^2.
}
\]

Hence no independent \(E\)-\(D\) quadratic invariant exists.

For \(H\), the hook symmetry gives

\[
\boxed{
H_{ijk}H^{jik}
=
\frac12H^2,
}
\]

and

\[
\boxed{
H_{ijk}H^{kij}
=
-\frac12H^2.
}
\]

Thus all parity-even contractions of two \(H\)'s reduce to its norm.

## 5. Why cross terms with H are absent

The centered tangent diamond is invariant under the full spatial orthogonal group

\[
O(n),
\]

not merely under \(SO(n)\).

A scalar observable cannot depend on a choice of spatial orientation.

The tensors have spatial index parity:

- \(E\): two spatial indices;
- \(D\): four spatial indices;
- \(H\): three spatial indices.

Using only \(\delta_{ij}\), a contraction containing one \(H\) and one \(E\) or \(D\) has an odd total number of spatial indices and cannot form a scalar.

A single Levi-Civita tensor could make a pseudoscalar, but it changes sign under a spatial reflection and is therefore forbidden by \(O(n)\)-invariance.

Hence no \(E\)-\(H\) or \(D\)-\(H\) cross term appears in the parity-even centered coefficient.

## 6. Complete quadratic basis for d >= 5

For

\[
d\ge5
\qquad
(n\ge4),
\]

the spatial Weyl piece \(W^{(s)}\) can be nonzero.

The three inequivalent orthogonal tensor sectors are:

1. the symmetric trace-free electric tensor \(E\);
2. the trace-free hook tensor \(H\);
3. the independent spatial Weyl tensor \(W^{(s)}\).

Their unique quadratic norms can equivalently be represented by

\[
\boxed{
E^2,
\qquad
H^2,
\qquad
D^2.
}
\]

Therefore every parity-even \(O(d-1)\)-invariant scalar quadratic in the Weyl tensor and depending on the distinguished timelike direction \(T\) has the form

\[
\boxed{
a_dE^2
+
b_dH^2
+
c_dD^2.
}
\]

The three coefficients are generically independent for

\[
d\ge5.
\]

## 7. Specialization to d = 4

For

\[
d=4,
\qquad
n=3,
\]

\[
D^2=4E^2.
\]

Dualize the last two spatial indices of \(H\):

\[
B_{ij}
=
\frac12
\epsilon_{jkl}
H_i{}^{kl}.
\]

Then

\[
\boxed{
H^2=2B^2.
}
\]

Thus the parity-even vacuum basis has only two independent elements:

\[
\boxed{
E^2,
\qquad
B^2.
}
\]

The first vacuum correction to the recovery coefficient must therefore be

\[
\boxed{
\frac{
K_{4,g}(D_L)
}{
9\pi
}
=
1
+
L^4
\left[
a_4E^2+b_4B^2
\right]_o
+
o(L^4).
}
\]

No third parity-even quadratic Weyl scalar exists.

Equivalently, using

\[
W=E^2+B^2
\]

and

\[
C_{\mu\nu\rho\sigma}
C^{\mu\nu\rho\sigma}
=
8(E^2-B^2),
\]

the same response can be written as a linear combination of

\[
W
\quad\text{and}\quad
C^2.
\]

## 8. Specialization to d = 3

In \(2+1\) spacetime,

\[
C_{\mu\nu\rho\sigma}\equiv0.
\]

Ricci flatness therefore implies local flatness.

Hence there is no nontrivial local vacuum tidal response:

\[
\boxed{
K_{3,g}(D_L)
=
K_3^{\rm Mink}
}
\]

for a Ricci-flat neighborhood, up to effects associated with global topology or leaving the local flat neighborhood.

The \(L^4\) Weyl frontier begins only at

\[
d\ge4.
\]

## 9. Potential second-derivative curvature terms

The fourth Riemann-normal-coordinate metric jet contains both:

\[
C*C
\]

and terms linear in

\[
\nabla\nabla C.
\]

We now show that the latter do not introduce an independent scalar sector in a Ricci-flat neighborhood.

## 10. Vacuum divergence identity

The contracted Bianchi identity gives, in vacuum,

\[
\boxed{
\nabla^a
C_{abcd}
=
0.
}
\]

This holds throughout the Ricci-flat neighborhood, not only at one point.

Consider an arbitrary complete scalar contraction of

\[
\nabla_e\nabla_f C_{abcd}
\]

using only:

- the metric;
- the distinguished vector \(T\).

## 11. Case 1: derivative indices do not contract into Weyl indices

Suppose neither \(e\) nor \(f\) is contracted with an index of \(C\).

After contracting the derivative indices with combinations of \(g\) and \(T\), the four Weyl indices must themselves be contracted into a scalar using \(g\) and \(T\).

But every scalar linear in a Weyl-type tensor constructed only from \(g\) and one vector \(T\) vanishes:

- a metric trace vanishes by Weyl trace-freeness;
- two \(T\)'s in one antisymmetric index pair vanish;
- four \(T\)'s vanish;
- two \(T\)'s in opposite pairs with the remaining pair traced reduce to a Weyl trace.

The same algebraic statement applies to

\[
\nabla_e\nabla_f C_{abcd}
\]

when \(e,f\) are not mixed into the Weyl slots because covariant differentiation preserves the algebraic Weyl symmetries and metric trace identities.

Hence such a scalar is zero.

## 12. Case 2: an inner derivative is a Weyl divergence

If the derivative acting directly on \(C\) is contracted with a Weyl index, the term contains a factor of the form

\[
\nabla^a C_{abcd},
\]

or an equivalent divergence related by Weyl symmetries.

It vanishes identically in vacuum.

## 13. Case 3: the outer derivative is contracted with a Weyl index

A representative term is

\[
\nabla^a\nabla_f C_{abcd}.
\]

Commute the derivatives:

\[
\begin{aligned}
\nabla^a\nabla_f C_{abcd}
&=
\nabla_f\nabla^a C_{abcd}
+
[\nabla^a,\nabla_f]C_{abcd}\\
&=
[\nabla^a,\nabla_f]C_{abcd}.
\end{aligned}
\]

The commutator of covariant derivatives acts algebraically by the Riemann tensor:

\[
[\nabla,\nabla]C
=
Riemann*C.
\]

In a Ricci-flat neighborhood,

\[
Riemann=C.
\]

Therefore

\[
\boxed{
\nabla^a\nabla_f C_{abcd}
=
C*C
}
\]

schematically.

Any complete scalar contraction of this expression is already in the quadratic Weyl sector classified above.

The same argument applies when both derivative indices are mixed into Weyl indices.

## 14. No independent linear nabla^2 C invariant

Combining the three cases:

\[
\boxed{
\text{every parity-even scalar linear in }
\nabla\nabla C
\text{ either vanishes or reduces to }
C*C
}
\]

in a Ricci-flat neighborhood.

Therefore the \(L^4\) vacuum response requires no independent second-derivative curvature coefficients.

## 15. Main vacuum basis theorem

For a centered regular causal diamond in a Ricci-flat neighborhood:

### d = 3

\[
\boxed{
K_{3,g}(D_L)=K_3^{\rm Mink}
}
\]

locally, because the Weyl tensor vanishes identically.

### d = 4

\[
\boxed{
\frac{
K_{4,g}(D_L)
}{
9\pi
}
=
1
+
L^4
\left[
a_4E^2+b_4B^2
\right]_o
+
o(L^4).
}
\]

### d >= 5

\[
\boxed{
\frac{
K_{d,g}(D_L)
}{
K_d^{\rm Mink}
}
=
1
+
L^4
\left[
a_dE^2+b_dH^2+c_dD^2
\right]_o
+
o(L^4).
}
\]

The numerical values of these universal coefficients are not determined here.

## 16. Relation to known small-diamond geometry

Jinzhao Wang decomposes the Weyl tensor exactly as

\[
E_{ij}=C_{0i0j},
\qquad
H_{ijk}=C_{0ijk},
\qquad
D_{ijkl}=C_{ijkl},
\]

and uses the superenergy density

\[
W
=
\frac12
\left[
E^2+H^2+\frac14D^2
\right].
\]

The same work records:

\[
D^2=4E^2
\qquad(d=4),
\]

and vacuum angular identities reducing the relevant tensor contractions.

Its vacuum Alexandrov-diamond area and volume corrections are explicit linear combinations of

\[
E^2,
\qquad
H^2,
\qquad
D^2,
\]

rather than new independent \(\nabla^2C\) scalars.

This is an independent consistency check on the invariant basis derived here.

It does not determine the project-specific coefficients \(a_d,b_d,c_d\).

## 17. Difference from Bel-Robinson proportionality

The basis theorem does **not** imply

\[
K^{(4)}
\propto
W.
\]

In dimensions \(d\ge5\), the three coefficients

\[
a_d,b_d,c_d
\]

need not occur in the Bel-Robinson ratio

\[
1:1:\frac14.
\]

Even in \(d=4\), a general parity-even response

\[
a_4E^2+b_4B^2
\]

is proportional to the Bel-Robinson density only if

\[
a_4=b_4.
\]

Known small-causal-diamond observables often produce different Weyl combinations; Wang explicitly finds that simple Bel-Robinson proportionality is not generic.

Therefore no superenergy interpretation should be imposed before the coefficients are calculated.

## 18. Next target

The vacuum problem is now coefficient determination rather than basis classification.

A minimal calibration program is:

### d = 4

Two independent vacuum geometries are enough to determine

\[
a_4,
\qquad
b_4.
\]

Natural candidates are:

1. a purely electric static vacuum geometry, such as a local Schwarzschild-type field;
2. a radiative/type-N plane-wave geometry, providing a different \(E^2/B^2\) ratio.

### d >= 5

Three independent vacuum calibrations are required to solve for

\[
a_d,
\qquad
b_d,
\qquad
c_d.
\]

Exact plane waves are especially useful for probing the \(H\)-containing sector, provided the centered diamond remains strictly before the first conjugate point.

No coefficient values are asserted until those calculations are performed.
