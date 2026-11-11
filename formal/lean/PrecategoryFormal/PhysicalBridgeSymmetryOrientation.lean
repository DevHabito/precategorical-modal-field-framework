import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/--
If a strict relation is equivariant under a map sigma that swaps a and b,
then it cannot orient a toward b.

This is the algebraic core of the symmetry-orientation gate. It contains no
physical interpretation.
-/
theorem swap_symmetry_forbids_asymmetric_orientation
    {α : Type}
    (prec : α → α → Prop)
    (sigma : α → α)
    (a b : α)
    (hab : sigma a = b)
    (hba : sigma b = a)
    (hasym : ∀ {x y : α}, prec x y → ¬ prec y x)
    (hequiv : ∀ x y : α, prec x y ↔ prec (sigma x) (sigma y)) :
    ¬ prec a b := by
  intro h
  have hrev : prec b a := by
    have hs : prec (sigma a) (sigma b) := (hequiv a b).1 h
    simpa [hab, hba] using hs
  exact (hasym h) hrev

end PrecategoryFormal.PhysicalBridge
