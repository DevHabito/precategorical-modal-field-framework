# MF-R049 — exact rational witness derivation

**Consolidation target:** F3 / C2  
**Purpose:** derive a minimal exact witness before proof-assistant implementation  
**Status:** mathematical derivation; no novelty claim

## 1. Target statement

For a finite probability distribution on scores `q_i`, define the exponential
moment

\[
M_\lambda(p)=\sum_i p_i e^{-\lambda q_i}
\]

and the entropic score

\[
Q_\lambda(p)=-\frac1\lambda\log M_\lambda(p),\qquad \lambda>0.
\]

Under the centered contraction

\[
q_i'=\bar q+a(q_i-\bar q),\qquad 0<a<1,
\]

the exact transport identity is

\[
Q_\lambda'=(1-a)\bar q+aQ_{a\lambda}.
\]

To disprove closure of the macrostate `(mean, Q_lambda)` on the unrestricted
finite-distribution class, it is enough to find two positive probability
vectors with

1. the same normalization;
2. the same mean;
3. the same `M_lambda` (hence the same `Q_lambda`);
4. different `M_{a lambda}` (hence different `Q_{a lambda}` and different next
   `Q_lambda`).

The historical witness used `lambda = log 2`, `a=1/2`, which introduces
`sqrt(2)` at the transported scale. The witness below is derived from the same
linear constraint structure but chooses `lambda = log 4`; then
`a lambda = log 2`, so all finite moment checks are rational.

## 2. Support and linear constraints

Use support

\[
q=(0,1,2,3).
\]

At

\[
\lambda=\log4,
\]

we have

\[
e^{-\lambda q_i}=4^{-q_i},
\]

so the initial moment vector is

\[
(1,1/4,1/16,1/64).
\]

Let `d=(d_0,d_1,d_2,d_3)` be a perturbation that preserves normalization,
mean, and this initial moment. Then

\[
\begin{aligned}
d_0+d_1+d_2+d_3&=0,\\
d_1+2d_2+3d_3&=0,\\
d_0+\frac14d_1+\frac1{16}d_2+\frac1{64}d_3&=0.
\end{aligned}
\]

Solving this rank-three system gives the one-dimensional null direction

\[
\boxed{d=\frac14(-1,6,-9,4)}.
\]

This is not selected by numerical fitting: it is the exact nullspace of the
three quantities that must remain fixed.

## 3. Two strictly positive distributions

Take the center distribution

\[
u=(1/4,1/4,1/4,1/4)
\]

and exact step

\[
t=\frac1{20}.
\]

Define

\[
p^+=u+td,
\qquad
p^-=u-td.
\]

Then

\[
\boxed{
p^+=\left(\frac{19}{80},\frac{13}{40},\frac{11}{80},\frac3{10}\right)
}
\]

and

\[
\boxed{
p^-=\left(\frac{21}{80},\frac7{40},\frac{29}{80},\frac15\right).
}
\]

Every entry is strictly positive.

Because `d` lies in the nullspace above, both vectors normalize to one and have
exactly the same mean and initial moment. Directly,

\[
\sum_i p_i^+=\sum_i p_i^-=1,
\]

\[
\sum_i q_i p_i^+=\sum_i q_i p_i^-=\frac32,
\]

and

\[
\sum_i p_i^+4^{-q_i}
=
\sum_i p_i^-4^{-q_i}
=
\boxed{\frac{85}{256}}.
\]

Therefore

\[
Q_{\log4}(p^+)=Q_{\log4}(p^-).
\]

## 4. Transported scale separates the pair

Set

\[
a=\frac12.
\]

Then

\[
a\lambda=\frac12\log4=\log2.
\]

The transported moment uses

\[
e^{-(\log2)q_i}=2^{-q_i}.
\]

For the two distributions,

\[
M_{\log2}(p^+)
=
\frac{151}{320},
\]

whereas

\[
M_{\log2}(p^-)
=
\frac{149}{320}.
\]

Hence

\[
\boxed{
M_{\log2}(p^+)-M_{\log2}(p^-)=\frac1{160}>0.
}
\]

Since `log` is injective on positive reals and `log 2 > 0`, this implies

\[
Q_{\log2}(p^+)\ne Q_{\log2}(p^-).
\]

The centered-contraction transport identity now gives

\[
Q_{\log4}'
=
\frac12\bar q+\frac12Q_{\log2}.
\]

The means are equal but the required `Q_{\log2}` values differ, so

\[
\boxed{
Q_{\log4}'(p^+)\ne Q_{\log4}'(p^-).
}
\]

Thus `(mean, Q_{log 4})` is not a dynamically closed state variable on the
unrestricted finite-distribution class.

## 5. Why this witness is preferable for formalization

Compared with the historical `(lambda=log 2, a=1/2)` witness, this construction:

- preserves the same logical MF-R049 existence claim;
- keeps the same four-point support;
- is derived exactly from the invariance constraints;
- replaces the transported `sqrt(2)` algebra by rational arithmetic;
- leaves only a small analytic bridge involving `exp`, `log`, positivity, and
  the centered-contraction identity.

The historical witness remains valid provenance. This witness is a proof-engineering
replacement, not a change in scientific claim.

## 6. Nonclaims

This witness does **not** prove that:

- no finite-dimensional closure can exist on restricted families;
- the whole curve `lambda -> Q_lambda` is always minimal;
- every contraction or nonlinear dynamics has the same obstruction;
- the result is a new general theorem of moment closure;
- the mathematical map is a physical evolution law.

It proves only the declared existence statement: on the unrestricted finite
four-point class, mean plus one fixed entropic score does not determine the next
fixed entropic score under the stated centered contraction.