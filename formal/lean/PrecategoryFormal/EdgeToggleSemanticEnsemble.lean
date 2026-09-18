import PrecategoryFormal.EdgeToggleEnsembleCount
import PrecategoryFormal.EdgeToggleMaskBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/--
Canonical absent-edge representative of a concrete five-vertex graph-toggle
pair. If the distinguished edge is already absent, keep the graph. If it is
present, toggle it once.
-/
def absentRepresentativeFive
    (graph : Nat) (u v : Fin 5) : Nat :=
  match maskHasDirectedEdge 5 graph u.val v.val with
  | false => graph
  | true => toggleEdgeMaskFive graph u v

/-- The canonical representative really has the distinguished non-loop edge absent. -/
theorem maskHasDirectedEdge_absentRepresentativeFive
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v) :
    maskHasDirectedEdge 5 (absentRepresentativeFive graph u v) u.val v.val = false := by
  cases h : maskHasDirectedEdge 5 graph u.val v.val with
  | false =>
      simp [absentRepresentativeFive, h]
  | true =>
      simpa [absentRepresentativeFive, h] using
        (maskHasDirectedEdge_toggleEdgeMaskFive graph u v huv)

/--
Executable semantic toggle-status predicate. It first moves the graph to the
absent member of its toggle pair and then asks the already-proved semantic
non-reachability checker whether `u` reaches `v` there.
-/
def toggleChangesBoolFive
    (graph : Nat) (u v : Fin 5) : Bool :=
  noReachWithBitLists
    (absentRepresentativeFive graph u v)
    (separatorBitLists 5 u v)

/--
End-to-end semantic meaning of `toggleChangesBoolFive`: for every concrete
five-vertex non-loop edge, the Boolean is true exactly when toggling that edge
changes the complete reflexive reachability preorder.
-/
theorem toggleChangesBoolFive_eq_true_iff
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v) :
    toggleChangesBoolFive graph u v = true ↔
      ¬ SameReachability
        (maskRelation 5 graph)
        (maskRelation 5 (toggleEdgeMaskFive graph u v)) := by
  cases hpresent : maskHasDirectedEdge 5 graph u.val v.val with
  | false =>
      simp only [toggleChangesBoolFive, absentRepresentativeFive, hpresent]
      rw [noReachWithBitLists_eq_true_iff]
      exact
        (maskToggle_changesReachability_iff_of_absent
          graph u v huv hpresent).symm
  | true =>
      have habsent :
          maskHasDirectedEdge 5
            (toggleEdgeMaskFive graph u v) u.val v.val = false := by
        simpa [hpresent] using
          (maskHasDirectedEdge_toggleEdgeMaskFive graph u v huv)
      have hreverse :
          (¬ SameReachability
            (maskRelation 5 (toggleEdgeMaskFive graph u v))
            (maskRelation 5 graph)) ↔
          ¬ RelationReach
            (maskRelation 5 (toggleEdgeMaskFive graph u v)) u v := by
        simpa [toggleEdgeMaskFive_involutive] using
          (maskToggle_changesReachability_iff_of_absent
            (toggleEdgeMaskFive graph u v) u v huv habsent)
      simp only [toggleChangesBoolFive, absentRepresentativeFive, hpresent]
      rw [noReachWithBitLists_eq_true_iff]
      constructor
      · intro hnoReach
        have hrev :
            ¬ SameReachability
              (maskRelation 5 (toggleEdgeMaskFive graph u v))
              (maskRelation 5 graph) :=
          hreverse.mpr hnoReach
        exact (maskToggle_both_directions_same_status graph u v).mpr hrev
      · intro hforward
        have hrev :
            ¬ SameReachability
              (maskRelation 5 (toggleEdgeMaskFive graph u v))
              (maskRelation 5 graph) :=
          (maskToggle_both_directions_same_status graph u v).mp hforward
        exact hreverse.mp hrev

/--
Direct count over all `2^20` graph masks for one fixed directed non-loop edge.
This is retained as the canonical finite object to be connected to the existing
absent-edge count by an explicit toggle-pair bijection, rather than evaluated
again by a redundant million-state computation.
-/
def fixedEdgeToggleChangedDirectCountFive
    (u v : Fin 5) : Nat :=
  if _h : u = v then
    0
  else
    let families := separatorBitLists 5 u v
    countNatWhere (2 ^ directedNonloopEdgeCount 5) fun graph =>
      noReachWithBitLists (absentRepresentativeFive graph u v) families

/-- For a non-loop edge, the direct counter is literally the semantic toggle predicate count. -/
theorem fixedEdgeToggleChangedDirectCountFive_eq_semanticCount
    (u v : Fin 5) (huv : u ≠ v) :
    fixedEdgeToggleChangedDirectCountFive u v =
      countNatWhere (2 ^ directedNonloopEdgeCount 5) fun graph =>
        toggleChangesBoolFive graph u v := by
  simp [
    fixedEdgeToggleChangedDirectCountFive,
    toggleChangesBoolFive,
    huv
  ]

/--
Direct full ordered graph-edge semantic numerator at `n = 5`. The twenty
summands are exactly the twenty directed non-loop edge positions. We do not
re-evaluate this aggregate with `native_decide`; the remaining obligation is a
structural count proof from toggle-pairing and relabeling/bijection lemmas.
-/
def semanticChangedGraphEdgePairsFive : Nat :=
  fixedEdgeToggleChangedDirectCountFive 0 1 +
  fixedEdgeToggleChangedDirectCountFive 0 2 +
  fixedEdgeToggleChangedDirectCountFive 0 3 +
  fixedEdgeToggleChangedDirectCountFive 0 4 +
  fixedEdgeToggleChangedDirectCountFive 1 0 +
  fixedEdgeToggleChangedDirectCountFive 1 2 +
  fixedEdgeToggleChangedDirectCountFive 1 3 +
  fixedEdgeToggleChangedDirectCountFive 1 4 +
  fixedEdgeToggleChangedDirectCountFive 2 0 +
  fixedEdgeToggleChangedDirectCountFive 2 1 +
  fixedEdgeToggleChangedDirectCountFive 2 3 +
  fixedEdgeToggleChangedDirectCountFive 2 4 +
  fixedEdgeToggleChangedDirectCountFive 3 0 +
  fixedEdgeToggleChangedDirectCountFive 3 1 +
  fixedEdgeToggleChangedDirectCountFive 3 2 +
  fixedEdgeToggleChangedDirectCountFive 3 4 +
  fixedEdgeToggleChangedDirectCountFive 4 0 +
  fixedEdgeToggleChangedDirectCountFive 4 1 +
  fixedEdgeToggleChangedDirectCountFive 4 2 +
  fixedEdgeToggleChangedDirectCountFive 4 3

end PrecategoryFormal
