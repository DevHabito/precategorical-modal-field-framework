# Cramer Reduction and the Total-Positivity Obstruction

**Programme:** Modal Field Research Programme  
**Provisional audit:** A69  
**Author line:** Felipe Gianini Romero  
**Status:** exact fixed-basis Cramer theorem, arithmetic-grid orientation audit, and exact obstruction to an order-only total-positivity proof

## Technical abstract

A68 identified the positive dual multiplier of the first observation as the
mechanism behind the boundary-anchor law. The proposed next step was to prove

\[
\lambda_\alpha^+>0
\]

directly from total positivity and contact order.

A69 shows that this proposal must be refined.

For any fixed active Charnes–Cooper basis, let

\[
s=2^{-\alpha}
\]

and write the active system as

\[
B(s,\varepsilon)z=b.
\]

The positive first-channel dual multiplier solves

\[
B(s,\varepsilon)^\top y=c_B.
\]

By Cramer's rule,

\[
\boxed{
\lambda_\alpha^+(s,\varepsilon)
=
\frac{
\Delta_\alpha(\varepsilon)
}{
\Delta(s,\varepsilon)
},
}
\]

where

\[
\Delta(s,\varepsilon)
=
\det B(s,\varepsilon)
\]

and \(\Delta_\alpha\) is obtained by replacing the active \(\alpha\)-row by the
basic objective row.

Two exact structural facts follow.

First,

\[
\boxed{
\frac{\partial\Delta_\alpha}{\partial s}=0.
}
\]

The only row depending on \(s\) is precisely the row replaced in the Cramer
numerator.

Second,

\[
\boxed{
\deg_\varepsilon\Delta_\alpha\le1.
}
\]

All tolerance dependence appears in the single scale column. A determinant
term can select that column only once, so the numerator is affine in the
common tolerance.

Consequently, at fixed \(\varepsilon\) with

\[
\Delta_\alpha(\varepsilon)\ne0,
\]

the multiplier cannot change sign while the same active basis remains
nonsingular:

\[
\boxed{
\operatorname{sgn}\lambda_\alpha^+
=
\operatorname{sgn}\Delta_\alpha
\operatorname{sgn}\Delta
}
\]

is constant on every connected nonsingular basis region.

This reduces the phasewise channel-sign problem from an arbitrary rational
function to:

1. one constant or affine numerator orientation;
2. one active-basis determinant orientation.

The result was verified exactly for all 33 phases of A67.

However, A69 also produces a rational counterexample to the stronger claim
that contact order alone determines the numerator sign.

The same contact signature

\[
P,B,Q,P,Q,P
\]

with active bands

\[
\alpha+,\quad\beta-,\quad\gamma+
\]

has positive numerator on the contacts

\[
(0,1,2,3,4,5)
\]

but negative numerator on

\[
(0,1,2,3,4,9).
\]

Both use the midpoint of the extreme contacts as the mean, exact
observations, target exponent \(1\), \(\beta=3\), and \(\gamma=10\).

Therefore:

\[
\boxed{
\text{contact order and abstract total positivity alone do not fix the
Cramer sign.}
}
\]

The mean/scale coupling between the upper and lower envelopes carries
additional geometric information.

The correct next structural target is narrower:

> exploit the arithmetic grid \(\{0,\ldots,M\}\), not arbitrary ordered
> contact nodes.

The likely tools are confluent \(q\)-Vandermonde determinants and
Schur-positive expansions.

---

## 1. Fixed-basis Cramer theorem

### Theorem 1.1

Consider an active basis in which:

1. only the positive \(\alpha\)-observation row depends on
   \[
   s=2^{-\alpha};
   \]
2. all observation tolerances enter through the single Charnes–Cooper scale
   column;
3. the active basis is nonsingular.

Then:

\[
\lambda_\alpha^+(s,\varepsilon)
=
\frac{
A+B\varepsilon
}{
\Delta(s,\varepsilon)
}
\]

for constants \(A,B\) independent of \(s\).

### Proof

The multiplier satisfies

\[
B^\top y=c_B.
\]

Cramer's rule replaces the column of \(B^\top\) corresponding to
\(\lambda_\alpha^+\). Equivalently, it replaces the \(\alpha\)-row of \(B\)
by \(c_B^\top\).

That replacement removes every occurrence of \(s\), since no other active
row depends on the first exponent.

The tolerance occurs only in the scale column. Every Leibniz term in a
determinant selects exactly one entry from each column, so at most one
tolerance-dependent scale entry can occur.

Hence the numerator is independent of \(s\) and affine in \(\varepsilon\).

### Corollary 1.2

If

\[
A+B\varepsilon\ne0,
\]

then the multiplier has no zero inside a connected region where

\[
\Delta(s,\varepsilon)\ne0.
\]

Any sign change requires at least one of:

1. a numerator tolerance threshold;
2. an active-basis singularity;
3. a change of active basis.

---

## 2. Exact A67 orientation audit

All 33 phases satisfy:

\[
\deg_s\Delta_\alpha=0,
\]

\[
\deg_\varepsilon\Delta_\alpha\le1,
\]

and the exact Cramer ratio equals the independently reconstructed dual
multiplier.

At the declared tolerances:

\[
\operatorname{sgn}
\Delta_\alpha
=
\operatorname{sgn}
\Delta
\]

in every phase.

Therefore:

\[
\lambda_\alpha^+>0
\]

in all 33 certified phase interiors.

The numerator orientations split as:

\[
21\text{ positive},
\qquad
12\text{ negative}.
\]

The multiplier is positive not because the numerator is always positive, but
because the basis determinant carries the same orientation.

This is an important distinction. A proof that ignores determinant
orientation is incomplete.

---

## 3. Tolerance robustness of the numerator

For 19 phases, the affine numerator has no positive root and its sign is
unchanged for every nonnegative tolerance.

Fourteen phases have a positive formal flip threshold

\[
\varepsilon_{\rm flip}
=
-\frac AB.
\]

The smallest ratio between that threshold and the declared tolerance is:

\[
\boxed{
\frac{
\varepsilon_{\rm flip}
}{
\varepsilon_{\rm declared}
}
=
102.44043276705599\ldots
}
\]

and occurs for:

\[
M=8,
\qquad
\text{phase }1.
\]

Thus every A67 Cramer numerator retains its orientation under at least a
\(102.44\)-fold enlargement of the declared common tolerance.

This is a numerator statement. It does not assert that the same basis remains
optimal, nonsingular, or identically oriented under such a large change in
the full optimization contract.

---

## 4. Contact-signature compression

The 33 phases reduce to 18 signatures when we retain only:

- the ordered \(P/Q/B\) contact labels;
- the active observation signs;
- the number of \(P\) and \(Q\) contacts.

Here \(B\) denotes a microscopic state appearing in both active supports.

| Class | Contact labels | Active bands | Instances | Numerator sign |
|---:|---:|---:|---:|---:|
| 1 | `PBQPQP` | alpha+, beta-, gamma+ | 1 | +1 |
| 2 | `PQBPQP` | alpha+, beta-, gamma+ | 3 | +1 |
| 3 | `PQBQQP` | alpha+, beta-, gamma+ | 2 | +1 |
| 4 | `PBBQP` | alpha+, beta-, gamma+ | 1 | +1 |
| 5 | `PBPQP` | alpha+, beta- | 1 | -1 |
| 6 | `QBPQP` | alpha+, beta- | 1 | -1 |
| 7 | `QBPQP` | alpha+, gamma- | 1 | -1 |
| 8 | `PPBPQP` | alpha+, beta-, gamma+ | 2 | +1 |
| 9 | `PQPBQP` | alpha+, beta-, gamma+ | 2 | +1 |
| 10 | `PQPQQP` | alpha+, beta- | 3 | +1 |
| 11 | `PQPQQP` | alpha+, gamma- | 4 | +1 |
| 12 | `QPBPQP` | alpha+, beta-, gamma+ | 1 | -1 |
| 13 | `QPQPQQP` | alpha+, beta-, gamma+ | 3 | -1 |
| 14 | `PPQPQQP` | alpha+, beta-, gamma+ | 2 | -1 |
| 15 | `PQQPQQP` | alpha+, beta-, gamma+ | 2 | +1 |
| 16 | `PQPPQQP` | alpha+, beta-, gamma+ | 1 | +1 |
| 17 | `PQPPQQP` | alpha+, beta-, gamma- | 2 | -1 |
| 18 | `QPQPPQP` | alpha+, beta-, gamma+ | 1 | -1 |

Ten signatures occur more than once. Within the arithmetic-grid A67 family,
every repeated signature has a consistent numerator orientation.

This is evidence of a hidden discrete orientation law, but it is not yet its
proof.

---

## 5. Why order-only total positivity fails

Consider the signature:

\[
P,B,Q,P,Q,P
\]

with:

\[
\alpha+,\quad\beta-,\quad\gamma+.
\]

For the uniformly spaced contacts

\[
X_{\rm uniform}
=
(0,1,2,3,4,5),
\]

the exact Cramer numerator is:

\[
\boxed{
\Delta_\alpha(X_{\rm uniform})
=
3022447223738387907/295147905179352825856
>0.
}
\]

For the stretched contacts

\[
X_{\rm stretched}
=
(0,1,2,3,4,9),
\]

the exact numerator is:

\[
\boxed{
\Delta_\alpha(X_{\rm stretched})
=
-3887828288997434151887072936457/324518553658426726783156020576256
<0.
}
\]

The order labels and active-band signs are unchanged. In each case the mean
is the midpoint of the smallest and largest contact.

Therefore no theorem based only on:

- ordering of the contacts;
- ordering of the exponents;
- the ordinary strict total positivity of \(e^{-\lambda x}\);

can determine the sign of the coupled Cramer numerator.

The obstruction is the upper/lower-envelope coupling through:

\[
\mathbb E[X]=m
\]

and the shared scale column.

Total positivity remains relevant, but additional arithmetic or metric
structure is necessary.

---

## 6. Why the phase partition remains necessary

Although the numerator has no \(s\)-dependence, the basis determinant does.

Among the 33 A67 active bases:

\[
\boxed{
17
}
\]

have a determinant root somewhere in the full nominal interval

\[
s\in\left[\frac18,\frac14\right].
\]

Those roots lie outside the phase where the corresponding basis is certified,
or at an excluded rank boundary.

This shows that one cannot take a basis discovered in one phase and extend its
orientation across the full \(\alpha\)-domain.

The phase decomposition in A66–A67 was not merely a computational
convenience. It is mathematically necessary.

---

## 7. Complete phase table

| \(M\) | Phase | \(\operatorname{sgn}\Delta_\alpha\) | \(\operatorname{sgn}\Delta\) | Degree in \(\varepsilon\) | Flip margin | Full-domain roots |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 1 | +1 | +1 | 1 | ∞ | 0 |
| 5 | 2 | +1 | +1 | 1 | ∞ | 0 |
| 5 | 3 | +1 | +1 | 1 | ∞ | 1 |
| 5 | 4 | +1 | +1 | 1 | ∞ | 0 |
| 5 | 5 | -1 | -1 | 0 | ∞ | 1 |
| 5 | 6 | -1 | -1 | 1 | ∞ | 0 |
| 5 | 7 | -1 | -1 | 1 | ∞ | 0 |
| 6 | 1 | +1 | +1 | 0 | ∞ | 1 |
| 6 | 2 | +1 | +1 | 1 | ∞ | 0 |
| 6 | 3 | +1 | +1 | 1 | ∞ | 1 |
| 6 | 4 | +1 | +1 | 1 | ∞ | 0 |
| 6 | 5 | +1 | +1 | 1 | 1693.4967041015625000000000000000000000000000000000 | 1 |
| 6 | 6 | +1 | +1 | 1 | 2143.0798806250095367431640625000000000000000000000 | 0 |
| 7 | 1 | -1 | -1 | 1 | 479.70603572842372345499070288344577396485850699561 | 1 |
| 7 | 2 | +1 | +1 | 0 | ∞ | 1 |
| 7 | 3 | +1 | +1 | 1 | ∞ | 0 |
| 7 | 4 | +1 | +1 | 1 | ∞ | 0 |
| 7 | 5 | +1 | +1 | 1 | 2108.9155936355225777511961722488038277511961722488 | 1 |
| 7 | 6 | +1 | +1 | 1 | 2442.6720287811242792594946172248803827751196172249 | 0 |
| 8 | 1 | -1 | -1 | 1 | 102.44043276705599181742846577437647611401080656777 | 1 |
| 8 | 2 | -1 | -1 | 1 | 122.62469479081519069753024006056431878470894304856 | 1 |
| 8 | 3 | +1 | +1 | 1 | ∞ | 1 |
| 8 | 4 | +1 | +1 | 1 | ∞ | 0 |
| 8 | 5 | -1 | -1 | 1 | ∞ | 0 |
| 8 | 6 | +1 | +1 | 1 | 3543.1548489623092578358627392344497607655502392344 | 0 |
| 9 | 1 | -1 | -1 | 1 | 145.77181257384740680747041472387331040408626019530 | 1 |
| 9 | 2 | -1 | -1 | 1 | 690.30426067075989165702606004732402952004951084998 | 1 |
| 9 | 3 | -1 | -1 | 1 | 133.76340309164348735790394974866327282041430538213 | 1 |
| 9 | 4 | -1 | -1 | 1 | 158.78679067598901807706029701044763269402340390198 | 1 |
| 9 | 5 | +1 | +1 | 1 | ∞ | 1 |
| 9 | 6 | +1 | +1 | 1 | 1945.0931498073639079211229946524064171122994652406 | 1 |
| 9 | 7 | -1 | -1 | 1 | ∞ | 0 |
| 9 | 8 | +1 | +1 | 1 | 4509.2616497499398960065937847235190856801374467767 | 0 |

The symbol \(\infty\) in the flip-margin column means that the affine
numerator has no positive zero.

---

## 8. What A69 proves

### Exact general result

For any fixed active basis of the declared type:

\[
\boxed{
\lambda_\alpha^+
=
\frac{
A+B\varepsilon
}{
\Delta(s,\varepsilon)
}.
}
\]

The multiplier has no internal zero in \(s\) while the basis remains
nonsingular.

### Exact family result

For all 33 A67 phases:

- the Cramer identity holds;
- the numerator is independent of \(\alpha\);
- the numerator is affine in tolerance;
- numerator and denominator orientations match;
- the multiplier is positive;
- numerator orientation has a large declared-noise margin.

### Exact negative result

An order-only total-positivity theorem is false for arbitrary contact
locations, even with:

- integer contacts;
- the same contact signature;
- the same active-band signs;
- a central mean rule;
- exact observations.

---

## 9. What remains open

A69 does not establish:

1. a direct sign formula for every arithmetic-grid contact pattern;
2. positivity for arbitrary support size \(M\);
3. an induction in \(M\);
4. a Schur-positive factorization of the Cramer determinants;
5. positivity when the mean is not central;
6. a theorem under separate or correlated channel tolerances.

---

## 10. Next rigorous target

The failed order-only conjecture tells us exactly what the next proof must use.

On the arithmetic support:

\[
x=0,1,\ldots,M,
\]

the exponential columns are geometric:

\[
2^{-\lambda x}
=
q_\lambda^x.
\]

Generalized Vandermonde minors on integer exponents admit factorizations of
the form:

\[
\det(q_j^{x_i})
=
V(q_1,\ldots,q_r)
\,s_\nu(q_1,\ldots,q_r),
\]

where \(V\) is a Vandermonde determinant and \(s_\nu\) is a Schur polynomial
with nonnegative coefficients.

The next audit should:

1. eliminate the scale column from \(\Delta_\alpha\);
2. expand the result into generalized \(q\)-Vandermonde minors;
3. express those minors as Vandermonde factors times Schur polynomials;
4. test whether the central-mean arithmetic-grid combinations have one fixed
   sign;
5. identify the precise combinatorial condition on the \(P/Q\) contact
   pattern.

That route uses the extra structure that the exact counterexample shows is
indispensable.
