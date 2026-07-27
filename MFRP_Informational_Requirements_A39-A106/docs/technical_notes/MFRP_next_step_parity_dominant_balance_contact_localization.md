# Parity-Resolved Dominant Balance and Asymptotic Contact Localization

**Programme:** Modal Field Research Programme  
**Audit:** A85  
**Author line:** Felipe Gianini Romero  
**Status:** analytic asymptotic localization plus finite exact transition-bracket certificates

## Technical abstract

A84 represented each adjacent compressed-objective difference as a ten-term confluent exponential polynomial in the discrete contact variable `k`. The coefficient sequence has seven sign variations, so a coefficient-only variation-diminishing argument cannot establish the observed single transition. A85 takes a different route: it identifies the channels that control the sign at the actual transition and derives their parity-dependent asymptotic balance.

For the A84 contract, the exact factor is decomposed into a four-term core

\[
(\beta t)^k,\qquad (st)^k,\qquad t^k,\qquad k t^k,
\]

with their exact coefficients, plus a six-term residual. At the two adjacent factors bracketing every exact A84 maximizer, rational arithmetic verifies 1,746 core/residual comparisons. From \(M=13\) through \(M=300\), the four-term core strictly dominates its residual and therefore determines every transition-bracket sign. At the smallest supports this statement is not universal: \(M=12\), \(s=129/1000\), \(k=3\) is an exact sign counterexample, and the same support at \(s=131/1000\) also fails strict magnitude dominance without flipping the sign. An eight-term fallback, omitting only \((\beta s)^k\) and the constant term, strictly dominates at all 1,746 audited factors.

The parity expansion gives

\[
C_{\rm even}(s)=s-\beta-\frac{2}{1875},
\qquad
C_{\rm odd}(s)=\frac34(s-\beta)-\frac{1}{1250}.
\]

With \(h=\lfloor M/2\rfloor\) and \(u=2^{-h}\),

\[
c_{kt}=\frac{C_p(s)}{M}u+o\!\left(\frac{u}{M}\right),
\]

\[
c_t=-\frac{M-2}{M}C_p(s)u+o(u).
\]

After division by \(t^k\), the dominant positive channel is proportional to \(s^k\), while the dominant negative target-affine channel is proportional to \(2^{-\lfloor M/2\rfloor}\). Their exponential rates are equal at

\[
\boxed{
\frac{k}{M}\longrightarrow
c(s)=\frac{\log 2}{-2\log s}
}.
\]

This establishes asymptotic localization of any sign-transition sequence under the declared reduced contract. It does not by itself prove unique all-\(M\) unimodality.

---

## 1. Contract inherited from A84

The fixed constants are

\[
\beta=\frac18,
\qquad
t=\frac12,
\]

and the three rational probes are

\[
s\in\left\{
\frac{129}{1000},
\frac{131}{1000},
\frac{133}{1000}
\right\}.
\]

The support range is

\[
10\le M\le300,
\]

with

\[
h=\left\lfloor\frac M2\right\rfloor.
\]

The normalized error remains

\[
\varepsilon_M=
\begin{cases}
\dfrac{1}{1875\,2^h},&M\text{ even},\\[6pt]
\dfrac{1}{2500\,2^h},&M\text{ odd}.
\end{cases}
\]

For each \((M,s)\), A84 supplies the exact compressed maximizer \(k^\star\). A85 evaluates only the two adjacent factors

\[
E_{M,k^\star-1}(s),
\qquad
E_{M,k^\star}(s),
\]

when both lie in the admissible contact range. These are precisely the factors that bracket the positive-to-negative transition recorded by A84.

---

## 2. Exact core decomposition

Write the A84 ten-term factor in the declared order:

\[
\begin{aligned}
E_{M,k}(s)={}&
 c_{\beta s}(\beta s)^k
+c_{\beta t}(\beta t)^k
+c_{st}(st)^k\\
&+(c_\beta+k c_{k\beta})\beta^k
+(c_s+k c_{ks})s^k\\
&+(c_t+k c_{kt})t^k+c_1.
\end{aligned}
\]

Define the four-term core

\[
K^{(4)}_{M,k}(s)=
 c_{\beta t}(\beta t)^k
+c_{st}(st)^k
+c_t t^k
+k c_{kt}t^k,
\]

and residual

\[
R^{(6)}_{M,k}(s)=E_{M,k}(s)-K^{(4)}_{M,k}(s).
\]

Whenever

\[
\left|K^{(4)}_{M,k}(s)\right|>
\left|R^{(6)}_{M,k}(s)\right|,
\]

the core and full factor have the same sign by the triangle inequality.

A finite fallback is also defined:

\[
K^{(8)}_{M,k}(s)=
E_{M,k}(s)-c_{\beta s}(\beta s)^k-c_1.
\]

Its residual contains only the fastest product node and the constant term.

---

## 3. Exact finite result

Across all 291 support sizes and all three probes, A85 evaluates

\[
291\times3\times2=1746
\]

transition-bracket factors.

### 3.1 Four-term core

The four-term core has exactly one sign mismatch:

\[
M=12,
\qquad
s=\frac{129}{1000},
\qquad
k=3.
\]

At this cell,

\[
\operatorname{sgn}K^{(4)}=+1,
\qquad
\operatorname{sgn}E=-1,
\]

and

\[
\frac{|K^{(4)}|}{|R^{(6)}|}
=0.4808973678301384863\ldots<1.
\]

There are exactly two failures of strict four-term magnitude dominance:

\[
(M,s,k)=
\left(12,\frac{129}{1000},3\right),
\]

and

\[
(M,s,k)=
\left(12,\frac{131}{1000},3\right).
\]

The second cell does not flip the sign, but the core alone is not protected by the triangle inequality.

For every transition-bracket factor with

\[
13\le M\le300,
\]

strict dominance holds. The smallest exact ratio in that range is

\[
\frac{|K^{(4)}|}{|R^{(6)}|}
=1.2440532584425797076\ldots
\]

at

\[
M=17,
\qquad
s=\frac{129}{1000},
\qquad
k=4.
\]

Thus the four-term core determines all exact transition-bracket signs from \(M=13\) through \(M=300\) at the three declared probes.

### 3.2 Eight-term fallback

The eight-term core matches the full sign in

\[
1746/1746
\]

cases and strictly dominates its two-term residual in

\[
1746/1746
\]

cases.

Its weakest margin occurs at the same small-support counterexample:

\[
\frac{|K^{(8)}|}{|E-K^{(8)}|}
=28.386750733172705156\ldots.
\]

This fallback is exact and useful, but it should not be confused with the asymptotic four-channel explanation.

---

## 4. Parity expansion

Set

\[
u=2^{-h}.
\]

For fixed \(r<1/2\), the terms \(r^h\) and \(r^M\) are \(o(u)\). The A67–A84 `D`-block therefore has the parity expansions

\[
D_M(r)=-2ur+o(u)
\qquad(M=2h),
\]

and

\[
D_M(r)=-\frac32ur+o(u)
\qquad(M=2h+1).
\]

The beta channel uses the opposite error-band sign from the released `s` channel. Consequently:

### Even supports

\[
H_\beta
=\frac12+u\left(2\beta+\frac{2}{1875}\right)+o(u),
\]

\[
H_s
=\frac12+u\left(2s-\frac{2}{1875}\right)+o(u).
\]

Hence

\[
H_s-H_\beta
=2u\left(s-\beta-\frac{2}{1875}\right)+o(u)
=2uC_{\rm even}(s)+o(u).
\]

### Odd supports

\[
H_\beta
=\frac12+u\left(\frac32\beta+\frac{2}{2500}\right)+o(u),
\]

\[
H_s
=\frac12+u\left(\frac32s-\frac{2}{2500}\right)+o(u),
\]

so

\[
H_s-H_\beta
=2u\left(\frac34(s-\beta)-\frac{1}{1250}\right)+o(u)
=2uC_{\rm odd}(s)+o(u).
\]

Both constants are positive throughout the declared probe interval. At the central probe,

\[
C_{\rm even}\left(\frac{131}{1000}\right)=\frac{37}{7500},
\]

\[
C_{\rm odd}\left(\frac{131}{1000}\right)=\frac{37}{10000}.
\]

These are the constants numerically visible in the A84 target-affine coefficients.

---

## 5. Leading target-affine coefficients

At leading order,

\[
a_r=\frac{1-r^M}{M}=\frac1M+o\left(\frac{u}{M}\right).
\]

Substitution into the exact A84 coefficient formulas gives

\[
c_{kt}
=(t-1)(H_\beta a_s-H_s a_\beta)
=\frac{C_p(s)}{M}u+o\left(\frac{u}{M}\right).
\]

The nonconfluent target coefficient satisfies

\[
c_t
=-\frac{M-2}{M}C_p(s)u+o(u).
\]

Therefore

\[
c_t+k c_{kt}
=-C_p(s)u\left(1-\frac{k+2}{M}\right)+o(u).
\]

For contacts with \(k/M\) bounded strictly below \(1/2\), this target-affine channel is asymptotically negative.

The positive product channel is

\[
c_{st}(st)^k
=\left(\frac{t-s}{2}+o(1)\right)(st)^k.
\]

After division by \(t^k>0\), the two leading scales are

\[
\frac{t-s}{2}s^k
\]

and

\[
-C_p(s)2^{-\lfloor M/2\rfloor}
\left(1-\frac{k}{M}\right).
\]

The beta-product channel is smaller by the factor

\[
\left(\frac{\beta}{s}\right)^k,
\]

and the remaining six terms have strictly smaller exponential order under proportional contact scaling.

---

## 6. Asymptotic contact slope

Let

\[
k=xM+O(1).
\]

The positive scale is

\[
s^{xM},
\]

while the target-affine scale is

\[
2^{-M/2}
\]

up to parity and subexponential factors. Equality of exponential rates requires

\[
x\log s=-\frac12\log 2.
\]

Therefore

\[
\boxed{
c(s)=\frac{\log2}{-2\log s}
}.
\]

For any fixed \(\delta>0\):

- when \(k/M\le c(s)-\delta\), the positive \(s^k\) channel decays more slowly and eventually dominates;
- when \(k/M\ge c(s)+\delta\), the negative \(2^{-M/2}\) target-affine channel decays more slowly and eventually dominates.

Thus any sequence of adjacent factors at which the sign transition occurs satisfies

\[
\frac{k_M}{M}\longrightarrow c(s).
\]

This is an asymptotic localization theorem. It does not assert that every finite sequence has only one sign transition.

---

## 7. Parity-resolved constant offset

Keeping the leading amplitudes gives a refined continuous prediction.

Let

\[
A(s)=\frac{1/2-s}{2}.
\]

For even \(M\), write

\[
k=c(s)M+d_{\rm even}(s).
\]

Since

\[
s^{c(s)M}=2^{-M/2},
\]

the leading balance yields

\[
\boxed{
d_{\rm even}(s)=
\frac{
\log\left(\dfrac{C_{\rm even}(s)(1-c(s))}{A(s)}\right)
}{\log s}
}.
\]

For odd \(M\),

\[
2^{-\lfloor M/2\rfloor}=\sqrt2\,2^{-M/2},
\]

so

\[
\boxed{
d_{\rm odd}(s)=
\frac{
\log\left(\dfrac{\sqrt2\,C_{\rm odd}(s)(1-c(s))}{A(s)}\right)
}{\log s}
}.
\]

At the central probe:

\[
c=0.1705110495345290147\ldots,
\]

\[
d_{\rm even}=1.8737866985309715917\ldots,
\]

\[
d_{\rm odd}=1.8448126081928865541\ldots.
\]

Using 80-digit arithmetic as a numerical diagnostic, the predictor

\[
\widehat{k}_M=c(s)M+d_p(s)
\]

lies within one integer contact of every exact A84 maximizer for

\[
13\le M\le300
\]

at all three probes:

\[
864/864.
\]

The largest absolute discrepancies are:

- \(0.9636039742\ldots\) at \(M=17\), \(s=129/1000\);
- \(0.9466929679\ldots\) at \(M=271\), \(s=131/1000\);
- \(0.9769926719\ldots\) at \(M=293\), \(s=133/1000\).

Because this check uses numerical logarithms rather than interval-certified transcendental bounds, it is not promoted to an exact theorem.

---

## 8. What A85 establishes

1. An exact core/residual decomposition at all A84 transition brackets.
2. Exact four-term sign determination at all declared brackets for \(13\le M\le300\).
3. An explicit small-support counterexample to universal four-term dominance.
4. An exact eight-term fallback at all 1,746 brackets.
5. Parity-specific leading constants for the target-affine channel.
6. The asymptotic contact slope
   \[
   k/M\to\log2/(-2\log s).
   \]
7. A parity-resolved constant-offset predictor consistent with all exact A84 maximizers from \(M=13\) through \(M=300\).

---

## 9. What A85 does not establish

A85 does not prove:

1. unique sign variation for every integer \(M\);
2. global four-term dominance for every adjacent contact;
3. an exact rounding rule for \(k^\star(M,s)\);
4. a periodic sequence of block lengths;
5. validity outside the declared reduced contract;
6. a physical interpretation of the support, contact, or observation channels.

The next rigorous target is to convert the asymptotic rate separation into explicit finite thresholds. A suitable A86 would seek computable functions \(M_0(\delta,s,p)\) such that the sign is certified outside the strip

\[
\left|\frac{k}{M}-c(s)\right|<\delta
\]

for every \(M\ge M_0\), while treating the remaining \(O(\delta M)\) central strip separately. That would move from asymptotic localization to a quantitative all-support exclusion theorem without assuming unique unimodality.
