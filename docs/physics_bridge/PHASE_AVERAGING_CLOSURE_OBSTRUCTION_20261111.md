# Phase averaging creates an exact closure obstruction

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact analytic correction to Bridge 1B  
**Physical source:** the randomized-phase protocol and master equation reported by Salhani et al.  
**Novelty status:** model-specific derivation; coarse-graining/correlation mechanisms are classical; priority not certified

## 1. Why this correction is necessary

The experiment randomizes the ac phase \(\phi\) between repeated measurements and reports phase-averaged observables.

For a fixed phase, the published entry rate is

$$
\Gamma_\phi^+(t)
=
\Gamma_0
\exp[-A\sin(\omega t+\phi)],
\qquad
A=\beta eS_{\rm AC}.
$$

For each fixed phase realization, the transform

$$
G_{c,\phi}(t)
=
\sum_N
\rho_N(t\mid\phi)e^{-cN},
\qquad
c=2\beta E_{\rm C},
$$

satisfies the exact scalar equation

$$
\boxed{
\dot G_{c,\phi}
=
-(1-q)\Gamma_\phi^+(t)G_{c,\phi}
+b,
}
$$

where

$$
q=e^{-c},
\qquad
b=D(q^{-1}-1),
\qquad
D=\Gamma_0e^{-c/2}.
$$

However, the experiment does not directly publish \(G_{c,\phi}\) for each phase. It averages over \(\phi\).

That averaging changes the closure question.

## 2. Exact phase-averaged equation

Define

$$
\bar G_c(t)
=
\mathbb E_\phi[G_{c,\phi}(t)]
$$

and

$$
\bar\Gamma(t)
=
\mathbb E_\phi[\Gamma_\phi^+(t)].
$$

Averaging the exact conditioned equation gives

$$
\dot{\bar G}_c
=
-(1-q)
\mathbb E_\phi[\Gamma_\phi^+G_{c,\phi}]
+b.
$$

Using

$$
\mathbb E[\Gamma G]
=
\bar\Gamma\,\bar G
+
\operatorname{Cov}(\Gamma,G),
$$

the exact coarse equation is

$$
\boxed{
\dot{\bar G}_c
=
-(1-q)\bar\Gamma\,\bar G_c
+b
-(1-q)
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{c,\phi}).
}
$$

The phase-averaged transform is therefore not generically scalar-autonomous.

The missing quantity is a phase-rate/transform correlation created by the hidden phase variable.

## 3. The published averaged-rate approximation

For uniformly distributed phase,

$$
\bar\Gamma
=
\Gamma_0 I_0(A),
$$

which is independent of time.

The paper uses the approximation

$$
\Gamma^+(t)
\approx
\bar\Gamma
$$

as a coarse-grained description over the drive period.

Applying that approximation to the transform equation amounts to neglecting the correlation term

$$
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{c,\phi}).
$$

This may be accurate in the regime studied experimentally, but it is not an exact consequence of phase averaging.

## 4. Exact short-time obstruction

Assume the ac drive is switched on from a common initial distribution, so that

$$
G_{c,\phi}(0)=G_0
$$

for every phase.

Then

$$
\operatorname{Cov}_\phi
(\Gamma_\phi^+(0),G_{c,\phi}(0))
=
0.
$$

Therefore the exact phase-averaged equation and the averaged-rate approximation agree in first derivative:

$$
\dot{\bar G}_c(0)
=
-(1-q)\bar\Gamma G_0+b.
$$

This agreement is only first order.

Differentiate the phase-conditioned equation once more:

$$
\ddot G_{c,\phi}
=
-(1-q)\dot\Gamma_\phi^+G_{c,\phi}
-(1-q)\Gamma_\phi^+\dot G_{c,\phi}.
$$

At \(t=0\), uniform phase implies

$$
\mathbb E_\phi[\dot\Gamma_\phi^+(0)]=0.
$$

Hence

$$
\ddot{\bar G}_c(0)
=
(1-q)^2
G_0
\mathbb E_\phi[(\Gamma_\phi^+)^2]
-
(1-q)b\bar\Gamma.
$$

The constant averaged-rate model would instead give

$$
\ddot G_c^{\rm av}(0)
=
(1-q)^2
G_0\bar\Gamma^2
-
(1-q)b\bar\Gamma.
$$

Subtracting,

$$
\boxed{
\ddot{\bar G}_c(0)
-
\ddot G_c^{\rm av}(0)
=
(1-q)^2G_0
\operatorname{Var}_\phi(\Gamma_\phi^+).
}
$$

For the sinusoidal drive,

$$
\mathbb E_\phi[(\Gamma_\phi^+)^2]
=
\Gamma_0^2I_0(2A),
$$

so

$$
\boxed{
\operatorname{Var}_\phi(\Gamma_\phi^+)
=
\Gamma_0^2
\left[
I_0(2A)-I_0(A)^2
\right].
}
$$

For nonzero drive amplitude this variance is strictly positive.

Therefore the phase-averaged constant-rate approximation generically separates from the exact phase-averaged transform already at second order in time.

## 5. Correlation is generated immediately

The covariance itself starts from zero but does not remain zero.

With the common initial condition,

$$
\left.
\frac{d}{dt}
\operatorname{Cov}_\phi
(\Gamma_\phi^+,G_{c,\phi})
\right|_{t=0}
=
-(1-q)G_0
\operatorname{Var}_\phi(\Gamma_\phi^+).
$$

Thus a nontrivial drive immediately generates the hidden correlation required by the exact coarse equation.

This is an explicit example of a closure variable being created by coarse-graining over an unobserved or discarded coordinate.

## 6. Consequence for the empirical protocol

There are now two distinct tests.

### Exact conditioned test

If the raw data retain the applied phase \(\phi\), bin or condition the trajectories by phase and test

$$
\dot G_{c,\phi}
=
-(1-q)\Gamma_\phi^+G_{c,\phi}+b.
$$

This is the exact closure test.

### Phase-averaged test

If only the published phase-averaged distribution is available, the exact scalar closure is **not** the correct null model.

The exact equation contains

$$
\operatorname{Cov}_\phi(\Gamma_\phi^+,G_{c,\phi}).
$$

A comparison with the constant-rate equation using

$$
\bar\Gamma=\Gamma_0I_0(A)
$$

tests the paper's coarse-grained approximation, not exact scalar closure.

These two evidence classes must not be mixed.

## 7. Relation to the repository's broader question

This correction is more informative than the original overstrong protocol.

At the phase-conditioned level, the transform \(G_c\) is an exact scalar coordinate.

After eliminating the phase, the same observable loses exact scalar autonomy because the coarse-grained dynamics needs a correlation with the discarded variable.

Symbolically,

$$
\boxed{
\text{exact micro/conditioned closure}
\not\Rightarrow
\text{exact closure after averaging}.
}
$$

This is a direct physical example of the repository's general concern that coarse-graining can create additional informational requirements.

## 8. Scientific boundary

This result does not show that the phase covariance is a new thermodynamic state variable.

It is a standard correlation generated by marginalization over phase.

The project-specific contribution is the explicit derivation of its role in the selected transform closure and the correction of the empirical protocol.

No physical validation is claimed until phase-resolved or appropriately joint data are analyzed.
