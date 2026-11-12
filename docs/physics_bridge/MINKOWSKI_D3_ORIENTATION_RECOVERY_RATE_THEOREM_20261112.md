# Theorem: exact leading orientation-recovery error in 2+1 Minkowski spacetime

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic asymptotic theorem  
**Physical status:** first-order reconstruction-error law for the declared arrow-erasure experiment in flat \(2+1\) Minkowski spacetime  
**Novelty status:** targeted literature review did not locate an equivalent \(2+1\) Minkowski arrow-erasure/UPO rate theorem; absolute novelty and priority are not certified

## 1. Statement

Let

\[
G_{3,n}
\]

be the undirected causal-comparability graph obtained from an iid size-\(n\) sprinkling into a fixed flat Alexandrov interval of \(\mathbb M^3\), after all causal arrows have been erased.

Let

\[
p_3^{\mathrm{UPO}}(n)
\]

denote the probability that the original causal partial order is recoverable from \(G_{3,n}\) up to global reversal.

Then

\[
\boxed{
1-p_3^{\mathrm{UPO}}(n)
\sim
\frac{32\pi}{3n}.
}
\]

Equivalently,

\[
\boxed{
p_3^{\mathrm{UPO}}(n)
=
1-
\frac{32\pi}{3n}
+
o(n^{-1}).
}
\]

The leading obstruction is a comparable true-twin pair.

## 2. Why d = 3 is different from d >= 4

For \(d=3\), the small-disagreement pair tail is bulk controlled:

\[
F_3(\varepsilon)
=
\Pr(
X\sim Y,\,
\Delta_3(X,Y)\le\varepsilon
)
=
\Theta(\varepsilon^3).
\]

The codimension-two null-joint core itself contributes only

\[
O(\varepsilon^{10/3}),
\]

so it is subleading.

The leading \(\varepsilon^3\) term is produced by ordinary small timelike displacements integrated over the entire interior, including a matching region approaching the joint.

This makes the coefficient a bulk integral rather than a null-joint scaling constant.

## 3. Local linearization of the disagreement

Let

\[
p=(-1,\mathbf0),
\qquad
q=(1,\mathbf0),
\]

and let \(x\in D^\circ\).

Write

\[
u=\tau(p,x),
\qquad
v=\tau(x,q).
\]

For a small future-timelike displacement

\[
y=x+h,
\]

the exact disagreement formula is

\[
\Delta_3(x,y)
=
\frac{
\tau(p,y)^3-\tau(p,x)^3
+
\tau(x,q)^3-\tau(y,q)^3
-
2\tau(x,y)^3
}{
8
}.
\]

The final interval term is

\[
O(|h|^3).
\]

The endpoint terms have the first-order expansion

\[
\Delta_3(x,x+h)
=
C_x\cdot_M h
+
O(|h|^2),
\]

where

\[
\boxed{
C_x
=
\frac38
\left[
u(x-p)
+
v(q-x)
\right].
}
\]

Here the right-hand side is interpreted as a future-timelike Minkowski vector defining the linear covector.

Define its Lorentz norm

\[
\kappa(x)
=
\sqrt{
C_x\cdot_M C_x
}.
\]

Then

\[
\kappa(x)>0
\]

for every interior point.

## 4. Local timelike-cone volume

Because \(C_x\) is future timelike, a Lorentz transformation with unit determinant sends it to

\[
(\kappa(x),0,0).
\]

In that rest frame, the future-timelike displacement region satisfying

\[
C_x\cdot_M h\le\varepsilon
\]

is

\[
0<h^0\le\frac{\varepsilon}{\kappa(x)},
\qquad
|\mathbf h|<h^0.
\]

Its coordinate volume is

\[
\int_0^{\varepsilon/\kappa(x)}
\pi (h^0)^2\,dh^0
=
\boxed{
\frac{\pi}{3}
\frac{\varepsilon^3}{\kappa(x)^3}.
}
\]

Lorentz transformations preserve the spacetime volume element, so this is the local coefficient in every frame.

## 5. Global coefficient

The \(2+1\) unit Alexandrov interval has spacetime volume

\[
V_3
=
\frac{2\pi}{3}.
\]

Both time orientations contribute equally.

Therefore the small-disagreement coefficient is

\[
C_3^{\mathrm{edge}}
=
2
\frac1{V_3}
\frac{\pi}{3}
\int_D
\kappa(x)^{-3}
\,d\mu(x).
\]

Because

\[
\frac{2\pi}{3V_3}=1,
\]

this simplifies to

\[
\boxed{
C_3^{\mathrm{edge}}
=
\int_D
\kappa(x)^{-3}
\,d\mu(x).
}
\]

The integral is finite.

Near the null joint,

\[
\kappa^{-3}
\]

has an integrable singularity; the genuinely nonlinear joint core contributes only \(o(\varepsilon^3)\).

## 6. Endpoint-distance coordinates

Use

\[
u=\tau(p,x),
\qquad
v=\tau(x,q).
\]

The domain becomes

\[
u>0,
\qquad
v>0,
\qquad
u+v<2.
\]

From

\[
u^2=(1+t)^2-r^2,
\]

\[
v^2=(1-t)^2-r^2,
\]

we obtain

\[
t
=
\frac{u^2-v^2}{4},
\]

and

\[
r^2
=
\frac{
\left(4-(u-v)^2\right)
\left(4-(u+v)^2\right)
}{16}.
\]

The spacetime volume element becomes

\[
d\mathrm{Vol}
=
\pi uv\,du\,dv.
\]

Since

\[
V_3=\frac{2\pi}{3},
\]

the normalized volume measure is

\[
\boxed{
d\mu
=
\frac32
uv\,du\,dv.
}
\]

## 7. Exact Lorentz norm

Using

\[
(x-p)+(q-x)=q-p
\]

and

\[
(q-p)^2=4,
\]

we obtain

\[
\kappa(x)^2
=
\frac9{64}
K(u,v),
\]

where

\[
\boxed{
K(u,v)
=
u^4+v^4+
(4-u^2-v^2)uv.
}
\]

Therefore

\[
\begin{aligned}
C_3^{\mathrm{edge}}
&=
\frac32
\left(\frac{64}{9}\right)^{3/2}
\int_{\substack{u,v>0\\u+v<2}}
\frac{uv}{
K(u,v)^{3/2}
}
\,du\,dv\\
&=
\frac{256}{9}
I,
\end{aligned}
\]

with

\[
I
=
\int_{\substack{u,v>0\\u+v<2}}
\frac{uv}{
K(u,v)^{3/2}
}
\,du\,dv.
\]

## 8. Closed evaluation of the bulk integral

Set

\[
s=u+v,
\qquad
w=\frac{u-v}{u+v}.
\]

Then

\[
0<s<2,
\qquad
-1<w<1,
\]

and

\[
u=\frac{s(1+w)}2,
\qquad
v=\frac{s(1-w)}2.
\]

The Jacobian is

\[
du\,dv
=
\frac{s}{2}\,ds\,dw.
\]

The polynomial \(K\) becomes

\[
K
=
\frac{s^2}{4}
\left[
4(1-w^2)
+
s^2w^2(w^2+3)
\right].
\]

A direct cancellation gives

\[
I
=
\int_{-1}^1
\int_0^2
\frac{
1-w^2
}{
\left[
4(1-w^2)
+
s^2w^2(w^2+3)
\right]^{3/2}
}
\,ds\,dw.
\]

For fixed \(w\),

\[
\int_0^2
\frac{ds}{
(A+Bs^2)^{3/2}
}
=
\frac{
2
}{
A\sqrt{A+4B}
},
\]

with

\[
A=4(1-w^2),
\qquad
B=w^2(w^2+3).
\]

Since

\[
A+4B
=
4(1+w^2)^2,
\]

the \(s\)-integral reduces exactly to

\[
\frac1{
4(1-w^2)(1+w^2)
}.
\]

After multiplying by \(1-w^2\),

\[
I
=
\frac14
\int_{-1}^1
\frac{dw}{
1+w^2
}
=
\boxed{
\frac{\pi}{8}.
}
\]

Hence

\[
\boxed{
C_3^{\mathrm{edge}}
=
\frac{256}{9}
\frac{\pi}{8}
=
\frac{32\pi}{9}.
}
\]

Therefore

\[
\boxed{
F_3(\varepsilon)
\sim
\frac{32\pi}{9}
\varepsilon^3.
}
\]

## 9. Boundary control

The local linear expansion is uniform on compact subsets separated from the null joint.

To justify integrating the local coefficient over the whole diamond, split the domain at a joint depth parameter \(\eta\).

On the complement of the \(\eta\)-joint neighborhood, dominated Taylor expansion gives the coefficient

\[
\int_{D\setminus J_\eta}
\kappa^{-3}\,d\mu.
\]

Inside \(J_\eta\), the one-side \(m=3/2\) analysis gives a contribution bounded by

\[
C\eta^\rho\varepsilon^3
+
O(\varepsilon^{10/3})
\]

for some fixed \(\rho>0\).

Also,

\[
\int_{J_\eta}
\kappa^{-3}\,d\mu
\to0
\]

as

\[
\eta\downarrow0.
\]

Letting first

\[
\varepsilon\downarrow0
\]

and then

\[
\eta\downarrow0
\]

establishes the global coefficient above.

## 10. Comparable true-twin expectation

Let \(T_n\) count adjacent true-twin pairs.

The exact identity is

\[
\mathbb E[T_n]
=
\binom n2
\int_0^1
(1-\delta)^{n-2}
\,dF_3(\delta).
\]

Since

\[
F_3(\delta)
\sim
\frac{32\pi}{9}
\delta^3,
\]

Laplace-Stieltjes transfer gives

\[
\begin{aligned}
\mathbb E[T_n]
&\sim
\frac12
\frac{32\pi}{9}
\Gamma(4)
n^{-1}\\
&=
\boxed{
\frac{32\pi}{3n}.
}
\end{aligned}
\]

## 11. True-twin occurrence probability

The fixed-size hierarchy and uniform comparable-ball theorem give the same second-moment separation used in higher dimensions.

For disjoint candidate twin pairs,

\[
O(n^{-2}).
\]

For overlapping pairs,

\[
H_{\mathrm{overlap}}(t)
=
O(t^5),
\]

so their factorial-moment contribution is also

\[
O(n^{-2}).
\]

Thus

\[
\mathbb E[T_n(T_n-1)]
=
O(n^{-2})
=
o(n^{-1}).
\]

Therefore

\[
\boxed{
\Pr(T_n>0)
\sim
\mathbb E[T_n]
\sim
\frac{32\pi}{3n}.
}
\]

## 12. Every other failure mechanism is smaller

The quantitative hierarchy already gives:

### Non-twin local escalation failures

Since

\[
\beta_3=3,
\]

\[
O(n^{1-\beta_3})
=
O(n^{-2}).
\]

### Fixed-size non-twin modules

For every fixed

\[
r\ge3,
\]

\[
O(n^{1-r}),
\]

so the first such level is

\[
O(n^{-2}).
\]

### Multiple edge-containing components without true twins

\[
O(n^{-2})
+
\text{superpolynomial}.
\]

### Balanced macroscopic modules

\[
\exp\!\left(
-\frac{n}{2\log n}
\right).
\]

### Near-whole modules

The tip-clearance theorem gives

\[
O(n^{1-d})
=
O(n^{-2}).
\]

Thus every verified non-twin failure class is

\[
o(n^{-1}).
\]

## 13. Final error law

The lower bound is supplied by comparable true-twin occurrence.

The upper bound is obtained by decomposing every remaining failure into the quantitative classes above.

Therefore

\[
\boxed{
1-p_3^{\mathrm{UPO}}(n)
\sim
\frac{32\pi}{3n}.
}
\]

Equivalently,

\[
\boxed{
p_3^{\mathrm{UPO}}(n)
=
1-
\frac{32\pi}{3n}
+
o(n^{-1}).
}
\]

## 14. Dimensional comparison

The leading error laws now read:

### 2+1

Bulk dominated:

\[
\boxed{
1-p_3^{\mathrm{UPO}}(n)
\sim
\frac{32\pi}{3n}.
}
\]

### 3+1

Null-joint dominated:

\[
\boxed{
1-p_4^{\mathrm{UPO}}(n)
\sim
\frac{9\pi}{n}.
}
\]

The powers coincide,

\[
n^{-1},
\]

but the geometries and constants differ.

For

\[
d>4,
\]

the null joint controls both exponent and constant:

\[
1-p_d^{\mathrm{UPO}}(n)
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
\]

## 15. Computational regression

The repository script

tools/verify_d3_bulk_recovery_constant.py

checks:

\[
I=\frac{\pi}{8},
\]

\[
C_3^{\mathrm{edge}}
=
\frac{32\pi}{9},
\]

and

\[
K_3^{\mathrm{twin}}
=
\frac{32\pi}{3}.
\]

The numerical integration is a regression only.

The closed evaluation above is the proof.

## 16. Literature boundary

The local Lorentz-cone calculation uses standard Minkowski geometry and volume preservation.

The UPO/comparability and graphon ingredients used to promote the true-twin statistic to the full error law are established machinery documented elsewhere in the repository.

A targeted literature review did not locate a prior \(2+1\) Minkowski result with the arrow-erasure error constant

\[
32\pi/3.
\]

This is limited negative evidence only.

No absolute priority claim is made.

## 17. Current consequence

The leading flat-space orientation-recovery error is now known for every fixed integer spacetime dimension

\[
d\ge3.
\]

The remaining flat-space questions concern second-order terms rather than the first-order asymptotic.
