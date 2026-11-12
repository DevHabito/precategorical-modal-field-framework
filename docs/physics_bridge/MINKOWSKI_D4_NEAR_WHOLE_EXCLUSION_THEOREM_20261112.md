# Theorem: exclusion of near-whole internal modules in 3+1 Minkowski sprinklings

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem  
**Physical status:** final sublinear-complement obstruction bound for arrow-erased \(3+1\)-dimensional Minkowski causal sets  
**Novelty status:** the concentration tools are standard; the proof uses the project-specific Minkowski degree/co-degree tails and low-degree internal-sparsity geometry

## 1. Statement

Let

\[
G_n=G_{4,n}
\]

be the unoriented comparability graph of an iid size-\(n\) sprinkling into a fixed flat Alexandrov interval of \(\mathbb M^4\).

Let \(C_n\) denote its unique edge-containing component on the high-probability event from the non-isolated giant theorem.

Let

\[
\varepsilon_n\downarrow0
\]

be any deterministic sequence tending to zero sufficiently slowly.

Then

\[
\boxed{
\Pr\!\left(
\exists\text{ proper graph module }M\subset C_n:
1\le |C_n\setminus M|\le\varepsilon_n n,
\;
M\text{ contains an edge}
\right)
\longrightarrow0.
}
\]

Equivalently, a near-whole non-stable internal module cannot survive asymptotically.

Combined with the previous near-whole reduction, this closes the last large-module regime in \(d=4\).

## 2. External types of a module

Suppose

\[
M\subsetneq C_n
\]

is a graph module and define

\[
O=C_n\setminus M,
\qquad
\ell=|O|.
\]

Every vertex of \(O\) is either complete or anticomplete to \(M\).

Write

\[
U
=
\{z\in O:z\text{ is complete to }M\},
\]

and

\[
N
=
\{z\in O:z\text{ is anticomplete to }M\}.
\]

Because \(C_n\) is connected and \(M\) is proper and nonempty,

\[
\boxed{
U\ne\varnothing.
}
\]

For \(z\in N\), every neighbor of \(z\) inside \(C_n\) lies in \(O\), so

\[
\deg(z)\le\ell-1.
\]

For \(z\in U\), every vertex of \(M\) is a neighbor.  Therefore its number of nonneighbors in the full graph is at most

\[
\ell-1+I_n,
\]

where \(I_n\) is the number of isolated vertices outside \(C_n\).

## 3. Isolates are negligible on the present scale

The isolated-vertex theorem gives

\[
\mathbb E[I_n]\to3\pi.
\]

Hence

\[
I_n=O_p(1),
\]

and in particular

\[
\boxed{
\Pr(I_n>\log n)\to0.
}
\]

We work on the event

\[
I_n\le\log n.
\]

## 4. Co-degree tail near the timelike tips

Define the continuum co-degree

\[
R(x)=1-Q_4(x).
\]

Near either timelike tip, write

\[
t=-1+s,
\qquad
r=s\rho
\]

at the past tip, with the time-reflected chart at the future tip.

The exact degree function gives, uniformly in \(\rho\in[0,1]\),

\[
Q_4
=
1-2s+O(s^2).
\]

The normalized volume of the two tip regions of depth at most \(s\) is

\[
4\int_0^s u^3\,du
=
s^4.
\]

Therefore

\[
\boxed{
\bar g_4(r)
:=
\mu\{x:1-Q_4(x)\le r\}
\sim
\frac{r^4}{16}.
}
\]

In particular, for sufficiently small \(r\),

\[
\bar g_4(r)\le Cr^4.
\]

## 5. Sampled small-co-degree bound

Let

\[
\bar D(v)
=
n-1-\deg(v)
\]

be the sampled co-degree.

Conditioned on

\[
R(x)=r,
\]

\[
\bar D
\sim
\operatorname{Binomial}(n-1,r).
\]

The tail estimate

\[
\bar g_4(r)\le Cr^4
\]

implies the uniform mixture bound

\[
\boxed{
\mathbb E
\#\{v:\bar D(v)\le L\}
\le
C\frac{(L+1)^4}{n^3}
}
\]

for

\[
L=o(n).
\]

One way to see this is to split the continuum co-degree at a constant multiple of \(L/n\).

The region below that threshold has measure

\[
O((L/n)^4),
\]

while above it a Chernoff bound contributes an exponentially weighted Stieltjes integral, also \(O(n^{-4})\) after the \(r^4\) tail is inserted.

Multiplication by the \(n\) sampled vertices gives the displayed estimate.

This extends the previously derived universal-vertex asymptotic

\[
\mathbb E[U_n]
\sim
\frac{3}{2n^3}.
\]

## 6. Very small complements are already impossible

Choose

\[
L_0
=
A\sqrt{n\log n}
\]

with a fixed sufficiently large \(A\).

If

\[
\ell\le L_0,
\]

then every vertex of \(U\) has

\[
\bar D(v)
\le
L_0+\log n
\le
2L_0
\]

for large \(n\).

The small-co-degree bound gives

\[
\mathbb E
\#\{v:\bar D(v)\le2L_0\}
=
O\!\left(
\frac{L_0^4}{n^3}
\right)
=
O\!\left(
\frac{\log^2 n}{n}
\right)
\to0.
\]

Thus with probability tending to one no such \(U\)-vertex exists.

Since every proper module in a connected component requires \(U\ne\varnothing\),

\[
\boxed{
\Pr(
\exists M:
1\le|O|\le L_0
)
\to0.
}
\]

## 7. Dyadic treatment of the remaining sublinear range

Now consider

\[
L_0<\ell\le\varepsilon_n n.
\]

Use dyadic ranges

\[
\frac L2<\ell\le L
\]

and write

\[
s=\frac Ln.
\]

The dyadic values satisfy

\[
s\le 2\varepsilon_n
\]

and their sum is \(O(\varepsilon_n)\).

All estimates below are uniform in one such range.

## 8. Low observed degree forces low continuum degree

Every \(z\in N\) satisfies

\[
\deg(z)\le\ell-1\le L.
\]

Choose a fixed constant \(a>2\).

If

\[
Q_4(z)>as,
\]

then the conditional expected sampled degree is at least

\[
(1-o(1))aL.
\]

A Chernoff lower-tail bound gives

\[
\Pr(
\deg(z)\le L
\mid
Q_4(z)>as
)
\le
e^{-c_aL}.
\]

Since

\[
L\ge L_0\gg\log n,
\]

a union bound over all sampled vertices and all dyadic ranges gives

\[
\boxed{
N\subseteq S_{as}
:=
\{x:Q_4(x)\le as\}
}
\]

simultaneously with probability tending to one.

## 9. The complete external type is sparse

Every \(u\in U\) has sampled co-degree at most

\[
\ell-1+I_n
\le
2L
\]

for large \(n\).

Let

\[
H_L
=
\#\{v:\bar D(v)\le2L\}.
\]

The small-co-degree bound gives

\[
\mathbb E[H_L]
\le
C\frac{L^4}{n^3}
=
Cn s^4.
\]

Use the threshold

\[
T_U
=
n s^3.
\]

Then Markov's inequality yields

\[
\Pr(H_L>T_U)
\le
Cs.
\]

Therefore, simultaneously over the dyadic ranges except on an event of total probability \(O(\varepsilon_n)\),

\[
\boxed{
|U|
\le
n s^3.
}
\]

Relative to the complement size \(L=ns\),

\[
\frac{|U|}{L}
\le
s^2
\to0.
\]

Thus the complete external type occupies only a vanishing fraction of a sublinear complement.

## 10. Low-degree internal sparsity forces \(N\) into an ultra-low layer

The low-degree internal-sparsity theorem gives, for sufficiently small \(t\),

\[
\sup_{x\in S_t}
\mu(A_x\cap S_t)
\le
C_0t^2.
\]

Apply this with

\[
t=as.
\]

For \(z\in N\subseteq S_{as}\),

\[
\mu(A_z\cap S_{as})
\le
C_1s^2.
\]

Choose a constant

\[
B>2C_1.
\]

Suppose

\[
Q_4(z)\ge Bs^2.
\]

Then the continuum mass of neighbors of \(z\) lying outside \(S_{as}\) satisfies

\[
\begin{aligned}
p_{\mathrm{high}}(z)
&=
\mu(A_z\setminus S_{as})\\
&\ge
Q_4(z)-C_1s^2\\
&\ge
c_Bs^2.
\end{aligned}
\]

Among the other \(n-1\) sampled points, the number

\[
Y_z
\]

of such high-continuum-degree neighbors is therefore binomial with mean at least

\[
c_Bns^2.
\]

But if \(z\in N\), every sampled neighbor lies in \(O\).

Any neighbor outside \(S_{as}\) cannot belong to \(N\), because \(N\subset S_{as}\).

Hence it must lie in \(U\).

Therefore the module condition requires

\[
Y_z\le|U|
\le
ns^3.
\]

Since

\[
s\to0,
\]

the required upper bound is a vanishing fraction of the conditional mean.

A Chernoff bound gives

\[
\Pr(
Y_z\le ns^3
\mid
Q_4(z)\ge Bs^2
)
\le
e^{-cns^2}.
\]

At the smallest dyadic scale,

\[
ns^2
\ge
\frac{L_0^2}{n}
=
A^2\log n.
\]

Choosing \(A\) sufficiently large, a union bound over all vertices and dyadic ranges tends to zero.

Thus, with probability tending to one,

\[
\boxed{
N
\subseteq
S_{Bs^2}.
}
\]

## 11. There are too few ultra-low vertices

The degree-tail theorem gives

\[
g_4(q)
\le
Cq
\]

for small \(q\).

Therefore

\[
\mathbb E
\#\{v:Q_4(v)\le Bs^2\}
\le
C n s^2.
\]

Since

\[
L=ns,
\]

the expected ratio is

\[
O(s).
\]

Markov's inequality gives

\[
\Pr\!\left(
\#S_{Bs^2}^{\mathrm{sample}}
>
\frac L4
\right)
\le
Cs.
\]

Summing over dyadic scales contributes only

\[
O(\varepsilon_n)
\to0.
\]

Hence simultaneously,

\[
\boxed{
|N|<\frac L4
}
\]

with probability tending to one.

From the previous section,

\[
|U|\le ns^3=s^2L<\frac L4
\]

for all sufficiently large \(n\).

Thus

\[
|O|
=
|U|+|N|
<
\frac L2.
\]

But the dyadic range assumes

\[
|O|=\ell>\frac L2.
\]

This is a contradiction.

## 12. Conclusion

No dyadic sublinear complement survives.

Combining the small-\(\ell\) and dyadic ranges gives

\[
\boxed{
\Pr\!\left(
\exists\text{ proper internal module }M\subset C_n:
1\le|C_n\setminus M|\le\varepsilon_n n
\right)
\to0
}
\]

for every sufficiently slowly decreasing deterministic sequence

\[
\varepsilon_n\downarrow0.
\]

The proof is driven by a mismatch between the two geometric boundary layers:

\[
\boxed{
\text{low degree near the null joint: mass }O(s),
}
\]

whereas

\[
\boxed{
\text{high degree near the timelike tips: mass }O(s^4).
}
\]

The internal-sparsity estimate then forces almost every anticomplete external vertex one scale deeper,

\[
Q=O(s^2),
\]

leaving only \(o(|O|)\) possible vertices of either type.

## 13. Research consequence

The previous reduction theorem showed that any surviving \(d=4\) UPO obstruction must be a near-whole module.

The present theorem eliminates that regime.

Therefore the modular obstruction analysis is now complete.

What remains is only to assemble the already proved component and modular statements into the final \(3+1\) orientation-recovery theorem and audit the logical dependencies one more time before promoting

\[
p_4^{\mathrm{UPO}}(n)\to1
\]

to theorem status.
