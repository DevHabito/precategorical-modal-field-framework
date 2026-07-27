# Continuous Release of the First Target-Excluding Anchor

**Programme:** Modal Field Research Programme  
**Provisional audit:** A50  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous controlled continuation of MFRP-TR-2026-01 and A39–A49; no physical design claim

## Technical abstract

A49 showed by exhaustive integer-catalogue optimization that the lower anchor pair
\(\{2,3\}\log2\) is selected at both audited contracts. The present audit tests whether the
first anchor \(2\log2\) is merely the best integer point or remains optimal when released
continuously.

The target remains \(L(\log2)\), so a target-exclusion distance of one exponent unit is
declared:

\[
2\le\alpha\le3.
\]

Two controlled contracts are studied.

### Exact-data contract

\[
D_0(\alpha)=\{\alpha,3,4\}\log2.
\]

The third point \(4\log2\) is the exact-data catalogue winner from A43 and A49.

### Positive-noise contract

\[
D_\varepsilon(\alpha)=
\{\alpha,3,\infty\}\log2,
\qquad
\varepsilon=10^{-4}.
\]

The compactified third observation is the globally optimal continuous endpoint proved in
A44–A47.

The microscopic support and exact mean remain

\[
\operatorname{supp}P\subseteq\{0,1,2,3,4,5\},
\qquad
\mathbb E[X]=\frac52.
\]

Set

\[
s=2^{-\alpha}.
\]

Then

\[
\alpha\in[2,3]
\quad\Longleftrightarrow\quad
s\in[1/8,1/4].
\]

For exact data and \(2\le\alpha<3\), the direct minimax ratio has the closed form

\[
\boxed{
\rho_0(\alpha)
=
\frac{5(392s+779)}
{2(1043s+1916)}.
}
\]

Its derivative is

\[
\frac{d\rho_0}{ds}
=
-\frac{307125}
{2(1043s+1916)^2}<0.
\]

Since \(ds/d\alpha<0\),

\[
\frac{d\rho_0}{d\alpha}>0.
\]

Thus \(\alpha=2\) is the unique minimizer on the distinct-anchor domain. Its ratio is

\[
\boxed{
\rho_0(2)=\frac{8770}{8707}.
}
\]

At the duplicated endpoint \(\alpha=3\), the first and second observations coincide. The
actual exact-data ratio is

\[
\boxed{
\rho_0(3)=\frac{3871}{3484},
}
\]

whereas the distinct-parameter limit is

\[
\lim_{\alpha\uparrow3}\rho_0(\alpha)
=
\frac{1840}{1819}.
\]

Therefore the exact-data value is discontinuous at the duplicated anchor, reproducing the
same derivative-information singularity found in A44.

For \(\varepsilon=10^{-4}\), the continuous interval is covered by seven exact
Charnes–Cooper primal–dual certificates. Six algebraic transition points occur at

\[
\alpha_1\approx2.279440756542555,
\]

\[
\alpha_2\approx2.650650181613537,
\]

\[
\alpha_3\approx2.877179641465428,
\]

\[
\alpha_4\approx2.909279500576673,
\]

\[
\alpha_5\approx2.911461258357648,
\]

\[
\alpha_6\approx2.913556909680131.
\]

The minimax ratio is continuous across all six transitions and strictly increasing in
\(\alpha\) within every phase. Hence

\[
\boxed{
\alpha^\star_{10^{-4}}=2
}
\]

is the unique global minimizer on \([2,3]\).

At the winner,

\[
\boxed{
\rho_{10^{-4}}(2)
=
\frac{26593405}{26235854},
}
\]

with future-score risk

\[
\boxed{
\mathcal R^Q_{10^{-4}}(2)
\approx0.00976437945133005.
}
\]

At the duplicated endpoint,

\[
\rho_{10^{-4}}(3)
=
\frac{202875104}{179268705},
\]

with future-score risk approximately

\[
0.0892340879650497.
\]

The main conclusion is therefore not that the number \(2\) has acquired a physical
privilege. It is a boundary theorem:

\[
\boxed{
\text{within the declared exclusion domain, the best first anchor is the one closest to the target.}
}
\]

The audit does not rule out better anchors in \(1<\alpha<2\). Rather, it shows that any
further release toward the target must explicitly declare a smaller target-exclusion
distance; otherwise the optimization converges toward the direct-measurement degeneracy
identified in A48.

---

## 1. Declared contract

Let

\[
S=\{0,1,2,3,4,5\},
\]

and

\[
L_p(\eta\log2)
=
\sum_{x=0}^{5}p_x2^{-\eta x}.
\]

The admissible class is

\[
\mathcal P_{5/2}
=
\left\{
p_x\ge0:
\sum_xp_x=1,
\quad
\sum_xxp_x=\frac52
\right\}.
\]

The target remains

\[
L_p(\log2).
\]

For a pair \(p,q\), the direct ratio objective is

\[
\frac{L_p(\log2)}
{L_q(\log2)}.
\]

The future-score width under the centered contraction \(a=1/2\) is

\[
\mathcal R^Q
=
\frac12\log_2\rho.
\]

The first-anchor domain is

\[
2\le\alpha\le3.
\]

This is equivalent to a target-exclusion distance of at least one exponent unit.

---

## 2. Exact-data theorem

For

\[
D_0(\alpha)
=
\{\alpha,3,4\}\log2,
\qquad
2\le\alpha<3,
\]

set

\[
s=2^{-\alpha}.
\]

An exact maximizing pair has support pattern

\[
\operatorname{supp}p=\{1,3,5\},
\qquad
\operatorname{supp}q=\{0,1,2,4\}.
\]

The symbolic Charnes–Cooper primal and dual objectives agree and give

\[
\rho_0(s)
=
\frac{5(392s+779)}
{2(1043s+1916)}.
\]

All primal weights and reduced costs are nonnegative for

\[
\frac18<s\le\frac14.
\]

Differentiation gives

\[
\rho_0'(s)
=
-\frac{307125}
{2(1043s+1916)^2}.
\]

Because

\[
\frac{ds}{d\alpha}
=
-(\log2)s,
\]

\[
\frac{d\rho_0}{d\alpha}
=
\frac{307125(\log2)s}
{2(1043s+1916)^2}>0.
\]

Therefore

\[
\boxed{
\alpha^\star_0=2.
}
\]

The winning value reproduces A43 and A49:

\[
\rho_0(2)
=
\frac{8770}{8707}.
\]

### Duplicated endpoint

At

\[
\alpha=3,
\]

the design contains only two distinct observations:

\[
\{3,4\}\log2.
\]

An exact optimal pair is

\[
p=
\left(
\frac{105}{27872},
\frac{2143}{13936},
\frac{17337}{27872},
0,
0,
\frac{192}{871}
\right),
\]

\[
q=
\left(
0,\frac14,0,\frac34,0,0
\right).
\]

Its ratio is

\[
\rho_0(3)=\frac{3871}{3484}.
\]

By contrast,

\[
\lim_{\alpha\uparrow3}
\rho_0(\alpha)
=
\frac{1840}{1819}.
\]

Thus two distinct exact observations approaching each other retain derivative-like
information that disappears when they coincide exactly.

---

## 3. Noisy continuous phase structure

Now fix

\[
\varepsilon=\frac1{10000}
\]

and use

\[
D_\varepsilon(\alpha)
=
\{\alpha,3,\infty\}\log2.
\]

The compactified observation is

\[
p\longmapsto p_0.
\]

The seven globally certified support regimes are:

| Phase | \(\operatorname{supp}p\) | \(\operatorname{supp}q\) | Active constraints |
|---|---|---|---|
| \(N_1\) | \(\{0,1,3,5\}\) | \(\{1,2,4\}\) | \(\alpha:+,\ 3:-,\ \infty:+\) |
| \(N_2\) | \(\{0,2,3,5\}\) | \(\{1,2,4\}\) | \(\alpha:+,\ 3:-,\ \infty:+\) |
| \(N_3\) | \(\{0,2,5\}\) | \(\{1,2,3,4\}\) | \(\alpha:+,\ 3:-,\ \infty:+\) |
| \(N_4\) | \(\{0,1,2,5\}\) | \(\{1,2,3\}\) | \(\alpha:+,\ 3:-,\ \infty:+\) |
| \(N_{4a}\) | \(\{0,1,2,5\}\) | \(\{1,3\}\) | \(\alpha:+,\ 3:-\) |
| \(N_{5a}\) | \(\{1,2,5\}\) | \(\{0,1,3\}\) | \(\alpha:+,\ 3:-\) |
| \(N_{5b}\) | \(\{1,2,5\}\) | \(\{0,1,3\}\) | \(\alpha:+,\ \infty:-\) |

An inactive constraint has zero dual multiplier and remains primal-feasible throughout its
phase.

---

## 4. Algebraic transition points

The transitions are defined by the unique roots in

\[
s\in(1/8,1/4)
\]

of the following polynomials:

\[
P_1(s)
=
2300416s^4-6174000s^3+5664406s^2-2011563s+223828,
\]

\[
P_2(s)
=
2778888s^4-4299425s^3+1786055s-268850,
\]

\[
P_3(s)
=
1307712s^4-4299425s^2+3369570s-379425,
\]

\[
P_4(s)
=
11702144s^4-38403750s^2+30009165s-3317800,
\]

\[
P_5(s)
=
1066112s^5-3491250s^3+2718052s^2-292914s-931,
\]

\[
P_6(s)
=
23507776s^5-76817741s^3+59583896s^2-6253449s-40964.
\]

Writing

\[
\alpha_j=-\log_2s_j,
\]

the transition values are:

| Transition | \(\alpha_j\) | Future risk |
|---:|---:|---:|
| 1 | 2.279440756542555 | 0.0135207764107065 |
| 2 | 2.650650181613537 | 0.0275836815146688 |
| 3 | 2.877179641465428 | 0.0713155493459304 |
| 4 | 2.909279500576673 | 0.0860332475355624 |
| 5 | 2.911461258357648 | 0.0866484622120530 |
| 6 | 2.913556909680131 | 0.0872506821965863 |

The exact \(s\)-ordering is

\[
\frac14>s_1>s_2>s_3>s_4>s_5>s_6>\frac18.
\]

---

## 5. Noisy global monotonicity

Let

\[
R_j(s)
\]

denote the exact rational ratio in phase \(N_j\).

For every phase,

\[
\boxed{
R_j'(s)<0
}
\]

throughout its interior.

Since \(s\) decreases as \(\alpha\) increases,

\[
\frac{dR_j}{d\alpha}>0.
\]

Adjacent objectives satisfy

\[
R_j(s_j)=R_{j+1}(s_j),
\]

because the numerator of every adjacent difference is divisible by the corresponding
transition polynomial \(P_j\).

Hence the complete noisy value function is continuous and strictly increasing:

\[
\boxed{
\rho_{10^{-4}}(\alpha)
\text{ is strictly increasing on }[2,3].
}
\]

The unique minimizer is therefore

\[
\boxed{
\alpha^\star_{10^{-4}}=2.
}
\]

At the winner,

\[
\rho_{10^{-4}}(2)
=
\frac{26593405}{26235854},
\]

which reproduces the compactified A44–A47 optimum for the fixed pair \(\{2,3\}\).

At the duplicated endpoint,

\[
\rho_{10^{-4}}(3)
=
\frac{202875104}{179268705}.
\]

Positive noise removes the exact discontinuity, but the nearly duplicated anchor remains
strongly inferior.

---

## 6. What the result means

The value \(2\) is not shown to be an interior universal constant of optimal design.

What has been proved is:

\[
\boxed{
\text{among all allowed }\alpha\in[2,3],
\text{ the closest permitted anchor to the target is optimal.}
}
\]

This is a genuine continuous theorem and rules out the possibility that A49 selected \(2\)
merely because the catalogue used integers.

But it is also a boundary result. If the allowed domain were extended to

\[
1+\Delta\le\alpha\le3
\]

with \(\Delta<1\), the winner might move toward the new lower boundary. As
\(\Delta\downarrow0\), the problem approaches the direct-target degeneracy of A48.

Thus a continuous target-excluding design cannot be discussed without declaring the
exclusion distance.

---

## 7. Logical status

### Established

1. The exact-data direct ratio has one closed rational branch for all distinct
   \(\alpha\in[2,3)\).
2. Its risk strictly increases with \(\alpha\).
3. The exact duplicated endpoint is discontinuous and has ratio \(3871/3484\).
4. At \(\varepsilon=10^{-4}\), seven exact primal–dual phases cover the whole interval.
5. Six algebraic transition roots are unique and strictly ordered.
6. Every noisy phase is globally optimal on its interval.
7. The noisy value is continuous at all transitions.
8. The noisy risk strictly increases with \(\alpha\).
9. \(\alpha=2\) is the unique minimizer in both contracts.
10. The values at \(\alpha=2\) reproduce A43, A44, A47, and A49.

### Not established

1. No theorem is claimed for \(1<\alpha<2\).
2. No continuous joint optimization over all three anchors is solved.
3. The use of \(4\) in the exact contract and \(\infty\) in the noisy contract is inherited
   from previous contract-specific optima rather than jointly reoptimized here.
4. No unequal-error or measurement-cost model is supplied.
5. No physical significance is assigned to the target-exclusion distance.

---

## 8. Next rigorous target

The result shows that the first anchor is driven to the nearest permitted point. The next
question is therefore not simply “can \(\alpha\) be lowered?” but:

> How does the optimum depend on an explicitly declared target-exclusion distance?

A natural continuation is to introduce

\[
\Delta>0,
\qquad
\alpha\ge1+\Delta,
\]

and derive the design and risk as functions of \(\Delta\) and \(\varepsilon\). This would
connect the predictive programme continuously to the direct-measurement limit without
silently changing the information contract.
