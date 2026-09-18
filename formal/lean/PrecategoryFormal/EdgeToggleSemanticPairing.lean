import PrecategoryFormal.EdgeToggleSemanticEnsemble

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Every concrete non-loop edge bit lies inside the twenty-bit graph mask. -/
theorem edgeBitMaskFive_lt_graphBound
    (u v : Fin 5) (huv : u ≠ v) :
    edgeBitMaskFive u v < 2 ^ directedNonloopEdgeCount 5 := by
  fin_cases u <;> fin_cases v <;>
    norm_num [
      edgeBitMaskFive,
      nonloopEdgeBitIndex,
      directedNonloopEdgeCount,
      Nat.one_shiftLeft
    ] at *

/-- Toggling one legal edge preserves the finite five-vertex graph-mask universe. -/
theorem toggleEdgeMaskFive_lt_graphBound
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v)
    (hgraph : graph < 2 ^ directedNonloopEdgeCount 5) :
    toggleEdgeMaskFive graph u v < 2 ^ directedNonloopEdgeCount 5 := by
  simpa [toggleEdgeMaskFive] using
    Nat.xor_lt_two_pow hgraph (edgeBitMaskFive_lt_graphBound u v huv)

/-- Canonicalizing a graph-toggle pair to its absent member stays inside the ensemble. -/
theorem absentRepresentativeFive_lt_graphBound
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v)
    (hgraph : graph < 2 ^ directedNonloopEdgeCount 5) :
    absentRepresentativeFive graph u v < 2 ^ directedNonloopEdgeCount 5 := by
  cases h : maskHasDirectedEdge 5 graph u.val v.val with
  | false =>
      simpa [absentRepresentativeFive, h] using hgraph
  | true =>
      simpa [absentRepresentativeFive, h] using
        toggleEdgeMaskFive_lt_graphBound graph u v huv hgraph

/-- Both members of a toggle pair have the same canonical absent representative. -/
theorem absentRepresentativeFive_toggleEdgeMaskFive
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v) :
    absentRepresentativeFive (toggleEdgeMaskFive graph u v) u v =
      absentRepresentativeFive graph u v := by
  cases h : maskHasDirectedEdge 5 graph u.val v.val <;>
    simp [
      absentRepresentativeFive,
      h,
      maskHasDirectedEdge_toggleEdgeMaskFive graph u v huv,
      toggleEdgeMaskFive_involutive
    ]

/-- The executable semantic toggle-status is constant on each two-element toggle pair. -/
theorem toggleChangesBoolFive_toggleEdgeMaskFive
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v) :
    toggleChangesBoolFive (toggleEdgeMaskFive graph u v) u v =
      toggleChangesBoolFive graph u v := by
  simp [
    toggleChangesBoolFive,
    absentRepresentativeFive_toggleEdgeMaskFive graph u v huv
  ]

/--
The semantic toggle predicate is exactly the absent-edge non-reachability
predicate evaluated at the canonical absent member of the toggle pair.
-/
theorem toggleChangesBoolFive_eq_absentNoReachBoolFive
    (graph : Nat) (u v : Fin 5) (huv : u ≠ v) :
    toggleChangesBoolFive graph u v =
      fixedEdgeAbsentNoReachBoolFive (absentRepresentativeFive graph u v) u v := by
  simp [
    toggleChangesBoolFive,
    fixedEdgeAbsentNoReachBoolFive,
    maskHasDirectedEdge_absentRepresentativeFive graph u v huv
  ]

/-- Graph masks whose concrete edge toggle changes the full reachability preorder. -/
def semanticToggleGraphsFive (u v : Fin 5) : Finset Nat :=
  (Finset.range (2 ^ directedNonloopEdgeCount 5)).filter fun graph =>
    toggleChangesBoolFive graph u v = true

/-- Graph masks in which the distinguished edge is absent and pivotal. -/
def absentNoReachGraphsFive (u v : Fin 5) : Finset Nat :=
  (Finset.range (2 ^ directedNonloopEdgeCount 5)).filter fun graph =>
    fixedEdgeAbsentNoReachBoolFive graph u v = true

/-- The executable semantic counter is the cardinality of its explicit finite set. -/
theorem fixedEdgeToggleChangedDirectCountFive_eq_semanticToggleGraphsFive_card
    (u v : Fin 5) (huv : u ≠ v) :
    fixedEdgeToggleChangedDirectCountFive u v =
      (semanticToggleGraphsFive u v).card := by
  rw [fixedEdgeToggleChangedDirectCountFive_eq_semanticCount u v huv]
  rw [countNatWhere_eq_filter_card]
  rfl

/-- The direct absent-edge counter is the cardinality of its explicit finite set. -/
theorem fixedEdgeNoReachDirectCountFive_eq_absentNoReachGraphsFive_card
    (u v : Fin 5) (huv : u ≠ v) :
    fixedEdgeNoReachDirectCountFive u v =
      (absentNoReachGraphsFive u v).card := by
  simp only [fixedEdgeNoReachDirectCountFive, dif_neg huv]
  rw [countNatWhere_eq_filter_card]
  rfl

/-- Encode a semantic graph as its canonical absent base plus the original edge state. -/
def semanticToAbsentPairFive
    (graph : Nat) (u v : Fin 5) : Nat × Bool :=
  (absentRepresentativeFive graph u v,
    maskHasDirectedEdge 5 graph u.val v.val)

/-- Reconstruct one member of a toggle pair from an absent base and one Boolean bit. -/
def absentPairToSemanticFive
    (pair : Nat × Bool) (u v : Fin 5) : Nat :=
  match pair.2 with
  | false => pair.1
  | true => toggleEdgeMaskFive pair.1 u v

/--
The semantic pivotal masks are in explicit bijection with absent pivotal masks
crossed with one Boolean recording which member of the toggle pair was chosen.
This is the structural source of the factor two in MF-R011.
-/
theorem semanticToggleGraphsFive_card_eq_absent_product
    (u v : Fin 5) (huv : u ≠ v) :
    (semanticToggleGraphsFive u v).card =
      ((absentNoReachGraphsFive u v).product (Finset.univ : Finset Bool)).card := by
  refine Finset.card_nbij'
    (fun graph => semanticToAbsentPairFive graph u v)
    (fun pair => absentPairToSemanticFive pair u v)
    ?_ ?_ ?_ ?_
  · intro graph hgraph
    simp only [semanticToggleGraphsFive, Finset.mem_filter, Finset.mem_range] at hgraph
    rcases hgraph with ⟨hbound, hsemantic⟩
    simp only [
      Finset.mem_product,
      absentNoReachGraphsFive,
      Finset.mem_filter,
      Finset.mem_range,
      Finset.mem_univ,
      and_true,
      semanticToAbsentPairFive
    ]
    refine ⟨absentRepresentativeFive_lt_graphBound graph u v huv hbound, ?_⟩
    simpa [toggleChangesBoolFive_eq_absentNoReachBoolFive graph u v huv] using hsemantic
  · intro pair hpair
    rcases pair with ⟨base, present⟩
    simp only [Finset.mem_product, Finset.mem_univ, and_true] at hpair
    simp only [absentNoReachGraphsFive, Finset.mem_filter, Finset.mem_range] at hpair
    rcases hpair with ⟨hbound, hcritical⟩
    have habsent : maskHasDirectedEdge 5 base u.val v.val = false := by
      cases hedge : maskHasDirectedEdge 5 base u.val v.val with
      | false => exact hedge
      | true =>
          have : False := by
            simpa [fixedEdgeAbsentNoReachBoolFive, hedge] using hcritical
          contradiction
    have hsemanticBase : toggleChangesBoolFive base u v = true := by
      simpa [
        toggleChangesBoolFive,
        absentRepresentativeFive,
        habsent,
        fixedEdgeAbsentNoReachBoolFive
      ] using hcritical
    cases hpresent : present with
    | false =>
        simp only [absentPairToSemanticFive, hpresent]
        simp [semanticToggleGraphsFive, hbound, hsemanticBase]
    | true =>
        have htoggleBound :=
          toggleEdgeMaskFive_lt_graphBound base u v huv hbound
        have htoggleSemantic :
            toggleChangesBoolFive (toggleEdgeMaskFive base u v) u v = true := by
          rw [toggleChangesBoolFive_toggleEdgeMaskFive base u v huv]
          exact hsemanticBase
        simp only [absentPairToSemanticFive, hpresent]
        simp [semanticToggleGraphsFive, htoggleBound, htoggleSemantic]
  · intro graph hgraph
    simp only [semanticToAbsentPairFive, absentPairToSemanticFive]
    cases h : maskHasDirectedEdge 5 graph u.val v.val with
    | false =>
        simp [absentRepresentativeFive, h]
    | true =>
        simp [absentRepresentativeFive, h, toggleEdgeMaskFive_involutive]
  · intro pair hpair
    rcases pair with ⟨base, present⟩
    simp only [Finset.mem_product, Finset.mem_univ, and_true] at hpair
    simp only [absentNoReachGraphsFive, Finset.mem_filter, Finset.mem_range] at hpair
    rcases hpair with ⟨_hbound, hcritical⟩
    have habsent : maskHasDirectedEdge 5 base u.val v.val = false := by
      cases hedge : maskHasDirectedEdge 5 base u.val v.val with
      | false => exact hedge
      | true =>
          have : False := by
            simpa [fixedEdgeAbsentNoReachBoolFive, hedge] using hcritical
          contradiction
    cases hpresent : present with
    | false =>
        simp [
          semanticToAbsentPairFive,
          absentPairToSemanticFive,
          hpresent,
          absentRepresentativeFive,
          habsent
        ]
    | true =>
        simp [
          semanticToAbsentPairFive,
          absentPairToSemanticFive,
          hpresent,
          absentRepresentativeFive_toggleEdgeMaskFive base u v huv,
          maskHasDirectedEdge_toggleEdgeMaskFive base u v huv,
          habsent
        ]

/-- Every non-loop edge contributes exactly twice its absent-base pivotal count. -/
theorem fixedEdgeToggleChangedDirectCountFive_eq_two_mul_absent
    (u v : Fin 5) (huv : u ≠ v) :
    fixedEdgeToggleChangedDirectCountFive u v =
      2 * fixedEdgeNoReachDirectCountFive u v := by
  rw [fixedEdgeToggleChangedDirectCountFive_eq_semanticToggleGraphsFive_card u v huv]
  rw [fixedEdgeNoReachDirectCountFive_eq_absentNoReachGraphsFive_card u v huv]
  rw [semanticToggleGraphsFive_card_eq_absent_product u v huv]
  simp [Nat.mul_comm]

end PrecategoryFormal
