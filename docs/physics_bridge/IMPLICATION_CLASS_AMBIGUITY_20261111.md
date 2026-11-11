# Implication-class ambiguity in finite random 2D orders

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite diagnostic using classical comparability-graph implication classes  
**Novelty status:** implication classes and forcing theory are classical. The project uses their count as a graded recovery diagnostic; no novelty claim is made.

## 1. Why move beyond the UPO yes/no test?

The finite Minkowski control used the classical UPO property:

$$
|\mathrm{TO}(G)|=2.
$$

This is an exact criterion for recovery of a nontrivial partial order from its comparability graph up to global reversal.

But UPO is a binary property.

The one-point refinement audit showed that exact UPO status can be lost or gained after adding one event.

A more graded diagnostic is therefore useful.

Classical comparability theory already supplies one.

## 2. Implication classes

For an undirected graph \(G=(V,E)\), let

$$
\vec E
$$

contain both directions of every edge.

Golumbic's forcing relation \(\Gamma\) relates directed edges when transitivity forces them to receive the same orientation.

One standard form is:

$$
\overrightarrow{ab}\,\Gamma\,\overrightarrow{ac}
$$

when

$$
\{b,c\}\notin E,
$$

and similarly for directed edges sharing a head.

The transitive closure

$$
\Gamma^*
$$

partitions \(\vec E\) into implication classes.

If one directed edge in a class belongs to a transitive orientation, the orientation of the entire class is forced.

This is classical comparability-graph theory.

## 3. Inverse pairing

For a comparability graph, every implication class \(A\) has an inverse class

$$
A^{-1}
=
\{
\overrightarrow{ba}:
\overrightarrow{ab}\in A
\}.
$$

For every nontrivial graph audited here, the implication classes therefore occur in inverse pairs.

Define the project diagnostic

$$
\boxed{
k_\Gamma(G)
=
\frac12
\left|
\vec E/\Gamma^*
\right|.
}
$$

This is simply the number of inverse implication-class pairs.

The symbol \(k_\Gamma\) is project notation for a classical count.

## 4. UPO as the minimal nontrivial case

Aigner-Prins/Golumbic theory gives:

$$
\boxed{
G\text{ nontrivial UPO}
\iff
k_\Gamma(G)=1.
}
$$

Thus UPO is the extreme case in which one forced orientation block and its inverse cover every edge.

For

$$
k_\Gamma>1,
$$

the unoriented graph leaves more than one forcing block.

## 5. What k_Gamma does not mean

It must not be described as:

- the number of independent physical arrows;
- the number of bits required to orient the graph;
- the logarithm of the number of compatible posets;
- a thermodynamic entropy;
- a time dimension.

Different implication classes can still be coupled by higher structural constraints.

The complete number of transitive orientations need not equal

$$
2^{k_\Gamma}.
$$

For example, complete graphs have many singleton forcing blocks, while their transitive orientations correspond to total orders.

Therefore \(k_\Gamma\) is only a **forcing-block ambiguity diagnostic**.

## 6. Exact random-2-order enumeration

For every relative permutation

$$
\pi\in S_N,
\qquad
N=2,\ldots,8,
$$

the audit constructs the comparability graph and computes all implication classes by exact union-find closure of \(\Gamma\).

The empty antichain is reported separately.

The distributions for nonempty graphs are:

### N = 2

| k_Gamma | count |
|---:|---:|
|1|1|

### N = 3

| k_Gamma | count |
|---:|---:|
|1|4|
|3|1|

### N = 4

| k_Gamma | count |
|---:|---:|
|1|12|
|2|5|
|3|5|
|6|1|

### N = 5

| k_Gamma | count |
|---:|---:|
|1|38|
|2|45|
|3|17|
|4|12|
|6|6|
|10|1|

### N = 6

| k_Gamma | count |
|---:|---:|
|1|165|
|2|280|
|3|112|
|4|105|
|5|7|
|6|28|
|7|14|
|10|7|
|15|1|

### N = 7

| k_Gamma | count |
|---:|---:|
|1|1042|
|2|1756|
|3|998|
|4|650|
|5|256|
|6|116|
|7|144|
|8|8|
|9|16|
|10|28|
|11|16|
|15|8|
|21|1|

Each \(N\) also has one empty antichain permutation.

## 7. Exact means

Conditioned on a nonempty comparability graph:

$$
E[k_\Gamma]
=
\begin{cases}
1,&N=2,\\
7/5,&N=3,\\
43/23,&N=4,\\
39/17,&N=5,\\
1867/719,&N=6,\\
13937/5039,&N=7.
\end{cases}
$$

Numerically, at \(N=7\),

$$
E[k_\Gamma]
\approx2.76583.
$$

The median is \(2\) for \(N=5,6,7\).

## 8. Low-ambiguity mass

At \(N=7\),

$$
P(k_\Gamma\le2\mid E\neq\varnothing)
=
\frac{2798}{5039}
\approx0.55527,
$$

and

$$
\boxed{
P(k_\Gamma\le3\mid E\neq\varnothing)
=
\frac{3796}{5039}
\approx0.75332.
}
$$

Thus exact UPO recovery is uncommon at this size, but most finite random 2D orders still have only a few implication-class pairs.

This does not imply that only a few independent choices remain globally.

It means only that the elementary forcing relation groups the directed edges into a small number of inverse blocks.

## 9. Extreme controls

### Total chain

The identity permutation gives

$$
G=K_N.
$$

Every directed edge is its own implication class because every pair of neighboring endpoints is adjacent.

Hence

$$
\boxed{
k_\Gamma(K_N)=\binom N2.
}
$$

The graph has

$$
N!
$$

transitive orientations.

This is the maximum \(k_\Gamma\) observed in the exact random-2-order enumerations.

### Antichain

The reverse permutation has no edges.

The diagnostic is undefined/trivial there and is recorded separately as the empty case.

## 10. One-point refinement

Using the same exact rank-insertion process as the UPO refinement audit, the project tracked

$$
k_\Gamma(G_N)
\to
k_\Gamma(G_{N+1})
$$

for every parent permutation and every one-point insertion.

The global exact statistics are:

| refinement | unchanged | change <= 1 | mean absolute change |
|---|---:|---:|---:|
|2 -> 3|\(1/2\)|\(5/6\)|\(2/3\)|
|3 -> 4|\(1/2\)|\(5/6\)|\(17/24\)|
|4 -> 5|\(59/120\)|\(101/120\)|\(43/60\)|
|5 -> 6|\(22/45\)|\(61/72\)|\(103/144\)|
|6 -> 7|\(2497/5040\)|\(1433/1680\)|\(887/1260\)|

For the last transition,

$$
P(
|k_{\Gamma,7}-k_{\Gamma,6}|
\le1
)
=
\frac{1433}{1680}
\approx0.85298.
$$

## 11. Interpretation

The graded implication-class count is not refinement invariant.

However, in the audited finite range, one-point refinement usually changes it only mildly.

This makes it a more informative diagnostic than the exact Boolean UPO status for studying gradual loss or recovery of orientational information.

No asymptotic stability theorem follows.

## 12. Relation to physical recovery

If the primitive observable were only symmetric causal connectibility, then:

- \(k_\Gamma=1\) means exact nontrivial recovery up to global reversal;
- \(k_\Gamma>1\) records multiple forcing blocks remaining in the unoriented data;
- large \(k_\Gamma\) signals greater local orientation underdetermination in this specific graph-theoretic sense.

The physical meaning of these blocks is not established.

They are not automatically local clocks, causal patches, or degrees of freedom.

## 13. Why this is preferable to inventing a new score

The diagnostic is already built into classical comparability theory.

It directly explains the mechanism by which one oriented edge forces others.

Using it therefore respects the repository's anti-ad-hoc rule:

> use established structure when it already measures the obstruction of interest.

Only if implication classes prove insufficient for the physical question should a new quantity be considered.

## 14. Current conclusion

Exact UPO is the zero-ambiguity endpoint

$$
k_\Gamma=1.
$$

Random 2D orders at small \(N\) often fail that endpoint while remaining close to it in implication-class count.

The next question is not whether \(k_\Gamma\) is a new invariant.

It is classical.

The next question is:

> Does the implication-class structure have a stable large-\(N\) or coarse-grained behavior in physically motivated causal-set ensembles, and can such behavior support robust recovery of one orientation class modulo global reversal?

That remains open.


## 15. Exact N = 8 extension

The audit was extended to all

$$
8!=40320
$$

relative permutations.

Exactly one is the empty antichain.

Among the 40319 nonempty comparability graphs, the implication-pair histogram is:

| k_Gamma | count |
|---:|---:|
|1|8464|
|2|12942|
|3|8568|
|4|4713|
|5|3006|
|6|693|
|7|1089|
|8|315|
|9|156|
|10|102|
|11|171|
|12|18|
|13|18|
|15|36|
|16|18|
|21|9|
|28|1|

The exact conditional mean is

$$
\boxed{
E[k_\Gamma\mid E\neq\varnothing]
=
\frac{114035}{40319}
\approx2.82827.
}
$$

Also,

$$
P(k_\Gamma\le2\mid E\neq\varnothing)
=
\frac{21406}{40319}
\approx0.53091,
$$

and

$$
\boxed{
P(k_\Gamma\le3\mid E\neq\varnothing)
=
\frac{29974}{40319}
\approx0.74342.
}
$$

For the exact one-point refinement

$$
N=7\to8,
$$

the forcing-block count is unchanged with probability

$$
\frac{859}{1680}
\approx0.51131,
$$

and satisfies

$$
\boxed{
|\Delta k_\Gamma|\le1
}
$$

with probability

$$
\boxed{
\frac{1929}{2240}
\approx0.86116.
}
$$

The mean absolute change is

$$
\frac{27413}{40320}
\approx0.67989.
$$

This extra exact size does not establish convergence or an asymptotic law.
