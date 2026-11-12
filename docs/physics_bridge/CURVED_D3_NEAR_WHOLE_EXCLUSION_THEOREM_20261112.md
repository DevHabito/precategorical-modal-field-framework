# Theorem: exclusion of near-whole modules in a regular curved 2+1 causal diamond

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem from curvature-robust degree/co-degree exponents  
**Physical status:** final global module estimate needed for qualitative curved \(2+1\) orientation recovery

## 1. Statement

Let \(G_n\) be the causal-comparability graph of \(n\) iid points sampled from a regular curved \(2+1\) Alexandrov interval satisfying:

\[
g_3(q)
=
O(q^{4/3}),
\]

\[
\bar g_3(r)
=
O(r^3),
\]

and

\[
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2).
\]

Assume \(G_n\) is connected.

Then, for every sufficiently slowly decreasing deterministic sequence

\[
\varepsilon_n\downarrow0,
\]

\[
\boxed{
\Pr\!\left(
\exists\text{ proper non-stable module }M:
1\le n-|M|\le\varepsilon_n n
\right)
\to0.
}
\]

The proof depends only on the three displayed exponents and standard concentration.

## 2. External types

Let

\[
O=V(G_n)\setminus M,
\qquad
\ell=|O|.
\]

Every vertex of \(O\) is either complete or anticomplete to \(M\).

Write

\[
U
=
\{z\in O:z\text{ complete to }M\},
\]

and

\[
N
=
\{z\in O:z\text{ anticomplete to }M\}.
\]

Connectedness gives

\[
\boxed{
U\ne\varnothing.
}
\]

For \(z\in N\),

\[
\deg(z)\le\ell-1.
\]

For \(u\in U\),

\[
\overline{\deg}(u)
\le
\ell-1.
\]

## 3. Sampled small-co-degree bound

The continuum co-degree tail

\[
\bar g_3(r)
=
O(r^3)
\]

implies

\[
\boxed{
\mathbb E
\#\{
v:
\overline{\deg}(v)\le L
\}
\le
C
\frac{
(L+1)^3
}{
n^2
}
}
\]

for \(L=o(n)\).

This is the binomial-mixture estimate derived by Stieltjes integration.

## 4. Very small complements

Choose

\[
L_0
=
A
\sqrt n
(\log n)^2.
\]

If

\[
1\le\ell\le L_0,
\]

then every \(u\in U\) has sampled co-degree at most \(L_0\).

Therefore

\[
\Pr(U\ne\varnothing)
\le
C
\frac{
L_0^3
}{
n^2
}
=
O\left(
\frac{
(\log n)^6
}{
\sqrt n
}
\right)
\to0.
\]

Since \(U\ne\varnothing\) is required, no such module survives.

## 5. Dyadic residual range

Now assume

\[
L_0<\ell\le\varepsilon_n n.
\]

Use dyadic ranges

\[
\frac L2<\ell\le L,
\]

and set

\[
s=\frac Ln.
\]

Then

\[
s\to0.
\]

At the smallest scale,

\[
ns^2
=
\frac{L^2}{n}
\ge
A^2
(\log n)^4.
\]

This supplies the required Chernoff exponent.

## 6. Anticomplete vertices have low continuum degree

Every \(z\in N\) has observed degree at most \(L\).

Choose a sufficiently large constant \(a>1\).

If

\[
Q(z)>as,
\]

then its expected sampled degree exceeds \(L\) by a fixed factor.

Chernoff gives

\[
\Pr(
\deg(z)\le L
\mid
Q(z)>as
)
\le
e^{-cL}.
\]

A union bound yields

\[
\boxed{
N\subseteq S_{as}
}
\]

simultaneously over all dyadic ranges with probability tending to one.

## 7. Complete vertices are sparse

Every \(u\in U\) has observed co-degree at most \(L\).

The co-degree mixture bound gives

\[
\mathbb E
\#\{
v:
\overline{\deg}(v)\le L
\}
=
O(ns^3).
\]

Use the larger threshold

\[
T_U
=
ns^{5/2}.
\]

Markov gives

\[
\Pr(
|U|>T_U
)
=
O(s^{1/2}).
\]

Summing over dyadic scales remains \(o(1)\).

Thus

\[
\boxed{
|U|
\le
ns^{5/2}
}
\]

with high probability.

## 8. Internal sparsity pushes N to scale s squared

For \(z\in N\subseteq S_{as}\),

\[
\mu(
A_z\cap S_{as}
)
\le
C_1s^2.
\]

Choose

\[
B>2C_1.
\]

If

\[
Q(z)>Bs^2,
\]

then

\[
\mu(
A_z\setminus S_{as}
)
\ge
c s^2.
\]

The number of sampled neighbors of \(z\) outside \(S_{as}\) therefore has mean

\[
\Theta(ns^2).
\]

Every sampled neighbor of \(z\in N\) lies outside \(M\).

A neighbor outside \(S_{as}\) cannot belong to \(N\).

Therefore it must lie in \(U\).

The module condition requires

\[
Y_z
\le
|U|
\le
ns^{5/2}.
\]

But

\[
ns^{5/2}
=
s^{1/2}
(ns^2)
=
o(ns^2).
\]

Chernoff gives

\[
\Pr(
Y_z\le ns^{5/2}
)
\le
e^{-cns^2}.
\]

Since

\[
ns^2\gg\log n
\]

at the smallest dyadic scale, a union bound yields

\[
\boxed{
N\subseteq S_{Bs^2}
}
\]

with probability tending to one.

## 9. Too few ultra-low-degree candidates

The curved low-degree tail gives

\[
g_3(q)
=
O(q^{4/3}).
\]

Therefore

\[
\mathbb E
\#S_{Bs^2}^{\mathrm{sample}}
=
O(
n(s^2)^{4/3}
)
=
O(
ns^{8/3}
).
\]

Relative to

\[
L=ns,
\]

the expected fraction is

\[
O(s^{5/3})
\to0.
\]

Markov and a dyadic union bound give

\[
\boxed{
|N|<L/4
}
\]

simultaneously with high probability.

Also

\[
|U|
\le
ns^{5/2}
=
s^{3/2}L
<
L/4
\]

for large \(n\).

Thus

\[
|O|
=
|U|+|N|
<
L/2,
\]

contradicting

\[
|O|=\ell>L/2.
\]

## 10. Conclusion

All sublinear complement scales are excluded.

Hence

\[
\boxed{
\Pr\!\left(
\exists\text{ proper non-stable module }M:
n-|M|=o(n)
\right)
\to0
}
\]

in the standard deterministic-diagonal sense.

No flat-space formula enters the proof.

The theorem depends only on the curvature-robust exponents

\[
4/3,
\qquad
3,
\qquad
2.
\]

## 11. Rate limitation

This proof is qualitative.

Its very-small-complement estimate is

\[
O(
n^{-1/2}
(\log n)^6
),
\]

which is sufficient for convergence to zero but not sufficient to show that near-whole modules are \(o(n^{-1})\).

Therefore this theorem closes the qualitative curved orientation-recovery problem but does **not** yet identify the leading curved reconstruction-error constant.

A curved analogue of the tip middle-band clearance theorem would be needed for that sharper result.
