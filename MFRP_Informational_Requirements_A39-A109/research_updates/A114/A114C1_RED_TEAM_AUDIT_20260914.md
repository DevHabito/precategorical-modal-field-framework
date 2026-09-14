# A114-C1 — independent red-team audit of the `b+1 / b+2` compressed tie

**Date:** 2026-09-14  
**Target:** `A114C1_BPLUS1_BPLUS2_COMPRESSED_TIE_THEOREM_20260914.md` on the staging branch derived from `a114-c-compressed-ties`.  
**Posture:** adversarial. The audit attempts to falsify the theorem by finding a hidden compressed tie, wrong determinant orientation, equality-by-continuity shortcut, unprotected dual sign, extra optimal direction, premature endpoint, or floating-point artifact.

## Verdict

**PASS WITH SCOPE.**

No counterexample or logical contradiction was found inside the declared analytic-tail contract. One proof-exposition gap was found during red-teaming: the original staging note explained why the optimal line could not pass beyond C/E, but did not explicitly rule out continuation through `G1+` in the opposite direction. The theorem was hardened before this verdict: gamma+ slack is zero at `G1+`, strictly positive at the C/E endpoint, and affine on the line, so continuation through `G1+` away from that endpoint makes gamma+ slack negative.

The supported scope is only

\[
M\ge521,\qquad 129/1000\le s\le133/1000,
\qquad E_{b+1}=0.
\]

The second compressed tie `E_(b+2)=0` remains open and is not imported into this result.

---

## 1. Triple-tie attack

A possible failure would be a simultaneous `b+1 / b+2 / b+3` compressed tie, invalidating the two-contact geometry.

A113 gives

\[
E_{b+1}-2E_{b+2}>0.
\]

On `E_(b+1)=0`, this forces

\[
E_{b+2}<0.
\]

Thus the compressed tie is exactly `b+1 / b+2`; no third compressed contact is tied. This is an analytic consequence, not a finite observation.

---

## 2. Attack on the `Phi>0` branch

At contact `b+2`, A112-A gives

\[
p_{b+3}=\Phi/D_G,
\qquad
p_{b+2}=-F_{b+3}^{up}/D_G.
\]

The promoted determinant orientation has `D_G>0`, the upper barrier has `F_(b+3)^up<0`, and the tie identity above has `E_(b+2)<0`. Therefore `Phi>0` gives adjacent primal positivity and exactly the compressed sign needed by A112-D.

The minimal A112 composition lemma does not require `E_(b+1)>0`; it only needs the localized contact, adjacent positivity and `E_j<0`. Hence the strict `G2+` conclusion is not obtained by illegally importing a strict-`b+2` theorem onto the tie.

No alternate optimum can coexist because all full-LP reduced costs and KKT gates are strict.

---

## 3. Attack on the new `y_gamma=0` dual argument

For `Phi<0`, contact `b+1` has both adjacent P masses strictly positive. A112-B/C/E/G and the pointwise Descartes argument therefore protect all primal masses and all variable reduced costs without using the sign of `E_(b+1)`.

A112-D gives exactly

\[
N_\gamma=-\frac{\det B}{D_G}E_{b+1},
\]

so the tie forces `y_gamma=0`.

The dangerous question is whether alpha or beta can also vanish or change sign at the same equality. The staging proof does not use continuity. With `y_gamma=0`, the P dual equations interpolate `tau^x` in

\[
\operatorname{span}\{1,x,\beta^x,s^x\}.
\]

An independently executed SymPy certificate gives the exact Wronskian

\[
W(1,x,e^{px},e^{qx})
=-p^2q^2(p-q)e^{(p+q)x}.
\]

For `p=log(a)<q=log(b)<0`, this is positive. Hence the ordered collocation determinants have the orientation used by the Cramer proof. With

\[
\beta<s<\tau<1,
\]

one obtains directly

\[
y_\alpha>0,
\qquad y_\beta>0,
\qquad y_\gamma=0.
\]

The symbolic certificate passes **5/5** exact algebra/sign-orientation gates. No floating-point sign is used.

---

## 4. Hidden-optimal-direction attack

A zero active multiplier can produce a larger optimal set than expected. Fix the `G1+` dual at the tie.

Every nonbasic P/Q variable has strictly positive reduced cost. Therefore any alternative primal optimum can use only the `G1+` support. Since `y_alpha,y_beta>0`, alpha+ and beta- must remain equalities at any optimum. Gamma+ may be released because `y_gamma=0`.

There are eight primal/support variables and seven independent equality rows after dropping gamma+. Independence is exact because restoring the gamma+ row gives the promoted nonsingular `G1+` basis. Thus the entire candidate optimal set is contained in one affine line; there is no second hidden zero-cost direction, including no QI/QA direction involving `q0`.

This directly rules out the concern that the strict `b+2` QI/QA branch could create an extra optimal face on the compressed tie.

---

## 5. Endpoint attack for `Phi<0`

The source-box lower argument is strict in the opposite direction:

\[
Q\le9/1000\Longrightarrow E_{b+1}<0.
\]

Therefore `E_(b+1)=0` itself gives `Q>9/1000`. The upper source bound depends on `Phi<0` through the promoted dyadic separation and remains valid. Hence the C1/C2 protected primal/slack bounds are available on the tie without assuming `E_(b+1)>0`.

The exact C/E exchange identity determines which non-gamma endpoint occurs:

- `p0^C>0`: C is feasible and is reached when `p_(b+1)=0`;
- `p0^C<0`: E is feasible and is reached when `p0=0`;
- `p0^C=0`: C and E coalesce.

All shared coordinates and inactive slacks are positive at both ends of each displayed segment, so the complete segment is feasible. Past C/E the defining endpoint mass becomes negative.

The first version of the staging proof did not explicitly close the other side of the line. That was hardened: gamma+ slack is zero at `G1+` and strictly positive at C/E. Since it is affine, extension through `G1+` in the direction opposite C/E makes gamma+ slack negative. Therefore the displayed segment is the entire feasible optimal face.

---

## 6. Codimension-two attack: `E_(b+1)=0` and `Phi=0`

This is the place where two independent zero gates could in principle create a two-dimensional or non-unique optimum.

The tie itself re-establishes the lower source box, while the promoted B2-E `Phi<=0` dyadic argument gives the upper source box. The exact B2-E gamma-zero elimination then yields the uniform separation

\[
p_0^C>0.
\]

Both gamma-plus bases collapse to C because their outer pivot masses vanish. C has

\[
S_{\gamma+}^C=0,
\qquad r_C(p_{b+1})=0,
\]

while the right neighboring P reduced cost is strict because `E_(b+2)<0`. ECT closure leaves `p_(b+1)` as the only zero-cost entering variable.

The remaining risk is the Schur sign. It was rederived independently. Appending the entering `p_(b+1)` column to C puts it in position 8; moving it to the declared GP1 P position requires six swaps, so determinant orientation is preserved. Both promoted basis determinants are positive. Therefore the Schur derivative

\[
d=\frac{\det B_{G1+}}{\det B_C}>0.
\]

For gamma+ the inactive slack is minus the active-row residual, hence

\[
S_{\gamma+}(z)=S_{\gamma+}^C-dz=-dz<0
\]

for every `z>0`. The only zero-cost direction is therefore blocked immediately by gamma+ feasibility. The primal optimum is unique although the basis representation is degenerate.

---

## 7. Rounding / numerical attack

No theorem sign is decided by ordinary floating point. The boundary regression uses exact `fractions.Fraction` arithmetic and records **24/24 PASS** across three deliberately different regimes:

- `GP1 -> C` across the tie with `Phi<0, p0^C>0`;
- `GP1 -> E` with `Phi<0, p0^C<0`;
- `GP2 -> GP2` with `Phi>0`.

The symbolic Wronskian/permutation certificate was executed independently and passes **5/5**. Numerical root locations, where used during discovery, are not proof premises.

---

## 8. Ad-hoc / overfitting attack

A tempting simpler rule — “the compressed tie always gives one particular lifted transition” — is false. The exact controls exhibit at least three different lifted behaviors. The theorem therefore keeps the already-existing discriminants `Phi` and `p0^C`; it does not add a fitted threshold after observing the outcomes.

No new physical or ontological interpretation is attached to the tie theorem.

---

## Verdict and reopen conditions

**PASS WITH SCOPE.** A114-C1 is internally consistent with the promoted A112/A113/A114 identities and survives the red-team checks above.

It must be reopened if any upstream result used here is retracted, especially:

1. A113 central nesting;
2. A114-B1 determinant orientation;
3. A112 reduced-cost closure under adjacent positivity;
4. C1/C2 source-box or endpoint-primal bounds;
5. B2-E `Phi<=0` dyadic/source-box and `p0^C>0` separation.

This audit does not certify the still-open second tie `E_(b+2)=0`, any extension outside the frozen source window, or any physical claim.