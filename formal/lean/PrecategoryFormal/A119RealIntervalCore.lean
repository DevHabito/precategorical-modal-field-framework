import PrecategoryFormal.A119IntervalEvaluator

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119RealIntervalCore

open PrecategoryFormal.A119IntervalEvaluator
open PrecategoryFormal.A119IntervalArithmetic

/--
The rational endpoints are embedded in the real numbers. No floating-point
number is introduced by this coercion.
-/
def containsReal (i : Interval) (x : ℝ) : Prop :=
  (i.lo : ℝ) ≤ x ∧ x ≤ (i.hi : ℝ)

/-- An ordered real multiplier maps a closed real interval to the endpoints. -/
private theorem real_scalar_min_max
    (t c d y : ℝ) (hcy : c ≤ y) (hyd : y ≤ d) :
    min (t*c) (t*d) ≤ t*y ∧ t*y ≤ max (t*c) (t*d) := by
  by_cases ht : 0 ≤ t
  · have h₁ : t*c ≤ t*y := by
      have h := mul_nonneg ht (sub_nonneg.mpr hcy)
      nlinarith
    have h₂ : t*y ≤ t*d := by
      have h := mul_nonneg ht (sub_nonneg.mpr hyd)
      nlinarith
    exact ⟨le_trans (min_le_left _ _) h₁,
      le_trans h₂ (le_max_right _ _)⟩
  · have htn : t ≤ 0 := le_of_lt (lt_of_not_ge ht)
    have h₁ : t*d ≤ t*y := by
      have h := mul_nonneg (neg_nonneg.mpr htn) (sub_nonneg.mpr hyd)
      nlinarith
    have h₂ : t*y ≤ t*c := by
      have h := mul_nonneg (neg_nonneg.mpr htn) (sub_nonneg.mpr hcy)
      nlinarith
    exact ⟨le_trans (min_le_right _ _) h₁,
      le_trans h₂ (le_max_left _ _)⟩

/-- Four-corner product inclusion holds for arbitrary real inputs. -/
private theorem real_four_corner_mul
    (a b c d x y : ℝ)
    (hx : a ≤ x ∧ x ≤ b)
    (hy : c ≤ y ∧ y ≤ d) :
    min (min (a*c) (a*d)) (min (b*c) (b*d)) ≤ x*y ∧
      x*y ≤ max (max (a*c) (a*d)) (max (b*c) (b*d)) := by
  have ha := real_scalar_min_max a c d y hy.1 hy.2
  have hb := real_scalar_min_max b c d y hy.1 hy.2
  have hlo_a :
      min (min (a*c) (a*d)) (min (b*c) (b*d)) ≤ a*y :=
    le_trans (min_le_left _ _) ha.1
  have hlo_b :
      min (min (a*c) (a*d)) (min (b*c) (b*d)) ≤ b*y :=
    le_trans (min_le_right _ _) hb.1
  have hhi_a :
      a*y ≤ max (max (a*c) (a*d)) (max (b*c) (b*d)) :=
    le_trans ha.2 (le_max_left _ _)
  have hhi_b :
      b*y ≤ max (max (a*c) (a*d)) (max (b*c) (b*d)) :=
    le_trans hb.2 (le_max_right _ _)
  by_cases hypos : 0 ≤ y
  · have h₁ : a*y ≤ x*y := by
      have h := mul_nonneg hypos (sub_nonneg.mpr hx.1)
      nlinarith
    have h₂ : x*y ≤ b*y := by
      have h := mul_nonneg hypos (sub_nonneg.mpr hx.2)
      nlinarith
    exact ⟨le_trans hlo_a h₁, le_trans h₂ hhi_b⟩
  · have hyneg : 0 ≤ -y := neg_nonneg.mpr (le_of_lt (lt_of_not_ge hypos))
    have h₁ : b*y ≤ x*y := by
      have h := mul_nonneg hyneg (sub_nonneg.mpr hx.2)
      nlinarith
    have h₂ : x*y ≤ a*y := by
      have h := mul_nonneg hyneg (sub_nonneg.mpr hx.1)
      nlinarith
    exact ⟨le_trans hlo_b h₁, le_trans h₂ hhi_a⟩

theorem add_real_sound (x y : Interval) (a b : ℝ)
    (ha : containsReal x a) (hb : containsReal y b) :
    containsReal (addI x y) (a+b) := by
  constructor
  · simpa [containsReal, addI] using add_le_add ha.1 hb.1
  · simpa [containsReal, addI] using add_le_add ha.2 hb.2

theorem sub_real_sound (x y : Interval) (a b : ℝ)
    (ha : containsReal x a) (hb : containsReal y b) :
    containsReal (subI x y) (a-b) := by
  constructor
  · simpa [containsReal, subI] using sub_le_sub ha.1 hb.2
  · simpa [containsReal, subI] using sub_le_sub ha.2 hb.1

theorem mul_real_sound (x y : Interval) (a b : ℝ)
    (ha : containsReal x a) (hb : containsReal y b) :
    containsReal (mulI x y) (a*b) := by
  have h := real_four_corner_mul
    (x.lo:ℝ) (x.hi:ℝ) (y.lo:ℝ) (y.hi:ℝ) a b ha hb
  simpa [containsReal, mulI, fourLower, fourUpper] using h

private theorem reciprocal_pos_real
    (c d y : ℝ) (hc : 0<c) (hcy : c≤y) (hyd : y≤d) :
    (1:ℝ)/d ≤ 1/y ∧ 1/y ≤ 1/c := by
  have hy : 0<y := lt_of_lt_of_le hc hcy
  have hd : 0<d := lt_of_lt_of_le hy hyd
  constructor
  · apply (div_le_div_iff₀ hd hy).2
    simpa using hyd
  · apply (div_le_div_iff₀ hy hc).2
    simpa using hcy

private theorem reciprocal_neg_real
    (c d y : ℝ) (hd : d<0) (hcy : c≤y) (hyd : y≤d) :
    (1:ℝ)/d ≤ 1/y ∧ 1/y ≤ 1/c := by
  have h := reciprocal_pos_real
    (-d) (-c) (-y) (by linarith) (by linarith) (by linarith)
  have h₁ : (1:ℝ)/d ≤ 1/y := by
    have hh := h.2
    simp only [div_neg] at hh
    linarith
  have h₂ : (1:ℝ)/y ≤ 1/c := by
    have hh := h.1
    simp only [div_neg] at hh
    linarith
  exact ⟨h₁,h₂⟩

/-- A successful rational interval division bounds arbitrary real inputs. -/
theorem div_real_sound (x y z : Interval) (a b : ℝ)
    (ha : containsReal x a) (hb : containsReal y b)
    (hz : divI? x y = some z) :
    containsReal z (a/b) := by
  unfold divI? at hz
  split at hz
  · rename_i hsep
    cases hz
    have hsepR : 0 < (y.lo:ℝ) ∨ (y.hi:ℝ) < 0 := by
      rcases hsep with h | h
      · exact Or.inl (by exact_mod_cast h)
      · exact Or.inr (by exact_mod_cast h)
    have hinv : (1:ℝ)/(y.hi:ℝ) ≤ 1/b ∧ 1/b ≤ 1/(y.lo:ℝ) := by
      rcases hsepR with h | h
      · exact reciprocal_pos_real (y.lo:ℝ) (y.hi:ℝ) b h hb.1 hb.2
      · exact reciprocal_neg_real (y.lo:ℝ) (y.hi:ℝ) b h hb.1 hb.2
    have h := real_four_corner_mul
      (x.lo:ℝ) (x.hi:ℝ)
      ((1:ℝ)/(y.hi:ℝ)) ((1:ℝ)/(y.lo:ℝ))
      a (1/b) ha hinv
    simpa [containsReal, fourLower, fourUpper, div_eq_mul_inv] using h
  · contradiction

end PrecategoryFormal.A119RealIntervalCore
