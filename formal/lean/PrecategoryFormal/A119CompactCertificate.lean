import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal.A119Compact

/--
Number of closed alpha intervals in the frozen A119 compact certificate
for one fixed parity and contact deficit.
The s interval is not subdivided.
-/
def boxCount (r : ℕ) : ℕ :=
  if r = 4 then 3 else if r = 5 ∨ r = 6 ∨ r = 7 then 2 else 1

/-- The published even-parity deficit range contributes 14 boxes. -/
theorem even_box_count :
    (∑ r ∈ Finset.Icc 4 12, boxCount r) = 14 := by
  decide

/-- The published odd-parity deficit range contributes 21 boxes. -/
theorem odd_box_count :
    (∑ r ∈ Finset.Icc 4 19, boxCount r) = 21 := by
  decide

/-- The entire finite manifest contains exactly 35 boxes. -/
theorem total_box_count :
    (∑ r ∈ Finset.Icc 4 12, boxCount r) +
      (∑ r ∈ Finset.Icc 4 19, boxCount r) = 35 := by
  rw [even_box_count, odd_box_count]

/--
Two overlapping closed half-intervals cover their closed parent interval.
This proves the split used at contact deficits 5, 6 and 7, without any
floating-point arithmetic or assumption about a sign expression.
-/
theorem half_split_covers
    (a b x : ℚ) (hax : a ≤ x) (hxb : x ≤ b) :
    (a ≤ x ∧ x ≤ (a + b) / 2) ∨
    ((a + b) / 2 ≤ x ∧ x ≤ b) := by
  by_cases h : x ≤ (a + b) / 2
  · exact Or.inl ⟨hax, h⟩
  · exact Or.inr ⟨by linarith, hxb⟩

/--
The three closed intervals of the r=4 certificate cover their entire
parent interval, including the two shared rational endpoints.
-/
theorem quarter_half_split_covers
    (a b x : ℚ) (hax : a ≤ x) (hxb : x ≤ b) :
    (a ≤ x ∧ x ≤ a + (b - a) / 4) ∨
    (a + (b - a) / 4 ≤ x ∧ x ≤ (a + b) / 2) ∨
    ((a + b) / 2 ≤ x ∧ x ≤ b) := by
  by_cases h₁ : x ≤ a + (b - a) / 4
  · exact Or.inl ⟨hax, h₁⟩
  · by_cases h₂ : x ≤ (a + b) / 2
    · exact Or.inr (Or.inl ⟨by linarith, h₂⟩)
    · exact Or.inr (Or.inr ⟨by linarith, hxb⟩)

/-- Sound interval addition for exact rational endpoints. -/
theorem add_enclosure
    (a b c d x y : ℚ)
    (hx : a ≤ x ∧ x ≤ b)
    (hy : c ≤ y ∧ y ≤ d) :
    a + c ≤ x + y ∧ x + y ≤ b + d := by
  constructor <;> linarith [hx.1, hx.2, hy.1, hy.2]

/-- Sound interval subtraction for exact rational endpoints. -/
theorem sub_enclosure
    (a b c d x y : ℚ)
    (hx : a ≤ x ∧ x ≤ b)
    (hy : c ≤ y ∧ y ≤ d) :
    a - d ≤ x - y ∧ x - y ≤ b - c := by
  constructor <;> linarith [hx.1, hx.2, hy.1, hy.2]

/--
Sound interval multiplication when both lower endpoints are nonnegative.
The full A119 checker has additional signed interval cases not covered here.
-/
theorem nonneg_mul_enclosure
    (a b c d x y : ℚ)
    (ha : 0 ≤ a) (hc : 0 ≤ c)
    (hx : a ≤ x ∧ x ≤ b)
    (hy : c ≤ y ∧ y ≤ d) :
    a * c ≤ x * y ∧ x * y ≤ b * d := by
  have hxn : 0 ≤ x := le_trans ha hx.1
  have hyn : 0 ≤ y := le_trans hc hy.1
  have hbn : 0 ≤ b := le_trans hxn hx.2
  constructor
  · calc
      a * c ≤ x * c := mul_le_mul_of_nonneg_right hx.1 hc
      _ ≤ x * y := mul_le_mul_of_nonneg_left hy.1 hxn
  · calc
      x * y ≤ b * y := mul_le_mul_of_nonneg_right hx.2 hyn
      _ ≤ b * d := mul_le_mul_of_nonneg_left hy.2 hbn

/--
These are the two exact *reported interval lower endpoints* of the
35-box computation. Positivity of these constants is checked here;
we do NOT claim that their origin as lower bounds has been kernel-proved.
-/
theorem reported_lower_endpoints_positive :
    (0 : ℚ) <
      (436152226670319684540420616481093 : ℚ) /
      (4002264870000313289466234723750000 : ℚ) ∧
    (0 : ℚ) <
      (334539706718612647585650758917552506997082603 : ℚ) /
      (1932898972921296034123328117372024031250000000 : ℚ) := by
  constructor <;> norm_num

end PrecategoryFormal.A119Compact
