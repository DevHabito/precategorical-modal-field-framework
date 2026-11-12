# Candidate theorem: first curvature response in d = 3 as exact bulk integrals

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic reduction to convergent integrals + numerical quadrature; no closed form claimed  
**Scope:** sufficiently small regular centered \(2+1\)-dimensional Lorentzian diamonds  
**Novelty status:** the curvature-invariant structure is general; the bulk response integrals are project-specific

## 1. Statement

Let

\[
D_L
=
I(
\exp_o(-LT),
\exp_o(LT)
)
\]

be a sufficiently small centered \(2+1\)-dimensional causal diamond.

The local curved theorem gives

\[
1-p_{3,g,L}^{\rm UPO}(n)
\sim
\frac{
K_{3,g}(D_L)
}{
n
}.
\]

The first curvature response has the invariant form

\[
\boxed{
\frac{
K_{3,g}(D_L)
}{
K_3^{\rm Mink}
}
=
1
+
L^2
\left[
\alpha_3R
+
\gamma_3R_{TT}
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

The coefficients are reduced below to explicit absolutely convergent bulk integrals.

A closed evaluation has **not** been obtained.

Numerical quadrature gives

\[
\boxed{
\alpha_3
\approx
-0.11262660485,
}
\]

\[
\boxed{
\gamma_3
\approx
0.22199955728.
}
\]

These decimal values are diagnostics of the exact integral formulas, not fitted constants.

## 2. Why d = 3 must be treated separately

For \(d\ge4\), the leading true-twin coefficient comes from the codimension-two null joint.

For \(d=3\), the joint core is subleading:

\[
F_{3}^{\rm joint\,core}(\varepsilon)
=
O(\varepsilon^{10/3}),
\]

while the leading pair tail is bulk controlled:

\[
F_3(\varepsilon)
\sim
C_3\varepsilon^3.
\]

Therefore the \(d\ge4\) weighted-joint curvature formula cannot be analytically continued to \(d=3\).

The first curvature response must instead be computed from the bulk volume-time functional.

## 3. Conformal calibration family

Use a spatially-flat \(2+1\) FLRW metric in conformal time:

\[
g
=
A(\eta)^2
\left(
-d\eta^2+d\mathbf x^2
\right),
\]

with

\[
A(0)=1,
\]

\[
A(\eta)
=
1+h\eta+\frac12k\eta^2+O(\eta^3).
\]

As in the \(d\ge4\) calculation, map the centered proper-time diamond to the unit Minkowski diamond.

To second order,

\[
\eta
=
Lt-\frac h2L^2+O(L^3).
\]

Hence

\[
A
=
1+hLt
+
L^2
\left(
-\frac12h^2+\frac12kt^2
\right)
+
O(L^3).
\]

The physical volume weight is

\[
A^3
=
1
+
3hLt
+
L^2
\left[
-\frac32h^2
+
\frac32(k+2h^2)t^2
\right]
+
O(L^3).
\]

## 4. Raw finite-diamond volume difference

For a unit-diamond point \(x\), define the raw weighted volume difference

\[
\Psi(x)
=
V_w(p,x)
-
V_w(x,q).
\]

The normalized finite-diamond volume-time function is

\[
\Phi
=
\frac{\Psi}{Z},
\]

where

\[
Z
=
\int_D A^3\,dV_\eta.
\]

For the conformal physical metric

\[
g_{\rm phys}
=
S^2A^2\eta,
\]

the bulk coefficient can be written without normalized derivatives as

\[
\boxed{
K_3
=
2\pi
Z
\int_D
A^6
\left[
-\eta^{-1}(d\Psi,d\Psi)
\right]^{-3/2}
dV_\eta.
}
\]

All powers of the conformal-coordinate scale \(S\) cancel.

This identity is exact.

## 5. Minkowski interval moments

Let a \(2+1\)-dimensional Minkowski Alexandrov interval have proper duration \(\tau\), endpoint coordinate-time difference \(\Delta t\), and midpoint time \(t_m\).

Its volume is

\[
V
=
\frac{\pi}{12}\tau^3.
\]

Lorentz symmetry gives the first time moment

\[
\boxed{
\int_I t\,dV
=
V t_m.
}
\]

The second time moment is

\[
\boxed{
\int_I t^2\,dV
=
V
\left[
t_m^2
-
\frac{3}{80}\tau^2
+
\frac{1}{16}(\Delta t)^2
\right].
}
\]

The constants follow from direct integration in the interval rest frame and Lorentz transformation of the second-moment tensor.

These two moment formulas are enough because the conformal weight is quadratic in \(t\) at order \(L^2\).

## 6. Endpoint-distance coordinates

For the unit parent diamond, set

\[
u=\tau(p,x),
\qquad
v=\tau(x,q).
\]

Then

\[
u>0,
\qquad
v>0,
\qquad
u+v<2,
\]

and

\[
t
=
\frac{u^2-v^2}{4}.
\]

The radial angular-integrated volume measure is

\[
dV_\eta
=
\pi uv\,du\,dv.
\]

The flat raw volume difference, with the common factor \(\pi/12\) suppressed, is

\[
\psi_0
=
u^3-v^3.
\]

## 7. Perturbed raw volume difference

Write

\[
\Psi
=
\frac{\pi}{12}
\left[
\psi_0
+
L\psi_1
+
L^2\psi_2
+
O(L^3)
\right].
\]

The first perturbation is

\[
\boxed{
\psi_1
=
3h
\left[
\frac12u^3(t-1)
-
\frac12v^3(t+1)
\right].
}
\]

For the second perturbation, define

\[
M_{2,p}
=
u^3
\left[
\frac{(t-1)^2}{4}
-
\frac{3u^2}{80}
+
\frac{(1+t)^2}{16}
\right],
\]

\[
M_{2,f}
=
v^3
\left[
\frac{(t+1)^2}{4}
-
\frac{3v^2}{80}
+
\frac{(1-t)^2}{16}
\right].
\]

Then

\[
\boxed{
\psi_2
=
-\frac32h^2\psi_0
+
\frac32(k+2h^2)
\left(
M_{2,p}-M_{2,f}
\right).
}
\]

This is an exact second-order consequence of the Minkowski moment formulas.

## 8. Lorentz norm in u,v coordinates

For any scalar functions \(f,g\), define the positive timelike bilinear form

\[
\mathcal B(f,g)
=
-\eta^{-1}(df,dg).
\]

In \((u,v)\) coordinates,

\[
\boxed{
\mathcal B(f,g)
=
f_ug_u
+
f_vg_v
-
c(u,v)
\left(
f_ug_v+f_vg_u
\right),
}
\]

where

\[
\boxed{
c(u,v)
=
\frac{
4-u^2-v^2
}{
2uv
}.
}
\]

Set

\[
S_0=\mathcal B(\psi_0,\psi_0),
\]

\[
S_1=2\mathcal B(\psi_0,\psi_1),
\]

\[
S_2=
2\mathcal B(\psi_0,\psi_2)
+
\mathcal B(\psi_1,\psi_1).
\]

Then

\[
-\eta^{-1}(d\Psi,d\Psi)
=
\left(\frac{\pi}{12}\right)^2
\left[
S_0+LS_1+L^2S_2+O(L^3)
\right].
\]

The flat term is

\[
\boxed{
S_0
=
9
\left[
u^4+v^4
+
(4-u^2-v^2)uv
\right].
}
\]

## 9. Expansion of the bulk integrand

The conformal prefactor satisfies

\[
A^6
=
1
+
L a_1
+
L^2 a_2
+
O(L^3),
\]

with

\[
a_1=6ht,
\]

\[
a_2
=
-3h^2
+
(3k+15h^2)t^2.
\]

Define

\[
r_1=\frac{S_1}{S_0},
\qquad
r_2=\frac{S_2}{S_0}.
\]

Then

\[
A^6
S^{-3/2}
=
S_0^{-3/2}
\left[
1
+
L(\cdots)
+
L^2B_2(u,v)
+
O(L^3)
\right],
\]

where

\[
\boxed{
B_2
=
a_2
-
\frac32r_2
+
\frac{15}{8}r_1^2
-
\frac32a_1r_1.
}
\]

The \(O(L)\) integral vanishes by the centered time-reflection symmetry.

## 10. Parent-volume normalization

The total physical volume factor is

\[
Z
=
V_0
\left[
1
+
L^2
\left(
\frac{3}{20}k
-
\frac65h^2
\right)
+
O(L^3)
\right],
\]

where

\[
V_0=\frac{2\pi}{3}.
\]

Therefore the relative \(L^2\) response is

\[
C_k\,k+C_h\,h^2,
\]

with

\[
\boxed{
C_k
=
\frac{3}{20}
+
\frac{
\int_D
S_0^{-3/2}
[B_2]_k
\,dV_\eta
}{
\int_D
S_0^{-3/2}
\,dV_\eta
},
}
\]

and

\[
\boxed{
C_h
=
-\frac65
+
\frac{
\int_D
S_0^{-3/2}
[B_2]_{h^2}
\,dV_\eta
}{
\int_D
S_0^{-3/2}
\,dV_\eta
}.
}
\]

Here \([B_2]_k\) and \([B_2]_{h^2}\) denote the exact coefficients of \(k\) and \(h^2\).

These are explicit rational-algebraic functions of \(u,v\).

## 11. Compact integration variables

Set

\[
s=u+v,
\qquad
w=\frac{u-v}{u+v}.
\]

Then

\[
0<s<2,
\qquad
-1<w<1.
\]

The flat normalized bulk weight becomes, up to a common constant,

\[
\boxed{
W_0(s,w)
=
\frac{
1-w^2
}{
\left[
4(1-w^2)
+
s^2w^2(w^2+3)
\right]^{3/2}
}.
}
\]

Its integral is exactly

\[
\boxed{
\int_{-1}^{1}
\int_0^2
W_0(s,w)\,ds\,dw
=
\frac{\pi}{8}.
}
\]

Thus the curvature coefficients are finite explicit integrals over a compact rectangle.

## 12. Conversion to R and R_TT

For the \(2+1\) spatially-flat FLRW calibration family,

\[
\boxed{
R
=
4k-2h^2,
}
\]

\[
\boxed{
R_{TT}
=
-2k+2h^2.
}
\]

If

\[
C_k k+C_hh^2
=
\alpha_3R+\gamma_3R_{TT},
\]

then

\[
\boxed{
\alpha_3
=
\frac{
C_k+C_h
}{2},
}
\]

\[
\boxed{
\gamma_3
=
\alpha_3+\frac{C_h}{2}.
}
\]

## 13. Numerical quadrature

Tensor-product Gauss--Legendre quadrature was applied directly to the exact compact integrals.

Representative convergence is:

| order | \(\alpha_3\) | \(\gamma_3\) |
|---:|---:|---:|
| 100 | -0.11262660442 | 0.22199955624 |
| 200 | -0.11262660483 | 0.22199955720 |
| 400 | -0.11262660485 | 0.22199955727 |
| 800 | -0.11262660485 | 0.22199955728 |

The flat denominator simultaneously reproduces

\[
\frac{\pi}{8}
\]

to double-precision quadrature accuracy.

Therefore the present numerical estimates are

\[
\boxed{
\alpha_3
\approx
-0.11262660485,
}
\]

\[
\boxed{
\gamma_3
\approx
0.22199955728.
}
\]

## 14. No closed-form claim

Attempts to force recognition of these decimals as simple combinations of familiar constants were rejected.

No closed form has been derived.

The rigorous content at this stage is:

1. the reduction to exact convergent integrals;
2. the invariant relation to \(R,R_{TT}\);
3. stable numerical evaluation of those integrals.

The decimal values should not be treated as exact constants.

## 15. Comparison with d >= 4

The \(d\ge4\) joint formula has rational dimension-dependent curvature-response coefficients:

\[
\alpha_d
=
-
\frac{
d(d+6)
}{
4(d-1)(d+1)(d+2)
},
\]

\[
\gamma_d
=
\frac{
d^2+2d-4
}{
4(d-1)(d+1)
}.
\]

Substituting \(d=3\) into those formulas would give

\[
-\frac{27}{160},
\qquad
\frac{11}{32},
\]

which are **not** the \(d=3\) bulk coefficients above.

This is another quantitative manifestation of the bulk-to-joint transition at \(d=4\).

## 16. Reproducibility

The repository script

\[
\texttt{tools/derive\_d3\_first\_curvature\_response.py}
\]

constructs the perturbation algebra symbolically and evaluates the final exact integrals by Gauss--Legendre quadrature.

## 17. Current status

The \(d=3\) first curvature response is substantially less closed than the \(d\ge4\) result.

The appropriate status is:

\[
\boxed{
\text{exact integral representation + stable numerical evaluation; closed form open}.
}
\]

An independent derivation or analytic evaluation of the two compact integrals is the next mathematical target.
