# Exact disagreement geometry for comparable-twin obstructions

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact geometric identity + Monte Carlo small-disagreement pilot  
**Physical status:** causal-set reconstruction analysis in a fixed flat Alexandrov interval  
**Novelty status:** no absolute novelty or priority claim is made

## 1. Purpose

The previous audit reduced the dominant finite higher-dimensional UPO obstruction to a simple object: a comparable twin pair.

For two comparable events (x,y), define

[
A_x={z:zsim x},
qquad
A_y={z:zsim y},
]

and the normalized disagreement volume

[
Delta(x,y)=mu(A_x	riangle A_y).
]

A pair can be comparable twins in an (n)-point sprinkling only when every remaining sampled event avoids the symmetric-difference region.

The exact expectation is

[
mathbb E[T_n]
=
inom n2
mathbb Eleft[
mathbf 1_{{Xsim Y}}
(1-Delta(X,Y))^{n-2}
ight].
]

The central analytic question is therefore the small-(Delta) geometry.

## 2. Exact closed form for comparable pairs

Let the full Alexandrov interval be

[
D=I(p,q),
]

with

[
p=(-1,mathbf0),
qquad
q=(1,mathbf0).
]

Assume

[
xprec y.
]

Write (I(a,b)) for the Alexandrov interval between causally related events (aprec b).

Because (xprec y),

[
A_xcap A_y
=
I(p,x)
;dotcup;
I(x,y)
;dotcup;
I(y,q),
]

up to measure-zero boundaries.

The three pieces are disjoint in their interiors.

Also,

[
mu(A_x)
=
mu(I(p,x))+mu(I(x,q)),
]

and

[
mu(A_y)
=
mu(I(p,y))+mu(I(y,q)).
]

Therefore

[
Delta(x,y)
=
mu(A_x)+mu(A_y)-2mu(A_xcap A_y).
]

In flat (d)-dimensional Minkowski spacetime, Alexandrov volume is proportional to the (d)-th power of proper time.

Since the full interval has proper time (2), normalized interval volume is

[
mu(I(a,b))
=
rac{	au(a,b)^d}{2^d}.
]

Hence:

[
oxed{
Delta(x,y)
=
rac{
	au(p,y)^d
-
	au(p,x)^d
+
	au(x,q)^d
-
	au(y,q)^d
-
2	au(x,y)^d
}{2^d}
}
]

for every comparable pair (xprec y).

Here

[
	au(a,b)^2
=
(t_b-t_a)^2
-
|mathbf x_b-mathbf x_a|^2.
]

No Monte Carlo approximation enters this identity.

## 3. Direct numerical validation

The closed form was checked against independent Monte Carlo estimation of

[
mu(A_x	riangle A_y)
]

for random comparable pairs in (d=3) and (d=4).

For each test pair, (10^5) fresh uniform points were sampled from the diamond and classified according to whether they belonged to exactly one of (A_x,A_y).

Representative checks were:

### (d=3)

| closed form | direct Monte Carlo |
|---:|---:|
|0.31564|0.31307|
|0.58992|0.58837|
|0.27150|0.26924|

### (d=4)

| closed form | direct Monte Carlo |
|---:|---:|
|0.16087|0.16186|
|0.13868|0.13983|
|0.19507|0.19500|

The deviations are consistent with ordinary finite-sample error.

This is a validation of the implementation, not a proof; the proof is the interval-volume decomposition above.

## 4. Small-disagreement distribution

Define

[
F_d(arepsilon)
=
mu^{otimes2}
left{
(x,y):
xsim y, 
Delta(x,y)learepsilon
ight}.
]

A dedicated pair-sampling code was added as

[
	exttt{tools/minkowski_twin_delta_geometry.py}.
]

A pilot with millions of iid pairs was used only to identify the likely asymptotic regime.

For (3	imes10^6) pairs per dimension, the empirical values were:

### (d=3)

| (arepsilon) | (F_3(arepsilon)) |
|---:|---:|
|0.015|(1.73	imes10^{-5})|
|0.020|(3.77	imes10^{-5})|
|0.030|(1.12	imes10^{-4})|
|0.040|(2.40	imes10^{-4})|
|0.050|(4.46	imes10^{-4})|
|0.070|(1.149	imes10^{-3})|
|0.100|(2.982	imes10^{-3})|
|0.150|(8.363	imes10^{-3})|

A simple log-log fit over this finite window gave an effective slope of approximately

[
2.70.
]

### (d=4)

| (arepsilon) | (F_4(arepsilon)) |
|---:|---:|
|0.015|(1.70	imes10^{-5})|
|0.020|(4.10	imes10^{-5})|
|0.030|(1.31	imes10^{-4})|
|0.040|(2.88	imes10^{-4})|
|0.050|(5.47	imes10^{-4})|
|0.070|(1.348	imes10^{-3})|
|0.100|(3.364	imes10^{-3})|
|0.150|(9.163	imes10^{-3})|

The corresponding finite-window effective slope was approximately

[
2.73.
]

These values are exploratory.

They do not establish a power law and should not be extrapolated directly to (arepsilon	o0).

## 5. Bulk versus null-waist split

The most informative diagnostic was to condition on the endpoint comparable-volume score

[
Q_{m pair}
=
rac{Q_d(x)+Q_d(y)}2.
]

In (d=4), the fitted exponent changes sharply when the low-(Q) region is removed.

Using (4	imes10^6) sampled pairs and the finite range

[
arepsilonin{0.02,0.03,0.04,0.05,0.07,0.10},
]

the effective slopes were approximately:

| cut | effective log-log slope |
|---|---:|
|(Q_{m pair}ge0)|2.78|
|(Q_{m pair}ge0.03)|3.81|
|(Q_{m pair}ge0.06)|4.40|
|(Q_{m pair}ge0.10)|4.00|

The estimates become noisy for strong cuts because the small-(Delta) sample becomes sparse.

Nevertheless the pattern is structurally suggestive.

In the (d=4) bulk, the exponent is compatible with ordinary four-dimensional local closeness.

When the null-waist region is restored, a lower-exponent population dominates the small-(Delta) tail.

For (d=3), the corresponding slopes remain near the high-(2) range under the same cuts, which is compatible with the fact that bulk dimension (d=3) and a possible boundary-controlled exponent near (3) are not cleanly separated.

## 6. Working hypothesis

The current evidence motivates, but does not prove, the following hypothesis.

### Bulk hypothesis

For pairs confined away from the null waist,

[
F_d^{m bulk}(arepsilon)
]

should scale with the ordinary local dimension,

[
F_d^{m bulk}(arepsilon)
sim
C_d^{m bulk}arepsilon^d.
]

This is geometrically plausible because making two generic interior comparability neighborhoods nearly equal requires the pair to become locally close in (d) spacetime coordinates.

### Boundary hypothesis

In the fixed Alexandrov-diamond ensemble, a second family of low-disagreement pairs lives near the null waist.

For (d=4), this population appears to dominate the full small-(Delta) tail and reduce the observed effective exponent from near (4) toward a value near (3).

A natural conjecture is therefore

[
F_4(arepsilon)
asymp
C_4arepsilon^3
]

for the full finite-diamond measure.

The present data are not sufficient to certify the exponent (3).

The conjecture is recorded only because it gives a precise analytic target.

## 7. Consequence if a small-(arepsilon) law is proved

Suppose one proves

[
F_d(arepsilon)
sim
C_darepsilon^{eta_d}
]

with

[
eta_d>2.
]

Then the exact twin expectation becomes a Laplace-Stieltjes asymptotic:

[
mathbb E[T_n]
=
inom n2
int_0^1
(1-delta)^{n-2},dF_d(delta).
]

Under the usual regularity needed for the asymptotic transfer,

[
mathbb E[T_n]
sim
rac{C_dGamma(eta_d+1)}2
n^{2-eta_d}.
]

Thus:

- if (eta_d>2), the expected comparable-twin count tends to zero;
- if (eta_d=3), then
  [
  mathbb E[T_n]=O(n^{-1});
  ]
- if the bulk exponent is (d), then the bulk contribution alone is
  [
  O(n^{2-d}).
  ]

This still would not prove UPO recovery tends to one, because larger non-stable modules must be controlled separately.

## 8. Why this matters for the physical bridge

The higher-dimensional obstruction is becoming geometrically interpretable.

The finite simulations no longer suggest a generic, volume-filling loss of orientation information.

Instead they suggest:

1. most late finite failures are minimal modular defects;
2. those defects are strongly associated with low-comparability regions;
3. in (3+1), the null-waist boundary appears to alter the small-disagreement scaling;
4. the bulk may obey the naive spacetime-dimensional scaling while the boundary controls the actual finite-window asymptotic.

This distinction is important because recent work has independently emphasized that finite-region sprinkling observables can acquire strong boundary biases.

That literature concerns links rather than the present comparability-neighborhood statistic, so it cannot be imported as a result here.

It does, however, reinforce the need to keep the finite Alexandrov-window ensemble explicit.

## 9. Literature boundary

Relevant established ingredients include:

- S. Surya, **The causal set approach to quantum gravity**, *Living Reviews in Relativity* 22, 5 (2019), DOI 10.1007/s41114-019-0023-1.
- C. J. Fewster, E. Hawkins, C. Minz, and K. Rejzner, **Local structure of sprinkled causal sets**, *Physical Review D* 103, 086020 (2021), DOI 10.1103/PhysRevD.103.086020.
- M. Boguñá and D. Krioukov, **Sampling biases in sprinkled causal sets**, arXiv:2610.03247 (2026).
- R. H. Möhring, **Almost all comparability graphs are UPO**, *Discrete Mathematics* 50 (1984), 63–70, DOI 10.1016/0012-365X(84)90035-9.
- R. M. McConnell and J. P. Spinrad, **Modular decomposition and transitive orientation**, *Discrete Mathematics* 201 (1999), 189–241, DOI 10.1016/S0012-365X(98)00319-7.

No source located in the targeted review gives the closed (Delta(x,y)) formula specifically as a comparable-twin obstruction observable or analyzes its small-(Delta) distribution for UPO recovery in Minkowski sprinklings.

This is limited negative evidence only.

## 10. Next analytic step

The next task is no longer to increase Monte Carlo size indiscriminately.

It is to derive the local expansion of

[
Delta(x,y)
]

in coordinates adapted to the null waist.

The key questions are:

1. which scalings of the two endpoint depths and relative angle make (Delta=O(arepsilon));
2. what volume element those scalings induce;
3. whether the resulting boundary contribution is rigorously (O(arepsilon^3)) in (d=4);
4. whether the bulk contribution is (O(arepsilon^d));
5. which contribution dominates for general spacetime dimension.

If those bounds can be proved, the comparable-twin asymptotic will follow from the exact expectation identity without any brute-force orientation enumeration.
