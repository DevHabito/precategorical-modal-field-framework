# Low-degree internal sparsity and a sub-square-root component bound in 3+1

**Date:** 2026-11-12  
**Author:** Felipe Gianini Romero  
**Status:** analytic geometric lemma + probabilistic component bound + Monte Carlo regression  
**Physical status:** arrow-erased Minkowski causal-set comparability graph  
**Novelty status:** the graphon and random-graph tools are established; no equivalent Minkowski low-degree internal-sparsity lemma or component bound was located in the targeted review

## 1. Motivation

The degree-tail theorem gives

\[
g_4(q)
=
\mu\{x:Q_4(x)\le q\}
\sim
3\pi q.
\]

This places the \(3+1\) causal graphon in the critical graphon regime

\[
g(q)=\Theta(q).
\]

For a general critical graphon, this degree-tail information alone is not enough to prove that isolated vertices are the only source of disconnectedness.

The Minkowski kernel has additional geometric structure.

The key fact established here is:

> low-degree events are much sparser internally than their total mass suggests.

## 2. Low-degree region

Define

\[
S_q
=
\{x\in D:Q_4(x)\le q\}.
\]

From the degree-tail theorem,

\[
\mu(S_q)
=
\Theta(q).
\]

For sufficiently small \(q\), the set \(S_q\) lies inside a null-joint chart.

In the coordinates

\[
a=1-r+t,
\qquad
b=1-r-t,
\]

there is a constant \(C\) such that

\[
x\in S_q
\quad\Longrightarrow\quad
a_x,b_x
\le
C\sqrt q.
\]

This follows because \(Q_4\) has a unique zero at the null joint and

\[
Q_4(a,b)
=
\frac{
[a(2-b)]^2+[b(2-a)]^2
}{16}.
\]

## 3. Restricted graphon degree

For \(x\in S_q\), define the degree into the low-degree region

\[
h_q(x)
=
\int_{S_q}
W_4(x,y)\,d\mu(y).
\]

Then

\[
\boxed{
\sup_{x\in S_q}
h_q(x)
=
O(q^2).
}
\]

### Geometric proof

Fix \(x\in S_q\).

Any \(y\in S_q\) also has

\[
a_y,b_y=O(\sqrt q).
\]

If \(x\prec y\), define

\[
A=a_y-a_x\ge0,
\qquad
B=b_x-b_y\ge0.
\]

Then

\[
A,B=O(\sqrt q).
\]

The causal condition is

\[
2r_xr_y(1-\cos\theta)<AB.
\]

Inside the small joint chart,

\[
r_x,r_y
\ge
c_0>0.
\]

Hence

\[
1-\cos\theta
=
O(q).
\]

On the relative two-sphere, the allowed angular cap has normalized area

\[
O(q).
\]

The allowed \((a_y,b_y)\)-region has area

\[
O(q).
\]

The normalized spacetime density is bounded on this chart.

Therefore one time orientation contributes

\[
O(q)\cdot O(q)
=
O(q^2),
\]

and including both orientations does not change the order.

Thus

\[
h_q(x)=O(q^2)
\]

uniformly over \(x\in S_q\).

## 4. Internal edge mass

Define

\[
e(q)
=
\int_{S_q\times S_q}
W_4(x,y)\,
d\mu(x)d\mu(y).
\]

Using the restricted-degree bound,

\[
e(q)
=
\int_{S_q}
h_q(x)\,d\mu(x)
\]

and hence

\[
\boxed{
e(q)=O(q^3).
}
\]

Since

\[
\mu(S_q)^2
=
\Theta(q^2),
\]

the conditional edge density among low-degree events satisfies

\[
\boxed{
\frac{
e(q)
}{
\mu(S_q)^2
}
=
O(q).
}
\]

Thus the low-degree layer becomes internally sparse as

\[
q\downarrow0.
\]

This is additional structure not implied by the critical degree tail alone.

## 5. Numerical regression

The repository tool

tools/minkowski_low_degree_internal_sparsity.py

samples independent point pairs and estimates

\[
g_4(q)
\]

and

\[
e(q).
\]

A two-million-pair run gave:

| \(q\) | \(g_4(q)/q\) | \(e(q)/q^3\) |
|---:|---:|---:|
|0.02|8.208|6.125|
|0.03|7.915|5.352|
|0.05|7.424|5.572|
|0.08|6.790|5.318|

The first ratio approaches the analytic limit

\[
3\pi
=
9.424777\ldots
\]

slowly from below.

The second remains of constant order, consistent with

\[
e(q)=\Theta(q^3).
\]

The Monte Carlo values are regression checks only.

## 6. Connected \(k\)-sets inside \(S_q\)

Take \(k\) iid graphon points.

For their induced graph to be connected, it must contain at least one spanning tree.

Cayley's formula gives

\[
k^{k-2}
\]

labeled spanning trees.

For a fixed rooted tree, integrate leaves recursively.

The root has mass at most

\[
\mu(S_q)=O(q),
\]

and each child integration contributes at most

\[
\sup_{x\in S_q}h_q(x)=O(q^2).
\]

Therefore

\[
\boxed{
\Pr(
X_1,\ldots,X_k\in S_q
\text{ and the induced graph is connected}
)
\le
C^k
k^{k-2}
q^{2k-1}
}
\]

for a constant \(C\) independent of \(k\) and sufficiently small \(q\).

This reproduces the same exponent

\[
2k-1
\]

that appeared in the null-joint module hierarchy, now as a uniform tree bound.

## 7. Graphon degree versus sampled graph degree

Let a sampled vertex have graphon degree

\[
Q=q.
\]

Its graph degree satisfies

\[
D\mid Q=q
\sim
\operatorname{Binomial}(n-1,q).
\]

If a vertex belongs to a connected component of order \(k\), then

\[
D\le k-1.
\]

Fix \(A>0\) and use the threshold

\[
q_{n,k}
=
A
\frac{
k\log n
}{
n
}.
\]

For \(Q\ge q_{n,k}\), the conditional mean degree is at least

\[
(1-o(1))Ak\log n.
\]

For sufficiently large \(n\), a standard Chernoff lower-tail bound gives

\[
\Pr(
D\le k-1
\mid
Q\ge q_{n,k}
)
\le
n^{-cAk}
\]

for an absolute constant \(c>0\).

Choosing \(A\) sufficiently large and taking a union bound shows that, with probability tending to one, every vertex lying in a component of order \(k\) in the range considered below satisfies

\[
Q\le q_{n,k}.
\]

## 8. Component bound below the square-root scale

Let \(N_k\) be the number of connected components of order \(k\).

On the high-probability event from the previous section, every such component is a connected \(k\)-set inside

\[
S_{q_{n,k}}.
\]

Hence

\[
\mathbb E[N_k]
\]

is bounded by

\[
\binom nk
C^k
k^{k-2}
q_{n,k}^{2k-1}.
\]

Using

\[
q_{n,k}
=
A\frac{k\log n}{n}
\]

and

\[
k!
\ge
\left(\frac{k}{e}\right)^k,
\]

the bound has the form

\[
\mathbb E[N_k]
\le
\frac{n}{k^3\log n}
\left[
C_A
\frac{
k^2\log^2 n
}{
n
}
\right]^k.
\]

Therefore, for every fixed

\[
\varepsilon>0,
\]

uniformly over

\[
2\le k\le n^{1/2-\varepsilon},
\]

the total probability of any nontrivial component in this size range tends to zero.

Thus:

\[
\boxed{
\Pr
\left(
\exists\text{ connected component }C:
2\le|C|\le n^{1/2-\varepsilon}
\right)
\longrightarrow0.
}
\]

This is the first component estimate in the project whose allowed component size grows polynomially with \(n\).

## 9. What is already known at larger scales

The causal graphon is connected.

Janson's connected-graphon theorem therefore gives

\[
\frac{|C_1|}{n}
\overset{p}{\longrightarrow}
1.
\]

So components of linear order other than the giant are already excluded.

Combining that result with the theorem above leaves only an intermediate window:

\[
\boxed{
n^{1/2-o(1)}
\lesssim
|C|
=
o(n).
}
\]

This is substantially narrower than the previous unrestricted mesoscopic gap.

## 10. Relation to the 2026 connectivity theorem

Hladký and Viswanathan prove full asymptotic connectivity for connected graphons satisfying

\[
g_W(q)=o(q).
\]

They explicitly leave the finite-positive critical regime

\[
\frac{g_W(q)}q
\to\beta\in(0,\infty)
\]

outside their main theorem and formulate a conjecture that local minimum-degree obstructions should asymptotically account for fixed-order connectivity failures.

The Minkowski \(d=4\) graphon satisfies

\[
\beta=3\pi.
\]

The internal-sparsity estimate

\[
e(q)=O(q^3)
\]

is extra geometric information that is absent from the general graphon hypothesis.

It is the mechanism that allows the present component bound to go beyond what the degree tail alone provides.

## 11. Current consequence for UPO recovery

UPO allows isolated vertices, but not multiple edge-containing connected components.

The present theorem shows that, in \(3+1\),

\[
\boxed{
\text{no second nontrivial component of size }
\le n^{1/2-\varepsilon}
}
\]

survives asymptotically.

Macroscopic competing components are also excluded by connected graphon theory.

The remaining component ambiguity is now confined to a genuinely intermediate scale.

This is separate from internal modular ambiguity inside the giant component.

The next research target is to extend the same low-degree geometry or splitter-cascade method across the remaining window

\[
n^{1/2-o(1)}
\ll k\ll n.
\]

## 12. Literature boundary

The spanning-tree union bound, Chernoff inequalities, graphon degree tails, and connected-graphon giant-component theory are classical.

The project does not claim those tools.

The project-specific ingredient is the Lorentzian estimate

\[
\sup_{x\in S_q}
\mu(A_x\cap S_q)
=
O(q^2),
\]

and its use to control nontrivial component sizes in the critical Minkowski causal graphon.

No equivalent estimate or resulting sub-square-root component theorem was located in the targeted literature review.
