# Adjacent-twin asymptotic coefficients in Minkowski comparability graphs

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** analytic coefficient derivation + exact two-point numerical validation  
**Proof status:** leading constants derived; global small-(D) domination/remainder lemma still open  
**Claim discipline:** the constants below are not promoted to theorem status until that final analytic step is closed

## 1. Problem

Let (C_{d,n}) be (n) iid uniform points in the standard flat Alexandrov interval

[
A=I(p,q),
qquad
p=(-1,0,ldots,0),
qquad
q=(1,0,ldots,0)
]

of (d)-dimensional Minkowski spacetime.

Erase causal direction and retain only the comparability graph.

An **adjacent twin pair** is a pair (x,y) such that

1. (x) and (y) are causally comparable; and
2. every third sprinkled event is comparable to (x) exactly when it is comparable to (y).

Graph-theoretically, this is a size-two non-stable module, also called a pair of adjacent or (1)-twins in standard graph terminology.

Let

[
T_n
]

be the number of adjacent twin pairs.

The earlier held-out experiment found finite data consistent with

[
E[T_n]=Theta(n^{-1})
]

for (d=3) and (d=4).

This note asks for the leading constants.

## 2. Exact two-point reduction

For a continuum event (xin A), define its comparability region

[
S_x
=
{zin A:z	ext{ is causally comparable to }x}.
]

For a comparable pair (x,y), define

[
D(x,y)
=
rac{
operatorname{vol}(S_x	riangle S_y)
}{
operatorname{vol}(A)
}.
]

Conditioned on (x,y), each of the remaining (n-2) iid points avoids the distinguishing region with probability

[
1-D(x,y).
]

Therefore

[
oxed{
E[T_n]
=
inom n2
Eleft[
mathbf 1_{{Xsim Y}}
(1-D(X,Y))^{n-2}
ight].
}
]

This identity is exact.

No simulation of the remaining (n-2) points is needed to compute the expectation.

For (xprec y), causal nesting gives the exact interval-volume formula

[
oxed{
D(x,y)
=
rac{
	au_{py}^{d}
-
	au_{px}^{d}
+
	au_{xq}^{d}
-
	au_{yq}^{d}
-
2	au_{xy}^{d}
}{
2^d
}.
}
]

Here (	au_{ab}) is the proper time between comparable events (aprec b).

## 3. The small-(D) formulation

Define

[
F_d(arepsilon)
=
P(
Xsim Y,,
D(X,Y)learepsilon
).
]

If one can prove

[
F_d(arepsilon)
sim
K_darepsilon^3,
qquad
arepsilondownarrow0,
]

then the Laplace relation

[
E[
mathbf1_{{Xsim Y}}
e^{-nD}
]
sim
6K_d n^{-3}
]

implies

[
E[T_n]
sim
rac{3K_d}{n}.
]

Thus the full twin problem in (d=3,4) can be reduced to a cubic small-(D) volume law.

The calculations below identify candidate values

[
oxed{
K_3=rac{32pi}{9}
}
]

and

[
oxed{
K_4=3pi.
}
]

Equivalently,

[
oxed{
E[T_n]
sim
rac{32pi}{3n}
quad(d=3)
}
]

and

[
oxed{
E[T_n]
sim
rac{9pi}{n}
quad(d=4).
}
]

The remaining obligation is a global proof that no omitted small-(D) stratum changes these coefficients.

## 4. (2+1) spacetime: bulk coefficient

Set

[
d=3.
]

For a fixed interior event (x), write

[
U=	au_{px}^2,
qquad
V=	au_{xq}^2.
]

Let

[
u=x-p,
qquad
v=q-x.
]

For a small future-timelike displacement (h),

[
y=x+h.
]

Taylor expansion of the exact distinguishing volume gives

[
D(x,x+h)
=
L_xcdot h
+
O(|h|^2),
]

where

[
L_x
=
rac38
left(
sqrt U,u
+
sqrt V,v
ight).
]

The (O(|h|^3)) term from (	au_{xy}^3) is subleading at a fixed nondegenerate interior point.

The Minkowski norm satisfies

[
L_x^2
=
rac9{64}H(U,V),
]

with

[
H(U,V)
=
U^2+V^2+sqrt{UV}(4-U-V).
]

The vector (L_x) is future timelike except at the null waist

[
U=V=0.
]

### 4.1 Local future-cone integral

For a future-timelike covector (L) in (2+1) dimensions,

[
int_{J^+(0)}
e^{-nLcdot h},d^3h
=
rac{2pi}{
n^3(L^2)^{3/2}
}.
]

Accounting for both causal directions and the factor

[
inom n2
]

then gives the candidate bulk coefficient

[
C_3
=
rac1{operatorname{vol}(A)^2}
int_A
rac{2pi}{
(L_x^2)^{3/2}
}
,d^3x.
]

For the standard (d=3) diamond,

[
operatorname{vol}(A)
=
rac{2pi}{3}.
]

## 5. Exact evaluation of the (d=3) coefficient integral

Set

[
x_0=sqrt U,
qquad
y_0=sqrt V.
]

The domain becomes

[
x_0ge0,
qquad
y_0ge0,
qquad
x_0+y_0le2.
]

After integrating the spatial angle, the spacetime measure becomes

[
d^3x
=
pi x_0y_0,dx_0,dy_0.
]

Therefore

[
C_3
=
rac{64}{3}I,
]

where

[
I
=
int_{x_0+y_0le2}
rac{
4x_0y_0
}{
left[
x_0^4+y_0^4
+x_0y_0(4-x_0^2-y_0^2)
ight]^{3/2}
}
dx_0dy_0.
]

Now set

[
s=x_0+y_0,
qquad
z=rac{x_0-y_0}{x_0+y_0}.
]

Then

[
0le sle2,
qquad
-1le zle1,
]

and

[
H
=
rac{s^2}{4}
left[
s^2z^4
+
3s^2z^2
-
4z^2
+
4
ight].
]

The transformed integrand is

[
rac{
4(1-z^2)
}{
left[
s^2z^4
+
3s^2z^2
-
4z^2
+
4
ight]^{3/2}
}.
]

The (s)-integral is elementary:

[
int_0^2
rac{
4(1-z^2),ds
}{
left[
s^2z^2(z^2+3)
+
4(1-z^2)
ight]^{3/2}
}
=
rac1{1+z^2}.
]

Hence

[
I
=
int_{-1}^{1}
rac{dz}{1+z^2}
=
racpi2.
]

Thus the candidate leading coefficient is

[
oxed{
C_3
=
rac{32pi}{3}
approx
33.5103216383.
}
]

## 6. Why the (d=3) null waist does not appear to change the coefficient

The local covector norm vanishes only at

[
U=V=0,
]

the spatial null waist of the diamond.

The coefficient integral above is nevertheless finite there.

Indeed, when

[
x_0sim y_0sim s	o0,
]

the transformed coefficient density behaves only like an integrable (1/s) singularity before the area element is included.

The separate waist scaling found earlier gives a contribution of order

[
n^{-4/3},
]

which is smaller than the bulk

[
n^{-1}
]

term.

This strongly suggests that the finite integral above is the correct global leading coefficient.

What is still missing is a written uniform bound controlling the transition region where the ordinary (h=O(n^{-1})) bulk scaling crosses into the (n^{-2/3}) waist scaling.

That is the main (d=3) proof obligation.

## 7. (3+1) spacetime: null-waist coefficient

Set

[
d=4.
]

In this dimension the bulk near-coincidence contribution scales as

[
n^{-2},
]

so it cannot produce the observed (n^{-1}) term.

The dominant contribution instead comes from the null waist.

Use

[
a=delta+t,
qquad
b=delta-t,
qquad
delta=1-r.
]

The normalized one-point measure is

[
dmu_4
=
3
left(
1-rac{a+b}{2}
ight)^2
da,db,dsigma,
]

where (dsigma) is normalized measure on (S^2).

Rescale two points (x,y) by

[
a_x=rac{2A}{sqrt n},
qquad
b_x=rac{2B}{sqrt n},
]

and

[
a_y=rac{2C}{sqrt n},
qquad
b_y=rac{2D}{sqrt n}.
]

For (xprec y), the leading causal conditions are

[
C>A,
qquad
B>D.
]

If the angular separation is written as

[
	heta
=
rac{2|z|}{sqrt n},
]

the timelike condition becomes

[
|z|^2
<
(C-A)(B-D).
]

The exact distinguishing fraction satisfies

[
nD(x,y)
longrightarrow
C^2-A^2+B^2-D^2.
]

The (	au_{xy}^4) term is one order smaller in this scaling.

## 8. Evaluation of the (d=4) waist integral

The rescaled pair measure contributes

[
rac{144}{pi n^3}
,dA,dB,dC,dD,d^2z
]

to leading order.

Integrating the angular disk gives

[
pi(C-A)(B-D).
]

Therefore the future-directed pair integral factorizes:

[
rac{144}{n^3}
left[
int_{0le A<C}
(C-A)
e^{-(C^2-A^2)}
,dA,dC
ight]^2.
]

Define

[
I_1
=
int_{0le A<C}
(C-A)
e^{-(C^2-A^2)}
,dA,dC.
]

With

[
u=C-A,
qquad
v=C+A,
]

one obtains

[
I_1
=
rac{sqrtpi}{4}.
]

Thus the future-directed pair integral is

[
rac{
144(pi/16)
}{
n^3
}
=
rac{9pi}{n^3}.
]

There are two causal directions, while

[
inom n2
sim
rac{n^2}{2}.
]

The factors cancel exactly to give the candidate coefficient

[
oxed{
C_4
=
9pi
approx
28.2743338823.
}
]

Hence

[
oxed{
E[T_n]
sim
rac{9pi}{n}
qquad
(d=4)
}
]

provided the complement of the rescaled null-waist region is (o(n^{-1})).

That complement bound is the remaining (d=4) proof obligation.

## 9. Exact finite expectation without full sprinklings

The exact two-point identity permits an important independent computational check.

Instead of generating all (n) events and searching the resulting graph for twin pairs, sample only (X,Y) with importance distributions concentrated on the relevant small-(D) geometry.

The repository now contains two full-support importance estimators.

### (d=3)

The proposal for (x) is proportional to the analytically evaluated local cone coefficient

[
(L_x^2)^{-3/2}.
]

Conditional on (x), the displacement proposal is proportional to

[
e^{-nL_xcdot h}
]

over the complete future timelike cone.

Every interior (x) and every future-comparable (y) in the diamond therefore has proposal support.

### (d=4)

The radial proposal is adapted to the limiting waist density, but the angular variable is sampled from the **exact finite-(n) causal cap**.

Thus every valid future-comparable pair in the diamond remains in support.

The resulting estimator evaluates the exact finite two-point expectation rather than the leading asymptotic integral alone.

## 10. Numerical coefficient approach

The exact two-point estimator gives:

### (d=3)

| (n) | (n,widehat E[T_n]) | candidate (32pi/3) |
|---:|---:|---:|
|48|9.9680|33.5103|
|384|16.7598|33.5103|
|(10^3)|19.3845|33.5103|
|(10^4)|24.2784|33.5103|
|(10^6)|29.8026|33.5103|
|(10^9)|32.6506|33.5103|
|(10^{12})|33.3101|33.5103|

The approach is slow but monotone over these audited points.

At

[
n=10^{12},
]

the estimate is already approximately

[
99.40%
]

of the analytic candidate.

### (d=4)

| (n) | (n,widehat E[T_n]) | candidate (9pi) |
|---:|---:|---:|
|48|11.3552|28.2743|
|384|18.1438|28.2743|
|(10^3)|20.1842|28.2743|
|(10^4)|23.5090|28.2743|
|(10^6)|26.6378|28.2743|
|(10^9)|27.9736|28.2743|

At

[
n=10^9,
]

the estimate is approximately

[
98.94%
]

of (9pi).

These high-(n) tests are possible precisely because the exact expectation is a two-point integral.

They are not simulations of causal sets with (10^9) or (10^{12}) vertices.

## 11. Independent finite-regime cross-check

The two-point expectations agree with the scale observed in full-sprinkling simulations.

For example:

- in (d=3,n=48), the two-point estimator gives
  [
  E[T_{48}]
  approx0.2077;
  ]
- in (d=4,n=48), it gives
  [
  E[T_{48}]
  approx0.2366.
  ]

The earlier full-causet Monte Carlo blocks produced values in the same statistical range.

This cross-check is useful because the two procedures have very different failure modes:

1. full sprinklings generate all vertices and detect graph twins directly;
2. the pair integral analytically marginalizes the other (n-2) vertices.

Agreement therefore tests both the geometric (D(x,y)) formula and the graph-level detector.

## 12. Relation to non-Hegelian pairs

Causal-set literature uses the term **non-Hegelian pair** for distinct events with identical directed relational profiles, usually requiring the events themselves to be incomparable.

That is not the object studied here.

Adjacent twins in the present audit are

- comparable to one another;
- identical only with respect to **unoriented comparability** to third events.

They are therefore a graph-module obstruction created by the deliberate arrow-erasure observation contract.

The concepts should not be conflated.

## 13. Current claim boundary

The following are now established exactly:

1. the two-point expectation identity;
2. the interval-volume formula for (D(x,y));
3. the local (d=3) coefficient integral and its evaluation to (32pi/3);
4. the (d=4) null-waist limiting integral and its evaluation to (9pi);
5. the finite two-point importance estimators.

The following is strongly numerically supported but still awaiting the final global analytic bound:

[
E[T_n]
sim
rac{32pi}{3n}
qquad(d=3),
]

and

[
E[T_n]
sim
rac{9pi}{n}
qquad(d=4).
]

The repository does **not** yet label these two asymptotic equivalences as proved theorems.

## 14. Precise next lemma

The cleanest remaining target is:

> **Small-distinguishing-volume lemma.**  
> For two iid uniform points in the standard Alexandrov diamond,
> [
> F_3(arepsilon)
> =
> rac{32pi}{9}arepsilon^3
> +o(arepsilon^3),
> ]
> and
> [
> F_4(arepsilon)
> =
> 3piarepsilon^3
> +o(arepsilon^3),
> ]
> where
> [
> F_d(arepsilon)
> =
> P(Xsim Y,D(X,Y)learepsilon).
> ]

This lemma would immediately convert the coefficient calculations into full twin asymptotic theorems by a standard Laplace argument.

It also isolates exactly what remains to be proved:

- control the (d=3) bulk-to-waist transition;
- control the (d=4) complement of the null-waist scaling region;
- rule out another small-(D) stratum with the same cubic measure.

That is now a much smaller mathematical problem than the original higher-dimensional UPO question.
