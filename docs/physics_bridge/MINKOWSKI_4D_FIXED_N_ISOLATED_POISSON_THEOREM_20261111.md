# Fixed-cardinality Poisson limit for isolated vertices in 3+1 Minkowski

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** project theorem — proof complete; independent/external review pending  
**Scope:** \(n\) iid uniform points in a fixed flat \(3+1\)-dimensional Alexandrov interval  
**Novelty status:** targeted review found general isolated-vertex Poisson approximation theory and causal-set discussions of isolated points, but no prior statement of this \(3\pi\) limit for the Lorentzian causal-comparability graph. Absolute novelty and priority are not certified.

## 1. Theorem

Let \(X_1,\ldots,X_n\) be iid uniform points in a fixed Alexandrov interval \(A=I(p,q)\) of flat \(3+1\)-dimensional Minkowski spacetime.

Construct the undirected causal-comparability graph \(G_n\):

\[
\{X_i,X_j\}\in E(G_n)
\quad\Longleftrightarrow\quad
X_i\prec X_j
\ \text{or}\
X_j\prec X_i.
\]

Let \(I_n\) be the number of isolated vertices of \(G_n\).

Then

\[
\boxed{
I_n
\xrightarrow{d}
\operatorname{Poisson}(3\pi)
}
\]

as \(n\to\infty\).

Consequently,

\[
\boxed{
P(I_n=0)
\longrightarrow
e^{-3\pi}
\approx
8.06995\times10^{-5}.
}
\]

This is the fixed-cardinality/binomial counterpart of the repository's Poisson-sprinkling theorem.

---

## 2. Exact factorial moments

Let

\[
S_x
=
\{y\in A:y\sim x\}
\]

be the continuum comparability region of \(x\), with normalized volume measure \(\mu\).

For fixed \(k\in\mathbb N\), write

\[
(I_n)_k
=
I_n(I_n-1)\cdots(I_n-k+1).
\]

Choose \(k\) distinguished iid points \(x_1,\ldots,x_k\).

For all of them to be isolated:

1. they must be pairwise incomparable;
2. every one of the remaining \(n-k\) points must avoid
   \[
   \bigcup_{i=1}^{k}S_{x_i}.
   \]

Therefore

\[
\boxed{
E[(I_n)_k]
=
(n)_k
\int_{A^k}
\mathbf 1_{\mathcal J_k(x_1,\ldots,x_k)}
\left(
1-
\mu\left(
\bigcup_{i=1}^{k}S_{x_i}
\right)
\right)^{n-k}
\mu^k(d\mathbf x),
}
\]

where \(\mathcal J_k\) is the event that the distinguished points are pairwise incomparable.

This identity is exact.

---

## 3. Null-waist coordinates

Use the standard diamond

\[
p=(-1,\mathbf 0),
\qquad
q=(1,\mathbf 0).
\]

For one point \(x=(t,\mathbf x)\), with \(r=\|\mathbf x\|\), set

\[
a=1+t-r,
\qquad
b=1-t-r.
\]

Then

\[
a,b\ge0,
\qquad
a+b\le2.
\]

With normalized spherical measure \(d\sigma\) on \(S^2\),

\[
\boxed{
d\mu
=
3
\left(
1-\frac{a+b}{2}
\right)^2
da\,db\,d\sigma.
}
\]

The exact comparable-volume fraction is

\[
\boxed{
Q(a,b)
=
\frac{
a^2(2-b)^2+b^2(2-a)^2
}{16}.
}
\]

The only zero is \(a=b=0\).

Thus isolated vertices localize to the null waist.

---

## 4. Rescaling \(k\) candidate points

For each distinguished point set

\[
a_i=\frac{2A_i}{\sqrt n},
\qquad
b_i=\frac{2B_i}{\sqrt n},
\qquad
\sigma_i\in S^2.
\]

The measure becomes

\[
(n)_k
\mu^k(d\mathbf x)
=
12^k
\frac{(n)_k}{n^k}
\prod_{i=1}^{k}
\left(
1-\frac{A_i+B_i}{\sqrt n}
\right)^2
dA_i\,dB_i\,d\sigma_i
\]

on the expanding domains

\[
A_i,B_i\ge0,
\qquad
A_i+B_i\le\sqrt n.
\]

Moreover,

\[
nQ(x_i)
=
A_i^2
\left(
1-\frac{B_i}{\sqrt n}
\right)^2
+
B_i^2
\left(
1-\frac{A_i}{\sqrt n}
\right)^2.
\]

Hence, for fixed \(A_i,B_i\),

\[
\boxed{
nQ(x_i)
\longrightarrow
A_i^2+B_i^2.
}
\]

---

## 5. Pairwise incomparability in the limit

Fix a configuration with pairwise distinct angular directions:

\[
\sigma_i\ne\sigma_j
\qquad
(i\ne j).
\]

This excludes only a set of spherical measure zero.

Under the waist scaling,

\[
t_i=O(n^{-1/2}),
\qquad
r_i=1+O(n^{-1/2}).
\]

If the angular separation between \(\sigma_i\) and \(\sigma_j\) is fixed and positive, their spatial separation remains order one, whereas their time separation is only \(O(n^{-1/2})\).

Therefore, for all sufficiently large \(n\),

\[
x_i
\not\sim
x_j.
\]

Thus

\[
\boxed{
\mathbf 1_{\mathcal J_k}
\longrightarrow1
}
\]

for almost every fixed rescaled configuration.

---

## 6. Pair-overlap decay

For incomparable waist points, the endpoint-overlap lemma proved in **MINKOWSKI_4D_ISOLATED_POISSON_THEOREM_20261111.md** gives, with

\[
v_{ij}
=
\sin\left(
\frac{\theta_{ij}}2
\right),
\]

\[
\mu(S_{x_i}\cap S_{x_j})
\le
C
\frac{
a_i^2a_j^2+b_i^2b_j^2
}{
v_{ij}^4
}.
\]

For a fixed configuration with \(v_{ij}>0\), the waist scaling gives

\[
\mu(S_{x_i}\cap S_{x_j})
=
O(n^{-2}).
\]

Therefore

\[
\boxed{
n\,
\mu(S_{x_i}\cap S_{x_j})
\longrightarrow0.
}
\]

Bonferroni's inequality gives

\[
0
\le
\sum_{i=1}^{k}Q(x_i)
-
\mu\left(
\bigcup_{i=1}^{k}S_{x_i}
\right)
\le
\sum_{1\le i<j\le k}
\mu(S_{x_i}\cap S_{x_j}).
\]

Hence, for almost every fixed rescaled configuration,

\[
\boxed{
n\,
\mu\left(
\bigcup_{i=1}^{k}S_{x_i}
\right)
\longrightarrow
\sum_{i=1}^{k}
(A_i^2+B_i^2).
}
\]

---

## 7. Pointwise limit of the avoidance probability

Set

\[
U_n
=
\mu\left(
\bigcup_{i=1}^{k}S_{x_i}
\right).
\]

The previous section gives

\[
nU_n
\longrightarrow
\sum_{i=1}^{k}
(A_i^2+B_i^2).
\]

In particular, \(U_n=O(n^{-1})\) for each fixed almost-everywhere configuration.

Therefore

\[
(n-k)\log(1-U_n)
\longrightarrow
-
\sum_{i=1}^{k}
(A_i^2+B_i^2),
\]

and thus

\[
\boxed{
(1-U_n)^{n-k}
\longrightarrow
\exp\left[
-\sum_{i=1}^{k}
(A_i^2+B_i^2)
\right].
}
\]

---

## 8. Uniform domination

For any measurable sets \(S_1,\ldots,S_k\),

\[
\mu\left(
\bigcup_{i=1}^{k}S_i
\right)
\ge
\max_i\mu(S_i)
\ge
\frac1k
\sum_{i=1}^{k}\mu(S_i).
\]

Hence

\[
U_n
\ge
\frac1k
\sum_{i=1}^{k}Q(x_i).
\]

On the rescaled triangular domain,

\[
nQ(x_i)
=
A_i^2
\left(
1-\frac{B_i}{\sqrt n}
\right)^2
+
B_i^2
\left(
1-\frac{A_i}{\sqrt n}
\right)^2.
\]

If \(A_i\ge B_i\), then \(B_i\le\sqrt n/2\), so

\[
nQ(x_i)
\ge
\frac{A_i^2}{4}
\ge
\frac{A_i^2+B_i^2}{8}.
\]

The case \(B_i\ge A_i\) is symmetric.

Thus, uniformly on the entire domain,

\[
\boxed{
nQ(x_i)
\ge
\frac{
A_i^2+B_i^2
}{8}.
}
\]

For \(n\ge2k\),

\[
(1-U_n)^{n-k}
\le
e^{-(n-k)U_n}
\le
\exp\left[
-\frac1{16k}
\sum_{i=1}^{k}
(A_i^2+B_i^2)
\right].
\]

The right-hand side is integrable on

\[
([0,\infty)^2\times S^2)^k.
\]

The remaining measure prefactors satisfy

\[
0
\le
\left(
1-\frac{A_i+B_i}{\sqrt n}
\right)^2
\le1,
\]

and

\[
0<
\frac{(n)_k}{n^k}
\le1.
\]

Therefore the complete factorial-moment integrand is dominated by an \(n\)-independent integrable function.

Dominated convergence applies.

---

## 9. Limiting factorial moments

Using the almost-everywhere pointwise limit and the domination above,

\[
\begin{aligned}
\lim_{n\to\infty}
E[(I_n)_k]
&=
12^k
\int
\exp\left[
-\sum_{i=1}^{k}
(A_i^2+B_i^2)
\right]
\prod_{i=1}^{k}
dA_i\,dB_i\,d\sigma_i
\\[4pt]
&=
\left[
12
\int_0^\infty
e^{-A^2}dA
\int_0^\infty
e^{-B^2}dB
\int_{S^2}d\sigma
\right]^k
\\[4pt]
&=
\left[
12
\left(
\frac{\sqrt\pi}{2}
\right)^2
\right]^k.
\end{aligned}
\]

Since the spherical measure is normalized,

\[
\int_{S^2}d\sigma=1.
\]

Therefore

\[
\boxed{
\lim_{n\to\infty}
E[(I_n)_k]
=
(3\pi)^k
}
\]

for every fixed \(k\in\mathbb N\).

These are exactly the factorial moments of

\[
\operatorname{Poisson}(3\pi).
\]

---

## 10. Completion by the method of moments

Ordinary moments are finite linear combinations of factorial moments through Stirling numbers of the second kind.

Thus, for every fixed \(m\),

\[
E[I_n^m]
\]

converges to the \(m\)-th moment of

\[
\operatorname{Poisson}(3\pi).
\]

The Poisson distribution is moment-determinate.

Therefore the method of moments gives

\[
\boxed{
I_n
\xrightarrow{d}
\operatorname{Poisson}(3\pi).
}
\]

This proves the theorem.

\(\square\)

---

## 11. Agreement with the Poisson-sprinkling theorem

The repository now has two ensemble-level proofs of the same critical \(3+1\) law.

### Poisson cardinality

For a Poisson sprinkling of mean cardinality \(\lambda\),

\[
d_{\mathrm{TV}}
\left(
\mathcal L(I_\lambda),
\operatorname{Poisson}(3\pi)
\right)
=
O(\lambda^{-1/2}).
\]

This proof uses a Stein–Palm coupling.

### Fixed cardinality

For exactly \(n\) iid uniform points,

\[
I_n
\xrightarrow{d}
\operatorname{Poisson}(3\pi).
\]

This proof uses factorial moments and the same Lorentzian endpoint-overlap lemma.

The fixed-\(n\) proof does not rely on an unproved depoissonization step.

---

## 12. Consequence for connectedness

Let \(B_n\) be the event that \(G_n\) has at least two components containing edges. For \(n\ge2\), a connected graph has no isolated vertices. If a graph has no isolated vertices but is disconnected, each component contains an edge, so \(B_n\) occurs. Consequently
\[
0\le
P(I_n=0)-P(G_n\text{ connected})
\le P(B_n).
\]

The [flat orientation-recovery theorem, Section 4.1](MINKOWSKI_D4_ORIENTATION_RECOVERY_THEOREM_20261112.md#41-one-nontrivial-component), gives \(P(B_n)\to0\) for the same fixed-cardinality ensemble. The Poisson limit above gives \(P(I_n=0)\to e^{-3\pi}\), by evaluating the distribution functions at \(1/2\) since both variables are integer-valued. Thus
\[
\boxed{
\lim_{n\to\infty}P(G_n\text{ connected})
=e^{-3\pi}
\approx 8.07\times10^{-5}.
}
\]

The [sharp recovery law](MINKOWSKI_ALLD_ORIENTATION_RECOVERY_RATE_THEOREM_20261112.md#3-the-31-law) also gives \(p_4^{\mathrm{UPO}}(n)\to1\). The probability of a graph that is both connected and UPO has the same limit \(e^{-3\pi}\), since omitting the UPO requirement changes that probability by at most \(1-p_4^{\mathrm{UPO}}(n)\).

---

## 13. Consequence for the UPO program

This theorem explains a feature that initially looked paradoxical in the higher-dimensional simulations.

In \(3+1\),

- the probability that the entire comparability graph is connected is strongly suppressed;
- nevertheless, isolated vertices do not create additional transitive-orientation freedom;
- the unique nontrivial component can contain a fraction of vertices tending toward one.

Thus

\[
\boxed{
\text{connectedness}
\ne
\text{orientation recoverability}.
}
\]

The critical \(3\pi\) cloud of isolated events is a boundary effect of the finite Alexandrov interval, not by itself an obstruction to recovering all existing causal arrows up to global reversal.

---

## 14. Literature boundary

The proof uses classical tools:

- factorial moments and the method of moments;
- Minkowski Alexandrov-volume scaling;
- causal-set Poisson/binomial sprinkling ensembles;
- the endpoint-overlap geometry established in the companion Poisson proof.

Penrose (2018) gives general Poisson-approximation machinery for isolated vertices in inhomogeneous random graphs, including both Poisson and binomial point-process settings under other sufficient conditions.

Those convenient homogeneous criteria do not directly cover the present deterministic Lorentzian kernel because the connection function attains \(1\) and the comparable volume degenerates at the null waist.

The fixed-\(n\) proof above therefore uses a direct factorial-moment argument rather than invoking those criteria.

Targeted searches did not locate a prior result stating

\[
I_n
\Rightarrow
\operatorname{Poisson}(3\pi)
\]

for the causal-comparability graph of \(n\) uniform points in a \(3+1\)-dimensional Minkowski Alexandrov interval.

This is limited negative evidence only.

Absolute novelty and priority are not certified.

---

## 15. Subsequent results

The [adjacent-twin asymptotic](MINKOWSKI_4D_ADJACENT_TWIN_ASYMPTOTIC_THEOREM_20261111.md) gives the \(9\pi/n\) first moment. The [sharp flat recovery law](MINKOWSKI_ALLD_ORIENTATION_RECOVERY_RATE_THEOREM_20261112.md) bounds the other failure modes and gives the same leading term for the probability of failure. The fixed-cardinality Poisson limit and the connectedness corollary in Section 12 remain specific to this flat finite-diamond ensemble.
