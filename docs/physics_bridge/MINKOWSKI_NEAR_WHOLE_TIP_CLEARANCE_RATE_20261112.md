# Theorem: near-whole modules have tip-clearance rate O(n^(1-d))

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic quantitative theorem  
**Physical status:** sharp suppression of sublinear-complement modules in arrow-erased flat Minkowski sprinklings  
**Novelty status:** the probability tools are standard; the middle-band nonneighbor geometry and its use in Minkowski module suppression are project-specific

## 1. Statement

Fix an integer spacetime dimension

\[
d\ge3.
\]

Let

\[
G_{d,n}
\]

be the arrow-erased causal-comparability graph of \(n\) iid uniform points in a fixed flat Alexandrov interval.

Let \(C_{d,n}\) be an edge-containing connected component and let

\[
M\subsetneq C_{d,n}
\]

be a proper graph module with

\[
|C_{d,n}\setminus M|=o(n)
\]

along any deterministic sublinear complement scale.

Then

\[
\boxed{
\Pr(
\text{such a near-whole non-stable module exists}
)
=
O(n^{1-d})
+
e^{-\Theta(n)}.
}
\]

In particular, for \(d=4\),

\[
\boxed{
\Pr(
\text{near-whole module}
)
=
O(n^{-3}).
}
\]

This removes the previously isolated square-root complement window as a possible \(n^{-1}\) obstruction in \(3+1\).

## 2. The complete external type

Let

\[
O=C_{d,n}\setminus M.
\]

Every vertex of \(O\) is either complete or anticomplete to \(M\).

Because \(C_{d,n}\) is connected, at least one outside vertex is complete to \(M\).

Choose one and call it

\[
u.
\]

Thus

\[
u\sim m
\qquad
\forall m\in M.
\]

Write the continuum co-degree of \(u\) as

\[
R(u)
=
1-Q_d(u).
\]

## 3. A middle-degree band in the nonneighbor region of a tip point

There exist constants

\[
r_0>0,
\qquad
c_0>0,
\qquad
0<q_-<q_+<1
\]

depending only on \(d\) and the normalized Alexandrov interval, such that whenever

\[
R(x)\le r_0,
\]

there is a measurable set

\[
B_x^{\mathrm{mid}}
\subseteq
D\setminus A_x
\]

with

\[
\boxed{
\mu(B_x^{\mathrm{mid}})
\ge
c_0R(x)
}
\]

and

\[
\boxed{
q_-
\le
Q_d(z)
\le
q_+
\qquad
\forall z\in B_x^{\mathrm{mid}}.
}
\]

Thus every sufficiently near-tip event has a nonneighbor region of size proportional to its total co-degree that contains only continuum vertices of degree bounded away from both zero and one.

## 4. Explicit past-tip construction

By time reflection it is enough to work near the past tip.

Write

\[
x=
(-1+s,\,
s\rho e_1),
\]

where

\[
0<s<s_0,
\qquad
0\le\rho\le1.
\]

The tip expansion gives, uniformly in \(\rho\),

\[
R(x)
=
\frac d2\,s
+
O(s^2).
\]

Hence

\[
R(x)\asymp s.
\]

Choose fixed numbers

\[
0<\tau_0<\tau_1<1,
\]

for example

\[
\tau_0=\frac13,
\qquad
\tau_1=\frac12.
\]

Consider points

\[
z=
(-1+\tau,\,
(\tau-h)\omega)
\]

with

\[
\tau\in[\tau_0,\tau_1],
\]

\[
\frac{s}{4}
\le
h
\le
\frac{s}{3},
\]

and

\[
e_1\cdot\omega\le0.
\]

These points lie inside the Alexandrov interval for sufficiently small \(s\).

## 5. Uniform spacelike separation

For such \(x,z\),

\[
\begin{aligned}
&|\mathbf z-\mathbf x|^2
-
(t_z-t_x)^2\\
&=
(\tau-h)^2
+
s^2\rho^2
-
2(\tau-h)s\rho(e_1\cdot\omega)
-
(\tau-s)^2.
\end{aligned}
\]

Rearranging,

\[
\begin{aligned}
&|\mathbf z-\mathbf x|^2
-
(t_z-t_x)^2\\
&=
2\tau
\left(
s-h-s\rho(e_1\cdot\omega)
\right)\\
&\quad+
h^2-s^2+s^2\rho^2
+
2hs\rho(e_1\cdot\omega).
\end{aligned}
\]

Because

\[
h\le s/3
\]

and

\[
e_1\cdot\omega\le0,
\]

the first line is at least a positive constant times \(s\), uniformly in \(\rho\).

The remaining terms are \(O(s^2)\).

Thus, for sufficiently small \(s\),

\[
|\mathbf z-\mathbf x|^2
>
(t_z-t_x)^2.
\]

Hence

\[
z\not\sim x.
\]

## 6. Volume of the middle band

The normalized spacetime density in spherical coordinates is bounded above and below by positive constants on the fixed \(\tau\)-band.

The radial thickness is

\[
\Theta(s),
\]

the \(\tau\)-interval has fixed length, and the angular condition

\[
e_1\cdot\omega\le0
\]

has fixed positive spherical measure.

Therefore

\[
\mu(B_x^{\mathrm{mid}})
\ge
c s.
\]

Using

\[
R(x)\asymp s,
\]

\[
\boxed{
\mu(B_x^{\mathrm{mid}})
\ge
c_0R(x).
}
\]

## 7. Middle graphon degree

As

\[
s\downarrow0,
\qquad
h=O(s),
\]

the points in the construction approach the past null face

\[
t=-1+\tau,
\qquad
r=\tau.
\]

On that null face,

\[
Q_d
=
(1-\tau)^{d/2}.
\]

Because

\[
\tau\in[\tau_0,\tau_1]
\Subset(0,1),
\]

this value is bounded away from both zero and one.

By continuity, after decreasing \(s_0\),

\[
q_-
\le
Q_d(z)
\le
q_+
\]

uniformly over the middle band.

This proves the geometric lemma.

## 8. Why a sampled middle-band point destroys a near-whole module

Suppose \(u\) is complete to a module \(M\) satisfying

\[
|M|=n-o(n).
\]

Any sampled point

\[
z\in B_u^{\mathrm{mid}}
\]

is a nonneighbor of \(u\).

Therefore

\[
z\notin M.
\]

Since \(M\) is a module, \(z\) must be either:

1. complete to \(M\);
2. anticomplete to \(M\).

But

\[
q_-
\le
Q_d(z)
\le
q_+.
\]

Conditioned on \(z\), its sampled degree is binomial with parameter \(Q_d(z)\).

For every deterministic

\[
\varepsilon_n\downarrow0,
\]

Chernoff concentration gives

\[
\Pr(
\deg(z)\le\varepsilon_n n
)
\le
e^{-c n},
\]

and

\[
\Pr(
\deg(z)\ge(1-\varepsilon_n)n
)
\le
e^{-c n},
\]

uniformly over

\[
Q_d(z)\in[q_-,q_+].
\]

Therefore a sampled middle-band point can have either module-compatible external type only with probability

\[
e^{-\Theta(n)}.
\]

A union bound over all sampled ordered pairs \((u,z)\) preserves an exponentially small error.

Thus, outside an \(e^{-\Theta(n)}\) event, every complete external vertex \(u\) of a near-whole module has

\[
\boxed{
B_u^{\mathrm{mid}}
\text{ empty of sampled vertices}.
}
\]

## 9. Tip localization of u

If

\[
R(u)\ge r_0,
\]

then \(u\) has continuum co-degree bounded below by a positive constant.

For \(u\) to be complete to a set of

\[
n-o(n)
\]

sampled vertices, its sampled co-degree would have to be \(o(n)\).

Chernoff gives probability

\[
e^{-\Theta(n)}.
\]

Thus, outside an exponentially small event, every complete external vertex relevant to a near-whole module satisfies

\[
R(u)<r_0
\]

and the middle-band lemma applies.

## 10. Tip-clear candidate probability

Condition on a sampled point

\[
X_i=x
\]

with

\[
R(x)<r_0.
\]

The probability that none of the other \(n-1\) points falls in

\[
B_x^{\mathrm{mid}}
\]

is at most

\[
\begin{aligned}
(1-\mu(B_x^{\mathrm{mid}}))^{n-1}
&\le
\exp(
-c_0(n-1)R(x)
).
\end{aligned}
\]

Hence the expected number of sampled tip-clear candidates is at most

\[
n
\int
e^{-c nR(x)}
\,d\mu(x).
\]

The timelike-tip co-degree tail satisfies

\[
\bar g_d(r)
=
\mu\{R\le r\}
=
O(r^d).
\]

A Laplace-Stieltjes estimate gives

\[
\int
e^{-cnr}
\,d\bar g_d(r)
=
O(n^{-d}).
\]

Therefore

\[
\boxed{
\mathbb E[
\#\text{ tip-clear candidates}
]
=
O(n^{1-d}).
}
\]

Markov gives the same order for the occurrence probability.

## 11. Near-whole module bound

A near-whole proper module requires a complete external vertex \(u\).

Outside an exponentially small event:

- \(u\) lies in the tip regime;
- \(u\) must be tip-clear.

Therefore

\[
\boxed{
\Pr(
\text{near-whole proper non-stable module}
)
=
O(n^{1-d})
+
e^{-\Theta(n)}.
}
\]

For \(d=4\),

\[
\boxed{
O(n^{-3}).
}
\]

For every \(d\ge4\),

\[
n^{1-d}
=
o(
n^{-4/d}
).
\]

Thus near-whole modules are quantitatively negligible relative to the true-twin scale.

## 12. Correction to the earlier square-root-window note

An earlier quantitative localization argument isolated

\[
|C_n\setminus M|
=
n^{1/2+o(1)}
\]

as the only \(d=4\) complement scale not excluded by the degree-tail/sparsity bounds used there.

The middle-band nonneighbor lemma supplies the missing geometric information.

It shows that the square-root window does not carry a competing \(n^{-1}\) obstruction.

Accordingly, the square-root-window document should now be read as an intermediate diagnostic, superseded by the present theorem for the final rate analysis.

## 13. Quantitative consequence

For \(d\ge4\), the known competing scales are now:

- comparable true twins:
  \[
  K_d^{\mathrm{twin}}n^{-4/d};
  \]
- fixed-size non-twin modules:
  \[
  O(n^{-1-4/d});
  \]
- non-twin escalation failures:
  \[
  O(n^{-1-4/d});
  \]
- balanced linear modules:
  superpolynomially small;
- near-whole modules:
  \[
  O(n^{1-d}).
  \]

Every verified non-twin modular regime is now

\[
o(n^{-4/d}).
\]

The only remaining item before a matching full UPO failure asymptotic is a quantitative bound on multiple edge-containing components when no comparable true twin is present.
