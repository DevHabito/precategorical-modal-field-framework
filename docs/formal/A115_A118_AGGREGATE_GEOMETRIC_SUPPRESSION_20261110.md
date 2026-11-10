# Uniform geometric suppression from the *full* A115 cofactor to the dominant collision core

**Date:** 2026-11-10. **Scope:** reduced C2(k) adjacent comparison; not unrestricted F2/F3 optimality.
**Evidence:** analytically derived estimates with the exact rational comparisons in [a115_finite_power_geometric_bound_gates_20261110.py](../../audits/a115_finite_power_geometric_bound_gates_20261110.py). The required polynomial identities are kernel-proved in Lean; **this aggregate inequality is not yet itself a Lean theorem**.

## Proposition and domain

Let beta=1/8, delta=1/1875, 129/1000<=s<=133/1000, 8<=alpha<=45, M>=1000, sigma=0 or 1/2 according to the parity of M, 4<=r<=19, h=floor(M/2), k=h-r+1, tau=s(1+2alpha/M), u=tau^h, x=1/M and q=k/M. Let U,V be the *exact* A115 central response coefficients and U0,V0 the previously defined approximations retaining (s/tau)^h. Set H=8^18 and rho=99/100.

Define the dominant collision core function

\[
\mathcal J(U,V)=
\frac{(1-s)(\tau-s)}2 W+
x(1-\tau)(U-V)+
U\frac W{\tau T}
\big[(s-\tau)(s-1)(q-1)+x(s^2-2s+\tau)\big],
\]

with W=s^k/u, T=tau^k/u, K=beta^k/u. Let J_full be the **original finite-M** adjacent cofactor E_k-tau^(-1)E_(k+1), including beta^M,s^M,tau^M in its source coefficients.

Then, under precisely these hypotheses,

\[
\boxed{
\left|\frac{J_{\mathrm{full}}}{u\tau^k}
-\mathcal J(U_0,V_0)\right|
<750(8^{18})^2(99/100)^M.
}
\]

The statement holds uniformly over the displayed compact source/alpha and finite parity/r domains. The coefficient is intentionally enormous: do **not** interpret it as a useful finite-M sign bound near M=1000.

## Exact starting identity

The individually successful Lean modules [A115CofactorReducedCore.lean](../../formal/lean/PrecategoryFormal/A115CofactorReducedCore.lean) and [A115FinitePowerDecomposition.lean](../../formal/lean/PrecategoryFormal/A115FinitePowerDecomposition.lean) establish the algebraic identities

\[
2\tau J_{\mathrm{aux}}=u^2\mathcal C+
u^2K\mathcal R_K+u^3\mathcal R_u,
\]

\[
2\tau(J_{\mathrm{full}}-J_{\mathrm{aux}})
=C_0+uC_1+u^2C_2,
\]

where \(\mathcal C=2\tau T\mathcal J(U,V)\). After division by \(2\tau u^2T\), all source terms remain visible and no finite power was silently set to zero.

## Four independently bounded differences

Throughout the domain, x<=1/1000, 0<q<1, 129/1000<=tau<=3/20, 0<u<=1, 1<=T<=H, 0<=K,W<=H, and |U|,|V|<3. From the exact A115 central equations and the positive L_h(tau) denominator,

\[
|U-U_0|<30\rho^M,\qquad |V-V_0|<29\rho^M,
\]
\[
u\le\frac{100}{99}\rho^M,\qquad
K\le H\frac{100}{99}\rho^M.
\]

These central-response inequalities, including all assumptions, were derived separately in [A115_A118_EXPLICIT_GEOMETRIC_Q_RESPONSE_20261110.md](A115_A118_EXPLICIT_GEOMETRIC_Q_RESPONSE_20261110.md).

**1. Beta contact channel.** For the exact polynomial \(\mathcal R_K=\texttt{betaRemainderTau}\),

\[
|\mathcal R_K|
\le \tau T+2|V|(1+4x)+W
<2H+7\le9H.
\]

Since \(1/(2\tau T)<4\),

\[
\left|\frac{K\mathcal R_K}{2\tau T}\right|
<36HK<40H^2\rho^M.
\]

**2. Cubic-u channel.** The exact expression \(\mathcal R_u=\texttt{cubicRemainderTau}\) has the factor \(2\tau T\). Consequently

\[
\left|\frac{u\mathcal R_u}{2\tau T}\right|
\le u\,3(K+W)\le6Hu<7H^2\rho^M.
\]

**3. Central-response replacement.** Let \(G=(s-\tau)(s-1)(q-1)+x(s^2-2s+\tau)\); then |G|<2 and W/(tau*T)<8H. By the exact linear dependence of the core on U,V,

\[
|\mathcal J(U,V)-\mathcal J(U_0,V_0)|
\le x(|U-U_0|+|V-V_0|)
+16H|U-U_0|
<(59/1000+480H)\rho^M
<481H^2\rho^M.
\]

**4. Full-length-power correction.** The exact C0,C1,C2 identity plus the interval estimates already derived in [A115_FINITE_POWER_UNIFORM_GEOMETRIC_BOUND_20261110.md](A115_FINITE_POWER_UNIFORM_GEOMETRIC_BOUND_20261110.md) yield

\[
\frac{|J_{\mathrm{full}}-J_{\mathrm{aux}}|}{u\tau^k}
<200H^2\rho^M.
\]

Summing all four independently obtained bounds gives

\[
(40+7+481+200)H^2\rho^M
=728H^2\rho^M
<750H^2\rho^M,
\]

proving the proposition with a spare exact rational margin. The [constant audit program](../../audits/a115_finite_power_geometric_bound_gates_20261110.py) verifies every decisive numerical comparison without floating point.

## Crucial remaining obligation

The whole normalized **finite-M** cofactor has now been reduced analytically to the single explicit smooth collision core \(\mathcal J(U_0,V_0)\) plus a uniform geometric error. But obtaining the desired

\[
|J_{\mathrm{full}}/(u\tau^k)-\Lambda_p/M-\Xi_p/M^2|\le C/M^3
\]

requires an **independent source-derived** Taylor expansion of \(\mathcal J(U_0,V_0)\) with uniform third-order error, across both f_h=(s/tau)^h and f_k=(s/tau)^k. Here f_k has exponent shift sigma+r-1 up to 18.5; one must **not reuse** a Taylor bound proved only for sigma<=1/2. The published A117/A118 coefficient identities must also be formally connected to that Taylor expansion. No end-to-end Lean theorem or numerical M threshold is claimed.

Other separate gates: high-deficit exclusion, C2 candidate feasibility, full F2/F3 primal-dual optimality, full-text originality and physical relevance.
