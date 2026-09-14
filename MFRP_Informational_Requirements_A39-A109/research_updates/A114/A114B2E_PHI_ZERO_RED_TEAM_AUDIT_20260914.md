# A114-B2-E — independent red-team audit of the `Phi=0` boundary

**Date:** 2026-09-14  
**Target:** `a114-b2-e-phi-zero`  
**Posture:** adversarial. The objective is to break the proposed C/G+ zero-pivot theorem, not to confirm it.

## Verdict

**PASS WITH SCOPE.**

No counterexample, hidden `Phi<0` dependency, circular pivot argument, sign reversal, rounding-dependent sign decision, or ad-hoc extra hypothesis was found in the proposed A114-B2-E theorem.

The supported statement remains narrow:

> Under `M>=521`, `129/1000<=s<=133/1000`, strict compressed `b+2`, and `Phi=0`, the full lifted LP has a unique primal optimum represented degenerately by C and G+; C has gamma+ tight with zero C-dual multiplier, while G+ has zero pivot mass `p_(j+1)`.

This audit does not certify any physical interpretation, does not extend the source window, and is not a from-first-principles re-proof of every dependency before A112/A113/A114.

---

## 1. Threat model

The audit tried to falsify E through six routes:

1. **Illegal continuity:** infer positivity at `Phi=0` only because a neighboring strict branch is positive.
2. **Hidden use of `Phi<0`:** import C2 wholesale even though C2 was originally stated only on the negative-pivot branch.
3. **Higher-codimension collision:** allow `Phi=0` to coincide with `p0^C=0` or another primal boundary.
4. **Pivot-sign error:** get the sign relation between `Phi` and `S_(gamma+)^C` backwards.
5. **False uniqueness:** confuse a tight inactive inequality with a genuine zero-cost primal direction.
6. **Numerical artifact:** decide a near-boundary sign using floating point rather than exact arithmetic.

---

## 2. `Phi=0` does not require a continuity extension of B2-B

The first part of A114-B2-B was stated under `Phi<0`, but the contradiction itself proves the standalone implication

\[
3j-h\le12
\Longrightarrow
\Phi>1.0392108565\times10^{-6}>0.
\]

The derivation of that positive lower bound does not use `Phi<0`; `Phi<0` appears only as the contradiction target in the original presentation. Therefore the logically valid contrapositive is

\[
\boxed{\Phi\le0\Longrightarrow3j-h\ge13}.
\]

This is enough to recover the dyadic gate

\[
\beta^j/U\le2^{-13}
\]

at `Phi=0` directly. No limit from the negative side is needed.

The B2-E analytic certificate recomputes the positive contradiction margin exactly with rational arithmetic.

---

## 3. The source box survives equality without changing a threshold

The lower source bound

\[
Q=s^{j-1}/U>9/1000
\]

comes from strict compressed `b+2`, through `E_(b+1)>0`, and the previously audited A113 majorant. It does not use the sign of `Phi`.

The upper source bound uses only the dyadic gate from the previous section plus the existing A112-A bridge. The exact certificate gives

\[
Q<0.0320622106086\ldots<1/25.
\]

Thus the original C2 source box

\[
\boxed{9/1000<Q<1/25}
\]

is recovered at equality without altering the thresholds after seeing the desired answer.

This matters for the anti-ad-hoc audit: no new local source window or fitted cutoff was introduced for E.

---

## 4. Independent algebra excludes `Phi=0=p0^C`

The exact C reduction gives

\[
A_\beta p_0+K_\beta t=C_\beta
\]

and

\[
S_{\gamma+}^C=C_\gamma-A_\gamma p_0-K_{\gamma+}t.
\]

Eliminating `t` gives

\[
\boxed{
S_{\gamma+}^C
=\frac{B_0-B_1p_0}{K_\beta}}
\]

with

\[
B_0=C_\gamma K_\beta-K_{\gamma+}C_\beta,
\qquad
B_1=A_\gamma K_\beta-K_{\gamma+}A_\beta.
\]

The equality `Phi=0` implies `S_(gamma+)^C=0` by the exact C/G+ bordered pivot and nonzero determinant orientations. The new analytic envelope proves in both parities

\[
K_\beta>0,
\qquad B_0>0,
\qquad B_1>0.
\]

The weakest certified margins are

\[
B_0>2.8144696\times10^{-4},
\qquad
B_1>9.4994463\times10^{-2}.
\]

Therefore

\[
\boxed{p_0^C=B_0/B_1>0}.
\]

More strongly, the uniform certificate gives

\[
\boxed{p_0^C>2.9407595\times10^{-3}}.
\]

Hence `Phi=0` and `p0^C=0` are analytically separated in the frozen tail contract. This is not inferred from a finite scan or from branch continuity.

---

## 5. C2 was not imported across its premise wholesale

This was the most important logical audit after the p0 calculation.

C2 was originally stated with `Phi<0`, so using its conclusion verbatim at equality would be invalid. The C2 proof was therefore split by section.

After the source box and `p0^C>0` are available:

- C2 Section 3 (primal feasibility) contains no `Phi` dependency;
- Section 4 (active duals) contains no `Phi` dependency;
- Section 5 (gamma-minus slack) contains no `Phi` dependency;
- Section 7 (all P reduced costs) contains no `Phi` dependency;
- Section 8 (all Q reduced costs) contains no `Phi` dependency.

The only post-source-box C2 step using `Phi` is Section 6, whose sole purpose is to prove the strict inactive gamma-plus slack

\[
S_{\gamma+}^C>0.
\]

At `Phi=0`, that one step is not reused. It is replaced by the exact bordered-pivot identity, which gives

\[
S_{\gamma+}^C=0.
\]

Thus the equality theorem is not a disguised reversal of C2 and does not smuggle a strict-branch premise into the boundary.

The section-scoped logical audit records this separation explicitly.

---

## 6. A tight inactive inequality does not create an optimal face here

At the proposed boundary, C has:

- every basic primal variable strictly positive;
- both active alpha/beta multipliers strictly positive;
- every nonbasic P/Q reduced cost strictly positive;
- gamma-minus slack strictly positive;
- gamma-plus slack exactly zero.

Fix the C dual optimum. Any alternative primal optimum with zero primal-dual gap must keep every variable with positive reduced cost at zero. Hence it cannot introduce any nonbasic P/Q atom.

The positive alpha/beta multipliers force those equalities to remain saturated. On the fixed C support, normalization, mean, target, alpha and beta give the nonsingular C square system. There is therefore exactly one primal point.

So the tight gamma-plus inequality is a **dual/activity degeneracy**, not a primal zero-cost direction. This is qualitatively different from the `r_E(q0)=0` surface in D, where an actual nonbasic primal variable has zero reduced cost and a one-dimensional optimal face appears.

---

## 7. The C/G+ coalescence is an exact pivot statement

A112-A gives

\[
p_{j+1}^{G+}=\Phi/D_G,
\qquad D_G>0.
\]

Thus `Phi=0` gives exactly

\[
p_{j+1}^{G+}=0.
\]

The upper-boundary barrier gives

\[
F_{b+3}^{up}<0,
\]

so the neighboring gamma-plus mass remains positive:

\[
p_j^{G+}>0.
\]

After deleting the zero `p_(j+1)` coordinate, G+ and C have the same primal support. C is already proved to saturate gamma+, so the remaining G+ coordinates satisfy the C equations. C nonsingularity makes the primal point identical.

The theorem therefore claims C=G+ **as primal points**, not that the optimal basis is unique.

---

## 8. Exact near-boundary falsification controls

An independent `fractions.Fraction` reconstruction brackets a Phi sign change in one even and one odd cell:

\[
M=538:\quad
0.129698549<s_\Phi<0.129698550,
\]

\[
M=555:\quad
0.130085841<s_\Phi<0.130085842.
\]

At the four rational endpoints:

- strict compressed `b+2` holds;
- C passes complete atom-by-atom strict KKT on the `Phi<0` side;
- G+ passes complete atom-by-atom strict KKT on the `Phi>0` side;
- `p0^C>0` on both sides;
- `S_(gamma+)^C` has the exact opposite sign to `Phi`.

The independent crosscheck reports **24/24 PASS**.

No floating-point sign is used in these decisions.

---

## 9. Multi-cell counterexample search

A second exact-rational red-team scan bracketed Phi sign changes in **13 distinct strict-b+2 cells** from `M=521` through `M=1000`. Each bracket was bisected exactly to width at most

\[
3.814697265625\times10^{-10}.
\]

Across all 26 bracket endpoints:

- `b` remained fixed inside each cell;
- strict compressed `b+2` remained true;
- `Phi(left)<0<Phi(right)`;
- `p0^C` remained positive;
- `S_(gamma+)^C(left)>0>S_(gamma+)^C(right)`.

The smallest observed endpoint mass was

\[
p_0^C=0.0031473865\ldots,
\]

comfortably above the analytic uniform bound `0.0029407595...`.

The scan reports **79/79 PASS**.

This finite scan is not used as the theorem proof; it is a counterexample search against the analytic result.

---

## 10. Rounding and implementation risk

All theorem-critical inequalities in the new B2-E certificate use `fractions.Fraction` arithmetic. The displayed decimals are renderings of exact rational bounds.

The near-boundary and multi-cell scans also make all sign decisions using exact rational arithmetic. Floating-point logarithms appear only as initial guesses for `b`; the scripts correct `b` by exact integer-power inequalities before any classification is accepted.

Therefore no theorem sign in E depends on binary floating-point rounding.

---

## 11. What could still invalidate E

E must be reopened if a future from-zero audit invalidates any of these imported ingredients:

1. the A113 strict `b+2` sign structure;
2. the A112-A Cramer identities or upper-boundary barrier;
3. the A114-B1 determinant orientation `D_G>0`;
4. the C2 exact C/G+ bordered-pivot identity;
5. the C2 source-box-dependent primal/dual/ECT gates reused in Sections 3--5 and 7--8.

This red-team audit does not shield those dependencies from future falsification.

---

## Final assessment

Within the stated mathematical contract, the evidence supports

\[
\boxed{
\Phi=0
\Longrightarrow
\text{unique primal optimum with degenerate C/G+ coalescence}.}
\]

The result did not require a fitted threshold, a continuity shortcut, a finite-census promotion, or a reinterpretation of a failed case. The decisive new step is the exact positive separation of `p0^C` on the zero-pivot surface.

**Verdict: PASS WITH SCOPE.**
