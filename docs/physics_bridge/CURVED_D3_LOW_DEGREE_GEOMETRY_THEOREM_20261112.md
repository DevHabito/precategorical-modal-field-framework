# Theorem: low-degree joint geometry in a regular curved 2+1 causal diamond

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem under regular volume-null joint coordinates  
**Physical status:** curvature-robust low-degree tail and internal sparsity in \(2+1\)  
**Novelty status:** the graphon degree identity is elementary; the volume-null reduction of the curved low-degree tail is project-specific

## 1. Setting

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth \(2+1\)-dimensional Lorentzian spacetime.

Use normalized physical volume

\[
\mathcal V(a,b)
=
\frac{
\operatorname{Vol}_g(I(a,b))
}{
\operatorname{Vol}_g(D)
}.
\]

Assume the null joint

\[
\Sigma
=
\partial I^+(p)
\cap
\partial I^-(q)
\]

admits a regular volume-null chart

\[
(a,b,\sigma),
\]

where

\[
a(x)
=
\mathcal V(p,x)^{2/3},
\]

\[
b(x)
=
\mathcal V(x,q)^{2/3},
\]

and

\[
0<c_J
\le
J(a,b,\sigma)
\le
C_J<\infty
\]

is the normalized spacetime-volume density.

Assume also the regular causal-cap estimate

\[
|\Delta\sigma|
\le
C_{\mathrm{cap}}
\sqrt{AB}
\]

for sufficiently close comparable pairs, with \(A,B\) the two volume-null causal increments.

## 2. Exact graphon degree identity

For any interior event \(x\in D\), the set of events comparable to \(x\) is, up to null boundaries,

\[
A_x
=
I(p,x)
\;\dot\cup\;
I(x,q).
\]

Therefore

\[
\boxed{
Q(x)
=
\mu(A_x)
=
\mathcal V(p,x)
+
\mathcal V(x,q).
}
\]

In volume-null coordinates,

\[
\mathcal V(p,x)=a^{3/2},
\]

and

\[
\mathcal V(x,q)=b^{3/2}.
\]

Hence

\[
\boxed{
Q(x)
=
a^{3/2}
+
b^{3/2}.
}
\]

This identity is exact.

No flatness assumption is used.

## 3. Small degree localizes to the joint

Inside the compact closure of \(D\), the function \(Q\) is positive away from the joint.

Indeed:

- on the future null boundary of \(p\) away from \(\Sigma\),
  \[
  \mathcal V(p,x)=0
  \]
  but
  \[
  \mathcal V(x,q)>0;
  \]
- on the past null boundary of \(q\) away from \(\Sigma\), the reverse holds;
- in the interior both terms are positive.

Therefore, for sufficiently small \(q_0>0\),

\[
\{x:Q(x)\le q_0\}
\]

lies entirely inside the regular joint chart.

## 4. Low-degree tail

Define

\[
g_3(q)
=
\mu\{x:Q(x)\le q\}.
\]

For sufficiently small \(q\),

\[
g_3(q)
=
\int_\Sigma
\int_{
a^{3/2}+b^{3/2}\le q
}
J(a,b,\sigma)
\,da\,db\,d\sigma.
\]

Scale

\[
a=q^{2/3}u,
\qquad
b=q^{2/3}v.
\]

Then

\[
da\,db
=
q^{4/3}
\,du\,dv.
\]

Therefore

\[
q^{-4/3}
g_3(q)
\longrightarrow
A_{3/2}
\int_\Sigma
J(0,0,\sigma)
\,d\sigma,
\]

where

\[
\boxed{
A_{3/2}
=
\int_{
u,v\ge0,\;
u^{3/2}+v^{3/2}\le1
}
du\,dv.
}
\]

The scalar shape constant can be written as

\[
\boxed{
A_{3/2}
=
\frac23
B\left(
\frac23,\frac53
\right).
}
\]

Hence

\[
\boxed{
g_3(q)
\sim
C_\Sigma
q^{4/3},
}
\]

with

\[
\boxed{
C_\Sigma
=
A_{3/2}
\int_\Sigma
J(0,0,\sigma)
\,d\sigma
>0.
}
\]

Thus the exponent

\[
\boxed{
4/3
}
\]

is universal over the regular curved class.

Only the coefficient depends on the joint geometry.

## 5. Low-degree layer size

Let

\[
S_t
=
\{x:Q(x)\le t\}.
\]

The exact degree identity gives

\[
a(x)\le t^{2/3},
\qquad
b(x)\le t^{2/3}
\]

for every

\[
x\in S_t.
\]

Thus the low-degree layer is a volume-null rectangle of transverse scale

\[
t^{2/3}
\]

intersected with the \(3/2\)-ball shape.

## 6. Comparable low-degree points

Fix

\[
x\in S_t.
\]

Consider a future-comparable point

\[
x\prec y
\]

with

\[
y\in S_t.
\]

Write

\[
A=a_y-a_x\ge0,
\]

and

\[
B=b_x-b_y\ge0.
\]

Because both points lie in \(S_t\),

\[
0\le A\le t^{2/3},
\]

and

\[
0\le B\le t^{2/3}.
\]

The regular causal-cap estimate gives

\[
|\sigma_y-\sigma_x|
\le
C
\sqrt{AB}.
\]

## 7. Internal low-degree comparable volume

Using the bounded joint-volume density,

\[
\begin{aligned}
\mu(
I^+(x)
\cap
S_t
)
&\le
C
\int_0^{t^{2/3}}
\int_0^{t^{2/3}}
\sqrt{AB}
\,dA\,dB\\
&=
C
\left(
\int_0^{t^{2/3}}
A^{1/2}\,dA
\right)^2\\
&=
O(t^2).
\end{aligned}
\]

The same bound holds in the past direction.

Therefore

\[
\boxed{
\sup_{x\in S_t}
\mu(
A_x\cap S_t
)
=
O(t^2).
}
\]

This is exactly the low-degree internal-sparsity estimate used in the flat recovery theorem.

## 8. Isolated-vertex scale

For an iid size-\(n\) sample, the expected number of isolated vertices is

\[
\mathbb E[I_n]
=
n
\mathbb E[
(1-Q(X))^{n-1}
].
\]

The tail

\[
g_3(q)
\sim
C_\Sigma q^{4/3}
\]

gives by Laplace-Stieltjes transfer

\[
\boxed{
\mathbb E[I_n]
\sim
C_\Sigma
\Gamma\left(\frac73\right)
n^{-1/3}.
}
\]

In particular,

\[
\boxed{
\Pr(I_n>0)\to0.
}
\]

Thus regular curved \(2+1\) causal graph samples have no isolated vertices asymptotically, just as in flat \(2+1\), although the coefficient changes with joint geometry.

## 9. Component-theorem input

The two estimates

\[
g_3(q)
=
\Theta(q^{4/3})
=
o(q),
\]

and

\[
\sup_{x\in S_t}
\mu(A_x\cap S_t)
=
O(t^2)
\]

are precisely the geometric inputs needed by the degree-escalation proof that sends every non-isolated low-degree vertex to a higher-degree core.

Therefore the flat non-isolated-component argument extends to this regular curved joint class.

No Minkowski symmetry is required in that step.

## 10. Relation to Penrose scaling

The volume-null coordinate regularity theorem derives the chart hypotheses from uniform near-null Penrose-limit scaling along a compact family of noncaustic joint generators.

Thus the present theorem is not an independent ad hoc coordinate assumption.

Its geometric dependency chain is:

\[
\boxed{
\text{regular null generators}
\to
\text{Penrose-limit near-null volume}
\to
\text{volume-null chart}
\to
g_3(q)\sim C_\Sigma q^{4/3}.
}
\]

## 11. Current consequence

The following ingredients of the \(2+1\) orientation-recovery proof are now curvature-robust under the regular-joint hypotheses:

- vanishing isolated-vertex probability;
- degree escalation;
- uniqueness of the nontrivial component;
- low-degree part of the uniform comparable-ball estimate.

The remaining curved ingredients are the bulk small-disagreement coefficient and the transition/bulk pieces of the comparable-ball estimate, treated through the volume-time gradient theorem and the regular joint-suppression theorem.
