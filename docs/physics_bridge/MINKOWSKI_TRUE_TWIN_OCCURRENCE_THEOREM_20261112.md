# Theorem: occurrence probability of comparable true twins for fixed d >= 4

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic rare-event theorem and lower bound on the full UPO convergence rate  
**Physical status:** leading verified local orientation-obstruction probability after arrow erasure  
**Novelty status:** true twins and second-moment inequalities are classical; no equivalent Minkowski-sprinkling asymptotic was located in the targeted review

## 1. Statement

Fix an integer spacetime dimension

\[
d\ge4.
\]

Let \(T_n\) be the number of adjacent true-twin pairs in the arrow-erased comparability graph of an iid size-\(n\) sprinkling into a fixed flat Alexandrov interval of \(\mathbb M^d\).

The true-twin expectation theorem gives

\[
\mathbb E[T_n]
\sim
K_d^{\mathrm{twin}}
n^{-4/d},
\]

with the explicit constant

\[
K_d^{\mathrm{twin}}>0
\]

recorded in

MINKOWSKI_ALLD_TRUE_TWIN_RATE_20261112.md.

Then

\[
\boxed{
\Pr(T_n>0)
\sim
\mathbb E[T_n]
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
}
\]

Consequently, for the full orientation-recovery probability,

\[
\boxed{
1-p_d^{\mathrm{UPO}}(n)
\ge
\left(
K_d^{\mathrm{twin}}+o(1)
\right)
n^{-4/d}.
}
\]

For \(d=4\),

\[
\boxed{
\Pr(T_n>0)
\sim
\frac{9\pi}{n},
}
\]

and hence

\[
\boxed{
1-p_4^{\mathrm{UPO}}(n)
\ge
\frac{9\pi+o(1)}{n}.
}
\]

This note does not prove a matching upper bound for the full UPO failure probability.

## 2. First moment

The exact identity is

\[
\mathbb E[T_n]
=
\binom n2
\int_0^1
(1-\delta)^{n-2}
\,dF_d(\delta),
\]

where

\[
F_d(t)
=
\Pr(
X\sim Y,\,
\Delta_d(X,Y)\le t
).
\]

For \(d\ge4\),

\[
F_d(t)
\sim
C_d^{\mathrm{edge}}
t^{\beta_d},
\]

with

\[
\beta_d
=
2+\frac4d.
\]

Therefore

\[
\mathbb E[T_n]
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
\]

## 3. Second factorial moment

To show that the occurrence probability is asymptotic to the expectation, it is enough to prove

\[
\boxed{
\mathbb E[
T_n(T_n-1)
]
=
o(
\mathbb E[T_n]
).
}
\]

Two distinct true-twin pair indicators are either:

1. overlapping, sharing one sampled vertex;
2. disjoint, using four distinct sampled vertices.

The two cases are treated separately.

## 4. Disjoint twin pairs

Consider two disjoint candidate pairs

\[
\{X_1,X_2\},
\qquad
\{X_3,X_4\}.
\]

Write

\[
\delta_1
=
\Delta_d(X_1,X_2),
\]

\[
\delta_2
=
\Delta_d(X_3,X_4).
\]

If both pairs are sampled true twins, every one of the remaining \(n-4\) sample points must avoid both splitter regions.

Dropping all internal compatibility conditions between the two pairs only enlarges the event.

Since

\[
\mu(
\mathcal D_1\cup\mathcal D_2
)
\ge
\max(\delta_1,\delta_2),
\]

the outside-avoidance probability is bounded by

\[
e^{-c n\max(\delta_1,\delta_2)}
\]

for a fixed \(c>0\).

Before imposing cross-pair constraints, the two continuum pairs are independent.

The distribution function of

\[
\max(\delta_1,\delta_2)
\]

on the event that both pairs are comparable is

\[
F_d(t)^2.
\]

Therefore the disjoint contribution to the factorial second moment is at most

\[
Cn^4
\int_0^1
e^{-cnt}
\,d(F_d(t)^2).
\]

Because

\[
F_d(t)
=
O(t^{\beta_d}),
\]

\[
F_d(t)^2
=
O(t^{2\beta_d}),
\]

and the Laplace-Stieltjes estimate gives

\[
\boxed{
\mathbb E[
T_n(T_n-1)
]_{\mathrm{disjoint}}
=
O(
n^{4-2\beta_d}
)
=
O(
n^{-8/d}
).
}
\]

Since

\[
n^{-8/d}
=
o(
n^{-4/d}
),
\]

disjoint twin-pair coincidences are negligible relative to the first moment.

## 5. Overlapping twin pairs

Now consider two true-twin pair indicators sharing one vertex, for example

\[
\{X_1,X_2\},
\qquad
\{X_1,X_3\}.
\]

If both events occur, then

\[
N[X_1]
=
N[X_2]
=
N[X_3].
\]

Hence the three vertices form a clique of one true-twin equivalence class.

Let

\[
\Delta_3(X_1,X_2,X_3)
\]

be the three-way splitter volume

\[
\mu
\left[
\left(
A_{X_1}\cup A_{X_2}\cup A_{X_3}
\right)
\setminus
\left(
A_{X_1}\cap A_{X_2}\cap A_{X_3}
\right)
\right].
\]

All remaining \(n-3\) points must avoid this region.

## 6. Overlap bound for d > 4

If

\[
\Delta_3\le t,
\]

then every pairwise disagreement is at most \(t\):

\[
\Delta_d(X_i,X_j)\le t.
\]

Fix \(X_1=x\).

Both \(X_2\) and \(X_3\) must lie in

\[
B_t(x)
=
\{
z:z\sim x,\,
\Delta_d(x,z)\le t
\}.
\]

The uniform comparable-ball theorem gives

\[
\sup_x
\mu(B_t(x))
=
O(t^2).
\]

Therefore

\[
\Pr(
X_1,X_2,X_3
\text{ can form an overlapping twin configuration},
\;
\Delta_3\le t
)
=
O(t^4).
\]

It follows that the overlapping contribution satisfies

\[
\boxed{
\mathbb E[
T_n(T_n-1)
]_{\mathrm{overlap}}
=
O(
n^3 n^{-4}
)
=
O(n^{-1})
}
\]

for every fixed

\[
d>4.
\]

Since

\[
\frac4d<1,
\]

\[
n^{-1}
=
o(
n^{-4/d}
).
\]

Thus overlap is negligible in every \(d>4\).

## 7. Sharpened d = 4 comparable-ball estimate

For \(d=4\), the preceding \(O(n^{-1})\) estimate is not enough, because the first moment itself is of order \(n^{-1}\).

A sharper local estimate is available.

Let

\[
q=Q_4(x).
\]

Then, uniformly for sufficiently small \(t\),

\[
\boxed{
\mu(B_t(x))
\le
C
\begin{cases}
t^2, & q\le Ct,\\[4pt]
t^3/q, & q>Ct.
\end{cases}
}
\]

### Joint derivation

Near the null joint, write the null depths of \(x\) as \(a,b\).

The leading pair disagreement is

\[
\frac{
2aA+A^2+
2bB+B^2
}{4}.
\]

The maximal allowed one-side increments satisfy

\[
L_t(a)^2
\le
C
\min\left(
t,
\frac{t^2}{a^2}
\right),
\]

and symmetrically for \(b\).

The conditional causal-pair volume is bounded by

\[
C
L_t(a)^2L_t(b)^2.
\]

Since

\[
q
\asymp
a^2+b^2,
\]

this gives

\[
\mu(B_t(x))
\le
Ct^3/q
\]

when

\[
q>Ct.
\]

For

\[
q\le Ct,
\]

the low-degree internal-sparsity theorem gives \(O(t^2)\).

Compact bulk charts are smaller still.

## 8. d = 4 three-point tail

Let

\[
H_3(t)
=
\Pr(
X_1,X_2,X_3
\text{ are a possible overlapping true-twin clique},
\;
\Delta_3\le t
).
\]

Since both \(X_2,X_3\) must lie in \(B_t(X_1)\),

\[
H_3(t)
\le
\int
\mu(B_t(x))^2
\,d\mu(x).
\]

Split according to graphon degree.

### Low-degree root

For

\[
Q_4(x)\le Ct,
\]

\[
\mu(B_t(x))^2
=
O(t^4).
\]

The degree-tail theorem gives

\[
\mu\{Q_4\le Ct\}
=
O(t).
\]

Thus this region contributes

\[
O(t^5).
\]

### Higher-degree root

For

\[
Q_4(x)>Ct,
\]

\[
\mu(B_t(x))^2
\le
Ct^6 Q_4(x)^{-2}.
\]

Near zero,

\[
g_4(q)
=
O(q).
\]

Stieltjes integration by parts gives

\[
\int_{Ct<Q_4<q_0}
Q_4^{-2}
\,d\mu
=
O(t^{-1}).
\]

The region

\[
Q_4\ge q_0
\]

contributes only \(O(1)\) to the integral.

Therefore

\[
\boxed{
H_3(t)
=
O(t^5).
}
\]

## 9. d = 4 overlap contribution

The outside sample must avoid the three-way splitter region.

Using

\[
H_3(t)=O(t^5),
\]

the overlapping factorial-moment contribution is

\[
\boxed{
O(
n^3 n^{-5}
)
=
O(n^{-2}).
}
\]

This is \(o(n^{-1})\), as required.

## 10. Factorial-moment conclusion

Combining the two cases:

### d = 4

\[
\mathbb E[
T_n(T_n-1)
]
=
O(n^{-2}).
\]

### d > 4

\[
\mathbb E[
T_n(T_n-1)
]
=
O(n^{-1})
+
O(n^{-8/d}).
\]

In every fixed

\[
d\ge4,
\]

\[
\boxed{
\mathbb E[
T_n(T_n-1)
]
=
o(
n^{-4/d}
)
=
o(
\mathbb E[T_n]
).
}
\]

## 11. Occurrence probability

For every nonnegative integer-valued random variable,

\[
\mathbb E[T_n]
-
\mathbb E\binom{T_n}{2}
\le
\Pr(T_n>0)
\le
\mathbb E[T_n].
\]

Since

\[
\mathbb E\binom{T_n}{2}
=
\frac12
\mathbb E[
T_n(T_n-1)
]
=
o(
\mathbb E[T_n]
),
\]

we obtain

\[
\boxed{
\Pr(T_n>0)
\sim
\mathbb E[T_n].
}
\]

Therefore

\[
\boxed{
\Pr(T_n>0)
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
}
\]

## 12. From true twins to UPO failure

An adjacent true-twin pair is a non-stable module whenever its connected component contains at least one additional vertex.

If the graph contains multiple edge-containing components, it is already outside the UPO recovery event.

Thus the only orientation-recoverable graph containing an adjacent true-twin pair is the degenerate case in which the unique nontrivial component is exactly one \(K_2\) and every other vertex is isolated.

That event is exponentially small.

Indeed, choose three fixed positive-volume open regions

\[
U_1,U_2,U_3
\]

with

\[
U_1\ll U_2\ll U_3.
\]

If all three are occupied, the graph contains a connected component with at least three vertices.

The probability that one of the three regions is empty is

\[
e^{-\Theta(n)}.
\]

Hence

\[
\Pr(
T_n>0
\text{ but the graph is orientation-recoverable}
)
=
e^{-\Theta(n)}.
\]

Therefore

\[
1-p_d^{\mathrm{UPO}}(n)
\ge
\Pr(T_n>0)
-
e^{-\Theta(n)}.
\]

Using the true-twin occurrence theorem,

\[
\boxed{
1-p_d^{\mathrm{UPO}}(n)
\ge
\left(
K_d^{\mathrm{twin}}+o(1)
\right)
n^{-4/d}.
}
\]

## 13. What remains open

This theorem gives a sharp lower bound on the convergence rate of the full orientation-recovery probability.

It does not prove

\[
1-p_d^{\mathrm{UPO}}(n)
\sim
K_d^{\mathrm{twin}}
n^{-4/d}.
\]

A matching upper bound requires quantitative control of every other obstruction at a scale smaller than

\[
n^{-4/d}.
\]

The current all-dimensional recovery proof establishes only that those other obstructions have probability \(o(1)\), with some steps based on compactness rather than a sharp rate.

The next quantitative problem is therefore:

\[
\boxed{
\text{Are comparable true twins the asymptotically dominant UPO obstruction?}
}
\]
