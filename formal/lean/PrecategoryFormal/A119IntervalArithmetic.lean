import PrecategoryFormal.A119CompactCertificate

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119IntervalArithmetic

/--
A signed rational multiplier of a closed rational interval is enclosed
between the two endpoint products. No assumption that t is positive.
-/
theorem scalar_min_max
    (t c d y : ℚ) (hcy : c ≤ y) (hyd : y ≤ d) :
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

/-- Exact four-corner lower bound, including sign changes. -/
def fourLower (a b c d : ℚ) : ℚ :=
  min (min (a*c) (a*d)) (min (b*c) (b*d))

/-- Exact four-corner upper bound, including sign changes. -/
def fourUpper (a b c d : ℚ) : ℚ :=
  max (max (a*c) (a*d)) (max (b*c) (b*d))

/--
Every product xy of points in closed rational intervals lies between
the minimum and maximum of all four endpoint products. This is the
operation used by the A119 Fraction interval checker, not a
positive-only approximation.
-/
theorem four_corner_mul_enclosure
    (a b c d x y : ℚ)
    (hx : a ≤ x ∧ x ≤ b)
    (hy : c ≤ y ∧ y ≤ d) :
    fourLower a b c d ≤ x*y ∧ x*y ≤ fourUpper a b c d := by
  have ha := scalar_min_max a c d y hy.1 hy.2
  have hb := scalar_min_max b c d y hy.1 hy.2
  have hlo_a : fourLower a b c d ≤ a*y :=
    le_trans (min_le_left _ _) ha.1
  have hlo_b : fourLower a b c d ≤ b*y :=
    le_trans (min_le_right _ _) hb.1
  have hhi_a : a*y ≤ fourUpper a b c d :=
    le_trans ha.2 (le_max_left _ _)
  have hhi_b : b*y ≤ fourUpper a b c d :=
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

/--
Inversion reverses order when the interval is strictly positive.
Both divisions on the right have nonzero denominators.
-/
theorem positive_reciprocal_enclosure
    (c d y : ℚ) (hc : 0 < c)
    (hcy : c ≤ y) (hyd : y ≤ d) :
    (1 : ℚ)/d ≤ 1/y ∧ 1/y ≤ 1/c := by
  have hypos : 0 < y := lt_of_lt_of_le hc hcy
  have hdpos : 0 < d := lt_of_lt_of_le hypos hyd
  constructor
  · apply (div_le_div_iff₀ hdpos hypos).2
    simpa using hyd
  · apply (div_le_div_iff₀ hypos hc).2
    simpa using hcy

/--
Inversion also reverses order on a strictly negative interval.
A denominator crossing zero is expressly excluded.
-/
theorem negative_reciprocal_enclosure
    (c d y : ℚ) (hd : d < 0)
    (hcy : c ≤ y) (hyd : y ≤ d) :
    (1 : ℚ)/d ≤ 1/y ∧ 1/y ≤ 1/c := by
  have h := positive_reciprocal_enclosure
    (-d) (-c) (-y) (by linarith) (by linarith) (by linarith)
  have h₁ : (1 : ℚ)/d ≤ 1/y := by
    have hh := h.2
    simp only [div_neg] at hh
    linarith
  have h₂ : (1 : ℚ)/y ≤ 1/c := by
    have hh := h.1
    simp only [div_neg] at hh
    linarith
  exact ⟨h₁, h₂⟩

/--
Sound division of two signed rational intervals, provided the
denominator is strictly on one side of zero.
This composes the already proved four-corner product bound with the
correct reciprocal enclosure, rather than assuming a numeric answer.
-/
theorem division_enclosure
    (a b c d x y : ℚ)
    (hx : a ≤ x ∧ x ≤ b)
    (hy : c ≤ y ∧ y ≤ d)
    (hsep : 0 < c ∨ d < 0) :
    fourLower a b (1/d) (1/c) ≤ x/y ∧
      x/y ≤ fourUpper a b (1/d) (1/c) := by
  have hinv : (1 : ℚ)/d ≤ 1/y ∧ 1/y ≤ 1/c := by
    rcases hsep with hc | hd
    · exact positive_reciprocal_enclosure c d y hc hy.1 hy.2
    · exact negative_reciprocal_enclosure c d y hd hy.1 hy.2
  have hprod := four_corner_mul_enclosure
    a b (1/d) (1/c) x (1/y) hx hinv
  simpa only [div_eq_mul_inv, one_div, one_mul] using hprod

end PrecategoryFormal.A119IntervalArithmetic
