# Theorem: exclusion of near-whole internal modules in 2+1 Minkowski sprinklings

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem  
**Physical status:** last sublinear-complement obstruction bound for arrow-erased \(2+1\)-dimensional Minkowski causal sets  
**Novelty status:** the proof combines established concentration tools with project-specific Minkowski degree tails and low-degree internal sparsity

## 1. Statement

Let

\[
G_n=G_{3,n}
\]

be the unoriented causal-comparability graph of an iid size-\(n\) sprinkling into a fixed flat Alexandrov interval of \(\mathbb M^3\).

Let \(C_n\) be its unique nontrivial connected component on the high-probability event from the component theorem.

For every sufficiently slowly decreasing deterministic sequence

\[
\varepsilon_n\downarrow0,
\]

\[
\boxed{
\Pr\!\left(
\exists\text{ proper graph module }M\subset C_n:
1\le|C_n\setminus M|\le\varepsilon_n n,
\;
M\text{ contains an edge}
\right)
\to0.
}
\]

## 2. External types

Let

\[
O=C_n\setminus M,
\qquad
\ell=|O|.
\]

Partition \(O\) into

\[
U
=
\{z\in O:z\text{ is complete to }M\}
\]

and

\[
N
=
\{z\in O:z\text{ is anticomplete to }M\}.
\]

Connectedness gives

\[
U\ne\varnothing.
\]

For \(z\in N\),

\[
\deg(z)\le\ell-1.
\]

For \(z\in U\),

\[
\overline{\deg}(z)
\le
\ell-1+I_n,
\]

where \(I_n\) is the number of isolated vertices outside \(C_n\).

In \(d=3\),

\[
\mathbb E[I_n]
=
\Theta(n^{-1/3}),
\]

so in particular

\[
I_n=0
\]

with probability tending to one.

The argument below does not need this strongest conclusion; \(I_n\le\log n\) is enough.

## 3. Degree and co-degree tails

The low-degree theorem gives

\[
\boxed{
g_3(q)
=
\mu\{Q_3\le q\}
=
O(q^{4/3}).
}
\]

Near either timelike tip,

\[
1-Q_3(x)
=
\frac32 s+O(s^2),
\]

where \(s\) is the tip depth.

The normalized two-tip volume of depth at most \(s\) is

\[
s^3.
\]

Therefore

\[
\boxed{
\bar g_3(r)
:=
\mu\{1-Q_3\le r\}
\sim
\left(\frac23\right)^3r^3
=
\frac{8}{27}r^3.
}
\]

Consequently, if \(\bar D(v)\) is sampled co-degree,

\[
\boxed{
\mathbb E
\#\{v:\bar D(v)\le L\}
\le
C\frac{(L+1)^3}{n^2}
}
\]

uniformly for \(L=o(n)\).

## 4. Small complements

Choose

\[
L_0
=
A\sqrt n\,(\log n)^2.
\]

Then

\[
\frac{L_0^3}{n^2}
=
A^3
\frac{(\log n)^6}{\sqrt n}
\to0.
\]

If

\[
\ell\le L_0,
\]

every \(U\)-vertex has co-degree at most \(2L_0\) for large \(n\).

The sampled co-degree bound gives

\[
\Pr(U\ne\varnothing)\to0.
\]

Since connectedness requires \(U\ne\varnothing\), no such module exists asymptotically.

## 5. Dyadic sublinear range

Now take

\[
L_0<\ell\le\varepsilon_n n.
\]

Use dyadic ranges

\[
\frac L2<\ell\le L
\]

and put

\[
s=\frac Ln.
\]

Then

\[
s\to0
\]

uniformly over the residual range.

## 6. Anticomplete vertices have low continuum degree

Every \(z\in N\) has sampled degree at most \(L\).

For a sufficiently large fixed \(a\), Chernoff concentration gives

\[
\boxed{
N\subseteq
S_{as}
=
\{Q_3\le as\}
}
\]

simultaneously over all dyadic ranges with probability tending to one.

The smallest range has

\[
ns^2
\ge
A^2(\log n)^4,
\]

so the union bounds below have ample exponential margin.

## 7. Complete vertices are much rarer

Every \(u\in U\) has sampled co-degree at most \(2L\).

The co-degree mixture bound gives

\[
\mathbb E|U_{\mathrm{cand}}|
\le
C\frac{L^3}{n^2}
=
Cn s^3.
\]

Use the larger threshold

\[
T_U
=
n s^{5/2}.
\]

Since

\[
s^3=o(s^{5/2}),
\]

Markov gives

\[
\Pr(
|U|>T_U
)
\le
Cs^{1/2}.
\]

Thus, with high probability,

\[
\boxed{
|U|
\le
n s^{5/2}
=
o(ns).
}
\]

## 8. Internal sparsity forces \(N\) one scale deeper

The dimension-independent low-degree internal-sparsity estimate gives

\[
\sup_{x\in S_{as}}
\mu(A_x\cap S_{as})
\le
C_1s^2.
\]

Choose

\[
B>2C_1.
\]

If \(z\in N\) and

\[
Q_3(z)\ge Bs^2,
\]

then the continuum mass of neighbors outside \(S_{as}\) is at least

\[
c_Bs^2.
\]

The sampled number of such high-continuum-degree neighbors has conditional mean

\[
\Theta(ns^2).
\]

But every sampled neighbor of \(z\in N\) lies in \(O\).

Any such neighbor outside \(S_{as}\) cannot be in \(N\), so it must lie in \(U\).

The module condition would therefore require

\[
Y_z
\le
|U|
\le
ns^{5/2}.
\]

Since

\[
ns^{5/2}
=
s^{1/2}(ns^2),
\]

this is a vanishing fraction of the conditional mean.

Chernoff concentration and a union bound yield

\[
\boxed{
N\subseteq
S_{Bs^2}
}
\]

simultaneously with probability tending to one.

## 9. Too few ultra-low vertices

Using

\[
g_3(q)=O(q^{4/3}),
\]

the expected number of sampled points in

\[
S_{Bs^2}
\]

is

\[
O\!\left(
n(s^2)^{4/3}
\right)
=
O(ns^{8/3}).
\]

Relative to the complement size scale

\[
L=ns,
\]

this is

\[
O(s^{5/3})
\to0.
\]

Thus Markov's inequality gives

\[
|N|<\frac L4
\]

simultaneously over all dyadic ranges except on an event whose total probability tends to zero.

Also,

\[
|U|
\le
ns^{5/2}
=
s^{3/2}L
<
\frac L4
\]

for sufficiently large \(n\).

Therefore

\[
|O|
=
|U|+|N|
<
\frac L2,
\]

contradicting

\[
|O|=\ell>\frac L2.
\]

## 10. Conclusion

No sublinear complement survives.

Hence

\[
\boxed{
\Pr\!\left(
\exists\text{ proper non-stable }M\subset C_n:
|C_n\setminus M|=o(n)
\right)
\to0
}
\]

in the precise diagonal-sequence sense stated in Section 1.

The decisive dimensional asymmetry is

\[
\text{low degree: }
g_3(s)=O(s^{4/3}),
\]

versus

\[
\text{near universal: }
\bar g_3(s)=O(s^3),
\]

together with

\[
\mu(A_x\cap S_s)=O(s^2).
\]

## 11. Consequence

The balanced-module theorem excludes modules whose two sides are both linear.

The edge-escalation theorem forces every UPO obstruction to contain a positive-disagreement core edge and therefore to have linear size.

The present theorem excludes the only residual near-whole possibility.

Thus the internal modular obstruction analysis in \(2+1\) is complete.
