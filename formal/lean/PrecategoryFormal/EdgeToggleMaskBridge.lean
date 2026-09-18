import PrecategoryFormal.EdgeToggleBridge
import PrecategoryFormal.EdgeTogglePairing

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- One-hot mask of a directed non-loop edge position on five vertices. -/
def edgeBitMaskFive (u v : Fin 5) : Nat :=
  1 <<< nonloopEdgeBitIndex 5 u.val v.val

/-- A shifted one-bit natural has exactly one set bit. -/
theorem testBit_one_shiftLeft_eq (pos bit : Nat) :
    Nat.testBit (1 <<< pos) bit = decide (bit = pos) := by
  rw [Nat.testBit_shiftLeft]
  by_cases hle : pos ≤ bit
  · by_cases heq : bit = pos
    · subst bit
      simp
    · have hsub : bit - pos ≠ 0 := by omega
      have hfalse : Nat.testBit 1 (bit - pos) = false := by
        cases hbit : Nat.testBit 1 (bit - pos) with
        | false => rfl
        | true =>
            exfalso
            exact hsub ((Nat.testBit_one_eq_true_iff_self_eq_zero).1 hbit)
      simp [hle, heq, hfalse]
  · have hne : bit ≠ pos := by omega
    simp [hle, hne]

/-- The edge one-hot mask tests true exactly at its encoded edge index. -/
theorem edgeBitMaskFive_testBit
    (u v : Fin 5) (bit : Nat) :
    Nat.testBit (edgeBitMaskFive u v) bit =
      decide (bit = nonloopEdgeBitIndex 5 u.val v.val) := by
  exact testBit_one_shiftLeft_eq _ _

/--
On five vertices, the row-major diagonal-removed index is injective on
non-loop directed edges.
-/
theorem nonloopEdgeBitIndex_five_eq_iff
    (u v x y : Fin 5) (huv : u ≠ v) (hxy : x ≠ y) :
    nonloopEdgeBitIndex 5 u.val v.val = nonloopEdgeBitIndex 5 x.val y.val ↔
      u = x ∧ v = y := by
  fin_cases u <;> fin_cases v <;> fin_cases x <;> fin_cases y <;>
    simp_all [nonloopEdgeBitIndex]

/-- Add the distinguished edge at the mask level. -/
def addEdgeMaskFive (graph : Nat) (u v : Fin 5) : Nat :=
  graph ||| edgeBitMaskFive u v

/-- Toggle the distinguished edge at the mask level. -/
def toggleEdgeMaskFive (graph : Nat) (u v : Fin 5) : Nat :=
  graph ^^^ edgeBitMaskFive u v

/-- Mask-level edge toggle is an involution. -/
theorem toggleEdgeMaskFive_involutive
    (graph : Nat) (u v : Fin 5) :
    toggleEdgeMaskFive (toggleEdgeMaskFive graph u v) u v = graph := by
  simp [toggleEdgeMaskFive, edgeBitMaskFive]

/--
The mask-level toggle flips exactly the distinguished non-loop edge state.
Together with involutivity, this gives an explicit absent/present pairing of
five-vertex graph masks for every fixed directed non-loop edge.
-/
theorem maskHasDirectedEdge_toggleEdgeMaskFive
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v) :
    maskHasDirectedEdge 5 (toggleEdgeMaskFive graph u v) u.val v.val =
      !(maskHasDirectedEdge 5 graph u.val v.val) := by
  have huvval : u.val ≠ v.val := by
    intro h
    apply huv
    exact Fin.ext h
  simp [
    toggleEdgeMaskFive,
    maskHasDirectedEdge,
    u.isLt,
    v.isLt,
    huvval,
    edgeBitMaskFive_testBit
  ]

/--
Adding one concrete non-loop edge bit to a five-vertex mask has exactly the
same mathematical edge relation as `addRelationEdge`.
-/
theorem maskRelation_addEdgeMaskFive
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v) :
    maskRelation 5 (addEdgeMaskFive graph u v) =
      addRelationEdge (maskRelation 5 graph) u v := by
  funext x y
  apply propext
  by_cases hxy : x = y
  · subst y
    have hnot : ¬ (x = u ∧ x = v) := by
      rintro ⟨hxu, hxv⟩
      apply huv
      exact hxu.symm.trans hxv
    simp [
      maskRelation,
      maskHasDirectedEdge,
      addRelationEdge,
      addEdgeMaskFive,
      hnot
    ]
  · have hxyval : x.val ≠ y.val := by
      intro h
      exact hxy (Fin.ext h)
    have hindex :
        nonloopEdgeBitIndex 5 x.val y.val = nonloopEdgeBitIndex 5 u.val v.val ↔
          x = u ∧ y = v := by
      rw [eq_comm]
      simpa [eq_comm] using
        (nonloopEdgeBitIndex_five_eq_iff u v x y huv hxy)
    simp [
      maskRelation,
      maskHasDirectedEdge,
      x.isLt,
      y.isLt,
      hxyval,
      addRelationEdge,
      addEdgeMaskFive,
      edgeBitMaskFive_testBit,
      hindex
    ]

/-- The added mask has the distinguished edge present. -/
theorem maskHasDirectedEdge_addEdgeMaskFive
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v) :
    maskHasDirectedEdge 5 (addEdgeMaskFive graph u v) u.val v.val = true := by
  have hrel :
      maskRelation 5 (addEdgeMaskFive graph u v) u v := by
    rw [maskRelation_addEdgeMaskFive graph u v huv]
    exact Or.inr ⟨rfl, rfl⟩
  simpa [maskRelation] using hrel

/--
If the distinguished edge is absent in the base mask, toggling its bit agrees
with adding it. This is the exact mask-level absent/present pairing used by
MF-R011.
-/
theorem toggleEdgeMaskFive_eq_addEdgeMaskFive_of_absent
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v)
    (habsent : maskHasDirectedEdge 5 graph u.val v.val = false) :
    toggleEdgeMaskFive graph u v = addEdgeMaskFive graph u v := by
  have huvval : u.val ≠ v.val := by
    intro h
    apply huv
    exact Fin.ext h
  have hgraph :
      graph.testBit (nonloopEdgeBitIndex 5 u.val v.val) = false := by
    simpa [maskHasDirectedEdge, u.isLt, v.isLt, huvval] using habsent
  apply Nat.eq_of_testBit_eq
  intro bit
  rw [Nat.testBit_xor, Nat.testBit_or]
  rw [edgeBitMaskFive_testBit]
  by_cases hbit : bit = nonloopEdgeBitIndex 5 u.val v.val
  · subst bit
    simp [hgraph]
  · simp [hbit]

/--
For an absent distinguished edge, the relation of the toggled graph mask is
exactly the original relation with that edge added.
-/
theorem maskRelation_toggleEdgeMaskFive_of_absent
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v)
    (habsent : maskHasDirectedEdge 5 graph u.val v.val = false) :
    maskRelation 5 (toggleEdgeMaskFive graph u v) =
      addRelationEdge (maskRelation 5 graph) u v := by
  rw [toggleEdgeMaskFive_eq_addEdgeMaskFive_of_absent graph u v huv habsent]
  exact maskRelation_addEdgeMaskFive graph u v huv

/--
Exact mask-level pivotality criterion for an absent edge: toggling the graph
mask changes the full reflexive reachability preorder iff the target was not
reachable from the source in the absent graph.
-/
theorem maskToggle_changesReachability_iff_of_absent
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v)
    (habsent : maskHasDirectedEdge 5 graph u.val v.val = false) :
    (¬ SameReachability
      (maskRelation 5 graph)
      (maskRelation 5 (toggleEdgeMaskFive graph u v)))
      ↔ ¬ RelationReach (maskRelation 5 graph) u v := by
  rw [maskRelation_toggleEdgeMaskFive_of_absent graph u v huv habsent]
  exact addEdge_changesReachability_iff (maskRelation 5 graph) u v

/--
The two ordered directions within one concrete graph-mask toggle pair have the
same changed/unchanged reachability status.
-/
theorem maskToggle_both_directions_same_status
    (graph : Nat) (u v : Fin 5) :
    (¬ SameReachability
      (maskRelation 5 graph)
      (maskRelation 5 (toggleEdgeMaskFive graph u v)))
    ↔
    (¬ SameReachability
      (maskRelation 5 (toggleEdgeMaskFive graph u v))
      (maskRelation 5 graph)) := by
  constructor
  · intro hforward hreverse
    exact hforward (sameReachability_symm hreverse)
  · intro hreverse hforward
    exact hreverse (sameReachability_symm hforward)

end PrecategoryFormal
