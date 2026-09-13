# A114-B2-B — analytic exclusion of the pure gamma-minus branch on the negative-pivot tail

## Status

**PROVED LEMMA under the frozen analytic-tail contract.**

Let

\[
M\ge521,\qquad s\in[129/1000,133/1000],\qquad h=\lfloor M/2\rfloor,
\]

\[
b=\lceil Mc(s)\rceil,\qquad c(s)=\frac{\log2}{-2\log s},\qquad j=b+2,
\]

and define the upper gamma pivot

\[
\Phi(M,s)=F_j^{\rm up}(s)=F_{b+2}^{\rm up}(s).
\]

If

\[
\Phi(M,s)<0,
\]

then the central-Q pure gamma-minus architecture

\[
P=\{0,j-1,j,M\},\qquad Q=\{1,h,h+1\},
\]

with active `alpha+`, `beta-`, `gamma-`, cannot be strictly primal feasible. In particular it cannot be a strict KKT optimum.

This result does **not** classify the remaining negative-pivot architectures.

## 1. Dyadic separation forced by the negative upper pivot

A112-A gives the exact k-space decomposition

\[
F_k^{\rm up}=X s^k+P_\beta\beta^k+P_\gamma\gamma^k-
\left(1-\frac{k}{M}\right)S-\frac{k}{M}T_M,
\]

and the rigorous A112-A V2 re-audit supplies uniform tail bounds on the cofactor and finite-tail remainders.

Assume for contradiction that

\[
3j-h\le12.
\]

Writing

\[
U=2^{-h},\qquad Y=\frac{\beta^j}{U}=2^{h-3j},
\]

this gives

\[
Y\ge2^{-12}.
\]

Since A89/A112-A give `b>=89`, we have `j>=91`. Therefore

\[
\frac{V_j}{U}
\ge
2^{-12}\left[(\beta-\gamma)(8s)^{91}-(s-\gamma)\right]
\]

and uniformly on the source window

\[
\frac{V_j}{U}
\ge
2^{-12}\left[\frac1{16}\left(8\frac{129}{1000}\right)^{91}
-\left(\frac{133}{1000}-\frac1{16}\right)\right].
\]

Also `j/M>c(s)>16923/100000`, so the largest affine subtraction is bounded by

\[
\left(1-\frac{16923}{100000}\right)
\frac{8(133/1000-1/16)}{1875}.
\]

After a conservative aggregate allowance `10^-70` for the already-audited A112-A V2 cofactor/remainder errors, the exact residual margin is

\[
>1.0392\times10^{-6}>0.
\]

Hence `F_j^up>0`, contradicting `Phi<0`. Thus

\[
\boxed{\Phi<0\Longrightarrow 3j-h\ge13.}
\]

## 2. Gamma-minus primal reduction

For the candidate

\[
P=\{0,j-1,j,M\},\qquad Q=\{1,h,h+1\},
\]

use only:

- P normalization and mean;
- Q normalization, mean and target;
- active beta-minus;
- active gamma-minus.

After eliminating Q and solving the four P interpolation equations, the two relevant P masses are affine functions of the Charnes-Cooper scale:

\[
p_0(t)=a_0t+c_0,
\qquad
p_j(t)=a_jt+c_j.
\]

The alpha equation is not used in this step.

Set

\[
T=2^{-j},\qquad Y=2^{h-3j},\qquad U=2^{-h}.
\]

From `j=b+2`, the A89 slope brackets and `M>=521` imply

\[
\frac13<\frac jh<\frac38.
\]

From the first part,

\[
Y\le2^{-13}.
\]

Also `j<h`, hence

\[
Y\ge8U^2.
\]

The standalone symbolic certificate reconstructs the exact even/odd matrices, factors every Cramer numerator, and bounds every non-leading monomial with rational majorants. It proves, in both parities,

\[
\boxed{a_0<0<c_0,\qquad c_j<0<a_j.}
\]

Define

\[
K=c_0a_j-c_ja_0.
\]

The same exact remainder certificate proves

\[
\boxed{K<0.}
\]

Therefore the two positive zeros

\[
t_0=-\frac{c_0}{a_0},\qquad t_j=-\frac{c_j}{a_j}
\]

satisfy

\[
t_j-t_0=\frac{K}{a_0a_j}>0.
\]

Consequently

\[
p_j>0\Longrightarrow t>t_j>t_0\Longrightarrow p_0<0.
\]

So the pure gamma-minus basis can never have all strict positive basic masses.

## 3. Independent falsification layers

The proof is analytic. The following are separate controls:

1. A standalone `fractions.Fraction` reduced-system implementation scans `M=521..1000` at nine exact rational probes. Among 1,232 `Phi<0` cases it finds zero violations of `3j-h>=13` and zero cases with `p_j>0` and `p_0>=0`.
2. An exact envelope scan checks 2,271 `(M,j)` pairs through `M=1000`, using a contact interval slightly wider than the A89 tail envelope. It finds zero failures of the coefficient signs and zero failures of `K<0`.
3. Fourteen exact small-M `unique_b_plus_2` A102 gamma-minus witnesses are retained as negative controls. Every one has `Phi<0`, all pure gamma-minus basic masses positive, and `3j-h<13`. Thus the tail gate is essential and the theorem is not falsely extrapolated downward.

## 4. Consequence for A114-B2

Inside the strict compressed `b+2` phase:

- `Phi>0` is already closed by A114-B2-A as gamma-plus;
- `Phi<0` can no longer select the pure central-Q gamma-minus family.

The remaining negative-pivot tail architectures observed exactly are still multiple: compressed two-band, endpoint-released, q0/q1 gamma-inactive, and q0/q1 gamma-minus active. Their all-tail partition remains open.

## Claim boundary

This note does not prove:

- a complete classification of `Phi<0`;
- exhaustiveness of the four remaining observed families;
- any statement on `Phi=0`;
- any extension outside the frozen tail window;
- any physical interpretation.
