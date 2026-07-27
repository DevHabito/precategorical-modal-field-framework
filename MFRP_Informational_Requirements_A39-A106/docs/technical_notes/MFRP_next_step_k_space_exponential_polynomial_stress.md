# A84 — k-Space Exponential-Polynomial Reduction and Finite One-Variation Stress

**Programme:** Modal Field Research Programme  
**Audit:** A84  
**Status:** exact algebraic reduction; exact finite pointwise stress for `10 <= M <= 300` at three rational probes

## 1. Question

A83 proved that each adjacent compressed-objective difference has a seven-term polynomial factor in the observation variable `s`, and that the adjacent-difference sequence has one sign variation for `10 <= M <= 80` throughout the audited local interval except at two exact ties.

A84 asks a different structural question:

> When `s` is fixed and the contact `k` varies, can the same adjacent factor be written in a form suited to a variation-diminishing argument, and does that argument itself explain the observed one-sign-variation law?

The answer has two parts:

1. there is an exact ten-term confluent exponential-polynomial representation in `k`;
2. its coefficient sign pattern has seven variations, so coefficient variation alone is too weak to prove a single variation in the evaluated sequence.

The finite one-variation property nevertheless survives an exact stress from `M=80` through `M=300` at three rational probes.

## 2. Exact k-space representation

Let

\[
b=\beta=\frac18,\qquad t=\frac12,
\]

and define

\[
a_r=\frac{1-r^M}{M}.
\]

For fixed `M` and fixed `s`, write

\[
B_k(r)=r^k-1+k a_r,
\]

\[
\delta B_k(r)=(r-1)r^k+a_r.
\]

With the A83 cofactors

\[
X=A_tB_k(b)-H_bB_k(t),
\]

\[
Y=-A_t\delta B_k(b)+H_b\delta B_k(t),
\]

\[
W=-B_k(b)\delta B_k(t)+B_k(t)\delta B_k(b),
\]

the seven-term factor is

\[
E_{M,k}(s)=X\delta B_k(s)+YB_k(s)+WH_s.
\]

Expanding in the discrete variable `k` gives the exact identity

\[
\begin{aligned}
E_{M,k}(s)= {}& c_{bs}(bs)^k+c_{bt}(bt)^k+c_{st}(st)^k\\
&+(c_b+k c_{kb})b^k+(c_s+k c_{ks})s^k\\
&+(c_t+k c_{kt})t^k+c_1.
\end{aligned}
\]

The coefficients are

\[
c_{bs}=A_t(s-b),
\]

\[
c_{bt}=H_s(b-t),
\]

\[
c_{st}=H_b(t-s),
\]

\[
c_{kb}=-(b-1)(A_ta_s-H_sa_t),
\]

\[
c_b=A_ta_s+A_tb-A_t-H_sa_t-H_sb+H_s,
\]

\[
c_{kt}=(t-1)(H_ba_s-H_sa_b),
\]

\[
c_t=-H_ba_s-H_bt+H_b+H_sa_b+H_st-H_s,
\]

\[
c_{ks}=(s-1)(A_ta_b-H_ba_t),
\]

\[
c_s=-A_ta_b-A_ts+A_t+H_ba_t+H_bs-H_b,
\]

\[
c_1=-A_ta_s+A_ta_b+H_ba_s-H_ba_t-H_sa_b+H_sa_t.
\]

A symbolic expansion independent of the finite scan verifies this identity exactly.

## 3. Fixed coefficient sign pattern

At each of the three exact probes

\[
s\in\left\{\frac{129}{1000},\frac{131}{1000},\frac{133}{1000}\right\},
\]

the nodes satisfy

\[
bs<bt<st<b<s<t<1.
\]

In the declared confluent-node order

\[
(bs)^k,(bt)^k,(st)^k,b^k,kb^k,s^k,ks^k,t^k,kt^k,1,
\]

the exact coefficient signs are

\[
\boxed{+,-,+,+,-,-,+,-,+,-}.
\]

This pattern was reproduced for all

\[
291\times3=873
\]

support/probe coefficient vectors.

It has exactly seven sign variations. Therefore a direct generalized-Descartes or variation-diminishing bound based only on this coefficient sequence permits up to seven zeros or sign changes. It cannot by itself imply the observed single sign variation.

This is an obstruction to the proposed proof route, not a disproof of the one-variation property.

## 4. Exact finite stress through M=300

The audit covers

\[
10\le M\le300,
\qquad
2\le k<\left\lfloor\frac M2\right\rfloor-1.
\]

It evaluates exactly

\[
\boxed{21,607\text{ adjacent pairs}}
\]

at three rational probes, for

\[
\boxed{64,821\text{ exact adjacent signs}}.
\]

Every one of the

\[
\boxed{873\text{ support/probe sequences}}
\]

has the strict pattern

\[
+,+,\ldots,+,-,\ldots,-,
\]

with exactly one sign variation and no zero value.

Thus each audited support has one strict compressed maximizer at each of the three probes.

This is a finite pointwise theorem. It is not a theorem on every `s` between the probes.

## 5. Endpoint crossings

Among the 21,607 adjacent factors, exactly 51 have opposite signs at the two local endpoints:

- 50 have direction `negative -> positive`;
- one, the already known `M=28` case, has direction `positive -> negative`.

For each of these factors, continuity guarantees at least one root in

\[
\left(\frac{129}{1000},\frac{133}{1000}\right).
\]

A84 does not isolate those roots and does not exclude multiple roots. The complete interval atlas of A83 therefore remains complete only through `M=80`.

## 6. Probe contact blocks

At

\[
s_0=\frac{131}{1000},
\]

the unique maximizing contact forms 51 consecutive support blocks through `M=300`:

- 38 blocks have length 6;
- 12 blocks have length 5;
- the initial block has length 3.

The predominance of lengths 5 and 6 is descriptive. No periodic or Beatty-type law is inferred.

## 7. What A84 proves

1. An exact ten-term confluent exponential-polynomial identity in the discrete contact `k`.
2. A fixed ten-coefficient sign pattern at 873 exact support/probe contracts.
3. Seven coefficient sign variations, showing that the naive variation-diminishing route is insufficient.
4. Exact one-sign-variation sequences for all `10 <= M <= 300` at all three rational probes.
5. Exact recovery of 51 endpoint-crossing factors and 51 probe contact blocks.

## 8. What A84 does not prove

A84 does not prove:

1. the one-sign-variation law for arbitrary `M`;
2. the law for every `s` in the local interval beyond `M=80`;
3. uniqueness of the 51 implied interior roots;
4. a periodic contact-selection rule;
5. that total positivity is irrelevant—only that the raw coefficient-variation bound is too weak;
6. any physical interpretation of contacts, compression, or observation channels.

## 9. Next rigorous target

A85 should search for an inequality stronger than raw coefficient variation. A legitimate target is a sign-preserving comparison of neighboring terms or a domination theorem separating the pre-transition and post-transition regions in `k`.

The target must allow failure. The exact stress through `M=300` is evidence for a finite structural regularity, not permission to state an unrestricted theorem.
