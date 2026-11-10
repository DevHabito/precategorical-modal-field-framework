# Uniform geometric suppression of the complete finite-power tail in A115

**Date:** 2026-11-10. **Mathematical object:** the reduced two-active-band C2(k) cofactor, not a global F2/F3 optimizer.

**Status:** analytic proof with independent exact rational checks for all constant comparisons. The exact polynomial decomposition is separately submitted in Lean; the *inequality in this note has not been kernel-checked*.

## Quantifiers

Fix beta=1/8, delta=1/1875, 129/1000<=s<=133/1000, 8<=alpha<=45, integer M>=1000, parity sigma in {0,1/2}, integer deficit 4<=r<=19, h=floor(M/2), k=h-r+1 and tau=s(1+2alpha/M). Set x=1/M, q=k/M, u=tau^h, rho=99/100, and let vb=beta^M, vs=s^M, vt=tau^M. Let E_full be the original A115 cofactor (including these full-length powers) and E_aux the same cofactor with those *three powers alone* set to zero. The original central responses H_beta,H_s are **not** truncated: each is written exactly as 1/2+uU and 1/2+uV.

Write J_full=E_full(k)-tau^(-1)E_full(k+1) and J_aux analogously. The exact identity independently checked with SymPy is

\[
2\tau(J_{\mathrm{full}}-J_{\mathrm{aux}})
=C_0+u C_1+u^2 C_2,
\]

with C0=x*(tau-1)*vt*(vs-vb); the full C1 and C2 are in [A115FinitePowerDecomposition.lean](../../formal/lean/PrecategoryFormal/A115FinitePowerDecomposition.lean).

## Uniform elementary bounds

Here 0<beta<s<tau<=3/20, tau>=129/1000, 0<x<=1/1000, 0<q<1 and 0<u<1. Since M>=2h and beta,s<=tau,

\[
0\le vb,vs,vt\le u^2.
\]

The central determinant satisfies L_h(tau)>=(7/10)*tau>0, by the geometric monotonic argument documented in [A115_A118_EXPLICIT_GEOMETRIC_Q_RESPONSE_20261110.md](A115_A118_EXPLICIT_GEOMETRIC_Q_RESPONSE_20261110.md). Also 0<L_h(a)<=a for a in {beta,s}. Hence C_a=L_h(a)/L_h(tau)<=10/7 and the exact response formulas give

\[
|U|,|V|\le 10/7+2/1875+1+1/2<3.
\]

Put H=8^18. The exact contact ratios obey

\[
K=\beta^{1-r}(\beta/\tau)^h\le H,\quad
W=s^{1-r}(s/\tau)^h\le H,\quad
1\le T=\tau^{1-r}\le H.
\]

Here 4<=r<=19 and beta<s<tau<1; no M-dependent upper-bound is hidden in H.

Define P_a=q(a-1)(a-tau)+x(a^2-2a+tau), Q_a=(a-1)(a-tau). For a in {beta,s}, the established range yields |P_a|<=1+4/1000<2, |Q_a|<=1. Now bound **each exact polynomial** by the triangle inequality, keeping all mixed finite-power terms:

\[
|C_0|\le2xu^4,
\]
\[
|C_1|\le u^2(18H+2xH+24x)<19Hu^2,
\]
\[
|C_2|\le u^2(H^2+(24+12x)H)<26H^2u^2.
\]

For C1 the terms vb and vs each cost at most u^2[x(H+6)+2H], the vt term at most u^2(10H+12x), and the two mixed products vb*vt and vs*vt together at most 4H u^4. For C2 the terms proportional to vs*U-vb*V cost at most 12Hxu^2; the vt group costs at most (H^2+24H)u^2. Thus no higher-order power product has been silently omitted.

Since tau^k=uT, the normalized original correction is bounded by

\[
\frac{|J_{\mathrm{full}}-J_{\mathrm{aux}}|}{u\tau^k}
\le\frac{2xu^2+19Hu+26H^2u^2}{2\tau T}
\le 4(2xu^2+19Hu+26H^2u^2).
\]

Because tau<=3/20<(99/100)^2, and 2h=M or M-1,

\[
u=\tau^h\le\frac{100}{99}\rho^M.
\]

Use u^2<=u and x<=1/1000. Exact rational arithmetic verifies

\[
4\frac{100}{99}\left(2/1000+19H+26H^2\right)<200H^2.
\]

Consequently, for **every** permitted integer M and all source/alpha/parity/deficit choices,

\[
\boxed{
\frac{|J_{\mathrm{full}}-J_{\mathrm{aux}}|}{u\tau^k}
<200(8^{18})^2(99/100)^M.
}
\]

The constant is intentionally huge. This proves **uniform geometric suppression of the full-length-power correction only**, not an informative sign threshold near M=1000. The elementary comparisons in the proof are independently checked in [a115_finite_power_geometric_bound_gates_20261110.py](../../audits/a115_finite_power_geometric_bound_gates_20261110.py).

## What is still open

1. The polynomial identity is already checked independently by SymPy; its Lean kernel replay must be confirmed separately.
2. The above **inequality** and the central-response bounds have not yet been formalized in Lean.
3. The auxiliary cofactor still contains the K and u-cubic corrections, plus U-U0 and V-V0. The source-to-A117/A118 Taylor coefficients and their uniform cubic error must be connected to a normalized exact cofactor with explicit sign conventions.
4. No global F2/F3 primal/dual optimality, historical novelty, or physical result follows from this reduced-family error bound.

**Engineering rule:** neither a successful finite Fraction regression nor this proof note substitutes for the final fully quantified Lean O(M^-3) theorem.
