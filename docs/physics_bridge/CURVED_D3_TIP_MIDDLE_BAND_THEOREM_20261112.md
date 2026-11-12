# Theorem: curved tip middle-band clearance from null-cone first variation

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem for regular noncaustic tip cones  
**Physical status:** quantitative curved replacement of the flat tip-clearance lemma

## 1. Statement

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex \(2+1\)-dimensional Lorentzian diamond.

Assume the future null cone segment from \(p\) to the joint is smooth, has unique generators, and contains no cut or conjugate point.

Assume the analogous statement for the past null cone from \(q\).

Then there exist constants

\[
r_0>0,
\qquad
c_0>0,
\qquad
0<q_-<q_+<1
\]

such that every point \(x\) sufficiently close to either timelike tip and satisfying

\[
R(x)
=
1-Q(x)
\le r_0
\]

has a measurable nonneighbor set

\[
B_x^{\mathrm{mid}}
\subseteq
D\setminus A_x
\]

with

\[
\boxed{
\mu(B_x^{\mathrm{mid}})
\ge
c_0R(x)
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
\forall z\in B_x^{\mathrm{mid}}
}
\]

up to a set whose relative volume tends to zero with \(R(x)\).

The constants are uniform over all causal directions in which the tip is approached.

## 2. Regular null-cone coordinates

Work at the past tip \(p\).

Parameterize the smooth future null boundary by

\[
z=z(\lambda,\theta),
\]

where

\[
\theta\in S^1
\]

labels the initial null direction and

\[
0<\lambda<L(\theta)
\]

is an affine parameter.

The joint occurs at

\[
\lambda=L(\theta).
\]

Regularity and compactness imply

\[
0<L_{\min}
\le
L(\theta)
\le
L_{\max}<\infty.
\]

Before the cut/conjugate locus, the null cone is a smooth embedded hypersurface.

## 3. World-function first variation

Let

\[
\sigma(x,z)
\]

be Synge's world function on the unique geodesic branch joining the tip neighborhood to the regular null cone.

Along the null generator,

\[
\sigma(p,z(\lambda,\theta))
=
0.
\]

Let

\[
k_\theta
\]

be the future null initial tangent at \(p\), with affine normalization consistent with \(\lambda\).

The standard first-variation identity gives

\[
\boxed{
d_p\sigma(
v
)
=
-\lambda
g_p(
v,k_\theta
)
}
\]

for a displacement vector \(v\in T_pM\).

Move the tip to

\[
x_\epsilon
=
\exp_p(\epsilon v),
\]

where \(v\) is future causal and normalized by a fixed positive timelike covector.

Then

\[
\sigma(
x_\epsilon,
z(\lambda,\theta)
)
=
-\epsilon
\lambda
g_p(v,k_\theta)
+
O(\epsilon^2).
\]

For future causal \(v,k_\theta\),

\[
-g_p(v,k_\theta)
\ge0.
\]

It vanishes only when both are null and parallel.

## 4. Transverse displacement of the null boundary

Choose a smooth transverse vector field \(N\) along the regular null cone such that

\[
d_z\sigma(N)>0.
\]

The implicit-function theorem gives the shifted null boundary of \(x_\epsilon\) as a transverse displacement

\[
s_\epsilon(\lambda,\theta)
=
\epsilon
A(\lambda,\theta)
\left[
-g_p(v,k_\theta)
\right]
+
O(\epsilon^2),
\]

where

\[
A(\lambda,\theta)>0
\]

is smooth on every compact regular portion of the cone.

The physical volume density in these coordinates has the form

\[
J(\lambda,\theta,s)
\,d\lambda\,d\theta\,ds
\]

with

\[
J(\lambda,\theta,0)>0.
\]

Thus the nonneighbor sliver created by moving the tip has first-order volume density

\[
\boxed{
\epsilon
H(\lambda,\theta)
\left[
-g_p(v,k_\theta)
\right]
d\lambda\,d\theta,
}
\]

where

\[
H(\lambda,\theta)
=
A(\lambda,\theta)
J(\lambda,\theta,0)
>0.
\]

## 5. Total co-degree first variation

The small interval

\[
I(p,x_\epsilon)
\]

has volume

\[
O(\epsilon^3)
\]

and does not affect the first variation.

Therefore

\[
R(x_\epsilon)
=
\epsilon
\int_{S^1}
\int_0^{L(\theta)}
H(\lambda,\theta)
\left[
-g_p(v,k_\theta)
\right]
\,d\lambda\,d\theta
+
O(\epsilon^2).
\]

This is the geometric form of the temporal tip-gradient coefficient.

## 6. Choose a middle affine band

Fix

\[
0<a<b<1.
\]

Define

\[
\mathcal B
=
\left\{
z(\lambda,\theta):
aL(\theta)
\le
\lambda
\le
bL(\theta)
\right\}.
\]

This is a compact subset of the null boundary separated from:

- the tip \(p\);
- the joint \(\Sigma\).

On the future null boundary of \(p\),

\[
\mathcal V(p,z)=0.
\]

Hence

\[
Q(z)
=
\mathcal V(z,q).
\]

The function is continuous on \(\mathcal B\).

Because \(\mathcal B\) is separated from both endpoints,

\[
\boxed{
0<q_-
\le
Q(z)
\le
q_+<1
}
\]

uniformly on \(\mathcal B\).

## 7. Uniform fraction of the first variation

For each \(\theta\), define

\[
H_{\mathrm{tot}}(\theta)
=
\int_0^{L(\theta)}
H(\lambda,\theta)
\,d\lambda,
\]

and

\[
H_{\mathrm{mid}}(\theta)
=
\int_{aL(\theta)}^{bL(\theta)}
H(\lambda,\theta)
\,d\lambda.
\]

Regularity gives

\[
0<
H_{\mathrm{mid}}(\theta)
<
\infty,
\]

and

\[
0<
H_{\mathrm{tot}}(\theta)
<
\infty.
\]

Both vary continuously in \(\theta\).

Compactness of \(S^1\) gives

\[
\boxed{
c_*
=
\min_\theta
\frac{
H_{\mathrm{mid}}(\theta)
}{
H_{\mathrm{tot}}(\theta)
}
>0.
}
\]

Now weight both numerator and denominator by

\[
-g_p(v,k_\theta)
\ge0.
\]

Since the same angular weight appears in both integrals,

\[
\begin{aligned}
&
\int
H_{\mathrm{mid}}(\theta)
[-g(v,k_\theta)]
\,d\theta
\\
&\qquad\ge
c_*
\int
H_{\mathrm{tot}}(\theta)
[-g(v,k_\theta)]
\,d\theta.
\end{aligned}
\]

This bound is uniform in the causal approach direction \(v\).

## 8. Middle-band nonneighbor volume

Let

\[
B_{x_\epsilon}^{\mathrm{mid}}
\]

be the part of the nonneighbor sliver swept out over \(\mathcal B\).

Then

\[
\mu(
B_{x_\epsilon}^{\mathrm{mid}}
)
\ge
c_*
R(x_\epsilon)
+
O(\epsilon^2).
\]

Since

\[
R(x_\epsilon)
=
\Theta(\epsilon)
\]

under the nondegenerate temporal tip-gradient hypothesis,

\[
O(\epsilon^2)
=
o(R(x_\epsilon)).
\]

Therefore, after shrinking the tip neighborhood,

\[
\boxed{
\mu(
B_x^{\mathrm{mid}}
)
\ge
c_0
R(x)
}
\]

for some

\[
c_0>0.
\]

Every point of this middle band has continuum graphon degree in

\[
[q_-,q_+].
\]

## 9. Future tip

The same argument, with time orientation reversed, applies to the past null cone of \(q\).

Thus the constants can be chosen uniformly over both tips by taking minima and maxima.

## 10. Tip-clear candidate probability

Condition on a sampled point \(X_i=x\) with small co-degree

\[
R(x)=r.
\]

The probability that no one of the other \(n-1\) points lands in the middle band is at most

\[
\left(
1-c_0r
\right)^{n-1}
\le
e^{-c_0nr}.
\]

The curved co-degree tail satisfies

\[
\bar g_3(r)
=
O(r^3).
\]

Therefore the expected number of sampled tip-clear candidates is

\[
n
\int_0^{r_0}
e^{-cnr}
\,d\bar g_3(r)
=
\boxed{
O(n^{-2}).
}
\]

## 11. Near-whole module consequence

Work on the event that the sampled graph has a unique edge-containing component.

A proper near-whole module requires an outside vertex complete to the module.

Such a complete external vertex must be near-universal, hence in the tip regime.

If its middle band contains a sampled point \(z\), then:

- \(z\) is a nonneighbor of the complete external vertex;
- \(z\) has continuum degree in \([q_-,q_+]\);
- with exponentially high probability, \(z\) has neither \(o(n)\) nor \(n-o(n)\) sampled degree.

Therefore \(z\) cannot have either module-compatible external type.

Thus a near-whole module requires a tip-clear candidate, except on an exponentially small event.

Hence

\[
\boxed{
\Pr(
\text{near-whole module}
)
=
O(n^{-2})
+
e^{-\Theta(n)}
}
\]

in regular curved \(2+1\).

## 12. Geometric meaning

The middle-band mechanism is not a flat-coordinate artifact.

It is the first variation of a smooth null cone under motion of its vertex.

The factor

\[
-g(v,k_\theta)
\]

is the universal Lorentzian directional response.

The function

\[
H(\lambda,\theta)
\]

contains the curved focusing/Jacobi information.

The proof works because this focusing factor is positive and regular before caustics.

## 13. Literature boundary

The first variation of Synge's world function and its relation to geodesic endpoint momenta are standard.

Van Vleck/Jacobi theory controls the regularity of the focusing factor.

The present use of the first-variation density to obtain a fixed-degree middle band and an \(O(n^{-2})\) module-clearance rate is project-specific.

## 14. Limitation

The argument can fail at:

- null cut points;
- conjugate points;
- branching null generators;
- nonsmooth causal boundaries.

Those are precisely the geometries excluded by the regular curved theorem.

No claim is made beyond the pre-caustic regular class.
