# Curvature bridge: exact disagreement identity, small-diamond expansion, and the rare-event obstruction

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** exact geometric identity + rigor boundary for generic curvature  
**Physical status:** identifies what is and is not currently proved beyond the conformally flat class  
**Novelty status:** small causal-diamond curvature expansions are established literature; the project-specific contribution is identifying the uniform rare-event estimate required by arrow-erasure orientation recovery

## 1. Purpose

The flat and conformally flat orientation-recovery problems are now controlled.

A generic curved Lorentzian metric changes both:

1. the causal cones;
2. the physical volume measure.

It is therefore tempting to apply the standard small-causal-diamond expansion and declare the flat UPO theorem perturbatively stable.

That step is not justified.

This note records the exact curved disagreement identity, imports the known causal-diamond volume expansion, and explains the missing uniform estimate.

## 2. Exact disagreement identity in a curved Alexandrov interval

Let

\[
D=I(p,q)
\]

be an Alexandrov interval in a Lorentzian spacetime.

Use the normalized spacetime volume measure

\[
\mu_D(E)
=
\frac{\operatorname{Vol}_g(E)}{
\operatorname{Vol}_g(D)
}.
\]

For

\[
x\prec y
\]

inside \(D\), define

\[
A_x
=
\{z\in D:z\sim x\}.
\]

Up to null boundaries,

\[
A_x
=
I(p,x)
\;\dot\cup\;
I(x,q),
\]

and

\[
A_y
=
I(p,y)
\;\dot\cup\;
I(y,q).
\]

Because

\[
p\prec x\prec y\prec q,
\]

their common comparability region is

\[
A_x\cap A_y
=
I(p,x)
\;\dot\cup\;
I(x,y)
\;\dot\cup\;
I(y,q).
\]

Therefore the symmetric-difference volume is exactly

\[
\boxed{
\Delta_g(x,y)
=
\frac{
V_g(p,y)-V_g(p,x)
+
V_g(x,q)-V_g(y,q)
-
2V_g(x,y)
}{
V_g(p,q)
},
}
\]

where

\[
V_g(a,b)
=
\operatorname{Vol}_g(I(a,b)).
\]

This identity does not assume flatness.

It is the correct starting point for generic curvature.

## 3. Known small-causal-diamond expansion

For a sufficiently small timelike-separated pair \(a\prec b\), let

\[
\tau=\tau(a,b)
\]

be their proper-time separation and let the curvature scale be much larger than \(\tau\).

Gibbons and Solodukhin derive, in arbitrary spacetime dimension \(d\),

\[
\boxed{
V_g(a,b)
=
V_{\rm flat}(\tau)
\left[
1
-
\frac{d}{
24(d+1)(d+2)
}
R\,\tau^2
+
\frac{d}{
24(d+1)
}
R_{\hat0\hat0}\,\tau^2
+
\cdots
\right].
}
\]

The curvature tensors are evaluated at the midpoint to the displayed order, with \(\hat0\) aligned with the timelike geodesic joining the interval endpoints.

Thus, schematically,

\[
V_g(a,b)
=
V_{\rm flat}(\tau)
\left[
1+O(\mathcal K\tau^2)
\right]
\]

when curvature is uniformly bounded by a scale \(\mathcal K\).

This expansion is established literature and is not a project result.

## 4. What the standard expansion gives for disagreement

Let the parent diamond have timelike diameter \(L\), small compared with the curvature radius.

Every subinterval occurring in the exact disagreement identity has duration at most \(L\).

Therefore the individual normalized volume terms have curvature corrections of order

\[
O(\mathcal K L^2).
\]

Without using additional cancellation, substitution into the exact disagreement identity yields only an **absolute** estimate of the schematic form

\[
\boxed{
\Delta_g(x,y)
=
\Delta_{\rm tangent}(x,y)
+
O(\mathcal K L^2),
}
\]

where \(\Delta_{\rm tangent}\) denotes the corresponding leading tangent-space expression after the coordinate/proper-time identification is fixed.

The important point is that the error is not yet known to contain a factor of \(\Delta\).

## 5. Why absolute control is insufficient

The leading UPO failure mechanism is a true-twin pair.

Conditioned on a pair with disagreement \(\Delta\), the pair survives as sampled twins with probability approximately

\[
e^{-n\Delta}.
\]

Therefore the relevant rare-event scale is

\[
\boxed{
\Delta
\asymp
\frac1n.
}
\]

For a fixed curved diamond,

\[
\mathcal K L^2
\]

is a fixed small number.

No matter how small it is, eventually

\[
\frac1n
\ll
\mathcal K L^2.
\]

Thus an additive estimate

\[
|\Delta_g-\Delta_{\rm flat}|
\le
C\mathcal K L^2
\]

cannot determine the geometry of the events with

\[
\Delta_g\sim\frac1n.
\]

The asymptotic error law is probing structure far below the resolution supplied by the standard small-diamond expansion.

## 6. The missing estimate

What would be sufficient is a **relative splitter estimate**.

A model target is

\[
\boxed{
\Delta_g(x,y)
=
\Delta_{\rm flat}^{\rm loc}(x,y)
\left[
1
+
O(\mathcal K L^2)
\right]
}
\]

uniformly over the small-disagreement sectors that dominate the rare-event probability.

A weaker two-sided form would also suffice:

\[
\boxed{
c(\mathcal K L^2)
\,
\Delta_{\rm flat}^{\rm loc}
\le
\Delta_g
\le
C(\mathcal K L^2)
\,
\Delta_{\rm flat}^{\rm loc},
}
\]

with positive constants remaining bounded away from zero and infinity as the pair approaches the null-joint or bulk small-disagreement scaling.

Such an estimate would preserve the small-\(\Delta\) exponent.

The standard causal-diamond volume expansion does not by itself provide this factorization.

## 7. Why cancellation may exist

The exact disagreement is not an arbitrary sum of interval volumes.

It is the measure of the geometric set

\[
A_x\triangle A_y.
\]

Hence it is nonnegative and vanishes exactly when the two causal neighborhoods agree up to measure zero.

This suggests that the large individual interval-volume curvature corrections in the algebraic formula should cancel when

\[
x\to y
\]

or when the pair approaches a twin-like null-joint configuration.

In other words, the true geometric quantity is the volume of a thin splitter region, not the difference of five unrelated large numbers.

A direct geometric expansion of that thin region is therefore more promising than term-by-term expansion of the five Alexandrov volumes.

## 8. Two asymptotic sectors must be treated separately

The flat theorem already shows two different mechanisms.

### d = 3

The leading small-disagreement tail is bulk dominated.

The curved problem should begin with a local Riemann-normal-coordinate expansion of the splitter region for a small timelike displacement

\[
y=x+h.
\]

The flat linear functional

\[
C_x\cdot_M h
\]

should acquire curvature corrections.

The target is a uniformly timelike perturbed covector with a controlled local cone-volume coefficient.

### d >= 4

The leading tail is null-joint dominated.

The required curved analysis is more delicate because the pair approaches the codimension-two edge of the parent diamond.

One must simultaneously control:

- curvature-induced deformation of the two null hypersurfaces;
- the physical volume density;
- the angular causal cap;
- cancellation in the splitter volume.

This is the true curved analogue of the flat joint blow-up.

## 9. A conditional double-scaling observation

Suppose, hypothetically, one had only the absolute estimate

\[
|\Delta_g-\Delta_{\rm flat}|
\le
C\mathcal K L^2.
\]

Then flat rare-event statistics at the scale

\[
1/n
\]

could be transferred only in a double limit satisfying

\[
\boxed{
n\mathcal K L^2
\to0.
}
\]

This would require the physical diamond itself to shrink as \(n\) grows.

That is a mathematically possible tangent-space regime, but it is not the fixed-window theorem we ultimately want.

Therefore this double-scaling route should not be confused with curvature robustness at fixed physical size.

## 10. Conformal class as the solved curved sector

If

\[
g=\Omega^2\eta,
\]

the causal relation is unchanged exactly.

Only the measure changes.

The weighted-measure theorem therefore proves full orientation recovery and preserves the flat error exponents without requiring any small-curvature assumption.

This identifies the first genuinely curved class for which the problem is already solved.

Generic curvature begins exactly where the null cones cease to be conformally equivalent to the flat ones.

## 11. Literature boundary

Relevant established results include:

- G. W. Gibbons and S. N. Solodukhin, **The Geometry of Small Causal Diamonds** (2007), which gives the arbitrary-dimensional \(O(\tau^2)\) curvature correction to Alexandrov-interval volume;
- Jinzhao Wang, **Geometry of small causal diamonds** (2019), which develops perturbative causal-diamond geometry in Riemann normal coordinates and higher-order vacuum corrections;
- causal-set curvature constructions such as Benincasa–Dowker, which show that discrete causal structures can encode continuum curvature observables.

These works supply geometric ingredients.

They do not, in the targeted review, address the rare small-splitter-volume statistic required by the present orientation-recovery problem.

## 12. Current generic-curvature target

The next theorem should not be stated as

> small curvature preserves the flat UPO theorem.

That has not been proved.

The correct target is:

> derive a curvature-uniform local asymptotic for the splitter volume
> \[
> \mu_g(A_x\triangle A_y)
> \]
> in the bulk and null-joint blow-up sectors.

The decisive question is whether curvature changes only the coefficient or can also alter the small-disagreement exponent.

Until that calculation is completed, the fixed generic-curved-spacetime recovery theorem remains open.
