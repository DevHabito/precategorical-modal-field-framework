# A114-B2-D — independent red-team audit

**Date:** 2026-09-14  
**Target branch audited:** `a114-b2-d-internal-boundaries` at `46ce222e4c9769ee6fb9de5d2202f6e544e0c1ed`  
**Audit posture:** adversarial. The purpose is to find a counterexample, hidden premise, circularity, rounding dependency, or ad-hoc repair — not to confirm the intended conclusion.

## Verdict

**PASS WITH SCOPE.**

No mathematical contradiction, hidden sign reversal, circular dependency, floating-point sign decision, or ad-hoc case repair was found in A114-B2-D after the checks below.

The supported statement is narrow:

> Under the already-frozen analytic-tail contract (`M>=521`, `129/1000<=s<=133/1000`, strict compressed `b+2`, `Phi<0`), the three internal equality sets `p0^C=0`, `r_E(q0)=0`, and `Gamma=0` have the boundary behavior stated in A114-B2-D.

This audit does **not** certify the physical interpretation of the framework, does not justify the frozen parameter window as physically privileged, does not close `Phi=0`, and is not a from-first-principles re-audit of every theorem before C1/C2/C3.

---

# 1. Threat model

The audit tried to falsify D through five failure modes.

1. **Boundary-by-continuity shortcut** — a quantity is assumed positive at equality merely because it was positive on a neighboring strict branch.
2. **Circular pivot logic** — a boundary theorem uses feasibility or optimality of the architecture that the boundary theorem is supposed to establish.
3. **Hidden optimal directions** — a zero reduced cost is interpreted as one segment while another zero-cost direction or another inequality creates a larger/different optimal face.
4. **Floating-point sign corruption** — extremely ill-conditioned exponential matrices cause the sign of a pivot, mass, slack, or reduced cost to be a numerical artifact.
5. **Ad-hoc classification** — thresholds or extra hypotheses are introduced after seeing the desired phase sequence and are then used to manufacture the conclusion.

The audit also checked higher-codimension overlap of the three internal equality conditions for logical consistency.

---

# 2. D1: `p0^C=0`

## Claim audited

At `p0^C=0`, the primal optimum is unique; `C`, `E`, and `QI` collapse to the same primal point after deletion of their zero pivot coordinates.

## Direct boundary feasibility

The most dangerous shortcut would have been to infer feasibility at `p0=0` only by continuity from `p0>0`. D does not need that shortcut.

At the boundary the exact beta equation is

\[
K_\beta t=C_\beta,
\qquad
Ut=\frac{C_\beta}{K_\beta/U}.
\]

The D boundary certificate, using the inherited exact rational envelopes, gives

\[
0.9954572159\ldots<Ut<0.9957514605\ldots
\]

for even `M`, and

\[
1.3271455640\ldots<Ut<1.3276686139\ldots
\]

for odd `M`.

Therefore the boundary `q1` numerator has a direct margin of about

\[
8.497\times10^{-3},
\]

in either parity; it is not a near-zero numerical decision. The inherited `q_h`/`q_(h+1)` bounds and `lambda<1.216<2` then protect the remaining nonzero basic masses.

The active-dual and reduced-cost signs of `C` do not depend on assuming `p0>0`; the C2 proof gives them uniformly on the frozen strict-`b+2`, `Phi<0` domain. The gamma-minus slack becomes

\[
S_{\gamma-}^C=A_0/K_\beta>0
\]

at `p0=0`, and the exact gamma-plus pivot relation remains protected by `Phi<0`.

Thus the only lost strict KKT gate is `p0=0` itself.

## Uniqueness

The `C` dual has strictly positive reduced costs on every nonbasic primal column. Any alternative optimal primal solution must therefore use only the `C` basic columns. Those columns are nonsingular, so the right-hand side has only one representation on that column set. The zero coefficient of the basic `p0` column creates basis degeneracy but does not create a second primal solution.

The promoted exact pivot identities give

\[
p_{j-1}^E=0,
\qquad
q_0^{QI}=0
\]

when `p0^C=0`. Removing the zero columns leaves the same positive support and the same equality system, so the three primal representations coincide.

**D1 audit result: PASS.**

---

# 3. D2: `p0^C<0`, `r_E(q0)=0`

## Claim audited

This surface is not merely a degenerate representation of one point. It has a genuine one-dimensional primal optimal face.

This was the highest-risk part of D.

## Exactly one zero nonbasic reduced cost

At the boundary all protected E primal/dual/slack/P-reduced-cost gates remain strict. The only C1 Q checkpoint that loses strictness is

\[
r_E(q_0)=0,
\]

while

\[
r_E(q_2)>0.
\]

The E Q reduced-cost function is a nonzero member of the five-dimensional ECT family used by C1. At this boundary it has the four distinct real roots

\[
0,1,h,h+1.
\]

The ECT zero budget is four, counting multiplicity. Hence there can be no fifth root and none of these four roots can have multiplicity greater than one. Since `q2` lies between `1` and `h` and has positive reduced cost, sign alternation implies every nonbasic integer Q reduced cost other than `q0` is strictly positive.

Therefore the E dual has exactly one zero nonbasic reduced cost.

## Why the full optimal set is one line

Fix that E dual optimum. Zero primal-dual gap forces every variable with strictly positive E reduced cost to remain zero in any other primal optimum. Thus only the E basic columns plus `q0` may appear.

The E basis has seven independent columns. Adding one `q0` column produces an eight-variable affine system with the same seven independent active equalities, so its solution set has dimension exactly one. There is no hidden second zero-cost direction.

Because `q0=0` at E and all E basic masses/slacks are strict, the feasible optimal set begins as a nontrivial interval leaving E in the positive-`q0` direction.

## Endpoint audit

The only remaining question is whether another constraint cuts this line before the endpoint asserted by D.

- The opposite alpha/beta slacks remain `4 epsilon t>0` on the edge.
- Gamma-plus is positive at E; at a QA endpoint it is the opposite slack of gamma-minus and equals `4 epsilon t>0`. On an E-to-QI endpoint with `Gamma>=0`, it is also positive by the promoted QI gamma-plus margin.
- For `Gamma<0`, the gamma-minus slack is affine, positive at E and negative at the formal QI endpoint, so it has exactly one zero before QI. That zero is the QA solution. E and QA have all common coordinates positive, and `p_(j-1)^QA>0`; every coordinate is affine on the line, so no nonnegativity boundary can occur before QA.
- For `Gamma>0`, the formal QI endpoint is primal-positive; both endpoints have positive common coordinates and positive gamma-minus slack, so the feasible interval reaches QI.
- For `Gamma=0`, the Schur identity gives `p_(j-1)^QA=0`; QA and QI reduce to the same primal equations and the direct QA common-mass bounds remain strict at the endpoint.

Hence the full primal optimal face is exactly

\[
\operatorname{conv}\{E,QI\}
\]

when `Gamma>=0`, and

\[
\operatorname{conv}\{E,QA\}
\]

when `Gamma<0`.

No use is made of the previously rejected false statement that QI must remain primal-feasible on the QA side.

**D2 audit result: PASS.**

---

# 4. D3: `p0^C<0`, `r_E(q0)<0`, `Gamma=0`

## Claim audited

QI and QA represent the same primal point and that primal optimum is unique.

The exact C3 Schur identity gives

\[
U p_{j-1}^{QA}
=-\Gamma D_Q/D_{QA}=0.
\]

The QA common-mass bounds remain strict when this exchanged coordinate is zero. QI itself saturates gamma-minus at `Gamma=0`, so deleting the zero QA pivot leaves exactly the QI primal system.

The separate residual identity gives

\[
r_{QI}(p_{j-1})
=-r_E(q_0)D_E/D_Q>0
\]

because the present D3 premise has `r_E(q0)<0` and both determinants have certified positive orientation. Every other QI nonbasic reduced cost is already strictly positive, and its active alpha/beta multipliers are positive. Gamma-plus remains strictly slack.

Thus any alternative optimum is restricted to the QI support and active alpha/beta equalities; nonsingularity of the QI basis forces the same primal point. The tight inactive gamma-minus inequality does not create an additional primal direction because its multiplier in the QI dual is zero while all nonbasic primal reduced costs stay strict.

**D3 audit result: PASS.**

---

# 5. Higher-codimension consistency

The theorem hierarchy avoids contradictory overlap.

- D2 explicitly requires `p0^C<0`, so a hypothetical simultaneous `p0^C=0` and `r_E(q0)=0` point is governed by D1, not by the D2 face claim. At such a degenerate E representation the zero `q0` reduced cost need not produce a feasible direction because `p_(j-1)^E` is already zero.
- D3 explicitly requires `r_E(q0)<0`, so the intersection `r_E(q0)=0`, `Gamma=0` is governed by D2. There the QI/QA endpoint is part of the one-dimensional E face, not a standalone unique optimum.

No contradiction was found between D1, D2 and D3 on their stated premises.

---

# 6. Independent exact reconstruction

The raw lifted LP was independently reconstructed with rational arithmetic using a separate SymPy-based solve, rather than importing the A114-B2-D project scripts.

For all ten published even/odd controls (`M=538` and `M=555`, covering E, QA, QI, C and GP), the independent reconstruction found:

- exact basis equations;
- exact primal-dual equality;
- all selected basic variables positive;
- all selected active multipliers positive;
- all inactive slacks positive;
- zero nonbasic P reduced-cost violations;
- zero nonbasic Q reduced-cost violations.

The result agrees with the repository `30/30` Fraction regression, but was obtained through a different exact linear-algebra implementation.

A second adversarial test used rational points only `~10^-8` away from each of the four transitions in one even and one odd tail cell. All sixteen points retained strict compressed `b+2`; on the two sides of each transition the full exact KKT winner switched exactly as predicted:

\[
E\leftrightarrow QA,
\qquad
QA\leftrightarrow QI,
\qquad
QI\leftrightarrow C,
\qquad
C\leftrightarrow G^+.
\]

Every one of those sixteen side controls passed complete exact KKT for the predicted basis.

This is falsification/regression evidence. It is not used as the all-tail proof.

---

# 7. Exact boundary isolation and rounding audit

The internal transitions were independently isolated by bisection in **rational arithmetic**, evaluating the discriminant sign exactly at each rational endpoint.

For `M=538`, `j=94`, the approximate enclosing intervals after exact-sign bisection were:

- `r_E(q0)=0`: `[0.129202961349..., 0.129202962494...]`;
- `Gamma=0`: `[0.129601972313..., 0.129601973114...]`;
- `p0^C=0`: `[0.129624687805..., 0.129624687958...]`;
- `Phi=0`: `[0.129698549309..., 0.129698549576...]`.

For `M=555`, `j=97`:

- `r_E(q0)=0`: `[0.129813491821..., 0.129813492584...]`;
- `Gamma=0`: `[0.129983379021..., 0.129983379364...]`;
- `p0^C=0`: `[0.130008143463..., 0.130008143654...]`;
- `Phi=0`: `[0.130085841599..., 0.130085841827...]`.

The decimal endpoints above are display renderings only; the sign decisions were made on exact rational endpoints. These checks show that the observed transitions in the two adversarial cells are not floating-point root coincidences.

The exact `b` index was also recomputed by an integer-only monotone binary search, with no logarithm or floating-point initial guess, and matched the project value on the tested endpoints and representative grid points.

---

# 8. Why ordinary floating point is not acceptable here

As a deliberate countertest, unscaled double-precision condition numbers were estimated for the five relevant basis matrices at a representative `M=538` control. They were of order

\[
10^{18}\text{ to }10^{22}.
\]

That is far beyond a regime in which a `float64` sign near a transition should be trusted. This audit therefore rejects ordinary double-precision root solving or KKT sign checks as certification evidence.

The D certificates themselves make sign decisions with exact `Fraction` arithmetic. Their decimal hard margins are presentation only. This is the correct numerical policy for the present tail problem.

---

# 9. Ad-hoc / overfitting audit

No new branch-defining threshold was introduced by D.

The numbers such as `Ut>0.995`, `Ut>1.327`, `lambda<1.216`, or the displayed decimal determinant margins are weaker rational consequences of the already-frozen contract. They are proof margins, not fitted conditions used to choose which data are accepted.

The theorem also explicitly refuses a tempting overgeneralization: the observed phase order in some cells is **not** promoted to a universal monotone ordering in `s`.

No theorem statement was widened to include `Phi=0`, points outside `[129/1000,133/1000]`, or a physical interpretation.

**Ad-hoc audit result: no ad-hoc repair detected inside D.**

---

# 10. Remaining risks and nonclaims

This PASS should not be read as “the whole research programme is now independently proved from zero.” The following remain separate tasks.

1. A future clean-room audit should rederive the upstream C1/C2/C3 determinant and ECT inputs from the raw LP, without trusting their promoted certificates.
2. The outer `Phi=0` boundary is still open in the strict compressed `b+2` phase.
3. The frozen tail/source window is a mathematical scope condition, not an experimentally established law of nature.
4. None of D identifies a physical ontology, spacetime, matter, gravity, or an origin law for the pre-categorical framework.
5. Finite controls, however adversarial, are not substitutes for the all-tail analytic arguments.

---

# Final audit statement

After adversarial review, the evidence supports keeping A114-B2-D as a **conditional mathematical boundary theorem** under its declared frozen contract.

The most important substantive point survived the red-team check: `r_E(q0)=0` is genuinely different from `p0^C=0` and `Gamma=0`. It produces a one-dimensional primal optimal face, while the other two internal boundaries retain a unique primal optimum with basis degeneracy.

No counterexample or hidden rounding dependency was found. If a later clean-room audit invalidates one of the upstream C1/C2/C3 identities used by D, D must of course be reopened; this audit does not immunize inherited premises from future falsification.