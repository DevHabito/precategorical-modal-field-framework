import PrecategoryFormal.EdgeToggleSemantics

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Full-reachability equality is symmetric. -/
theorem sameReachability_symm {α : Type*}
    {r s : α → α → Prop}
    (h : SameReachability r s) : SameReachability s r := by
  intro x y
  exact (h x y).symm

/-- Symmetric equivalence form for full-reachability equality. -/
theorem sameReachability_comm {α : Type*}
    (r s : α → α → Prop) :
    SameReachability r s ↔ SameReachability s r := by
  constructor <;> exact sameReachability_symm

/--
The two states of one distinguished edge over a fixed base relation:
`false` means absent, `true` means present.
-/
def pairedEdgeState {α : Type*}
    (r : α → α → Prop) (u v : α) : Bool → α → α → Prop
  | false => r
  | true => addRelationEdge r u v

/--
Toggling either direction inside a fixed absent/present pair changes the full
reachability preorder exactly when the distinguished target was not reachable
from the source in the absent base relation.
-/
theorem pairedEdge_toggle_changes_iff {α : Type*}
    (r : α → α → Prop) (u v : α) (present : Bool) :
    ¬ SameReachability
        (pairedEdgeState r u v present)
        (pairedEdgeState r u v (!present))
      ↔ ¬ RelationReach r u v := by
  cases present with
  | false =>
      simpa [pairedEdgeState] using addEdge_changesReachability_iff r u v
  | true =>
      have hcomm :
          SameReachability (addRelationEdge r u v) r ↔
            SameReachability r (addRelationEdge r u v) :=
        sameReachability_comm _ _
      rw [show pairedEdgeState r u v true = addRelationEdge r u v by rfl]
      rw [show pairedEdgeState r u v (!true) = r by rfl]
      rw [hcomm]
      exact addEdge_changesReachability_iff r u v

/--
Both ordered toggle directions in one absent/present graph pair are pivotal
under exactly the same condition.
-/
theorem pairedEdge_both_directions_same_status {α : Type*}
    (r : α → α → Prop) (u v : α) :
    (¬ SameReachability
        (pairedEdgeState r u v false)
        (pairedEdgeState r u v true))
    ↔
    (¬ SameReachability
        (pairedEdgeState r u v true)
        (pairedEdgeState r u v false)) := by
  constructor
  · intro hforward hreverse
    exact hforward (sameReachability_symm hreverse)
  · intro hreverse hforward
    exact hreverse (sameReachability_symm hforward)

/-- Arithmetic form of the fixed-edge pairing factor used at n=5. -/
theorem mf_r011_fixed_edge_pairing_arithmetic :
    2 * 153600 = 307200 := by
  norm_num

end PrecategoryFormal
