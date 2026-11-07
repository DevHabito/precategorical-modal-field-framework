# A115 — Third-node gamma feasibility under the A81 contract

**Date:** 7 November 2026  
**Status:** exact finite conditional stress test; **not** a refutation of A115's stated compressed algebraic theorem.  
**Branch:** `formal/a115-a122-critical-audit-20261106`

## Why this test matters

The preceding A115 adjacent-contact derivation starts from two active transform bands, at beta=1/8 and at s in [129/1000,133/1000]. Its exact rational checks show 213 adjacent objective identities, of which 159 pairs have nonnegative P and Q weights.

However, A81's original compressed-branch study explicitly defines a **third** transform node, gamma=1/16, and gamma upper/lower slack boundaries. Its source `MFRP_Informational_Requirements_A39-A109/audits/a81_reduced_boundary_system_audit.py` defines `GAMMA=1/16` and uses the gamma bounds to determine boundary polynomials.

The A115 deformed-target audit `MFRP_Informational_Requirements_A39-A109/research_updates/A115/a115_target_deformation_exact_audit.py` contains **no gamma node or gamma-band feasibility calculation**. Its documented scope is exact compressed factorization and sign stress; it explicitly does not transfer all A113/A114 lifted active-set results to deformed tau.

This raises a **conditional compatibility question**:

> If the A81 gamma-band constraint is retained unchanged when tau is deformed, do the A115 beta-lower/s-upper active candidates remain primal-feasible?

This is a test of the *lift from the compressed algebraic family to an inherited full optimization problem*. It is not an assertion that A115 itself imposes the gamma band.

## Tested contract and exact arithmetic

The independent `audits/a115_independent_compressed_adjacent_identity_20261107.py` reconstructs both three-site measures from the two active equations, with

```
P_beta - Q_beta = -2*epsilon*t
P_s    - Q_s    = +2*epsilon*t
epsilon = (1/1875)*tau^h * (1 if M even else (1+tau)/2)
Q_tau = 1.
```

The new `audits/a115_gamma_band_contract_stress_20261107.py` checks the inherited third-node band **only as a conditional additional constraint**:

```
gamma = 1/16
-2*epsilon*t <= P_gamma - Q_gamma <= 2*epsilon*t.
```

All transforms and inequalities use exact `fractions.Fraction`. No numerical tolerance or floating-point sign comparison enters the verdict.

The finite grid is **exactly the earlier 213 adjacent-pair sample**, with

```
M in {24,25,40,41,100,101,521,522}
s in {129/1000,131/1000,133/1000}
tau in {14/100,1/5,1/2,4/5}
k in {max(2,b-1),b,b+1}, subject to 2<=k and k+1<=floor(M/2)-2,
b=min{j: s^(2j)<=tau^M}.
```

### Observed finite verdict

| Check | Number of adjacent pairs |
|---|---:|
| Total checked | 213 |
| Both P and Q supports nonnegative at both contacts | 159 |
| Both contacts satisfy the inherited gamma band | 0 |
| Both contacts nonnegative **and** gamma-feasible | 0 |

All 426 *individual* algebraic contacts in this finite sample violate the inherited gamma band, under the declared gamma and tolerance convention.

For a transparent nonnegative-weight witness, choose `M=24`, `s=129/1000`, `tau=1/5`, `k=9`. The active beta and s equalities and Q target normalization hold, both P and Q supports are nonnegative, but

```
(P_gamma-Q_gamma)/(2*epsilon*t) > 1.
```

The script records the exact rational ratio. In an exploratory display, it was approximately 5572.07, but the CI proof obligation is the rational inequality, not that rounded display.

### Interpretation

**The A115 compressed factor algebra can be correct even if the inherited A81 gamma constraint eliminates its candidate support.** The two statements have different scopes.

If the full deformed-target LP *does* include the same gamma band, these sampled active bases are not feasible for that LP. This does **not** imply the full LP is infeasible: other supports and active sets may satisfy the constraints. It also does not imply the gamma band is automatically part of A115's declared algebraic contract.

The first priority is now to freeze a **single explicit primal optimization contract** for the proposed A115–A122 paper, including all source nodes, all bands, target normalization, positivity, support range and objective. A global KKT certificate is meaningful only after that contract is fixed.

## Regression, source, and limitations

- [Conditional exact gamma stress script](../../audits/a115_gamma_band_contract_stress_20261107.py)
- [Independent A115 active-band reconstruction](../../audits/a115_independent_compressed_adjacent_identity_20261107.py)
- [A81 original third-node implementation](../../MFRP_Informational_Requirements_A39-A109/audits/a81_reduced_boundary_system_audit.py)
- [A115 deformed target implementation](../../MFRP_Informational_Requirements_A39-A109/research_updates/A115/a115_target_deformation_exact_audit.py)

No statement is made for all M, all s, or all tau. This is a finite exact **compatibility** audit, not a theorem of universal gamma infeasibility, nor a claim of novelty.

Classical reference for why feasibility and dual constraints cannot be skipped: *Applied Mathematical Programming*, chapter 4, duality and complementary slackness, https://web.mit.edu/15.053/www/AppliedMathematicalProgramming.pdf (accessed 7 November 2026). Related finite-support moment LP precedent: A. Prékopa, *The discrete moment problem and linear programming*, Discrete Applied Mathematics 27 (1990), 235–254, DOI 10.1016/0166-218X(90)90068-N.

## Next gate

Before extending asymptotic claims to global optima:

1. Verify whether gamma=1/16 and its original tolerance are included in the *deformed* LP under consideration.
2. If yes, do not use the sampled beta/s-only active bases as global candidates; search for a feasible lifted support and a valid dual certificate.
3. If no, state explicitly that A115–A122 investigate a different, reduced two-band optimization problem, and do not import global optimality conclusions from A81/A114.
4. Keep the algebraic A119/A122 certificates independent of either interpretation until the full contract is specified.
