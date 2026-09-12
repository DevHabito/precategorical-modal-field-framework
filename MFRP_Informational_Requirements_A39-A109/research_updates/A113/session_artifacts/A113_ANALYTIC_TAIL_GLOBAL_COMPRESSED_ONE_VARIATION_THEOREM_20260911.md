# A113 — Analytic tail global compressed one-variation theorem

## Status

**PROVED for the frozen reduced/compressed contract.**

Domain:

\[
M\ge521,\qquad \frac{129}{1000}\le s\le\frac{133}{1000},
\qquad \beta=\frac18,\quad \tau=\frac12.
\]

Let

\[
c(s)=\frac{\log2}{-2\log s},\qquad b=\lceil Mc(s)\rceil,
\]

and let

\[
E_{M,k}(s)=V_{M,k+1}(s)-V_{M,k}(s)
\]

be the exact A84 adjacent compressed-objective factor.

This theorem concerns the **compressed objective**. It does not by itself select the globally optimal lifted LP active-set architecture.

## The theorem

For every admissible contact index under the frozen A84 reduced contract,

\[
\boxed{E_{M,k}(s)>0\qquad(k\le b),}
\]

and

\[
\boxed{E_{M,k}(s)<0\qquad(k\ge b+3).}
\]

The two central factors obey the strict nesting inequality

\[
\boxed{E_{M,b+1}(s)-2E_{M,b+2}(s)>0.}
\]

Hence the forbidden central pattern

\[
E_{M,b+1}<0<E_{M,b+2}
\]

cannot occur. The complete adjacent-factor sequence therefore has exactly one positive-to-negative variation.

Consequently the global compressed maximizer belongs to

\[
\boxed{\{b+1,b+2,b+3\}},
\]

with only adjacent central ties possible when one of the two central factors vanishes.

## Why the central inequality is the right one

A tempting stronger target was the second-secant inequality

\[
E_{b+1}-E_{b+2}>0.
\]

That statement is false in the deep tail. An exact example is

\[
M=2049,\qquad s=133/1000,
\]

where both central factors are negative but

\[
E_{b+1}-E_{b+2}<0.
\]

The successful quantity is instead

\[
J=E_{b+1}-2E_{b+2}.
\]

The factor 2 is structural: because the target node is \(\tau=1/2\), the large nonconfluent part of the target-affine channel cancels exactly in \(J\). Only its \(O(U/M)\) slope remains.

Thus \(J>0\) is weaker than false global local-monotonicity, but exactly strong enough to rule out a second sign reversal.

## Proof architecture

Write the exact A84 ten-term factor as

\[
\begin{aligned}
E_k={}&A(s-\beta)(\beta s)^k
+H_s(\beta-\tau)(\beta\tau)^k
+H_\beta(\tau-s)(s\tau)^k\\
&+(c_\beta+k c_{k\beta})\beta^k
 +(c_s+k c_{ks})s^k
 +(c_\tau+k c_{k\tau})\tau^k+c_1.
\end{aligned}
\]

Set

\[
h=\lfloor M/2\rfloor,\qquad U=2^{-h}.
\]

The hardened certificate derives, uniformly for the complete tail,

\[
0.49<H_\beta,H_s<0.51,
\]

\[
0.0044<\frac{H_s-H_\beta}{U}<0.013866\ldots,
\]

and exact uniform bounds for the affine and constant channels.

### 1. Small left contacts

For \(k\le29\), set \(U=0\). The remaining core factors exactly as

\[
\frac12(s-\beta)(\tau-\beta)(\tau-s)
 h_{k-1}(\beta s,\beta\tau,s\tau)>0,
\]

where \(h_n\) is the complete homogeneous symmetric polynomial.

The certificate verifies this factorization symbolically for every \(k=1,\ldots,29\). Its uniform lower bound is

\[
1.2805582470\ldots\times10^{-37},
\]

while the complete finite-\(U\) perturbation is less than one copy of

\[
U\le2^{-260}\approx5.4\times10^{-79}.
\]

Hence all admissible small-left factors are positive.

### 2. Middle left contacts

For \(30\le k\le b\), divide by \(U\tau^k>0\). The product channels give a uniform positive lower core. The target-affine, beta/source-affine, and constant channels are then subtracted by exact rational majorants.

The remaining certified margin is

\[
\boxed{0.002525932971282254\ldots>0.}
\]

Therefore

\[
E_k>0\qquad(30\le k\le b).
\]

### 3. Right remote contacts

For \(k\ge b+3\), divide \(-E_k\) by \(U\tau^k\). The positive contribution now comes from the target-affine channel because

\[
\frac{H_s-H_\beta}{U}>0.
\]

The source/product and affine tails are bounded above. The final conservative gap is

\[
\boxed{0.00062985755323\ldots>0.}
\]

so

\[
E_k<0\qquad(k\ge b+3).
\]

### 4. Central nesting

For

\[
J=E_{b+1}-2E_{b+2},
\]

the target-affine transform is

\[
(c+k d)\tau^k-2(c+(k+1)d)\tau^{k+1}=-d\tau^k
\]

because \(2\tau=1\).

After bounding the remaining channels, the exact rational lower margin is

\[
\boxed{0.001148865057514029\ldots>0.}
\]

and therefore \(J>0\) uniformly.

## Independent reconstruction

A separate script reconstructs every checked factor in two ways without importing the A113 certificate:

1. the original reduced cofactor form
   \[
   X\,\Delta B_s+Y\,B_s+W\,H_s;
   \]
2. the independent A84 ten-term k-space expansion.

The values agree exactly as `Fraction` objects.

The replication covers 34 exact cases, five complete sign sequences, both parities, both source endpoints, several interior rational probes, and the deliberately adversarial cases below.

## Preserved adversarial facts

### `b+3` does not disappear in the tail

The stronger claim that the tail maximizer is always only `b+1` or `b+2` is false.

At

\[
M=561,\qquad s=129/1000,
\]

one has exactly

\[
E_{b+2}>0,
\]

so the compressed maximizer is `b+3`.

### The second secant is not uniformly positive

At

\[
M=2049,\qquad s=133/1000,
\]

one has exactly

\[
E_{b+1}<0,\qquad E_{b+2}<0,
\]

but

\[
E_{b+1}-E_{b+2}<0.
\]

Thus no proof of A113 may rely on global/local monotonicity of the factor sequence.

## Combination with A94

A94 already proves complete compressed-objective one-variation for every real source value in the same window and every effective finite support

\[
14\le M\le520.
\]

A113 proves the analytic tail

\[
M\ge521.
\]

Therefore A94 + A113 establish, under the frozen reduced/compressed contract,

\[
\boxed{
M\ge14,\quad 129/1000\le s\le133/1000
\Longrightarrow
\text{the complete compressed adjacent-factor sequence has one variation.}
}
\]

The global compressed maximizer is always among

\[
\boxed{\{b+1,b+2,b+3\}}.
\]

This is an all-support-size theorem for the **compressed objective in the declared source window**, not an all-architecture theorem for the lifted LP.

## What remains open

The next problem is the lift.

A112 proves that inside a strict gamma-plus compressed phase, the corresponding lifted basis is strict KKT exactly where the two adjacent masses are positive. A112-A additionally shows that such a strict gamma-plus KKT point in the tail can occur only for

\[
j=b+1\quad\text{or}\quad j=b+2.
\]

A113 shows that the global compressed maximizer may also be

\[
j=b+3.
\]

Therefore a `b+3` compressed phase cannot itself lift to a strict gamma-plus KKT basis of the A112 form. Determining which alternative lifted architecture is selected there — and what happens when the `b+1`/`b+2` gamma-plus masses lose positivity — is the next genuinely global active-set problem.

## Claim boundary

A113 does **not** prove:

- global selection among all lifted LP active-set architectures;
- that every global compressed maximizer lifts to a gamma-plus KKT basis;
- monotonicity of `E_(M,k)` in `k`;
- positivity of `E_(b+1)-E_(b+2)`;
- disappearance of the `b+3` phase;
- anything outside the source window `[0.129,0.133]`;
- any physical interpretation.
