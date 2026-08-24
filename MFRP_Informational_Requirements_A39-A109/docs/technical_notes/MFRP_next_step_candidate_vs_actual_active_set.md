# Candidate Orientation Versus Actual Active-Set Selection

**Programme:** Modal Field Research Programme  
**Provisional audit:** A76  
**Author line:** Felipe Gianini Romero  
**Status:** exact interval theorem and complete declared one-pivot classification; full-\(\alpha\) phase atlases are numerical discovery only

## Technical abstract

A75 proved an exact support-size orientation theorem for the candidate
signature

\[
C_M:
\quad
P=\{0,3,4,M\},
\qquad
Q=\{1,h,h+1\},
\qquad
h=\lfloor M/2\rfloor,
\]

with active bands

\[
\alpha+,\qquad\beta-,\qquad\gamma+.
\]

On the interval

\[
I=
\left[
\frac{13}{100},
\frac{33}{250}
\right],
\]

the candidate \(\gamma+\) multiplier is:

\[
-\quad(M=21),
\qquad
+\quad(M=22),
\qquad
+\quad(M=23).
\]

This looked like a possible active-set re-entry at \(M=22\).

A76 tests that interpretation against the actual optimizer.

The globally certified branch on the same interval instead uses:

\[
A_M:
\quad
P=\{0,5,6,M\},
\qquad
Q=\{1,h,h+1\}.
\]

Its exact selected completion-band sequence is:

\[
\boxed{
M=21:\gamma+,
\qquad
M=22:\gamma+,
\qquad
M=23:\gamma-.
}
\]

Therefore:

\[
\boxed{
\text{the A75 orientation re-entry at }M=22
\text{ is not an active-set re-entry.}
}
\]

The actual optimizer already uses \(\gamma+\) at \(M=21\). The real
active-sign transition occurs at:

\[
\boxed{
M=22\longrightarrow M=23.
}
\]

For the actual contact family, the \(\gamma+\) Cramer orientations are:

\[
M=21:
\quad
N>0,\ D>0,
\]

\[
M=22:
\quad
N>0,\ D>0,
\]

\[
M=23:
\quad
N<0,\ D>0.
\]

Thus the actual sign flip is caused by the Cramer numerator, while the active
basis determinant remains positive.

Every KKT condition of the selected branches was certified by exact
Bernstein-coefficient signs on the complete interval \(I\):

\[
51+53+55
=
\boxed{159}
\]

strict positive conditions.

The opposite gamma sign was also reconstructed on the same contacts. In each
support its active multiplier is strictly negative throughout \(I\).

At the exact rational probe:

\[
s_0=\frac{131}{1000},
\]

every signature in the declared one-pivot neighborhood was classified over
the rationals.

The neighborhood contains:

\[
145+152+159
=
\boxed{456}
\]

neighbors.

Every neighbor is rejected, and the actual reference basis is the unique
strict local KKT optimum at each support.

---

## 1. Exact interval and probe

The exact interval is:

\[
\boxed{
s\in
\left[
\frac{13}{100},
\frac{33}{250}
\right].
}
\]

In first-anchor coordinates:

\[
2.9213901653036336\ldots
\le
\alpha
\le
2.9434164716336325\ldots.
\]

The one-pivot probe is:

\[
\boxed{
s_0=\frac{131}{1000},
}
\]

corresponding to:

\[
\alpha_0
=
2.9323612831246370718\ldots.
\]

The numerical discovery atlas places the probe in the same signatures later
certified exactly.

---

## 2. Candidate orientation is not active-set selection

The A75 candidate family is:

\[
P_C=\{0,3,4,M\}.
\]

The actual family on \(I\) is:

\[
P_A=\{0,5,6,M\}.
\]

Both use:

\[
Q=\{1,h,h+1\}.
\]

The sign sequences differ:

| \(M\) | Old candidate \(\lambda_{\gamma+}\) | Actual selected gamma band |
|---:|---:|---:|
| 21 | negative | \(\gamma+\) |
| 22 | positive | \(\gamma+\) |
| 23 | positive | \(\gamma-\) |

At \(M=22\) and \(M=23\), the old candidate does have a positive
\(\gamma+\) multiplier. Nevertheless, its basic variable associated with
\(p_4\) satisfies:

\[
\boxed{
p_4^{(C)}<0
}
\]

throughout the complete interval.

At the exact probe:

\[
p_4^{(C,22)}
=
-9270094351436139009125541199056571667146717857846646505226020868833793431182595054993693/3144021709953065404612772895485622731981305481957364281236573226412853555739354836992,
\]

and:

\[
p_4^{(C,23)}
=
-700403864601901396940138041051806982173817702955327693897348855002626959649421230955115118657/372732922649361821862821492596940418949980801059202950349342741161562135167673909588881408.
\]

A positive active multiplier cannot rescue a primal-infeasible basis.

Therefore:

\[
\boxed{
\text{dual orientation is necessary but not sufficient for active-set
selection.}
}
\]

---

## 3. Exact KKT certificates for the actual branches

### \(M=21\)

\[
P=\{0,5,6,21\},
\qquad
Q=\{1,10,11\},
\]

with:

\[
\alpha+,\quad\beta-,\quad\gamma+.
\]

All:

\[
\boxed{51}
\]

KKT conditions are strictly positive on \(I\).

At the probe:

\[
\lambda_{\gamma+}^{(21)}
=
339514957986713475893797562763668429616564250158302674994303565476742931595395072/3215871945024937978346780479207423319800735486853955678370960913161851157469651.
\]

The opposite candidate has:

\[
\lambda_{\gamma-}^{(21)}
=
-339514957986713475893797562763668429616564250158302674994303565476742931595395072/3139372271821615317713466620720758930697085316312550337219858325777428270406099
<0.
\]

### \(M=22\)

\[
P=\{0,5,6,22\},
\qquad
Q=\{1,11,12\},
\]

with:

\[
\alpha+,\quad\beta-,\quad\gamma+.
\]

All:

\[
\boxed{53}
\]

KKT conditions are strictly positive.

At the probe:

\[
\lambda_{\gamma+}^{(22)}
=
62941809546489619716360144188624810723863958861170467173614783754713029327093128757248/1563379565034315252766256064157529544275529961465767289352732999752032463252614890909.
\]

The opposite sign gives:

\[
\lambda_{\gamma-}^{(22)}
=
-62941809546489619716360144188624810723863958861170467173614783754713029327093128757248/1525848399197606248146446299121482930816394705461858330372234865596053166761734653341
<0.
\]

### \(M=23\)

\[
P=\{0,5,6,23\},
\qquad
Q=\{1,11,12\},
\]

with:

\[
\alpha+,\quad\beta-,\quad\gamma-.
\]

All:

\[
\boxed{55}
\]

KKT conditions are strictly positive.

At the probe:

\[
\lambda_{\gamma-}^{(23)}
=
3593405296266840047315584662422602112177997596244600273102176926268150329628335374598144/153778585812616442569440564683933163657814756417476351644706366801029361723341779529927.
\]

The rejected positive sign has:

\[
\lambda_{\gamma+}^{(23)}
=
-3593405296266840047315584662422602112177997596244600273102176926268150329628335374598144/157578947409981789162721717562259965658923967706667977704367819712880151041466094874823
<0.
\]

---

## 4. Actual-family Cramer mechanism

For the actual family, let:

\[
\lambda_{\gamma+}^{A_M}
=
\frac{N_M^A}{D_M^A}.
\]

Exact Bernstein certificates on \(I\) give:

| \(M\) | \(\operatorname{sgn}N_M^A\) | \(\operatorname{sgn}D_M^A\) | \(\operatorname{sgn}\lambda_{\gamma+}^{A_M}\) |
|---:|---:|---:|---:|
| 21 | \(+\) | \(+\) | \(+\) |
| 22 | \(+\) | \(+\) | \(+\) |
| 23 | \(-\) | \(+\) | \(-\) |

Hence:

\[
\boxed{
22\longrightarrow23
}
\]

is an actual-family Cramer-numerator bifurcation.

This is distinct from the old-candidate determinant bifurcation found by
A75 at:

\[
21\longrightarrow22.
\]

The two results concern different contact families and must not be conflated.

---

## 5. Complete declared one-pivot neighborhood

The declared moves are:

1. exchange one active \(P\) contact;
2. exchange one active \(Q\) contact;
3. flip the active \(\beta\) or \(\gamma\) sign;
4. deactivate \(\beta\) or \(\gamma\) while one active contact leaves the
   reduced basis.

The exact classifications are:

| \(M\) | Neighbors | Primal | Active dual | Reduced cost | Inactive slack |
|---:|---:|---:|---:|---:|---:|
| 21 | 145 | 105 | 8 | 31 | 1 |
| 22 | 152 | 110 | 8 | 33 | 1 |
| 23 | 159 | 114 | 39 | 4 | 2 |

Combined:

\[
\boxed{
329\text{ primal infeasible},
}
\]

\[
\boxed{
55\text{ active-dual infeasible},
}
\]

\[
\boxed{
68\text{ reduced-cost infeasible},
}
\]

and:

\[
\boxed{
4\text{ inactive-slack infeasible}.
}
\]

No neighbor is locally optimal.

Including the three references, 459 rational bases were evaluated. No basis
was singular and no rank mismatch occurred.

Each reference is the unique strict local KKT optimum.

---

## 6. Numerical full-domain discovery

The full-\(\alpha\) scan found seven stable phases at each support.

These phase atlases are discovery artifacts, not exact global phase
theorems.

| \(M\) | Phase | Approximate start \(\alpha\) | \(P\)-support | \(Q\)-support | Active bands |
|---:|---:|---:|---:|---:|---|
| 21 | 1 | 2.000000000000 | [1, 7, 21] | [0, 2, 10, 11] | alpha+, beta-, gamma+ |
| 21 | 2 | 2.255529080675 | [1, 6, 21] | [0, 2, 10, 11] | alpha+, beta-, gamma+ |
| 21 | 3 | 2.778457786116 | [0, 1, 6, 21] | [2, 10, 11] | alpha+, beta-, gamma+ |
| 21 | 4 | 2.807821763602 | [0, 6, 21] | [1, 2, 10, 11] | alpha+, beta-, gamma+ |
| 21 | 5 | 2.839060037523 | [0, 5, 6, 21] | [1, 10, 11] | alpha+, beta-, gamma+ |
| 21 | 6 | 2.965262664165 | [0, 5, 21] | [1, 10, 11] | alpha+, beta- |
| 21 | 7 | 2.966512195122 | [0, 5, 21] | [1, 10, 11] | alpha+, gamma- |
| 22 | 1 | 2.000000000000 | [1, 7, 22] | [0, 2, 11, 12] | alpha+, beta-, gamma+ |
| 22 | 2 | 2.497313320826 | [0, 1, 7, 22] | [2, 11, 12] | alpha+, beta-, gamma+ |
| 22 | 3 | 2.561039399625 | [0, 6, 7, 22] | [2, 11, 12] | alpha+, beta-, gamma+ |
| 22 | 4 | 2.859677298311 | [0, 6, 22] | [1, 2, 11, 12] | alpha+, beta-, gamma+ |
| 22 | 5 | 2.882168855535 | [0, 5, 6, 22] | [1, 11, 12] | alpha+, beta-, gamma+ |
| 22 | 6 | 2.964637898687 | [0, 5, 6, 22] | [1, 11, 12] | alpha+, beta-, gamma- |
| 22 | 7 | 2.977133208255 | [0, 5, 22] | [1, 11, 12] | alpha+, gamma- |
| 23 | 1 | 2.000000000000 | [1, 7, 23] | [0, 2, 11, 12] | alpha+, beta-, gamma+ |
| 23 | 2 | 2.566662288931 | [0, 1, 7, 23] | [2, 11, 12] | alpha+, beta-, gamma+ |
| 23 | 3 | 2.621016885553 | [0, 6, 7, 23] | [2, 11, 12] | alpha+, beta-, gamma+ |
| 23 | 4 | 2.875921200750 | [0, 6, 7, 23] | [1, 11, 12] | alpha+, beta-, gamma+ |
| 23 | 5 | 2.907159474672 | [0, 6, 23] | [1, 11, 12] | alpha+, beta- |
| 23 | 6 | 2.915906191370 | [0, 5, 6, 23] | [1, 11, 12] | alpha+, beta-, gamma- |
| 23 | 7 | 2.982131332083 | [0, 5, 23] | [1, 11, 12] | alpha+, gamma- |

The discovery is used only to identify candidate signatures and to verify
that the exact probe lies in the expected branches.

All interval conclusions in Sections 2–5 are independent exact rational
certificates.

---

## 7. What A76 proves

1. The A75 candidate orientation re-entry at \(M=22\) is not an actual
   active-set re-entry.
2. The actual optimizer already uses \(\gamma+\) at \(M=21\).
3. The actual selected sequence on \(I\) is:
   \[
   \gamma+,\gamma+,\gamma-.
   \]
4. The actual sign flip occurs between \(M=22\) and \(M=23\).
5. The actual flip is caused by the Cramer numerator.
6. All 159 selected-branch KKT conditions are positive on \(I\).
7. The opposite gamma sign is excluded exactly in each support.
8. The old candidate remains primal-infeasible at \(M=22,23\).
9. All 456 declared one-pivot neighbors are rejected.
10. Each actual reference is the unique strict local optimum at the probe.

---

## 8. What A76 does not prove

A76 does not provide exact full-domain phase theorems for \(M=21,22,23\).

The numerical seven-phase atlases do not replace algebraic transition
certificates.

A76 also does not prove:

1. the actual-family sign pattern for arbitrary \(M\);
2. that the contacts \(\{5,6\}\) persist indefinitely;
3. a complete enumeration of every LP basis;
4. joint continuous optimization of all three anchors;
5. the global integer-catalogue winner at \(M=21,22,23\).

---

## 9. Next rigorous target

The next structural object should be the actual contact family:

\[
P=\{0,5,6,M\},
\qquad
Q=\{1,h,h+1\}.
\]

The next audit should:

1. derive even and odd symbolic Cramer formulas for this family;
2. determine the complete support-size sign pattern of
   \(\lambda_{\gamma+}^{A_M}\) on \(I\);
3. test whether the \(22\to23\) numerator flip is temporary or permanent;
4. identify when the active contacts move from \(\{5,6\}\) to another pair;
5. separate contact-family transitions from completion-band sign
   transitions.

This is the correct route toward an actual active-set support-size theorem.
