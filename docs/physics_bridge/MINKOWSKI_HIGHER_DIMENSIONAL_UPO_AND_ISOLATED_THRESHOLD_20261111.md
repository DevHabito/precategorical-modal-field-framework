# Higher-dimensional Minkowski orientation recovery and the isolated-vertex threshold

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact classifier regression + reproducible Monte Carlo pilot + analytic isolated-vertex asymptotic  
**Physical status:** causal-set-inspired reconstruction benchmark; not an empirical time-emergence result  
**Novelty status:** no exact prior statement of the isolated-vertex asymptotic below was located in the targeted review. Absolute novelty and priority are not certified.

## 1. Question

The (1+1)-dimensional random-(2)-order benchmark is now analytically closed:

[
p_2(n)
=
Pr(
	ext{unoriented comparability determines the order up to duality}
)
longrightarrow
rac{1}{e}.
]

That proof relies on the special permutation representation of (1+1) Minkowski sprinklings.

The next question is whether orientation recoverability survives in genuine higher-dimensional sprinklings, where no single relative permutation describes the causal order.

For spacetime dimension (d), let (C_{d,n}) be (n) iid uniform points in a flat Alexandrov interval, equivalently a Poisson sprinkling conditioned on cardinality (n).

Erase the causal arrows and retain only

[
xsim y
iff
xprec y
 	ext{or}yprec x.
]

Let (G(C_{d,n})) be the resulting comparability graph.

Define

[
p_d^{mathrm{UPO}}(n)
=
Pr(
G(C_{d,n})
	ext{ is nontrivial UPO}
).
]

This is the direct higher-dimensional analogue of the (1+1) recovery problem.

## 2. Important distinction: logical recovery versus connected causal support

Isolated vertices contain no comparability edges.

They therefore introduce no additional orientation choice.

A graph with one nontrivial UPO component and any number of isolated vertices still reconstructs the complete partial order up to global reversal.

Accordingly,

[
p_d^{mathrm{UPO}}(n)
]

is the correct logical recovery probability.

A second diagnostic is useful but must not be confused with it:

[
p_d^{mathrm{conn}}(n)
=
Pr(
G(C_{d,n})
	ext{ is connected and UPO}
).
]

This asks whether every sampled event belongs to the single causally connected recovery component.

It is a causal-support diagnostic, not a stricter definition of orientation recovery.

For UPO samples also define

[
alpha_d(n)
=
rac{
	ext{size of the unique nontrivial component}
}{n}.
]

## 3. Classifier independent of permutation structure

The higher-dimensional classifier uses classical implication/color classes of comparability graphs.

For every nonempty comparability graph, let

[
k_Gamma
]

be the number of inverse implication-class pairs.

Classical comparability theory gives

[
G	ext{ is UPO}
iff
k_Gamma(G)=1.
]

The implementation computes the forcing closure on undirected edges: two incident edges are joined in the forcing graph when their two non-shared endpoints are nonadjacent, i.e. when they form an induced (P_3).

The connected components of this forcing graph are the undirected color classes, equivalently the inverse-paired directed implication classes.

This avoids any use of the (1+1) permutation representation.

## 4. Exact regression before higher-dimensional use

The classifier was first applied to all relative permutations for

[
n=2,ldots,8.
]

It reproduced the exact nontrivial UPO counts already established independently in the repository:

[
oxed{
1, 4, 12, 38, 165, 1042, 8464.
}
]

Thus the higher-dimensional classifier passes an exact finite regression against the earlier modular/substitution pipeline.

A separate (1+1) sprinkling calibration at (n=7) used (50,000) samples and returned

[
hat p_2(7)=0.2062,
]

with Wilson 95% interval

[
[0.20268,0.20977].
]

The exact value

[
rac{1042}{7!}
=
0.206746ldots
]

lies inside that interval.

The same calibration produced ordering fraction

[
0.49991,
]

consistent with the exact (d=2) Myrheim-Meyer value (1/2).

## 5. Sprinkling construction

Use the Alexandrov interval between

[
p=(-1,0,ldots,0),
qquad
q=(1,0,ldots,0)
]

in flat (d)-dimensional Minkowski spacetime.

At coordinate time (t), the spatial section is a ((d-1))-ball of radius

[
1-|t|.
]

Uniform volume sampling therefore uses

[
|t|
=
1-U^{1/d},
]

with independent random sign, followed by a point uniform in the spatial ball of radius (1-|t|).

For two sampled events (x,y), a comparability edge is present exactly when

[
|t_x-t_y|^2
>
|mathbf x-mathbf y|^2.
]

Null equality has measure zero.

## 6. Ordering-fraction calibration

The Myrheim-Meyer ordering fraction for a flat (d)-dimensional Alexandrov interval is

[
r_d
=
rac{
Gamma(d+1)Gamma(d/2)
}{
2Gamma(3d/2)
}.
]

Therefore

[
r_2=rac12,
qquad
r_3approx0.22857,
qquad
r_4=0.1.
]

Across the pilot grid, the measured mean ordering fractions remained close to these values.

Representative values at (n=48) were

[
0.49842,quad
0.22733,quad
0.10052
]

for (d=2,3,4), respectively.

This is an ensemble-level calibration that the generator is sampling the intended Lorentzian causal geometry.

## 7. Monte Carlo pilot

The main reproducible grid used

[
nin
{7,9,11,16,24,32,48}.
]

The sample count was (5000) at the smaller sizes, reduced at the larger sizes for computational cost.

The mean isolated count includes every trial. A graph with no edges contributes
all of its vertices as isolates. The four small-size rows in each table were
regenerated from the original seeded pilot after finding that their published
sums omitted those contributions.

From the repository root, run
`python docs/physics_bridge/minkowski_higher_dimensional_upo_pilot.py --output pilot.json`.
For each dimension and sample size, the table's mean isolated count comes from
`runs[].mean_isolated_vertices`.

### 2+1 spacetime, (d=3)

| n | (p_3^{m UPO}) | (p_3^{m conn}) | mean (alpha_3midmathrm{UPO}) | mean isolated |
|---:|---:|---:|---:|---:|
|7|0.5872|0.0994|0.6795|2.1672|
|9|0.5566|0.1072|0.7571|2.1432|
|11|0.5628|0.1196|0.8172|2.0942|
|16|0.6210|0.1484|0.8912|1.8966|
|24|0.7017|0.1840|0.9346|1.6567|
|32|0.7553|0.2013|0.9535|1.5453|
|48|0.8027|0.2573|0.9721|1.3680|

An independent four-block replication gave

[
p_3^{m UPO}(48)=0.8160
]

from (2000) samples, Wilson 95% interval

[
[0.7984,0.8324].
]

At (n=64),

[
p_3^{m UPO}(64)=0.8492
]

from (1200) samples.

At (n=96),

[
p_3^{m UPO}(96)=0.8725
]

from (400) samples.

These are finite Monte Carlo observations only.

They do not establish

[
p_3^{m UPO}(n)	o1.
]

### 3+1 spacetime, (d=4)

| n | (p_4^{m UPO}) | (p_4^{m conn}) | mean (alpha_4midmathrm{UPO}) | mean isolated |
|---:|---:|---:|---:|---:|
|7|0.6366|0.0178|0.4930|4.2412|
|9|0.6720|0.0140|0.4967|4.8172|
|11|0.6618|0.0114|0.5310|5.2892|
|16|0.6288|0.0094|0.6375|6.1538|
|24|0.6777|0.0073|0.7416|6.7957|
|32|0.7087|0.0033|0.7892|7.3720|
|48|0.7893|0.0040|0.8486|7.5787|

The independent four-block replication gave

[
p_4^{m UPO}(48)=0.7775
]

from (2000) samples, Wilson 95% interval

[
[0.7587,0.7952].
]

At (n=64),

[
p_4^{m UPO}(64)=0.8208
]

from (1200) samples.

At (n=96),

[
p_4^{m UPO}(96)=0.8475
]

from (400) samples.

Again, no asymptotic recovery limit is inferred.

The striking separation is instead

[
p_4^{m UPO}
gg
p_4^{m conn}.
]

That separation is explained in part by boundary-induced isolated vertices.

## 8. Exact comparable-volume function for one event

Let

[
r=|mathbf x|.
]

For a point (x=(t,mathbf x)) in the diamond, every comparable point lies either in the interval (I(p,x)) or in (I(x,q)).

The volume of a flat Alexandrov interval scales as the (d)-th power of its proper time.

Therefore the fraction of the full diamond volume comparable to (x) is exactly

[
Q_d(x)
=
rac{
left((1+t)^2-r^2ight)^{d/2}
+
left((1-t)^2-r^2ight)^{d/2}
}{
2^d
}.
]

Conditioned on (x), the other (n-1) points are independent.

Hence the probability that (x) is isolated in the comparability graph is

[
(1-Q_d(x))^{n-1}.
]

If (I_n) is the number of isolated vertices,

[
oxed{
mathbb E[I_n]
=
n,
mathbb E[
(1-Q_d(X))^{n-1}
].
}
]

This identity is exact.

## 9. Coordinates adapted to the null waist

The minimum of (Q_d) occurs at the spatial waist of the diamond,

[
t=0,qquad r=1,
]

where both endpoint intervals become null.

Set

[
delta=1-r,
qquad
a=delta+t,
qquad
b=delta-t.
]

The diamond becomes

[
age0,
qquad
bge0,
qquad
a+ble2.
]

Also,

[
(1+t)^2-r^2
=
a(2-b),
]

and

[
(1-t)^2-r^2
=
b(2-a).
]

Thus

[
Q_d(a,b)
=
2^{-d}
left[
a(2-b)
ight]^{d/2}
+
2^{-d}
left[
b(2-a)
ight]^{d/2}.
]

The normalized volume measure is

[
dmu_d
=
rac{d(d-1)}4
left(
1-rac{a+b}{2}
ight)^{d-2}
da,db.
]

The coefficient follows from the spatial sphere/ball relation and the exact volume of the diamond.

## 10. Isolated-vertex asymptotic

Let

[
m=rac d2
]

and rescale

[
a=2n^{-2/d}x,
qquad
b=2n^{-2/d}y.
]

Then

[
nQ_d
=
x^m
left(
1-n^{-2/d}y
ight)^m
+
y^m
left(
1-n^{-2/d}x
ight)^m.
]

For fixed (x,y),

[
nQ_d
longrightarrow
x^m+y^m.
]

The volume Jacobian contributes

[
n^{-4/d},
]

while the outer factor in (mathbb E[I_n]) contributes (n).

The region away from the null waist has (Q_d) bounded away from zero and is exponentially suppressed.

A standard Laplace/dominated-convergence argument on the rescaled waist region therefore gives

[
rac{
mathbb E[I_n]
}{
n^{1-4/d}
}
longrightarrow
d(d-1)
int_0^infty!!
int_0^infty
e^{-(x^{d/2}+y^{d/2})}
dx,dy.
]

The integral factorizes:

[
int_0^infty
e^{-x^{d/2}}dx
=
Gammaleft(1+rac2dight).
]

Hence

[
oxed{
mathbb E[I_n]
sim
d(d-1)
Gammaleft(1+rac2dight)^2
n^{1-4/d}.
}
]

No fitted parameter enters this result.

## 11. Dimension threshold at the level of expectation

The asymptotic gives three qualitatively different regimes.

### (d<4)

[
mathbb E[I_n]	o0.
]

In particular,

[
d=2:
qquad
oxed{
mathbb E[I_n]simrac2n
}
]

and

[
d=3:
qquad
oxed{
mathbb E[I_n]
sim
6Gamma(5/3)^2
n^{-1/3}
}
]

with coefficient

[
6Gamma(5/3)^2
approx4.889694.
]

### (d=4)

The exponent vanishes:

[
1-rac44=0.
]

Therefore

[
oxed{
mathbb E[I_n]	o
12Gamma(3/2)^2
=
3pi
approx9.424778.
}
]

Thus (3+1) spacetime is the critical dimension for this isolated-vertex expectation in the declared finite-diamond ensemble.

### (d>4)

[
mathbb E[I_n]
]

grows sublinearly as

[
n^{1-4/d}.
]

This does not by itself prove that the probability of having at least one isolated vertex tends to one.

A distributional or second-moment analysis is required for that stronger statement.

## 12. Numerical check of the asymptotic

The prediction is already visible in the pilot.

### (d=2,n=48)

Analytic leading term:

[
rac2{48}
=
0.041667.
]

Measured mean:

[
0.041333.
]

### (d=3,n=48)

Analytic leading term:

[
4.889694,
48^{-1/3}
=
1.345451.
]

Measured mean:

[
1.368.
]

The independent four-block run gave

[
1.3415.
]

### (d=4)

The asymptotic limit is

[
3pi
=
9.424778.
]

Finite means increase toward this value:

[
7.58quad(n=48),
]

[
8.07quad(n=64),
]

[
8.42quad(n=96)
]

in the reported runs.

The (d=4) approach is visibly slower, as expected from a constant-limit boundary layer rather than a decaying isolated count.

## 13. Consequence for interpreting connected-UPO

The very small (p_4^{m conn}) values must not be interpreted as failure of orientation recoverability.

The correct logical UPO probability remains high in the finite pilot.

The small connected probability is strongly affected by the geometric population of isolated vertices near the null waist.

At the same time, the isolated fraction is sublinear:

[
rac{
mathbb E[I_n]
}{n}
sim
d(d-1)
Gammaleft(1+rac2dight)^2
n^{-4/d}
	o0
]

for every finite (d).

Thus a nonzero or growing number of isolated events can coexist with a vanishing isolated fraction.

This is consistent with the observed increase of

[
alpha_d(n)
]

toward one among UPO samples.

## 14. What remains genuinely open

The isolated-vertex asymptotic does **not** answer the main higher-dimensional UPO question.

The central unknowns are still

[
lim_{n	oinfty}
p_3^{m UPO}(n)
]

and

[
lim_{n	oinfty}
p_4^{m UPO}(n),
]

including whether these limits exist.

The finite data suggest that both probabilities may become large.

That is a hypothesis-generating observation only.

The next structural target is to measure the obstruction conditional on

[
k_Gamma>1:
]

1. distribution of (k_Gamma);
2. size and geometry of non-stable modules;
3. whether bad modules concentrate near the null boundary or in the bulk;
4. whether the probability of (k_Gamma>1) can be bounded analytically;
5. whether the higher-dimensional limit is controlled by a prime/modular phenomenon analogous to the simple-permutation mechanism in (1+1).

## 15. Literature boundary

The ingredients used here are classical or established:

- **Myrheim (1978)** and **Meyer (1988/1989)**: ordering fraction and dimension estimation in Minkowski causal sets.
- **Bombelli, Lee, Meyer, and Sorkin (1987)**: causal-set kinematics.
- **Golumbic** and classical comparability-graph theory: transitive orientations and implication classes.
- **Möhring (1984)**: almost all comparability graphs are UPO under the uniform comparability-graph counting measure.
- **Surya (2019)**, *The causal set approach to quantum gravity*, Living Reviews in Relativity 22, 5: modern review of sprinklings, ordering fractions, dimension estimators, and reconstruction.
- **Carlip (2024)**, *Causal sets and an emerging continuum*, General Relativity and Gravitation 56, 95: modern account of the continuum-reconstruction problem and remaining manifoldlikeness difficulties.

Möhring's asymptotic does not settle the present problem because the measure here is not uniform over comparability graphs.

It is the geometry-induced measure obtained from Minkowski sprinklings.

A targeted search did not locate the exact expectation law

[
d(d-1)
Gamma(1+2/d)^2
n^{1-4/d}
]

for isolated vertices of this comparability graph ensemble.

This is limited negative evidence only.

No absolute novelty or priority claim is made.

## 16. Boundary and finite-window caution

All present calculations concern a fixed finite Alexandrov interval conditioned on cardinality (n).

The null-waist boundary is therefore part of the declared ensemble, not an accidental numerical artifact.

Recent work on sampling biases in sprinkled causal sets has emphasized that finite-region choices can matter strongly for some observables, especially link-based ones.

The present observable is not a link statistic, but the same general warning applies:

> do not silently reinterpret a finite-diamond result as a boundary-free infinite-volume statement.

A different window or boundary prescription must be tested separately.

## 17. Current conclusion

The move from (1+1) to higher-dimensional Minkowski sprinklings produced two distinct findings.

First, the finite Monte Carlo evidence shows that exact UPO recovery does not immediately disappear in (2+1) or (3+1).

Second, the apparent connectedness failure in (3+1) has an analytically identifiable geometric contribution.

For isolated vertices,

[
oxed{
mathbb E[I_n]
sim
d(d-1)
Gammaleft(1+rac2dight)^2
n^{1-4/d}.
}
]

In (3+1),

[
oxed{
mathbb E[I_n]	o3pi.
}
]

This is not a theorem about emergent time.

It is a precise statement about how much of a finite Lorentzian sprinkling can remain completely incomparable after arrow erasure, and it separates that boundary phenomenon from the genuinely open UPO-orientation question.

The next frontier is therefore sharper than before:

> after removing the now-understood isolated-vertex boundary contribution, do nontrivial orientation ambiguities themselves become rare in (2+1) and (3+1) Minkowski sprinklings?

That is the next problem to attack.
