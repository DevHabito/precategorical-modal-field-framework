# A114-C2 — `b+2 / b+3` compressed-tie theorem on the analytic tail

## Status

**STAGING THEOREM — analytic proof assembled from promoted A112/A113/A114 identities and the new exact `Phi>0` boundary certificate; pending independent red-team before promotion.**

Let

\[
M\ge521,\qquad 129/1000\le s\le133/1000,
\qquad h=\lfloor M/2\rfloor,
\]

\[
b=\left\lceil\frac{M\log2}{-2\log s}\right\rceil,
\qquad j=b+2,
\qquad U=2^{-h},
\]

and assume the second central compressed boundary

\[
\boxed{E_j=E_{b+2}=0}.
\]

Define

\[
\Phi:=F_j^{\rm up}=F_{b+2}^{\rm up}.
\]

Use

\[
G_2^+:\quad P=\{0,j,j+1,M\},\qquad Q=\{1,h,h+1\},
\]

with `alpha+`, `beta-`, `gamma+` active, and

\[
ER_3:\quad P=\{j,j+1,M\},\qquad Q=\{1,h,h+1\},
\]

with `alpha+`, `beta-` active and gamma inactive.

---

# Theorem

Under the frozen tail contract and `E_(b+2)=0`:

1. the compressed maximizers are exactly `b+2` and `b+3`;
2. the upper gamma pivot is uniformly positive,
   \[
   \boxed{\Phi>0};
   \]
3. `G_2^+` is a global KKT optimum with every primal basic variable, every nonbasic P/Q reduced cost, both alpha/beta multipliers and all opposite slacks strict, while
   \[
   \boxed{y_\gamma^{G_2^+}=0};
   \]
4. `ER_3` is primal feasible with all of its masses and both inactive gamma slacks strictly positive;
5. the complete primal optimal set is exactly
   \[
   \boxed{\operatorname{Opt}=\operatorname{conv}\{G_2^+,ER_3\}}.
   \]

Thus the second compressed tie creates a genuine one-dimensional optimal face joining the gamma-plus `b+2` lift to the endpoint-released `b+3` lift.

---

# Proof

## 1. The compressed tie is exactly `b+2 / b+3`

A113 proves

\[
E_{b+1}-2E_{b+2}>0.
\]

At `E_(b+2)=0`,

\[
\boxed{E_{b+1}>0}.
\]

A113 also gives

\[
E_k<0\qquad(k\ge b+3).
\]

Hence `b+2` and `b+3` are exactly the two compressed maximizers. There is no triple compressed tie.

## 2. The tie forces a quantitative source ratio

Set

\[
R=\frac{s^j}{U}=\frac{s^{b+2}}U.
\]

The promoted A114-A proof established the strict implication

\[
R\le\frac9{1000}
\Longrightarrow
\frac{E_{b+2}}{U\tau^{b+2}}
<-5.71066\times10^{-5}<0.
\]

Therefore equality `E_(b+2)=0` forces

\[
\boxed{R>9/1000}.
\]

This is a direct contrapositive of an already-proved strict upper bound; no limiting argument is used.

Also, because `b=ceil(Mc(s))`,

\[
s^b\le s^{Mc(s)}=2^{-M/2}\le U,
\]

and hence

\[
R=\frac{s^{b+2}}U\le s^2\le (133/1000)^2<0.018.
\]

The frozen tail localization gives

\[
j=b+2\ge91.
\]

## 3. `Phi>0` on the complete tie surface

Write

\[
Y=\frac{\beta^j}{U}
=R\left(\frac\beta s\right)^j.
\]

Since `beta=1/8`, `s>=129/1000` and `j>=91`,

\[
Y\le R\left(\frac{125}{129}\right)^{91}.
\]

The standalone A114-C2 certificate reconstructs the exact A81 upper-gamma boundary polynomial and separates exponentially tiny high-node tails from the common-denominator core.

Let

\[
a=1-\frac jM,
\qquad e=\frac\varepsilon U,
\qquad d=1-(h+1)U.
\]

After retaining the exact common Q-block denominator, the core identity is

\[
\frac{\Phi_0}{U}
=
\frac{1}{d}\Big[
R(\beta-\gamma)-Y(s-\gamma)-8ae(s-\gamma)
-4UeR(\beta+\gamma)+4UeY(s-\gamma)
\Big].
\]

The parity coefficient in the Q-block cancels identically from this expression.

The omitted normalized primitives are bounded uniformly by `1e-28`; the six triple products making up `Phi` therefore contribute aggregate normalized error below `1e-26`.

Using

\[
R>9/1000,
\quad R<(133/1000)^2,
\quad a<1,
\quad e\le1/1875,
\]

and dropping the final positive term gives the exact conservative lower bound

\[
\frac{\Phi}{U}
>
\frac9{1000}
\left[
(\beta-\gamma)
-(133/1000-\gamma)\left(\frac{125}{129}\right)^{91}
\right]
-
\frac{8}{1875}(133/1000-\gamma)
-
10^{-26}.
\]

The certificate evaluates this rational expression as

\[
\boxed{
\frac{\Phi}{U}>2.25594\times10^{-4}>0.}
\]

Hence

\[
\boxed{\Phi>0}.
\]

This proof does not use the false shortcut `3j-h<=12`; that rejected route and exact counterexamples are preserved in `A114C2_CORRECTIONS_AND_DEAD_ENDS_20260914.md`.

## 4. `G_2^+` is an equality-set KKT optimum

A112-A gives

\[
p_{j+1}^{G_2^+}=\frac{\Phi}{D_G}>0,
\]

because A114-B1 proves `D_G>0` independently of primal positivity. The upper boundary barrier gives

\[
p_j^{G_2^+}=-\frac{F_{j+1}^{\rm up}}{D_G}>0.
\]

Thus both adjacent P masses are strict.

A112-B/C/E/G and the pointwise Descartes argument depend on adjacent positivity and localization, but not on a strict sign of `E_j`. They therefore give:

- every basic primal mass and `t` strictly positive;
- every nonbasic P reduced cost strictly positive;
- every nonbasic Q reduced cost strictly positive;
- every opposite inactive slack strictly positive.

A112-D gives exactly

\[
N_\gamma=-\frac{\det B}{D_G}E_j,
\]

so on the tie

\[
\boxed{y_\gamma=0}.
\]

It remains to protect alpha and beta without continuity. With `y_gamma=0`, the P dual equations interpolate `tau^x` in

\[
\operatorname{span}\{1,x,\beta^x,s^x\}
\]

on the ordered nodes

\[
0<j<j+1<M.
\]

The same generalized-Vandermonde/Wronskian argument independently certified in A114-C1 gives

\[
y_\alpha>0,
\qquad y_\beta>0.
\]

Therefore `G_2^+` satisfies the complete non-strict KKT system, with the gamma multiplier as the only lost strict dual gate.

## 5. The optimal set has at most one affine dimension

Fix the `G_2^+` dual optimum. Every nonbasic P/Q variable has strictly positive reduced cost. Therefore every alternative primal optimum uses only the `G_2^+` primal support.

Because `y_alpha,y_beta>0`, every optimum must keep alpha+ and beta- saturated. Because `y_gamma=0`, gamma+ may be released.

The `G_2^+` support contains eight primal variables including `t`. Dropping the gamma+ equality leaves seven independent equality rows: row independence follows because restoring gamma+ gives the already-proved nonsingular eight-by-eight `G_2^+` basis.

Thus the entire primal optimal set is contained in one affine line.

## 6. `ER_3` is the opposite feasible endpoint

The quantitative source inequality needed by A114-A's endpoint primal proof is exactly

\[
R>9/1000,
\]

which was re-established on the tie in Step 2.

Inspecting the promoted A114-A dependency DAG, the strict sign `E_(b+2)>0` was used to obtain that source bound and, separately, to make the endpoint reduced cost `r_{ER_3}(p_0)` strict. The endpoint primal signs and the two inactive gamma-slack margins are consequences of the source bound and frozen tail envelopes themselves.

Hence on `E_(b+2)=0`, the `ER_3` point still has

- `p_j,p_(j+1),p_M>0`;
- `q_1,q_h,q_(h+1)>0`;
- `t>0`;
- both inactive gamma slacks strictly positive.

It satisfies the same normalization, mean, target, alpha+ and beta- equalities as the `G_2^+` affine line and is characterized on that line by

\[
p_0=0.
\]

Because all columns used by `ER_3` are `G_2^+` basic columns and the only released active row has multiplier zero, the `G_2^+` dual gives zero gap at `ER_3`. Thus `ER_3` is also globally optimal.

## 7. The complete face is exactly `conv{G2+,ER3}`

At `G_2^+`, gamma+ is saturated and the opposite gamma slack is

\[
4\varepsilon t>0.
\]

At `ER_3`, both gamma slacks are strictly positive. All primal coordinates and inactive slacks are affine along the one-dimensional alpha+/beta- line. Therefore every point in

\[
\operatorname{conv}\{G_2^+,ER_3\}
\]

is primal feasible and optimal.

The line cannot continue past `ER_3`: the defining coordinate `p_0` becomes negative.

It cannot continue through `G_2^+` in the opposite direction: gamma+ slack is zero at `G_2^+` and strictly positive at `ER_3`, so affine continuation away from `ER_3` through `G_2^+` makes gamma+ slack negative.

Since Step 5 excluded every other zero-cost direction, the displayed segment is the entire primal optimal set.

Hence

\[
\boxed{\operatorname{Opt}=\operatorname{conv}\{G_2^+,ER_3\}}.
\]

---

# Independent regression

A standalone `Fraction` implementation brackets the tie in two adversarial cells:

- odd `M=525`, `d=11`;
- even `M=760`, `d=13`.

On the `E_(b+2)<0` side, `G_2^+` passes the complete unused-atom KKT scan. On the `E_(b+2)>0` side, `ER_3` passes the complete scan. `Phi` is positive on all four exact rational bracket endpoints.

The regression reports **12/12 PASS**. It is falsification/transcription evidence only and is not a premise of the equality theorem.

---

# Nonclaims

This theorem does not claim:

- anything outside `M>=521`, `129/1000<=s<=133/1000`;
- a monotone ordering in `s` of every lifted discriminant;
- that the false dyadic shortcut recorded in the corrections note is valid;
- any physical or ontological interpretation.

Together with A114-C1, this theorem would close both non-strict compressed-tie surfaces in the frozen analytic tail, subject to independent red-team and promotion.