import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
A Z2-equivariant linear sector update preserves equality of the two
symmetry-related sector weights.

The variables gamma, delta and epsilon encode the most general two-sector
linear update with equal neutral-to-sector coupling and coefficients swapped
under + <-> -.
-/
theorem z2_equivariant_sector_update_preserves_symmetry
    (neutral plus minus gamma delta epsilon : ℚ)
    (h : plus = minus) :
    gamma * neutral + delta * plus + epsilon * minus
      =
    gamma * neutral + epsilon * plus + delta * minus := by
  rw [h]
  ring

/--
The minimal unbiased sector-selection witness gives equal ensemble weights to
the two absorbing sectors.
-/
theorem unbiased_sector_selection_has_zero_odd_polarity :
    (1 / 2 : ℚ) - (1 / 2 : ℚ) = 0 := by
  norm_num

/--
A nonzero explicit bias produces nonzero ensemble polarity in the minimal
one-step witness.
-/
theorem biased_sector_selection_polarity
    (eps : ℚ) :
    ((1 / 2 : ℚ) + eps) - ((1 / 2 : ℚ) - eps) = 2 * eps := by
  ring

end PrecategoryFormal.PhysicalBridge
