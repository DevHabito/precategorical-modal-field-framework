import PrecategoryFormal.A119Real35Boxes

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119RealManifest

open PrecategoryFormal.A119RealIntervalCore
open PrecategoryFormal.A119CertifiedExpression
open PrecategoryFormal.A119RealCritical
open PrecategoryFormal.A119Real35Boxes

/-- Two closed halves cover the entire closed real interval. -/
theorem two_closed_cover (a b x : ℝ)
    (h : a ≤ x ∧ x ≤ b) :
    (a ≤ x ∧ x ≤ (a+b)/2) ∨
    ((a+b)/2 ≤ x ∧ x ≤ b) := by
  by_cases hx : x ≤ (a+b)/2
  · exact Or.inl ⟨h.1, hx⟩
  · exact Or.inr ⟨by linarith, h.2⟩

/-- Three quarter/quarter/half pieces cover the closed real interval. -/
theorem three_closed_cover (a b x : ℝ)
    (h : a ≤ x ∧ x ≤ b) :
    (a ≤ x ∧ x ≤ a+(b-a)/4) ∨
    (a+(b-a)/4 ≤ x ∧ x ≤ (a+b)/2) ∨
    ((a+b)/2 ≤ x ∧ x ≤ b) := by
  by_cases h₁ : x ≤ a+(b-a)/4
  · exact Or.inl ⟨h.1, h₁⟩
  · by_cases h₂ : x ≤ (a+b)/2
    · exact Or.inr (Or.inl ⟨by linarith, h₂⟩)
    · exact Or.inr (Or.inr ⟨by linarith, h.2⟩)

/-- Pilot: the even r=4 cell with all endpoint cases, over reals. -/
theorem even_r4_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (8:ℝ) ≤ α ∧ α ≤ 21/2) :
    0 < criticalXiHatReal s α false 4 := by
  rcases three_closed_cover 8 (21/2) α hα with h | h | h
  · exact even_r4_box0 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [h.1, h.2])
  · exact even_r4_box1 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [h.1, h.2])
  · exact even_r4_box2 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [h.1, h.2])

/-- Pilot: unsplit even r=8 cell, over reals. -/
theorem even_r8_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (16:ℝ) ≤ α ∧ α ≤ 189/10) :
    0 < criticalXiHatReal s α false 8 := by
  exact even_r8_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

end PrecategoryFormal.A119RealManifest
