# Adjacent-twin obstruction in Minkowski comparability graphs — preregistered scaling hypothesis

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** historical preregistration — the (d=4) (1/n) prediction has now been proved with constant (9\pi); the (d=3) theorem remains open  
**Claim level:** not a theorem; exponent prediction derived from local geometric scaling, not fitted to the held-out sizes

## 1. Why this obstruction matters

In a comparability graph, an adjacent twin pair is a pair of vertices (x,y) such that

1. (x) and (y) are adjacent, and
2. every other vertex is adjacent to (x) exactly when it is adjacent to (y).

Thus ({x,y}) is a non-stable module of size two.

For a connected comparability graph this is an immediate obstruction to unique partial orderability.

The finite higher-dimensional pilot shows that adjacent twins account for most of the observed non-UPO samples at the larger audited sizes.

This note asks for their asymptotic scale.

## 2. Exact conditional twin probability

Let (A=I(p,q)) be a flat Alexandrov interval and let

[
S_x
=
{zin A:z	ext{ is causally comparable to }x}.
]

For a comparable pair (xprec y), define the normalized distinguishing volume

[
D(x,y)
=
rac{
operatorname{vol}(S_x	riangle S_y)
}{
operatorname{vol}(A)
}.
]

Conditioned on (x,y), the remaining (n-2) sprinkled points are independent.

Therefore the pair is adjacent twins with conditional probability

[
oxed{
(1-D(x,y))^{n-2}.
}
]

If (T_n) is the number of adjacent twin pairs,

[
oxed{
mathbb E[T_n]
=
inom n2
mathbb Eleft[
mathbf 1_{{Xsim Y}}
(1-D(X,Y))^{n-2}
ight].
}
]

This identity is exact.

## 3. Exact distinguishing-volume identity

For (xprec y), causal nesting gives

[
J^-(x)subset J^-(y),
qquad
J^+(y)subset J^+(x).
]

The points comparable to one event but not the other occupy two wedges.

Using interval volumes,

[
operatorname{vol}(S_x	riangle S_y)
=
V(p,y)-V(p,x)
+
V(x,q)-V(y,q)
-
2V(x,y).
]

In flat (d)-dimensional Minkowski spacetime,

[
V(a,b)
=
c_d,	au(a,b)^d,
]

so for the standard diamond with endpoint proper time (2),

[
oxed{
D(x,y)
=
rac{
	au_{py}^d-	au_{px}^d
+
	au_{xq}^d-	au_{yq}^d
-
2	au_{xy}^d
}{
2^d
}.
}
]

This converts the twin problem into a continuum Laplace-type pair integral.

## 4. Candidate mechanism A — bulk coincidence

Take (x) in a compact interior region away from the null boundary and let (y) approach (x) through a timelike displacement of coordinate scale (arepsilon).

For a generic interior point, the symmetric difference of the two causal-comparable regions changes at first order:

[
D(x,y)=O(arepsilon).
]

To keep

[
nD=O(1),
]

the relevant displacement scale is

[
arepsilon=O(n^{-1}).
]

The volume of a (d)-dimensional local timelike neighborhood at this scale is

[
O(n^{-d}).
]

Multiplying by the (inom n2=O(n^2)) candidate pairs gives the bulk scaling

[
oxed{
mathbb E[T_n]_{m bulk}
sim
A_d^{m bulk}
n^{2-d}
}
]

provided the first-order distinguishing-volume coefficient is nondegenerate on a set of positive measure.

This is a scaling argument, not yet a proof of the constant.

## 5. Candidate mechanism B — null-waist boundary layer

The isolated-vertex analysis identified the special waist

[
t=0,qquad r=1,
]

where the comparable volume of a single event vanishes.

Near that waist, use

[
a=delta+t,
qquad
b=delta-t,
qquad
delta=1-r.
]

The single-event comparable fraction is (O(arepsilon^{d/2})) when

[
a,b=O(arepsilon).
]

To make the relevant distinguishing volume (D=O(1/n)), the natural boundary-layer scale is

[
arepsilon
=
n^{-2/d}.
]

For the first point, the two transverse waist coordinates contribute

[
arepsilon^2.
]

For a second point to be timelike comparable while remaining in the same boundary layer, its two transverse coordinates contribute another

[
arepsilon^2,
]

and its angular position on the ((d-2))-sphere must lie in an angular patch of scale

[
arepsilon^{d-2}.
]

Thus the pair phase-space volume scales as

[
arepsilon^{d+2}.
]

Since

[
arepsilon=n^{-2/d},
]

this is

[
n^{-2(d+2)/d}.
]

After multiplying by (O(n^2)) candidate pairs,

[
oxed{
mathbb E[T_n]_{m waist}
sim
A_d^{m waist}
n^{-4/d}.
}
]

Again, the exponent is the current prediction; the constant has not been derived.

## 6. Preregistered dominant exponent

The slower-decaying of the two mechanisms should dominate if both local coefficients are nonzero and no third lower-codimension zero set of (D) intervenes.

Therefore the preregistered scaling hypothesis is

[
oxed{
mathbb E[T_n]
asymp
n^{eta_d},
qquad
eta_d
=
max
left(
2-d,
-rac4d
ight).
}
]

This gives:

| spacetime dimension (d) | bulk exponent (2-d) | waist exponent (-4/d) | predicted dominant exponent |
|---:|---:|---:|---:|
|2|0|-2|0|
|3|-1|-4/3|-1|
|4|-2|-1|-1|
|5|-3|-4/5|-4/5|
|6|-4|-2/3|-2/3|

The (d=3) and (d=4) predictions are therefore both

[
oxed{
mathbb E[T_n]
=
Theta(n^{-1})
}
]

if the scaling hypothesis is correct.

The mechanisms differ:

- (d=3): bulk near-coincidence should dominate;
- (d=4): the null-waist boundary layer should dominate.

## 7. Existing data used to motivate, not test, this prediction

Before this preregistration, the project had already observed finite twin-pair means.

Representative values were:

### (d=3)

[
n=48: 0.222,
qquad
n=64: 0.1764,
qquad
n=96: 0.1190,
qquad
n=128: 0.0967.
]

The products (n,E[T_n]) are roughly (10)–(12) over this range.

### (d=4)

[
n=48: 0.2393,
qquad
n=64: 0.1968,
qquad
n=96: 0.1545,
qquad
n=128: 0.1293.
]

The products (n,E[T_n]) are roughly (11)–(17).

These data are not prospective evidence for the exponent because they were visible before the hypothesis was frozen.

They merely show that the predicted order is plausible enough to justify a held-out test.

## 8. Held-out test protocol

The next simulation must use sizes not inspected while deriving the exponent.

The preregistered targets are

[
oxed{
n=320,quad n=384
}
]

for both

[
d=3,quad d=4.
]

Primary diagnostic:

[
n,widehat{E[T_n]}.
]

Under the (n^{-1}) hypothesis this quantity should remain (O(1)), rather than growing or decaying by a power of (n).

Secondary diagnostic:

[
widehat P(T_n>0).
]

No fixed constant is preregistered.

The test is about the exponent only.

## 9. Failure criteria

The (n^{-1}) scaling hypothesis should be treated as weakened or rejected if the held-out data, together with the already observed range, show a systematic power trend incompatible with a bounded (nE[T_n]).

A single noisy block is not sufficient because twin pairs are rare at large (n).

The number of observed twin pairs and Monte Carlo uncertainty must be reported.

No post-hoc change of the target exponent is permitted without creating a new hypothesis.

## 10. Consequence if the hypothesis survives

If

[
E[T_n]	o0
]

in (d=3,4), Markov's inequality would immediately give

[
P(T_n>0)le E[T_n]	o0.
]

Thus the size-two non-stable-module obstruction would vanish in probability.

That still would **not** prove

[
p_d^{m UPO}(n)	o1,
]

because larger non-stable modules and multiple nontrivial components could remain.

The correct next step would then be to bound those residual obstruction classes separately.

## 11. Nonclaims

This note does not claim:

- a proved twin-pair asymptotic;
- a value for the constants (A_d^{m bulk}) or (A_d^{m waist});
- that adjacent twins are the only UPO obstruction;
- that (p_3^{m UPO}) or (p_4^{m UPO}) tends to one;
- a physical law of time;
- a boundary-independent infinite-volume result.

The purpose of this note is to freeze a geometric exponent prediction before the next numerical test.
