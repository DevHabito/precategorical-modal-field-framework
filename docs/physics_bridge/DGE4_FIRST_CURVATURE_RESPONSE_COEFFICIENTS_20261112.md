# Theorem candidate: explicit first curvature response of the recovery coefficient for d >= 4

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic derivation, internally checked, requires independent review  
**Scope:** sufficiently small regular centered Lorentzian diamonds, fixed integer \(d\ge4\)  
**Novelty status:** the small-diamond curvature invariants are classical; the response coefficients of the arrow-erasure recovery constant are project-specific

## 1. Result

Let

\[
D_L
=
I(
\exp_o(-LT),
\exp_o(LT)
)
\]

be a sufficiently small centered causal diamond around a strongly causal point \(o\), with \(T\) a unit future timelike vector.

For fixed

\[
d\ge4,
\]

let

\[
K_{d,g}(D_L)
\]

be the leading coefficient in

\[
1-p_{d,g,L}^{\rm UPO}(n)
\sim
K_{d,g}(D_L)n^{-4/d}.
\]

Then the first curvature correction is

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
L^2
\left[
\alpha_d R
+
\gamma_d R_{TT}
\right]_o
+
o(L^2),
}
\]

where

\[
R_{TT}
=
R_{\mu\nu}T^\mu T^\nu,
\]

and

\[
\boxed{
\alpha_d
=
-
\frac{
d(d+6)
}{
4(d-1)(d+1)(d+2)
},
}
\]

\[
\boxed{
\gamma_d
=
\frac{
d^2+2d-4
}{
4(d-1)(d+1)
}.
}
\]

Equivalently,

\[
\boxed{
K_{d,g}(D_L)
=
K_d^{\rm Mink}
+
L^2
\left[
A_dR+B_dR_{TT}
\right]_o
+
o(L^2),
}
\]

with

\[
A_d
=
K_d^{\rm Mink}\alpha_d,
\qquad
B_d
=
K_d^{\rm Mink}\gamma_d.
\]

## 2. Why two special curvature directions suffice

The structural theorem

LOCAL_CURVED_FIRST_CURVATURE_CORRECTION_STRUCTURE_20261112.md

shows that the \(O(L^2)\) correction to \(K\) is a universal linear combination of only

\[
R
\quad\text{and}\quad
R_{TT}.
\]

Therefore it is enough to evaluate \(K\) on any smooth two-parameter metric family whose values of

\[
(R,R_{TT})
\]

span a two-dimensional set at the center.

Spatially flat FLRW metrics provide such a family while keeping the causal structure exactly conformal to Minkowski.

This converts the curvature calculation into a weighted flat-joint calculation.

## 3. Weighted Minkowski joint

Consider the unit Minkowski diamond

\[
D_0
=
I((-1,\mathbf0),(1,\mathbf0))
\]

with a positive raw density depending only on Minkowski time,

\[
w=w(t).
\]

Normalize it to a probability measure:

\[
d\nu_w
=
\frac{
w(t)\,dV_\eta
}{
\int_{D_0}w\,dV_\eta
}.
\]

Set

\[
m=\frac d2,
\qquad
a_m=1+\frac2d.
\]

For \(d\ge4\), the leading small-disagreement tail is controlled by the codimension-two null joint.

The universal scalar integral is unchanged.

Only three density factors change:

1. the probability density of the two pair endpoints on the joint;
2. the weighted thin-null volume coefficient from the past tip;
3. the weighted thin-null volume coefficient toward the future tip.

## 4. Diamond average

Define the normalized unit-diamond average

\[
\boxed{
\langle w\rangle_D
=
\frac{
\int_{D_0}w(t)\,dV_\eta
}{
V_\eta(D_0)
}.
}
\]

The normalized sampling density relative to uniform Minkowski probability is

\[
\frac{
w(t)
}{
\langle w\rangle_D
}.
\]

At the joint,

\[
t=0.
\]

Therefore the pair endpoint-density factor changes by

\[
\boxed{
\left(
\frac{
w(0)
}{
\langle w\rangle_D
}
\right)^2.
}
\]

## 5. Thin-null weight kernel

Take the null generator from the past tip to a point on the joint.

For a nearly null endpoint, introduce the standard blow-up

\[
u=\delta U,
\qquad
y=\sqrt\delta\,Y,
\qquad
v=O(1).
\]

At fixed longitudinal null coordinate \(v\), integrating over \(U\) and the transverse ball gives the one-dimensional kernel

\[
[v(V-v)]^{m-1}.
\]

For the unit diamond,

\[
V=2.
\]

Set

\[
s=\frac v2\in[0,1].
\]

Then the generator time is

\[
t=s-1
\]

and the normalized kernel is the Beta distribution

\[
s^{m-1}(1-s)^{m-1}.
\]

Define

\[
\boxed{
\langle w\rangle_-
=
\frac{
1
}{
B(m,m)
}
\int_0^1
w(s-1)
s^{m-1}(1-s)^{m-1}\,ds.
}
\]

Similarly, for the future half,

\[
\boxed{
\langle w\rangle_+
=
\frac{
1
}{
B(m,m)
}
\int_0^1
w(1-s)
s^{m-1}(1-s)^{m-1}\,ds.
}
\]

These are the leading raw-density corrections to the two thin-null volume coefficients.

After probability normalization, the two coefficients are multiplied by

\[
\frac{
\langle w\rangle_\pm
}{
\langle w\rangle_D
}.
\]

## 6. Exact weighted-joint coefficient ratio

The regular joint scalar factor contains the thin-null coefficients to the power

\[
-a_m
\]

on each side.

Therefore the full leading coefficient satisfies the exact density identity

\[
\boxed{
\frac{
K_d[w]
}{
K_d[1]
}
=
w(0)^2
\,
\langle w\rangle_-^{-a_m}
\,
\langle w\rangle_+^{-a_m}
\,
\langle w\rangle_D^{\,2a_m-2}.
}
\]

This formula is invariant under

\[
w\mapsto c\,w,
\qquad
c>0,
\]

as required, since

\[
2-2a_m+(2a_m-2)=0.
\]

It is the central identity used below.

## 7. FLRW family

Take a spatially flat FLRW metric in conformal time:

\[
\boxed{
g
=
A(\eta)^2
\left(
-d\eta^2+d\mathbf x^2
\right).
}
\]

Normalize at the central event:

\[
A(0)=1.
\]

Write

\[
A(\eta)
=
1
+
h\eta
+
\frac12k\eta^2
+
O(\eta^3).
\]

Physical proper time on the central comoving geodesic satisfies

\[
d\tau=A(\eta)d\eta.
\]

The centered physical endpoints are defined by

\[
\tau=\pm L.
\]

## 8. Conformal endpoint centering

Integrating,

\[
\tau
=
\eta
+
\frac h2\eta^2
+
\frac k6\eta^3
+
O(\eta^4).
\]

Inverting,

\[
\eta(\tau)
=
\tau
-
\frac h2\tau^2
+
\left(
\frac{h^2}{2}
-
\frac k6
\right)\tau^3
+
O(\tau^4).
\]

Hence the conformal midpoint and half-width are

\[
\eta_c
=
-\frac h2L^2
+
O(L^4),
\]

\[
S
=
L
+
O(L^3).
\]

Map the conformal diamond to the unit Minkowski diamond by

\[
\eta
=
\eta_c
+
S t.
\]

To the required order,

\[
\boxed{
\eta
=
Lt
-
\frac h2L^2
+
O(L^3).
}
\]

## 9. Sprinkling density expansion

Physical volume is

\[
dV_g
=
A(\eta)^d
dV_\eta.
\]

The irrelevant constant coordinate scale \(S^d\) cancels after normalization.

Thus the raw unit-diamond density is

\[
w_L(t)
=
A(\eta_c+St)^d.
\]

Expanding,

\[
\boxed{
w_L(t)
=
1
+
pLt
+
L^2
\left(
q_0+q_2t^2
\right)
+
O(L^3),
}
\]

where

\[
p=dh,
\]

\[
q_0=-\frac d2h^2,
\]

and

\[
\boxed{
q_2
=
\frac d2
\left[
k+(d-1)h^2
\right].
}
\]

The odd \(O(L)\) term records the asymmetry between conformal and proper-time centering.

It cancels from the final scalar at first order.

## 10. Required time moments

For uniform volume in the unit \(d\)-dimensional Minkowski diamond,

\[
\boxed{
\langle t\rangle_D=0,
}
\]

and

\[
\boxed{
\langle t^2\rangle_D
=
\frac{
2
}{
(d+1)(d+2)
}.
}
\]

For the Beta\((m,m)\) thin-null kernel,

\[
\langle t\rangle_-
=
-\frac12,
\]

\[
\langle t\rangle_+
=
+\frac12,
\]

and

\[
\boxed{
\langle t^2\rangle_-
=
\langle t^2\rangle_+
=
\frac{
d+2
}{
4(d+1)
}.
}
\]

These identities are elementary Beta-function moments.

## 11. Expansion of the weighted coefficient

Take the logarithm of the exact weighted identity:

\[
\log\frac{K_d[w]}{K_d[1]}
=
2\log w(0)
-
a_m
\left[
\log\langle w\rangle_-
+
\log\langle w\rangle_+
\right]
+
(2a_m-2)
\log\langle w\rangle_D.
\]

Using the moments above, all terms proportional to the constant coefficient

\[
q_0
\]

cancel exactly.

This is required by invariance under constant conformal rescaling.

The remaining \(L^2\) coefficient is

\[
\boxed{
\mathcal C_d(h,k)
=
-
\frac{
d^3+6d^2+12d-8
}{
4(d+1)(d+2)
}
k
+
\frac{
d^2+12d-4
}{
2(d+1)(d+2)
}
h^2.
}
\]

Equivalently,

\[
\frac{K_{d,g}(D_L)}{K_d^{\rm Mink}}
=
1
+
L^2
\mathcal C_d(h,k)
+
o(L^2).
\]

## 12. FLRW curvature invariants

For a spatially flat \(d\)-dimensional FLRW metric with the conventions above,

\[
\boxed{
R_{TT}
=
-(d-1)
\left(
k-h^2
\right),
}
\]

and

\[
\boxed{
R
=
(d-1)
\left[
2k+(d-4)h^2
\right].
}
\]

The map

\[
(k,h^2)
\mapsto
(R,R_{TT})
\]

has determinant proportional to

\[
d-2,
\]

so it spans the two invariant curvature directions for every

\[
d\ge3.
\]

## 13. Solving for the universal coefficients

Solve

\[
\mathcal C_d(h,k)
=
\alpha_d R
+
\gamma_d R_{TT}.
\]

The result is

\[
\boxed{
\alpha_d
=
-
\frac{
d(d+6)
}{
4(d-1)(d+1)(d+2)
},
}
\]

\[
\boxed{
\gamma_d
=
\frac{
d^2+2d-4
}{
4(d-1)(d+1)
}.
}
\]

Because the structural invariant theorem already proves that no third independent linear curvature scalar can occur, these two FLRW directions determine the general regular-diamond response.

## 14. d = 4 specialization

For

\[
d=4,
\]

\[
\alpha_4=-\frac19,
\]

\[
\gamma_4=\frac13.
\]

Since

\[
K_4^{\rm Mink}=9\pi,
\]

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
\left[
1
+
L^2
\left(
-\frac19R
+
\frac13R_{TT}
\right)_o
+
o(L^2)
\right].
}
\]

Equivalently,

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
+
\pi L^2
\left[
-R+3R_{TT}
\right]_o
+
o(L^2).
}
\]

## 15. Constant-curvature check

In a constant-curvature spacetime,

\[
R_{\mu\nu}
=
\frac Rd
g_{\mu\nu}.
\]

For a unit timelike \(T\),

\[
R_{TT}
=
-\frac Rd.
\]

Therefore the relative response becomes

\[
\alpha_dR
+
\gamma_dR_{TT}
=
\left(
\alpha_d
-
\frac{\gamma_d}{d}
\right)R.
\]

For \(d=4\),

\[
\boxed{
\frac{
K_{4,g}
}{
9\pi
}
=
1
-
\frac{
7
}{
36
}
RL^2
+
o(L^2).
}
\]

For de Sitter with

\[
R=12H^2,
\]

this is

\[
\boxed{
\frac{
K_{4,\rm dS}
}{
9\pi
}
=
1
-
\frac73
H^2L^2
+
o(L^2).
}
\]

This agrees with the direct conformal-weight expansion of

\[
w(t)
=
[
\cosh(HL)-t\sinh(HL)
]^{-4}.
\]

## 16. Vacuum consequence

At a Ricci-flat point,

\[
R=0,
\qquad
R_{TT}=0.
\]

Hence, for every fixed

\[
d\ge4,
\]

\[
\boxed{
K_{d,g}(D_L)
=
K_d^{\rm Mink}
+
o(L^2).
}
\]

The first Weyl-dependent response must occur at a higher order.

This is consistent with established small-causal-diamond geometry, where leading vacuum corrections involve quadratic Weyl invariants rather than a linear Weyl scalar.

## 17. Relation to established small-diamond literature

Gibbons and Solodukhin, *The Geometry of Small Causal Diamonds*, Phys. Lett. B 649 (2007) 317--324, DOI 10.1016/j.physletb.2007.03.068, showed that the leading small-Alexandrov-diamond volume correction is a universal linear combination of

\[
R
\quad\text{and}\quad
R_{TT}.
\]

Jinzhao Wang, *Geometry of small causal diamonds*, Phys. Rev. D 100 (2019) 064020, DOI 10.1103/PhysRevD.100.064020, gives arbitrary-dimensional leading non-vacuum edge-area and volume corrections in the same Ricci invariant sector and studies the higher-order vacuum/Weyl terms.

Those works do not calculate the arrow-erasure coefficient \(K\).

They provide an independent consistency check on the invariant structure used here.

## 18. Symbolic regression

The repository script

\[
\texttt{tools/derive\_dge4\_first\_curvature\_response.py}
\]

reproduces the Beta moments, FLRW curvature conversion, and the closed forms

\[
\alpha_d,
\qquad
\gamma_d.
\]

Equivalent symbolic algebra was checked during the derivation.

## 19. Current confidence boundary

The algebraic weighted-joint calculation is exact within the conformally flat FLRW family.

The extension of the resulting two coefficients to every regular small diamond relies on the previously derived theorem that the first variation of \(K\) is:

1. differentiable at the flat diamond;
2. linear in the local curvature tensor;
3. invariant under the spatial rotation group fixing \(T\);
4. therefore exhausted by \(R\) and \(R_{TT}\).

That structural step remains an external-review priority.

Accordingly, the formulas in this note should currently be described as

\[
\boxed{
\text{internally derived universal coefficient candidates}.
}
\]

They are substantially stronger than a numerical fit, but they are not yet externally validated.
