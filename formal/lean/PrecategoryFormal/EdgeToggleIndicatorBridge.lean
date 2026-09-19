import PrecategoryFormal.EdgeToggleEnsembleBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- The semantic event counted by MF-R011 for one graph-coordinate pair. -/
def ReachabilityChanged5 (g : GraphMask 5) (e : Fin (edgeCount 5)) : Prop :=
  ¬ ∀ u v : Vertex,
      Reach (maskGraph5 g) u v ↔
        Reach (maskGraph5 (toggleMask g e)) u v

/-- The cached table really returns the direct compact reachability code. -/
theorem reachCodeTable_get5 (g : GraphMask 5) :
    (reachCodeTable 5)[g.val]! = reachCode g := by
  simp [reachCodeTable]

/-- A zero indicator is equivalent to preservation of the full mathematical reachability relation. -/
theorem edgeToggleChanges5_eq_zero_iff_sameReachability
    (g : GraphMask 5) (e : Fin (edgeCount 5)) :
    edgeToggleChanges (reachCodeTable 5) g e = 0 ↔
      ∀ u v : Vertex,
        Reach (maskGraph5 g) u v ↔
          Reach (maskGraph5 (toggleMask g e)) u v := by
  simp [edgeToggleChanges, reachCodeTable, reachCode_eq_iff_sameReachability5]

/-- A one indicator is exactly the declared semantic event: some reachability fact changed. -/
theorem edgeToggleChanges5_eq_one_iff_changed
    (g : GraphMask 5) (e : Fin (edgeCount 5)) :
    edgeToggleChanges (reachCodeTable 5) g e = 1 ↔ ReachabilityChanged5 g e := by
  simp [ReachabilityChanged5, edgeToggleChanges, reachCodeTable,
    reachCode_eq_iff_sameReachability5]

/-- Every MF-R011 summand is Boolean-valued. -/
theorem edgeToggleChanges5_zero_or_one
    (g : GraphMask 5) (e : Fin (edgeCount 5)) :
    edgeToggleChanges (reachCodeTable 5) g e = 0 ∨
      edgeToggleChanges (reachCodeTable 5) g e = 1 := by
  unfold edgeToggleChanges
  split <;> simp_all

end PrecategoryFormal
