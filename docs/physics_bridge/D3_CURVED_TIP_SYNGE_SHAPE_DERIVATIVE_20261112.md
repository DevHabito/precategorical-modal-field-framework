# Theorem: Synge-world-function proof of the curved 2+1 tip middle-band estimate

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic first-variation theorem under a regular null-cone band hypothesis  
**Physical status:** closes the swept-volume obligation in the curved \(2+1\) near-whole-module argument  
**Literature basis:** Synge's world function and its endpoint derivatives are classical; the application to the arrow-erasure middle band is project-specific

## 1. Setting

Let

\[
D=I(p,q)
\]

be a compact causally convex \(2+1\)-dimensional Lorentzian Alexandrov interval.

Consider the future null cone of \(p\).

Choose a compact regular band

\[
\mathcal N_{\rm mid}
\subset
\partial I^+(p)\cap D
\]

with the following properties:

1. the null generators contain no conjugate or cut points on the band;
2. every point of the band is connected to \(p\) by a unique null geodesic inside a common normal-geodesic tube;
3. the affine parameter satisfies
   \[
   0<\lambda_0\le\lambda\le\lambda_1<\infty;
   \]
4. the graphon degree along a sufficiently small tubular neighborhood of the band satisfies
   \[
   0<q_-<Q(z)<q_+<1.
   \]

Let

\[
x=\exp_p(h)
\]

approach \(p\) through future timelike directions.

## 2. Synge world function

Inside the regular geodesic tube, let

\[
\sigma(x,z)
\]

be Synge's world function, one half of the signed squared geodesic distance.

The null cone of \(x\) is locally characterized by

\[
\boxed{
\sigma(x,z)=0.
}
\]

For the original tip,

\[
\sigma(p,z)=0
\qquad
(z\in\mathcal N_{\rm mid}).
\]

The absence of cut/conjugate points makes \(\sigma\) smooth in both endpoints on the chosen two-point domain.

## 3. Endpoint derivative

Let

\[
\gamma_z:[0,\lambda]\to M
\]

be the null geodesic from \(p\) to \(z\), affinely parametrized, and let

\[
k_z=\dot\gamma_z(0).
\]

The standard first-variation formula for Synge's world function gives

\[
\boxed{
D_x\sigma(p,z)[h]
=
-\lambda\,g_p(h,k_z),
}
\]

up to the chosen affine normalization.

Because

\[
\lambda\in[\lambda_0,\lambda_1],
\]

the affine factor is uniformly bounded above and below by positive constants.

## 4. A transverse coordinate to the null cone

Choose a smooth vector field

\[
N_z
\]

along the compact band, transverse to the null hypersurface.

Normalize it so that

\[
\boxed{
D_z\sigma(p,z)[N_z]
}
\]

is bounded away from zero uniformly:

\[
0<c_N
\le
|D_z\sigma(p,z)[N_z]|
\le
C_N.
\]

This is possible because

\[
d_z\sigma(p,z)\ne0
\]

on a regular null cone away from the vertex and caustics.

Use a tubular coordinate

\[
\rho
\]

defined by

\[
z_\rho=\exp_z(\rho N_z).
\]

## 5. Implicit-function theorem

Define

\[
G(h,z,\rho)
=
\sigma(
\exp_p h,
z_\rho
).
\]

At

\[
h=0,
\qquad
\rho=0,
\]

\[
G(0,z,0)=0,
\]

and

\[
\partial_\rho G(0,z,0)
=
D_z\sigma(p,z)[N_z]
\]

is uniformly nonzero.

The parameter-dependent implicit-function theorem therefore gives a unique smooth boundary displacement

\[
\rho=\rho(h,z)
\]

for all sufficiently small \(h\), uniformly over the compact band, such that

\[
G(h,z,\rho(h,z))=0.
\]

Its first variation is

\[
\begin{aligned}
\rho(h,z)
&=
-
\frac{
D_x\sigma(p,z)[h]
}{
D_z\sigma(p,z)[N_z]
}
+
O(|h|^2)\\
&=
\boxed{
c(z)\,
[-g_p(h,k_z)]
+
O(|h|^2),
}
\end{aligned}
\]

where

\[
0<c_*\le c(z)\le c^*<\infty
\]

after choosing the transverse orientation consistently.

## 6. Uniform positive angular sector

Let the near-tip co-degree first variation be

\[
R(\exp_p h)
=
\Lambda_p(h)+O(|h|^2),
\]

where

\[
\Lambda_p
\]

is a future-positive timelike covector.

Normalize causal directions by

\[
\Lambda_p(h)=1.
\]

The section

\[
\mathcal H
=
\{
h:
h\text{ future causal},
\ \Lambda_p(h)=1
\}
\]

is compact.

Parametrize null directions at \(p\) by \(\theta\) and write

\[
k(\theta).
\]

Define

\[
f_h(\theta)
=
-g_p(h,k(\theta)).
\]

For every

\[
h\in\mathcal H,
\]

\[
f_h(\theta)\ge0
\]

and it is not identically zero.

Its angular average

\[
A(h)
=
\int f_h(\theta)\,d\theta
\]

is continuous and strictly positive on the compact set \(\mathcal H\).

Therefore

\[
A_*
=
\min_{h\in\mathcal H}A(h)
>
0.
\]

Also

\[
f_h(\theta)\le C_*
\]

uniformly.

Hence there exist constants

\[
c_f>0,
\qquad
m_f>0
\]

such that for every normalized future causal \(h\),

\[
\boxed{
\operatorname{meas}
\{
\theta:
f_h(\theta)\ge c_f
\}
\ge
m_f.
}
\]

Rescaling gives, for arbitrary sufficiently small future causal \(h\),

\[
-g_p(h,k(\theta))
\ge
c_f\Lambda_p(h)
\]

on an angular set of measure at least \(m_f\).

## 7. Swept null-cone band

Restrict the regular null band to those angular directions.

For every such generator,

\[
\rho(h,z)
\ge
c\Lambda_p(h)
+
O(|h|^2).
\]

Because

\[
\Lambda_p(h)\asymp |h|
\]

on the future cone, for sufficiently small \(h\),

\[
\boxed{
\rho(h,z)
\ge
c'\Lambda_p(h).
}
\]

The tubular volume element has the form

\[
J(z,\rho)
\,d\rho\,dA_{\mathcal N},
\]

with

\[
0<J_*\le J\le J^*
\]

on the compact tube.

Integrating the region between the old and shifted null boundaries gives

\[
\boxed{
\operatorname{Vol}
(
\text{swept middle band}
)
\ge
c_0\Lambda_p(h).
}
\]

## 8. The swept region consists of nonneighbors

For \(x=\exp_p h\) future timelike and sufficiently close to \(p\), the future cone of \(x\) lies strictly inside the future cone of \(p\) in the regular band.

The region swept between the two null boundaries therefore consists of events that are:

- chronologically to the future of \(p\);
- not chronologically to the future of \(x\);
- far to the future of \(x\), so not in its causal past.

Hence the swept region is a subset of the nonneighbor set of \(x\).

Call a measurable subregion

\[
B_x^{\rm mid}.
\]

Then

\[
\boxed{
B_x^{\rm mid}
\subseteq
D\setminus A_x.
}
\]

## 9. Conversion to co-degree

The tip first variation gives

\[
R(x)
=
\Lambda_p(h)
+
O(|h|^2).
\]

Therefore

\[
\Lambda_p(h)
\asymp
R(x)
\]

for sufficiently near-tip \(x\).

Thus

\[
\boxed{
\mu(B_x^{\rm mid})
\ge
c\,R(x).
}
\]

## 10. Intermediate graphon degree

The original compact null band is separated from:

- the tip \(p\);
- the opposite tip \(q\);
- the null joint edge.

The degree function \(Q\) is continuous on its tubular neighborhood.

After shrinking the tube if needed,

\[
\boxed{
q_-
\le
Q(z)
\le
q_+
\qquad
(z\in B_x^{\rm mid}),
}
\]

with

\[
0<q_-<q_+<1.
\]

This is exactly the middle-band property needed in the near-whole-module proof.

## 11. Near-whole consequence

The co-degree tail is

\[
\bar g_3(r)
=
\Theta(r^3).
\]

A near-whole module requires a complete external vertex \(u\).

Outside an exponentially small degree-deviation event, such a vertex must be near a tip.

For the module to survive, the sampled point set must miss

\[
B_u^{\rm mid},
\]

because any sampled point in that band has intermediate degree and cannot be complete or anticomplete to an \(n-o(n)\) module except with probability \(e^{-\Theta(n)}\).

Conditioned on \(u\),

\[
\Pr(
B_u^{\rm mid}
\text{ empty}
)
\le
e^{-cnR(u)}.
\]

Integrating,

\[
n
\int
e^{-cnr}
\,d\bar g_3(r)
=
O(n^{-2}).
\]

Therefore

\[
\boxed{
\Pr(
\text{near-whole module}
)
=
O(n^{-2})
+
e^{-\Theta(n)}.
}
\]

## 12. Literature boundary

The world-function ingredients are classical:

- \(\sigma\) is smooth on a geodesically regular two-point domain;
- its endpoint gradient is the affinely scaled geodesic tangent;
- null hypersurfaces in a regular normal tube are locally given by \(\sigma=0\).

The present proof uses these facts with a parameter-dependent implicit-function theorem to calculate the volume swept by moving the cone vertex.

This closes the shape-derivative obligation identified in the curved-recovery audit without importing an unverified standalone null-cone shape theorem.

## 13. Remaining assumptions

The result still requires a regular middle null band.

It does not cover a band containing:

- conjugate points;
- cut points;
- caustics;
- nonsmooth cone self-intersections.

Those are genuine geometric regimes requiring separate analysis.
