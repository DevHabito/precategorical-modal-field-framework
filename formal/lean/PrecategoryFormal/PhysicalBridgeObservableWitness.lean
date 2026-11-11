import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
Exact rational surrogate of the mean-nonclosure witness for the published
multi-electron birth-death bridge.

At the diagnostic value exp(-c)=1/2, the two distributions on {0,1,2}
have the same mean, but different values of G_{-c}=E[exp(cN)]. Therefore
the exact mean derivative GammaPlus - D*G_{-c} differs under the same
instantaneous rates.

This theorem is purely algebraic. It does not formalize the experiment.
-/
theorem equal_mean_different_mean_derivative_witness :
    let pA0 : ℚ := 0
    let pA1 : ℚ := 1
    let pA2 : ℚ := 0
    let pB0 : ℚ := 1 / 2
    let pB1 : ℚ := 0
    let pB2 : ℚ := 1 / 2
    let birth : ℚ := 3
    let deathPrefactor : ℚ := 5 / 7
    let meanA := pA1 + 2 * pA2
    let meanB := pB1 + 2 * pB2
    let gMinusA := pA0 + 2 * pA1 + 4 * pA2
    let gMinusB := pB0 + 2 * pB1 + 4 * pB2
    let derivA := birth - deathPrefactor * gMinusA
    let derivB := birth - deathPrefactor * gMinusB
    meanA = 1 ∧
    meanB = 1 ∧
    gMinusA = 2 ∧
    gMinusB = 5 / 2 ∧
    derivA = 11 / 7 ∧
    derivB = 17 / 14 ∧
    derivB - derivA = -(5 / 14) := by
  norm_num

end PrecategoryFormal.PhysicalBridge
