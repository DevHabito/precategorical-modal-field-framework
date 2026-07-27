# Universal Continuum Witness and Complete Joint Anchor Optimum

**Programme:** Modal Field Research Programme  
**Provisional audit:** A54  
**Author line:** Felipe Gianini Romero  
**Status:** exact global theorem under the declared finite-support, mean, noise, and target-exclusion contract; no physical design claim

## Technical abstract

A53 proved that

\[
(\beta^\star,\gamma^\star)
=
(2.728401216547027876\ldots,\infty)
\]

is globally optimal along each coordinate separately for the noisy design

\[
D(\beta,\gamma)
=
\{2,\beta,\gamma\}\log2.
\]

The only remaining obstruction was a possible jointly varying finite pair in the low-\(\beta\) region.

The present audit removes that obstruction with a stronger theorem.

Let

\[
s^\star
=
2^{-\beta^\star}
=
0.1508931044081924687\ldots
\]

be the unique root in

\[
\left(\frac3{20},\frac{19}{125}\right)
\]

of

\[
\begin{aligned}
S(s)=\;&
1079248s^7-3781400s^6+4931589s^5-2900539s^4\\
&+734375s^3-70149s^2+4896s-504.
\end{aligned}
\]

Take the exact A52 extremal pair \(p^\star,q^\star\) associated with
\(\{2,\beta^\star,\infty\}\log2\). Define

\[
d(r)
=
\sum_{x=0}^{5}
\left(
p_x^\star-q_x^\star
\right)r^x.
\]

For an observed exponent \(\eta\ge2\),

\[
r=2^{-\eta}\in[0,1/4].
\]

The exact theorem is

\[
\boxed{
-\frac1{5000}
\le
d(r)
\le
\frac1{5000}
\qquad
\forall r\in[0,1/4].
}
\]

Thus the same pair remains compatible, within the common absolute tolerance
\(\varepsilon=10^{-4}\), with **every possible observation exponent**
\(\eta\ge2\).

Consequently it remains feasible for:

- every finite triple of exponents in \([2,\infty)\);
- every finite observation budget;
- every countable collection of such observations;
- even the full continuum of observations \(\eta\in[2,\infty]\).

Its target ratio is

\[
\rho^\star
=
\frac{L_{p^\star}(\log2)}
{L_{q^\star}(\log2)},
\]

with direct future-score risk

\[
\boxed{
\mathcal R^{Q,\star}
=
0.0095832452322186017096\ldots.
}
\]

Therefore every admissible design \(D\subseteq[2,\infty]\) satisfies

\[
\mathcal R^Q(D)
\ge
\mathcal R^{Q,\star}.
\]

A52 already supplied a three-observation design attaining equality:

\[
\boxed{
D^\star
=
\{2,\beta^\star,\infty\}\log2.
}
\]

Hence

\[
\boxed{
D^\star
\text{ is a complete global minimax design.}
}
\]

This closes the joint second–third-anchor problem and strengthens it: adding
more observations anywhere in the permitted exponent domain cannot improve
the worst-case risk.

The witness has an exact equioscillation pattern:

\[
d(0)=+\frac1{5000},
\]

\[
d(s^\star)=-\frac1{5000},
\]

\[
d(1/4)=+\frac1{5000}.
\]

The optimum balances the common error band at the compactified endpoint, the
interior exponent \(\beta^\star\), and the lower allowed exponent \(2\).

The result remains entirely contract-relative. It does not establish that
the support, mean, tolerance, target-exclusion boundary, or exponent
coordinates describe a physical experiment.

---

## 1. Declared global design class

The microscopic class is

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
L_p(\log2)
=
\sum_{x=0}^{5}p_x2^{-x}.
\]

Every admissible observed exponent satisfies

\[
\eta\ge2.
\]

For a design \(D\), two microscopic distributions are compatible when

\[
\left|
L_p(\eta\log2)
-
L_q(\eta\log2)
\right|
\le2\varepsilon
\qquad
(\eta\in D),
\]

with

\[
\varepsilon=\frac1{10000}.
\]

The pairwise direct ratio is

\[
\rho(D)
=
\max_{p,q}
\frac{L_p(\log2)}
{L_q(\log2)}.
\]

The future-score width is

\[
\mathcal R^Q(D)
=
\frac12\log_2\rho(D).
\]

No restriction on the number of observations is required for the lower-bound
theorem.

---

## 2. The stationary algebraic parameter

The A52 stationary polynomial is

\[
\begin{aligned}
S(s)=\;&
1079248s^7-3781400s^6+4931589s^5-2900539s^4\\
&+734375s^3-70149s^2+4896s-504.
\end{aligned}
\]

It has exactly one root in the rational interval

\[
I_s
=
\left[
\frac3{20},
\frac{19}{125}
\right].
\]

Call it \(s^\star\). Then

\[
\beta^\star
=
-\log_2s^\star
=
2.728401216547027876\ldots.
\]

The rational interval is used to certify signs without replacing the exact
algebraic root by a decimal approximation.

---

## 3. Exact extremal pair

In the final A52 phase,

\[
\operatorname{supp}p^\star
=
\{0,1,3,5\},
\]

\[
\operatorname{supp}q^\star
=
\{1,2,4\}.
\]

The pair satisfies exactly:

\[
\sum_xp_x^\star
=
\sum_xq_x^\star
=
1,
\]

\[
\sum_xxp_x^\star
=
\sum_xxq_x^\star
=
\frac52,
\]

and the three active observation differences are

\[
d(1/4)=+\frac1{5000},
\]

\[
d(s^\star)=-\frac1{5000},
\]

\[
d(0)=+\frac1{5000}.
\]

The target ratio equals the A52 primal–dual optimum.

---

## 4. Uniform upper error bound

For symbolic \(s\), define the A52 pair \(p(s),q(s)\) and

\[
d(r;s)
=
\sum_{x=0}^{5}
\left(
p_x(s)-q_x(s)
\right)r^x.
\]

The upper residual factors exactly as

\[
\frac1{5000}-d(r;s)
=
\frac{
-r(4r-1)U(r,s)
}{
D(s)
},
\]

where

\[
D(s)
=
90000s(s-1)^2(4s-1)(9s+14).
\]

For

\[
s\in I_s,
\]

\[
D(s)<0.
\]

Map the full observation rectangle to the unit square:

\[
s
=
\frac3{20}
+
\left(
\frac{19}{125}-\frac3{20}
\right)v,
\]

\[
r=\frac{u}{4},
\qquad
0\le u,v\le1.
\]

Every tensor-product Bernstein coefficient of \(U\) on this rectangle is
strictly negative. In particular,

\[
\max b_{ij}(U)
=
-\frac{2027399878168}{30517578125}
<0.
\]

Thus

\[
U(r,s)<0
\]

throughout

\[
s\in I_s,
\qquad
0\le r\le\frac14.
\]

Also,

\[
-r(4r-1)\ge0.
\]

Therefore

\[
\boxed{
\frac1{5000}-d(r;s^\star)\ge0
}
\]

for every \(r\in[0,1/4]\).

---

## 5. Uniform lower error bound

The lower residual factors as

\[
\frac1{5000}+d(r;s)
=
\frac{(r-s)L(r,s)}{D(s)}.
\]

Exact polynomial division gives

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
\frac1{5000}+d(r;s^\star)
=
\frac{
(r-s^\star)^2A(r,s^\star)
}{
D(s^\star)
}.
\]

Using the same full rectangle

\[
s\in I_s,
\qquad
0\le r\le\frac14,
\]

all Bernstein coefficients of \(A\) are strictly negative. The largest is

\[
\max b_{ij}(A)
=
-\frac{20775505401}{20000000}
<0.
\]

Therefore

\[
A(r,s^\star)<0.
\]

Because

\[
D(s^\star)<0
\]

and

\[
(r-s^\star)^2\ge0,
\]

\[
\boxed{
\frac1{5000}+d(r;s^\star)\ge0
}
\]

for every \(r\in[0,1/4]\).

Combining the two residual bounds yields the universal continuum witness.

---

## 6. Universal continuum witness theorem

### Theorem 6.1

Let \(p^\star,q^\star\) be the A52 extremal pair at \(s^\star\). Then

\[
\boxed{
\left|
L_{p^\star}(\eta\log2)
-
L_{q^\star}(\eta\log2)
\right|
\le
2\varepsilon
}
\]

for every

\[
\eta\in[2,\infty],
\]

with

\[
\varepsilon=10^{-4}.
\]

### Proof

For finite \(\eta\ge2\), put

\[
r=2^{-\eta}\in(0,1/4].
\]

Sections 4 and 5 give

\[
-\frac1{5000}
\le
d(r)
\le
\frac1{5000}.
\]

At \(\eta=\infty\), \(r=0\), where

\[
d(0)=\frac1{5000}.
\]

Since \(1/5000=2\varepsilon\), the result follows. \(\square\)

---

## 7. Complete global minimax theorem

Consider any observation design

\[
D\subseteq[2,\infty].
\]

The universal pair \(p^\star,q^\star\) is compatible with every observation
in \(D\). Therefore

\[
\rho(D)
\ge
\frac{
L_{p^\star}(\log2)
}{
L_{q^\star}(\log2)
}
=
\rho^\star.
\]

A52 proves that

\[
D^\star
=
\{2,\beta^\star,\infty\}
\]

has exact direct minimax ratio \(\rho^\star\). Therefore:

### Theorem 7.1 — complete global design optimum

\[
\boxed{
\inf_{D\subseteq[2,\infty]}
\mathcal R^Q(D)
=
\mathcal R^{Q,\star}
}
\]

and the infimum is attained by the three-observation design

\[
\boxed{
D^\star
=
\{2,\beta^\star,\infty\}\log2.
}
\]

In particular, among all ordered triples

\[
2\le\alpha<\beta<\gamma\le\infty,
\]

the global optimum is

\[
\boxed{
(\alpha^\star,\beta^\star,\gamma^\star)
=
\left(
2,
2.728401216547027876\ldots,
\infty
\right).
}
\]

---

## 8. Observation-budget saturation

The theorem is stronger than optimization over three observations.

Even if the observer is allowed:

- four observations;
- one hundred observations;
- a dense grid;
- or the complete continuum of generalized moments for
  \(\eta\ge2\),

the same pair \(p^\star,q^\star\) remains compatible.

Therefore

\[
\boxed{
\text{additional observations in the allowed domain cannot reduce the minimax floor.}
}
\]

This is a robust non-identifiability result caused by the positive error band,
not by a shortage of sampled exponents.

At exact zero error, a continuum with an accumulation point would identify the
finite-support distribution. At fixed positive error, the universal witness
survives the full continuum.

---

## 9. Equioscillation interpretation

The extremal difference polynomial satisfies

\[
d(0)=+\frac1{5000},
\]

\[
d(s^\star)=-\frac1{5000},
\]

\[
d(1/4)=+\frac1{5000}.
\]

This is an error-band alternation pattern:

\[
+\quad-\quad+.
\]

The three optimal observations are precisely the three contact points:

\[
r=1/4
\quad\Longleftrightarrow\quad
\eta=2,
\]

\[
r=s^\star
\quad\Longleftrightarrow\quad
\eta=\beta^\star,
\]

\[
r=0
\quad\Longleftrightarrow\quad
\eta=\infty.
\]

The interior anchor is not arbitrary. It is the algebraic point that balances
the two distributions against the upper and lower tolerance boundaries.

---

## 10. Logical status

### Established

1. The stationary root \(s^\star\) is isolated exactly.
2. The A52 extremal pair satisfies every observation constraint for
   \(\eta\ge2\).
3. The proof is uniform over the full continuum, not a numerical grid.
4. Every admissible design has risk at least
   \(0.0095832452322186017\ldots\).
5. The three-point design
   \(\{2,\beta^\star,\infty\}\log2\) attains that floor.
6. The coupled second–third-anchor problem is globally closed.
7. The first anchor \(2\) is also globally selected under the declared
   exclusion boundary.
8. Arbitrarily many additional observations cannot improve the minimax value.
9. The optimal observation locations are the three equioscillation contacts.

### Not established

1. No theorem applies if exponents below \(2\) are permitted.
2. No unequal-error or correlated-error model is included.
3. No measurement cost is assigned to the compactified endpoint.
4. No extension to continuous microscopic support is proved.
5. No physical meaning is inferred for the exponent coordinates or
   \(\beta^\star\).

---

## 11. Next rigorous target

The three-anchor design problem is now closed under the declared contract.

The next meaningful extension should change the information geometry rather
than continue optimizing the same solved problem. The strongest candidates
are:

1. unequal tolerances \(\varepsilon(\eta)\);
2. correlated observation errors;
3. unknown or interval-valued mean;
4. larger or continuous microscopic support;
5. a finite cost for approaching \(\eta=\infty\).

Without one of these changes, further anchor optimization would only rederive
the already certified minimax floor.
