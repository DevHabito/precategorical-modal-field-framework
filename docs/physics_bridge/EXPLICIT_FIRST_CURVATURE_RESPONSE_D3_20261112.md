# Theorem: first curvature-response constants in 2+1 dimensions

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic integral representation + stabilized numerical evaluation  
**Physical status:** completes the \(O(L^2)\) curvature response of the local orientation-recovery coefficient in the bulk-dominated \(2+1\) case  
**Novelty status:** targeted review did not locate an equivalent recovery-rate curvature response; absolute priority is not certified

## 1. Statement

For a centered sufficiently small causal diamond

\[
D_L
=
I(
\exp_o(-LT),
\exp_o(LT)
)
\]

in a smooth strongly causal \(2+1\)-dimensional Lorentzian spacetime,

\[
\boxed{
K_{3,g}(D_L)
=
K_3^{\rm Mink}
+
L^2
\left[
A_3 R
+
B_3 R_{\mu\nu}T^\mu T^\nu
\right]_o
+
o(L^2),
}
\]

where

\[
K_3^{\rm Mink}
=
\frac{32\pi}{3}.
\]

The universal constants \(A_3,B_3\) admit exact convergent integral representations.

Their numerical values are

\[
\boxed{
\frac{A_3}{K_3^{\rm Mink}}
=
-0.112626604856\ldots
}
\]

and

\[
\boxed{
\frac{B_3}{K_3^{\rm Mink}}
=
0.221999557266\ldots
}
\]

so

\[
\boxed{
A_3
=
-3.774153754\ldots
}
\]

and

\[
\boxed{
B_3
=
7.439276568\ldots.
}
\]

No elementary closed form is claimed.

## 2. Why d = 3 is different

For \(d\ge4\), the leading recovery defect is localized at the codimension-two null edge.

Its first curvature response can therefore be obtained by perturbing a compact edge integral.

For \(d=3\), the leading small-disagreement law is bulk dominated:

\[
F_3(\varepsilon)
\sim
C_3\varepsilon^3.
\]

The curved coefficient is

\[
\boxed{
K_{3,g}
=
\frac{
2\pi
}{
V_D
}
\int_D
\kappa(x)^{-3}\,d\mu(x),
}
\]

where

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi,d\Phi)
}.
\]

Thus the curvature response is a genuine bulk functional.

## 3. Conformal test strategy

The structural theorem has already shown that the first correction can only be

\[
A_3R+B_3R_{TT}.
\]

Two independent conformal perturbations therefore determine the constants.

Take

\[
g_\epsilon^{(t)}
=
e^{2\epsilon t^2}\eta
\]

and

\[
g_\epsilon^{(r)}
=
e^{2\epsilon r^2}\eta.
\]

The conformal factor leaves the causal kernel exactly unchanged.

The entire first variation can therefore be computed as a weighted-Minkowski sprinkling problem.

## 4. Weighted probability measure

Let \(\mu_0\) be normalized flat volume on the unit \(2+1\) diamond.

For

\[
g_\epsilon
=
e^{2\epsilon f}\eta,
\]

the physical volume density relative to \(\mu_0\) is

\[
w_\epsilon(x)
=
\frac{
e^{3\epsilon f(x)}
}{
\int_D e^{3\epsilon f}\,d\mu_0
}.
\]

Hence

\[
\boxed{
w_\epsilon(x)
=
1
+
3\epsilon
\left(
f(x)-\langle f\rangle
\right)
+
O(\epsilon^2).
}
\]

Write

\[
s_f(x)
=
3
\left(
f(x)-\langle f\rangle
\right).
\]

## 5. Weighted volume-time function

Define

\[
\Phi_\epsilon(x)
=
\int_{I(p,x)}
w_\epsilon(z)\,d\mu_0(z)
-
\int_{I(x,q)}
w_\epsilon(z)\,d\mu_0(z).
\]

Then

\[
\Phi_\epsilon
=
\Phi_0
+
\epsilon\psi_f
+
O(\epsilon^2),
\]

where

\[
\boxed{
\psi_f(x)
=
3
\left[
\int_{I(p,x)}
(f-\langle f\rangle)\,d\mu_0
-
\int_{I(x,q)}
(f-\langle f\rangle)\,d\mu_0
\right].
}
\]

Let

\[
C_0=d\Phi_0,
\qquad
C_f=d\psi_f.
\]

Define

\[
\kappa_0^2
=
\eta^{-1}(C_0,C_0).
\]

Then

\[
\frac{
d
}{
d\epsilon
}
\log\kappa_\epsilon
\Big|_{\epsilon=0}
=
\frac{
\eta^{-1}(C_0,C_f)
}{
\kappa_0^2
}.
\]

## 6. First variation of the bulk coefficient

For the unit \(2+1\) flat diamond,

\[
\frac{
2\pi
}{
3V_3
}
=
1.
\]

The weighted small-disagreement coefficient is therefore

\[
\boxed{
C_3(\epsilon)
=
\int_D
w_\epsilon(x)^2
\kappa_\epsilon(x)^{-3}
\,d\mu_0(x).
}
\]

Differentiating gives

\[
\boxed{
\delta C_f
=
\int_D
\kappa_0^{-3}
\left[
6(f-\langle f\rangle)
-
3
\frac{
\eta^{-1}(C_0,C_f)
}{
\kappa_0^2
}
\right]
d\mu_0.
}
\]

Since

\[
K_3=3C_3,
\]

the logarithmic response of \(K_3\) is the same as that of \(C_3\).

## 7. Endpoint-distance coordinates

Use

\[
u=\tau(p,x),
\qquad
v=\tau(x,q),
\]

and then

\[
s=u+v,
\qquad
w=\frac{u-v}{u+v}.
\]

The domain is

\[
0<s<2,
\qquad
-1<w<1.
\]

Define

\[
\boxed{
D(s,w)
=
s^2w^4
+
3s^2w^2
-
4w^2
+
4.
}
\]

The unperturbed bulk coefficient measure becomes

\[
\boxed{
d\nu_0
=
\frac{256}{9}
\frac{
1-w^2
}{
D(s,w)^{3/2}
}
\,ds\,dw.
}
\]

Its total mass is

\[
\int d\nu_0
=
\frac{32\pi}{9}.
\]

## 8. Exact t^2 response integral

For

\[
f=t^2,
\qquad
\langle t^2\rangle
=
\frac1{10},
\]

the first-variation algebra reduces exactly to

\[
\boxed{
\delta C_t
=
\int_{-1}^{1}
\int_0^2
\frac{
(1-w^2)N_t(s,w)
}{
15D(s,w)^{5/2}
}
\,ds\,dw,
}
\]

where

\[
\begin{aligned}
N_t(s,w)
={}&
35s^6w^6
+
105s^6w^4
+
60s^4w^6\\
&+
1020s^4w^4
+
1000s^4w^2\\
&-
1312s^2w^4
-
1776s^2w^2
+
720s^2\\
&+
4288w^2
-
4288.
\end{aligned}
\]

The integral is absolutely convergent.

Numerically,

\[
\boxed{
\delta C_t
=
-19.9834454334\ldots
}
\]

and therefore

\[
\boxed{
c_t
:=
\frac{
\delta K_t
}{
K_3^{\rm Mink}
}
=
\frac{
\delta C_t
}{
32\pi/9
}
=
-1.78901106791\ldots.
}
\]

## 9. Exact r^2 response integral

For

\[
f=r^2,
\qquad
\langle r^2\rangle
=
\frac3{10},
\]

the exact response is

\[
\boxed{
\delta C_r
=
\int_{-1}^{1}
\int_0^2
\frac{
(1-w^2)N_r(s,w)
}{
15D(s,w)^{5/2}
}
\,ds\,dw,
}
\]

where

\[
\begin{aligned}
N_r(s,w)
={}&
35s^6w^6
+
105s^6w^4
-
260s^4w^6\\
&-
1860s^4w^4
-
920s^4w^2\\
&+
2784s^2w^4
+
2832s^2w^2
-
1840s^2\\
&-
6976w^2
+
6976.
\end{aligned}
\]

Again the integral is absolutely convergent.

Numerically,

\[
\boxed{
\delta C_r
=
30.0478554434\ldots
}
\]

and

\[
\boxed{
c_r
:=
\frac{
\delta K_r
}{
K_3^{\rm Mink}
}
=
2.69002390675\ldots.
}
\]

## 10. Curvature of the test metrics

Using the same curvature convention as the \(d\ge4\) theorem:

### t^2 test

\[
\omega=\epsilon t^2
\]

gives, at the center,

\[
\boxed{
\frac R\epsilon=8,
\qquad
\frac{R_{TT}}\epsilon=-4.
}
\]

### r^2 test

\[
\omega=\epsilon r^2
\]

gives

\[
\boxed{
\frac R\epsilon=-16,
\qquad
\frac{R_{TT}}\epsilon=4.
}
\]

## 11. Solving for the universal constants

Let

\[
a_3
=
\frac{A_3}{K_3^{\rm Mink}},
\qquad
b_3
=
\frac{B_3}{K_3^{\rm Mink}}.
\]

The two conformal responses satisfy

\[
8a_3-4b_3=c_t,
\]

and

\[
-16a_3+4b_3=c_r.
\]

Thus

\[
\boxed{
a_3
=
-\frac{
c_t+c_r
}{
8
},
}
\]

and

\[
\boxed{
b_3
=
2a_3-\frac{c_t}{4}.
}
\]

Substituting the exact integral definitions of \(c_t,c_r\) gives exact integral representations for \(A_3,B_3\).

Numerically,

\[
\boxed{
a_3
=
-0.112626604856\ldots
}
\]

and

\[
\boxed{
b_3
=
0.221999557266\ldots.
}
\]

Therefore

\[
\boxed{
A_3
=
-3.774153754\ldots,
}
\]

\[
\boxed{
B_3
=
7.439276568\ldots.
}
\]

## 12. Local 2+1 curvature-corrected recovery law

The leading true-twin/recovery coefficient is

\[
\boxed{
K_{3,g}(D_L)
=
\frac{32\pi}{3}
+
L^2
\left[
A_3R
+
B_3R_{TT}
\right]_o
+
o(L^2).
}
\]

Hence

\[
\boxed{
1-p_{3,g,L}^{\rm UPO}(n)
\sim
\frac{
\frac{32\pi}{3}
+
L^2(A_3R+B_3R_{TT})_o
+
o(L^2)
}{
n
}.
}
\]

## 13. Centered physical-size normalization

For the \(r^2\) conformal test, the conformal factor equals one on the central timelike geodesic, so the unit coordinate half-height is already the physical unit half-size to first order.

For the \(t^2\) test,

\[
L
=
\int_0^T
e^{\epsilon t^2}\,dt
=
T+\frac{\epsilon}{3}T^3+O(\epsilon^2).
\]

At fixed physical \(L=1\),

\[
T
=
1-\frac{\epsilon}{3}
+
O(\epsilon^2).
\]

Rescaling the coordinate diamond by \(T\) changes the metric by an irrelevant constant conformal factor and replaces

\[
\epsilon
\mapsto
\epsilon T^2
=
\epsilon+O(\epsilon^2).
\]

Therefore the first-order response integrals above are already the fixed-physical-size responses.

## 14. Regression

The repository script

tools/verify_d3_first_curvature_response.py

uses tensor-product Gauss-Legendre quadrature.

For orders

\[
100,\ 200,\ 400,\ 800,
\]

the estimates stabilize toward the values quoted above.

The numerical quadrature is not the proof of the response formula.

The proof is the exact integral representation.

No elementary closed form for those integrals is claimed.

## 15. Comparison with d >= 4

For \(d\ge4\), the curvature-response constants reduce to rational functions of \(d\) times the flat coefficient.

For \(d=3\), the bulk geometry retains information from the full finite diamond and the corresponding universal constants are represented by nontrivial bulk integrals.

This difference mirrors the leading rare-event transition:

- \(d=3\): bulk dominated;
- \(d\ge4\): null-edge dominated.

## 16. Vacuum remark

In \(2+1\), the Riemann tensor is determined entirely by the Ricci tensor.

Thus

\[
R=0,
\qquad
R_{\mu\nu}=0
\]

already implies local flatness at the curvature-tensor level.

There is no independent Weyl sector to probe.

The \(d=3\) curvature response therefore has no analogue of the \(3+1\) "pure Weyl but Ricci-flat" case.

## 17. Current status

The first \(L^2\) curvature correction is now determined in every fixed dimension

\[
d\ge3.
\]

For \(d=3\), the constants are integral-exact and numerically evaluated.

For \(d\ge4\), they have closed formulas.

The next unresolved perturbative problem is the first nonzero correction in Ricci-flat \(3+1\) spacetime, where the entire \(L^2\) term vanishes.
