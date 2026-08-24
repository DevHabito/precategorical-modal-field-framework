# A107-A109 exact equations and classifier

This document collects the equations actually used by the gamma-plus continuum audits. It does not add a physical interpretation.

## 1. Declared gamma-plus architecture

For integer maximum `M`, let

\[
h=\left\lfloor\frac{M}{2}\right\rfloor,
\qquad
\bar m=\frac{M}{2},
\qquad
P=\{0,j,j+1,M\},
\qquad
Q=\{1,h,h+1\}.
\]

The fixed dyadic functions used by the finite LP are

\[
t(x)=2^{-x},\qquad
b(x)=2^{-3x},\qquad
g(x)=2^{-4x}.
\]

The normalized tolerance used by A103 and inherited here is

\[
\varepsilon(M)=
\begin{cases}
\displaystyle \frac{1}{1875\,2^h}, & M\ \text{even},\\[6pt]
\displaystyle \frac{1}{2500\,2^h}, & M\ \text{odd}.
\end{cases}
\]

The reference source probe for the rank-one reconstruction is

\[
s_{\mathrm{ref}}=\frac18.
\]

## 2. Exact basis matrix

With columns ordered as the four `P` basic masses, the three `Q` basic masses, and `t`, the gamma-plus basis matrix at source probe `s` is

\[
A(s)=
\begin{pmatrix}
1&1&1&1&0&0&0&-1\\
0&0&0&0&1&1&1&-1\\
0&j&j+1&M&0&0&0&-\bar m\\
0&0&0&0&1&h&h+1&-\bar m\\
0&0&0&0&t(1)&t(h)&t(h+1)&0\\
1&s^j&s^{j+1}&s^M&-s&-s^h&-s^{h+1}&-2\varepsilon\\
-b(0)&-b(j)&-b(j+1)&-b(M)&b(1)&b(h)&b(h+1)&-2\varepsilon\\
g(0)&g(j)&g(j+1)&g(M)&-g(1)&-g(h)&-g(h+1)&-2\varepsilon
\end{pmatrix}.
\]

The right-hand side and objective vectors are

\[
r=(0,0,0,0,1,0,0,0)^\top,
\]

\[
c=(t(0),t(j),t(j+1),t(M),0,0,0,0)^\top.
\]

At the reference probe,

\[
b_0=A(s_{\mathrm{ref}})^{-1}r,
\qquad
\lambda_0=A(s_{\mathrm{ref}})^{-\top}c.
\]

## 3. Rank-one source update

Only the alpha row varies with `s`. Let `u=A(s_ref)^{-1}e_6` be the basis-update direction associated with that row, and let `\Delta a(s)` be the exact row change from `s_ref` to `s`. The common denominator is

\[
D(s)=1+\Delta a(s)^\top u.
\]

Let

\[
\eta(s)=\Delta a(s)^\top b_0.
\]

Then every basic variable has the exact rational form

\[
p_k(s)=\frac{N_k(s)}{D(s)},
\]

with numerator

\[
N_k(s)=D(s)b_{0,k}-u_k\eta(s).
\]

The audits orient the integerized polynomials so that `D(s_0)>0` at the frozen witness.

## 4. Dual numerators and reduced costs

If

\[
\rho=c^\top u,
\]

and `v_r(s)` denotes the exact row-update polynomial for row `r`, then the dual numerator for basis column `q` is

\[
L_q(s)=D(s)\lambda_{0,q}-\rho\sum_r v_r(s)\,[A(s_{\mathrm{ref}})^{-1}]_{rq}.
\]

For a nonbasic `P` index `x`, the denominator-cleared reduced-cost numerator is

\[
R^P_x(s)=L_0+xL_2+s^xL_5-b(x)L_6+g(x)L_7-t(x)D(s).
\]

For a nonbasic `Q` index `x`,

\[
R^Q_x(s)=L_1+xL_3+t(x)L_4-s^xL_5+b(x)L_6-g(x)L_7.
\]

The active dual numerators are

\[
L_5(s),\qquad L_6(s),\qquad L_7(s),
\]

corresponding to active `alpha+`, `beta-`, and `gamma+`.

## 5. Inactive slack numerators

Let `N_t(s)` be the basic-`t` numerator and define the denominator-cleared channel differences

\[
\Delta_\alpha(s)=\sum_{x\in P}s^xN^P_x(s)-\sum_{x\in Q}s^xN^Q_x(s),
\]

\[
\Delta_\beta(s)=\sum_{x\in P}b(x)N^P_x(s)-\sum_{x\in Q}b(x)N^Q_x(s),
\]

\[
\Delta_\gamma(s)=\sum_{x\in P}g(x)N^P_x(s)-\sum_{x\in Q}g(x)N^Q_x(s).
\]

The inactive-slack numerators are

\[
S_{\alpha-}(s)=2\varepsilon N_t(s)+\Delta_\alpha(s),
\]

\[
S_{\beta+}(s)=2\varepsilon N_t(s)-\Delta_\beta(s),
\]

\[
S_{\gamma-}(s)=2\varepsilon N_t(s)+\Delta_\gamma(s).
\]

## 6. Current two-sided adjacent-boundary classifier

Let `[L,R]` be the frozen source segment and `s_0` its frozen witness. The classifier is applicable only when

\[
D(s)>0\quad\forall s\in[L,R],
\]

\[
N'_{j+1}(s)>0\quad\forall s\in[L,R],
\qquad
N'_j(s)<0\quad\forall s\in[L,R],
\]

\[
N_{j+1}(s_0)>0,
\qquad
N_j(s_0)>0,
\]

and the relevant endpoint signs are nonzero.

The frozen classification rule is

\[
\mathcal C=
\begin{cases}
\text{full\_segment\_coverage},
&N_{j+1}(L)>0\ \land\ N_j(R)>0,\\[5pt]
\text{proper\_strict\_subcomponent},
&N_{j+1}(L)<0\ \land\ N_j(R)>0,\\[5pt]
\text{proper\_strict\_subcomponent},
&N_{j+1}(L)>0\ \land\ N_j(R)<0,\\[5pt]
\text{proper\_strict\_subcomponent},
&N_{j+1}(L)<0\ \land\ N_j(R)<0.
\end{cases}
\]

Boundary identities are

\[
N_{j+1}(s_L^*)=0
\iff
p_{j+1}(s_L^*)=0
\qquad\text{(left boundary)},
\]

\[
N_j(s_R^*)=0
\iff
p_j(s_R^*)=0
\qquad\text{(right boundary)}.
\]

In compact form,

\[
\boxed{p_{j+1}=0\ \Longrightarrow\ \text{left adjacent boundary}},
\qquad
\boxed{p_j=0\ \Longrightarrow\ \text{right adjacent boundary}}.
\]

The fourth branch, with both endpoint target signs negative, is a logically declared two-sided possibility. No two-sided case has been observed in the mathematically resolved prospective sequence through rank 414.

## 7. Exact certification requirement

The classifier by itself is a prediction rule, not a proof that no other KKT condition wins. A resolved record additionally requires exact positivity/certification of all nonselected conditions on the claimed strict component (or the complete source segment for a full case), exact isolation and derivative-sign certification for any selected root, and independent direct rational matrix regression with zero discrepancy.
