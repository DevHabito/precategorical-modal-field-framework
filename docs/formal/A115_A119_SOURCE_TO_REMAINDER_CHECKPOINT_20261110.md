# A115–A119 source-to-remainder checkpoint — 10 November 2026

**Research branch:** `research/a115-a119-uniform-remainder-20261110`  
**Frozen scope:** reduced two-active-band C2(k) model, source (s\in[129/1000,133/1000]), \(\beta=1/8\), \(\delta=1/1875\), collision \(\tau=s(1+2\alpha/M)\), \(8\le\alpha\le45\), and fixed contact deficit \(4\le r\le19\).
**Editorial status:** partial **source-derived** formal algebra and explicit analytic error estimates. **The uniform \(O(M^{-3})\) theorem has not been proved end-to-end in Lean.**

## What has genuinely been verified

The exact finite regression [run 42914016273](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42914016273), job `exact-python`, **SUCCEEDED**, including `A115-A118 independent exact finite cofactor regression`. It reconstructs the actual finite (E_k) from the original ((A_a,B_a,\Delta B_a,H_a)) equations using `Fraction`, checks the auxiliary K/u decomposition and tests six parity-resolved finite inputs. It rejects changes that silently drop the full powers or replace (\tau^{-1}) with 1. No floating-point comparison determines a PASS.

The corrected Lean run [42914436667](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42914436667) at exact source commit `c025d081479fd9a27a841b3bc7135dedd4b35515` has individually successful kernel-replay jobs:

- `leanchecker (PrecategoryFormal.A115CofactorReducedCore)`, job `130174373472`: proves the exact reduced cofactor adjacent identity, including the (u^2K) and (u^3) remainders. Full-length powers are specialized to zero *only in this auxiliary lemma*.
- `leanchecker (PrecategoryFormal.A115FullPowerTail)`, job `130174373599`: introduces all (\beta^M,s^M,\tau^M) channels, establishes their exact mixed quadratic cancellation when (u=0), and verifies that their zero-power specialization matches the reduced cofactor.
- `leanchecker (PrecategoryFormal.A119CriticalSubstitutionIdentity)`, job `130174373540`: proves the algebraic substitution of the critical equation in the **published A118 formula**, under an explicit nonzero denominator, equals the real (widehat\Xi) expression certified by A119.

These three individual Lean jobs are PASS; the status of other jobs or the overall workflow, if still running, must be inspected independently. The *first* compilation attempts [42910102041](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42910102041) and [42912510306](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42912510306) FAILED due respectively to unnecessary `ring` tactics after a closed goal and to the missing `noncomputable` declaration for real division. The corrections changed no mathematical statement or hypothesis. These failed runs remain part of the engineering record.

The existing global finite-contact real positivity theorem `A119GlobalRealManifest` also passed in [run 42909538752](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42909538752), **46/46 SUCCESS**. That theorem covers the 25 permitted parity/deficit candidate cells of the explicit rational (widehat\Xi), but does not derive the tail cutoff outside those cells.

## What we have established analytically, not in Lean

The derivations and exact numerical comparisons are recorded in:

- [A115_A118_EXPLICIT_COLLISION_LOG_TAYLOR_BOUND_20261110.md](A115_A118_EXPLICIT_COLLISION_LOG_TAYLOR_BOUND_20261110.md): for (f(x)=(1+2\alpha x)^{-1/(2x)+\sigma}), (0\le x\le10^{-3}), (alpha\in[8,45]), (sigma\in\{0,1/2\}), an explicit uniform cubic remainder bound (5\cdot10^{10}x^3), with the corrected coefficients (alpha^2+2\sigma\alpha) and (-4\alpha^3/3-2\sigma\alpha^2) in the logarithmic exponent.
- [A115_A118_EXPLICIT_GEOMETRIC_Q_RESPONSE_20261110.md](A115_A118_EXPLICIT_GEOMETRIC_Q_RESPONSE_20261110.md): with (ho=99/100), the exact central (Q) responses satisfy (|U-U_0|<30ho^M) and (|V-V_0|<29ho^M). This includes proof of (L_h(\tau)\ge(7/10)\tau>0) and the finite-channel bound (K\le8^{18}(100/99)ho^M). All decisive decimal-independent rational inequalities were separately verified with `Fraction`.

Those are hand-auditable analytic arguments, **not** already kernel-replayed uniform estimates. The constants are intentionally non-optimized. The K prefactor is enormous; no claim of small finite-M error at (M=1000) follows without evaluating the eventual complete bound.

## What remains to prove to close the genuine obstacle

1. **Full finite-M algebra, not a model with v=0.** Combine the exact (\beta^M,s^M,\tau^M) cofactor with the reduced core and expose all mixed (u v_a), (u^2v_a) and (v_av_\tau) terms; provide a Lean identity with their explicit coefficients.
2. **Uniform coefficient bounds.** Prove the required alpha/s/parity/r bounds, including the third-order Taylor estimate, inside Lean or state a transparent external analytic dependency; obtain one final uniform constant for all normalized finite residuals.
3. **Source-derived coefficient identity.** Show that the actual original-cofactor Taylor expansion produces the **A117 (Lambda)** and the **A118 (Xi)** as the first two coefficients. The new `A119CriticalSubstitutionIdentity` theorem only replaces (q) in the *published* (Xi) formula; that is necessary but insufficient for source derivation.
4. **Uniform finite-M result.** For some (C<\infty) and (M_0), both independent of the frozen parameter box and parity/contact deficit, prove
   [
   \left|\frac{J_{M,k}}{\tau^{h+k}}
     -\frac{\Lambda_p}{M}-\frac{\Xi_p}{M^2}\right|
      \le C/M^3.
   ]
   The remainder in the current repository is supported by analytic arguments and computational identities, but this final assembly is **not** a Lean theorem.
5. **Contact selection and publication scope.** Keep A117's high-deficit exclusion, central support feasibility, and F2/F3 primal/dual optimality separate. Do not call the reduced sign result a global LP optimum, physical theory or original theorem without full prior-art review and external assessment.

The new theorem statements were not weakened after failed checks, and the `main` branch remains untouched.
