# Universal vertices and the timelike-tip large-module asymptotic

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** analytic asymptotic + finite-n quadrature validation  
**Physical status:** boundary diagnostic for arrow-erased Minkowski causal-set comparability graphs  
**Novelty status:** causal-set "posts" are established terminology in other stochastic causet models; the fixed-Alexandrov-interval asymptotic below was not located in the targeted review, but absolute priority is not certified

## 1. Why universal vertices matter here

The splitter-closure reduction controls modules of arbitrary size by starting from an edge.

A separate large-module risk occurs when a connected comparability graph contains a universal vertex \(x\): a vertex adjacent to every other vertex.

Then

\[
V\setminus\{x\}
\]

is a graph module.

If that complement contains an edge, it is a non-stable module and obstructs UPO.

Thus universal vertices are the simplest mechanism that can generate a module of size

\[
n-1.
\]

They are geometrically different from the null-joint true-twin obstruction.

## 2. Exact expectation

Let

\[
Q_d(x)
=
\mu(A_x)
\]

be the normalized volume fraction of the Alexandrov diamond causally comparable to \(x\).

For the unit-height diamond

\[
D=I((-1,\mathbf0),(1,\mathbf0))
\subset\mathbb M^d,
\]

\[
Q_d(t,r)
=
\frac{
\left((1+t)^2-r^2\right)^{d/2}
+
\left((1-t)^2-r^2\right)^{d/2}
}{
2^d
}.
\]

Conditioned on a sampled point \(X=x\), that point is universal exactly when all remaining \(n-1\) iid points lie in \(A_x\).

Therefore, if \(U_n\) is the number of universal vertices,

\[
\boxed{
\mathbb E[U_n]
=
n\,
\mathbb E
\left[
Q_d(X)^{n-1}
\right].
}
\]

This identity is exact.

## 3. The maxima of \(Q_d\)

Inside the open diamond,

\[
Q_d(x)<1.
\]

The value \(Q_d=1\) is reached only at the two timelike tips

\[
p=(-1,\mathbf0),
\qquad
q=(1,\mathbf0),
\]

where the event is causally comparable to the entire diamond.

Thus the large-\(n\) expectation is a two-tip Laplace problem.

## 4. Coordinates near one tip

Near the past tip write

\[
t=-1+s,
\qquad
0\le s\le1,
\]

and

\[
r=s\rho,
\qquad
0\le\rho\le1.
\]

The two endpoint proper-time squares are

\[
\tau(p,x)^2
=
s^2(1-\rho^2),
\]

and

\[
\tau(x,q)^2
=
(2-s)^2-s^2\rho^2.
\]

Hence

\[
Q_d(s,\rho)
=
\frac{
s^d(1-\rho^2)^{d/2}
+
\left(
(2-s)^2-s^2\rho^2
\right)^{d/2}
}{
2^d
}.
\]

Uniformly for \(\rho\in[0,1]\),

\[
\boxed{
Q_d(s,\rho)
=
1-\frac d2\,s+O(s^2)
}
\]

as

\[
s\downarrow0.
\]

## 5. Normalized volume element near the tip

Let \(V_{d-1}\) be the Euclidean volume of the unit \((d-1)\)-ball.

The full Alexandrov diamond has volume

\[
\frac{2V_{d-1}}{d}.
\]

Using spherical coordinates in the spatial section and then \(r=s\rho\), the normalized spacetime measure is

\[
\boxed{
d\mu
=
\frac{d(d-1)}2
s^{d-1}
\rho^{d-2}\,
ds\,d\rho
}
\]

after the angular directions have been integrated out.

## 6. Laplace scaling

Set

\[
s=\frac zn.
\]

Then

\[
Q_d\!\left(\frac zn,\rho\right)^{n-1}
\longrightarrow
e^{-dz/2}
\]

for every fixed \(z,\rho\).

The measure contributes

\[
n^{-d},
\]

while the outer count in

\[
\mathbb E[U_n]
\]

contributes \(n\).

The two tips contribute equally.

Therefore

\[
\begin{aligned}
\mathbb E[U_n]
&\sim
n^{1-d}
\,
d
\int_0^\infty
z^{d-1}e^{-dz/2}\,dz\\
&=
n^{1-d}
\,
d
\frac{\Gamma(d)}{(d/2)^d}.
\end{aligned}
\]

Thus

\[
\boxed{
\mathbb E[U_n]
\sim
\frac{
2^d\Gamma(d)
}{
d^{\,d-1}
}
n^{1-d}.
}
\]

No fitted parameter appears.

## 7. The 3+1 result

For spacetime dimension

\[
d=4,
\]

the coefficient is

\[
\frac{
2^4\Gamma(4)
}{
4^3
}
=
\frac{16\cdot6}{64}
=
\frac32.
\]

Therefore

\[
\boxed{
\mathbb E[U_n]
\sim
\frac{3}{2n^3}.
}
\]

This is one power of \(n\) smaller than the induced-\(P_3\) module scale

\[
\Theta(n^{-2}),
\]

and two powers smaller than the true-twin scale

\[
\frac{9\pi}{n}.
\]

Hence this simplest nearly macroscopic module mechanism cannot control the leading \(d=4\) UPO failure probability.

## 8. Finite-n quadrature check

The repository tool

tools/minkowski_universal_vertex_tip_asymptotic.py

numerically integrates the exact expectation.

For \(d=4\):

| \(n\) | \(n^3\mathbb E[U_n]\) |
|---:|---:|
|10|1.505336|
|20|1.501103|
|50|1.500160|
|100|1.500039|
|200|1.500010|
|500|1.500002|
|1000|1.5000004|

The convergence to

\[
\frac32
\]

is already visible at small \(n\).

The quadrature is a validation check only.

The asymptotic coefficient comes from the tip expansion above.

## 9. Relation to causal-set "posts"

Causal-set literature uses the word **post** for an element comparable to every other element in the causet.

Posts are especially important in classical sequential-growth and transitive-percolation models.

That established use is not the result studied here.

The ensemble in this note is different:

- a fixed flat Alexandrov interval;
- iid uniform sprinkling conditioned on cardinality \(n\);
- continuum causal order inherited from Minkowski geometry.

The result concerns the finite-window probability of a post/universal vertex in that geometry-induced ensemble.

A targeted search did not locate the asymptotic

\[
\frac{
2^d\Gamma(d)
}{
d^{d-1}
}
n^{1-d}
\]

for this setting.

This is limited negative evidence only.

## 10. Boundary hierarchy

The current higher-dimensional reconstruction program now contains three geometrically distinct boundary mechanisms.

### Null-waist isolated vertices

\[
\mathbb E[I_n]
\sim
d(d-1)
\Gamma\!\left(1+\frac2d\right)^2
n^{1-4/d}.
\]

### Null-joint true-twin modules in \(d=4\)

\[
\mathbb E[T_n]
\sim
\frac{9\pi}{n}.
\]

### Timelike-tip universal vertices

\[
\mathbb E[U_n]
\sim
\frac{
2^d\Gamma(d)
}{
d^{d-1}
}
n^{1-d}.
\]

These are different geometric loci and different combinatorial effects.

In \(d=4\), the orders are

\[
\mathbb E[I_n]=\Theta(1),
\]

\[
\mathbb E[T_n]=\Theta(n^{-1}),
\]

\[
\mathbb E[U_n]=\Theta(n^{-3}).
\]

Only the first concerns isolated events, which do not by themselves create extra orientation choices.

The latter two concern potential non-stable modular structure.

## 11. Current consequence

The universal-vertex calculation removes the simplest \(n-1\)-sized obstruction from contention as a leading mechanism.

The remaining global problem is narrower:

> can a mesoscopic or macroscopic proper edge-generated module survive without being generated by a universal-tip configuration?

The splitter-closure audit has not observed such modules at large tested \(n\), but a uniform analytic cascade bound is still required before concluding

\[
p_4^{\mathrm{UPO}}(n)\to1.
\]
