# Theorem: near-universal tip tail in a regular curved 2+1 causal diamond

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem under temporal tip-gradient hypotheses  
**Physical status:** curved-spacetime co-degree tail required for near-whole module exclusion

## 1. Setting

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth \(2+1\)-dimensional Lorentzian spacetime.

Use normalized physical volume measure

\[
\mu
=
\frac{
d\operatorname{Vol}_g
}{
V_D
},
\qquad
V_D
=
\operatorname{Vol}_g(D).
\]

Let

\[
Q(x)
=
\mu(A_x)
\]

be the causal-comparability graphon degree and define the co-degree

\[
R(x)
=
1-Q(x).
\]

Assume \(R\) extends \(C^2\)-regularly to the two timelike tips \(p,q\) from inside \(D\), and that its first derivatives there are nonzero timelike covectors.

## 2. Exact degree identity

For every interior point,

\[
Q(x)
=
\mathcal V(p,x)
+
\mathcal V(x,q).
\]

Hence

\[
R(x)
=
1
-
\mathcal V(p,x)
-
\mathcal V(x,q).
\]

At the past tip,

\[
Q(p)=1,
\qquad
R(p)=0,
\]

in the limiting sense.

Similarly,

\[
R(q)=0.
\]

## 3. Tip differential

Near \(p\),

\[
\mathcal V(p,x)
=
O(
d_g(p,x)^3
)
\]

for timelike \(x\to p\).

Therefore its first derivative at \(p\) vanishes.

Hence

\[
dR_p
=
-
d_x
\mathcal V(x,q)
\big|_{x=p}.
\]

Equivalently, for the volume-difference function

\[
\Phi(x)
=
\mathcal V(p,x)
-
\mathcal V(x,q),
\]

\[
\boxed{
dR_p
=
d\Phi_p.
}
\]

At \(q\), the analogous relation holds up to the time-orientation sign.

Thus the same volume-time gradient that controls the bulk small-disagreement statistic also controls the near-universal tip layer.

## 4. Temporal tip-gradient norm

Define

\[
\kappa_p
=
\sqrt{
-g^{-1}_p(
dR_p,dR_p
)
},
\]

and similarly

\[
\kappa_q.
\]

By hypothesis,

\[
\kappa_p,\kappa_q>0.
\]

Choose a local Lorentz frame at \(p\) in which

\[
dR_p
=
\kappa_p\,dh^0
\]

on future-timelike displacements.

Then

\[
R(\exp_p h)
=
\kappa_p h^0
+
O(|h|^2).
\]

## 5. Past-tip sublevel volume

The region

\[
R(x)\le r
\]

near \(p\) is, to leading order,

\[
0<h^0\le\frac r{\kappa_p},
\qquad
|\mathbf h|<h^0.
\]

In \(2+1\), its physical spacetime volume is

\[
\int_0^{r/\kappa_p}
\pi(h^0)^2\,dh^0
=
\frac{\pi}{3}
\frac{r^3}{\kappa_p^3}.
\]

After normalization,

\[
\boxed{
\mu\{
x\text{ near }p:
R(x)\le r
\}
\sim
\frac{
\pi
}{
3V_D
}
\kappa_p^{-3}
r^3.
}
\]

## 6. Future tip

The same argument at \(q\) gives

\[
\boxed{
\mu\{
x\text{ near }q:
R(x)\le r
\}
\sim
\frac{
\pi
}{
3V_D
}
\kappa_q^{-3}
r^3.
}
\]

Away from the two tips, \(R\) is bounded below by a positive constant on compact subsets.

Therefore the two tip contributions exhaust the small-co-degree tail.

## 7. Co-degree tail

Define

\[
\bar g_3(r)
=
\mu\{x:R(x)\le r\}.
\]

Then

\[
\boxed{
\bar g_3(r)
\sim
C_{\mathrm{tip}}
r^3,
}
\]

where

\[
\boxed{
C_{\mathrm{tip}}
=
\frac{
\pi
}{
3V_D
}
\left(
\kappa_p^{-3}
+
\kappa_q^{-3}
\right).
}
\]

Thus the exponent

\[
\boxed{
3
}
\]

is universal over the stated regular curved class.

## 8. Sampled small-co-degree bound

Let

\[
\bar D(v)
=
n-1-\deg(v)
\]

be sampled co-degree.

Conditioned on continuum co-degree \(R=r\),

\[
\bar D
\sim
\operatorname{Binomial}(n-1,r).
\]

The tail

\[
\bar g_3(r)
=
O(r^3)
\]

gives the mixture bound

\[
\boxed{
\mathbb E
\#\{
v:
\bar D(v)\le L
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

uniformly for

\[
L=o(n).
\]

The proof is the same Stieltjes/binomial-CDF integration used in the flat theorem.

## 9. Universal vertices

Let \(U_n\) be the number of sampled vertices adjacent to all others.

Then

\[
\mathbb E[U_n]
=
n
\mathbb E[
Q(X)^{n-1}
].
\]

The co-degree tail gives

\[
\boxed{
\mathbb E[U_n]
\sim
6
C_{\mathrm{tip}}
n^{-2}.
}
\]

Thus

\[
\boxed{
\mathbb E[U_n]
\sim
\frac{
2\pi
}{
V_D
}
\left(
\kappa_p^{-3}
+
\kappa_q^{-3}
\right)
n^{-2}.
}
\]

This is the curved \(2+1\) analogue of the flat near-tip post asymptotic.

## 10. Near-whole-module input

The near-whole module proof needs three geometric estimates:

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
\mu(
A_x\cap S_t
)
=
O(t^2).
\]

All three are now available in the regular curved \(2+1\) class.

Therefore the qualitative near-whole-module exclusion proof transfers without using flat symmetry.

## 11. Scope

The theorem assumes the temporal nondegeneracy of the co-degree gradient at the tips.

This is a geometric hypothesis, not a probabilistic one.

It should be checked independently for any proposed curved spacetime class.

For conformally Minkowskian diamonds it follows from the weighted flat theorem.

For a generic curved diamond, it is naturally related to differentiability and temporality of the finite-diamond volume-time function.
