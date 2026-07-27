# Monotone Information Refinement and Asymptotic Identification

**Programme:** Modal Field Research Programme  
**Provisional audit:** A40  
**Author line:** Felipe Gianini Romero  
**Status:** rigorous mathematical continuation of MFRP-TR-2026-01 and A39; no new physical assumptions

## Technical abstract

Let \(P_\star\) be a probability measure supported on a compact nondegenerate interval
\([L,U]\), and define

\[
L_P(\lambda)=\int_{L}^{U} e^{-\lambda x}\,dP(x),
\qquad
Q_P(\lambda)=-\lambda^{-1}\log L_P(\lambda),
\quad \lambda>0.
\]

A39 showed that finitely many exact transform observations, together with a mean and a
bounded-support contract, determine a sharp interval for an omitted transform value and
therefore a sharp interval for a future effective score under the centered contraction.

This note establishes the next layer.

1. Adding exact transform constraints can only shrink the feasible measure class. Hence
   omitted-transform intervals, effective-score intervals, and transported future-score
   intervals are nested monotonically.
2. The shrinkage need not be strict.
3. No finite transform grid universally identifies an omitted transform on the unrestricted
   class of probability measures on a nondegenerate compact interval, even when normalization
   and the mean are known.
4. If the union of an increasing sequence of observed parameter sets has a finite accumulation
   point, then the exact transform observations identify the compactly supported measure.
   Consequently every sharp interval for a continuous observable converges to its true value.
5. Finite exact identification is possible under a stronger finite-support contract: if the
   admissible support is known to lie in \(N\) prescribed points, \(N\) independent generalized
   moments determine the weights uniquely.

An exact six-point rational witness is supplied for the finite-grid obstruction. The witness
matches the mean and three transform values at
\(\{2\log2,3\log2,4\log2\}\) while differing at the dynamically required parameter
\(\log2\). The result remains mathematical. It does not establish a physical \(q\)-field,
support interval, contraction, or empirical observation law.

---

## 1. Setup

Fix a compact interval

\[
I=[L,U],\qquad L<U.
\]

Let \(\mathcal P(I)\) denote the Borel probability measures on \(I\). For \(P\in\mathcal P(I)\),
define

\[
m_P=\int_I x\,dP(x),
\]

\[
L_P(\lambda)=\int_I e^{-\lambda x}\,dP(x),
\qquad \lambda>0,
\]

and

\[
Q_P(\lambda)=-\frac{1}{\lambda}\log L_P(\lambda).
\]

Fix a reference measure \(P_\star\). For a finite observed parameter set
\(\Lambda\subset(0,\infty)\), define the exact feasible class

\[
\mathcal F(\Lambda)=
\left\{
P\in\mathcal P(I):
m_P=m_{P_\star},
\quad
L_P(\lambda)=L_{P_\star}(\lambda)
\ \text{for every }\lambda\in\Lambda
\right\}.
\]

For an omitted parameter \(\mu>0\), define

\[
\underline L_\mu(\Lambda)
=
\min_{P\in\mathcal F(\Lambda)}L_P(\mu),
\]

\[
\overline L_\mu(\Lambda)
=
\max_{P\in\mathcal F(\Lambda)}L_P(\mu).
\]

Compactness of \(I\) guarantees that these extrema exist whenever the feasible class is
nonempty.

---

## 2. Monotonicity under added information

### Theorem 2.1 — nested feasible classes

If

\[
\Lambda\subseteq\Gamma,
\]

then

\[
\mathcal F(\Gamma)\subseteq\mathcal F(\Lambda).
\]

Consequently,

\[
\underline L_\mu(\Lambda)
\le
\underline L_\mu(\Gamma)
\le
\overline L_\mu(\Gamma)
\le
\overline L_\mu(\Lambda).
\]

### Proof

Every measure satisfying all constraints indexed by \(\Gamma\) also satisfies the subset of
constraints indexed by \(\Lambda\). Therefore the feasible set can only decrease. Minimizing
a fixed functional over a smaller set cannot lower the minimum, and maximizing over a
smaller set cannot raise the maximum. \(\square\)

### Corollary 2.2 — monotone effective-score intervals

Because \(z\mapsto-\mu^{-1}\log z\) is strictly decreasing on \((0,\infty)\), the sharp
effective-score interval is

\[
\underline Q_\mu(\Lambda)
=
-\frac{1}{\mu}\log\overline L_\mu(\Lambda),
\]

\[
\overline Q_\mu(\Lambda)
=
-\frac{1}{\mu}\log\underline L_\mu(\Lambda).
\]

If \(\Lambda\subseteq\Gamma\), then

\[
\underline Q_\mu(\Lambda)
\le
\underline Q_\mu(\Gamma)
\le
\overline Q_\mu(\Gamma)
\le
\overline Q_\mu(\Lambda).
\]

Thus the \(Q\)-interval is nested as information is added.

### Corollary 2.3 — monotone future-score intervals

Under the centered contraction

\[
x'=m_{P_\star}+a(x-m_{P_\star}),
\qquad 0<a<1,
\]

the exact transport identity is

\[
Q'_\lambda=(1-a)m_{P_\star}+aQ_{a\lambda}.
\]

Therefore the sharp interval for \(Q'_\lambda\) inherits the same nesting property from the
interval for \(Q_{a\lambda}\).

### Boundary: shrinkage need not be strict

The inclusions and inequalities can be equalities. An added constraint may already be
implied by the current feasible class, or the current feasible class may already be a singleton.
Therefore “more information never worsens the interval” is proved; “every new parameter
strictly improves the interval” is false without an additional nonredundancy condition.

---

## 3. A zero-count lemma

The finite-grid obstruction below uses only a standard zero-count argument, reproduced here
to avoid hiding the crucial step.

### Lemma 3.1 — distinct exponentials

Let \(\alpha_1,\ldots,\alpha_m\) be distinct real numbers. A nonzero function

\[
g(x)=\sum_{j=1}^{m}c_j e^{\alpha_jx}
\]

has at most \(m-1\) real zeros, counted with multiplicity, on any interval.

### Proof sketch

For \(m=1\), the claim is immediate. Assume it holds for \(m-1\). Multiply \(g\) by
\(e^{-\alpha_1x}\), which does not change its zeros, and differentiate:

\[
\frac{d}{dx}\left(e^{-\alpha_1x}g(x)\right)
=
\sum_{j=2}^{m}c_j(\alpha_j-\alpha_1)e^{(\alpha_j-\alpha_1)x}.
\]

The derivative is a combination of \(m-1\) distinct exponentials and therefore has at most
\(m-2\) zeros by induction. Rolle's theorem, including multiplicities, then limits the
original function to at most \(m-1\) zeros. \(\square\)

### Lemma 3.2 — affine term plus distinct decaying exponentials

Let \(\beta_1,\ldots,\beta_m>0\) be distinct. A nonzero function

\[
f(x)=a+bx+\sum_{j=1}^{m}c_j e^{-\beta_jx}
\]

has at most \(m+1\) zeros, counted with multiplicity.

### Proof

If \(f\) had at least \(m+2\) zeros, then two applications of Rolle's theorem would imply
that

\[
f''(x)=\sum_{j=1}^{m}c_j\beta_j^2e^{-\beta_jx}
\]

has at least \(m\) zeros. Lemma 3.1 permits at most \(m-1\), unless \(f''\equiv0\).
If \(f''\equiv0\), all exponential coefficients vanish and \(f\) is affine, which has at most
one zero unless it is identically zero. \(\square\)

Consequently, the functions

\[
1,\quad x,\quad e^{-\beta_1x},\ldots,e^{-\beta_mx}
\]

form a Chebyshev system: their evaluation matrix at \(m+2\) distinct points is nonsingular.

---

## 4. No universal finite-grid identification on compact support

### Theorem 4.1 — finite-grid compact-support obstruction

Let \(I=[L,U]\) with \(L<U\). Let

\[
\Lambda=\{\lambda_1,\ldots,\lambda_r\}\subset(0,\infty)
\]

be finite with distinct elements, and let

\[
\mu\in(0,\infty)\setminus\Lambda.
\]

Then there exist two distinct strictly positive finite probability measures \(P^+\) and \(P^-\),
both supported inside \(I\), such that

\[
m_{P^+}=m_{P^-},
\]

\[
L_{P^+}(\lambda_j)=L_{P^-}(\lambda_j)
\quad\text{for all }j=1,\ldots,r,
\]

but

\[
L_{P^+}(\mu)\ne L_{P^-}(\mu).
\]

Therefore no finite positive transform grid, even when combined with normalization and the
mean, universally identifies every omitted transform on \(\mathcal P(I)\).

### Proof

Choose \(r+3\) distinct points

\[
L\le x_0<\cdots<x_{r+2}\le U.
\]

Form the \((r+2)\times(r+3)\) constraint matrix whose rows evaluate

\[
1,\quad x,\quad e^{-\lambda_1x},\ldots,e^{-\lambda_rx}
\]

at these points. By Lemma 3.2, the constraint functions have full row rank \(r+2\), so the
matrix has a nonzero one-dimensional null vector \(v\).

Augment the matrix with the row evaluating \(e^{-\mu x}\). The resulting square matrix
evaluates

\[
1,\quad x,\quad e^{-\lambda_1x},\ldots,e^{-\lambda_rx},
\quad e^{-\mu x}
\]

at the \(r+3\) points. Lemma 3.2 again implies that this square matrix is nonsingular.
Therefore the omitted-transform row is not orthogonal to \(v\):

\[
\sum_i v_i e^{-\mu x_i}\ne0.
\]

Let \(p_i>0\) be any positive probability vector on the chosen points. For sufficiently small
\(\varepsilon>0\),

\[
p_i^\pm=p_i\pm\varepsilon v_i
\]

remain strictly positive. Since the normalization row belongs to the constraint matrix,
\(\sum_i v_i=0\), so both perturbed vectors remain normalized. Every other supplied
constraint is unchanged because \(v\) lies in the constraint nullspace. The omitted transform
changes with opposite sign because its row is not orthogonal to \(v\). \(\square\)

### Consequence for the centered contraction

If \(\mu=a\lambda\) and \(\lambda\) is among the tracked parameters while \(\mu\) is omitted,
the two measures have the same tracked macrostate but different next \(Q_\lambda\). The
bounded-support contract can make the uncertainty finite and computable, as in A39, but a
finite grid does not universally reduce it to zero.

---

## 5. Exact rational six-point witness

The preceding theorem is constructive. The following instance uses only rational arithmetic.

Take

\[
I=[0,5],
\qquad
\Lambda=\{2\log2,3\log2,4\log2\},
\qquad
\mu=\log2.
\]

Use support points

\[
x=0,1,2,3,4,5.
\]

The constraint matrix has rows

\[
1,\quad x,\quad 2^{-2x},\quad2^{-3x},\quad2^{-4x}.
\]

An exact integer null vector is

\[
v=(-1,30,-281,988,-1248,512).
\]

Starting from the uniform weights and choosing \(\varepsilon=10^{-4}\), define

\[
p^\pm_i=\frac16\pm\frac{v_i}{10000}.
\]

Explicitly,

\[
p^+=
\left(
\frac{4997}{30000},
\frac{509}{3000},
\frac{4157}{30000},
\frac{1991}{7500},
\frac{157}{3750},
\frac{817}{3750}
\right),
\]

\[
p^-=
\left(
\frac{5003}{30000},
\frac{491}{3000},
\frac{5843}{30000},
\frac{509}{7500},
\frac{1093}{3750},
\frac{433}{3750}
\right).
\]

All weights are strictly positive. The measures agree exactly on

\[
m=\frac52,
\]

\[
L(2\log2)=\frac{455}{2048},
\]

\[
L(3\log2)=\frac{12483}{65536},
\]

\[
L(4\log2)=\frac{372827}{2097152}.
\]

At the omitted parameter,

\[
L_{P^+}(\log2)=\frac{6573}{20000},
\]

\[
L_{P^-}(\log2)=\frac{819}{2500},
\]

so

\[
L_{P^+}(\log2)-L_{P^-}(\log2)=\frac{21}{20000}>0.
\]

For \(a=\tfrac12\) and tracked parameter \(\lambda=2\log2\), the next-score difference is

\[
Q_{\lambda}^{\prime -}-Q_{\lambda}^{\prime +}
=
\frac12\log_2\left(\frac{2191}{2184}\right)
\approx
0.0023083140351849961685.
\]

This is an exact compact-support nonclosure witness. It is not based on random search,
floating-point fitting, or tolerance matching.

---

## 6. Identification from an accumulating parameter set

Finite grids do not universally identify an omitted transform. An infinite exact observation
set with a finite accumulation point does.

### Theorem 6.1 — accumulation-point identification

Let \(P,Q\in\mathcal P([L,U])\). Let \(S\subset\mathbb R\) contain infinitely many distinct
points with a finite accumulation point. If

\[
L_P(\lambda)=L_Q(\lambda)
\quad\text{for every }\lambda\in S,
\]

then

\[
P=Q.
\]

### Proof

Compact support implies that

\[
L_P(z)=\int_{L}^{U}e^{-zx}\,dP(x)
\]

defines an entire function of the complex variable \(z\); differentiation under the integral
is valid on every compact subset of the complex plane. Hence

\[
H(z)=L_P(z)-L_Q(z)
\]

is entire. It vanishes on a set with a finite accumulation point, so the identity theorem gives

\[
H\equiv0.
\]

In particular, all derivatives agree at zero:

\[
\int x^k\,dP(x)=\int x^k\,dQ(x)
\quad\text{for every }k\ge0.
\]

Therefore \(P\) and \(Q\) integrate every polynomial equally. Polynomials are uniformly
dense in \(C([L,U])\), so the two measures integrate every continuous function equally and
must be identical. \(\square\)

The accumulation point may be zero or any other finite real value. It need not belong to
the observed set.

---

## 7. Convergence of all sharp intervals

Let

\[
\Lambda_1\subseteq\Lambda_2\subseteq\cdots
\]

be finite parameter sets and suppose

\[
S=\bigcup_{n=1}^{\infty}\Lambda_n
\]

has a finite accumulation point. Let

\[
\mathcal F_n=\mathcal F(\Lambda_n).
\]

### Theorem 7.1 — convergence to the true measure

The feasible classes are nonempty nested compact sets and

\[
\bigcap_{n=1}^{\infty}\mathcal F_n=\{P_\star\}.
\]

For every continuous observable \(\varphi\in C([L,U])\),

\[
\min_{P\in\mathcal F_n}\int\varphi\,dP
\longrightarrow
\int\varphi\,dP_\star,
\]

\[
\max_{P\in\mathcal F_n}\int\varphi\,dP
\longrightarrow
\int\varphi\,dP_\star.
\]

### Proof

Nestedness and compactness were established earlier. Any measure in the intersection matches
\(P_\star\) on every parameter in \(S\), so Theorem 6.1 makes the intersection a singleton.

Consider maximizers \(P_n^{\max}\in\mathcal F_n\). Compactness gives a convergent
subsequence. For every fixed \(N\), all sufficiently late members of that subsequence belong
to \(\mathcal F_N\); closedness puts the limit in every \(\mathcal F_N\), hence the limit is
\(P_\star\). Continuity of \(P\mapsto\int\varphi\,dP\) then forces every convergent subsequence
of objective values to approach \(\int\varphi\,dP_\star\). The nested maximum sequence is
monotone and bounded, so it converges to that value. The minimum is analogous. \(\square\)

### Corollary 7.2 — omitted-transform convergence

For every fixed \(\mu>0\),

\[
\underline L_\mu(\Lambda_n)
\uparrow
L_{P_\star}(\mu),
\]

\[
\overline L_\mu(\Lambda_n)
\downarrow
L_{P_\star}(\mu).
\]

### Corollary 7.3 — effective and future-score convergence

The sharp \(Q_\mu\) interval converges to the singleton
\(\{Q_{P_\star}(\mu)\}\). Under the centered contraction, the sharp future interval for every
fixed \(Q'_\lambda\) also converges to its exact value.

This is asymptotic identification from increasingly rich exact information. It is not a
finite-dimensional autonomous closure theorem.

---

## 8. Finite-support exception

The finite-grid obstruction depends on allowing arbitrary measures on the interval. A stronger
support contract changes the result.

### Proposition 8.1 — known finite support

Suppose the admissible support is known in advance to lie in \(N\) distinct points

\[
s_1<\cdots<s_N.
\]

Choose \(N-2\) distinct positive transform parameters
\(\lambda_1,\ldots,\lambda_{N-2}\). Then normalization, the mean, and the \(N-2\) transform
values determine the \(N\) support weights uniquely.

### Proof

The square evaluation matrix of

\[
1,\quad x,\quad e^{-\lambda_1x},\ldots,e^{-\lambda_{N-2}x}
\]

at the \(N\) distinct support points is nonsingular by Lemma 3.2. Therefore the linear system
for the weights has at most one solution. \(\square\)

For the six-point support \(\{0,1,2,3,4,5\}\), normalization, mean, and transform values at

\[
\log2,\quad2\log2,\quad3\log2,\quad4\log2
\]

form a nonsingular six-equation system. Its exact determinant is

\[
\frac{6251175}{1099511627776}\ne0.
\]

Thus finite exact identification is available only after the stronger finite-support structure
is declared. It is not supplied by the bounded interval alone.

---

## 9. Logical status

### Established

1. Exact added constraints produce nested feasible classes.
2. Sharp transform, effective-score, and transported future-score intervals can only shrink.
3. Strict shrinkage is not automatic.
4. No finite grid universally identifies an omitted transform over all probability measures
   on a nondegenerate compact interval.
5. An infinite exact parameter set with a finite accumulation point identifies the
   compactly supported measure.
6. Under nested exact observations, sharp intervals for every continuous observable converge
   to the true value.
7. Known finite support permits finite exact identification when enough independent moments
   are supplied.

### Not established

1. No quantitative convergence rate follows from the proofs.
2. No optimal finite parameter grid has been derived.
3. No stability theorem for noisy or interval-valued observations has been proved.
4. No support interval has been empirically calibrated.
5. No physical origin of \(q\), \(\lambda\), the contraction, or the observations is claimed.
6. No theorem here promotes a transform grid into a fundamental physical state.

---

## 10. Next rigorous target

The next problem should be stability rather than another exact-identification theorem.

Given observational tolerances

\[
|L_P(\lambda_j)-\widehat s_j|\le\delta_j,
\]

determine certified upper and lower bounds for \(L_P(\mu)\), and quantify how those bounds
depend on

- the support diameter \(U-L\);
- the parameter locations \(\lambda_j\);
- the error levels \(\delta_j\);
- the omitted parameter \(\mu\).

Only after such a stability theory is available does finite-grid design become an operational
question. Exact identifiability alone does not control sensitivity to measurement error.
