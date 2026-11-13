# Lemma: exact flat boosted-lens regime decomposition in d = 5

**Date:** 2026-11-13  
**Author:** Felipe Gianini Romero  
**Status:** exact elementary geometric lemma  
**Purpose:** fix the leading integration domains for a future analytic boosted-Kasner ACD expansion

## 1. Setup

Take the flat \(L\to0\) limit of the five-dimensional transversely boosted Kasner diamond.

Let

\[
P>0,
\qquad
\gamma=\sqrt{1+P^2}.
\]

Use scaled coordinates

\[
T=\frac{t-1}{L},
\qquad
X=\frac{x}{L}.
\]

At leading order the two tips are

\[
(-\gamma,-P),
\qquad
(+\gamma,+P)
\]

in the \((T,y_1)\) plane.

For fixed

\[
T\ge0
\]

and fixed axial coordinate \(X\), the two transverse sections are three-balls with radii

\[
R_-(T,X)
=
\sqrt{
(\gamma+T)^2-X^2
},
\]

\[
R_+(T,X)
=
\sqrt{
(\gamma-T)^2-X^2
}.
\]

Their centers are separated by

\[
d=2P.
\]

Because \(T\ge0\),

\[
R_-\ge R_+.
\]

The smaller cone exists for

\[
0\le X\le\gamma-T.
\]

The \(T<0\) half follows by tip exchange.

## 2. Monotonicity

Define

\[
S(X)=R_-+R_+,
\]

and

\[
D(X)=R_--R_+.
\]

For

\[
X>0,
\]

\[
\frac{dS}{dX}
=
-X
\left(
\frac1{R_-}
+
\frac1{R_+}
\right)
<0,
\]

while

\[
\frac{dD}{dX}
=
X
\left(
\frac1{R_+}
-
\frac1{R_-}
\right)
>0.
\]

Thus:

- the sum of the radii decreases monotonically;
- their difference increases monotonically.

This makes every regime crossing unique.

## 3. Axis values

At

\[
X=0,
\]

\[
R_-=\gamma+T,
\qquad
R_+=\gamma-T.
\]

Hence

\[
S(0)=2\gamma>2P,
\]

and

\[
D(0)=2T.
\]

Therefore the smaller ball is already contained on the axis exactly when

\[
T\ge P.
\]

Because \(D(X)\) increases with \(X\), for

\[
T\ge P
\]

containment holds throughout the allowed axial interval.

Thus

\[
\boxed{
P\le T\le\gamma
\quad\Longrightarrow\quad
\text{full containment}.
}
\]

## 4. Smaller-cone axial endpoint

At

\[
X=\gamma-T,
\]

the smaller radius vanishes:

\[
R_+=0.
\]

The larger radius is

\[
R_-
=
\sqrt{
(\gamma+T)^2-(\gamma-T)^2
}
=
2\sqrt{\gamma T}.
\]

Compare this with the center separation

\[
2P.
\]

Equality occurs at

\[
2\sqrt{\gamma T_c}
=
2P,
\]

so

\[
\boxed{
T_c
=
\frac{P^2}{\gamma}.
}
\]

For

\[
0\le T<T_c,
\]

the two balls cease to overlap before the smaller axial endpoint.

For

\[
T>T_c,
\]

they still overlap at that endpoint, and the outer region must therefore be a containment region rather than a non-overlap region.

## 5. Switching surface

In the non-overlap/lens regime, the switch is determined by

\[
R_-+R_+=2P.
\]

In the lens/containment regime, the switch is determined by

\[
R_--R_+=2P.
\]

Solving either branch gives the same squared axial location,

\[
\boxed{
X_*^2
=
1-\frac{T^2}{P^2}.
}
\]

The branch is selected by the sign of the corresponding smaller-radius expression.

## 6. Exact three-regime decomposition

For

\[
T\ge0,
\]

the flat boosted spatial section decomposes as follows.

### Regime I

If

\[
0\le T<\frac{P^2}{\gamma},
\]

then

\[
0\le X<X_*
\]

is a genuine three-ball lens, while

\[
X_*<X\le\gamma-T
\]

has no intersection.

Thus

\[
\boxed{
\text{lens}\to\text{empty}.
}
\]

### Regime II

If

\[
\frac{P^2}{\gamma}
\le T<P,
\]

then

\[
0\le X<X_*
\]

is a genuine lens and

\[
X_*<X\le\gamma-T
\]

has the smaller ball contained in the larger one.

Thus

\[
\boxed{
\text{lens}\to\text{containment}.
}
\]

### Regime III

If

\[
P\le T\le\gamma,
\]

then

\[
D(0)\ge2P.
\]

Since \(D(X)\) is increasing,

\[
D(X)\ge2P
\]

throughout the allowed axial interval.

Therefore

\[
\boxed{
\text{full containment}.
}
\]

## 7. Why this matters for the exact boosted calculation

The direct numerical boosted-volume checker treats the switching geometry exactly through the three-ball lens formula.

For an analytic small-\(L\) expansion, the present lemma supplies the unperturbed integration domains.

The remaining task is to expand:

1. the tip locations;
2. the null-cone radii;
3. the transverse center separation;
4. the lens volume density;

around these three fixed flat regimes.

The exact building blocks already available are:

- tools/derive_d5_boosted_kasner_timelike_tip_jets.py
- tools/derive_d5_kasner_null_cone_profile_jets.py
- tools/derive_d5_boosted_flat_lens_switching.py

The unresolved analytic step is the curvature perturbation of the lens integral through relative order \(L^4\).
