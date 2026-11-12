# Theorem: comparable-twin tail in 3+1 Minkowski sprinklings

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem for the fixed Alexandrov-interval ensemble  
**Physical status:** causal-set reconstruction result after erasing causal arrows  
**Novelty status:** targeted literature review has not located an equivalent theorem; absolute priority is not certified

## 1. Statement

Let (D=I(p,q)subsetmathbb M^4) be the flat Alexandrov interval with

[
p=(-1,mathbf0),
qquad
q=(1,mathbf0),
]

equipped with normalized spacetime volume measure (mu).

For (xin D), define its symmetric comparability neighborhood

[
A_x
=
{zin D: zprec x 	ext{or} xprec z}.
]

For iid (X,Ysimmu), define

[
Delta(X,Y)
=
mu(A_X	riangle A_Y).
]

Let

[
F_4(arepsilon)
=
Pr(
Xsim Y,,
Delta(X,Y)learepsilon
).
]

Then

[
oxed{
F_4(arepsilon)
sim
3pi,arepsilon^3
qquad
(arepsilondownarrow0).
}
]

Now let (T_n) be the number of adjacent true-twin pairs in the unoriented comparability graph of an iid size-(n) sprinkling into (D).

Then

[
oxed{
mathbb E[T_n]
sim
rac{9pi}{n}
qquad
(n	oinfty).
}
]

The second statement follows from the first through the exact identity

[
mathbb E[T_n]
=
inom n2
int_0^1
(1-delta)^{n-2},dF_4(delta).
]

## 2. Joint-adapted coordinates

Write a point in the diamond using

[
delta=1-r,
qquad
a=delta+t,
qquad
b=delta-t.
]

Then

[
age0,
qquad
bge0,
qquad
a+ble2,
]

and

[
t=rac{a-b}{2},
qquad
r=1-rac{a+b}{2}.
]

The codimension-two null joint is

[
a=b=0.
]

The endpoint proper-time squares are

[
	au(p,x)^2=a(2-b),
]

[
	au(x,q)^2=b(2-a).
]

## 3. Ordered comparable-pair coordinates

Assume

[
xprec y.
]

Set

[
a_x=alpha,
qquad
b_y=eta,
]

and

[
A=a_y-a_xge0,
qquad
B=b_x-b_yge0.
]

Thus

[
a_y=alpha+A,
qquad
b_x=eta+B.
]

Let (	heta) be the relative spatial angle.

The exact pair proper-time square is

[
oxed{
	au(x,y)^2
=
AB
-
2r_xr_y(1-cos	heta).
}
]

Therefore the pair is causal exactly when

[
2r_xr_y(1-cos	heta)<AB.
]

## 4. Exact d=4 pair measure

In four spacetime dimensions,

[
dmu
=
rac{3}{4pi}
r^2,da,db,dOmega_2.
]

Within the unsaturated causal-cap regime, define

[
u
=
rac{
2r_xr_y(1-cos	heta)
}{AB},
qquad
0le ule1.
]

After integrating the global angular direction, the ordered-pair measure is exactly

[
oxed{
dmu(x)dmu(y)
=
rac94
r_xr_y,AB,
dalpha,deta,dA,dB,du.
}
]

The null-joint small-(Delta) sector is always inside this regime for sufficiently small (arepsilon).

## 5. Exact disagreement formula

For (xprec y),

[
Delta(x,y)
=
rac{
	au(p,y)^4-	au(p,x)^4
+
	au(x,q)^4-	au(y,q)^4
-
2	au(x,y)^4
}{16}.
]

Equivalently, in the pair coordinates above,

[
egin{aligned}
Delta
={}&
rac12alpha A
+
rac14A^2
+
rac12eta B
+
rac14B^2\
&+
rac14alpha^2B
-rac12alphaeta A
-rac12alphaeta B
-rac14alpha B^2\
&+
rac14eta^2A
-rac14eta A^2
-
rac18(1-u)^2A^2B^2.
end{aligned}
]

This polynomial identity is exact.

## 6. The unique degeneracy of the diagonal

At (A=B=0), the first derivatives in the two causal-increment directions are

[
oxed{
c_A(alpha,eta)
=
rac{
2alpha-2alphaeta+eta^2
}{4},
}
]

and

[
oxed{
c_B(alpha,eta)
=
rac{
alpha^2-2alphaeta+2eta
}{4}.
}
]

On the closed triangle

[
alphage0,
qquad
etage0,
qquad
alpha+etale2,
]

both coefficients are strictly positive except at

[
(alpha,eta)=(0,0).
]

Hence the only point at which the linear response of (Delta) to both causal increments disappears is the null joint.

This fact is what separates the joint from the rest of the diamond.

## 7. Complement of the joint is subleading

Fix (eta>0), and consider the region

[
alpha+etageeta.
]

Compactness and the positivity of (c_A,c_B) give a constant

[
m_eta>0
]

such that

[
c_Age m_eta,
qquad
c_Bge m_eta
]

throughout that region.

The exact polynomial expansion then implies, uniformly for sufficiently small (A+B),

[
Delta
ge
rac{m_eta}{2}(A+B).
]

If (A+B) is not small, continuity and the distinguishing property of Minkowski causal neighborhoods give a positive lower bound for (Delta).

Therefore

[
Deltalearepsilon
]

forces

[
A=O(arepsilon),
qquad
B=O(arepsilon)
]

uniformly away from the joint.

### Unsaturated causal cap

The exact pair density contains the factor

[
AB.
]

Integrating

[
0le A,Ble C_etaarepsilon
]

therefore gives

[
O(arepsilon^4).
]

### Saturated causal cap

Write

[
c=2-alpha-eta.
]

The causal cap saturates only when

[
A+B>c.
]

Since (A+B=O(arepsilon)), this forces

[
c=O(arepsilon).
]

Then

[
r_x,r_y=O(arepsilon),
]

so the original radial measure contributes

[
r_x^2r_y^2=O(arepsilon^4).
]

Together with the (A,B) integration and the (c)-strip thickness, this sector is even smaller than (O(arepsilon^4)).

Hence

[
oxed{
F_4^{mathrm{outside joint}}(arepsilon)
=
O(arepsilon^4).
}
]

A single null face does not create a separate lower exponent.

The other causal cone supplies a nonzero linear term unless both null-depth coordinates vanish simultaneously.

## 8. Blow-up of the null joint

Now restrict to a sufficiently small joint neighborhood.

Set

[
alpha=sqrt{arepsilon},aralpha,
qquad
eta=sqrt{arepsilon},areta,
]

[
A=sqrt{arepsilon},ar A,
qquad
B=sqrt{arepsilon},ar B.
]

Then

[
r_xr_y	o1,
]

and

[
rac{Delta}{arepsilon}
longrightarrow
H,
]

where

[
oxed{
H
=
rac{
2aralphaar A+ar A^2
+
2aretaar B+ar B^2
}{4}.
}
]

The exact remainder terms are one order higher under this scaling.

Moreover, for a sufficiently small fixed joint chart,

[
Delta
ge
(1-Ceta)
left(
rac12alpha A+rac14A^2
+
rac12eta B+rac14B^2
ight),
]

so the rescaled integrands are dominated by an integrable limiting function.

This permits dominated convergence after the blow-up.

## 9. Evaluation of the limiting step integral

Define

[
g(alpha,A)
=
2alpha A+A^2.
]

Then

[
H
=
rac{
g(alpha,A)+g(eta,B)
}{4}.
]

For one side,

[
g=2alpha A+A^2
]

gives

[
dalpha
=
rac{dg}{2A}.
]

Thus

[
A,dalpha,dA
=
rac12,dg,dA.
]

The condition (alphage0) is equivalent to

[
0le Alesqrt g.
]

Therefore the induced one-side density is

[
w(g)
=
rac{sqrt g}{2}.
]

Hence

[
egin{aligned}
J_{mathrm{step}}
&=
int_{Hle1}
AB,
dalpha,dA,deta,dB\
&=
rac14
int_{g_1+g_2le4}
g_1^{1/2}g_2^{1/2}
,dg_1,dg_2.
end{aligned}
]

The beta-simplex integral gives

[
oxed{
J_{mathrm{step}}
=
rac{2pi}{3}.
}
]

For one time orientation, the geometric coefficient is

[
rac94.
]

Including both orientations,

[
2cdotrac94cdotrac{2pi}{3}
=
3pi.
]

Therefore

[
oxed{
F_4(arepsilon)
=
3piarepsilon^3
+
o(arepsilon^3).
}
]

Because the complement is (O(arepsilon^4)), no other sector contributes at the leading order.

## 10. Twin-count asymptotic

The exact pair-count identity is

[
mathbb E[T_n]
=
inom n2
int_0^1
(1-delta)^{n-2},dF_4(delta).
]

Since

[
F_4(delta)
sim
3pidelta^3,
]

the standard Laplace-Stieltjes asymptotic gives

[
int_0^1
(1-delta)^{n-2},dF_4(delta)
sim
rac{
3piGamma(4)
}{
n^3
}.
]

Using

[
Gamma(4)=6
]

and

[
inom n2simrac{n^2}{2},
]

we obtain

[
oxed{
mathbb E[T_n]
sim
rac{9pi}{n}.
}
]

Thus comparable true-twin obstructions vanish in expectation, but only at the slow rate

[
n^{-1}.
]

## 11. Independent finite-n diagnostic

The analytic coefficient is

[
9pi
=
28.2743338823ldots
]

for

[
n,mathbb E[T_n].
]

Direct graph simulations converge slowly because the limiting blown-up variables have long tails.

A dedicated importance sampler uses the exact limiting Laplace measure.

Representative estimates from a two-million-sample run were:

| (n) | estimate of (n,mathbb E[T_n]) |
|---:|---:|
|100|14.20|
|300|17.53|
|1000|20.20|
|3000|22.01|
|10000|23.52|
|30000|24.58|
|100000|25.48|

The sequence approaches the analytic target from below.

These numbers are validation only.

The theorem is the analytic argument above.

The reproducible implementation is:

[
	exttt{tools/minkowski_null_joint_twin_asymptotic.py}.
]

## 12. Dimensional interpretation

The same joint blow-up in spacetime dimension (d) has local exponent

[
oxed{
eta_{mathrm{joint}}(d)
=
2+rac4d.
}
]

Generic interior pairs instead have

[
oxed{
eta_{mathrm{bulk}}(d)=d.
}
]

Therefore the joint dominates when

[
2+rac4d<d.
]

This is equivalent to

[
d^2-2d-4>0.
]

The first integer spacetime dimension satisfying it is

[
oxed{
d=4.
}
]

For (d=3),

[
eta_{mathrm{bulk}}=3
<
rac{10}{3}
=
eta_{mathrm{joint}},
]

so the bulk controls the asymptotic small-(Delta) tail.

For (d=4),

[
eta_{mathrm{joint}}=3<4=eta_{mathrm{bulk}},
]

so the codimension-two null joint controls it.

## 13. Relation to established literature

The null joint itself is not new.

Buck, Dowker, Jubb, and Surya showed that the continuum limit of the mean causal-set action for a flat Alexandrov interval contains a contribution equal to the volume of the codimension-two joint.

Their observable is the causal-set action, not orientation recoverability.

Bombelli's 1987 dissertation also used symmetric differences of Alexandrov neighborhoods to quantify disagreement between causal structures.

Therefore this project does not claim that either null joints or symmetric-difference causal comparisons were invented here.

The contribution established in this note is the specific chain

[
	ext{arrow erasure}
longrightarrow
	ext{comparability graph}
longrightarrow
	ext{true-twin module}
longrightarrow
Delta(x,y)
longrightarrow
3piarepsilon^3
longrightarrow
rac{9pi}{n}.
]

No equivalent result was located in the targeted literature review.

That is limited negative evidence, not absolute proof of priority.

## 14. References

- Luca Bombelli, **Space-time as a causal set**, PhD dissertation, Syracuse University, 1987.
- Luca Bombelli, Joohan Lee, David Meyer, and Rafael D. Sorkin, **Space-time as a causal set**, *Physical Review Letters* 59 (1987), 521–524. DOI: 10.1103/PhysRevLett.59.521.
- Michel Buck, Fay Dowker, Ian Jubb, and Sumati Surya, **Boundary terms for causal sets**, *Classical and Quantum Gravity* 32 (2015), 205004. DOI: 10.1088/0264-9381/32/20/205004.
- Sumati Surya, **The causal set approach to quantum gravity**, *Living Reviews in Relativity* 22, 5 (2019). DOI: 10.1007/s41114-019-0023-1.
- Martin Aigner and Geert Prins, **Uniquely Partially Orderable Graphs**, *Journal of the London Mathematical Society* s2-3 (1971), 260–266. DOI: 10.1112/jlms/s2-3.2.260.
- Rolf H. Möhring, **Almost all comparability graphs are UPO**, *Discrete Mathematics* 50 (1984), 63–70. DOI: 10.1016/0012-365X(84)90035-9.
- Ross M. McConnell and Jeremy P. Spinrad, **Modular decomposition and transitive orientation**, *Discrete Mathematics* 201 (1999), 189–241. DOI: 10.1016/S0012-365X(98)00319-7.

## 15. What this theorem does not prove

The theorem removes the dominant size-two non-stable module asymptotically:

[
mathbb E[T_n]	o0.
]

It does **not** yet prove

[
p_4^{mathrm{UPO}}(n)	o1.
]

Larger non-stable modules and other multiple-implication-class configurations must still be controlled.

The next question is therefore:

> after size-two comparable twin modules vanish as (9pi/n), what is the leading asymptotic probability of all remaining UPO obstructions in (3+1) Minkowski sprinklings?

That is now the central higher-dimensional reconstruction problem.
