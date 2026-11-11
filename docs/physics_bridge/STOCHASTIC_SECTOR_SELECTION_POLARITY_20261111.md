# Symmetric stochastic sector selection — realization polarity without ensemble polarity

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact finite symmetry audit + classical spontaneous-symmetry-breaking boundary  
**Novelty status:** symmetry-preserving ensemble dynamics and sector selection are classical; project value is the polarity classification

## 1. Question

The current frontier asks whether polarity can arise when the primitive law itself does not prefer either sign.

There are two distinct possibilities:

1. the **theory/ensemble** selects one polarity;
2. an **individual realization** lands in one of two symmetry-related sectors while the theory remains neutral between them.

These are not the same.

## 2. Minimal exact model

Use three states

$$
0,\quad +,\quad -,
$$

with involution

$$
\sigma(0)=0,\qquad
\sigma(+)=-,\qquad
\sigma(-)=+.
$$

Take the stochastic kernel

$$
K=
\begin{pmatrix}
0&1/2&1/2\\
0&1&0\\
0&0&1
\end{pmatrix}.
$$

From the neutral state, the process selects \(+\) or \(-\) with equal probability.

After selection, both sectors are absorbing.

The law is exactly invariant under \(+\leftrightarrow-\).

## 3. Symmetric initial state

Start from

$$
\pi_0=(1,0,0).
$$

After one update,

$$
\pi_1=
\left(
0,\frac12,\frac12
\right).
$$

For every

$$
n\ge1,
$$

$$
\boxed{
\pi_n=
\left(
0,\frac12,\frac12
\right).
}
$$

Thus the ensemble remains exactly invariant under the sector swap.

## 4. Odd and even polarity observables

Define the reversal-odd order parameter

$$
M(\pi)=\pi_+-\pi_-.
$$

Then

$$
\boxed{
M(\pi_n)=0
\qquad
\text{for every }n.
}
$$

The ensemble has no preferred polarity.

Now define the sector-selection magnitude

$$
A(\pi)=\pi_++\pi_-.
$$

Then

$$
A(\pi_0)=0,
$$

while

$$
\boxed{
A(\pi_n)=1
\qquad
(n\ge1).
}
$$

Therefore the process can leave the symmetric neutral sector completely while retaining zero ensemble-average polarity.

## 5. Individual realizations

Every trajectory beginning at \(0\) has, after the first update, one of the forms

$$
0,+,+,+,\ldots
$$

or

$$
0,-,-,-,\ldots
$$

with probability \(1/2\) each.

Each realized trajectory therefore possesses a stable polarity.

But the probability law over trajectories is invariant under

$$
+\leftrightarrow-.
$$

Hence

$$
\boxed{
\text{realization-level asymmetry}
\not\Rightarrow
\text{ensemble-level preferred sign}.
}
$$

## 6. Relation to the symmetry no-go

The automorphism no-go ruled out a **canonical deterministic** choice of one direction from perfectly symmetric primitive data.

The present model does not violate that theorem.

It does not canonically choose \(+\).

It samples one of two symmetry-related sectors.

The reversed realization is assigned the same probability.

Thus stochastic sector selection evades deterministic uniqueness only by giving up uniqueness.

## 7. Relation to A21

A21 showed that when two symmetry-related models are evolved with the same equivariant update structure and coupled randomness, their trajectories remain symmetry-related.

The current model is the complementary perspective.

A single unbiased random draw can select one sector in one realization.

Applying the symmetry to the same realization produces an equally admissible partner realization.

The law over the pair remains symmetric.

There is no contradiction.

## 8. General finite symmetry statement

Let a finite state space carry an involution

$$
\sigma^2=\mathrm{id}.
$$

Let the initial probability law satisfy

$$
\pi(\sigma x)=\pi(x),
$$

and let the Markov kernel be equivariant:

$$
K(\sigma x,\sigma y)=K(x,y).
$$

Then the pushed-forward distribution

$$
\pi'(y)=\sum_x\pi(x)K(x,y)
$$

is also invariant:

$$
\boxed{
\pi'(\sigma y)=\pi'(y).
}
$$

Proof:

$$
\begin{aligned}
\pi'(\sigma y)
&=
\sum_x\pi(x)K(x,\sigma y)\\
&=
\sum_x\pi(\sigma x)K(\sigma x,\sigma y)\\
&=
\sum_x\pi(x)K(x,y)\\
&=
\pi'(y),
\end{aligned}
$$

where the middle change of variable uses the bijection \(x\mapsto\sigma x\).

Therefore a symmetric law plus symmetric ensemble cannot generate a nonzero ensemble-average reversal-odd observable.

## 9. What stochastic sector selection can explain

It can explain how one realization may exhibit:

- a definite sign;
- a stable sector;
- broken symmetry;
- persistent records correlated with that sector;

even though the law itself does not prefer one sign.

This is a legitimate route to **realized asymmetry**.

## 10. What it cannot explain by itself

It cannot explain:

- why \(+\) rather than \(-\) is universally preferred;
- a nonzero ensemble-average polarity without additional asymmetric information;
- temporal succession itself;
- duration;
- why the two sectors should be interpreted as past-to-future rather than another binary physical choice.

Therefore

$$
\boxed{
\text{stochastic sector selection can produce a realized arrow candidate,
but not a canonical arrow of the symmetric theory}.
}
$$

## 11. Strict SSB terminology

For finite systems, the phrase “spontaneous symmetry breaking” requires care.

In the orthodox equilibrium/statistical-mechanical treatment, strict SSB is tied to infinite-volume or thermodynamic-limit structure and multiple symmetry-related equilibrium phases.

Large finite systems can nevertheless display very long-lived approximately isolated sectors and the phenomenology associated with symmetry breaking.

The present three-state witness is therefore classified as:

**symmetric stochastic sector selection**, not a new finite-system SSB theorem.

## 12. Thermodynamic-limit benchmark

In established SSB, the order of limits matters.

A small symmetry-breaking field can select one phase before the infinite-volume limit is taken; after the limit, the selected phase can remain asymmetric when the explicit field tends to zero.

This illustrates an important difference from the minimal finite witness:

- a macroscopic phase can become dynamically stable;
- sector restoration times can diverge;
- the ensemble of all symmetry-related sectors can remain symmetric even while one realized phase is asymmetric.

The project should preserve these distinctions.

## 13. Consequence for pregeometric polarity

The polarity problem now splits into two versions.

### Canonical polarity

The theory itself distinguishes one sign.

This requires asymmetric law, boundary data, operational typing, or another non-invariant ingredient.

### Realized polarity

The theory is symmetric but one realization occupies one symmetry-broken sector.

This can arise by stochastic/sector selection.

The latter is a logically viable route for a universe that is one realization.

But it creates new obligations.

## 14. Obligations for a sector-selection explanation of an arrow

A serious proposal must specify:

1. the symmetric primitive state space;
2. the symmetry exchanging opposite polarities;
3. the sector-selection mechanism or measure;
4. an order parameter that is reversal-odd;
5. stability/decoherence of the selected sector;
6. why internal observers can operationally identify the sector;
7. why the sector variable corresponds to causal/temporal polarity rather than another broken symmetry;
8. whether the opposite sector is physically equivalent;
9. how ordinary causal order is recovered;
10. how duration is subsequently calibrated.

Without these steps, “spontaneous arrow” is only a label.

## 15. Current verdict

**Can symmetric laws admit asymmetric realized sectors?**  
YES.

**Can one realization acquire stable polarity with no law-level sign preference?**  
YES.

**Does the symmetric ensemble acquire a preferred sign?**  
NO.

**Does this violate the automorphism/equivariance no-go?**  
NO.

**Is the finite witness strict thermodynamic SSB?**  
NO.

**Can sector selection by itself derive physical time?**  
NO.

**Is sector selection a viable candidate mechanism for realized polarity?**  
YES, conditionally.

## 16. Revised frontier

The direction programme now has two distinct polarity questions:

$$
\boxed{
\text{Where does a canonical sign preference come from?}
}
$$

and

$$
\boxed{
\text{Can a symmetric theory yield stable realized polarity
without canonical sign preference?}
}
$$

The second question has a mathematical **yes**.

The remaining physical problem is whether a sector variable can be given a non-circular causal/temporal interpretation.
