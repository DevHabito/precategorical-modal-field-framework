# A112 — analytic-tail structural theorem

## Status

**PROVED, under the frozen gamma-plus family and strict compressed-phase hypotheses.**

Domain:

\[
M\ge521,\qquad \frac{129}{1000}\le s\le\frac{133}{1000}.
\]

Frozen architecture:

\[
P=\{0,j,j+1,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

with active signs alpha+, beta-, gamma+.

No new canonical full-KKT/full-atlas outcome after rank 430 is used in the proof package recorded here.

## Theorem

Fix `M>=521` and a contact `j`. On any source interval inside the frozen source window on which `j` is a strict compressed maximizer for the frozen gamma-plus family, the complete strict KKT conditions for the corresponding basis hold exactly where

\[
p_j(s)>0,\qquad p_{j+1}(s)>0.
\]

The common-positive set is an interval, possibly empty. Its only possible internal KKT boundaries are

\[
\boxed{p_{j+1}=0\ \text{on the left},\qquad p_j=0\ \text{on the right}.}
\]

Source-window endpoints or compressed-phase endpoints may of course truncate the interval externally.

## Proof map

### 1. Contact localization — A112-A

The exact Cramer bridge gives

\[
p_{j+1}=\frac{F_j^{up}}{D_G},\qquad
p_j=-\frac{F_{j+1}^{up}}{D_G}.
\]

Uniform left/right barriers for `F_k^{up}` imply

\[
p_j,p_{j+1}>0
\Longrightarrow
j=\lceil Mc(s)\rceil+1\ \text{or}\ \lceil Mc(s)\rceil+2.
\]

### 2. q2 pivot-square interlacing — A112-B

Write the primal-boundary numerator and q2 augmented determinant as affine functions of

\[
R=s^j/2^{-h}.
\]

The linear resultant orders the two roots. Exact orientation identities give `D_G>0` and `det B>0` under adjacent positivity. The uniform determinant certificate then proves

\[
\boxed{p_j,p_{j+1}>0\Longrightarrow R_Q(2)>0.}
\]

### 3. All nonbasic reduced costs — A112-C

Uniform resultant certificates show

\[
R_Q(2)>0
\Longrightarrow
r_P(1),R_Q(0),R_Q(h-1),R_Q(h+2),R_Q(M)>0.
\]

The pre-existing generalized-Vandermonde P-collapse and Q5 extended-Chebyshev theorem then give positivity of every nonbasic P/Q reduced cost.

### 4. Active duals — A112-D

The gamma multiplier numerator obeys the exact identity

\[
\boxed{N_\gamma=-\frac{\det B}{D_G}E_j.}
\]

Inside a strict compressed phase `E_j<0`; under adjacent positivity `det B/D_G>0`. Hence `y_gamma>0`. The pre-existing active-dual collapse then gives

\[
y_\alpha>0,\qquad y_\beta>0,\qquad y_\gamma>0.
\]

### 5. Q basic masses — A112-E/G

A112-E proves

\[
p_{j+1}>0\Longrightarrow q_h>0.
\]

A112-G proves

\[
p_j>0\Longrightarrow q_1>0.
\]

The exact Q-block formulas then give `q_(h+1)>0`, and `t>0` follows.

### 6. Extreme P masses — pointwise Descartes argument

With `q_1,q_h,q_(h+1),p_j,p_(j+1)>0`, the active equations force four positive roots counting multiplicity in the signed generating polynomial. If `p_0<=0`, the coefficient sequence has at most three sign changes, contradiction. Thus `p_0>0`. With `p_0>0`, the same argument excludes `p_M<=0`.

Therefore all basic masses are strictly positive.

### 7. Inactive slacks

The active equalities imply identically

\[
S_{\alpha-}=S_{\beta+}=S_{\gamma-}=4\varepsilon t>0.
\]

### 8. No hidden components — A112-F/G

The source-independent primal slopes satisfy

\[
\frac{\partial p_j}{\partial t}<0,
\qquad
\frac{\partial p_{j+1}}{\partial t}>0.
\]

A112-G proves branch regularity

\[
A(s)<0<B(s),\qquad t(s)=-B(s)/A(s)>0,
\]

while A112-F proves the chain-rule numerator `BA'-B'A>0`. Therefore

\[
t'(s)>0,
\]

and hence

\[
\boxed{p_j'(s)<0,\qquad p_{j+1}'(s)>0.}
\]

For fixed `M,j`, A112-A confines every common-positive point to the localization strip

\[
j=\lceil Mc(s)\rceil+1\ \text{or}\ +2,
\]

which is an interval because `c(s)` is increasing. The two opposite monotonicities therefore make the common-positive set a single interval with no hidden islands.

This completes the theorem.

## Relationship to A110

A110 already proves the same local adjacent-boundary mechanism on the frozen finite contract

\[
14\le M\le520.
\]

A112 supplies the analytic-tail closure for `M>=521`. Thus the same local structural mechanism is now covered for every `M>=14` **within the frozen gamma-plus architecture and its declared source window**, with the finite and tail proofs kept distinguishable.

## Nonclaims

This theorem does **not** establish:

- global selection of the gamma-plus architecture among all possible LP architectures for every `(M,s)`;
- an unrestricted theorem over all support/band patterns;
- any source interval outside `[129/1000,133/1000]`;
- any physical, spacetime, gravity, quantum, or experimental interpretation.

It also does not erase the historical finite/prospective evidence program. The proof is an analytic structural result under explicit hypotheses; the old finite atlases remain separate evidence and provenance.

## Reproducibility

See the sibling A112-B ... A112-G audit scripts and JSON outputs, the logical composition audit, and `MANIFEST_A112_TAIL_CLOSURE_20260911.sha256`.
