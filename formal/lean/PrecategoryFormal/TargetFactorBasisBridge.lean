import PrecategoryFormal.TargetDeformationAudit
import PrecategoryFormal.TargetFactorTenChannel

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.TargetFactor

/--
The finite-support moment-adjusted basis used in the original A115
Python audit, with genuine natural exponents and a positive size M.
-/
noncomputable def finiteBasis (M k : ℕ) (r : ℝ) : ℝ :=
  r ^ k - ((M : ℝ) - (k : ℝ)) / (M : ℝ) -
    ((k : ℝ) / (M : ℝ)) * r ^ M

/--
The finite basis is exactly one exponential channel plus a constant
and a linear-in-k channel.
-/
theorem finiteBasis_channel (M k : ℕ) (r : ℝ) (hM : M ≠ 0) :
    finiteBasis M k r =
      r ^ k - 1 + (k : ℝ) * ((1 - r ^ M) / (M : ℝ)) := by
  have hMR : (M : ℝ) ≠ 0 := by exact_mod_cast hM
  unfold finiteBasis
  field_simp [hMR]
  ring

/--
The adjacent finite-basis difference is the confluent exponential
channel used in the cofactor identity.
-/
theorem finiteBasis_difference_channel (M k : ℕ) (r : ℝ) (hM : M ≠ 0) :
    finiteBasis M (k + 1) r - finiteBasis M k r =
      (r - 1) * r ^ k + (1 - r ^ M) / (M : ℝ) := by
  calc
    finiteBasis M (k + 1) r - finiteBasis M k r =
        r ^ (k + 1) - r ^ k + (1 - r ^ M) / (M : ℝ) := by
          simpa only [finiteBasis] using
            (PrecategoryFormal.TargetDeformation.exponential_basis_difference_nat
              M k r hM)
    _ = (r - 1) * r ^ k + (1 - r ^ M) / (M : ℝ) := by
      rw [pow_succ]
      ring

end PrecategoryFormal.TargetFactor
