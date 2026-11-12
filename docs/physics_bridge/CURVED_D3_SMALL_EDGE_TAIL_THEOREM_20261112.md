# Theorem: small-disagreement edge tail in a regular curved 2+1 causal diamond

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem under explicit regularity hypotheses  
**Physical status:** curved-spacetime extension of the \(2+1\) bulk-dominated small-edge law

## 1. Statement

Let

\[
D=I(p,q)
\]

be a relatively compact causally convex Alexandrov interval in a smooth \(2+1\)-dimensional Lorentzian spacetime.

Use normalized volume

\[
\mathcal V(a,b)
=
\frac{
\operatorname{Vol}_g(I(a,b))
}{
V_D
},
\qquad
V_D
=
\operatorname{Vol}_g(D).
\]

Define

\[
\Phi(x)
=
\mathcal V(p,x)
-
\mathcal V(x,q).
\]

Assume:

1. the null joint is regular in the sense of the volume-null coordinate theorem;
2. the regular curved joint-suppression theorem applies;
3. \(\Phi\) is \(C^2\) in the interior away from the joint;
4. \(d\Phi\) is timelike there;
5. the function
   \[
   \kappa(x)^{-3},
   \qquad
   \kappa(x)
   =
   \sqrt{
   -g^{-1}(d\Phi,d\Phi)
   },
   \]
   is integrable over \(D\);
6. the compact-exhaustion Taylor remainder in the bulk is uniformly dominated.

Then

\[
\boxed{
F_{3,g}(\varepsilon)
:=
\Pr(
X\sim Y,\,
\Delta_g(X,Y)\le\varepsilon
)
\sim
C_g
\varepsilon^3,
}
\]

where

\[
\boxed{
C_g
=
\frac{
2\pi
}{
3V_D
}
\int_D
\kappa(x)^{-3}
\,d\mu(x).
}
\]

The coefficient is finite and strictly positive.

## 2. Exact disagreement identity

For

\[
x\prec y
\]

inside \(D\),

\[
\Delta_g(x,y)
=
\Phi(y)-\Phi(x)
-
2\mathcal V(x,y).
\]

For

\[
y=\exp_x(h)
\]

with \(h\) future timelike and small,

\[
\Phi(y)-\Phi(x)
=
d\Phi_x(h)
+
O(|h|^2).
\]

In \(2+1\),

\[
\mathcal V(x,y)
=
O(|h|^3).
\]

Hence

\[
\boxed{
\Delta_g(x,\exp_x h)
=
d\Phi_x(h)
+
O(|h|^2).
}
\]

## 3. Local bulk coefficient

At a point where \(d\Phi\) is timelike, choose a local Lorentz frame in which

\[
d\Phi
=
\kappa\,dh^0.
\]

The future-timelike displacement region satisfying

\[
d\Phi(h)\le\varepsilon
\]

has physical volume

\[
\frac{\pi}{3}
\frac{\varepsilon^3}{\kappa^3}.
\]

Dividing by \(V_D\) gives the conditional probability contribution for \(Y\).

Including both future and past orientations yields the local pair coefficient

\[
\frac{
2\pi
}{
3V_D
}
\kappa(x)^{-3}.
\]

## 4. Compact bulk exhaustion

Let

\[
K_\eta
\Subset D
\]

be the complement of an \(\eta\)-neighborhood of the null joint and any other boundary chart where the bulk Taylor expansion is not uniform.

On \(K_\eta\), continuity and timelikeness give

\[
\kappa(x)\ge c_\eta>0.
\]

Dominated Taylor expansion therefore gives

\[
\lim_{\varepsilon\downarrow0}
\varepsilon^{-3}
F_{3,g}^{K_\eta}(\varepsilon)
=
\frac{
2\pi
}{
3V_D
}
\int_{K_\eta}
\kappa(x)^{-3}
\,d\mu(x).
\]

## 5. Regular joint contribution

The curved joint-suppression theorem gives

\[
F_{3,g}^{\mathrm{joint}}
(
\varepsilon;\eta
)
\le
C
\left[
\eta^{1/2}\varepsilon^3
+
\eta^{1/4}\varepsilon^{19/6}
+
\varepsilon^{10/3}
\right].
\]

Therefore

\[
\limsup_{\varepsilon\downarrow0}
\frac{
F_{3,g}^{\mathrm{joint}}
(
\varepsilon;\eta
)
}{
\varepsilon^3
}
\le
C\eta^{1/2}.
\]

Letting

\[
\eta\downarrow0
\]

removes any independent joint coefficient.

## 6. Integrability near the joint

By hypothesis,

\[
\kappa^{-3}\in L^1(D,\mu).
\]

Therefore

\[
\int_{D\setminus K_\eta}
\kappa^{-3}
\,d\mu
\to0
\]

as

\[
\eta\downarrow0.
\]

The bulk coefficient obtained on compact exhaustions therefore converges to the full integral.

## 7. Global limit

For every fixed \(\eta\),

\[
F_{3,g}(\varepsilon)
=
F_{3,g}^{K_\eta}(\varepsilon)
+
F_{3,g}^{\mathrm{joint}}(\varepsilon;\eta)
+
o_\eta(\varepsilon^3),
\]

where any remaining regular boundary charts are handled by the same local bulk expansion or are strictly subleading.

Take

\[
\varepsilon\downarrow0
\]

first and then

\[
\eta\downarrow0.
\]

The result is

\[
\boxed{
F_{3,g}(\varepsilon)
\sim
\frac{
2\pi
}{
3V_D
}
\left(
\int_D
\kappa^{-3}
\,d\mu
\right)
\varepsilon^3.
}
\]

## 8. Flat regression

For the unit flat \(2+1\) Minkowski diamond,

\[
V_D
=
\frac{2\pi}{3}.
\]

The intrinsic integral evaluates exactly to

\[
\int_D
\kappa^{-3}
\,d\mu
=
\frac{32\pi}{9}.
\]

Therefore

\[
C_g
=
\frac{32\pi}{9},
\]

recovering

\[
F_3(\varepsilon)
\sim
\frac{32\pi}{9}
\varepsilon^3.
\]

## 9. True-twin first moment

Let \(T_n\) be the number of comparable true-twin pairs.

The exact identity remains

\[
\mathbb E[T_n]
=
\binom n2
\int_0^1
(1-\delta)^{n-2}
\,dF_{3,g}(\delta).
\]

Hence

\[
\boxed{
\mathbb E[T_n]
\sim
3C_g
\,n^{-1}.
}
\]

Explicitly,

\[
\boxed{
\mathbb E[T_n]
\sim
\frac{
2\pi
}{
V_D
}
\left(
\int_D
\kappa^{-3}
\,d\mu
\right)
\frac1n.
}
\]

This is the natural curved generalization of the flat coefficient

\[
32\pi/3.
\]

## 10. Scope

This theorem establishes the local rare-edge statistic.

It does not by itself prove the full finite-sample orientation-recovery theorem in the curved spacetime.

For that, one must additionally control:

- components;
- implication escalation;
- balanced modules;
- near-whole modules.

The regular curved \(2+1\) program now has all local ingredients except the tip/co-degree estimate needed for the last item.
