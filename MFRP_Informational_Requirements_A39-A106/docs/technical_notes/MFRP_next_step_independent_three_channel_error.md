# Independent Three-Channel Error Vector and Calibration Priorities

**Programme:** Modal Field Research Programme  
**Provisional audit:** A58  
**Author line:** Felipe Gianini Romero  
**Status:** exact independent-error theorem around the A54 compactified optimum; no empirical covariance or instrument claim

## Technical abstract

A57 allowed the third observation to have its own tolerance while keeping the
first two equal. The present audit releases all three error channels
independently at the compactified optimal design

\[
D^\star
=
\{2,\beta^\star,\infty\}\log2,
\]

where

\[
\beta^\star
=
2.728401216547027876\ldots.
\]

Let the three absolute tolerances be

\[
\varepsilon_2
=
u_2\varepsilon_0,
\]

\[
\varepsilon_\beta
=
u_\beta\varepsilon_0,
\]

\[
\varepsilon_\infty
=
u_\infty\varepsilon_0,
\]

with

\[
\varepsilon_0=10^{-4}.
\]

The complete independent-error box is

\[
\boxed{
1
\le
u_2,u_\beta,u_\infty
\le
\frac{11}{10}.
}
\]

On the exact algebraic isolation interval

\[
s^\star
\in
\left[
\frac3{20},
\frac{19}{125}
\right],
\]

one Charnes–Cooper primal–dual basis remains globally optimal throughout the
entire four-dimensional box

\[
(s,u_2,u_\beta,u_\infty).
\]

Its direct minimax ratio is an exact linear-fractional function

\[
\rho(s,u_2,u_\beta,u_\infty).
\]

All active primal variables, inequality dual multipliers, and nonbasic
reduced costs are certified nonnegative by exact tensor-product Bernstein
coefficients.

The ratio is strictly increasing in each independent error factor:

\[
\boxed{
\frac{\partial\rho}{\partial u_2}>0,
\qquad
\frac{\partial\rho}{\partial u_\beta}>0,
\qquad
\frac{\partial\rho}{\partial u_\infty}>0.
}
\]

Moreover, throughout the complete certified box,

\[
\boxed{
\frac{\partial Q}{\partial u_2}
>
4
\frac{\partial Q}{\partial u_\infty},
}
\]

and

\[
\boxed{
\frac{\partial Q}{\partial u_\beta}
>
4
\frac{\partial Q}{\partial u_\infty}.
}
\]

Thus the two lower-exponent channels are uniformly more than four times as
important to calibrate than the compactified channel, per equal fractional
increase in their absolute-error factors.

At the baseline point

\[
(u_2,u_\beta,u_\infty)
=
(1,1,1),
\]

the future-risk sensitivities are

\[
\boxed{
\lambda_2
=
0.0017858958907759984854\ldots,
}
\]

\[
\boxed{
\lambda_\beta
=
0.0017175563019995716054\ldots,
}
\]

\[
\boxed{
\lambda_\infty
=
0.0003626282234755227507\ldots.
}
\]

The local exchange rates are therefore

\[
\frac{\lambda_2}{\lambda_\infty}
=
4.924864\ldots,
\]

\[
\frac{\lambda_\beta}{\lambda_\infty}
=
4.736412\ldots.
\]

In first order, a one-percentage-point deterioration in the first channel
has approximately the same risk effect as a \(4.92\)-percentage-point
deterioration in the extreme channel.

The baseline risk is

\[
Q^\star
=
0.0095832452322186017096\ldots.
\]

If all three channels deteriorate independently by the maximum certified
10%,

\[
(u_2,u_\beta,u_\infty)
=
(1.1,1.1,1.1),
\]

the exact risk becomes

\[
0.0099690857432755532297\ldots.
\]

The absolute increase is

\[
0.0003858405110569515201\ldots,
\]

or

\[
\boxed{
4.02619886799689\%
}
\]

relative to the baseline risk.

The individual 10% deteriorations produce:

| Deteriorated channel | Absolute risk increase | Relative increase |
|---|---:|---:|
| \(2\) | \(1.7846757488\times10^{-4}\) | 1.86229% |
| \(\beta^\star\) | \(1.7158871152\times10^{-4}\) | 1.79051% |
| \(\infty\) | \(3.6250758231\times10^{-5}\) | 0.37827% |

The practical conclusion is:

\[
\boxed{
\text{calibration effort should prioritize the two lower channels before
the extreme channel.}
}
\]

---

## 1. Independent error-vector contract

The microscopic class remains

\[
\operatorname{supp}P
\subseteq
\{0,1,2,3,4,5\},
\]

\[
\mathbb E[X]
=
\frac52.
\]

The target is

\[
L_P(\log2).
\]

The three observation differences satisfy

\[
\left|
L_p(2\log2)-L_q(2\log2)
\right|
\le
2u_2\varepsilon_0,
\]

\[
\left|
L_p(\beta^\star\log2)
-
L_q(\beta^\star\log2)
\right|
\le
2u_\beta\varepsilon_0,
\]

\[
|p_0-q_0|
\le
2u_\infty\varepsilon_0.
\]

The future-score risk is

\[
Q
=
\frac12\log_2\rho.
\]

---

## 2. Exact active basis

The support pattern is

\[
\operatorname{supp}p
=
\{0,1,3,5\},
\]

\[
\operatorname{supp}q
=
\{1,2,4\}.
\]

The active signs remain

\[
2:+,
\qquad
\beta^\star:-,
\qquad
\infty:+.
\]

The exact symbolic solution yields:

- eight active Charnes–Cooper primal variables;
- three inequality dual multipliers;
- five nonzero nonbasic reduced costs;
- one exact linear-fractional ratio.

All sixteen sign conditions are certified directly on the complete box using
tensor-product Bernstein coefficients. No floating-point grid is used as the
proof.

---

## 3. Coordinatewise monotonicity

The exact ratio derivatives satisfy

\[
\partial_{u_2}\rho>0,
\]

\[
\partial_{u_\beta}\rho>0,
\]

\[
\partial_{u_\infty}\rho>0.
\]

Since the logarithm is increasing, the same coordinatewise monotonicity holds
for the future risk \(Q\).

Therefore the minimum within the error box is the baseline corner

\[
(1,1,1),
\]

and the maximum is the fully deteriorated corner

\[
\left(
\frac{11}{10},
\frac{11}{10},
\frac{11}{10}
\right).
\]

This gives exact robust lower and upper risk bounds without enumerating
interior error vectors.

---

## 4. Uniform calibration-priority theorem

At a common point in the error box, all risk derivatives share the same
positive factor

\[
\frac{1}{2(\log2)\rho}.
\]

Therefore derivative comparisons can be certified directly using the ratio
derivatives.

The exact Bernstein certificates prove

\[
\partial_{u_2}\rho
-
4\partial_{u_\infty}\rho
>0,
\]

and

\[
\partial_{u_\beta}\rho
-
4\partial_{u_\infty}\rho
>0.
\]

Consequently:

### Theorem 4.1

Throughout the entire certified independent-error box, reducing either lower
channel's error factor produces more than four times the local risk benefit
of reducing the extreme-channel factor by the same amount.

The theorem does not impose a fixed ordering between the first and second
channels throughout the whole box. Their sensitivities are close enough that
their ordering can change locally. Both remain uniformly more consequential
than the third.

---

## 5. Baseline differential error budget

At the baseline point,

\[
dQ
=
\lambda_2\,du_2
+
\lambda_\beta\,du_\beta
+
\lambda_\infty\,du_\infty
+
O(\|du\|^2).
\]

Numerically,

\[
dQ
\approx
0.00178589589\,du_2
+
0.00171755630\,du_\beta
+
0.00036262822\,du_\infty.
\]

This gives a first-order calibration budget.

For example, a small deterioration \(\delta\) in \(u_2\) can only be
compensated, to first order, by improving the extreme channel by approximately

\[
4.924864\,\delta.
\]

Likewise, a small deterioration in \(u_\beta\) requires approximately

\[
4.736412\,\delta
\]

of compensating improvement in \(u_\infty\).

These exchange rates are local statements at the baseline optimum. The exact
nonlinear ratio remains available for finite changes inside the certified
box.

---

## 6. Robust corner bounds

Because risk increases in every coordinate,

\[
Q(1,1,1)
\le
Q(u_2,u_\beta,u_\infty)
\le
Q(1.1,1.1,1.1).
\]

The exact numerical interval is

\[
\boxed{
0.00958324523221860
\le
Q
\le
0.00996908574327555.
}
\]

Thus arbitrary independent error deteriorations of at most 10% cannot increase
the future risk by more than approximately 4.0262% relative to baseline.

---

## 7. Interpretation

A measurement system often has several separately calibrated channels. Equal
nominal tolerances do not imply equal informational importance.

A58 identifies the sensitivity structure:

- the lower boundary observation is highly influential;
- the interior observation is almost equally influential;
- the compactified observation is substantially less sensitive to an equal
  proportional deterioration.

This means engineering effort should not be distributed equally merely
because the channels report errors in the same units.

The result supplies a quantitative priority ordering before a full covariance
model is introduced.

---

## 8. Logical status

### Established

1. One exact active basis covers the full independent three-error box.
2. Each error factor worsens minimax risk monotonically.
3. The two lower channels are uniformly more than four times as sensitive as
   the extreme channel.
4. Exact baseline gradient components are supplied.
5. Exact local error-exchange rates are supplied.
6. Exact robust corner risk bounds are supplied.
7. The equal-error A54 optimum is reproduced at the baseline corner.

### Not established

1. Error factors below one are not included in the certified box.
2. Factors above \(1.1\) are not jointly certified here.
3. The errors remain independent box uncertainties.
4. No covariance or common-mode error is included.
5. The anchor \(\beta^\star\) is not reoptimized as the error vector changes.
6. No real apparatus calibration values are supplied.

---

## 9. Next rigorous target

The independent error vector is now controlled locally and nonlinearly.

The next step is to replace the error box by a correlated ellipsoid,

\[
e^\top\Sigma^{-1}e\le1,
\]

and compare:

- common-mode errors;
- anti-correlated errors;
- independent errors with the same marginal scales.

That will identify whether correlation makes the experiment safer or more
adversarial than the independent-box model.
