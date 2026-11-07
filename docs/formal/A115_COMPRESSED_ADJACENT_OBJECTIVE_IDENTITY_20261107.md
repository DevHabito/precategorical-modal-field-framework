# A115 — compressed adjacent objective, Cramer's rule, and the sign of E

**Date:** 7 November 2026  
**Status:** exact symbolic derivation, independent rational regression, and a newly submitted Lean 4 proof. The final kernel result is a separate gate.  
**Source:** the A81 and A83 reduced system, specialized through the A115 deformed target definitions.

## Question

Previous checkpoints verified the moment-adjusted basis and the ten-channel expansion of the cofactor expression, but there was still no explicit proof that its sign was tied to a *change in the compressed objective*. That gap matters: a polynomial determinant may be algebraically correct while the comparison of feasible candidates uses the opposite orientation.

I reconstructed the two active band equations from the original P and Q transforms rather than starting from an assumed sign rule.

## From the active bands to a two-variable linear system

For the P support `{0,k,M}`, write

```
P_r = A_r*t + B_r(k)*z,
A_r = (1+r^M)/2,  z = p_k.
```

For the Q support `{1,h,h+1}`, the central equations yield

```
Q_r = C_r + D_r*t.
```

The beta-lower and s-upper band equalities are

```
P_beta - Q_beta = -2*epsilon*t
P_s    - Q_s    = +2*epsilon*t.
```

Thus, with

```
H_beta = A_beta - D_beta + 2*epsilon
H_s    = A_s    - D_s    - 2*epsilon,
```

the two constraints reduce **exactly** to

```
B_beta(k)*z + H_beta*t = C_beta
B_s(k)*z    + H_s*t    = C_s.
```

These are active *equalities* imposed on one proposed compressed basis. Satisfying them does not imply that the remaining bands, nonnegative weights, or dual KKT constraints hold.

Set

```
Delta_k = B_beta(k)*H_s - B_s(k)*H_beta,
Z       = C_beta*H_s - C_s*H_beta.
```

If `Delta_k != 0`, Cramer's rule gives

```
t_k = [B_beta(k)*C_s - B_s(k)*C_beta]/Delta_k
z_k = Z/Delta_k.
```

The actual scaled target objective of that candidate is

```
V_k = A_tau*t_k + B_tau(k)*z_k.
```

It is therefore a *rational function* of the contact basis coefficients.

## Exact adjacent objective factorization

Write `Db=DeltaB_beta(k)`, `Ds=DeltaB_s(k)`, `Dt=DeltaB_tau(k)`. The next contact has `B_r(k+1)=B_r(k)+DeltaB_r(k)`. Define the already verified A115 cofactor factor

```
E_k = (A_tau*B_beta(k)-H_beta*B_tau(k))*Ds
    + (-A_tau*Db+H_beta*Dt)*B_s(k)
    + (-B_beta(k)*Dt+B_tau(k)*Db)*H_s.
```

An independent polynomial expansion proves

```
N_(k+1)*Delta_k - N_k*Delta_(k+1) = -Z*E_k,
N_k = A_tau*[B_beta(k)*C_s-B_s(k)*C_beta] + B_tau(k)*Z.
```

Consequently, provided both determinants are nonzero,

```
(V_(k+1)-V_k)*Delta_k*Delta_(k+1) = -Z*E_k.
```

Equivalently,

```
V_(k+1)-V_k = -Z*E_k / [Delta_k*Delta_(k+1)].
```

The sign of the *actual compressed-objective difference* is the sign of `E_k` **if** `Z<0` and `Delta_k*Delta_(k+1)>0`. A universal, assumption-free sign statement would be false.

### Reconciliation with the original A81/A83 convention

There is a potential sign trap in the notation. A81 constructs the two source polynomials with coefficients

```
Delta_source = B_s*H_beta - H_s*B_beta = -Delta_k
Z_source     = C_s*H_beta - H_s*C_beta = -Z.
```

A83 calls the contact-independent interior-mass numerator `Z_source` and proves its positivity on its **declared local domain**. Thus its statement that the cross numerator factors as `Z_source*E_k` is consistent with the present calculation:

```
-Z*E_k = Z_source*E_k.
```

The denominators also have the same positive *product* after both are negated. The older A113 notation `E=V_(k+1)-V_k` is best read as a shorthand for the **sign-controlling factor** unless the objective itself is redefined by normalization. For the literal transform-ratio objective, the exact rational prefactor above is necessary. The paper should state this explicitly to prevent sign ambiguity.

## Independent falsification and replication

The new script [`a115_independent_compressed_adjacent_identity_20261107.py`](../../audits/a115_independent_compressed_adjacent_identity_20261107.py) reconstructs `Q_r=C_r+D_r t` from the even/odd central three-site weights at `t=0` and `t=1`; it does not import the A115 audit implementation.

For each tested `M,s,tau,k`, it solves the two active band equalities with exact `fractions.Fraction`, reconstructs the P and Q weights, checks their mass/mean/target constraints, checks the beta-lower and s-upper bands, and calculates the target objective *directly* from the weights. It then tests the full cross-product formula and, when its sign hypotheses hold, the sign equivalence.

The verified GitHub Actions [run 42356754967](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42356754967) reported:

```text
PASS: exact primal active-band Cramer/adjacent identity checks:
  {'identities': 213, 'oriented': 213,
   'both_three_site_nonnegative': 159, 'other_orientation': 0}
PASS: synthetic sign orientation control:
  E positive / V decrease when Z positive
  (outside original model assumptions)
```

**Interpretation:** all 213 tested adjacent pairs satisfied the exact identity and the conditional sign orientation. Only 159 had all P and Q weights nonnegative at **both** contacts; those are still not certified as globally LP-feasible because the remaining transform bands and dual reduced costs were not audited in this test.

The synthetic sign-control point has `Z>0`, both determinants positive, `E>0`, and `V_(k+1)<V_k`. It is a mathematical counterexample to *dropping the factor-sign hypothesis in the abstract two-by-two algebra*, not a counterexample to the original A115 model.

## Lean formalization

New module:
[`formal/lean/PrecategoryFormal/CompressedAdjacentObjective.lean`](../../formal/lean/PrecategoryFormal/CompressedAdjacentObjective.lean).

The submitted statements are:

- `exact_adjacent_cross_difference`: universal polynomial factorization of the cross numerator.
- `two_ratios_adjacent_cross_difference`: exact adjacent rational difference with nonzero determinants.
- `compressed_objective_difference_identity`: the cross-multiplied objective identity.
- `oriented_adjacent_sign_transfer`: the sign implication in both directions, **provided** `Z<0` and `Delta_k*Delta_(k+1)>0`.

A first Lean run [42356645829](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42356645829) failed at line 45 with `No goals to be solved` because `field_simp` had already closed a rational identity and an unnecessary `ring` remained. The mathematical statements were not modified. Commit `05b0aca7b103ecf9faeb25fe707d5bd14ef563c0` removed the redundant tactic; its verification run is [42356782549](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42356782549). **Read the final CI status before claiming kernel certification.**

## Literature and interpretation

Cramer's rule, basis changes and reduced-cost optimality conditions are classical parts of linear optimization. The specific determinant equality here is an exact calculation for the selected active-band family, not a general new theory of optimality.

References for the general method:
- The archived project sources: [A81 reduced system](../../MFRP_Informational_Requirements_A39-A109/audits/a81_reduced_boundary_system_audit.py), [A83 exact factorization](../../MFRP_Informational_Requirements_A39-A109/docs/technical_notes/MFRP_next_step_seven_term_adjacent_sign_atlas.md), [A115 target deformation](../../MFRP_Informational_Requirements_A39-A109/research_updates/A115/A115_TARGET_NODE_DEFORMATION_EXACT_AUDIT_20260914.md).
- MIT OpenCourseWare, *Optimization Methods*, Fall 2009, lecture notes on Simplex I–II, Duality I–II, and Sensitivity Analysis: https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/pages/lecture-notes/
- The earlier project [literature and attribution record](../research/A115_A122_LITERATURE_AND_ATTRIBUTION_20261106.md) for historical parametric LP and moment optimization references.

## Next independent proof obligations

1. Derive the globally required signs `Z<0` and `Delta_k*Delta_(k+1)>0` under precise admissible parameter hypotheses, not from 213 examples.
2. Prove the adjacent compared candidates satisfy **all** primal bands and nonnegativity constraints, not just the two active equalities.
3. Construct an actual dual-feasible multiplier certificate with its row orientation and objective sense established explicitly.
4. Only then connect local compressed value comparisons to global LP optimality, and A118/A119 sign conclusions.

A positive compressed adjacent difference is not a certificate of global optimality. That is the substantive logical boundary this audit seeks to make explicit.

## Follow-up: Cramer elimination from the equations themselves

The first corrected module's [run 42356782549](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42356782549) finished **21/21 SUCCESS**, including the `CompressedAdjacentObjective` Leanchecker job.

Two further theorems were added to that same module. `active_band_cramer_solution` starts with the two actual linear band equalities and an explicitly nonzero determinant, and proves the formulas for the masses `z` and `t`. `active_band_objective_value` then derives the rational target objective without assuming the Cramer numerator as a definition.

The first attempt at this addition failed [run 42357055959](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42357055959) with `No goals to be solved` at line 150: `rw [hbeta, hs]` had completed the goal, leaving a redundant `ring`. The spare tactic was removed in commit `be87503ce701238ae779bd27be6545f65e9c8c7b` without altering the theorem or its hypotheses. The corrected build and individual kernel checks **passed 21/21** in [run 42357203452](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42357203452).

A separate [`CompressedActualBandComparison.lean`](../../formal/lean/PrecategoryFormal/CompressedActualBandComparison.lean) now starts with *two actual solutions* of the active band equations at adjacent contacts. It derives their objective difference and the conditional equivalence between `E_k>0` and `V_(k+1)>V_k`. This adds a direct bridge from the hypotheses of the candidate equations to the reduced sign formula. The [build on run 42357382631](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42357382631) **succeeded**; the two module-specific Leanchecker jobs must be checked separately before declaring the entire new statement kernel-certified.

## A real feasibility trap, preserved as a regression

The exact-rational test has a particularly useful failing *candidate*:

```text
M=24, beta=1/8, delta=1/1875,
s=129/1000, tau=1/2;
adjacent contact k=5 -> k=6.
```

The two active band equalities, the central Q target normalization and the mass/mean equations all hold for both algebraic candidates. The sign factor `E_(24,5)>0` and the **unscaled target objective increases** from k=5 to k=6.

However, the putative P mass at the left endpoint at k=6 is exactly

```
p_0 =
-3584502932965903373596977777684072721755589435382466075590968697323579413854720000
/
345047398895750303288444261617038319958450237568253037270226500133498976787761804121
< 0.
```

The adjacent index itself is valid (`7<=h-2=10`), but the k=6 P measure is **not nonnegative** and hence is **not a feasible measure**. This is not a counterexample to the exact E identity; it is a counterexample to interpreting every improving compressed candidate as admissible.

The case is now an exact `Fraction` assertion in `audits/a115_independent_compressed_adjacent_identity_20261107.py`. The [published-code CI run 42357508468](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42357508468) finished **SUCCESS**, including the regression and the prior 213 cross-product identities.

This concrete example is the reason that KKT and all primal feasibility checks must not be replaced by an adjacent objective sign calculation.
