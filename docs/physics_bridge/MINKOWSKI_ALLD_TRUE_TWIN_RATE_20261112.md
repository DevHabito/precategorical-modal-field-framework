# Theorem: true-twin asymptotic rate in fixed Minkowski dimensions d >= 4

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic asymptotic theorem + numerical constant regression  
**Physical status:** leading size-two modular-defect statistic after causal-arrow erasure  
**Novelty status:** no equivalent all-dimensional true-twin asymptotic for Minkowski causal-comparability graphs was located in the targeted review; absolute priority is not certified

## 1. Purpose

The all-dimensional orientation-recovery theorem proves

\[
p_d^{\mathrm{UPO}}(n)\to1
\qquad
\text{for every fixed integer }d\ge3.
\]

The next question is quantitative:

> which rare obstruction controls the approach to one?

For \(d=4\), the adjacent true-twin count already satisfies

\[
\mathbb E[T_n]
\sim
\frac{9\pi}{n}.
\]

This note extends the true-twin expectation asymptotic, including its leading constant, to every fixed

\[
d\ge4.
\]

It does **not** yet prove that the full UPO failure probability has the same asymptotic constant.

## 2. Definitions

Let

\[
D_d
\subset
\mathbb M^d
\]

be the unit flat Alexandrov interval with normalized volume measure.

For a comparable pair \(x\sim y\), define

\[
\Delta_d(x,y)
=
\mu(A_x\triangle A_y).
\]

Let

\[
F_d(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta_d(X,Y)\le\varepsilon
).
\]

Let \(T_n\) be the number of adjacent true-twin pairs in the sampled comparability graph.

Conditioned on a comparable pair with disagreement \(\Delta\), the pair is a sampled true-twin pair exactly when all other \(n-2\) sampled vertices avoid its splitter region.

Therefore

\[
\boxed{
\mathbb E[T_n]
=
\binom n2
\int_0^1
(1-\delta)^{n-2}
\,dF_d(\delta).
}
\]

## 3. Joint regime for d >= 4

Set

\[
m=\frac d2.
\]

For \(d\ge4\),

\[
m\ge2,
\]

and the null-joint integral is convergent.

In joint-adapted coordinates for an ordered pair \(x\prec y\),

\[
a_x=\alpha,
\qquad
b_y=\beta,
\]

\[
A=a_y-a_x\ge0,
\qquad
B=b_x-b_y\ge0.
\]

The leading disagreement is

\[
\boxed{
H_m
=
2^{-m}
\left[
g_m(\alpha,A)
+
g_m(\beta,B)
\right],
}
\]

where

\[
g_m(u,v)
=
(u+v)^m-u^m.
\]

The exact interval term involving \(\tau(x,y)^d\) is higher order under the joint blow-up.

## 4. Exact one-side constant

Define

\[
J_m(s)
=
\int_0^\infty
\int_0^\infty
A^{m-1}
\mathbf1_{
\{g_m(\alpha,A)\le s\}
}
\,dA\,d\alpha.
\]

Use

\[
t=\frac{\alpha}{A}.
\]

Then

\[
g_m(\alpha,A)
=
A^m
\left[
(1+t)^m-t^m
\right],
\]

and

\[
d\alpha\,dA
=
A\,dt\,dA.
\]

Hence

\[
A^{m-1}d\alpha\,dA
=
A^m\,dt\,dA.
\]

For fixed \(t\),

\[
0\le
A
\le
\left(
\frac{s}{
(1+t)^m-t^m
}
\right)^{1/m}.
\]

Therefore

\[
\boxed{
J_m(s)
=
L_m
s^{1+1/m},
}
\]

where

\[
\boxed{
L_m
=
\frac1{m+1}
\int_0^\infty
\left[
(1+t)^m-t^m
\right]^{-(m+1)/m}
dt.
}
\]

For \(m\ge2\), this integral converges.

Write

\[
a_m
=
1+\frac1m
=
1+\frac2d.
\]

The induced one-side Stieltjes density is

\[
dJ_m(g)
=
a_mL_m
g^{a_m-1}
\,dg.
\]

## 5. Angular coefficient

After angular variables are normalized, a single Minkowski point has measure

\[
d\mu
=
c_d
r^{d-2}
\,da\,db\,d\sigma,
\]

where

\[
c_d
=
\frac{d(d-1)}4
\]

and \(d\sigma\) is normalized measure on \(S^{d-2}\).

Let

\[
S_k
=
\frac{
2\pi^{(k+1)/2}
}{
\Gamma((k+1)/2)
}
\]

denote the Euclidean area of the unit \(k\)-sphere.

For a small causal angular cap, with

\[
u
=
\frac{
2r_xr_y(1-\cos\theta)
}{
AB
},
\qquad
0\le u\le1,
\]

the relative angular density has leading form

\[
\frac{
S_{d-3}
}{
2S_{d-2}
}
\left(
\frac{AB}{r_xr_y}
\right)^{m-1}
u^{m-2}\,du.
\]

At the joint,

\[
r_x,r_y\to1.
\]

After integrating

\[
u\in[0,1]
\]

and including both time orientations, the angular/time-order coefficient is

\[
\boxed{
K_d^{\mathrm{ang}}
=
\frac{
c_d^2
}{
m-1
}
\frac{
S_{d-3}
}{
S_{d-2}
}.
}
\]

For \(d=4\), this reduces to

\[
K_4^{\mathrm{ang}}
=
\frac92.
\]

## 6. Exact small-disagreement coefficient

The leading condition

\[
H_m\le\varepsilon
\]

is

\[
g_1+g_2
\le
2^m\varepsilon.
\]

Using the two one-side Stieltjes densities,

\[
\begin{aligned}
&\int_{g_1+g_2\le R}
dJ_m(g_1)\,dJ_m(g_2)
\\
&\qquad=
(a_mL_m)^2
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}
R^{2a_m}.
\end{aligned}
\]

With

\[
R=2^m\varepsilon
\]

and

\[
2a_m
=
2+\frac4d
=:
\beta_d,
\]

we obtain

\[
\boxed{
F_d(\varepsilon)
\sim
C_d^{\mathrm{edge}}
\varepsilon^{\beta_d}
\qquad
(d\ge4),
}
\]

where

\[
\boxed{
C_d^{\mathrm{edge}}
=
\frac{
c_d^2
}{
m-1
}
\frac{
S_{d-3}
}{
S_{d-2}
}
(a_mL_m)^2
2^{d+2}
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}.
}
\]

Equivalently,

\[
\boxed{
C_d^{\mathrm{edge}}
=
\frac{
2^{d-1}d^2(d-1)^2
}{
d-2
}
\frac{
S_{d-3}
}{
S_{d-2}
}
(a_mL_m)^2
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}.
}
\]

The ordinary bulk contribution is \(O(\varepsilon^d)\), which is subleading for every \(d\ge4\), with equality of exponents only at \(d=4\) avoided because the joint exponent is \(3<4\).

## 7. True-twin expectation

The exact expectation identity is a Laplace-Stieltjes transform of \(F_d\).

Since

\[
F_d(\delta)
\sim
C_d^{\mathrm{edge}}
\delta^{\beta_d},
\]

\[
\int_0^1
(1-\delta)^{n-2}
\,dF_d(\delta)
\sim
C_d^{\mathrm{edge}}
\Gamma(\beta_d+1)
n^{-\beta_d}.
\]

Using

\[
\binom n2
\sim
\frac{n^2}{2},
\]

\[
\boxed{
\mathbb E[T_n]
\sim
K_d^{\mathrm{twin}}
n^{-4/d},
}
\]

where

\[
\boxed{
K_d^{\mathrm{twin}}
=
\frac12
C_d^{\mathrm{edge}}
\Gamma\!\left(3+\frac4d\right).
}
\]

The gamma factor cancels the denominator in \(C_d^{\mathrm{edge}}\), giving the simpler form

\[
\boxed{
K_d^{\mathrm{twin}}
=
2^{d-2}
\frac{
d^2(d-1)^2
}{
d-2
}
\frac{
S_{d-3}
}{
S_{d-2}
}
\left[
a_mL_m\Gamma(a_m)
\right]^2.
}
\]

Thus the true-twin decay becomes slower as \(d\) increases:

\[
n^{-4/d}.
\]

It still tends to zero for every fixed finite dimension.

## 8. d = 4 control

For

\[
d=4,
\qquad
m=2,
\]

\[
(1+t)^2-t^2
=
2t+1.
\]

Hence

\[
L_2
=
\frac13
\int_0^\infty
(2t+1)^{-3/2}
dt
=
\frac13.
\]

Substitution gives

\[
\boxed{
C_4^{\mathrm{edge}}
=
3\pi
}
\]

and

\[
\boxed{
K_4^{\mathrm{twin}}
=
9\pi.
}
\]

Therefore

\[
\mathbb E[T_n]
\sim
\frac{9\pi}{n},
\]

recovering the independently derived \(d=4\) theorem exactly.

## 9. Numerical constants

The repository tool

tools/minkowski_alld_true_twin_constants.py

evaluates \(L_m\), \(C_d^{\mathrm{edge}}\), and \(K_d^{\mathrm{twin}}\).

Representative values are:

| \(d\) | \(\beta_d\) | \(C_d^{\mathrm{edge}}\) | \(K_d^{\mathrm{twin}}\) |
|---:|---:|---:|---:|
|4|3.000000|9.424778|28.274334|
|5|2.800000|9.432595|22.139123|
|6|2.666667|16.230502|32.560021|
|7|2.571429|31.517995|56.713838|
|8|2.500000|63.295889|105.177227|
|9|2.444444|128.129578|200.355834|
|10|2.400000|259.288800|386.496719|

For \(d=4\), the script explicitly checks

\[
C_4^{\mathrm{edge}}=3\pi
\]

and

\[
K_4^{\mathrm{twin}}=9\pi.
\]

The numerical quadrature is a regression of the closed formulas, not the proof.

## 10. Interpretation for the recovery-rate problem

A comparable true-twin pair is a size-two non-stable module whenever it lies inside a connected component containing additional vertices.

The all-dimensional component theorem puts all non-isolated vertices into one component with probability tending to one.

Therefore true twins are genuine UPO obstructions asymptotically.

The theorem above supplies a natural candidate scale for the full failure probability:

\[
\boxed{
1-p_d^{\mathrm{UPO}}(n)
\quad\text{candidate scale}\quad
n^{-4/d}
\qquad(d\ge4).
}
\]

This statement is deliberately labelled a candidate.

To prove

\[
1-p_d^{\mathrm{UPO}}(n)
\sim
K_d^{\mathrm{twin}}
n^{-4/d},
\]

two additional ingredients are required:

1. a rare-event second-moment/Poisson estimate showing
   \[
   \Pr(T_n>0)
   \sim
   \mathbb E[T_n];
   \]
2. an upper bound showing every other UPO obstruction is
   \[
   o(n^{-4/d}).
   \]

Neither is assumed in this note.

## 11. Dimensional meaning

For \(d\ge4\), the leading true-twin geometry is controlled by the codimension-two null joint.

The exponent

\[
\frac4d
\]

in the expected defect count comes from subtracting the \(O(n^2)\) possible pairs from the small-edge exponent

\[
2+\frac4d.
\]

Thus the same joint geometry that creates the isolated-vertex dimension threshold also governs the slow disappearance of the leading size-two modular defect.

The two observables remain distinct:

- isolated vertices do not create orientation ambiguity;
- comparable true twins do.

## 12. Current frontier

The next quantitative theorem is to determine whether true twins actually dominate the full UPO failure probability.

The immediate targets are:

1. bound
   \[
   \mathbb E[T_n(T_n-1)];
   \]
2. classify overlapping twin configurations;
3. control two disjoint rare twin pairs;
4. compare all larger fixed modules to the \(n^{-4/d}\) scale;
5. quantify the nonlocal module bounds from the all-dimensional recovery proof.

Only after those steps should the repository promote \(K_d^{\mathrm{twin}}\) from a defect-count constant to the convergence-rate constant for \(p_d^{\mathrm{UPO}}\).
