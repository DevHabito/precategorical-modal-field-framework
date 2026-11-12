# Adjacent-twin asymptotic theorem in 3+1 Minkowski

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** project theorem — proof complete; independent/external review pending  
**Scope:** exactly \(n\) iid uniform points in a fixed flat \(3+1\)-dimensional Alexandrov interval  
**Novelty status:** adjacent twins are classical graph modules; targeted review did not locate this Lorentzian \(9\pi/n\) asymptotic. Absolute novelty and priority are not certified.

## 1. Theorem

Let \(G_n\) be the undirected causal-comparability graph of \(n\) iid uniform points in a fixed Alexandrov interval of flat \(3+1\)-dimensional Minkowski spacetime.

Let \(T_n\) be the number of **adjacent twin pairs**: unordered pairs \(\{x,y\}\) such that

1. \(x\) and \(y\) are causally comparable;
2. every third sampled event is comparable to \(x\) exactly when it is comparable to \(y\).

Then

\[
\boxed{
E[T_n]
\sim
\frac{9\pi}{n}.
}
\]

Consequently,

\[
\boxed{
P(T_n>0)
\le
E[T_n]
=
\frac{9\pi+o(1)}{n}
\longrightarrow0.
}
\]

Thus the size-two non-stable-module obstruction to unique partial orderability vanishes in probability in the \(3+1\) fixed-diamond ensemble.

This theorem does **not** by itself imply that the entire comparability graph is UPO with probability tending to one, because larger non-stable modules and multiple nontrivial components remain possible.

---

## 2. Exact two-point formula

For a continuum point \(x\), let

\[
S_x
=
\{z:z\sim x\}
\]

be its causal-comparability region.

For comparable \(x,y\), define the normalized distinguishing volume

\[
D(x,y)
=
\mu(S_x\triangle S_y).
\]

Conditioned on the selected pair, they are adjacent twins exactly when all other \(n-2\) points avoid the distinguishing region.

Therefore

\[
\boxed{
E[T_n]
=
\binom n2
E\left[
\mathbf1_{\{X\sim Y\}}
(1-D(X,Y))^{n-2}
\right].
}
\]

By future/past symmetry,

\[
\boxed{
E[T_n]
=
n(n-1)
\int_{x\prec y}
(1-D(x,y))^{n-2}
\,\mu(dx)\mu(dy).
}
\]

For \(x\prec y\),

\[
\boxed{
D(x,y)
=
\frac{
\tau_{py}^{4}
-\tau_{px}^{4}
+\tau_{xq}^{4}
-\tau_{yq}^{4}
-2\tau_{xy}^{4}
}{16}.
}
\]

---

## 3. Standard diamond coordinates

Use

\[
p=(-1,\mathbf0),
\qquad
q=(1,\mathbf0).
\]

For

\[
x=(t_x,r_x\sigma_x),
\]

define

\[
a=1+t_x-r_x,
\qquad
b=1-t_x-r_x.
\]

Then

\[
r_x
=
1-\frac{a+b}{2}.
\]

For a future point \(y\), write

\[
c=a+u,
\qquad
d=b-w,
\]

with

\[
u\ge0,
\qquad
0\le w\le b.
\]

Then

\[
r_y
=
1-\frac{a+b+u-w}{2}.
\]

Let

\[
\theta
=
\angle(\sigma_x,\sigma_y),
\qquad
v=\sin(\theta/2).
\]

A direct calculation gives the exact timelike condition

\[
\boxed{
4r_xr_yv^2
<
uw.
}
\]

Inside a sufficiently small fixed waist neighborhood, the right-hand side is less than \(4r_xr_y\), so introduce

\[
s
=
\frac{
4r_xr_yv^2
}{
uw
},
\qquad
0\le s<1.
\]

Then

\[
\boxed{
\tau_{xy}^2
=
uw(1-s).
}
\]

For normalized spherical measure on \(S^2\),

\[
d\sigma_y
=
2v\,dv
=
\frac{
uw
}{
4r_xr_y
}
\,ds
\]

after fixing \(\sigma_x\).

The normalized spacetime measure is

\[
d\mu
=
3r^2\,da\,db\,d\sigma.
\]

Hence the exact future-directed pair measure in these variables is

\[
\boxed{
\mu(dx)\mu(dy)
=
\frac94
r_xr_y
uw
\,da\,db\,du\,dw\,ds.
}
\]

---

## 4. Null-waist scaling

Set

\[
a=\frac{2A}{\sqrt n},
\qquad
b=\frac{2B}{\sqrt n},
\]

\[
u=\frac{2U}{\sqrt n},
\qquad
w=\frac{2W}{\sqrt n}.
\]

Then

\[
c=\frac{2(A+U)}{\sqrt n},
\qquad
d=\frac{2(B-W)}{\sqrt n}.
\]

For fixed scaled variables with

\[
A,B,U\ge0,
\qquad
0\le W\le B,
\]

the exact distinguishing-volume polynomial gives

\[
\boxed{
nD(x,y)
\longrightarrow
H(A,B,U,W)
}
\]

where

\[
\boxed{
H
=
2AU+U^2+2BW-W^2.
}
\]

Equivalently,

\[
H
=
(A+U)^2-A^2
+
B^2-(B-W)^2.
\]

The limit is independent of \(s\).

The pair measure satisfies

\[
\frac94
r_xr_y
uw
\,da\,db\,du\,dw\,ds
=
\frac{
144
}{
n^3
}
r_xr_y
UW
\,dA\,dB\,dU\,dW\,ds.
\]

Multiplying by

\[
nE[T_n]
=
n^2(n-1)
\int_{x\prec y}
(1-D)^{n-2}
\,\mu(dx)\mu(dy),
\]

the scaled integrand tends pointwise to

\[
144
UW
e^{-H}.
\]

---

## 5. Uniform lower bound in the waist

To justify dominated convergence, a uniform lower bound on \(D\) is needed.

Let

\[
h(a,b,u,w)
=
u(2a+u)
+
w(2b-w).
\]

Choose a fixed waist neighborhood small enough that

\[
0\le a,b,c,d\le\varepsilon
\]

with, for example,

\[
\varepsilon\le\frac18.
\]

Then

\[
u\le\varepsilon,
\qquad
w\le b\le\varepsilon.
\]

For fixed \(a,b,u,w\), \(D\) is minimized over the causal angular parameter at

\[
s=0,
\]

because the only \(s\)-dependent term is

\[
-\frac18u^2w^2(1-s)^2.
\]

At \(s=0\), exact expansion gives

\[
\begin{aligned}
D_0
={}&
\left[
\frac{a(1-b)}2+\frac{b^2}{4}
\right]u
+
\frac{1-b}{4}u^2
\\
&+
\left[
\frac{a^2}{4}
-\frac{ab}{2}
+\frac b2
\right]w
+
\frac{a-1}{4}w^2
\\
&+
\frac{a-b}{2}uw
+
\frac14u^2w
+
\frac14uw^2
-
\frac18u^2w^2.
\end{aligned}
\]

Using

\[
w^2\le bw,
\qquad
2uw\le u^2+w^2\le u^2+bw,
\]

and the smallness of \(a,b,u,w\), all negative terms can be absorbed into the positive linear/quadratic terms.

Thus, after possibly decreasing \(\varepsilon\),

\[
\boxed{
D(x,y)
\ge
\frac1{16}
\left[
u(2a+u)
+
w(2b-w)
\right].
}
\]

Under the scaling,

\[
h
=
\frac4n
H.
\]

Hence, for all sufficiently large \(n\),

\[
(n-2)D
\ge
cH
\]

for a fixed \(c>0\).

Therefore the scaled integrand is dominated by

\[
C
UW
e^{-cH}.
\]

This is integrable.

Indeed,

\[
H
=
U(2A+U)
+
W(2B-W),
\]

with

\[
0\le W\le B.
\]

Integrating first in \(A\) and \(B\) cancels the factors \(U\) and \(W\), leaving Gaussian tails in \(U\) and \(W\).

---

## 6. Evaluation of the waist limit

Dominated convergence gives

\[
\lim_{n\to\infty}
nE[T_n;\text{ both points in the waist}]
=
144
\int_0^\infty
\int_0^\infty
\int_0^\infty
\int_0^B
UW
e^{-H}
\,dW\,dU\,dB\,dA.
\]

The \(s\)-integral contributes \(1\).

The integral factorizes:

\[
\int_0^\infty
\int_0^\infty
U
e^{-(2AU+U^2)}
\,dA\,dU
\]

times

\[
\int_0^\infty
\int_0^B
W
e^{-(2BW-W^2)}
\,dW\,dB.
\]

For the first,

\[
\int_0^\infty
e^{-2AU}\,dA
=
\frac1{2U},
\]

so

\[
\int_0^\infty
\int_0^\infty
U
e^{-(2AU+U^2)}
\,dA\,dU
=
\frac12
\int_0^\infty
e^{-U^2}\,dU
=
\frac{\sqrt\pi}{4}.
\]

For the second, set

\[
D=B-W\ge0.
\]

Then

\[
2BW-W^2
=
W^2+2DW,
\]

and similarly

\[
\int_0^\infty
\int_0^\infty
W
e^{-(W^2+2DW)}
\,dD\,dW
=
\frac{\sqrt\pi}{4}.
\]

Therefore

\[
\boxed{
\lim_{n\to\infty}
nE[T_n;\text{ waist}]
=
144
\left(
\frac{\sqrt\pi}{4}
\right)^2
=
9\pi.
}
\]

---

## 7. Bulk nondegeneracy lemma

It remains to show that pairs outside the null-waist scaling contribute only lower order.

For a point \(x\), define

\[
U_x=\tau_{px}^2,
\qquad
V_x=\tau_{xq}^2.
\]

For a small future-causal displacement

\[
y=x+h,
\]

Taylor expansion of the exact distinguishing volume gives

\[
D(x,x+h)
=
L_x\cdot h
+
O(\|h\|^2),
\]

where

\[
\boxed{
L_x
=
\frac14
\left(
U_x(x-p)
+
V_x(q-x)
\right).
}
\]

Its Minkowski norm is

\[
\boxed{
16L_x^2
=
U_x^3
+
V_x^3
+
U_xV_x(4-U_x-V_x).
}
\]

Inside the diamond,

\[
U_x,V_x\ge0,
\qquad
U_x+V_x\le4.
\]

Therefore

\[
L_x^2>0
\]

unless

\[
U_x=V_x=0,
\]

which is exactly the null waist.

Thus on every compact subset separated from the waist, \(L_x\) is uniformly future timelike.

For every future-causal \(h\),

\[
L_x\cdot h
\ge
c\|h\|_{\mathrm E}
\]

with a uniform \(c>0\).

Hence, for sufficiently small \(h\),

\[
D(x,x+h)
\ge
c'\|h\|_{\mathrm E}.
\]

Away from the diagonal, \(D\) is continuous and strictly positive for distinct comparable points, so compactness supplies a positive lower bound.

It follows uniformly outside any fixed waist neighborhood that

\[
\int_{y:x\prec y}
e^{-nD(x,y)}
\,\mu(dy)
=
O(n^{-4}).
\]

After integrating \(x\),

\[
\int_{\substack{x\prec y\\
\text{at least one point outside the waist}}}
e^{-nD(x,y)}
\,\mu(dx)\mu(dy)
=
O(n^{-4}).
\]

Since

\[
(1-D)^{n-2}
\le
e^{-(n-2)D},
\]

the corresponding contribution to \(E[T_n]\) is

\[
O(n^{-2}),
\]

and therefore

\[
\boxed{
nE[T_n;\text{ outside waist}]
\longrightarrow0.
}
\]

---

## 8. Completion

Combining Sections 6 and 7,

\[
nE[T_n]
=
nE[T_n;\text{ waist}]
+
nE[T_n;\text{ outside waist}]
\longrightarrow
9\pi.
\]

Therefore

\[
\boxed{
E[T_n]
\sim
\frac{9\pi}{n}.
}
\]

Markov's inequality gives

\[
P(T_n>0)
\le
E[T_n]
\longrightarrow0.
\]

This proves the theorem.

\(\square\)

---

## 9. Numerical regression

Before the proof was closed, the exponent \(1/n\) was frozen in a preregistration and tested at held-out sizes.

The exact two-point importance estimator later showed the slow approach

\[
nE[T_n]
=
11.36,\ 18.14,\ 20.18,\ 23.51,\ 26.64,\ 27.97
\]

at representative effective sizes

\[
n=
48,\ 384,\ 10^3,\ 10^4,\ 10^6,\ 10^9.
\]

The theorem gives the limiting constant

\[
9\pi
\approx
28.27433.
\]

The numerical work was therefore diagnostic and prospective support; it is no longer the basis of the asymptotic claim.

---

## 10. Consequence for UPO failures

An adjacent twin pair is a size-two non-stable module.

For a connected comparability graph, any non-stable module obstructs unique partial orderability.

Hence the theorem proves that this particular obstruction disappears:

\[
\boxed{
P(
\text{at least one size-two non-stable module}
)
\to0.
}
\]

The finite simulations had shown that adjacent twins explain roughly \(91\%\)–\(96\%\) of observed non-UPO failures in the audited \(3+1\) range.

The theorem now removes that dominant finite obstruction asymptotically.

What remains is the residual event

\[
q_4^{\mathrm{res}}(n)
=
P(
k_\Gamma>1,\ T_n=0
),
\]

which contains

- non-stable modules of size at least three;
- multiple nontrivial connected components.

A proof that

\[
q_4^{\mathrm{res}}(n)\to0
\]

would imply

\[
p_4^{\mathrm{UPO}}(n)\to1.
\]

That implication is not yet claimed as a theorem.

---

## 11. Literature boundary

The graph-theoretic fact that adjacent twins form a nontrivial module is classical.

The causal-set and Lorentzian ingredients are also classical.

The project-specific theorem is the \(9\pi/n\) asymptotic under the declared fixed-diamond Minkowski sprinkling measure.

Targeted searches did not locate this exact asymptotic.

This is limited negative evidence only.

Absolute novelty and priority are not certified.

---

## 12. Current research consequence

The \(3+1\) orientation-recovery problem has now lost its dominant observed finite obstruction.

The remaining frontier is no longer

> do adjacent twins disappear?

That is answered yes.

The next question is

\[
\boxed{
P(
\text{non-UPO and no adjacent twins}
)
\stackrel{?}{\longrightarrow}
0.
}
\]

That residual modular problem is now the shortest route toward deciding whether symmetric causal comparability recovers the full \(3+1\) sprinkled order up to global duality with probability tending to one.
