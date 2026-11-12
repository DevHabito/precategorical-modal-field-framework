# Null-joint scaling of comparable-twin obstructions in 3+1 Minkowski sprinklings

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact local-coordinate reduction + proved null-joint scaling contribution + global asymptotic conjecture pending complementary-sector upper bound  
**Physical status:** finite Alexandrov-interval causal-set reconstruction problem  
**Novelty status:** no absolute priority claim is made

## 1. Why this calculation matters

The higher-dimensional UPO audit found that most observed late finite failures are minimal non-stable modules: comparable twin pairs.

For a comparable pair (x,y), let

[
A_x={z:zsim x},
qquad
A_y={z:zsim y},
]

and define the normalized disagreement volume

[
Delta(x,y)=mu(A_x	riangle A_y).
]

If (T_n) is the number of comparable twin pairs in an iid size-(n) sprinkling, then

[
mathbb E[T_n]
=
inom n2
mathbb E!left[
mathbf 1_{{Xsim Y}}
(1-Delta(X,Y))^{n-2}
ight].
]

Thus the twin problem is controlled by the geometry of pairs with very small (Delta).

The previous numerical audit suggested that, in (3+1) spacetime, these pairs concentrate near the codimension-two joint where the two null boundaries of the Alexandrov interval meet.

This note derives the local scaling analytically.

## 2. Joint-adapted coordinates

Use the unit-height convention

[
D=I(p,q),
qquad
p=(-1,mathbf 0),
qquad
q=(1,mathbf 0).
]

For a point with time coordinate (t) and spatial radius (r), define

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

The null joint is

[
a=b=0.
]

The endpoint proper-time squares are exactly

[
	au(p,x)^2=a(2-b),
]

and

[
	au(x,q)^2=b(2-a).
]

## 3. Comparable-pair coordinates

Assume

[
xprec y.
]

Write

[
a_x=alpha,
qquad
b_y=eta,
]

and introduce positive causal increments

[
A=a_y-a_xge0,
qquad
B=b_x-b_yge0.
]

Thus

[
x=(alpha,eta+B,mathbf n_x),
]

[
y=(alpha+A,eta,mathbf n_y)
]

in ((a,b,	ext{angle})) coordinates.

Let (	heta) be the angle between the spatial unit vectors.

A direct calculation gives the exact interval relation

[
oxed{
	au(x,y)^2
=
AB
-
2r_xr_y(1-cos	heta)
}.
]

Hence (xprec y) exactly when

[
2r_xr_y(1-cos	heta)<AB.
]

Near the joint,

[
r_x,r_y	o1,
]

so the causal angular cap has

[
	heta^2lesssim AB.
]

## 4. Exact pair measure in d=4

In four spacetime dimensions the normalized single-point measure is

[
dmu
=
rac{3}{4pi}
r^2,da,db,dOmega_2.
]

For an ordered comparable pair (xprec y), integrate over the global angular direction and parameterize the relative causal cap by

[
u
=
rac{
2r_xr_y(1-cos	heta)
}{
AB
},
qquad
0le ule1.
]

The angular integration is exact in the unsaturated cap regime and gives

[
oxed{
dmu(x),dmu(y)
=
rac94
r_xr_y
AB,
dalpha,deta,dA,dB,du
}.
]

The small-(Delta) joint regime lies inside this unsaturated-cap sector.

## 5. Leading disagreement geometry

For (d=4), the exact disagreement formula is

[
Delta(x,y)
=
rac{
	au(p,y)^4-	au(p,x)^4+
	au(x,q)^4-	au(y,q)^4-
2	au(x,y)^4
}{16}.
]

Scale all four joint variables by a common small parameter (lambda):

[
alpha=lambdaaralpha,
qquad
eta=lambdaareta,
qquad
A=lambdaar A,
qquad
B=lambdaar B.
]

Then

[
oxed{
Delta(x,y)
=
lambda^2
H(aralpha,areta,ar A,ar B)
+
O(lambda^3)
}
]

uniformly on compact scaled sets, where

[
oxed{
H
=
rac{
2aralphaar A+ar A^2+
2aretaar B+ar B^2
}{4}.
}
]

The interval term involving (	au(x,y)^4) is (O(lambda^4)) and therefore does not enter the leading homogeneous form.

Thus

[
Delta=O(arepsilon)
]

in the joint sector when

[
lambda=sqrt{arepsilon}.
]

## 6. Why the exponent is three

Under the scaling

[
alpha,eta,A,Bmapstolambda(alpha,eta,A,B),
]

the scalar differential contributes

[
lambda^4,
]

while the causal angular factor (AB) contributes

[
lambda^2.
]

Therefore the ordered-pair measure scales as

[
lambda^6.
]

Since

[
arepsilon=lambda^2,
]

the joint contribution scales as

[
oxed{
arepsilon^3.
}
]

This is not a fitted exponent.

It follows from the local Lorentzian geometry and the codimension-two null joint.

## 7. Exact d=4 tail coefficient of the joint scaling sector

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

For one side, use the change of variables

[
g=2alpha A+A^2.
]

At fixed (A),

[
dalpha
=
rac{dg}{2A}.
]

Hence

[
A,dalpha,dA
=
rac12,dg,dA,
]

and the condition (alphage0) gives

[
0le Alesqrt g.
]

Therefore the induced one-side density is

[
oxed{
w(g)=rac{sqrt g}{2}.
}
]

The leading step integral is

[
J_{mathrm{step}}
=
int_{Hle1}
AB,
dalpha,dA,deta,dB.
]

Equivalently,

[
J_{mathrm{step}}
=
rac14
int_{g_1+g_2le4}
g_1^{1/2}g_2^{1/2},dg_1,dg_2.
]

The beta-simplex integral gives

[
oxed{
J_{mathrm{step}}
=
rac{2pi}{3}.
}
]

For one time orientation, the geometric prefactor is (9/4).

The symmetric comparability event contains both

[
xprec y
]

and

[
yprec x.
]

Thus the complete null-joint scaling contribution to the small-disagreement tail has coefficient

[
2cdotrac94cdotrac{2pi}{3}
=
3pi.
]

This yields the rigorous local contribution

[
oxed{
liminf_{arepsilondownarrow0}
rac{F_4(arepsilon)}
{arepsilon^3}
ge
3pi,
}
]

where

[
F_4(arepsilon)
=
Pr(
Xsim Y,,
Delta(X,Y)learepsilon
).
]

The inequality is stated rather than equality because the complementary bulk and single-null-face sectors have not yet been given a complete global upper bound in the repository.

## 8. Exact Laplace coefficient for twin expectation

For the twin expectation the relevant limiting integral is

[
J_{mathrm{Lap}}
=
int
AB,e^{-H}
dalpha,dA,deta,dB.
]

Using the same (g)-variables,

[
int_0^infty
rac{sqrt g}{2}
e^{-g/4},dg
=
2sqrtpi.
]

Therefore

[
oxed{
J_{mathrm{Lap}}
=
4pi.
}
]

For the expectation

[
mathbb E[T_n]
=
inom n2
mathbb E[
mathbf1_{{Xsim Y}}
(1-Delta)^{n-2}
],
]

the two time orientations cancel the asymptotic factor (1/2) from

[
inom n2.
]

The null-joint contribution therefore gives

[
oxed{
liminf_{n	oinfty}
n,mathbb E[T_n]
ge
rac94(4pi)
=
9pi.
}
]

Equivalently, the joint sector alone contributes asymptotically at least

[
oxed{
rac{9pi}{n}
}
]

to the expected comparable-twin count.

Again, equality requires an upper bound on all complementary sectors.

## 9. Why finite simulations approach the coefficient slowly

Direct finite-(n) simulations substantially underestimate (9pi) at accessible sizes.

This is not evidence against the scaling calculation.

The limiting scaled variables are unbounded.

Configurations with large scaled base depth and very small causal increment converge slowly to the limiting measure.

The dedicated importance sampler

[
	exttt{tools/minkowski_null_joint_twin_asymptotic.py}
]

samples directly from the limiting Laplace measure.

A representative two-million-sample run gave the following estimates for the null-joint contribution to

[
n,mathbb E[T_n].
]

| (n) | importance estimate |
|---:|---:|
|100|14.20|
|300|17.53|
|1000|20.20|
|3000|22.01|
|10000|23.52|
|30000|24.58|
|100000|25.48|

The analytic limiting target is

[
9pi
=
28.27433388ldots
]

The slow monotone approach explains why finite graph simulations around (nsim10^2) should not be used to estimate the asymptotic coefficient directly.

The numerical calculation is diagnostic only.

The constants (3pi) and (9pi) come from the analytic integrals above.

## 10. General dimensional scaling

Let

[
m=rac d2.
]

In general dimension the leading joint disagreement is

[
H_m
=
2^{-m}
left[
(alpha+A)^m-alpha^m
+
(eta+B)^m-eta^m
ight].
]

The causal angular cap contributes

[
(AB)^{m-1}.
]

Scaling all four scalar variables by

[
lambda=arepsilon^{1/m}
]

therefore gives the joint exponent

[
oxed{
eta_{mathrm{joint}}(d)
=
2+rac4d.
}
]

For comparison, ordinary interior closeness gives

[
oxed{
eta_{mathrm{bulk}}(d)=d.
}
]

A mixed sector in which only one side approaches a null face gives the scaling exponent

[
oxed{
eta_{mathrm{face}}(d)
=
rac d2+1+rac2d.
}
]

These three exponents imply a dimension-dependent competition.

### d=3

[
eta_{mathrm{bulk}}=3,
]

[
eta_{mathrm{face}}=rac{19}{6}approx3.1667,
]

[
eta_{mathrm{joint}}=rac{10}{3}approx3.3333.
]

Thus the bulk should dominate asymptotically.

This means the earlier finite-window effective slope below three should not be interpreted as the true asymptotic exponent.

### d=4

[
eta_{mathrm{joint}}=3,
]

[
eta_{mathrm{face}}=rac72,
]

[
eta_{mathrm{bulk}}=4.
]

Thus the codimension-two null joint is the unique lowest-exponent sector.

This explains why the boundary changes the (3+1) asymptotic qualitatively.

## 11. The convergence threshold

The one-side homogeneous integral can be written

[
L_m
=
rac1{m+1}
int_0^infty
left[
(1+t)^m-t^m
ight]^{-(m+1)/m}
dt.
]

At large (t),

[
(1+t)^m-t^m
sim
m t^{m-1}.
]

Therefore the integrand behaves as

[
t^{-(m-1/m)}.
]

The integral converges exactly when

[
m-rac1m>1.
]

Equivalently,

[
m^2-m-1>0.
]

Thus

[
m>rac{1+sqrt5}{2}.
]

In integer spacetime dimension this becomes

[
oxed{
dge4.
}
]

So the same dimension at which the null-joint exponent overtakes the bulk is also the first integer dimension in which the homogeneous joint integral becomes self-contained.

This is a structural threshold, not a fitted crossover.

## 12. Relation to existing causal-set boundary literature

Codimension-two joints of Alexandrov intervals are already important in causal-set theory.

Buck, Dowker, Jubb, and Surya showed that the continuum limit of the mean causal-set action for a flat Alexandrov interval contains a contribution equal to the volume of the codimension-two joint.

That result concerns the causal-set action, not orientation recoverability or graph modules.

The present calculation is therefore not a discovery of the null joint itself.

What is different here is that the same geometric locus controls a reconstruction obstruction after causal arrows are erased.

There is also an important novelty correction concerning symmetric differences.

Bombelli's 1987 dissertation already used symmetric differences of Alexandrov neighborhoods as a way to quantify disagreement between causal structures/metrics.

Modern Lorentzian metric-space work likewise uses symmetric differences of causal futures or pasts in metric comparison constructions.

Therefore the project should **not** claim that the use of symmetric difference as a causal-geometric comparison tool is itself new.

The project-specific object is narrower:

[
Delta(x,y)
=
mu(A_x	riangle A_y)
]

for comparability neighborhoods of two events in the **same** spacetime, linked to the probability that they become true twins in the arrow-erased comparability graph.

## 13. Literature references

- Luca Bombelli, **Space-time as a causal set**, PhD dissertation, Syracuse University, 1987.
- Luca Bombelli, Joohan Lee, David Meyer, and Rafael D. Sorkin, **Space-time as a causal set**, *Physical Review Letters* 59 (1987), 521–524. DOI: 10.1103/PhysRevLett.59.521.
- Michel Buck, Fay Dowker, Ian Jubb, and Sumati Surya, **Boundary terms for causal sets**, *Classical and Quantum Gravity* 32 (2015), 205004. DOI: 10.1088/0264-9381/32/20/205004.
- Sumati Surya, **The causal set approach to quantum gravity**, *Living Reviews in Relativity* 22, 5 (2019). DOI: 10.1007/s41114-019-0023-1.
- Martin Aigner and Geert Prins, **Uniquely Partially Orderable Graphs**, *Journal of the London Mathematical Society* s2-3 (1971), 260–266. DOI: 10.1112/jlms/s2-3.2.260.
- Rolf H. Möhring, **Almost all comparability graphs are UPO**, *Discrete Mathematics* 50 (1984), 63–70. DOI: 10.1016/0012-365X(84)90035-9.
- Ross M. McConnell and Jeremy P. Spinrad, **Modular decomposition and transitive orientation**, *Discrete Mathematics* 201 (1999), 189–241. DOI: 10.1016/S0012-365X(98)00319-7.

## 14. What is proved and what is not

### Established in this note

The following are analytic consequences of the local null-joint geometry:

[
Delta
=
lambda^2 H+O(lambda^3)
]

in (d=4);

[
eta_{mathrm{joint}}(4)=3;
]

[
J_{mathrm{step}}=rac{2pi}{3};
]

[
J_{mathrm{Lap}}=4pi;
]

and the null-joint sector yields the lower asymptotic contributions

[
oxed{
liminf_{arepsilondownarrow0}
rac{F_4(arepsilon)}{arepsilon^3}
ge3pi
}
]

and

[
oxed{
liminf_{n	oinfty}
n,mathbb E[T_n]
ge9pi.
}
]

### Not yet established

The repository does not yet contain a complete proof that

[
F_4(arepsilon)
sim
3piarepsilon^3
]

or

[
mathbb E[T_n]
sim
rac{9pi}{n}.
]

To promote the lower contributions to equalities, the remaining task is to prove that:

1. the ordinary bulk contributes (O(arepsilon^4));
2. a single-null-face sector contributes (O(arepsilon^{7/2}));
3. the timelike tips and all remaining boundary charts are (o(arepsilon^3));
4. no nonlocal pair family produces an additional (arepsilon^3) contribution.

Only after those complementary estimates are closed should (3pi) and (9pi) be advertised as the complete asymptotic constants.

## 15. Current research consequence

The next step is now sharply defined.

The main target is no longer another Monte Carlo extension.

It is the complementary-sector estimate

[
oxed{
F_4(arepsilon)
-
F_4^{mathrm{joint}}(arepsilon)
=
o(arepsilon^3).
}
]

If that is proved, then

[
oxed{
F_4(arepsilon)
sim3piarepsilon^3
}
]

and

[
oxed{
mathbb E[T_n]
simrac{9pi}{n}.
}
]

That would turn the currently dominant finite UPO obstruction in (3+1) Minkowski sprinklings into a fully controlled Lorentzian boundary asymptotic.
