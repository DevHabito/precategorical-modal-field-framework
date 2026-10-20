import PrecategoryFormal.A113IdealCoreUniform
import Mathlib

set_option autoImplicit false
set_option warningAsError true
set_option exponentiation.threshold 512

namespace PrecategoryFormal

/-!
# A113: the actual parity-dependent moment channels

The finite-M definitions below retain the parity split and the
opposite beta/source epsilon adjustments from the historical A84
cofactor reconstruction. They are not asymptotic replacements.

This module proves the dyadic unit estimate, the denominator's strict
positivity on the frozen size range, and the exact relationship between
the beta/source channels. It does NOT assert a uniform D or E error
estimate; those are the next outstanding analytical obligations.
-/

/-- The half-index is the integer floor of M/2. -/
def a113HalfIndex (size : ℕ) : ℕ := size / 2

/-- The positive dyadic scale U_M = 2^(-floor(M/2)). -/
noncomputable def a113Unit (size : ℕ) : ℝ :=
  (1 / 2 : ℝ) ^ a113HalfIndex size

/-- The common denominator in both parity branches of D_M. -/
noncomputable def a113Denominator (size : ℕ) : ℝ :=
  1 - ((a113HalfIndex size + 1 : ℕ) : ℝ) * a113Unit size

/--
The frozen even-M formula for D_M(r), written without an assumed
positive denominator.
-/
noncomputable def a113EvenDefect (size : ℕ) (node : ℝ) : ℝ :=
  let h := a113HalfIndex size
  let unit := a113Unit size
  let denominator := a113Denominator size
  (-2 : ℝ) * unit * node / denominator +
    (1 + 2 * (h : ℝ) * unit / denominator) * node ^ h -
    2 * ((h : ℝ) - 1) * unit * node ^ (h + 1) / denominator

/-- The frozen odd-M formula for D_M(r). -/
noncomputable def a113OddDefect (size : ℕ) (node : ℝ) : ℝ :=
  let h := a113HalfIndex size
  let unit := a113Unit size
  let denominator := a113Denominator size
  (-(3 / 2 : ℝ)) * unit * node / denominator +
    (1 / 2 + (3 / 2 : ℝ) * (h : ℝ) * unit / denominator) * node ^ h +
    (1 / 2 - (3 / 2 : ℝ) * ((h : ℝ) - 1) * unit / denominator) *
      node ^ (h + 1)

/-- The actual A84 defect selects the branch using integer parity. -/
noncomputable def a113Defect (size : ℕ) (node : ℝ) : ℝ :=
  if size % 2 = 0 then a113EvenDefect size node
  else a113OddDefect size node

/-- The historical parity-specific tolerance epsilon_M. -/
noncomputable def a113Epsilon (size : ℕ) : ℝ :=
  if size % 2 = 0 then a113Unit size / 1875
  else a113Unit size / 2500

/--
The beta channel has +2 epsilon; the source channel has -2 epsilon.
These are deliberately different functions at equal node values.
-/
noncomputable def a113H (size : ℕ) (node : ℝ)
    (betaChannel : Bool) : ℝ :=
  (1 + node ^ size) / 2 - a113Defect size node +
    (if betaChannel then 2 * a113Epsilon size
     else -2 * a113Epsilon size)

/-- A83 target normalization at finite M. -/
noncomputable def a113TargetMass (size : ℕ) : ℝ :=
  (1 + (1 / 2 : ℝ) ^ size) / 2

/-- Finite-size moment slope a_M(r). -/
noncomputable def a113MomentSlope (size : ℕ) (node : ℝ) : ℝ :=
  (1 - node ^ size) / size

/--
The exact A83 adjacent factor, not the idealized zero-U core.
The H-values have the historically specified opposite adjustments.
-/
noncomputable def a113ActualFactor
    (size k : ℕ) (source : ℝ) : ℝ :=
  contactAdjacentFactor k (1 / 8) (1 / 2) source
    (a113TargetMass size)
    (a113H size (1 / 8) true)
    (a113H size source false)
    (a113MomentSlope size (1 / 8))
    (a113MomentSlope size (1 / 2))
    (a113MomentSlope size source)

/-- Both parity branches share the same strictly positive unit. -/
theorem a113Unit_pos (size : ℕ) : 0 < a113Unit size := by
  unfold a113Unit
  positivity

private theorem a113HalfIndex_ge_260 (size : ℕ)
    (hsize : 521 ≤ size) : 260 ≤ a113HalfIndex size := by
  unfold a113HalfIndex
  omega

private theorem a113HalfIndex_ge_5 (size : ℕ)
    (hsize : 521 ≤ size) : 5 ≤ a113HalfIndex size := by
  have h := a113HalfIndex_ge_260 size hsize
  omega

/-- Powers of one half are bounded above by one. -/
private theorem a113HalfPower_le_one (n : ℕ) :
    (1 / 2 : ℝ) ^ n ≤ 1 := by
  induction n with
  | zero => norm_num
  | succ n ih =>
      calc
        (1 / 2 : ℝ) ^ (n + 1) =
            (1 / 2 : ℝ) ^ n * (1 / 2 : ℝ) := pow_succ _ _
        _ ≤ (1 / 2 : ℝ) ^ n * 1 :=
          mul_le_mul_of_nonneg_left (by norm_num) (by positivity)
        _ = (1 / 2 : ℝ) ^ n := by ring
        _ ≤ 1 := ih

/--
Dyadic scale bound for all integer M≥521, not just sampled sizes.
No real-valued approximation of 2^260 is used.
-/
theorem a113Unit_le_boundary (size : ℕ)
    (hsize : 521 ≤ size) :
    a113Unit size ≤ (1 / 2 : ℝ) ^ 260 := by
  have hhalf := a113HalfIndex_ge_260 size hsize
  obtain ⟨offset, hindex⟩ :
      ∃ offset : ℕ, a113HalfIndex size = 260 + offset := by
    refine ⟨a113HalfIndex size - 260, ?_⟩
    omega
  unfold a113Unit
  rw [hindex, pow_add]
  simpa only [mul_one] using
    (mul_le_mul_of_nonneg_left (a113HalfPower_le_one offset)
      (pow_nonneg (by norm_num : (0 : ℝ) ≤ 1 / 2) 260))

/--
A geometric induction bounds the denominator correction:
(h+1)2^(-h) ≤ 1/4 for every h≥5.
-/
private theorem a113DenominatorCorrection_le_quarter :
    ∀ h : ℕ, 5 ≤ h →
      (((h + 1 : ℕ) : ℝ) * (1 / 2 : ℝ) ^ h) ≤ 1 / 4 := by
  intro h hh
  induction h, hh using Nat.le_induction with
  | base =>
      norm_num
  | succ h hh ih =>
      have hcoef :
          (((h + 1 + 1 : ℕ) : ℝ) / 2) ≤
            (((h + 1 : ℕ) : ℝ)) := by
        push_cast
        have hn : 0 ≤ (h : ℝ) := Nat.cast_nonneg _
        linarith
      calc
        (((h + 1 + 1 : ℕ) : ℝ) * (1 / 2 : ℝ) ^ (h + 1)) =
            (((h + 1 + 1 : ℕ) : ℝ) / 2) *
              (1 / 2 : ℝ) ^ h := by rw [pow_succ]; ring
        _ ≤ (((h + 1 : ℕ) : ℝ) * (1 / 2 : ℝ) ^ h) :=
          mul_le_mul_of_nonneg_right hcoef (by positivity)
        _ ≤ 1 / 4 := ih

/--
The historical denominator is safely bounded away from zero for
every integer size in the frozen A113 range.
-/
theorem a113Denominator_ge_three_quarters (size : ℕ)
    (hsize : 521 ≤ size) :
    (3 / 4 : ℝ) ≤ a113Denominator size := by
  have hc := a113DenominatorCorrection_le_quarter
    (a113HalfIndex size) (a113HalfIndex_ge_5 size hsize)
  unfold a113Denominator a113Unit
  linarith

theorem a113Denominator_pos (size : ℕ)
    (hsize : 521 ≤ size) :
    0 < a113Denominator size := by
  have h := a113Denominator_ge_three_quarters size hsize
  linarith

/-- The parity split is selected solely by size mod 2. -/
theorem a113Defect_even (size : ℕ) (node : ℝ)
    (heven : size % 2 = 0) :
    a113Defect size node = a113EvenDefect size node := by
  simp [a113Defect, heven]

theorem a113Defect_odd (size : ℕ) (node : ℝ)
    (hodd : size % 2 ≠ 0) :
    a113Defect size node = a113OddDefect size node := by
  simp [a113Defect, hodd]

theorem a113Epsilon_even (size : ℕ)
    (heven : size % 2 = 0) :
    a113Epsilon size = a113Unit size / 1875 := by
  simp [a113Epsilon, heven]

theorem a113Epsilon_odd (size : ℕ)
    (hodd : size % 2 ≠ 0) :
    a113Epsilon size = a113Unit size / 2500 := by
  simp [a113Epsilon, hodd]

theorem a113Epsilon_pos (size : ℕ) :
    0 < a113Epsilon size := by
  unfold a113Epsilon
  split_ifs <;> have h := a113Unit_pos size <;> positivity

/-- Verify the opposite signs algebraically for arbitrary real r. -/
theorem a113H_channel_difference (size : ℕ) (node : ℝ) :
    a113H size node true - a113H size node false =
      4 * a113Epsilon size := by
  simp only [a113H, Bool.false_eq_true, ite_true, ite_false]
  ring

theorem a113H_beta_expansion (size : ℕ) (node : ℝ) :
    a113H size node true =
      (1 + node ^ size) / 2 - a113Defect size node +
        2 * a113Epsilon size := by
  rfl

theorem a113H_source_expansion (size : ℕ) (node : ℝ) :
    a113H size node false =
      (1 + node ^ size) / 2 - a113Defect size node -
        2 * a113Epsilon size := by
  simp only [a113H, Bool.false_eq_true, ite_false]
  ring

/-- The true finite-M factor satisfies the already checked A83/A84 algebra. -/
theorem a113ActualFactor_eq_tenTerm (size k : ℕ) (source : ℝ) :
    a113ActualFactor size k source =
      contactTenTermFactor k (1 / 8) (1 / 2) source
        (a113TargetMass size)
        (a113H size (1 / 8) true)
        (a113H size source false)
        (a113MomentSlope size (1 / 8))
        (a113MomentSlope size (1 / 2))
        (a113MomentSlope size source) := by
  unfold a113ActualFactor
  exact contactAdjacentFactor_eq_tenTermFactor
    k (1 / 8) (1 / 2) source
    (a113TargetMass size)
    (a113H size (1 / 8) true)
    (a113H size source false)
    (a113MomentSlope size (1 / 8))
    (a113MomentSlope size (1 / 2))
    (a113MomentSlope size source)

/--
The previous ideal-core result now transfers to the actual historical
parity-dependent factor conditional *only* on the finite-M error bound.
The dyadic size bound is supplied by the proved lemma above.
-/
theorem a113ActualFactor_pos_of_uniform_error
    (size k : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hkLower : 2 ≤ k) (hkUpper : k ≤ 29)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ))
    (herror :
      |a113ActualFactor size k source -
        contactIdealCore k (1 / 8) (1 / 2) source| <
        20 * a113Unit size) :
    0 < a113ActualFactor size k source := by
  unfold a113ActualFactor at *
  exact contactA113SmallLeftPositive_of_error_and_unit
    size k source hsize hkLower hkUpper hsLower hsUpper
    (a113TargetMass size)
    (a113H size (1 / 8) true)
    (a113H size source false)
    (a113MomentSlope size (1 / 8))
    (a113MomentSlope size (1 / 2))
    (a113MomentSlope size source)
    (a113Unit size) herror (by
      simpa only [div_pow, one_pow] using a113Unit_le_boundary size hsize)

end PrecategoryFormal
