# Research Note: Finite-Grid Nonclosure and Parameter-Orbit Closure

**Programme:** Modal Field Research Programme  
**Status:** preliminary mathematical continuation; not yet an official numbered report  
**Author line:** Felipe Gianini Romero  
**Purpose:** strengthen the dynamic-closure result of *Informational Requirements for Pre-Categorical Relational Models* without introducing new physical assumptions.

## 1. Research question

The current report proves that the pair consisting of the mean and one fixed exponential effective score does not determine the next score under the centered contraction

\[
q_i' = \bar q + a(q_i-\bar q), \qquad 0<a<1.
\]

A natural repair would be to carry several fixed transform scores. The next question is therefore:

> Can any finite positive grid of transform parameters provide exact autonomous closure on the unrestricted class of finite marked distributions?

The answer is no. The obstruction is not limited to one score.

## 2. Definitions

Let \(p\) be a probability distribution with finite support on \(\mathbb R\). Define

\[
L_p(\lambda)=\sum_i p_i e^{-\lambda q_i},
\qquad
Q_p(\lambda)=-\frac{1}{\lambda}\log L_p(\lambda),
\quad \lambda>0.
\]

Let

\[
m_p=\sum_i p_i q_i.
\]

Under the centered contraction, the mean is preserved and

\[
Q_{p'}(\lambda)=(1-a)m_p+aQ_p(a\lambda).
\]

Thus prediction at \(\lambda\) requires information at the rescaled parameter \(a\lambda\).

## 3. Finite-grid separation lemma

### Lemma 1 — finite Laplace data do not determine an omitted positive parameter

Let \(\Gamma=\{\gamma_1,\ldots,\gamma_m\}\subset(0,\infty)\) be finite with distinct elements, and let \(\mu\in(0,\infty)\setminus\Gamma\). Then there exist two strictly positive finitely supported probability distributions \(p^+\) and \(p^-\) such that

\[
m_{p^+}=m_{p^-},
\]

\[
L_{p^+}(\gamma)=L_{p^-}(\gamma)
\quad\text{for every }\gamma\in\Gamma,
\]

but

\[
L_{p^+}(\mu)\ne L_{p^-}(\mu).
\]

Consequently, \(Q_{p^+}(\gamma)=Q_{p^-}(\gamma)\) for every \(\gamma\in\Gamma\), while \(Q_{p^+}(\mu)\ne Q_{p^-}(\mu)\).

### Proof

Consider the functions

\[
1,\quad x,\quad e^{-\gamma_1x},\ldots,e^{-\gamma_mx},\quad e^{-\mu x}.
\]

They are linearly independent on \(\mathbb R\). Indeed, suppose

\[
c_0+c_1x+\sum_{j=1}^m c_{j+1}e^{-\gamma_jx}+c_{m+2}e^{-\mu x}=0
\]

for every \(x\). Sending \(x\to+\infty\) forces \(c_0=c_1=0\). The remaining exponentials have distinct exponents and are linearly independent, for example by evaluating successive derivatives at one point and using the resulting Vandermonde matrix.

A standard evaluation lemma for linearly independent functions gives points \(x_0,\ldots,x_{m+2}\) for which the full \((m+3)\times(m+3)\) evaluation matrix is nonsingular. Let \(A\) be the first \(m+2\) rows, corresponding to normalization, mean, and the values at \(\Gamma\). Then \(A\) has a nonzero null vector \(v\). The final row, corresponding to \(e^{-\mu x}\), cannot annihilate the same \(v\), because otherwise the full evaluation matrix would annihilate \(v\) and would be singular.

Choose any strictly positive probability vector \(p^0\) on these support points. For sufficiently small \(\varepsilon>0\),

\[
p^\pm=p^0\pm\varepsilon v
\]

remain strictly positive. Since the normalization row belongs to \(A\), both vectors still sum to one. All rows of \(A\) agree between \(p^+\) and \(p^-\), while the omitted transform row differs. This proves the claim. \(\square\)

## 4. Main dynamic theorem

### Theorem 2 — no finite positive fixed grid is universally autonomous

Fix \(0<a<1\). Let \(\Lambda\subset(0,\infty)\) be any nonempty finite set. On the unrestricted class of finite marked probability distributions, the macrostate

\[
\left(m_p,\{Q_p(\lambda):\lambda\in\Lambda\}\right)
\]

does not determine its own next value under the centered contraction.

### Proof

Let \(\lambda_* = \min\Lambda\). Since \(0<a<1\),

\[
0<a\lambda_*<\lambda_*,
\]

so \(a\lambda_*\notin\Lambda\). Apply Lemma 1 with \(\Gamma=\Lambda\) and \(\mu=a\lambda_*\). This gives \(p^+\) and \(p^-\) with the same mean and the same scores on every tracked parameter, but different scores at \(a\lambda_*\). The transport identity then gives

\[
Q_{(p^+)'}(\lambda_*)
=(1-a)m+aQ_{p^+}(a\lambda_*),
\]

\[
Q_{(p^-)'}(\lambda_*)
=(1-a)m+aQ_{p^-}(a\lambda_*),
\]

which are unequal. \(\square\)

### Interpretation

Adding finitely many fixed positive values of \(Q\) does not repair exact general closure. The failure is structural: the contraction moves the required parameter toward zero.

This theorem does **not** rule out:

- exact closure on an invariant parametric distribution family;
- approximate closure with explicit error bounds;
- a finite state using different information that reconstructs the required transform values under additional support restrictions;
- closure for a finite prediction horizon when the required parameter orbit is supplied in advance.

## 5. Exact parameter-orbit transport

Iterating the microscopic contraction gives

\[
q_i^{(t)}=m_p+a^t(q_i^{(0)}-m_p).
\]

Therefore

\[
L_t(\lambda)
=e^{-\lambda(1-a^t)m_p}L_0(a^t\lambda),
\]

and

\[
Q_t(\lambda)
=(1-a^t)m_p+a^tQ_0(a^t\lambda).
\]

### Corollary 3 — exact finite-horizon orbit message

For a target grid \(\Lambda\) and horizon \(T\), the message

\[
\mathcal C_{\Lambda,T}
=
\left(
 m_p,
 \{Q_0(a^t\lambda):\lambda\in\Lambda,\ 0\le t\le T\}
\right)
\]

is sufficient to recover every \(Q_t(\lambda)\) for \(\lambda\in\Lambda\) and \(0\le t\le T\).

On the unrestricted finite-distribution class, omitted orbit values are generally not recoverable from finitely many other transform evaluations, by Lemma 1. The statement is informational and should not be promoted to a uniqueness theorem over all possible encodings.

For indefinite prediction, the required parameter orbit

\[
\{a^t\lambda:t=0,1,2,\ldots\}
\]

is countably infinite and accumulates at zero. Equivalent representations include the transform curve on that orbit, an analytic germ under suitable exponential-moment conditions, or a justified invariant-family parametrization.

## 6. Explicit exact dyadic witness family

The abstract proof can be made constructive for every number \(m\ge1\) of tracked scores.

Take

\[
\Lambda_m=\{\log2,2\log2,\ldots,m\log2\},
\qquad a=\frac12,
\]

and support

\[
q_k=k,\qquad k=0,1,\ldots,m+2.
\]

Define

\[
P_m(t)=(t-1)^2\prod_{j=1}^m(t-2^{-j})
      =\sum_{k=0}^{m+2}v_k t^k.
\]

Then

\[
\sum_k v_k=P_m(1)=0,
\]

\[
\sum_k kv_k=P_m'(1)=0,
\]

and, for \(j=1,\ldots,m\),

\[
\sum_k v_k2^{-jk}=P_m(2^{-j})=0.
\]

However,

\[
\sum_k v_k2^{-k/2}=P_m(2^{-1/2})\ne0,
\]

because \(2^{-1/2}\) is not one of the rational roots of \(P_m\).

Let

\[
u_k=\frac1{m+3},
\qquad
0<\varepsilon<\frac{1}{(m+3)\max_k|v_k|},
\]

and define

\[
p_k^\pm=u_k\pm\varepsilon v_k.
\]

These are strictly positive probabilities with equal mean and equal scores at all \(m\) tracked parameters, but different scores at \(\tfrac12\log2\). Their next \(Q_{\log2}\) values are therefore different.

### Five-point example for two tracked scores

For \(m=2\),

\[
P_2(t)=(t-1)^2(t-1/2)(t-1/4)
      =\frac18-t+\frac{21}{8}t^2-\frac{11}{4}t^3+t^4.
\]

Multiplying the coefficient vector by eight gives

\[
v=(1,-8,21,-22,8).
\]

Taking \(u_k=1/5\) and \(\varepsilon=1/200\) gives

\[
p^+=\left(\frac{41}{200},\frac{4}{25},\frac{61}{200},\frac{9}{100},\frac{6}{25}\right),
\]

\[
p^-=\left(\frac{39}{200},\frac{6}{25},\frac{19}{200},\frac{31}{100},\frac{4}{25}\right).
\]

They have exactly the same normalization, mean, \(L_{\log2}\), and \(L_{2\log2}\). At the omitted parameter \(\tfrac12\log2\),

\[
L_{p^+}-L_{p^-}
=\frac{27-19\sqrt2}{200}>0.
\]

Thus even mean plus two fixed scores fails to close the next \(Q_{\log2}\).

## 7. Reproducibility protocol

The accompanying script `validate_finite_grid_nonclosure.py`:

1. constructs \(P_m\) using exact rational arithmetic;
2. constructs strictly positive \(p^+\) and \(p^-\);
3. verifies normalization, mean equality, and all tracked Laplace equalities exactly;
4. verifies that the omitted dyadic transform differs;
5. evaluates the resulting future-score difference numerically at high precision.

The analytic proof remains primary. The script is a regression check, not evidence replacing the proof.

## 8. Claim discipline

### Established by the derivation in this note

- Every finite positive fixed grid of exponential effective scores fails to provide exact autonomous closure under the centered contraction on the unrestricted class of finite distributions.
- Exact finite-horizon prediction is obtained by carrying the required parameter orbit.
- An explicit exact dyadic witness exists for every finite grid size \(m\).

### Not established

- novelty in the mathematical literature;
- physical relevance of the centered contraction;
- empirical meaning of \(q\), \(\lambda\), or the transform curve;
- optimality of the orbit message among all encodings;
- approximate closure rates without tail, support, or cumulant assumptions;
- closure under a broader stochastic or nonlinear update.

## 9. Literature position

The proof uses standard ingredients: linear independence of exponential functions, finite generalized-moment indeterminacy, and invariant-observable closure logic. Existing work on truncated/generalized moment problems shows that finitely many generalized moments ordinarily leave a nontrivial class of representing measures, while Koopman theory frames exact reduced dynamics in terms of invariant observable subspaces. The theorem above specializes those ideas to the report's centered contraction and its parameter-rescaling identity.

A limited search did not locate this exact fixed-grid statement in the same notation. That absence is not a novelty proof. A publication draft should describe the result as a self-contained project-specific theorem unless a deeper literature audit establishes priority.

## 10. Next rigorous extension

The next non-ad-hoc problem is quantitative rather than ontological:

> Given bounded support \(q\in[L,U]\), a finite parameter grid, and a finite horizon, what are the sharp upper and lower bounds on the omitted transform value and therefore on the future score?

This is a generalized moment extremal problem. It would turn exact nonclosure into certified prediction intervals and create a clean bridge from impossibility to controlled approximation without assuming Gaussianity.
