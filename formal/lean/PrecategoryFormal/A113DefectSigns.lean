import PrecategoryFormal.A113DefectEnvelopes
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113: parity-specific defect envelopes

Every premise of the two real-algebra lemmas is discharged below
from the previously kernel-checked dyadic and high-power estimates.
No finite sampling and no assumption of the desired defect sign.
-/

private theorem evenAlgebraBound
    (h u d r p q : ℝ)
    (hu : 0 < u) (hd : 3 / 4 ≤ d)
    (hr0 : 0 ≤ r) (hr : r ≤ 1 / 6)
    (hh : 1 ≤ h) (hratio : h * u / d ≤ 1 / 3)
    (hp0 : 0 ≤ p) (hp : p ≤ u / 128)
    (hq0 : 0 ≤ q) (hq : q ≤ u / 768) :
    |(-2 : ℝ) * u * r / d +
       (1 + 2 * h * u / d) * p -
       2 * (h - 1) * u * q / d| < u / 2 := by
  have hdpos : 0 < d := by linarith
  have hrbound : 2 * r / d ≤ 4 / 9 := by
    apply (div_le_iff₀ hdpos).2
    nlinarith
  have hrest : (h - 1) * u / d ≤ 1 / 3 := by
    have hupos : 0 ≤ u / d := by positivity
    have heq : (h - 1) * u / d = h * u / d - u / d := by ring
    rw [heq]
    linarith
  let a := 2 * u * r / d
  let b := (1 + 2 * h * u / d) * p
  let c := 2 * (h - 1) * u * q / d
  have ha0 : 0 ≤ a := by dsimp [a]; positivity
  have hb0 : 0 ≤ b := by
    dsimp [b]
    have hc0 : 0 ≤ h * u / d := by positivity
    positivity
  have hc0 : 0 ≤ c := by
    dsimp [c]
    have hh0 : 0 ≤ h - 1 := by linarith
    positivity
  have ha : a ≤ (4 / 9 : ℝ) * u := by
    dsimp [a]
    calc
      2 * u * r / d = u * (2 * r / d) := by ring
      _ ≤ u * (4 / 9 : ℝ) :=
        mul_le_mul_of_nonneg_left hrbound (le_of_lt hu)
      _ = (4 / 9 : ℝ) * u := by ring
  have hb : b ≤ (5 / 384 : ℝ) * u := by
    dsimp [b]
    have hcoef : 1 + 2 * h * u / d ≤ 5 / 3 := by
      calc
        1 + 2 * h * u / d = 1 + 2 * (h * u / d) := by ring
        _ ≤ 5 / 3 := by linarith
    calc
      (1 + 2 * h * u / d) * p ≤ (5 / 3 : ℝ) * p :=
        mul_le_mul_of_nonneg_right hcoef hp0
      _ ≤ (5 / 3 : ℝ) * (u / 128) :=
        mul_le_mul_of_nonneg_left hp (by norm_num)
      _ = (5 / 384 : ℝ) * u := by ring
  have hc : c ≤ (1 / 1152 : ℝ) * u := by
    dsimp [c]
    have hcoef : 2 * (h - 1) * u / d ≤ 2 / 3 := by
      calc
        2 * (h - 1) * u / d = 2 * ((h - 1) * u / d) := by ring
        _ ≤ 2 / 3 := by linarith
    calc
      2 * (h - 1) * u * q / d = (2 * (h - 1) * u / d) * q := by ring
      _ ≤ (2 / 3 : ℝ) * q :=
        mul_le_mul_of_nonneg_right hcoef hq0
      _ ≤ (2 / 3 : ℝ) * (u / 768) :=
        mul_le_mul_of_nonneg_left hq (by norm_num)
      _ = (1 / 1152 : ℝ) * u := by ring
  have hbound : |-a + b - c| < u / 2 := by
    apply abs_lt.mpr
    constructor <;> nlinarith [ha0, hb0, hc0, ha, hb, hc]
  have hform : (-2 : ℝ) * u * r / d +
      (1 + 2 * h * u / d) * p -
      2 * (h - 1) * u * q / d = -a + b - c := by
    dsimp [a, b, c]
    ring
  rw [hform]
  exact hbound

private theorem oddAlgebraBound
    (h u d r p q : ℝ)
    (hu : 0 < u) (hd : 3 / 4 ≤ d)
    (hr0 : 0 ≤ r) (hr : r ≤ 1 / 6)
    (hh : 1 ≤ h) (hratio : h * u / d ≤ 1 / 3)
    (hp0 : 0 ≤ p) (hp : p ≤ u / 128)
    (hq0 : 0 ≤ q) (hq : q ≤ u / 768) :
    |(-(3 / 2 : ℝ)) * u * r / d +
       (1 / 2 + (3 / 2 : ℝ) * h * u / d) * p +
       (1 / 2 - (3 / 2 : ℝ) * (h - 1) * u / d) * q| < u / 2 := by
  have hdpos : 0 < d := by linarith
  have hrbound : (3 / 2 : ℝ) * r / d ≤ 1 / 3 := by
    apply (div_le_iff₀ hdpos).2
    nlinarith
  have hrest : (h - 1) * u / d ≤ 1 / 3 := by
    have hupos : 0 ≤ u / d := by positivity
    have heq : (h - 1) * u / d = h * u / d - u / d := by ring
    rw [heq]
    linarith
  have hrest0 : 0 ≤ (h - 1) * u / d := by
    have hh0 : 0 ≤ h - 1 := by linarith
    positivity
  let a := (3 / 2 : ℝ) * u * r / d
  let b := (1 / 2 + (3 / 2 : ℝ) * h * u / d) * p
  let c := (1 / 2 - (3 / 2 : ℝ) * (h - 1) * u / d) * q
  have ha0 : 0 ≤ a := by dsimp [a]; positivity
  have hb0 : 0 ≤ b := by
    dsimp [b]
    have hc0 : 0 ≤ h * u / d := by positivity
    positivity
  have hc0 : 0 ≤ c := by
    dsimp [c]
    have hcoef : 0 ≤ (1 / 2 : ℝ) - (3 / 2) * (h - 1) * u / d := by
      have heq : (3 / 2 : ℝ) * (h - 1) * u / d =
          (3 / 2) * ((h - 1) * u / d) := by ring
      rw [heq]
      linarith
    positivity
  have ha : a ≤ u / 3 := by
    dsimp [a]
    calc
      (3 / 2 : ℝ) * u * r / d = u * ((3 / 2 : ℝ) * r / d) := by ring
      _ ≤ u * (1 / 3 : ℝ) :=
        mul_le_mul_of_nonneg_left hrbound (le_of_lt hu)
      _ = u / 3 := by ring
  have hb : b ≤ u / 128 := by
    dsimp [b]
    have hcoef : (1 / 2 : ℝ) + (3 / 2) * h * u / d ≤ 1 := by
      have heq : (3 / 2 : ℝ) * h * u / d =
          (3 / 2) * (h * u / d) := by ring
      rw [heq]
      linarith
    have hcoef0 : 0 ≤ (1 / 2 : ℝ) + (3 / 2) * h * u / d := by
      have hc0 : 0 ≤ h * u / d := by positivity
      positivity
    calc
      ((1 / 2 : ℝ) + (3 / 2) * h * u / d) * p ≤ 1 * p :=
        mul_le_mul_of_nonneg_right hcoef hp0
      _ = p := one_mul _
      _ ≤ u / 128 := hp
  have hc : c ≤ u / 1536 := by
    dsimp [c]
    have hcoef : (1 / 2 : ℝ) - (3 / 2) * (h - 1) * u / d ≤ 1 / 2 := by
      have heq : (3 / 2 : ℝ) * (h - 1) * u / d =
          (3 / 2) * ((h - 1) * u / d) := by ring
      rw [heq]
      linarith
    calc
      ((1 / 2 : ℝ) - (3 / 2) * (h - 1) * u / d) * q
          ≤ (1 / 2 : ℝ) * q :=
        mul_le_mul_of_nonneg_right hcoef hq0
      _ ≤ (1 / 2 : ℝ) * (u / 768) :=
        mul_le_mul_of_nonneg_left hq (by norm_num)
      _ = u / 1536 := by ring
  have hbound : |-a + b + c| < u / 2 := by
    apply abs_lt.mpr
    constructor <;> nlinarith [ha0, hb0, hc0, ha, hb, hc]
  have hform : (-(3 / 2 : ℝ)) * u * r / d +
      (1 / 2 + (3 / 2 : ℝ) * h * u / d) * p +
      (1 / 2 - (3 / 2 : ℝ) * (h - 1) * u / d) * q = -a + b + c := by
    dsimp [a, b, c]
    ring
  rw [hform]
  exact hbound

/-- Exact even-parity A84 defect bound for every admissible real node. -/
theorem a113EvenDefect_abs_lt_half (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node) (hnode : node ≤ 1 / 6) :
    |a113EvenDefect size node| < a113Unit size / 2 := by
  have hh : (1 : ℝ) ≤ (a113HalfIndex size : ℝ) := by
    have hnat : 1 ≤ a113HalfIndex size := by
      unfold a113HalfIndex
      omega
    exact_mod_cast hnat
  have h := evenAlgebraBound
    (a113HalfIndex size : ℝ) (a113Unit size)
    (a113Denominator size) node
    (node ^ a113HalfIndex size)
    (node ^ (a113HalfIndex size + 1))
    (a113Unit_pos size)
    (a113Denominator_ge_three_quarters size hsize)
    hnode0 hnode hh
    (a113HalfCoefficient_div_denominator_le_third size hsize)
    (pow_nonneg hnode0 _)
    (a113NodePower_le_unit_div_128 size node hsize hnode0 hnode)
    (pow_nonneg hnode0 _)
    (a113NodeNextPower_le_unit_div_768 size node hsize hnode0 hnode)
  simpa only [a113EvenDefect] using h

/-- Exact odd-parity A84 defect bound for every admissible real node. -/
theorem a113OddDefect_abs_lt_half (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node) (hnode : node ≤ 1 / 6) :
    |a113OddDefect size node| < a113Unit size / 2 := by
  have hh : (1 : ℝ) ≤ (a113HalfIndex size : ℝ) := by
    have hnat : 1 ≤ a113HalfIndex size := by
      unfold a113HalfIndex
      omega
    exact_mod_cast hnat
  have h := oddAlgebraBound
    (a113HalfIndex size : ℝ) (a113Unit size)
    (a113Denominator size) node
    (node ^ a113HalfIndex size)
    (node ^ (a113HalfIndex size + 1))
    (a113Unit_pos size)
    (a113Denominator_ge_three_quarters size hsize)
    hnode0 hnode hh
    (a113HalfCoefficient_div_denominator_le_third size hsize)
    (pow_nonneg hnode0 _)
    (a113NodePower_le_unit_div_128 size node hsize hnode0 hnode)
    (pow_nonneg hnode0 _)
    (a113NodeNextPower_le_unit_div_768 size node hsize hnode0 hnode)
  simpa only [a113OddDefect] using h

/-- Uniform A113 defect estimate, including both size parities. -/
theorem a113Defect_abs_lt_half (size : ℕ) (node : ℝ)
    (hsize : 521 ≤ size)
    (hnode0 : 0 ≤ node) (hnode : node ≤ 1 / 6) :
    |a113Defect size node| < a113Unit size / 2 := by
  by_cases heven : size % 2 = 0
  · rw [a113Defect_even size node heven]
    exact a113EvenDefect_abs_lt_half size node hsize hnode0 hnode
  · rw [a113Defect_odd size node heven]
    exact a113OddDefect_abs_lt_half size node hsize hnode0 hnode

end PrecategoryFormal
