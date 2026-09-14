# A114-B2-D — internal zero-discriminant boundary theorem on the strict `b+2`, negative-pivot tail

## Status

**PROVED conditional boundary theorem under the frozen analytic-tail contract, by composition of the already-promoted C1/C2/C3 identities and one boundary ECT argument.**

This theorem closes the three *internal* zero-discriminant sets inside the already-classified `Phi<0` branch. It does **not** classify the outer pivot set `Phi=0`.

Let

\[
M\ge 521,\qquad 129/1000\le s\le 133/1000,
\qquad h=\lfloor M/2\rfloor,
\]

\[
b=\left\lceil \frac{M\log 2}{-2\log s}\right\rceil,
\qquad j=b+2,
\qquad U=2^{-h},
\]

assume `j=b+2` is the strict compressed maximizer, and assume

\[
\boxed{\Phi=F_j^{\rm up}<0.}
\]

Use the promoted architectures

\[
C:\ P=\{0,j,M\},\quad Q=\{1,h,h+1\},
\]

\[
E:\ P=\{j-1,j,M\},\quad Q=\{1,h,h+1\},
\]

\[
QI:\ P=\{j,M\},\quad Q=\{0,1,h,h+1\},
\]

\[
QA:\ P=\{j-1,j,M\},\quad Q=\{0,1,h,h+1\},
\]

with the active-band conventions of A114-B2-C1/C2/C3, and define

\[
\Gamma=S_{\gamma-}^{QI}.
\]

The strict regions are already known:

\[
p_0^C>0\Rightarrow C,
\]

\[
p_0^C<0,\ r_E(q_0)>0\Rightarrow E,
\]

\[
p_0^C<0,\ r_E(q_0)<0,\ \Gamma>0\Rightarrow QI,
\]

\[
p_0^C<0,\ r_E(q_0)<0,\ \Gamma<0\Rightarrow QA.
\]

This note classifies the equality sets between them.

---

# Theorem

## D1. The `p_0^C=0` boundary has a unique primal optimum

Assume

\[
\boxed{p_0^C=0.}
\]

Then the `C` solution is primal feasible with

\[
p_j^C>0,\qquad p_M^C>0,
\qquad q_1^C,q_h^C,q_{h+1}^C>0,
\qquad t^C>0.
\]

All active dual multipliers, all nonbasic P/Q reduced costs, and all inactive band slacks are strictly positive. The only lost strict gate is the basic mass

\[
p_0^C=0.
\]

Hence `C` is a global optimum and the **primal optimum is unique**, although its basis representation is degenerate.

Moreover, the exact C1/C3 pivot identities imply

\[
p_{j-1}^E=0,
\qquad q_0^{QI}=0.
\]

After deleting those zero coordinates, `C`, `E`, and `QI` have the same positive primal support

\[
P=\{j,M\},\qquad Q=\{1,h,h+1\},
\]

and satisfy the same normalization, mean, target, `alpha+`, and `beta-` equalities. Therefore all three primal representations collapse to the **same primal point**.

This does not assert that the `E` or `QI` dual basis is feasible for every sign of the remaining discriminants; the statement is about primal coalescence and uniqueness of the optimum.

## D2. The `r_E(q_0)=0` boundary has a nontrivial optimal face

Assume

\[
\boxed{p_0^C<0,\qquad r_E(q_0)=0.}
\]

Then all basic variables of `E` remain strictly positive. Its active duals, inactive slacks, and every nonbasic P reduced cost remain strictly positive. In the Q reduced-cost family,

\[
r_E(q_0)=0
\]

while every other nonbasic Q reduced cost is strictly positive.

Therefore `E` is a global optimum, but the primal optimum is **not unique**.

Indeed, `q_0` is a nonbasic variable with zero reduced cost. Because every basic variable and every inactive slack of `E` is strictly positive, the simplex direction obtained by increasing `q_0` is feasible for a nonzero interval. The objective derivative along this edge is exactly zero. Hence there is a nontrivial line segment of globally optimal primal points.

More precisely, consider the formal `E -> QI` alpha+/beta- pivot edge. The gamma-minus slack is affine on this edge. It is strictly positive at `E` and equals `Gamma` at the formal `QI` endpoint.

- If `Gamma>0`, the `QI` endpoint is primal feasible and the optimal segment reaches `QI`.
- If `Gamma=0`, the optimal segment reaches `QI`, which is simultaneously the gamma-zero cut; `QA` collapses to that same endpoint.
- If `Gamma<0`, the gamma-minus inequality cuts the zero-cost edge before the formal `QI` endpoint. The cut point is exactly the `QA` primal point; the optimal face is the segment from `E` to `QA`.

Thus `r_E(q_0)=0` is qualitatively different from the other internal boundaries: it is a genuine **primal nonuniqueness surface**, not merely two bases representing one point.

## D3. The `Gamma=0` boundary has a unique primal optimum

Assume

\[
\boxed{p_0^C<0,\qquad r_E(q_0)<0,\qquad \Gamma=0.}
\]

The exact C3 Schur identity gives

\[
U p_{j-1}^{QA}
=-\Gamma\frac{D_Q}{D_{QA}}=0.
\]

The common QA masses remain strictly positive by the direct QA Cramer bounds, and `q_0>0` follows from the common QI/QA primal system. Hence deleting the zero coordinate `p_(j-1)` from QA leaves exactly the QI primal support.

At the same time `Gamma=0` says that the QI primal point saturates the gamma-minus inequality. Therefore `QI` and `QA` collapse to the **same primal point**.

For `QI`, the residual identity

\[
r_{QI}(p_{j-1})
=-\,r_E(q_0)\frac{D_E}{D_Q}
\]

gives

\[
r_{QI}(p_{j-1})>0.
\]

All other nonbasic reduced costs and the active alpha/beta multipliers remain strictly positive by the C3 analytic certificate; the gamma-plus slack remains strictly positive. The only lost strict gate is the inactive gamma-minus slack itself,

\[
S_{\gamma-}^{QI}=0.
\]

Consequently the common `QI=QA` primal point is a global optimum and the **primal optimum is unique**. The basis/dual representation is non-unique: QI treats gamma-minus as an inactive tight inequality with zero multiplier, whereas QA treats it as active and has

\[
y_{\gamma-}^{QA}
=-r_E(q_0)\frac{D_E}{D_{QA}}>0
\]

with the degenerate basic mass `p_(j-1)=0`.

---

# Proof map

## 1. Ingredients already proved before D

A114-B2-C1/C2/C3 establish, uniformly on the present `Phi<0` contract,

\[
D_C<0,\qquad D_E>0,\qquad D_Q>0,\qquad D_{QA}>0,
\]

plus the source/tail box

\[
\frac9{1000}<\frac{s^{j-1}}U<\frac1{25},
\qquad h-j\ge168.
\]

C2 proves strict positivity of all C duals/reduced costs and gives the gamma-minus slack in the form

\[
S_{\gamma-}^C=\frac{A_0+A_1p_0}{K_\beta},
\]

with

\[
A_0>0,\qquad A_1>0,\qquad K_\beta>0.
\]

It also proves the exact gamma-plus pivot relation

\[
p_{j+1}^{G+}
=-S_{\gamma+}^C\frac{\det B_C}{\det B_{G+}},
\]

and therefore `Phi<0` protects `S_(gamma+)^C>0` independently of `p0^C>0`.

C1 proves the exact C/E exchange numerator with opposite determinant orientation, hence

\[
p_0^C=0\Longrightarrow p_{j-1}^E=0.
\]

C3 proves that C and QI use the same exact Cramer numerator for `p0^C` and `q0^QI`, with nonzero opposite-orientation denominators, hence

\[
p_0^C=0\Longrightarrow q_0^{QI}=0.
\]

C3 also proves

\[
r_E(q_0)=\frac{N_g}{D_E},
\qquad
r_{QI}(p_{j-1})=-\frac{N_g}{D_Q},
\]

and

\[
y_{\gamma-}^{QA}
=-r_E(q_0)\frac{D_E}{D_{QA}},
\qquad
U p_{j-1}^{QA}
=-\Gamma\frac{D_Q}{D_{QA}}.
\]

No finite control is used as a premise below.

## 2. D1 primal positivity at `p0^C=0`

Set `p0=0` in the exact C two-variable system. The beta row becomes

\[
K_\beta t=C_\beta.
\]

The already-certified C2 bounds give `K_beta>0`, `C_beta>0`, and the same strict normalized upper/lower bounds on `Ut` needed for the Q block. Thus

\[
t>0.
\]

The exact P mean formulas reduce to

\[
p_j=\frac\lambda2 t>0,
\qquad
p_M=\left(1-\frac\lambda2\right)t>0,
\]

with `lambda<1.216<2`. The exact Q formulas then give strict positivity of `q1,qh,q_(h+1)` exactly as in C2.

The C dual solution depends on the basis matrix/objective, not on the right-hand-side sign of `p0`. Hence all C2 strict reduced-cost and active-dual bounds remain unchanged at `p0=0`. For gamma-minus the displayed formula gives

\[
S_{\gamma-}^C=\frac{A_0}{K_\beta}>0,
\]

and `Phi<0` still gives `S_(gamma+)^C>0`.

Therefore the only zero KKT gate is `p0` itself. Strict reduced costs and strict active/inactive dual gates force any optimal primal point to use the same C columns and equalities; nonsingularity of the C basis then forces the same primal solution. This proves uniqueness.

## 3. D2 boundary ECT closure

At `r_E(q0)=0`, the C1 protected primal/dual/slack gates remain strict. The only C1 Q checkpoint that loses strictness is `q0`; the independent checkpoint

\[
r_E(q_2)>0
\]

remains strict.

The E Q reduced-cost function lies in the same five-dimensional extended-Chebyshev space used in C1. It has the four distinct roots

\[
0,\quad1,\quad h,\quad h+1.
\]

A nonzero function in this ECT space has at most four real zeros counting multiplicity. Therefore there can be no additional Q reduced-cost zero. Moreover none of the four displayed roots can have multiplicity greater than one, because that would already exceed the zero budget. The signs consequently alternate across the simple roots. Since `r_E(q2)>0`, every nonbasic integer Q reduced cost other than `q0` is strictly positive.

Thus E is dual feasible with exactly one zero nonbasic reduced cost. Increasing `q0` along its simplex direction gives a nontrivial feasible zero-objective-slope interval because all E basic variables and inactive slacks start strictly positive. This proves primal nonuniqueness.

The endpoint refinement follows from affine edge geometry. The gamma-minus slack is positive at E and equals `Gamma` at the formal QI endpoint. When `Gamma<0`, its unique zero on the edge is the gamma-active QA solution. The exact C3 identity gives `p_(j-1)^QA>0`, and the direct QA primal bounds protect the common masses. When `Gamma>=0`, no gamma cut occurs before QI; the QI primal positivity argument uses `p0^C<0` and `Gamma>=0` and is independent of the strict sign of `r_E(q0)` needed only for the QI pivot reduced cost. At `Gamma=0`, use the D3 coalescence argument.

## 4. D3 QI/QA coalescence and uniqueness

At `Gamma=0`, C3 gives `p_(j-1)^QA=0`. The QA direct-primal bounds for the common masses remain strict at `w=U p_(j-1)=0`; deleting that zero coordinate leaves the QI support. Since QI itself satisfies the gamma-minus equality at `Gamma=0`, the two square systems represent the same primal point.

The residual premise `r_E(q0)<0` gives `r_QI(p_(j-1))>0`. Every other QI nonbasic reduced cost, active multiplier, and inactive gamma-plus slack has a strict positive C3 margin. Hence the QI dual certificate has strict reduced costs for every nonbasic primal variable. Any alternative optimal primal point would therefore have to use the same QI support and active alpha/beta equalities, and QI nonsingularity forces equality with the displayed point. Thus the primal optimum is unique.

---

# What D closes

Within the strict compressed `b+2`, `Phi<0` analytic-tail contract, the negative-pivot branch is now classified including its internal equality sets:

- `p0^C>0` -> unique strict C;
- `p0^C=0` -> unique primal optimum, degenerate C/E/QI coalescence;
- `p0^C<0, r_E(q0)>0` -> unique strict E;
- `p0^C<0, r_E(q0)=0` -> nontrivial optimal face from E along the q0 pivot edge;
- `p0^C<0, r_E(q0)<0, Gamma>0` -> unique strict QI;
- `p0^C<0, r_E(q0)<0, Gamma=0` -> unique primal optimum, degenerate QI/QA coalescence;
- `p0^C<0, r_E(q0)<0, Gamma<0` -> unique strict QA.

The outer set

\[
\boxed{\Phi=0}
\]

remains separate and is **not** claimed closed here.

# Nonclaims

This theorem does not claim:

- a universal monotone ordering of the discriminant zeros as `s` varies;
- uniqueness of an optimal basis on any equality set;
- closure of the outer `Phi=0` boundary;
- anything outside the frozen source/tail contract;
- any physical interpretation.

Exact finite controls are retained only as regression/falsification evidence. The theorem itself is a composition of promoted analytic identities, determinant signs, strict margins, and the boundary ECT zero-budget argument above.