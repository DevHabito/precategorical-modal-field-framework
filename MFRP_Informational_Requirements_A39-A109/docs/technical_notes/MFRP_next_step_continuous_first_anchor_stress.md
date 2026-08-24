# Continuous First-Anchor Stress and Exact Local Sensitivity

**Programme:** Modal Field Research Programme  
**Provisional audit:** A65  
**Author line:** Felipe Gianini Romero  
**Status:** exact right-local theorem for nondegenerate active bases plus dense continuous counterexample search; no global continuous monotonicity theorem

## Technical abstract

A64 found that every optimal integer-catalogue design used the first admissible
anchor

\[
\mu+1.
\]

A65 tests whether this persists when that anchor is released continuously.

For every one of the 240 A64 contracts, choose the smallest-\(\gamma\)
minimax-optimal completion containing the boundary pair:

\[
D_\alpha
=
\{\alpha,\mu+2,\gamma\}.
\]

The first anchor varies on

\[
\boxed{
\alpha\in
\left[
\mu+1,\,
\mu+2-2^{-8}
\right].
}
\]

The result has two separate logical layers.

### Exact local layer

Set

\[
s=2^{-\alpha}.
\]

For an active Charnes–Cooper basis,

\[
B(s)z(s)=b.
\]

At the boundary

\[
s_0=2^{-(\mu+1)},
\]

exact differentiation gives

\[
\boxed{
z_s(s_0)
=
-B(s_0)^{-1}B_s(s_0)z(s_0).
}
\]

If

\[
\rho(s)=c_B^\top z(s),
\]

define

\[
\boxed{
\kappa_\alpha
=
-s_0
\left.
\frac{d\rho}{ds}
\right|_{s=s_0}.
}
\]

Then

\[
\boxed{
\left.
\frac{d\rho}{d\alpha}
\right|_{\alpha=\mu+1}
=
(\log2)\kappa_\alpha.
}
\]

The audit produced exact rational branch-derivative certificates in

\[
\boxed{232/240}
\]

contracts, and every one had

\[
\kappa_\alpha>0.
\]

Among them,

\[
\boxed{226/240}
\]

also had strictly positive basic variables, active inequality multipliers, and
nonbasic reduced costs. These conditions certify that the same basis remains
optimal in a right neighborhood. Therefore the boundary is a strict
right-local minimizer for the selected completion in those 226 contracts.

Six additional contracts had exact positive branch derivatives but zero
reduced costs, so strict basis stability could not be asserted.

Eight contracts had seven-variable degenerate boundary optima and were not
resolved by the declared eight-variable basis extraction.

The exact sensitivity factors satisfy

\[
\boxed{
0.000172903737911054
\le
\kappa_\alpha
\le
0.642304213354513.
}
\]

Their median is approximately

\[
0.0409885428336831.
\]

### Continuous stress-atlas layer

Every contract was evaluated at 129 first-anchor positions, producing

\[
\boxed{30\,960}
\]

linear-programme evaluations.

Three points per contract were independently recomputed with a second HiGHS
algorithm, producing 720 cross-checks. The maximum discrepancy was

\[
\boxed{
3.11\times10^{-12}.
}
\]

Every contract was strictly increasing at every adjacent grid step:

\[
\boxed{240/240}.
\]

The smallest observed adjacent increase in the minimax ratio was

\[
\boxed{
4.87209274258049\times10^{-7}.
}
\]

No continuous-grid counterexample was found.

The grid is a dense counterexample search, not a proof between grid points.

---

## 1. Exact active-basis theorem

Only the first observation row depends on \(s\). Consequently, the derivative
of the active solution requires one exact rational linear solve:

\[
Bz_s=-B_sz.
\]

At the boundary, every matrix entry is rational because

\[
s_0=2^{-(\mu+1)}.
\]

### Theorem 1

Fix a support, mean, target, normalized error contract, and completion

\[
\{\alpha,\mu+2,\gamma\}.
\]

Suppose that at

\[
\alpha_0=\mu+1
\]

the active basis satisfies:

\[
z_B>0,
\]

positive multipliers for all active observation inequalities, and positive
reduced costs on every nonbasic variable.

If

\[
\kappa_\alpha>0,
\]

then there exists \(\eta>0\) such that

\[
\rho(\alpha)>\rho(\alpha_0)
\]

for every

\[
\alpha\in(\alpha_0,\alpha_0+\eta).
\]

Strict primal and dual inequalities are open conditions, so the basis remains
optimal for sufficiently small perturbations. The active value branch is
differentiable and has positive right derivative.

---

## 2. Certificate coverage

The contracts separate as follows:

| Classification | Count |
|---|---:|
| Strict right-local primal–dual certificate | 226 |
| Positive exact derivative, degenerate reduced cost | 6 |
| Seven-variable unresolved degeneracy | 8 |

Thus strict local optimality is proved for

\[
\boxed{94.17\%}
\]

of the complete A64 stress domain.

An exact positive derivative was obtained for

\[
\boxed{96.67\%}
\]

of the domain.

The unresolved cases are not negative-derivative cases. They are cases where
the selected optimum has only seven numerically positive variables, so the
eight-variable sensitivity theorem does not apply.

No perturbation was introduced merely to force them into the theorem.

---

## 3. Continuous counterexample search

The grid points are

\[
\alpha_j
=
\mu+1+
j\frac{1-2^{-8}}{128},
\qquad
j=0,\ldots,128.
\]

The point \(\mu+2\) is excluded because it coalesces with the fixed second
anchor and changes the rank of the information system.

For every contract,

\[
\rho(\alpha_{j+1})-\rho(\alpha_j)>0.
\]

The largest total relative increase from the boundary to the
near-coalescence point was approximately

\[
\boxed{285.26\%}.
\]

Thus, in the most sensitive contracts, moving the first observation toward
coalescence substantially worsened ambiguity.

---

## 4. Scientific interpretation

The first admissible observation is consistently the most valuable local
measurement of the omitted target.

Moving it away sacrifices near-target information. The higher anchors still
constrain rapidly decaying components, but they do not replace that loss.

This behavior persists under:

- five support sizes;
- four mean fractions;
- three target exponents;
- exact and normalized noisy observations;
- different optimal third-anchor completions.

The first-boundary law is therefore much more robust than the boundary-pair
uniqueness claim rejected by A64.

---

## 5. Logical status

### Established

1. Exact active-basis sensitivity identity.
2. Exact positive first-anchor derivatives in 232 contracts.
3. Strict right-local optimality in 226 contracts.
4. Explicit classification of every remaining degeneracy.
5. Strict increase on all 240 declared continuous grids.
6. Independent cross-solver agreement.
7. No counterexample in 30,960 LP evaluations.

### Not established

1. Monotonicity between every pair of grid points.
2. A theorem for the eight seven-variable degeneracies.
3. A theorem for arbitrary supports and means.
4. Monotonicity for every possible fixed completion.
5. A theorem allowing the other anchors to reoptimize with \(\alpha\).
6. Continuous microscopic supports.

---

## 6. Next rigorous target

A larger numerical atlas is no longer the right move.

The next step should decompose the interval into exact active-basis phases in

\[
s=2^{-\alpha}.
\]

For each phase:

1. derive the rational value branch;
2. locate exact transition roots;
3. certify primal and dual feasibility;
4. prove the derivative sign with Bernstein or Sturm methods;
5. join the phases continuously.

That would upgrade the stress result into a genuine global continuous theorem
for the declared finite-contract family.
