# A80 — Exact Local Compression-Window Atlas

**Programme:** Modal Field Research Programme  
**Audit:** A80  
**Author:** Felipe Gianini Romero  
**Status:** exact finite local theorem under the frozen A78 contract

## Technical abstract

A78 classified the unique strict-KKT selected contact family at the rational probe

\[
s_0=\frac{131}{1000}
\]

for every integer support maximum \(10\le M\le80\). A79 then upgraded the three gamma-inactive selections at \(M=40,57,74\) to exact algebraic intervals. A80 asks the converse local question: for the A78-selected contact \(k(M)\), which support sizes possess any exact gamma-inactive compression interval inside

\[
I=\left[\frac{129}{1000},\frac{133}{1000}\right]?
\]

The answer is not three. There are exactly **20** strict-KKT compression windows on this local domain. Seventeen lie entirely below \(s_0\); only the windows at \(M=40,57,74\) contain \(s_0\). Thus the three A78 compressions are probe intersections with a broader local atlas, not the only compression phases admitted by the finite contract.

For every one of the 142 lower/upper boundary polynomials attached to the 71 A78-selected contacts, A80 proves an exact six-monomial reduction and strict monotonicity on \(I\). Every complete root pair is isolated by exact rational bisection. For the resulting 20 intervals, all 1,888 non-boundary KKT conditions are certified positive on the enclosing rational hulls. The two gamma slacks alone generate the endpoints.

## 1. Frozen contract

For each integer \(10\le M\le80\):

\[
X_M=\{0,1,\ldots,M\},\qquad \mathbb E[X]=\frac M2,
\]

with target exponent \(1\), fixed channels \(\beta=3\), \(\gamma=4\), and parity-normalized tolerance

\[
\varepsilon_M=
\begin{cases}
\dfrac{1}{1875\,2^{M/2}}, & M\text{ even},\\[6pt]
\dfrac{1}{2500\,2^{\lfloor M/2\rfloor}}, & M\text{ odd}.
\end{cases}
\]

The contact \(k(M)\) is not re-optimized for A80. It is imported from the unique strict-KKT selection certified by A78 at \(s_0=131/1000\). A80 then studies the compressed branch

\[
P=\{0,k,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

with active bands \(\alpha+\) and \(\beta-\), while \(\gamma\) is inactive.

## 2. Exact six-term boundary law

Let \(F^-_{M,k}(s)\) be the Cramer numerator for entry of the left atom \(k-1\) in the branch

\[
P=\{0,k-1,k,M\},\qquad \gamma-,
\]

and let \(F^+_{M,k}(s)\) be the corresponding numerator for entry of the right atom \(k+1\) in

\[
P=\{0,k,k+1,M\},\qquad \gamma+.
\]

For all 71 selected pairs \((M,k(M))\), both polynomials contain exactly six nonzero monomials.

For even \(M=2h\):

\[
F^{\pm}_{M,k}(s)
=c_M^{\pm}s^{2h}
+c_{h+1}^{\pm}s^{h+1}
+c_h^{\pm}s^h
+c_k^{\pm}s^k
+c_1^{\pm}s
+c_0^{\pm}.
\]

For odd \(M=2h+1\):

\[
F^{\pm}_{M,k}(s)
=c_M^{\pm}s^{2h+1}
+c_{h+1}^{\pm}s^{h+1}
+c_h^{\pm}s^h
+c_k^{\pm}s^k
+c_1^{\pm}s
+c_0^{\pm}.
\]

Each coefficient is the exact signed cofactor associated with the corresponding monomial in the unique \(s\)-dependent row of the entering-atom Cramer determinant. This is an exact sparsity theorem for the 142 audited polynomials. It is not yet a closed all-\(M\) formula for the six coefficient functions.

A direct rational interval enclosure of each derivative proves

\[
\frac{d}{ds}F^-_{M,k}(s)>0,
\qquad
\frac{d}{ds}F^+_{M,k}(s)>0
\]

throughout \(I\), for all 142 polynomials. Hence each polynomial has at most one root on the local interval, and an endpoint sign change isolates exactly one simple root.

## 3. Exact local atlas

The exact root classification is:

- 20 selected contacts have a complete ordered pair \(r^-_{M,k}<r^+_{M,k}\) inside \(I\);
- 3 have only the upper root inside \(I\);
- 48 have neither root inside \(I\);
- no selected contact has only a lower root inside \(I\);
- no complete pair is reversed.

The 20 exact compression windows are:

| \(M\) | \(k\) | \(r^-\) display | \(r^+\) display | width | contains \(s_0\)? |
|---:|---:|---:|---:|---:|:---:|
| 10 | 3 | 0.129628352401327640 | 0.129966490016452135 | 0.000338137615124506 | no |
| 14 | 4 | 0.130159856956476749 | 0.130571370357121269 | 0.000411513400644520 | no |
| 15 | 4 | 0.129056313066299583 | 0.129312577134679890 | 0.000256264068380316 | no |
| 19 | 5 | 0.130374930138032391 | 0.130811643053996063 | 0.000436712915963673 | no |
| 24 | 6 | 0.130422832501786380 | 0.130858105966748240 | 0.000435273464961859 | no |
| 25 | 6 | 0.129260762225442587 | 0.129534120509422480 | 0.000273358283979895 | no |
| 30 | 7 | 0.129497746451937317 | 0.129796156479143887 | 0.000298410027206566 | no |
| 35 | 8 | 0.130391693011910281 | 0.130804832301268714 | 0.000413139289358432 | no |
| 40 | 9 | 0.130933737852070436 | 0.131416967562124037 | 0.000483229710053607 | yes |
| 41 | 9 | 0.129708897165488946 | 0.130023151344402232 | 0.000314254178913280 | no |
| 46 | 10 | 0.130273694477634260 | 0.130654299512106415 | 0.000380605034472166 | no |
| 47 | 10 | 0.129177647240082405 | 0.129424451864371515 | 0.000246804624289101 | no |
| 52 | 11 | 0.129744344994118077 | 0.130051658161508238 | 0.000307313167390172 | no |
| 57 | 12 | 0.130913164050332986 | 0.131362029972385302 | 0.000448865922052319 | yes |
| 58 | 12 | 0.129310808923715492 | 0.129564031860093020 | 0.000253222936377528 | no |
| 63 | 13 | 0.130423117232514096 | 0.130799814614428911 | 0.000376697381914813 | no |
| 69 | 14 | 0.130007646416631650 | 0.130328216971868332 | 0.000320570555236679 | no |
| 74 | 15 | 0.130748135735491156 | 0.131148321473730928 | 0.000400185738239763 | yes |
| 75 | 15 | 0.129651030922596972 | 0.129927108136780574 | 0.000276077214183595 | no |
| 80 | 16 | 0.130368276516385634 | 0.130716694012083579 | 0.000348417495697948 | no |

The decimals are displays only. Every endpoint is stored as an exact rational isolating bracket of width below \(4/10^{3}2^{80}\), together with the primitive integer boundary polynomial.

## 4. Full interval KKT theorem

For each complete root pair, A80 reconstructs the compressed symbolic basis and certifies every KKT condition except the two defining gamma slacks over the full rational hull

\[
[\underline r^-,\overline r^+].
\]

The audited condition classes include:

1. all positive basic variables;
2. positive active multipliers for \(\alpha+\) and \(\beta-\);
3. every nonbasic primal reduced cost;
4. every nonbasic dual reduced cost;
5. the inactive \(\alpha-\) slack;
6. the inactive \(\beta+\) slack;
7. all denominators of the rational conditions.

Across the 20 windows, this produces

\[
\boxed{1888}
\]

non-boundary interval certificates. Every one is strictly positive. No interval subdivision was needed: exact Horner enclosures already separated every numerator and denominator from zero on its complete hull.

The gamma conditions are treated separately. Their primitive numerators are exactly the two Cramer boundary polynomials. Strict monotonicity and the ordered simple roots imply

\[
\text{slack}_{\gamma-}>0
\quad\text{for }s>r^-,
\]

and

\[
\text{slack}_{\gamma+}>0
\quad\text{for }s<r^+.
\]

Therefore the compressed branch is strict-KKT precisely on

\[
\boxed{r^-_{M,k}<s<r^+_{M,k}}
\]

within the declared local domain. Each endpoint is maximal for that connected strict component because the corresponding gamma slack changes sign immediately across it.

An independent exact rational midpoint evaluation reproduces a strict global KKT pass for all 20 windows.

## 5. What changed relative to A79

A79 did not claim that only three compression intervals existed. It proved only the three intervals containing \(s_0\). A80 shows that the wider local structure contains 20 windows, while exactly three intersect the frozen probe:

\[
\boxed{M=40,57,74.}
\]

Thus the finite-probe observation in A78 is now explained as an intersection statement:

\[
\text{A78 compression at }s_0
\iff
s_0\in(r^-_{M,k},r^+_{M,k})
\]

for the 20 exact windows in the A80 atlas.

The six A79 boundary polynomials at \(M=40,57,74\) are reproduced exactly, including their primitive coefficient hashes.

## 6. An exact negative result about contact entry

The upper contact-entry candidate

\[
\{k,k+1\},\gamma+
\]

passes the complete strict KKT test at a rational witness immediately above every one of the 20 upper roots.

The analogous lower candidate

\[
\{k-1,k\},\gamma-
\]

passes for 18 of the 20 lower roots, but fails at

\[
M=10,\qquad M=15
\]

because the active \(\alpha+\) multiplier is already negative at the declared outside witness.

This matters conceptually. Equality of a gamma-slack boundary polynomial with an entering-atom Cramer numerator identifies the local pivot equation, but it does **not** by itself prove that the adjacent basis is globally KKT-valid on the other side. A80 therefore preserves the distinction between:

- a candidate contact-entry equation;
- primal feasibility;
- dual feasibility;
- actual active-set selection.

## 7. What A80 proves

1. Exact generation of 142 selected-contact boundary polynomials.
2. Exact six-term parity-reduced monomial support for all 142.
3. Strict monotonicity of all 142 polynomials on \(I\).
4. Exact local root classification: 20 complete pairs, 3 upper-only, 48 none.
5. Exact isolation of 40 ordered algebraic roots.
6. Exact strict-KKT compression intervals for all 20 complete pairs.
7. Positivity of all 1,888 non-boundary KKT conditions over their full interval hulls.
8. Exact reproduction of the three A79 intervals containing \(s_0\).
9. Exact identification of 17 additional compression windows lying below \(s_0\).
10. Exact counterexamples at \(M=10,15\) to the claim that a Cramer contact-entry root automatically selects the declared adjacent lower branch.

## 8. What A80 does not prove

A80 does not establish:

- a periodic law for the support sizes possessing compression windows;
- an all-\(M\) formula for the selected contact \(k(M)\);
- closed formulas for the six coefficient functions \(c_j^{\pm}(M,k)\);
- that every compression window lies inside the chosen local interval;
- a global \(2\le\alpha<3\) phase atlas;
- a physical meaning for the support, contacts, gamma channel, or compression phase.

The support list

\[
10,14,15,19,24,25,30,35,40,41,46,47,52,57,58,63,69,74,75,80
\]

must not be fitted to a recurrence merely because visual subpatterns appear.

## 9. Next rigorous target

The next legitimate audit is not to extrapolate the observed list. It is to derive explicit cofactor formulas for

\[
(c_M^{\pm},c_{h+1}^{\pm},c_h^{\pm},c_k^{\pm},c_1^{\pm},c_0^{\pm})
\]

as functions of \((M,k)\) and parity, and then ask whether the root-order condition

\[
r^-_{M,k}<r^+_{M,k}
\]

can be reduced to an exact sign inequality before numerical root isolation. Such a theorem would explain the local atlas rather than merely extend it.
