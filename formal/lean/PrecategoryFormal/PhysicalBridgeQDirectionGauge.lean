import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
For a reciprocal raw edge-score difference qij-qji, independent source-row
offsets can move the difference to any prescribed rational target.

This is the finite algebraic core of the A24 row-gauge obstruction to using
the raw reciprocal q difference as an observable orientation.
-/
theorem reciprocal_q_difference_row_gauge_hits_any_target
    (qij qji target : ℚ) :
    ∃ ci cj : ℚ,
      (qij + ci) - (qji + cj) = target := by
  refine ⟨target - (qij - qji), 0, ?_⟩
  ring

/--
In particular, any positive reciprocal q difference can be gauge-shifted to
a negative one while preserving all observables of a model that is invariant
under independent source-row offsets.
-/
theorem positive_reciprocal_q_difference_can_flip_sign
    (qij qji : ℚ)
    (h : 0 < qij - qji) :
    ∃ ci cj : ℚ,
      (qij + ci) - (qji + cj) < 0 := by
  obtain ⟨ci, cj, htarget⟩ :=
    reciprocal_q_difference_row_gauge_hits_any_target qij qji (-1)
  refine ⟨ci, cj, ?_⟩
  rw [htarget]
  norm_num

end PrecategoryFormal.PhysicalBridge
