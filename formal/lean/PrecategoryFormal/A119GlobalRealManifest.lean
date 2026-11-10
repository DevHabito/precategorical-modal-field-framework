import PrecategoryFormal.A119RealFullCells

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119GlobalRealManifest

open PrecategoryFormal.A119RealIntervalCore
open PrecategoryFormal.A119CertifiedExpression
open PrecategoryFormal.A119RealCritical
open PrecategoryFormal.A119RealFullCells

/-!
One universally quantified *finite-contact* theorem over real
source and collision parameters. The finite ranges are exactly the
ones accepted by the A119 35-box certificate. This proof does NOT
derive that these are the only possible A117 critical deficits;
that remains an external analytic lemma.
-/

theorem all_even_cells_real (r : ℕ) (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hr : 4 ≤ r ∧ r ≤ 12)
    (hα : containsReal (alphaBox false r 0 1) α) :
    0 < criticalXiHatReal s α false r := by
  have cases : r = 4 ∨ r = 5 ∨ r = 6 ∨ r = 7 ∨ r = 8 ∨ r = 9 ∨ r = 10 ∨ r = 11 ∨ r = 12 := by omega
  rcases cases with h | h | h | h | h | h | h | h | h
  all_goals subst r
  all_goals norm_num [containsReal, alphaBox] at hα
  all_goals first
    | exact even_r4_entire s α hs hα
    | exact even_r5_entire s α hs hα
    | exact even_r6_entire s α hs hα
    | exact even_r7_entire s α hs hα
    | exact even_r8_entire s α hs hα
    | exact even_r9_entire s α hs hα
    | exact even_r10_entire s α hs hα
    | exact even_r11_entire s α hs hα
    | exact even_r12_entire s α hs hα

theorem all_odd_cells_real (r : ℕ) (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hr : 4 ≤ r ∧ r ≤ 19)
    (hα : containsReal (alphaBox true r 0 1) α) :
    0 < criticalXiHatReal s α true r := by
  have cases : r = 4 ∨ r = 5 ∨ r = 6 ∨ r = 7 ∨ r = 8 ∨ r = 9 ∨ r = 10 ∨ r = 11 ∨ r = 12 ∨ r = 13 ∨ r = 14 ∨ r = 15 ∨ r = 16 ∨ r = 17 ∨ r = 18 ∨ r = 19 := by omega
  rcases cases with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  all_goals subst r
  all_goals norm_num [containsReal, alphaBox] at hα
  all_goals first
    | exact odd_r4_entire s α hs hα
    | exact odd_r5_entire s α hs hα
    | exact odd_r6_entire s α hs hα
    | exact odd_r7_entire s α hs hα
    | exact odd_r8_entire s α hs hα
    | exact odd_r9_entire s α hs hα
    | exact odd_r10_entire s α hs hα
    | exact odd_r11_entire s α hs hα
    | exact odd_r12_entire s α hs hα
    | exact odd_r13_entire s α hs hα
    | exact odd_r14_entire s α hs hα
    | exact odd_r15_entire s α hs hα
    | exact odd_r16_entire s α hs hα
    | exact odd_r17_entire s α hs hα
    | exact odd_r18_entire s α hs hα
    | exact odd_r19_entire s α hs hα

/--
All 25 parity/contact cells at the frozen source window, with
every closed enlarged alpha interval included. This proves positivity
of *the explicit real Xi-hat rational expression* only.
-/
theorem all_critical_candidate_cells_real
    (odd : Bool) (r : ℕ) (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hlegal :
      (odd = false ∧ 4 ≤ r ∧ r ≤ 12) ∨
      (odd = true ∧ 4 ≤ r ∧ r ≤ 19))
    (hα : containsReal (alphaBox odd r 0 1) α) :
    0 < criticalXiHatReal s α odd r := by
  rcases hlegal with ⟨he,hlo,hhi⟩ | ⟨he,hlo,hhi⟩
  · subst odd
    exact all_even_cells_real r s α hs ⟨hlo,hhi⟩ hα
  · subst odd
    exact all_odd_cells_real r s α hs ⟨hlo,hhi⟩ hα

end PrecategoryFormal.A119GlobalRealManifest
