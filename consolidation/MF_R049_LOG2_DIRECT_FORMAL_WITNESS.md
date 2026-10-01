# MF-R049 — parameter-preserving direct formal witness

**Consolidation target:** F3 / C2  
**Status:** exact derivation checked before Lean implementation  
**Preferred final witness:** yes, subject to kernel verification

This note freezes a Lean-oriented counterexample for MF-R049 that keeps the historical parameters

\[
\lambda=\log 2,
\qquad
a=\frac12,
\]

while avoiding the square-root arithmetic of the historical support `{0,1,2,3}`.

The construction is not a numerical fit. It is obtained from the same algebraic difference polynomial used in the rational red-team, followed by an exact rescaling of the support. Earlier witness notes are preserved as derivation history; no earlier exact result is being invalidated.

## 1. Difference direction

Let

\[
D(z)=(z-1)^2(4z-1)
=4z^3-9z^2+6z-1,
\]

so the perturbation direction is

\[
\boxed{d=(-1,6,-9,4)}.
\]

The exact constraints are

\[
D(1)=0,
\qquad
D'(1)=0,
\qquad
D\!\left(\frac14\right)=0,
\qquad
D\!\left(\frac12\right)=\frac14.
\]

Thus the direction preserves total mass, preserves the index mean, preserves the base-`1/4` moment, and separates the base-`1/2` moment.

## 2. Probability vectors

Use the mean-one index baseline

\[
b=\left(\frac25,\frac3{10},\frac15,\frac1{10}\right)
\]

and

\[
\varepsilon=\frac1{80}.
\]

Define

\[
p^+=b+\varepsilon d,
\qquad
p^-=b-\varepsilon d.
\]

Then

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

All eight probabilities are strictly positive and both vectors sum exactly to `1`.

For the index support `i in {0,1,2,3}`, both have index mean exactly `1`.

## 3. Physical score support for this witness

For the formal MF-R049 counterexample, use score support

\[
\boxed{q\in\{0,2,4,6\}},
\]

that is,

\[
q_i=2i.
\]

Because the common index mean is `1`, both score distributions have

\[
\boxed{\bar q^+=\bar q^-=2}.
\]

This support rescaling is permitted by the MF-R049 claim, whose domain is the unrestricted class of finite distributions. The historical support `{0,1,2,3}` is part of its particular witness, not an assumption of the non-closure statement.

## 4. Same initial score at the historical parameter

Freeze

\[
\boxed{\lambda=\log2}.
\]

Then for `q_i=2i`,

\[
e^{-\lambda q_i}
=e^{-2i\log2}
=\left(\frac14\right)^i.
\]

The exact initial exponential moments are therefore

\[
M_\lambda(p^+)
=\sum_{i=0}^3p_i^+\left(\frac14\right)^i
\]

and

\[
M_\lambda(p^-)
=\sum_{i=0}^3p_i^-\left(\frac14\right)^i.
\]

Because `D(1/4)=0`, they coincide. Direct exact arithmetic gives

\[
\boxed{
M_\lambda(p^+)=M_\lambda(p^-)=\frac{313}{640}.
}
\]

Since the moment is positive and the same fixed nonzero `lambda` is used,

\[
\boxed{
Q_{\log2}(p^+)=Q_{\log2}(p^-).
}
\]

Thus the two initial macrostates `(mean,Q_log2)` are exactly identical:

\[
\boxed{
(\bar q^+,Q_{\log2}(p^+))
=(\bar q^-,Q_{\log2}(p^-)).
}
\]

## 5. Declared centered half-contraction

Use the historical contraction parameter

\[
\boxed{a=\frac12}.
\]

Since the common score mean is `2`,

\[
q_i'
=2+\frac12(q_i-2).
\]

With `q_i=2i`, this reduces exactly to

\[
q_i'=1+i.
\]

Therefore the updated support is

\[
\boxed{q'\in\{1,2,3,4\}}.
\]

No transport identity is needed for the counterexample: the next fixed-`lambda` score can be evaluated directly from this updated support.

## 6. Exact next-state moments

At the same fixed observational parameter `lambda=log 2`,

\[
e^{-\lambda q_i'}
=e^{-(1+i)\log2}
=\frac12\left(\frac12\right)^i.
\]

The base-`1/2` index moments are

\[
\boxed{
\sum_i p_i^+\left(\frac12\right)^i
=\frac{197}{320}
}
\]

and

\[
\boxed{
\sum_i p_i^-\left(\frac12\right)^i
=\frac{39}{64}=\frac{195}{320}.
}
\]

Their exact difference is

\[
\boxed{\frac1{160}>0}.
\]

Multiplying by the common factor `1/2`, the actual next-state exponential moments are

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

Hence

\[
\boxed{
M_\lambda'(p^+)-M_\lambda'(p^-)=\frac1{320}>0.
}
\]

Both moments are strictly positive. Since `Real.log` is injective on positive reals and `log 2` is positive,

\[
\boxed{
Q_{\log2}'(p^+)\ne Q_{\log2}'(p^-).
}
\]

Combining the initial equality and next-state inequality yields the desired exact dynamic non-closure witness at the **same `lambda=log2` and `a=1/2` used by the historical MF-R049 witness**.

## 7. Why this witness is preferred for Lean

Compared with the historical witness, this construction removes `sqrt(2)` entirely.

Compared with the first rational candidate on support `{0,1,2,3}` at `lambda=2 log2`, it preserves the historical value `lambda=log2` exactly.

Compared with proving MF-R048 first and importing the transport identity, it establishes the dynamic divergence directly from the declared updated scores.

The intended formal chain is therefore minimal:

1. exact positive probability vectors;
2. exact common mean `2`;
3. exact common initial exponential moment `313/640`;
4. exact updated supports `{1,2,3,4}` under the centered half-contraction;
5. exact next exponential moments `197/640` and `39/128`;
6. positivity of `log 2` and of all moments;
7. injectivity of `log` on positive reals;
8. equal initial `Q_log2`, unequal next `Q_log2`.

No square roots, approximations, numerical tolerance, Monte Carlo evidence, asymptotics, or general closure theorem are required.

## 8. Frozen targets

The following values are frozen before Lean implementation:

- support: `(0,2,4,6)`;
- updated support under `a=1/2`: `(1,2,3,4)`;
- `lambda = log 2`;
- `p+ = (31/80, 3/8, 7/80, 3/20)`;
- `p- = (33/80, 9/40, 5/16, 1/20)`;
- masses: `1`, `1`;
- score means: `2`, `2`;
- initial exponential moments: `313/640`, `313/640`;
- base-`1/2` index moments: `197/320`, `39/64`;
- next exponential moments: `197/640`, `39/128`;
- next-moment difference: `1/320`.

A formal checker is not permitted to alter these targets. Any disagreement must be diagnosed.

## 9. Nonclaims

This witness does not prove that four support points are globally minimal, does not prove that no restricted finite-dimensional family can close, does not claim that the whole `lambda -> Q_lambda` curve is always minimal, and does not establish a new general theorem in moment-closure theory.

It is a deliberately narrow constructive witness for the selected MF-R049 statement on the unrestricted finite-distribution class.
