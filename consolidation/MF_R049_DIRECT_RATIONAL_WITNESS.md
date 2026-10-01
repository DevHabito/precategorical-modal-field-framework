# MF-R049 — direct rational next-state witness

**Consolidation target:** F3 / C2  
**Status:** exact derivation checked before analytic Lean formalization  
**Role:** refinement of the proof witness, not a change to the MF-R049 claim

This note records a second rational construction found while red-teaming the analytic bridge for F3. The previously frozen rational witness is preserved in `MF_R049_RATIONAL_FORMAL_WITNESS.md`; its arithmetic remains correct. The purpose of this refinement is narrower: choose the baseline mean so that the **actual post-contraction exponential moment is rational as well**, allowing the dynamic non-closure claim to be proved directly from the update rather than by importing the transport identity MF-R048.

No numerical fitting or search is used. The same algebraically derived difference direction is retained.

## 1. Difference direction

On support

\[
q\in\{0,1,2,3\},
\]

retain

\[
D(z)=(z-1)^2(4z-1)
=4z^3-9z^2+6z-1,
\]

so

\[
\boxed{d=(-1,6,-9,4)}.
\]

Hence

\[
D(1)=0,
\qquad
D'(1)=0,
\qquad
D\!\left(\frac14\right)=0,
\qquad
D\!\left(\frac12\right)=\frac14.
\]

The first two identities preserve normalization and mean along the perturbation; the third preserves the initial exponential moment at base `1/4`; the fourth separates the rescaled base `1/2` moment.

## 2. Mean-one baseline

Choose the strictly positive baseline

\[
b=\left(\frac25,\frac3{10},\frac15,\frac1{10}\right).
\]

It satisfies

\[
\sum_i b_i=1
\]

and

\[
\sum_{i=0}^3 i b_i
=\frac3{10}+2\cdot\frac15+3\cdot\frac1{10}
=1.
\]

Freeze

\[
\varepsilon=\frac1{80}
\]

and define

\[
p^+=b+\varepsilon d,
\qquad
p^-=b-\varepsilon d.
\]

This gives

\[
\boxed{
p^+=\left(
\frac{31}{80},
\frac38,
\frac7{80},
\frac3{20}
\right)
}
\]

and

\[
\boxed{
p^-=\left(
\frac{33}{80},
\frac9{40},
\frac5{16},
\frac1{20}
\right).
}
\]

All eight weights are strictly positive. Because `D(1)=D'(1)=0`,

\[
\boxed{
\sum_i p_i^+=\sum_i p_i^-=1,
\qquad
\bar q^+=\bar q^-=1.
}
\]

## 3. Same initial entropic score

Choose

\[
\boxed{\lambda=2\log2},
\qquad
\boxed{a=\frac12}.
\]

Then

\[
e^{-\lambda}=\frac14.
\]

Since `D(1/4)=0`, the two initial exponential moments coincide. Direct exact arithmetic gives

\[
\boxed{
M_\lambda(p^+)=M_\lambda(p^-)=\frac{313}{640}.
}
\]

Therefore

\[
\boxed{
Q_\lambda(p^+)=Q_\lambda(p^-).
}
\]

Together with the common mean, the two initial macrostates `(mean,Q_lambda)` are identical.

## 4. Different half-scale moments

At

\[
a\lambda=\log2,
\]

we have base

\[
e^{-a\lambda}=\frac12.
\]

Exact arithmetic gives

\[
\boxed{
M_{a\lambda}(p^+)=\frac{197}{320}
}
\]

and

\[
\boxed{
M_{a\lambda}(p^-)=\frac{39}{64}=\frac{195}{320}.
}
\]

Thus

\[
\boxed{
M_{a\lambda}(p^+)-M_{a\lambda}(p^-)=\frac1{160}>0.
}
\]

## 5. Direct next-state calculation

Because the common mean is exactly `1`, the centered half-contraction is

\[
q_i'
=1+\frac12(q_i-1)
=\frac12+\frac12 q_i.
\]

Hence the four updated support values are exactly

\[
\left\{\frac12,1,\frac32,2\right\}.
\]

At the fixed observational parameter

\[
\lambda=2\log2,
\]

we have, for each original integer support value `q=i`,

\[
\begin{aligned}
e^{-\lambda q_i'}
&=e^{-2\log2\,(1/2+i/2)}\\
&=e^{-(1+i)\log2}\\
&=\frac12\left(\frac12\right)^i.
\end{aligned}
\]

Therefore the **actual next-state** exponential moments are exactly one half of the base-`1/2` moments above:

\[
\boxed{
M_\lambda'(p^+)=\frac{197}{640}
}
\]

and

\[
\boxed{
M_\lambda'(p^-)=\frac{39}{128}=\frac{195}{640}.
}
\]

Their difference is

\[
\boxed{
M_\lambda'(p^+)-M_\lambda'(p^-)=\frac1{320}>0.
}
\]

Both moments are positive. Since `log` is injective on positive reals and `lambda=2 log 2` is positive,

\[
\boxed{
Q_\lambda'(p^+)\ne Q_\lambda'(p^-).
}
\]

Thus we obtain the MF-R049 non-closure statement **directly from the declared centered update**, without needing the transport identity as an imported theorem:

\[
\boxed{
(\bar q^+,Q_\lambda(p^+))
=(\bar q^-,Q_\lambda(p^-))
}
\]

but

\[
\boxed{
Q_\lambda'(p^+)\ne Q_\lambda'(p^-).
}
\]

## 6. Why this is preferable for the formal proof

The first rational witness already removes the historical `sqrt(2)` from the two pre-update moments, but its mean `3/2` creates a non-rational common exponential factor if one computes the updated distribution directly.

The present witness changes only the **baseline distribution**, not the algebraic difference direction or the scientific claim. Selecting mean `1` makes the affine offset under the half-contraction exactly `1/2`; with `lambda=2 log 2`, every updated exponential factor becomes a rational power of `1/2`.

This means the formal proof can be layered as follows:

1. rational probability/mean/moment identities;
2. elementary `exp/log` bridge proving `exp(-log 2)=1/2` and `exp(-2 log 2)=1/4`;
3. exact initial exponential-moment equality;
4. exact updated exponential-moment inequality;
5. log injectivity on positive moments;
6. final non-closure theorem.

No square-root inequality, asymptotics, numerical tolerance, Monte Carlo computation, or general moment-closure machinery is required.

## 7. Frozen exact targets

For any direct Lean implementation based on this refinement, the exact targets are frozen as:

- `p+ = (31/80, 3/8, 7/80, 3/20)`;
- `p- = (33/80, 9/40, 5/16, 1/20)`;
- both masses `=1`;
- both means `=1`;
- both initial base-`1/4` moments `=313/640`;
- base-`1/2` moments `=197/320` and `39/64`;
- base-`1/2` difference `=1/160`;
- post-contraction fixed-`lambda` moments `=197/640` and `39/128`;
- post-contraction moment difference `=1/320`.

If a checker disagrees with any of these values, the implementation or this derivation must be investigated; the targets are not to be edited to make a proof pass.

## 8. Nonclaims

This refinement does not claim uniqueness or minimality of the witness, does not invalidate the historical witness or the first rational witness, does not establish a general impossibility of finite-dimensional closure on restricted families, and carries no physical interpretation.

Its only purpose is proof hygiene: an exact constructive counterexample to the already selected MF-R049 claim with the analytic surface area reduced as far as practical.
