# Theorem: implication-edge escalation in 3+1 Minkowski sprinklings

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic theorem + finite-n diagnostic  
**Physical status:** transitive-orientation forcing after causal-arrow erasure  
**Novelty status:** implication classes and forcing are classical comparability-graph theory; the project-specific result is the Lorentzian small-disagreement escalation theorem below

## 1. Why edge space is the right object

For a comparability graph \(G\), two edges

\[
xy,\;xz
\]

directly force one another when

\[
yz\notin E(G).
\]

Equivalently, \(x,y,z\) induce a \(P_3\).

The transitive-orientation implication classes are the connected components of the forcing relation.

For a connected comparability graph,

\[
\boxed{
G\text{ is UPO}
\iff
\text{all edges belong to one undirected forcing/color class}.
}
\]

Thus the remaining reconstruction problem can be studied directly in edge space.

## 2. Continuum splitter volume of an edge

For an event \(x\), write

\[
A_x=\{z:z\sim x\}.
\]

For a comparable pair

\[
x\sim y,
\]

define

\[
\Delta(x,y)
=
\mu(A_x\triangle A_y).
\]

The region

\[
A_x\triangle A_y
\]

is exactly the continuum splitter region of the edge \(\{x,y\}\).

If a sampled point \(z\) lies there, it is comparable to exactly one endpoint.

Therefore the sampled edge \(\{x,y\}\) is directly forced with one of

\[
\{x,z\},
\qquad
\{y,z\}.
\]

## 3. The proved d=4 small-edge tail

The previous theorem established

\[
\boxed{
F_4(t)
:=
\Pr(
X\sim Y,\,
\Delta(X,Y)\le t
)
\sim
3\pi t^3.
}
\]

In particular, for sufficiently small \(t\),

\[
F_4(t)\le Ct^3.
\]

This cubic tail is the first ingredient in the escalation theorem.

## 4. Uniform comparable metric-ball lemma

Define

\[
B_t(x)
=
\{z:
z\sim x,\;
\Delta(x,z)\le t
\}.
\]

Then in \(d=4\),

\[
\boxed{
\sup_{x\in D}
\mu(B_t(x))
\le
Ct^2
}
\]

for all sufficiently small \(t\).

### 4.1 Low-degree chart

The graphon degree

\[
Q(x)=\mu(A_x)
\]

satisfies

\[
|Q(x)-Q(z)|
\le
\Delta(x,z).
\]

If

\[
Q(x)\le 4t
\]

and

\[
\Delta(x,z)\le t,
\]

then

\[
Q(z)\le5t.
\]

Hence

\[
B_t(x)
\subseteq
A_x\cap S_{5t},
\]

where

\[
S_s=\{u:Q(u)\le s\}.
\]

The low-degree internal-sparsity theorem gives

\[
\sup_{x\in S_{5t}}
\mu(A_x\cap S_{5t})
=
O(t^2).
\]

Thus

\[
\mu(B_t(x))
=
O(t^2)
\]

in the null-joint regime.

### 4.2 Away from the degree-zero joint

If

\[
Q(x)>4t,
\]

the exact comparable-pair disagreement polynomial has a nondegenerate local response.

In ordinary interior charts,

\[
\Delta(x,z)\le t
\]

forces a four-dimensional displacement of order \(O(t)\), giving volume \(O(t^4)\).

The only potentially weaker chart is a single-null-face chart approaching the joint.

There the linear coefficient in one causal increment can become small, but the exact disagreement polynomial contains the corresponding positive quadratic term.

Writing the local null-depth scale as

\[
s\asymp\sqrt{Q(x)},
\]

the two causal increments are bounded by the combination

\[
A
=
O\!\left(
\min\!\left\{
\sqrt t,\,
\frac{t}{Q(x)}
\right\}
\right),
\]

\[
B
=
O\!\left(
\frac{t}{\sqrt{Q(x)}}
\right),
\]

up to chart constants.

The causal angular cap contributes the factor \(AB\).

Integrating the exact conditional pair measure

\[
d\mu(z)
\asymp
AB\,dA\,dB\,du
\]

gives a uniform \(O(t^2)\) bound throughout the transition range

\[
Q(x)\ge4t.
\]

The remaining compact charts are strictly better.

Therefore

\[
\sup_x\mu(B_t(x))
=
O(t^2).
\]

## 5. Good and bad splitters

Fix

\[
\alpha\in\left(\frac12,1\right).
\]

Let

\[
e=\{x,y\}
\]

be a continuum comparable edge with

\[
\delta=\Delta(x,y).
\]

A splitter \(z\in A_x\triangle A_y\) is called **bad** when the new forced edge \(e_z\) satisfies

\[
\Delta(e_z)\le\delta^\alpha.
\]

Otherwise it is **good**.

Every bad splitter lies in

\[
B_{\delta^\alpha}(x)
\cup
B_{\delta^\alpha}(y).
\]

Therefore

\[
\mu(\text{bad splitters})
\le
C\delta^{2\alpha}.
\]

Because

\[
2\alpha>1,
\]

\[
\delta^{2\alpha}=o(\delta).
\]

Hence there exists

\[
\delta_0>0
\]

such that for every comparable edge with

\[
0<\delta<\delta_0,
\]

\[
\boxed{
\mu(\text{good splitters})
\ge
\frac{\delta}{2}.
}
\]

## 6. A sampled edge that fails to escalate

Condition on a sampled edge with continuum disagreement

\[
\Delta(e)=\delta<\delta_0.
\]

The remaining \(n-2\) sample points are iid.

The probability that none falls in the good-splitter region is at most

\[
\left(
1-\frac{\delta}{2}
\right)^{n-2}
\le
e^{-c n\delta}.
\]

Let \(Z_n\) be the number of sampled low-disagreement edges that have no good sampled splitter.

Then

\[
\mathbb E[Z_n]
\le
\binom n2
\int_0^{\delta_0}
e^{-cn\delta}\,
dF_4(\delta).
\]

Using

\[
F_4(\delta)\le C\delta^3
\]

and integration by parts,

\[
\int_0^{\delta_0}
e^{-cn\delta}\,
dF_4(\delta)
=
O(n^{-3}).
\]

Therefore

\[
\boxed{
\mathbb E[Z_n]
=
O(n^{-1}).
}
\]

Markov's inequality gives

\[
\boxed{
\Pr(Z_n>0)
\longrightarrow0.
}
\]

## 7. Edge-escalation theorem

With probability tending to one, every sampled edge \(e\) satisfying

\[
0<\Delta(e)<\delta_0
\]

has a directly forced edge \(e'\) such that

\[
\boxed{
\Delta(e')
>
\Delta(e)^\alpha.
}
\]

Since

\[
0<\Delta(e)<1
\]

and

\[
\alpha<1,
\]

\[
\Delta(e)^\alpha>\Delta(e).
\]

Thus following forcing moves gives a strictly increasing sequence

\[
\delta_0^{(edge)}
<
\delta_1
<
\delta_2
<
\cdots
\]

with

\[
\delta_{j+1}
>
\delta_j^\alpha.
\]

The finite sampled graph cannot support an infinite strictly increasing chain of distinct edge disagreements.

Therefore every implication class containing an edge eventually reaches the fixed core

\[
\boxed{
\mathcal E_{\mathrm{core}}
=
\{e:\Delta(e)\ge\delta_0\}
}
\]

with probability tending to one.

Equivalently,

\[
\boxed{
\text{every sampled implication class intersects }\mathcal E_{\mathrm{core}}
\quad\text{a.a.s.}
}
\]

## 8. Why d=2 is naturally different

The escalation argument depends on the small-edge tail being strictly better than quadratic.

In \(1+1\), the random-\(2\)-order problem has a nontrivial limiting UPO probability rather than convergence to one.

Peter Winkler's 1990 paper already establishes prior results on limiting unique orientability in the random dimension-two order ensemble.

The project independently derives the \(1/e\) limit, but does not claim priority for that asymptotic question.

The present \(d=4\) argument has

\[
F_4(t)=\Theta(t^3),
\]

so

\[
n^2F_4(1/n)=O(n^{-1}),
\]

and the microscopic non-escalating edge population disappears.

This is precisely the kind of dimensional separation absent in the \(1+1\) case.

## 9. Finite-n diagnostic

The repository script

tools/minkowski_edge_escalation_audit.py

checks the escalation rule directly.

A session audit with

\[
\alpha=\frac34,
\qquad
\delta_0=0.08
\]

showed the expected finite-size trend:

- at \(n=64\), violations were still visible;
- at \(n=128\), they were substantially rarer;
- at \(n=256\), almost every remaining violation in the tested runs was a zero-splitter edge, i.e. a true-twin-type microscopic obstruction.

The numerical audit is diagnostic only.

The asymptotic result is the analytic bound above.

## 10. What this theorem changes

Previously, arbitrary-size modules had to be tracked through splitter closure.

The edge-escalation theorem gives a stronger reduction:

\[
\boxed{
\text{all implication classes must touch a fixed macroscopic-disagreement edge core.}
}
\]

Therefore the full UPO problem no longer requires controlling a continuum of small module scales separately.

The remaining question is only:

> Are all edges in \(\mathcal E_{\mathrm{core}}\) in one implication class with probability tending to one?

If yes, then every edge in the unique nontrivial component is in that same class and the graph is UPO.

## 11. Continuum forcing connectivity

There is strong deterministic evidence for the final step.

Let

\[
\mathcal E^\circ
=
\{(x,y)\in D^\circ\times D^\circ:x\ll y\}.
\]

For a fixed \(x\), the set

\[
I^+(x)\cap D^\circ
\]

is connected by finite chains of spacelike steps.

If

\[
y_i,y_{i+1}\in I^+(x)
\]

are spacelike separated, then the two timelike edges

\[
xy_i,
\qquad
xy_{i+1}
\]

directly force one another.

For arbitrary timelike edges

\[
(x,y),
\qquad
(x',y'),
\]

choose a common future point

\[
z\in
I^+(x)\cap I^+(x')\cap D^\circ.
\]

Then one can:

1. move \(y\) to \(z\) by spacelike forcing steps while keeping \(x\) fixed;
2. move \(x\) to \(x'\) by spacelike forcing steps while keeping \(z\) fixed;
3. move \(z\) to \(y'\) while keeping \(x'\) fixed.

Thus the **continuum timelike-edge forcing graph is connected**.

What is still required is a uniform discretization lemma showing that a random sprinkling realizes these robust forcing paths simultaneously for every sampled core edge.

That is now the last unresolved step in this route.

## 12. Literature boundary

The forcing relation, implication classes, color classes, modular decomposition, and UPO criterion are classical.

Relevant sources include Gallai's transitive-orientation theory, Golumbic's comparability-graph treatment, and McConnell–Spinrad's modular-decomposition/transitive-orientation work.

The project-specific ingredients are:

- the Lorentzian disagreement metric
  \[
  \Delta(x,y);
  \]
- the cubic \(d=4\) edge tail
  \[
  F_4(t)\sim3\pi t^3;
  \]
- the uniform comparable-ball estimate
  \[
  \sup_x\mu(B_t(x))=O(t^2);
  \]
- and the resulting implication-edge escalation theorem.

No equivalent Minkowski-sprinkling result was located in the targeted review.

Absolute novelty is not certified.

## 13. Current frontier

The remaining statement is now sharply isolated:

\[
\boxed{
\Pr(
\mathcal E_{\mathrm{core}}
\text{ has more than one forcing class}
)
\stackrel{?}{\longrightarrow}
0.
}
\]

The continuum edge space is forcing-connected.

The final task is to transfer that connectivity uniformly to the finite random sample.

If that discretization closes, then the \(3+1\) orientation-recovery problem itself closes.
