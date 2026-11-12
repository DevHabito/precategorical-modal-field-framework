# Theorem: regular curved boundary geometry for causal-comparability graphons in fixed d >= 3

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** analytic theorem package under regular null-joint and tip hypotheses
**Physical status:** curvature-robust degree tails, internal sparsity, comparable balls, and tip clearance

## 1. Setting

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth \(d\)-dimensional Lorentzian spacetime, with fixed integer

\[
d\ge3.
\]

Use normalized physical volume

\[
\mathcal V(a,b)
=
\frac{
\operatorname{Vol}_g(I(a,b))
}{
V_D
},
\qquad
V_D=\operatorname{Vol}_g(D).
\]

Set

\[
m=\frac d2.
\]

Assume:

1. a smooth compact transverse null joint
   \[
   \Sigma=\partial I^+(p)\cap\partial I^-(q);
   \]
2. regular volume-null coordinates
   \[
   a=\mathcal V(p,\cdot)^{1/m},
   \qquad
   b=\mathcal V(\cdot,q)^{1/m};
   \]
3. a regular double-null causal cap near \(\Sigma\);
4. no relevant cut/conjugate degeneration;
5. a nondegenerate temporal finite-diamond volume gradient away from the joint;
6. nondegenerate temporal co-degree gradients at the two timelike tips;
7. regular noncaustic tip cones.

These hypotheses are supplied by the Penrose/null-Fermi regularity theorems in the repository.

## 2. Exact graphon degree identity

For any interior point \(x\),

\[
A_x
=
I(p,x)
\;\dot\cup\;
I(x,q)
\]

up to null boundaries.

Therefore

\[
\boxed{
Q(x)
=
\mathcal V(p,x)
+
\mathcal V(x,q).
}
\]

In volume-null coordinates,

\[
\boxed{
Q(x)
=
a^m+b^m.
}
\]

This identity is exact in every spacetime dimension.

## 3. Low-degree tail

Let

\[
g_d(q)
=
\mu\{x:Q(x)\le q\}.
\]

For sufficiently small \(q\), the sublevel set lies in the joint chart.

Write the normalized spacetime density as

\[
J(a,b,\sigma).
\]

Then

\[
g_d(q)
=
\int_\Sigma
\int_{a^m+b^m\le q}
J(a,b,\sigma)
\,da\,db\,d\sigma.
\]

Scale

\[
a=q^{1/m}u,
\qquad
b=q^{1/m}v.
\]

Since

\[
da\,db
=
q^{2/m}
du\,dv,
\]

and

\[
\frac2m=\frac4d,
\]

we obtain

\[
\boxed{
g_d(q)
\sim
C_{\Sigma,d}
q^{4/d}.
}
\]

The coefficient is

\[
\boxed{
C_{\Sigma,d}
=
A_m
\int_\Sigma
J(0,0,\sigma)
\,d\sigma,
}
\]

where

\[
\boxed{
A_m
=
\int_{\substack{u,v\ge0\\u^m+v^m\le1}}
du\,dv
=
\frac1m
B\left(
\frac1m,
1+\frac1m
\right).
}
\]

Using the joint metric

\[
g
=
2\chi\,da\,db+h_\Sigma+\cdots,
\]

\[
J(0,0,\sigma)
=
\frac{
\chi(\sigma)
\sqrt{\det h}
}{
V_D
}.
\]

Thus the coefficient has the invariant form

\[
\boxed{
C_{\Sigma,d}
=
\frac{
A_m
}{
V_D
}
\int_\Sigma
\chi\,dA_\Sigma.
}
\]

## 4. Isolated-vertex scale

For an iid size-\(n\) graphon sample,

\[
\mathbb E[I_n]
=
n
\mathbb E[
(1-Q(X))^{n-1}
].
\]

Using

\[
g_d(q)
\sim
C_{\Sigma,d}q^{4/d},
\]

Laplace-Stieltjes transfer gives

\[
\boxed{
\mathbb E[I_n]
\sim
C_{\Sigma,d}
\Gamma\left(
1+\frac4d
\right)
n^{1-4/d}.
}
\]

Therefore:

- \(d=3\): isolates disappear;
- \(d=4\): the isolate count stays at order one;
- \(d>4\): the expected isolate count grows sublinearly.

This dimension threshold is curvature-robust in the regular class.

## 5. Internal low-degree sparsity

Let

\[
S_t
=
\{x:Q(x)\le t\}.
\]

If \(x,y\in S_t\), then

\[
a,b
=
O(t^{1/m}).
\]

For a comparable pair with volume-null increments \(A,B\),

\[
0\le A,B\le Ct^{1/m}.
\]

The tangential causal cap has coordinate volume

\[
O(
(AB)^{m-1}
).
\]

Therefore, uniformly in \(x\in S_t\),

\[
\begin{aligned}
\mu(
A_x\cap S_t
)
&\le
C
\int_0^{Ct^{1/m}}
\int_0^{Ct^{1/m}}
(AB)^{m-1}
\,dA\,dB\\
&=
O(t^2).
\end{aligned}
\]

Hence

\[
\boxed{
\sup_{x\in S_t}
\mu(
A_x\cap S_t
)
=
O(t^2).
}
\]

The exponent \(2\) is independent of spacetime dimension.

## 6. Uniform comparable-disagreement balls

Define

\[
B_t(x)
=
\{
z:z\sim x,\,
\Delta_g(x,z)\le t
\}.
\]

Then

\[
\boxed{
\sup_x
\mu(B_t(x))
=
O(t^2).
}
\]

### Low-degree regime

The general graphon inequality

\[
|Q(x)-Q(z)|
\le
\Delta_g(x,z)
\]

places both points in a low-degree layer.

Section 5 then gives \(O(t^2)\).

### Joint transition

In the joint chart the disagreement is comparable to

\[
g_m(a,A)
+
g_m(b,B).
\]

Let \(L_t(u)\) be the maximal one-side increment allowed by

\[
g_m(u,L_t(u))\le Ct.
\]

Then

\[
L_t(u)^m
\le
C
\begin{cases}
t,
&
u^m\le Ct,
\\[4pt]
t^m
u^{-m(m-1)},
&
u^m>Ct.
\end{cases}
\]

The tangential cap integration gives conditional volume bounded by

\[
C
L_t(a)^m
L_t(b)^m.
\]

If

\[
Q(x)=a^m+b^m>Ct,
\]

at least one side is in the second regime.

Exactly as in the flat all-dimensional proof, every case yields

\[
O(t^2).
\]

### Bulk

Away from the joint, the temporal finite-diamond volume gradient gives

\[
\Delta_g(x,\exp_xh)
=
d\Phi_x(h)
+
O(|h|^2).
\]

The small-disagreement timelike displacement region has volume

\[
O(t^d),
\]

which is

\[
O(t^2)
\]

for every

\[
d\ge2.
\]

Thus the bound is uniform.

## 7. Near-universal co-degree tail

Define

\[
R(x)=1-Q(x).
\]

Assume the differential \(dR\) at each timelike tip is nonzero and timelike.

Let

\[
\kappa_p
=
\sqrt{
-g^{-1}_p(dR_p,dR_p)
},
\]

and similarly \(\kappa_q\).

A local Lorentz-frame cone-volume calculation gives

\[
\boxed{
\bar g_d(r)
:=
\mu\{R\le r\}
\sim
C_{\mathrm{tip},d}
r^d,
}
\]

where

\[
\boxed{
C_{\mathrm{tip},d}
=
\frac{
\omega_{d-1}
}{
dV_D
}
\left(
\kappa_p^{-d}
+
\kappa_q^{-d}
\right).
}
\]

Thus the near-universal exponent is exactly \(d\).

## 8. Sampled small-co-degree bound

The co-degree tail implies

\[
\boxed{
\mathbb E
\#\{
v:
\overline{\deg}(v)\le L
\}
\le
C_d
\frac{
(L+d)^d
}{
n^{d-1}
}
}
\]

for \(L=o(n)\).

This is the same binomial-mixture/Stieltjes estimate as in the flat theorem.

## 9. Curved tip middle band in general dimension

Parameterize the regular future null cone from \(p\) by

\[
z=z(\lambda,\theta),
\]

where

\[
\theta\in S^{d-2}.
\]

Moving the tip to

\[
x_\varepsilon
=
\exp_p(\varepsilon v)
\]

changes Synge's world function to first order by

\[
d_p\sigma(v)
=
-\lambda
g(v,k_\theta).
\]

The shifted null boundary therefore sweeps a first-order volume density

\[
\varepsilon
H(\lambda,\theta)
[-g(v,k_\theta)]
\,d\lambda\,d\theta,
\]

with

\[
H>0
\]

smooth before caustics.

Choose a fixed affine band

\[
aL(\theta)
\le
\lambda
\le
bL(\theta),
\qquad
0<a<b<1.
\]

Compactness gives a uniform positive ratio between the band flux and the total flux for every null direction.

Therefore there exist constants

\[
c_0>0,
\qquad
0<q_-<q_+<1
\]

such that every sufficiently near-tip point has a nonneighbor middle band satisfying

\[
\boxed{
\mu(
B_x^{\mathrm{mid}}
)
\ge
c_0R(x),
}
\]

with

\[
\boxed{
q_-
\le
Q(z)
\le
q_+
}
\]

throughout that band up to a negligible higher-order subset.

## 10. Tip-clear candidate rate

Conditioned on continuum co-degree

\[
R(x)=r,
\]

the probability that all other sampled points miss the middle band is at most

\[
e^{-cnr}.
\]

Therefore the expected number of tip-clear candidates is

\[
n
\int
e^{-cnr}
\,d\bar g_d(r).
\]

Since

\[
\bar g_d(r)=O(r^d),
\]

\[
\boxed{
\mathbb E[
\#\text{ tip-clear candidates}
]
=
O(n^{1-d}).
}
\]

Thus near-whole-module candidates are extremely rare in every fixed dimension.

## 11. Consequence for near-whole modules

On the event of a unique edge-containing component, a proper near-whole module requires a complete external vertex.

Outside an exponentially small deviation event, that vertex must lie in the near-universal tip regime.

If its middle band contains a sampled point, the intermediate-degree point cannot have either module-compatible external type relative to an \(n-o(n)\) block.

Hence the module requires a tip-clear candidate.

Therefore

\[
\boxed{
\Pr(
\text{near-whole proper non-stable module}
)
=
O(n^{1-d})
+
e^{-\Theta(n)}.
}
\]

## 12. Summary of curvature-robust exponents

For every regular curved fixed-dimensional diamond,

\[
\boxed{
g_d(q)
\asymp
q^{4/d},
}
\]

\[
\boxed{
\sup_{x\in S_q}
\mu(A_x\cap S_q)
=
O(q^2),
}
\]

\[
\boxed{
\sup_x
\mu(B_t(x))
=
O(t^2),
}
\]

and

\[
\boxed{
\bar g_d(r)
\asymp
r^d.
}
\]

These are exactly the boundary exponents needed by the all-dimensional orientation-recovery proof.

Curvature changes their coefficients but not their powers, as long as the null joint and tip cones remain regular.
