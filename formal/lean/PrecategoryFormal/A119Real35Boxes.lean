import PrecategoryFormal.A119RealCritical
import PrecategoryFormal.A119R4Remaining
import PrecategoryFormal.A119R5Boxes
import PrecategoryFormal.A119R6Boxes
import PrecategoryFormal.A119R7Boxes
import PrecategoryFormal.A119R8R12Boxes
import PrecategoryFormal.A119OddR13R19

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119Real35Boxes

open PrecategoryFormal.A119RealCritical
open PrecategoryFormal.A119RealIntervalCore
open PrecategoryFormal.A119CertifiedExpression

/-!
Each result is a direct real-valued corollary of a separately
kernel-checked rational 35-box Boolean inclusion certificate.
No floating point, native_decide, or positivity assumption is inserted.
This proves the explicit critical rational formula only, not the
A115-A118 source derivation or global F3 optimality.
-/

theorem even_r4_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 4 (0) (1/4)) α) :
    0 < criticalXiHatReal s α false 4 := by
  exact certified_box_sound_real false 4 (0) (1/4) s α hs hα
    PrecategoryFormal.A119R4Remaining.even_r4_left_passes

theorem even_r4_box1 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 4 (1/4) (1/2)) α) :
    0 < criticalXiHatReal s α false 4 := by
  exact certified_box_sound_real false 4 (1/4) (1/2) s α hs hα
    PrecategoryFormal.A119R4Remaining.even_r4_middle_passes

theorem even_r4_box2 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 4 (1/2) (1)) α) :
    0 < criticalXiHatReal s α false 4 := by
  exact certified_box_sound_real false 4 (1/2) (1) s α hs hα
    PrecategoryFormal.A119BoxReplay.even_r4_upper_half_passes

theorem even_r5_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 5 (0) (1/2)) α) :
    0 < criticalXiHatReal s α false 5 := by
  exact certified_box_sound_real false 5 (0) (1/2) s α hs hα
    PrecategoryFormal.A119R5Boxes.even_left

theorem even_r5_box1 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 5 (1/2) (1)) α) :
    0 < criticalXiHatReal s α false 5 := by
  exact certified_box_sound_real false 5 (1/2) (1) s α hs hα
    PrecategoryFormal.A119R5Boxes.even_right

theorem even_r6_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 6 (0) (1/2)) α) :
    0 < criticalXiHatReal s α false 6 := by
  exact certified_box_sound_real false 6 (0) (1/2) s α hs hα
    PrecategoryFormal.A119R6Boxes.even_left

theorem even_r6_box1 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 6 (1/2) (1)) α) :
    0 < criticalXiHatReal s α false 6 := by
  exact certified_box_sound_real false 6 (1/2) (1) s α hs hα
    PrecategoryFormal.A119R6Boxes.even_right

theorem even_r7_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 7 (0) (1/2)) α) :
    0 < criticalXiHatReal s α false 7 := by
  exact certified_box_sound_real false 7 (0) (1/2) s α hs hα
    PrecategoryFormal.A119R7Boxes.even_left

theorem even_r7_box1 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 7 (1/2) (1)) α) :
    0 < criticalXiHatReal s α false 7 := by
  exact certified_box_sound_real false 7 (1/2) (1) s α hs hα
    PrecategoryFormal.A119R7Boxes.even_right

theorem even_r8_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 8 (0) (1)) α) :
    0 < criticalXiHatReal s α false 8 := by
  exact certified_box_sound_real false 8 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.even_r8_passes

theorem even_r9_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 9 (0) (1)) α) :
    0 < criticalXiHatReal s α false 9 := by
  exact certified_box_sound_real false 9 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.even_r9_passes

theorem even_r10_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 10 (0) (1)) α) :
    0 < criticalXiHatReal s α false 10 := by
  exact certified_box_sound_real false 10 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.even_r10_passes

theorem even_r11_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 11 (0) (1)) α) :
    0 < criticalXiHatReal s α false 11 := by
  exact certified_box_sound_real false 11 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.even_r11_passes

theorem even_r12_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox false 12 (0) (1)) α) :
    0 < criticalXiHatReal s α false 12 := by
  exact certified_box_sound_real false 12 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.even_r12_passes

theorem odd_r4_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 4 (0) (1/4)) α) :
    0 < criticalXiHatReal s α true 4 := by
  exact certified_box_sound_real true 4 (0) (1/4) s α hs hα
    PrecategoryFormal.A119R4Remaining.odd_r4_left_passes

theorem odd_r4_box1 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 4 (1/4) (1/2)) α) :
    0 < criticalXiHatReal s α true 4 := by
  exact certified_box_sound_real true 4 (1/4) (1/2) s α hs hα
    PrecategoryFormal.A119R4Remaining.odd_r4_middle_passes

theorem odd_r4_box2 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 4 (1/2) (1)) α) :
    0 < criticalXiHatReal s α true 4 := by
  exact certified_box_sound_real true 4 (1/2) (1) s α hs hα
    PrecategoryFormal.A119BoxReplay.odd_r4_upper_half_passes

theorem odd_r5_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 5 (0) (1/2)) α) :
    0 < criticalXiHatReal s α true 5 := by
  exact certified_box_sound_real true 5 (0) (1/2) s α hs hα
    PrecategoryFormal.A119R5Boxes.odd_left

theorem odd_r5_box1 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 5 (1/2) (1)) α) :
    0 < criticalXiHatReal s α true 5 := by
  exact certified_box_sound_real true 5 (1/2) (1) s α hs hα
    PrecategoryFormal.A119R5Boxes.odd_right

theorem odd_r6_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 6 (0) (1/2)) α) :
    0 < criticalXiHatReal s α true 6 := by
  exact certified_box_sound_real true 6 (0) (1/2) s α hs hα
    PrecategoryFormal.A119R6Boxes.odd_left

theorem odd_r6_box1 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 6 (1/2) (1)) α) :
    0 < criticalXiHatReal s α true 6 := by
  exact certified_box_sound_real true 6 (1/2) (1) s α hs hα
    PrecategoryFormal.A119R6Boxes.odd_right

theorem odd_r7_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 7 (0) (1/2)) α) :
    0 < criticalXiHatReal s α true 7 := by
  exact certified_box_sound_real true 7 (0) (1/2) s α hs hα
    PrecategoryFormal.A119R7Boxes.odd_left

theorem odd_r7_box1 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 7 (1/2) (1)) α) :
    0 < criticalXiHatReal s α true 7 := by
  exact certified_box_sound_real true 7 (1/2) (1) s α hs hα
    PrecategoryFormal.A119R7Boxes.odd_right

theorem odd_r8_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 8 (0) (1)) α) :
    0 < criticalXiHatReal s α true 8 := by
  exact certified_box_sound_real true 8 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.odd_r8_passes

theorem odd_r9_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 9 (0) (1)) α) :
    0 < criticalXiHatReal s α true 9 := by
  exact certified_box_sound_real true 9 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.odd_r9_passes

theorem odd_r10_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 10 (0) (1)) α) :
    0 < criticalXiHatReal s α true 10 := by
  exact certified_box_sound_real true 10 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.odd_r10_passes

theorem odd_r11_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 11 (0) (1)) α) :
    0 < criticalXiHatReal s α true 11 := by
  exact certified_box_sound_real true 11 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.odd_r11_passes

theorem odd_r12_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 12 (0) (1)) α) :
    0 < criticalXiHatReal s α true 12 := by
  exact certified_box_sound_real true 12 (0) (1) s α hs hα
    PrecategoryFormal.A119R8R12Boxes.odd_r12_passes

theorem odd_r13_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 13 (0) (1)) α) :
    0 < criticalXiHatReal s α true 13 := by
  exact certified_box_sound_real true 13 (0) (1) s α hs hα
    PrecategoryFormal.A119OddR13R19.odd_r13_passes

theorem odd_r14_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 14 (0) (1)) α) :
    0 < criticalXiHatReal s α true 14 := by
  exact certified_box_sound_real true 14 (0) (1) s α hs hα
    PrecategoryFormal.A119OddR13R19.odd_r14_passes

theorem odd_r15_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 15 (0) (1)) α) :
    0 < criticalXiHatReal s α true 15 := by
  exact certified_box_sound_real true 15 (0) (1) s α hs hα
    PrecategoryFormal.A119OddR13R19.odd_r15_passes

theorem odd_r16_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 16 (0) (1)) α) :
    0 < criticalXiHatReal s α true 16 := by
  exact certified_box_sound_real true 16 (0) (1) s α hs hα
    PrecategoryFormal.A119OddR13R19.odd_r16_passes

theorem odd_r17_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 17 (0) (1)) α) :
    0 < criticalXiHatReal s α true 17 := by
  exact certified_box_sound_real true 17 (0) (1) s α hs hα
    PrecategoryFormal.A119OddR13R19.odd_r17_passes

theorem odd_r18_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 18 (0) (1)) α) :
    0 < criticalXiHatReal s α true 18 := by
  exact certified_box_sound_real true 18 (0) (1) s α hs hα
    PrecategoryFormal.A119OddR13R19.odd_r18_passes

theorem odd_r19_box0 (s α : ℝ)
    (hs : containsReal sourceBox s)
    (hα : containsReal (alphaBox true 19 (0) (1)) α) :
    0 < criticalXiHatReal s α true 19 := by
  exact certified_box_sound_real true 19 (0) (1) s α hs hα
    PrecategoryFormal.A119OddR13R19.odd_r19_passes

end PrecategoryFormal.A119Real35Boxes
