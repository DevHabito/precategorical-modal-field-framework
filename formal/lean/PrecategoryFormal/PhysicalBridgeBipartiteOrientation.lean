import Mathlib
import PrecategoryFormal.PhysicalBridgeOrientationDoublet

namespace PrecategoryFormal.PhysicalBridge

/-- Symmetry of an undirected adjacency relation. -/
def RelationSymmetric {α : Type*} (adj : α → α → Prop) : Prop :=
  ∀ a b, adj a b → adj b a

/--
Orient an undirected adjacency relation from the vertices satisfying `side`
toward the vertices not satisfying `side`.
-/
def orientationFromSide
    {α : Type*}
    (adj : α → α → Prop)
    (side : α → Prop) :
    α → α → Prop :=
  fun a b => adj a b ∧ side a ∧ ¬ side b

/-- An orientation from one side of a bipartition is irreflexive. -/
theorem orientationFromSide_irrefl
    {α : Type*}
    (adj : α → α → Prop)
    (side : α → Prop) :
    RelationIrreflexive (orientationFromSide adj side) := by
  intro a haa
  exact haa.2.2 haa.2.1

/--
No two oriented edges can compose when every edge is directed from one side
toward the other.
-/
theorem orientationFromSide_no_two_step
    {α : Type*}
    (adj : α → α → Prop)
    (side : α → Prop)
    {a b c : α}
    (hab : orientationFromSide adj side a b)
    (hbc : orientationFromSide adj side b c) :
    False := by
  exact hab.2.2 hbc.2.1

/--
The side orientation is transitive vacuously because it has no directed path
of length two.
-/
theorem orientationFromSide_trans
    {α : Type*}
    (adj : α → α → Prop)
    (side : α → Prop) :
    RelationTransitive (orientationFromSide adj side) := by
  intro a b c hab hbc
  exact (orientationFromSide_no_two_step adj side hab hbc).elim

/-- The side orientation is asymmetric. -/
theorem orientationFromSide_asymm
    {α : Type*}
    (adj : α → α → Prop)
    (side : α → Prop) :
    RelationAsymmetric (orientationFromSide adj side) := by
  intro a b hab hba
  exact hab.2.2 hba.2.1

/--
For symmetric adjacency, swapping the two sides gives exactly the globally
reversed orientation.
-/
theorem orientationFromComplement_eq_reverse
    {α : Type*}
    (adj : α → α → Prop)
    (side : α → Prop)
    (hsymm : RelationSymmetric adj) :
    orientationFromSide adj (fun x => ¬ side x)
      =
    reverseRelation (orientationFromSide adj side) := by
  classical
  funext a b
  apply propext
  constructor
  · intro h
    rcases h with ⟨hab, hna, hnnb⟩
    have hb : side b := Classical.not_not.mp hnnb
    exact ⟨hsymm a b hab, hb, hna⟩
  · intro h
    rcases h with ⟨hba, hb, hna⟩
    refine ⟨hsymm b a hba, hna, ?_⟩
    intro hnb
    exact hnb hb

end PrecategoryFormal.PhysicalBridge
