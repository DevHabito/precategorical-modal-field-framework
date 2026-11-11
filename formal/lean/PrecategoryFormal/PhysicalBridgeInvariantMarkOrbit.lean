import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
An invariant mark cannot distinguish two points related by a symmetry map.
-/
theorem invariant_mark_equal_on_symmetry_orbit
    {α β : Type*}
    (sigma : α → α)
    (mark : α → β)
    (hInvariant : ∀ x, mark (sigma x) = mark x)
    {a b : α}
    (hab : sigma a = b) :
    mark a = mark b := by
  calc
    mark a = mark (sigma a) := (hInvariant a).symm
    _ = mark b := by rw [hab]

/--
If a symmetry swaps two points, every symmetry-invariant mark gives them the
same value.
-/
theorem invariant_mark_cannot_split_swapped_pair
    {α β : Type*}
    (sigma : α → α)
    (mark : α → β)
    (hInvariant : ∀ x, mark (sigma x) = mark x)
    {a b : α}
    (hab : sigma a = b) :
    mark a = mark b :=
  invariant_mark_equal_on_symmetry_orbit sigma mark hInvariant hab

end PrecategoryFormal.PhysicalBridge
