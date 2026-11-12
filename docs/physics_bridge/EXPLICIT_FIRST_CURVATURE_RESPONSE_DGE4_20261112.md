# Theorem: explicit first curvature-response constants for d >= 4

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic perturbative theorem + independent regression  
**Physical status:** computes the complete \(O(L^2)\) curvature response of the local orientation-recovery coefficient for every fixed \(d\ge4\)  
**Novelty status:** targeted review did not locate an equivalent recovery-rate curvature response; absolute priority is not certified

## 1. Statement

For the centered small diamond

\[
D_L
=
I(
\exp_o(-LT),
\exp_o(LT)
)
\]

in a smooth strongly causal Lorentzian spacetime of fixed dimension

\[
d\ge4,
\]

the local orientation-recovery coefficient satisfies

\[
\boxed{
K_{d,g}(D_L)
=
K_d^{\rm Mink}
+
L^2
\left[
A_dR
+
B_dR_{\mu\nu}T^\mu T^\nu
\right]_o
+
o(L^2),
}
\]

with the explicit universal constants

\[
\boxed{
A_d
=
-
K_d^{\rm Mink}
\frac{
d(d+6)
}{
4(d-1)(d+1)(d+2)
},
}
\]

and

\[
\boxed{
B_d
=
K_d^{\rm Mink}
\frac{
d^2+2d-4
}{
4(d-1)(d+1)
}.
}
\]

The curvature convention is

\[
R^\rho{}_{\sigma\mu\nu}
=
\partial_\mu
\Gamma^\rho_{\nu\sigma}
-
\partial_\nu
\Gamma^\rho_{\mu\sigma}
+
\cdots.
\]

## 2. Strategy

The structural curvature theorem has already shown that the first correction can only involve

\[
R
\]

and

\[
R_{TT}
=
R_{\mu\nu}T^\mu T^\nu.
\]

Therefore two independent perturbation families determine \(A_d,B_d\).

Choose conformal perturbations of flat space:

\[
g_\varepsilon^{(t)}
=
e^{2\varepsilon t^2}\eta,
\]

and

\[
g_\varepsilon^{(r)}
=
e^{2\varepsilon r^2}\eta.
\]

At the center:

\[
f(0)=0,
\qquad
df(0)=0,
\]

so the central coordinates are locally inertial.

The causal relation is exactly unchanged by the conformal factor.

Thus the response of the orientation-recovery constant can be computed from the weighted sprinkling measure while retaining the flat causal kernel.

## 3. Centered physical diamond

For the \(r^2\) perturbation, the conformal factor equals one on the central timelike geodesic, so the coordinate half-height equals the physical half proper time to first order.

For the \(t^2\) perturbation,

\[
L
=
\int_0^T
e^{\varepsilon t^2}\,dt
=
T
+
\frac{\varepsilon}{3}T^3
+
O(\varepsilon^2).
\]

At fixed physical half-size \(L=1\),

\[
T
=
1-\frac{\varepsilon}{3}
+
O(\varepsilon^2).
\]

Dilation by \(T\) maps the coordinate diamond back to the unit flat diamond.

The metric acquires an overall constant factor \(T^2\), which does not affect the normalized causal-sampling problem, while

\[
\varepsilon T^2
=
\varepsilon
+
O(\varepsilon^2).
\]

Therefore the first-order response can be computed on the unit coordinate diamond for both test families.

## 4. Conformal sprinkling weight

Let

\[
g_\varepsilon
=
e^{2\varepsilon f}\eta.
\]

The physical volume form is

\[
dV_\varepsilon
=
e^{d\varepsilon f}
dV_0.
\]

Thus

\[
dV_\varepsilon
=
\left[
1+d\varepsilon f+O(\varepsilon^2)
\right]
dV_0.
\]

After normalization by the parent diamond volume,

\[
d\mu_\varepsilon
=
\left[
1+
d\varepsilon
(
f-\langle f\rangle_D
)
+
O(\varepsilon^2)
\right]
d\mu_0.
\]

## 5. Weighted thin-null coefficient

Let \(m=d/2\).

Along a flat null generator from the past tip to an edge point, use null coordinate

\[
v\in[0,2].
\]

For a thin interval of optical depth \(a\), the transverse cross-section gives the one-dimensional kernel

\[
\boxed{
w_m(v)
\propto
[v(2-v)]^{m-1}.
}
\]

Therefore the weighted null-generator average is

\[
\boxed{
\overline f_\gamma
=
\frac{
\int_0^2
[v(2-v)]^{m-1}
f(\gamma(v))
\,dv
}{
\int_0^2
[v(2-v)]^{m-1}
\,dv
}.
}
\]

The normalized thin-null coefficient obeys

\[
\boxed{
\delta\ln c_\pm
=
d\varepsilon
\left(
\overline f_\pm
-
\langle f\rangle_D
\right).
}
\]

## 6. Response of the geometric edge factor

The curved edge formula contains

\[
\mathcal A_d
dA_E
\propto
\frac{
\Omega_{\rm null}^{d+2}
dA_E
}{
V_D^2
}.
\]

Under

\[
g\mapsto e^{2\varepsilon f}g,
\]

the null cross coefficient scales as

\[
\Omega_{\rm null}
\mapsto
e^{\varepsilon f_E}
\Omega_{\rm null},
\]

while the \((d-2)\)-dimensional edge area scales as

\[
dA_E
\mapsto
e^{(d-2)\varepsilon f_E}
dA_E.
\]

The parent volume satisfies

\[
\delta\ln V_D
=
d\varepsilon
\langle f\rangle_D.
\]

Therefore

\[
\boxed{
\delta\ln(
\mathcal A_d dA_E
)
=
2d\varepsilon
\left(
f_E-\langle f\rangle_D
\right).
}
\]

## 7. Response of the scalar disagreement factor

The scalar factor contains

\[
c_+^{-a_m}
c_-^{-a_m},
\]

where

\[
a_m
=
1+\frac1m
=
1+\frac2d.
\]

Since

\[
d\,a_m
=
d+2,
\]

we obtain

\[
\boxed{
\delta\ln\mathcal S_d
=
-(d+2)\varepsilon
\left(
\overline f_+
+
\overline f_-
-
2\langle f\rangle_D
\right).
}
\]

## 8. General conformal response formula

Adding the edge and scalar responses,

\[
\boxed{
\frac{
\delta K_d
}{
K_d^{\rm Mink}
}
=
\varepsilon
\left\langle
2d\,f_E
-
(d+2)
(
\overline f_+
+
\overline f_-
)
+
4\langle f\rangle_D
\right\rangle_E.
}
\]

The outer edge average is with respect to the flat edge measure.

For rotationally symmetric test functions \(t^2,r^2\), the edge integrand is constant.

## 9. Null-generator averages for t^2 and r^2

Along a generator from

\[
p=(-1,\mathbf0)
\]

to the unit edge,

\[
t
=
-1+\frac v2,
\]

\[
r
=
\frac v2.
\]

The kernel is symmetric under

\[
v\mapsto2-v.
\]

Therefore

\[
\overline{t^2}_\gamma
=
\overline{r^2}_\gamma.
\]

Writing

\[
x=\frac v2,
\]

the normalized kernel is a beta distribution

\[
x\sim
{\rm Beta}(m,m).
\]

Hence

\[
\boxed{
\overline{t^2}_\gamma
=
\overline{r^2}_\gamma
=
\frac{
d+2
}{
4(d+1)
}.
}
\]

## 10. Diamond averages

For the unit \(d\)-dimensional Minkowski diamond,

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

For the spatial radius,

\[
\boxed{
\langle r^2\rangle_D
=
\frac{
d(d-1)
}{
(d+1)(d+2)
}.
}
\]

On the edge,

\[
t=0,
\qquad
r=1.
\]

Thus

\[
(t^2)_E=0,
\]

and

\[
(r^2)_E=1.
\]

## 11. Logarithmic response for the t^2 family

Substitution gives

\[
\boxed{
C_t(d)
:=
\frac1{\varepsilon}
\frac{
\delta K_d^{(t)}
}{
K_d^{\rm Mink}
}
=
-
\frac{
d^3+6d^2+12d-8
}{
2(d+1)(d+2)
}.
}
\]

Equivalently,

\[
C_t(d)
=
-
\frac{
(d+2)^3-16
}{
2(d+1)(d+2)
}.
\]

## 12. Logarithmic response for the r^2 family

Likewise,

\[
\boxed{
C_r(d)
:=
\frac1{\varepsilon}
\frac{
\delta K_d^{(r)}
}{
K_d^{\rm Mink}
}
=
\frac{
3d^3+14d^2-12d-8
}{
2(d+1)(d+2)
}.
}
\]

## 13. Curvature of the conformal test metrics

For

\[
g=e^{2\omega}\eta
\]

with

\[
d\omega(0)=0,
\]

the conformal Ricci formula at the center gives

\[
R_{\mu\nu}
=
-(d-2)
\partial_\mu\partial_\nu\omega
-
\eta_{\mu\nu}
\Box\omega
\]

to first order.

Also,

\[
R
=
-2(d-1)
\Box\omega.
\]

### t^2 family

For

\[
\omega=\varepsilon t^2,
\]

\[
\boxed{
\frac R\varepsilon
=
4(d-1),
}
\]

and

\[
\boxed{
\frac{R_{TT}}\varepsilon
=
-2(d-1).
}
\]

### r^2 family

For

\[
\omega=\varepsilon r^2,
\]

\[
\boxed{
\frac R\varepsilon
=
-4(d-1)^2,
}
\]

and

\[
\boxed{
\frac{R_{TT}}\varepsilon
=
2(d-1).
}
\]

These two curvature vectors are linearly independent for

\[
d\ge3.
\]

## 14. Solving for A_d and B_d

The structural theorem gives

\[
K_d^{\rm Mink}
C_t(d)
=
4(d-1)A_d
-
2(d-1)B_d,
\]

and

\[
K_d^{\rm Mink}
C_r(d)
=
-4(d-1)^2A_d
+
2(d-1)B_d.
\]

Solving the \(2\times2\) system gives

\[
\boxed{
A_d
=
-
K_d^{\rm Mink}
\frac{
d(d+6)
}{
4(d-1)(d+1)(d+2)
},
}
\]

and

\[
\boxed{
B_d
=
K_d^{\rm Mink}
\frac{
d^2+2d-4
}{
4(d-1)(d+1)
}.
}
\]

## 15. Explicit 3+1 result

For

\[
d=4,
\]

\[
K_4^{\rm Mink}
=
9\pi.
\]

The universal ratios are

\[
\frac{A_4}{K_4}
=
-\frac19,
\]

\[
\frac{B_4}{K_4}
=
\frac13.
\]

Therefore

\[
\boxed{
A_4=-\pi,
\qquad
B_4=3\pi.
}
\]

Hence

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
+
\pi L^2
\left(
3R_{\mu\nu}T^\mu T^\nu
-
R
\right)_o
+
o(L^2).
}
\]

The local orientation-recovery error is therefore

\[
\boxed{
1-p_{4,g,L}^{\rm UPO}(n)
\sim
\frac{
9\pi
+
\pi L^2(3R_{TT}-R)
+
o(L^2)
}{
n
}.
}
\]

## 16. Vacuum consequence

In Ricci-flat spacetime,

\[
R_{\mu\nu}=0,
\]

so

\[
\boxed{
K_{d,g}(D_L)
=
K_d^{\rm Mink}
+
o(L^2).
}
\]

In particular,

\[
d=4:
\qquad
K_{4,g}(D_L)
=
9\pi
+
o(L^2).
\]

Thus the first curvature correction to the local recovery rate is insensitive to pure Weyl curvature.

## 17. Relation to small-diamond literature

Small causal-diamond observables studied by Gibbons--Solodukhin and later work also receive their first nonvacuum corrections through

\[
R
\]

and

\[
R_{TT}.
\]

The present coefficients are not imported from those observables.

They arise from the stochastic arrow-erasure recovery functional.

The agreement in tensorial structure follows from local covariance and the isotropy of the centered flat reference diamond.

## 18. Regression

The repository script

tools/verify_first_curvature_response_constants.py

checks for

\[
d=4,\ldots,12:
\]

1. the null-generator beta-kernel average;
2. the two conformal logarithmic responses;
3. solution of the two curvature-response equations;
4. the closed formulas for \(A_d/K_d\) and \(B_d/K_d\);
5. the explicit \(d=4\) ratios
   \[
   -1/9,\quad1/3.
   \]

## 19. Remaining question

The \(d\ge4\) first curvature correction is now explicit.

The analogous \(d=3\) constants require perturbing the bulk volume-time integral rather than the null-edge coefficient.

That is a different calculation and remains open.

## 20. Next physical question

In \(3+1\), the next term after

\[
\pi L^2(3R_{TT}-R)
\]

is especially interesting.

In Ricci-flat spacetime the \(L^2\) term vanishes, so the leading correction must probe higher-order curvature information.

Possible \(L^4\) invariants include quadratic electric/magnetic Weyl combinations.

The exact vacuum \(L^4\) response should be computed rather than inferred from analogy with other causal-diamond observables.
