# Stein–Palm reduction for the 3+1 isolated-vertex Poisson limit

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** superseded by `MINKOWSKI_4D_ISOLATED_POISSON_THEOREM_20261111.md`; the endpoint-overlap lemma proposed here has now been proved and closes the Poisson-process argument  
**Target:** prove \(I_\lambda\Rightarrow\operatorname{Poisson}(3\pi)\)

## 1. Setup

Work first in the Poisson sprinkling ensemble.

Let \(A\) be the standard flat \(3+1\)-dimensional Alexandrov interval equipped with normalized volume measure \(\mu\).

Let \(\eta_\lambda\) be a Poisson point process on \(A\) with intensity measure

\[
\lambda\mu.
\]

Join two sprinkled points exactly when they are causally comparable.

For \(x\in A\), define its continuum comparability region

\[
S_x
=
\{y\in A:y\sim x\},
\]

its normalized comparable volume

\[
Q(x)=\mu(S_x),
\]

and for two points

\[
R(x,y)
=
\mu(S_x\cap S_y).
\]

Let

\[
I_\lambda
\]

be the number of isolated vertices in the resulting comparability graph.

The exact mean is

\[
\alpha_\lambda
:=
E[I_\lambda]
=
\lambda
\int_A
e^{-\lambda Q(x)}
\,\mu(dx).
\]

The previous null-waist analysis gives

\[
\alpha_\lambda\to3\pi.
\]

## 2. Why Penrose's homogeneous theorem is not a black box here

Penrose (2018), *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, gives general Poisson approximation criteria.

The convenient homogeneous theorem in that paper does not directly apply to the present causal kernel because

\[
\phi(x,y)
=
\mathbf 1_{\{x\sim y\}}
\]

is deterministic, has

\[
\sup\phi=1,
\]

and fails uniform \(\varepsilon\)-homogeneity because

\[
\inf_x Q(x)=0
\]

at the null waist.

However, Penrose's more general Poisson-process coupling theorem (his Theorem 3.1) does not require this special homogeneous geometry.

It gives a total-variation bound once an explicit Palm coupling is constructed.

That coupling is particularly simple here.

## 3. Exact isolation coupling

Fix \(x\in A\).

Split the Poisson process into the independent restrictions

\[
\eta_{\mathrm{in}}
=
\eta_\lambda\cap S_x
\]

and

\[
\eta_{\mathrm{out}}
=
\eta_\lambda\cap S_x^c.
\]

In the graph on

\[
\eta_\lambda\cup\{x\},
\]

the event

\[
x\text{ is isolated}
\]

is exactly

\[
\eta_{\mathrm{in}}=\varnothing.
\]

By Poisson independence, conditioning on that event leaves

\[
\eta_{\mathrm{out}}
\]

unchanged.

Therefore an exact coupling is:

- \(U_x\): number of isolated vertices in the original graph on \(\eta_\lambda\);
- \(V_x\): number of isolated vertices in the graph induced by \(\eta_{\mathrm{out}}\).

Then

\[
U_x\overset d=I_\lambda,
\]

and

\[
1+V_x
\]

has the conditional distribution of the isolated count after adding \(x\), given that \(x\) is isolated.

This is exactly the structure required by the \(k=1\) case of Penrose's general coupling theorem.

## 4. What deleting \(S_x\) can change

Deleting the points of \(\eta_{\mathrm{in}}\) can affect the isolated count in only two ways.

### A. Destroyed isolated vertices

An originally isolated point lying in \(S_x\) is removed.

Let its expected number be

\[
a_\lambda(x).
\]

By Campbell–Mecke,

\[
\boxed{
a_\lambda(x)
=
\lambda
\int_{S_x}
e^{-\lambda Q(y)}
\,\mu(dy).
}
\]

### B. Newly isolated vertices

A point \(y\notin S_x\) can become isolated after the deletion if

1. it has no neighbors in
   \[
   S_y\setminus S_x,
   \]
   and
2. it had at least one neighbor in
   \[
   S_y\cap S_x.
   \]

The two regions are disjoint Poisson sets.

Hence the expected number of newly isolated vertices is exactly

\[
\boxed{
b_\lambda(x)
=
\lambda
\int_{S_x^c}
e^{-\lambda(Q(y)-R(x,y))}
\left(
1-e^{-\lambda R(x,y)}
\right)
\mu(dy).
}
\]

Consequently,

\[
\boxed{
E|U_x-V_x|
\le
a_\lambda(x)+b_\lambda(x).
}
\]

## 5. Total-variation reduction

The Palm probability that an inserted point \(x\) is isolated is

\[
p_\lambda(x)
=
e^{-\lambda Q(x)}.
\]

Applying the \(k=1\) case of Penrose's general Poisson coupling theorem gives

\[
d_{\mathrm{TV}}
\left(
\mathcal L(I_\lambda),
\operatorname{Poisson}(\alpha_\lambda)
\right)
\le
(1\wedge\alpha_\lambda^{-1})
\left(
A_\lambda+B_\lambda
\right),
\]

where

\[
\boxed{
A_\lambda
=
\lambda^2
\int_A
\int_{S_x}
e^{-\lambda(Q(x)+Q(y))}
\,\mu(dy)\mu(dx)
}
\]

and

\[
\boxed{
B_\lambda
=
\lambda^2
\int_A
e^{-\lambda Q(x)}
\int_{S_x^c}
e^{-\lambda(Q(y)-R(x,y))}
\left(
1-e^{-\lambda R(x,y)}
\right)
\mu(dy)\mu(dx).
}
\]

Therefore the Poisson-limit conjecture reduces to

\[
\boxed{
A_\lambda\to0,
\qquad
B_\lambda\to0.
}
\]

Since

\[
\alpha_\lambda\to3\pi,
\]

those two limits imply

\[
\boxed{
I_\lambda
\xrightarrow d
\operatorname{Poisson}(3\pi).
}
\]

This is now a two-integral geometric problem.

## 6. The first error term

The factor

\[
e^{-\lambda Q(x)}
e^{-\lambda Q(y)}
\]

localizes both points to the null waist:

\[
a_x,b_x,a_y,b_y
=
O(\lambda^{-1/2}).
\]

Use the rescaled coordinates

\[
a_x=\frac{2A}{\sqrt\lambda},
\qquad
b_x=\frac{2B}{\sqrt\lambda},
\]

and

\[
a_y=\frac{2C}{\sqrt\lambda},
\qquad
b_y=\frac{2D}{\sqrt\lambda}.
\]

For the two points to be causally comparable, their angular separation is of order

\[
\lambda^{-1/2}.
\]

Writing

\[
\theta
=
\frac{2|z|}{\sqrt\lambda},
\]

the future-directed condition tends to

\[
C>A,
\qquad
B>D,
\qquad
|z|^2<(C-A)(B-D).
\]

The limiting pair calculation gives

\[
A_\lambda
\sim
\frac{288J^2}{\lambda},
\]

where

\[
J
=
\int_{0\le A<C}
(C-A)
e^{-(A^2+C^2)}
\,dA\,dC.
\]

The integral is

\[
J
=
\frac{\sqrt\pi(\sqrt2-1)}4.
\]

Hence the candidate leading term is

\[
\boxed{
A_\lambda
\sim
\frac{
18\pi(3-2\sqrt2)
}{\lambda}.
}
\]

Numerically,

\[
18\pi(3-2\sqrt2)
\approx
9.70222.
\]

In particular,

\[
A_\lambda=O(\lambda^{-1})
\]

if the same standard null-waist domination used for the mean is supplied.

This term is therefore too small to control the leading convergence rate suggested by the simulations.

## 7. The second error term and the \(n^{-1/4}\) angular scale

The difficult term is

\[
B_\lambda.
\]

Here \(x\) and \(y\) are themselves incomparable.

Correlation arises only because their continuum comparability regions overlap:

\[
R(x,y)>0.
\]

For two waist points whose angular directions differ by \(\theta\), their long thin endpoint Alexandrov intervals have transverse width of order

\[
\lambda^{-1/4}.
\]

This identifies the collision scale

\[
\boxed{
\theta
\asymp
\lambda^{-1/4}.
}
\]

A spherical cap on \(S^2\) of this angular radius has normalized area

\[
O(\lambda^{-1/2}).
\]

This suggests

\[
B_\lambda
=
O(\lambda^{-1/2}),
\]

which would both prove convergence and explain the slow finite approach of the Fano factor and factorial moments.

## 8. A useful overlap estimate to prove

Near the past endpoint, write an almost-null waist event as

\[
x=(T_x,r_x\sigma_x)
\]

with null deficit

\[
a_x=T_x-r_x.
\]

A fixed-time cross-section of the thin Alexandrov interval \(I(p,x)\) has

- longitudinal thickness \(O(a_x)\);
- transverse squared radius \(O(a_x s)\) near the endpoint time \(s\).

For two directions separated by \(\theta\), the transverse centers are separated by \(O(s\theta)\).

The overlap can therefore persist only while

\[
s\theta
\lesssim
\sqrt{a s},
\]

or

\[
s
\lesssim
\frac{a}{\theta^2}.
\]

This scaling yields the candidate four-volume bound

\[
\operatorname{vol}
\left(
I(p,x)\cap I(p,y)
\right)
\lesssim
\frac{
C\,a_x^2a_y^2
}{
\theta^4
}
\]

in the symmetric regime, with an analogous future term using \(b_x,b_y\).

A rigorous asymmetric version of this inequality is the cleanest remaining geometric lemma.

Under waist scaling

\[
a_x,a_y=O(\lambda^{-1/2}),
\]

it would imply, away from the collision cap,

\[
\lambda R(x,y)
\lesssim
\frac{
C\,\mathcal R(A,B,C,D)
}{
\lambda\theta^4
}.
\]

## 9. Two-region proof strategy

Fix a large \(L\).

Split the angular integral into

\[
\theta
\le
L\lambda^{-1/4}
\]

and its complement.

### Collision region

The angular measure is

\[
O(L^2\lambda^{-1/2}).
\]

After radial localization, the remaining integral is expected to stay uniformly bounded.

Thus this contribution is

\[
O(L^2\lambda^{-1/2}).
\]

### Separated region

If the overlap lemma holds, then for

\[
\theta
>
L\lambda^{-1/4}
\]

one gets

\[
\lambda R(x,y)
\lesssim
\frac{
C\,\mathcal R
}{
L^4
}.
\]

Using

\[
1-e^{-u}\le u,
\]

the separated-region contribution can then be made uniformly small by taking

\[
L\to\infty.
\]

A standard two-limit argument would establish

\[
B_\lambda\to0.
\]

With sharper uniform estimates, it should give the rate

\[
B_\lambda=O(\lambda^{-1/2})
\]

up to possible slowly varying factors.

## 10. Consequence

The distributional problem is now reduced to one geometric overlap statement.

The proof no longer needs to establish every factorial moment independently.

The chain is:

\[
\text{endpoint-overlap lemma}
\Longrightarrow
B_\lambda\to0,
\]

\[
A_\lambda=O(\lambda^{-1}),
\]

\[
\alpha_\lambda\to3\pi,
\]

therefore

\[
\boxed{
I_\lambda
\Rightarrow
\operatorname{Poisson}(3\pi).
}
\]

A subsequent depoissonization step would transfer the result to the fixed-\(n\) sprinkling.

## 11. Literature boundary

The probabilistic machinery is not claimed as new.

The relevant source is:

Mathew D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, **Journal of Applied Probability 55(1)**, 112–136 (2018), DOI 10.1017/jpr.2018.9.

The project-specific work is the Lorentzian causal kernel, its null-waist localization, the \(3\pi\) mean, and the geometry required to verify a Poisson approximation despite failure of the standard uniform-homogeneity hypotheses.

## 12. Current status

What is exact:

- the Palm isolation probability;
- the coupling obtained by deleting \(S_x\);
- the formulas for \(a_\lambda(x)\) and \(b_\lambda(x)\);
- the reduction of total variation to \(A_\lambda+B_\lambda\).

What is analytically derived but still needs uniform remainder control:

\[
A_\lambda
\sim
18\pi(3-2\sqrt2)\lambda^{-1}.
\]

What remains open:

\[
B_\lambda\to0,
\]

with the expected mechanism

\[
B_\lambda=O(\lambda^{-1/2}).
\]

That overlap estimate was subsequently proved and is incorporated into `MINKOWSKI_4D_ISOLATED_POISSON_THEOREM_20261111.md`, which establishes the Poisson-process limit with total-variation rate (O(\lambda^{-1/2})). The fixed-cardinality version remains separate.
