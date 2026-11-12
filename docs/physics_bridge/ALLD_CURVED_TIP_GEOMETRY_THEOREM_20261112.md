# Theorem: regular curved all-dimensional tip co-degree and middle-band geometry

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem under a regular timelike-tip/null-cone hypothesis  
**Physical status:** curvature-robust tip estimate used to suppress near-whole modules in every fixed dimension

## 1. Setting

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth time-oriented Lorentzian spacetime of dimension

\[
d\ge3.
\]

Let

\[
Q(x)=\mu(A_x),
\qquad
R(x)=1-Q(x).
\]

Assume the future-volume function

\[
F(x)
=
\frac{
\operatorname{Vol}(I(x,q))
}{
V_D
}
\]

has a nonzero temporal first derivative at \(p\).

Write

\[
\Lambda_p
=
-dF_p.
\]

Assume also that the future null cone of \(p\) contains a compact regular middle affine band free of cut and conjugate points.

The time-reversed hypotheses hold at \(q\).

## 2. Co-degree first variation

Let

\[
x=\exp_p h
\]

with \(h\) future timelike and small.

The degree decomposes as

\[
Q(x)
=
\mathcal V(p,x)
+
\mathcal V(x,q).
\]

The small local interval satisfies

\[
\mathcal V(p,x)
=
O(|h|^d).
\]

Taylor expansion of the future-volume term gives

\[
\mathcal V(x,q)
=
1
-
\Lambda_p(h)
+
o(|h|).
\]

Therefore

\[
\boxed{
R(x)
=
\Lambda_p(h)
+
o(|h|).
}
\]

Because \(\Lambda_p\) is temporal,

\[
R(x)
\asymp
|h|
\]

uniformly on the future causal cone near the origin.

## 3. Co-degree tail

Define

\[
\bar g_{d,g}(r)
=
\mu\{x:R(x)\le r\}.
\]

The condition

\[
R(x)\le r
\]

is equivalent, up to fixed constants, to

\[
\Lambda_p(h)\le Cr
\]

inside a \(d\)-dimensional future timelike cone.

The cone cut by a timelike linear functional has volume proportional to

\[
r^d.
\]

Hence

\[
\boxed{
\bar g_{d,g}(r)
=
\Theta(r^d).
}
\]

The same result holds at the future tip.

## 4. Regular null middle band

Choose a compact subset

\[
\mathcal N_{\rm mid}
\]

of the future null cone of \(p\), parametrized by:

- affine parameter
  \[
  \lambda\in[\lambda_0,\lambda_1];
  \]
- null direction
  \[
  \theta\in S^{d-2}.
  \]

Assume the band lies inside a geodesically regular two-point domain.

Because it is separated from the tips and the codimension-two edge, continuity of \(Q\) gives

\[
\boxed{
0<q_-<Q(z)<q_+<1
}
\]

on a sufficiently small tubular neighborhood of the band.

## 5. Synge-world-function displacement

Let

\[
\sigma(x,z)
\]

be Synge's world function on the regular two-point domain.

The original cone is

\[
\sigma(p,z)=0.
\]

For

\[
x=\exp_p h,
\]

the shifted cone is

\[
\sigma(x,z)=0.
\]

If \(k_z\) is the future null tangent at \(p\) along the generator through \(z\), then the endpoint first variation gives

\[
\boxed{
D_x\sigma(p,z)[h]
=
-\lambda
g_p(h,k_z).
}
\]

Choose a smooth transverse field \(N_z\) along the band with

\[
D_z\sigma(p,z)[N_z]
\]

bounded away from zero.

The parameter-dependent implicit-function theorem gives the transverse shifted-cone displacement

\[
\boxed{
\rho(h,z)
=
c(z)
[-g_p(h,k_z)]
+
O(|h|^2),
}
\]

with \(c(z)\) positive and uniformly bounded.

## 6. Uniform positive-measure angular sector

Normalize future causal directions by

\[
\Lambda_p(h)=1.
\]

This normalized section is compact.

Define

\[
f_h(\theta)
=
-g_p(h,k(\theta)).
\]

For each normalized \(h\),

\[
f_h\ge0
\]

and is not identically zero.

The integral

\[
A(h)
=
\int_{S^{d-2}}
f_h(\theta)\,d\theta
\]

is continuous and strictly positive on the compact normalized causal section.

Hence there exist

\[
c_f>0,
\qquad
m_f>0
\]

such that for every normalized \(h\),

\[
\operatorname{meas}
\{
\theta:
f_h(\theta)\ge c_f
\}
\ge
m_f.
\]

Undoing the normalization,

\[
-g_p(h,k(\theta))
\ge
c_f\Lambda_p(h)
\]

on a direction set of uniformly positive measure.

## 7. Swept middle-band volume

On that angular sector,

\[
\rho(h,z)
\ge
c\Lambda_p(h)
\]

for sufficiently small \(h\).

The tubular volume density is smooth and positive.

Integrating over:

- the fixed affine interval;
- the positive-measure angular sector;
- the swept transverse thickness;

gives

\[
\boxed{
\mu(B_x^{\rm mid})
\ge
c_0\Lambda_p(h).
}
\]

Since

\[
R(x)
=
\Lambda_p(h)+o(|h|),
\]

we obtain

\[
\boxed{
\mu(B_x^{\rm mid})
\ge
cR(x).
}
\]

The swept band consists of nonneighbors of \(x\).

## 8. Intermediate-degree property

By construction,

\[
B_x^{\rm mid}
\]

lies in the fixed tubular neighborhood of the regular affine band.

Therefore

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

## 9. Near-whole-module probability

Suppose a sampled vertex \(u\) is complete to a module containing

\[
n-o(n)
\]

vertices.

Except on an exponentially small sampled-co-degree deviation event, \(u\) must satisfy small continuum co-degree \(R(u)\).

A sampled point in

\[
B_u^{\rm mid}
\]

has degree bounded away from both zero and one, so it cannot be complete or anticomplete to an \(n-o(n)\) module except with probability

\[
e^{-\Theta(n)}.
\]

Therefore the middle band must be empty.

Conditioned on \(u\),

\[
\Pr(
B_u^{\rm mid}
\text{ empty}
)
\le
e^{-cnR(u)}.
\]

The expected number of such tip-clear candidates is bounded by

\[
n
\int
e^{-cnr}
\,d\bar g_{d,g}(r).
\]

Using

\[
\bar g_{d,g}(r)
=
O(r^d),
\]

Laplace-Stieltjes asymptotics give

\[
\boxed{
n
\int
e^{-cnr}
\,d\bar g_{d,g}(r)
=
O(n^{1-d}).
}
\]

Thus

\[
\boxed{
\Pr(
\text{near-whole module}
)
=
O(n^{1-d})
+
e^{-\Theta(n)}.
}
\]

## 10. Comparison with the true-twin scale

For \(d=3\),

\[
n^{1-d}
=
n^{-2}
=
o(n^{-1}).
\]

For \(d\ge4\),

\[
n^{1-d}
=
o(n^{-4/d}).
\]

Thus near-whole modules are subleading in every fixed dimension

\[
d\ge3.
\]

## 11. Structural interpretation

The tip exponent

\[
d
\]

comes from ordinary \(d\)-dimensional timelike-cone volume near a tip.

It is independent of the codimension-two null-joint mechanism controlling low degrees.

The two boundary geometries therefore play complementary roles:

- the null edge controls rare low-degree/twin defects;
- the timelike tips suppress near-universal vertices and near-whole modules.
