# A87 — Exact Secant-Residual Offset Classifier

## Status

Exact finite theorem for the declared A84–A86 contract:

\[
10\le M\le 300,
\qquad
s\in\left\{\frac{129}{1000},\frac{131}{1000},\frac{133}{1000}\right\}.
\]

The result uses exact rational arithmetic. Decimal values in the outputs and figure are display-only.

## 1. Question

A86 proved that the exact compressed transition contact lies in the three-contact strip

\[
k^*\in\{b,b+1,b+2\},
\qquad
b=\lceil M c(s)\rceil,
\qquad
c(s)=\frac{\log 2}{-2\log s}.
\]

The remaining problem is discrete: which of the offsets \(0,1,2\) is selected?

A87 asks whether this can be decided by one normalized local residual rather than by inspecting three separate candidate objectives.

## 2. Exact residual

Let \(E_{M,k}(s)\) denote the exact adjacent-objective factor derived in A83 and represented in A84 as a ten-term confluent exponential polynomial in \(k\). Define

\[
\tau_{M,s}
=
\frac{E_{M,b}(s)}{E_{M,b}(s)-E_{M,b+1}(s)}.
\]

The denominator is the local secant drop across the first two factors in the A86 strip.

If

\[
E_{M,b}(s)-E_{M,b+1}(s)>0,
\]

then elementary sign algebra gives

\[
\tau<0
\iff
E_b<0,
\]

\[
0<\tau<1
\iff
E_b>0>E_{b+1},
\]

and

\[
\tau>1
\iff
E_{b+1}>0.
\]

Combining these equivalences with A84's exact one-sign-variation theorem and A86's three-contact strip yields the classifier

\[
\boxed{
\begin{aligned}
\tau<0 &\Longrightarrow k^*=b,\\
0<\tau<1 &\Longrightarrow k^*=b+1,\\
\tau>1 &\Longrightarrow k^*=b+2.
\end{aligned}}
\]

This is not a fitted threshold rule. The thresholds \(0\) and \(1\) follow directly from the definition of a secant coordinate.

## 3. Finite exact result

All 873 support/probe cells satisfy

\[
E_b-E_{b+1}>0.
\]

The exact class counts are

\[
\boxed{3\text{ offset-0 cells}},
\]

\[
\boxed{303\text{ offset-1 cells}},
\]

and

\[
\boxed{567\text{ offset-2 cells}}.
\]

The full residual reproduces all 873 A86 offsets with zero mismatch.

The observed exact ranges are

\[
-0.7246366253\ldots\le \tau< -0.1430859917\ldots
\quad\text{for offset }0,
\]

\[
0.2054254748\ldots\le \tau\le 0.9999278920\ldots
\quad\text{for offset }1,
\]

and

\[
1.0001964568\ldots\le \tau\le 1.0610158448\ldots
\quad\text{for offset }2.
\]

The smallest exact distance to either decision threshold occurs at

\[
M=119,
\qquad
s=\frac{133}{1000},
\qquad
b=21,
\]

where the true offset is one and

\[
1-\tau
=
0.0000721079269588\ldots>0.
\]

The inequality is stored as an exact rational number; the decimal is not used as a certificate.

## 4. Four-term and eight-term reductions

A85 split the exact factor into a four-term dominant core, an eight-term fallback, and residual terms.

Applying the same secant normalization to the four-term core gives the correct offset in

\[
\boxed{872/873}
\]

cells. The sole failure is the already-known small-support counterexample

\[
M=12,
\qquad
s=\frac{129}{1000},
\qquad
b=3.
\]

There the true offset is zero, while the four-term residual lies in \((0,1)\) and incorrectly predicts offset one. The failure is preserved rather than removed by changing the finite contract.

The eight-term secant residual has positive local denominator and classifies

\[
\boxed{873/873}
\]

cells correctly.

Thus the finite hierarchy is

\[
\text{four terms: almost sufficient but false universally},
\]

\[
\text{eight terms: sufficient in all declared cells},
\]

\[
\text{full factor: exact reference classifier}.
\]

## 5. Global monotonicity is false

A natural but stronger explanation would be that \(E_{M,k}(s)\) is globally decreasing in \(k\). A87 tests this directly over the complete A84 finite sequences.

Among 63,948 consecutive secants,

\[
23,465
\]

are positive drops and

\[
40,483
\]

are negative drops. There are no exact ties.

Therefore

\[
\boxed{
E_{M,k}(s)\text{ is not globally decreasing in }k.
}
\]

The first recorded failure occurs at \(M=14\), the lower probe, and contact \(k=4\).

The valid statement is local: the secant across \(b,b+1\) is positive in every declared A86 cell. It must not be promoted to a global monotonicity theorem.

## 6. Computational consequence

The original A84 finite stress contains 64,821 factor/probe evaluations. A86 reduced the candidate set to 2,607 contacts. A87 needs exactly two factors per cell:

\[
2\times873=1,746.
\]

This is a reduction by a factor of approximately

\[
37.12
\]

relative to the full A84 factor catalogue and by approximately

\[
1.49
\]

relative to inspecting all three A86 candidates.

These are computational reductions inside the finite declared contract, not complexity theorems for arbitrary support size.

## 7. What A87 proves

1. Exact positivity of the local secant denominator in all 873 A84/A86 cells.
2. Exact three-interval classification of offsets \(0,1,2\) by one normalized secant residual.
3. Zero mismatch for the full factor.
4. Zero mismatch for the eight-term fallback.
5. Exactly one preserved failure for the four-term reduction.
6. Exact rejection of global factor monotonicity.

## 8. What A87 does not prove

A87 does not prove:

- the secant denominator is positive for every \(M\);
- A84 one-sign variation for every support size or every observation parameter;
- the three-contact strip outside the A86 finite contract;
- an exact closed rounding formula using only \(M\) and \(s\);
- that the four-term core is universally sufficient;
- a physical meaning for contacts, active bands, or the secant residual.

The result remains a theorem about the declared generalized-moment/minimax model.

## 9. Next rigorous target

A88 should derive the local secant drop

\[
E_{M,b}(s)-E_{M,b+1}(s)
\]

in a reduced parity form and ask whether its positivity can be proved uniformly inside a rational strip around \(c(s)M\). A successful proof would remove one finite empirical dependency from A87. A failed proof should identify an explicit support or parameter counterexample rather than narrowing the domain after inspection.
