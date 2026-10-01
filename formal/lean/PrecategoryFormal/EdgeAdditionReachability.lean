import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Add one directed edge `s → t` to an arbitrary binary relation. -/
def addDirectedEdge {α : Type} (r : α → α → Prop) (s t : α) : α → α → Prop :=
  fun x y => r x y ∨ (x = s ∧ y = t)

/-- Every old path remains a path after one edge is added. -/
theorem reflTransGen_mono_addDirectedEdge
    {α : Type} {r : α → α → Prop} {s t x y : α}
    (h : Relation.ReflTransGen r x y) :
    Relation.ReflTransGen (addDirectedEdge r s t) x y := by
  induction h with
  | refl =>
      exact Relation.ReflTransGen.refl
  | tail hxy hyz ih =>
      exact ih.tail (Or.inl hyz)

/--
If `t` was already reachable from `s`, then every path using the newly added
edge can be rewritten as a path in the original relation.
-/
theorem reflTransGen_addDirectedEdge_of_reachable
    {α : Type} {r : α → α → Prop} {s t x y : α}
    (hst : Relation.ReflTransGen r s t)
    (h : Relation.ReflTransGen (addDirectedEdge r s t) x y) :
    Relation.ReflTransGen r x y := by
  induction h with
  | refl =>
      exact Relation.ReflTransGen.refl
  | tail hxy hyz ih =>
      rcases hyz with hold | hnew
      · exact ih.tail hold
      · rcases hnew with ⟨rfl, rfl⟩
        exact ih.trans hst

/--
Adding `s → t` preserves the entire reflexive-transitive closure exactly when
`t` was already reachable from `s` before the insertion.

No finiteness, decidability, graph encoding, or probability assumption is used.
-/
theorem addDirectedEdge_preserves_reachability_iff
    {α : Type} (r : α → α → Prop) (s t : α) :
    (∀ x y : α,
      Relation.ReflTransGen (addDirectedEdge r s t) x y ↔
        Relation.ReflTransGen r x y) ↔
      Relation.ReflTransGen r s t := by
  constructor
  · intro hall
    apply (hall s t).1
    exact Relation.ReflTransGen.single (Or.inr ⟨rfl, rfl⟩)
  · intro hst x y
    constructor
    · exact reflTransGen_addDirectedEdge_of_reachable hst
    · exact reflTransGen_mono_addDirectedEdge

/--
Equivalent change criterion: the full reachability relation changes after
inserting `s → t` exactly when `t` was not already reachable from `s`.
-/
theorem addDirectedEdge_changes_reachability_iff
    {α : Type} (r : α → α → Prop) (s t : α) :
    (¬ ∀ x y : α,
      Relation.ReflTransGen (addDirectedEdge r s t) x y ↔
        Relation.ReflTransGen r x y) ↔
      ¬ Relation.ReflTransGen r s t := by
  constructor
  · intro hchange hst
    exact hchange ((addDirectedEdge_preserves_reachability_iff r s t).2 hst)
  · intro hnot hsame
    exact hnot ((addDirectedEdge_preserves_reachability_iff r s t).1 hsame)

end PrecategoryFormal
