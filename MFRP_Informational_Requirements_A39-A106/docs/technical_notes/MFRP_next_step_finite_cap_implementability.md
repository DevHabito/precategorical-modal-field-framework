# Finite-Cap Implementability of the Compactified Optimal Design

**Programme:** Modal Field Research Programme  
**Provisional audit:** A55  
**Author line:** Felipe Gianini Romero  
**Status:** exact finite-cap implementability theorem under the A54 contract; no physical instrument claim

## Technical abstract

A54 proved the complete global minimax theorem for the positive-noise design
class with allowed observation exponents

\[
\eta\in[2,\infty].
\]

The globally optimal three-point design is

\[
D^\star
=
\{2,\beta^\star,\infty\}\log2,
\]

where

\[
\beta^\star
=
2.728401216547027876\ldots
\]

and

\[
\mathcal R^{Q,\star}
=
0.0095832452322186017096\ldots.
\]

The compactified endpoint \(\infty\) is mathematically exact but not literally
an instrument setting. The present audit asks:

> How large must a finite third exponent \(\Gamma\) be to reproduce the
> compactified optimum to a declared accuracy?

Fix

\[
D_\Gamma
=
\{2,\beta^\star,\Gamma\}\log2.
\]

Set

\[
r=2^{-\Gamma}.
\]

For every

\[
\Gamma\ge6,
\qquad
0\le r\le\frac1{64},
\]

the same active primal–dual basis as the compactified A52 optimum remains
exactly feasible and globally optimal for the fixed design \(D_\Gamma\).
The resulting exact ratio is a rational function

\[
\rho_{\mathrm{fix}}(r)
=
R(s^\star,r),
\]

where \(s^\star=2^{-\beta^\star}\) is the A52 algebraic stationary root.

A54 supplies a universal lower bound for every finite-cap design, while
\(D_\Gamma\) supplies an attainable upper bound. Therefore the fully
reoptimized finite-cap risk obeys the exact sandwich

\[
\boxed{
0
\le
\mathcal R_{\Gamma}^{Q,\mathrm{opt}}
-
\mathcal R^{Q,\star}
\le
\mathcal R_{\Gamma}^{Q,\mathrm{fix}}
-
\mathcal R^{Q,\star}.
}
\]

Near the compactified endpoint,

\[
\boxed{
\mathcal R_{\Gamma}^{Q,\mathrm{fix}}
=
\mathcal R^{Q,\star}
+
\kappa_Q\,2^{-\Gamma}
+
O(4^{-\Gamma}),
}
\]

with

\[
\boxed{
\kappa_Q
=
0.0020308153065398546459\ldots.
}
\]

Thus the implementation error decays exponentially with the finite cap.

Exact certified evaluations give:

| Finite cap \(\Gamma\) | Fixed-\(\beta^\star\) risk | Absolute excess | Relative excess |
|---:|---:|---:|---:|
| 6 | 0.00964471716206734 | \(6.1472\times10^{-5}\) | 0.64145% |
| 8 | 0.00959290101302357 | \(9.6558\times10^{-6}\) | 0.10076% |
| 9 | 0.00958763724503648 | \(4.3920\times10^{-6}\) | 0.04583% |
| 10 | 0.00958533421302621 | \(2.0890\times10^{-6}\) | 0.02180% |
| 12 | 0.00958374761763959 | \(5.0239\times10^{-7}\) | 0.00524% |
| 14 | 0.00958336959419999 | \(1.2436\times10^{-7}\) | 0.00130% |
| 16 | 0.00958327624567214 | \(3.1013\times10^{-8}\) | 0.000324% |
| 20 | 0.00958324716905527 | \(1.9368\times10^{-9}\) | 0.0000202% |

Because the right side is an upper bound on the **fully reoptimized** cap
penalty, these values are conservative guarantees.

Practical rules follow:

- \(\Gamma=9\) guarantees less than \(0.05\%\) relative degradation;
- \(\Gamma=12\) guarantees less than \(0.01\%\);
- \(\Gamma=15\) guarantees less than \(0.001\%\);
- \(\Gamma=18\) guarantees less than \(0.0001\%\).

The result converts the compactified mathematical optimum into a finite,
quantitatively controlled approximation.

---

## 1. Finite-cap contract

The microscopic class remains

\[
\mathcal P_{5/2}
=
\left\{
p_x\ge0:
\sum_{x=0}^{5}p_x=1,
\quad
\sum_{x=0}^{5}xp_x=\frac52
\right\}.
\]

The target is

\[
L_p(\log2).
\]

The observation tolerance is

\[
\varepsilon=10^{-4}.
\]

For a finite cap \(\Gamma\), use

\[
D_\Gamma
=
\{2,\beta^\star,\Gamma\}\log2.
\]

The direct minimax ratio is

\[
\rho_\Gamma
=
\max_{p,q}
\frac{L_p(\log2)}{L_q(\log2)}
\]

subject to the three observation differences lying within

\[
[-2\varepsilon,2\varepsilon].
\]

The future-score width is

\[
\mathcal R_\Gamma^Q
=
\frac12\log_2\rho_\Gamma.
\]

---

## 2. Exact finite-\(r\) active basis

Set

\[
s=2^{-\beta},
\qquad
r=2^{-\Gamma}.
\]

Use the A52 support pattern

\[
\operatorname{supp}p=\{0,1,3,5\},
\]

\[
\operatorname{supp}q=\{1,2,4\},
\]

with the three active signs

\[
2:+,
\qquad
\beta:-,
\qquad
\Gamma:+.
\]

The Charnes–Cooper system is solved symbolically in \(s\) and \(r\).
It yields:

- rational primal variables;
- rational dual variables;
- rational reduced costs;
- a rational objective \(R(s,r)\).

At \(r=0\), this basis reduces exactly to the final A52 phase.

---

## 3. Exact validity region

The A52 stationary root satisfies

\[
s^\star\in
\left[
\frac3{20},
\frac{19}{125}
\right].
\]

The finite-cap rectangle is

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
\right].
\]

Every sign required for primal–dual optimality is certified on this full
rectangle:

1. all active primal variables are nonnegative;
2. the Charnes–Cooper scale is positive;
3. all inequality dual multipliers are nonnegative;
4. every nonbasic reduced cost is nonnegative;
5. every relevant denominator has fixed nonzero sign;
6. primal and dual objectives agree identically.

The certificates use exact tensor-product Bernstein expansions with adaptive
rational subdivision. No floating-point grid is used for the proof.

Therefore, for every

\[
\Gamma\ge6,
\]

\[
\boxed{
\rho_{\mathrm{fix}}(\Gamma)
=
R(s^\star,2^{-\Gamma})
}
\]

is the exact minimax ratio of the fixed design

\[
\{2,\beta^\star,\Gamma\}.
\]

---

## 4. Global finite-cap sandwich

A54 proves that every design whose observed exponents satisfy \(\eta\ge2\)
has risk at least

\[
\mathcal R^{Q,\star}.
\]

Therefore the globally reoptimized finite-cap problem satisfies

\[
\mathcal R_{\Gamma}^{Q,\mathrm{opt}}
\ge
\mathcal R^{Q,\star}.
\]

The fixed design

\[
\{2,\beta^\star,\Gamma\}
\]

is admissible, so

\[
\mathcal R_{\Gamma}^{Q,\mathrm{opt}}
\le
\mathcal R_{\Gamma}^{Q,\mathrm{fix}}.
\]

Combining:

\[
\boxed{
\mathcal R^{Q,\star}
\le
\mathcal R_{\Gamma}^{Q,\mathrm{opt}}
\le
\mathcal R_{\Gamma}^{Q,\mathrm{fix}}.
}
\]

This theorem does not require solving the finite-cap joint optimization.

---

## 5. Exponential convergence

The exact fixed-design ratio is analytic at \(r=0\). Write

\[
R(s^\star,r)
=
R^\star
+
\kappa_R r
+
O(r^2).
\]

The exact first derivative is

\[
\kappa_R
=
\left.
\frac{\partial R}{\partial r}
\right|_{(s^\star,0)}
=
0.0028529592817991496716\ldots.
\]

Passing to the future score gives

\[
\mathcal R_{\mathrm{fix}}^Q(r)
=
\mathcal R^{Q,\star}
+
\frac{\kappa_R}
{2(\log2)R^\star}
r
+
O(r^2).
\]

Hence

\[
\kappa_Q
=
\frac{\kappa_R}
{2(\log2)R^\star}
=
0.0020308153065398546459\ldots.
\]

Since

\[
r=2^{-\Gamma},
\]

\[
\boxed{
\mathcal R_{\Gamma}^{Q,\mathrm{fix}}
-
\mathcal R^{Q,\star}
=
\kappa_Q2^{-\Gamma}
+
O(4^{-\Gamma}).
}
\]

Each unit increase in \(\Gamma\) asymptotically halves the remaining cap
penalty.

---

## 6. Practical finite-cap guarantees

The exact fixed-design evaluations imply conservative upper guarantees for
the fully optimized finite-cap problem.

### Less than \(0.1\%\) degradation

\[
\Gamma=9
\]

is sufficient. The relative upper gap is approximately

\[
0.04583\%.
\]

### Less than \(0.01\%\)

\[
\Gamma=12
\]

is sufficient:

\[
0.00524\%.
\]

### Less than \(0.001\%\)

\[
\Gamma=15
\]

is sufficient:

\[
0.000648\%.
\]

### Less than \(0.0001\%\)

\[
\Gamma=18
\]

is sufficient:

\[
0.0000809\%.
\]

These are guarantees, not just best-fit extrapolations.

---

## 7. Interpretation

The symbol \(\gamma=\infty\) does not require a physically infinite
instrument setting.

It denotes the limit in which

\[
L_p(\gamma\log2)
\longrightarrow
p_0.
\]

A finite exponent approximates this limit exponentially quickly because the
remaining support contributions scale as

\[
2^{-\Gamma x}.
\]

The theorem quantifies exactly how quickly the approximation becomes
minimax-equivalent.

In practical terms:

- a moderate finite cap can already reproduce the optimal information;
- pushing the cap further gives exponentially diminishing returns;
- the appropriate cap can be chosen from an explicit accuracy requirement.

---

## 8. Logical status

### Established

1. The compactified A52 active basis extends exactly to every
   \(\Gamma\ge6\) at fixed \(\beta^\star\).
2. Its primal and dual certificates remain valid on the full finite-cap
   rectangle.
3. The fixed-design ratio is an exact rational function of
   \(s^\star\) and \(2^{-\Gamma}\).
4. The finite-cap globally reoptimized risk is sandwiched between the A54
   floor and the fixed-design value.
5. The cap penalty decays as \(2^{-\Gamma}\).
6. Exact conservative finite-cap accuracy thresholds are supplied.
7. The compactified optimum is operationally approximable without requiring
   a literal infinite parameter.

### Not established

1. The exact jointly reoptimized value of \(\beta\) is not derived for every
   finite \(\Gamma\).
2. No instrument cost is assigned to increasing \(\Gamma\).
3. No empirical apparatus maps exponent \(\Gamma\) to a real control setting.
4. No unequal-error or continuous-support extension is included.
5. No physical status is assigned to the finite-cap thresholds.

---

## 9. Next rigorous target

The compactified endpoint is now mathematically and operationally controlled.

The next meaningful extension is to introduce a precision profile

\[
\varepsilon(\eta)
\]

or a measurement cost

\[
C(\eta).
\]

That would determine an economically optimal finite cap instead of choosing
\(\Gamma\) solely from an accuracy tolerance.
