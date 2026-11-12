# Theorem: uniform comparable-disagreement balls in a regular curved 2+1 causal diamond

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem under regular-joint and temporal-volume-gradient hypotheses  
**Physical status:** curvature-robust forcing input for \(2+1\) arrow-erasure recovery

## 1. Statement

Let

\[
D=I(p,q)
\]

be a regular \(2+1\)-dimensional curved Alexandrov interval satisfying:

1. the regular volume-null joint hypotheses;
2. the curved joint disagreement lower bound;
3. away from the joint, the volume-difference function
   \[
   \Phi(x)
   =
   \mathcal V(p,x)-\mathcal V(x,q)
   \]
   is \(C^2\) with timelike differential.

Define

\[
B_t(x)
=
\{
z\in D:
z\sim x,\,
\Delta_g(x,z)\le t
\}.
\]

Then

\[
\boxed{
\sup_{x\in D}
\mu(B_t(x))
=
O(t^2)
}
\]

as

\[
t\downarrow0.
\]

## 2. Low-degree regime

The graphon degree satisfies, in every probability graphon,

\[
|Q(x)-Q(z)|
\le
\Delta(x,z).
\]

Therefore, if

\[
Q(x)\le Ct
\]

and

\[
\Delta(x,z)\le t,
\]

then

\[
Q(z)\le(C+1)t.
\]

The curved low-degree geometry theorem gives

\[
\sup_{x:Q(x)\le Ct}
\mu(
A_x
\cap
S_{(C+1)t}
)
=
O(t^2).
\]

Hence

\[
\boxed{
\mu(B_t(x))
=
O(t^2)
}
\]

uniformly in the low-degree joint layer.

## 3. Volume-null joint coordinates

Now assume \(x\) lies in the regular joint chart but

\[
Q(x)>Ct.
\]

Write

\[
x=(a,b,\sigma).
\]

For a future-comparable point \(y\), use increments

\[
A=a_y-a\ge0,
\]

and

\[
B=b-b_y\ge0.
\]

The curved joint-suppression theorem gives, after shrinking the chart if necessary,

\[
\Delta_g(x,y)
\ge
c
\left[
(a+A)^{3/2}-a^{3/2}
+
b^{3/2}-(b-B)^{3/2}
\right].
\]

The tangential causal cap satisfies

\[
|\sigma_y-\sigma|
\le
C\sqrt{AB}.
\]

## 4. One-side increment bounds

Let

\[
L_t^+(a)
\]

be the maximal \(A\ge0\) satisfying

\[
(a+A)^{3/2}-a^{3/2}
\le
Ct.
\]

Then

\[
\boxed{
(L_t^+(a))^{3/2}
\le
C
\begin{cases}
t,
&
a^{3/2}\le Ct,
\\[4pt]
t^{3/2}a^{-3/4},
&
a^{3/2}>Ct.
\end{cases}
}
\]

The proof is elementary.

If \(a^{3/2}\le Ct\), then

\[
A^{3/2}
\le
(a+A)^{3/2}-a^{3/2}
\le
Ct.
\]

If \(a^{3/2}>Ct\), the mean-value theorem gives

\[
(a+A)^{3/2}-a^{3/2}
\ge
c a^{1/2}A,
\]

so

\[
A
\le
Ct a^{-1/2}.
\]

Raising to the \(3/2\) power gives the second line.

## 5. Decreasing-side bound

Let

\[
L_t^-(b)
\]

be the maximal

\[
0\le B\le b
\]

satisfying

\[
b^{3/2}-(b-B)^{3/2}
\le
Ct.
\]

Then the same type of estimate holds:

\[
\boxed{
(L_t^-(b))^{3/2}
\le
C
\begin{cases}
t,
&
b^{3/2}\le Ct,
\\[4pt]
t^{3/2}b^{-3/4},
&
b^{3/2}>Ct.
\end{cases}
}
\]

## 6. Joint comparable-ball volume

For fixed \(x\), the future contribution is bounded by

\[
C
\int_0^{L_t^+(a)}
\int_0^{L_t^-(b)}
\sqrt{AB}
\,dA\,dB.
\]

Thus

\[
\mu(
B_t(x)\cap I^+(x)
)
\le
C
(L_t^+(a))^{3/2}
(L_t^-(b))^{3/2}.
\]

Because

\[
Q(x)
=
a^{3/2}
+
b^{3/2}
>
Ct,
\]

at least one of the two null-depth contributions is larger than a fixed multiple of \(t\).

### One side small, one side large

Suppose

\[
a^{3/2}\le Ct,
\qquad
b^{3/2}>ct.
\]

Then

\[
(L_t^+(a))^{3/2}
\le
Ct,
\]

and

\[
(L_t^-(b))^{3/2}
\le
Ct^{3/2}b^{-3/4}.
\]

Since

\[
b^{3/2}\ge ct,
\]

\[
b^{-3/4}
\le
Ct^{-1/2}.
\]

Hence the product is

\[
O(t^2).
\]

### Both sides large

If

\[
a^{3/2},b^{3/2}>ct,
\]

then

\[
(L_t^+(a))^{3/2}
(L_t^-(b))^{3/2}
\le
Ct^3
(ab)^{-3/4}.
\]

Because

\[
a,b
\ge
ct^{2/3},
\]

\[
(ab)^{-3/4}
\le
Ct^{-1}.
\]

Again the result is

\[
O(t^2).
\]

The past contribution is identical.

Therefore the full joint-transition regime satisfies

\[
\boxed{
\mu(B_t(x))
=
O(t^2).
}
\]

## 7. Bulk regime

Let \(K\Subset D\) be a compact set separated from the joint.

By hypothesis,

\[
d\Phi
\]

is timelike on \(K\).

Set

\[
\kappa(x)
=
\sqrt{
-g^{-1}(d\Phi,d\Phi)
}.
\]

Continuity and compactness give

\[
\kappa(x)\ge\kappa_K>0.
\]

For \(z=\exp_x h\) sufficiently close and timelike,

\[
\Delta_g(x,z)
=
d\Phi_x(h)
+
O(|h|^2).
\]

Thus

\[
\Delta_g(x,z)\le t
\]

confines \(h\) to a future or past timelike cone of linear size

\[
O(t).
\]

In \(2+1\), its spacetime volume is

\[
O(t^3).
\]

Hence

\[
\mu(B_t(x))
=
O(t^3)
\]

uniformly on \(K\).

This is stronger than the required \(O(t^2)\).

## 8. Finite chart cover

A sufficiently small joint chart covers every point where the volume-gradient norm may degenerate as the null joint is approached.

The complement is compact and handled by the bulk argument.

Therefore

\[
\boxed{
\sup_{x\in D}
\mu(B_t(x))
=
O(t^2).
}
\]

## 9. Consequence for implication forcing

The curved small-edge tail has exponent

\[
3.
\]

Fix

\[
\alpha\in(1/2,1).
\]

For an edge of disagreement \(\delta\), the mass of splitters leading only to edges of disagreement at most

\[
\delta^\alpha
\]

is bounded by

\[
O(
\delta^{2\alpha}
)
=
o(\delta).
\]

Thus every low-disagreement edge has a good-splitter region of asymptotic size comparable to its full splitter volume.

The same Laplace-Stieltjes argument as in the flat case yields an expected number of non-escalating low edges of order

\[
O(n^{-1}).
\]

For constant-factor escalation after excluding true twins, the residual rate is

\[
O(n^{-2}).
\]

Hence the local forcing mechanism required for \(2+1\) orientation recovery is stable under the stated curved regularity assumptions.
