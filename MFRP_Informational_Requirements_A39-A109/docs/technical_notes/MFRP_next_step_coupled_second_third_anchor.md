# Coupled Second–Third Anchor Audit

**Programme:** Modal Field Research Programme  
**Provisional audit:** A53  
**Author line:** Felipe Gianini Romero  
**Status:** exact coordinatewise theorem plus global numerical reconnaissance; no claim of a complete two-dimensional global proof

## Technical abstract

A52 released the second anchor while keeping the third observation at the compactified endpoint. It found the unique noisy optimum

\[
\beta^\star
=
2.728401216547027876\ldots
\]

for the design

\[
\{2,\beta,\infty\}\log2
\]

at common absolute tolerance

\[
\varepsilon=10^{-4}.
\]

The present audit couples the second and third anchors:

\[
D(\beta,\gamma)
=
\{2,\beta,\gamma\}\log2,
\qquad
2<\beta<\gamma\le\infty.
\]

The finite-support, exact-mean, target, and future-score contracts are unchanged.

The exact result is:

\[
\boxed{
\gamma^\star(\beta^\star)=\infty.
}
\]

More strongly, the A52 compactified extremal pair at \(\beta^\star\) remains feasible for every finite

\[
\gamma>\beta^\star.
\]

It therefore supplies the same lower bound against every finite third anchor. Since the compactified design attains that bound,

\[
\boxed{
\mathcal R^Q(\beta^\star,\gamma)
\ge
\mathcal R^Q(\beta^\star,\infty)
\qquad
\forall\gamma>\beta^\star.
}
\]

A52 already proved that

\[
\boxed{
\beta^\star
=
\arg\min_{\beta\in[2,4]}
\mathcal R^Q(\beta,\infty).
}
\]

Consequently,

\[
\boxed{
(\beta^\star,\infty)
}
\]

is a **coordinatewise global minimizer**: neither coordinate can be changed alone to improve the minimax risk.

The certified risk is

\[
\boxed{
\mathcal R^{Q,\star}
=
0.0095832452322186017\ldots.
}
\]

A deterministic numerical search over the coupled domain found no better point. Finite-cap optimizations converge monotonically toward the certified coordinatewise solution:

| Third-anchor cap | Numerically optimized \(\beta\) | Future risk |
|---:|---:|---:|
| \(4\) | \(2.69237856\) | \(0.01094524969\) |
| \(6\) | \(2.71942355\) | \(0.00964441024\) |
| \(10\) | \(2.72808865\) | \(0.00958533441\) |
| \(20\) | \(2.72840101\) | \(0.00958324717\) |
| \(\infty\) | \(2.72840122\) | \(0.00958324523\) |

This numerical convergence is strong evidence that the coordinatewise optimum is also the full joint optimum. It is not, by itself, a proof.

A small low-\(\beta\) strip behaves differently: near duplicated lower anchors, some finite third parameters outperform the compactified third observation. Their risks remain numerically far above the candidate optimum, but A53 does not claim an exact global exclusion theorem for that entire two-dimensional strip.

The rigorous verdict is therefore deliberately limited:

\[
\boxed{
\text{exact coordinatewise global optimum, with full 2D globality still open.}
}
\]

---

## 1. Coupled design contract

Let

\[
L_p(\eta\log2)
=
\sum_{x=0}^{5}p_x2^{-\eta x},
\]

with

\[
\operatorname{supp}p\subseteq\{0,1,2,3,4,5\},
\qquad
\sum_xxp_x=\frac52.
\]

The observed design is

\[
D(\beta,\gamma)
=
\{2,\beta,\gamma\}\log2.
\]

The target remains

\[
L_p(\log2).
\]

For common error

\[
\varepsilon=\frac1{10000},
\]

the pairwise direct ratio is

\[
\rho(\beta,\gamma)
=
\max_{p,q}
\frac{L_p(\log2)}{L_q(\log2)}
\]

subject to

\[
\left|
L_p(k\log2)-L_q(k\log2)
\right|
\le2\varepsilon
\]

at all three observed exponents.

The future-score width is

\[
\mathcal R^Q(\beta,\gamma)
=
\frac12\log_2\rho(\beta,\gamma).
\]

Set

\[
s=2^{-\beta},
\qquad
r=2^{-\gamma}.
\]

Then

\[
0\le r<s<\frac14.
\]

---

## 2. Compactified A52 extremal pair

In the final A52 phase, the compactified optimizer has support

\[
\operatorname{supp}p=\{0,1,3,5\},
\qquad
\operatorname{supp}q=\{1,2,4\}.
\]

It satisfies

\[
p_0-q_0=\frac1{5000}=2\varepsilon.
\]

Let

\[
\Delta(r;s)
=
\sum_{x=0}^{5}(p_x(s)-q_x(s))r^x.
\]

For a finite third exponent \(\gamma\), its feasibility is exactly

\[
-\frac1{5000}
\le
\Delta(r;s)
\le
\frac1{5000}.
\]

At the stationary value \(s=s^\star\), the proof below establishes both inequalities for every

\[
0\le r\le s^\star.
\]

---

## 3. Exact algebraic stationary point

The stationary point is the unique root in

\[
\frac3{20}
<
s
<
\frac{19}{125}
\]

of

\[
\begin{aligned}
S(s)=\;&
1079248s^7-3781400s^6+4931589s^5-2900539s^4\\
&+734375s^3-70149s^2+4896s-504.
\end{aligned}
\]

Thus

\[
s^\star
=
0.1508931044081924687\ldots,
\]

and

\[
\beta^\star=-\log_2s^\star.
\]

The interval

\[
\left[\frac3{20},\frac{19}{125}\right]
=
[0.15,0.152]
\]

is used only as a rational isolating box for exact sign certification.

---

## 4. Finite-\(\gamma\) feasibility certificate

Let

\[
D(s)
=
90000s(s-1)^2(4s-1)(9s+14).
\]

On the rational isolation interval,

\[
D(s)<0.
\]

The upper residual factors as

\[
\frac1{5000}-\Delta(r;s)
=
\frac{-r(4r-1)U(r,s)}{D(s)}.
\]

After substituting

\[
r=su,
\qquad
0\le u\le1,
\]

all tensor-product Bernstein coefficients of \(U\) on

\[
s\in\left[\frac3{20},\frac{19}{125}\right],
\qquad
u\in[0,1]
\]

are strictly negative. The largest coefficient is still negative:

\[
\max b_{ij}(U)
=
-\frac{2027399878168}{30517578125}<0.
\]

Therefore

\[
U(r,s)<0.
\]

Because

\[
-r(4r-1)\ge0
\]

for \(0\le r\le s<1/4\), the upper residual is nonnegative.

For the lower residual,

\[
\frac1{5000}+\Delta(r;s)
=
\frac{(r-s)L(r,s)}{D(s)}.
\]

Polynomial division gives the exact identity

\[
L(r,s)
=
(r-s)A(r,s)
+
(s-1)S(s).
\]

At the stationary root,

\[
S(s^\star)=0,
\]

so

\[
L(r,s^\star)
=
(r-s^\star)A(r,s^\star).
\]

Hence

\[
\frac1{5000}+\Delta(r;s^\star)
=
\frac{(r-s^\star)^2A(r,s^\star)}
{D(s^\star)}.
\]

All Bernstein coefficients of \(A(su,s)\) on the same rational rectangle are strictly negative. The largest is

\[
\max b_{ij}(A)
=
-\frac{20775505401}{20000000}<0.
\]

Thus

\[
A(r,s^\star)<0.
\]

Since \(D(s^\star)<0\),

\[
\frac1{5000}+\Delta(r;s^\star)\ge0.
\]

Both observation bounds are therefore satisfied for every

\[
0\le r\le s^\star.
\]

---

## 5. Exact coordinatewise theorem

The compactified A52 pair has ratio

\[
\rho^\star
=
\rho(\beta^\star,\infty).
\]

The same pair is feasible for every finite \(\gamma>\beta^\star\). Therefore

\[
\rho(\beta^\star,\gamma)
\ge
\rho^\star
\qquad
\forall\gamma>\beta^\star.
\]

Since \(\gamma=\infty\) attains \(\rho^\star\),

\[
\boxed{
\gamma^\star(\beta^\star)=\infty.
}
\]

Separately, A52 proved

\[
\boxed{
\beta^\star
=
\arg\min_{\beta\in[2,4]}
\rho(\beta,\infty).
}
\]

Combining the two:

### Theorem 5.1 — coordinatewise global optimality

\[
\boxed{
(\beta^\star,\infty)
}
\]

is globally optimal along each coordinate line:

\[
\rho(\beta^\star,\gamma)
\ge
\rho(\beta^\star,\infty)
\]

for every admissible \(\gamma\), and

\[
\rho(\beta,\infty)
\ge
\rho(\beta^\star,\infty)
\]

for every admissible \(\beta\).

This is stronger than a local stationary condition, but weaker than a full joint minimization theorem.

---

## 6. Numerical joint reconnaissance

A deterministic Charnes–Cooper LP search was performed over:

\[
2<\beta<4,
\qquad
\beta<\gamma\le20,
\]

together with the compactified boundary.

The search included:

- a rectangular adaptive grid;
- one-dimensional reoptimization of \(\beta\) at fixed third-anchor caps;
- a deterministic differential-evolution search in the finite plane;
- explicit comparison with the compactified A52 solution.

No sampled or optimized finite point improved the certified risk

\[
0.0095832452322186017\ldots.
\]

At cap \(20\), the numerical optimum already differs from the compactified value by only about

\[
2.0\times10^{-9}
\]

in future-score risk.

### Important limitation

This reconnaissance is not a substitute for an exact semialgebraic partition of the whole \((\beta,\gamma)\) domain.

Near \(\beta=2\), finite \(\gamma\) can outperform \(\gamma=\infty\) for that fixed \(\beta\). For example, the numerical low-anchor basin contains values near

\[
\gamma\approx2.23476
\]

with future risk around

\[
0.03610.
\]

That is far above the candidate optimum, but an exact global proof still needs a uniform lower certificate over that low-\(\beta\) region.

---

## 7. What has and has not closed

### Established exactly

1. The A52 stationary root is isolated exactly.
2. The compactified extremal pair remains feasible for every finite third anchor at \(\beta^\star\).
3. No finite \(\gamma\) improves the risk when \(\beta=\beta^\star\).
4. No other \(\beta\) improves the risk when \(\gamma=\infty\).
5. The pair \((\beta^\star,\infty)\) is coordinatewise globally optimal.
6. The finite-\(\gamma\) feasibility proof uses exact polynomial identities and exact Bernstein signs.

### Supported numerically

1. No jointly varying finite pair beats the coordinatewise optimum.
2. Finite caps converge to \((\beta^\star,\infty)\).
3. The low-\(\beta\) finite-\(\gamma\) basin remains far above the candidate risk.

### Not yet proved

1. Full global optimality over every
   \[
   2<\beta<\gamma\le\infty.
   \]
2. A complete two-dimensional active-basis atlas.
3. A uniform exact lower bound over the low-\(\beta\) strip.
4. Any empirical or physical interpretation of \(\beta^\star\) or \(\gamma=\infty\).

---

## 8. Next rigorous target

The remaining mathematical obstruction is now sharply localized.

The next audit should isolate the low-\(\beta\) strip and construct an exact lower envelope over all finite \(\gamma\). If that envelope remains above

\[
\rho^\star,
\]

then the coordinatewise theorem can be promoted to a complete global two-dimensional minimax theorem.
