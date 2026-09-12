# A112 logical composition audit — 2026-09-11

## Verdict

**PASS — conditional analytic-tail structural theorem for the frozen gamma-plus family.**

The composition A112-A/B/C/D/E/F/G is logically sufficient, with no circular dependency, to prove the two-sided adjacent-boundary rule on the frozen analytic tail

\[
M\ge521,\qquad 129/1000\le s\le133/1000,
\]

for the gamma-plus architecture

\[
P=\{0,j,j+1,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

**inside a strict compressed-maximizer phase for the fixed contact `j`**.

This is not a theorem that the gamma-plus architecture is globally selected among all possible architectures for every `(M,s)`.

---

## Theorem obtained by composition

Fix an integer `M>=521`, a contact `j`, and a source interval contained in `[129/1000,133/1000]` on which the frozen gamma-plus basis is considered and the compressed contact is strict, in particular

\[
E_j(s)<0
\]

(and, for a strict interior compressed maximum, `E_{j-1}(s)>0`).

Then the full strict KKT conditions for this basis hold exactly where

\[
p_j(s)>0,\qquad p_{j+1}(s)>0.
\]

Moreover this common-positive set is an interval (possibly empty). Its only possible **internal** KKT boundaries are

\[
\boxed{p_{j+1}=0\quad\text{on the left},\qquad p_j=0\quad\text{on the right}.}
\]

External endpoints may instead be source-window or compressed-phase endpoints.

---

## Dependency audit

### A112-A — localization

From `p_j>0` and `p_{j+1}>0`, exact Cramer identities and the upper-boundary barriers give

\[
j=b+1\quad\text{or}\quad j=b+2,\qquad b=\lceil Mc(s)\rceil.
\]

No strict-compressed assumption is needed for this implication.

### A112-B — q2 interlacing

Under adjacent positivity and A112-A localization:

- `D_G>0` follows from the signed upper-boundary barriers;
- `det(B)/D_G>0` is an exact parity identity;
- the two affine-in-`R` boundaries satisfy `R_P>R_Q`.

Hence

\[
p_j,p_{j+1}>0\Longrightarrow R_Q(2)>0.
\]

### A112-C — all nonbasic reduced costs

A112-C proves, uniformly on the tail,

\[
R_Q(2)>0
\Longrightarrow
r_P(1),R_Q(0),R_Q(h-1),R_Q(h+2),R_Q(M)>0.
\]

The pre-existing generalized-Vandermonde P-collapse and the six-dimensional extended-Chebyshev Q5 theorem then give positivity of **every** nonbasic P/Q reduced cost.

The localization bounds imply `2<=j<=h-2`, so the hypotheses of those structural reductions are satisfied.

### A112-D — active duals

The exact identity is

\[
N_\gamma=-\frac{\det B}{D_G}E_j.
\]

Under adjacent positivity `det(B)/D_G>0`; inside a strict compressed phase `E_j<0`. Thus `y_gamma>0`. The pre-existing active-dual theorem D1 then forces

\[
y_\alpha>0,\qquad y_\beta>0,\qquad y_\gamma>0.
\]

This is the only point in the KKT closure that needs the strict-compressed sign `E_j<0`.

### A112-E — central Q mass

The source-independent affine comparison proves

\[
p_{j+1}>0\Longrightarrow q_h>0.
\]

Consequently `t>0`, because the exact Q-block formula for `q_h` requires `t` to lie above a positive threshold.

### A112-F1 — source-independent adjacent slopes and derivative numerator

Without using A112-G, A112-F certifies

\[
\frac{\partial p_j}{\partial t}<0,
\qquad
\frac{\partial p_{j+1}}{\partial t}>0,
\]

and the exact chain-rule numerator

\[
BA'-B'A>0.
\]

The latter alone is not yet a complete statement about `t'(s)` until `A!=0` is known.

### A112-G1 — branch regularity

Using

\[
Z=\frac YR=\left(\frac{1/8}{s}\right)^j<\frac3{50},
\]

A112-G proves on the entire localization strip

\[
\boxed{A(s)<0<B(s)}.
\]

Thus

\[
t(s)=-\frac{B(s)}{A(s)}>0
\]

and the branch has no pole on the strip.

Combining this with A112-F's positive numerator gives

\[
\boxed{t'(s)>0}.
\]

Therefore

\[
\boxed{p_j'(s)<0,\qquad p_{j+1}'(s)>0}.
\]

There is no circularity: A112-G1 does not use `t'(s)` or adjacent monotonicity.

### A112-G2 — lower Q endpoint mass

At the exact `q_1=0` threshold, A112-G proves

\[
p_j\big|_{q_1=0}<0.
\]

Together with `partial p_j/partial t<0`, this yields the pointwise implication

\[
\boxed{p_j>0\Longrightarrow q_1>0}.
\]

No historical strict witness is needed.

### Remaining basic variables — pointwise Descartes argument

From adjacent positivity:

- A112-E gives `q_h>0` and hence `t>0`;
- A112-G gives `q_1>0`;
- for even `M`, `q_{h+1}=(h-1)q_1>0`;
- for odd `M`, the exact Q-block formula gives `q_{h+1}>0` whenever `t>0`.

The signed generating polynomial therefore has known signs

\[
?,\ -,+,+,-,-,\ ?
\]

at the support positions `0,1,j,j+1,h,h+1,M`.
The active equations with `t>0` force one root in `(gamma,beta)`, one in `(beta,s)`, and a double root at `1`: at least four positive roots counting multiplicity.

If `p_0<=0`, the nonzero coefficient sequence has at most three sign changes, contradicting Descartes. Hence `p_0>0`. With `p_0>0`, if `p_M<=0` there are again at most three sign changes. Hence

\[
\boxed{p_0>0,\qquad p_M>0}.
\]

This upgrades the old "cannot be the first zero" argument into a pointwise sign proof and removes the need for a strict anchor.

### Inactive slacks

The frozen active equalities give identically

\[
S_{\alpha-}=S_{\beta+}=S_{\gamma-}=4\varepsilon t>0.
\]

Thus all inactive band slacks are strict.

---

## Connectedness / no hidden islands

For fixed `M,j`, A112-A implies every point with both adjacent masses positive lies in

\[
S_j=\{s:\ j=\lceil Mc(s)\rceil+1\text{ or }+2\}.
\]

Since `c(s)` is strictly increasing,

\[
S_j=\{s:\ j-3<Mc(s)\le j-1\}
\]

(up to intersection with the frozen source window), hence `S_j` is an interval.

On all of `S_j`, A112-G gives a regular continuous branch and A112-F/G give

\[
p_j'(s)<0<p_{j+1}'(s).
\]

Therefore `p_j>0` is a left interval and `p_{j+1}>0` is a right interval. Their intersection is one interval. No disconnected strict-KKT island can be hidden behind a pole because `A(s)<0` throughout `S_j`.

---

## Quantifier and circularity audit

- `M`: integer, uniformly all `M>=521`.
- `s`: every real source in the closed frozen interval.
- parity: proved separately even/odd where needed.
- `j`: fixed integer contact; adjacent positivity automatically localizes it to `b+1` or `b+2`.
- support ordering required by the generalized-Vandermonde/Q5 lemmas follows automatically from tail localization.
- no finite `M` grid is used in A112-A/B/C/D/E/F/G proofs.
- no post-rank-430 canonical full-atlas outcome is used.
- no proof step uses its own conclusion. The only apparent dependency (`t'` versus branch regularity) is resolved by splitting A112-F into numerator/slopes first and invoking A112-G regularity afterwards.

---

## What can now be claimed

### PROVED

For the frozen gamma-plus architecture, on every strict compressed-maximizer phase in the analytic tail `M>=521`, the A109 two-sided local rule is a theorem:

\[
\text{strict KKT}\iff p_j>0\text{ and }p_{j+1}>0,
\]

and the only internal KKT boundaries are the two adjacent masses, left `p_{j+1}=0` and right `p_j=0`.

Together with the finite A110 result, this gives the same structural mechanism on the declared finite and analytic-tail regimes of the frozen gamma-plus family.

### NOT PROVED

This composition does **not** prove:

1. that the gamma-plus architecture is the globally selected LP architecture for every `M,s`;
2. that every possible active-band/support architecture obeys the same rule;
3. any statement outside `s in [129/1000,133/1000]`;
4. any physical interpretation;
5. a new canonical full-atlas outcome after rank 430.

Accordingly the safe phrase is **"all-M analytic structural theorem within the frozen gamma-plus strict-compressed family"**, not an unrestricted global all-M theorem.

---

## Repository-status note

The repository file `A112_PIVOT_SQUARE_STATUS_NOTE.md` at parent commit
`d1b1a951618d3778b43f04698111db5643ed5414` still says `OPEN / INCONCLUSIVE`.
That statement predates A112-B through A112-G. The mathematical status in this audit is newer than the repository note; the repository should not be described as updated until these certificates and a revised status note are actually committed.
