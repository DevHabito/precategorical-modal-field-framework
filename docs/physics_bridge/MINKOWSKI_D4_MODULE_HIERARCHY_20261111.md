# Size-three module hierarchy after the d=4 twin theorem

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact expectation identity + analytic scaling order + reproducible finite-n audit  
**Physical status:** causal-set reconstruction after arrow erasure  
**Novelty status:** no equivalent causal-set module hierarchy was located in the targeted review; absolute priority is not certified

## 1. Motivation

The d=4 true-twin theorem gives

[
mathbb E[T_n]
sim
rac{9pi}{n},
]

where (T_n) counts adjacent true-twin pairs in the arrow-erased comparability graph.

True twins are the minimal size-two non-stable modules and dominate the observed finite UPO failures.

The next question is:

> what is the first obstruction after true-twin pairs are absent?

Finite audits show that the next recurrent minimal obstruction is an induced (P_3) graph module.

Its two leaves are incomparable false twins, while the center is comparable to both.

## 2. Size-three non-stable module

Let

[
M={x,y,z}.
]

The set (M) is a graph module when every vertex outside (M) is adjacent either to all three vertices or to none of them.

If the induced graph (G[M]) is a path (P_3), then (M) contains edges and is therefore non-stable.

Such a module obstructs unique partial orderability.

If a size-three module induces a triangle, it already contains true-twin pairs.

Thus, after conditioning away adjacent true twins, the induced (P_3) is the first genuinely new size-three obstruction.

## 3. Exact three-point disagreement volume

For three continuum events (x_1,x_2,x_3), define

[
Delta_3(x_1,x_2,x_3)
=
mu
left{
w:
igl(
mathbf1_{wsim x_1},
mathbf1_{wsim x_2},
mathbf1_{wsim x_3}
igr)
	ext{ is not constant}
ight}.
]

Equivalently,

[
Delta_3
=
mu
left[
(A_{x_1}	riangle A_{x_2})
cup
(A_{x_1}	riangle A_{x_3})
ight].
]

A sampled outside event preserves the module condition exactly when it lies outside this disagreement region.

Let (M_{3,n}) be the number of induced-(P_3) modules in an iid size-(n) sprinkling.

Then

[
oxed{
mathbb E[M_{3,n}]
=
inom n3
mathbb E
left[
mathbf1_{{	ext{induced }P_3}}
(1-Delta_3)^{n-3}
ight].
}
]

This identity is exact.

No graph-enumeration approximation enters it.

## 4. Why the d=4 joint gives an epsilon-to-the-fifth tail

Near the codimension-two null joint, use the same null-depth coordinates as in the true-twin theorem.

Set

[
lambda=sqrt{arepsilon}.
]

For each event, the two null-depth coordinates scale as

[
O(lambda).
]

For three events, those six scalar coordinates contribute

[
lambda^6.
]

Fix the global angular direction of one event.

The other two events must lie within relative angular distances

[
O(lambda)
]

of the same joint direction in order to produce the required local comparability pattern while keeping all three comparability neighborhoods close.

In (3+1) spacetime the joint is a two-sphere, so each relative angular displacement contributes

[
lambda^2.
]

There are two independent relative angular displacements.

Hence the angular contribution is

[
lambda^4.
]

The total joint measure therefore scales as

[
lambda^{10}.
]

Since

[
arepsilon=lambda^2,
]

this is

[
oxed{
arepsilon^5.
}
]

The induced-(P_3) condition is open in the scaled local variables: there are open sets in which one event is comparable to the other two while the two leaves remain mutually spacelike.

Therefore the joint sector supplies both a nonzero lower-order contribution and the correct local upper scaling.

## 5. Why the bulk is subleading

Away from the null joint, the pairwise disagreement map has a nonzero linear response.

If

[
Delta_3learepsilon,
]

then every pairwise symmetric difference also satisfies

[
Delta(x_i,x_j)learepsilon,
]

because

[
A_{x_i}	riangle A_{x_j}
subseteq
{	ext{three-way disagreement}}.
]

Away from the joint this forces each of the two additional events to lie within an ordinary (O(arepsilon)) four-dimensional displacement of the first event.

The two relative displacements therefore contribute

[
O(arepsilon^8).
]

Thus the ordinary bulk is smaller than the joint contribution:

[
arepsilon^8
=
o(arepsilon^5).
]

The same compactness argument used in the true-twin theorem excludes an additional lower-order sector away from the joint.

## 6. Size-three tail law

Define

[
G_{P_3}(arepsilon)
=
Pr
left(
	ext{the three sampled events induce }P_3,
;
Delta_3learepsilon
ight).
]

The joint blow-up and the bulk estimate give

[
oxed{
G_{P_3}(arepsilon)
=
Theta(arepsilon^5)
qquad
(arepsilondownarrow0).
}
]

The current analysis establishes the exponent but does not yet evaluate the leading constant.

## 7. Consequence for the expected module count

Insert the tail order into the exact expectation identity.

A Laplace-Stieltjes scaling with exponent five gives

[
mathbb E
left[
mathbf1_{{P_3}}
(1-Delta_3)^{n-3}
ight]
=
Theta(n^{-5}).
]

Since

[
inom n3
=
Theta(n^3),
]

we obtain

[
oxed{
mathbb E[M_{3,n}]
=
Theta(n^{-2}).
}
]

Thus the first genuinely new size-three obstruction vanishes one full power of (n) faster than the true-twin obstruction:

[
mathbb E[T_n]
=
Theta(n^{-1}),
]

[
mathbb E[M_{3,n}]
=
Theta(n^{-2}).
]

## 8. Reproducible finite-n audit

The repository tool

[
	exttt{tools/minkowski_module_hierarchy_audit.py}
]

counts true-twin pairs and induced-(P_3) modules directly from Minkowski comparability graphs.

An independent (d=4) audit gave:

| (n) | samples | mean (P_3) modules | Monte Carlo SE | (n^2) times mean |
|---:|---:|---:|---:|---:|
|24|12000|0.07167|0.00259|41.28|
|32|10000|0.04310|0.00220|44.13|
|48|8000|0.01925|0.00157|44.35|
|64|6000|0.01317|0.00155|53.93|
|96|3500|0.00629|0.00140|57.93|
|128|2200|0.00318|0.00120|52.13|

The large-(n) rows are rare-event estimates and therefore noisy.

No constant is inferred from this table.

The finite data are used only as a regression against the analytic order

[
n^{-2}.
]

## 9. Residual-failure structure

A separate UPO audit classified failures after removing samples containing a true-twin pair.

At moderate sizes, most of those remaining failures contained a size-three non-stable module.

Every size-three module found in the true-twin-free residual sample induced exactly two internal edges:

[
P_3.
]

No triangle can survive this conditioning because an induced triangle module contains adjacent true twins.

Some residual failures contained no size-three module.

Therefore the (P_3) mechanism is not the entire remaining UPO problem.

It is simply the next identifiable level of the hierarchy.

## 10. Fixed-size module hierarchy suggested by the joint geometry

The same dimensional count extends naturally to a fixed number (k) of events whose external comparability signatures become indistinguishable near one null-joint direction.

In (d=4):

- the (2k) null-depth coordinates contribute
  [
  lambda^{2k};
  ]
- the (k-1) relative two-dimensional angular displacements contribute
  [
  lambda^{2(k-1)}.
  ]

Hence the joint configuration measure has order

[
lambda^{4k-2}.
]

Since

[
arepsilon=lambda^2,
]

the corresponding disagreement tail has the candidate fixed-(k) exponent

[
oxed{
2k-1.
}
]

Multiplying the resulting

[
n^{-(2k-1)}
]

small-disagreement probability by the

[
Theta(n^k)
]

possible (k)-sets gives the hierarchy

[
oxed{
mathbb E[M_{k,n}]
=
O(n^{1-k})
}
]

for fixed-size joint-localized module families satisfying the same nondegeneracy assumptions.

For

[
k=2
]

this gives

[
n^{-1},
]

matching the proved true-twin theorem.

For

[
k=3
]

it gives

[
n^{-2},
]

matching the (P_3) result above.

The general (k) statement is currently a scaling program, not a fully proved theorem for every graph-module type.

## 11. Why this matters for UPO recovery

The finite data previously suggested that higher-dimensional UPO failures increasingly collapse onto minimal local modules.

The first two levels are now separated asymptotically:

[
oxed{
	ext{true-twin pair}
sim
n^{-1}
}
]

in expectation, while

[
oxed{
P_3	ext{ module}
=
Theta(n^{-2}).
}
]

This supports a much sharper route toward the global question

[
p_4^{mathrm{UPO}}(n)stackrel{?}{longrightarrow}1.
]

However, that conclusion still requires control of:

1. all fixed module sizes (kge4);
2. modules whose size grows with (n);
3. non-module mechanisms that can produce multiple implication classes;
4. multiple nontrivial connected components.

The next mathematical obstacle is therefore not the (P_3).

It is to find a uniform bound that remains valid when the obstructing module size is allowed to grow.

## 12. Literature boundary

True and false twin vertices, graph modules, modular decomposition, and UPO theory are classical graph theory.

Recent work also studies false-twin witness counts in abstract graphs.

Those works do not use the geometry-induced Minkowski sprinkling measure and do not address recovery of a causal orientation after arrow erasure.

The project therefore does not claim novelty for twin or module terminology.

The candidate contribution is the Lorentzian asymptotic hierarchy produced by the specific causal-set ensemble and reconstruction contract.

A targeted search did not locate an existing result equivalent to

[
mathbb E[M_{3,n}]
=
Theta(n^{-2})
]

for induced-(P_3) modules in Minkowski-sprinkled comparability graphs.

This remains limited negative evidence only.
