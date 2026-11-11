# Refinement stability of unoriented causal-order recovery in random 2D orders

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite one-point-extension audit  
**Physical status:** causal-set-inspired refinement control, not experimental evidence  
**Novelty status:** random 2D orders and UPO theory are classical; the combined refinement statistic has no certified novelty claim

## 1. Motivation

The finite Minkowski control showed that some random \(1+1\)-dimensional causal orders can be reconstructed from their unoriented comparability graph up to global reversal.

That is not enough for a physical precursor.

A candidate temporal structure should also be reasonably stable when the discrete description is refined by adding events.

This audit asks:

> If a random 2D order is UPO at size \(N\), how often does a one-point refinement remain UPO at size \(N+1\)?

It also asks the reverse question:

> Can a non-UPO parent become UPO after one-point refinement?

## 2. Exact insertion process

Represent an \(N\)-element random 2D order by a relative permutation

$$
\pi\in S_N.
$$

Add one new independent point to the Minkowski diamond.

Relative to the existing sample, its \(u\)-rank can occupy any of

$$
N+1
$$

positions and its \(v\)-rank can independently occupy any of

$$
N+1
$$

positions.

Thus, conditional on the parent rank structure, there are

$$
(N+1)^2
$$

equiprobable rank insertions.

At the permutation level, choose:

- insertion position \(i\in\{0,\ldots,N\}\);
- new value \(j\in\{0,\ldots,N\}\);

increment every old permutation value greater than or equal to \(j\), then insert \(j\) at position \(i\).

This produces the exact one-point refinement law for the rank model.

## 3. Exact transition counts

All parent permutations and all rank insertions were enumerated for

$$
N=2,\ldots,6.
$$

The UPO/non-UPO transition counts are:

### N = 2 -> 3

$$
U\to U:6,\quad U\to N:3,
$$

$$
N\to U:6,\quad N\to N:3.
$$

### N = 3 -> 4

$$
U\to U:36,\quad U\to N:28,
$$

$$
N\to U:12,\quad N\to N:20.
$$

### N = 4 -> 5

$$
U\to U:160,\quad U\to N:140,
$$

$$
N\to U:30,\quad N\to N:270.
$$

### N = 5 -> 6

$$
U\to U:768,\quad U\to N:600,
$$

$$
N\to U:222,\quad N\to N:2730.
$$

### N = 6 -> 7

$$
U\to U:5110,\quad U\to N:2975,
$$

$$
N\to U:2184,\quad N\to N:25011.
$$

Here \(U\) means a nontrivial UPO comparability graph.

## 4. Exact conditional probabilities

The conditional probability that a UPO parent remains UPO is:

| refinement | \(P(U_{N+1}\mid U_N)\) |
|---|---:|
|2 -> 3|\(2/3\)|
|3 -> 4|\(9/16\)|
|4 -> 5|\(8/15\)|
|5 -> 6|\(32/57\)|
|6 -> 7|\(146/231\)|

The probability that a non-UPO parent becomes UPO is:

| refinement | \(P(U_{N+1}\mid \neg U_N)\) |
|---|---:|
|2 -> 3|\(2/3\)|
|3 -> 4|\(3/8\)|
|4 -> 5|\(1/10\)|
|5 -> 6|\(37/492\)|
|6 -> 7|\(104/1295\)|

## 5. UPO is not refinement invariant

The exact counts show both transition types:

$$
U\to N
$$

and

$$
N\to U.
$$

Therefore:

$$
\boxed{
\text{UPO recovery is not preserved under one-point refinement}.
}
$$

It is neither hereditary under deletion nor monotone under insertion in this random-2-order setting.

## 6. Structural persistence exists nevertheless

For \(N\ge3\) in the audited range, a UPO parent is more likely to produce a UPO child than a non-UPO parent is.

For example,

$$
P(U_7\mid U_6)
=
\frac{146}{231}
\approx0.6320,
$$

whereas

$$
P(U_7\mid\neg U_6)
=
\frac{104}{1295}
\approx0.0803.
$$

Thus UPO status carries predictive information about the next rank-refined sample.

This is finite structural persistence.

It is not closure or an asymptotic law.

## 7. Parent-by-parent variability

The number of UPO children also varies between individual parents.

For UPO parents, the observed ranges of UPO children out of \((N+1)^2\) possible insertions are:

| N | minimum | maximum |
|---:|---:|---:|
|2|6|6|
|3|9|9|
|4|12|15|
|5|15|24|
|6|18|35|

Thus even within the UPO class, refinement robustness is not uniform.

## 8. Consequence for pregeometry

Exact UPO at one finite resolution is too fragile to be identified directly with physical time orientability.

A stronger physical programme would need one of the following:

- an asymptotically stable recovery property;
- a coarse-grained orientation class robust under microscopic additions;
- a probability of recovery tending to a controlled limit;
- a renormalized observable that preserves the orientation class;
- a theorem that physically admissible refinements form a restricted subclass under which recovery is stable.

None is established here.

## 9. Important methodological correction

The correct target should not automatically be:

$$
\text{UPO at every finite discretization}.
$$

That may be unnecessarily rigid.

The physical requirement is closer to:

$$
\boxed{
\text{stable recoverability of orientation under physically irrelevant refinement}.
}
$$

UPO is only one exact finite diagnostic for that broader requirement.

## 10. Relation to the repository's refinement philosophy

The foundational programme already distinguishes genuine physical information from artifacts introduced by descriptive refinement.

The same governance should apply here.

If adding one event that does not change the intended macroscopic causal regime destroys the orientation criterion, then that criterion should not be promoted as a fundamental observable without a stability theorem.

This is the temporal analogue of the repository's earlier refinement/multiplicity audits.

## 11. No asymptotic claim

The conditional probabilities above are exact for

$$
N\le6
$$

parents and \(N+1\le7\) children.

They do not establish:

- convergence;
- monotonicity;
- an infinite-size recovery probability;
- a phase transition;
- a continuum theorem.

Those remain open.

## 12. Current verdict

**Exact finite UPO recovery:** useful diagnostic.

**Refinement invariance:** FAIL.

**Statistical persistence under one-point growth:** PRESENT in the audited range.

**Macroscopic stable time orientation:** NOT ESTABLISHED.

## 13. Next question

The next target is:

> Is there a coarser orientation-recovery invariant, weaker than exact UPO, that is stable under random causal-set refinement and still determines one order class modulo global reversal in an appropriate macroscopic regime?

That question should be compared with:

- modular decomposition of comparability graphs;
- random 2D-order asymptotics;
- causal-set coarse graining;
- order-invariant/covariant observables;

before a new construction is introduced.
