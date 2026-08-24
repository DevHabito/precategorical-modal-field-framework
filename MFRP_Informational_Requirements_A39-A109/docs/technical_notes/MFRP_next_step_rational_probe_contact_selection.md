# Exact Rational-Probe Contact Selection and Compression Resets

**Programme:** Modal Field Research Programme  
**Audit:** A78  
**Author:** Felipe Gianini Romero  
**Status:** exact finite rational-probe theorem for the declared central-mean contract

## Technical abstract

A77 ended with a discrete structural question: for the family

\[
P=\{0,k,k+1,M\},
\qquad
Q=\{1,h,h+1\},
\qquad
h=\lfloor M/2\rfloor,
\]

which interior contact \(k\) is actually selected, and does that adjacent-pair family remain valid as the support size grows?

A78 freezes the exact rational probe

\[
s_0=\frac{131}{1000},
\qquad
\alpha_0=-\log_2 s_0
=2.932361283124637\ldots,
\]

and exhaustively checks all declared contact choices for every integer

\[
10\le M\le80.
\]

The computation uses exact rational arithmetic. It does not use a floating-point LP to certify the result.

Two basis families are tested:

\[
\mathcal F_3(M,k,\sigma):
\quad
P=\{0,k,k+1,M\},
\quad
Q=\{1,h,h+1\},
\quad
\{\alpha+,\beta-,\gamma_\sigma\},
\]

and the gamma-inactive compression

\[
\mathcal F_2(M,k):
\quad
P=\{0,k,M\},
\quad
Q=\{1,h,h+1\},
\quad
\{\alpha+,\beta-\}.
\]

A total of

\[
\boxed{9230}
\]

candidate branches are classified. Every branch is tested against the full finite-LP KKT system: all basic variables, all active band multipliers, every nonbasic reduced cost, and every inactive observation-band slack.

For each of the 71 support sizes, exactly one branch passes strictly. Therefore each selected branch is a unique strict global basic optimum at the declared probe.

## 1. Frozen contract

For every \(M\), the support, mean, target, completion channels, and scale-normalized error are

\[
X_M=\{0,1,\ldots,M\},
\qquad
\mathbb E[X]=\frac M2,
\qquad
\mu=1,
\]

\[
D=\{\alpha_0,3,4\},
\]

and

\[
\varepsilon_M=
\begin{cases}
\dfrac{1}{1875\,2^{M/2}}, & M\text{ even},\\[6pt]
\dfrac{1}{2500\,2^{\lfloor M/2\rfloor}}, & M\text{ odd}.
\end{cases}
\]

No parameter was retuned after seeing the result. The probe is the same exact point used in the A77 active-reset analysis.

## 2. Exact selection sequence

The adjacent three-band family is selected on the following blocks:

| Support sizes \(M\) | Interior pair | Gamma orientation |
|---:|---:|---|
| 10–13 | \(\{3,4\}\) | \(\gamma+\), except \(M=13\): \(\gamma-\) |
| 14–18 | \(\{4,5\}\) | \(\gamma+\), except \(M=18\): \(\gamma-\) |
| 19–23 | \(\{5,6\}\) | \(\gamma+\), except \(M=23\): \(\gamma-\) |
| 24–29 | \(\{6,7\}\) | \(\gamma+\), except \(M=28,29\): \(\gamma-\) |
| 30–34 | \(\{7,8\}\) | \(\gamma+\), except \(M=34\): \(\gamma-\) |
| 35–39 | \(\{8,9\}\) | \(\gamma+\) |
| 41–45 | \(\{9,10\}\) | \(\gamma+\), except \(M=45\): \(\gamma-\) |
| 46–51 | \(\{10,11\}\) | \(\gamma+\), except \(M=51\): \(\gamma-\) |
| 52–56 | \(\{11,12\}\) | \(\gamma+\), except \(M=56\): \(\gamma-\) |
| 58–62 | \(\{12,13\}\) | \(\gamma+\), except \(M=62\): \(\gamma-\) |
| 63–68 | \(\{13,14\}\) | \(\gamma+\), except \(M=68\): \(\gamma-\) |
| 69–73 | \(\{14,15\}\) | \(\gamma+\) |
| 75–79 | \(\{15,16\}\) | \(\gamma+\) |
| 80 | \(\{16,17\}\) | \(\gamma+\) |

The A77 sequence is reproduced exactly:

\[
M=23:\{5,6\},\gamma-,
\qquad
M=24,25:\{6,7\},\gamma+.
\]

## 3. Gamma-inactive compression resets

The adjacent-pair family fails at exactly three support sizes in the audited window:

\[
\boxed{M=40,57,74.}
\]

At those supports, the unique strict optimum is instead

\[
M=40:
\quad
P=\{0,9,40\},
\]

\[
M=57:
\quad
P=\{0,12,57\},
\]

\[
M=74:
\quad
P=\{0,15,74\},
\]

with

\[
Q=\{1,h,h+1\}
\]

and only the \(\alpha+\) and \(\beta-\) bands active.

These are not arbitrary exceptions inserted to preserve a pattern. At each compression support, the adjacent family on the left with \(\gamma+\) and the adjacent family on the right with \(\gamma-\) are both primal feasible but have a strictly negative active gamma multiplier. Removing the disappearing interior atom produces the same compressed support from either side. Gamma inactivity is therefore forced by the exact dual conditions.

## 4. Negative result: no uniform five-support law

A77 explicitly warned against promoting the observed contacts to a rule such as “the pair advances every five supports.” A78 gives an exact counterexample at the fixed probe.

The adjacent-pair block lengths include

\[
4,5,5,6,5,5,\ldots
\]

and are interrupted by genuine two-band compression phases. The uniform five-support recurrence is therefore false on the audited domain.

This does not prove that no more complicated arithmetic or asymptotic selection law exists. It proves only that the simplest proposed recurrence is wrong.

## 5. Evidence classification

The A78 result is an **exact finite computational certificate**:

- all matrix entries are rational at \(s_0=131/1000\);
- all basis solves and KKT comparisons use exact SymPy rational arithmetic;
- 9230 declared branches are exhaustively classified;
- no candidate basis is singular;
- no tested condition is exactly zero at the probe;
- each selected branch satisfies strict full-LP KKT conditions.

The result is not based on a dense numerical scan, Monte Carlo evidence, or visual inspection.

## 6. What A78 proves

1. Exact contact selection at \(s=s_0\) for every integer \(10\le M\le80\).
2. A unique strict global basic optimum at the probe for every audited support size.
3. Exact reproduction of the A77 \(M=23,24,25\) reset.
4. Exact selection of 68 adjacent three-band branches.
5. Exact selection of three gamma-inactive compressed branches at \(M=40,57,74\).
6. Exact rejection of a uniform five-support contact-reset law on the audited domain.

## 7. What A78 does not prove

A78 does not prove:

1. interval stability around \(s_0\);
2. the complete \(2\le\alpha<3\) phase atlas for \(M>25\);
3. an all-\(M\) formula for the selected contact;
4. periodicity of the compression supports;
5. that the two declared families contain the optimizer for arbitrary contracts;
6. any physical interpretation of contacts, bands, support size, or compression.

In particular, the finite sequence \(40,57,74\) must not be extrapolated as an arithmetic progression without proof.

## 8. Next rigorous target

The next audit should be interval-valued rather than pointwise.

For each compression support \(M=40,57,74\), it should isolate the maximal rational or algebraic interval containing \(s_0\) on which

\[
P=\{0,k,M\},
\qquad
\{\alpha+,\beta-\}
\]

remains the strict active basis. It should then identify the exact boundary conditions where one gamma multiplier reaches zero and an adjacent pair re-enters.

The structural goal is an inequality or Cramer-minor criterion distinguishing

\[
\mathcal F_3
\quad\text{from}\quad
\mathcal F_2,
\]

not a fitted recurrence for the observed support numbers.
