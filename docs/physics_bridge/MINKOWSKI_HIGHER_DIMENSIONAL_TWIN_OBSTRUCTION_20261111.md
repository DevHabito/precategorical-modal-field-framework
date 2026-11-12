# Higher-dimensional UPO obstruction audit — comparable twins and boundary localization

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact classifier regression + reproducible Monte Carlo obstruction audit + exact twin-pair expectation identity  
**Physical status:** causal-set-inspired reconstruction benchmark; not an empirical time-emergence result  
**Novelty status:** no priority claim is made. The graph-theoretic ingredients are classical; the higher-dimensional statistics below are project computations.

## 1. Why this audit was needed

The previous higher-dimensional Minkowski study established two facts.

1. UPO recoverability survives at appreciable finite probability in sprinklings into (2+1) and (3+1) dimensional Minkowski Alexandrov intervals.
2. Isolated vertices have a separate boundary-controlled asymptotic,
   [
   mathbb E[I_n]
   sim
   d(d-1)Gamma!left(1+rac2dight)^2 n^{1-4/d}.
   ]

That calculation explains part of the gap between connected-UPO and logical UPO recovery, but it does not explain the remaining failures.

The present audit asks a narrower question:

> When a higher-dimensional sprinkling is not UPO after causal arrows are erased, what is the smallest structural obstruction that remains?

The first candidate is the size-two non-stable module: a comparable twin pair.

## 2. Comparable twins

Let (G) be the unoriented comparability graph of a finite causal set.

Two distinct vertices (x,y) are **comparable twins** when

1. (x) and (y) are adjacent in (G); and
2. every vertex outside ({x,y}) is adjacent either to both or to neither.

Equivalently,
[
N(x)setminus{y}
=
N(y)setminus{x}.
]

Then ({x,y}) is a non-stable graph module.

By the classical UPO characterization, a connected comparability graph containing such a module is not uniquely partially orderable.

Thus a comparable twin pair is a minimal certificate of orientation ambiguity.

## 3. Independent classifier regression

The higher-dimensional code does not use the special permutation representation of (1+1).

It computes the Gallai forcing/color classes of the comparability graph.

For a nonempty comparability graph,
[
G	ext{ is UPO}
iff
k_Gamma(G)=1,
]
where (k_Gamma) is the number of undirected color classes, equivalently inverse-paired directed implication classes.

Before using this classifier on sprinklings, it was tested on every relative permutation through (n=7).

The exact UPO counts were reproduced:

[
oxed{
1, 4, 12, 38, 165, 1042
}
]
for
[
n=2,ldots,7.
]

This matches the earlier direct-orientation and modular/substitution calculations in the repository.

The reproducible implementation is:

[
	exttt{tools/minkowski_upo_obstruction_audit.py}.
]

## 4. Sprinkling calibration

For spacetime dimension (d), the generator samples uniformly from the Alexandrov interval
[
I((-1,mathbf0),(1,mathbf0)).
]

The expected Myrheim-Meyer ordering fraction is
[
r_d
=
rac{Gamma(d+1)Gamma(d/2)}
{2Gamma(3d/2)}.
]

Hence
[
r_3=rac{8}{35}approx0.228571,
qquad
r_4=0.1.
]

The Monte Carlo ordering fractions below remain close to these values, providing an ensemble-level check of the sprinkling generator.

## 5. Reproducible obstruction grid

Each cell used the deterministic seed
[
20261113+1000003,d+1009,n.
]

For (nle48), 2000 independent sprinklings were used per cell.
For (n=64), 1000 were used.
For (n=96), 600 were used.

### (2+1) spacetime: (d=3)

| (n) | UPO fraction | non-UPO nonempty | failures with comparable twin | mean twin pairs | mean ordering fraction | mean (Q_d) on twin endpoints |
|---:|---:|---:|---:|---:|---:|---:|
|7|0.5885|0.3645|0.8066|0.4120|0.22660|0.24204|
|16|0.6500|0.3500|0.8186|0.3590|0.23235|0.19493|
|32|0.7630|0.2370|0.9198|0.2575|0.22731|0.16129|
|48|0.8115|0.1885|0.9390|0.2015|0.22761|0.15950|
|64|0.8130|0.1870|0.9572|0.1990|0.22752|0.14400|
|96|0.8533|0.1467|1.0000|0.1600|0.22736|0.14298|

The value (1.0000) at (n=96) means that every non-UPO sample in this finite run contained at least one comparable twin. It is not a theorem that all failures have this form.

### (3+1) spacetime: (d=4)

| (n) | UPO fraction | non-UPO nonempty | failures with comparable twin | mean twin pairs | mean ordering fraction | mean (Q_d) on twin endpoints |
|---:|---:|---:|---:|---:|---:|---:|
|7|0.6200|0.1180|0.9449|0.1670|0.09790|0.13762|
|16|0.6225|0.3720|0.8306|0.4060|0.09925|0.09098|
|32|0.7390|0.2610|0.8544|0.2720|0.10060|0.06097|
|48|0.7885|0.2115|0.9314|0.2300|0.09937|0.05193|
|64|0.8110|0.1890|0.9577|0.2050|0.10079|0.04264|
|96|0.8650|0.1350|1.0000|0.1450|0.10022|0.02892|

Again, the (n=96) twin fraction is a finite-sample observation.

## 6. Implication-class collapse

The same runs record the distribution of (k_Gamma).

At large (n), most failures have only one additional orientation class.

For (d=3,n=96):
[
P(k_Gamma=1)=0.8533,
]
[
P(k_Gamma=2)=0.1350,
]
[
P(k_Gammage3)=0.0117.
]

For (d=4,n=96):
[
P(k_Gamma=1)=0.8650,
]
[
P(k_Gamma=2)=0.1250,
]
[
P(k_Gammage3)=0.0100.
]

Thus the observed non-UPO population is not becoming more combinatorially complicated with (n).

In this finite range it is becoming concentrated near the smallest possible excess over UPO:
[
k_Gamma=2.
]

This is a statistical observation, not an asymptotic proof.

## 7. Geometric localization diagnostic

For a point (x=(t,mathbf x)), let
[
Q_d(x)
]
be the exact fraction of the full Alexandrov diamond comparable to (x):
[
Q_d(x)
=
rac{
left((1+t)^2-|mathbf x|^2ight)^{d/2}
+
left((1-t)^2-|mathbf x|^2ight)^{d/2}
}{2^d}.
]

Small (Q_d) means that the event lies in a geometrically weakly comparable region, approaching zero at the null waist.

The twin-endpoint means decrease with (n).

In (d=4):
[
0.1376, 0.0910, 0.0610, 0.0519, 0.0426, 0.0289
]
for
[
n=7,16,32,48,64,96.
]

The unconditional mean of (Q_d(X)) is the pair ordering fraction, approximately
[
0.1
]
in (d=4).

Therefore, by (n=32) and beyond, comparable twins are strongly biased toward the low-(Q_d) region relative to a uniformly selected event.

In (d=3), the same tendency is present but weaker: the twin-endpoint mean falls below the bulk mean
[
r_3approx0.22857
]
and reaches approximately
[
0.143
]
at (n=96).

This supports, but does not prove, the working hypothesis that surviving orientation obstructions concentrate near the null-waist boundary layer.

## 8. Exact expectation identity for comparable twin pairs

The twin statistic admits an exact geometric representation.

Let ((D,mu)) be the normalized Alexandrov diamond.

For (xin D), define its symmetric comparability region
[
A_x
=
{zin D: zsim x}.
]

For a pair (x,y), define the disagreement volume
[
Delta(x,y)
=
mu(A_x	riangle A_y),
]
where (	riangle) is symmetric difference.

Let (T_n) be the number of comparable twin pairs in an iid size-(n) sprinkling.

Then

[
oxed{
mathbb E[T_n]
=
inom n2
int_D!!int_D
mathbf 1_{{xsim y}}
left(1-Delta(x,y)ight)^{n-2}
,dmu(x),dmu(y).
}
]

Equivalently,
[
oxed{
mathbb E[T_n]
=
inom n2
mathbb E!left[
mathbf 1_{{Xsim Y}}
left(1-Delta(X,Y)ight)^{n-2}
ight].
}
]

### Proof

Fix two sampled events (X_i=x) and (X_j=y).

They are comparable twins exactly when

1. (xsim y); and
2. every remaining sampled point lies outside
   [
   A_x	riangle A_y.
   ]

Conditioned on (x,y), the remaining (n-2) points are independent and uniform in (D).

Therefore the conditional probability is
[
mathbf 1_{{xsim y}}
left(1-Delta(x,y)ight)^{n-2}.
]

Summing the pair indicators over the (inom n2) unordered pairs and taking expectation gives the formula.

No approximation is used.

## 9. What the identity changes

The comparable-twin question is no longer fundamentally a graph-enumeration problem.

Its asymptotic is controlled by the small-(Delta) geometry of pairs:
[
Delta(x,y)ll1.
]

The next analytic target is therefore:

> characterize the measure of comparable pairs whose comparability neighborhoods have symmetric-difference volume at most (arepsilon).

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

If the small-(arepsilon) behavior of (F_d) can be obtained,
[
F_d(arepsilon)
sim C_darepsilon^{eta_d}
]
or bounded sharply enough, then the exact integral for (mathbb E[T_n]) becomes a Laplace/Tauberian asymptotic problem.

This is the cleanest route presently visible from finite computation toward a theorem.

## 10. What is not established

The present audit does **not** establish

[
p_3^{mathrm{UPO}}(n)	o1
]
or
[
p_4^{mathrm{UPO}}(n)	o1.
]

It also does not establish that comparable twins are the only asymptotically relevant obstruction.

In particular:

- a non-stable module can have size greater than two;
- several implication classes can exist without an adjacent twin pair;
- finite samples at (n=96) cannot certify extinction of those mechanisms;
- a boundary-localized observation in a finite Alexandrov interval must not be silently reinterpreted as a boundary-free infinite-volume result.

What the audit does establish is narrower:

1. the UPO classifier passes the exact (1+1) regression;
2. higher-dimensional UPO fractions remain large and rise over the larger tested sizes;
3. the observed failures increasingly contain minimal size-two modular obstructions;
4. those twin obstructions move toward lower-(Q_d) regions as (n) grows;
5. the expected twin count has an exact continuum integral representation.

## 11. Literature boundary

The graph-theoretic ingredients are classical.

- R. H. Möhring, **Almost all comparability graphs are UPO**, *Discrete Mathematics* 50 (1984), 63–70. DOI: 10.1016/0012-365X(84)90035-9.
- R. M. McConnell and J. P. Spinrad, **Modular decomposition and transitive orientation**, *Discrete Mathematics* 201 (1999), 189–241. DOI: 10.1016/S0012-365X(98)00319-7.
- Classical work of Gallai underlies implication classes and modular decomposition.

For causal sets and Minkowski sprinklings:

- S. Surya, **The causal set approach to quantum gravity**, *Living Reviews in Relativity* 22, 5 (2019). DOI: 10.1007/s41114-019-0023-1.
- C. J. Fewster, E. Hawkins, C. Minz, and K. Rejzner, **Local structure of sprinkled causal sets**, *Physical Review D* 103, 086020 (2021). DOI: 10.1103/PhysRevD.103.086020.
- M. Boguñá and D. Krioukov, **Sampling biases in sprinkled causal sets**, arXiv:2610.03247 (2026), is relevant to finite-region boundary cautions, although its central observable is link-based rather than the present comparability-module statistic.

No source located in the targeted review states the higher-dimensional UPO/twin statistics or the exact (T_n) expectation identity in this causal-set reconstruction context.

This is limited negative evidence only.

## 12. Next rigorous target

The next mathematical object is

[
oxed{
F_d(arepsilon)
=
mu^{otimes2}
{(x,y):xsim y, Delta(x,y)learepsilon}.
}
]

The immediate tasks are:

1. derive or bound (Delta(x,y)) in coordinates adapted to the null waist;
2. identify which pair configurations make (Delta	o0);
3. determine the small-(arepsilon) exponent of (F_d);
4. insert that result into the exact expectation integral for (T_n);
5. only then ask whether the size-two obstruction probability vanishes;
6. separately control larger non-stable modules before making any claim about
   [
   p_d^{mathrm{UPO}}(n).
   ]

That is the current frontier.
