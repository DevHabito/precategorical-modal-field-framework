# Theorem: critical near-whole complement window in 3+1

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** superseded quantitative localization note; the apparent square-root window is eliminated by MINKOWSKI_NEAR_WHOLE_TIP_CLEARANCE_RATE_20261112.md  
**Physical status:** finite-rate refinement of the \(3+1\) arrow-erasure recovery theorem  
**Novelty status:** the concentration tools are standard; the \(\sqrt n\) localization follows from the project-specific Minkowski degree/co-degree tails and internal-sparsity geometry

## 1. Motivation

The \(3+1\) orientation-recovery theorem gives

\[
p_4^{\mathrm{UPO}}(n)\to1.
\]

Comparable true twins satisfy

\[
\Pr(T_n>0)
\sim
\frac{9\pi}{n}.
\]

All fixed-size non-twin modular defects are already

\[
O(n^{-2})
\]

or smaller, and balanced linear modules are superpolynomially rare.

The only remaining quantitative question is whether a near-whole module can contribute another term of order \(n^{-1}\).

This note localizes any such possible contribution to the square-root complement scale.

## 2. Statement

Let

\[
C_n
\]

be the unique edge-containing component of the \(d=4\) sampled comparability graph on the high-probability component event.

Let

\[
M\subsetneq C_n
\]

be a proper non-stable module and define

\[
L
=
|C_n\setminus M|.
\]

For every fixed

\[
\eta>0,
\]

the following hold.

### Below the square-root window

\[
\boxed{
\Pr\!\left(
\exists M:
1\le L\le n^{1/2-\eta}
\right)
=
o(n^{-1}).
}
\]

### Above the square-root window but below linear scale

For any deterministic

\[
\varepsilon_n\downarrow0,
\]

\[
\boxed{
\Pr\!\left(
\exists M:
n^{1/2+\eta}\le L\le\varepsilon_n n
\right)
=
o(n^{-m})
}
\]

for every fixed \(m>0\), after choosing \(\varepsilon_n\) sufficiently slowly if needed.

Consequently, any non-twin near-whole obstruction that could compete with the \(9\pi/n\) true-twin scale must satisfy

\[
\boxed{
L
=
n^{1/2+o(1)}.
}
\]

## 3. External module types

Write

\[
O=C_n\setminus M.
\]

Every vertex of \(O\) is either complete or anticomplete to \(M\).

Let

\[
U
=
\{z\in O:z\text{ complete to }M\},
\]

and

\[
N
=
\{z\in O:z\text{ anticomplete to }M\}.
\]

Because \(C_n\) is connected,

\[
U\ne\varnothing.
\]

A vertex in \(U\) has sampled co-degree at most

\[
L-1+I_n,
\]

where \(I_n\) is the number of isolated vertices outside \(C_n\).

A vertex in \(N\) has sampled degree at most

\[
L-1.
\]

## 4. Polynomial tail control for the isolate count

The \(d=4\) low-degree tail is

\[
g_4(q)=O(q).
\]

Fix any desired power \(A>0\).

Choose

\[
q_n
=
B\frac{\log n}{n}
\]

with \(B\) sufficiently large.

The number of sampled points with

\[
Q_4\le q_n
\]

is binomial with expectation

\[
O(\log n).
\]

Chernoff concentration gives a constant \(C_A\) such that

\[
\Pr(
\#\{Q_4\le q_n\}>C_A\log n
)
\le
n^{-A}.
\]

For a sampled point with

\[
Q_4>q_n,
\]

the probability of being isolated is at most

\[
(1-q_n)^{n-1}
\le
n^{-B+o(1)}.
\]

A union bound therefore gives

\[
\boxed{
\Pr(
I_n>C_A\log n
)
\le
n^{-A}
}
\]

after increasing \(B,C_A\).

Thus isolates can be bounded by \(O(\log n)\) with arbitrarily high polynomial confidence.

## 5. Small complements

Take

\[
1\le L\le n^{1/2-\eta}.
\]

On the isolate-good event,

\[
I_n\le C\log n.
\]

If

\[
L\ge C\log n,
\]

any \(u\in U\) has sampled co-degree at most \(2L\).

The \(d=4\) sampled small-co-degree mixture bound gives

\[
\mathbb E
\#\{v:\bar D(v)\le2L\}
\le
C\frac{L^4}{n^3}.
\]

Therefore

\[
\Pr(U\ne\varnothing)
\le
C\frac{L^4}{n^3}.
\]

At the upper endpoint,

\[
\frac{L^4}{n^3}
\le
n^{-1-4\eta}.
\]

Using dyadic \(L\)-ranges contributes only an \(O(\log n)\) factor.

Hence

\[
\boxed{
\Pr(
\exists M:
C\log n\le L\le n^{1/2-\eta}
)
=
O(
n^{-1-4\eta}\log n
)
=
o(n^{-1}).
}
\]

If

\[
L<C\log n,
\]

then every \(u\in U\) has co-degree \(O(\log n)\).

The same mixture bound gives

\[
O\left(
\frac{\log^4 n}{n^3}
\right),
\]

again \(o(n^{-1})\).

Combining the two subranges proves the below-window statement.

## 6. Large sublinear complements

Now take

\[
L\ge n^{1/2+\eta},
\qquad
s=\frac Ln.
\]

Then

\[
ns^2
=
\frac{L^2}{n}
\ge
n^{2\eta}.
\]

This produces a growing Chernoff exponent.

## 7. Continuum localization of U

Every \(u\in U\) has sampled co-degree at most

\[
L+O(\log n).
\]

For large \(L\), this is at most \(2L\).

Choose a sufficiently large fixed constant \(A\).

If the continuum co-degree satisfies

\[
1-Q_4(u)>As,
\]

then the conditional mean sampled co-degree is at least a fixed multiple of \(L\).

Chernoff gives

\[
\Pr(
\bar D(u)\le2L
\mid
1-Q_4(u)>As
)
\le
e^{-cL}.
\]

A union bound gives

\[
\boxed{
U
\subseteq
T_{As}
:=
\{x:1-Q_4(x)\le As\}
}
\]

except with probability \(e^{-n^{\Omega(1)}}\).

The tip tail gives

\[
\mu(T_{As})
=
O(s^4).
\]

Thus the number of continuum \(U\)-candidates is binomial with mean

\[
O(ns^4).
\]

Because

\[
ns^4
=
s^2(ns^2)
=
o(ns^2),
\]

Chernoff gives

\[
\boxed{
|U|
\le
c_1ns^2
}
\]

with superpolynomially high probability, for a sufficiently small fixed \(c_1>0\).

## 8. First localization of N

Every \(z\in N\) has sampled degree at most

\[
L.
\]

Exactly as in the qualitative near-whole proof, Chernoff concentration implies

\[
\boxed{
N\subseteq
S_{As}
=
\{Q_4\le As\}
}
\]

except with probability \(e^{-cL}\).

## 9. Internal sparsity pushes N to scale s squared

The low-degree internal-sparsity theorem gives

\[
\sup_{x\in S_{As}}
\mu(
A_x\cap S_{As}
)
\le
C_0s^2.
\]

Choose

\[
B>2C_0.
\]

If \(z\in N\) satisfies

\[
Q_4(z)>Bs^2,
\]

then

\[
\mu(
A_z\setminus S_{As}
)
\ge
c_2s^2.
\]

The number of sampled neighbors of \(z\) outside \(S_{As}\) has mean at least

\[
c_2ns^2.
\]

Every such sampled neighbor must lie in \(O\).

It cannot lie in \(N\), because \(N\subset S_{As}\).

Therefore it must lie in \(U\).

But the previous section gives

\[
|U|
\le
c_1ns^2
\]

with \(c_1<c_2/2\).

Chernoff therefore yields

\[
\Pr(
z\in N,\,
Q_4(z)>Bs^2
)
\le
e^{-cns^2}.
\]

Because

\[
ns^2\ge n^{2\eta},
\]

a union bound over all sampled vertices and dyadic scales remains superpolynomially small.

Thus

\[
\boxed{
N\subseteq
S_{Bs^2}
}
\]

with superpolynomially high probability.

## 10. Too few N candidates

The \(d=4\) degree tail gives

\[
\mu(S_{Bs^2})
=
O(s^2).
\]

Hence the number of sampled candidates for \(N\) is binomial with mean

\[
O(ns^2).
\]

But the complement has size

\[
L=ns,
\]

and

\[
ns^2=o(ns).
\]

A binomial upper-tail estimate gives

\[
\Pr(
\#S_{Bs^2}^{\mathrm{sample}}
\ge L/2
)
\le
\exp(
-cL\log(1/s)
).
\]

The same is true for the event that the \(U\)-candidate population contributes a positive fraction of \(L\).

Therefore

\[
\boxed{
\Pr(
\exists\text{ module at a fixed dyadic scale }L
)
\le
e^{-n^{\Omega(\eta)}}
}
\]

uniformly for

\[
L\ge n^{1/2+\eta}
\]

and \(L=o(n)\).

Summing over \(O(\log n)\) dyadic scales preserves a superpolynomial bound.

## 11. Critical window

The two estimates leave only

\[
n^{1/2-\eta}
<
L
<
n^{1/2+\eta}.
\]

Since \(\eta>0\) is arbitrary, a competing near-whole obstruction at the true-twin scale must satisfy

\[
\boxed{
L=n^{1/2+o(1)}.
}
\]

This is the first quantitative localization of the residual large-module problem.

## 12. Why the square-root scale appears

At

\[
L=\sqrt n,
\qquad
s=n^{-1/2},
\]

the expected number of near-universal tip candidates is

\[
n s^4
=
n^{-1}.
\]

This is exactly the \(d=4\) true-twin failure scale.

At the same time,

\[
ns^2
=
1,
\]

so the internal-sparsity Chernoff exponent stops growing.

Thus the square-root window is not an artifact of the proof.

It is the scale at which the rare tip vertex and the low-degree joint layer meet the \(1/n\) target.

Whether this window contains a genuine second obstruction or whether an additional geometric constraint suppresses it is now the central quantitative question.

## 13. Current convergence-rate frontier

The verified contributions are now:

### True twins

\[
\Pr(T_n>0)
\sim
\frac{9\pi}{n}.
\]

### Fixed-size non-twin modules

\[
O(n^{-2}).
\]

### Non-twin escalation failures

\[
O(n^{-2}).
\]

### Balanced linear modules

\[
\exp\left(
-\frac{n}{2\log n}
\right).
\]

### Near-whole modules outside the square-root window

\[
o(n^{-1}).
\]

Therefore a failure of the candidate law

\[
1-p_4^{\mathrm{UPO}}(n)
\stackrel{?}{\sim}
\frac{9\pi}{n}
\]

can now come only from a near-whole module with complement

\[
\boxed{
|C_n\setminus M|
=
n^{1/2+o(1)}.
}
\]

That was the next target at the time of this note.

The subsequent middle-band nonneighbor argument proves the stronger estimate

\[
\Pr(
\text{near-whole module}
)
=
O(n^{-3})
\]

in \(d=4\), so the square-root window does not contribute at order \(n^{-1}\).

The current quantitative endpoint is

\[
\texttt{MINKOWSKI\_ALLD\_ORIENTATION\_RECOVERY\_RATE\_THEOREM\_20261112.md}.
\]
