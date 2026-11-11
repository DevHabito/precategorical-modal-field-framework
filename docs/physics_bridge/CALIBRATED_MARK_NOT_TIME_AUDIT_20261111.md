# Calibrated quantitative marks are not temporal ranks

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** physical-boundary audit using the existing reversible Markov and single-electron-box bridges  
**Novelty status:** detailed balance, reversible transitions, and cycle affinities are classical

## 1. Purpose

The symmetry-breaking audits show that an additional quantitative mark can distinguish structures that relation/order data alone cannot.

That fact must not be promoted into:

> a calibrated quantitative mark is a time coordinate.

The existing physical bridges already provide direct counterexamples to that shortcut.

## 2. Reversible three-state pilot

The Markov thermal pilot uses

$$
q=(0,1,2)
$$

and rates

$$
W=
\begin{pmatrix}
0&4&1\\
8&0&3\\
4&6&0
\end{pmatrix}.
$$

With

$$
\beta=\log2,
$$

the exact ratios satisfy

$$
\frac{W_{ij}}{W_{ji}}
=
e^{-\beta(q_j-q_i)}.
$$

Thus the q-differences are physically encoded in the reversible rate ratios up to an additive zero.

The mark is not merely an arbitrary label inside this model.

## 3. q is not monotone along physical transitions

Both directions of every state pair have positive rates.

For example,

$$
W_{01}=4>0
$$

allows

$$
0\to1,
$$

which increases q:

$$
0\to1.
$$

But

$$
W_{10}=8>0
$$

also allows

$$
1\to0,
$$

which decreases q:

$$
1\to0.
$$

Therefore there is no rule

$$
\text{physical transition}
\Longrightarrow
q_{\rm next}>q_{\rm current}.
$$

The calibrated q is a state potential, not a strict temporal rank.

The same argument applies to the other reversible pairs.

## 4. Detailed balance permits ongoing microscopic change

The stationary distribution is

$$
\pi^{\rm eq}
=
\left(
\frac47,\frac27,\frac17
\right),
$$

and satisfies

$$
\pi_iW_{ij}=\pi_jW_{ji}.
$$

Microscopic transitions continue in both directions.

The absence of net stationary current does not mean absence of dynamical events.

Therefore:

$$
\boxed{
\text{reversible change}
\neq
\text{monotone motion along }q.
}
$$

This is precisely why a potential coordinate and a temporal parameter must be separated.

## 5. Scalar-potential consistency

In the reversible model, q differences reconstructed along different paths are consistent.

Around the three-state cycle,

$$
W_{01}W_{12}W_{20}
=
W_{10}W_{21}W_{02}
=
48.
$$

Equivalently, the cycle affinity vanishes.

Thus the edge force is integrable into a scalar state potential.

## 6. Nonequilibrium modification

Change only

$$
W_{02}:1\to2.
$$

Then

$$
W_{01}W_{12}W_{20}
=
48,
$$

while

$$
W_{10}W_{21}W_{02}
=
96.
$$

The cycle consistency condition fails.

The path

$$
0\to1\to2
$$

and the direct pair

$$
0\leftrightarrow2
$$

no longer imply one common scalar potential difference.

The missing information is cyclic/non-integrable.

This is exactly the structural distinction isolated by the q-cycle audit.

## 7. What changes when detailed balance is broken

In the reversible sector:

$$
\text{edge asymmetry}
=
\text{gradient of a scalar potential}
$$

up to the declared thermodynamic scaling.

In the driven/nonreversible sector:

$$
\text{edge asymmetry}
=
\text{potential-like part}
+
\text{cycle driving}.
$$

The latter cannot be compressed into one scalar state function.

This is standard stochastic thermodynamics.

Its value to the repository is to show where q ceases to be a complete representation.

## 8. Why cycle affinity is not time either

A nonzero cycle affinity provides an orientation-sensitive measure of nonequilibrium driving.

It can support:

- net currents;
- entropy production;
- irreversible statistical asymmetry.

But it does not supply a complete temporal coordinate.

A system can traverse many events while the affinity is constant.

Different cycles can have different affinities.

An affinity has thermodynamic dimensions/meaning, not units of duration.

Therefore:

$$
\boxed{
\text{arrow/drive indicator}
\neq
\text{clock}.
}
$$

## 9. Single-electron-box calibration strengthens the distinction

Bridge 1A maps q to calibrated electrostatic energy:

$$
q_t(n)=\frac{U(n,n_g(t))}{E_c}.
$$

This is a genuine operational physical mark.

But the mark depends on the externally controlled gate protocol

$$
n_g(t).
$$

Using the explicit t-dependence of q to derive time would be circular.

Furthermore, electron transfers can exchange energy in either direction depending on state and protocol.

Thus even a physically calibrated energy coordinate is not automatically temporal order.

## 10. Consequence for the symmetry-breaking programme

The current hierarchy is now:

1. relation \(R\) alone may leave symmetry/identifiability classes;
2. independent q can add quantitative information;
3. q can break some structural symmetries;
4. a scalar q supplies potential-like asymmetry, not universal temporal progression;
5. nonzero cyclic asymmetry requires edge/cycle information beyond one scalar potential;
6. neither potential nor cycle affinity alone is a physical duration variable.

This prevents a common category error:

$$
\boxed{
\text{symmetry-breaking information}
\not\Rightarrow
\text{time}.
}
$$

## 11. Relation to the Page-Wootters benchmark

Page-Wootters showed from another direction that reversible relational evolution does not require a globally monotone energy or entropy coordinate.

The Markov pilot now gives a classical stochastic analogue:

a scalar potential can be operationally real while the dynamics repeatedly moves both up and down that potential.

Together these benchmarks reject any attempt to identify one monotonic quantitative mark as the universal content of time.

## 12. Current conclusion

A physically calibrated q can be important.

It may encode:

- energy;
- cost;
- relative potential;
- preference;
- another cardinal mark.

Its physical meaning must be established case by case.

The project currently has no evidence that q itself is time, duration, or universal temporal orientation.

In the reversible pilot q behaves as a potential.

Outside the reversible sector the missing directional information moves into cycles/edges rather than becoming a better clock.
