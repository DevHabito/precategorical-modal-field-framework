# Residual orientation ambiguity after removing adjacent twins

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exploratory higher-dimensional obstruction audit  
**Claim level:** finite computational evidence; no asymptotic law inferred

## 1. Question

The higher-dimensional Minkowski pilot found that adjacent twin pairs account for most observed failures of unique partial orderability.

An adjacent twin pair is a non-stable module of size two, so it is a sufficient UPO obstruction.

The preregistered held-out test is consistent with

[
mathbb E[T_n]=Theta(n^{-1})
]

for both (d=3) and (d=4), although that scaling is not yet proved.

The next question is therefore:

> when a non-UPO sprinkling contains no adjacent twin pair, what obstruction remains?

Define

[
q_d^{m res}(n)
=
Pr(
k_Gamma>1
 	ext{and}T_n=0
).
]

The audit splits this residual into two disjoint classes:

1. at least two connected components contain edges;
2. exactly one nontrivial component remains, so the ambiguity is internal and cannot be a size-two adjacent-twin module.

## 2. Independent UPO regression

The residual audit uses only the forcing/color-class criterion for comparability graphs.

Before the higher-dimensional runs, the classifier was exhaustively checked on all random (2)-orders through (n=7).

It reproduced exactly

[
1, 4, 12, 38, 165, 1042
]

nontrivial UPO permutations.

Thus the residual classification does not depend on the permutation-specific substitution theorem.

## 3. Results in (2+1)

| n | trials | (p^{m UPO}) | failures with twins / all failures | (q_3^{m res}) | residual internal | residual multi-component |
|---:|---:|---:|---:|---:|---:|---:|
|48|2000|0.8145|351/371|0.0100|0.0080|0.0020|
|64|1200|0.8408|181/191|0.00833|0.00750|0.00083|
|96|800|0.8538|115/117|0.00250|0.00250|0|
|128|400|0.9300|28/28|0|0|0|

At (n=48), adjacent twins occur in

[
94.61%
]

of all non-UPO samples.

At (n=96), the fraction is

[
98.29%.
]

At (n=128), every one of the 28 observed failures contains an adjacent twin.

The zero residual count at (n=128) must not be read as zero probability.

The Wilson 95% upper bound from that finite block is approximately

[
0.00951.
]

## 4. Results in (3+1)

| n | trials | (p^{m UPO}) | failures with twins / all failures | (q_4^{m res}) | residual internal | residual multi-component |
|---:|---:|---:|---:|---:|---:|---:|
|48|2000|0.7795|400/441|0.0205|0.0055|0.0150|
|64|1200|0.8192|203/217|0.01167|0.0050|0.00667|
|96|800|0.8663|99/107|0.0100|0.0050|0.0050|
|128|400|0.8725|49/51|0.0050|0|0.0050|

At (n=48), adjacent twins explain

[
90.70%
]

of observed failures.

At (n=128), they explain

[
96.08%.
]

The two residual failures in the (n=128) block come from multiple nontrivial connected components rather than a detected internal ambiguity.

## 5. What the data do and do not say

The finite pattern is structurally useful.

The disappearance of adjacent twins is not exposing a growing second obstruction over the audited range.

Instead,

[
q_d^{m res}(n)
]

is small and decreases numerically in both dimensions.

That is evidence against the specific failure scenario

> size-two modules become rare but are replaced by equally common larger modular ambiguities.

It is not evidence strong enough to state

[
q_d^{m res}(n)	o0.
]

The sample sizes shrink with (n), residual events are rare, and no residual exponent was preregistered.

## 6. Why the distinction matters

The total non-UPO probability can be decomposed exactly as

[
Pr(k_Gamma>1)
=
Pr(k_Gamma>1,T_n>0)
+
q_d^{m res}(n).
]

The first term is controlled by the adjacent-twin event.

If a future proof gives

[
mathbb E[T_n]=O(n^{-1}),
]

then

[
Pr(T_n>0)
le
mathbb E[T_n]
=
O(n^{-1}).
]

The entire higher-dimensional UPO problem would then reduce to controlling

[
q_d^{m res}(n).
]

This is a much narrower target than the original unrestricted orientation problem.

## 7. Candidate structural explanation

A non-stable module of size (mge3) requires a larger collection of events to remain externally indistinguishable than a size-two module does.

Likewise, after size-two isolated edge components are removed, multiple nontrivial components require a larger boundary configuration.

This suggests that both residual mechanisms may occupy lower-probability geometric regions than adjacent twins.

That statement is presently heuristic.

No exponent or asymptotic constant is assigned to it here.

## 8. Current boundary

The evidence now supports three increasingly strong statements with different statuses.

First:

[
oxed{
	ext{adjacent twins dominate finite UPO failures in the audited range}
}
]

is a reproducible computational observation.

Second:

[
oxed{
mathbb E[T_n]=Theta(n^{-1})
}
]

for (d=3,4) has passed the first held-out finite scaling-consistency test but remains unproved.

Third:

[
oxed{
p_d^{m UPO}(n)	o1
}
]

remains an open possibility, not a result.

The third statement requires both a proof that the twin obstruction vanishes and an independent bound showing

[
q_d^{m res}(n)	o0.
]

## 9. Next mathematical target

The next useful theorem should not estimate (p_d^{m UPO}) directly.

It should attack one of two smaller statements:

[
mathbb E[T_n]=O(n^{-1})
qquad
(d=3,4),
]

or

[
q_d^{m res}(n)=o(1).
]

The first is currently more tractable because the exact pair formula

[
mathbb E[T_n]
=
inom n2
mathbb E[
mathbf 1_{{Xsim Y}}
(1-D(X,Y))^{n-2}
]
]

already reduces the problem to a continuum integral.

Proving that bound would turn the dominant empirical obstruction into a theorem and leave only the genuinely higher-order modular residue.
