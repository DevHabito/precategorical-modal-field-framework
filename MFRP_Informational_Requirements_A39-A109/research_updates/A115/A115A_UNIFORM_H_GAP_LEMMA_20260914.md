# A115-A — uniform normalized `H_s-H_beta` gap on a local parameter box

**Date:** 2026-09-14  
**Status:** **PROVED ANALYTIC LEMMA under the declared local box.**

This is a supporting lemma for a possible open-neighborhood extension of A113. It is **not** by itself a one-variation theorem.

## Contract

Let

\[
M\ge521,\qquad h=\lfloor M/2\rfloor,
\]

\[
\beta\in[31/250,63/500],
\qquad
s\in[129/1000,133/1000],
\qquad
\tau\in[49/100,51/100].
\]

Set

\[
U=\tau^h
\]

and use the dimensionless tolerance scaling

\[
\varepsilon=\bar\varepsilon U,
\qquad
\bar\varepsilon=
\begin{cases}
1/1875,&M\text{ even},\\
1/2500,&M\text{ odd}.
\end{cases}
\]

For the central-Q block `Q={1,h,h+1}`, solve normalization, mean and target equations with target node `tau`. Write the coefficient of `t` in the transform at a node `v` as

\[
D(v)=D_1v+D_hv^h+D_{h+1}v^{h+1}.
\]

Define

\[
H_s=\frac{1+s^M}{2}-D(s)-2\varepsilon,
\qquad
H_\beta=\frac{1+\beta^M}{2}-D(\beta)+2\varepsilon.
\]

## Claim

Uniformly over the complete contract,

\[
\boxed{
\frac{H_s-H_\beta}{U}>\frac{28}{10000}=0.0028.
}
\]

## Proof

Let

\[
\Delta=\tau-U\bigl[h(1-\tau)+\tau\bigr].
\]

Direct solution of the three central-Q equations gives the following exact `t` coefficients.

For even `M` (`M=2h`):

\[
D_1=-\frac{U}{\Delta},
\qquad
D_h=\frac{\tau(1+U(h-1))}{\Delta},
\qquad
D_{h+1}=-\frac{U(h-1)}{\Delta}.
\]

For odd `M` (`M=2h+1`):

\[
D_1=-\frac{U(1+\tau)}{2\Delta},
\]

\[
D_h=\frac{\tau(1/2+U(h-1/2))}{\Delta},
\qquad
D_{h+1}=\frac{\tau/2-U(h-1/2)}{\Delta}.
\]

Since

\[
H_s-H_\beta
=
\frac{s^M-\beta^M}{2}
-D_1(s-\beta)
-D_h(s^h-\beta^h)
-D_{h+1}(s^{h+1}-\beta^{h+1})
-4\varepsilon,
\]

the first term is nonnegative and may be discarded in a lower bound.

### Tail denominator

For `h>=260`, the sequence `h(0.51)^h` is decreasing because

\[
\frac{h+1}{h}\,0.51
\le \frac{261}{260}\,0.51
<1.
\]

The exact certificate gives

\[
\frac{U[h(1-\tau)+\tau]}{\tau}
<2.525\times10^{-74}<\frac12.
\]

Hence

\[
\Delta>\frac\tau2>0,
\qquad
\Delta<\tau.
\]

### Dominant positive term

Because `Delta<tau`, the normalized contribution from `-D_1(s-beta)` is strictly larger than

\[
\frac{s-\beta}{\tau}
\]

for even `M`, and than

\[
\frac{1+\tau}{2\tau}(s-\beta)
\]

for odd `M`.

The smallest source/beta separation in the box is

\[
s-\beta\ge\frac3{1000}.
\]

### High-node tails

Using `Delta>tau/2` and the exponentially small `hU`, the potentially negative high-node contribution is bounded in both parities by

\[
3s^h.
\]

After division by `U=tau^h`,

\[
\frac{3s^h}{U}
\le
3\left(\frac{133}{490}\right)^{260}
<1.689\times10^{-147}.
\]

### Even parity

Therefore

\[
\frac{H_s-H_\beta}{U}
>
\frac{3/1000}{51/100}
-\frac4{1875}
-3\left(\frac{133}{490}\right)^{260}
\]

\[
>0.003749019607843137\ldots
>0.0037.
\]

### Odd parity

Similarly,

\[
\frac{H_s-H_\beta}{U}
>
\frac{3}{1000}\frac{1+51/100}{2(51/100)}
-\frac4{2500}
-3\left(\frac{133}{490}\right)^{260}
\]

\[
>0.002841176470588235\ldots
>0.0028.
\]

The odd bound is the uniform minimum, proving the claim.

## Interpretation of the lemma

The dominant dimensionless separation is

\[
\kappa(\tau)(s-\beta)-4\bar\varepsilon,
\]

with

\[
\kappa_{\rm even}(\tau)=\frac1\tau,
\qquad
\kappa_{\rm odd}(\tau)=\frac{1+\tau}{2\tau}.
\]

This gives a concrete structural reason that moving `beta` too close to `s` can destroy the frozen-tail sign mechanism. It is consistent with, but does not by itself prove the cause of, the exact A115 counterexamples near `beta=0.128`.

## Nonclaims

This lemma does not prove:

- the generalized A113 one-variation theorem;
- the middle-left or remote-right `E_k` signs by itself;
- generalized central nesting `J_tau>0`;
- persistence of any A114 lifted active-set architecture;
- any physical or ontological statement.
