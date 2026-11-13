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
