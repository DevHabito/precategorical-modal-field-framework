# A116 — compact-uniform target-deformation nesting and boundary-layer obstruction

**Date:** 2026-09-15  
**Status:** **PROVED under the target-deformed reduced-factor contract stated below; independently red-teamed in the accompanying audit note.**  
**Classification:** asymptotic mathematical theorem + exact boundary-layer obstruction.  
**No physical or ontological interpretation is claimed.**

## 1. Scope

Keep the A115 target-deformed reduced factor with

\[
\beta=\frac18,\qquad \delta=\frac1{1875},\qquad
\frac{129}{1000}\le s\le\frac{133}{1000}.
\]

To preserve the declared A84 confluent-node order, work in

\[
\Omega_{84}
=
\left\{(s,\tau):
\frac{129}{1000}\le s\le\frac{133}{1000},
\quad s<\tau<1,
\quad s\tau<\beta
\right\}.
\]

For integer \(M\), set

\[
h=\left\lfloor\frac M2\right\rfloor,
\qquad
u=\tau^h,
\]

and use the A115 scale-normalized tolerance

\[
\varepsilon_{\tau,M}
=
\begin{cases}
\delta\tau^h,&M=2h,\\[4pt]
\delta\dfrac{1+\tau}{2}\tau^h,&M=2h+1.
\end{cases}
\]

Define

\[
c_\tau(s)=\frac{\log\tau}{2\log s},
\qquad
b_\tau=\lceil M c_\tau(s)\rceil,
\]

and

\[
J_{\tau,k}=E_{M,k}(s,\tau)-\tau^{-1}E_{M,k+1}(s,\tau).
\]

A115 proved the exact target-deformed Q-block and the exact generalized
\(J\)-cancellation identity but left eventual positivity open.

---

## 2. Theorem A — compact-uniform eventual positivity

Let

\[
K\Subset\Omega_{84}
\]

be any compact subset. Then there exists an integer

\[
M_0=M_0(K)
\]

such that for every integer \(M\ge M_0\) and every \((s,\tau)\in K\):

1. the two factors used by \(J_{\tau,b_\tau+1}\) lie in the A84 adjacent-factor domain;
2. and

\[
\boxed{
J_{\tau,b_\tau+1}>0.
}
\]

In particular, every fixed interior pair \((s,\tau)\in\Omega_{84}\) has eventual positive central nesting.

### Important qualification

The theorem gives existence of \(M_0(K)\). It does **not** claim that `521`, or any other fixed finite number independent of \(K\), works globally.

---

## 3. Exact J decomposition

The A84 ten-term factor is

\[
\begin{aligned}
E_k={}&
 c_{\beta s}(\beta s)^k
+c_{\beta\tau}(\beta\tau)^k
+c_{s\tau}(s\tau)^k\\
&+(c_\beta+k c_{k\beta})\beta^k
 +(c_s+k c_{ks})s^k
 +(c_\tau+k c_{k\tau})\tau^k+c_1.
\end{aligned}
\]

The exact A115 transform gives

\[
\begin{aligned}
J_{\tau,k}={}&
 c_{\beta s}\left(1-\frac{\beta s}{\tau}\right)(\beta s)^k\\
&+c_{\beta\tau}(1-\beta)(\beta\tau)^k\\
&+c_{s\tau}(1-s)(s\tau)^k\\
&+\beta^k\left[
\left(1-\frac\beta\tau\right)c_\beta
+\left(k\left(1-\frac\beta\tau\right)-\frac\beta\tau\right)c_{k\beta}
\right]\\
&+s^k\left[
\left(1-\frac s\tau\right)c_s
+\left(k\left(1-\frac s\tau\right)-\frac s\tau\right)c_{ks}
\right]\\
&-c_{k\tau}\tau^k
+c_1\left(1-\frac1\tau\right).
\end{aligned}
\]

The nonconfluent target coefficient \(c_\tau\) cancels identically.
The accompanying symbolic audit verifies this formula directly.

---

## 4. Uniform contact localization on a compact interior set

Because \(K\Subset\Omega_{84}\), continuity gives constants

\[
0<c_-\le c_\tau(s)\le c_+<\frac12
\]

uniformly on \(K\).

Hence, with

\[
k=b_\tau+1,
\]

one has

\[
k=M c_\tau(s)+O(1)
\]

uniformly, and therefore

\[
k\to\infty,
\qquad
h-k\to\infty
\]

uniformly as \(M\to\infty\).

This proves eventual A84 admissibility of both central factors.

Write

\[
\theta_M=b_\tau-Mc_\tau(s)\in[0,1).
\]

Since

\[
s^{M c_\tau(s)}=\tau^{M/2},
\]

we obtain the exact identity

\[
\frac{s^k}{\tau^h}
=s^{1+\theta_M}\tau^{M/2-h}.
\]

Thus this ratio is bounded above and, crucially, bounded away from zero uniformly on \(K\). For example,

\[
\boxed{
\frac{s^k}{\tau^h}
\ge s_-^2\sqrt{\tau_-}>0,
}
\]

where \(s_-\) and \(\tau_-\) are the minima on \(K\).

---

## 5. Uniform coefficient asymptotics

Let

\[
D_\tau=\tau-h\tau^h+(h-1)\tau^{h+1}.
\]

For \(r\in\{\beta,s\}\), A115 gives

\[
D_r=
\begin{cases}
r^h-\tau^h\dfrac{L_r}{D_\tau},&M=2h,\\[7pt]
\dfrac{r^h+r^{h+1}}2
-\dfrac{1+\tau}{2}\tau^h\dfrac{L_r}{D_\tau},&M=2h+1,
\end{cases}
\]

with

\[
L_r=r-hr^h+(h-1)r^{h+1}.
\]

On compact \(K\),

\[
\tau\le\tau_+<1,
\qquad
\frac r\tau\le\rho<1.
\]

Therefore uniformly,

\[
h\tau^h\to0,
\qquad
h r^h\to0,
\qquad
D_\tau\to\tau,
\qquad
L_r\to r.
\]

If

\[
a_0(\tau)=1,
\qquad
a_1(\tau)=\frac{1+\tau}{2}
\]

for even and odd parity respectively, then

\[
\frac{D_r}{\tau^h}
\longrightarrow
-a_p(\tau)\frac r\tau
\]

uniformly on \(K\).

Since

\[
\frac{\varepsilon_{\tau,M}}{\tau^h}
=\delta a_p(\tau),
\]

it follows that

\[
H_\beta\to\frac12,
\qquad
H_s\to\frac12,
\qquad
A=\frac{1+\tau^M}{2}\to\frac12
\]

uniformly.

More precisely,

\[
A-H_\beta=O(\tau^h),
\qquad
A-H_s=O(\tau^h).
\]

Now set

\[
a_r=\frac{1-r^M}{M}.
\]

Using the exact grouped identities

\[
X=Aa_s-H_s a_\tau,
\qquad
Y=Aa_\beta-H_\beta a_\tau,
\qquad
Z=H_\beta a_s-H_s a_\beta,
\]

one obtains uniformly

\[
X,Y,Z=O\left(\frac{\tau^h}{M}\right).
\]

Consequently,

\[
c_\beta,c_s=O(\tau^h),
\]

\[
c_{k\beta},c_{ks},c_{k\tau}
=O\left(\frac{\tau^h}{M}\right).
\]

The constant channel requires a sharper estimate. Its exact grouping is

\[
c_1
=A(a_\beta-a_s)
+H_\beta(a_s-a_\tau)
+H_s(a_\tau-a_\beta).
\]

Hence

\[
\boxed{
c_1=O\left(\frac{\tau^M}{M}\right),}
\]

not merely \(O(\tau^h/M)\). This sharper estimate is essential after normalization.

---

## 6. Positive main channel and vanishing remainder

Normalize by the positive scale

\[
\tau^h\tau^k.
\]

The `s tau` channel becomes

\[
T_{\rm main}
=H_\beta(\tau-s)(1-s)
\frac{s^k}{\tau^h}.
\]

Because \(K\) stays a positive distance from \(\tau=s\), and because
\(H_\beta\to1/2\) uniformly, there is a constant \(m_K>0\) such that eventually

\[
\boxed{T_{\rm main}\ge m_K>0.}
\]

Every other normalized channel tends uniformly to zero:

\[
O\!\left(\left(\frac\beta\tau\right)^k\right),
\qquad
O\!\left(\left(\frac\beta s\right)^k\right),
\]

\[
O\!\left(\left(\frac s\tau\right)^k\right),
\qquad
O\!\left(\frac1M\right),
\]

and, for the constant channel,

\[
O\!\left(
\frac{\tau^{M-h-k}}{M}
\right).
\]

Since \(c_+<1/2\),

\[
M-h-k\ge \kappa_K M-O(1)
\]

for some \(\kappa_K>0\), so the last term also vanishes uniformly.

Therefore

\[
\frac{J_{\tau,b_\tau+1}}
{\tau^h\tau^{b_\tau+1}}
=T_{\rm main}+o_K(1)>0
\]

for all sufficiently large \(M\), proving Theorem A.

---

# 7. Theorem B — no global uniform threshold up to the collision wall

The compact theorem cannot be extended to one threshold valid all the way to
\(\tau=s\).

Set

\[
s_0=\frac{133}{1000},
\qquad
\lambda=\frac52.
\]

For even \(M\), define

\[
\boxed{
\tau_M=s_0+\frac{\lambda}{M}.
}
\]

Then, for all sufficiently large even \(M\),

\[
(s_0,\tau_M)\in\Omega_{84},
\]

\[
\boxed{b_{\tau_M}=\frac M2-4,}
\]

so

\[
b_{\tau_M}+2=\frac M2-2
\]

is exactly the largest admissible A84 adjacent-factor contact, and

\[
\boxed{
J_{\tau_M,b_{\tau_M}+1}<0.
}
\]

Therefore there is **no** integer \(M_\star\) such that

\[
M\ge M_\star,
\quad (s,\tau)\in\Omega_{84}
\Longrightarrow
J_{\tau,b_\tau+1}>0
\]

uniformly over the full open target-deformation domain.

---

## 8. Boundary-layer limit

For even \(M=2h\), let more generally

\[
\tau_M=s+\frac\lambda M.
\]

Define

\[
\alpha=\frac\lambda{2s},
\qquad
B=\frac\beta s+2\delta,
\qquad
S=1-e^{-\alpha}-2\delta.
\]

If

\[
d<\frac{\lambda}{2s(-\log s)}<d+1,
\]

then eventually

\[
b_{\tau_M}=h-d,
\qquad
k=b_{\tau_M}+1=h-d+1.
\]

For the normalized quantity

\[
N_M=
\frac{J_{\tau_M,k}}
{\tau_M^h\tau_M^k},
\]

the exact A115 formulas give

\[
\boxed{
M N_M\longrightarrow
\Lambda(s,\lambda,d),
}
\]

where

\[
\boxed{
\Lambda(s,\lambda,d)
=(1-s)\left[
\frac\lambda2 s^{1-d}e^{-\alpha}
+(B-S)
-B(\alpha+1)e^{-\alpha}
\right].
}
\]

This limit includes the source-affine and target-slope terms that disappear on a fixed compact interior set. It is precisely the boundary layer missed by any argument that treats \(s/\tau\) as uniformly bounded away from one.

---

## 9. Exact negativity certificate for the chosen boundary sequence

For

\[
s=\frac{133}{1000},
\qquad
\lambda=\frac52,
\qquad
d=4,
\]

one has

\[
\alpha=\frac{1250}{133}.
\]

The exact audit gives rational Taylor certificates for

\[
2< -\log\left(\frac{133}{1000}\right)<\frac{21}{10}.
\]

Hence

\[
4<
\frac{\alpha}{-\log s}
<5,
\]

which proves the eventual contact identity \(b=h-4\).

Write

\[
\frac{\Lambda}{1-s}
=-C+e^{-\alpha}Q,
\]

where exactly

\[
C=1-\frac\beta s-4\delta
=\frac{14468}{249375}>0,
\]

and

\[
Q
=1+\frac\lambda2 s^{-3}
-\left(\frac\beta s+2\delta\right)(\alpha+1)
=\frac{768333854492}{1470398125}>0.
\]

The positive Taylor partial sum through degree 12 satisfies exactly

\[
\sum_{n=0}^{12}\frac{\alpha^n}{n!}>10000,
\]

so

\[
e^{-\alpha}<\frac1{10000}.
\]

Finally,

\[
C-\frac{Q}{10000}
=
\frac{63560739131}{11027985937500}>0.
\]

Therefore

\[
\boxed{\Lambda<0.}
\]

Since \(MN_M\to\Lambda\), the exact negative boundary sequence follows.

---

## 10. Exact finite regression

The accompanying standalone `Fraction` audit checks the boundary sequence at

\[
M=2000,\ 5000,\ 10000,\ 20000
\]

and obtains

\[
b=M/2-4,
\qquad
J<0
\]

in all four exact controls.

It also records 30 exact positive controls at two deep-tail support sizes on a fixed interior stress set. These computations are regression/falsification evidence only; neither finite set is a premise of either theorem.

---

## 11. What A116 establishes

1. A115 fixed-pair eventual positivity is proved inside the inherited A84 node-order domain.
2. The result is stronger: positivity is uniform on every compact interior subset.
3. The convergence is not uniform up to \(\tau=s\).
4. A concrete even-M boundary sequence remains negative arbitrarily deep in the tail.
5. Hence replacing the refuted threshold `521` by any larger global constant cannot solve the problem.
6. The correct structure is an interior theorem plus a nontrivial \(1/M\) collision boundary layer.

## 12. Nonclaims

A116 does not establish:

- a finite minimal formula for \(M_0(K)\);
- positivity on the collision surface \(\tau=s\);
- a complete classification of the boundary-layer sign for every \(d\) and \(\lambda\);
- a target-deformed A114 lifted active-set staircase;
- any physical or ontological interpretation.
