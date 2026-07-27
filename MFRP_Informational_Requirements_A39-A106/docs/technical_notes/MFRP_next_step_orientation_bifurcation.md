# Orientation Bifurcation and Active-Set Protection at \(M=10\)

**Programme:** Modal Field Research Programme  
**Provisional audit:** A71  
**Author line:** Felipe Gianini Romero  
**Status:** exact \(M=10\) catalogue and global continuous theorem plus exact obstruction to fixed-signature induction

## Technical abstract

A70 proved signed \(q\)-Schur dominance for the central-mean support family

\[
M=5,6,7,8,9.
\]

Its weakest phase occurred at

\[
M=9,
\qquad
P=\{0,2,3,9\},
\qquad
Q=\{1,4,5\},
\]

with active bands

\[
\alpha+,\qquad
\beta-,\qquad
\gamma-.
\]

The dominance margin was only about \(1.279\%\), suggesting that a direct
induction preserving the same contact pattern might fail.

A71 continues that exact contact signature to a symbolic support maximum
\(M\). Write

\[
R=2^{-M},
\qquad
\varepsilon=\varepsilon_M.
\]

For

\[
P=\{0,2,3,M\},
\qquad
Q=\{1,4,5\},
\]

central mean \(M/2\), \(\beta=3\), and \(\gamma=4\), the first-channel Cramer
numerator is

\[
\boxed{
\begin{aligned}
2^{36}\Delta_{\rm weak}
={}&
\varepsilon\Bigl(
-423886848M
+23622320128R^4
-23622320128R^3\\
&\qquad
-1499463680R
+1499463680
\Bigr)\\
&+
8376795M^2
+1266843648MR^4
-1404748800MR^3\\
&+
183544200MR
-122051118M
-10009509888R^4\\
&+
11144448000R^3
-1536973200R
+402035088.
\end{aligned}
}
\]

Under the normalized central-mean error contract, its orientation is

\[
\Delta_{\rm weak}(8)<0,
\qquad
\Delta_{\rm weak}(9)<0,
\qquad
\Delta_{\rm weak}(10)>0.
\]

Thus the fixed contact-signature orientation bifurcates exactly between
\(M=9\) and \(M=10\).

At \(M=10\), the inherited active-basis determinant has no root on

\[
s\in\left[\frac18,\frac14\right]
\]

and is strictly negative there. Since the Cramer numerator is strictly
positive,

\[
\boxed{
\lambda_\alpha^+
=
\frac{\Delta_{\rm weak}}{\Delta_{\rm basis}}
<0
}
\]

throughout the full first-anchor interval.

Therefore the inherited \(M=8,9\) weak phase is dual-infeasible at \(M=10\).

The optimizer does not preserve the invalid signature. It changes active
contact pattern.

For the exact \(M=10\) contract,

\[
\operatorname{supp}P\subseteq\{0,\ldots,10\},
\qquad
\mathbb E[X]=5,
\]

\[
\mu=1,
\qquad
\delta=\frac1{1875},
\qquad
\varepsilon=\frac1{60000},
\]

the complete three-anchor integer catalogue

\[
\binom{\{2,\ldots,10\}}3
\]

was solved exactly over the rationals.

The unique winner is

\[
\boxed{
\{2,3,4\}.
}
\]

The fixed continuous completion

\[
D_\alpha=\{\alpha,3,4\},
\qquad
2\le\alpha<3,
\]

decomposes into six exact primal-dual phases joined by five simple algebraic
transitions.

Every phase has:

- primal feasibility;
- dual feasibility;
- positive first-channel multiplier;
- positive first-anchor derivative;
- finite transition denominators.

Consequently,

\[
\boxed{
\frac{d\rho_{10}}{d\alpha}>0
\quad\text{for all }2\le\alpha<3.
}
\]

Therefore:

\[
\boxed{
\alpha^\star=2
}
\]

is the unique global first-anchor optimum at \(M=10\).

The conclusion is not a fixed-signature induction. It is an active-set
selection theorem:

\[
\boxed{
\text{when the inherited contact orientation becomes invalid, dual
feasibility forces a new contact pattern that preserves the boundary law.}
}
\]

---

## 1. Exact catalogue at \(M=10\)

All

\[
\binom93=84
\]

integer designs were solved exactly.

| Rank | Design | Exact-ratio decimal | Future risk |
|---:|---:|---:|---:|
| 1 | (2, 3, 4) | 1.271857201113 | 0.173468349929 |
| 2 | (2, 3, 5) | 1.285777364875 | 0.181320429266 |
| 3 | (2, 3, 6) | 1.293703143422 | 0.185753305325 |
| 4 | (2, 3, 7) | 1.297717588700 | 0.187988227989 |
| 5 | (2, 3, 8) | 1.299661545657 | 0.189067984713 |
| 6 | (2, 3, 9) | 1.301119847906 | 0.189876928382 |
| 7 | (2, 3, 10) | 1.302023074792 | 0.190377508274 |
| 8 | (2, 4, 5) | 1.356709383124 | 0.220055859115 |
| 9 | (2, 4, 6) | 1.369615619033 | 0.226885529687 |
| 10 | (2, 4, 7) | 1.377929988917 | 0.231251294091 |

The winner ratio is

\[
\boxed{
\rho_{10}(2,3,4)
=
35973228924774922/28284015605920837.
}
\]

The runner-up is

\[
\{2,3,5\}
\]

with exact ratio

\[
12797439174974298722/9953075489256038897.
\]

The exact gap is

\[
\boxed{
3918706260222099169030640120129280/281512942465025974177535050774796789>0.
}
\]

Both winner and runner-up have independently matching exact primal and dual
values.

---

## 2. Weak-signature orientation bifurcation

The exact values are:

\[
\Delta_{\rm weak}(8)
=
-\frac{
1580657726195793
}{
2814749767106560000
},
\]

\[
\Delta_{\rm weak}(9)
=
-\frac{
4649933655952137
}{
18014398509481984000
},
\]

and

\[
\Delta_{\rm weak}(10)
=
\frac{
50984904514300239
}{
180143985094819840000
}.
\]

Thus the orientation crosses zero between the two consecutive integer support
sizes \(9\) and \(10\).

The continuation remains positive for every audited value

\[
M=10,\ldots,16.
\]

This disproves a recurrence of the form:

> the weakest A70 contact signature retains one fixed Cramer orientation as
> \(M\) increases.

---

## 3. Why the inherited basis cannot remain optimal

For the \(M=10\) continuation of the weak signature, the active-basis
determinant is

\[
\Delta_{\rm basis}(s)
=
\frac{
P_{10}(s)
}{
270215977642229760000
},
\]

where

\[
\begin{aligned}
P_{10}(s)
={}&
1173528807756267520s^{10}
-4620525879186000000s^5\\
&-2310262939593000000s^4
+9628789238444185794s^3\\
&-4427770186745741291s^2
+577565734898250000s\\
&-21536549676758048.
\end{aligned}
\]

Exact root isolation finds no root in

\[
\left[\frac18,\frac14\right].
\]

At the exact rational sample

\[
s=\frac3{16},
\]

the determinant is negative. Hence it is negative on the whole interval.

Because the Cramer numerator is positive at \(M=10\),

\[
\lambda_\alpha^+<0.
\]

A negative multiplier violates dual feasibility for an active positive error
band. The inherited phase therefore cannot participate in the \(M=10\)
optimal envelope.

This is not a numerical choice between nearly equal bases. It is an exact
duality obstruction.

---

## 4. Six exact \(M=10\) phases

| Phase | \(\alpha\)-interval | Active \(P\)-support | Active \(Q\)-support | Active bands |
|---:|---:|---:|---:|---|
| 1 | [2.000000000000, 2.562390719601] | [1, 4, 10] | [0, 2, 5, 6] | alpha+, beta-, gamma+ |
| 2 | [2.562390719601, 2.668041905503] | [0, 1, 4, 10] | [2, 5, 6] | alpha+, beta-, gamma+ |
| 3 | [2.668041905503, 2.768365791805] | [0, 4, 10] | [1, 2, 5, 6] | alpha+, beta-, gamma+ |
| 4 | [2.768365791805, 2.943788401780] | [0, 3, 4, 10] | [1, 5, 6] | alpha+, beta-, gamma+ |
| 5 | [2.943788401780, 2.947546794912] | [0, 3, 10] | [1, 5, 6] | alpha+, beta- |
| 6 | [2.947546794912, 3.000000000000] | [0, 3, 10] | [1, 5, 6] | alpha+, gamma- |

The five transition coordinates are:

\[
\begin{aligned}
\alpha_1&\approx2.562390719601230,\\
\alpha_2&\approx2.668041905502717,\\
\alpha_3&\approx2.768365791805390,\\
\alpha_4&\approx2.943788401780076,\\
\alpha_5&\approx2.947546794911715.
\end{aligned}
\]

The positive \(\alpha\) band remains active in all six phases.

The completion bands behave non-universally:

- \(\gamma+\) is active in the first four phases;
- \(\gamma\) becomes inactive in phase 5;
- \(\beta\) becomes inactive and \(\gamma-\) becomes active in phase 6.

The active contact pattern therefore reorganizes exactly where required to
maintain dual feasibility.

---

## 5. Global \(M=10\) theorem

### Theorem 5.1

For the declared \(M=10\) contract and fixed completion

\[
D_\alpha=\{\alpha,3,4\},
\]

the exact minimax ratio is continuous and strictly increasing on

\[
[2,3).
\]

Thus:

\[
\boxed{
\arg\min_{2\le\alpha<3}\rho_{10}(\alpha)=\{2\}.
}
\]

At the boundary:

\[
\rho_{10}(2)
=
35973228924774922/28284015605920837,
\]

and

\[
Q_{10}(2)
=
0.17346834992930848267812309234663568001198253981156.
\]

At coalescence:

\[
\lim_{\alpha\to3^-}\rho_{10}(\alpha)
=
170834562629502133156/72934461253621283173,
\]

and

\[
Q_{10}(3^-)
=
0.61396366834000204376552932214894031105947177818047.
\]

---

## 6. What A71 establishes

1. The weakest A70 contact signature admits an exact symbolic continuation in
   \(M\).
2. Its Cramer orientation flips between \(M=9\) and \(M=10\).
3. The inherited \(M=10\) basis is dual-infeasible over the full continuous
   interval.
4. Fixed-signature induction is therefore false.
5. The exact \(M=10\) optimizer changes active contact pattern.
6. The integer catalogue winner remains the boundary design
   \(\{2,3,4\}\).
7. The continuous first-anchor law remains globally true at \(M=10\).
8. Active-set selection protects the positive first-channel multiplier.

---

## 7. What remains open

A71 does not prove:

1. the boundary law for every \(M\);
2. that active-set protection always succeeds;
3. a finite classification of every possible contact bifurcation;
4. a recurrence for the optimal active pattern;
5. a uniform lower bound on the positive multiplier;
6. joint continuous reoptimization of all three anchors.

The main new lesson is that an arbitrary-\(M\) proof cannot follow one active
signature indefinitely.

It must allow combinatorial active-set bifurcations.

---

## 8. Next rigorous target

The next object should be the sequence of active contact patterns rather than
one determinant.

A suitable target is an orientation-selection theorem:

> among all candidate contact signatures, the minimax LP selects only those
> whose Cramer numerator and active-basis determinant have compatible
> orientation.

The next audit should:

1. enumerate all locally feasible signatures at \(M=10,11,12\);
2. compute their Cramer orientation pairs;
3. classify which signatures are rejected solely by dual sign;
4. identify the pivot rule connecting the final valid signatures;
5. test whether the pivot sequence is governed by an oriented-matroid
   elimination law.

That would replace the failed fixed-signature recurrence with a recurrence on
active-set pivots.
