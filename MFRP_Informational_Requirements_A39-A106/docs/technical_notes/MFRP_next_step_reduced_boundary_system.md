# A81 — Reduced Two-Variable Boundary System and Ordered-Root Theorem

**Programme:** Modal Field Research Programme  
**Audit:** A81  
**Author:** Felipe Gianini Romero  
**Status:** exact algebraic reduction plus finite local positivity theorem

## Technical abstract

A80 found that every selected compression boundary is described by a primitive integer polynomial with exactly six nonzero monomials. A81 derives that sparsity from the branch equations themselves.

For the compressed support

\[
P=\{0,k,M\},\qquad Q=\{1,h,h+1\},\qquad h=\lfloor M/2\rfloor,
\]

the normalization and central-mean constraints reduce the primal branch to two unknowns: the scaled mass \(t\) and the interior mass \(z=p_k\). Every transform is then affine in \((z,t)\). The active \(\alpha+\) and \(\beta-\) bands form an exact \(2\times2\) system. The two inactive gamma slacks reduce to two closed boundary formulas

\[
F_{\rm lower}(s),\qquad F_{\rm upper}(s),
\]

whose coefficients are given explicitly by three scalar cofactors \(X_\delta,Y_\delta,Z\). This proves the six-term law for arbitrary admissible \((M,k)\), before any finite scan.

The finite audit covers every pair

\[
10\le M\le80,\qquad 2\le k<\lfloor M/2\rfloor,
\]

for a total of 1,438 contacts. On

\[
I=\left[\frac{129}{1000},\frac{133}{1000}\right],
\]

the numerator \(T(s)\) of \(t\) and the basis determinant \(\Delta(s)\) are both strictly positive for all 1,438 pairs. For the 71 contacts selected by A78, both boundary polynomials are also strictly increasing. The exact identity

\[
F_{\rm lower}(s)-F_{\rm upper}(s)=4\varepsilon T(s)>0
\]

then proves that reversed root pairs and lower-only local roots cannot occur in the selected family. The complete A80 classification follows from endpoint signs alone: 20 complete ordered pairs, three upper-only cases, and 48 no-root cases.

## 1. Frozen contract

For each integer \(M\ge10\), let

\[
X_M=\{0,1,\ldots,M\},\qquad m=\frac M2,
\]

with target exponent \(1\), fixed channels

\[
\beta=3,\qquad \gamma=4,
\]

and compactified variables

\[
b=2^{-3}=\frac18,\qquad g=2^{-4}=\frac1{16},\qquad s=2^{-\alpha}.
\]

The parity-normalized tolerance is

\[
\varepsilon_M=
\begin{cases}
\dfrac{1}{1875\,2^h}, & M=2h,\\[6pt]
\dfrac{1}{2500\,2^h}, & M=2h+1.
\end{cases}
\]

A81 treats every admissible contact

\[
2\le k<h,
\]

for the finite positivity census, and separately reconstructs the 71 A78-selected contacts for comparison with A80.

## 2. Reduction of the P branch

Write the scaled P masses as

\[
p_0+p_k+p_M=t,
\]

\[
k p_k+M p_M=\frac M2 t.
\]

Set

\[
z=p_k.
\]

Then

\[
p_M=\frac t2-\frac{k}{M}z,
\]

\[
p_0=\frac t2-\frac{M-k}{M}z.
\]

For any transform base \(r\),

\[
P_r=p_0+r^k p_k+r^M p_M=A_r t+B_r z,
\]

where

\[
A_r=\frac{1+r^M}{2},
\]

\[
B_r=r^k-\frac{M-k}{M}-\frac{k}{M}r^M.
\]

Thus \(B_r\) has support only at exponents

\[
\{0,k,M\}.
\]

## 3. Reduction of the Q branch

Let

\[
U=2^{-h},\qquad d=1-(h+1)U,
\]

and define

\[
W_r=r-h r^h+(h-1)r^{h+1}.
\]

The Q masses satisfy normalization, central mean, and the target equation

\[
\frac12 q_1+2^{-h}q_h+2^{-(h+1)}q_{h+1}=1.
\]

For even support \(M=2h\),

\[
q_1=\frac{2(1-Ut)}{d},
\]

\[
q_h=t-hq_1,
\]

\[
q_{h+1}=(h-1)q_1.
\]

For odd support \(M=2h+1\),

\[
q_1=\frac{2-\frac32Ut}{d},
\]

\[
q_h=\frac t2-hq_1,
\]

\[
q_{h+1}=\frac t2+(h-1)q_1.
\]

In both cases,

\[
Q_r=C_r+D_r t,
\]

with

\[
C_r=\frac{2W_r}{d}.
\]

For even \(M\),

\[
D_r=r^h-\frac{2U}{d}W_r.
\]

For odd \(M\),

\[
D_r=\frac{r^h+r^{h+1}}2-\frac{3U}{2d}W_r.
\]

Therefore \(C_r\) and \(D_r\) use only the exponents

\[
\{1,h,h+1\}.
\]

## 4. Exact two-variable system

The active \(\alpha+\) equation is

\[
P_s-Q_s=2\varepsilon t.
\]

Define

\[
H_s=A_s-D_s-2\varepsilon.
\]

Then

\[
B_s z+H_s t=C_s.
\]

The active \(\beta-\) equation is

\[
P_b-Q_b=-2\varepsilon t.
\]

Define

\[
H_\beta=A_b-D_b+2\varepsilon.
\]

Then

\[
B_\beta z+H_\beta t=C_\beta.
\]

The exact determinant and Cramer numerators are

\[
\Delta(s)=B_sH_\beta-B_\beta H_s,
\]

\[
N_z(s)=C_sH_\beta-C_\beta H_s,
\]

\[
T(s)=B_sC_\beta-B_\beta C_s.
\]

Hence

\[
z=\frac{N_z(s)}{\Delta(s)},
\qquad
 t=\frac{T(s)}{\Delta(s)}.
\]

A81 verifies these identities against the full symbolic compressed branch on eight declared witnesses spanning both parities, all three A80 root classes, compression supports, and the upper end of the finite domain.

## 5. Closed boundary formulas

Let

\[
G_\gamma=A_g-D_g.
\]

Use \(\delta=+1\) for the lower gamma-minus boundary and \(\delta=-1\) for the upper gamma-plus-oriented boundary. Define

\[
q_\delta=G_\gamma+2\delta\varepsilon,
\]

\[
X_\delta=q_\delta C_\beta-C_\gamma H_\beta,
\]

\[
Y_\delta=B_\gamma H_\beta-q_\delta B_\beta,
\]

\[
Z=C_\gamma B_\beta-B_\gamma C_\beta.
\]

Then the two oriented boundary formulas are

\[
\boxed{
F_\delta(s)=X_\delta B_s+Y_\delta C_s+Z H_s.
}
\]

The inactive slacks are

\[
\operatorname{slack}_{\gamma-}=\frac{F_{+1}(s)}{\Delta(s)},
\]

\[
\operatorname{slack}_{\gamma+}=-\frac{F_{-1}(s)}{\Delta(s)}.
\]

## 6. Explicit six coefficients

Because

\[
B_s\text{ uses }\{0,k,M\},
\]

\[
C_s\text{ uses }\{1,h,h+1\},
\]

and

\[
H_s\text{ uses }\{0,1,h,h+1,M\},
\]

while \(2\le k<h\), the union is exactly

\[
\{M,h+1,h,k,1,0\}.
\]

No exponent collides. The six coefficients are

\[
c_k^{(\delta)}=X_\delta,
\]

\[
c_M^{(\delta)}=-\frac{k}{M}X_\delta+\frac12 Z,
\]

\[
c_0^{(\delta)}=-\frac{M-k}{M}X_\delta+
\left(\frac12-2\varepsilon\right)Z,
\]

\[
c_1^{(\delta)}=Y_\delta C_1+Z H_1,
\]

\[
c_h^{(\delta)}=Y_\delta C_h+Z H_h,
\]

\[
c_{h+1}^{(\delta)}=Y_\delta C_{h+1}+Z H_{h+1}.
\]

Thus

\[
F_\delta(s)=
 c_M^{(\delta)}s^M+
 c_{h+1}^{(\delta)}s^{h+1}+
 c_h^{(\delta)}s^h+
 c_k^{(\delta)}s^k+
 c_1^{(\delta)}s+
 c_0^{(\delta)}.
\]

This is an analytic sparsity theorem for every admissible \((M,k)\) under the frozen contract. The finite audit confirms that none of the six coefficients vanishes for all 2,876 lower/upper formulas generated from the 1,438 audited pairs.

## 7. Positive boundary-gap identity

Only \(q_\delta\) changes between the lower and upper formulas. Therefore

\[
X_{+1}-X_{-1}=4\varepsilon C_\beta,
\]

\[
Y_{+1}-Y_{-1}=-4\varepsilon B_\beta,
\]

while \(Z\) is unchanged. Hence

\[
\boxed{
F_{\rm lower}(s)-F_{\rm upper}(s)
=4\varepsilon\bigl(B_sC_\beta-B_\beta C_s\bigr)
=4\varepsilon T(s).
}
\]

A81 certifies by exact rational interval enclosure that

\[
T(s)>0,
\qquad
\Delta(s)>0
\]

on \(I\) for every one of the 1,438 admissible pairs. Consequently

\[
t(s)=\frac{T(s)}{\Delta(s)}>0
\]

and

\[
F_{\rm lower}(s)>F_{\rm upper}(s)
\]

throughout the finite local domain.

## 8. Ordered-root theorem for the selected contacts

For the 71 A78-selected contacts, A81 independently certifies

\[
F_{\rm lower}'(s)>0,
\qquad
F_{\rm upper}'(s)>0
\]

on \(I\).

Because the two functions are strictly increasing and

\[
F_{\rm lower}(s)>F_{\rm upper}(s),
\]

a lower root cannot occur to the right of an upper root. A lower-only local root is also impossible: if the lower function crosses inside \(I\), the upper function is smaller at that same point and cannot already be positive throughout the interval.

The root classes therefore follow from endpoint signs:

- complete ordered pair when
  \[
  F_{\rm lower}(I_{\rm left})<0,
  \qquad
  F_{\rm upper}(I_{\rm right})>0;
  \]
- upper-only when the lower boundary is already positive at the left endpoint while the upper boundary changes sign;
- no local root when both boundaries are positive throughout.

This endpoint-only rule exactly reproduces A80:

\[
\boxed{20\text{ complete ordered pairs}},
\]

\[
\boxed{3\text{ upper-only cases at }M=20,36,64},
\]

\[
\boxed{48\text{ no-root cases}},
\]

\[
\boxed{0\text{ lower-only or reversed cases}}.
\]

## 9. Primitive normalization correction

The closed formulas above are rational-coefficient polynomials. A80 stored each boundary after independent primitive integer normalization.

For 67 of the 71 selected contacts, the lower and upper formulas acquire the same positive normalization factor. Four supports have different primitive contents:

| \(M\) | \(k\) | lower normalization / upper normalization |
|---:|---:|---:|
| 34 | 7 | 29 |
| 64 | 13 | 13 |
| 69 | 14 | \(1/19\) |
| 77 | 15 | 11 |

This is not a failure of the boundary-gap identity. It is a warning about representation:

> The identity \(F_{\rm lower}-F_{\rm upper}=4\varepsilon T\) holds for the common raw reduced formulas. It must not be applied after independently dividing the two sides by different primitive integer contents.

A81 preserves this distinction explicitly rather than forcing a false common normalization.

## 10. Computational certificate

The audit produces:

- 142/142 exact reconstructions of the committed A80 Cramer polynomials;
- 2,876 exact six-coefficient formulas over all 1,438 admissible pairs;
- 1,438/1,438 positive \(T\) interval certificates;
- 1,438/1,438 positive \(\Delta\) interval certificates;
- exact reduced/full-branch identities on eight declared symbolic witnesses;
- exact reproduction of the A80 root-class counts and support lists;
- 17/17 top-level gates passed.

## 11. What A81 proves

1. An exact two-variable reduction of the compressed branch.
2. Closed parity-dependent formulas for \(Q_r=C_r+D_rt\).
3. Closed cofactor formulas for both gamma boundaries.
4. An exact six-coefficient law for arbitrary admissible \((M,k)\) under the frozen contract.
5. Exact reconstruction of all 142 selected-contact A80 polynomials.
6. Positivity of \(T\) and \(\Delta\) for all 1,438 finite-domain contacts on \(I\).
7. The exact positive-gap identity \(F_{\rm lower}-F_{\rm upper}=4\varepsilon T\).
8. Endpoint-only reproduction of the selected-contact local root atlas.
9. Exact exclusion of lower-only and reversed selected root pairs on \(I\).
10. Exact identification of four primitive-content asymmetries.

## 12. What A81 does not prove

A81 does not establish:

- positivity of \(T\) or \(\Delta\) for arbitrary \(M\) or outside \(I\);
- strict boundary monotonicity for every admissible \(k\);
- a formula selecting \(k(M)\);
- a periodic law for compression supports;
- global phase completeness outside the local interval;
- a physical meaning for contacts, bands, or compression.

## 13. Next rigorous target

The next justified audit is not another finite scan of roots. The reduction exposes the remaining discrete problem directly:

\[
\text{which }k\text{ is selected by the full KKT system at a given }(M,s)?
\]

A82 should compare adjacent contacts using the reduced formulas and determine whether the selected-contact reset can be governed by one exact sign function, while retaining the A80 counterexamples showing that a contact-entry equation alone need not make the adjacent branch dual-feasible.
