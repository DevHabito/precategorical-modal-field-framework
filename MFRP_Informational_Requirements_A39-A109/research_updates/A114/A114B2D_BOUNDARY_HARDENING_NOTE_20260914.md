# A114-B2-D boundary hardening note

**Status:** supporting proof note for the staging branch `a114-b2-d-internal-boundaries`. This note does not extend the theorem scope.

## 1. Direct `Ut` bounds at `p0^C=0`

At the D1 boundary the exact C beta row is

\[
K_\beta t=C_\beta.
\]

The promoted C2 certificate bounds `C_beta` and the normalized coefficient `K_beta/U` uniformly. Therefore

\[
Ut=\frac{C_\beta}{K_\beta/U}.
\]

Using the same exact rational envelopes as `a114b2c2_compressed_branch_analytic_certificate.py` gives the conservative numerical consequences

\[
\boxed{0.9954<Ut<0.9958<1}\qquad(M\text{ even}),
\]

and

\[
\boxed{1.3271<Ut<1.3277<4/3}\qquad(M\text{ odd}).
\]

(The underlying exact-rational bounds are stronger; decimals here are only readable outward roundings.)

Hence the exact C2 formulas give immediately

\[
q_1=\frac{2(1-Ut)}{1-(h+1)U}>0
\]

for even `M`, and

\[
q_1=\frac{2-\frac32Ut}{1-(h+1)U}>0
\]

for odd `M`.

The lower bound on `Ut`, together with `h>=260`, also gives the same strict `q_h>0` margin used in C2, followed by `q_(h+1)>0` from the exact central-Q identities. Thus D1 does not need a continuity argument for primal feasibility: the nonzero basic masses are directly protected at `p0=0`.

The P masses are even simpler:

\[
p_j=\frac\lambda2t>0,
\qquad
p_M=\left(1-\frac\lambda2\right)t>0,
\]

because `t>0` and the promoted tail bound gives `lambda<1.216<2`.

## 2. Why the `r_E(q0)=0` optimum set is exactly one segment

At the D2 boundary, the E basis has:

- all basic primal variables strictly positive;
- both active multipliers strictly positive;
- all inactive gamma slacks strictly positive;
- every nonbasic P reduced cost strictly positive;
- `r_E(q0)=0`;
- every other nonbasic Q reduced cost strictly positive by the four-root ECT argument.

Fix the E dual optimum. For any other primal optimum, zero primal-dual gap forces every primal variable with strictly positive E reduced cost to remain zero. Therefore an alternative optimum can use only

\[
P=\{j-1,j,M\},
\qquad
Q\subseteq\{0,1,h,h+1\},
\]

with `q0` the only possible new nonbasic variable.

Because the E alpha+ and beta- multipliers are strictly positive, every optimum must also keep those two inequalities saturated. Thus every optimum lies in the affine system formed by

- the two normalizations;
- the two mean equations;
- the target equation;
- alpha+ equality;
- beta- equality;

on the eight variables corresponding to

\[
P=\{j-1,j,M\},\quad Q=\{0,1,h,h+1\},\quad t.
\]

The E basis is nonsingular. Adding the single column `q0` to its seven basis columns therefore produces an affine solution set of dimension exactly one. Hence the complete optimal set is contained in the single E-to-q0 simplex line; there is no hidden second optimal direction.

The feasible part of that line starts at E because all E basic variables and inactive slacks are strict. Its far endpoint is determined as follows.

### `Gamma>0`

The formal QI endpoint has `q0>0` from `p0^C<0`. The QI primal proof uses `p0^C<0` and `Gamma>0`; the strict sign `r_E(q0)<0` is needed for the QI *reduced cost* `r_QI(p_(j-1))`, not for QI primal positivity. Thus at `r_E(q0)=0, Gamma>0`, QI is a positive primal endpoint. Since both E and QI have positive common coordinates and positive gamma-minus slack, the complete feasible optimal interval is

\[
\boxed{\operatorname{conv}\{E,QI\}}.
\]

### `Gamma=0`

The Schur identity gives

\[
U p_{j-1}^{QA}=-\Gamma D_Q/D_{QA}=0.
\]

QI simultaneously has zero gamma-minus slack. The QA system with its zero pivot coordinate and the QI system therefore share the same primal variables and equations; the direct QA common-mass bounds at `w=0`, together with `q0^QI>0`, make this a positive endpoint. Hence

\[
QA=QI
\]

as primal points and the complete optimal interval is again

\[
\boxed{\operatorname{conv}\{E,QI\}}.
\]

### `Gamma<0`

The gamma-minus slack is affine along the E-to-formal-QI line. It is strictly positive at E and negative at the formal QI endpoint, so there is a unique gamma-zero cut before QI. That cut is exactly QA. The pivot identity gives

\[
p_{j-1}^{QA}>0,
\]

and the C3 direct QA estimates protect all common masses; `q0^QA>0` follows from the strict interior position of the cut. Thus no nonnegativity boundary occurs before the gamma cut. The complete feasible optimal interval is

\[
\boxed{\operatorname{conv}\{E,QA\}}.
\]

This proves that D2 is not merely an existence statement for a zero-cost segment: the displayed segment is the entire primal optimal face.

## 3. Scope discipline

Nothing in this note proves a universal ordering of the zero surfaces as `s` varies. Exact rational controls show that the full strict sequence `E -> QA -> QI -> C -> G+` occurs in at least one even and one odd tail cell, but other cells can skip some regions. The theorem is therefore discriminant-based, not an asserted monotone phase-order theorem.

The outer boundary `Phi=0` is not addressed here.