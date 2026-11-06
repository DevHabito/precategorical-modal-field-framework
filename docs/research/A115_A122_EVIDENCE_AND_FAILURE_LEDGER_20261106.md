# Evidence and failure ledger: A115–A122

*Updated 6 November 2026. This is an execution record, not a list of results we hoped to obtain.*

This ledger distinguishes source claims, finite observations, symbolic identities, Lean-certified statements, and pending work. Each result is tied to the script, source module, commit, or GitHub Actions run that can be inspected. Failed attempts are kept alongside the successful corrections. A failed compiler command is not automatically a mathematical counterexample, and a passing script is not automatically a proof of the whole theorem.

## 1. Lean formal verification: observed successful checkpoints

| Revision or run | Actual observation | What this supports | What it does not support |
|---|---|---|---|
| [42304567864](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42304567864) | Lean build and 16 individual Leanchecker jobs passed | A115 basic central identities and finite denominator algebra | Full primal/dual feasibility |
| [42306617445](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42306617445), source commit `0227750ae48ba265de19201cb376e2297683fba5` | **17/17 jobs succeeded**, including `TargetDeformationAudit` Leanchecker | Necessary-and-sufficient nonnegativity of the three central Q weights | The whole coupled two-measure LP |
| [42307816396](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42307816396), source commit `2908039bdcb9b893022e4348cac2cd80206cef12` | **19/19 jobs succeeded**, including `TargetFactorTenChannel` and `TargetFactorBasisBridge` Leanchecker | Universal cofactor-to-ten-channel polynomial identity; finite-basis channel and difference identities | Derivation of the cofactor from a primal/dual optimum or the asymptotic A116–A122 chain |

The formal project uses [Lean 4.33.1](../../formal/lean/lean-toolchain), Mathlib revision v4.33.1, and the project [Lean workflow](../../.github/workflows/lean-formal.yml). A source-level scan rejects `sorry` and `admit`. A successful build plus individual kernel replay is stronger evidence than a successful source-only scan.

The main Lean modules added in the study:

- [Central deformation, denominator and weight viability](../../formal/lean/PrecategoryFormal/TargetDeformationAudit.lean)
- [Universal cofactor expansion](../../formal/lean/PrecategoryFormal/TargetFactorTenChannel.lean)
- [Exact finite-basis bridge](../../formal/lean/PrecategoryFormal/TargetFactorBasisBridge.lean)

## 2. Exact and independent computational checks

| Script / evidence | Arithmetic | Observed result | Honest boundary |
|---|---|---|---|
| [A115 independent central reconstruction](../../audits/a115_independent_central_reconstruction_20261106.py) | Python `fractions.Fraction` | **1,515** three-equation checks; **505** denominator checks; **2,020** independent `D_r` slope checks, all passed | Finite deterministic controls |
| [A115 central feasible interval](../../audits/a115_independent_feasibility_bounds_20261106.py) | `Fraction` | **1,400/1,400** sign-versus-interval comparisons passed, including endpoints and outside points | Tests the Q block only; it is not a test of all LP constraints |
| [A119 independently written rational certificate](../../audits/a119_independent_fraction_certificate_20261106.py) | `Fraction` interval extension | **2,304** even + **4,096** odd cells with positive certified lower endpoints; cutoff lower bounds positive | Accepts the stated A119 formula for `Xi-hat`; its derivation from A118 is not independently proved |
| [A122 independently written log brackets](../../audits/a122_independent_rational_log_brackets_20261106.py) | `Fraction`, rigorous finite logarithm-series remainder | At `s=129/1000`: `Omega_even(xi)<0` for `tau=131/1000` and `Omega_even(xi)>0` for `tau=132/1000` | Shows a continuous parameter sign change, not realization by a discrete rounding subsequence |

On **6 November 2026**, two local scripts matching the checked-in A119 and A122 routines were actually executed again with Python **3.13.5**. Their observed output included:

```text
even boxes 2304 worst bound
  7962094616280060340361057850523941099377/
  4460543890481278214239707910840320000000
  approx 1.7850053293435872 location (4, 0, 0)
odd boxes 4096 worst bound
  3296636265099577642233577213168576496429665038806348563/
  2438741833785351580293579578096010608476160000000000000
  approx 1.351777469607197 location (4, 0, 0)
cutoffs True 0.0020902493780287305 True 0.00024277493510525955

tau 131/1000 omega
  -0.001972611525827406 -0.001972611525744094
  certified sign True
tau 33/250 omega
  0.0029866169718171763 0.0029866169718171767
  certified sign True
```

The decimal figures display exactly computed rational bounds; the script comparisons use exact arithmetic. The rational interval values themselves are the certificate, **not** the rounded decimal output. See the earlier [A119/A122 independent audit](../novelty/A119_A122_INDEPENDENT_CERTIFICATE_RECHECK_20261106.md).

### Run everything from the checked-in files

```bash
python3 audits/a115_independent_central_reconstruction_20261106.py
python3 audits/a115_independent_feasibility_bounds_20261106.py
python3 audits/a119_independent_fraction_certificate_20261106.py
python3 audits/a122_independent_rational_log_brackets_20261106.py
```

The dedicated GitHub Actions [exact arithmetic workflow](../../.github/workflows/a115-a122-exact-audits.yml) runs precisely those scripts with Python 3.13. Record its job status independently; do not promote a local result to a GitHub CI result until the actual job completes.

## 3. Failed and corrected Lean attempts

These failures are relevant engineering evidence. They did not by themselves falsify the mathematical statements.

| Failing run | Observed fault | Corrective action / subsequent evidence |
|---|---|---|
| [42305718215](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42305718215) | `linarith failed to find a contradiction` at two positivity-proof steps | Reassociated `h(v/D)=(hv)/D` explicitly, instead of expecting tactic normalization; later sufficiency compilation passed |
| [42306216903](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42306216903) and [42306337134](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42306337134) | Proof script reported `No goals to be solved` after `field_simp` | Removed the redundant `ring` calls; later 17/17 successful run [42306617445](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42306617445) |
| [42307413377](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42307413377) | Parser rejected `at` because it is a reserved Lean keyword | Renamed the variable `aτ` |
| [42307614789](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42307614789) | The ten-channel module built, but the finite-basis module required `noncomputable` for real division and had a strict tactic-style warning | Marked the real-valued definition `noncomputable`, replaced the tactic with a `calc` proof; 19/19 jobs passed in [42307816396](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42307816396) |

**Important distinction:** these were source/tactic/type errors; no source theorem was rescued by changing its mathematical hypotheses. The public CI history contains more unsuccessful intermediate builds than the representative examples listed here; this table is an **identified failure log**, not an assertion that no other failures occurred.

## 4. Source claim ledger: what is not yet Lean-proved

| Research stage | Project manuscript says | Independently established in this checkpoint |
|---|---|---|
| A115 | Target deformation and the ten-channel cofactor factor | Central block, nonnegativity iff, basis bridge, algebraic cofactor expansion: **Lean-checked**; derivation from primal/dual optimum still open |
| A116 | Compact-uniform eventual positivity and boundary layer | Not kernel-formalized in the new Lean modules |
| A117 | Parity-resolved leading collision classification | Not kernel-formalized |
| A118 | Second-order collision coefficient `Xi` | Not independently reconstructed from the original constraints |
| A119 | Positivity of `Xi` along all specified critical surfaces | Reproduced rational 6,400-cell sign check; full theorem chain **not Lean-certified** |
| A120–A121 | Fixed-interior rounding phase and sign staircase | Not kernel-formalized |
| A122 | Near-resonant rounding layer and continuous double-critical sign change | Two exact interval-log sign checks independently reproduced; integer subsequence realization **not established** |

The original manuscripts use words such as `PROVED` for their own derivations. In this ledger, that is a **source-reported status**. It should not be silently replaced with `Lean-verified` unless the actual formal theorem has been checked.

## 5. Unresolved tests and potential counterexamples

1. Can the A115 sign factor be derived from the full primal/dual LP and the correct KKT orientation, not just an algebraically defined cofactor?
2. Could an admissible Q-block configuration fail another transform-band or positivity requirement for the second measure? Test the **whole** finite LP, not the isolated block.
3. Does independent expansion of the A118 formula reproduce the precise rational function used in the A119 interval script? A wrong algebraic reduction could survive all 6,400 sign checks.
4. Does the analytic tail argument genuinely exclude all later contact deficits in A119 under the frozen constants?
5. Are resonance endpoints and the ceiling convention handled consistently in A117 and A122?
6. Which claimed boundary classifications are direct consequences of classical variation-diminishing theory, and which are genuinely family-specific? This remains a literature task.

**Current verdict:** the recorded algebraic Lean statements have passed kernel replay, and the specified rational checks have passed. The whole A115–A122 program has **not** been independently formalized, and originality has **not** been certified.

## 6. Published-code CI verification (confirmed)

The new GitHub Actions workflow `A115-A122 exact arithmetic audits` ran on the checked-in audit scripts at source commit `80a7797b33d54781789405736c4470ec41d000e1`.

**Run:** [42314533047](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42314533047)  
**Observed status:** `completed / success`.  
**Individual steps:** Python 3.13 setup, syntax checking, A115 central reconstruction, A115 feasibility, A119 interval covering, and A122 rational logarithm sign brackets all reported `success`.

This is the first reported successful execution of all four scripts **from their published repository paths** in a clean GitHub runner. It is distinct from the prior local Python re-execution. The scope limitations in Sections 2 and 4 remain unchanged: the workflow does not run Lean, derive the A119 reduced formula from A118, or establish literature novelty.

## 7. Genuine mathematical refutations, not merely failed build jobs

The original [A115 source audit](../../MFRP_Informational_Requirements_A39-A109/research_updates/A115/A115_TARGET_NODE_DEFORMATION_EXACT_AUDIT_20260914.md) tested whether the frozen threshold `M>=521` implies a positive central combination `J_{tau,b+1}` for every deformed target. **It does not.**

The source reports a coarse rational grid with `J>0` in **192/192** cases, while the stronger three-sign package held in only **170/192**. Crucially, a separate near-wall stress test returned **58 positive and 2 negative among 60 admissible controls**. The apparently reassuring coarse grid was not a theorem.

The two legitimate negative points, copied from A115 and **recomputed here with independent exact fractions**, are:

| M | s | tau | b | Factor-domain check | Exact sign | Recomputed fraction SHA-256 |
|---|---|---|---:|---|---|---|
| 521 | 131/1000 | 141/1000 | 252 | `b+2=254 <= h-2=258` | `J<0` | `dc0efb5b23581db2a5c4983e87097884582dddee1fd68d5ec28d9b459bef8bac` |
| 521 | 133/1000 | 143/1000 | 252 | `b+2=254 <= h-2=258` | `J<0` | `e60c0f4b4bf1ef74867c3d80cebb5fb805364b7d542114fe2f858b6aeea7e34f` |

The SHA-256 hashes were recomputed from the canonical `numerator/denominator` representation and **matched the original A115 document exactly**. This independently supports the **failure of universal positivity** in the claimed domain. It does not invalidate the restricted compact-interior assertions of A116.

One earlier candidate must remain visible but **rejected**:

```text
M = 521, s = 129/1000, tau = 667/5000
b = 257, h = 260; b+2 = 259 > h-2 = 258
algebraic J < 0, but the A84 adjacent factor is out of domain
DISPOSITION: REJECTED_AS_COUNTEREXAMPLE_OUTSIDE_A84_ADJACENT_FACTOR_DOMAIN
```

The source note explicitly withdraws this purported counterexample. I recomputed its negative algebraic value and the failed domain check, which are **both** needed to report the result correctly.

Reproduction file: [A115 near-wall counterexamples](../../audits/a115_near_wall_exact_counterexamples_20261106.py). The updated [exact arithmetic CI workflow](../../.github/workflows/a115-a122-exact-audits.yml) now contains a dedicated step for this test. Inspect the run before claiming that the five-script CI has passed.

### A real failed computational attempt and its correction

The initial local replay of these three points was interrupted on the *third* point by Python's `ValueError: Exceeds the limit (4300 digits) for integer string conversion`. The first two hashes had already matched. This was an output/serialization limit, not a failed rational sign comparison. I corrected the replay with `sys.set_int_max_str_digits(0)`, ran all three points again, and confirmed both valid hashes and the rejected-domain disposition. The checked-in script includes this explicit setting and explains why.

This is precisely why the evidence log keeps **three different categories**: a refuted mathematical conjecture, an invalid would-be counterexample, and a transient execution failure. Combining them under a generic `FAILED` heading would obscure what actually happened.

## 8. Five-script CI including true refutations — confirmed

The subsequent workflow run [42314767131](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42314767131), from source commit `33921fb02786932d63b1cdc3b2dbacbf037e9bb6`, finished **completed / success**. Its syntax check and **all five** independent exact-rational script steps passed, including the new A115 near-wall refutations. This independently confirms that the version of the code now checked into the repository runs successfully on a clean Python 3.13 GitHub runner.

The previously observed local large-integer serialization failure remains recorded in Section 7 as a **failed earlier attempt**. Successful reruns do not erase the history, and the two `J<0` controls remain true **mathematical refutations**, not test-system errors.
