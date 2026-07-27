# Dual Envelopes and the Exact Value of the First Channel

**Programme:** Modal Field Research Programme  
**Provisional audit:** A68  
**Author line:** Felipe Gianini Romero  
**Status:** exact dual-envelope and channel-removal theorem for the five A67 family members; not an arbitrary-support theorem

## Technical abstract

A67 proved that the first-anchor minimax curve is globally increasing for the
central-mean family

\[
M=5,6,7,8,9.
\]

A68 identifies the dual mechanism behind that result.

The direct-\(Q\) Charnes–Cooper programme has two hidden distributions,
\(p\) and \(q\), a scale variable \(t\), and observation bands

\[
-\;2\varepsilon_jt
\le
L_p(\lambda_j)-L_q(\lambda_j)
\le
2\varepsilon_jt.
\]

Its dual constructs two affine-exponential envelopes of the target function

\[
\phi_\mu(x)=2^{-\mu x}.
\]

Let

\[
w_j
=
\lambda_j^+-\lambda_j^-,
\]

where \(\lambda_j^\pm\ge0\) are the dual multipliers of the positive and
negative observation bands.

The upper envelope is

\[
\boxed{
U(x)
=
A+Cx+\sum_jw_j\phi_{\lambda_j}(x)
\ge
\phi_\mu(x).
}
\]

The lower envelope is

\[
\boxed{
L(x)
=
\frac{
-B-Dx+\sum_jw_j\phi_{\lambda_j}(x)
}{
\rho
}
\le
\phi_\mu(x).
}
\]

At the minimax optimum:

- \(U(x)=\phi_\mu(x)\) on the active support of \(p\);
- \(L(x)=\phi_\mu(x)\) on the active support of \(q\);
- the same exponential coefficients \(w_j\) appear in both envelopes;
- the noise tolerances enter the scalar dual budget through
  \[
  2\sum_j
  \varepsilon_j
  (\lambda_j^++\lambda_j^-).
  \]

Across all 33 exact phases of A67:

\[
\boxed{
\lambda_\alpha^+>0,
\qquad
\lambda_\alpha^-=0.
}
\]

Thus

\[
\boxed{
w_\alpha>0
}
\]

throughout the entire family.

By the parametric LP envelope theorem,

\[
\boxed{
\frac{\partial\rho^\star}
{\partial\varepsilon_\alpha}
=
2t^\star\lambda_\alpha^+
>0.
}
\]

For the future-score risk,

\[
Q^\star
=
\frac12\log_2\rho^\star,
\]

we obtain

\[
\boxed{
\frac{\partial Q^\star}
{\partial\varepsilon_\alpha}
=
\frac{
t^\star\lambda_\alpha^+
}{
(\log2)\rho^\star
}
>0.
}
\]

Therefore the precision of the first channel has strictly positive marginal
value in every exact phase.

The other channels do not have this property:

- the \(\beta\) channel is inactive in 5 phases;
- the \(\gamma\) channel is inactive in 5 phases;
- the active sign of \(\gamma\) changes;
- \(\alpha\) is positively active in all 33 phases.

A68 then removes the \(\alpha\) observation entirely and solves the remaining
two-anchor programmes exactly in primal and dual form.

For each support,

\[
\boxed{
\rho_M^{-\alpha}
=
\lim_{\alpha\to3^-}
\rho_M(\alpha).
}
\]

Hence coalescing \(\alpha\) with the second anchor is informationally
equivalent to deleting the first channel.

The removal raises the future risk by factors between

\[
\boxed{3.6308}
\]

and

\[
\boxed{9.1181}.
\]

This turns the first-boundary law into a channel-value statement:

\[
\boxed{
\text{the first observation is never locally redundant and its removal has a
strict, exactly certified minimax cost.}
}
\]

---

## 1. Primal programme

Let

\[
c_x=2^{-\mu x}
\]

be the target transform and

\[
a_{j,x}=2^{-\lambda_jx}
\]

the observed transforms.

After Charnes–Cooper scaling, the programme maximizes

\[
c^\top p
\]

subject to

\[
\mathbf1^\top p=t,
\qquad
\mathbf1^\top q=t,
\]

\[
x^\top p=mt,
\qquad
x^\top q=mt,
\]

\[
c^\top q=1,
\]

and

\[
-2\varepsilon_jt
\le
a_j^\top(p-q)
\le
2\varepsilon_jt.
\]

The optimum is the worst target ratio

\[
\rho^\star.
\]

---

## 2. Dual sandwich derivation

Assign unrestricted dual variables

\[
A,B,C,D,R
\]

to the two normalization equations, the two mean equations, and the target
denominator equation.

Assign nonnegative multipliers

\[
\lambda_j^+,\lambda_j^-
\]

to the two sides of each observation band.

The \(p_x\) dual inequalities are

\[
A+Cx+
\sum_j
(\lambda_j^+-\lambda_j^-)
a_{j,x}
\ge
c_x.
\]

These define the upper envelope.

The \(q_x\) inequalities are

\[
B+Dx-
\sum_j
(\lambda_j^+-\lambda_j^-)
a_{j,x}
+
Rc_x
\ge0.
\]

At optimum,

\[
R=\rho^\star.
\]

Rearranging gives the lower envelope.

The scale-variable inequality is

\[
-A-B-mC-mD
\ge
2\sum_j
\varepsilon_j
(\lambda_j^++\lambda_j^-).
\]

It states that the affine parts of the two envelopes must finance the complete
noise penalty.

---

## 3. Contact geometry

Complementary slackness gives:

\[
p_x>0
\quad\Longrightarrow\quad
U(x)=\phi_\mu(x),
\]

and

\[
q_x>0
\quad\Longrightarrow\quad
L(x)=\phi_\mu(x).
\]

Thus the primal support points are exactly the contact points of the dual
sandwich.

This provides a geometric reading of the phase changes in A66 and A67:

- a primal state enters or leaves when a new envelope contact appears or
  disappears;
- an observation band becomes inactive when its dual coefficient vanishes;
- a band changes sign when the corresponding exponential changes its role in
  the sandwich.

The first exponential does not undergo those changes in the declared family.

---

## 4. Exact channel activity

Across the 33 A67 phases:

| Channel status | Phase count |
|---|---:|
| \(\alpha\), positive band active | 33 |
| \(\alpha\), negative band active | 0 |
| \(\alpha\), inactive | 0 |
| \(\beta\), negative band active | 28 |
| \(\beta\), inactive | 5 |
| \(\gamma\), positive band active | 21 |
| \(\gamma\), negative band active | 7 |
| \(\gamma\), inactive | 5 |

Therefore:

\[
\boxed{
\alpha
\text{ is the only observation channel with one fixed active sign in every
phase.}
}
\]

The positive \(\alpha\) band means:

\[
L_p(\alpha)-L_q(\alpha)
=
2\varepsilon_\alpha t.
\]

The adversarial distributions always use the full allowed discrepancy in this
direction.

---

## 5. Parametric value theorem

Treat \(\varepsilon_\alpha\) as an independent channel tolerance while holding
the other tolerances fixed.

The active positive constraint is

\[
L_p(\alpha)-L_q(\alpha)
-
2\varepsilon_\alpha t
\le0.
\]

Let its dual multiplier be \(\lambda_\alpha^+\).

The LP envelope theorem gives

\[
\frac{\partial\rho^\star}
{\partial\varepsilon_\alpha}
=
-\lambda_\alpha^+
\frac{\partial}{
\partial\varepsilon_\alpha}
\left[
L_p(\alpha)-L_q(\alpha)
-
2\varepsilon_\alpha t
\right].
\]

Therefore:

\[
\frac{\partial\rho^\star}
{\partial\varepsilon_\alpha}
=
2t^\star\lambda_\alpha^+.
\]

A67 certified exactly that:

\[
t^\star>0
\]

and

\[
\lambda_\alpha^+>0
\]

throughout every phase.

Hence loosening the first-channel error strictly worsens the minimax ratio on
every phase interior.

Equivalently, improving its precision strictly improves the achievable
robust bound.

---

## 6. Removal and coalescence theorem

Deleting the first channel leaves the designs

\[
\{3,\gamma_M\}.
\]

Every resulting two-anchor programme was solved independently in exact
rational primal and dual form.

| \(M\) | Remaining anchors | Full \(Q_M(2)\) | Removed-channel \(Q_M^{-\alpha}\) | Absolute premium | Risk multiplier |
|---:|---:|---:|---:|---:|---:|
| 5 | [3, 10] | 0.009768145211376 | 0.089066653294910 | 0.079298508083534 | 9.118072× |
| 6 | [3, 5] | 0.023987956688136 | 0.182519257439987 | 0.158531300751851 | 7.608787× |
| 7 | [3, 4] | 0.055903711799154 | 0.271663518174007 | 0.215759806374853 | 4.859490× |
| 8 | [3, 4] | 0.092385313965809 | 0.362292312716144 | 0.269906998750334 | 3.921536× |
| 9 | [3, 4] | 0.126337828822730 | 0.458704035944579 | 0.332366207121849 | 3.630773× |

For every support:

\[
\boxed{
\rho_M^{-\alpha}
=
\lim_{\alpha\to3^-}\rho_M(\alpha).
}
\]

This identity has a direct informational meaning.

As

\[
\alpha\to3^-,
\]

the first and second observations become identical:

\[
2^{-\alpha x}
\longrightarrow
2^{-3x}.
\]

The nominal three-channel design loses one independent direction and becomes
the two-channel design.

The equality is not only a qualitative rank argument. The exact rational
two-anchor primal and dual values coincide with the exact A67 coalescence
fractions.

---

## 7. Quantitative value of the first channel

The risk multipliers are:

\[
9.1181,\;
7.6088,\;
4.8595,\;
3.9215,\;
3.6308
\]

for

\[
M=5,6,7,8,9.
\]

The relative multiplier decreases with \(M\), but the absolute risk premium
increases:

\[
0.07930,\;
0.15853,\;
0.21576,\;
0.26991,\;
0.33237.
\]

This happens because the baseline ambiguity itself grows with the number of
hidden states.

The correct conclusion is not that the first channel becomes less useful for
larger supports. It is:

> relative to an already larger uncertainty floor, its multiplicative effect
> becomes smaller, while the absolute ambiguity prevented by the channel
> becomes larger.

---

## 8. Structural interpretation

The dual sandwich explains why the first anchor differs from the completion
anchors.

The target transform has exponent

\[
\mu=1.
\]

Among the allowed observations, \(\alpha\) is the closest exponential to the
target.

Its positive coefficient helps the upper envelope follow the target at the
active \(p\)-contacts while simultaneously lowering the shared lower-envelope
expression at the active \(q\)-contacts.

Removing it forces the affine terms and more rapidly decaying exponentials to
bridge a much larger functional gap.

The exact coalescence/removal identity confirms that this is genuine
independent information, not merely a numerically favorable coordinate.

---

## 9. Logical status

### Established exactly

1. Dual upper/lower envelope representation.
2. Contact interpretation of the primal supports.
3. Positive \(\alpha\)-band activity in all 33 phases.
4. Positive first-channel shadow price throughout every phase.
5. Strictly positive marginal cost of first-channel tolerance.
6. Exact two-anchor primal–dual removal certificates for all five supports.
7. Exact equality of channel removal and the coalescence limit.
8. Strict risk deterioration after removal.

### Not established

1. A positive-\(\alpha\) multiplier theorem for arbitrary support size.
2. A proof for arbitrary means, targets, or completion anchors.
3. A lower bound on the shadow price uniform in all \(M\).
4. A theorem under correlated observation bands.
5. A continuous microscopic-support version.
6. A physical interpretation of the dual coefficients.

---

## 10. Next rigorous target

A68 identifies the mechanism, but the positivity of

\[
\lambda_\alpha^+
\]

is still inherited from the five exact phase decompositions.

The next mathematical target is to prove that sign without enumerating
phases.

The likely route is total positivity of the collocation system

\[
\left\{
1,\;
x,\;
2^{-\alpha x},\;
2^{-3x},\;
2^{-\gamma x},\;
2^{-x}
\right\}.
\]

A possible theorem would state that, under an ordered upper/lower contact
pattern, the Cramer determinant defining \(w_\alpha\) has fixed positive sign.

The next audit should:

1. express \(w_\alpha\) as a ratio of generalized Vandermonde minors;
2. classify the contact-order patterns in the 33 phases;
3. reduce their determinant signs to total positivity;
4. determine whether one oriented-matroid argument covers all patterns.

That would replace phasewise positivity checks with a structural dual-envelope
proof.
