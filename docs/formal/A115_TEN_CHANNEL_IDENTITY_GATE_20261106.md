# A115: universal cofactor-to-ten-channel identity — formalization gate

**Date:** 2026-11-06  
**Branch:** `formal/a115-a122-critical-audit-20261106`  
**Formal module:** `formal/lean/PrecategoryFormal/TargetFactorTenChannel.lean`

## Question

Does A115's declared reduced adjacent factor
`E = X ΔB_s + Y B_s + W H_s`, with
`X=A B_beta-H_beta B_tau`, `Y=-A ΔB_beta+H_beta ΔB_tau`,
and `W=-B_beta ΔB_tau+B_tau ΔB_beta`, expand **identically**
into the ten channels used in A115–A122?

## Exact reduction

For arbitrary real `beta,tau,s,A,H_beta,H_s,ab,at,as_,bk,tk,sk,K`, set:

```
B_r = r^k - 1 + K*a_r
dB_r = (r-1)*r^k + a_r
a_r = (1-r^M)/M,  K = k.
```

The formal theorem treats `bk,tk,sk,ab,at,as_,K` as **independent real variables**, so it asserts an unrestricted polynomial identity. The source model is recovered by substituting `bk=beta^k`, `tk=tau^k`, `sk=s^k`, `K=k`, and `a_r=(1-r^M)/M` with positive integer `M`.

The ten coefficients match the A115 executable audit `coeffs`: three pairwise product channels (`beta*s`, `beta*tau`, `s*tau`), three pure exponential channels, three `k*r^k` confluent channels, and one constant channel.

A separate SymPy expansion (with independent symbolic variables for all inputs, without substitutions from the main script) gave **zero** for `cofactor_expression - expanded_expression`. This is a reproducible algebraic cross-check, not a Lean proof.

Lean file `TargetFactorTenChannel.lean` supplies the exact universal identity with a `ring` proof, no `sorry`, `admit`, or nonstandard axiom. The module is imported by the project and included as an individual `leanchecker` matrix target. The corresponding GitHub Actions build **must** pass before calling it formally validated.

Track CI:
https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42307413377

## Interpretation and limitations

This identity validates a nontrivial **algebraic junction** between the cofactor form and the channel expansion. It does NOT prove:

- that the source cofactor is derived from the original primal/dual LP correctly;
- feasibility of either probability measure or the transform-band constraints;
- validity of the asymptotic estimates A116–A122;
- the precise coefficient asymptotics for A118;
- the A119 covering-certificate theorem in Lean;
- originality.

Do not call the ten channels ten independent theorems. The coefficient identity follows by polynomial algebra; the potentially interesting theory is the subsequent parametric asymptotic sign classification.

## Next stringent proof gate

1. Formalize `B(M,k,r)` and `ΔB(M,k,r)` with natural exponents and integer `M>0`; connect the universal-polynomial variables to those exact definitions.
2. Define `E` from the original finite-support primal/dual constraints and show this *is* the declared cofactor expression. No renaming of expressions may substitute for that derivation.
3. Formally derive the `J_tau,k` cancellation for the **full** ten-channel expression with `tau>0` and exact integer exponents.
4. Keep the global LP-feasibility and novelty gates separate from the algebra.

**Epistemic classification:** formal algebra submitted to Lean verification, no new mathematical discovery claimed from the expansion alone.

## Execution and corrections

The first CI attempt failed to parse the variable name `at`, a Lean reserved keyword. It was renamed to `aτ` without changing any formula.

Next, run [42307614789](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42307614789) **successfully built** `TargetFactorTenChannel.lean`, but the overall build failed in `TargetFactorBasisBridge.lean`: the real-valued division definition required `noncomputable`, and strict warning-as-error rejected a tactic composition. The follow-up commit `2908039bdcb9b893022e4348cac2cd80206cef12` marked the definition `noncomputable` and replaced the tactic with a direct `calc` proof.

GitHub Actions [run 42307816396](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42307816396), on the corrected code, reported the overall **Lean build SUCCESS**. The individual `leanchecker` jobs for both new modules were QUEUED at the time of this entry. Their completion must be checked independently.

The new bridge states two separate facts with `M,k : Nat` and `M≠0`:
```
finiteBasis M k r = r^k - 1 + k(1-r^M)/M
finiteBasis M (k+1) r - finiteBasis M k r
  = (r-1)r^k + (1-r^M)/M
```
This is a direct connection to the exact finite basis, not just a generic polynomial identity. Neither statement proves global primal or dual feasibility.
