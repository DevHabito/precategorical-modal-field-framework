# A114-B2-C1 — endpoint-released branch on the strict `b+2`, negative-pivot tail

## Status

**PROVED conditional branch theorem under the frozen analytic-tail contract.**

Let

\[
M\ge521,\qquad 129/1000\le s\le133/1000,
\qquad h=\lfloor M/2\rfloor,
\]

\[
b=\lceil M\log2/(-2\log s)\rceil,
\qquad j=b+2,
\]

assume `j=b+2` is the strict compressed maximizer, and define

\[
\Phi=F_j^{\rm up}.
\]

Assume \(\Phi<0\). Let

\[
C:\quad P=\{0,j,M\},\ Q=\{1,h,h+1\},
\]

and

\[
E:\quad P=\{j-1,j,M\},\ Q=\{1,h,h+1\},
\]

with `alpha+`, `beta-` active and gamma inactive.

## Theorem

If

\[
\boxed{p_0^C<0,\qquad r_E(q_0)>0},
\]

then the endpoint-released basis `E` satisfies the complete strict KKT system. Hence it is the unique strict global basic optimum of the declared finite lifted LP.

Equivalently,

\[
\boxed{
\text{strict }b+2,\ \Phi<0,\ p_0^C<0,\ r_E(q_0)>0
\Longrightarrow E.}
\]

## Proof dependencies

### 1. B2-specific source box

The standalone exact certificate proves

\[
\boxed{9/1000<s^{b+1}/2^{-h}<1/25}.
\]

The lower inequality follows because strict `b+2` gives \(E_{b+1}>0\), whereas the exact A113 ten-term majorant gives \(E_{b+1}<0\) under the contrary assumption \(s^{b+1}/2^{-h}\le9/1000\). The certified normalized upper bound is approximately

\[
-5.71066\times10^{-5}.
\]

For the upper inequality, A114-B2-B already proves

\[
\Phi<0\Rightarrow3j-h\ge13,
\]

and the audited A112-A V2 bridge yields

\[
s^{j-1}/2^{-h}<0.03206221\ldots<1/25.
\]

### 2. Exact `C -> E` exchange

The symbolic endpoint system gives the exact numerator identity linking \(p_{j-1}^E\) to \(p_0^C\), with opposite denominator orientation. Therefore

\[
\boxed{\operatorname{sgn}p_{j-1}^E=-\operatorname{sgn}p_0^C}.
\]

Thus the branch hypothesis \(p_0^C<0\) gives \(p_{j-1}^E>0\). The protected endpoint certificate also gives \(p_j^E>0\), \(t>0\), the remaining P/Q basic masses, both active multipliers and both inactive gamma slacks.

### 3. All P reduced costs

Strict compressed maximality gives

\[
V_j-V_{j-1}=E_{j-1}>0.
\]

Together with the exact compressed straddling identity, the simplex exchange formula gives

\[
\boxed{r_E(p_0)>0}.
\]

The protected P checkpoints plus the five-dimensional extended-Chebyshev zero bound then imply

\[
\boxed{r_E(p_x)>0\quad\forall x\notin P_E}.
\]

### 4. All Q reduced costs

The protected certificate gives \(r_E(q_2)>0\), while the branch hypothesis gives \(r_E(q_0)>0\). The Q reduced-cost function has basic roots at \(1,h,h+1\). The same extended-Chebyshev zero-count argument therefore yields

\[
\boxed{r_E(q_x)>0\quad\forall x\notin Q_E}.
\]

Hence every strict primal, dual, reduced-cost and inactive-slack gate is positive.

## Executable audit

The analytic endpoint certificate reports **121/121 protected gates PASS**. A separate `fractions.Fraction` implementation rebuilds the original LP and checks:

- positive controls: `(522,263/2000)`, `(999,129/1000)`, `(1000,261/2000)` — all complete `2M+9` KKT passes;
- C hostile control `(538,53/400)` — E fails only through the exchanged lower P mass;
- QI/QA hostile controls `(555,13/100)` and `(521,129/1000)` — E fails only through `r_E(q0)<0`.

The finite controls are regression checks, not premises of the all-tail proof.

## Claim boundary

C1 does **not** prove:

- `p0^C>0 => C`;
- the QI/QA partition when `p0^C<0` and `r_E(q0)<0`;
- strictness or uniqueness on `p0^C=0`, `r_E(q0)=0`, or `Phi=0`;
- anything outside the frozen tail/source window;
- any physical interpretation.
