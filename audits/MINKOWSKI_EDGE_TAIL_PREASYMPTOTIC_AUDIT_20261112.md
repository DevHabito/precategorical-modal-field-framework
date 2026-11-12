# Audit: slow pre-asymptotic convergence of the higher-dimensional edge tail

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** computational stress test + asymptotic interpretation  
**Scope:** verify that moderate-\(\varepsilon\) Monte Carlo does not falsely reject the all-dimensional small-disagreement theorem

## 1. Motivation

The analytic theorem states

\[
F_d(\varepsilon)
=
\Theta(
\varepsilon^{\beta_d}
),
\]

where

\[
\beta_d
=
\min\left(
d,\,
2+\frac4d
\right).
\]

A direct Monte Carlo stress test showed that the effective log-log slope at accessible \(\varepsilon\) can lie substantially below \(\beta_d\), especially in \(d=6\) and \(d=8\).

This note records that discrepancy rather than hiding it.

The discrepancy is pre-asymptotic.

## 2. Direct full-diamond audit

An independent session run used:

- iid uniform Alexandrov-diamond sampling;
- the exact closed disagreement formula;
- \(5{,}000{,}000\) independent point pairs per dimension;
- base seed \(9876\), with dimension added to the RNG seed.

Representative results were:

### d = 5

The predicted exponent is

\[
\beta_5=2.8.
\]

| \(\varepsilon\) | count | \(F_5(\varepsilon)/\varepsilon^{2.8}\) |
|---:|---:|---:|
|0.008|49|7.2874|
|0.012|135|6.4514|
|0.016|281|6.0007|
|0.024|797|5.4689|
|0.032|1628|4.9919|
|0.045|3853|4.5481|
|0.060|7750|4.0880|

The analytic asymptotic coefficient from the joint integral is approximately

\[
9.4326.
\]

The ratio rises as \(\varepsilon\) decreases, but the asymptotic constant is not yet reached.

### d = 6

\[
\beta_6=\frac83.
\]

| \(\varepsilon\) | count | \(F_6(\varepsilon)/\varepsilon^{8/3}\) |
|---:|---:|---:|
|0.006|49|8.2443|
|0.009|153|8.7312|
|0.012|319|8.4529|
|0.018|795|7.1450|
|0.025|1721|6.4413|
|0.035|3615|5.5160|
|0.050|7622|4.4928|

The analytic asymptotic coefficient is approximately

\[
16.2305.
\]

Again the direct finite-\(\varepsilon\) ratios are much smaller.

### d = 8

\[
\beta_8=\frac52.
\]

| \(\varepsilon\) | count | \(F_8(\varepsilon)/\varepsilon^{5/2}\) |
|---:|---:|---:|
|0.004|104|20.5548|
|0.006|216|15.4919|
|0.009|501|13.0395|
|0.013|972|10.0888|
|0.019|1882|7.5642|
|0.028|3384|5.1590|
|0.040|5534|3.4588|

The analytic asymptotic coefficient is approximately

\[
63.2959.
\]

A naive slope fit over these points is therefore misleading.

## 3. Exact formula validation

The discrepancy is not caused by an error in the closed formula for

\[
\Delta_d(x,y).
\]

For low-\(\Delta\) pairs in \(d=8\), the exact formula was independently compared against direct Monte Carlo integration of

\[
\mu(A_x\triangle A_y)
\]

using \(300{,}000\) fresh test points per selected pair.

Representative comparisons included:

\[
0.00547835
\quad\text{versus}\quad
0.00555000,
\]

\[
0.00241995
\quad\text{versus}\quad
0.00244333,
\]

\[
0.00355011
\quad\text{versus}\quad
0.00351333.
\]

The differences are consistent with the sampling uncertainty of the direct integration.

Thus the finite-slope discrepancy is not evidence against the exact disagreement identity.

## 4. Why high dimension converges slowly

For \(d\ge4\), the leading null-joint scaling is

\[
a,b,A,B
=
O(
\varepsilon^{2/d}
).
\]

Define

\[
\lambda_d(\varepsilon)
=
\varepsilon^{2/d}.
\]

This is the actual small geometric parameter.

For example, in \(d=8\),

\[
\lambda_8(0.004)
=
0.004^{1/4}
\approx
0.252.
\]

That is not a small local scale.

Even when the measured disagreement is already of order \(10^{-3}\), the geometric joint chart can still have depths of order \(10^{-1}\).

Therefore the exact finite-window density, radial factors, and endpoint-volume corrections remain substantial.

The convergence becomes slower as \(d\) increases because

\[
\frac2d
\downarrow0.
\]

## 5. Reduced integral removes the finite-window obstruction

The one-side asymptotic integral is

\[
J_m(s)
=
\int
A^{m-1}
\mathbf1_{
\{(\alpha+A)^m-\alpha^m\le s\}
}
\,dA\,d\alpha,
\]

where

\[
m=\frac d2.
\]

This integral isolates the joint blow-up directly.

Its predicted exponent is

\[
\begin{cases}
m, & m(m-1)<1,\\[4pt]
1+\dfrac1m, & m(m-1)>1.
\end{cases}
\]

Independent numerical quadrature gives:

- \(d=3\), expected \(1.5\): small-\(s\) slopes approach \(1.5\);
- \(d=4\), expected \(1.5\): slopes approach \(1.5\);
- \(d=5\), expected \(1.4\): slopes approach \(1.4\);
- \(d=6\), expected \(4/3\): slopes agree with \(4/3\);
- \(d=8\), expected \(1.25\): slopes agree with \(1.25\) to numerical precision.

Since the full joint tail uses two such sides, this independently reproduces

\[
2+\frac4d
\]

for every tested \(d\ge4\).

## 6. Interpretation

The direct Monte Carlo and the reduced asymptotic integral are testing different regimes.

The first asks whether currently accessible \(\varepsilon\) is already asymptotic.

For high \(d\), the answer is no.

The second tests the local scaling after the correct blow-up has already been performed.

It agrees with the analytic theorem.

Thus the observed low effective slopes in \(d=6,8\) are a finite-window crossover, not a discovered lower-exponent sector.

## 7. Publication consequence

A future article should not validate the all-dimensional exponent by showing only a direct log-log Monte Carlo plot at moderate \(\varepsilon\).

That plot can look inconsistent with the theorem.

A responsible numerical section should instead show both:

1. the raw finite-\(\varepsilon\) data;
2. the reduced \(J_m\) scaling or an importance-sampled joint calculation.

The slow crossover itself is a useful result because it explains why brute-force numerical experiments in high dimension can misidentify the asymptotic exponent.

## 8. Reproducibility

The repository tool

tools/minkowski_edge_tail_preasymptotic_audit.py

implements both checks.

The full pair count is configurable because multi-million-pair runs are expensive.

No Monte Carlo result in this note is used as part of the proof of the all-dimensional theorem.
