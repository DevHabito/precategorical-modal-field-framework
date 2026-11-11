# Random 2-order orientation recovery — substitution theorem and asymptotic limit

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** proved counting corollary from classical UPO, modular/substitution decomposition, and simple-permutation asymptotics  
**Novelty status:** exact prior equivalent not located in targeted review; absolute novelty and priority are not certified

## 1. Problem

Let \(\pi\) be uniformly distributed over \(S_n\).

Fix one total order as the identity and define the corresponding random \(2\)-order by

\[
i\prec_\pi j
\quad\Longleftrightarrow\quad
i<j
\ \text{and}\
\pi(i)<\pi(j).
\]

Forget the direction of \(\prec_\pi\) and retain only its comparability graph.

Call \(\pi\) **orientation-recoverable** when the nonempty comparability graph has exactly two transitive orientations, one the global reverse of the other. Equivalently, the original partial order is determined by symmetric comparability data up to global duality.

The empty antichain is kept separate because it has no nontrivial orientation.

The question is:

> What fraction of uniform relative permutations are orientation-recoverable as \(n\to\infty\)?

## 2. Classical ingredients

The proof uses only established ingredients.

1. A comparability graph is UPO when it has exactly two transitive orientations, one the reverse of the other.
2. For a connected comparability graph, UPO is characterized by the absence of proper non-stable modules/partitive sets.
3. In permutation graphs, graph modules correspond to intervals/common blocks of permutation representations through modular/substitution decomposition.
4. Prime permutation graphs correspond to simple permutation skeletons.
5. Every permutation has a canonical substitution decomposition, with the standard special treatment of sum- and skew-decomposable roots.
6. If \(s_n\) is the number of simple permutations of length \(n\), then
   \[
   s_n
   =
   \frac{n!}{e^2}
   \left(
   1-\frac4n+\frac{2}{n(n-1)}+O(n^{-3})
   \right).
   \]

The project does not claim any of these ingredients as new.

## 3. Connected recoverable permutations

Let \(C_n\) denote the number of relative permutations of length \(n\) whose comparability graph is connected and UPO.

Let

\[
\delta_m=m,m-1,\ldots,1
\]

denote the unique decreasing permutation of length \(m\).

### Theorem 1 — structural form

A relative permutation has connected UPO comparability graph if and only if it has one of the following forms.

### Binary sum case

\[
\boxed{
\pi=12[\delta_a,\delta_b],
\qquad
a,b\ge1,\quad a+b=n.
}
\]

### Simple-root case

\[
\boxed{
\pi=
\tau[
\delta_{n_1},
\ldots,
\delta_{n_k}
],
}
\]

where

- \(k\ge4\);
- \(\tau\) is a simple permutation of length \(k\);
- every \(n_i\ge1\);
- \(\sum_i n_i=n\).

### Proof

Use the canonical substitution decomposition of \(\pi\).

#### Skew root

If the root is a skew sum, cross-block pairs are decreasing in the relative permutation. Hence there are no comparability edges between the skew components.

The comparability graph is disconnected.

This is excluded from \(C_n\).

#### Sum root

If the root is a sum, cross-block pairs are all comparable.

A proper union of two or more sum children is therefore a graph module containing edges unless the canonical root has only two children and each child itself contains no comparability edge.

A permutation block contains no comparability edge exactly when it is decreasing.

Thus the connected UPO sum case is precisely

\[
12[\delta_a,\delta_b].
\]

#### Simple root

Let the root be a simple permutation \(\tau\) of length \(k\ge4\).

Each inflation block is a proper graph module.

The connected UPO criterion requires every such proper module to be stable.

In the current comparability representation, a block is stable exactly when its induced relative permutation is decreasing.

Hence every inflation block must equal \(\delta_{n_i}\).

Conversely, a simple root has no nontrivial quotient interval. Inflating each entry only by a stable decreasing block introduces no internal edge orientation to choose. The prime quotient has only the two opposite transitive orientations, and each stable block contributes no extra orientation freedom.

Therefore the resulting connected comparability graph is UPO.

This proves the characterization. \(\square\)

## 4. Exact connected count

For the binary sum case there are

\[
n-1
\]

positive splits

\[
a+b=n.
\]

For a fixed simple skeleton of length \(k\), the positive inflation sizes

\[
n_1+\cdots+n_k=n
\]

are counted by

\[
\binom{n-1}{k-1}.
\]

Therefore:

### Theorem 2 — connected counting formula

\[
\boxed{
C_n
=
(n-1)
+
\sum_{k=4}^{n}
s_k
\binom{n-1}{k-1}.
}
\]

No fitted parameter appears in this formula.

## 5. Exact finite regression

The repository independently enumerated simple permutations through \(n=9\):

\[
s_4,\ldots,s_9
=
2,\ 6,\ 46,\ 338,\ 2926,\ 28146.
\]

Substitution into Theorem 2 gives

\[
\boxed{
C_2,\ldots,C_9
=
1,\ 2,\ 5,\ 18,\ 101,\ 750,\ 6545,\ 64134.
}
\]

These counts agree exactly with an independent connected-UPO classification derived from the modular audit.

## 6. Adding isolated components

Let \(R_n\) be the total number of nontrivial orientation-recoverable relative permutations of length \(n\), allowing isolated vertices.

The comparability graph of a skew sum is the disjoint union of the comparability graphs of its skew components.

A UPO graph can therefore contain exactly one nontrivial connected component; every other component must be an isolated vertex. Otherwise two nontrivial components could be reversed independently.

If the unique connected UPO component has size \(m\), the \(n-m\) isolated singleton skew components can place that component in exactly

\[
n-m+1
\]

positions in the unique maximal skew decomposition.

Hence:

### Theorem 3 — total counting formula

\[
\boxed{
R_n
=
\sum_{m=2}^{n}
(n-m+1)C_m.
}
\]

For \(n=2,\ldots,9\), this gives

\[
\boxed{
R_n
=
1,\ 4,\ 12,\ 38,\ 165,\ 1042,\ 8464,\ 80020,
}
\]

exactly matching the two earlier independent exhaustive classifiers:

- direct transitive-orientation enumeration through \(n=7\);
- modular/common-interval enumeration through \(n=9\).

## 7. Connected asymptotic

Write

\[
a_m=\frac{s_m}{m!}.
\]

The classical simple-permutation theorem gives

\[
a_m\to e^{-2}.
\]

Set \(j=n-k\) in Theorem 2. Then

\[
\frac{C_n}{n!}
=
\frac{n-1}{n!}
+
\sum_{j=0}^{n-4}
a_{n-j}
\frac{n-j}{n}
\frac1{j!}.
\]

For every fixed \(j\),

\[
a_{n-j}
\frac{n-j}{n}
\frac1{j!}
\longrightarrow
\frac{e^{-2}}{j!}.
\]

Since

\[
0\le a_m\le1
\]

and

\[
0\le\frac{n-j}{n}\le1,
\]

the summands are dominated by

\[
\frac1{j!}.
\]

The dominating series is summable:

\[
\sum_{j=0}^{\infty}\frac1{j!}=e.
\]

Dominated convergence therefore gives

\[
\boxed{
\lim_{n\to\infty}\frac{C_n}{n!}
=
e^{-2}e
=
\frac1e.
}
\]

## 8. Isolated components are asymptotically negligible

From Theorem 3,

\[
R_n-C_n
=
\sum_{j=1}^{n-2}
(j+1)C_{n-j}.
\]

Since

\[
C_m\le m!,
\]

split the sum into \(j\le n/2\) and \(j>n/2\).

For \(j\le n/2\),

\[
\frac{(j+1)C_{n-j}}{n!}
\le
\frac{j+1}{n(n-1)\cdots(n-j+1)}
\le
(j+1)\left(\frac2n\right)^j.
\]

The sum of these terms is \(O(n^{-1})\).

For \(j>n/2\), the factorial ratio is exponentially/superpolynomially smaller than \(n!\); summing the remaining \(O(n)\) terms still tends to zero.

Hence

\[
\frac{R_n-C_n}{n!}\to0.
\]

Combining this with the connected asymptotic gives:

### Theorem 4 — random \(2\)-order recovery probability

For a uniformly random relative permutation,

\[
\boxed{
\lim_{n\to\infty}
\Pr(
\text{unoriented comparability data recover the order up to duality}
)
=
\frac1e.
}
\]

Numerically,

\[
\boxed{
\frac1e
\approx
0.3678794412.
}
\]

## 9. Why the finite sequence looked misleading

The exact finite probabilities through \(n=9\) are

\[
0.500000,\;
0.666667,\;
0.500000,\;
0.316667,\;
0.229167,\;
0.206746,\;
0.209921,\;
0.220514.
\]

They are nonmonotone and remain far below \(1/e\) at \(n=9\).

The asymptotic theorem explains why no monotone extrapolation from \(n\le9\) was justified.

The finite data were correctly retained without an asymptotic claim until the substitution decomposition was identified.

## 10. Physical interpretation

For a flat \(1+1\)-dimensional Minkowski sprinkling conditioned on \(n\) points, the relative light-cone order is a uniform permutation.

Under the deliberately weakened observation contract that retains only symmetric causal comparability,

\[
x\sim y
\iff
x\prec y
\ \text{or}\
y\prec x,
\]

the theorem says that asymptotically a fraction

\[
1/e
\]

of these finite random \(2\)-orders retain enough information to reconstruct their causal partial order up to one global reversal.

The complementary fraction does not.

This is an orientation-recoverability theorem for a specific information-loss experiment.

It is not a theorem that physical time emerges with probability \(1/e\).

## 11. What the theorem does not establish

It does not establish:

- a preferred future rather than past;
- duration or proper time;
- Lorentzian metric reconstruction;
- dimension beyond the declared \(1+1\) control;
- generic behavior of higher-dimensional causal sets;
- a fundamental probability for time;
- empirical support for a pregeometric ontology.

The theorem concerns one precise finite-to-asymptotic reconstruction problem.

## 12. Literature boundary

The proof combines classical work on:

- UPO comparability graphs;
- modular decomposition and transitive orientation;
- permutation graphs and common intervals;
- simple/substitution decomposition of permutations;
- asymptotic enumeration of simple permutations.

Targeted review also located earlier work that counts:

- permutation graphs;
- unlabeled \(2\)-dimensional posets;
- unlabeled UPO graphs and posets.

Those are close and important precedents.

The present counting measure is different: it is the **uniform relative-permutation measure** induced by the random-\(2\)-order representation, and it counts labeled relative permutations according to whether arrow erasure preserves the order up to duality.

No source located in the targeted review stated the exact formulas above or the \(1/e\) recovery limit for this ensemble.

This is limited negative evidence only.

**Absolute novelty and priority remain uncertified.**

## 13. Current research consequence

The previous open question

> Does the finite recovery fraction tend to zero?

is answered negatively for this model.

Instead,

\[
\boxed{
P_n\to1/e.
}
\]

The next mathematical work should not extend brute-force enumeration.

More useful questions are:

1. derive higher-order asymptotics for \(R_n/n!\);
2. quantify the modular obstruction conditioned on failure;
3. ask whether analogous reconstruction limits exist for higher-dimensional random orders;
4. determine which parts survive under more physically realistic causal-set observation contracts.

The next physical bridge remains separate:

> Why should symmetric causal comparability, rather than the full directed causet order, be the physically available primitive information?
