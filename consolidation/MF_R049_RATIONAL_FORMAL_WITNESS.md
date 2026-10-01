# MF-R049 — exact rational witness for formalization

**Consolidation target:** F3 / C2  
**Purpose:** derive and freeze a Lean-friendly exact witness before proof-script iteration  
**Status:** mathematical derivation checked; Lean formalization not yet claimed

This note does **not** replace the historical MF-R049 witness. The historical witness remains valid provenance. The purpose here is to derive a second witness that proves the same existence/non-closure claim while removing the square-root arithmetic that appears in the historical choice `lambda = log 2`, `a = 1/2`.

No numerical search or fitted optimization is used below.

## 1. Target claim

For a finite probability distribution on scores `q_i`, define

\[
Q_\lambda
=-\frac1\lambda
\log\!\left(\sum_i p_i e^{-\lambda q_i}\right),
\qquad \lambda>0.
\]

Under the centered contraction

\[
q_i'=(1-a)\bar q+a q_i,
\qquad
\bar q=\sum_i p_iq_i,
\]

classical affine covariance gives

\[
Q_\lambda(q')
=(1-a)\bar q+aQ_{a\lambda}(q).
\]

To refute closure of the macrostate `(mean, Q_lambda)` on the unrestricted finite-distribution class, it is enough to exhibit two distributions with

\[
\bar q^+=\bar q^-,
\qquad
Q_\lambda^+=Q_\lambda^-,
\]

but

\[
Q_{a\lambda}^+\ne Q_{a\lambda}^-.
\]

Then their next fixed-`lambda` scores are different.

## 2. Why four support points appear naturally

Use support

\[
q\in\{0,1,2,3\}.
\]

Let `d=(d_0,d_1,d_2,d_3)` be the difference direction between two weight vectors, and define the cubic polynomial

\[
D(z)=d_0+d_1z+d_2z^2+d_3z^3.
\]

Three equality requirements become three exact root constraints:

1. equal normalization:
   \[
   D(1)=\sum_i d_i=0;
   \]
2. equal mean:
   \[
   D'(1)=\sum_i i\,d_i=0;
   \]
3. equal exponential moment at an initial base `r`:
   \[
   D(r)=\sum_i d_i r^i=0.
   \]

Therefore the simplest nonzero cubic difference polynomial has the form

\[
D(z)=c(z-1)^2(z-r).
\]

For a half-contraction `a=1/2`, the required rescaled exponential base is `sqrt(r)`. If `0<r<1`, then

\[
D(\sqrt r)
=c(\sqrt r-1)^2(\sqrt r-r),
\]

which is nonzero for `c\ne0`.

This is the structural mechanism behind the witness. The formalization instance below chooses `r=1/4`, so both `r` and `sqrt(r)=1/2` are rational. This is why the new witness avoids square roots; the choice is algebraic, not numerical fitting.

## 3. Frozen difference direction

Take

\[
r=\frac14
\]

and choose the integer normalization

\[
D(z)=(z-1)^2(4z-1).
\]

Expanding,

\[
D(z)=4z^3-9z^2+6z-1.
\]

Hence freeze

\[
\boxed{d=(-1,6,-9,4)}.
\]

The required constraints are immediate:

\[
D(1)=0,
\qquad
D'(1)=0,
\qquad
D\!\left(\frac14\right)=0.
\]

At the rescaled base,

\[
D\!\left(\frac12\right)
=\left(\frac12-1\right)^2\left(4\cdot\frac12-1\right)
=\frac14.
\]

Thus the rescaled moment will differ exactly.

## 4. Frozen probability vectors

Start from the uniform interior point

\[
b=\left(\frac14,\frac14,\frac14,\frac14\right)
\]

and freeze

\[
\varepsilon=\frac1{40}.
\]

Define

\[
p^+=b+\varepsilon d,
\qquad
p^-=b-\varepsilon d.
\]

Explicitly,

\[
\boxed{
p^+
=\left(
\frac9{40},
\frac25,
\frac1{40},
\frac7{20}
\right)
}
\]

and

\[
\boxed{
p^-
=\left(
\frac{11}{40},
\frac1{10},
\frac{19}{40},
\frac3{20}
\right).
}
\]

Every entry is strictly positive, and

\[
\sum_i p_i^+=\sum_i p_i^-=1.
\]

The two distributions therefore lie strictly inside the three-dimensional probability simplex on four support points; no zero or signed weights are being used.

## 5. Equal means

Because `D'(1)=0`, the perturbation does not change the mean. The uniform baseline has mean

\[
\frac{0+1+2+3}{4}=\frac32.
\]

Therefore

\[
\boxed{
\bar q^+=\bar q^-=\frac32.
}
\]

Directly,

\[
\sum_i i p_i^+
=\sum_i i p_i^-
=\frac32.
\]

## 6. Equal initial exponential moment

Choose

\[
\boxed{\lambda=2\log2},
\qquad
\boxed{a=\frac12}.
\]

Then

\[
e^{-\lambda}=e^{-2\log2}=\frac14.
\]

For integer support `q=i`, the initial exponential moment is therefore

\[
M_\lambda(p)=\sum_{i=0}^3 p_i\left(\frac14\right)^i.
\]

Since `D(1/4)=0`, the two moments are identical. Their exact common value is

\[
\boxed{
M_\lambda(p^+)=M_\lambda(p^-)=\frac{85}{256}.
}
\]

Hence

\[
\boxed{
Q_\lambda(p^+)=Q_\lambda(p^-).
}
\]

No decimal approximation is involved.

## 7. Different required rescaled moment

With `a=1/2`,

\[
a\lambda=\log2,
\]

so

\[
e^{-a\lambda}=\frac12.
\]

The required previous-state moment is

\[
M_{a\lambda}(p)=\sum_{i=0}^3p_i\left(\frac12\right)^i.
\]

The uniform baseline contributes

\[
\frac14\left(1+\frac12+\frac14+\frac18\right)
=\frac{15}{32}.
\]

Because

\[
D\!\left(\frac12\right)=\frac14
\]

and `epsilon=1/40`, the two moments are

\[
\boxed{
M_{a\lambda}(p^+)=\frac{19}{40}
}
\]

and

\[
\boxed{
M_{a\lambda}(p^-)=\frac{37}{80}.
}
\]

Their exact difference is

\[
\boxed{
M_{a\lambda}(p^+)-M_{a\lambda}(p^-)=\frac1{80}>0.
}
\]

Since both moments are positive, `log` is injective on them; since `a lambda = log 2` is nonzero,

\[
\boxed{
Q_{a\lambda}(p^+)\ne Q_{a\lambda}(p^-).
}
\]

## 8. Dynamic non-closure

For the declared centered contraction,

\[
Q_\lambda'
=(1-a)\bar q+aQ_{a\lambda}.
\]

Here

\[
(1-a)\bar q
=\frac12\cdot\frac32
=\frac34.
\]

Therefore

\[
Q_\lambda'(p^+)
=\frac34+\frac12Q_{\log2}(p^+),
\]

and

\[
Q_\lambda'(p^-)
=\frac34+\frac12Q_{\log2}(p^-).
\]

Because the two `Q_{log 2}` values differ,

\[
\boxed{
Q_\lambda'(p^+)\ne Q_\lambda'(p^-).
}
\]

Yet the initial macrostates satisfy

\[
\boxed{
(\bar q^+,Q_\lambda(p^+))
=(\bar q^-,Q_\lambda(p^-)).
}
\]

This is the required exact failure of scalar dynamic closure.

## 9. Relation to the historical witness

The historical MF-R049 witness uses

\[
\lambda=\log2,
\qquad
a=\frac12,
\]

and its difference direction is proportional to

\[
(-1,4,-5,2),
\]

whose polynomial is

\[
2z^3-5z^2+4z-1
=(z-1)^2(2z-1).
\]

Thus the historical witness follows the same root mechanism with initial base `r=1/2`. Its rescaled base is `1/sqrt(2)`, which explains the exact `sqrt(2)` terms in the archived calculation.

The new witness simply selects the rational-square base `r=(1/2)^2=1/4`, keeping the same mathematical mechanism while making both relevant moments rational.

## 10. Frozen formalization contract

The first Lean attempt must check, from definitions and without importing numerical audit outputs as axioms:

1. all eight frozen probabilities are strictly positive;
2. each probability vector sums exactly to `1`;
3. both means are exactly `3/2`;
4. both base-`1/4` moments are exactly `85/256`;
5. the base-`1/2` moments are exactly `19/40` and `37/80`;
6. their difference is exactly `1/80`;
7. a small analytic bridge proves equality/inequality of `Q_lambda` from equality/inequality of positive exponential moments at fixed nonzero `lambda`;
8. the centered-contraction transport identity is applied with `a=1/2` and `lambda=2 log 2` to obtain unequal next scores.

The rational arithmetic layer should be formalized separately from the `exp`/`log` bridge so that failures in analytic library plumbing cannot obscure the finite counterexample.

## 11. Nonclaims

This witness does **not** establish:

- that no finite-dimensional closure can exist on a restricted distribution family;
- that four support points are globally minimal for every formulation of non-closure;
- that the whole curve `lambda -> Q_lambda` is always the unique minimal state;
- a new theorem resolving the general moment-closure problem;
- novelty or priority of transform non-identifiability;
- any physical law or empirical claim.

Its role is narrower: it gives an exact, strictly positive, four-point, rational-arithmetic witness for the already selected MF-R049 existence claim and is designed to expose that claim cleanly to the Lean kernel.
