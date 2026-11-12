# Theorem: Penrose-scaled Alexandrov-domain convergence in a regular null tube

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic convergence theorem  
**Physical status:** closes the scaled-domain step in the thin-null Alexandrov-volume asymptotic  
**Literature basis:** Penrose-Fermi metric convergence is established by Blau, Frank, and Weiss; the causal-stability ingredients are standard Lorentzian limit-curve theory

## 1. Setting

Let

\[
\gamma:[0,L]\to(M,g)
\]

be a compact null geodesic segment contained in a regular null-Fermi tube, with no conjugate or cut points on the segment relevant to the construction.

Let \(a>0\) parametrize a family of timelike endpoints approaching the null-related endpoint at \(a=0\).

Use the Penrose-Fermi anisotropic blow-up

\[
u=aU,
\qquad
y^A=\sqrt a\,Y^A,
\qquad
v=V.
\]

Let \(g_a\) denote the corresponding rescaled metric in the \((U,V,Y)\) coordinates, including the usual overall conformal normalization that keeps the causal cones finite.

The Penrose-Fermi expansion gives

\[
\boxed{
g_a
\longrightarrow
g_0=g_{\rm PW}
}
\]

in \(C^\infty\) on every compact subset of the regular tube.

Let the rescaled endpoints be

\[
P_a,\ Q_a,
\]

and assume

\[
P_a\to P_0,
\qquad
Q_a\to Q_0,
\]

with

\[
P_0\ll_{g_0}Q_0.
\]

Assume also that all rescaled Alexandrov intervals considered below are contained in one fixed compact set \(K\) inside the regular coordinate tube.

## 2. Claim

Let

\[
I_a
=
I_{g_a}(P_a,Q_a),
\]

and

\[
I_0
=
I_{g_0}(P_0,Q_0).
\]

Then

\[
\boxed{
\mathbf 1_{I_a}(z)
\longrightarrow
\mathbf 1_{I_0}(z)
}
\]

for almost every \(z\in K\).

Consequently, if the rescaled volume densities satisfy

\[
J_a\to J_0
\]

uniformly on \(K\), then

\[
\boxed{
\int_{I_a}J_a\,dz
\longrightarrow
\int_{I_0}J_0\,dz.
}
\]

This is the scaled-domain convergence required by the thin-null volume theorem.

## 3. Interior stability

Take

\[
z\in I_0.
\]

Then

\[
P_0\ll_{g_0}z
\ll_{g_0}Q_0.
\]

Choose smooth timelike curves

\[
\alpha:P_0\to z,
\qquad
\beta:z\to Q_0
\]

whose tangent vectors remain strictly inside the \(g_0\)-timelike cone.

Because their images are compact, there is a uniform cone margin.

The convergence

\[
g_a\to g_0
\]

in \(C^0\) on compact sets implies that the same tangent vectors remain timelike for \(g_a\) for all sufficiently small \(a\).

The endpoint convergence

\[
P_a\to P_0,
\qquad
Q_a\to Q_0
\]

allows the short initial and final pieces to be adjusted inside convex normal neighborhoods.

Therefore

\[
P_a\ll_{g_a}z
\ll_{g_a}Q_a
\]

for sufficiently small \(a\).

Hence

\[
\boxed{
z\in I_0
\quad\Longrightarrow\quad
z\in I_a
\text{ eventually.}
}
\]

## 4. Exclusion away from the limiting causal diamond

Now take

\[
z\notin
J_{g_0}^+(P_0)
\cap
J_{g_0}^-(Q_0).
\]

Suppose for contradiction that there is a sequence

\[
a_k\downarrow0
\]

such that

\[
z\in I_{a_k}.
\]

Then there are \(g_{a_k}\)-timelike curves

\[
P_{a_k}\to z
\]

and

\[
z\to Q_{a_k}
\]

contained in the fixed compact set \(K\).

Because

\[
g_{a_k}\to g_0
\]

uniformly on \(K\), choose a standard cone sandwich: for every sufficiently small fixed \(\epsilon>0\),

\[
g_0^{-\epsilon}
\prec
g_{a_k}
\prec
g_0^{+\epsilon}
\]

for all large \(k\), where \(g_0^{+\epsilon}\) is a small widening of the \(g_0\)-cones.

The compactness/limit-curve theorem applied to the widened metrics gives, after passing to a subsequence, continuous \(g_0\)-causal limit curves

\[
P_0\to z
\]

and

\[
z\to Q_0.
\]

Thus

\[
z\in
J_{g_0}^+(P_0)
\cap
J_{g_0}^-(Q_0),
\]

contradiction.

Therefore

\[
\boxed{
z\notin
J_{g_0}^+(P_0)\cap J_{g_0}^-(Q_0)
\quad\Longrightarrow\quad
z\notin I_a
\text{ eventually.}
}
\]

## 5. The only undecided set is the null boundary

Sections 3 and 4 show pointwise convergence except possibly on

\[
\partial I_0
\subseteq
\left[
J_{g_0}^+(P_0)\cap J_{g_0}^-(Q_0)
\right]
\setminus I_0.
\]

Under the regular-tube hypothesis, this boundary is a finite union of smooth null hypersurface pieces up to lower-dimensional intersections.

Therefore

\[
\boxed{
\operatorname{Leb}(\partial I_0)=0.
}
\]

Hence

\[
\mathbf1_{I_a}
\to
\mathbf1_{I_0}
\]

almost everywhere on \(K\).

## 6. Volume convergence

The rescaled metric determinants satisfy

\[
J_a(z)
=
\sqrt{|\det g_a(z)|}
\longrightarrow
J_0(z)
\]

uniformly on \(K\).

The functions

\[
\mathbf1_{I_a}J_a
\]

are uniformly bounded by an integrable constant on the fixed compact set \(K\).

Dominated convergence therefore yields

\[
\boxed{
\operatorname{Vol}_{g_a}(I_a)
\longrightarrow
\operatorname{Vol}_{g_0}(I_0).
}
\]

## 7. Thin-null consequence

Undoing the anisotropic coordinate Jacobian,

\[
du\,dv\,d^{d-2}y
=
a^{d/2}
dU\,dV\,d^{d-2}Y.
\]

Therefore

\[
\operatorname{Vol}_g(I(p,x_a))
=
a^{d/2}
\left[
\operatorname{Vol}_{g_{\rm PW}}(I_0)
+
o(1)
\right].
\]

Thus

\[
\boxed{
\operatorname{Vol}_g(I(p,x_a))
=
\mathcal C_\gamma
a^{d/2}
[1+o(1)],
}
\]

with

\[
\mathcal C_\gamma
=
\operatorname{Vol}_{g_{\rm PW}}(I_0)
\in(0,\infty).
\]

The positivity follows from

\[
P_0\ll_{g_0}Q_0.
\]

The finiteness follows from compact containment.

This closes the scaled-domain convergence obligation in the thin-null theorem.

## 8. Literature boundary

Blau, Frank, and Weiss prove that the Penrose limit is the leading term of a covariant null-Fermi expansion and give the higher-order metric corrections around a null geodesic.

Lorentzian limit-curve theory establishes stability of causal limits under convergent cone structures; modern reviews by Minguzzi collect these results.

The project-specific step is using those facts to obtain almost-everywhere convergence of the rescaled Alexandrov-domain indicators and hence the thin-null volume coefficient.

## 9. Remaining assumptions

The theorem does not remove the regular-tube hypotheses.

It can fail to apply if:

- the scaled intervals escape every compact coordinate tube;
- a conjugate point or cut point enters the limiting domain;
- the limiting endpoints become null rather than timelike related;
- the null boundary ceases to be a regular measure-zero hypersurface.

Within the regular null-tube class used by the curved \(2+1\) theorem, the domain-convergence gap is closed.
