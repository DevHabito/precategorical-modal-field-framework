# Target-Inclusion Degeneracy and the Honest Anchor Contract

**Programme:** Modal Field Research Programme  
**Provisional audit:** A48  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous continuation of MFRP-TR-2026-01 and A39–A47; no physical design claim

## Technical abstract

A47 completed the global noise–separation phase diagram while keeping the two anchor
parameters fixed at \(2\log2\) and \(3\log2\). A natural next question is to release those
anchors. Before attempting a continuous multi-parameter optimization, however, the design
domain must distinguish **prediction of an omitted target** from **direct observation of the
target itself**.

The current future score satisfies

\[
Q'_{2\log2}
=
\frac54+\frac12Q_{\log2},
\]

so the transform target is

\[
L_P(\log2).
\]

Consider any three-observation design that contains \(\log2\), while its other two parameters
are \(\alpha\log2\) and \(\beta\log2\) with

\[
\alpha,\beta\ge1.
\]

Assume the same compact six-point support, exact mean \(5/2\), and common absolute tolerance
\(\varepsilon\). Then for every

\[
0\le\varepsilon\le\frac1{128},
\]

the exact direct minimax target ratio is

\[
\boxed{
\rho_{\mathrm{target}}(\varepsilon)
=
1+\frac{32}{3}\varepsilon.
}
\]

The corresponding direct future-score risk is

\[
\boxed{
\mathcal R_{\mathrm{target}}^Q(\varepsilon)
=
\frac12\log_2
\left(
1+\frac{32}{3}\varepsilon
\right).
}
\]

Neither \(\alpha\) nor \(\beta\) appears in the result. In the worst case, the two additional
observations supply no reduction beyond the direct target observation.

The upper bound follows from the sharp discrete mean constraint

\[
L_P(\log2)\ge\frac3{16}
\]

and the direct target tolerance

\[
|L_P(\log2)-L_Q(\log2)|\le2\varepsilon.
\]

It is attained by

\[
q=
\left(
0,0,\frac12,\frac12,0,0
\right)
\]

and

\[
p_\varepsilon=
\left(
0,0,
\frac12+32\varepsilon,
\frac12-64\varepsilon,
32\varepsilon,
0
\right).
\]

For every additional exponent \(\alpha\ge1\), their observation difference is

\[
L_{p_\varepsilon}(\alpha\log2)
-
L_q(\alpha\log2)
=
32\varepsilon\,
2^{-2\alpha}
\left(
1-2^{-\alpha}
\right)^2,
\]

which is at most \(2\varepsilon\). Hence the same extremal pair survives every choice of the
other two observations in the declared domain.

For the expanded integer catalogue

\[
\{1,2,3,4,5,6\}\log2
\]

with budget three, all ten designs containing \(1\cdot\log2\) tie:

- at exact data, their future risk is zero;
- at \(\varepsilon=10^{-4}\), their exact ratio is
  \[
  \frac{1877}{1875}
  \]
  and their future risk is
  \[
  0.000769027280134359\ldots.
  \]

Every target-excluding design in the same catalogue is worse at both audited benchmarks. At
\(\varepsilon=10^{-4}\), the best target-excluding design from A43 is
\(\{2,3,6\}\), with future risk

\[
0.00986529623594507\ldots,
\]

approximately \(12.83\) times the target-inclusive risk.

Therefore a joint anchor optimization that permits the target itself is mathematically
degenerate for the predictive question. A nontrivial continuation must explicitly impose

\[
\boxed{\log2\notin D}
\]

or, more generally, a positive exclusion distance from the target. This is not an auxiliary
physical assumption. It is the distinction between estimating an omitted quantity and
measuring that quantity directly.

---

## 1. Declared microscopic contract

Let

\[
S=\{0,1,2,3,4,5\}.
\]

For a probability vector \(p\), define

\[
L_p(\lambda)=
\sum_{x=0}^{5}p_xe^{-\lambda x}.
\]

The mean is fixed:

\[
\sum_xxp_x=\frac52.
\]

At the target parameter

\[
\mu=\log2,
\]

\[
L_p(\mu)=
\sum_{x=0}^{5}p_x2^{-x}.
\]

The future transport law under \(a=1/2\) is

\[
Q'_{2\log2}
=
\frac54+\frac12Q_{\log2}.
\]

Therefore differences of future scores are

\[
\left|
Q'_{2\log2}(p)-Q'_{2\log2}(q)
\right|
=
\frac12
\left|
\log_2
\frac{L_p(\log2)}{L_q(\log2)}
\right|.
\]

---

## 2. Sharp lower bound for the target transform

### Lemma 2.1

Every probability distribution on \(S\) with mean \(5/2\) satisfies

\[
L_p(\log2)\ge\frac3{16}.
\]

### Proof

For every \(x\in S\),

\[
2^{-x}
\ge
\frac12-\frac{x}{8}.
\]

This affine lower envelope is exact at \(x=2\) and \(x=3\). Taking expectations gives

\[
L_p(\log2)
\ge
\frac12-\frac18\mathbb E_p[X]
=
\frac12-\frac5{16}
=
\frac3{16}.
\]

Equality is attained uniquely under the mean constraint by

\[
q=
\frac12\delta_2+\frac12\delta_3.
\]

\(\square\)

---

## 3. Universal target-inclusive upper bound

Suppose the observation design contains the target parameter \(\log2\), with common absolute
tolerance \(\varepsilon\). Two distributions that fit one common reported-data box satisfy

\[
\left|
L_p(\log2)-L_q(\log2)
\right|
\le2\varepsilon.
\]

Orient the pair so that

\[
L_p(\log2)\ge L_q(\log2).
\]

Then

\[
\frac{L_p(\log2)}{L_q(\log2)}
\le
1+
\frac{2\varepsilon}{L_q(\log2)}
\le
1+
\frac{2\varepsilon}{3/16}.
\]

Thus

\[
\boxed{
\rho_{\mathrm{target}}(\varepsilon)
\le
1+\frac{32}{3}\varepsilon.
}
\]

---

## 4. Exact attainment

Define

\[
q=
\left(
0,0,\frac12,\frac12,0,0
\right)
\]

and

\[
p_\varepsilon=
\left(
0,0,
\frac12+32\varepsilon,
\frac12-64\varepsilon,
32\varepsilon,
0
\right).
\]

For

\[
0\le\varepsilon\le\frac1{128},
\]

all weights are nonnegative.

Normalization is preserved because

\[
32-64+32=0.
\]

The mean is preserved because

\[
2(32)-3(64)+4(32)=0.
\]

At the target,

\[
L_{p_\varepsilon}(\log2)
-
L_q(\log2)
=
32\varepsilon
\left(
\frac14-\frac{2}{8}+\frac1{16}
\right)
=
2\varepsilon.
\]

Since

\[
L_q(\log2)=\frac3{16},
\]

their ratio is

\[
\frac{L_{p_\varepsilon}(\log2)}
{L_q(\log2)}
=
1+\frac{32}{3}\varepsilon.
\]

---

## 5. Why every other observation is inactive in the worst case

Let the additional observed parameter be

\[
\lambda=\alpha\log2,
\qquad
\alpha\ge1.
\]

Set

\[
t=2^{-\alpha},
\qquad
0<t\le\frac12.
\]

The same extremal pair gives

\[
L_{p_\varepsilon}(\lambda)
-
L_q(\lambda)
=
32\varepsilon
\left(
t^2-2t^3+t^4
\right)
\]

or

\[
32\varepsilon\,t^2(1-t)^2.
\]

On \(0\le t\le1/2\),

\[
t^2(1-t)^2\le\frac1{16}.
\]

Therefore

\[
0\le
L_{p_\varepsilon}(\lambda)-L_q(\lambda)
\le
2\varepsilon.
\]

The pair is compatible with every additional observation whose exponent is at least the
target exponent. Combining this with the upper bound proves:

### Theorem 5.1 — target-inclusion degeneracy

For any design

\[
D=\{\log2,\alpha\log2,\beta\log2\},
\qquad
\alpha,\beta\ge1,
\]

and

\[
0\le\varepsilon\le\frac1{128},
\]

\[
\boxed{
\rho_D(\varepsilon)
=
1+\frac{32}{3}\varepsilon.
}
\]

The other two parameters do not affect the minimax value.

---

## 6. Expanded catalogue audit

Consider the integer catalogue

\[
\mathcal C_{\mathrm{expanded}}
=
\{1,2,3,4,5,6\}.
\]

There are

\[
\binom63=20
\]

three-parameter designs:

- ten contain the target exponent \(1\);
- ten exclude it.

### Exact data

For every target-inclusive design,

\[
\rho_D(0)=1,
\qquad
\mathcal R_D^Q(0)=0.
\]

Every target-excluding design has ratio strictly greater than one. The best target-excluding
design in A43 is

\[
\{2,3,4\},
\]

with

\[
\rho=\frac{8770}{8707}>1.
\]

Thus the expanded exact-data problem has ten tied, trivial minimizers.

### Error \(\varepsilon=10^{-4}\)

For every target-inclusive design,

\[
\rho_D
=
1+\frac{32}{30000}
=
\boxed{\frac{1877}{1875}}.
\]

The future-score risk is

\[
\boxed{
\frac12\log_2\frac{1877}{1875}
=
0.000769027280134359\ldots.
}
\]

The best target-excluding design is

\[
\{2,3,6\},
\]

with

\[
\rho
=
\frac{1828961429248}{1804118444725}
\]

and

\[
\mathcal R^Q
=
0.00986529623594507\ldots.
\]

The ratio of the two risks is approximately

\[
12.83.
\]

Equivalently, direct target inclusion reduces the minimax future-score risk by approximately

\[
92.20\%
\]

relative to the best target-excluding integer design.

This comparison is a catalogue result, not a theorem over every possible continuous
target-excluding design.

---

## 7. Interpretation

The target-inclusive problem is not invalid. It answers a different question:

> Given a noisy direct measurement of the target transform, what is the worst possible future
> score uncertainty?

The target-excluding programme answers:

> How well can the target be predicted from other generalized moments?

These are distinct information contracts.

If the aim is to study omitted-message prediction, dynamic sufficiency, or informative
parameter placement, the design domain must exclude the target:

\[
\boxed{\mu\notin D.}
\]

A stronger operational version can impose

\[
|\lambda_j-\mu|\ge\Delta_{\mathrm{target}}>0.
\]

Without such a condition, releasing the anchors permits the optimization to solve the problem
by measuring the requested quantity directly.

---

## 8. Logical status

### Established

1. The discrete mean contract gives the sharp target-transform lower bound \(3/16\).
2. Every target-inclusive design with other exponents at least \(1\) has exact minimax ratio
   \(1+32\varepsilon/3\) for \(0\le\varepsilon\le1/128\).
3. The same explicit extremal pair satisfies every additional observation in that domain.
4. The other observations are minimax-irrelevant.
5. In the expanded integer catalogue, all ten target-inclusive designs tie.
6. At exact data their risk is zero.
7. At \(\varepsilon=10^{-4}\) their exact ratio is \(1877/1875\).
8. They dominate every target-excluding design in the same catalogue at both audited
   benchmarks.

### Not established

1. No globally optimal continuous target-excluding triple has been derived.
2. No parameters below the target exponent are covered by the universal witness theorem.
3. No empirical reason is given for permitting or forbidding direct target measurement.
4. No physical measurement cost or error law is inferred.
5. The support and mean remain formal contracts.

---

## 9. Next rigorous target

The nontrivial joint-anchor problem must now be stated with target exclusion.

A minimal mathematically honest domain is

\[
1+\Delta_{\mathrm{target}}
\le
\alpha<\beta<\gamma,
\]

with a declared upper cap and common error contract. The next audit should begin with a finite
catalogue or a one-dimensional anchor-release problem, rather than attempting an unrestricted
three-dimensional continuous optimization immediately.

The exclusion distance is not a fitted correction. It defines the difference between direct
measurement and prediction from genuinely omitted information.
