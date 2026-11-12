# Corollary: matter interpretation of the 3+1 first curvature response

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** algebraic corollary of the geometric curvature-response theorem plus Einstein's field equation  
**Physical status:** interprets the first local recovery-rate correction in terms of matter variables  
**Novelty status:** Einstein's equation is standard; only its application to the project-specific recovery coefficient is new to this program

## 1. Geometric result

The local \(3+1\) recovery coefficient is

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
+
\pi L^2
\left(
3R_{TT}-R
\right)_o
+
o(L^2),
}
\]

where

\[
R_{TT}
=
R_{\mu\nu}T^\mu T^\nu
\]

and \(T\) is the future unit timelike vector defining the centered diamond.

This statement is purely geometric.

No field equation is required.

## 2. Einstein equation convention

Now assume the spacetime satisfies

\[
\boxed{
R_{\mu\nu}
-
\frac12
Rg_{\mu\nu}
+
\Lambda g_{\mu\nu}
=
8\pi G
T_{\mu\nu}.
}
\]

Use signature

\[
(+---)
\]

and normalize

\[
T^\mu T_\mu=1.
\]

Let

\[
\rho
=
T_{\mu\nu}T^\mu T^\nu
\]

be the matter energy density measured by the diamond observer.

Let

\[
T
=
T^\mu{}_\mu
\]

be the stress-energy trace.

## 3. Ricci tensor in terms of matter

Taking the trace of Einstein's equation in four dimensions gives

\[
\boxed{
R
=
4\Lambda
-
8\pi G T.
}
\]

Solving for the Ricci tensor,

\[
\boxed{
R_{\mu\nu}
=
8\pi G
\left(
T_{\mu\nu}
-
\frac12
Tg_{\mu\nu}
\right)
+
\Lambda g_{\mu\nu}.
}
\]

Therefore

\[
\boxed{
R_{TT}
=
8\pi G
\left(
\rho-\frac12T
\right)
+
\Lambda.
}
\]

## 4. Recovery curvature combination

Substitute into

\[
3R_{TT}-R.
\]

Then

\[
\begin{aligned}
3R_{TT}-R
&=
24\pi G\rho
-
12\pi GT
+
3\Lambda\\
&\quad
-
4\Lambda
+
8\pi GT\\
&=
\boxed{
4\pi G(6\rho-T)-\Lambda.
}
\end{aligned}
\]

Hence

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
+
\pi L^2
\left[
4\pi G(6\rho-T)
-
\Lambda
\right]_o
+
o(L^2).
}
\]

## 5. Perfect fluid

For a perfect fluid in the observer rest frame,

\[
T_{\mu\nu}
=
(\rho+p)T_\mu T_\nu
-
pg_{\mu\nu},
\]

and

\[
T=\rho-3p.
\]

Therefore

\[
6\rho-T
=
5\rho+3p.
\]

Thus

\[
\boxed{
K_{4,g}(D_L)
=
9\pi
+
\pi L^2
\left[
4\pi G(5\rho+3p)
-
\Lambda
\right]_o
+
o(L^2).
}
\]

## 6. Dust

For pressureless matter,

\[
p=0.
\]

Then

\[
\boxed{
K_4
=
9\pi
+
\pi L^2
\left(
20\pi G\rho
-
\Lambda
\right)
+
o(L^2).
}
\]

## 7. Radiation

For a radiation fluid,

\[
p=\frac{\rho}{3},
\qquad
T=0.
\]

Then

\[
5\rho+3p
=
6\rho.
\]

Hence

\[
\boxed{
K_4
=
9\pi
+
\pi L^2
\left(
24\pi G\rho
-
\Lambda
\right)
+
o(L^2).
}
\]

## 8. Vacuum with cosmological constant

If

\[
T_{\mu\nu}=0,
\]

then

\[
R_{\mu\nu}
=
\Lambda g_{\mu\nu}.
\]

Therefore

\[
3R_{TT}-R
=
-\Lambda,
\]

and

\[
\boxed{
K_4
=
9\pi
-
\pi\Lambda L^2
+
o(L^2).
}
\]

Thus:

- positive de Sitter-type \(\Lambda\) lowers the local leading ambiguity coefficient at this order;
- negative AdS-type \(\Lambda\) raises it.

This statement concerns the coefficient within the declared arrow-erasure experiment, not a general notion of physical disorder.

## 9. Ricci-flat vacuum

For

\[
\Lambda=0,
\qquad
T_{\mu\nu}=0,
\]

\[
R_{\mu\nu}=0.
\]

Therefore

\[
\boxed{
K_4
=
9\pi
+
o(L^2).
}
\]

The first matter/Ricci response disappears and the next correction probes vacuum Weyl geometry at higher order.

## 10. Poisson sprinkling form

For a Poisson sprinkling of density \(\rho_{\rm spr}\), let

\[
\lambda
=
\rho_{\rm spr}V(D_L).
\]

The local \(3+1\) recovery failure is

\[
\boxed{
\Pr_{\rm fail}
\sim
\frac{
K_{4,g}(D_L)
}{
\lambda
}.
}
\]

Therefore, under Einstein's equation and a perfect fluid,

\[
\boxed{
\Pr_{\rm fail}
\sim
\frac{
9\pi
+
\pi L^2
[
4\pi G(5\rho+3p)-\Lambda
]
+
o(L^2)
}{
\rho_{\rm spr}V(D_L)
}.
}
\]

The matter density \(\rho\) and sprinkling density \(\rho_{\rm spr}\) are different physical quantities and should never be conflated.

## 11. Interpretation boundary

The result does **not** imply that matter "creates time" or that lower recovery error is physically preferable.

It says only that, within the declared stochastic information-loss experiment, the first curvature dependence of the leading reconstruction-error coefficient can be rewritten in terms of local stress-energy if Einstein's field equation is assumed.

This supplies a bridge from the purely Lorentzian theorem to familiar physical variables without changing the mathematical content.
