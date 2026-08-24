# Expanded Target-Excluding Anchor Catalogue

**Programme:** Modal Field Research Programme  
**Provisional audit:** A49  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous finite-catalogue continuation of MFRP-TR-2026-01 and A39–A48; no physical design claim

## Technical abstract

A48 showed that permitting the target parameter \(\log2\) makes the anchor-design problem
degenerate: the predictive task is replaced by direct target measurement. The present audit
therefore imposes the honest target-exclusion contract and releases all three observed
parameters inside the enlarged integer catalogue

\[
\mathcal C_{10}
=
\{2,3,4,5,6,7,8,9,10\}.
\]

The microscopic contract remains

\[
\operatorname{supp}P\subseteq\{0,1,2,3,4,5\},
\qquad
\mathbb E[X]=\frac52,
\]

with budget three, common absolute tolerance, target \(L(\log2)\), and direct future-score
risk under the centered contraction \(a=1/2\).

There are

\[
\binom93=84
\]

target-excluding designs. Every design is solved twice:

\[
\varepsilon=0
\]

and

\[
\varepsilon=10^{-4}.
\]

Thus the audit covers 168 linear-fractional optimization problems. Each problem is converted
by the Charnes–Cooper substitution into an exact rational linear programme. For every
design-contract pair, the audit supplies:

- an exact rational primal optimum;
- an exact rational dual optimum;
- exact primal feasibility;
- exact dual feasibility;
- exact equality of primal and dual objectives.

The exact-data catalogue has the unique minimizer

\[
\boxed{
D_0^\star=\{2,3,4\},
}
\]

with ratio

\[
\boxed{
\rho_0^\star=\frac{8770}{8707}
}
\]

and future-score risk

\[
\boxed{
\mathcal R_0^{Q,\star}
=
\frac12\log_2\frac{8770}{8707}
\approx0.00520055966453554.
}
\]

At the noisy benchmark,

\[
\boxed{
D_{10^{-4}}^\star=\{2,3,10\},
}
\]

with ratio

\[
\boxed{
\rho_{10^{-4}}^\star
=
\frac{2263558795360587104}
{2233113362221566575}
}
\]

and future-score risk

\[
\boxed{
\mathcal R_{10^{-4}}^{Q,\star}
\approx0.00976814521137570.
}
\]

Therefore the fixed anchor pair \(\{2,3\}\) used in A44–A47 is not merely a convenient
choice inside this enlarged catalogue. It is selected by exhaustive minimax optimization at
both audited contracts.

The role of the third parameter remains noise-dependent:

- exact data select the nearest available distinct third exponent, \(4\);
- error \(10^{-4}\) selects the largest available exponent, \(10\).

This matches the continuous conclusions already proved:

- exact-data risk increases as the third parameter moves away from \(3\);
- at \(\varepsilon=10^{-4}\), risk decreases toward the compactified boundary
  \(\gamma=\infty\).

The finite noisy winner is already extremely close to the continuous compactified optimum.
Its future-score risk exceeds the A44 boundary value by only approximately

\[
0.03857\%.
\]

The result is finite-catalogue and target-excluding. It does not prove that \(\{2,3\}\) is
globally optimal among all real-valued anchor triples, nor does it provide a physical
measurement prescription.

---

## 1. Declared design problem

Let

\[
S=\{0,1,2,3,4,5\}.
\]

For a probability vector \(p\), define

\[
L_p(k\log2)
=
\sum_{x=0}^{5}p_x2^{-kx}.
\]

The admissible microscopic class is

\[
\mathcal P_{5/2}
=
\left\{
p_x\ge0:
\sum_xp_x=1,\quad
\sum_xxp_x=\frac52
\right\}.
\]

The target is

\[
L_p(\log2),
\]

which remains omitted because the candidate catalogue begins at exponent \(2\).

A design is a three-element subset

\[
D\subset\mathcal C_{10},
\qquad
|D|=3.
\]

For a common absolute tolerance \(\varepsilon\), define

\[
\rho_\varepsilon(D)
=
\max_{p,q\in\mathcal P_{5/2}}
\frac{L_p(\log2)}{L_q(\log2)}
\]

subject to

\[
\left|
L_p(k\log2)-L_q(k\log2)
\right|
\le2\varepsilon
\qquad(k\in D).
\]

The direct future-score minimax width is

\[
\mathcal R_\varepsilon^Q(D)
=
\frac12\log_2\rho_\varepsilon(D).
\]

---

## 2. Exact primal-dual formulation

Set

\[
t=\frac1{L_q(\log2)},
\qquad
y^p=tp,
\qquad
y^q=tq.
\]

Then

\[
L_{y^q}(\log2)=1
\]

and the ratio objective becomes

\[
\max L_{y^p}(\log2).
\]

The normalization and mean constraints become linear:

\[
\sum_xy_x^p=t,
\qquad
\sum_xy_x^q=t,
\]

\[
\sum_xxy_x^p=\frac52t,
\qquad
\sum_xxy_x^q=\frac52t.
\]

At exact data,

\[
L_{y^p}(k\log2)-L_{y^q}(k\log2)=0.
\]

With error,

\[
\left|
L_{y^p}(k\log2)-L_{y^q}(k\log2)
\right|
\le2\varepsilon t.
\]

All coefficients are rational because the exponents are integers. The dual linear programme
is solved independently in exact arithmetic. Equality of exact primal and dual objectives
certifies global optimality for every catalogue entry.

---

## 3. Exact-data ranking

The ten best exact-data designs are:

| Rank | Design | Exact ratio | Future risk |
|---:|---|---:|---:|
| 1 | \(\{2,3,4\}\) | \(\frac{8770}{8707}\) | 0.00520055966454 |
| 2 | \(\{2,3,5\}\) | \(\frac{5758}{5713}\) | 0.00565962948974 |
| 3 | \(\{2,3,6\}\) | \(\frac{34282}{34003}\) | 0.00589462043291 |
| 4 | \(\{2,3,7\}\) | \(\frac{22766}{22577}\) | 0.00601351789418 |
| 5 | \(\{2,3,8\}\) | \(\frac{136330}{135187}\) | 0.00607332201193 |
| 6 | \(\{2,3,9\}\) | \(\frac{30266}{30011}\) | 0.00610331353795 |
| 7 | \(\{2,3,10\}\) | \(\frac{544522}{539923}\) | 0.00611833174587 |
| 8 | \(\{2,4,5\}\) | \(\frac{33526}{33211}\) | 0.00680960056270 |
| 9 | \(\{2,4,6\}\) | \(\frac{22178}{21961}\) | 0.00709276028356 |
| 10 | \(\{2,4,7\}\) | \(\frac{132550}{131227}\) | 0.00723604235570 |

All seven designs preceding the first design without the pair \(\{2,3\}\) contain that pair.

The best design without both anchors is

\[
\{2,4,5\},
\]

with future risk

\[
0.00680960056269662\ldots.
\]

The winning pair \(\{2,3\}\) therefore reduces the exact minimax risk by approximately

\[
23.63\%
\]

relative to the best catalogue design that does not contain both anchors.

---

## 4. Noisy ranking at \(\varepsilon=10^{-4}\)

The ten best noisy designs are:

| Rank | Design | Exact ratio | Future risk |
|---:|---|---:|---:|
| 1 | \(\{2,3,10\}\) | \(\frac{2263558795360587104}{2233113362221566575}\) | 0.00976814521138 |
| 2 | \(\{2,3,9\}\) | \(\frac{2860730621027936}{2822237155653215}\) | 0.00977221464452 |
| 3 | \(\{2,3,8\}\) | \(\frac{25798532644006304}{25451072061605165}\) | 0.00978129183073 |
| 4 | \(\{2,3,7\}\) | \(\frac{172478410182368}{170150215560405}\) | 0.00980340310534 |
| 5 | \(\{2,3,6\}\) | \(\frac{1828961429248}{1804118444725}\) | 0.00986529623595 |
| 6 | \(\{2,3,5\}\) | \(\frac{522712930768}{515460125745}\) | 0.01007900947425 |
| 7 | \(\{2,4,10\}\) | \(\frac{3349214562264352828}{3295657662972549725}\) | 0.01162820646910 |
| 8 | \(\{2,4,9\}\) | \(\frac{370410470093273836}{364469483475279457}\) | 0.01166342695807 |
| 9 | \(\{2,3,4\}\) | \(\frac{1384952831}{1362663390}\) | 0.01170380753403 |
| 10 | \(\{2,4,8\}\) | \(\frac{33121245217252}{32586596870875}\) | 0.01173910931495 |

The first six designs all contain the pair \(\{2,3\}\). The best design without both anchors is

\[
\{2,4,10\},
\]

with future risk

\[
0.0116282064690954\ldots.
\]

The winning design reduces the noisy minimax risk by approximately

\[
16.00\%
\]

relative to that best pair-excluding competitor.

---

## 5. Relation to the continuous third-parameter theorem

A44–A47 proved that, with anchors fixed at \(\{2,3\}\) and
\(\varepsilon=10^{-4}\), the continuous risk decreases toward

\[
\gamma=\infty.
\]

The compactified ratio is

\[
\rho_\infty
=
\frac{26593405}{26235854},
\]

with future risk

\[
\mathcal R_\infty^Q
=
0.00976437945133005\ldots.
\]

The enlarged finite catalogue selects its largest available third exponent:

\[
\gamma=10.
\]

Its risk is only approximately

\[
0.03857\%
\]

above the compactified continuous optimum.

Thus the noisy catalogue result is not an isolated combinatorial accident. It is the finite-cap
manifestation of the exact continuous monotonicity theorem established previously.

At exact data, A44 proved the opposite monotonic direction: among distinct parameters above
\(3\), the risk increases with \(\gamma\). Accordingly, the expanded catalogue selects the
nearest available distinct value,

\[
\gamma=4.
\]

---

## 6. Anchor-pair conclusion

Within the target-excluding integer catalogue \(\mathcal C_{10}\):

\[
\boxed{
\text{the pair }\{2,3\}
\text{ is selected at both audited contracts}.
}
\]

What changes with noise is not the lower anchor pair, but the placement of the third
observation:

\[
\varepsilon=0
\quad\Rightarrow\quad
\{2,3,4\},
\]

\[
\varepsilon=10^{-4}
\quad\Rightarrow\quad
\{2,3,10\}.
\]

The first result exploits exact derivative-like information from a nearby third parameter.
The second exploits increasing separation from the anchors under fixed positive error.

---

## 7. Logical status

### Established

1. All 84 target-excluding integer designs are solved exactly at two error contracts.
2. All 168 primal optima have exact matching dual certificates.
3. \(\{2,3,4\}\) is the unique exact-data minimizer.
4. \(\{2,3,10\}\) is the unique minimizer at \(\varepsilon=10^{-4}\).
5. The pair \(\{2,3\}\) occurs in both winners.
6. At exact data, the seven best designs all contain \(\{2,3\}\).
7. At the noisy benchmark, the six best designs all contain \(\{2,3\}\).
8. The noisy finite-cap winner lies within \(0.04\%\) of the continuous compactified risk.
9. All results on the subcatalogue \(\{2,\ldots,6\}\) reproduce A43 exactly.

### Not established

1. No continuous global optimization over \((\alpha,\beta,\gamma)\) is solved.
2. The pair \(\{2,3\}\) is not proved optimal among all real-valued target-excluding anchors.
3. Exponents between \(1\) and \(2\) are not included.
4. No unequal-error, covariance, or parameter-cost model is supplied.
5. No physical meaning is assigned to any catalogue value.

---

## 8. Next rigorous target

The finite anchor-release audit supports, but does not yet prove, continuous optimality of the
lower pair \(\{2,3\}\).

A controlled next step is to release one lower anchor continuously while retaining target
exclusion, for example

\[
D(\alpha,\gamma)
=
\{\alpha\log2,3\log2,\gamma\log2\},
\]

with

\[
1+\Delta_{\mathrm{target}}\le\alpha<3<\gamma
\]

and a declared compact domain. That two-dimensional problem is substantially smaller and
more auditable than releasing all three anchors simultaneously.
