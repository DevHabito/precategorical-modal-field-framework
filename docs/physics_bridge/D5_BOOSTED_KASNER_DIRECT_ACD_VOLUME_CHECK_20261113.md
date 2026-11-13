> **CI STATUS — 2026-11-13:** GitHub Actions run **43411592007** completed successfully on commit \`0d56cfb108a63b353ea1c4fcb8d88df3dd450ca5\`. The run reproduced the three boosted extrapolations and the direct discrimination between the re-integrated coefficient law and the printed Eq. (79). An earlier run, **43411112221**, failed only because an attempted numerical inversion for the full \((A_5,B_5,C_5)\) vector used an unrealistically tight tolerance on an ill-conditioned matrix. The individual boosted scalar extrapolations in that failed run already agreed with the corrected law. The inversion has been demoted to a diagnostic and is no longer a pass/fail criterion.

# Direct boosted d = 5 LRS-Kasner ACD volume calibration

**Date:** 2026-11-13  
**Author:** Felipe Gianini Romero  
**Status:** independent numerical geometry check of the nonzero-\(H^2\) sector  
**Scope:** centered small Alexandrov intervals along transversely moving timelike geodesics in five-dimensional LRS Kasner  
**Purpose:** test the corrected all-dimensional vacuum ACD law in an invariant direction not proportional to the Cahen--Wallach type-N relation

## 1. Background

The corrected all-dimensional vacuum ACD expansion is

\[
\frac{V(D_L)}{V_{\rm flat}(L)}
=
1+
L^4
\left[
A_dE^2+B_dH^2+C_dD^2
\right]
+
o(L^4).
\]

The exact Cahen--Wallach family checks

\[
\frac{A_d}{4}
+
\frac{B_d}{2}
+
C_d.
\]

The comoving LRS-Kasner family checks

\[
A_dE^2+C_dD^2
\]

because

\[
H^2=0.
\]

A genuinely independent test of \(B_d\) therefore requires a geometry/observer pair with

\[
H^2\ne0
\]

and invariant ratios different from the type-N relation.

## 2. Boosted five-dimensional Kasner observer

Use

\[
ds^2
=
-dt^2
+
t^{-1}dx^2
+
t(dy_1^2+dy_2^2+dy_3^2).
\]

Center the causal diamond on a timelike geodesic carrying conserved momentum in the \(y_1\) direction.

At the midpoint \(t=1\), let the local orthonormal speed be \(v\).

The exact boosted Weyl invariants are

\[
E^2(v)
=
\frac{
v^4+2v^2+3
}{
4(1-v^2)^2
},
\]

\[
H^2(v)
=
\frac{
3v^2
}{
(1-v^2)^2
},
\]

\[
D^2(v)
=
\frac{
7v^4+2v^2+3
}{
2(1-v^2)^2
}.
\]

The corrected \(d=5\) law predicts

\[
\boxed{
c_{\rm target}(v)
=
\frac{
8v^4+24v^2+25
}{
1152(1-v^2)^2
}.
}
\]

The direct volume calculation below does not use this expression.

## 3. Why the first numerical route was rejected

A first implementation integrated the intersection of the past and future null cones by taking the smaller radial boundary on a generic angular grid.

That method failed the flat boosted control at relative order

\[
10^{-4},
\]

which is the same order as the small-diamond \(L^4\) signal.

No coefficient from that implementation was accepted.

The failure was traced to the nonsmooth switching set where the active boundary changes from the past cone to the future cone.

## 4. Geometric reduction used in the new calculation

The LRS symmetry makes every fixed-time null-cone section a body of revolution about the distinguished \(x\)-axis.

For a fixed \(x\), the remaining transverse section is a three-ball.

The two cone sections therefore reduce, at each fixed \((t,x)\), to two three-balls with radii

\[
R_-(t,x),
\qquad
R_+(t,x),
\]

whose centers are separated only in the \(y_1\) direction.

Their intersection volume is known exactly.

For radii \(R,r\) and center separation \(d\),

\[
V_{\rm lens}
=
0
\]

if

\[
d\ge R+r,
\]

and

\[
V_{\rm lens}
=
\frac{4\pi}{3}
\min(R,r)^3
\]

if

\[
d\le |R-r|.
\]

In the genuine lens regime,

\[
|R-r|<d<R+r,
\]

the exact three-ball intersection is

\[
\boxed{
V_{\rm lens}
=
\frac{
\pi(R+r-d)^2
\left[
d^2+2d(R+r)-3(R-r)^2
\right]
}{
12d
}.
}
\]

This removes the problematic angular minimum entirely.

The spatial four-volume of the diamond slice is then

\[
V_{\rm slice}(t)
=
2
\int_0^{x_{\max}}
V_{\rm lens}
\left(
R_-(t,x),
R_+(t,x),
d_\perp
\right)
dx.
\]

Finally,

\[
V(D_L)
=
\int
t\,
V_{\rm slice}(t)\,
dt,
\]

because

\[
\sqrt{\det g_{\rm spatial}}=t.
\]

## 5. Exact timelike-geodesic centering

Let

\[
P=\gamma v,
\qquad
\gamma=(1-v^2)^{-1/2}.
\]

The central geodesic obeys

\[
\frac{dt}{d\tau}
=
\sqrt{
1+\frac{P^2}{t}
},
\]

and

\[
\frac{dy_1}{d\tau}
=
\frac{P}{t}.
\]

The primitive used to place the tips at proper times

\[
\tau=\pm L
\]

around \(t=1\) is

\[
\tau(t)
=
\sqrt{t(t+P^2)}
-
P^2
\operatorname{arsinh}
\sqrt{
\frac{t}{P^2}
}.
\]

The transverse geodesic displacement uses

\[
y_1(t)
=
2P
\operatorname{arsinh}
\sqrt{
\frac{t}{P^2}
}.
\]

Thus the tip coordinates are obtained without numerically integrating the timelike geodesic.

## 6. Null-cone construction

For each null ray, let \(c\in[0,1]\) be the conserved axial momentum fraction.

The null energy is

\[
\mathcal E(t,c)
=
\sqrt{
ct+\frac{1-c}{t}
}.
\]

The axial and transverse coordinate integrals are

\[
X(c)
=
\sqrt c
\int
\frac{t}{\mathcal E(t,c)}
dt,
\]

\[
R(c)
=
\sqrt{1-c}
\int
\frac{dt/t}{\mathcal E(t,c)}.
\]

The numerical implementation samples these functions using

\[
c=\sin^2\theta
\]

so both axis endpoints are resolved regularly.

A monotone PCHIP interpolation produces

\[
R=R(X)
\]

for each cone section.

## 7. Convergence structure

The causal diamond is centered in proper time.

Therefore reversing the sign of \(L\) exchanges the two tips but leaves the interval itself unchanged.

Hence the relative small-\(L\) expansion is even:

\[
\frac{V}{V_{\rm flat}}
=
1+
c_4L^4+
c_6L^6+
\cdots.
\]

The scaled quantity

\[
C(L)
=
\frac{
V/V_{\rm flat}-1
}{
L^4
}
\]

must therefore satisfy

\[
C(L)
=
c_4+c_6L^2+\cdots.
\]

This makes a linear extrapolation in \(L^2\) the correct first asymptotic regression.

## 8. High-resolution results

The high-resolution calculation used

\[
L=
0.07,\ 0.06,\ 0.05
\]

with:

- 2561 null-cone profile nodes;
- 56-point Gauss--Legendre null quadrature;
- 320 time panels;
- 8-point Gauss--Legendre integration per time panel.

### v = 0.3

Target:

\[
c_{\rm target}(0.3)
=
0.028538387741684445.
\]

Measured scaled coefficients:

\[
C(0.07)
=
0.028682238573204902,
\]

\[
C(0.06)
=
0.028642946793538484,
\]

\[
C(0.05)
=
0.02860551344241457.
\]

Linear extrapolation in \(L^2\):

\[
\boxed{
C(0)
=
0.028526539347059808.
}
\]

Difference from target:

\[
\boxed{
-1.18484\times10^{-5}.
}
\]

### v = 0.5

Target:

\[
c_{\rm target}(0.5)
=
\frac7{144}
=
0.04861111111111111.
\]

Measured:

\[
C(0.07)
=
0.048986476543915414,
\]

\[
C(0.06)
=
0.04888682492086041,
\]

\[
C(0.05)
=
0.04880023737996452.
\]

The higher-order residual scales almost perfectly as \(L^2\):

\[
\frac{
C(L)-c_{\rm target}
}{
L^2
}
=
0.07661,\ 0.07659,\ 0.07565.
\]

The extrapolated intercept is

\[
\boxed{
C(0)
=
0.04860675154013165.
}
\]

Difference:

\[
\boxed{
-4.35957\times10^{-6}.
}
\]

### v = 0.7

Target:

\[
c_{\rm target}(0.7)
=
0.12909297706010509.
\]

Measured:

\[
C(0.07)
=
0.13096434671149948,
\]

\[
C(0.06)
=
0.13046207684123085,
\]

\[
C(0.05)
=
0.13004044085107577.
\]

Again,

\[
\frac{
C(L)-c_{\rm target}
}{
L^2
}
=
0.38191,\ 0.38031,\ 0.37899,
\]

showing the expected even small-\(L\) correction.

The extrapolated value is

\[
\boxed{
C(0)
=
0.1290772777673617.
}
\]

Difference:

\[
\boxed{
-1.56993\times10^{-5}.
}
\]

## 9. Interpretation

All three nonzero boosts approach the independently predicted function

\[
\boxed{
c_5(v)
=
\frac{
8v^4+24v^2+25
}{
1152(1-v^2)^2
}
}
\]

within a few times \(10^{-5}\) in the extrapolated coefficient.

This is important because the calculation:

1. uses the physical Kasner null cones directly;
2. does not use Wang Eq. (74);
3. does not use the corrected ACD coefficient formula in the integration;
4. has \(H^2\ne0\);
5. probes three distinct invariant ratios;
6. reproduces the expected \(L^2\) approach to the centered-diamond limit.

Thus the magnetic/hook sector is no longer supported only by the type-N Cahen--Wallach combination.

## 10. Evidence status

This is a numerical geometry check, not an analytic proof.

The strongest internally justified statement is now:

> The corrected all-dimensional ACD coefficient formula is consistent with two independent Ricci-flat geometry families. Cahen--Wallach provides an exact all-dimensional type-N test, while LRS-Kasner provides exact comoving checks in \(d=4,5,6\) and an independent nonzero-\(H^2\) boosted numerical check in \(d=5\).

The remaining strongest upgrade would be an exact formal boosted-Kasner jet derivation.

## 11. Reproducibility

Checker:

tools/check_d5_boosted_kasner_acd_volume_numerically.py

The checker keeps the target formula separate from the physical volume integration and fails if the \(L\to0\) extrapolation exceeds the declared absolute tolerance.



## 12. Attempted coefficient-vector inversion and why it is not used as primary evidence

The boosted family initially suggested a stronger numerical inversion.

Using

\[
v=0,\quad \frac12,\quad \frac7{10},
\]

the three invariant rows are linearly independent, with exact determinant

\[
\det M=\frac{392}{289}\ne0.
\]

Algebraically, the three directions therefore determine

\[
A_5,\quad B_5,\quad C_5.
\]

However, the numerical matrix is poorly conditioned:

\[
\kappa(M)\approx121.
\]

This matters because the boosted volumes are extracted from finite-\(L\) numerical extrapolations.

Errors of order \(10^{-5}\) in the extrapolated scalar coefficients can be amplified to order \(10^{-4}\) in the reconstructed invariant vector.

A GitHub Actions reproduction exposed exactly this effect.

The individual boosted extrapolations remained accurate, but the reconstructed \(A_5,B_5,C_5\) vector moved outside the initially imposed \(10^{-5}\) tolerance.

Therefore:

\[
\boxed{
\text{the coefficient-vector inversion is diagnostic only.}
}
\]

It is not used as primary evidence for the corrected law.

This is a numerical-conditioning limitation, not evidence against the boosted-volume agreement.

## 13. Better-conditioned direct comparison with the printed Eq. (79)

The robust comparison is scalar and pointwise in \(v\).

The corrected \(d=5\) law predicts

\[
\boxed{
c_{\rm corr}(v)
=
\frac{
8v^4+24v^2+25
}{
1152(1-v^2)^2
}.
}
\]

The \(d=5\) specialization of the printed Eq. (79) predicts instead

\[
\boxed{
c_{\rm printed}(v)
=
\frac{
1508v^4+5914v^2+4713
}{
217728(1-v^2)^2
}.
}
\]

For the CI-reproduced boosted volumes:

### v = 0.3

Numerical extrapolation:

\[
0.02854511484.
\]

Corrected prediction:

\[
0.02853838774.
\]

Printed Eq. (79):

\[
0.02915950396.
\]

Errors:

\[
|c_{\rm num}-c_{\rm corr}|
\approx
6.73\times10^{-6},
\]

\[
|c_{\rm num}-c_{\rm printed}|
\approx
6.14\times10^{-4}.
\]

### v = 0.5

Numerical extrapolation:

\[
0.04862267975.
\]

Corrected prediction:

\[
0.04861111111.
\]

Printed Eq. (79):

\[
0.05132397609.
\]

Errors:

\[
|c_{\rm num}-c_{\rm corr}|
\approx
1.16\times10^{-5},
\]

\[
|c_{\rm num}-c_{\rm printed}|
\approx
2.70\times10^{-3}.
\]

### v = 0.7

Numerical extrapolation:

\[
0.12907927742.
\]

Corrected prediction:

\[
0.12909297706.
\]

Printed Eq. (79):

\[
0.14078726080.
\]

Errors:

\[
|c_{\rm num}-c_{\rm corr}|
\approx
1.37\times10^{-5},
\]

\[
|c_{\rm num}-c_{\rm printed}|
\approx
1.17\times10^{-2}.
\]

Thus the boosted physical geometry is consistently much closer to the re-integrated coefficient law than to the printed Eq. (79).

This comparison does not require inversion of an ill-conditioned invariant matrix.

## 14. Updated evidence statement

The boosted Kasner test now supports the following statement:

\[
\boxed{
\text{direct non-type-N physical volumes favor the re-integrated d=5 law over the printed Eq. (79).}
}
\]

The statement is numerical and internal.

It does not establish a published correction by itself.

The strongest remaining analytic upgrade is an exact boosted-cone expansion, beginning with the exact timelike-tip jets recorded in

tools/derive_d5_boosted_kasner_timelike_tip_jets.py.


## 15. Mesh-convergence audit

A representative convergence check was performed at

\[
v=0.5,
\qquad
L=0.08.
\]

### Time-panel refinement

With 2561 cone-profile nodes and 56-point null quadrature:

\[
N_t=80:
\quad
C(L)\approx0.04909771093,
\]

\[
N_t=160:
\quad
C(L)\approx0.04910485075,
\]

\[
N_t=320:
\quad
C(L)\approx0.04910107616.
\]

The 160-to-320 change is approximately

\[
3.8\times10^{-6}.
\]

### Cone-profile refinement

With 160 time panels:

\[
N_{\rm profile}=1281:
\quad
C(L)\approx0.04910023425,
\]

\[
N_{\rm profile}=2561:
\quad
C(L)\approx0.04910485076.
\]

The change is approximately

\[
4.6\times10^{-6}.
\]

The lower-resolution 321- and 641-node runs show visibly larger interpolation error and are not used for the final high-resolution evidence.

These convergence scales are below the declared

\[
3\times10^{-5}
\]

absolute tolerance of the CI extrapolation test.

The convergence audit does not turn the numerical calculation into an analytic proof; it bounds the most obvious discretization sensitivity at a representative small-\(L\) point.
