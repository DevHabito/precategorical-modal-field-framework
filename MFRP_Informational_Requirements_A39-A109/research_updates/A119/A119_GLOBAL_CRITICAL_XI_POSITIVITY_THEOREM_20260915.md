# A119 — global positivity of the second-order critical coefficient

**Date:** 2026-09-15  
**Status:** **PROVED under the inherited A115/A116/A117/A118 reduced-factor contract.**  
**Classification:** computer-assisted exact theorem (analytic cutoff + rational interval exhaustion).  
**No physical or ontological interpretation is claimed.**

---

## 1. Scope

Keep

\[
\beta=\frac18,\qquad \delta=\frac1{1875},\qquad
\frac{129}{1000}\le s\le\frac{133}{1000}.
\]

Use the A117 collision layer

\[
\tau_M=s+\frac{\lambda}{M},
\]

with fixed parity, eventual contact deficit `r>=4`, and

\[
\alpha=\frac{\lambda}{2s},\qquad q=e^{-\alpha}.
\]

A117 writes the leading phase as

\[
F_{p,r}(s,\alpha)
=-a_p C+q\bigl(A_p+\alpha D_{p,r}\bigr),
\]

where

\[
a_p=
\begin{cases}
1,&p=\mathrm{even},\\[2pt]
\dfrac{1+s}{2},&p=\mathrm{odd},
\end{cases}
\]

\[
B=\frac\beta s+2\delta,
\qquad
C=1-\frac\beta s-4\delta,
\]

\[
A_p=a_p(1-B),
\qquad
D_{p,r}=s^{2-r}-a_pB.
\]

A117 proves `A_p>0`, `D_{p,r}>0`, and strict decrease of `F` inside every admissible cell. A118 proves

\[
N_M
=\frac{\Lambda_p}{M}+\frac{\Xi_p}{M^2}+o(M^{-2}).
\]

A119 decides the sign of `Xi_p` on **every** A117 critical surface.

---

# 2. Theorem

For every source value

\[
\frac{129}{1000}\le s\le\frac{133}{1000},
\]

every parity, and every A117 critical collision sequence satisfying

\[
\boxed{\Lambda_p=0},
\]

one has

\[
\boxed{\Xi_p>0.}
\]

Consequently the higher degeneracy

\[
\boxed{\Lambda_p=\Xi_p=0}
\]

is impossible under the frozen contract.

Since A118 gives

\[
M^2N_M\to\Xi_p
\]

on a critical surface, every fixed A117 critical sequence has

\[
\boxed{J_M>0}
\]

for all sufficiently large `M` of its fixed parity.

No finite minimal realization threshold is claimed.

---

# 3. Exact critical substitution

On `Lambda_p=0`, equivalently `F_{p,r}=0`,

\[
q\bigl(A_p+\alpha D_{p,r}\bigr)=a_pC.
\]

Because `A_p>0`, `D_{p,r}>0`, and `alpha>0`, the denominator is positive and

\[
\boxed{
q
=\frac{a_pC}{A_p+\alpha D_{p,r}}.
}
\]

Substitute this identity into the exact A118 formula for `Xi_p`.

This produces a purely rational function

\[
\widehat\Xi_{p,r}(s,\alpha)
\]

for each fixed integer `r` and parity. On every actual critical surface,

\[
\boxed{
\Xi_p=\widehat\Xi_{p,r}(s,\alpha).
}
\]

Therefore no numerical root solve, Lambert-W evaluation, or floating-point exponential is needed for the global sign proof.

---

# 4. Only finitely many contact deficits can be critical

Let

\[
L=-\log s,
\qquad
2<L<\frac{21}{10},
\]

using the exact A117 logarithm certificate.

At the right edge of an A117 cell, with

\[
n=r+1+\sigma_p,
\]

A117 gives

\[
R_{p,r}(s)
=-a_pC+nLs^{3+\sigma_p}
+a_ps^n\left[1-B-nLB\right].
\]

Since `1-B>0`,

\[
R_{p,r}(s)
\ge
-a_pC+nLs^{3+\sigma_p}-a_p nLBs^n.
\]

## 4.1 Even parity

For `r=13`, so `n=14`, use

\[
s\in\left[\frac{129}{1000},\frac{133}{1000}\right],
\quad
2<L<\frac{21}{10}.
\]

The exact lower bound is

\[
\boxed{
R_{\mathrm{even},13}
>
\frac{112070026808871649563637353403352532242819592731}
{53615625000000000000000000000000000000000000000000}
>0.
}
\]

Also

\[
\frac{15}{14}\frac{133}{1000}<1,
\]

so `n(133/1000)^n` decreases for every subsequent integer `n>=14`, while the positive linear term grows. Hence

\[
\boxed{R_{\mathrm{even},r}>0\quad\text{for all }r\ge13.}
\]

Because each cell enters from the positive side and `F` is strictly decreasing, no even critical surface exists for `r>=13`.

## 4.2 Odd parity

Use the exact A117 square-root brackets

\[
\frac{359}{1000}<\sqrt{\frac{129}{1000}},
\qquad
\sqrt{\frac{133}{1000}}<\frac{365}{1000},
\]

and

\[
a_p\le\frac{567}{1000}.
\]

At `r=20`, so `n=43/2`, the exact lower bound is

\[
\boxed{
R_{\mathrm{odd},20}
>
\frac{11531809417499828244814003200343395403216479227213725023919447158702411}
{47500000000000000000000000000000000000000000000000000000000000000000000000}
>0.
}
\]

Furthermore

\[
\frac{45}{43}\frac{133}{1000}<1,
\]

so the negative exponential envelope decreases after this point while the positive linear term grows. Hence

\[
\boxed{R_{\mathrm{odd},r}>0\quad\text{for all }r\ge20.}
\]

Thus no odd critical surface exists for `r>=20`.

The only possible critical deficits are therefore

\[
\boxed{4\le r\le12\quad\text{(even)}}
\]

and

\[
\boxed{4\le r\le19\quad\text{(odd)}}.
\]

---

# 5. Rational interval exhaustion of every remaining cell

For a fixed parity and deficit, the exact A117 cell is

\[
\bigl((r+\sigma_p)L,(r+1+\sigma_p)L\bigr].
\]

Since

\[
2<L<\frac{21}{10},
\]

every true cell is contained in the larger rational rectangle

\[
\boxed{
2(r+\sigma_p)
\le\alpha\le
\frac{21}{10}(r+1+\sigma_p).
}
\]

The accompanying audit partitions

\[
\frac{129}{1000}\le s\le\frac{133}{1000}
\]

into 16 equal rational intervals, and each enlarged `alpha` interval into 16 equal rational intervals.

For each box it evaluates the natural interval extension of

\[
\widehat\Xi_{p,r}(s,\alpha)
\]

using only Python `fractions.Fraction` arithmetic. Interval multiplication/division includes all dependency overestimation; positivity is accepted only when the resulting **lower endpoint** is strictly positive.

There are

\[
9\times16\times16=2304
\]

even boxes and

\[
16\times16\times16=4096
\]

odd boxes, for

\[
\boxed{6400}
\]

exact rational boxes in total.

Every box passes.

The worst certified even lower endpoint is

\[
\boxed{
\frac{7962094616280060340361057850523941099377}
{4460543890481278214239707910840320000000}
>0
}
\]

(approximately `1.7850053293`).

The worst certified odd lower endpoint is

\[
\boxed{
\frac{3296636265099577642233577213168576496429665038806348563}
{2438741833785351580293579578096010608476160000000000000}
>0
}
\]

(approximately `1.3517774696`).

These bounds hold on rectangles larger than the actual contact cells. Therefore they contain every possible critical root in the finite deficit ranges.

---

# 6. Conclusion

The proof has two exhaustive pieces:

1. analytic exact bounds exclude all critical surfaces for `r>=13` in even parity and `r>=20` in odd parity;
2. exact rational interval arithmetic proves `Xi_p>0` over supersets of every remaining possible critical cell.

Hence

\[
\boxed{
\Lambda_p=0\Longrightarrow\Xi_p>0
}
\]

throughout the inherited source window and both parities.

This closes the open global-sign question left by A118.

---

# 7. Methodological status

The 6400 boxes are not a finite sample of points. They form a covering certificate: the interval evaluation encloses the value of `Xi-hat` at every real point in each box.

The theorem remains conditional on the inherited A115/A116/A117/A118 reduced-factor contract and the exact formulas already proved there.

A119 does **not** establish:

- a finite minimal `M` at which the asymptotic positive sign is realized;
- a target-deformed A114 lifted active-set classification;
- any RZS, modal-field, spacetime, gravity, matter, or physical interpretation.
