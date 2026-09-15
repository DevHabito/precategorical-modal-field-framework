# A120 — fixed-interior remote-sign rounding-phase theorem

**Date:** 2026-09-15  
**Status:** **PROVED under the inherited A115 target-deformed reduced-factor contract; exact counterexamples and executable audit included.**  
**Classification:** asymptotic theorem + exact refutation of naive remote-sign stabilization.  
**No physical or ontological interpretation is claimed.**

---

## 1. Scope

Keep

\[
\beta=\frac18,\qquad \delta=\frac1{1875},\qquad
\frac{129}{1000}\le s\le\frac{133}{1000}.
\]

Fix a target node strictly in the inherited A84 ordering region,

\[
\boxed{s<\tau<\frac\beta s<1.}
\]

Thus

\[
\beta s<\beta\tau<s\tau<\beta<s<\tau<1.
\]

Let

\[
h=\left\lfloor\frac M2\right\rfloor,
\qquad
u_M=\tau^h,
\]

and define the exact contact location

\[
 c=c_\tau(s):=\frac{\log\tau}{2\log s}\in(0,1/2),
\qquad
 b_M=\lceil Mc\rceil.
\]

Write the rounding phase

\[
\boxed{\rho_M=b_M-Mc\in[0,1).}
\]

Fix an integer offset `j`. For all sufficiently large `M`, the factor

\[
E_{M,b_M+j}(s,\tau)
\]

is inside the inherited central-factor domain for every fixed `j` considered here.

---

## 2. Parity constants

Along one fixed parity define

\[
\sigma_p=
\begin{cases}
0,&M\text{ even},\\[2pt]
\frac12,&M\text{ odd},
\end{cases}
\]

and

\[
a_p(\tau)=
\begin{cases}
1,&M\text{ even},\\[2pt]
\dfrac{1+\tau}{2},&M\text{ odd}.
\end{cases}
\]

Set

\[
\boxed{
G(s,\tau)=\frac{s-\beta}{\tau}-4\delta.
}
\]

On the frozen source window and the declared target-ordering region, `G>0`. Indeed

\[
\frac{s-\beta}{\tau}
>
\frac{s(s-\beta)}{\beta}
\ge
\frac{129}{1000}\frac{4}{125}
>
\frac4{1875}.
\]

---

# 3. Theorem A — rounding-phase asymptotic

For every fixed interior pair `(s,tau)`, fixed parity `p`, and fixed integer offset `j`,

\[
\boxed{
\frac{E_{M,b_M+j}(s,\tau)}
{\nu_M\tau^{b_M+j}}
-
\Psi_{p,j}(s,\tau;\rho_M)
\longrightarrow0
}
\]

along integers `M` of that parity, where

\[
\boxed{
\Psi_{p,j}(s,\tau;\rho)
=
\frac{\tau-s}{2}\,\tau^{\sigma_p}s^{j+\rho}
-a_p(\tau)(1-\tau)G(s,\tau)(1-c).
}
\]

Thus a fixed interior target does **not** generally produce a single remote-sign limit. The surviving limit depends on the ceiling phase `rho_M`.

---

# 4. Proof of Theorem A

A115 gives the exact ten-term expansion

\[
\begin{aligned}
E_k={}&
 c_{\beta s}(\beta s)^k
+c_{\beta\tau}(\beta\tau)^k
+c_{s\tau}(s\tau)^k\\
&+(c_\beta+k c_{k\beta})\beta^k
+(c_s+k c_{ks})s^k
+(c_\tau+k c_{k\tau})\tau^k
+c_1.
\end{aligned}
\]

We analyze these coefficients for fixed `beta<s<tau<1` as `M->infinity`.

## 4.1 Central-Q response

For `r` equal to `beta` or `s`, the exact A115 Q-response coefficient satisfies

\[
D_r=
\begin{cases}
 r^h-\nu_M\dfrac{L_r}{D_\tau},&M\text{ even},\\[8pt]
 \dfrac{r^h+r^{h+1}}2
 -\dfrac{1+\tau}{2}\nu_M\dfrac{L_r}{D_\tau},&M\text{ odd},
\end{cases}
\]

where

\[
L_r=r-hr^h+(h-1)r^{h+1},
\qquad
D_\tau=\tau-h\nu_M+(h-1)\tau\nu_M.
\]

Because `r<tau<1`,

\[
\frac{r^h}{\nu_M}=\left(\frac r\tau\right)^h\to0,
\qquad
L_r\to r,
\qquad
D_\tau\to\tau.
\]

Hence

\[
\boxed{
\frac{D_r}{\nu_M}\to-a_p(\tau)\frac r\tau.
}
\]

The exact A115 tolerance satisfies

\[
\frac{\varepsilon_{\tau,M}}{\nu_M}\to a_p(\tau)\delta.
\]

Therefore

\[
H_\beta
=
\frac12+a_p\nu_M\left(\frac\beta\tau+2\delta\right)+o(\nu_M),
\]

\[
H_s
=
\frac12+a_p\nu_M\left(\frac s\tau-2\delta\right)+o(\nu_M).
\]

In particular,

\[
\boxed{
H_\beta-H_s=-a_p\nu_M G+o(\nu_M).
}
\]

Also

\[
A=\frac{1+\tau^M}{2}=\frac12+o(\nu_M).
\]

## 4.2 Surviving coefficients

Let

\[
a_x=\frac{1-x^M}{M}.
\]

For `x<=tau`,

\[
a_x=\frac1M+o(\nu_M/M).
\]

From the exact A115 coefficient identities,

\[
\boxed{c_{s\tau}=H_\beta(\tau-s)\to\frac{\tau-s}{2}.}
\]

For the target-affine coefficients,

\[
c_\tau
=(1-\tau)(H_\beta-H_s)
+(H_s a_\beta-H_\beta a_s),
\]

so

\[
\boxed{
\frac{c_\tau}{\nu_M}
\to-a_p(1-\tau)G.
}
\]

Likewise

\[
c_{k\tau}
=(\tau-1)(H_\beta a_s-H_s a_\beta),
\]

which gives

\[
\boxed{
\frac{M c_{k\tau}}{\nu_M}
\to a_p(1-\tau)G.
}
\]

Since

\[
\frac{b_M+j}{M}\to c,
\]

the normalized target-affine channel tends to

\[
-a_p(1-\tau)G(1-c).
\]

## 4.3 Rounding phase in the product channel

By definition of `c`,

\[
s^{Mc}=\tau^{M/2}.
\]

Since

\[
b_M+j=Mc+\rho_M+j,
\]

we obtain the exact identity

\[
\frac{s^{b_M+j}}{\nu_M}
=
\tau^{\sigma_p}s^{j+\rho_M}.
\]

Therefore the normalized `s tau` channel is

\[
\frac{c_{s\tau}(s\tau)^{b_M+j}}
{\nu_M\tau^{b_M+j}}
\to
\frac{\tau-s}{2}\tau^{\sigma_p}s^{j+\rho_M}.
\]

## 4.4 All other channels vanish

The product channels containing `beta` vanish after normalization because `beta<s<tau` and `s^{b_M+j}/nu_M` remains bounded between positive parity-dependent constants.

The beta-affine and source-affine coefficients satisfy

\[
c_\beta,c_s=O(\nu_M),
\qquad
c_{k\beta},c_{ks}=O(\nu_M/M),
\]

while their exponential factors contribute respectively `(beta/tau)^k` and `(s/tau)^k`, both tending to zero.

Finally the exact constant grouping gives

\[
c_1=O\left(\frac{\nu_M\tau^M}{M}\right),
\]

so

\[
\frac{c_1}{\nu_M\tau^{b_M+j}}
=O\left(\frac{\tau^{M-b_M-j}}M\right)\to0
\]

because `b_M/M->c<1/2`.

Summing the two surviving channels proves Theorem A.

---

# 5. Corollary — one rounding threshold per parity and offset

For fixed `(s,tau,p,j)`, write

\[
P_{p,j}=\frac{\tau-s}{2}\tau^{\sigma_p}s^j,
\qquad
Q_p=a_p(1-\tau)G(1-c)>0.
\]

Then

\[
\Psi_{p,j}(\rho)=P_{p,j}s^\rho-Q_p.
\]

Since `0<s<1`, this is strictly decreasing in `rho`.

Hence exactly one of the following occurs:

1. **uniform positive phase:** `Q_p < P_{p,j}s`;
2. **uniform negative phase:** `Q_p > P_{p,j}`;
3. **mixed rounding phase:**
   \[
   P_{p,j}s<Q_p<P_{p,j},
   \]
   in which case there is a unique
   \[
   \boxed{
   \rho^*_{p,j}=\frac{\log(Q_p/P_{p,j})}{\log s}\in(0,1)
   }
   \]
   with positive phase below `rho*` and negative phase above it;
4. equality cases give a phase zero at an endpoint.

Thus the remote sign problem has a one-dimensional rounding-phase classification.

---

# 6. The naive target-deformed A113 remote package is false

A natural but incorrect conjecture was that every fixed interior target eventually satisfies

\[
E_{b_M}>0,
\qquad
E_{b_M+3}<0.
\]

Both halves fail.

## 6.1 Exact negative `E_b`

With

\[
M=1200,
\qquad
s=\frac{131}{1000},
\qquad
\tau=\frac15,
\]

the exact contact is

\[
b_M=476,
\]

and exact `Fraction` arithmetic gives

\[
\boxed{E_{M,b_M}<0.}
\]

The factors are admissible.

## 6.2 Exact positive `E_{b+3}`

With

\[
M=536,
\qquad
s=\frac{129}{1000},
\qquad
\tau=\frac9{10},
\]

the exact contact is

\[
b_M=14,
\]

and exact arithmetic gives

\[
\boxed{E_{M,b_M+3}>0.}
\]

This target also obeys

\[
s\tau<\beta.
\]

---

# 7. The failures persist infinitely often for fixed interior targets

The two finite counterexamples above are not merely small-`M` accidents.

## 7.1 Negative and positive `E_b` infinitely often

Take

\[
s=\frac{131}{1000},
\qquad
\tau=\frac15.
\]

The exact power comparisons

\[
s^{790}>\tau^{1000},
\qquad
s^{794}<\tau^{1000}
\]

prove

\[
\frac{395}{1000}<c<\frac{397}{1000}.
\]

For even parity and `j=0`, exact rational bounds give

\[
\Psi_{\rm even,0}(0)
>
\frac{78797}{3750000}>0,
\]

while

\[
\Psi_{\rm even,0}(1)
<
-\frac{446169}{50000000}<0.
\]

Moreover `c` is irrational. If `c=m/n` were rational, then

\[
\tau^n=s^{2m}.
\]

But `s=131/(2^3 5^3)` contains the prime `131`, while `tau=1/5` does not, contradicting unique factorization.

Thus `{2nc}` is dense modulo one, so the even-parity rounding phases `rho_{2n}` are dense in `(0,1)`. By Theorem A and the strict nonzero margins above,

\[
\boxed{E_{b_M}>0\text{ for infinitely many even }M}
\]

and

\[
\boxed{E_{b_M}<0\text{ for infinitely many even }M.}
\]

Therefore no eventual sign exists for `E_b` at this fixed interior pair.

## 7.2 Positive and negative `E_{b+3}` infinitely often

Take

\[
s=\frac{129}{1000},
\qquad
\tau=\frac9{10}.
\]

Exact power comparisons give

\[
\frac{25}{1000}<c<\frac{27}{1000}.
\]

For even parity and `j=3`,

\[
\Psi_{\rm even,3}(0)
>
\frac{3613291657}{6000000000000}>0,
\]

while

\[
\Psi_{\rm even,3}(1)
<
-\frac{2126112128741}{18000000000000000}<0.
\]

Again `c` is irrational: `s=129/1000` contains the prime `43`, while `tau=9/10` does not, so no positive rational-power identity `tau^n=s^{2m}` is possible.

Hence the even rounding phases are dense and

\[
\boxed{E_{b_M+3}>0\text{ infinitely often}}
\]

and

\[
\boxed{E_{b_M+3}<0\text{ infinitely often}.}
\]

Thus no eventual negative sign exists for `E_{b+3}` at this fixed interior pair either.

---

# 8. Relation to the frozen A113 theorem

A120 does **not** refute A113. A113 is the special frozen target `tau=1/2` and proves finite all-tail inequalities there.

A120 explains why that success cannot be exported by simply replacing `1/2` with arbitrary `tau`: once the target moves, the remote factors can retain the ceiling phase `rho_M` at leading order.

The accompanying exact audit rechecks 21 frozen `tau=1/2` sentinels and reproduces

\[
E_b>0,
\qquad
E_{b+3}<0.
\]

---

# 9. What A120 establishes

1. The fixed-interior remote factors possess a parity-resolved rounding-phase asymptotic.
2. For each fixed offset there is at most one sign transition as a function of the ceiling phase `rho`.
3. The naive target-deformed remote-sign stabilization is false.
4. There are explicit fixed interior pairs for which `E_b` changes sign infinitely often.
5. There are explicit fixed interior pairs for which `E_{b+3}` changes sign infinitely often.
6. The obstruction is structural ceiling arithmetic, not a finite-`M` numerical artifact.

---

# 10. Nonclaims

A120 does **not** establish:

- a target-deformed A113 one-variation theorem;
- a target-deformed A114 lifted active-set classification;
- a classification of the separate collision scaling `tau-s=O(1/M)` for the remote factors;
- a minimal finite realization threshold for any rounding phase;
- novelty or priority relative to the literature;
- any RZS, modal-field, physical, spacetime, gravity, matter, or ontological interpretation.
