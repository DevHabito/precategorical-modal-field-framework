import PrecategoryFormal.EdgeToggleBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- One-hot mask of a directed non-loop edge position on five vertices. -/
def edgeBitMaskFive (u v : Fin 5) : Nat :=
  1 <<< nonloopEdgeBitIndex 5 u.val v.val

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
  simp [toggleEdgeMaskFive, edgeBitMaskFive, Nat.xor_assoc]

/--
Adding one concrete non-loop edge bit to a five-vertex mask has exactly the
same mathematical edge relation as `addRelationEdge`.

This theorem is intentionally about the original graph-mask representation,
not the compressed enumeration used by an optimization path.
-/
theorem maskRelation_addEdgeMaskFive
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v) :
    maskRelation 5 (addEdgeMaskFive graph u v) =
      addRelationEdge (maskRelation 5 graph) u v := by
  funext x y
  apply propext
  fin_cases u <;> fin_cases v <;>
    try { exact (huv rfl).elim } <;>
    fin_cases x <;> fin_cases y <;>
    simp [
      addEdgeMaskFive,
      edgeBitMaskFive,
      maskRelation,
      maskHasDirectedEdge,
      nonloopEdgeBitIndex,
      addRelationEdge,
      Nat.testBit_lor,
      Nat.testBit_shiftLeft
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
  apply Nat.eq_of_testBit_eq
  intro bit
  simp only [toggleEdgeMaskFive, addEdgeMaskFive, edgeBitMaskFive,
    Nat.testBit_xor, Nat.testBit_lor]
  by_cases hbit : bit = nonloopEdgeBitIndex 5 u.val v.val
  · subst bit
    have hgraph : graph.testBit (nonloopEdgeBitIndex 5 u.val v.val) = false := by
      simpa [maskHasDirectedEdge, u.isLt, v.isLt, huv] using habsent
    simp [hgraph, Nat.testBit_shiftLeft]
  · simp [Nat.testBit_shiftLeft, hbit]

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

end PrecategoryFormal
