# Theorem: primeness of the causal-comparability graphon for regular Lorentzian diamonds

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic continuum theorem  
**Physical status:** curvature-independent exclusion of nontrivial measurable causal modules  
**Novelty status:** weakly homogeneous graphon sets are classical; no equivalent Lorentzian causal-graphon primeness theorem was located in the targeted review

## 1. Statement

Let

\[
(M,g)
\]

be a smooth time-oriented Lorentzian manifold of dimension

\[
d\ge2.
\]

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval with

\[
0<\operatorname{Vol}_g(D)<\infty.
\]

Equip \(D\) with normalized physical volume measure

\[
\mu(E)
=
\frac{\operatorname{Vol}_g(E)}{\operatorname{Vol}_g(D)}.
\]

Define the symmetric causal-comparability kernel

\[
W_D(x,y)
=
\mathbf1_{\{x\ll y\text{ or }y\ll x\}}.
\]

Then \(W_D\) has no nontrivial weakly homogeneous measurable set.

Equivalently,

\[
\boxed{
W_D
\text{ is prime in the graphon homogeneous-set sense.}
}
\]

The theorem does not assume flatness, conformal flatness, constant curvature, or any field equation.

## 2. Weak homogeneity

A measurable set

\[
S\subset D
\]

with positive measure is weakly homogeneous when there exists a measurable function

\[
e:D\setminus S\to\{0,1\}
\]

such that

\[
W_D(z,x)=e(z)
\]

for almost every

\[
(z,x)\in(D\setminus S)\times S.
\]

Thus almost every outside point is timelike-comparable either to almost every point of \(S\) or to almost none of \(S\).

We prove that

\[
\mu(S)>0
\quad\Longrightarrow\quad
\mu(S)=1.
\]

## 3. Splitter consequence

For

\[
x\in D,
\]

write

\[
A_x
=
\{z\in D:z\sim x\}.
\]

If \(S\) is weakly homogeneous, Fubini's theorem gives a conull subset

\[
G\subseteq S
\]

such that for every \(x\in G\), for almost every \(y\in G\),

\[
\boxed{
\mu\!\left(
(A_x\triangle A_y)\setminus S
\right)
=
0.
}
\]

Indeed, an outside point in the symmetric difference would distinguish \(x\) and \(y\).

The set

\[
A_x\triangle A_y
\]

is the continuum splitter region of the pair.

## 4. Positive-measure sets contain timelike pairs

Let

\[
\mu(S)>0.
\]

Choose an interior Lebesgue-density point

\[
x\in S.
\]

Every sufficiently small convex normal neighborhood of \(x\) contains an open future-timelike cone sector of positive spacetime volume.

Because \(x\) is a density point of \(S\), this sector intersects \(S\) in positive measure.

After intersecting with the conull Fubini-good set \(G\), we can choose

\[
x_0,y_0\in G,
\qquad
x_0\ll y_0.
\]

Thus \(S\) contains a Fubini-good continuum edge.

## 5. Local spacelike-chain lemma

Let

\[
U\subset M
\]

be open and path connected.

Any two points of \(U\) can be joined by a finite chain

\[
z_0,z_1,\ldots,z_k
\]

lying in \(U\) such that every consecutive pair is spacelike separated.

### Local step

Inside a sufficiently small convex normal neighborhood, identify the leading geometry with a Lorentzian vector space.

Given two sufficiently close points \(a,b\), choose a small transverse spatial displacement \(v\) so that

\[
c=a+v
\]

satisfies

\[
a\not\sim c,
\qquad
c\not\sim b.
\]

The displacement can be chosen arbitrarily small, so all three points remain inside the prescribed open set.

### Global chain

Cover a continuous path in \(U\) by finitely many such normal neighborhoods and replace each sufficiently short path segment by at most two spacelike steps.

Hence \(U\) is spacelike-chain connected.

The argument requires at least one spatial dimension, i.e. \(d\ge2\).

## 6. Chronological slabs are path connected

Fix

\[
x\in D.
\]

The open set

\[
U_x^+
=
I^+(x)\cap D
=
I^+(x)\cap I^-(q)
\]

is path connected.

Indeed, every point

\[
y\in U_x^+
\]

lies on a future-directed timelike curve from \(y\) to \(q\).

Every point of that curve before \(q\) remains in

\[
I^+(x)\cap I^-(q).
\]

Two such curves from different starting points enter a common sufficiently small neighborhood of \(q\), where they can be connected while staying inside the same open chronological slab.

Thus all points of \(U_x^+\) lie in one path component.

Time reversal gives the same result for

\[
U_x^-
=
I^-(x)\cap D.
\]

By the previous section, both sets are spacelike-chain connected.

## 7. Continuum forcing connectivity

Two timelike edges

\[
xy,
\qquad
xz
\]

directly force one another when

\[
y
\]

and

\[
z
\]

are spacelike separated.

They then form an induced continuum \(P_3\) with common endpoint \(x\).

Take arbitrary interior timelike edges

\[
(x,y),
\qquad
(x',y').
\]

Choose

\[
z\in
I^+(x)
\cap
I^+(x')
\cap
D.
\]

Such a point exists because \(q\in I^+(x)\cap I^+(x')\) and the chronological futures are open; choose \(z\) sufficiently near \(q\) but still inside \(D\).

Now:

1. connect \(y\) to \(z\) by a spacelike chain inside \(I^+(x)\cap D\);
2. connect \(x\) to \(x'\) by a spacelike chain inside \(I^-(z)\cap D\);
3. connect \(z\) to \(y'\) by a spacelike chain inside \(I^+(x')\cap D\).

Each spacelike step produces a direct forcing move between timelike edges sharing the fixed endpoint.

Therefore

\[
\boxed{
\text{the interior timelike-edge forcing graph is connected.}
}
\]

No flat-space symmetry is used.

## 8. Robustness of a finite forcing path

Every direct forcing step uses strict inequalities:

- one pair is timelike;
- the opposite pair is spacelike.

Both relations are open.

Therefore every finite forcing path admits open neighborhoods of its auxiliary vertices in which the same forcing pattern persists.

This robustness is essential for the measure argument.

## 9. Propagation inside a weakly homogeneous set

Start with the Fubini-good edge

\[
x_0y_0
\subset S.
\]

Consider one robust direct forcing step from a current good edge

\[
ab
\subset S
\]

to a new edge through a splitter vertex \(c\).

The robust splitter condition gives an open positive-volume neighborhood

\[
U_c
\subset
A_a\triangle A_b.
\]

By the splitter consequence,

\[
\mu(U_c\setminus S)=0.
\]

Because the Fubini-good set \(G\subseteq S\) is conull in \(S\),

\[
U_c\cap G
\]

has positive measure.

Choose the next auxiliary vertex in this intersection.

The new edge therefore again has endpoints in \(G\), and the argument can continue.

Since the forcing path is finite, repeated intersection with full-measure sets causes no difficulty.

Thus any fixed robust continuum forcing path starting from \(x_0y_0\) can be realized with all intermediate vertices in \(S\), up to null sets.

## 10. Contradiction with a complement density point

Assume

\[
0<\mu(S)<1.
\]

Choose an interior density point

\[
w\in D\setminus S.
\]

Choose any interior event \(v\) timelike-related to \(w\).

By continuum forcing connectivity, there is a finite robust forcing path from the initial edge

\[
x_0y_0
\]

to the edge

\[
vw.
\]

Stop one step before the endpoint.

The preceding edge has both endpoints in \(S\), and the last forcing relation is robust in an open neighborhood

\[
U\ni w.
\]

Every point of \(U\) is a splitter of that preceding \(S\)-edge.

Weak homogeneity therefore implies

\[
\mu(U\setminus S)=0.
\]

But \(w\) is a density point of \(D\setminus S\), so every sufficiently small neighborhood of \(w\) has positive complement measure.

Contradiction.

Hence

\[
\boxed{
\mu(S)=1.
}
\]

The null case is trivial.

Therefore \(W_D\) is prime.

## 11. Measure-class robustness

The same proof works for any Borel probability measure \(\nu\) on \(D\) that:

1. has full support;
2. is mutually absolutely continuous with spacetime volume.

In particular, any smooth positive density

\[
d\nu=w\,d\mu
\]

has the same weakly homogeneous null sets.

Thus primeness is invariant under the equivalent-measure changes used in the conformal-weight theorem.

## 12. Consequence for finite sampling

Primeness alone does not prove finite-sample UPO.

It does imply, through standard coloured-graphon compactness and sampling convergence, that for every fixed

\[
\varepsilon>0,
\]

modules with

\[
\varepsilon n
\le
|M|
\le
(1-\varepsilon)n
\]

disappear asymptotically in iid samples from the causal graphon.

The quantitative rate then follows from cut-distance sampling exactly as in the flat case.

Thus the balanced-module part of the recovery proof is curvature independent.

## 13. Literature boundary

Weakly homogeneous graphon sets are established graphon theory, including the treatment by Hatami and Norin.

The Lorentzian ingredients used here are elementary causal properties of smooth spacetimes:

- openness of chronological relations;
- convex normal neighborhoods;
- local spacelike directions;
- existence of common chronological futures inside an Alexandrov interval.

A targeted search did not locate a prior theorem identifying causal-comparability graphons of Lorentzian diamonds as prime.

This is limited negative evidence only.

## 14. Remaining curved difficulty

The result removes one entire part of the generic-curvature problem.

Generic curvature does **not** threaten:

- graphon primeness;
- balanced-module exclusion.

The remaining genuinely geometric difficulties are local rare-event estimates:

- the small-disagreement tail;
- the uniform comparable-ball bound;
- low-degree and co-degree boundary tails;
- near-whole-module suppression.

Those are the places where curvature can change the recovery rate.
