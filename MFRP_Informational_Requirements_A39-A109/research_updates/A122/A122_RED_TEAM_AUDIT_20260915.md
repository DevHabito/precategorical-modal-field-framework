# A122 — red-team audit

**Date:** 2026-09-15  
**Verdict:** **PASS WITH SCOPE**

## Attacks performed

1. **Naive second-order attack.** A static `Psi=0 => sign(Omega)` rule is rejected unless the rounding phase approaches the front by `o(1/M)`. At `1/M` phase distance, the linearized A121 front contributes at the same order.

2. **Missing-polynomial-term attack.** The ten-term A115 representation was regrouped to verify that, for a fixed interior pair, only the `s*tau` product channel and target-affine channel contribute at algebraic orders. Their exact algebra gives `Phi + Omega/M`; all other channels are exponentially small.

3. **Parity attack.** The proof retains both `sigma_p` and `a_p`; odd parity is not copied from even parity.

4. **Finite arithmetic attack.** Six exact `Fraction` controls compare the full normalized factor with the polynomial core. Four even controls have exact remainder `<M^-5`; two odd controls have exact remainder `<M^-3`. Signs agree in every control.

5. **Near-front sign attack.** For `s=131/1000, tau=1/5`, exact even controls cross from positive to negative between scaled phase drifts on opposite sides of the predicted critical drift. Floating `eta` diagnostics are not used to decide the exact finite signs.

6. **Intrinsic-coefficient sign attack.** The conjecture `Omega_p(xi_p)` has a fixed nonzero sign is refuted. An exact rational log-interval calculation proves negative sign at `(s,tau)=(129/1000,131/1000)` and positive sign at `(129/1000,132/1000)` for even parity. Continuity gives an interior zero.

7. **Exact-log attack.** The double-critical certificate uses the identity `log x = 2 atanh((x-1)/(x+1))` with an exact rational geometric tail bound. Float output is diagnostic only.

8. **Overreach attack.** Existence of an intrinsic double-critical target is not converted into a claim that the discrete rounding sequence actually realizes exact resonance. That remains Diophantine and open.

9. **Collision attack.** The proof assumes a fixed interior pair. It is not applied to `tau-s=O(1/M)`.

## Result

No contradiction was found in the polynomial-core theorem or the near-resonant scaling law. The naive idea of a universally signed intrinsic resonant coefficient is refuted.
