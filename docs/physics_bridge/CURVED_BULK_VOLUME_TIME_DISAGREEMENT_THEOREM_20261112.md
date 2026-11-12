# Theorem capsule: curved-spacetime bulk disagreement from a volume-time gradient

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** conditional analytic theorem under explicit differentiability and temporal-gradient hypotheses  
**Physical status:** intrinsic curved-spacetime generalization of the bulk small-disagreement mechanism  
**Novelty status:** volume time functions are classical; the project-specific observation is that their differential is the first variation of arrow-erasure splitter volume

## 1. Setting

Let

\[
D=I(p,q)
\]

be a causally convex Alexandrov interval in a smooth \(d\)-dimensional Lorentzian spacetime.

Let

\[
V_D
=
\operatorname{Vol}_g(D)
\]

and use the normalized physical volume measure

\[
d\mu
=
\frac{
d\operatorname{Vol}_g
}{
V_D
}.
\]

For \(a\prec b\), write

\[
\mathcal V(a,b)
=
\frac{
\operatorname{Vol}_g(I(a,b))
}{
V_D
}.
\]

Define the local volume-difference function

\[
\boxed{
\Phi(x)
=
\mathcal V(p,x)
-
\mathcal V(x,q).
}
\]

## 2. Exact disagreement identity

For

\[
x\prec y
\]

inside \(D\),

\[
\boxed{
\Delta_g(x,y)
=
\mathcal V(p,y)
-
\mathcal V(p,x)
+
\mathcal V(x,q)
-
\mathcal V(y,q)
-
2\mathcal V(x,y).
}
\]

Equivalently,

\[
\boxed{
\Delta_g(x,y)
=
\Phi(y)-\Phi(x)
-
2\mathcal V(x,y).
}
\]

This identity is exact and does not assume flatness.

## 3. First variation

Fix an interior point \(x\).

Assume the functions

\[
x\mapsto\mathcal V(p,x),
\qquad
x\mapsto\mathcal V(x,q)
\]

are \(C^2\) in a neighborhood of \(x\).

Let

\[
y=\exp_x(h)
\]

with \(h\) future timelike and small.

Taylor expansion gives

\[
\Phi(y)-\Phi(x)
=
d\Phi_x(h)
+
O(|h|^2).
\]

A sufficiently small Alexandrov interval has volume

\[
\mathcal V(x,y)
=
O(|h|^d).
\]

Therefore

\[
\boxed{
\Delta_g(x,\exp_x h)
=
d\Phi_x(h)
+
O(|h|^2)
+
O(|h|^d).
}
\]

For

\[
d>2,
\]

this simplifies to

\[
\boxed{
\Delta_g(x,\exp_x h)
=
d\Phi_x(h)
+
O(|h|^2).
}
\]

Thus the first-order splitter geometry is the differential of a volume-time function.

## 4. Temporal-gradient hypothesis

Assume

\[
d\Phi_x
\]

is a timelike covector at the point.

Define

\[
\boxed{
\kappa(x)
=
\sqrt{
-g_x^{-1}
(
d\Phi_x,
d\Phi_x
)
}.
}
\]

Choose the sign convention so that

\[
d\Phi_x(h)>0
\]

for future-timelike \(h\).

A local Lorentz frame sends

\[
d\Phi_x
\]

to

\[
\kappa(x)\,dh^0.
\]

Hence the leading small-disagreement condition is

\[
0<h^0
\le
\frac{\varepsilon}{
\kappa(x)
},
\]

with

\[
|\mathbf h|<h^0.
\]

## 5. Universal local cone volume

Let

\[
\omega_{d-1}
=
\operatorname{Vol}(
B^{d-1}_{\mathrm{Eucl}}(1)
).
\]

The coordinate volume of the future-timelike cone cut by

\[
d\Phi_x(h)\le\varepsilon
\]

is

\[
\begin{aligned}
\int_0^{\varepsilon/\kappa(x)}
\omega_{d-1}
(h^0)^{d-1}
\,dh^0
&=
\boxed{
\frac{
\omega_{d-1}
}{
d
}
\frac{
\varepsilon^d
}{
\kappa(x)^d
}.
}
\end{aligned}
\]

Riemann normal coordinates have

\[
\sqrt{|g|}
=
1+O(|h|^2),
\]

so the physical volume has the same leading coefficient.

After dividing by \(V_D\), the conditional probability for \(Y\) is

\[
\boxed{
\Pr(
x\prec Y,\,
\Delta_g(x,Y)\le\varepsilon
\mid
X=x
)
\sim
\frac{
\omega_{d-1}
}{
dV_D
}
\frac{
\varepsilon^d
}{
\kappa(x)^d
}.
}
\]

## 6. Bulk pair coefficient

Including both time orientations gives the bulk contribution

\[
\boxed{
F_d^{\mathrm{bulk}}(\varepsilon)
\sim
C_d^{\mathrm{bulk}}
\varepsilon^d,
}
\]

where

\[
\boxed{
C_d^{\mathrm{bulk}}
=
\frac{
2\omega_{d-1}
}{
dV_D
}
\int_D
\kappa(x)^{-d}
\,d\mu(x),
}
\]

provided:

1. \(d\Phi\) is timelike almost everywhere in the contributing region;
2. \(\kappa^{-d}\) is integrable;
3. the Taylor remainder is uniformly dominated on an exhaustion by compact interior sets.

This is an intrinsic curved-spacetime formula.

## 7. Flat d = 3 check

In the unit \(2+1\) Minkowski diamond,

\[
V_D
=
\frac{2\pi}{3},
\]

and

\[
\omega_2=\pi.
\]

Therefore

\[
\frac{
2\omega_2
}{
3V_D
}
=
1.
\]

Hence

\[
C_3^{\mathrm{bulk}}
=
\int_D
\kappa(x)^{-3}
\,d\mu(x).
\]

The dedicated flat calculation evaluates this integral exactly:

\[
C_3^{\mathrm{bulk}}
=
\frac{32\pi}{9}.
\]

Thus the intrinsic formula reproduces the previously derived result.

## 8. Relation to Geroch volume functions

The structure

\[
x
\mapsto
\operatorname{Vol}(I^-(x))
\]

is classical in Lorentzian causality theory.

Geroch introduced volume functions as time functions in the study of globally hyperbolic spacetimes.

Modern work continues to characterize when causal-volume functions are continuous, differentiable, or temporal.

The present function

\[
\Phi(x)
=
\frac{
\operatorname{Vol}(I(p,x))
-
\operatorname{Vol}(I(x,q))
}{
V_D
}
\]

is a finite-diamond analogue combining a past-volume and future-volume contribution.

The project-specific identity is

\[
\boxed{
d\Phi
=
\text{first variation of the symmetric causal-neighborhood disagreement}.
}
\]

## 9. Consequence for generic curved 2+1 spacetime

In \(d=3\), the flat leading tail is bulk dominated.

Therefore the natural curved candidate is

\[
\boxed{
F_3(\varepsilon)
\sim
\frac{
2\pi
}{
3V_D
}
\left(
\int_D
\kappa(x)^{-3}
\,d\mu(x)
\right)
\varepsilon^3.
}
\]

This becomes a theorem if, in addition to the bulk hypotheses above, every boundary degeneration contributes

\[
o(\varepsilon^3).
\]

That final boundary statement has not yet been proved in a generic curved diamond.

Accordingly, the full generic-curved \(2+1\) recovery-rate formula remains conditional.

## 10. Why this matters

This formulation converts the generic-curvature problem into two geometric questions:

1. Is the finite-diamond volume function \(\Phi\) temporal with sufficiently regular gradient?
2. Are null-boundary degenerations subleading to the bulk in \(2+1\)?

These are recognizable problems in Lorentzian geometry.

They are substantially more precise than the vague question of whether "small curvature preserves the flat result."

## 11. Failure modes

The bulk formula can fail if:

- \(\Phi\) is not differentiable;
- \(d\Phi\) becomes null or vanishes on a positive-measure set;
- \(\kappa^{-d}\) is nonintegrable;
- cut loci or caustics destroy uniform local expansions;
- a boundary sector has a smaller small-\(\Delta\) exponent than \(d\).

The theorem does not assume these possibilities away silently; they are explicit hypotheses or open checks.

## 12. Next target

For \(2+1\), the next rigorous step is to prove the null-boundary remainder

\[
F_3^{\mathrm{boundary}}(\varepsilon)
=
o(\varepsilon^3)
\]

under geometric conditions such as:

- smooth compact diamond edge;
- transverse future/past null hypersurface intersection;
- no null conjugate points inside the relevant generators;
- quantitative bounds on expansion and shear.

For \(d\ge4\), the boundary sector is leading rather than subleading and requires a separate curved joint theorem.
