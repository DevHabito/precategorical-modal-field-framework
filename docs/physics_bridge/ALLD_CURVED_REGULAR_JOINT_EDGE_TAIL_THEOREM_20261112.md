# Theorem: universal regular curved null-joint small-disagreement law for d >= 4

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic local asymptotic theorem under regular transverse-edge hypotheses  
**Physical status:** curved-spacetime generalization of the flat null-joint exponent and leading coefficient structure  
**Novelty status:** Penrose limits and double-null geometry are classical; the arrow-erasure small-disagreement law is project-specific

## 1. Setting

Let

\[
(M^d,g)
\]

be a smooth time-oriented Lorentzian spacetime with fixed integer

\[
d\ge4.
\]

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval.

Assume the future null boundary of \(p\) and the past null boundary of \(q\) meet transversely along a compact smooth spacelike codimension-two edge

\[
E.
\]

Assume the relevant null generators:

- contain no cut points;
- contain no conjugate points;
- admit uniform compact null-Fermi tubes;
- satisfy the Penrose-scaled compact-containment condition.

Use normalized physical volume

\[
d\mu
=
\frac{
d\operatorname{Vol}_g
}{
V_D
}.
\]

## 2. Optical coordinates

Near \(E\), choose regular double-null coordinates

\[
(a,b,s^A),
\qquad
A=1,\ldots,d-2,
\]

where:

- \(a=0\) is the future null boundary of \(p\);
- \(b=0\) is the past null boundary of \(q\);
- \(s\) are coordinates on \(E\).

Write

\[
m=\frac d2.
\]

The metric has leading edge form

\[
\boxed{
g
=
-2\Omega(s)^2\,da\,db
+
h_{AB}(s)\,ds^A ds^B
+
O(a+b),
}
\]

with

\[
\Omega(s)>0
\]

and \(h_{AB}\) positive definite.

## 3. Thin-null endpoint-volume laws

The Penrose-Fermi thin-null theorem gives uniformly along the compact edge

\[
\boxed{
\mathcal V(p,x)
=
c_+(s)a^m
[1+o(1)],
}
\]

and

\[
\boxed{
\mathcal V(x,q)
=
c_-(s)b^m
[1+o(1)],
}
\]

where

\[
0<c_*\le c_\pm(s)\le c^*<\infty.
\]

The coefficients encode the plane-wave limits of the corresponding null generators.

The exponent \(m=d/2\) is universal.

## 4. Pair coordinates

For an ordered comparable pair

\[
x\prec y
\]

near the joint, write

\[
a_x=\alpha,
\qquad
b_y=\beta,
\]

\[
A=a_y-a_x\ge0,
\qquad
B=b_x-b_y\ge0,
\]

and

\[
\xi^A
=
s_y^A-s_x^A.
\]

## 5. Tangential causal cap

The squared separation has leading form

\[
g(\delta x,\delta x)
=
-2\Omega(s)^2AB
+
h_{AB}(s)\xi^A\xi^B
+
o(AB+|\xi|^2).
\]

Thus the timelike condition defines, to leading order, an ellipsoid

\[
h_{AB}\xi^A\xi^B
<
2\Omega^2 AB.
\]

Its \((d-2)\)-dimensional coordinate volume is

\[
\boxed{
\omega_{d-2}
\frac{
(2\Omega^2AB)^{(d-2)/2}
}{
\sqrt{\det h}
}
[1+o(1)],
}
\]

where

\[
\omega_k
=
\operatorname{Vol}(B^k_{\rm Eucl}(1)).
\]

Since

\[
\frac{d-2}{2}=m-1,
\]

the curved pair cap has exactly the scalar weight

\[
\boxed{
(AB)^{m-1}
}
\]

that appears in the flat theorem.

## 6. Local ordered-pair measure

At the edge,

\[
\sqrt{|\det g|}
=
\Omega^2\sqrt{\det h}.
\]

After integrating the relative tangential displacement \(\xi\), the normalized ordered-pair measure has leading form

\[
\boxed{
\mathcal A_d(s)
(AB)^{m-1}
\,d\alpha\,d\beta\,dA\,dB\,dA_E(s),
}
\]

where

\[
dA_E
=
\sqrt{\det h}\,d^{d-2}s
\]

is edge area and

\[
\boxed{
\mathcal A_d(s)
=
\frac{
\omega_{d-2}
2^{m-1}
\Omega(s)^{d+2}
}{
V_D^2
}.
}
\]

This expression corresponds to the displayed double-null normalization.

Under a different optical normalization, the individual factors \(\Omega,c_+,c_-\) change, but the final coefficient below is invariant.

## 7. Leading disagreement

The exact curved identity is

\[
\Delta(x,y)
=
\Phi(y)-\Phi(x)
-
2\mathcal V(x,y).
\]

Using the endpoint laws,

\[
\begin{aligned}
\Delta(x,y)
&=
c_+(s)
\left[
(\alpha+A)^m-\alpha^m
\right]\\
&\quad+
c_-(s)
\left[
(\beta+B)^m-\beta^m
\right]\\
&\quad+
o(
\alpha^m+\beta^m+A^m+B^m
)
-
2\mathcal V(x,y).
\end{aligned}
\]

In the joint blow-up,

\[
\alpha,\beta,A,B
=
O(\lambda),
\]

while

\[
\xi=O(\lambda).
\]

The nearby interval \(I(x,y)\) has volume

\[
O(\lambda^d)
=
O(\lambda^{2m}).
\]

The endpoint increments are

\[
O(\lambda^m).
\]

Therefore for

\[
m\ge2,
\]

the interval term is higher order.

Coefficient variation along the edge is also higher order because

\[
|s_y-s_x|=O(\lambda).
\]

Thus the leading disagreement is

\[
\boxed{
H_s
=
c_+(s)g_m(\alpha,A)
+
c_-(s)g_m(\beta,B),
}
\]

where

\[
g_m(u,v)
=
(u+v)^m-u^m.
\]

## 8. One-side integral

Define

\[
J_m(r)
=
\int_0^\infty
\int_0^\infty
A^{m-1}
\mathbf1_{
\{g_m(\alpha,A)\le r\}
}
\,dA\,d\alpha.
\]

For

\[
m\ge2,
\]

the integral converges after scaling and has the exact homogeneous form

\[
\boxed{
J_m(r)
=
L_m
r^{a_m},
}
\]

where

\[
a_m
=
1+\frac1m
=
1+\frac2d,
\]

and

\[
\boxed{
L_m
=
\frac1{m+1}
\int_0^\infty
\left[
(1+t)^m-t^m
\right]^{-(m+1)/m}
dt.
}
\]

With a coefficient \(c>0\),

\[
J_{m,c}(r)
=
L_m
c^{-a_m}
r^{a_m}.
\]

## 9. Two-side scalar integral

The Stieltjes density of the one-side volume is

\[
a_mL_m
c^{-a_m}
r^{a_m-1}dr.
\]

Therefore

\[
\begin{aligned}
&\int
(AB)^{m-1}
\mathbf1_{\{
c_+g_1+c_-g_2\le\varepsilon
\}}
\,d\alpha\,dA\,d\beta\,dB\\
&\qquad\sim
\boxed{
\mathcal S_d(s)
\varepsilon^{2a_m},
}
\end{aligned}
\]

where

\[
\boxed{
\mathcal S_d(s)
=
(a_mL_m)^2
c_+(s)^{-a_m}
c_-(s)^{-a_m}
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}.
}
\]

## 10. Curved joint coefficient

There are two time orientations.

Hence the local edge density of comparable small-disagreement pairs is

\[
2\mathcal A_d(s)\mathcal S_d(s).
\]

Integrating over the compact edge gives

\[
\boxed{
C_{d,g}^{\rm joint}
=
2
\int_E
\mathcal A_d(s)
\mathcal S_d(s)
\,dA_E(s).
}
\]

The combination is invariant under regular redefinitions of the optical coordinates.

## 11. Small-disagreement law

Since

\[
2a_m
=
2+\frac4d,
\]

the regular curved joint gives

\[
\boxed{
F_{d,g}^{\rm joint}(\varepsilon)
\sim
C_{d,g}^{\rm joint}
\varepsilon^{2+4/d}.
}
\]

For

\[
d\ge4,
\]

the ordinary bulk contribution is

\[
O(\varepsilon^d).
\]

Because

\[
2+\frac4d<d
\qquad
(d\ge4),
\]

the joint dominates.

Therefore

\[
\boxed{
F_{d,g}(\varepsilon)
\sim
C_{d,g}^{\rm joint}
\varepsilon^{2+4/d}
}
\]

provided the bulk volume-time gradient is nondegenerate and no additional singular boundary sector is present.

In a convex normal regular diamond, those conditions are supplied by the local theorem chain.

## 12. True-twin expectation

Let \(T_n\) count comparable true-twin pairs.

The exact identity is

\[
\mathbb E[T_n]
=
\binom n2
\int
(1-\delta)^{n-2}
\,dF_{d,g}(\delta).
\]

Set

\[
\beta_d
=
2+\frac4d.
\]

Laplace-Stieltjes transfer gives

\[
\boxed{
\mathbb E[T_n]
\sim
K_{d,g}^{\rm twin}
n^{-4/d},
}
\]

where

\[
\boxed{
K_{d,g}^{\rm twin}
=
\frac12
C_{d,g}^{\rm joint}
\Gamma\left(
3+\frac4d
\right).
}
\]

Thus curvature changes the coefficient but not the exponent.

## 13. Flat-space check

For the unit Minkowski diamond:

- the edge geometry is homogeneous;
- the Penrose limits are flat;
- \(c_\pm\) and \(\Omega\) reduce to their flat values.

The edge integral collapses to the previously derived constant

\[
C_d^{\rm edge}.
\]

In particular,

\[
d=4:
\qquad
K_{4,\eta}^{\rm twin}
=
9\pi.
\]

Thus the curved formula reduces to the exact flat theorem.

## 14. Geometric meaning

The exponent

\[
2+\frac4d
\]

comes from two independent universal structures:

### Thin-null endpoint volume

\[
V_{\rm thin}
\sim
a^{d/2}.
\]

### Codimension-two causal cap

\[
\operatorname{Vol}_{T_sE}(\text{cap})
\sim
(AB)^{(d-2)/2}.
\]

Their combination fixes the small-disagreement universality class.

Flatness is not responsible for the exponent.

The edge and its Penrose-limit data determine the coefficient.

## 15. Failure modes

The theorem does not cover:

- null caustics;
- conjugate points on the relevant generator families;
- cut loci entering the edge neighborhood;
- nonsmooth or nontransverse edge intersections;
- degeneration of the Penrose-scaled interval;
- extra causal-boundary components not represented by the regular edge.

Those regimes can alter the coefficient and may potentially alter the exponent.

## 16. Consequence for the broader program

The principal rare-event exponent required for orientation recovery is now available in a regular curved spacetime for every fixed

\[
d\ge4.
\]

The next step is to transport the remaining estimates:

\[
g_d(q)
\sim
q^{4/d},
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

and the tip co-degree law

\[
\bar g_d(r)
=
\Theta(r^d).
\]

Their power counting is already suggested by the same local normal forms.
