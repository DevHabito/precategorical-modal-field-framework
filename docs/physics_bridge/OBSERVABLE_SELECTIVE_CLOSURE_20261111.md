# Observable-selective exact closure in the multi-electron birth-death model

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact analytic bridge result + constructive counterexample  
**Novelty status:** generating-function and moment-hierarchy mechanisms are classical; project-specific comparison not certified as novel

## 1. Question

The multi-electron dot model provides an unusually clean test of a methodological question already present in the repository:

> Is the most intuitive macroscopic summary also the dynamically closed one?

For this model, the answer is no.

The mean electron number is not an autonomous state over unrestricted distributions, while one physically selected exponential transform is exactly autonomous.

## 2. Published generator

Write

$$
D=\Gamma_0e^{-\beta E_{\rm C}},
\qquad
c=2\beta E_{\rm C}>0.
$$

The birth-death generator is

$$
(\mathcal L_t f)(N)
=
\Gamma^+(t)[f(N+1)-f(N)]
+
De^{cN}[f(N-1)-f(N)].
$$

## 3. The mean is not exactly closed

Choose

$$
f(N)=N.
$$

Then

$$
f(N+1)-f(N)=1,
$$

and

$$
f(N-1)-f(N)=-1.
$$

Therefore

$$
\mathcal L_tN
=
\Gamma^+(t)-De^{cN}.
$$

Taking expectation gives

$$
\boxed{
\frac{d}{dt}\langle N\rangle
=
\Gamma^+(t)-DG_{-c},
}
$$

where

$$
G_{-c}
=
\left\langle e^{cN}\right\rangle.
$$

Thus the mean does not determine its own derivative on the unrestricted distribution class.

## 4. Exact three-state witness

Consider the two probability distributions on

$$
N\in\{0,1,2\}:
$$

$$
p^{(A)}=(0,1,0),
$$

and

$$
p^{(B)}
=
\left(
\frac12,0,\frac12
\right).
$$

Both have

$$
\langle N\rangle=1.
$$

But

$$
G_{-c}^{(A)}=e^c,
$$

while

$$
G_{-c}^{(B)}
=
\frac{1+e^{2c}}2.
$$

Their difference is

$$
G_{-c}^{(B)}-G_{-c}^{(A)}
=
\frac{(e^c-1)^2}{2}>0.
$$

Under the same instantaneous drive,

$$
\boxed{
\dot{\langle N\rangle}_{B}
-
\dot{\langle N\rangle}_{A}
=
-\frac{D}{2}(e^c-1)^2
<0.
}
$$

Equal mean therefore does not imply equal next mean derivative.

This is an exact physical-model non-closure statement. It does not rely on the repository's C2 update law.

## 5. The tuned exponential observable closes exactly

Now choose

$$
f_c(N)=e^{-cN}.
$$

The generator action is

$$
\mathcal L_t f_c
=
\Gamma^+(t)(e^{-c}-1)f_c
+
D(e^c-1).
$$

Taking expectation gives

$$
\boxed{
\dot G_c
=
-\Gamma^+(t)(1-e^{-c})G_c
+
D(e^c-1).
}
$$

This is a closed scalar equation for arbitrary distributions satisfying the transform assumptions.

No Gaussian approximation and no moment closure are required.

## 6. Closed equation for the repository-style score

Define

$$
Q_c
=
-\frac1c\log G_c.
$$

Because

$$
G_c=e^{-cQ_c},
$$

the scalar transform equation gives

$$
\boxed{
\dot Q_c
=
\frac{\Gamma^+(t)(1-e^{-c})}{c}
-
\frac{D(e^c-1)}{c}e^{cQ_c}.
}
$$

Since

$$
D=\Gamma_0e^{-c/2},
$$

this can also be written as

$$
\boxed{
\dot Q_c
=
\frac{\Gamma^+(t)(1-e^{-c})}{c}
-
\frac{2\Gamma_0\sinh(c/2)}{c}
e^{cQ_c}.
}
$$

Thus the log-transform score itself is an exact one-dimensional dynamical state at the physically selected transform parameter \(c\).

## 7. Constant-rate solution and relaxation

If

$$
\Gamma^+(t)=\Gamma^+
$$

is constant, define

$$
a_c=\Gamma^+(1-e^{-c})>0.
$$

Then

$$
G_c(t)
=
G_c^{\rm ss}
+
[G_c(0)-G_c^{\rm ss}]e^{-a_ct},
$$

with

$$
G_c^{\rm ss}
=
e^{c/2}\frac{\Gamma_0}{\Gamma^+}.
$$

The exact relaxation rate of this transform is

$$
\boxed{
a_c=\Gamma^+(1-e^{-c}).
}
$$

The corresponding stationary score is

$$
Q_c^{\rm ss}
=
\frac1c\log\left(\frac{\Gamma^+}{\Gamma_0}\right)-\frac12
=
\langle N\rangle_{\rm ss}-\frac12.
$$

## 8. Why this matters for coarse-graining

The model gives a direct comparison:

### Intuitive coordinate

$$
\langle N\rangle
$$

has a derivative requiring

$$
G_{-c}.
$$

### Dynamically matched coordinate

$$
G_c
\quad\text{or}\quad
Q_c
$$

has an exact scalar evolution law.

Therefore the dynamic quality of a coarse variable depends on how the observable interacts with the generator.

A variable is not privileged merely because it is simple to interpret.

This is a concrete physical realization of the repository's broader principle:

$$
\boxed{
\text{coarse-graining is observable- and dynamics-relative.}
}
$$

## 9. Connection with the published transient analysis

The 2026 article reports that, during the transient from equilibrium to the nonequilibrium steady state:

- the mean electron number changes;
- the variance first increases and later decreases;
- skewness and kurtosis deviate from their stationary Gaussian values;
- the stationary distribution returns to a Gaussian form.

The paper also derives an approximate/simplified transient expression for the mean within its physical analysis.

The exact identity above does not contradict that treatment.

It says that, over the unrestricted distribution class governed by the master equation, the mean derivative depends on an additional exponential moment. Any closed mean law therefore uses additional structure supplied by the physical solution family or approximation.

By contrast, \(G_c\) closes directly at the generator level.

## 10. A stationary deviation diagnostic

Define

$$
\Delta_c(t)
=
Q_c(t)-\langle N\rangle_t+\frac12.
$$

For the stationary discrete-Gaussian family obtained in the paper's averaged-rate approximation,

$$
\boxed{
\Delta_c^{\rm ss}=0.
}
$$

For a general distribution, the cumulant expansion gives formally

$$
Q_c
=
\kappa_1
-\frac c2\kappa_2
+\frac{c^2}{6}\kappa_3
-\frac{c^3}{24}\kappa_4+\cdots.
$$

Hence

$$
\Delta_c
=
\frac12
-\frac c2\kappa_2
+\frac{c^2}{6}\kappa_3
-\frac{c^3}{24}\kappa_4+\cdots.
$$

The transient experiment reports changes in variance, skewness, and kurtosis, so \(\Delta_c(t)\) is a natural secondary diagnostic of departure from the stationary family.

This proposed diagnostic is not yet tested because the raw time-resolved distributions are not publicly available.

## 11. Exact Jensen bound

For \(c>0\), convexity of the exponential gives

$$
G_c
=
\mathbb E[e^{-cN}]
\ge
e^{-c\mathbb E[N]}.
$$

Therefore

$$
\boxed{
Q_c\le\langle N\rangle.
}
$$

Equivalently,

$$
\Delta_c\le\frac12.
$$

This bound is distribution-independent whenever the expectation exists.

## 12. Scientific boundary

The result establishes neither a new thermodynamic law nor empirical superiority of \(Q_c\).

It establishes an exact structural fact for the published master equation:

> the conventional mean is generically non-autonomous on unrestricted distributions, while the transform selected by the exponential rate scale is exactly autonomous.

Whether this observable is experimentally useful must be tested against the measured \(\rho_N(t)\) data.

No pregeometric or spacetime interpretation is inferred.


## 13. Exact generator eigenfunction under the constant-rate coarse-grained model

Under the time-averaged model used in the paper's coarse-grained transient analysis, let

$$
\Gamma^+(t)=\Gamma^+
$$

be constant.

The scalar transform equation is

$$
\dot G_c
=
-a_cG_c+b_c,
$$

where

$$
a_c=\Gamma^+(1-e^{-c}),
$$

and

$$
b_c=D(e^c-1).
$$

Define

$$
G_c^{\rm ss}=\frac{b_c}{a_c}.
$$

At the observable level define

$$
h_c(N)=e^{-cN}-G_c^{\rm ss}.
$$

Because the generator annihilates constants,

$$
\boxed{
\mathcal L h_c=-a_c h_c.
}
$$

Thus \(h_c\) is an exact eigenfunction of the backward generator with eigenvalue

$$
\boxed{
-a_c=-\Gamma^+(1-e^{-c}).
}
$$

Consequently,

$$
\boxed{
G_c(t)-G_c^{\rm ss}
=
[G_c(0)-G_c^{\rm ss}]
e^{-a_ct}.
}
$$

The relaxation rate is determined entirely by the published model parameters.

## 14. Comparison with the mean relaxation scale

The paper's simplified mean transient contains the exponential scale

$$
c\Gamma^+.
$$

The exact \(G_c\) relaxation rate is instead

$$
a_c=\Gamma^+(1-e^{-c}).
$$

For every \(c>0\),

$$
1-e^{-c}<c,
$$

so

$$
\boxed{
a_c<c\Gamma^+.
}
$$

The two observables therefore need not relax at the same rate even though their stationary values are algebraically related through

$$
Q_c^{\rm ss}
=
\langle N\rangle_{\rm ss}-\frac12.
$$

For small \(c\),

$$
1-e^{-c}
=
c-\frac{c^2}{2}+O(c^3),
$$

so the relaxation scales approach one another in the weak-charging/high-temperature limit.

This is another concrete example of why static equivalence does not imply dynamical equivalence.

## 15. Experimental signature

If the constant-rate approximation used for the transient model is adequate, then the quantity

$$
\log
\left|
G_c(t)-G_c^{\rm ss}
\right|
$$

must be linear in time wherever the difference is nonzero, with predetermined slope

$$
\boxed{
-\Gamma^+(1-e^{-c}).
}
$$

The slope is not to be fitted as a free closure parameter.

This signature has been added to the pre-registered data protocol.


## 16. Phase-conditioned scope correction

The scalar equation

$$
\dot G_c
=
-\Gamma^+(t)(1-e^{-c})G_c
+
D(e^c-1)
$$

is exact for a distribution evolving under a specified drive history.

The experiment randomizes the ac phase between repetitions. Therefore, for the phase-averaged observable

$$
\bar G_c
=
\mathbb E_\phi[G_{c,\phi}],
$$

the exact equation becomes

$$
\dot{\bar G}_c
=
-(1-e^{-c})\bar\Gamma\,\bar G_c
+
D(e^c-1)
-
(1-e^{-c})
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{c,\phi}).
$$

The correct scopes are therefore:

- exact scalar autonomy for a known deterministic drive history or fixed phase;
- no generic scalar autonomy after random-phase marginalization;
- constant averaged-rate dynamics only as the coarse-grained approximation used in the paper.

This correction changes the empirical protocol, not the fixed-phase generator identity.
