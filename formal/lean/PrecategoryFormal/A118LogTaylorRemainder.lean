import Mathlib

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 1000000

namespace PrecategoryFormal.A118LogTaylorRemainder

/--
A genuine real-analytic cubic logarithm enclosure, directly derived
from Mathlib's absolute log series remainder theorem at -z.

Unlike the unformalized tighter alternating-series constant z^4/4,
this rigorously established bound uses z^4/(1-z). All real z in
the frozen collision range 0<=z<=9/100 are included.
-/
theorem log_one_add_cubic_remainder
    (z : ℝ) (hz0 : 0 ≤ z) (hzmax : z ≤ 9/100) :
    |Real.log (1+z)-(z-z^2/2+z^3/3)| ≤
      z^4/(1-z) := by
  have habs : |(-z)| < 1 := by
    rw [abs_neg, abs_of_nonneg hz0]
    linarith
  have h := Real.abs_log_sub_add_sum_range_le (x := -z) habs 3
  have hsum :
      (∑ i ∈ Finset.range 3,
        (-z)^(i+1)/((i:ℝ)+1)) =
        -z+z^2/2-z^3/3 := by
    simp [Finset.sum_range_succ]
    ring
  have hleft :
      (∑ i ∈ Finset.range 3,
        (-z)^(i+1)/((i:ℝ)+1))+
        Real.log (1-(-z)) =
      Real.log (1+z)-(z-z^2/2+z^3/3) := by
    rw [hsum]
    ring
  have hright :
      |(-z)|^(3+1)/(1-|(-z)|) = z^4/(1-z) := by
    rw [abs_neg, abs_of_nonneg hz0]
    norm_num
  rw [hleft, hright] at h
  exact h

end PrecategoryFormal.A118LogTaylorRemainder
