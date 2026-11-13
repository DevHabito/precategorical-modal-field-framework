# Perturbative \(L^4\) jet calibration of the boosted \(d=5\) Kasner ACD volume

**Date:** 2026-11-13  
**Author:** Felipe Gianini Romero  
**Status:** exact local jets plus numerical quadrature of the coefficient functions  
**Scope:** five-dimensional LRS-Kasner, central timelike geodesic with midpoint speed \(v=1/2\)  
**Purpose:** remove the finite-\(L\) extrapolation from the independent nonzero-\(H^2\) volume check

## 1. Background

The direct finite-diamond calculation already found that boosted Kasner volumes approach

\[
c_4(v)
=
\frac{
8v^4+24v^2+25
}{
1152(1-v^2)^2
},
\]

rather than the \(d=5\) specialization of the printed Eq. (79).

For

\[
v=\frac12,
\]

the corrected target is

\[
\boxed{
c_4=\frac7{144}.
}
\]

The earlier calculation obtained this coefficient by evaluating finite diamonds at several small \(L\) and extrapolating the scaled volume to \(L=0\).

The purpose of the present calculation is different:

> expand the full causal-volume construction directly as a Taylor jet in \(L\) and integrate the \(L^4\) coefficient itself.

No finite-\(L\) parent volume is evaluated.

## 2. Geometry

Use

\[
ds^2
=
-dt^2
+
t^{-1}dx^2
+
t(dy_1^2+dy_2^2+dy_3^2).
\]

At the midpoint,

\[
v=\frac12,
\qquad
P=\frac1{\sqrt3},
\qquad
\gamma=\frac2{\sqrt3}.
\]

The tips lie at proper times

\[
s=\pm L
\]

along the boosted timelike geodesic.

The exact timelike-tip jets are documented and checked in

\[
\texttt{tools/derive\_d5\_boosted\_kasner\_timelike\_tip\_jets.py}.
\]

## 3. Null-cone jets

For null conserved axial fraction \(c\),

\[
\mathcal E(t,c)
=
\sqrt{
ct+\frac{1-c}{t}
}.
\]

The axial and transverse first-integral densities are

\[
f_x(t,c)
=
\frac{t}{\mathcal E(t,c)},
\]

\[
f_\perp(t,c)
=
\frac{1/t}{\mathcal E(t,c)}.
\]

Their exact Taylor jets through the order required for a relative \(L^4\) volume correction are generated in

\[
\texttt{tools/derive\_d5\_kasner\_null\_cone\_profile\_jets.py}.
\]

The calculation does not expand the physical cone radius at fixed axial coordinate near its endpoint, because that produces a nonuniform artificial singularity.

Instead, the future cone's conserved parameter

\[
s=\sqrt c
\in[0,1]
\]

is used as the regular integration coordinate.

## 4. Exact three-ball lens

At fixed coordinate time and fixed axial coordinate, the two null-cone transverse sections are three-balls.

Their intersection volume is evaluated with the exact lens formula

\[
V_{\rm lens}
=
\frac{
\pi(R+r-d)^2
\left[
d^2+2d(R+r)-3(R-r)^2
\right]
}{
12d
}
\]

in the partial-overlap regime.

The matching to the empty and containment branches is \(C^1\).

This is checked in

\[
\texttt{tools/verify\_three\_ball\_lens\_c1\_switching.py}.
\]

Thus the lens is treated locally, before any angular or time averaging.

## 5. Flat switching geometry

At \(L=0\), define

\[
T=\frac{t-\bar t}{L},
\qquad
X=\frac{x}{L}.
\]

The flat switching surface satisfies

\[
\boxed{
X_*^2
=
1-\frac{T^2}{P^2}.
}
\]

For \(T\ge0\), the flat regimes are

\[
0\le T<\frac{P^2}{\gamma}
\quad:
\quad
\text{lens}\to\text{empty},
\]

\[
\frac{P^2}{\gamma}
\le T<P
\quad:
\quad
\text{lens}\to\text{containment},
\]

and

\[
P\le T\le\gamma
\quad:
\quad
\text{full containment}.
\]

This decomposition is proved in

\[
\texttt{D5\_BOOSTED\_FLAT\_LENS\_REGIME\_LEMMA\_20261113.md}.
\]

## 6. Why the moving time boundaries matter

A first coefficient-level attempt kept the flat time-regime boundaries fixed.

That calculation already reproduced the flat volume and nearly removed the \(L^2\) vacuum term, but it gave an incorrect \(L^4\) coefficient of order

\[
0.25.
\]

The angular lens switch was then allowed to move perturbatively.

That changed the result but did not remove the discrepancy.

The missing contribution was traced to the motion of the **time-regime boundaries themselves**.

This is important methodologically:

\[
\boxed{
\text{a local moving boundary cannot be frozen before the nonlinear lens integral is assembled.}
}
\]

The failure mechanism is closely analogous to the earlier warning about premature angular averaging in the RNC audit.

## 7. Exact moving time switches

For \(v=1/2\), the first critical time is determined by the future cone reaching its axial endpoint while the corresponding past-cone transverse radius equals the center separation.

The exact jet is

\[
\boxed{
T_1(L)
=
\frac{\sqrt3}{6}
+
\frac1{16}L
+
\frac{61\sqrt3}{432}L^2
-
\frac{367}{2304}L^3
+
\frac{25949\sqrt3}{207360}L^4
+
O(L^5).
}
\]

The second critical time is determined on the transverse axis by

\[
R_--R_+=d_\perp.
\]

Its exact jet is

\[
\boxed{
T_2(L)
=
\frac{\sqrt3}{3}
-
\frac14L
+
\frac{19\sqrt3}{216}L^2
-
\frac7{72}L^3
+
\frac{3937\sqrt3}{51840}L^4
+
O(L^5).
}
\]

These coefficients are derived symbolically, not fitted.

Checker:

\[
\texttt{tools/derive\_d5\_boosted\_kasner\_lens\_time\_switch\_jets.py}.
\]

## 8. Perturbative integration architecture

Every quantity is represented as a truncated jet

\[
q(L)
=
q_0
+
q_1L
+
q_2L^2
+
q_3L^3
+
q_4L^4
+
O(L^5).
\]

The numerical coefficient-level checker propagates these jets through:

1. the tip positions;
2. the slice time;
3. the null first integrals;
4. the conserved parameter required to match the two cones at the same axial coordinate;
5. the angular lens switch;
6. \(T_1(L)\) and \(T_2(L)\);
7. the lens or containment volume;
8. the physical spatial density
   \[
   \sqrt{\det g_{\rm spatial}}=t;
   \]
9. the time integral.

The negative-time half follows by tip exchange

\[
L\mapsto-L.
\]

Only after the local cone/lens calculation is complete are the even coefficients combined.

## 9. Convergence

Using Gauss-Legendre quadrature directly on the perturbative coefficient functions gives:

\[
\begin{array}{c|c|c}
N_T & N_s & c_4\\
\hline
18 & 20 & 0.0486101493113\\
20 & 22 & 0.0486105602187\\
22 & 24 & 0.0486107793171\\
24 & 26 & 0.0486109027153
\end{array}
\]

The exact target is

\[
\frac7{144}
=
0.0486111111111\ldots
\]

At the \(24\times26\) level,

\[
\boxed{
c_4-\frac7{144}
\approx
-2.08\times10^{-7}.
}
\]

At the same resolution the relative \(L^2\) coefficient is

\[
\boxed{
c_2
\approx
-4.36\times10^{-8}.
}
\]

Thus the perturbative construction simultaneously reproduces:

1. the Ricci-flat cancellation
   \[
   c_2=0;
   \]
2. the nonzero boosted vacuum response
   \[
   c_4=\frac7{144}.
   \]

## 10. Reproducible CI checker

The repository checker is

\[
\texttt{tools/check\_d5\_boosted\_kasner\_l4\_jet\_quadrature.py}.
\]

Its default CI quadrature is intentionally lower than the highest private convergence run, to keep runtime modest.

It requires:

\[
|c_2|<2\times10^{-6},
\]

and

\[
\left|
c_4-\frac7{144}
\right|
<
10^{-5}.
\]

The target value is declared before integration.

No rational reconstruction is performed.

## 11. Relation to the finite-L boosted test

The two calculations have different systematics.

### Finite-L physical-volume test

This integrates the actual finite causal diamond and then extrapolates

\[
L\to0.
\]

Its main systematic is finite-\(L\) extrapolation.

### Perturbative jet test

This expands the causal geometry first and integrates the coefficient directly.

Its main systematic is quadrature of the coefficient functions.

Agreement between the two therefore provides a nontrivial cross-check.

## 12. Current status of the magnetic/hook sector

For \(d=5\), the nonzero-\(H^2\) sector now has:

1. exact observer-frame Weyl invariants;
2. Lean-certified reduction to the corrected rational target;
3. direct finite-L physical-volume integration;
4. direct perturbative \(L^4\) coefficient integration;
5. exact moving lens-switch and time-switch jets.

The remaining gap is narrower:

\[
\boxed{
\text{replace the final coefficient quadrature by closed-form analytic integration.}
}
\]

Until that is done, the boosted calculation remains semi-analytic rather than a fully closed analytic proof.

## 13. Methodological lesson

The calculation gives another explicit example where a locally zero-mean or apparently subleading geometric displacement cannot be discarded before nonlinear assembly.

The correct order is

\[
\boxed{
\text{local geometry}
\to
\text{moving boundaries}
\to
\text{nonlinear volume}
\to
\text{integration}.
}
\]

Freezing the time-regime boundaries before the lens integral produced the wrong \(L^4\) coefficient even though lower-order controls looked good.

This observation should be retained when completing the generic unabridged RNC derivation.
