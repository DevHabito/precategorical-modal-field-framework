# A114-B2-C2 — compressed branch on the strict `b+2`, negative-pivot tail

## Status

**PROVED conditional branch theorem under the frozen analytic-tail contract.**

Let

\[
M\ge521,\qquad 129/1000\le s\le133/1000,\qquad h=\lfloor M/2\rfloor,
\]
\[
b=\left\lceil M\log2/(-2\log s)\right\rceil,\qquad j=b+2,
\]

assume `j=b+2` is the strict compressed maximizer, and define

\[
\Phi=F_j^{\rm up}.
\]

Assume `Phi<0`. Let

\[
C:\quad P_C=\{0,j,M\},\qquad Q_C=\{1,h,h+1\},
\]

with `alpha+`, `beta-` active and gamma inactive.

## Theorem

If

\[
\boxed{p_0^C>0},
\]

then `C` satisfies the complete strict KKT system of the declared finite lifted LP. Hence `C` is the unique strict global basic optimum.

Equivalently,

\[
\boxed{\text{strict }b+2,\ \Phi<0,\ p_0^C>0\Longrightarrow C.}
\]

The sets `Phi=0` and `p0^C=0` are excluded.

## 1. Inherited source box

C1 proves

\[
\frac9{1000}<Q:=\frac{s^{j-1}}{U}<\frac1{25},\qquad U=2^{-h}.
\]

B2-B gives `3j-h>=13`, hence `beta^j/U<=2^-13`. The certified enclosure `0.16923<c(s)<0.17180`, together with `M>=521` and `j=b+2`, yields

\[
\boxed{h-j\ge168},\qquad \boxed{j/M<0.178},
\]

and `k/M<0.18` for `k=j-1,j,j+1`.

## 2. Exact two-variable reduction

Set

\[
\lambda=\frac{M}{M-j}.
\]

From normalization and the mean,

\[
p_j=\lambda\left(\frac t2-p_0\right),
\]
\[
p_M=\left(1-\frac\lambda2\right)t+(\lambda-1)p_0.
\]

For any transform base `r`,

\[
P_r=A_rp_0+T_rt,
\]

where

\[
A_r=1-\lambda r^j+(\lambda-1)r^M,
\]
\[
T_r=\frac\lambda2r^j+\left(1-\frac\lambda2\right)r^M.
\]

A81 gives `Q_r=C_r+D_rt`. Therefore the active source and beta equations are

\[
A_s p_0+K_st=C_s,\qquad A_\beta p_0+K_\beta t=C_\beta,
\]

with

\[
K_s=T_s-D_s-2\varepsilon,\qquad K_\beta=T_\beta-D_\beta+2\varepsilon.
\]

The exact C2 certificate proves `0.999<A_r<1.001` and the following normalized bounds.

Even `M`:

\[
0.2569333<K_s/U<0.2692343,
\]
\[
0.2510666<K_\beta/U<0.2511409.
\]

Odd `M`:

\[
0.1927<K_s/U<0.2027343,
\]
\[
0.1883<K_\beta/U<0.1883743.
\]

Hence, for

\[
D_C=A_sK_\beta-A_\beta K_s,
\]

one has uniformly

\[
\boxed{D_C<0},
\]

with certified margins

\[
-D_C/U>0.005284380330246409\ldots\quad(M\text{ even}),
\]
\[
-D_C/U>0.003944713663579742\ldots\quad(M\text{ odd}).
\]

## 3. Complete primal feasibility from `p0^C>0`

Put `x=Ut`. The beta equation and `p0^C>0` give

\[
x<0.9957514604354754\ldots<1\quad(M\text{ even}),
\]
\[
x<1.3276686139139671\ldots<4/3\quad(M\text{ odd}).
\]

Combining the alpha equation with the beta upper bound on `p0` gives

\[
x>0.0278549215331910\ldots\quad(M\text{ even}),
\]
\[
x>0.0369917698351910\ldots\quad(M\text{ odd}).
\]

Thus `Ut>1/100`. Since `h>=260`, `t` is exponentially larger than every polynomial-in-`h` term in the Q block. The beta equation gives an `O(1)` upper bound on `p0`, hence `t/2>p0` and therefore `p_j>0`. Also `1-lambda/2>0.39`, so `p_M>0`.

The exact A81 Q formulas are

\[
q_1=\frac{2(1-Ut)}{1-(h+1)U}\quad(M\text{ even}),
\]

and

\[
q_1=\frac{2-\frac32Ut}{1-(h+1)U}\quad(M\text{ odd}),
\]

so `q1>0`. The lower bound on `Ut` gives `q_h>0`, and then the exact Q identities give `q_(h+1)>0`. Therefore all basic masses and `t` are strictly positive.

## 4. Active duals

The reduced target objective is `A_tau p0+T_tau t`. Solving the dual two-by-two system gives

\[
y_\alpha=\frac{A_\tau K_\beta-A_\beta T_\tau}{D_C},
\]
\[
y_\beta=\frac{A_\tau K_s-A_sT_\tau}{D_C}.
\]

Since `h-j>=168`,

\[
T_\tau/U>2^{167}.
\]

All `K/U` terms are below `0.3`, so both dual numerators are negative. Since `D_C<0`,

\[
\boxed{y_\alpha>0,\qquad y_\beta>0}.
\]

The opposite alpha/beta slacks are identically `4 epsilon t>0`.

## 5. Inactive `gamma-` slack

Let

\[
K_{\gamma-}=T_\gamma-D_\gamma+2\varepsilon.
\]

Eliminating `t` with the beta equation gives

\[
S_{\gamma-}^C=\frac{A_0+A_1p_0}{K_\beta},
\]

where

\[
A_0=K_{\gamma-}C_\beta-C_\gamma K_\beta,
\]
\[
A_1=A_\gamma K_\beta-K_{\gamma-}A_\beta.
\]

The certificate proves

\[
A_0/U>1.2405681779633815\times10^{-4},\quad A_1/U>0.1245485803302464
\]

for even support, and

\[
A_0/U>9.07234844630048\times10^{-5},\quad A_1/U>0.0933928636635797
\]

for odd support. Since `K_beta>0` and `p0>0`,

\[
\boxed{S_{\gamma-}^C>0}.
\]

## 6. `Phi<0` protects the inactive `gamma+` slack

Let `G+` denote the adjacent gamma-plus basis with `P={0,j,j+1,M}`. The exact bordered-basis identity is

\[
\boxed{p_{j+1}^{G+}=-S_{\gamma+}^C\frac{\det B_C}{\det B_{G+}}.}
\]

The minus sign comes from the odd five-column insertion needed to place `p_(j+1)` in the declared P order.

A81 block elimination gives

\[
\det B_C=(M/2)\Delta_C.
\]

The C2 neighboring-determinant estimate gives `Delta_C>0`, so `det B_C>0`. A114-B1 fixes the gamma-plus determinant orientation positively on the complete tail localization strip. A112-A gives

\[
p_{j+1}^{G+}=\Phi/D_G,\qquad D_G>0.
\]

Therefore

\[
\boxed{\Phi<0\Longrightarrow S_{\gamma+}^C>0}.
\]

This is an exact pivot relation, not a finite-census inference.

## 7. All P reduced costs

For each neighboring compressed contact `k=j-1,j,j+1`, the A81 interior-mass numerator satisfies

\[
N_z>0.003,
\]

and the neighboring reduced determinant has normalized lower margin above `0.003`. Thus the neighboring interior masses are positive.

Strict compressed maximality gives

\[
E_{j-1}=V_j-V_{j-1}>0,\qquad E_j=V_{j+1}-V_j<0.
\]

The exact adjacent simplex identities therefore yield

\[
\boxed{r_C(p_{j-1})>0},\qquad \boxed{r_C(p_{j+1})>0}.
\]

The P reduced-cost function belongs to the previously validated five-dimensional extended-Chebyshev space and has basic roots at `0,j,M`. Positivity at the two neighboring checkpoints exhausts the remaining zero budget around `j`; any additional nonpositive integer would force an extra zero. Hence

\[
\boxed{r_C(p_x)>0\quad\forall x\notin\{0,j,M\}}.
\]

## 8. Q checkpoints and ECT closure

Let `R_f(x)` be the interpolation remainder obtained by interpolating `f^x` at `1,h,h+1` in `span{1,x,tau^x}`. Then exactly

\[
r_C(q_x)=y_\beta R_\beta(x)-y_\alpha R_s(x).
\]

For `x=0` and `x=2`, the node-1 interpolation coefficients are

\[
a_0=\frac{2-(h+2)U}{1-(h+1)U}>1.99,
\]
\[
a_2=\frac{1/2-hU}{1-(h+1)U}>0.49.
\]

The high-node derivative tail is bounded by

\[
13(h+1)^2s^{h-1}<10^{-3}.
\]

Thus, uniformly for `beta<=f<=s`,

\[
R_0'(f)<-1.9,\qquad R_2'(f)<-0.2.
\]

Since `s-beta>=0.004`,

\[
R_\beta(0)-R_s(0)>19/2500,
\]
\[
R_\beta(2)-R_s(2)>1/1250.
\]

The remaining `A_s-A_beta` correction is below `10^-20`. The exact positive cores satisfy

\[
J_0>0.0075924,
\qquad J_2>0.0007992.
\]

Since `T_tau/U>2^167` while every remaining normalized K term is `O(1)`, these cores dominate strictly, giving

\[
\boxed{r_C(q_0)>0},\qquad \boxed{r_C(q_2)>0}.
\]

The Q reduced-cost function lies in the same five-dimensional ECT class and has basic roots at `1,h,h+1`. Positivity at `0,2` forces an even zero count across the root at `1`; the consecutive roots `h,h+1` consume the rest of the zero budget and flip sign twice. Hence

\[
\boxed{r_C(q_x)>0\quad\forall x\notin\{1,h,h+1\}}.
\]

## 9. KKT closure

All basic variables and `t` are positive; both active duals are positive; all nonbasic P/Q reduced costs are positive; the opposite alpha/beta slacks and both inactive gamma slacks are positive. Therefore `C` satisfies the complete strict KKT system and is the unique strict global basic optimum of the full declared finite LP.

## 10. Executable evidence

`a114b2c2_compressed_branch_analytic_certificate.py` reports

\[
\boxed{49/49\text{ exact rational gates PASS}}.
\]

The pre-existing independent full-LP Fraction reconstruction contains three C controls:

- `(538,53/400)`: `1085/1085`;
- `(973,13/100)`: `1955/1955`;
- `(989,33/250)`: `1987/1987`.

All have exact basis equations and exact primal-dual equality. They are regression controls only; they are not premises of the all-tail proof.

## Claim boundary

C2 does **not** prove:

- anything on `p0^C=0`;
- anything on `Phi=0`;
- the QI/QA split when `p0^C<0` and `r_E(q0)<0`;
- strictness on any zero-discriminant boundary;
- anything outside the frozen source/tail contract;
- any physical interpretation.

After C2, the only open strict interior branch of the negative-pivot `b+2` tail is

\[
\boxed{p_0^C<0,\qquad r_E(q_0)<0},
\]

where QI and QA compete.
