import PrecategoryFormal.A113DefectSigns
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113: finite-M H-channel uniform envelopes

The historical plus/minus epsilon adjustments are retained verbatim.
Both parity branches are covered by the already checked actual defect
definition, not by a sampled or idealized replacement.
-/

/-- Nodes in [0,1] have all natural powers at most one. -/
private theorem a113NodePow_le_one (node : ℝ)
    (hnode0 : 0 ≤ node) (hnode1 : node ≤ 1) (k : ℕ) :
    node ^ k ≤ 1 := by
  induction k with
  | zero => norm_num
  | succ k ih =>
      calc
        node ^ (k + 1) = node ^ k * node := pow_succ _ _
        _ ≤ node ^ k * 1 :=
          mul_le_mul_of_nonneg_left hnode1 (pow_nonneg hnode0 k)
        _ = node ^ k := mul_one _
        _ ≤ 1 := ih

/--
The full-size power is at most the already certified half-size
envelope. This holds for *every* integer size >= 521.
-/
theorem a113FullPower_le_unit_div_128 (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node) (hnode : node ≤ 1 / 6) :
    node ^ size ≤ a113Unit size / 128 := by
  have hhalf : a113HalfIndex size ≤ size := by
    unfold a113HalfIndex
    omega
  obtain ⟨offset, hindex⟩ :
      ∃ offset : ℕ, size = a113HalfIndex size + offset := by
    refine ⟨size - a113HalfIndex size, ?_⟩
    omega
  have hnode1 : node ≤ 1 := by linarith
  have hpow := a113NodePower_le_unit_div_128
    size node hsize hnode0 hnode
  calc
    node ^ size = node ^ (a113HalfIndex size + offset) :=
      congrArg (fun exponent : ℕ => node ^ exponent) hindex
    _ = node ^ a113HalfIndex size * node ^ offset := pow_add _ _ _
    _ ≤
        node ^ a113HalfIndex size * 1 :=
      mul_le_mul_of_nonneg_left
        (a113NodePow_le_one node hnode0 hnode1 offset)
        (pow_nonneg hnode0 _)
    _ = node ^ a113HalfIndex size := mul_one _
    _ ≤ a113Unit size / 128 := hpow

/--
Uniform tolerance bound preserving the exact even/odd denominators
1875 and 2500. In the odd case, the 1875 cap is conservative.
-/
theorem a113Epsilon_le_unit_div_1875 (size : ℕ) :
    a113Epsilon size ≤ a113Unit size / 1875 := by
  by_cases heven : size % 2 = 0
  · rw [a113Epsilon_even size heven]
  · rw [a113Epsilon_odd size heven]
    have hu : 0 ≤ a113Unit size := le_of_lt (a113Unit_pos size)
    calc
      a113Unit size / 2500 =
          a113Unit size * (1 / 2500 : ℝ) := by ring
      _ ≤ a113Unit size * (1 / 1875 : ℝ) :=
        mul_le_mul_of_nonneg_left (by norm_num) hu
      _ = a113Unit size / 1875 := by ring

/--
A real-algebra estimate for either historical correction sign.
Every quantitative bound is an explicit premise; the callers below
supply each one from proved finite-M formulas.
-/
private theorem a113ChannelAlgebraBound (p defect eps unit : ℝ)
    (hp0 : 0 ≤ p)
    (hp : p ≤ unit / 256)
    (hdefect : |defect| < unit / 2)
    (heps0 : 0 ≤ eps)
    (heps : eps ≤ unit / 1875)
    (hu : 0 < unit)
    (betaChannel : Bool) :
    |p - defect + (if betaChannel then 2 * eps else -2 * eps)| <
      unit := by
  have hdefectLower := (abs_lt.mp hdefect).1
  have hdefectUpper := (abs_lt.mp hdefect).2
  cases betaChannel with
  | false =>
      simp only [Bool.false_eq_true, ite_false]
      apply abs_lt.mpr
      constructor <;> linarith
  | true =>
      simp only [ite_true]
      apply abs_lt.mpr
      constructor <;> linarith

/--
Uniform historical H-channel deviation. The boolean parameter
distinguishes +2epsilon on beta and -2epsilon on source; the
quantified estimate covers both without erasing that difference.
-/
theorem a113H_abs_sub_half_lt_unit (size : ℕ) (node : ℝ)
    (betaChannel : Bool)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node) (hnode : node ≤ 1 / 6) :
    |a113H size node betaChannel - (1 / 2 : ℝ)| <
      a113Unit size := by
  have hfull := a113FullPower_le_unit_div_128
    size node hsize hnode0 hnode
  have hp : node ^ size / 2 ≤ a113Unit size / 256 := by
    linarith
  have hp0 : 0 ≤ node ^ size / 2 := by positivity
  have hdefect := a113Defect_abs_lt_half
    size node hsize hnode0 hnode
  have heps := a113Epsilon_le_unit_div_1875 size
  have heps0 : 0 ≤ a113Epsilon size :=
    le_of_lt (a113Epsilon_pos size)
  have hbound := a113ChannelAlgebraBound
    (node ^ size / 2) (a113Defect size node)
    (a113Epsilon size) (a113Unit size)
    hp0 hp hdefect heps0 heps (a113Unit_pos size)
    betaChannel
  have hexact :
      a113H size node betaChannel - (1 / 2 : ℝ) =
        node ^ size / 2 - a113Defect size node +
          (if betaChannel then 2 * a113Epsilon size
           else -2 * a113Epsilon size) := by
    unfold a113H
    ring
  rw [hexact]
  exact hbound

/-- Original beta H channel with the positive tolerance correction. -/
theorem a113HBeta_abs_sub_half_lt_unit (size : ℕ)
    (hsize : 521 ≤ size) :
    |a113H size (1 / 8) true - (1 / 2 : ℝ)| <
      a113Unit size := by
  apply a113H_abs_sub_half_lt_unit size (1 / 8) true hsize
  · norm_num
  · norm_num

/-- Original source H channel with the negative tolerance correction. -/
theorem a113HSource_abs_sub_half_lt_unit (size : ℕ)
    (source : ℝ) (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    |a113H size source false - (1 / 2 : ℝ)| <
      a113Unit size := by
  apply a113H_abs_sub_half_lt_unit size source false hsize
  · linarith
  · linarith

end PrecategoryFormal
