# Audit: all-dimensional regular-curved orientation-recovery error law

**Date:** 2026-11-12
**Author:** Felipe Gianini Romero
**Status:** adversarial dimension, normalization, and isolate audit
**Target:** CURVED_ALLD_ORIENTATION_RECOVERY_RATE_THEOREM_20261112.md

## 1. Target law

For a regular curved Lorentzian diamond, the target theorem states

\[
1-p_{d,g}^{\mathrm{UPO}}(n)
\sim
\begin{cases}
K_{3,g}n^{-1}, & d=3,\\[4pt]
K_{d,g}n^{-4/d}, & d\ge4.
\end{cases}
\]

The leading defect is a comparable true-twin pair.

This audit checks the new \(d\ge4\) curved joint coefficient and the parts of the global proof that are sensitive to large dimension.

## 2. Curved joint coefficient

Set

\[
m=d/2,
\qquad
a_m=1+1/m.
\]

In volume-null coordinates, the joint metric is

\[
g
=
2\chi\,da\,db
+
h_\Sigma
+
O(a+b).
\]

The normalized pair measure, after integration over the tangential causal cap, gives the geometric factor

\[
\frac{
2^m\omega_{d-2}
}{
V_D^2
}
\left(
\int_\Sigma
\chi^{m+1}
\,dA_\Sigma
\right)
\]

after both time orientations are included.

The scalar one-side convolution contributes

\[
(a_mL_m)^2
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}.
\]

Hence

\[
C_{d,g}^{\mathrm{edge}}
=
\frac{
2^m\omega_{d-2}
}{
V_D^2
}
\mathcal J_d
(a_mL_m)^2
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
}.
\]

No extra factor of two remains.

## 3. Global metric-scale invariance

Under

\[
g\mapsto c^2g,
\]

normalized causal volumes are unchanged, so \(a,b\) are unchanged.

The double-null coefficient transforms as

\[
\chi\mapsto c^2\chi.
\]

The joint area form transforms as

\[
dA_\Sigma
\mapsto
c^{d-2}
dA_\Sigma.
\]

Therefore

\[
\mathcal J_d
=
\int_\Sigma
\chi^{d/2+1}
\,dA_\Sigma
\]

scales as

\[
c^{d+2+d-2}
=
c^{2d}.
\]

Meanwhile

\[
V_D^2
\mapsto
c^{2d}V_D^2.
\]

Thus

\[
\boxed{
\mathcal J_d/V_D^2
}
\]

is exactly invariant.

The curved leading coefficient is dimensionless, as a probability asymptotic coefficient must be.

## 4. Flat all-dimensional regression

For the unit flat diamond,

\[
V_D
=
\frac{
2S_{d-2}
}{
d(d-1)
},
\]

\[
\chi=2,
\]

and

\[
\operatorname{Area}(\Sigma)
=
S_{d-2}.
\]

Thus

\[
\mathcal J_d
=
2^{d/2+1}
S_{d-2}.
\]

Substitution reduces the curved coefficient to

\[
\frac{
2^{d-1}
d^2(d-1)^2
}{
d-2
}
\frac{
S_{d-3}
}{
S_{d-2}
}
(a_mL_m)^2
\frac{
\Gamma(a_m)^2
}{
\Gamma(2a_m+1)
},
\]

which is exactly the independently derived flat expression.

The repository regression tool

tools/verify_curved_joint_flat_regression.py

checks this numerically.

A session run verified equality for

\[
d=4,\ldots,10
\]

to floating-point error only.

In \(d=4\),

\[
C_{4,\eta}^{\mathrm{edge}}=3\pi.
\]

## 5. True-twin transfer factor

The curved edge exponent is

\[
\beta_d=2+\frac4d
\]

for \(d\ge4\).

Therefore

\[
\mathbb E[T_n]
\sim
\frac12
C_{d,g}^{\mathrm{edge}}
\Gamma(\beta_d+1)
n^{2-\beta_d}.
\]

Since

\[
2-\beta_d=-4/d,
\]

and

\[
\beta_d+1
=
2a_m+1,
\]

the gamma denominator in the edge coefficient cancels.

This gives

\[
K_{d,g}
=
\frac{
2^{m-1}
\omega_{d-2}
}{
V_D^2
}
\mathcal J_d
[
a_mL_m\Gamma(a_m)
]^2.
\]

The factor is consistent with the flat \(9\pi\) control in \(d=4\).

## 6. Isolated vertices for d > 4

The curved low-degree tail is

\[
g_d(q)
\sim
C_{\Sigma,d}q^{4/d}.
\]

Hence

\[
\mathbb E[I_n]
\sim
C_{\Sigma,d}
\Gamma(1+4/d)
n^{1-4/d}.
\]

For \(d>4\), this diverges.

The final curved proof does **not** assume that the isolate count is tight.

The recovery event allows isolated vertices, because they carry no edge orientation.

The proof requires only that there is asymptotically one edge-containing component and that this component is UPO.

## 7. Component ambiguity with many isolates

Outside true twins and residual edge-escalation failure, every edge-containing component reaches a core edge.

Every core edge has a linear number of sampled splitters.

Therefore every edge-containing component has size at least

\[
c_0n.
\]

This statement is unaffected by the presence of \(o(n)\) isolated vertices.

Two edge-containing components would each be linear and hence create a balanced graph module.

The graphon-prime sampling bound excludes that event.

Thus multiple edge-containing components remain subleading even when the number of isolates diverges.

## 8. Modules inside the unique edge-containing component

Let \(C_n\) be the unique edge-containing component and let

\[
M\subset C_n
\]

be a module of \(C_n\).

Every vertex outside \(C_n\) is isolated and therefore anticomplete to \(M\).

Hence

\[
\boxed{
M
\text{ is also a module of the full sampled graph}.
}
\]

This justifies applying the full-graph balanced-module theorem to an internal module witness.

## 9. Near-whole modules and isolates

Suppose a non-stable module has already been forced to linear size and escapes the balanced range.

Then, with a suitable diagonal threshold,

\[
n-|M|=o(n)
\]

in the **full graph**.

This complement includes:

- isolated vertices outside \(C_n\);
- vertices of \(C_n\setminus M\).

Because \(C_n\) is connected and \(M\subsetneq C_n\), there exists

\[
u\in C_n\setminus M
\]

complete to \(M\).

Its sampled co-degree can include all isolates, but that number is still \(o(n)\).

If its continuum co-degree were bounded below by a fixed \(r_0>0\), Chernoff concentration would make such an \(o(n)\) observed co-degree exponentially unlikely.

Therefore the complete external vertex still localizes to the timelike tip regime.

No tight-isolate assumption is used.

## 10. Middle-band points cannot hide among isolates

For a near-tip complete external vertex \(u\), the middle-band theorem gives a nonneighbor region containing continuum points with

\[
q_-\le Q(z)\le q_+.
\]

A sampled middle-band point could in principle lie outside \(C_n\).

But outside the unique edge-containing component every vertex is isolated.

For

\[
Q(z)\ge q_->0,
\]

the probability that \(z\) is isolated is

\[
(1-Q(z))^{n-1}
\le
e^{-q_-(n-1)}.
\]

A union bound over all sampled candidates is still exponentially small.

Thus, outside an exponentially small event, every sampled middle-band point lies in \(C_n\setminus M\) and must obey one of the two module external types.

This closes the isolate loophole.

## 11. Near-whole rate comparison

The tip co-degree tail is

\[
\bar g_d(r)=O(r^d).
\]

Tip-clear candidates therefore have expectation

\[
O(n^{1-d}).
\]

Compare with the leading true-twin scale:

### d = 3

\[
n^{1-d}=n^{-2}=o(n^{-1}).
\]

### d >= 4

\[
n^{1-d}
=
o(n^{-4/d})
\]

because

\[
d-1>\frac4d.
\]

Thus near-whole modules are strictly subleading in every fixed \(d\ge3\).

## 12. Second-moment comparison in high dimension

The true-twin first-moment scale is

\[
n^{2-\beta_d}.
\]

Disjoint twin-pair coincidences contribute

\[
O(n^{4-2\beta_d})
=
O(
[n^{2-\beta_d}]^2
).
\]

Because

\[
\beta_d>2,
\]

this is smaller than the first moment.

Overlapping twin pairs contribute

\[
O(n^{1-\beta_d}),
\]

which is smaller by an explicit factor

\[
n^{-1}.
\]

Thus

\[
\Pr(T_n>0)
\sim
\mathbb E[T_n]
\]

in every fixed \(d\ge3\).

## 13. Failure-class completeness

With \(T_n=0\), every UPO failure lies in one of:

1. residual low-edge escalation;
2. multiple edge-containing components;
3. a balanced internal non-stable module;
4. a near-whole internal non-stable module;
5. exponentially rare core-splitter concentration/empty-graph events.

The classical connected-comparability-graph module criterion ensures that there is no additional internal failure type once a unique edge-containing component has been isolated.

No dimension-dependent failure class was found.

## 14. Principal geometric review risks

The all-dimensional stochastic assembly is robust once the local geometric estimates are granted.

The main external-review targets are now geometric:

1. uniform regularity of the volume-null chart along the full joint;
2. the curved causal-cap coefficient
   \[
   (2\chi AB)^{(d-2)/2};
   \]
3. absorption of the small central interval term;
4. bulk nondegeneracy of the finite-diamond volume-time gradient;
5. uniform tip middle-band shape derivatives before caustics.

## 15. Audit verdict

The all-dimensional regular-curved error law survives the present internal audit.

In particular, the growth of isolated vertices for \(d>4\) does not invalidate either the component or module arguments.

The curved joint coefficient is dimensionally invariant and reproduces the independent flat coefficient exactly.
