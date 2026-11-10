import PrecategoryFormal.A119RealManifest

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119RealFullCells

open PrecategoryFormal.A119RealIntervalCore
open PrecategoryFormal.A119CertifiedExpression
open PrecategoryFormal.A119RealCritical
open PrecategoryFormal.A119Real35Boxes
open PrecategoryFormal.A119RealManifest

/-!
Complete rational-endpoint alpha cell coverage over real parameters.
Three/two/one *kernel-verified* box inequalities are composed using
the already proved closed split lemmas; no interval endpoints are
discarded. The subject is the reduced Xi-hat rational expression.
-/

theorem even_r4_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (8:ℝ) ≤ α ∧ α ≤ 21/2) :
    0 < criticalXiHatReal s α false 4 := by
  exact PrecategoryFormal.A119RealManifest.even_r4_entire s α hs hα

theorem even_r5_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (10:ℝ) ≤ α ∧ α ≤ 63/5) :
    0 < criticalXiHatReal s α false 5 := by
  rcases two_closed_cover 10 (63/5) α hα with hl | hr
  · exact even_r5_box0 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hl.1, hl.2])
  · exact even_r5_box1 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hr.1, hr.2])

theorem even_r6_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (12:ℝ) ≤ α ∧ α ≤ 147/10) :
    0 < criticalXiHatReal s α false 6 := by
  rcases two_closed_cover 12 (147/10) α hα with hl | hr
  · exact even_r6_box0 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hl.1, hl.2])
  · exact even_r6_box1 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hr.1, hr.2])

theorem even_r7_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (14:ℝ) ≤ α ∧ α ≤ 84/5) :
    0 < criticalXiHatReal s α false 7 := by
  rcases two_closed_cover 14 (84/5) α hα with hl | hr
  · exact even_r7_box0 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hl.1, hl.2])
  · exact even_r7_box1 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hr.1, hr.2])

theorem even_r8_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (16:ℝ) ≤ α ∧ α ≤ 189/10) :
    0 < criticalXiHatReal s α false 8 := by
  exact PrecategoryFormal.A119RealManifest.even_r8_entire s α hs hα

theorem even_r9_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (18:ℝ) ≤ α ∧ α ≤ 21) :
    0 < criticalXiHatReal s α false 9 := by
  exact even_r9_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem even_r10_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (20:ℝ) ≤ α ∧ α ≤ 231/10) :
    0 < criticalXiHatReal s α false 10 := by
  exact even_r10_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem even_r11_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (22:ℝ) ≤ α ∧ α ≤ 126/5) :
    0 < criticalXiHatReal s α false 11 := by
  exact even_r11_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem even_r12_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (24:ℝ) ≤ α ∧ α ≤ 273/10) :
    0 < criticalXiHatReal s α false 12 := by
  exact even_r12_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r4_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (9:ℝ) ≤ α ∧ α ≤ 231/20) :
    0 < criticalXiHatReal s α true 4 := by
  rcases three_closed_cover 9 (231/20) α hα with hl | hm | hr
  · exact odd_r4_box0 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hl.1, hl.2])
  · exact odd_r4_box1 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hm.1, hm.2])
  · exact odd_r4_box2 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hr.1, hr.2])

theorem odd_r5_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (11:ℝ) ≤ α ∧ α ≤ 273/20) :
    0 < criticalXiHatReal s α true 5 := by
  rcases two_closed_cover 11 (273/20) α hα with hl | hr
  · exact odd_r5_box0 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hl.1, hl.2])
  · exact odd_r5_box1 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hr.1, hr.2])

theorem odd_r6_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (13:ℝ) ≤ α ∧ α ≤ 63/4) :
    0 < criticalXiHatReal s α true 6 := by
  rcases two_closed_cover 13 (63/4) α hα with hl | hr
  · exact odd_r6_box0 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hl.1, hl.2])
  · exact odd_r6_box1 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hr.1, hr.2])

theorem odd_r7_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (15:ℝ) ≤ α ∧ α ≤ 357/20) :
    0 < criticalXiHatReal s α true 7 := by
  rcases two_closed_cover 15 (357/20) α hα with hl | hr
  · exact odd_r7_box0 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hl.1, hl.2])
  · exact odd_r7_box1 s α hs (by
      norm_num [containsReal, alphaBox]
      constructor <;> linarith [hr.1, hr.2])

theorem odd_r8_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (17:ℝ) ≤ α ∧ α ≤ 399/20) :
    0 < criticalXiHatReal s α true 8 := by
  exact odd_r8_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r9_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (19:ℝ) ≤ α ∧ α ≤ 441/20) :
    0 < criticalXiHatReal s α true 9 := by
  exact odd_r9_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r10_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (21:ℝ) ≤ α ∧ α ≤ 483/20) :
    0 < criticalXiHatReal s α true 10 := by
  exact odd_r10_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r11_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (23:ℝ) ≤ α ∧ α ≤ 105/4) :
    0 < criticalXiHatReal s α true 11 := by
  exact odd_r11_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r12_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (25:ℝ) ≤ α ∧ α ≤ 567/20) :
    0 < criticalXiHatReal s α true 12 := by
  exact odd_r12_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r13_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (27:ℝ) ≤ α ∧ α ≤ 609/20) :
    0 < criticalXiHatReal s α true 13 := by
  exact odd_r13_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r14_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (29:ℝ) ≤ α ∧ α ≤ 651/20) :
    0 < criticalXiHatReal s α true 14 := by
  exact odd_r14_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r15_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (31:ℝ) ≤ α ∧ α ≤ 693/20) :
    0 < criticalXiHatReal s α true 15 := by
  exact odd_r15_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r16_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (33:ℝ) ≤ α ∧ α ≤ 147/4) :
    0 < criticalXiHatReal s α true 16 := by
  exact odd_r16_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r17_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (35:ℝ) ≤ α ∧ α ≤ 777/20) :
    0 < criticalXiHatReal s α true 17 := by
  exact odd_r17_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r18_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (37:ℝ) ≤ α ∧ α ≤ 819/20) :
    0 < criticalXiHatReal s α true 18 := by
  exact odd_r18_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

theorem odd_r19_entire (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : (39:ℝ) ≤ α ∧ α ≤ 861/20) :
    0 < criticalXiHatReal s α true 19 := by
  exact odd_r19_box0 s α hs (by
    norm_num [containsReal, alphaBox]
    exact hα)

end PrecategoryFormal.A119RealFullCells
