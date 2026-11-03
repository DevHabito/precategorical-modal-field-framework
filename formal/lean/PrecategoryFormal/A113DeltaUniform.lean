import PrecategoryFormal.A113DeltaParityIdentities
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113 Delta: uniform strict interval from actual finite-M H channels

The proof composes separately checked dyadic, power-gap, scalar and parity
identities. It does not assume any Delta bound in its hypotheses.
The theorem is scoped to the frozen source window, not global A113 signs.
-/

/-- The actual source-minus-beta H gap is strictly inside the frozen interval. -/
theorem a113Delta_uniform_interval
    (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    (43 / 10000 : ℝ) < a113Delta size source ∧
      a113Delta size source < (7 / 500 : ℝ) := by
  have hdenLower := a113Denominator_ge_999_thousand size hsize
  have hdenUpper := a113Denominator_le_one size
  have hfull := a113DeltaFullPowerRatio_bounds
    size source hsize hsLower hsUpper
  have hhalf := a113DeltaHalfPowerRatio_bounds
    size source hsize hsLower hsUpper
  have hnext := a113DeltaNextPowerRatio_bounds
    size source hsize hsLower hsUpper

  have hp0 : 0 ≤ a113DeltaP size source := by
    unfold a113DeltaP
    linarith [hfull.1]
  have hpUpper : a113DeltaP size source ≤ (1 / 2000000 : ℝ) := by
    unfold a113DeltaP
    linarith [hfull.2]
  have hq0 : 0 ≤ a113DeltaQ size source := by
    change 0 ≤
      (source ^ a113HalfIndex size -
        (1 / 8 : ℝ) ^ a113HalfIndex size) / a113Unit size
    exact hhalf.1
  have hqUpper : a113DeltaQ size source ≤ (1 / 1000000 : ℝ) := by
    change
      (source ^ a113HalfIndex size -
        (1 / 8 : ℝ) ^ a113HalfIndex size) / a113Unit size ≤
          1 / 1000000
    exact hhalf.2
  have hr0 : 0 ≤ a113DeltaR size source := by
    change 0 ≤
      (source ^ (a113HalfIndex size + 1) -
        (1 / 8 : ℝ) ^ (a113HalfIndex size + 1)) / a113Unit size
    exact hnext.1
  have hrUpper : a113DeltaR size source ≤ (1 / 1000000 : ℝ) := by
    change
      (source ^ (a113HalfIndex size + 1) -
        (1 / 8 : ℝ) ^ (a113HalfIndex size + 1)) /
        a113Unit size ≤ 1 / 1000000
    exact hnext.2

  have hu : 0 < a113Unit size := a113Unit_pos size
  have hd : 0 < a113Denominator size :=
    a113Denominator_pos size hsize
  have hx0 : 0 ≤ a113DeltaX size := by
    unfold a113DeltaX
    exact div_nonneg
      (mul_nonneg (Nat.cast_nonneg _) (le_of_lt hu))
      (le_of_lt hd)
  have hxUpper : a113DeltaX size ≤ 1 / 3 := by
    unfold a113DeltaX
    exact a113HalfCoefficient_div_denominator_le_third size hsize
  have hhalfReal : (1 : ℝ) ≤ (a113HalfIndex size : ℝ) := by
    have hh : 1 ≤ a113HalfIndex size := by
      unfold a113HalfIndex
      omega
    exact_mod_cast hh
  have hy0 : 0 ≤ a113DeltaY size := by
    unfold a113DeltaY
    exact div_nonneg
      (mul_nonneg (sub_nonneg.mpr hhalfReal) (le_of_lt hu))
      (le_of_lt hd)
  have hyUpper : a113DeltaY size ≤ 1 / 3 := by
    have hrelation :
        a113DeltaY size =
          a113DeltaX size -
            a113Unit size / a113Denominator size := by
      unfold a113DeltaY a113DeltaX
      ring
    rw [hrelation]
    have hpositive : 0 ≤ a113Unit size / a113Denominator size :=
      div_nonneg (le_of_lt hu) (le_of_lt hd)
    linarith [hxUpper]

  by_cases heven : size % 2 = 0
  · rw [a113Delta_even_formula size source hsize heven]
    exact a113EvenDeltaScalarInterval
      source (a113Denominator size)
      (a113DeltaP size source) (a113DeltaQ size source)
      (a113DeltaR size source) (a113DeltaX size) (a113DeltaY size)
      hsLower hsUpper hdenLower hdenUpper
      hp0 hpUpper hq0 hqUpper hr0 hrUpper
      hx0 hxUpper hy0 hyUpper
  · rw [a113Delta_odd_formula size source hsize heven]
    exact a113OddDeltaScalarInterval
      source (a113Denominator size)
      (a113DeltaP size source) (a113DeltaQ size source)
      (a113DeltaR size source) (a113DeltaX size) (a113DeltaY size)
      hsLower hsUpper hdenLower hdenUpper
      hp0 hpUpper hq0 hqUpper hr0 hrUpper
      hx0 hxUpper hy0 hyUpper

/-- Direct form without the Delta helper name. -/
theorem a113H_sourceBeta_gap_uniform_interval
    (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size)
    (hsLower : (129 / 1000 : ℝ) ≤ source)
    (hsUpper : source ≤ (133 / 1000 : ℝ)) :
    (43 / 10000 : ℝ) <
      (a113H size source false - a113H size (1 / 8) true) /
        a113Unit size ∧
      (a113H size source false - a113H size (1 / 8) true) /
        a113Unit size < (7 / 500 : ℝ) := by
  simpa only [a113Delta] using
    a113Delta_uniform_interval size source hsize hsLower hsUpper

end PrecategoryFormal
