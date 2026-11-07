# A113/A115–A122 corrective engineering review

**7 November 2026. Working branch:** formal/a115-a122-critical-audit-20261106.  
**Verdict:** substantial repair completed; full target-deformed LP optimality is **not yet certified**.

This report tracks the distinction between a theorem, a reproducible finite test, an active-set candidate, and a conjecture. Passing a solver or kernel run does not make an unstated implication valid.

## 1. Repair the A113 factor/objective confusion

The historical A113 theorem defines the cofactor factor E as though it were the literal difference between consecutive scaled target objectives. Under the verified A115 two-active-band equations the exact identity instead reads

    (V_(k+1)-V_k) * Delta_k * Delta_(k+1) = -Z * E_(M,k).

Thus the literal difference is the factor times a rational prefactor. The signs agree only under correctly oriented and independently justified sign hypotheses. Exact-rational controls, including M=521 inside A113's stated domain, falsify the literal equality while preserving the cross-product identity.

An [editorial erratum](../../MFRP_Informational_Requirements_A39-A109/research_updates/A113/session_artifacts/A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_THEOREM_20260911.md) is now at the top of the original note. The original assertion was retained, not silently erased. The erratum does not independently disprove or establish A113's sign-variation result.

## 2. Freeze the three different optimization objects

The [canonical LP specification](A115_A122_CANONICAL_LP_CONTRACT_AND_GATES_20261107.md) now separates:

- **F3(τ):** unrestricted finite two-measure LP with target-normalized Q, common mass and mean, nonnegative atoms, and two-sided bands at s, beta and gamma. Extending the frozen third-node contract to deformed tau is an explicit modeling assumption.
- **F2(τ):** the analogous unrestricted LP with only the s and beta observation bands. Its feasible set is generally larger than F3's.
- **C2(k):** the reduced, sparse P and Q architecture with two **active equalities**. It can produce an exact algebraic candidate that fails the remaining primal constraints.

It is scientifically invalid to promote a C2(k) comparison to an F3 optimum without proving that candidate's entire feasibility and its full dual certificate. The earlier inherited-gamma test eliminated both contacts in 213 sampled pairs, **not the full F3 feasible set**.

The original frozen A100 LP, including its gamma constraints, is used as provenance. No finite certificate from A100 at tau=1/2 is transferred to a deformed-target problem without revalidation.

## 3. A complete exact primal checker, with falsification controls

New source: [explicit primal and dual acceptance gates](../../audits/a115_explicit_full_primal_and_dual_gate_20261107.py). It evaluates, independently of the Cramer solver:

- atom support and nonnegativity;
- the two exact total-mass and mean equations, including a common positive scaled mass;
- Q target transform exactly equal to 1;
- **both sides** of every band selected by F2 or F3, with epsilon's correct parity scaling;
- the literal P target transform objective.

Everything is represented as exact Python Fraction objects. Each rejection identifies the actual failed requirement. The runner refuses optimized Python mode, which could suppress its assertions.

The deliberately invalid controls include wrong mass, wrong mean, wrong target normalization, negative support weight, an oversized transform gap that preserves the other primal equalities, an incorrectly signed dual multiplier, a missing dual band and a wrong dual t-row. The real C2(5) candidate at M=24 is valid in F2 but violates F3 gamma; the adjacent C2(6) solution has a negative P atom even in F2.

## 4. Constructive nontrivial full-primal feasibility

The earlier centered witness P=Q had objective 1. We also have a *strictly better feasible pair* for any admissible M and positive epsilon, using a small symmetric outward shift while keeping Q centered.

For even M=2h, let the scaled Q mass t be at h. Choose a=epsilon*t/8 and move mass a from Q's center to each site h-1 and h+1 when constructing P. Then

    G_r(P)-G_r(Q) = a*r^(h-1)*(1-r)^2.

For odd M=2h+1, take Q with equal masses t/2 at h and h+1, then shift a=epsilon*t/8 from each central site to h-1 and h+2 in P. Then

    G_r(P)-G_r(Q) = a*r^(h-1)*(1-r)*(1-r^2).

For every 0<r<1, the gap is strictly positive and no larger than a, which is smaller than 2*epsilon*t. Mass, first moment and Q target normalization remain exact; P masses remain nonnegative. Evaluating at r=tau gives a **strictly larger-than-1** scaled objective. This is a constructive feasible lower bound, not an optimal value or a novel theorem claim.

The executable regression passed 80 nontrivial rational F2/F3 models, alongside 80 centered models. It uses no floating-point threshold.

## 5. Duality: the right direction, without a made-up optimal certificate

The canonical specification explicitly includes free multipliers for both mass constraints, both centered mean constraints and the Q target equation, plus nonnegative multipliers for *both* sides of all observation bands. It gives a pointwise P reduced-cost inequality, a pointwise Q reduced-cost inequality and the usually forgotten coefficient inequality for the common mass t.

A feasible collection of those multipliers proves a global upper bound by weak duality. The code verifies the inequalities **at every finite support atom**, even those missing from a proposed sparse candidate. It also checks the sign of every band multiplier and the presence of every observation row.

A valid but loose universal certificate with upper bound tau^(-M) is implemented and tested. It is not a KKT optimum, and no claim of equality with the candidate objective is made.

A new Lean module, [FiniteLPWeakDuality.lean](../../formal/lean/PrecategoryFormal/FiniteLPWeakDuality.lean), formalizes the **general finite maximization LP weak-duality inequality** from exact nonnegative primal and dual constraints. This remains a general theorem, **not** an instantiation of the full F3 program or a tight dual certificate for A115. Its own CI build and module-specific kernel replay are separate evidence gates.

## 6. The previous fail-open tests were repaired

The independent A119 verifier originally printed positive tail bounds without asserting them; the independent A122 verifier similarly printed expected signs without requiring success. The gamma-band checker printed individual-contact counts without asserting them.

The tests now use mandatory exact assertions for the A119 cutoff and decay ratios, A122's two strict sign brackets and log domains, and the exact gamma counts. The corrected [A119/A122 CI checkpoint](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42377130346) passed.

The full F2/F3 gate initially passed [80 centered primal + 80 dual controls and eight negative controls](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42385152728). The next run [42385378198](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42385378198) passed 80 **nontrivial** feasible P!=Q controls as well. Three more deliberate invalid cases were added. The most recent CI conclusion must be read separately before treating those additional controls as verified.

## 7. Unresolved, and not to be fixed by rhetoric

The full monotonicity derivative bridge was not kernel-certified in Lean and its failed experiment remains archived. The exact A118-to-A119 asymptotic derivation has not been reconstructed end-to-end independently. A122's discrete integer resonance realization is not proved by two continuous sign brackets. F3(τ) lacks a tight verified dual certificate and complementary slackness for the claimed active sets. The literature on moment problems, linear-fractional optimization, sparse extreme measures and parametric LP predates this research; priority remains unestablished.

These are mathematical obligations, not a reason to disregard separately proved algebraic identities. The next step is to derive **one actual full F3 dual certificate with all atom reduced costs** for an explicitly fixed finite example before attempting universal support and asymptotic claims.

**Decision:** retain proven algebra; correct false literal equalities; keep F2, F3 and C2 distinct; require full exact primal and dual gates; withhold global optimum and originality claims until the missing proofs exist.

## 8. Final, source-matched verification: two complete finite optimality examples

Two exact primal-dual certificates now close the **entire F3 optimization problem at individual finite parameters**, rather than merely supplying loose feasible witnesses or bounds.

- [Even M=4 exact full-F3 certificate](../formal/A115_FIXED_F3_M4_EXACT_PRIMAL_DUAL_CERTIFICATE_20261107.md). Exact unique optimal objective: 550870246006266889/533058861574687500. Active bands s+ and gamma-. [Published-code CI 42386200355](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42386200355): **SUCCESS**.
- [Odd M=5 exact full-F3 certificate](../formal/A115_FIXED_F3_M5_EXACT_PRIMAL_DUAL_CERTIFICATE_20261107.md). Exact unique optimal objective: 123288732982051199633/110644995632951812500. Active bands s+ and gamma-. [Published-code CI 42386517555](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42386517555): **SUCCESS**.

Both certificates use a candidate support suggested during discovery, but the published proof uses only rational Gaussian elimination, full primal constraints, all dual reduced costs, strictly positive complementary slacks and a nonzero active determinant. All of those conditions are checked by the published code, cross-validated against the separate full F3 acceptance tool. The certificates establish **global unique optima only for their respective fixed finite contracts**. Neither proves a universal support pattern.

The generic [Lean weak-duality theorem](../../formal/lean/PrecategoryFormal/FiniteLPWeakDuality.lean) passed the project build and individual Leanchecker on [run 42385255807](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42385255807): **26/26 SUCCESS**. Its scope is general finite LP weak duality. It is not a Lean proof of the two specific rational coordinate certificates.

The strengthened primal/dual acceptance gate, with deliberately wrong constraints and the false bound created by omitting the common-mass t row, reported **12 deliberately invalid controls rejected** together with 80 centered and 80 nontrivial F2/F3 primal instances. [Exact-audit run 42385813659](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42385813659): **SUCCESS**.

**Corrective verdict:** the two finite F3 examples are individually closed by exact rational primal/dual certificates; the target-deformed A115–A122 family is still not proved globally optimal, and the source A113 sign classification is not certified anew by these finite checks.
