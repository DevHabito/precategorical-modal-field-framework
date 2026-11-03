import PrecategoryFormal.A113DeltaPowerGaps
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113: exact scalar intervals for the even/odd Delta remainder budgets

These theorems state explicit algebraic implications from separately named
premises. They do not assume the result as a hypothesis, and they are not
yet a proof that the actual finite-M Delta satisfies every premise.
-/

/-- The even-parity scalar expression stays inside the frozen interval. -/
theorem a113EvenDeltaScalarInterval
    (source denominator p q r x y : ℝ)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ))
    (hdLower : (999 / 1000 : ℝ) ≤ denominator)
    (hdUpper : denominator ≤ 1)
    (hp0 : 0 ≤ p) (hpUpper : p ≤ 1 / 2000000)
    (hq0 : 0 ≤ q) (hqUpper : q ≤ 1 / 1000000)
    (hr0 : 0 ≤ r) (hrUpper : r ≤ 1 / 1000000)
    (hx0 : 0 ≤ x) (hxUpper : x ≤ 1 / 3)
    (hy0 : 0 ≤ y) (hyUpper : y ≤ 1 / 3) :
    (43 / 10000 : ℝ) <
      2 * (source - 1 / 8) / denominator - 4 / 1875 +
        p - (1 + 2 * x) * q + 2 * y * r ∧
      2 * (source - 1 / 8) / denominator - 4 / 1875 +
        p - (1 + 2 * x) * q + 2 * y * r < (7 / 500 : ℝ) := by
  have hdPos : 0 < denominator := by linarith
  have hleadingLower :
      (8 / 1000 : ℝ) ≤
        2 * (source - 1 / 8) / denominator := by
    apply (le_div_iff₀ hdPos).2
    linarith
  have hleadingUpper :
      2 * (source - 1 / 8) / denominator ≤
        (16 / 1000 : ℝ) / (999 / 1000) := by
    apply (div_le_iff₀ hdPos).2
    linarith
  have hqBound :
      (1 + 2 * x) * q ≤ (5 / 3 : ℝ) / 1000000 := by
    have hfactor : 1 + 2 * x ≤ (5 / 3 : ℝ) := by linarith
    calc
      (1 + 2 * x) * q ≤ (5 / 3 : ℝ) * q :=
        mul_le_mul_of_nonneg_right hfactor hq0
      _ ≤ (5 / 3 : ℝ) * (1 / 1000000 : ℝ) :=
        mul_le_mul_of_nonneg_left hqUpper (by norm_num)
      _ = (5 / 3 : ℝ) / 1000000 := by ring
  have hqNonnegative : 0 ≤ (1 + 2 * x) * q :=
    mul_nonneg (by linarith) hq0
  have hrBound : 2 * y * r ≤ (2 / 3 : ℝ) / 1000000 := by
    calc
      2 * y * r = (2 * y) * r := by ring
      _ ≤ (2 / 3 : ℝ) * r :=
        mul_le_mul_of_nonneg_right (by linarith) hr0
      _ ≤ (2 / 3 : ℝ) * (1 / 1000000 : ℝ) :=
        mul_le_mul_of_nonneg_left hrUpper (by norm_num)
      _ = (2 / 3 : ℝ) / 1000000 := by ring
  have hrNonnegative : 0 ≤ 2 * y * r := by positivity
  constructor
  · nlinarith [hleadingLower, hp0, hqBound, hrNonnegative]
  · nlinarith [hleadingUpper, hpUpper, hqNonnegative, hrBound]

/-- The odd-parity scalar expression has the narrower lower margin. -/
theorem a113OddDeltaScalarInterval
    (source denominator p q r x y : ℝ)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ))
    (hdLower : (999 / 1000 : ℝ) ≤ denominator)
    (hdUpper : denominator ≤ 1)
    (hp0 : 0 ≤ p) (hpUpper : p ≤ 1 / 2000000)
    (hq0 : 0 ≤ q) (hqUpper : q ≤ 1 / 1000000)
    (hr0 : 0 ≤ r) (hrUpper : r ≤ 1 / 1000000)
    (hx0 : 0 ≤ x) (hxUpper : x ≤ 1 / 3)
    (hy0 : 0 ≤ y) (hyUpper : y ≤ 1 / 3) :
    (43 / 10000 : ℝ) <
      (3 / 2) * (source - 1 / 8) / denominator -
        4 / 2500 + p -
        (1 / 2 + (3 / 2) * x) * q -
        (1 / 2 - (3 / 2) * y) * r ∧
      (3 / 2) * (source - 1 / 8) / denominator -
        4 / 2500 + p -
        (1 / 2 + (3 / 2) * x) * q -
        (1 / 2 - (3 / 2) * y) * r < (7 / 500 : ℝ) := by
  have hdPos : 0 < denominator := by linarith
  have hleadingLower :
      (6 / 1000 : ℝ) ≤
        (3 / 2) * (source - 1 / 8) / denominator := by
    apply (le_div_iff₀ hdPos).2
    linarith
  have hleadingUpper :
      (3 / 2) * (source - 1 / 8) / denominator ≤
        (12 / 1000 : ℝ) / (999 / 1000) := by
    apply (div_le_iff₀ hdPos).2
    linarith
  have hcoefQ0 : 0 ≤ (1 / 2 : ℝ) + (3 / 2) * x := by
    linarith
  have hcoefQ1 : (1 / 2 : ℝ) + (3 / 2) * x ≤ 1 := by
    linarith
  have hcoefR0 : 0 ≤ (1 / 2 : ℝ) - (3 / 2) * y := by
    linarith
  have hcoefR1 : (1 / 2 : ℝ) - (3 / 2) * y ≤ 1 / 2 := by
    linarith
  have hqBound :
      (1 / 2 + (3 / 2) * x) * q ≤ (1 / 1000000 : ℝ) := by
    calc
      _ ≤ 1 * q := mul_le_mul_of_nonneg_right hcoefQ1 hq0
      _ = q := by ring
      _ ≤ 1 / 1000000 := hqUpper
  have hrBound :
      (1 / 2 - (3 / 2) * y) * r ≤ (1 / 2000000 : ℝ) := by
    calc
      _ ≤ (1 / 2 : ℝ) * r :=
        mul_le_mul_of_nonneg_right hcoefR1 hr0
      _ ≤ (1 / 2 : ℝ) * (1 / 1000000 : ℝ) :=
        mul_le_mul_of_nonneg_left hrUpper (by norm_num)
      _ = 1 / 2000000 := by ring
  have hqNonnegative : 0 ≤ (1 / 2 + (3 / 2) * x) * q :=
    mul_nonneg hcoefQ0 hq0
  have hrNonnegative : 0 ≤ (1 / 2 - (3 / 2) * y) * r :=
    mul_nonneg hcoefR0 hr0
  constructor
  · nlinarith [hleadingLower, hp0, hqBound, hrBound]
  · nlinarith [hleadingUpper, hpUpper, hqNonnegative, hrNonnegative]

end PrecategoryFormal
