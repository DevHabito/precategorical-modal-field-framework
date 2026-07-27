# Robust Moment Bounds under Interval-Valued Exponential Data

**Programme:** Modal Field Research Programme  
**Provisional audit:** A41  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous mathematical continuation of MFRP-TR-2026-01, A39, and A40; no new physical assumptions

## Technical abstract

The previous stages established three facts. First, the exponential effective score is an
exact static message but not a generally autonomous dynamic state. Second, bounded support
and finitely many exact exponential observations determine sharp intervals for omitted
transform values. Third, adding exact observations shrinks those intervals monotonically,
although no finite grid universally identifies the microscopic law on a nondegenerate compact
interval.

This note treats interval-valued observations. Let

\[
L_P(\lambda)=\int e^{-\lambda x}\,dP(x)
\]

for a probability measure \(P\) supported on a compact interval. Suppose the supplied
generalized moments satisfy

\[
\left|\int \phi_j\,dP-\widehat b_j\right|\le \delta_j.
\]

The noisy feasible class is compact, so sharp extrema of every continuous observable exist.
It grows monotonically with the tolerances. As the tolerances decrease to zero, the noisy
extrema converge to the exact finite-grid extrema—not necessarily to a singleton. This
separates two logically distinct uncertainty sources:

\[
\text{total uncertainty}
=
\text{finite-grid structural ambiguity}
+
\text{observational enlargement}.
\]

A robust dual-envelope theorem gives certified bounds. If

\[
y_0+\sum_j y_j\phi_j(x)\le \psi(x)
\]

on the support, then

\[
\int\psi\,dP
\ge
y_0+\sum_j y_j\widehat b_j-\sum_j |y_j|\delta_j.
\]

The reversed envelope gives the corresponding upper bound. Hence any exact dual certificate
automatically becomes a noisy-data certificate with an explicit weighted \(\ell^1\) penalty.

For the continuous-support A39 problem on \([0,4]\), reusing the certified dual envelopes
gives a rigorous, though not asserted sharp, noisy interval. With exact mean and common
absolute error \(\varepsilon\) in the two observed transforms, the lower and upper Laplace
endpoints degrade by at most

\[
0.7972062090339338\ldots\,\varepsilon
\]

and

\[
0.8708803547704875\ldots\,\varepsilon,
\]

respectively.

A second, fully exact stress test assumes the known support
\(\{0,1,2,3,4,5\}\), exact mean \(5/2\), and common tolerance \(\varepsilon\) in the three
observations at \(2\log2,3\log2,4\log2\). For

\[
0\le \varepsilon\le
\varepsilon_\star
=
\frac{437325}{2210299904}
\approx1.9785776545914378\times10^{-4},
\]

the sharp omitted-transform interval at \(\log2\) is

\[
\frac{5173}{15808}
-\frac{366188}{25935}\varepsilon
\le
L_P(\log2)
\le
\frac{3283}{9984}
+\frac{233188}{20475}\varepsilon.
\]

Its width is exactly

\[
\frac{301}{189696}
+
\frac{9923392}{389025}\varepsilon.
\]

The constant term is irreducible finite-grid ambiguity. The linear term is the exact
observational enlargement in this regime. The corresponding \(Q\)- and future-score
intervals follow by monotone transformation. No empirical error law, physical support,
physical contraction, or physical meaning of the marks is inferred.

---

## 1. Setup

Let

\[
I=[L,U],\qquad L<U,
\]

and let \(\mathcal P(I)\) be the Borel probability measures supported on \(I\). Let
\(\phi_1,\ldots,\phi_r\in C(I)\) be observed functions, with reported central values
\(\widehat b_j\) and nonnegative tolerances \(\delta_j\).

Define

\[
\mathcal F(\widehat b,\delta)
=
\left\{
P\in\mathcal P(I):
\left|\int_I\phi_j\,dP-\widehat b_j\right|
\le\delta_j
\quad\forall j
\right\}.
\]

Normalization is built into \(\mathcal P(I)\). Exact constraints can be included by setting
the corresponding tolerance to zero.

For a continuous target \(\psi\), define the sharp noisy extrema

\[
\underline V_\psi(\delta)
=
\min_{P\in\mathcal F(\widehat b,\delta)}
\int_I\psi\,dP,
\]

\[
\overline V_\psi(\delta)
=
\max_{P\in\mathcal F(\widehat b,\delta)}
\int_I\psi\,dP.
\]

For exponential data,

\[
\phi_j(x)=e^{-\lambda_jx},
\qquad
\psi(x)=e^{-\mu x}.
\]

---

## 2. Existence and tolerance monotonicity

### Proposition 2.1 — existence

If the noisy feasible class is nonempty, both extrema are attained.

### Proof

The probability measures on the compact interval \(I\) form a weakly compact set. Every
constraint functional

\[
P\mapsto\int\phi_j\,dP
\]

is weakly continuous because \(\phi_j\) is continuous. Therefore the noisy feasible set is a
closed subset of a compact set and is compact. The target functional is continuous, so it
attains its minimum and maximum. \(\square\)

### Proposition 2.2 — monotonicity in tolerances

If

\[
0\le\delta_j\le\Delta_j
\quad\forall j,
\]

then

\[
\mathcal F(\widehat b,\delta)
\subseteq
\mathcal F(\widehat b,\Delta),
\]

and hence

\[
\underline V_\psi(\Delta)
\le
\underline V_\psi(\delta)
\le
\overline V_\psi(\delta)
\le
\overline V_\psi(\Delta).
\]

Increasing observational uncertainty can only enlarge the admissible range.

---

## 3. The zero-noise limit does not erase structural ambiguity

Let \(\delta^{(n)}\downarrow0\) coordinatewise and suppose the central exact class

\[
\mathcal F_0
=
\mathcal F(\widehat b,0)
\]

is nonempty.

### Theorem 3.1 — convergence to the exact finite-grid interval

For every continuous target \(\psi\),

\[
\underline V_\psi(\delta^{(n)})
\uparrow
\underline V_\psi(0),
\]

\[
\overline V_\psi(\delta^{(n)})
\downarrow
\overline V_\psi(0).
\]

### Proof

The feasible classes are nested compact sets and their intersection is exactly
\(\mathcal F_0\). Choose maximizers in the noisy classes. Any convergent subsequence has a
limit in every fixed noisy class and therefore in their intersection. Continuity of the target
shows that every limiting objective value belongs to the exact class. Monotonicity then
forces convergence to the exact maximum. The minimum is analogous. \(\square\)

### Consequence

If the exact finite-grid interval has positive width, then arbitrarily accurate measurements
do not remove that width. They remove only the observational enlargement.

Thus

\[
\lim_{\delta\to0}
\left[
\overline V_\psi(\delta)
-
\underline V_\psi(\delta)
\right]
=
\overline V_\psi(0)
-
\underline V_\psi(0),
\]

which may be strictly positive.

This is the precise distinction between non-identifiability and measurement error.

---

## 4. Robust dual envelopes

### Theorem 4.1 — certified lower bound

Suppose coefficients \(y_0,y_1,\ldots,y_r\) satisfy

\[
y_0+\sum_{j=1}^r y_j\phi_j(x)
\le
\psi(x)
\qquad\forall x\in I.
\]

Then every \(P\in\mathcal F(\widehat b,\delta)\) satisfies

\[
\int_I\psi\,dP
\ge
y_0+\sum_{j=1}^r y_j\widehat b_j
-
\sum_{j=1}^r |y_j|\delta_j.
\]

### Proof

Integrating the pointwise envelope gives

\[
\int\psi\,dP
\ge
y_0+\sum_j y_j\int\phi_j\,dP.
\]

Write

\[
\int\phi_j\,dP=\widehat b_j+e_j,
\qquad |e_j|\le\delta_j.
\]

Then

\[
\sum_j y_je_j\ge-\sum_j|y_j|\delta_j.
\]

Substitution proves the claim. \(\square\)

### Theorem 4.2 — certified upper bound

If

\[
y_0+\sum_{j=1}^r y_j\phi_j(x)
\ge
\psi(x)
\qquad\forall x\in I,
\]

then

\[
\int_I\psi\,dP
\le
y_0+\sum_{j=1}^r y_j\widehat b_j
+
\sum_{j=1}^r |y_j|\delta_j.
\]

The proof is the same with inequalities reversed.

### Interpretation

The penalty is not inserted ad hoc. It is the exact support function of the rectangular
error set

\[
[-\delta_1,\delta_1]\times\cdots\times[-\delta_r,\delta_r].
\]

For a correlated or nonrectangular error set \(E\), the penalty becomes its support function

\[
\sigma_E(y)=\sup_{e\in E}y\cdot e.
\]

Therefore the geometry of the observational uncertainty must be declared; it cannot be
silently replaced by independent absolute errors.

---

## 5. Propagation to effective scores

For \(\mu>0\), define

\[
Q_\mu(P)=-\frac1\mu\log L_P(\mu).
\]

On the support interval,

\[
e^{-\mu U}\le L_P(\mu)\le e^{-\mu L}.
\]

If a certified transform interval is

\[
0<\underline L_\mu\le L_P(\mu)\le\overline L_\mu,
\]

then the corresponding sharp monotone image is

\[
-\frac1\mu\log\overline L_\mu
\le
Q_\mu(P)
\le
-\frac1\mu\log\underline L_\mu.
\]

Moreover,

\[
\left|
-\frac1\mu\log z_1+
\frac1\mu\log z_2
\right|
\le
\frac{e^{\mu U}}{\mu}|z_1-z_2|
\]

for all admissible transform values. Thus the logarithmic map can amplify absolute transform
error, particularly when \(\mu U\) is large.

Under the centered contraction

\[
x'=m+a(x-m),
\qquad 0<a<1,
\]

\[
Q'_\lambda=(1-a)m+aQ_{a\lambda}.
\]

When the mean is exact, the future interval is the affine image of the interval for
\(Q_{a\lambda}\). If the mean has tolerance \(\delta_m\), a safe outer interval adds

\[
(1-a)\delta_m
\]

to each side. This separate treatment is conservative because it does not exploit possible
correlation between the mean and the omitted transform.

---

## 6. Continuous-support reuse of the A39 certificate

A39 considered

\[
\operatorname{supp}P\subset[0,4],
\qquad
\mathbb E[X]=2,
\]

\[
L(\log2)=\frac{31}{80},
\qquad
L(2\log2)=\frac{341}{1280},
\]

with target

\[
\mu=\frac12\log2.
\]

Its certified exact interval was

\[
L_{\min}^{(0)}
=
0.5599571720587944588199174791268\ldots,
\]

\[
L_{\max}^{(0)}
=
0.5630735173874428658558427940415\ldots.
\]

The certified lower-envelope transform coefficients are

\[
y_{\log2}^{-}
=
0.6591415481095810564\ldots,
\]

\[
y_{2\log2}^{-}
=
-0.1380646609243527769\ldots,
\]

so

\[
\kappa_-
=
|y_{\log2}^{-}|+|y_{2\log2}^{-}|
=
0.7972062090339338334\ldots.
\]

The upper-envelope coefficients give

\[
\kappa_+
=
0.8708803547704874736\ldots.
\]

If the mean remains exact and both observed transforms have common absolute tolerance
\(\varepsilon\), then every admissible distribution satisfies

\[
L_{\min}^{(0)}-\kappa_-\varepsilon
\le
L_P(\mu)
\le
L_{\max}^{(0)}+\kappa_+\varepsilon,
\]

after intersection with the trivial support interval

\[
[e^{-4\mu},1].
\]

These are certified outer bounds inherited from the exact A39 dual envelopes. They are not
asserted to be sharp for the enlarged noisy class, because the optimal dual coefficients may
change when \(\varepsilon>0\).

For illustration, the resulting certified future-score widths are approximately:

| Common transform tolerance \(\varepsilon\) | Certified width of \(Q'_{\log2}\) |
|---:|---:|
| \(0\) | \(0.00800681144988872\) |
| \(10^{-6}\) | \(0.00801109675334529\) |
| \(10^{-5}\) | \(0.00804966446074546\) |
| \(10^{-4}\) | \(0.00843533919038160\) |
| \(10^{-3}\) | \(0.01229185486854958\) |

The first width is structural. The additional growth is observational and certificate-based.

---

## 7. Exact sharp finite-support stress test

Now add the stronger contract

\[
\operatorname{supp}P
\subseteq
\{0,1,2,3,4,5\}.
\]

Keep the mean exact:

\[
\mathbb E[X]=\frac52.
\]

Let the three observed transform values satisfy

\[
\left|
L(2\log2)-\frac{455}{2048}
\right|\le\varepsilon,
\]

\[
\left|
L(3\log2)-\frac{12483}{65536}
\right|\le\varepsilon,
\]

\[
\left|
L(4\log2)-\frac{372827}{2097152}
\right|\le\varepsilon.
\]

The target is

\[
L(\log2)=\sum_{k=0}^5p_k2^{-k}.
\]

Because the support is prescribed, this is a finite linear programme.

### 7.1 Exact lower dual envelope

Define on the six support points

\[
h_-(x)
=
\frac{3427}{25935}
-\frac{31}{1482}x
+\frac{8876}{2223}2^{-2x}
-\frac{11456}{1729}2^{-3x}
+\frac{2048}{585}2^{-4x}.
\]

Direct rational evaluation gives

\[
2^{-x}-h_-(x)=0
\]

for

\[
x=0,1,2,4,5,
\]

and

\[
2^{-3}-h_-(3)=\frac{21}{3952}>0.
\]

Hence \(h_-\le2^{-x}\) on the declared support. Its coefficient signs select the lower,
upper, and lower observational endpoints respectively, yielding

\[
L(\log2)
\ge
\frac{5173}{15808}
-
\frac{366188}{25935}\varepsilon.
\]

### 7.2 Exact upper dual envelope

Define

\[
h_+(x)
=
\frac{3287}{20475}
-\frac{31}{1170}x
+\frac{1204}{351}2^{-2x}
-\frac{480}{91}2^{-3x}
+\frac{23552}{8775}2^{-4x}.
\]

Then

\[
2^{-x}-h_+(x)=0
\]

for

\[
x=0,1,2,3,5,
\]

while

\[
2^{-4}-h_+(4)=-\frac7{1664}<0.
\]

Thus \(h_+\ge2^{-x}\) on the declared support, and

\[
L(\log2)
\le
\frac{3283}{9984}
+
\frac{233188}{20475}\varepsilon.
\]

### 7.3 Primal attainment and validity interval

The lower bound is attained by a distribution with \(p_3=0\) and weights affine in
\(\varepsilon\). The upper bound is attained by a distribution with \(p_4=0\), also affine in
\(\varepsilon\).

All weights remain nonnegative throughout

\[
0\le\varepsilon\le
\varepsilon_\star
=
\frac{437325}{2210299904}.
\]

At \(\varepsilon_\star\), the lower extremizer acquires a second zero weight. The primal and
dual objectives coincide exactly, so the bounds are sharp on the whole stated interval.

### Theorem 7.1 — exact local noisy interval

For

\[
0\le\varepsilon\le\varepsilon_\star,
\]

\[
\boxed{
\frac{5173}{15808}
-\frac{366188}{25935}\varepsilon
\le
L_P(\log2)
\le
\frac{3283}{9984}
+\frac{233188}{20475}\varepsilon
}
\]

is the sharp interval.

Its exact width is

\[
\boxed{
W_L(\varepsilon)
=
\frac{301}{189696}
+
\frac{9923392}{389025}\varepsilon
}.
\]

Therefore

\[
\underbrace{\frac{301}{189696}}_{\text{structural finite-grid ambiguity}}
+
\underbrace{\frac{9923392}{389025}\varepsilon}_{\text{observational enlargement}}
\]

is not a heuristic decomposition. It is the exact parametric linear-programming result in
this regime.

---

## 8. Sharp effective-score and future intervals

Since

\[
Q_{\log2}=-\log_2L(\log2),
\]

the sharp score interval is

\[
-\log_2\left(
\frac{3283}{9984}
+
\frac{233188}{20475}\varepsilon
\right)
\le
Q_{\log2}
\le
-\log_2\left(
\frac{5173}{15808}
-
\frac{366188}{25935}\varepsilon
\right).
\]

With

\[
a=\frac12,
\qquad
m=\frac52,
\qquad
\lambda=2\log2,
\]

the transport identity gives

\[
Q'_{2\log2}
=
\frac54+\frac12Q_{\log2}.
\]

Hence the sharp future interval is

\[
\boxed{
\frac54
-\frac12\log_2\left(
\frac{3283}{9984}
+
\frac{233188}{20475}\varepsilon
\right)
\le
Q'_{2\log2}
\le
\frac54
-\frac12\log_2\left(
\frac{5173}{15808}
-
\frac{366188}{25935}\varepsilon
\right)
}.
\]

Selected values are:

| \(\varepsilon\) | Sharp future lower | Sharp future upper | Sharp width |
|---:|---:|---:|---:|
| \(0\) | \(2.052301592144634\) | \(2.055790877690461\) | \(0.003489285545827\) |
| \(10^{-6}\) | \(2.052276608660765\) | \(2.055822002465245\) | \(0.003545393804480\) |
| \(10^{-5}\) | \(2.052051796235439\) | \(2.056102185888690\) | \(0.004050389653251\) |
| \(10^{-4}\) | \(2.049807517126118\) | \(2.058910021982857\) | \(0.009102504856739\) |

At \(\varepsilon=10^{-4}\), observational error has already enlarged the future interval
beyond twice its zero-noise width. This is a property of the declared finite-support moment
problem, not evidence for any physical noise law.

---

## 9. Strong inverse stability remains impossible on a finite grid

A finite grid can admit two distinct measures with exactly identical supplied data. Therefore
there is no single-valued inverse map from those data to the microscopic probability measure
on the unrestricted compact-support class.

In particular, no estimate of the form

\[
d(P,Q)
\le
C\max_j
|L_P(\lambda_j)-L_Q(\lambda_j)|
\]

can hold universally for any metric \(d\) that separates distinct measures: the right-hand
side can be zero while the left-hand side is positive.

This does not prevent stable recovery of selected observables through certified intervals.
It prevents promoting a finite set of generalized moments into a stable reconstruction of the
entire microscopic law without additional structure.

---

## 10. Logical status

### Established

1. Noisy moment classes on compact support have attained sharp extrema.
2. Larger tolerances produce larger feasible classes and wider or equal intervals.
3. Vanishing error converges to the exact finite-grid interval, which may retain positive
   structural width.
4. Every valid exact dual envelope yields a certified noisy bound with a weighted
   \(\ell^1\) penalty.
5. The A39 continuous-support certificate gives explicit rigorous noisy outer intervals.
6. On the declared six-point support, the sharp omitted-transform bounds are affine in the
   common tolerance up to an exact rational breakpoint.
7. The corresponding effective-score and future intervals are sharp monotone images.
8. Finite generalized-moment data do not support a universally stable inverse reconstruction
   of the entire measure.

### Not established

1. The continuous-support A39 noisy bounds are not proved sharp for \(\varepsilon>0\).
2. No observational error distribution has been inferred.
3. No optimal parameter grid has been derived.
4. No minimax design criterion has yet been selected.
5. No physical support, physical scale, or physical contraction has been calibrated.
6. No statement here converts the formal marks into physical observables.

---

## 11. Next rigorous target

The next step is finite-budget parameter design.

Given

- a support contract;
- an omitted target parameter \(\mu\);
- a number \(r\) of observable transform values;
- an error geometry and tolerance budget;

choose

\[
\lambda_1,\ldots,\lambda_r
\]

to minimize a declared risk, such as

\[
\sup_{P\in\mathcal P(I)}
\left[
\overline Q_\mu-\underline Q_\mu
\right]
\]

or the corresponding future-score width.

Before optimization, the risk functional and error geometry must be fixed. Different choices
will generally produce different “optimal” grids. There is no unique optimal design without
that contract.
