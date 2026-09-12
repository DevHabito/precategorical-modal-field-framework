# A114-B1 — analytic-tail `b+1` gamma-pivot lift theorem

## Status

**PROVED under the frozen tail contract for every point whose strict compressed maximizer is `b+1`.**

Away from the scalar pivot condition \(\Phi=0\), the full lifted optimum is represented by a unique strict gamma-plus KKT basis. On the pivot set itself the optimum is a non-strict degenerate transition point; strict complementarity and uniqueness are not claimed there.

No finite `M` grid or floating-point sign decision is used in the theorem. Numerical/high-precision work was used only for discovery and for independent adversarial checks.

## Contract

Let

\[
M\ge 521,
\qquad
\frac{129}{1000}\le s\le\frac{133}{1000},
\qquad
h=\lfloor M/2\rfloor,
\]

with

\[
\beta=\frac18,
\qquad
\gamma=\frac1{16},
\qquad
\tau=\frac12,
\]

and

\[
c(s)=\frac{\log2}{-2\log s},
\qquad
b=\lceil Mc(s)\rceil.
\]

Assume the compressed objective has the strict global maximizer

\[
\boxed{j_*=b+1}.
\]

In adjacent-factor notation this gives in particular

\[
E_{b+1}<0.
\]

Define the upper gamma boundary pivot

\[
\boxed{\Phi(M,s):=F_{b+2}^{\rm up}(s)}.
\]

## The theorem

### Case 1: \(\Phi<0\)

The unique strict global lifted optimum is

\[
P=\{0,b+1,b+2,M\},
\qquad
Q=\{1,h,h+1\},
\]

with active bands

\[
\alpha+,
\qquad
\beta-,
\qquad
\gamma+.
\]

### Case 2: \(\Phi>0\)

The unique strict global lifted optimum is instead

\[
P=\{0,b+2,b+3,M\},
\qquad
Q=\{1,h,h+1\},
\]

with the same active bands

\[
\alpha+,
\qquad
\beta-,
\qquad
\gamma+.
\]

Thus inside the strict compressed `b+1` phase the lifted gamma-plus contact may sit one step to the right of the compressed maximizer. The compressed maximizing contact and the lifted adjacent P pair are not identical objects.

### Case 3: \(\Phi=0\)

Neither adjacent gamma-plus basis is strict: one basic P mass vanishes in each representation.

The two bases share the seven non-pivot columns and collapse to the same degenerate primal point. Its P law is supported in

\[
\{0,b+2,M\},
\]

and its Q law is supported in

\[
\{1,h,h+1\}.
\]

The alpha+, beta- and gamma+ equalities remain saturated. The point is a global optimum by continuity from the neighboring strict KKT branch. No claim of strict complementarity, a unique optimal basis, or a unique primal optimum is made at \(\Phi=0\).

## Proof

### 1. The determinant orientation is independent of primal positivity

A112-A writes the gamma-plus adjacent branch as

\[
G_j
\begin{pmatrix}
p_j\\ p_{j+1}\\ t
\end{pmatrix}
=
\begin{pmatrix}
C_\beta\\ C_\gamma\\ C_s
\end{pmatrix},
\qquad
D_G:=\det G_j.
\]

A114-B1 reconstructs independently the A112-F/G four-by-four P interpolation matrix

\[
C=
\begin{pmatrix}
1&1&1&1\\
0&j/M&(j+1)/M&1\\
1&\beta^j&\beta^{j+1}&\beta^M\\
1&\gamma^j&\gamma^{j+1}&\gamma^M
\end{pmatrix}
\]

in the normalized tail variables and the coefficient \(A(s)\) of the remaining alpha equation after the first four equations are solved.

The standalone symbolic certificate proves identically, for both parities,

\[
\boxed{D_G=\det(C)\,A(s)}.
\]

A110's generalized-Vandermonde theorem gives

\[
\det(C)<0,
\]

while A112-G proves on the complete localization strip

\[
A(s)<0.
\]

Therefore

\[
\boxed{D_G>0}
\]

without assuming \(p_j>0\) or \(p_{j+1}>0\).

The same certificate also reconstructs the exact A112-B orientation transfer

\[
\frac{\det B_8}{D_G}
=
\begin{cases}
\dfrac{2m-U(2m+1)}4,&M\text{ even},\\[6pt]
\dfrac{2m-U(m+1)}4,&M\text{ odd},
\end{cases}
\]

where \(m=1/M\) and \(U=2^{-h}\). The existing tail gates make both ratios strictly positive. Hence the complete eight-by-eight gamma-plus basis remains nonsingular throughout the localization strip.

### 2. The strict `b+1` compressed phase also gives \(E_{b+2}<0\)

A113 proves the strict central nesting

\[
\boxed{E_{b+1}-2E_{b+2}>0}.
\]

Under the present hypothesis \(E_{b+1}<0\), so

\[
2E_{b+2}<E_{b+1}<0,
\]

and therefore

\[
\boxed{E_{b+2}<0}.
\]

Thus the active-dual sign needed by A112-D is available for *both* candidate gamma-plus contacts `b+1` and `b+2`.

### 3. Minimal A112 composition lemma

The A112 logical composition audit records that the active-dual step A112-D is the **only** place in the full KKT closure where the compressed sign enters, and there it enters only as

\[
E_j<0.
\]

All other A112-A/B/C/E/F/G steps require the frozen tail domain, localization and adjacent primal positivity, but not \(E_{j-1}>0\) and not the statement that `j` itself is the compressed maximizer.

Consequently the already-proved A112 composition yields the following corollary:

> For a localized gamma-plus contact `j` in the analytic tail, if
> \(p_j>0\), \(p_{j+1}>0\), and \(E_j<0\), then every strict KKT condition of that basis holds.

This is a logical weakening of a hypothesis in the existing composition, not a new empirical extrapolation.

### 4. Cramer signs leave exactly one strict candidate when \(\Phi\ne0\)

A112-A proves the exact identities

\[
p_{j+1}=\frac{F_j^{\rm up}}{D_G},
\qquad
p_j=-\frac{F_{j+1}^{\rm up}}{D_G}.
\]

It also proves the uniform barriers

\[
F_k^{\rm up}>0\quad(k\le b+1),
\qquad
F_k^{\rm up}<0\quad(k\ge b+3).
\]

For contact \(j=b+1\),

\[
p_{b+2}=\frac{F_{b+1}^{\rm up}}{D_G}>0,
\qquad
p_{b+1}=-\frac{\Phi}{D_G}.
\]

Hence this basis has both adjacent masses positive iff \(\Phi<0\).

For contact \(j=b+2\),

\[
p_{b+2}=-\frac{F_{b+3}^{\rm up}}{D_G}>0,
\qquad
p_{b+3}=\frac{\Phi}{D_G}.
\]

Hence this basis has both adjacent masses positive iff \(\Phi>0\).

Because \(E_{b+1}<0\) and \(E_{b+2}<0\), the minimal A112 composition lemma closes the entire strict KKT system for the feasible candidate. Because every nonbasic reduced cost is strict, this strict KKT basis represents the unique global optimum of the declared finite LP. The other gamma-plus candidate is already primal-infeasible by the displayed adjacent mass.

This proves the two strict cases.

### 5. The zero pivot is a genuine degenerate transition

Suppose \(\Phi=0\).

For the `b+1` basis,

\[
p_{b+1}=0,
\qquad
p_{b+2}>0.
\]

For the `b+2` basis,

\[
p_{b+2}>0,
\qquad
p_{b+3}=0.
\]

Both full basis matrices are nonsingular because \(D_G>0\) and \(\det B_8/D_G>0\). They share seven columns. Since a subset of the columns of a nonsingular matrix is linearly independent, the representation of the right-hand side in those seven common columns is unique. Removing the zero pivot coefficient from each basis therefore leaves the same primal point.

A112-F/G proves

\[
p_j'(s)<0<p_{j+1}'(s)
\]

on the localization strip. Hence at a zero of the relevant adjacent mass there is a one-sided neighborhood on which one of the two gamma-plus branches has both adjacent masses strictly positive. The signs \(E_{b+1}<0\) and \(E_{b+2}<0\) persist locally by continuity. That neighboring branch is therefore strict global KKT by the preceding argument.

The basis matrix stays nonsingular at the zero, so its primal solution, dual solution, reduced costs and slacks are continuous rational functions of `s`. Passing to the limit yields primal and dual feasibility, complementary slackness and objective equality with non-strict inequalities at the pivot. Therefore the common degenerate point is a global optimum.

This argument deliberately does **not** promote strictness or uniqueness at the zero.

## Independent exact cross-check

A standalone exact-rational program, not importing the theorem certificate, checks three adversarial points.

1. `M=522, s=131/1000, b=90`: strict compressed winner `b+1`, \(\Phi<0\). Contact `b+1` passes all `1053=2M+9` KKT conditions; contact `b+2` fails exactly through `basic_p_93`.
2. `M=561, s=53/400, b=97`: strict compressed winner `b+1`, \(\Phi<0\). Contact `b+1` passes all `1131=2M+9` conditions; contact `b+2` fails exactly through `basic_p_100`.
3. `M=561, s=13277/100000, b=97`: strict compressed winner `b+1`, \(\Phi>0\). Contact `b+2` passes all `1131=2M+9` conditions; contact `b+1` fails exactly through `basic_p_98`.

The third case is the exact counterexample that refuted the earlier, stronger claim that a compressed `b+1` maximum must lift at the same contact.

## What this closes

A114-B1 closes the lifted selection problem in the strict compressed `b+1` phase:

\[
\boxed{
\begin{array}{c|c}
F_{b+2}^{\rm up}<0 & \text{gamma-plus contact }b+1\\
F_{b+2}^{\rm up}=0 & \text{degenerate global pivot point}\\
F_{b+2}^{\rm up}>0 & \text{gamma-plus contact }b+2
\end{array}}
\]

The scalar \(F_{b+2}^{\rm up}\) is therefore a **proved classifier for the strict compressed `b+1` phase**, not a universal classifier of all A114 architectures.

## Claim boundary

This theorem does **not** prove:

- the lifted architecture in a strict compressed `b+2` phase;
- that \(F_{b+2}^{\rm up}\) classifies the entire lifted problem;
- uniqueness or strict complementarity at \(F_{b+2}^{\rm up}=0\);
- anything outside `M>=521` and `129/1000<=s<=133/1000`;
- any physical interpretation.

The next unresolved target is A114-B2: classify the strict compressed `b+2` phase, where the `b+1` gamma-plus branch can be primal-feasible but has the wrong active-gamma dual sign because \(E_{b+1}>0\).
