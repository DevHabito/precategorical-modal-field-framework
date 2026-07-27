# Direct Minimax Design for the Nonlinear Future Effective Score

**Programme:** Modal Field Research Programme  
**Provisional audit:** A43  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous mathematical continuation of MFRP-TR-2026-01 and A39–A42; no physical design claim

## Technical abstract

A42 optimized the worst-case interval width of the omitted additive transform
\(L(\log2)\) and then converted that width into an outer bound for the future effective
score. That conversion was rigorous but not generally sharp because

\[
Q_{\log2}=-\log_2 L(\log2)
\]

is nonlinear.

This note optimizes the future-score width directly under the same explicit finite design
contract:

- support is known to lie in \(\{0,1,2,3,4,5\}\);
- the mean is exactly \(5/2\);
- the target is the next value of \(Q_{2\log2}\) under the centered contraction
  \(a=1/2\);
- three observed parameters are selected from
  \[
  \{2\log2,3\log2,4\log2,5\log2,6\log2\};
  \]
- selected observations have common absolute tolerance \(\varepsilon\);
- the risk is the worst possible future-score interval width over every compatible reported
  data box.

For a design \(D\), symmetry reduces the direct nonlinear minimax risk to

\[
\mathcal R_\varepsilon^Q(D)
=
\frac12\log_2 \rho_\varepsilon(D),
\]

where

\[
\rho_\varepsilon(D)
=
\max_{p,q}
\frac{L_p(\log2)}{L_q(\log2)}
\]

subject to equal normalization and mean and

\[
|L_p(k\log2)-L_q(k\log2)|\le2\varepsilon
\quad(k\in D).
\]

The ratio problem is converted exactly to a linear programme by the Charnes–Cooper
substitution. Because all coefficients are rational, every candidate optimum is certified by
an exact rational primal solution and an exact rational dual solution.

All ten three-parameter designs are exhaustively audited at \(\varepsilon=0\) and
\(\varepsilon=10^{-4}\).

With exact data, the unique direct-\(Q\) minimax design is

\[
\boxed{D_0^{Q,\star}=\{2,3,4\}}
\]

with ratio

\[
\rho_0(D_0^{Q,\star})=\frac{8770}{8707}
\]

and future-score risk

\[
\boxed{
\mathcal R_0^Q(D_0^{Q,\star})
=
\frac12\log_2\frac{8770}{8707}
\approx0.00520055966453554.
}
\]

At \(\varepsilon=10^{-4}\), the unique direct-\(Q\) minimax design is

\[
\boxed{D_{10^{-4}}^{Q,\star}=\{2,3,6\}}
\]

with

\[
\rho_{10^{-4}}(D_{10^{-4}}^{Q,\star})
=
\frac{1828961429248}{1804118444725}
\]

and

\[
\boxed{
\mathcal R_{10^{-4}}^Q(D_{10^{-4}}^{Q,\star})
=
\frac12
\log_2
\frac{1828961429248}{1804118444725}
\approx0.00986529623594507.
}
\]

Thus the A42 transform-width designs remain optimal for the direct nonlinear risk at the two
declared benchmarks. This agreement is an audited result for this catalogue, not a general
equivalence theorem.

The direct optima are substantially tighter than the A42 transform-to-score outer bounds.
At exact data the earlier outer bound exceeds the direct minimax value by about \(73.73\%\);
at \(\varepsilon=10^{-4}\) it exceeds the direct value by about \(66.59\%\).

No continuous-parameter optimum, empirical error law, physical support, physical
measurement cost, or physical meaning of the marks is inferred.

---

## 1. Declared model and target

Let

\[
S=\{0,1,2,3,4,5\}.
\]

For a probability vector \(p=(p_0,\ldots,p_5)\), define

\[
L_p(k\log2)=\sum_{x=0}^{5}p_x2^{-kx}.
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

The centered contraction is

\[
x'=\frac52+\frac12\left(x-\frac52\right).
\]

The transport identity gives

\[
Q'_{2\log2}
=
\frac54+\frac12Q_{\log2}.
\]

Since

\[
Q_{\log2}(p)=-\log_2L_p(\log2),
\]

the difference between two future scores is

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

The additive mean term cancels because both distributions have mean \(5/2\).

---

## 2. Direct minimax risk

Let

\[
\mathcal C=\{2,3,4,5,6\}.
\]

A design is a three-element subset

\[
D\subset\mathcal C.
\]

For reported transform values \(b=(b_k)_{k\in D}\) and common absolute tolerance
\(\varepsilon\), define

\[
\mathcal F_D(b,\varepsilon)
=
\left\{
p\in\mathcal P_{5/2}:
|L_p(k\log2)-b_k|\le\varepsilon
\quad\forall k\in D
\right\}.
\]

The direct future-score risk is

\[
\mathcal R_\varepsilon^Q(D)
=
\sup_b
\left[
\max_{p\in\mathcal F_D(b,\varepsilon)}
Q'_{2\log2}(p)
-
\min_{p\in\mathcal F_D(b,\varepsilon)}
Q'_{2\log2}(p)
\right].
\]

### Proposition 2.1 — pairwise form

Define

\[
\rho_\varepsilon(D)
=
\max_{p,q\in\mathcal P_{5/2}}
\frac{L_p(\log2)}{L_q(\log2)}
\]

subject to

\[
|L_p(k\log2)-L_q(k\log2)|
\le2\varepsilon
\quad\forall k\in D.
\]

Then

\[
\boxed{
\mathcal R_\varepsilon^Q(D)
=
\frac12\log_2\rho_\varepsilon(D).
}
\]

### Proof

As in A42, two distributions lie in one common observation box of radius \(\varepsilon\)
exactly when their selected transform values differ by at most \(2\varepsilon\).

The feasible pair set is invariant under exchanging \(p\) and \(q\). Hence

\[
\sup_{p,q}
\left|
\log_2\frac{L_p}{L_q}
\right|
=
\log_2
\sup_{p,q}\frac{L_p}{L_q}.
\]

Multiplication by the contraction factor \(1/2\) gives the stated result. \(\square\)

The denominator is strictly positive because every support value is finite and every
probability vector has positive total mass.

---

## 3. Exact linear-fractional reduction

The ratio problem is not linear in \((p,q)\), but it is a linear-fractional programme.

Set

\[
t=\frac{1}{L_q(\log2)},
\qquad
y^p=tp,
\qquad
y^q=tq.
\]

Then

\[
L_{y^q}(\log2)=1
\]

and the objective becomes

\[
\max L_{y^p}(\log2).
\]

The probability and mean constraints become

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

For every observed exponent \(k\in D\),

\[
\left|
L_{y^p}(k\log2)-L_{y^q}(k\log2)
\right|
\le2\varepsilon t.
\]

Thus the transformed problem is a finite linear programme in the thirteen nonnegative
variables

\[
(y_0^p,\ldots,y_5^p,y_0^q,\ldots,y_5^q,t).
\]

All coefficients are rational whenever \(\varepsilon\) is rational. Therefore exact rational
primal-dual certificates are available.

---

## 4. Exact-data direct design

For

\[
\varepsilon=0,
\]

the complete direct-\(Q\) ranking is:

| Design \(D\) | Exact maximum ratio \(\rho_0(D)\) | Direct future risk |
|---|---:|---:|
| \(\{2,3,4\}\) | \(\frac{8770}{8707}\) | 0.00520055966453554 |
| \(\{2,3,5\}\) | \(\frac{5758}{5713}\) | 0.00565962948974306 |
| \(\{2,3,6\}\) | \(\frac{34282}{34003}\) | 0.00589462043291409 |
| \(\{2,4,5\}\) | \(\frac{33526}{33211}\) | 0.00680960056269662 |
| \(\{2,4,6\}\) | \(\frac{22178}{21961}\) | 0.00709276028355555 |
| \(\{2,5,6\}\) | \(\frac{131038}{129643}\) | 0.00772046598596649 |
| \(\{3,4,5\}\) | \(\frac{4220}{4157}\) | 0.01085012548508753 |
| \(\{3,4,6\}\) | \(\frac{125620}{123667}\) | 0.01130279983256531 |
| \(\{3,5,6\}\) | \(\frac{82468}{81073}\) | 0.01230644545234704 |
| \(\{4,5,6\}\) | \(\frac{480136}{470371}\) | 0.01482199787873868 |

Therefore the exact-data winner is uniquely

\[
\boxed{\{2,3,4\}}.
\]

### Exact worst-case pair

A maximizing pair is

\[
p^\star=
\left(
0,
\frac{887}{2012},
0,
\frac{741}{2012},
0,
\frac{96}{503}
\right),
\]

\[
q^\star=
\left(
\frac{3}{8048},
\frac{1729}{4024},
\frac{843}{8048},
0,
\frac{234}{503},
0
\right).
\]

They satisfy equal normalization, equal mean, and exact equality of the three observed
transforms. Their target transforms are

\[
L_{p^\star}(\log2)=\frac{4385}{16096},
\]

\[
L_{q^\star}(\log2)=\frac{8707}{32192},
\]

so

\[
\frac{L_{p^\star}(\log2)}{L_{q^\star}(\log2)}
=
\frac{8770}{8707}.
\]

---

## 5. Noise-aware direct design

For

\[
\varepsilon=10^{-4},
\]

the complete ranking is:

| Design \(D\) | Exact maximum ratio \(\rho_{10^{-4}}(D)\) | Direct future risk |
|---|---:|---:|
| \(\{2,3,6\}\) | \(\frac{1828961429248}{1804118444725}\) | 0.00986529623594507 |
| \(\{2,3,5\}\) | \(\frac{522712930768}{515460125745}\) | 0.01007900947425480 |
| \(\{2,3,4\}\) | \(\frac{1384952831}{1362663390}\) | 0.01170380753403111 |
| \(\{2,4,6\}\) | \(\frac{38376251275948}{37723035874025}\) | 0.01238400256463465 |
| \(\{2,4,5\}\) | \(\frac{439245342931}{430300944334}\) | 0.01484049191248512 |
| \(\{2,5,6\}\) | \(\frac{300845512945939}{291981170554720}\) | 0.02157375231237272 |
| \(\{3,4,6\}\) | \(\frac{54756141074237}{52062204895646}\) | 0.03639218186327022 |
| \(\{3,4,5\}\) | \(\frac{139450088725057}{130590843111622}\) | 0.04734755603119838 |
| \(\{3,5,6\}\) | \(\frac{1404250535781335}{1293233484634562}\) | 0.05940879289290666 |
| \(\{4,5,6\}\) | \(\frac{1902345060919}{1650301275000}\) | 0.10252476641497894 |

The unique winner is

\[
\boxed{\{2,3,6\}}.
\]

### Exact worst-case pair

One maximizing pair is

\[
p^\star=
\left(
\frac{395536913}{1629577136250},
\frac{254885367383}{543192378750},
0,
\frac{253335186866}{814788568125},
0,
\frac{19880840192}{90532063125}
\right),
\]

\[
q^\star=
\left(
0,
\frac{153627846887}{325915427250},
\frac{4664933369}{108638475750},
0,
\frac{79146390128}{162957713625},
0
\right).
\]

Their observation differences are exactly

\[
L_p(2\log2)-L_q(2\log2)=\frac1{5000},
\]

\[
L_p(3\log2)-L_q(3\log2)=-\frac1{5000},
\]

\[
L_p(6\log2)-L_q(6\log2)=\frac1{5000}.
\]

Because \(2\varepsilon=1/5000\), all three inequalities are saturated. Their target ratio is

\[
\frac{L_p(\log2)}{L_q(\log2)}
=
\frac{1828961429248}{1804118444725}.
\]

---

## 6. Comparison with A42

A42 minimized the additive target-width risk and converted it into a universal future-score
bound. That operation was safe but did not preserve sharpness.

For the exact-data winning design:

\[
\text{A42 outer bound}
=
0.009034708626844655,
\]

whereas direct optimization gives

\[
\text{A43 exact minimax risk}
=
0.00520055966453554.
\]

The outer bound is approximately

\[
73.73\%
\]

larger than the exact direct risk.

At \(\varepsilon=10^{-4}\):

\[
\text{A42 outer bound}
=
0.016434200690519877,
\]

while

\[
\text{A43 exact minimax risk}
=
0.00986529623594507.
\]

The outer bound is approximately

\[
66.59\%
\]

larger.

This does not invalidate A42. It identifies precisely what A42 supplied: a rigorous outer
conversion, not the solution of the nonlinear design problem.

---

## 7. Design agreement and non-equivalence boundary

At the two audited contracts,

\[
\arg\min_D R_\varepsilon(D)
=
\arg\min_D\mathcal R_\varepsilon^Q(D):
\]

- both criteria select \(\{2,3,4\}\) at exact data;
- both select \(\{2,3,6\}\) at \(\varepsilon=10^{-4}\).

However, the two objective functions are different:

\[
\max L-\min L
\]

versus

\[
\log\frac{\max L}{\min L}.
\]

The common winners in these two cases do not prove that transform-width design and
direct-\(Q\) design are generally equivalent. A different support, mean, catalogue, target,
or error geometry can alter the ranking.

---

## 8. Exact certification

For every one of the twenty design-contract pairs, the audit supplies:

1. an exact rational Charnes–Cooper primal point;
2. exact normalization and mean identities;
3. exact denominator normalization \(L_{y^q}(\log2)=1\);
4. exact observation equalities or inequalities;
5. an exact rational dual point;
6. nonnegative inequality multipliers;
7. nonnegative reduced costs;
8. exact primal-dual objective equality.

Therefore each ratio is a global optimum of its declared linear-fractional problem.

The final verdict is

\[
\boxed{
\texttt{PASS\_DIRECT\_Q\_MINIMAX\_DESIGN\_WITH\_EXACT\_FRACTIONAL\_CERTIFICATES}.
}
\]

---

## 9. Logical status

### Established

1. Direct future-score minimax risk reduces exactly to a maximum target-transform ratio.
2. The ratio problem reduces exactly to a finite linear programme.
3. All ten candidate designs are exactly certified at both declared error contracts.
4. \(\{2,3,4\}\) is the unique exact-data direct-\(Q\) minimax design.
5. \(\{2,3,6\}\) is the unique direct-\(Q\) minimax design at
   \(\varepsilon=10^{-4}\).
6. The A42 winners survive direct nonlinear optimization at these benchmarks.
7. A42's transform-to-score bounds are rigorous but quantitatively conservative here.

### Not established

1. No universal equivalence between transform-width and score-width design is proved.
2. No continuous optimization over arbitrary positive parameters is solved.
3. No full tolerance phase diagram is established.
4. No parameter-dependent measurement cost is included.
5. No empirical covariance or noise distribution is inferred.
6. No physical support, scale, contraction, or observation mechanism is calibrated.

---

## 10. Next rigorous target

The strongest remaining mathematical simplification is the finite candidate catalogue.

A natural next step is a **continuous one-parameter replacement audit**:

- retain two anchor observations, for example \(2\log2\) and \(3\log2\);
- allow the third parameter \(\gamma\log2\) to vary continuously over a declared compact
  interval;
- minimize the direct minimax ratio
  \[
  \rho_\varepsilon(\{2,3,\gamma\});
  \]
- certify the global optimum in \(\gamma\), including active-set changes.

This would determine whether the catalogue winners \(4\) and \(6\) are genuine optima or
only the best available grid points.
