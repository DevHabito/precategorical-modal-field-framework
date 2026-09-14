# A115 — parameter-dependence audit after frozen-tail closure

**Date:** 2026-09-14  
**Status:** **AUDIT / FINITE EXACT EVIDENCE + ONE SYMBOLIC IDENTITY; NOT A GENERALIZATION THEOREM.**

A114 closes the lifted classification under the frozen analytic-tail contract. A115 asks a different question:

> Which parts of the A113/A114 mechanism are structural, and which parts are artifacts of the frozen numerical choices?

The present note deliberately starts with the compressed problem. It does **not** assume that the A114 active-set staircase survives parameter variation.

## 1. Frozen point and natural reparameterization

The frozen compressed contract uses

\[
\beta=\frac18,\qquad \tau=\frac12,
\qquad 0.129\le s\le0.133,
\]

and

\[
\varepsilon=
\begin{cases}
2^{-h}/1875,&M\text{ even},\\
2^{-h}/2500,&M\text{ odd},
\end{cases}
\qquad h=\lfloor M/2\rfloor.
\]

For a variable target node \(\tau\), the natural tail scale is

\[
U_\tau:=\tau^h.
\]

At the frozen point the dimensionless tolerance is therefore

\[
\bar\varepsilon:=\frac{\varepsilon}{U_\tau}
=
\begin{cases}
1/1875,&M\text{ even},\\
1/2500,&M\text{ odd}.
\end{cases}
\]

This suggests that a genuine local perturbation of the frozen asymptotic contract should hold \(\bar\varepsilon\) fixed, i.e.

\[
\varepsilon=\bar\varepsilon\tau^h,
\]

rather than keep the old absolute value proportional to \(2^{-h}\).

The corresponding asymptotic locator is

\[
c_\tau(s)=\frac{\log(1/\tau)}{-2\log s},
\qquad
b_\tau=\lceil M c_\tau(s)\rceil.
\]

For rational stress tests `b_tau` is found exactly as the smallest integer satisfying

\[
s^{2b}\le\tau^M,
\]

so no floating-point logarithm is used for the sign/localization decisions.

## 2. The A113 central cancellation is more general than `2 tau = 1`

A113 uses

\[
J=E_{b+1}-2E_{b+2}
\]

because \(\tau=1/2\). For a generic target node the target-affine channel satisfies identically

\[
(c+kd)\tau^k
-\tau^{-1}(c+(k+1)d)\tau^{k+1}
=-d\tau^k.
\]

Thus the structurally natural central combination is

\[
\boxed{
J_\tau:=E_{b_\tau+1}-\tau^{-1}E_{b_\tau+2}.
}
\]

The exact cancellation is symbolic and does not require \(\tau=1/2\). What remains nontrivial is the sign of the **complete** \(J_\tau\), including the other exponential channels and finite-tail corrections.

## 3. Exact tau stress: normalized versus frozen absolute tolerance

The exact compressed two-band branch was reconstructed directly from the seven linear equalities for

\[
P=\{0,k,M\},\qquad Q=\{1,h,h+1\},
\]

with `alpha+`, `beta-` active. No A113 sign certificate is imported.

The tau grid is

\[
\tau\in\{0.47,0.475,\ldots,0.53\},
\]

with \(s\in\{0.129,0.131,0.133\}\) and \(\beta=1/8\).

### 3.1 Dimensionless/co-scaled tolerance

Using

\[
\varepsilon=\bar\varepsilon\tau^h,
\]

the exact stress gives:

- **312/312** complete sequences for `M in {20,30,40,50,60,70,80,100}` with no one-variation failure;
- **312/312** with the compressed maximizer localized in `b_tau+{1,2,3}`;
- **312/312** with `J_tau>0`;
- **234/234** local tail controls for `M in {521,538,561,760,1000,1500}` with all checked factors `k<=b_tau` positive and all checked factors `k>=b_tau+3` negative;
- **234/234** local tail controls with `J_tau>0`.

These counts are finite exact evidence only.

### 3.2 Keeping the old absolute `2^-h` tolerance is not a small tail perturbation

If `tau` is changed while

\[
\varepsilon=
\begin{cases}
2^{-h}/1875,\\
2^{-h}/2500,
\end{cases}
\]

is left numerically frozen, then

\[
\frac{\varepsilon}{\tau^h}
=\bar\varepsilon\left(\frac{1/2}{\tau}\right)^h,
\]

which changes exponentially with `h` whenever `tau != 1/2`.

The exact stress then finds:

- 25 one-variation failures among the 312 complete small/medium-M controls;
- 7 failures of the `b_tau+{1,2,3}` localization;
- 17 failures of `J_tau>0`;
- 108 remote/local-sign failures among 234 tail controls;
- 74 tail failures of `J_tau>0`.

Therefore the statement “A113 is robust if tau changes while every other numerical input is frozen” is false.

### Exact tail counterexample

At

\[
M=521,\quad s=129/1000,\quad \beta=1/8,\quad \tau=49/100,
\]

with the **old absolute** tolerance proportional to `2^-h`, exact rational reconstruction gives

\[
b_\tau=91,
\]

but the compressed adjacent-factor sequence has two sign changes. In particular

\[
E_{90}<0<E_{91},
\]

while the global compressed maximizer is at

\[
k=90=b_\tau-1.
\]

The final checked factor near the right support edge is positive as well. Thus the frozen A113 one-variation/localization mechanism genuinely fails in this altered asymptotic contract. This is not a floating-point effect.

## 4. Beta variation is not unrestricted either

With `tau=1/2` and the normalized tolerance convention, an exact complete-sequence stress was run for

\[
\beta\in\{0.115,0.120,0.123,0.124,0.125,0.126,0.127,0.128\},
\]

on `M in {20,30,40,50,60,80,100}` and the three source probes.

Every one of the 21 controls for each beta through `0.127` preserves one variation, the frozen-style localization, and the central nesting test. At

\[
\beta=0.128,
\]

seven of the 21 complete sequences fail one-variation and two fail the generalized nesting inequality.

For example,

\[
M=20,\quad s=0.129,\quad \beta=0.128,\quad \tau=1/2
\]

has the exact sign pattern

\[
+,+,+,+,-,+,+
\]

across the audited adjacent factors. Hence ordering alone (`beta<s<tau`) is not sufficient for the full A113 one-variation theorem.

## 5. Joint local box: finite evidence for a realistic theorem target

A joint exact stress used

\[
\beta\in\{0.124,0.125,0.126\},
\qquad
\tau\in\{0.49,0.495,0.5,0.505,0.51\},
\]

with the normalized tolerance \(\varepsilon=\bar\varepsilon\tau^h\).

Results:

- **315/315** complete sequences for `M in {20,30,40,50,60,80,100}` preserve one variation, `b_tau+{1,2,3}` localization and `J_tau>0`;
- **225/225** local tail controls for `M in {521,538,561,760,1000}` preserve the audited remote signs and `J_tau>0`.

Again, this is not a continuum theorem. It identifies a plausible local parameter box worth proving analytically.

## 6. What appears structural versus frozen

### Exact / symbolic mechanism

The following mechanism survives immediately:

\[
E_{b+1}-2E_{b+2}
\quad\leadsto\quad
E_{b_\tau+1}-\tau^{-1}E_{b_\tau+2},
\]

because the target-affine cancellation is an identity.

The generalized locator

\[
s^{2b_\tau}\lesssim\tau^M
\]

is likewise the natural balance underlying the frozen formula.

### Strongly suggested but not proved

There is substantial exact finite evidence that the compressed one-variation mechanism persists in an open neighborhood of

\[
(\beta,\tau)=(1/8,1/2)
\]

when the dimensionless tolerance `epsilon/tau^h` is held fixed.

### Explicitly false unrestricted extensions

The current evidence refutes both of the following naive generalizations:

1. vary `tau` while retaining the old absolute `2^-h` epsilon scale and expect the same tail theorem;
2. assume `0<beta<s<tau<1` alone is enough for one variation.

## 7. Next rigorous target

The next theorem attempt should be local, not universal.

A reasonable target is to find an explicit compact box

\[
\beta\in[\beta_-,\beta_+],\qquad
\tau\in[\tau_-,\tau_+],\qquad
s\in[0.129,0.133],
\]

around `(1/8,1/2)`, with

\[
\varepsilon=\bar\varepsilon\tau^h,
\]

and prove uniformly for the analytic tail:

\[
E_k>0\ (k\le b_\tau),
\qquad
E_k<0\ (k\ge b_\tau+3),
\]

and

\[
\boxed{J_\tau>0}.
\]

Only after that compressed open-neighborhood theorem is available should the lifted A114 staircase be tested for structural stability under `gamma`, `beta`, `tau` perturbations.

## Nonclaims

This audit does **not** prove:

- an open-parameter theorem;
- persistence for arbitrary `0<beta<s<tau<1`;
- persistence of the A114 lifted staircase;
- anything about varying `gamma` yet;
- any physical or ontological interpretation.
