# Bridge 1B — transform non-closure in a published multi-electron dot model

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact analytic bridge theorem + exact finite witness  
**Physical source:** published multi-electron Markov model; no empirical validation claim  
**Novelty status:** not assessed; the moment-shift mechanism is mathematically elementary and must not be advertised as new physics

## 1. Why this bridge is different from C2

The repository's mathematical claim C2 studies non-closure under a centered contraction of quantitative marks.

The multi-electron dot studied by C. Salhani, K. Chida, T. Shimizu, T. Hayashi, and K. Nishiguchi evolves differently. Its measured state distribution follows a birth-death master equation.

I therefore do **not** identify the published dynamics with C2.

Instead, I ask a new and narrower bridge question:

> Does the actual published master equation close on one exponential score, or does its evolution require additional transform information?

This question is derived from the physical model itself.

## 2. Published master equation

Let \(N\in\mathbb Z\) be the excess electron number in the dot and let \(\rho_N(t)\) be its probability.

The published model is

$$
\dot\rho_N(t)
=
\Gamma^+(t)\rho_{N-1}(t)
-
[\Gamma^+(t)+\Gamma_N^-]\rho_N(t)
+
\Gamma_{N+1}^-\rho_{N+1}(t).
$$

The rates are

$$
\Gamma^+(t)
=
\Gamma_0 e^{-\beta eV(t)}
$$

and

$$
\Gamma_N^-
=
\Gamma_0 e^{\beta\mu_N},
\qquad
\mu_N=2E_{\rm C}\left(N-\frac12\right).
$$

Define

$$
c=2\beta E_{\rm C}>0.
$$

Then

$$
\Gamma_N^-
=
\Gamma_0 e^{-\beta E_{\rm C}}e^{cN}.
$$

The experiment reports \(E_{\rm C}=9.8\) meV and operates at room temperature with time-resolved single-electron counting. The present theorem uses only the stated master equation and rate law.

## 3. Exponential transform

For a parameter \(\lambda\), define

$$
G_\lambda(t)
=
\sum_N \rho_N(t)e^{-\lambda N},
$$

whenever the sum is finite.

The corresponding log-transform score is

$$
Q_\lambda(t)
=
-\frac1\lambda\log G_\lambda(t)
$$

for \(\lambda\neq0\).

This is the same mathematical family of exponential scores studied elsewhere in the repository, but the dynamics below are derived from the published electronic model rather than imported from C2.

## 4. Exact transform evolution identity

Apply the birth-death generator to

$$
f_\lambda(N)=e^{-\lambda N}.
$$

A birth event \(N\to N+1\) changes \(f_\lambda\) by

$$
f_\lambda(N+1)-f_\lambda(N)
=
e^{-\lambda N}(e^{-\lambda}-1).
$$

A death event \(N\to N-1\) changes it by

$$
f_\lambda(N-1)-f_\lambda(N)
=
e^{-\lambda N}(e^\lambda-1).
$$

Therefore

$$
\dot G_\lambda
=
\Gamma^+(t)(e^{-\lambda}-1)G_\lambda
+
(e^\lambda-1)
\sum_N \rho_N\Gamma_N^-e^{-\lambda N}.
$$

Using

$$
\Gamma_N^-
=
\Gamma_0e^{-\beta E_{\rm C}}e^{cN},
$$

the second sum becomes

$$
\Gamma_0e^{-\beta E_{\rm C}}
\sum_N\rho_Ne^{-(\lambda-c)N}.
$$

Hence

$$
\boxed{
\dot G_\lambda
=
\Gamma^+(t)(e^{-\lambda}-1)G_\lambda
+
\Gamma_0e^{-\beta E_{\rm C}}(e^\lambda-1)
G_{\lambda-c}.
}
$$

This identity is exact under the published master equation.

### Immediate consequence

The evolution of one transform value \(G_\lambda\) is generically coupled to a second transform value \(G_{\lambda-c}\).

Thus one fixed transform does not form an autonomous scalar state unless an additional relation closes the shifted transform.

## 5. Score evolution

For \(\lambda\neq0\),

$$
\dot Q_\lambda
=
-\frac1\lambda\frac{\dot G_\lambda}{G_\lambda}.
$$

Therefore

$$
\boxed{
\dot Q_\lambda
=
-\frac1\lambda
\left[
\Gamma^+(t)(e^{-\lambda}-1)
+
\Gamma_0e^{-\beta E_{\rm C}}(e^\lambda-1)
\frac{G_{\lambda-c}}{G_\lambda}
\right].
}
$$

One score \(Q_\lambda\) is not enough to evaluate this derivative unless the ratio \(G_{\lambda-c}/G_\lambda\) is known from other information.

## 6. Exact four-state non-closure witness

The preceding identity says that the shifted transform matters. I now show that normalization, mean electron number, and one transform value do not generally determine that shifted transform.

Let

$$
z=e^{-\lambda},
\qquad
y=e^{-(\lambda-c)}.
$$

Consider distributions supported on

$$
N\in\{0,1,2,3\}.
$$

Define the perturbation vector

$$
v=(-z,\;2z+1,\;-z-2,\;1).
$$

It satisfies

$$
\sum_{n=0}^3v_n=0,
$$

$$
\sum_{n=0}^3nv_n=0,
$$

and

$$
\sum_{n=0}^3v_nz^n=0.
$$

Therefore, starting from any strictly positive interior distribution \(p\), sufficiently small perturbations

$$
p^\pm=p\pm\varepsilon v
$$

have the same:

- total probability;
- mean electron number;
- transform \(G_\lambda\).

But at the shifted transform,

$$
\sum_{n=0}^3v_ny^n
=
(y-1)^2(y-z).
$$

Thus, whenever

$$
y\neq1
\quad\text{and}\quad
y\neq z,
$$

the two distributions have different \(G_{\lambda-c}\).

In physical parameters these exclusions are

$$
c\neq0
$$

and

$$
\lambda\neq c.
$$

The model has \(c=2\beta E_{\rm C}>0\), so the only exceptional transform parameter in this statement is \(\lambda=c\).

### Theorem

For the published multi-electron birth-death model, if

$$
c>0,\qquad \lambda\neq0,\qquad \lambda\neq c,
$$

there exist finite-support probability distributions with equal mean electron number and equal \(Q_\lambda\) but different instantaneous \(\dot Q_\lambda\) under the same instantaneous external drive.

The proof is constructive: use the four-state perturbation above and the exact transform-evolution identity.

## 7. Concrete rational witness

For an exact arithmetic audit, choose

$$
z=\frac12,
\qquad
y=\frac34.
$$

This corresponds algebraically to one transform point and one shifted transform point; it is used only as an exact finite witness, not as a fit to the experimental \(E_{\rm C}/k_{\rm B}T\).

Take

$$
p^+
=
\left(
\frac9{40},
\frac7{20},
\frac18,
\frac3{10}
\right),
$$

and

$$
p^-
=
\left(
\frac{11}{40},
\frac3{20},
\frac38,
\frac15
\right).
$$

Both have mean

$$
\frac32
$$

and both satisfy

$$
G_z=\frac{15}{32}.
$$

At the shifted point,

$$
G_y(p^+)=\frac{219}{320},
$$

while

$$
G_y(p^-)=\frac{437}{640}.
$$

Their exact difference is

$$
\frac1{640}.
$$

Therefore the physical transform derivative differs whenever the coefficient multiplying \(G_{\lambda-c}\) is nonzero.

## 8. What this says about the repository

This is the first bridge in which the repository's general concern about dynamic closure meets a published physical master equation without identifying that equation with the earlier C2 update.

The result is narrower and cleaner:

> A physically established birth-death model generates its own transform hierarchy. One exponential score at one parameter is not generically dynamically autonomous.

This does not prove C2 physically. It shows that a related non-closure issue arises independently in a real stochastic-thermodynamic model.

## 9. What it does not say

This result does not establish:

- a new law of stochastic thermodynamics;
- that the transform hierarchy is absent from existing birth-death literature;
- that \(Q_\lambda\) is the best physical macrostate;
- that the experiment itself prepared the four-state witness distributions;
- that the four-state rational witness uses the experiment's numerical parameters;
- that C2 has been experimentally validated;
- any spacetime or pregeometric consequence.

## 10. Empirical route

The paper reports time-resolved distributions \(\rho_N(t)\), transition rates, a charging energy \(E_{\rm C}=9.8\) meV, a baseline rate \(\Gamma_0=0.1\) Hz, and a driven multi-state nonequilibrium protocol.

A genuine empirical closure test would require the underlying time-series distributions or raw electron-count trajectories.

The protocol should then be frozen before the final comparison:

1. choose \(\lambda\);
2. compute \(G_\lambda(t)\) and \(G_{\lambda-c}(t)\);
3. estimate \(\dot G_\lambda(t)\) from held-out time points;
4. compare a one-score predictor against the exact two-transform identity;
5. quantify whether adding \(G_{\lambda-c}\) improves out-of-sample prediction by the amount required by the master equation.

Until raw or sufficiently tabulated data are recovered, the present result remains an analytic bridge theorem grounded in the published physical model, not an experimental validation.

## 11. Literature boundary

The master equation, transition-rate law, stochastic-thermodynamic interpretation, and nonequilibrium heat decomposition belong to the published work of Salhani et al. and to established stochastic thermodynamics.

The four-state witness and the use of the exact transform shift as a repository bridge are recorded here as a project derivation.

No priority claim is made until a targeted literature review of generating-function closure for birth-death processes is completed.
