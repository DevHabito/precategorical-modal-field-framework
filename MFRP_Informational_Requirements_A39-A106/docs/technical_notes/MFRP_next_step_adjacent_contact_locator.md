# A82 — Exact Adjacent-Contact Locator and Local Orientation Switches

**Programme:** Modal Field Research Programme  
**Audit:** A82  
**Author:** Felipe Gianini Romero  
**Status:** exact rational-probe theorem plus two certified local algebraic transitions

## Technical abstract

A78 recovered the optimum of the declared finite LP at

\[
s_0=\frac{131}{1000}
\]

by exhaustively classifying 9,230 candidate bases for \(10\le M\le80\). A81 then reduced each gamma-inactive compressed family

\[
C_{M,k}:\qquad
P=\{0,k,M\},\qquad
Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

with active bands \(\alpha+\) and \(\beta-\), to a two-variable system. A82 asks whether the contact selected by the full LP can be located through adjacent comparisons of those reduced families.

Let \(V_{M,k}(s)\) be the target ratio of the algebraic compressed basis and let \(z_{M,k}(s)\) be its interior \(P\)-mass. Define

\[
D_{M,k}(s)=V_{M,k+1}(s)-V_{M,k}(s).
\]

For adjacent compressed bases, the exact simplex exchange identity is

\[
\rho^{\rightarrow}_{M,k}
=-\frac{D_{M,k}}{z_{M,k+1}},
\qquad
\rho^{\leftarrow}_{M,k+1}
=\frac{D_{M,k}}{z_{M,k}},
\]

and therefore

\[
\frac{\rho^{\leftarrow}_{M,k+1}}
     {\rho^{\rightarrow}_{M,k}}
=-\frac{z_{M,k+1}}{z_{M,k}}.
\]

At the frozen probe, all 1,438 compressed systems have positive determinant, positive scaled mass \(t\), and positive interior mass \(z\). Consequently, one sign \(\operatorname{sgn}D_{M,k}\) determines the orientation of every adjacent compressed pivot.

The 1,367 exact adjacent differences are nonzero at \(s_0\). For every one of the 71 support sizes, the sequence \(k\mapsto V_{M,k}(s_0)\) is strictly unimodal. Its unique algebraic maximizer \(j(M)\), followed by the signs of the two gamma slacks, reproduces all 71 A78 selections: 57 gamma-plus adjacent branches, 11 gamma-minus adjacent branches, and three gamma-inactive compressed branches.

The reduction has an important limit. In eight gamma-minus supports, the algebraic compressed maximizer is not primal feasible: 15 non-gamma KKT failures occur, all in basic variables. The adjacent branch predicted by the locator nevertheless passes the full KKT system. Thus the locator is exact as a finite selection rule, but the full branch certificate cannot be discarded.

A local endpoint scan on

\[
I=\left[\frac{129}{1000},\frac{133}{1000}\right]
\]

finds two adjacent-difference polynomials with opposite endpoint signs. Each contains a certified simple root:

\[
(M,k)=(28,6),\qquad s\approx0.131364542019008629,
\]

and

\[
(M,k)=(79,15),\qquad s\approx0.131138299445625328.
\]

Exact rational witnesses on both sides show orientation switches with the contact pair unchanged:

\[
M=28:\quad \{6,7\},\gamma-
\longrightarrow
\{6,7\},\gamma+,
\]

\[
M=79:\quad \{15,16\},\gamma+
\longrightarrow
\{15,16\},\gamma-.
\]

A82 does not claim that the other same-endpoint-sign polynomials are root-free inside \(I\); therefore this secondary scan is not promoted to a complete interval atlas.

## 1. Frozen contract

For every integer \(10\le M\le80\), the support and mean are

\[
X_M=\{0,1,\ldots,M\},
\qquad
m=\frac M2.
\]

The target exponent is \(1\), and the fixed observation channels are

\[
\beta=3,
\qquad
\gamma=4.
\]

In transform-base coordinates,

\[
b=2^{-3}=\frac18,
\qquad
g=2^{-4}=\frac1{16},
\qquad s=2^{-\alpha}.
\]

The parity-normalized tolerance remains

\[
\varepsilon_M=
\begin{cases}
\dfrac{1}{1875\,2^{M/2}},&M\text{ even},\\[6pt]
\dfrac{1}{2500\,2^{\lfloor M/2\rfloor}},&M\text{ odd}.
\end{cases}
\]

No parameter was changed relative to A78–A81.

## 2. Adjacent basis-exchange identity

Let \(B_k\) be the compressed basis with interior contact \(k\), and let \(B_{k+1}\) replace that contact by \(k+1\). Denote their objective values by \(V_k\) and \(V_{k+1}\), and their positive entering masses by \(z_k\) and \(z_{k+1}\).

With the repository sign convention, the reduced cost of the entering \(p_{k+1}\) column in \(B_k\) is \(\rho^{\rightarrow}_k\). The ordinary simplex objective-change identity gives

\[
V_{k+1}-V_k=-\rho^{\rightarrow}_k z_{k+1}.
\]

Reversing the pivot gives

\[
V_k-V_{k+1}=-\rho^{\leftarrow}_{k+1}z_k.
\]

Eliminating the value difference yields

\[
\rho^{\leftarrow}_{k+1}
=-\rho^{\rightarrow}_k\frac{z_{k+1}}{z_k}.
\]

Because A82 verifies \(z_k,z_{k+1}>0\) at the probe for every declared adjacent pair, the cross reduced costs always have opposite signs. The implementation checks the direct dual reduced costs against these formulas on eight declared witnesses spanning the support range.

## 3. Strict unimodality at the rational probe

The admissible compressed contacts are

\[
2\le k<\lfloor M/2\rfloor.
\]

Across \(10\le M\le80\), this gives

\[
\boxed{1438\text{ compressed contacts}}
\]

and

\[
\boxed{1367\text{ adjacent comparisons}}.
\]

Every exact adjacent difference is nonzero at \(s_0\). For each fixed \(M\), its sign sequence is

\[
+,+,\ldots,+,-,\ldots,-,
\]

with exactly one sign transition. Hence the algebraic compressed objective has a unique maximizer

\[
j(M)=\operatorname*{arg\,max}_k V_{M,k}(s_0).
\]

This is a finite exact theorem for the stated support range. A82 does not derive a closed formula for \(j(M)\) and does not extrapolate it beyond \(M=80\).

## 4. Gamma-slack lift to the full optimum

At the unique compressed maximizer, inspect the two inactive gamma slacks.

If

\[
S_{\gamma+}<0<S_{\gamma-},
\]

the selected branch is

\[
P=\{0,j,j+1,M\},\qquad \gamma+.
\]

If

\[
S_{\gamma-}<0<S_{\gamma+},
\]

the selected branch is

\[
P=\{0,j-1,j,M\},\qquad \gamma-.
\]

If both are positive, the selected branch remains compressed:

\[
P=\{0,j,M\},
\qquad\gamma\text{ inactive}.
\]

The exact finite census is

\[
\boxed{57\ \gamma+},
\qquad
\boxed{11\ \gamma-},
\qquad
\boxed{3\ \text{compressed}}.
\]

The resulting 71 branches coincide exactly with the A78 catalogue and all pass the complete finite LP KKT system.

## 5. The feasibility obstruction

The compressed objective maximizer is algebraic; it is not automatically a feasible compressed LP solution. Among 6,887 non-gamma KKT conditions evaluated at the 71 maximizers,

\[
6872>0,
\qquad
15<0,
\qquad
0=0.
\]

The 15 failures occur at

\[
M=23,28,34,45,51,56,62,68.
\]

Every failure is a negative basic variable, and every exceptional support belongs to the gamma-minus class. No active-dual, reduced-cost, or non-gamma inactive-slack failure occurs in this exception set.

This falsifies the stronger possible claim that the full optimizer can always be obtained by first finding a feasible optimal compressed basis and then activating gamma. The correct finite statement is weaker:

> The algebraic compressed objective and gamma-slack signs locate the correct branch, but the predicted adjacent branch must still receive an independent full KKT certificate.

## 6. Local orientation switches

For every adjacent pair, A82 also forms the exact numerator polynomial of

\[
D_{M,k}(s)=V_{M,k+1}(s)-V_{M,k}(s).
\]

The endpoint scan on \(I\) has opposite signs only for

\[
(M,k)=(28,6),\qquad(79,15).
\]

The primitive integer polynomials have, respectively,

\[
\deg D_{28,6}=56,
\qquad
\deg D_{79,15}=158,
\]

and both have 20 nonzero terms. Exact rational bisection produces isolating brackets of width below \(2^{-100}\). On each bracket, the derivative has a certified fixed nonzero sign, so the enclosed root is simple and unique within that bracket.

The full adjacent KKT systems are then checked at rational witnesses on both sides. The only passing orientations are

\[
M=28:
\begin{cases}
\gamma-,&s<s_{28}^{\star},\\
\gamma+,&s>s_{28}^{\star},
\end{cases}
\]

and

\[
M=79:
\begin{cases}
\gamma+,&s<s_{79}^{\star},\\
\gamma-,&s>s_{79}^{\star}.
\end{cases}
\]

These are orientation switches with a fixed contact pair, not gamma-inactive compression windows.

## 7. Evidence classification

### Analytic identity

The adjacent simplex exchange relation and its reduced-cost ratio are algebraic consequences of exchanging one basic contact column.

### Exact finite certificate

The positivity census, 1,367 probe comparisons, 71 unimodality classifications, gamma-slack trichotomy, A78 reproduction, full KKT passes, and two local root brackets use exact rational or integer arithmetic.

### Limited local discovery

The endpoint scan identifies which difference polynomials change sign between the declared endpoints. Same endpoint signs do not exclude an even number of interior roots. A82 therefore does not assert a complete interval contact-transition atlas.

## 8. What A82 proves

1. All 1,438 compressed systems have positive determinant, \(z\), and \(t\) at \(s_0\).
2. All 1,367 adjacent compressed objective differences are nonzero at \(s_0\).
3. The compressed objective sequence is strictly unimodal for every \(10\le M\le80\).
4. The unique compressed maximizer plus the gamma-slack signs reproduces all 71 A78 selections.
5. Every predicted full branch passes the complete KKT system.
6. Eight exact primal-feasibility exceptions prevent promotion of the compressed maximizer itself to a universal feasible intermediate state.
7. Two simple local objective-crossing roots are certified, at \((M,k)=(28,6)\) and \((79,15)\).
8. Those roots exchange the gamma orientation while retaining the same adjacent contact pair.

## 9. What A82 does not prove

A82 does not prove:

1. a formula for \(j(M)\);
2. strict unimodality for arbitrary \(M\);
3. root-freedom of all same-endpoint-sign adjacent-difference polynomials on \(I\);
4. a complete local contact-transition atlas;
5. that the algebraic compressed maximizer is always primal feasible;
6. a physical interpretation of a contact, gamma orientation, objective crossing, or compression.

## 10. Next rigorous target

The next defensible step is not to fit a periodic rule to \(j(M)\). It is to derive a closed numerator for

\[
D_{M,k}(s)
\]

from the A81 two-variable formulas and test whether its sign in \(k\) can be controlled by a variation-diminishing or discrete-concavity argument. Such an argument would have to explain both the strict probe unimodality and the eight primal-feasibility exceptions, rather than hiding the latter.
