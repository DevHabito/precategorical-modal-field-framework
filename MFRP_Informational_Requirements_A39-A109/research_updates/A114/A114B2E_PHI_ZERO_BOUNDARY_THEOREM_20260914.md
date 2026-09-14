# A114-B2-E — outer `Phi=0` boundary theorem in the strict compressed `b+2` phase

## Status

**PROVED conditional boundary theorem under the frozen analytic-tail contract, subject to the analytic certificate and logical audit packaged with this result.**

This theorem addresses the outer zero-pivot set that remained open after A114-B2-D. It does **not** import the distinct A114-B1 `b+1` zero-pivot result.

Let

\[
M\ge521,\qquad \frac{129}{1000}\le s\le\frac{133}{1000},
\qquad h=\lfloor M/2\rfloor,
\]

\[
b=\left\lceil\frac{M\log2}{-2\log s}\right\rceil,
\qquad j=b+2,
\qquad U=2^{-h},
\]

and assume `j=b+2` is the **strict compressed maximizer**. Define

\[
\Phi=F_j^{\rm up}=F_{b+2}^{\rm up}.
\]

Assume

\[
\boxed{\Phi=0}.
\]

Use the compressed two-band basis

\[
C:\qquad P=\{0,j,M\},\qquad Q=\{1,h,h+1\},
\]

with `alpha+`, `beta-` active and gamma inactive, and the adjacent gamma-plus basis

\[
G^+:\qquad P=\{0,j,j+1,M\},\qquad Q=\{1,h,h+1\},
\]

with `alpha+`, `beta-`, `gamma+` active.

---

# Theorem

Under the contract above:

1. the C basis has
   \[
   p_0^C>0,
   \]
   and every other C basic mass and `t` is strictly positive;
2. both active C multipliers are strictly positive;
3. every nonbasic P and Q reduced cost of C is strictly positive;
4. the inactive gamma-minus slack is strictly positive;
5. the inactive gamma-plus slack is exactly zero:
   \[
   \boxed{S_{\gamma+}^C=0};
   \]
6. consequently C is a global optimum and the **primal optimum is unique**;
7. the adjacent gamma-plus basis has
   \[
   p_{j+1}^{G^+}=0,
   \qquad p_j^{G^+}>0,
   \]
   and collapses to the same primal point as C after deletion of the zero pivot coordinate.

Thus `Phi=0` is a genuine degenerate C/G+ transition, but it does **not** create a nontrivial primal optimal face.

In compact form,

\[
\boxed{
\text{strict compressed }b+2,\ \Phi=0
\Longrightarrow
\text{unique primal optimum with degenerate }C/G^+\text{ coalescence}.}
\]

---

# Proof

## 1. The dyadic gate extends to `Phi=0`

A114-B2-B was stated for `Phi<0`, but its first contradiction proves the stronger implication

\[
3j-h\le12
\Longrightarrow
\Phi>1.0392\times10^{-6}>0.
\]

Therefore its contrapositive gives, without continuity,

\[
\boxed{\Phi\le0\Longrightarrow3j-h\ge13}.
\]

In particular this holds on `Phi=0`, so

\[
\frac{\beta^j}{U}=2^{h-3j}\le2^{-13}.
\]

The standalone B2-E certificate independently recomputes the exact rational lower margin behind this implication.

## 2. The B2 source box also holds on the equality set

The lower source bound used in C1/C2 does not use the sign of `Phi`: strict compressed `b+2` gives

\[
E_{b+1}>0,
\]

while the A113 exact majorant would force `E_(b+1)<0` if

\[
\frac{s^{j-1}}U\le\frac9{1000}.
\]

Hence

\[
\frac{s^{j-1}}U>\frac9{1000}.
\]

For the upper bound, the dyadic gate from Step 1 is exactly the only `Phi`-dependent input in the previous source-box argument. Reusing the audited A112-A bridge gives

\[
\frac{s^{j-1}}U
<0.0320622107\ldots
<\frac1{25}.
\]

Therefore the complete source box is valid at equality:

\[
\boxed{
\frac9{1000}<Q:=\frac{s^{j-1}}U<\frac1{25}.}
\]

## 3. `Phi=0` makes the C gamma-plus slack exactly zero

A112-A gives for the adjacent gamma-plus basis

\[
p_{j+1}^{G^+}=\frac{\Phi}{D_G}.
\]

A114-B1 proves independently on the complete localization strip that

\[
D_G>0.
\]

Hence

\[
\Phi=0\Longrightarrow p_{j+1}^{G^+}=0.
\]

C2 proves the exact bordered-pivot identity

\[
p_{j+1}^{G^+}
=-S_{\gamma+}^C\frac{\det B_C}{\det B_{G^+}}.
\]

Once the equality-set source box is available, the C2 neighboring-determinant estimate gives

\[
\det B_C>0,
\]

while A114-B1 gives the nonzero positive gamma-plus determinant orientation. Thus

\[
\boxed{S_{\gamma+}^C=0}.
\]

No limiting argument is used.

## 4. The equality cannot coincide with `p0^C=0`

Write the C transform reduction as

\[
P_r=A_rp_0+T_rt,
\qquad
Q_r=C_r+D_rt.
\]

The beta-minus equality is

\[
A_\beta p_0+K_\beta t=C_\beta,
\qquad
K_\beta=T_\beta-D_\beta+2\varepsilon.
\]

Define

\[
K_{\gamma+}=T_\gamma-D_\gamma-2\varepsilon.
\]

The gamma-plus slack is

\[
S_{\gamma+}^C
=C_\gamma-A_\gamma p_0-K_{\gamma+}t.
\]

Eliminating `t` with the beta-minus equation gives the exact identity

\[
\boxed{
S_{\gamma+}^C
=\frac{B_0-B_1p_0}{K_\beta},}
\]

where

\[
B_0=C_\gamma K_\beta-K_{\gamma+}C_\beta,
\]

\[
B_1=A_\gamma K_\beta-K_{\gamma+}A_\beta.
\]

The B2-E analytic certificate uses the inherited exact rational coefficient envelopes and proves uniformly

\[
K_\beta>0,
\qquad B_0>0,
\qquad B_1>0.
\]

The weakest parity margins are

\[
B_0>2.81446\times10^{-4},
\qquad
B_1>9.49944\times10^{-2}.
\]

Since `S_(gamma+)^C=0`,

\[
\boxed{p_0^C=\frac{B_0}{B_1}>0}.
\]

The certificate gives the explicit uniform lower bound

\[
\boxed{p_0^C>2.9407\times10^{-3}}.
\]

Thus the surfaces `Phi=0` and `p0^C=0` do not intersect anywhere in the frozen tail contract.

## 5. All remaining C KKT gates are strict

The C2 proof can now be reused only after checking which of its steps actually depended on `Phi<0`.

After the source box and `p0^C>0` are established, C2 Sections 3--5 and 7--8 prove, without any further use of the sign of `Phi`, that:

- `t,p_j,p_M,q_1,q_h,q_(h+1)>0`;
- the active alpha/beta multipliers are strictly positive;
- `S_(gamma-)^C>0`;
- every nonbasic P reduced cost is strictly positive;
- every nonbasic Q reduced cost is strictly positive;
- the opposite alpha/beta slacks are strictly positive.

The only C2 step where `Phi<0` was used after the source box was Section 6, whose purpose was precisely to prove

\[
S_{\gamma+}^C>0.
\]

At the present equality set, Step 3 replaces that strict gate by the exact and correct boundary value

\[
S_{\gamma+}^C=0.
\]

Hence C satisfies the complete non-strict KKT system with exactly one lost strict slack gate.

## 6. The primal optimum is unique

Fix the C dual optimum. Every nonbasic P/Q reduced cost is strictly positive. Therefore zero primal-dual gap forces every alternative primal optimum to use only the C primal support

\[
P=\{0,j,M\},\qquad Q=\{1,h,h+1\}.
\]

The positive active alpha/beta multipliers force those two inequalities to remain saturated at any optimum. On this support the normalization, mean, target, alpha and beta equalities are exactly the nonsingular C basis system. Hence there is only one primal solution.

The fact that the inactive gamma-plus inequality is tight does not create a primal direction: its C-dual multiplier is zero, while the variable reduced costs remain strict.

Therefore the primal optimum is unique.

## 7. C and G+ are two degenerate representations of the same point

At `Phi=0`, A112-A gives

\[
p_{j+1}^{G^+}=0.
\]

The uniform upper-boundary barrier gives

\[
F_{j+1}^{\rm up}=F_{b+3}^{\rm up}<0,
\]

so

\[
p_j^{G^+}=-\frac{F_{b+3}^{\rm up}}{D_G}>0.
\]

After deleting the zero `p_(j+1)` coordinate, G+ has the same primal support as C. The C point also satisfies the gamma-plus equality because `S_(gamma+)^C=0`. Therefore both systems contain the same common equations on the same common support. Nonsingularity of C forces the remaining primal coordinates to coincide.

Thus

\[
\boxed{C=G^+\quad\text{as primal points at }\Phi=0.}
\]

No claim of a unique optimal basis or strict complementarity is made.

---

# Consequence for A114-B2

Together with A114-B2-A, C1, C2, C3 and D, the strict compressed `b+2` phase is now classified throughout the frozen source window:

- `Phi>0` -> unique strict gamma-plus optimum at contact `b+2`;
- `Phi=0` -> unique primal optimum, degenerate C/G+ coalescence;
- `Phi<0` -> C/E/QI/QA classification, including the D equality sets.

This is a classification of the declared finite lifted LP under the frozen analytic-tail contract. It is not a physical statement and it is not an extension outside the source window.

# Nonclaims

This theorem does not claim:

- strict complementarity at `Phi=0`;
- uniqueness of the optimal basis at `Phi=0`;
- a universal monotone ordering of all discriminant zeros in `s`;
- anything outside `M>=521` and `129/1000<=s<=133/1000`;
- any physical, spacetime, quantum, gravitational or ontological interpretation.

Finite near-boundary controls, if supplied, are regression/falsification evidence only and are not premises of this proof.
