# Theorem: fixed-size modular-obstruction hierarchy in Minkowski sprinklings

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic fixed-size hierarchy theorem  
**Physical status:** finite local obstruction rates for arrow-erased Minkowski causal-order recovery  
**Novelty status:** splitter closure and graph modules are classical; no equivalent Minkowski fixed-size hierarchy was located in the targeted review

## 1. Setting

Fix an integer spacetime dimension

\[
d\ge3.
\]

Let

\[
G_{d,n}
\]

be the unoriented causal-comparability graph of \(n\) iid uniform points in a fixed flat Alexandrov interval.

For a finite tuple

\[
x_1,\ldots,x_r,
\]

define the \(r\)-way splitter region

\[
\mathcal D_r
=
\left(
\bigcup_{i=1}^r A_{x_i}
\right)
\setminus
\left(
\bigcap_{i=1}^r A_{x_i}
\right),
\]

and

\[
\Delta_r
=
\mu(\mathcal D_r).
\]

## 2. Splitter-generated certificates

An ordered \(r\)-tuple

\[
x_1,\ldots,x_r
\]

is a splitter-generated certificate when

\[
x_1\sim x_2
\]

and, for every

\[
m=3,\ldots,r,
\]

the point \(x_m\) is adjacent to some but not all of

\[
x_1,\ldots,x_{m-1}.
\]

Every minimal non-stable module of size \(r\) admits such an ordering, obtained from edge-seeded splitter closure.

## 3. Pairwise disagreement is controlled by the k-way disagreement

For every pair \(i,j\),

\[
A_{x_i}\triangle A_{x_j}
\subseteq
\mathcal D_r.
\]

Hence

\[
\boxed{
\Delta_d(x_i,x_j)
\le
\Delta_r.
}
\]

Therefore, on the event

\[
\Delta_r\le\varepsilon,
\]

every pairwise graphon-neighborhood disagreement is at most \(\varepsilon\).

## 4. Imported local estimates

The all-dimensional edge-tail theorem gives

\[
F_d(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta_d(X,Y)\le\varepsilon
)
=
O(
\varepsilon^{\beta_d}
),
\]

where

\[
\beta_d
=
\min\left(
d,\,
2+\frac4d
\right).
\]

The uniform comparable-ball theorem gives

\[
\boxed{
\sup_x
\mu
\{
z:z\sim x,\,
\Delta_d(x,z)\le\varepsilon
\}
=
O(\varepsilon^2).
}
\]

## 5. Fixed-r certificate tail

Define

\[
H_{d,r}(\varepsilon)
=
\Pr(
X_1,\ldots,X_r
\text{ form a splitter-generated certificate},
\;
\Delta_r\le\varepsilon
).
\]

The first two sampled points must satisfy

\[
X_1\sim X_2
\]

and

\[
\Delta_d(X_1,X_2)\le\varepsilon.
\]

This contributes

\[
O(
\varepsilon^{\beta_d}
).
\]

Now condition on

\[
X_1,\ldots,X_{m-1}.
\]

Because \(X_m\) is a splitter of the previous set, it is comparable to at least one earlier point \(X_j\).

Also,

\[
\Delta_d(X_m,X_j)
\le
\Delta_r
\le
\varepsilon.
\]

Therefore

\[
X_m
\in
\bigcup_{j<m}
B_\varepsilon(X_j),
\]

where

\[
B_\varepsilon(x)
=
\{
z:z\sim x,\,
\Delta_d(x,z)\le\varepsilon
\}.
\]

For fixed \(r\),

\[
\mu
\left(
\bigcup_{j<m}
B_\varepsilon(X_j)
\right)
\le
C_{d,r}\varepsilon^2.
\]

Each additional certificate point therefore contributes an \(O(\varepsilon^2)\) factor.

Thus

\[
\boxed{
H_{d,r}(\varepsilon)
=
O_{d,r}
\left(
\varepsilon^{
\beta_d+2(r-2)
}
\right).
}
\]

No joint-coordinate rederivation is required for each \(r\).

## 6. Expected number of minimal non-stable r-modules

Let

\[
M_{r,n}^{\min}
\]

be the number of minimal non-stable modules of cardinality exactly \(r\).

A minimal non-stable module admits at least one splitter-generated ordering.

For a fixed ordered certificate with splitter volume \(\Delta_r=\delta\), all remaining \(n-r\) points must avoid its splitter region.

Therefore, up to an \(r\)-dependent constant accounting for possible orderings,

\[
\mathbb E[M_{r,n}^{\min}]
\le
C_r
n^r
\int_0^1
(1-\delta)^{n-r}
\,dH_{d,r}(\delta).
\]

Using the certificate-tail bound,

\[
\boxed{
\mathbb E[M_{r,n}^{\min}]
=
O_{d,r}
\left(
n^{
4-r-\beta_d
}
\right).
}
\]

## 7. d >= 4 hierarchy

For

\[
d\ge4,
\]

\[
\beta_d
=
2+\frac4d.
\]

Hence

\[
\boxed{
\mathbb E[M_{r,n}^{\min}]
=
O_{d,r}
\left(
n^{
2-r-4/d
}
\right).
}
\]

The first levels are:

### r = 2

\[
O(n^{-4/d}).
\]

This is the comparable true-twin scale, and the sharper theorem gives

\[
\mathbb E[T_n]
\sim
K_d^{\mathrm{twin}}n^{-4/d}.
\]

### r = 3

\[
\boxed{
O(n^{-1-4/d}).
}
\]

### r = 4

\[
\boxed{
O(n^{-2-4/d}).
}
\]

Every additional fixed vertex contributes another factor \(n^{-1}\).

Therefore true twins are the unique fixed-size obstruction family living at the candidate leading scale

\[
n^{-4/d}.
\]

## 8. d = 3 hierarchy

For

\[
d=3,
\]

\[
\beta_3=3.
\]

Hence

\[
\boxed{
\mathbb E[M_{r,n}^{\min}]
=
O_r(n^{1-r}).
}
\]

In particular,

\[
r=2:
\quad
O(n^{-1}),
\]

\[
r=3:
\quad
O(n^{-2}),
\]

and again every additional fixed vertex costs another factor \(n^{-1}\).

## 9. Relation to the earlier d = 4 P3 theorem

For

\[
d=4,
\qquad
r=3,
\]

the general formula gives

\[
O(n^{-2}).
\]

The dedicated \(P_3\) theorem proved the sharper two-sided statement

\[
\mathbb E[M_{3,n}]
=
\Theta(n^{-2}).
\]

Thus the general certificate theorem is consistent with the independently derived \(d=4\) result.

## 10. Consequence for the convergence-rate problem

For every fixed

\[
d\ge4,
\]

the verified true-twin occurrence probability is

\[
\Pr(T_n>0)
\sim
K_d^{\mathrm{twin}}n^{-4/d}.
\]

The present theorem proves that every minimal non-stable module of any fixed size

\[
r\ge3
\]

has probability at most

\[
O(n^{-1-4/d}),
\]

or smaller.

Therefore no fixed-size module family other than size-two true twins can modify the leading \(n^{-4/d}\) constant.

The unresolved matching upper bound must come from a module size that grows with \(n\), or from another nonlocal forcing obstruction.

This narrows the quantitative frontier substantially.
