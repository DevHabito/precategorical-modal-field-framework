# Theorem: all-dimensional exclusion of near-whole internal modules for d >= 3

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem for every fixed integer spacetime dimension \(d\ge3\)  
**Physical status:** final sublinear-complement module bound for arrow-erased flat Minkowski sprinklings  
**Novelty status:** concentration inequalities and modular terminology are standard; the project-specific input is the Minkowski degree/co-degree geometry and its iterative low-degree sparsity mechanism

## 1. Statement

Fix an integer spacetime dimension

\[
d\ge3.
\]

Let

\[
G_{d,n}
\]

be the unoriented causal-comparability graph of \(n\) iid uniform points in a fixed flat Alexandrov interval of \(\mathbb M^d\).

On the high-probability event supplied by the non-isolated giant theorem, let

\[
C_{d,n}
\]

be the unique connected component containing an edge.

For every deterministic sequence

\[
\varepsilon_n\downarrow0,
\]

\[
\boxed{
\Pr\!\left(
\exists\text{ proper graph module }M\subset C_{d,n}:
1\le |C_{d,n}\setminus M|\le \varepsilon_n n,
\;
M\text{ contains an edge}
\right)
\longrightarrow0.
}
\]

Thus a non-stable internal module cannot occupy all but a sublinear exceptional set.

## 2. External types of a module

Let

\[
M\subsetneq C_{d,n}
\]

be a proper module and define

\[
O=C_{d,n}\setminus M,
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

Because \(C_{d,n}\) is connected and \(M\) is nonempty and proper,

\[
\boxed{U\ne\varnothing.}
\]

For \(z\in N\),

\[
\deg_{G_{d,n}}(z)\le \ell-1.
\]

For \(z\in U\), every vertex of \(M\) is a neighbor, so its sampled co-degree in the full graph satisfies

\[
\overline{\deg}(z)
\le
\ell-1+I_n,
\]

where \(I_n\) is the number of isolated vertices outside \(C_{d,n}\).

## 3. Low-degree tail

The all-dimensional Minkowski degree-tail theorem gives

\[
\boxed{
g_d(q)
:=
\mu\{x:Q_d(x)\le q\}
\le
C_dq^{4/d}
}
\]

for sufficiently small \(q\).

Here

\[
Q_d(x)=\mu(A_x)
\]

is the causal-comparability graphon degree.

## 4. Near-universal co-degree tail

Define

\[
R_d(x)=1-Q_d(x).
\]

Near the past timelike tip use

\[
t=-1+s,
\qquad
r=s\rho,
\qquad
0\le\rho\le1.
\]

Uniformly in \(\rho\),

\[
Q_d(s,\rho)
=
1-\frac d2\,s+O(s^2).
\]

The normalized volume of the two tip regions of depth at most \(s\) is exactly

\[
s^d.
\]

Therefore

\[
\boxed{
\bar g_d(r)
:=
\mu\{x:R_d(x)\le r\}
\sim
\left(\frac2d\right)^d r^d.
}
\]

In particular,

\[
\bar g_d(r)\le C_dr^d
\]

for small \(r\).

## 5. Sampled small-co-degree mixture bound

Let

\[
\bar D(v)=n-1-\deg(v)
\]

be sampled co-degree.

Conditioned on continuum co-degree \(R=r\),

\[
\bar D
\sim
\operatorname{Binomial}(n-1,r).
\]

For an integer \(L<n-1\), put

\[
h_L(r)
=
\Pr(
\operatorname{Binomial}(n-1,r)\le L
).
\]

The function \(h_L\) is decreasing.

Because the continuum co-degree distribution satisfies

\[
\bar g_d(r)\le Cr^d
\]

globally after increasing \(C\), Stieltjes integration by parts gives

\[
\mathbb E[h_L(R)]
\le
C
\int_0^1
r^d(-h_L'(r))\,dr.
\]

For

\[
N=n-1,
\]

the binomial-CDF derivative is

\[
-h_L'(r)
=
(N-L)
\binom NL
r^L(1-r)^{N-L-1}.
\]

Hence

\[
\begin{aligned}
\int_0^1
r^d(-h_L'(r))\,dr
&=
\frac{
(L+1)(L+2)\cdots(L+d)
}{
(N+1)(N+2)\cdots(N+d)
}.
\end{aligned}
\]

Multiplying by the \(n\) sampled vertices yields the uniform bound

\[
\boxed{
\mathbb E
\#\{v:\bar D(v)\le L\}
\le
C_d
\frac{(L+d)^d}{n^{d-1}}.
}
\]

This is the general-dimensional version of the \(d=3\) and \(d=4\) tip bounds.

## 6. Parameter choice

Let

\[
r=2^J
\]

be the smallest power of two satisfying

\[
\boxed{r>\frac d4.}
\]

For every integer \(d\ge3\),

\[
r<d.
\]

Choose constants

\[
\boxed{
1-\frac1r<a<1-\frac1d
}
\]

and

\[
\boxed{
r<\gamma<d.
}
\]

Set

\[
L_0
=
n^a(\log n)^2.
\]

The first inequality gives

\[
n\left(\frac{L_0}{n}\right)^r
=
n^{1-r(1-a)}(\log n)^{2r}
\gg
\log n.
\]

The second upper bound on \(a\) gives

\[
\frac{L_0^d}{n^{d-1}}
\to0.
\]

Finally, because

\[
r>\frac d4,
\]

we have

\[
a>1-\frac1r>1-\frac4d.
\]

The isolated-vertex theorem

\[
\mathbb E[I_n]
=
O(n^{1-4/d})
\]

therefore implies

\[
\boxed{
\Pr(I_n>L_0)\to0.
}
\]

This point is essential for \(d>4\), where the number of isolated vertices is not tight.

## 7. Very small complements

Work on the event

\[
I_n\le L_0.
\]

If

\[
1\le\ell\le L_0,
\]

then every \(u\in U\) has sampled co-degree at most

\[
\ell-1+I_n
\le
2L_0.
\]

The sampled co-degree bound gives

\[
\mathbb E
\#\{v:\bar D(v)\le2L_0\}
\le
C_d
\frac{L_0^d}{n^{d-1}}
\to0.
\]

Thus, with probability tending to one, no \(U\)-vertex exists.

But a proper module inside a connected component requires

\[
U\ne\varnothing.
\]

Therefore

\[
\boxed{
\Pr(
\exists M:
1\le|C_{d,n}\setminus M|\le L_0
)
\to0.
}
\]

## 8. Dyadic sublinear ranges

It remains to consider

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

Then

\[
s\le2\varepsilon_n\to0.
\]

All estimates below are uniform within one dyadic range.

## 9. Anticomplete vertices enter the first low-degree layer

Every \(z\in N\) has sampled degree at most

\[
L.
\]

Fix a sufficiently large constant \(A_0>1\).

If

\[
Q_d(z)>A_0s,
\]

the conditional mean sampled degree is at least a fixed multiple of \(L\).

A Chernoff lower-tail bound gives

\[
\Pr(
\deg(z)\le L
\mid
Q_d(z)>A_0s
)
\le
e^{-cL}.
\]

Since

\[
L\ge L_0\gg\log n,
\]

a union bound over all vertices and all dyadic ranges yields

\[
\boxed{
N\subseteq S_{C_0s}
}
\]

simultaneously with probability tending to one, where

\[
S_t=\{x:Q_d(x)\le t\}.
\]

## 10. Complete vertices are sparse

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

The co-degree mixture bound gives

\[
\mathbb E[H_L]
\le
C_dn s^d.
\]

Use the threshold

\[
T_U
=
n s^\gamma,
\]

where

\[
r<\gamma<d.
\]

Markov's inequality gives

\[
\Pr(
H_L>T_U
)
\le
C_ds^{d-\gamma}.
\]

Summing over the dyadic ranges gives total failure probability

\[
O(
\varepsilon_n^{d-\gamma}
)
\to0.
\]

Thus, simultaneously over all residual scales,

\[
\boxed{
|U|
\le
n s^\gamma.
}
\]

Because \(\gamma>1\),

\[
|U|=o(ns)=o(L).
\]

## 11. Iterative low-degree descent for \(N\)

The dimension-independent internal-sparsity theorem gives

\[
\boxed{
\sup_{x\in S_t}
\mu(A_x\cap S_t)
\le
C_dt^2.
}
\]

Start with

\[
t_0=C_0s.
\]

Suppose inductively that

\[
N\subseteq S_{t_j}
\]

with

\[
t_j=C_js^{r_j},
\qquad
r_j=2^j.
\]

If \(J=0\), no iteration is needed.

Otherwise consider \(j<J\).

Choose \(C_{j+1}\) sufficiently large.

If \(z\in N\) satisfies

\[
Q_d(z)>C_{j+1}s^{2r_j},
\]

then

\[
\begin{aligned}
\mu(
A_z\setminus S_{t_j}
)
&\ge
Q_d(z)
-
\mu(A_z\cap S_{t_j})\\
&\ge
c_js^{2r_j}.
\end{aligned}
\]

Among the other sampled vertices, the number \(Y_z\) of neighbors in

\[
D\setminus S_{t_j}
\]

therefore has conditional mean at least

\[
c_jn s^{2r_j}.
\]

Since \(z\in N\), every sampled neighbor of \(z\) lies in

\[
O=U\cup N.
\]

But all \(N\)-vertices lie in \(S_{t_j}\).

Therefore every sampled neighbor outside \(S_{t_j}\) must belong to \(U\), and the module condition requires

\[
Y_z\le|U|
\le
ns^\gamma.
\]

Because

\[
\gamma>r\ge2r_j,
\]

\[
ns^\gamma
=
o(
n s^{2r_j}
).
\]

A Chernoff bound gives

\[
\Pr(
Y_z\le ns^\gamma
)
\le
\exp(
-c_jn s^{2r_j}
).
\]

The weakest exponent occurs at the final iteration, where

\[
2r_j=r.
\]

At the smallest dyadic scale,

\[
n s^r
\ge
n(L_0/n)^r
\gg
\log n.
\]

Hence a union bound over all vertices, all iterations, and all dyadic scales tends to zero.

Thus the induction closes:

\[
\boxed{
N\subseteq S_{C_Js^r}.
}
\]

## 12. Too few final low-degree candidates

The low-degree tail gives

\[
\mathbb E
\#\{
v:Q_d(v)\le C_Js^r
\}
\le
C_dn s^{4r/d}.
\]

Since

\[
r>\frac d4,
\]

\[
\theta_d
:=
\frac{4r}{d}-1
>
0.
\]

Relative to

\[
L=ns,
\]

the expected fraction is

\[
O(s^{\theta_d}).
\]

Markov gives

\[
\Pr\!\left(
\#S_{C_Js^r}^{\mathrm{sample}}
>
\frac L4
\right)
\le
C_ds^{\theta_d}.
\]

Summing over dyadic ranges contributes

\[
O(
\varepsilon_n^{\theta_d}
)
\to0.
\]

Therefore

\[
\boxed{
|N|<\frac L4
}
\]

simultaneously with probability tending to one.

Also,

\[
|U|
\le
ns^\gamma
=
s^{\gamma-1}L
<
\frac L4
\]

for all sufficiently large \(n\).

Hence

\[
|O|
=
|U|+|N|
<
\frac L2,
\]

contradicting the dyadic assumption

\[
|O|=\ell>\frac L2.
\]

## 13. Conclusion

The very-small and dyadic ranges exhaust

\[
1\le|O|\le\varepsilon_n n.
\]

Therefore

\[
\boxed{
\Pr\!\left(
\exists\text{ proper non-stable internal module }M:
1\le|C_{d,n}\setminus M|\le\varepsilon_n n
\right)
\to0
}
\]

for every fixed integer

\[
d\ge3.
\]

## 14. Dimensional mechanism

The proof works because three exponents are compatible:

### Low-degree joint layer

\[
g_d(s)
=
O(s^{4/d}).
\]

### Near-universal tip layer

\[
\bar g_d(s)
=
O(s^d).
\]

### Internal low-degree neighbor mass

\[
\sup_{x\in S_s}
\mu(A_x\cap S_s)
=
O(s^2).
\]

Repeated use of the third estimate sends

\[
s
\longmapsto
s^2
\longmapsto
s^4
\longmapsto\cdots
\]

until the low-degree-tail exponent becomes greater than one.

The number of squarings needed is the smallest \(J\) such that

\[
2^J>\frac d4.
\]

This is finite for every fixed dimension.

## 15. Consequence

The all-dimensional edge-tail theorem already proves that for every fixed

\[
d\ge3
\]

each implication class reaches a positive-disagreement core edge.

Such a core edge has a linear number of sampled splitters and therefore forces every containing non-stable module to have linear size.

Causal-graphon primeness excludes balanced linear modules.

The present theorem excludes the only residual near-whole regime.

Thus all ingredients needed for the full fixed-\(d\ge3\) orientation-recovery theorem are now available.
