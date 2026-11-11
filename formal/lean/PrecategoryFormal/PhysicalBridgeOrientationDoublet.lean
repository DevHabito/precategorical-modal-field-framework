import Mathlib

namespace PrecategoryFormal.PhysicalBridge

/-- Global reversal of a binary relation. -/
def reverseRelation {α : Type*} (r : α → α → Prop) : α → α → Prop :=
  fun a b => r b a

@[simp]
theorem reverseRelation_apply {α : Type*} (r : α → α → Prop) (a b : α) :
    reverseRelation r a b ↔ r b a := by
  rfl

/-- Global reversal is an involution. -/
theorem reverseRelation_involutive {α : Type*} (r : α → α → Prop) :
    reverseRelation (reverseRelation r) = r := by
  funext a b
  rfl

/-- Irreflexivity is preserved by global reversal. -/
theorem reverseRelation_irrefl
    {α : Type*}
    (r : α → α → Prop)
    (h : IsIrrefl α r) :
    IsIrrefl α (reverseRelation r) := by
  intro a
  exact h a

/-- Asymmetry is preserved by global reversal. -/
theorem reverseRelation_asymm
    {α : Type*}
    (r : α → α → Prop)
    (h : IsAsymm α r) :
    IsAsymm α (reverseRelation r) := by
  intro a b hab
  exact h b a hab

/-- Transitivity is preserved by global reversal. -/
theorem reverseRelation_trans
    {α : Type*}
    (r : α → α → Prop)
    (h : IsTrans α r) :
    IsTrans α (reverseRelation r) := by
  intro a b c hab hbc
  exact h c b a hbc hab

/--
A strict-order candidate remains a strict-order candidate after global
reversal.  This is the logical reason an orientation axis can come as a
two-element reversal class even when no polarity has been selected.
-/
theorem reverse_strict_order_kernel
    {α : Type*}
    (r : α → α → Prop)
    (hirr : IsIrrefl α r)
    (htrans : IsTrans α r) :
    IsIrrefl α (reverseRelation r) ∧
    IsTrans α (reverseRelation r) := by
  exact ⟨reverseRelation_irrefl r hirr, reverseRelation_trans r htrans⟩

end PrecategoryFormal.PhysicalBridge
