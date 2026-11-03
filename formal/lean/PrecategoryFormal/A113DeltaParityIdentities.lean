import PrecategoryFormal.A113DeltaScalarBudgets
import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-!
# A113 Delta: exact normalized parity identities

This file connects the original finite-M H channels to the scalar
even/odd expressions used in the error-budget proof. No sign is assumed.
-/

/-- The actual source-minus-beta channel gap normalized by U_M. -/
noncomputable def a113Delta (size : ℕ) (source : ℝ) : ℝ :=
  (a113H size source false - a113H size (1 / 8) true) /
    a113Unit size

/-- The normalized full-size source/beta power term, divided by two. -/
noncomputable def a113DeltaP (size : ℕ) (source : ℝ) : ℝ :=
  ((source ^ size - (1 / 8 : ℝ) ^ size) / a113Unit size) / 2

/-- The normalized source/beta half-index power difference. -/
noncomputable def a113DeltaQ (size : ℕ) (source : ℝ) : ℝ :=
  (source ^ a113HalfIndex size -
    (1 / 8 : ℝ) ^ a113HalfIndex size) / a113Unit size

/-- The normalized source/beta next-half-index power difference. -/
noncomputable def a113DeltaR (size : ℕ) (source : ℝ) : ℝ :=
  (source ^ (a113HalfIndex size + 1) -
    (1 / 8 : ℝ) ^ (a113HalfIndex size + 1)) /
    a113Unit size

/-- The half-index correction normalized by the common denominator. -/
noncomputable def a113DeltaX (size : ℕ) : ℝ :=
  (a113HalfIndex size : ℝ) * a113Unit size /
    a113Denominator size

/-- The previous half-index correction, used with next-power terms. -/
noncomputable def a113DeltaY (size : ℕ) : ℝ :=
  ((a113HalfIndex size : ℝ) - 1) * a113Unit size /
    a113Denominator size

/-- Exact even-M Delta identity for all real sources. -/
theorem a113Delta_even_formula (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size) (heven : size % 2 = 0) :
    a113Delta size source =
      2 * (source - 1 / 8) / a113Denominator size -
        4 / 1875 + a113DeltaP size source -
        (1 + 2 * a113DeltaX size) * a113DeltaQ size source +
        2 * a113DeltaY size * a113DeltaR size source := by
  unfold a113Delta a113DeltaP a113DeltaQ a113DeltaR
    a113DeltaX a113DeltaY
  rw [a113H_sourceBeta_gap_exact size source,
    a113Defect_even size source heven,
    a113Defect_even size (1 / 8) heven,
    a113Epsilon_even size heven]
  unfold a113EvenDefect
  dsimp
  have hu : a113Unit size ≠ 0 := ne_of_gt (a113Unit_pos size)
  have hd : a113Denominator size ≠ 0 :=
    ne_of_gt (a113Denominator_pos size hsize)
  field_simp [hu, hd]
  ring

/-- Exact odd-M Delta identity for all real sources. -/
theorem a113Delta_odd_formula (size : ℕ) (source : ℝ)
    (hsize : 521 ≤ size) (hodd : size % 2 ≠ 0) :
    a113Delta size source =
      (3 / 2) * (source - 1 / 8) / a113Denominator size -
        4 / 2500 + a113DeltaP size source -
        (1 / 2 + (3 / 2) * a113DeltaX size) *
          a113DeltaQ size source -
        (1 / 2 - (3 / 2) * a113DeltaY size) *
          a113DeltaR size source := by
  unfold a113Delta a113DeltaP a113DeltaQ a113DeltaR
    a113DeltaX a113DeltaY
  rw [a113H_sourceBeta_gap_exact size source,
    a113Defect_odd size source hodd,
    a113Defect_odd size (1 / 8) hodd,
    a113Epsilon_odd size hodd]
  unfold a113OddDefect
  dsimp
  have hu : a113Unit size ≠ 0 := ne_of_gt (a113Unit_pos size)
  have hd : a113Denominator size ≠ 0 :=
    ne_of_gt (a113Denominator_pos size hsize)
  field_simp [hu, hd]
  ring

end PrecategoryFormal
