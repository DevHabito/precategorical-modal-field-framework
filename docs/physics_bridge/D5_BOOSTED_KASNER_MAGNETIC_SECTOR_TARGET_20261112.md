# d = 5 boosted LRS-Kasner target for the independent hook/magnetic ACD-volume sector

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact algebraic target established; direct causal-volume integration not yet validated  
**Purpose:** construct an independent geometry-based test of the \(H^2\) coefficient in the corrected all-dimensional Alexandrov-volume law

## 1. Why a boosted Kasner observer is useful

The comoving LRS-Kasner family is purely electric:

\[
H^2=0.
\]

It therefore checks only the combination

\[
A_dE^2+C_dD^2.
\]

The exact Cahen--Wallach plane wave has

\[
E^2:H^2:D^2
=
\frac14:\frac12:1,
\]

so it checks only one different linear combination.

To probe the hook/magnetic coefficient independently, it is useful to retain an exactly integrable Ricci-flat geometry while changing the timelike observer.

A transverse Lorentz boost of the \(d=5\) LRS-Kasner Weyl tensor does exactly this.

## 2. d = 5 LRS-Kasner background

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

At

\[
t=1,
\]

the comoving orthonormal Kasner exponents are

\[
p_x=-\frac12,
\qquad
p_{y_a}=\frac12.
\]

The nonzero orthonormal-frame Weyl components follow directly from the Kasner Riemann tensor,

\[
C_{0i0i}
=
p_i(1-p_i),
\]

\[
C_{ijij}
=
p_ip_j.
\]

The comoving invariants are

\[
E^2=\frac34,
\qquad
H^2=0,
\qquad
D^2=\frac32.
\]

## 3. Transverse boost

Boost the orthonormal frame with speed \(v\) in the \(y_1\) direction.

Let

\[
\gamma
=
\frac1{\sqrt{1-v^2}}.
\]

The exact Lorentz transformation of the Weyl tensor gives

\[
\boxed{
E^2(v)
=
\frac{
v^4+2v^2+3
}{
4(1-v^2)^2
},
}
\]

\[
\boxed{
H^2(v)
=
\frac{
3v^2
}{
(1-v^2)^2
},
}
\]

and

\[
\boxed{
D^2(v)
=
\frac{
7v^4+2v^2+3
}{
2(1-v^2)^2
}.
}
\]

Thus

\[
H^2(v)>0
\]

for every nonzero subluminal boost.

The boosted observer therefore probes a genuinely different invariant direction.

The exact algebra is implemented in

tools/derive_d5_boosted_kasner_weyl_target.py.

## 4. Corrected all-d prediction

For \(d=5\),

\[
A_5=\frac{151}{5184},
\]

\[
B_5=\frac{11}{5184},
\]

\[
C_5=-\frac1{10368}.
\]

Therefore

\[
A_5E^2(v)
+
B_5H^2(v)
+
C_5D^2(v)
\]

reduces exactly to

\[
\boxed{
c_5(v)
=
\frac{
8v^4+24v^2+25
}{
1152(1-v^2)^2
}.
}
\]

At

\[
v=0,
\]

this returns the exact comoving result

\[
\boxed{
c_5(0)=\frac{25}{1152}.
}
\]

The \(v\)-dependence therefore supplies a one-parameter target that is sensitive to the hook/magnetic coefficient.

## 5. Timelike geodesic remains integrable

The boost should be implemented physically by centering the Alexandrov interval on the timelike geodesic with conserved transverse momentum.

If the conserved momentum is \(P\), then

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

At the midpoint \(t=1\),

\[
P=\gamma v.
\]

Both integrals are elementary.

Writing

\[
a=P^2,
\]

one antiderivative for proper time is

\[
\boxed{
\tau(t)
=
\sqrt{t(t+a)}
-
a\,\operatorname{arsinh}\sqrt{\frac ta}
+
\text{constant},
}
\]

while the transverse displacement is

\[
\boxed{
y_1(t)
=
2P\,
\operatorname{arsinh}\sqrt{\frac ta}
+
\text{constant}.
}
\]

Thus the centered boosted tips can be obtained without integrating the timelike geodesic numerically.

## 6. Null cones also retain first integrals

For a null geodesic, let \(c\) denote the conserved axial momentum fraction.

Then

\[
\mathcal E^2(t,c)
=
ct
+
\frac{1-c}{t},
\]

and the coordinate displacements satisfy

\[
\frac{dx}{dt}
=
\frac{
\sqrt c\,t
}{
\sqrt{ct+(1-c)/t}
},
\]

\[
\frac{d\rho_\perp}{dt}
=
\frac{
\sqrt{1-c}/t
}{
\sqrt{ct+(1-c)/t}
}.
\]

Therefore each individual null cone remains exactly reducible to one-dimensional quadratures.

The remaining complication is geometric rather than dynamical: the two cone centers are displaced relative to each other in the transverse direction.

## 7. Rejected first numerical route

A preliminary deterministic integration was attempted using:

1. Gauss quadrature in time;
2. Gauss--Jacobi quadrature on \(S^3\);
3. interpolation of each null-cone radial profile;
4. ray tracing from the central timelike geodesic;
5. the minimum of the past- and future-cone radial intersections.

This route was **not accepted**.

The required control is the exactly flat boosted diamond, whose physical volume must be Lorentz invariant.

With ordinary angular quadrature, the flat control retained a relative error of order

\[
10^{-4}.
\]

For the intended small-diamond extraction, the physical signal is of order

\[
L^4,
\]

which is also around \(10^{-4}\) for practical test sizes.

Therefore the numerical discretization error is of the same order as the coefficient being measured.

Any extrapolated \(H^2\) coefficient from that implementation would be unreliable.

No boosted-volume coefficient was recorded.

## 8. Source of the numerical difficulty

On each spatial slice, the causal section is the intersection of two translated convex null-cone sections.

The radial boundary is piecewise determined by the past cone or future cone.

The switching hypersurface produces a nonsmooth derivative in the angular radial function.

Generic tensor-product quadrature converges too slowly across that switching set for a clean \(L^4\) extraction.

This is already visible in the flat boosted control and is not a curvature effect.

## 9. Required improved method

The next numerical or analytic implementation should integrate the switching surface explicitly.

Two viable approaches are:

### A. Exact split-angle quadrature

For each time and remaining angular coordinate:

1. solve the equality of the past and future radial boundaries;
2. use that angle as an exact quadrature split;
3. integrate each smooth branch separately.

This should restore high-order convergence.

### B. Formal boosted directional jets

Expand the translated cone intersection itself in \(L\) before integration.

This is algebraically harder but would produce an exact rational result analogous to the comoving \(d=5,6\) checkers.

The target is fixed in advance:

\[
\boxed{
c_5(v)
=
\frac{
8v^4+24v^2+25
}{
1152(1-v^2)^2
}.
}
\]

No parameter should be adjusted to obtain this expression.

## 10. Scientific value of a successful boosted check

A direct boosted-Kasner volume calculation would test a Weyl direction with

\[
H^2\ne0
\]

that is not proportional to the Cahen--Wallach invariant relation.

Together with:

- exact Cahen--Wallach;
- exact comoving LRS-Kasner in \(d=4,5,6\);

it would independently probe all three all-dimensional invariant sectors

\[
E^2,\qquad H^2,\qquad D^2.
\]

This would substantially reduce the remaining dependence on Wang's abridged printed null-boundary formula.
