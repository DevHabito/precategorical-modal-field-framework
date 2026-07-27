# A88 — Nine-Term Local Secant Reduction and Extended Positivity Stress

**Programme:** Modal Field Research Programme  
**Audit:** A88  
**Status:** exact algebraic reduction, exact finite stress on a declared rational grid, and a parity-phase asymptotic leading-limit certificate  
**Claim boundary:** no all-
\(M\) finite threshold, no global monotonicity theorem, and no physical interpretation

## 1. Question

A87 introduced the local secant

\[
S_{M,b}(s)=E_{M,b}(s)-E_{M,b+1}(s),
\qquad
b=\lceil M c(s)\rceil,
\]

where

\[
c(s)=\frac{\log 2}{-2\log s}.
\]

The three-offset classifier requires

\[
S_{M,b}(s)>0.
\]

A87 certified that inequality for \(10\le M\le300\) at three rational probes. A88 asks three narrower questions:

1. Does the secant itself possess a reduced exact form?
2. Does its positivity persist on a denser rational probe grid and a substantially larger support range?
3. Is there an asymptotic mechanism explaining the sign without pretending that the finite scan is an all-\(M\) proof?

## 2. Exact secant transform

The A84 factor is a confluent exponential polynomial with pure terms \(c r^k\), affine terms \((a+b k)r^k\), and one constant term.

For a pure term,

\[
c r^k-c r^{k+1}=c(1-r)r^k.
\]

For an affine term,

\[
(a+b k)r^k-(a+b(k+1))r^{k+1}
=
\left([(1-r)a-rb]+(1-r)b k\right)r^k.
\]

The constant channel cancels. Consequently, the ten-term A84 factor becomes the exact nine-term secant

\[
\begin{aligned}
S_{M,k}(s)={}&
 d_{\beta s}(\beta s)^k
+d_{\beta t}(\beta t)^k
+d_{st}(st)^k\\
&+(d_\beta+k d_{k\beta})\beta^k
 +(d_s+k d_{ks})s^k\\
&+(d_t+k d_{kt})t^k,
\end{aligned}
\]

with \(\beta=1/8\) and \(t=1/2\).

The transformed coefficients are not independently fitted. They are determined from the A84 coefficients by

\[
d_r=(1-r)c_r-r c_{kr},
\qquad
d_{kr}=(1-r)c_{kr}
\]

for the affine nodes, and by \(d_r=(1-r)c_r\) for pure nodes.

## 3. Coefficient-sign obstruction

In the declared order

\[
(\beta s)^k,
(\beta t)^k,
(st)^k,
\beta^k,
k\beta^k,
s^k,
ks^k,
t^k,
kt^k,
\]

the exact coefficient signs are

\[
\boxed{+,-,+,+,-,-,+,-,+}.
\]

This pattern is invariant in all 8,019 finite cells audited by A88 and has six sign variations.

Therefore, the constant cancellation improves the representation from ten to nine terms, but a raw Descartes or variation-diminishing count still cannot prove positivity or a single zero. Six is not one. This is a negative result about a tempting proof route.

## 4. Exact finite contract

A88 freezes

\[
10\le M\le900
\]

and the nine rational probes

\[
s_j=\frac{258+j}{2000},
\qquad j=0,1,\ldots,8.
\]

Thus

\[
\frac{129}{1000}
\le s_j\le
\frac{133}{1000}
\]

in steps of \(1/2000\). The original A84–A87 probes are included as \(j=0,4,8\).

For every \((M,s_j)\), the base contact

\[
b=\lceil Mc(s_j)\rceil
\]

is computed without logarithmic floating-point gates, using

\[
c(s)>\frac pq
\iff
2^q s^{2p}>1.
\]

The finite catalogue therefore contains

\[
891\times9=oxed{8,019}
\]

exact cells.

## 5. Finite result

A88 certifies

\[
\boxed{S_{M,b}(s_j)>0}
\]

in all

\[
\boxed{8,019/8,019}
\]

cells.

No zero and no negative local secant occurs.

The four A85 leading terms in secant form are

\[
S^{(4)}_{M,k}(s)
=
S_{\beta t}+S_{st}+S_t+S_{kt}.
\]

They have the same positive sign as the complete secant in every cell and satisfy

\[
|S^{(4)}_{M,b}(s_j)|
>
|S_{M,b}(s_j)-S^{(4)}_{M,b}(s_j)|
\]

in every cell. The weakest exact ratio is

\[
\frac{|S^{(4)}|}{|S-S^{(4)}|}
=
4.5409361743653968267\ldots
\]

at

\[
M=12,
\qquad
s=\frac{133}{1000},
\qquad
b=3.
\]

This is stronger than a sign match: the leading core is protected by the triangle inequality throughout the declared finite contract.

The 873 original A87 base contacts are reproduced exactly as a subset.

## 6. Parity-phase leading limit

Let

\[
h=\lfloor M/2\rfloor,
\qquad
u_M=2^{-h},
\qquad
b=\lceil Mc(s)\rceil,
\qquad
\delta_M=b-Mc(s)\in(0,1].
\]

A85 gives

\[
C_{\rm even}(s)=s-\beta-\frac{2}{1875},
\]

\[
C_{\rm odd}(s)=\frac34(s-\beta)-\frac{1}{1250}.
\]

After division by \(\nu_M t^b\), the secant leading limits are

\[
L_{\rm even}(s,\delta)
=
\frac{t-s}{2}(1-st)s^\delta
-(1-t)C_{\rm even}(s)(1-c(s)),
\]

and

\[
L_{\rm odd}(s,\delta)
=
\frac{t-s}{2\sqrt2}(1-st)s^\delta
-(1-t)C_{\rm odd}(s)(1-c(s)).
\]

The factor \(1/\sqrt2\) comes from

\[
2^{-\lfloor M/2\rfloor}
=
\sqrt2\,2^{-M/2}
\]

on odd supports.

### 6.1 Conservative rational lower bounds

For

\[
\frac{129}{1000}\le s\le\frac{133}{1000},
\qquad 0\le\delta\le1,
\]

use

\[
s^\delta\ge s\ge\frac{129}{1000},
\qquad
0<c(s)<1,
\]

and

\[
\frac1{\sqrt2}>\frac7{10},
\]

because \(49/100<1/2\).

The common positive even lower contribution is

\[
\frac{88,389,381}{4,000,000,000}
=0.02209734525.
\]

The even negative contribution is at most

\[
\frac{13}{3750},
\]

so

\[
\boxed{
L_{\rm even}
>
\frac{223,568,143}{12,000,000,000}
=0.01863067858\ldots>0.
}
\]

For odd supports, the rational \(7/10\) bound gives

\[
\boxed{
L_{\rm odd}
>
\frac{514,725,667}{40,000,000,000}
=0.012868141675>0.
}
\]

Thus every parity-phase leading limit in the declared local interval is strictly positive.

## 7. What this proves

A88 proves:

1. an exact nine-term formula for the A87 local secant;
2. exact positivity at \(b=\lceil Mc(s)\rceil\) in 8,019 declared cells;
3. exact four-term-core sign agreement and strict dominance in all cells;
4. a fixed nine-term coefficient-sign pattern with six variations;
5. strictly positive parity-phase leading limits over the full local interval.

## 8. What this does not prove

A88 does **not** prove:

1. finite positivity for every \(M>900\);
2. an explicit uniform remainder threshold \(M_0\);
3. global monotonicity of \(E_{M,k}\) in \(k\)—A87 already falsified that statement;
4. a universal three-contact strip outside the declared probes;
5. a physical meaning for contacts, bands, secants, or the asymptotic slope.

The finite scan and the asymptotic leading-limit argument support one another, but they are not silently merged into an all-\(M\) theorem.

## 9. Next rigorous target

The next step is to bound the five-term secant residual explicitly relative to the four-term core. A successful A89 would produce a computable threshold

\[
M_0(s)
\]

or a uniform threshold on the local interval, beyond which

\[
S_{M,\lceil Mc(s)\rceil}(s)>0
\]

follows analytically rather than from support-by-support enumeration. If such a uniform bound fails, the failure must be reported rather than repaired by changing the interval.
