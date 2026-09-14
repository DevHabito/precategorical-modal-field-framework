# A114-C1 — `b+1 / b+2` compressed-tie theorem on the analytic tail

## Status

**STAGING THEOREM — analytic proof assembled from promoted A112/A113/A114 identities; pending independent red-team before promotion.**

This note treats the first non-strict compressed boundary left open after A114-B2-E.

Let

\[
M\ge521,\qquad 129/1000\le s\le133/1000,
\qquad h=\lfloor M/2\rfloor,
\]

\[
b=\left\lceil\frac{M\log2}{-2\log s}\right\rceil,
\qquad j=b+2,
\]

and assume

\[
\boxed{E_{b+1}=0}.
\]

Write

\[
\Phi=F_{b+2}^{\rm up}.
\]

Use the architectures

\[
G_1^+:\ P=\{0,b+1,b+2,M\},\quad Q=\{1,h,h+1\},
\]

\[
G_2^+:\ P=\{0,b+2,b+3,M\},\quad Q=\{1,h,h+1\},
\]

both with `alpha+`, `beta-`, `gamma+` active, and

\[
C:\ P=\{0,b+2,M\},\quad Q=\{1,h,h+1\},
\]

\[
E:\ P=\{b+1,b+2,M\},\quad Q=\{1,h,h+1\},
\]

with `alpha+`, `beta-` active and gamma inactive.

---

# Theorem

A113 implies immediately

\[
E_{b+2}<0,
\]

so the compressed optimum is tied exactly between `b+1` and `b+2`; there is no triple tie with `b+3`.

The lifted optimum is then classified by `Phi` and, on the negative-`Phi` side, by the sign of `p_0^C`.

## C1-A. `Phi>0`

If

\[
\boxed{\Phi>0},
\]

then `G_2^+` satisfies the complete **strict** KKT system and is the unique strict global optimum.

Thus the compressed tie need not produce any lifted degeneracy.

## C1-B. `Phi=0`

If

\[
\boxed{\Phi=0},
\]

then the three representations `C`, `G_1^+`, and `G_2^+` collapse to the same primal point after deletion of their zero pivot coordinates. The primal optimum is unique, although the basis/active-set representation is degenerate.

## C1-C. `Phi<0`

If

\[
\boxed{\Phi<0},
\]

then `G_1^+` is a global KKT optimum with all primal masses, all variable reduced costs, the alpha/beta multipliers and all opposite slacks strict, while

\[
\boxed{y_\gamma^{G_1^+}=0}.
\]

Consequently the complete primal optimal set is one-dimensional. Its second endpoint is selected by the sign of the compressed two-band endpoint mass `p_0^C`:

\[
\boxed{
\begin{array}{rcl}
p_0^C>0 &\Rightarrow& \operatorname{Opt}=\operatorname{conv}\{G_1^+,C\},\\[3pt]
p_0^C=0 &\Rightarrow& \operatorname{Opt}=\operatorname{conv}\{G_1^+,C=E\},\\[3pt]
p_0^C<0 &\Rightarrow& \operatorname{Opt}=\operatorname{conv}\{G_1^+,E\}.
\end{array}}
\]

In particular the QI/QA architectures do not create an additional optimal direction on this compressed-tie surface.

---

# Proof

## 1. A113 rules out a triple compressed tie

A113 proves

\[
E_{b+1}-2E_{b+2}>0.
\]

At `E_(b+1)=0`,

\[
-2E_{b+2}>0,
\]

hence

\[
\boxed{E_{b+2}<0}.
\]

Together with the A113 remote signs this means that `b+1` and `b+2` are exactly the two compressed maximizers.

## 2. `Phi>0` gives strict `G_2^+`

At contact `j=b+2`, A112-A gives

\[
p_{b+3}^{G_2^+}=\frac{\Phi}{D_G}>0,
\]

while the upper barrier gives

\[
p_{b+2}^{G_2^+}=-\frac{F_{b+3}^{\rm up}}{D_G}>0.
\]

A114-B1 proves `D_G>0` independently of adjacent primal positivity. Step 1 gives `E_(b+2)<0`.

The minimal A112 composition lemma therefore applies: adjacent positivity plus `E_j<0` closes every strict KKT gate for the fixed gamma-plus contact, without requiring `E_(j-1)>0` or a strict compressed maximizer at `j`.

Thus `G_2^+` is the unique strict global optimum.

## 3. A gamma-zero dual lemma

The difficult negative-`Phi` tie uses contact `b+1`. Because `Phi<0`, A112-A gives both adjacent masses strictly positive:

\[
p_{b+1}^{G_1^+}=-\frac{\Phi}{D_G}>0,
\qquad
p_{b+2}^{G_1^+}=\frac{F_{b+1}^{\rm up}}{D_G}>0.
\]

A112-B/C/E/G and the pointwise Descartes argument therefore give, without using the sign of `E_(b+1)`:

- every basic primal variable and `t` strictly positive;
- every nonbasic P/Q reduced cost strictly positive;
- all opposite inactive slacks strictly positive.

A112-D gives the exact multiplier identity

\[
N_\gamma=-\frac{\det B}{D_G}E_{b+1}.
\]

Therefore

\[
\boxed{y_\gamma=0}.
\]

It remains to protect alpha and beta at equality rather than infer them by continuity.

On the four P nodes

\[
0<b+1<b+2<M,
\]

the P dual equations with `y_gamma=0` interpolate `tau^x` in

\[
\operatorname{span}\{1,x,\beta^x,s^x\}.
\]

For `0<a<b<1`, the Wronskian of

\[
\{1,x,a^x,b^x\}
\]

is

\[
(\log a)^2(\log b)^2\bigl(\log b-\log a\bigr)(ab)^x>0.
\]

Hence every ordered generalized-Vandermonde collocation determinant has the same positive orientation. Cramer's rule then gives

\[
y_\alpha=
\frac{\det[1,x,\beta^x,\tau^x]}
     {\det[1,x,\beta^x,s^x]}>0,
\]

and, since the beta coefficient in the dual interpolation is `-y_beta`,

\[
-y_\beta=
\frac{\det[1,x,\tau^x,s^x]}
     {\det[1,x,\beta^x,s^x]}
=-\frac{\det[1,x,s^x,\tau^x]}
        {\det[1,x,\beta^x,s^x]}<0.
\]

Thus

\[
\boxed{y_\alpha>0,\qquad y_\beta>0,\qquad y_\gamma=0}.
\]

This is an equality-set proof, not a limiting argument.

## 4. The optimal set for `Phi<0` is exactly one affine line segment

Fix the `G_1^+` dual optimum from Step 3. Every nonbasic primal variable has strictly positive reduced cost. Therefore every alternative primal optimum uses only the `G_1^+` primal support.

Because `y_alpha,y_beta>0`, every optimum must keep alpha+ and beta- saturated. Since `y_gamma=0`, gamma+ need not remain saturated.

On the eight variables consisting of the four `G_1^+` P masses, the three central-Q masses and `t`, the two normalizations, two mean equations, target equation, alpha+ equality and beta- equality have rank seven. Rank seven follows because adding the gamma+ row gives the already-proved nonsingular `G_1^+` basis.

Hence the entire optimal set is contained in one affine line. At `G_1^+`, gamma+ is tight and the opposite gamma slack equals `4 epsilon t>0`.

The other feasible endpoint is determined by endpoint release.

## 5. The source box extends to the tie when `Phi<0`

For `j=b+2`, the C1/C2 lower source-box proof establishes the strict implication

\[
Q:=s^{j-1}/U\le9/1000\Longrightarrow E_{b+1}<0.
\]

Therefore `E_(b+1)=0` also forces

\[
Q>9/1000.
\]

The upper source-box proof uses only `Phi<0`, via the already-proved dyadic separation, and remains unchanged. Thus

\[
\boxed{9/1000<Q<1/25}
\]

holds on the present equality surface.

Consequently all C1/C2 protected primal and inactive-slack gates that depend only on this source box remain valid at the tie.

## 6. Endpoint selection by `p_0^C`

### `p_0^C>0`

The C solution is primal feasible; all of its nonzero masses and both gamma slacks are strict under the equality-set source box and `Phi<0`. It lies on the same alpha+/beta- affine line and is characterized there by

\[
p_{b+1}=0.
\]

The segment `conv{G_1^+,C}` is feasible because all primal coordinates and inactive slacks are affine and nonnegative at both endpoints. Beyond C on this line, `p_(b+1)` becomes negative. Since `S_(gamma+)` is zero at `G_1^+` and strictly positive at C, the affine continuation through `G_1^+` in the direction opposite C makes `S_(gamma+)<0`. Thus the feasible line cannot extend past either endpoint.

### `p_0^C<0`

The exact C/E exchange identity gives

\[
\operatorname{sgn}p_{b+1}^E=-\operatorname{sgn}p_0^C,
\]

so `p_(b+1)^E>0`. The C1 protected endpoint certificate gives all other E masses and both gamma slacks strictly positive under the same source box. E lies on the alpha+/beta- line and is characterized by

\[
p_0=0.
\]

Thus `conv{G_1^+,E}` is feasible, and extension beyond E makes `p_0<0`. Since `S_(gamma+)` is zero at `G_1^+` and strictly positive at E, continuation through `G_1^+` away from E makes the gamma-plus slack negative. Again no extension beyond either endpoint is feasible.

### `p_0^C=0`

The exact exchange/coalescence identities give

\[
C=E
\]

as primal points after their zero endpoint coordinates are removed. The common endpoint has strict positive gamma-plus slack because `Phi<0`. Therefore the same affine-slack argument blocks continuation past `G_1^+`, while endpoint nonnegativity blocks continuation past `C=E`. Hence

\[
\operatorname{Opt}=\operatorname{conv}\{G_1^+,C=E\}.
\]

This proves C1-C.

## 7. The codimension-two case `Phi=0`

At `Phi=0`, the source-box lower bound again follows from `E_(b+1)=0`; the B2-E dyadic argument for `Phi<=0` supplies the upper bound. The B2-E gamma-zero elimination then gives

\[
\boxed{p_0^C>0}.
\]

A112-A gives

\[
p_{b+1}^{G_1^+}=0,
\qquad
p_{b+3}^{G_2^+}=0,
\]

so both gamma-plus bases reduce to the C support. B2-E gives

\[
S_{\gamma+}^C=0.
\]

Meanwhile `E_(b+1)=0` gives the left neighboring C reduced cost

\[
r_C(p_{b+1})=0,
\]

while `E_(b+2)<0` gives the right neighboring reduced cost strictly positive. The C2 ECT closure therefore leaves `p_(b+1)` as the only possible extra zero-cost variable.

It remains to show that this zero reduced cost does not create a nontrivial feasible face. Let `A_C` be the seven-row C equality matrix and append the entering `p_(b+1)` column. Along that one-dimensional alpha+/beta- line, write the gamma-plus slack as

\[
S_{\gamma+}(z)=S_{\gamma+}^C-dz.
\]

The Schur complement satisfies

\[
d=\frac{\det B_{G_1^+}}{\det B_C}>0.
\]

Indeed C2 gives `det B_C>0`; A114-B1 gives `det B_(G_1^+)>0`; moving the entering column from the last block position to its declared P position uses six column swaps and does not change the sign.

Since `S_(gamma+)^C=0`, every `z>0` gives

\[
S_{\gamma+}(z)<0.
\]

Thus the only feasible point on the zero-cost line is `z=0`. Therefore the common C/G1+/G2+ primal point is the unique primal optimum.

This proves C1-B.

---

# Nonclaims

This theorem does not claim:

- any result on the second compressed tie `E_(b+2)=0`;
- a monotone ordering in `s` of all lifted discriminants;
- anything outside the frozen tail/source contract;
- any physical or ontological interpretation.

Finite near-root controls are regression/falsification evidence only and are not premises of the proof.