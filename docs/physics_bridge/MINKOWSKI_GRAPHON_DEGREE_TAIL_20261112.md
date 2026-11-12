# Degree-tail theorem for Minkowski causal graphons

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem + finite-n quadrature regression + literature bridge  
**Physical status:** graphon reformulation of arrow-erased Minkowski sprinklings  
**Novelty status:** no equivalent closed degree-tail asymptotic for this causal-comparability graphon was located in the targeted review; absolute priority is not certified

## 1. Causal comparability graphon

Let \(D\subset\mathbb M^d\) be the unit Alexandrov interval

\[
D=I((-1,\mathbf0),(1,\mathbf0))
\]

with normalized volume measure \(\mu\).

Define

\[
W_d(x,y)
=
\mathbf1_{\{x\sim y\}},
\]

where \(x\sim y\) means that the two events are causally comparable.

The graphon degree is

\[
\deg_{W_d}(x)
=
Q_d(x)
=
\mu\{y:y\sim x\}.
\]

For \(q>0\), define the low-degree mass

\[
g_d(q)
=
\mu\{x:Q_d(x)\le q\}.
\]

## 2. Exact degree function in null-waist coordinates

Use

\[
a=1-r+t,
\qquad
b=1-r-t,
\]

so that

\[
a\ge0,
\qquad
b\ge0,
\qquad
a+b\le2.
\]

The null waist is

\[
a=b=0.
\]

The exact graphon degree is

\[
\boxed{
Q_d(a,b)
=
2^{-d}
\left(
[a(2-b)]^{d/2}
+
[b(2-a)]^{d/2}
\right).
}
\]

After angular variables are integrated out, the normalized measure is

\[
\boxed{
d\mu_d
=
\frac{d(d-1)}4
\left(
1-\frac{a+b}{2}
\right)^{d-2}
da\,db.
}
\]

## 3. Small-degree blow-up

Let

\[
m=\frac d2.
\]

Near the waist,

\[
Q_d(a,b)
=
2^{-m}(a^m+b^m)
+
o(a^m+b^m).
\]

Set

\[
a=2q^{1/m}x,
\qquad
b=2q^{1/m}y.
\]

Since

\[
\frac1m=\frac2d,
\]

the Jacobian is

\[
da\,db
=
4q^{4/d}\,dx\,dy.
\]

The condition

\[
Q_d(a,b)\le q
\]

converges to

\[
x^m+y^m\le1.
\]

The positive-quadrant volume of this \(\ell_m\)-ball is

\[
\int_{\substack{x,y\ge0\\x^m+y^m\le1}}
dx\,dy
=
\frac{
\Gamma(1+1/m)^2
}{
\Gamma(1+2/m)
}.
\]

Therefore

\[
\boxed{
g_d(q)
\sim
C_d\,q^{4/d},
}
\]

where

\[
\boxed{
C_d
=
d(d-1)
\frac{
\Gamma(1+2/d)^2
}{
\Gamma(1+4/d)
}.
}
\]

## 4. Dimension-specific cases

### \(d=2\)

\[
C_2=1,
\qquad
g_2(q)\sim q^2.
\]

### \(d=3\)

\[
C_3
=
6
\frac{
\Gamma(5/3)^2
}{
\Gamma(7/3)
}
\approx
4.1067804359,
\]

so

\[
g_3(q)
\sim
C_3q^{4/3}
=
o(q).
\]

### \(d=4\)

\[
C_4
=
12
\Gamma(3/2)^2
=
3\pi.
\]

Hence

\[
\boxed{
g_4(q)
\sim
3\pi q.
}
\]

Thus \(3+1\) Minkowski spacetime lies exactly at the critical graphon degree-tail regime

\[
\frac{g_4(q)}q
\longrightarrow
3\pi.
\]

### \(d>4\)

Since

\[
\frac4d<1,
\]

\[
\frac{g_d(q)}q
\to\infty.
\]

The dimension-four transition is therefore visible directly at the graphon-degree level.

## 5. Recovery of the isolated-vertex asymptotic

Let \(I_n\) be the number of isolated vertices.

Conditioned on \(X=x\),

\[
\Pr(X\text{ isolated}\mid X=x)
=
(1-Q_d(x))^{n-1}.
\]

Therefore

\[
\mathbb E[I_n]
=
n\,
\mathbb E[
(1-Q_d(X))^{n-1}
].
\]

From

\[
g_d(q)
\sim
C_dq^{4/d}
\]

and a Laplace-Stieltjes asymptotic,

\[
\mathbb E[I_n]
\sim
C_d
\Gamma\!\left(1+\frac4d\right)
n^{1-4/d}.
\]

Using the expression for \(C_d\),

\[
\boxed{
\mathbb E[I_n]
\sim
d(d-1)
\Gamma\!\left(1+\frac2d\right)^2
n^{1-4/d}.
}
\]

This recovers the earlier isolated-vertex theorem from a more general graphon-degree statement.

In \(d=4\),

\[
\boxed{
\mathbb E[I_n]\to3\pi.
}
\]

## 6. Fixed finite graph degrees

Let \(D_j\) denote the number of sampled vertices of graph degree exactly \(j\).

Conditioned on a point with graphon degree \(Q=q\),

\[
\deg_{G_n}(v)
\sim
\operatorname{Binomial}(n-1,q).
\]

Therefore

\[
\mathbb E[D_j]
=
n
\mathbb E
\left[
\binom{n-1}{j}
Q^j
(1-Q)^{n-1-j}
\right].
\]

If

\[
g_d(q)
\sim
C_dq^\alpha,
\qquad
\alpha=\frac4d,
\]

then

\[
\boxed{
\mathbb E[D_j]
\sim
C_d
\alpha
\frac{
\Gamma(j+\alpha)
}{
j!
}
n^{1-\alpha}.
}
\]

Equivalently,

\[
\boxed{
\mathbb E[D_j]
\sim
C_d
\frac4d
\frac{
\Gamma(j+4/d)
}{
j!
}
n^{1-4/d}.
}
\]

## 7. Critical simplification in 3+1

For

\[
d=4,
\]

we have

\[
\alpha=1,
\qquad
C_4=3\pi.
\]

Thus for every fixed

\[
j=0,1,2,\ldots,
\]

\[
\boxed{
\mathbb E[D_j]
\longrightarrow
3\pi.
}
\]

This includes the isolated count \(j=0\), but it is stronger:

> every fixed finite degree has the same asymptotic expected count.

The finite-\(n\) approach is slow for larger \(j\), as expected from the critical boundary layer.

The repository script

tools/minkowski_graphon_degree_tail.py

evaluates the exact finite-\(n\) integral as a regression.

For example, in \(d=4\):

| \(n\) | \(\mathbb E[D_0]\) | \(\mathbb E[D_1]\) | \(\mathbb E[D_2]\) | \(\mathbb E[D_3]\) |
|---:|---:|---:|---:|---:|
|20|6.5447|4.6781|3.1611|2.0298|
|50|7.7657|6.8071|5.9803|5.1898|
|100|8.2917|7.6782|7.1871|6.7512|
|200|8.6398|8.2273|7.9061|7.6294|

All four columns approach

\[
3\pi
=
9.4247779608\ldots
\]

from below.

The quadrature is diagnostic only.

## 8. Connectedness of the continuum graphon

The causal-comparability graphon \(W_d\) is connected in the graphon sense.

A useful stronger observation is:

> for any two interior points \(x,y\in D\), there is a positive-volume set of events \(z\) that are causally comparable to both.

Indeed, the future tip \(q\) is timelike to every interior point.

By openness of the timelike relation, a sufficiently small interior neighborhood below \(q\) lies in both futures

\[
I^+(x)\cap I^+(y).
\]

Hence

\[
\int_D
W_d(x,z)W_d(z,y)
\,d\mu(z)
>
0
\]

for almost every \(x,y\).

A measurable graphon partition with zero cross-edge mass would force the two-step kernel above to vanish across the two parts, which is impossible.

Therefore \(W_d\) is connected.

## 9. Consequence in 2+1 spacetime

Hladký and Viswanathan prove that if a graphon \(W\) is connected and

\[
\frac{g_W(q)}q
\to0,
\]

then for every fixed \(K\),

\[
G(n,W)
\]

is asymptotically almost surely \(K\)-connected.

For \(d=3\),

\[
g_3(q)
=
\Theta(q^{4/3})
=
o(q).
\]

Therefore their theorem applies directly:

\[
\boxed{
\text{For every fixed }K,
\quad
G(n,W_3)
\text{ is a.a.s. }K\text{-connected}.
}
\]

This closes the component-ambiguity problem asymptotically in \(2+1\).

It does not by itself prove UPO, because internal non-stable modules remain a separate issue.

## 10. The critical 3+1 regime

For \(d=4\),

\[
\frac{g_4(q)}q
\to3\pi\in(0,\infty).
\]

This is precisely the critical degree-tail regime that is not covered by the main connectivity theorem of Hladký and Viswanathan.

Their 2026 paper explicitly notes that this finite-positive limit is subtler, and their Conjecture 14 proposes that for connected graphons, fixed-order vertex-connectivity failures should asymptotically be explained by the corresponding minimum-degree failures.

The present Minkowski kernel therefore supplies a concrete geometric graphon in that unresolved regime.

Our earlier simulations suggest that, in this kernel, nontrivial components outside the giant disappear while isolated vertices persist.

That statement is still not promoted to theorem.

## 11. Giant-component consequence

Janson's connected-graphon theorem implies

\[
\frac{
|C_1(G(n,W_d))|
}{n}
\overset{p}{\longrightarrow}
1.
\]

Therefore for every finite \(d\), and in particular for \(d=4\),

\[
\boxed{
\text{all vertices outside the largest component are }o_p(n).
}
\]

This rules out a second linear-sized component.

Combined with the current fixed-size component audits, it narrows the unresolved \(d=4\) component problem to genuinely mesoscopic scales.

## 12. Literature boundary

The graphon notions and general connectivity theorems are established.

Relevant sources include:

- Svante Janson, **Connectedness in graph limits**, *European Journal of Combinatorics* 29 (2008), 1195–1211.
- Jan Hladký and Gopal Viswanathan, **Connectivity of Inhomogeneous Random Graphs II**, *Random Structures & Algorithms* 69 (2026), e70098, DOI 10.1002/rsa.70098.
- Mathew D. Penrose, **Inhomogeneous random graphs, isolated vertices, and Poisson approximation**, *Journal of Applied Probability* 55 (2018), 112–136, DOI 10.1017/jpr.2018.9.

Penrose gives general Poisson-approximation criteria for low-degree vertices and fixed-size components, but his broad theorems impose conditions such as homogeneity or connection probabilities bounded away from one that do not directly cover this deterministic \(0/1\) Minkowski graphon.

No existing source located in the targeted review states the closed Minkowski causal-graphon tail

\[
g_d(q)
\sim
d(d-1)
\frac{
\Gamma(1+2/d)^2
}{
\Gamma(1+4/d)
}
q^{4/d},
\]

or the critical consequence

\[
\mathbb E[D_j]\to3\pi
\]

for every fixed \(j\) in \(3+1\).

This remains limited negative evidence only.

## 13. Current research consequence

The global \(3+1\) UPO problem now has three separate scale regimes.

### Microscopic modular defects

Already controlled at the first levels:

\[
\mathbb E[T_n]
\sim
\frac{9\pi}{n},
\]

\[
\mathbb E[M_{3,n}]
=
\Theta(n^{-2}).
\]

### Macroscopic component separation

Ruled out by connected graphon theory:

\[
|C_1|/n\to1
\]

in probability.

### Remaining gap

The unresolved component and modular obstruction scales are mesoscopic:

\[
1\ll k\ll n.
\]

The next analytic target is therefore a uniform mesoscopic bound, not another fixed-\(k\) enumeration.
