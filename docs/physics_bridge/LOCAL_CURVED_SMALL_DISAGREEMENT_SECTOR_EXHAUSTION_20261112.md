# Theorem: global exhaustion of small-disagreement sectors in a local convex Lorentzian diamond

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic sector-classification theorem  
**Purpose:** remove the possibility of an unaccounted boundary sector changing the curved small-disagreement exponent

## 1. Setting

Let

\[
D=I(p,q)
\]

be a sufficiently small Alexandrov interval whose closure lies inside a causally convex convex-normal neighborhood of a smooth time-oriented Lorentzian spacetime.

Assume

\[
d\ge3.
\]

For ordered causally comparable points

\[
x\le y
\]

in the closure, define the normalized disagreement by the exact continuous extension

\[
\boxed{
\Delta(x,y)
=
\frac{
V(p,y)-V(p,x)
+
V(x,q)-V(y,q)
-
2V(x,y)
}{
V(p,q)
}.
}
\]

For interior iid samples, null pairs have probability zero; the closure is used only to classify possible small-\(\Delta\) limits.

## 2. Continuity

Inside the convex-normal neighborhood, Alexandrov interval volumes depend continuously on their endpoints.

Therefore

\[
\boxed{
(x,y)\mapsto\Delta(x,y)
}
\]

is continuous on the compact ordered causal-pair space

\[
\mathcal C
=
\{
(x,y)\in\overline D^2:
x\le y
\}.
\]

## 3. Zero-disagreement ordered pairs

The only ordered-pair zero sets relevant to the compactification are:

1. the diagonal
   \[
   x=y;
   \]
2. the opposite-tip pair
   \[
   (p,q).
   \]

### Interior distinct pairs

Let

\[
x<y
\]

be distinct and not equal to \((p,q)\).

If

\[
x\ll y,
\]

choose a sufficiently small normal neighborhood of \(x\).

Because

\[
I^-(y)
\]

is open and contains \(x\), there is an open set of points \(z\) near \(x\) that remain in \(I^-(y)\) but are spacelike to \(x\).

Thus

\[
z\sim y,
\qquad
z\not\sim x
\]

on a positive-volume open set.

Hence

\[
\Delta(x,y)>0.
\]

### Null-related boundary pairs

If \(x<y\) are null related and do not form the opposite tips, the regular null hypersurface separating \(I^-(y)\) from its spacelike exterior has nonzero transverse gradient.

A small wedge on the timelike side of the cone of \(y\) and the spacelike side of the cone of \(x\) gives a positive-volume splitter region.

Hence again

\[
\Delta(x,y)>0.
\]

### One endpoint equal to a tip

The past tip \(p\) is comparable to every point of \(D\), so

\[
A_p=D
\]

up to null sets.

If

\[
y\ne q,
\]

then \(y\) has a positive-volume spacelike region in \(D\).

Thus

\[
\Delta(p,y)>0.
\]

The time-dual statement holds for

\[
(x,q)
\]

unless

\[
x=p.
\]

### Opposite tips

Both tips are comparable to every interior event:

\[
A_p=A_q=D
\]

up to measure zero.

Therefore

\[
\boxed{
\Delta(p,q)=0.
}
\]

Hence the zero set on ordered comparable pairs is

\[
\boxed{
Z_\Delta
=
\{
(x,x):x\in\overline D
\}
\cup
\{(p,q)\}.
}
\]

## 4. Compact separation away from the zero set

Let \(U_{\rm diag}\) be a neighborhood of the diagonal and \(U_{\rm tips}\) a neighborhood of \((p,q)\).

On the compact set

\[
\mathcal C
\setminus
(
U_{\rm diag}
\cup
U_{\rm tips}
),
\]

\(\Delta\) is continuous and strictly positive.

Therefore there exists

\[
c>0
\]

such that

\[
\boxed{
\Delta(x,y)\ge c
}
\]

on that set.

Consequently every sequence of ordered comparable pairs with

\[
\Delta\to0
\]

must enter either:

1. the diagonal sector;
2. the opposite-tip sector.

The diagonal sector itself splits into regular bulk/face/tip charts and the codimension-two null-joint chart.

## 5. Diagonal away from the null joint

On a compact diagonal chart separated from the null edge, the finite-diamond volume function

\[
\Phi
=
\frac{
V(p,\cdot)-V(\cdot,q)
}{
V_D
}
\]

has a nonzero temporal first variation.

For

\[
y=\exp_x h
\]

with \(h\) small future timelike,

\[
\Delta(x,y)
=
d\Phi_x(h)+o(|h|).
\]

Therefore

\[
\Delta(x,y)
\asymp
|h|
\]

uniformly on compact subcharts.

The conditional comparable-pair volume with

\[
\Delta\le\varepsilon
\]

is

\[
O(\varepsilon^d).
\]

This includes:

- ordinary interior bulk points;
- a single regular null face away from the edge;
- neighborhoods approaching one tip while the pair itself remains diagonal/local.

Thus

\[
\boxed{
F^{\rm local,\ away\ edge}(\varepsilon)
=
O(\varepsilon^d).
}
\]

For \(d=3\), this is the leading bulk scale.

For \(d\ge4\), it is subleading to the null-joint scale.

## 6. Diagonal near the null joint

Near the codimension-two edge, both endpoint-volume derivatives degenerate together.

The Penrose-Fermi thin-null law and the double-null cap geometry give:

### d = 3

The nonlinear core is

\[
O(\varepsilon^{10/3}),
\]

while its transition matches the integrable bulk coefficient.

### d >= 4

The edge is leading:

\[
\boxed{
F^{\rm joint}_{d,g}(\varepsilon)
\sim
C_{d,g}^{\rm joint}
\varepsilon^{2+4/d}.
}
\]

This is the only diagonal sector with exponent smaller than \(d\).

## 7. Opposite-tip sector

Now let

\[
x=\exp_p h,
\]

and

\[
y=\exp_q(-k),
\]

with \(h,k\) future/past inward timelike displacements.

The one-sided volume first variations at the two tips define positive temporal covectors

\[
\Lambda_p,
\qquad
\Lambda_q.
\]

The interval-volume expansions are:

\[
V(p,x)
=
O(|h|^d),
\]

\[
V(y,q)
=
O(|k|^d),
\]

\[
V(x,q)
=
V_D
-
V_D\Lambda_p(h)
+
o(|h|),
\]

\[
V(p,y)
=
V_D
-
V_D\Lambda_q(k)
+
o(|k|),
\]

and moving both endpoints inward gives

\[
V(x,y)
=
V_D
-
V_D\Lambda_p(h)
-
V_D\Lambda_q(k)
+
o(|h|+|k|).
\]

Substitution into the exact disagreement identity yields

\[
\boxed{
\Delta(x,y)
=
\Lambda_p(h)
+
\Lambda_q(k)
+
o(|h|+|k|).
}
\]

Because the two covectors are temporal,

\[
\Delta(x,y)
\asymp
|h|+|k|.
\]

## 8. Opposite-tip pair volume

The physical volume of a \(d\)-dimensional timelike cone cut by

\[
\Lambda_p(h)\le\varepsilon
\]

is

\[
O(\varepsilon^d).
\]

The same holds independently at the future tip.

Therefore the pair volume satisfying

\[
\Delta(x,y)\le\varepsilon
\]

in the opposite-tip sector is

\[
\boxed{
O(\varepsilon^{2d}).
}
\]

This is always subleading:

### d = 3

\[
2d=6>3.
\]

### d >= 4

\[
2d
>
2+\frac4d.
\]

Thus the nonlocal zero

\[
\Delta(p,q)=0
\]

does not compete with the leading reconstruction-error mechanism.

## 9. Exhaustion theorem

Combining compact separation and the local analyses:

\[
\boxed{
\text{every ordered comparable pair with }\Delta\to0
}
\]

belongs asymptotically to exactly one of:

1. a local diagonal bulk/face/tip sector;
2. the local codimension-two null-joint sector;
3. the opposite-tip sector.

Their pair-volume scales are:

\[
\boxed{
\begin{array}{c|c}
\text{sector}
&
\text{small-disagreement scale}
\\ \hline
\text{local bulk/regular face}
&
O(\varepsilon^d)
\\
\text{joint, }d=3
&
O(\varepsilon^{10/3})
\text{ core, matched to }\varepsilon^3
\\
\text{joint, }d\ge4
&
\Theta(\varepsilon^{2+4/d})
\\
\text{opposite tips}
&
O(\varepsilon^{2d})
\end{array}
}
\]

No fourth sector remains.

## 10. Consequence

For a sufficiently small convex regular diamond:

### d = 3

\[
\boxed{
F_{3,g}(\varepsilon)
\sim
C_{3,g}\varepsilon^3.
}
\]

### d >= 4

\[
\boxed{
F_{d,g}(\varepsilon)
\sim
C_{d,g}^{\rm joint}
\varepsilon^{2+4/d}.
}
\]

The caveat

> "provided no additional singular boundary sector exists"

can therefore be removed from the local small-diamond theorem.

## 11. Interpretation

There are two geometrically different ways for symmetric causal neighborhoods to become identical in the compactified diamond:

- two points coalesce;
- the two universal tips are approached simultaneously.

The first contains the null-joint degeneracy responsible for the leading higher-dimensional error.

The second is too small in sampling measure to compete.

This sector classification is a global compactness check on the local asymptotic calculations.
