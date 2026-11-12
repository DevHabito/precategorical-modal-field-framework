# Theorem: comparable-twin tail in 3+1 Minkowski sprinklings

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem for the fixed Alexandrov-interval ensemble  
**Physical status:** causal-set reconstruction result after erasing causal arrows  
**Novelty status:** targeted literature review has not located an equivalent theorem; absolute priority is not certified

## 1. Statement

Let \(D=I(p,q)\subset\mathbb M^4\) be the flat Alexandrov interval with

\[
p=(-1,\mathbf 0),
\qquad
q=(1,\mathbf 0),
\]

equipped with normalized spacetime volume measure \(\mu\).

For \(x\in D\), define its symmetric comparability neighborhood

\[
A_x=\{z\in D:\ z\prec x\ \text{or}\ x\prec z\}.
\]

For iid \(X,Y\sim\mu\), define

\[
\Delta(X,Y)=\mu(A_X\triangle A_Y).
\]

Let

\[
F_4(\varepsilon)
=
\Pr\!\left(
X\sim Y,\,
\Delta(X,Y)\le\varepsilon
\right).
\]

Then

\[
\boxed{
F_4(\varepsilon)
\sim
3\pi\,\varepsilon^3
\qquad
(\varepsilon\downarrow0).
}
\]

Let \(T_n\) be the number of adjacent true-twin pairs in the unoriented comparability graph of an iid size-\(n\) sprinkling into \(D\). Then

\[
\boxed{
\mathbb E[T_n]
\sim
\frac{9\pi}{n}
\qquad
(n\to\infty).
}
\]

The second statement follows from the first through the exact identity

\[
\mathbb E[T_n]
=
\binom n2
\int_0^1
(1-\delta)^{n-2}\,dF_4(\delta).
\]

## 2. Joint-adapted coordinates

For a point with time coordinate \(t\) and spatial radius \(r\), set

\[
\delta=1-r,
\qquad
a=\delta+t,
\qquad
b=\delta-t.
\]

Then

\[
a\ge0,
\qquad
b\ge0,
\qquad
a+b\le2,
\]

with

\[
t=\frac{a-b}{2},
\qquad
r=1-\frac{a+b}{2}.
\]

The codimension-two null joint is

\[
a=b=0.
\]

The endpoint proper-time squares are exactly

\[
\tau(p,x)^2=a(2-b),
\]

\[
\tau(x,q)^2=b(2-a).
\]

## 3. Ordered comparable-pair coordinates

Assume \(x\prec y\). Set

\[
a_x=\alpha,
\qquad
b_y=\beta,
\]

and define

\[
A=a_y-a_x\ge0,
\qquad
B=b_x-b_y\ge0.
\]

Thus

\[
a_y=\alpha+A,
\qquad
b_x=\beta+B.
\]

Let \(\theta\) be the relative spatial angle. A direct calculation gives

\[
\boxed{
\tau(x,y)^2
=
AB
-
2r_xr_y(1-\cos\theta).
}
\]

Hence the pair is causal exactly when

\[
2r_xr_y(1-\cos\theta)<AB.
\]

## 4. Exact \(d=4\) pair measure

In four spacetime dimensions,

\[
d\mu
=
\frac{3}{4\pi}
r^2\,da\,db\,d\Omega_2.
\]

Within the unsaturated causal-cap regime define

\[
u
=
\frac{
2r_xr_y(1-\cos\theta)
}{
AB
},
\qquad
0\le u\le1.
\]

After integrating the global angular direction, the ordered-pair measure is exactly

\[
\boxed{
d\mu(x)\,d\mu(y)
=
\frac94
r_xr_y\,AB\,
d\alpha\,d\beta\,dA\,dB\,du.
}
\]

The null-joint small-\(\Delta\) sector lies inside this regime for sufficiently small \(\varepsilon\).

## 5. Exact disagreement polynomial

For \(x\prec y\),

\[
\Delta(x,y)
=
\frac{
\tau(p,y)^4-\tau(p,x)^4
+
\tau(x,q)^4-\tau(y,q)^4
-
2\tau(x,y)^4
}{16}.
\]

In the pair coordinates,

\[
\begin{aligned}
\Delta
={}&
\frac12\alpha A
+
\frac14A^2
+
\frac12\beta B
+
\frac14B^2\\
&+
\frac14\alpha^2B
-\frac12\alpha\beta A
-\frac12\alpha\beta B
-\frac14\alpha B^2\\
&+
\frac14\beta^2A
-\frac14\beta A^2
-
\frac18(1-u)^2A^2B^2.
\end{aligned}
\]

This identity is exact.

## 6. The unique degeneracy of the diagonal

At \(A=B=0\), the first derivatives in the two causal-increment directions are

\[
\boxed{
c_A(\alpha,\beta)
=
\frac{
2\alpha-2\alpha\beta+\beta^2
}{4},
}
\]

\[
\boxed{
c_B(\alpha,\beta)
=
\frac{
\alpha^2-2\alpha\beta+2\beta
}{4}.
}
\]

On the physical triangle

\[
\alpha\ge0,
\qquad
\beta\ge0,
\qquad
\alpha+\beta\le2,
\]

both coefficients are strictly positive except at

\[
(\alpha,\beta)=(0,0).
\]

For \(c_A\),

\[
4c_A
=
\beta^2+2\alpha(1-\beta).
\]

If \(\beta\le1\), this is nonnegative and vanishes only for \(\alpha=\beta=0\).

If \(\beta\ge1\), the coefficient of \(\alpha\) is nonpositive, so the minimum on

\[
0\le\alpha\le2-\beta
\]

occurs at \(\alpha=2-\beta\), where

\[
4c_A
\ge
3(\beta-1)^2+1
>
0.
\]

The proof for \(c_B\) is the symmetric argument with \(\alpha\) and \(\beta\) exchanged.

Thus the only point at which the linear response of \(\Delta\) to both causal increments disappears is the null joint.

The exact polynomial and coefficient identities are independently checked by tools/verify_d4_twin_asymptotic_symbolic.py.

## 7. Complement of the joint is subleading

Fix \(\eta>0\) and consider

\[
\alpha+\beta\ge\eta.
\]

Compactness and the positivity of \(c_A,c_B\) give \(m_\eta>0\) such that

\[
c_A\ge m_\eta,
\qquad
c_B\ge m_\eta.
\]

The exact expansion then implies, uniformly for sufficiently small \(A+B\),

\[
\Delta
\ge
\frac{m_\eta}{2}(A+B).
\]

If \(A+B\) is not small, continuity and the distinguishing property of Minkowski causal neighborhoods give a positive lower bound for \(\Delta\). Therefore

\[
\Delta\le\varepsilon
\]

forces

\[
A=O(\varepsilon),
\qquad
B=O(\varepsilon)
\]

uniformly away from the joint.

### Unsaturated causal cap

The exact pair density contains \(AB\). Hence

\[
\int_0^{C\varepsilon}\!\!\int_0^{C\varepsilon}
AB\,dA\,dB
=
O(\varepsilon^4).
\]

### Saturated causal cap

Set

\[
c=2-\alpha-\beta.
\]

The cap saturates only when

\[
A+B>c.
\]

Since \(A+B=O(\varepsilon)\), saturation forces \(c=O(\varepsilon)\). Then

\[
r_x,r_y=O(\varepsilon),
\]

so the original radial density contributes

\[
r_x^2r_y^2=O(\varepsilon^4).
\]

This sector is smaller still.

Therefore

\[
\boxed{
F_4^{\mathrm{outside\ joint}}(\varepsilon)
=
O(\varepsilon^4).
}
\]

A single null face does not produce a separate lower exponent: away from the joint, the opposite causal-cone term restores a nonzero linear response.

## 8. Blow-up of the null joint

In a sufficiently small joint neighborhood set

\[
\alpha=\sqrt{\varepsilon}\,\bar\alpha,
\qquad
\beta=\sqrt{\varepsilon}\,\bar\beta,
\]

\[
A=\sqrt{\varepsilon}\,\bar A,
\qquad
B=\sqrt{\varepsilon}\,\bar B.
\]

Then

\[
r_xr_y\to1,
\]

and

\[
\frac{\Delta}{\varepsilon}
\longrightarrow
H,
\]

where

\[
\boxed{
H
=
\frac{
2\bar\alpha\bar A+\bar A^2
+
2\bar\beta\bar B+\bar B^2
}{4}.
}
\]

The exact remainder terms are one order higher under this scaling.

Moreover, in a sufficiently small fixed chart,

\[
\Delta
\ge
(1-C\eta)
\left(
\frac12\alpha A+\frac14A^2
+
\frac12\beta B+\frac14B^2
\right),
\]

which supplies an integrable dominating bound after rescaling.

## 9. Limiting step integral

Define

\[
g(\alpha,A)=2\alpha A+A^2.
\]

Then

\[
H
=
\frac{
g(\alpha,A)+g(\beta,B)
}{4}.
\]

At fixed \(A\),

\[
d\alpha=\frac{dg}{2A},
\]

so

\[
A\,d\alpha\,dA
=
\frac12\,dg\,dA.
\]

The constraint \(\alpha\ge0\) gives

\[
0\le A\le\sqrt g,
\]

and therefore the one-side density is

\[
w(g)=\frac{\sqrt g}{2}.
\]

Thus

\[
\begin{aligned}
J_{\mathrm{step}}
&=
\int_{H\le1}
AB\,
d\alpha\,dA\,d\beta\,dB\\
&=
\frac14
\int_{g_1+g_2\le4}
g_1^{1/2}g_2^{1/2}\,
dg_1\,dg_2\\
&=
\boxed{\frac{2\pi}{3}}.
\end{aligned}
\]

For one time orientation the geometric prefactor is \(9/4\). Including both orientations,

\[
2\cdot\frac94\cdot\frac{2\pi}{3}
=
3\pi.
\]

Together with the \(O(\varepsilon^4)\) complement,

\[
\boxed{
F_4(\varepsilon)
=
3\pi\varepsilon^3
+
o(\varepsilon^3).
}
\]

## 10. Twin-count asymptotic

The exact pair-count identity is

\[
\mathbb E[T_n]
=
\binom n2
\int_0^1
(1-\delta)^{n-2}\,dF_4(\delta).
\]

Since

\[
F_4(\delta)
\sim
3\pi\delta^3,
\]

the Laplace-Stieltjes asymptotic gives

\[
\int_0^1
(1-\delta)^{n-2}\,dF_4(\delta)
\sim
\frac{
3\pi\Gamma(4)
}{
n^3
}.
\]

Using \(\Gamma(4)=6\) and \(\binom n2\sim n^2/2\),

\[
\boxed{
\mathbb E[T_n]
\sim
\frac{9\pi}{n}.
}
\]

## 11. Independent finite-\(n\) diagnostic

The analytic target is

\[
9\pi
=
28.2743338823\ldots
\]

for \(n\,\mathbb E[T_n]\).

Direct graph simulations converge slowly because the blown-up variables have long tails. The importance sampler tools/minkowski_null_joint_twin_asymptotic.py samples directly from the limiting Laplace measure.

A representative two-million-sample run gave:

| \(n\) | estimate of \(n\,\mathbb E[T_n]\) |
|---:|---:|
|100|14.20|
|300|17.53|
|1000|20.20|
|3000|22.01|
|10000|23.52|
|30000|24.58|
|100000|25.48|

The numerical values are diagnostic only. The coefficient \(9\pi\) comes from the analytic calculation.

## 12. Dimensional interpretation

The same joint blow-up in spacetime dimension \(d\) has local exponent

\[
\boxed{
\beta_{\mathrm{joint}}(d)
=
2+\frac4d.
}
\]

Generic pairs away from the joint have the ordinary local exponent

\[
\boxed{
\beta_{\mathrm{bulk}}(d)=d.
}
\]

The joint dominates when

\[
2+\frac4d<d.
\]

The first integer spacetime dimension satisfying this inequality is

\[
\boxed{d=4}.
\]

For \(d=3\),

\[
3<\frac{10}{3},
\]

so the bulk dominates.

For \(d=4\),

\[
3<4,
\]

so the codimension-two null joint dominates.

## 13. Literature boundary

The null joint itself is not new. Buck, Dowker, Jubb, and Surya showed that the continuum limit of the mean causal-set action for a flat Alexandrov interval contains a contribution equal to the volume of the codimension-two joint.

Bombelli's 1987 dissertation also used symmetric differences of Alexandrov neighborhoods to quantify disagreement between causal structures.

Accordingly, this project does not claim novelty for either null joints or symmetric-difference causal comparisons.

The project-specific result is the chain

\[
\text{arrow erasure}
\longrightarrow
\text{comparability graph}
\longrightarrow
\text{true-twin module}
\longrightarrow
\Delta(x,y)
\longrightarrow
3\pi\varepsilon^3
\longrightarrow
\frac{9\pi}{n}.
\]

No equivalent result was located in the targeted literature review. This remains limited negative evidence, not proof of absolute priority.

## 14. References

- Luca Bombelli, **Space-time as a causal set**, PhD dissertation, Syracuse University, 1987.
- Luca Bombelli, Joohan Lee, David Meyer, and Rafael D. Sorkin, **Space-time as a causal set**, *Physical Review Letters* 59 (1987), 521–524. DOI: 10.1103/PhysRevLett.59.521.
- Michel Buck, Fay Dowker, Ian Jubb, and Sumati Surya, **Boundary terms for causal sets**, *Classical and Quantum Gravity* 32 (2015), 205004. DOI: 10.1088/0264-9381/32/20/205004.
- Sumati Surya, **The causal set approach to quantum gravity**, *Living Reviews in Relativity* 22, 5 (2019). DOI: 10.1007/s41114-019-0023-1.
- Martin Aigner and Geert Prins, **Uniquely Partially Orderable Graphs**, *Journal of the London Mathematical Society* s2-3 (1971), 260–266. DOI: 10.1112/jlms/s2-3.2.260.
- Rolf H. Möhring, **Almost all comparability graphs are UPO**, *Discrete Mathematics* 50 (1984), 63–70. DOI: 10.1016/0012-365X(84)90035-9.
- Ross M. McConnell and Jeremy P. Spinrad, **Modular decomposition and transitive orientation**, *Discrete Mathematics* 201 (1999), 189–241. DOI: 10.1016/S0012-365X(98)00319-7.

## 15. What the theorem does not prove

The theorem removes the dominant size-two non-stable module asymptotically:

\[
\mathbb E[T_n]\to0.
\]

It does **not** yet prove

\[
p_4^{\mathrm{UPO}}(n)\to1.
\]

Larger non-stable modules and other multiple-implication-class configurations still require control.

The next question is:

> after size-two comparable twin modules vanish as \(9\pi/n\), what is the leading asymptotic probability of all remaining UPO obstructions in \(3+1\) Minkowski sprinklings?
