# Universal marginal closure criteria for hidden-context linear dynamics

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** exact elementary theorem package  
**Novelty status:** classical linear/projection algebra; no originality claim

## 1. Purpose

The quantum-dot bridge produced two opposite effects:

1. continuous-time closure was lost after marginalizing a hidden drive phase;
2. exact finite closure reappeared after sampling one full drive period.

This note states the minimal necessary-and-sufficient criteria behind those two effects.

The results are elementary. Their purpose is methodological: they tell future bridge work when a closure failure is forced and when a finite recurrence is available without inventing new variables.

## 2. Scalar hidden-context dynamics

Let the hidden context take finitely many values

$$
\xi\in\{1,\ldots,r\},
$$

with fixed positive weights

$$
w_i>0,
\qquad
\sum_iw_i=1.
$$

Suppose the conditioned scalar states satisfy

$$
\dot x_i(t)
=
a_i(t)x_i(t)
+
b_i(t).
$$

Define the marginal mean

$$
m(t)=\sum_iw_ix_i(t).
$$

Then

$$
\dot m
=
\sum_iw_ia_ix_i
+
\sum_iw_ib_i.
$$

## 3. Theorem A — exact criterion for universal scalar marginal closure

Fix a time \(t\).

Assume the conditioned values \(x_i\) are otherwise unrestricted.

There exists a function \(F_t:\mathbb R\to\mathbb R\) such that

$$
\dot m=F_t(m)
$$

for **every** conditioned state vector

$$
(x_1,\ldots,x_r)
$$

if and only if

$$
\boxed{
a_1(t)=a_2(t)=\cdots=a_r(t).
}
$$

When this holds,

$$
F_t(m)
=
a(t)m+\bar b(t),
$$

where

$$
\bar b(t)=\sum_iw_ib_i(t).
$$

### Proof — sufficiency

If every multiplicative coefficient equals \(a(t)\), then

$$
\dot m
=
a(t)\sum_iw_ix_i+\bar b(t)
=
a(t)m+\bar b(t).
$$

### Proof — necessity

Suppose two contexts \(i,j\) satisfy

$$
a_i\neq a_j.
$$

Because the weights need not be equal, use a perturbation that lies exactly in the kernel of the marginalization map.

For any nonzero scalar \(\delta\), change only contexts \(i\) and \(j\) by

$
\Delta x_i=w_j\delta,
\qquad
\Delta x_j=-w_i\delta.
$

Then

$
\Delta m
=
w_iw_j\delta-w_jw_i\delta
=
0.
$

But the derivative changes by

$
\boxed{
\Delta\dot m
=
w_iw_j(a_i-a_j)\delta.
}
$

Since \(w_i,w_j>0\), \(a_i\neq a_j\), and \(\delta\neq0\),

$
\Delta\dot m\neq0.
$

Thus two conditioned states can have exactly the same marginal mean and different marginal derivatives.

In the equal-weight two-context case,

$$
m=\frac{x_1+x_2}{2},
$$

and the exact gap is

$$
\boxed{
\dot m^{(r,s)}-\dot m^{(s,r)}
=
\frac{(a_1-a_2)(r-s)}2.
}
$$

Therefore the same marginal value can have two different derivatives.

No function of \(m\) alone can describe both.

\(\square\)

## 4. Interpretation of Theorem A

The theorem is stronger than the covariance identity

$$
\dot m
=
\bar a\,m+\bar b+\operatorname{Cov}(a,x).
$$

It says that, over the unrestricted conditioned-state class, varying multiplicative dynamics across hidden contexts do not merely make scalar closure inconvenient.

They make universal scalar closure impossible.

A closure can still exist on a smaller invariant family of conditioned states. That is an additional structure and must be demonstrated rather than assumed.

## 5. Vector version

Let

$$
x_i\in\mathbb R^d,
$$

with

$$
\dot x_i=A_i(t)x_i+b_i(t),
$$

and

$$
m=\sum_iw_ix_i.
$$

Over unrestricted conditioned states, a universal closed equation

$$
\dot m=F_t(m)
$$

exists if and only if all matrices are identical:

$$
\boxed{
A_1(t)=A_2(t)=\cdots=A_r(t).
}
$$

The proof is the same kernel argument: the linear map

$$
(x_1,\ldots,x_r)\mapsto
\sum_iw_iA_ix_i
$$

must factor through

$$
(x_1,\ldots,x_r)\mapsto
\sum_iw_ix_i.
$$

That factorization is possible for arbitrary conditioned vectors exactly when the \(A_i\) coincide.

## 6. Discrete-time hidden-context system

Now consider fixed hidden contexts with one-step maps

$$
X_{i,n+1}
=
M_iX_{i,n},
$$

where

$$
X_{i,n}\in\mathbb F^d.
$$

Define

$$
\bar X_n
=
\sum_iw_iX_{i,n}.
$$

Let

$$
P(z)=p_0+p_1z+\cdots+p_kz^k.
$$

## 7. Theorem B — necessary and sufficient common-polynomial criterion

The recurrence

$$
\boxed{
P(E)\bar X_n=0
}
$$

holds for **every** set of conditioned initial states

$$
X_{1,0},\ldots,X_{r,0}
$$

if and only if

$$
\boxed{
P(M_i)=0
\quad\text{for every context }i.
}
$$

Here \(E\) denotes the forward shift in \(n\).

### Proof — sufficiency

If

$$
P(M_i)=0,
$$

then

$$
P(E)X_{i,n}=0
$$

for every conditioned trajectory.

Averaging preserves the linear identity:

$$
P(E)\bar X_n
=
\sum_iw_iP(E)X_{i,n}
=
0.
$$

### Proof — necessity

Assume the marginal recurrence holds for every choice of initial states.

At \(n=0\),

$$
0
=
P(E)\bar X_0
=
\sum_iw_iP(M_i)X_{i,0}.
$$

The conditioned initial vectors are independent and every \(w_i>0\).

Choose all initial vectors zero except one.

Then

$$
P(M_i)X_{i,0}=0
$$

for every \(X_{i,0}\).

Therefore

$$
P(M_i)=0.
$$

This holds for each context.

\(\square\)

## 8. Minimal universal recurrence

Let

$$
m_i(z)
$$

be the minimal polynomial of \(M_i\).

A polynomial annihilates every hidden-context map exactly when it is a common multiple of all \(m_i\).

Therefore the monic polynomial of least degree producing a universal marginal recurrence is

$$
\boxed{
P_{\min}
=
\operatorname{lcm}(m_1,\ldots,m_r).
}
$$

This is ordinary linear algebra.

It gives a precise meaning to the smallest **universal** stroboscopic recurrence over unrestricted conditioned initial states.

## 9. Application to the randomized-phase quantum-dot hierarchy

For the augmented commensurate hierarchy

$$
X_m=(1,G_c,\ldots,G_{mc})^\top,
$$

each phase-conditioned one-period monodromy matrix is lower triangular with diagonal

$$
1,\mu_1,\ldots,\mu_m.
$$

For

$$
0<q<1,
$$

the multipliers satisfy

$$
1>\mu_1>\mu_2>\cdots>\mu_m>0.
$$

Thus the eigenvalues are distinct.

Every monodromy matrix therefore has minimal polynomial

$$
\boxed{
P_m(z)
=
\prod_{j=0}^m(z-\mu_j).
}
$$

The polynomial is independent of phase.

By Theorem B, the phase-averaged augmented hierarchy obeys the exact universal recurrence

$$
P_m(E)\bar X_{m,n}=0.
$$

Moreover, for the **full augmented state**, no lower-degree universal polynomial recurrence can hold over all conditioned initial states.

### Coordinate caution

A particular scalar coordinate can sometimes obey a lower-order recurrence for special initial conditions or because some modes are not visible in that coordinate.

The minimality statement above is for the full augmented hierarchy and universal initial-state class.

No stronger scalar minimality claim is made without a separate observability proof.

## 10. Why this helps future physical bridges

These two theorems provide a strict decision procedure.

### Continuous time

If hidden contexts carry different multiplicative generators, do not expect a universal marginal Markov closure on the mean alone unless a restricted invariant family is proved.

### Discrete/stroboscopic time

Search for a common annihilating polynomial of the hidden-context maps.

- If one exists, an exact finite marginal recurrence exists.
- If none exists, no universal finite linear recurrence with those coefficients can hold over unrestricted initial conditions.

This avoids adding ad hoc hidden variables merely because one representation fails.

## 11. Relationship to classical literature

Theorem A is elementary factorization/projection algebra and is consistent with Mori-Zwanzig's general message: unresolved variables appear as memory/noise/coupling terms in exact reduced equations.

Theorem B is a direct consequence of matrix polynomial identities and Cayley-Hamilton. Matrix-power sequences satisfying linear recurrences are standard linear algebra.

Koopman theory provides a broader operator language for finite invariant observable subspaces.

No novelty claim is attached to either theorem.

## 12. Project-specific role

The value to the repository is organizational:

- it converts the quantum-dot example into reusable falsification criteria;
- it separates a true obstruction from a poor choice of variable;
- it distinguishes continuous-time marginal closure from recurrence closure after sampling;
- it gives an exact criterion before a new physical system is analyzed.

The next bridge should be accepted only if it tests something not already decided by these classical criteria.
