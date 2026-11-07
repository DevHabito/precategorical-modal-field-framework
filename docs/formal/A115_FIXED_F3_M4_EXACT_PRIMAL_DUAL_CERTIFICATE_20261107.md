# Exact full-F3 optimum and uniqueness at one finite contract

**Date:** 7 November 2026  
**Status:** exact rational primal/dual certificate, checked on a clean GitHub runner.  
**Scope:** precisely one unrestricted finite LP: M=4, s=129/1000, target τ=1/2, β=1/8, γ=1/16, δ=1/1875. Nothing in this note asserts a theorem for all M or a universal A115 active set.

## What was proved

The full three-band finite LP, with support x=0,...,4, allows **all** P and Q atoms. They must be nonnegative, share scaled total mass t and first moment 2t, satisfy Q target normalization, and obey both orientations of the s, beta and gamma bands. The width coefficient for M=4 is epsilon=1/7500. Maximize the P target transform.

A complete exact certificate establishes

    maximum G_(1/2)(P)
      = 550870246006266889 / 533058861574687500
      = approximately 1.0334135415720573.

The optimum is **unique for this exact parameter choice**. The proof is not a floating-point solver verdict: every matrix, basic mass, multiplier, inactive-band slack and reduced cost is checked with Python fractions.Fraction. The published script imports the independent complete-primal/dual gate to cross-check the result using a second representation of the model.

## 1. Active primal solution

Variable order is P0,P1,P2,P3,P4,Q0,Q1,Q2,Q3,Q4,t.

The positive variables, exactly, are:

    P0 = 952055399372741 / 310951002585234375
    P1 = 1383257157247763554 / 932853007755703125
    P2 = 33501168761124749 / 34550111398359375
    P4 = 44447023668608 / 59702592496365
    Q1 = 8/5
    Q3 = 8/5
    t  = 16/5.

All remaining P/Q masses are zero. All masses are nonnegative. The Q target transform is (8/5)*(1/2+1/8)=1; both means are exactly 2t. All six two-sided band inequalities are checked exactly. Only **s upper (+)** and **gamma lower (-)** bind; all other band slacks are strictly positive.

The exact active 7×7 matrix consists of the five equality rows (two masses, two centered means, Q target) and those two binding bands, with the seven positive variables as its columns. Its nonzero exact determinant is

    -3980172833091 / 65536000000000.

Thus the active primal solution is uniquely determined by those seven equalities.

## 2. Exact dual certificate

Five unrestricted multipliers correspond, in order, to P mass, Q mass, P centered mean, Q centered mean, and Q target=1. Two positive inequality multipliers correspond to s+ and gamma-. The exact values are:

    aP = 161040603668 / 748152788175
    aQ = -5768619549207676 / 26652943078734375
    bP = -8785651 / 114527790
    bQ = 32777813513203283 / 355372574383125000
    v  = 550870246006266889 / 533058861574687500

    u_s     = 160156250000 / 63177346557 > 0
    w_gamma = 35670272 / 18737325 > 0.

Every other band multiplier is zero. **Every** P and Q dual reduced cost, including atoms outside the active support, is checked to be nonnegative. The common-mass t coefficient is also checked. The reduced cost is exactly zero at all seven positive primal variables and **strictly positive** at every absent variable; the smallest missing-variable reduced cost is

    31548043535176 / 26652943078734375 > 0.

All four inactive band slacks are strictly positive; the smallest is

    492876347779241 / 2132235446298750000 > 0.

The sum of the equality multipliers weighted by their right-hand sides equals v, because the only nonzero equality right-hand side is Q target=1. Both active inequality right-hand sides are zero. Exact primal and dual objectives coincide at the fraction above.

## 3. Why uniqueness follows

Weak duality bounds every feasible primal objective by the verified dual value. The exhibited primal attains that value, hence it is globally optimal.

Suppose a second primal also attained the same value. Equality in the dual bound, together with nonnegative primal variables, strictly positive missing-variable reduced costs, nonnegative band slacks and strictly positive multipliers on s+ and gamma-, forces:

1. every currently absent P/Q atom to have mass exactly zero;
2. the s+ and gamma- constraints to bind;
3. the five mass, centered mean and target equalities to hold.

Those are the same seven independent equations on the same seven remaining variables. Their determinant is nonzero. Therefore the second primal equals the first. This establishes **uniqueness** for the specified finite LP.

This reasoning requires the correct t-row dual condition: without that row a formally tempting bound v=0 could appear valid while the centered feasible witness has objective 1. The generic dual validator has an exact regression against that error.

## 4. Solver independence and reproducibility

A numerical HiGHS solve was used **only once to propose** the active support and binding bands. It is not a premise of the mathematical result, and the published audit does not import SciPy or a numerical solver.

The final checker reconstructs the solution using a handwritten exact rational Gaussian elimination, with an explicit nonzero-determinant check. It then independently checks all original LP inequalities, stationarity at every atom, strict complementarity on unused atoms and bands, objective equality and two deliberately invalid mutations.

- [Executable full F3 exact certificate](../../audits/a115_small_full_lp_exact_kkt_certificate_20261107.py)
- [Independent primal/dual acceptance gate](../../audits/a115_explicit_full_primal_and_dual_gate_20261107.py)
- [Canonical F2/F3 mathematical contract](../research/A115_A122_CANONICAL_LP_CONTRACT_AND_GATES_20261107.md)
- [General finite LP weak-duality Lean lemma](../../formal/lean/PrecategoryFormal/FiniteLPWeakDuality.lean)

The clean published-code [GitHub Actions run 42386200355](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42386200355) ended **SUCCESS** and printed the exact target objective, determinant, full primal/dual equality and strict slack verdict. That run contains the source revision 1bdb510a71d00e55a6e74366fa17cb7083c6d35e.

The Lean theorem proves **general finite LP weak duality**, not a Lean-checked computation of these particular seven basis coordinates. The latter remains an independently exact rational computational certificate.

## 5. What this result does not tell us

This M=4 optimizer has positive P support {0,1,2,4} and Q support {1,3}, with s+ and gamma- binding. It is **not** the A115 C2(k) sparse active-set architecture. An exact example of a different optimizer is not evidence that A115's claimed contacts apply to the full F3 LP.

The certificate does not prove persistence under changing s or τ, eventual active-set structure as M grows, the A118/A119 asymptotic expansion, A122's integer resonance, or novelty. It is instead a **fully closed, finite, auditable reference example** against which proposed general mechanisms can be tested.

A future paper should not conflate this proven instance with a whole-parameter theorem. The right next experiment is to extend the same exact primal/dual methodology to adjacent finite sizes and determine which support and band activities actually change.
