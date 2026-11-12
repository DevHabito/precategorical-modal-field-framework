# Theorem: regular curved 2+1 timelike-tip co-degree and middle-band control

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem under explicit regular-tip hypotheses  
**Physical status:** curved analogue of the tip geometry used to suppress near-whole modules  
**Novelty status:** volume first variation and null-cone geometry are classical; the project-specific statement is the co-degree/middle-band estimate for causal-comparability recovery

## 1. Setting

Let

\[
D=I(p,q)
\]

be a compact causally convex Alexandrov interval in a smooth \(2+1\)-dimensional Lorentzian spacetime.

Let

\[
Q(x)
=
\mu(A_x)
\]

be the causal-comparability graphon degree and

\[
R(x)
=
1-Q(x)
\]

the continuum co-degree.

We analyze \(x\to p\). The future-tip statement at \(q\) follows by time reversal.

## 2. Regular-tip hypotheses

Assume:

### T1. Temporal future-volume derivative

The function

\[
F(x)
=
\frac{
\operatorname{Vol}(I(x,q))
}{
V_D
}
\]

extends \(C^2\) from the interior to a future neighborhood of \(p\), with

\[
F(p)=1,
\]

and

\[
-dF_p
\]

a future-positive timelike covector.

Define

\[
\Lambda_p
=
-dF_p.
\]

### T2. Regular null cone from p

There is a compact affine interval of the future null cone of \(p\),

\[
\mathcal N_{\mathrm{mid}},
\]

free of conjugate points and cut points, with smooth null exponential parametrization by affine parameter and null direction.

### T3. Intermediate degree band

On a small tubular neighborhood of \(\mathcal N_{\mathrm{mid}}\),

\[
\boxed{
0<q_-<Q(z)<q_+<1.
}
\]

### T4. Uniform null-boundary first variation

For every sufficiently small future-timelike displacement

\[
x=\exp_p(h),
\]

the part of the shifted future boundary of \(x\) intersecting the chosen middle null tube sweeps a spacetime volume comparable to

\[
\Lambda_p(h).
\]

More precisely, there is a measurable nonneighbor band

\[
B_x^{\mathrm{mid}}
\]

inside that tube with

\[
\mu(B_x^{\mathrm{mid}})
\ge
c_0\Lambda_p(h)
\]

for a fixed \(c_0>0\).

Section 6 explains why T4 is the curved analogue of the opposite-hemisphere construction and follows from regular null-flow first variation.

## 3. Co-degree first variation

For

\[
x=\exp_p(h),
\]

the exact degree is

\[
Q(x)
=
\mathcal V(p,x)
+
\mathcal V(x,q).
\]

In \(2+1\),

\[
\mathcal V(p,x)
=
O(|h|^3).
\]

Taylor expansion of \(F(x)=\mathcal V(x,q)\) gives

\[
F(x)
=
1
-
\Lambda_p(h)
+
O(|h|^2).
\]

Therefore

\[
\boxed{
R(x)
=
\Lambda_p(h)
+
O(|h|^2).
}
\]

Because \(\Lambda_p\) is timelike and future positive, it is uniformly comparable to any auxiliary Euclidean norm on the future causal cone near the origin:

\[
c|h|
\le
\Lambda_p(h)
\le
C|h|.
\]

Thus

\[
\boxed{
R(x)\asymp |h|.
}
\]

## 4. Co-degree tail

Define

\[
\bar g_3(r)
=
\mu\{x:R(x)\le r\}.
\]

For sufficiently small \(r\), the relevant points lie in a normal neighborhood of \(p\).

The condition

\[
R(x)\le r
\]

is equivalent up to constants to

\[
\Lambda_p(h)\le Cr
\]

inside the future timelike cone.

A timelike linear functional cuts a \(2+1\)-dimensional cone with volume proportional to the cube of the cutoff.

Hence

\[
\boxed{
\bar g_3(r)
=
\Theta(r^3).
}
\]

The leading coefficient can be written in terms of the Lorentz norm of \(\Lambda_p\) and the normalized volume density at \(p\), but the exponent is sufficient for the recovery proof.

## 5. Geometry of the middle null band

Parametrize regular null generators from \(p\) by a direction variable \(\theta\) and affine parameter \(\lambda\).

Let

\[
k(\theta)
\]

be the future null tangent at \(p\).

For a future causal displacement \(h\), the first displacement of the null boundary along the generator is controlled by the null support function

\[
-\,
g_p(h,k(\theta)).
\]

For every future timelike or null \(h\ne0\), this quantity is nonnegative and is strictly positive away from the generator parallel to \(h\).

Normalize \(h\) by

\[
\Lambda_p(h)=1.
\]

The normalized future causal directions form a compact section after quotienting the scale.

For each such \(h\), there is a positive-measure set of null directions on which

\[
-g_p(h,k(\theta))
\ge c_1>0.
\]

By compactness, a finite collection of angular patches gives a uniform lower bound on the measure of such directions.

This is the curved replacement for the opposite hemisphere in Minkowski space.

## 6. First-variation volume in the middle affine band

Restrict those null directions to a fixed affine interval

\[
\lambda\in[\lambda_0,\lambda_1]
\]

inside the regular cone, chosen so that T3 holds.

Because the null exponential map is nonsingular there, its transverse Jacobi factor is smooth and bounded above and below.

Shifting the cone vertex from \(p\) to

\[
x=\exp_p(h)
\]

moves the null boundary through a thickness

\[
\Theta(
-g_p(h,k(\theta))
).
\]

Integrating over:

- the fixed affine interval;
- the positive-measure angular patch;
- the boundary displacement thickness;

gives

\[
\mu(B_x^{\mathrm{mid}})
\ge
c_2|h|.
\]

Using

\[
R(x)\asymp
\Lambda_p(h)
\asymp
|h|,
\]

we obtain

\[
\boxed{
\mu(B_x^{\mathrm{mid}})
\ge
c_0R(x).
}
\]

Thus T4 follows from the regular null-flow geometry.

## 7. Intermediate degree of band points

The middle affine band is compact and separated from:

- the tip \(p\);
- the opposite tip \(q\);
- the codimension-two edge.

The degree function \(Q\) is continuous there.

By choosing the affine band inside a region where \(Q\) is neither near zero nor near one, compactness gives

\[
\boxed{
q_-
\le
Q(z)
\le
q_+
}
\]

for every \(z\) in the band, with

\[
0<q_-<q_+<1.
\]

This justifies T3 whenever such an intermediate cross-section exists on every generator.

## 8. Tip middle-band theorem

Combining the preceding sections:

for every sufficiently near-tip point \(x\),

\[
\boxed{
\mu(B_x^{\mathrm{mid}})
\ge
c_0R(x),
}
\]

and

\[
\boxed{
q_-
\le
Q(z)
\le
q_+
\qquad
(z\in B_x^{\mathrm{mid}}).
}
\]

Together with

\[
\boxed{
\bar g_3(r)
=
\Theta(r^3),
}
\]

this is the curved \(2+1\) analogue of the flat timelike-tip theorem.

## 9. Near-whole-module consequence

Suppose a sampled vertex \(u\) is complete to a module containing

\[
n-o(n)
\]

vertices.

Then \(u\) must have small sampled co-degree and therefore small continuum co-degree except on an exponentially small large-deviation event.

If a sampled point falls in

\[
B_u^{\mathrm{mid}},
\]

its continuum degree lies in

\[
[q_-,q_+].
\]

Such a point cannot be complete or anticomplete to an \(n-o(n)\) module except with probability

\[
e^{-\Theta(n)}.
\]

Therefore the middle band must be empty of sampled points.

Conditioned on \(u\),

\[
\Pr(
B_u^{\mathrm{mid}}
\text{ empty}
)
\le
e^{-cnR(u)}.
\]

Integrating against

\[
\bar g_3(r)=O(r^3)
\]

gives

\[
n
\int
e^{-cnr}
\,d\bar g_3(r)
=
O(n^{-2}).
\]

Hence

\[
\boxed{
\Pr(
\text{near-whole module}
)
=
O(n^{-2})
+
e^{-\Theta(n)}.
}
\]

This is subleading to the curved true-twin scale \(n^{-1}\).

## 10. What remains

Under the regular-tip and regular-joint hypotheses, the local geometric inputs for the \(2+1\) recovery proof are now all available:

- small-disagreement tail \(C_{3,g}\varepsilon^3\);
- comparable-ball \(O(t^2)\);
- low-degree tail \(q^{4/3}\);
- internal sparsity \(O(t^2)\);
- co-degree tail \(r^3\);
- tip middle-band suppression;
- curvature-independent graphon primeness.

The remaining work is now stochastic assembly: component uniqueness, implication escalation, and the modular hierarchy in the curved graphon sample.
