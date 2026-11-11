# Boundary-state asymmetry can select an effective arrow without creating time

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite calibration + literature boundary  
**Novelty status:** initial/boundary-condition explanations of arrows are classical; no project priority claim

## 1. Question

The current architecture contains a state/occupancy component

$$
\pi.
$$

The time-origin audit showed that \(\pi\) does not derive temporal order.

A narrower question remains legitimate:

> Can an asymmetric preparation \(\pi\) select a macroscopic direction of relaxation when the transition law itself respects the corresponding symmetry?

Yes.

This is a boundary-state or preparation mechanism for an **effective arrow**.

It is not an origin of time.

## 2. Exact reflection-symmetric Markov witness

Consider three states

$$
0,\;1,\;2
$$

and the stochastic matrix

$$
K=
\begin{pmatrix}
3/4&1/4&0\\
1/4&1/2&1/4\\
0&1/4&3/4
\end{pmatrix}.
$$

The matrix is symmetric,

$$
K=K^\top,
$$

doubly stochastic, and invariant under the reflection

$$
0\leftrightarrow2.
$$

Its stationary distribution is

$$
\pi_*=
\left(
\frac13,\frac13,\frac13
\right).
$$

The kernel itself does not prefer the left or right endpoint.

## 3. Two reflected preparations

Choose

$$
\pi_L=(1,0,0)
$$

and

$$
\pi_R=(0,0,1).
$$

They are exchanged by the same reflection symmetry that leaves \(K\) invariant.

Let the positional observable be

$$
x=(0,1,2).
$$

Initially,

$$
\langle x\rangle_L=0,
\qquad
\langle x\rangle_R=2.
$$

After one application of the same kernel,

$$
\pi_LK=
\left(
\frac34,\frac14,0
\right),
$$

and

$$
\pi_RK=
\left(
0,\frac14,\frac34
\right).
$$

Hence

$$
\langle x\rangle_{L,1}=\frac14,
$$

while

$$
\langle x\rangle_{R,1}=\frac74.
$$

The one-step drifts are

$$
\boxed{
\Delta\langle x\rangle_L=+\frac14,
\qquad
\Delta\langle x\rangle_R=-\frac14.
}
$$

The law is the same.

The preparation selects the sign.

## 4. Exact all-step relation

Define the centered observable

$$
m=x-1=(-1,0,1).
$$

It is an eigenmode of the kernel:

$$
\boxed{
Km^\top=\frac34m^\top.
}
$$

Therefore

$$
\boxed{
\langle m\rangle_{L,n}
=
-\left(\frac34\right)^n,
\qquad
\langle m\rangle_{R,n}
=
+\left(\frac34\right)^n.
}
$$

Equivalently,

$$
\boxed{
\langle x\rangle_{L,n}
=
1-\left(\frac34\right)^n,
}
$$

and

$$
\boxed{
\langle x\rangle_{R,n}
=
1+\left(\frac34\right)^n.
}
$$

The two relaxation histories are exact mirror images.

No asymmetry in \(K\) selects which one is physically prepared.

## 5. What the witness proves

It proves a modest structural statement:

$$
\boxed{
\text{symmetric law}+\text{asymmetric state}
\Longrightarrow
\text{asymmetric observed relaxation}.
}
$$

The sign of the relaxation trajectory can therefore be carried by \(\pi\), even when \(K\) respects the relevant reflection symmetry.

This is the same general logical pattern emphasized by boundary-condition approaches to thermodynamic arrows.

## 6. What the witness does not prove

The iteration index

$$
n=0,1,2,\ldots
$$

is already supplied.

The kernel is already interpreted as an update law.

Therefore the witness does not derive:

- temporal succession;
- before/after order;
- duration;
- microscopic time reversal;
- the cosmological thermodynamic arrow.

It concerns selection of an observable direction **inside an already temporal/dynamical description**.

## 7. Reversible Markov is not microscopic time-reversal invariance

The kernel satisfies detailed-balance-type reversibility with respect to the uniform stationary distribution.

That is a Markov-chain notion of reversibility.

It should not be conflated with a fundamental invertible time-reversal-symmetric Hamiltonian law.

A stochastic relaxation kernel generally loses information and its inverse need not be stochastic.

Therefore this finite witness is used only to demonstrate symmetry selection by the initial occupancy.

The stronger cosmological arrow question must be compared with statistical-mechanical boundary-condition literature.

## 8. Past Hypothesis benchmark

A major family of explanations for the thermodynamic arrow starts from approximately time-reversal-symmetric microscopic laws and locates the asymmetry in a special low-entropy boundary condition.

In this language, the **Past Hypothesis** restricts the universe to a special low-entropy macroregion at one temporal boundary.

The basic lesson relevant here is not that the Past Hypothesis has been proven necessary.

It is:

$$
\boxed{
\text{an asymmetric state/boundary condition can carry an arrow not selected by a symmetric law alone}.
}
$$

This is a classical idea.

## 9. The boundary explanation is not unique

The literature also contains models that aim to obtain thermodynamic arrows without imposing the conventional low-entropy Past Hypothesis.

For example, reversible models with unbounded expansion can generate entropy-growth structure in both directions away from a special region or through dynamical expansion mechanisms.

Therefore the repository must not elevate

$$
\pi_{\rm special}
$$

into a universal explanation of the arrow.

It is one logically coherent route among others.

## 10. Quantum boundary-condition benchmark

Recent work on the **Entanglement Past Hypothesis** asks whether a low-entanglement initial quantum state can ground the decoherent arrow when unitary Schrödinger dynamics itself allows recoherence.

This is another example of the same architecture:

- symmetric/reversible dynamical law;
- special boundary-state information;
- asymmetric effective behavior.

It also highlights that different arrows—thermodynamic and decoherent—need not be identical.

## 11. Relation to A21

A21 proved that a fully equivariant endogenous evolution cannot distinguish symmetry-related latent models when its state and randomness carry no additional non-invariant information.

The present witness gives the complementary case.

The initial occupancy itself is not invariant under reflection:

$$
\pi_R=\mathcal R_*\pi_L,
\qquad
\pi_L\neq\pi_R.
$$

Thus the preparation supplies the missing symmetry-breaking information.

There is no contradiction with A21.

The asymmetry did not arise endogenously from the symmetric law.

It was present in the boundary state.

## 12. Relation to the current architecture

This sharpens the role of \(\pi\).

### What \(\pi\) can do

- select a symmetry sector;
- encode preparation/history information;
- change transient currents and coarse-grained behavior;
- select the sign of some macroscopic relaxation observables.

### What \(\pi\) does not currently do

- derive the temporal parameter;
- define causal precedence;
- provide duration;
- explain why one boundary condition rather than its reflected alternative is realized.

Therefore

$$
\boxed{
\pi\text{ can carry arrow information without being time}.
}
$$

## 13. Comparison with q and cycle circulation

The recent audits now separate three distinct sources of asymmetry.

### State potential q

Can distinguish states and supply cardinal structure.

Not a temporal rank.

### Cycle circulation

Can encode gauge-invariant chirality/non-equilibrium driving.

Not a vertex precedence relation.

### Boundary occupancy \(\pi\)

Can select one relaxation sector under a symmetric law.

Not an origin of temporal succession.

These mechanisms should remain distinct.

## 14. Exact computational regression

The repository includes a Fraction-based exact audit.

For

$$
n=0,\ldots,12,
$$

it computes the two reflected trajectories exactly and verifies

$$
\pi_RK^n
=
\mathcal R_*(\pi_LK^n),
$$

together with

$$
\langle x\rangle_{L,n}
=
1-(3/4)^n
$$

and

$$
\langle x\rangle_{R,n}
=
1+(3/4)^n.
$$

No floating-point tolerance is used.

## 15. Current verdict

**Can \(\pi\) break a symmetry of an otherwise symmetric transition law?**  
YES.

**Can \(\pi\) select an effective relaxation direction?**  
YES, preparation-dependently.

**Does this derive physical time?**  
NO.

**Does it prove the Past Hypothesis?**  
NO.

**Does it provide a clean architectural role for boundary-state asymmetry?**  
YES.

## 16. Revised foundational picture

The current programme should distinguish at least:

$$
\boxed{
\text{law asymmetry}
}
$$

from

$$
\boxed{
\text{state/boundary asymmetry}
}
$$

from

$$
\boxed{
\text{loop/chiral asymmetry}
}
$$

from

$$
\boxed{
\text{temporal order and duration}.
}
$$

The next pregeometric problem is not to collapse these categories into one “time field.”

It is to determine which asymmetric structures, if any, can be defined non-temporally and then shown to recover ordinary causal/temporal physics in a controlled regime.
