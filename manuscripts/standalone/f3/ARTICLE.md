# A Four-Point Obstruction to Fixed-Score Dynamic Closure

**Felipe Gianini Romero**  
**Date:** 3 November 2026  
**Status:** short mathematical note for external review, **not peer-reviewed**  
**Source claim:** MF-R049 / C2. The result is an explicit counterexample, not a proposed physical theory or a general impossibility theorem.

## Abstract

Under a deterministic centered contraction, the mean and one fixed-parameter log-Laplace score need not determine the next score. I give two strictly positive probability vectors on the same four-point support with the same mean and the same initial score but different scores after contraction. The witness is rational at the level of exponential moments, and the proof uses only a cubic polynomial identity and the injectivity of the real logarithm on positive inputs. A short kernel calculation identifies why a four-point example exists. The construction illustrates a familiar obstruction in moment closure; novelty and priority are not claimed.

## 1. Definitions

Fix the marked support \(\{0,1,2,3\}\) and let \(p=(p_0,p_1,p_2,p_3)\) be a strictly positive probability vector. Write

\[
m(p)=\sum_{j=0}^{3}jp_j,\qquad
P_p(t)=\sum_{j=0}^{3}p_jt^j.
\]

For a fixed \(\lambda>0\), define the log-Laplace score

\[
S_\lambda(p)=-\frac{1}{\lambda}
   \log P_p(e^{-\lambda}).
\]

The deterministic centered contraction with scale \(0<a<1\) changes the marked positions, not the masses:

\[
x_j'=m(p)+a(j-m(p))=(1-a)m(p)+aj.
\]

Let \(S_\lambda(T_a p)\) denote the same score evaluated at the transformed marked positions, retaining weights \(p_j\). All required exponential moments are strictly positive.

A direct calculation, term by term, gives the transport identity

\[
\sum_{j=0}^{3}p_je^{-\lambda x_j'}
=e^{-\lambda(1-a)m(p)}P_p(e^{-a\lambda})
\]
and hence
\[
S_\lambda(T_ap)=(1-a)m(p)+aS_{a\lambda}(p). \tag{1}
\]

This is an exact change-of-argument identity, not a new transform theorem.

## 2. The explicit counterexample

**Proposition.** Let \(\lambda=2\log2\) and \(a=1/2\). There is no single-valued function \(G\) defined on the macrostates realized by all strictly positive laws on \(\{0,1,2,3\}\) such that

\[
S_\lambda(T_ap)=G(m(p),S_\lambda(p))
\]

for every such \(p\).

**Proof.** Consider the two strictly positive probability vectors

\[
p^+=\frac1{64}(15,22,7,20),\qquad
p^-=\frac1{64}(17,10,25,12).
\]

Direct integer arithmetic gives

| Observable | \(p^+\) | \(p^-\) |
|---|---:|---:|
| Total mass | \(1\) | \(1\) |
| Mean \(m\) | \(3/2\) | \(3/2\) |
| \(P_p(1/4)\) | \(85/256\) | \(85/256\) |
| \(P_p(1/2)\) | \(121/256\) | \(119/256\) |

Because \(e^{-\lambda}=1/4\), the equal values at \(1/4\) imply equal initial \(S_\lambda\). Both means are \(3/2\); consequently the input macrostates \((m,S_\lambda)\) agree.

The contraction uses \(e^{-a\lambda}=1/2\) and has common shift \((1-a)m=3/4\). Therefore its two future exponential moments are exactly

\[
e^{-3\lambda/4}\frac{121}{256}
\quad\text{and}\quad
e^{-3\lambda/4}\frac{119}{256}.
\]

They differ by \(e^{-3\lambda/4}/128>0\). The real logarithm is strictly increasing on \((0,\infty)\), and \(\lambda>0\). Thus the next scores are unequal. A function \(G\) receiving identical input macrostates cannot return two distinct next scores. \(\square\)

The statement fails already within one **fixed four-point support**; varying supports is not required.

## 3. How the witness is constructed

The previous calculation can be checked without guessing its eight numerators. Put \(t_0=1/4\) and consider a signed perturbation of the uniform vector. To preserve total mass, mean, and \(P(t_0)\), its coefficient polynomial \(D\) must satisfy

\[
D(1)=0,\quad D'(1)=0,\quad D(t_0)=0.
\]

For a polynomial of degree at most three these conditions imply

\[
D(t)=c(t-1)^2(t-t_0)
\]

for some constant \(c\). Choosing \(c=1/8\) produces the table above, since

\[
P_{p^+}(t)-P_{p^-}(t)
=\frac{(t-1)^2(t-1/4)}8. \tag{2}
\]

At \(t=1/2\), the right-hand side is \(1/128\). Equation (2) also explains both conservation constraints without decimal arithmetic.

As a separate finite-dimensional check, the three linear rows for mass, mean, and evaluation at \(t_0\),

\[
\begin{pmatrix}
1&1&1&1\\
0&1&2&3\\
1&t_0&t_0^2&t_0^3
\end{pmatrix},
\]

have rank three whenever \(t_0\ne1\): the minor formed by the first three columns is \((t_0-1)^2\ne0\). Thus the nullspace is one-dimensional. On the **fixed support \(\{0,1,2\}\)** the same constraints instead determine the weights uniquely. This is a rank observation for these supports, **not** a theorem that arbitrary three-point distributions are always identifiable.

For completeness, the construction has an elementary parameter version. If \(0<t_0<1\), set

\[
d(t_0)=(-t_0,\ 1+2t_0,\ -(2+t_0),\ 1)
\]
and
\[
p^\pm(t_0)=\left(\frac14,\frac14,\frac14,\frac14\right)
\pm\frac1{16}d(t_0).
\]

Each entry is positive because \(|d_j|<3\) and \(1/4-3/16>0\). The vectors have mass one and equal mean. Their moment difference at any \(t\) is \((t-1)^2(t-t_0)/8\). In particular, a later evaluation at \(t_1\in(0,1)\) differs whenever \(t_1\ne t_0\). This is a simple polynomial mechanism for the fixed example, not a claim of minimality or originality.

## 4. Scope, exceptions, and prior work

The proposition rules out **this one selected coarse state**, \((m,S_\lambda)\), as an autonomous predictor for the specified deterministic update on the declared class. It does not rule out all finite-dimensional macrostates, restricted invariant distribution families, additional sufficient observables, or approximate closure. It does not claim that the entire transform curve is always a minimal state. For \(a=1\), no new transform evaluation is required, and the present nonclosure argument does not apply.

Moment reconstruction and non-identifiability are classical subjects. Shohat and Tamarkin (1943) developed the classical problem of moments; Kuehn (2016) reviews the difficulty of moment closure; Lin (2017) surveys moment determinacy from much richer sequences of moments. Those references establish context, **not** priority for this specific witness or equivalence of their theorems to the present one. I have not completed a full-text theorem-by-theorem novelty comparison.

An earlier **different** witness already exists in this repository at \(\lambda=\log2\), with square-root expressions after contraction. The rational polynomial version here uses \(\lambda=2\log2\); these should not be conflated. This note isolates the latter construction to facilitate independent checking.

## 5. Verification and availability

This document contains a complete human-readable proof. The exact rational witness and transport identity are also formalized in the existing repository modules \`DynamicNonclosure.lean\` and \`DynamicNonclosureTransport.lean\`. Their earlier Lean assurance results are described in \`consolidation/F3_RATIONAL_NONCLOSURE_2026-10-19.md\`. The new standalone checker \`tools/f3_standalone_exact.py\` uses Python's standard-library \`Fraction\` and performs no project imports.

Automated checks are not independent external review. The reviewer should first receive \`REVIEWER_PROBLEM.md\` **without this proof**, submit a derivation or counterexample, and then review the manuscript. The external review gate remains open until a qualified, uninvolved reviewer provides an actual written assessment.

## References

1. J. A. Shohat and J. D. Tamarkin (1943). *The Problem of Moments*. American Mathematical Society, Mathematical Surveys, vol. 1. DOI: https://doi.org/10.1090/surv/001.
2. Christian Kuehn (2016). “Moment Closure—A Brief Review.” Springer, pp. 253–271. DOI: https://doi.org/10.1007/978-3-319-28028-8_13. Related 2015 preprint: https://arxiv.org/abs/1505.02190.
3. Gwo Dong Lin (2017). “Recent developments on the moment problem.” *Journal of Statistical Distributions and Applications* **4**, article 5 (published 3 July 2017). DOI: https://doi.org/10.1186/s40488-017-0059-2.

Bibliographic metadata was checked on 3 November 2026 against the American Mathematical Society/Google Books catalog, the institutional Kuehn publication record, and the Springer journal page, respectively. These are background sources; no detailed equivalence/priority check has yet been completed.
