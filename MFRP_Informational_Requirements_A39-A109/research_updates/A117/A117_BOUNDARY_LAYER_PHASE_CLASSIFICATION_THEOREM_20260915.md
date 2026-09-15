# A117 — parity-resolved boundary-layer phase classification theorem

**Date:** 2026-09-15  
**Status:** **PROVED under the inherited A115/A116 target-deformed reduced-factor contract; independently red-teamed.**  
**Classification:** asymptotic mathematical theorem + exact phase classification of the leading `1/M` collision layer.  
**No physical or ontological interpretation is claimed.**

---

## 1. Scope

Keep the frozen structural constants

\[
\beta=\frac18,
\qquad
\delta=\frac1{1875},
\qquad
\frac{129}{1000}\le s\le\frac{133}{1000}.
\]

A115 deforms the target node from `1/2` to `tau`, and A116 proves compact-interior eventual positivity while exhibiting a nontrivial collision layer when `tau-s=O(1/M)`.

A117 studies that layer directly.

Fix

\[
\lambda>0
\]

and set

\[
\boxed{
\tau_M=s+\frac{\lambda}{M}.
}
\]

For sufficiently large `M`, the inherited A84 node order holds automatically because

\[
s\tau_M\longrightarrow s^2
\le \left(\frac{133}{1000}\right)^2
<\frac18=\beta.
\]

Set

\[
h=\left\lfloor\frac M2\right\rfloor,
\qquad
u=\tau_M^h,
\]

and keep the exact A115 scale-normalized tolerance

\[
\varepsilon_{\tau,M}
=
\begin{cases}
\delta\tau_M^h,&M=2h,\\[4pt]
\delta\dfrac{1+\tau_M}{2}\tau_M^h,&M=2h+1.
\end{cases}
\]

Let

\[
b_M
=
\left\lceil
M\frac{\log\tau_M}{2\log s}
\right\rceil,
\qquad
k_M=b_M+1,
\]

and

\[
J_M
=E_{M,k_M}(s,\tau_M)
-\tau_M^{-1}E_{M,k_M+1}(s,\tau_M).
\]

The factors are A84-admissible exactly when

\[
k_M+1\le h-2.
\]

---

# 2. Boundary coordinates and parity

Define

\[
L=-\log s>0,
\qquad
\alpha=\frac{\lambda}{2s},
\qquad
x=\frac{\alpha}{L}
=\frac{\lambda}{2s(-\log s)}.
\]

Let

\[
\sigma_p=
\begin{cases}
0,&M\text{ even},\\[3pt]
\frac12,&M\text{ odd},
\end{cases}
\]

and

\[
a_p(s)=
\begin{cases}
1,&M\text{ even},\\[3pt]
\dfrac{1+s}{2},&M\text{ odd}.
\end{cases}
\]

The half-cell shift in the odd case is structural and comes from

\[
\frac M2=h+\frac12.
\]

It is not obtained by copying the even formula.

---

# 3. Eventual contact cell, including resonances

Because

\[
\tau_M
=s\left(1+\frac{2\alpha}{M}\right),
\]

Taylor expansion gives

\[
\begin{aligned}
M\frac{\log\tau_M}{2\log s}
&=
\frac M2
-\frac{\alpha}{L}
+\frac{\alpha^2}{LM}
+O(M^{-2})\\[3pt]
&=
 h+\sigma_p-x+
\frac{\alpha^2}{LM}
+O(M^{-2}).
\end{aligned}
\]

The `1/M` correction is strictly positive.

Define

\[
\boxed{
r_p(x)
=
\left\lceil x-\sigma_p\right\rceil-1.
}
\]

Then for every fixed `s,lambda` and fixed parity, for all sufficiently large `M` of that parity,

\[
\boxed{
b_M=h-r_p(x).}
\]

This formula also resolves the resonant surfaces.

For example, in the even case, if `x=d` is exactly an integer, then

\[
M c_{\tau_M}(s)
=h-d+\frac{\alpha^2}{LM}+O(M^{-2}),
\]

so eventually

\[
b_M=h-d+1,
\qquad
r=d-1,
\]

rather than `r=d`.

Likewise, in the odd case, a resonance at

\[
x=n+\frac12
\]

belongs eventually to the preceding contact cell.

Thus a fixed deficit `r` corresponds to the half-open phase cell

\[
\boxed{
(r+\sigma_p)L
<\alpha
\le
(r+1+\sigma_p)L.
}
\]

The A84 central pair is eventually admissible iff

\[
\boxed{r\ge4.}
\]

Indeed,

\[
k_M+1
=h-r+2\le h-2
\iff r\ge4.
\]

---

# 4. Parity-unified boundary-layer limit

Define

\[
B(s)=\frac\beta s+2\delta,
\]

\[
S(\alpha)=1-e^{-\alpha}-2\delta,
\]

and normalize by

\[
N_M
=
\frac{J_M}{\tau_M^h\tau_M^{k_M}}.
\]

## Theorem A — boundary-layer limit

Fix `s`, `lambda`, one parity, and assume the eventual deficit

\[
r=r_p(x)\ge4.
\]

Then

\[
\boxed{
M N_M
\longrightarrow
\Lambda_p(s,\lambda,r),
}
\]

where

\[
\boxed{
\Lambda_p(s,\lambda,r)
=(1-s)
\left[
\frac\lambda2 s^{1-r}e^{-\alpha}
+a_p(s)\left(
B-S-B(\alpha+1)e^{-\alpha}
\right)
\right].
}
\]

Equivalently, since

\[
\frac\lambda2=\alpha s,
\]

\[
\boxed{
\frac{\Lambda_p}{1-s}
=
\alpha s^{2-r}e^{-\alpha}
+a_p(B-S)
-a_pB(\alpha+1)e^{-\alpha}.
}
\]

For even `M`, `a_p=1`, and this reduces exactly to the A116 boundary formula.

For odd `M`,

\[
\boxed{a_p(s)=\frac{1+s}{2},}
\]

which is the parity correction absent from the even theorem.

---

# 5. Derivation of the parity factor

The result follows directly from the exact A115 central-Q formulas.

Write

\[
u=\tau_M^h.
\]

For `r` in `{beta,s}`, the exact Q-response coefficient satisfies

\[
D_r
=
\begin{cases}
 r^h-u\dfrac{L_r}{D_\tau},&M=2h,\\[8pt]
 \dfrac{r^h+r^{h+1}}2
 -\dfrac{1+\tau_M}{2}u\dfrac{L_r}{D_\tau},&M=2h+1,
\end{cases}
\]

with

\[
L_r=r-hr^h+(h-1)r^{h+1},
\]

\[
D_\tau=\tau_M-hu+(h-1)\tau_Mu.
\]

Because

\[
\left(\frac{s}{\tau_M}\right)^h
\longrightarrow e^{-\alpha},
\qquad
\left(\frac{\beta}{\tau_M}\right)^h
\longrightarrow0,
\]

one obtains

\[
\frac{D_\beta}{u}
\longrightarrow
-a_p\frac\beta s,
\]

\[
\frac{D_s}{u}
\longrightarrow
 a_p(e^{-\alpha}-1),
\]

and

\[
\frac{\varepsilon_{\tau,M}}u
\longrightarrow
\delta a_p.
\]

Hence

\[
H_\beta
=
\frac12+u\,a_pB+o(u),
\]

\[
H_s
=
\frac12+u\,a_pS+o(u),
\]

while

\[
A=\frac{1+\tau_M^M}{2}
=\frac12+o(u).
\]

Now use the exact A84 coefficient identities. Uniformly in a fixed boundary cell,

\[
M c_{s\tau}\longrightarrow\frac\lambda2,
\]

\[
\frac{c_s}{u}
\longrightarrow
-a_pB(1-s),
\]

\[
\frac{M c_{ks}}{u}
\longrightarrow
 a_pB(1-s),
\]

and

\[
\frac{M c_{k\tau}}{u}
\longrightarrow
-(1-s)a_p(B-S).
\]

Furthermore,

\[
M\left(1-\frac{s}{\tau_M}\right)
\longrightarrow2\alpha,
\]

\[
k_M\left(1-\frac{s}{\tau_M}\right)
\longrightarrow\alpha,
\]

\[
\left(\frac{s}{\tau_M}\right)^{k_M}
\longrightarrow e^{-\alpha},
\]

and

\[
\frac{s^{k_M}}{u}
\longrightarrow s^{1-r}e^{-\alpha}.
\]

Therefore the source-affine contribution tends to

\[
-(1-s)a_pB(\alpha+1)e^{-\alpha},
\]

the target-slope contribution tends to

\[
(1-s)a_p(B-S),
\]

and the `s tau` product channel tends to

\[
(1-s)\frac\lambda2 s^{1-r}e^{-\alpha}.
\]

All beta channels vanish exponentially.

The constant coefficient is controlled by the exact grouping

\[
c_1
=(H_\beta-A)(a_s-a_\tau)
+(H_s-A)(a_\tau-a_\beta),
\]

because the equal-`A` part telescopes exactly. Thus in the collision layer

\[
\boxed{
c_1=O\left(\frac{u\tau_M^M}{M}\right),}
\]

which is stronger than the coarse estimate needed in A116. Its normalized contribution therefore vanishes.

Summing the three surviving channels proves Theorem A.

---

# 6. Reduced phase function

Set

\[
C(s)=1-\frac\beta s-4\delta.
\]

On the declared source window,

\[
B<1,
\qquad
C>0.
\]

For a fixed parity and contact deficit `r`, define

\[
A_p(s)=a_p(s)(1-B(s)),
\]

\[
D_{p,r}(s)=s^{2-r}-a_p(s)B(s).
\]

For every admissible `r>=4`,

\[
D_{p,r}>0.
\]

The phase function simplifies exactly to

\[
\boxed{
F_{p,r}(s,\alpha)
:=
\frac{\Lambda_p}{1-s}
=
-a_p C
+e^{-\alpha}
\left[
A_p+\alpha D_{p,r}
\right].
}
\]

Thus the entire leading collision-layer sign problem has been reduced to one affine function multiplied by one exponential.

---

# 7. Strict monotonicity inside every admissible cell

Differentiate at fixed `s,p,r`:

\[
\boxed{
\frac{\partial F_{p,r}}{\partial\alpha}
=e^{-\alpha}
\left[
D_{p,r}(1-\alpha)-A_p
\right].
}
\]

Every admissible cell has

\[
\alpha>8
\]

in the even case and

\[
\alpha>9
\]

in the odd case, because

\[
2< -\log s<\frac{21}{10}
\]

throughout the source window and `r>=4`.

Since

\[
D_{p,r}>0,
\qquad
A_p>0,
\]

we have

\[
\boxed{
\frac{\partial F_{p,r}}{\partial\alpha}<0
}
\]

throughout every admissible contact cell.

Therefore no cell can contain two phase reversals.

---

# 8. Uniform positive entry into every cell

The left endpoint of a parity cell is not included, but its one-sided limit is important.

## 8.1 Even cells

At

\[
\alpha=rL,
\]

one has

\[
F_{\rm even,r}^{\rm left}
=-C+rLs^2
+s^r\left[(1-B)-rLB\right].
\]

Using the exact source-window bounds

\[
2<L<\frac{21}{10},
\]

\[
C<\frac3{50},
\qquad
B<1,
\]

and the fact that `r s^r` decreases for `r>=4`, we obtain

\[
F_{\rm even,r}^{\rm left}
>
-\frac3{50}
+8\left(\frac{129}{1000}\right)^2
-\frac{42}{5}\left(\frac{133}{1000}\right)^4.
\]

The exact rational margin is

\[
\boxed{
\frac{176249084859}{2500000000000}>0.
}
\]

Hence every even cell is entered from the positive side.

## 8.2 Odd cells

At

\[
\alpha=\left(r+\frac12\right)L,
\]

one has

\[
F_{\rm odd,r}^{\rm left}
=-a_pC
+\left(r+\frac12\right)Ls^{5/2}
+a_p s^{r+1/2}
\left[(1-B)-\left(r+\frac12\right)LB\right].
\]

Use

\[
\frac{359}{1000}<\sqrt{\frac{129}{1000}},
\qquad
\sqrt{\frac{133}{1000}}<\frac{365}{1000},
\]

\[
a_p\le\frac{567}{1000},
\]

and the fact that

\[
\left(r+\frac12\right)s^{r+1/2}
\]

decreases for `r>=4`.

Then

\[
F_{\rm odd,r}^{\rm left}
>
-\frac{567}{1000}\frac3{50}
+9\left(\frac{129}{1000}\right)^2\frac{359}{1000}
-\frac{567}{1000}\frac92\frac{21}{10}
\left(\frac{133}{1000}\right)^4\frac{365}{1000}.
\]

The exact margin is

\[
\boxed{
\frac{76540493262589821}
{4000000000000000000}>0.
}
\]

Hence every odd cell is also entered from the positive side.

---

# 9. Theorem B — one-crossing phase classification

Fix `s`, parity `p`, and an admissible deficit `r>=4`. The phase cell is

\[
\mathcal I_{p,r}(s)
=
\left(
(r+\sigma_p)L,
(r+1+\sigma_p)L
\right].
\]

Let

\[
R_{p,r}(s)
=
F_{p,r}
\left(
 s,(r+1+\sigma_p)L
\right).
\]

Then exactly one of the following occurs.

### Phase P — entirely positive cell

If

\[
R_{p,r}(s)>0,
\]

then

\[
\boxed{
F_{p,r}(s,\alpha)>0
\quad
\text{for every }\alpha\in\mathcal I_{p,r}(s).
}
\]

Consequently

\[
J_M>0
\]

eventually for every fixed boundary sequence in that cell.

### Phase C — critical endpoint

If

\[
R_{p,r}(s)=0,
\]

then the leading boundary-layer limit is positive throughout the open part of the cell and vanishes only at the included resonant endpoint.

The sign of finite `J_M` on that critical sequence requires the next asymptotic order and is **not** classified by A117.

### Phase M — mixed cell

If

\[
R_{p,r}(s)<0,
\]

then there exists a unique

\[
\alpha_{p,r}^*(s)
\in
\mathcal I_{p,r}(s)
\]

such that

\[
F_{p,r}(s,\alpha)>0
\quad\text{for}\quad
\alpha<\alpha_{p,r}^*(s),
\]

\[
F_{p,r}(s,\alpha_{p,r}^*)=0,
\]

and

\[
F_{p,r}(s,\alpha)<0
\quad\text{for}\quad
\alpha>\alpha_{p,r}^*(s).
\]

Thus each admissible contact cell has **at most one** positive-to-negative phase transition.

---

# 10. Explicit critical phase via Lambert W

Let

\[
C_p=a_pC,
\qquad
A_p=a_p(1-B),
\qquad
D=D_{p,r}.
\]

The critical equation is

\[
A_p+\alpha D=C_p e^\alpha.
\]

Its unique admissible large positive root can be written

\[
\boxed{
\alpha_{p,r}^*(s)
=
-W_{-1}\!\left(
-\frac{C_p}{D}
\exp\left[-\frac{A_p}{D}\right]
\right)
-\frac{A_p}{D}.
}
\]

The `W_{-1}` branch is the relevant branch because the admissible collision cells lie at `alpha>8` while the principal branch corresponds to the small root structure outside the admissible phase range.

The Lambert representation is not needed for the proof of existence or uniqueness; monotonicity already supplies both.

---

# 11. Only finitely many mixed/negative cells occur

At the right edge of a cell,

\[
\alpha=(r+1+\sigma_p)L,
\]

so

\[
e^{-\alpha}=s^{r+1+\sigma_p}.
\]

Therefore

\[
\begin{aligned}
R_{p,r}(s)
={}&-a_pC
+(r+1+\sigma_p)Ls^{3+\sigma_p}\\
&+a_p s^{r+1+\sigma_p}
\left[
1-B-(r+1+\sigma_p)LB
\right].
\end{aligned}
\]

The last term decays exponentially in `r`, while

\[
(r+1+\sigma_p)Ls^{3+\sigma_p}
\]

grows linearly.

Hence

\[
\boxed{
R_{p,r}(s)\longrightarrow+\infty
\quad(r\to\infty).
}
\]

The convergence is uniform for

\[
\frac{129}{1000}\le s\le\frac{133}{1000}
\]

because this source interval is compact and bounded away from both zero and one.

Consequently there exists a finite `r_0`, uniform over the frozen source window and both parities, such that every contact cell with

\[
r\ge r_0
\]

is entirely positive.

Thus the boundary layer cannot contain an infinite cascade of alternating negative phases at increasing contact deficit.

---

# 12. Finite exact regression

The accompanying standalone audit uses only exact `Fraction` arithmetic for the reduced factors and rational Taylor bounds for the sign of the limiting phase function.

Eight parity-resolved controls are checked at `M=2000` or `M=2001`. They include:

- even negative phases;
- even positive phases;
- odd negative phases;
- odd positive phases;
- all three source probes.

For all eight controls:

1. the finite factor sign is computed exactly;
2. the corresponding limiting phase sign is certified by rational upper/lower bounds on `exp(alpha)`;
3. the two signs agree.

These controls are regression/falsification evidence only and are not premises of Theorems A or B.

---

# 13. Preserved numerical warning

During exploratory work, insufficient arbitrary precision produced false zeroes and at least one false finite sign in very deep odd-parity cells because individual terms are exponentially tiny and strongly cancel.

Those calculations were discarded.

All promoted finite signs in A117 use exact `Fraction` arithmetic. The phase-limit signs in the audit use rational Taylor enclosures rather than floating-point sign decisions.

---

# 14. What A117 establishes

1. The A116 boundary layer has a parity-resolved exact leading limit.
2. Odd supports are shifted by one half-cell and carry the factor `(1+s)/2`.
3. Resonant contact surfaces are assigned by the positive second-order ceiling correction.
4. Every admissible contact cell is entered with strictly positive leading sign.
5. The phase function is strictly decreasing inside each cell.
6. Therefore each cell is either entirely positive, endpoint-critical, or has exactly one positive-to-negative transition.
7. The critical transition has an explicit `W_{-1}` representation.
8. Only finitely many mixed/negative contact cells can occur; sufficiently deep contact deficits are uniformly positive over the frozen source window.

---

# 15. Nonclaims

A117 does **not** establish:

- the next-order sign when `Lambda_p=0` exactly;
- a closed elementary expression for the smallest uniform all-positive contact deficit;
- a finite minimal `M` at which the asymptotic sign is already realized;
- a target-deformed A114 lifted active-set staircase;
- any relation to RZS, a modal field, spacetime, gravity, matter, or physical observables.

The result is a theorem about the inherited reduced exponential-moment optimization contract only.
