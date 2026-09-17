import Mathlib

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Reflexive-transitive reachability of an arbitrary directed relation. -/
abbrev RelationReach {α : Type*} (r : α → α → Prop) (x y : α) : Prop :=
  Relation.ReflTransGen r x y

/-- Add one distinguished directed edge `u → v` to a relation. -/
def addRelationEdge {α : Type*} (r : α → α → Prop) (u v : α) : α → α → Prop :=
  fun x y => r x y ∨ (x = u ∧ y = v)

/-- Equality of the full reflexive reachability preorders of two relations. -/
def SameReachability {α : Type*} (r s : α → α → Prop) : Prop :=
  ∀ x y, RelationReach r x y ↔ RelationReach s x y

/--
If every edge of `r` is already realizable as an `s`-path, every `r`-path can
be simulated by an `s`-path.
-/
theorem relationReach_simulate {α : Type*} {r s : α → α → Prop}
    (hEdge : ∀ ⦃x y⦄, r x y → RelationReach s x y)
    {x y : α} (h : RelationReach r x y) : RelationReach s x y := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail hxy hyz ih =>
      exact ih.trans (hEdge hyz)

/-- Adding an edge can only enlarge reachability. -/
theorem relationReach_mono_addEdge {α : Type*} (r : α → α → Prop) (u v x y : α)
    (h : RelationReach r x y) :
    RelationReach (addRelationEdge r u v) x y := by
  apply relationReach_simulate (r := r)
  · intro a b hab
    exact Relation.ReflTransGen.single (Or.inl hab)
  · exact h

/-- The newly added edge is reachable in the enlarged relation. -/
theorem addedEdge_reachable {α : Type*} (r : α → α → Prop) (u v : α) :
    RelationReach (addRelationEdge r u v) u v := by
  exact Relation.ReflTransGen.single (Or.inr ⟨rfl, rfl⟩)

/--
If `u` already reaches `v`, every edge of the enlarged relation can be
simulated in the original relation.
-/
theorem addedEdge_reach_simulates_original {α : Type*}
    (r : α → α → Prop) (u v : α)
    (huv : RelationReach r u v) {x y : α}
    (h : RelationReach (addRelationEdge r u v) x y) : RelationReach r x y := by
  apply relationReach_simulate (r := addRelationEdge r u v)
  · intro a b hab
    rcases hab with hab | hab
    · exact Relation.ReflTransGen.single hab
    · rcases hab with ⟨rfl, rfl⟩
      exact huv
  · exact h

/--
Core MF-R011 semantic lemma: adding `u → v` leaves the entire reflexive
reachability preorder unchanged exactly when `v` was already reachable from
`u` before the addition.
-/
theorem sameReachability_addEdge_iff {α : Type*}
    (r : α → α → Prop) (u v : α) :
    SameReachability r (addRelationEdge r u v) ↔ RelationReach r u v := by
  constructor
  · intro hsame
    exact (hsame u v).2 (addedEdge_reachable r u v)
  · intro huv x y
    constructor
    · exact relationReach_mono_addEdge r u v x y
    · exact addedEdge_reach_simulates_original r u v huv

/-- Equivalent pivotal-edge form used by the finite pairing argument. -/
theorem addEdge_changesReachability_iff {α : Type*}
    (r : α → α → Prop) (u v : α) :
    ¬ SameReachability r (addRelationEdge r u v) ↔ ¬ RelationReach r u v := by
  rw [sameReachability_addEdge_iff]

end PrecategoryFormal
