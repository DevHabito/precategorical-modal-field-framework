# Heteroscedastic Third-Channel Error and Exact Upgrade Thresholds

**Programme:** Modal Field Research Programme  
**Provisional audit:** A57  
**Author line:** Felipe Gianini Romero  
**Status:** exact profile-agnostic stopping theorem inside a certified heteroscedastic region; no empirical noise claim

## Technical abstract

A55 and A56 treated the third observation

\[
\Gamma\log2
\]

with the same absolute tolerance as the two lower observations. The present
audit allows the third channel to have its own tolerance.

The first two observations retain

\[
\varepsilon_0=10^{-4}.
\]

The third observation receives

\[
\varepsilon_3=t\varepsilon_0,
\qquad
1\le t\le\frac74.
\]

The design family remains

\[
D_{\Gamma,t}
=
\{2,\beta^\star,\Gamma\}\log2,
\qquad
\Gamma\ge6,
\]

where

\[
\beta^\star
=
2.728401216547027876\ldots.
\]

Set

\[
s^\star=2^{-\beta^\star},
\qquad
r=2^{-\Gamma}.
\]

On the full rational box

\[
s\in
\left[
\frac3{20},
\frac{19}{125}
\right],
\qquad
r\in
\left[
0,\frac1{64}
\right],
\qquad
t\in
\left[
1,\frac74
\right],
\]

one exact Charnes–Cooper primal–dual basis remains globally optimal for the
fixed design. Its ratio is a rational function

\[
\rho(s,r,t).
\]

The exact sign certificates prove

\[
\boxed{
\frac{\partial\rho}{\partial r}>0
}
\]

and

\[
\boxed{
\frac{\partial\rho}{\partial t}>0.
}
\]

Thus risk worsens both when the finite cap is less extreme and when the third
channel becomes noisier.

For any current noise factor \(t_\Gamma\), define the break-even next-channel
factor \(\Theta_\Gamma(t_\Gamma)\) by

\[
\rho
\left(
s^\star,
2^{-(\Gamma+1)},
\Theta_\Gamma(t_\Gamma)
\right)
=
\rho
\left(
s^\star,
2^{-\Gamma},
t_\Gamma
\right).
\]

Because \(\rho\) is strictly increasing in \(t\), this solution is unique.
The exact upgrade rule is:

\[
\boxed{
t_{\Gamma+1}<\Theta_\Gamma(t_\Gamma)
\Longleftrightarrow
Q_{\Gamma+1}<Q_\Gamma.
}
\]

Equality gives a tie; a larger next-channel tolerance makes the upgrade
counterproductive.

This is profile-agnostic. It applies after an experimental error curve
\(t_\Gamma\) has been measured, without assuming a linear, exponential, or
monetary model.

Starting from a baseline third-channel factor \(t_\Gamma=1\), the maximum
allowed next factor is:

| Upgrade | Maximum \(t_{\Gamma+1}\) | Allowed tolerance increase |
|---:|---:|---:|
| \(6\to7\) | 1.096664102854524 | 9.666410% |
| \(7\to8\) | 1.034920201716912 | 3.492020% |
| \(8\to9\) | 1.014179564791573 | 1.417956% |
| \(9\to10\) | 1.006277159169278 | 0.627716% |
| \(10\to11\) | 1.002936274951072 | 0.293627% |
| \(11\to12\) | 1.001417662479194 | 0.141766% |
| \(12\to13\) | 1.000696224815878 | 0.069622% |
| \(13\to14\) | 1.000344962322909 | 0.034496% |
| \(14\to15\) | 1.000171693829080 | 0.017169% |
| \(15\to16\) | 1.000085650104981 | 0.008565% |
| \(16\to17\) | 1.000042775853037 | 0.004278% |
| \(17\to18\) | 1.000021375627022 | 0.002138% |
| \(18\to19\) | 1.000010684738683 | 0.001068% |
| \(19\to20\) | 1.000005341600640 | 0.000534% |
| \(20\to21\) | 1.000002670608145 | 0.000267% |

The allowed deterioration shrinks exponentially. At the baseline \(t=1\),

\[
\boxed{
\Theta_\Gamma(1)-1
=
C_{\mathrm{noise}}2^{-\Gamma}
+
O(4^{-\Gamma}),
}
\]

where

\[
\boxed{
C_{\mathrm{noise}}
=
2.800134097500734\ldots.
}
\]

This yields a practical stopping principle:

\[
\boxed{
\text{move to a more extreme third observation only if its measured
noise increase is below the exact break-even threshold.}
}
\]

---

## 1. Heteroscedastic information contract

Let

\[
L_p(\eta\log2)
=
\sum_{x=0}^{5}p_x2^{-\eta x}.
\]

The microscopic class remains

\[
\operatorname{supp}p\subseteq\{0,1,2,3,4,5\},
\qquad
\mathbb E[X]=\frac52.
\]

The first and second observation constraints are

\[
\left|
L_p(2\log2)-L_q(2\log2)
\right|
\le2\varepsilon_0,
\]

\[
\left|
L_p(\beta^\star\log2)-L_q(\beta^\star\log2)
\right|
\le2\varepsilon_0.
\]

The third constraint is

\[
\left|
L_p(\Gamma\log2)-L_q(\Gamma\log2)
\right|
\le2t\varepsilon_0.
\]

The target remains

\[
L_p(\log2).
\]

The future-score risk is

\[
Q(r,t)
=
\frac12\log_2\rho(s^\star,r,t).
\]

---

## 2. Certified active basis

The active support pattern is inherited from the final A52 phase:

\[
\operatorname{supp}p=\{0,1,3,5\},
\]

\[
\operatorname{supp}q=\{1,2,4\}.
\]

The active signs are:

\[
2:+,
\qquad
\beta^\star:-,
\qquad
\Gamma:+.
\]

All of the following remain nonnegative on the complete
\((s,r,t)\)-box:

1. active primal variables;
2. the Charnes–Cooper scale;
3. inequality dual multipliers;
4. nonbasic reduced costs.

Primal and dual objectives agree identically.

Therefore the rational branch is not merely a local numerical fit; it is the
exact fixed-design minimax solution throughout the certified region.

---

## 3. Monotonicity theorem

The derivative with respect to the finite residual satisfies

\[
\frac{\partial\rho}{\partial r}>0.
\]

Since

\[
r=2^{-\Gamma},
\]

increasing \(\Gamma\) lowers risk when the tolerance factor is held fixed.

The derivative with respect to the third-channel noise factor satisfies

\[
\frac{\partial\rho}{\partial t}>0.
\]

Thus increasing the error band always worsens the minimax risk.

These two monotonic effects compete when moving from one finite cap to the
next.

---

## 4. Exact break-even map

For a current state \((\Gamma,t)\), define \(\Theta_\Gamma(t)\) by

\[
\rho
\left(
s^\star,
2^{-(\Gamma+1)},
\Theta_\Gamma(t)
\right)
=
\rho
\left(
s^\star,
2^{-\Gamma},
t
\right).
\]

The ratio is linear-fractional in the tolerance factor, so
\(\Theta_\Gamma(t)\) has an exact rational expression in

\[
s^\star,
\quad
2^{-\Gamma},
\quad
t.
\]

Because the next-cap risk is strictly increasing in its tolerance factor:

### Theorem 4.1

For any profile values within the certified region,

\[
t_{\Gamma+1}<\Theta_\Gamma(t_\Gamma)
\]

if and only if

\[
Q
\left(
2^{-(\Gamma+1)},
t_{\Gamma+1}
\right)
<
Q
\left(
2^{-\Gamma},
t_\Gamma
\right).
\]

At equality the two settings tie. Above the threshold, moving to the more
extreme observation increases the total minimax uncertainty.

---

## 5. Geometric benefit versus noise penalty

The one-step change can be decomposed exactly:

\[
\begin{aligned}
&
Q
\left(
2^{-(\Gamma+1)},
t_{\Gamma+1}
\right)
-
Q
\left(
2^{-\Gamma},
t_\Gamma
\right)
\\[3pt]
={}&
\underbrace{
Q
\left(
2^{-(\Gamma+1)},
t_{\Gamma+1}
\right)
-
Q
\left(
2^{-(\Gamma+1)},
t_\Gamma
\right)
}_{\text{noise penalty}}
\\
&-
\underbrace{
\left[
Q
\left(
2^{-\Gamma},
t_\Gamma
\right)
-
Q
\left(
2^{-(\Gamma+1)},
t_\Gamma
\right)
\right]
}_{\text{geometric benefit}}.
\end{aligned}
\]

The upgrade helps precisely when

\[
\boxed{
\text{noise penalty}
<
\text{geometric benefit}.
}
\]

This is the heteroscedastic analogue of the A56 cost rule.

---

## 6. Asymptotic tolerance budget

At the compactified endpoint and baseline tolerance,

\[
\lambda_t
=
\left.
\frac{\partial Q}{\partial t}
\right|_{r=0,t=1}
=
0.0003626282234755227507\ldots.
\]

From A55,

\[
\lambda_r
=
\left.
\frac{\partial Q}{\partial r}
\right|_{r=0,t=1}
=
0.0020308153065398546459\ldots.
\]

The geometric benefit of halving \(r\) is asymptotically

\[
\frac{\lambda_r}{2}r.
\]

Equating that benefit to the first-order noise penalty
\(\lambda_t\Delta t\) yields

\[
\Delta t_{\mathrm{crit}}
\sim
\frac{\lambda_r}{2\lambda_t}r.
\]

Hence

\[
C_{\mathrm{noise}}
=
\frac{\lambda_r}{2\lambda_t}
=
2.800134097500734\ldots.
\]

Since \(r=2^{-\Gamma}\),

\[
\Theta_\Gamma(1)-1
=
2.800134097500734\ldots\;2^{-\Gamma}
+
O(4^{-\Gamma}).
\]

The allowable deterioration of the extreme channel therefore halves
asymptotically with every unit increase of the cap.

---

## 7. Interpretation

A larger \(\Gamma\) suppresses unwanted finite-support contributions and moves
the third observation closer to the compactified endpoint.

But a more extreme measurement may also be harder or noisier.

A57 gives the exact balance:

- the geometric improvement is known;
- the noise sensitivity is known;
- the largest acceptable increase in the third-channel error is known.

After a real apparatus supplies measured tolerances
\(\varepsilon_3(\Gamma)\), the policy can be applied directly:

1. compute
   \[
   t_\Gamma
   =
   \frac{\varepsilon_3(\Gamma)}{\varepsilon_0};
   \]
2. compare \(t_{\Gamma+1}\) with
   \(\Theta_\Gamma(t_\Gamma)\);
3. continue only while the measured next tolerance stays below the threshold.

No invented monetary or hardware cost is required.

---

## 8. Logical status

### Established

1. One exact heteroscedastic primal–dual branch covers
   \[
   \Gamma\ge6,
   \qquad
   1\le t\le7/4.
   \]
2. Risk strictly increases with the finite residual \(r\).
3. Risk strictly increases with the third-channel tolerance factor \(t\).
4. Every one-step upgrade has a unique exact break-even next tolerance.
5. The upgrade rule applies to arbitrary measured noise profiles.
6. Baseline break-even thresholds are supplied through \(\Gamma=20\).
7. The admissible tolerance increase decays as \(2^{-\Gamma}\).

### Not established

1. The branch is not certified beyond
   \[
   t=7/4.
   \]
2. The first two observation errors remain fixed and equal.
3. Correlated errors are not included.
4. \(\beta\) is not reoptimized under the heteroscedastic profile.
5. No real instrument error curve has been measured.
6. No physical meaning is assigned to the exponent coordinates.

---

## 9. Next rigorous target

The one-channel heteroscedastic policy is now closed inside its certified
region.

The next extension should allow the complete error vector

\[
(\varepsilon_2,\varepsilon_\beta,\varepsilon_\Gamma)
\]

and then replace the independent error box by a correlated uncertainty set.
That is the natural bridge from abstract tolerance bands to calibrated
experimental covariance.
