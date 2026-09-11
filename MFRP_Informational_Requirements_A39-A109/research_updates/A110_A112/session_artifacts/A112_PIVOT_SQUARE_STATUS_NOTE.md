# A112 — Pivot-square reduction and analytic-tail status

## Status

`OPEN / INCONCLUSIVE`.

This note records the current structural reduction of the A112 analytic-tail
problem. It does **not** promote the tail program to a theorem. No new
canonical full-KKT/full-atlas outcome after rank 430 is used.

The finite A110 result remains the established theorem on the frozen contract

\[
14\le M\le 520,\qquad 129/1000\le s\le133/1000.
\]

A111/A111B are finite exact tail reconnaissance only.

## 1. Residual reduced costs as interpolation-error ratios

For each residual KKT column `x`, after the active P interpolation is solved,
the reduced cost can be written in the affine dual coordinate `y_alpha` as

\[
r_x(s;y_\alpha)=a_x(s)y_\alpha-a_x(\tau),
\qquad \tau=1/2.
\]

Hence its zero threshold is

\[
T_x(s)=\frac{a_x(\tau)}{a_x(s)},
\]

whenever the denominator is nonzero. Thus the residual-threshold ordering is
a comparison inside one interpolation-error family, not an unrelated list of
numerical KKT margins.

The dual denominator and the primal alpha-coordinate denominator are likewise
not independent sign problems: in the reduced representation they occur with
opposite orientation, so one sign certificate controls both.

## 2. Exact pivot update for `RQ(2)`

Let `C_j` denote the compressed basis at contact `j`. Let

- `u = p_(j+1)` be the adjacent P pivot column;
- `v = q_2` be the Q-side test column;
- `rho_x^{C_j}` denote the reduced cost of column `x` in the compressed basis;
- `H_x = g_x - g_B B^{-1} a_x` denote the residual of the gamma row after
  projection on the compressed basis.

After adjoining the gamma row and pivoting in `u`, the gamma-plus reduced cost
of `v` obeys the exact Schur-complement identity

\[
\boxed{
R_Q^{G_j}(2)
=
\rho_{q_2}^{C_j}
-
\rho_{p_{j+1}}^{C_j}
\frac{H_{q_2}}{H_{p_{j+1}}}
}.
\]

Equivalently, its numerator is the bordered `2 x 2` minor

\[
\boxed{
K_{j,2}
=
\begin{vmatrix}
\rho_{q_2}^{C_j} & \rho_{p_{j+1}}^{C_j}\\
H_{q_2} & H_{p_{j+1}}
\end{vmatrix}.
}
\]

This is the natural Pluecker/Schur-complement object for the pivot square
formed by the P-side exchange `j <-> j+1` and the Q-side exchange
`q_1 <-> q_2`.

A82 already supplies the adjacent compressed-basis exchange identity

\[
\rho_{\rm forward}
=-\frac{V_{j+1}-V_j}{z_{j+1}},
\]

so the correction term above is directly tied to the same compressed
orientation factor that selects the neighboring contact.

## 3. Augmented determinant representation

In the frozen gamma-plus matrix ordering, appending the `q_2` column and the
objective row gives an augmented minor `Delta_(j,2)` satisfying

\[
\boxed{
R_Q(2)=-\frac{\Delta_{j,2}}{\det G_j}.
}
\]

Only the alpha row depends on the probe `s`. Consequently
`Delta_(j,2)(s)` is an eight-channel exponential polynomial whose exponent
support is exactly

\[
\boxed{
\{0,1,2,j,j+1,h,h+1,M\},
\qquad h=\lfloor M/2\rfloor.
}
\]

This reduces the analytic-tail sign problem to the orientation of one
structured eight-channel minor plus the gamma-plus basis determinant.

## 4. Why the contact rule is essential

The residual-threshold ordering is not valid for arbitrary contacts merely
from the base ordering

\[
0<c<b<s<\tau<1.
\]

Therefore the A112 tail proof must explicitly use the compressed-contact
localization

\[
j\approx M\,c(s),
\qquad
c(s)=\frac{\log 2}{-2\log s},
\]

and the exact finite-offset classifier developed in A85--A89. This is a
hypothesis of the tail theorem, not bookkeeping.

If `b = ceil(M c(s))` and `j=b+d`, then in the even case the exact ceiling
relation gives the useful scale bracket

\[
 s^{d+1}
 <
 \frac{s^j}{2^{-M/2}}
 \le
 s^d.
\]

This is the mechanism by which the selected contact controls the apparently
vanishing residual margins.

## 5. Current asymptotic candidate — not yet a theorem

Exploratory expansion of the augmented minor, after normalization by its
natural exponentially small scale, suggests that the leading competition can
be expressed through the contact ratio `j/M` and the normalized channel
`s^j / 2^{-h}`. The observed positive leading coefficient on the frozen
source interval explains why raw margins can tend rapidly to zero without
forcing a sign change.

No all-M claim follows until the remainder is explicitly bounded uniformly on

\[
M\ge521,
\qquad
129/1000\le s\le133/1000,
\]

with parity and finite contact offsets treated correctly.

## 6. Next falsifiable theorem target

The immediate target is no longer a uniform lower bound on the unnormalized
`RQ(2)` margin. It is an **ordering/interlacing statement for pivot
boundaries**:

\[
\boxed{
\text{compressed-contact selection boundary}
\quad\Longrightarrow\quad
\Delta_{j,2}<0
}
\]

with the gamma-plus determinant oriented positively.

If proved, this yields `RQ(2)>0` throughout the selected compressed phase even
when its numerical margin converges exponentially to zero.

A valid A112 closure still requires uniform proofs for the remaining tail
conditions used by the A110 finite closure. One exact counterexample to a
claimed universal tail inequality refutes that attempted extension.

## Nonclaims

This note does not prove:

- A109 for arbitrary `M`;
- any result outside the frozen source interval;
- any different support/active-band architecture;
- any physical, spacetime, gravity, quantum, or experimental interpretation.
