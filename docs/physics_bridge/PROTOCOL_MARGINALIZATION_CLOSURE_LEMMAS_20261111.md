# Protocol marginalization and stroboscopic closure — reusable bridge lemmas

**Date:** 2026-11-11  
**Author:** Felipe Gianini Romero  
**Status:** elementary exact lemmas for reuse across physical bridges  
**Novelty status:** classical probability/linear-systems content; no originality claim

## 1. Purpose

The multi-electron example revealed a pattern that is useful beyond that device.

A reduced observable may close when an external protocol is known, lose closure when the protocol is marginalized, and regain a finite recurrence after sampling at a natural period.

This note isolates the minimal mathematics needed to test that pattern elsewhere.

## 2. Hidden-context scalar dynamics

Let \(\xi\) be an unobserved or marginalized context variable and suppose

$$
\dot x_\xi(t)
=
a_\xi(t)x_\xi(t)
+
b_\xi(t).
$$

Define ensemble averages

$$
\bar x=\mathbb E_\xi[x_\xi],
\qquad
\bar a=\mathbb E_\xi[a_\xi],
\qquad
\bar b=\mathbb E_\xi[b_\xi].
$$

Then exactly

$$
\boxed{
\dot{\bar x}
=
\bar a\,\bar x
+
\bar b
+
\operatorname{Cov}_\xi(a_\xi,x_\xi).
}
$$

The covariance is not a modeling correction. It is the algebraic consequence of marginalization.

## 3. Universal scalar closure obstruction

Suppose \(a_\xi\) takes at least two different values at a fixed time.

Choose two hidden contexts with

$$
a_1\neq a_2.
$$

Consider two conditioned states

$$
(x_1,x_2)=(r,s)
$$

and

$$
(x_1',x_2')=(s,r),
$$

with

$$
r\neq s.
$$

They have the same marginal mean,

$$
\frac{r+s}{2},
$$

but

$$
\frac{a_1r+a_2s}{2}
\neq
\frac{a_1s+a_2r}{2}.
$$

Therefore the same \(\bar x\) can have different \(\dot{\bar x}\).

So, over an unrestricted conditioned-state class, a hidden variation in the multiplicative coefficient obstructs universal scalar closure of the marginal mean.

This is the abstract form of the random-phase covariance obstruction.

## 4. Why adding one covariance is not automatically a closure

Defining

$$
C(t)=\operatorname{Cov}(a_\xi,x_\xi)
$$

rewrites the marginal equation but does not prove that \((\bar x,C)\) closes.

The derivative of \(C\) generally contains higher mixed moments involving \(a_\xi\), \(\dot a_\xi\), and \(x_\xi\).

A finite augmentation is justified only if the context dynamics and coefficient family produce a finite invariant hierarchy.

Otherwise the correct exact reduced description can be non-Markovian or infinite-dimensional.

This is consistent with the general Mori-Zwanzig lesson that projection can generate memory.

## 5. Stroboscopic common-polynomial lemma

Now suppose the hidden-context system is periodic and, after augmenting affine coordinates if necessary, each context has a one-period linear map

$$
X_{\xi,n+1}
=
M_\xi X_{\xi,n}.
$$

Assume there is a single polynomial

$$
P(z)=p_0+p_1z+\cdots+p_dz^d
$$

such that

$$
P(M_\xi)=0
$$

for every hidden context \(\xi\).

Then

$$
\sum_{k=0}^d
p_kX_{\xi,n+k}=0
$$

for every \(\xi\).

Averaging gives

$$
\boxed{
P(E)\bar X_n=0,
}
$$

where \(E\) is the one-step shift in the stroboscopic index.

Thus the marginal stroboscopic sequence has an exact finite recurrence even when the continuous-time marginal is not closed.

No independence assumption between \(X_{\xi,n}\) and \(\xi\) is needed.

## 6. Common characteristic polynomial

A sufficient condition is that all one-period maps \(M_\xi\) have the same characteristic polynomial.

Then Cayley-Hamilton supplies a common annihilating polynomial.

This is exactly what happens in the commensurate transform hierarchy of the randomized-phase quantum-dot bridge: the monodromy matrices are lower triangular with phase-independent diagonal Floquet multipliers.

## 7. Scalar affine corollary

If

$$
x_{\xi,n+1}
=
\mu x_{\xi,n}+C_\xi
$$

with one common \(\mu\), augment by the constant coordinate or eliminate the intercept directly.

The marginal obeys

$$
\bar x_{n+1}
=
\mu\bar x_n+\bar C,
$$

and hence

$$
\boxed{
\bar x_{n+2}
-
(1+\mu)\bar x_{n+1}
+
\mu\bar x_n
=
0.
}
$$

The result remains true even if \(x_{\xi,n}\) is strongly correlated with the hidden context.

## 8. Interpretation for the repository

The reusable lesson is not that every coarse-grained process closes stroboscopically.

It is conditional:

> Marginalization can destroy instantaneous closure, while a common finite one-period algebra can restore a finite recurrence at a coarser temporal resolution.

This supplies a practical test for future physical bridges.

Before adding new state variables, ask:

1. what information was marginalized?
2. does the conditioned observable close?
3. does the marginal require correlations or memory?
4. is there a natural sampling map with a common annihilating polynomial?
5. can the reduced representation be tested without fitting its closure coefficients?

## 9. Literature boundary

These lemmas are elementary consequences of expectation algebra, linear systems, Floquet/monodromy theory, and Cayley-Hamilton.

They sit inside a much broader literature:

- Mori-Zwanzig projection and memory under coarse-graining;
- hidden Markov and partially observed dynamics;
- Koopman invariant observable subspaces;
- Floquet theory for periodically driven stochastic systems.

No novelty claim is attached to the lemmas themselves.

Their role is methodological: they prevent future bridge work from adding ad hoc variables when a known projection or sampling structure already explains the apparent loss of closure.
