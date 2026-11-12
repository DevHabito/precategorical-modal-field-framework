# Held-out adjacent-twin scaling test in higher-dimensional Minkowski sprinklings

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** prospective finite scaling-consistency pass retained as a pre-proof audit; the (d=4) asymptotic has since been proved  
**Preregistration:** commit `01d38cafb959ab395c2c1666ad9be143335e2a5f`  
**Claim level:** finite prospective evidence only; no asymptotic theorem

## 1. Frozen prediction

Before the held-out sizes were inspected, the repository froze the geometric scaling hypothesis

[
mathbb E[T_n]
=
Theta(n^{-1})
]

for adjacent-twin pairs in both

[
d=3
]

and

[
d=4
]

spacetime dimensions.

Here (T_n) is the number of adjacent twin pairs in the unoriented causal comparability graph of (n) iid points in a flat Alexandrov interval.

The two dimensions were predicted to share the same exponent for different geometric reasons:

- (d=3): bulk near-coincidence should dominate;
- (d=4): the null-waist boundary layer should dominate.

No asymptotic constant was frozen.

The held-out sizes were

[
n=320,qquad n=384.
]

The primary diagnostic was

[
n,widehat{mathbb E[T_n]}.
]

## 2. Detector regression

The held-out implementation counts adjacent twins by grouping identical closed-neighborhood rows.

For adjacent vertices (u,v),

[
N[u]=N[v]
]

is equivalent to equality of their external open neighborhoods.

Before the held-out runs, this vectorized criterion was checked against the literal definition:

1. require (usim v);
2. for every third vertex (w), require
   [
   wsim u
   iff
   wsim v.
   ]

The comparison covered

[
1200
]

independent small sprinklings across

[
d=2,3,4
]

and sizes

[
n=7,11,17,23.
]

Every count agreed exactly.

[
oxed{	ext{DETECTOR REGRESSION: PASS}}
]

## 3. Held-out protocol

Each target used

[
2500
]

independent conditioned sprinklings.

Frozen seeds:

| (d) | (n) | seed |
|---:|---:|---:|
|3|320|202611113320|
|3|384|202611113384|
|4|320|202611114320|
|4|384|202611114384|

The four runs were not used to construct or alter the exponent hypothesis.

## 4. Results

### (d=3)

At

[
n=320,
]

the run found

[
118
]

twin pairs in (2500) samples:

[
widehat{mathbb E[T_{320}]}
=
0.0472.
]

Hence

[
oxed{
320,
widehat{mathbb E[T_{320}]}
=
15.104.
}
]

The estimated probability of at least one twin pair was

[
0.0452,
]

with Wilson 95% interval

[
[0.03773,0.05406].
]

At

[
n=384,
]

the run found

[
108
]

twin pairs:

[
widehat{mathbb E[T_{384}]}
=
0.0432,
]

and therefore

[
oxed{
384,
widehat{mathbb E[T_{384}]}
=
16.5888.
}
]

The estimated probability of at least one twin pair was

[
0.0424,
]

with Wilson 95% interval

[
[0.03518,0.05103].
]

### (d=4)

At

[
n=320,
]

the run found

[
128
]

twin pairs:

[
widehat{mathbb E[T_{320}]}
=
0.0512,
]

so

[
oxed{
320,
widehat{mathbb E[T_{320}]}
=
16.384.
}
]

The estimated probability of at least one twin pair was

[
0.0488,
]

with Wilson 95% interval

[
[0.04102,0.05796].
]

At

[
n=384,
]

the run found

[
117
]

twin pairs:

[
widehat{mathbb E[T_{384}]}
=
0.0468,
]

giving

[
oxed{
384,
widehat{mathbb E[T_{384}]}
=
17.9712.
}
]

The estimated probability of at least one twin pair was

[
0.0460,
]

with Wilson 95% interval

[
[0.03846,0.05493].
]

## 5. Prospective assessment

The preregistered exponent survives this test at the level the protocol was designed to examine.

For both dimensions:

1. the raw mean twin count decreases from (n=320) to (n=384);
2. (n,widehat{mathbb E[T_n]}) remains of order one;
3. the held-out products remain in the same broad finite range already seen before the holdout;
4. no power-law blow-up or collapse is visible.

Accordingly,

[
oxed{
	ext{PROSPECTIVE SCALING-CONSISTENCY PASS}
}
]

is the appropriate status.

This wording is deliberately weaker than

[
mathbb E[T_n]sim C/n.
]

The test does not determine (C), and four finite Monte Carlo blocks cannot prove the asymptotic.

## 6. Why this matters for UPO recovery

An adjacent twin pair is a non-stable module of size two.

Therefore

[
T_n>0
]

is a sufficient obstruction to UPO.

If a future proof establishes

[
mathbb E[T_n]
=
O(n^{-1}),
]

then Markov's inequality gives

[
Pr(T_n>0)
le
mathbb E[T_n]
=
O(n^{-1}),
]

so the size-two modular obstruction vanishes in probability.

The finite simulations are consistent with exactly this scenario.

They do not prove it.

## 7. What remains after twins are removed

Even if

[
Pr(T_n>0)	o0,
]

UPO failure can still come from:

- non-stable modules of size at least three;
- more than one nontrivial connected component;
- other modular-decomposition structures that create more than one implication class.

Therefore the next quantity should not be another twin statistic.

The correct residual failure probability is

[
oxed{
q_d^{mathrm{res}}(n)
=
Pr(
k_Gamma>1
 	ext{and}T_n=0
).
}
]

It should then be decomposed into

[
q_d^{mathrm{res}}
=
q_d^{mathrm{multi}}
+
q_d^{mathrm{module}ge3}
]

with disjoint definitions.

If both residual terms vanish and the twin bound is proved, then one could begin to justify the conjecture

[
p_d^{mathrm{UPO}}(n)	o1
]

for the relevant dimension.

The repository does not make that conjecture a theorem.

## 8. Current scientific boundary

The present evidence supports a narrow statement:

> the dominant finite size-two ambiguity seen in the higher-dimensional pilot is becoming rare, and the first held-out scaling test is consistent with the preregistered (1/n) law.

It does not support:

- a proof of the (1/n) law;
- a value for its constant;
- a proof that all modular obstructions vanish;
- a proof that (p_3^{mathrm{UPO}}) or (p_4^{mathrm{UPO}}) tends to one;
- a preferred future direction;
- emergence of physical duration;
- a boundary-independent infinite-volume statement.

## 9. Next rigorous target

There are now two nonredundant mathematical obligations.

First, turn the geometric exponent argument into a controlled asymptotic bound for

[
mathbb E[T_n].
]

Second, independently measure and classify

[
q_d^{mathrm{res}}(n)
]

after conditioning on

[
T_n=0.
]

The first asks whether the observed (1/n) scale can be proved.

The second asks whether adjacent twins are only the leading obstruction or whether a different obstruction becomes dominant after they disappear.

Those two questions are the next bridge from the finite simulations to an actual higher-dimensional theorem.
