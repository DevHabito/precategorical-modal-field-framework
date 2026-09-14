# A114-C2 — independent red-team audit of the `b+2 / b+3` compressed tie

**Date:** 2026-09-14  
**Target:** `A114C2_BPLUS2_BPLUS3_COMPRESSED_TIE_THEOREM_20260914.md`  
**Posture:** adversarial. The audit attempts to falsify the second-tie theorem by attacking the compressed-tie localization, the new `Phi>0` proof, the remainder bounds, the equality-set dual signs, the scoped reuse of A114-A, and the claimed one-dimensional optimal face.

## Verdict

**PASS WITH SCOPE, after two corrections/hardenings discovered during adversarial review.**

No counterexample to the final theorem was found inside

\[
M\ge521,\qquad 129/1000\le s\le133/1000,
\qquad E_{b+2}=0.
\]

Two tempting or insufficient intermediate routes were rejected before this verdict:

1. the proposed dyadic shortcut `3(b+2)-h>=13 => E_(b+2)<0` is false and has exact rational counterexamples;
2. an early tail certificate checked the maximum individual remainder source, whereas a primitive can contain several remainder sources. The certificate was hardened to bound their **sum**.

Neither correction changes the theorem conclusion. Both are preserved explicitly.

---

## 1. Compressed-tie attack

A possible failure would be a triple tie involving `b+1`, `b+2`, and `b+3`.

A113 gives

\[
E_{b+1}-2E_{b+2}>0.
\]

At `E_(b+2)=0`, this gives

\[
E_{b+1}>0.
\]

A113 also gives `E_k<0` for every `k>=b+3`. Thus the only compressed maximizers are exactly `b+2` and `b+3`.

No finite census is used for this conclusion.

---

## 2. False dyadic route attack

The first attempted shortcut was

\[
3(b+2)-h\ge13\stackrel{?}{\Longrightarrow}E_{b+2}<0.
\]

It is false.

Exact rational counterexamples at `s=129/1000` include:

- `M=821`, `b=139`, `j=141`, `3j-h=13`, but `E_j>0`;
- `M=886`, `b=150`, `j=152`, `3j-h=13`, but `E_j>0`;
- `M=951`, `b=161`, `j=163`, `3j-h=14`, but `E_j>0`.

Therefore the final proof does not infer `Phi>0` from a dyadic offset threshold. The rejected route is preserved in `A114C2_CORRECTIONS_AND_DEAD_ENDS_20260914.md`.

---

## 3. Source-ratio attack

The replacement variable is

\[
R=\frac{s^{b+2}}U.
\]

A114-A already proved the strict implication

\[
R\le9/1000\Longrightarrow E_{b+2}<0.
\]

Hence the equality `E_(b+2)=0` gives directly

\[
R>9/1000.
\]

This is a contrapositive of a strict analytic bound, not continuity from the strict `b+3` phase.

The upper bound also follows without a compressed-sign assumption. Since `b=ceil(Mc(s))`,

\[
s^b\le s^{Mc(s)}=2^{-M/2}\le U,
\]

so

\[
R\le s^2\le(133/1000)^2<0.018.
\]

---

## 4. Exact `Phi`-core identity attack

The new certificate rebuilds the A81 upper-gamma boundary in normalized variables. With

\[
Y=\frac{\beta^j}{U},\qquad
 a=1-j/M,\qquad
 e=\varepsilon/U,\qquad
 d=1-(h+1)U,
\]

SymPy exact algebra verifies identically that the common-denominator core is

\[
\frac{\Phi_0}{U}
=
\frac{1}{d}
\left[
R(\beta-\gamma)-Y(s-\gamma)-8ae(s-\gamma)
-4UeR(\beta+\gamma)+4UeY(s-\gamma)
\right].
\]

The parity-dependent central-Q coefficient cancels algebraically. It is not replaced by a numerical approximation.

Because `j>=91`,

\[
Y=R(\beta/s)^j
\le R(125/129)^{91}.
\]

The resulting conservative core margin is

\[
\Phi_0/U>2.25594\times10^{-4}.
\]

---

## 5. Remainder-bound attack

This was the most delicate point in the new proof.

The omitted primitive contributions come from:

- `gamma^j`;
- the `r^M` tails;
- the central-Q high-node terms `r^h,r^(h+1)`.

The first certificate version verified only the largest individual source. Red-teaming identified that a single primitive can contain a **sum** of such sources. The certificate was therefore hardened before this verdict.

At the worst tail endpoint it now proves

\[
\eta_\gamma+\eta_{\rm central}+\eta_M
<4.066\times10^{-31}<10^{-28}.
\]

It also checks that the central-tail sequence decreases after `h=260`:

\[
\frac{h+2}{h+1}(2s_{\max})
\le0.2670191571<1,
\]

and separately verifies that every exact/core primitive entering the product telescoping has absolute value below `2`.

The six expanded triple products therefore have aggregate normalized perturbation below the declared `1e-26` envelope.

The final analytic margin remains

\[
\boxed{\Phi/U>2.25594\times10^{-4}>0}.
\]

The hardened analytic certificate passes **15/15** gates.

### Independent transcription crosscheck

A separate exact-`Fraction` reconstruction of both the complete A81 upper boundary and the simplified core was run on 171 rational tail controls. The contact index `b` is found by exact rational binary search, not logarithms.

All 171 cases fall below the `1e-26` error envelope. The worst normalized discrepancy is approximately

\[
2.95823\times10^{-34}
\]

at `M=521, s=131/1000`.

This crosscheck is finite regression only. The uniform theorem sign comes from the analytic bound above.

---

## 6. Gamma-plus equality KKT attack

The analytic `Phi>0` result gives both adjacent `G2+` P masses positive. A112-B/C/E/G and the pointwise Descartes argument then protect all basic masses and every nonbasic P/Q reduced cost without using a sign of `E_j`.

A112-D gives exactly

\[
N_\gamma=-\frac{\det B}{D_G}E_j,
\]

so the tie gives

\[
y_\gamma=0.
\]

The alpha/beta signs are not imported by continuity. The independent A114-C1 symbolic Wronskian certificate gives the generalized-Vandermonde orientation needed for

\[
y_\alpha>0,\qquad y_\beta>0.
\]

Thus the only lost strict dual gate at `G2+` is the gamma multiplier.

---

## 7. Hidden-optimal-direction attack

A zero multiplier can create a larger optimal set than a single edge.

Fix the `G2+` dual at the tie. Every nonbasic P/Q reduced cost is strictly positive, so any other primal optimum must use only columns already in the `G2+` support.

Because `y_alpha,y_beta>0`, alpha+ and beta- remain saturated at every optimum. Gamma+ can release because `y_gamma=0`.

Dropping that row from the nonsingular eight-by-eight `G2+` basis leaves seven independent equalities on eight support variables. Therefore the candidate optimal set has affine dimension exactly at most one; there is no hidden second zero-cost direction.

---

## 8. Scoped A114-A reuse attack

A dangerous shortcut would be to import the strict `b+3` theorem wholesale onto the tie. The final proof does not do this.

The promoted A114-A dependency audit separates:

\[
E_{b+2}>0\to R>0.009
\]

from the downstream endpoint primal/gamma-slack estimates. The strict compressed sign is additionally used in the simplex exchange that makes `r_{ER3}(p0)>0`.

At the present tie:

- `R>0.009` has been independently re-established from equality;
- the endpoint primal and inactive-gamma estimates therefore remain strict;
- **the endpoint `p0` reduced cost is not imported as strict**.

Hence `ER3` retains positive masses and both gamma slacks, but the equality theorem does not smuggle in the strict `b+3` reduced-cost conclusion.

---

## 9. Exact face-endpoint attack

`ER3` uses a subset of the `G2+` columns and lies on the same alpha+/beta- line with `p0=0`. Since the `G2+` dual has `y_gamma=0`, all `ER3` columns have zero reduced cost under that dual, and the primal point satisfies the required active equalities. Thus its primal-dual gap is zero.

The whole segment

\[
\operatorname{conv}\{G2+,ER3\}
\]

is feasible: all coordinates and slacks are affine and nonnegative at both endpoints.

There are two exact endpoint barriers:

- beyond `ER3`, `p0<0`;
- through `G2+` in the direction opposite `ER3`, gamma-plus slack becomes negative because it is zero at `G2+` and strictly positive at `ER3`.

Combined with the one-dimensionality result, this excludes extension or an additional branch of optima.

---

## 10. Exact near-tie regression attack

The standalone exact-`Fraction` regression brackets `E_(b+2)=0` in two deliberately different cells:

- odd `M=525`, dyadic offset `d=11`;
- even `M=760`, dyadic offset `d=13`.

On the `E_(b+2)<0` side, `G2+` passes the full unused-atom KKT scan. On the `E_(b+2)>0` side, `ER3` passes the full scan. `Phi` is positive at all four rational bracket endpoints.

The regression reports **12/12 PASS**. It is not a proof premise.

---

## 11. Logical-composition audit

After the remainder hardening, the logical audit requires:

- the 15/15 `Phi` certificate;
- explicit tail monotonicity;
- explicit **summed** primitive-error bound;
- explicit primitive magnitude bound;
- scoped A114-A reuse;
- the exact face barriers;
- the 12/12 regression;
- no physical/ontological claim.

It reports **36/36 PASS**.

---

# Verdict and reopen conditions

**PASS WITH SCOPE.** No surviving counterexample or circular dependency was found after the false dyadic route and the max-versus-sum remainder issue were corrected.

A114-C2 must be reopened if any of the following upstream inputs is retracted:

1. A113 central nesting or remote-right signs;
2. the A114-A strict implication `R<=0.009 => E_(b+2)<0`;
3. A114-B1 determinant orientation;
4. A112 reduced-cost/primal closure under adjacent positivity;
5. the C1 generalized-Vandermonde equality-dual orientation;
6. the A114-A endpoint primal/gamma-slack bounds downstream of `R>0.009`.

The theorem is only a classification of the declared finite lifted LP under the frozen analytic-tail contract. It makes no physical or ontological claim.