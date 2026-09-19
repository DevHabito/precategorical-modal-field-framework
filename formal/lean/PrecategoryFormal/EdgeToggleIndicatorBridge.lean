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
  unfold reachCodeTable
  let table := Array.ofFn (fun h : GraphMask 5 => reachCode h)
  have hg : g.val < table.size := by
    simpa [table] using g.isLt
  change table[g.val]! = reachCode g
  rw [getElem!_pos table g.val hg]
  change (Array.ofFn (fun h : GraphMask 5 => reachCode h))[g.val] = reachCode g
  rw [Array.getElem_ofFn]
  apply congrArg reachCode
  exact Fin.ext rfl

/-- A zero indicator is equivalent to preservation of the full mathematical reachability relation. -/
theorem edgeToggleChanges5_eq_zero_iff_sameReachability
    (g : GraphMask 5) (e : Fin (edgeCount 5)) :
    edgeToggleChanges (reachCodeTable 5) g e = 0 ↔
      ∀ u v : Vertex,
        Reach (maskGraph5 g) u v ↔
          Reach (maskGraph5 (toggleMask g e)) u v := by
  unfold edgeToggleChanges
  rw [reachCodeTable_get5 g, reachCodeTable_get5 (toggleMask g e)]
  constructor
  · intro hind
    by_cases hcode : reachCode g = reachCode (toggleMask g e)
    · exact reachCode_eq_implies_sameReachability5 hcode
    · simp [hcode] at hind
  · intro hsame
    have hcode : reachCode g = reachCode (toggleMask g e) :=
      sameReachability5_implies_reachCode_eq hsame
    simp [hcode]

/-- A one indicator is exactly the declared semantic event: some reachability fact changed. -/
theorem edgeToggleChanges5_eq_one_iff_changed
    (g : GraphMask 5) (e : Fin (edgeCount 5)) :
    edgeToggleChanges (reachCodeTable 5) g e = 1 ↔ ReachabilityChanged5 g e := by
  unfold ReachabilityChanged5 edgeToggleChanges
  rw [reachCodeTable_get5 g, reachCodeTable_get5 (toggleMask g e)]
  constructor
  · intro hind hsame
    have hcode : reachCode g = reachCode (toggleMask g e) :=
      sameReachability5_implies_reachCode_eq hsame
    simp [hcode] at hind
  · intro hchanged
    by_cases hcode : reachCode g = reachCode (toggleMask g e)
    · exact False.elim (hchanged (reachCode_eq_implies_sameReachability5 hcode))
    · simp [hcode]

/-- Every MF-R011 summand is Boolean-valued. -/
theorem edgeToggleChanges5_zero_or_one
    (g : GraphMask 5) (e : Fin (edgeCount 5)) :
    edgeToggleChanges (reachCodeTable 5) g e = 0 ∨
      edgeToggleChanges (reachCodeTable 5) g e = 1 := by
  unfold edgeToggleChanges
  split <;> simp_all

end PrecategoryFormal
