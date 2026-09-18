import PrecategoryFormal.EdgeToggleFastSemantic

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- All vertex-subset lists, generated constructively from the finite carrier. -/
def vertexSubsetLists (n : Nat) : List (List (MaskVertex n)) :=
  (List.finRange n).powerset

/-- Source/target-separating vertex lists. -/
def separatingVertexLists
    (n : Nat) (u v : MaskVertex n) : List (List (MaskVertex n)) :=
  (vertexSubsetLists n).filter fun S =>
    decide (u ∈ S) && !(decide (v ∈ S))

/--
Directed non-loop edge-bit indices that leave a concrete vertex list.
This is fully computable and uses only `List` operations.
-/
def crossingEdgeBitList
    (n : Nat) (S : List (MaskVertex n)) : List Nat :=
  (List.finRange n).flatMap fun x =>
    (List.finRange n).filterMap fun y =>
      if h : x ∈ S ∧ y ∉ S ∧ x ≠ y then
        some (nonloopEdgeBitIndex n x.val y.val)
      else
        none

/-- Membership characterization of the constructively generated crossing-bit list. -/
theorem mem_crossingEdgeBitList_iff
    (n bit : Nat) (S : List (MaskVertex n)) :
    bit ∈ crossingEdgeBitList n S ↔
      ∃ x y : MaskVertex n,
        x ∈ S ∧ y ∉ S ∧ x ≠ y ∧
        bit = nonloopEdgeBitIndex n x.val y.val := by
  simp [crossingEdgeBitList]
  constructor
  · rintro x y hx hy hxy rfl
    exact ⟨x, y, hx, hy, hxy, rfl⟩
  · rintro ⟨x, y, hx, hy, hxy, rfl⟩
    exact ⟨x, y, hx, hy, hxy, rfl⟩

/-- Allocation-free checker that all listed edge bits are absent. -/
def noPresentEdgeBitListBool (graph : Nat) (bits : List Nat) : Bool :=
  bits.all fun bit => !(graph.testBit bit)

/--
For a concrete vertex list, absence of all crossing edge bits is exactly
forward closure under the mathematical mask relation.
-/
theorem noPresentCrossingEdgeBitListBool_eq_true_iff
    (n graph : Nat) (S : List (MaskVertex n)) :
    noPresentEdgeBitListBool graph (crossingEdgeBitList n S) = true ↔
      ∀ ⦃x y : MaskVertex n⦄, x ∈ S → maskRelation n graph x y → y ∈ S := by
  constructor
  · intro hall x y hx hedge
    by_contra hy
    have hxy : x ≠ y := by
      intro h
      subst y
      exact hy hx
    have hbit :
        graph.testBit (nonloopEdgeBitIndex n x.val y.val) = true :=
      (maskRelation_iff_testBit_of_ne n graph hxy).1 hedge
    have hmem :
        nonloopEdgeBitIndex n x.val y.val ∈ crossingEdgeBitList n S :=
      (mem_crossingEdgeBitList_iff n _ S).2
        ⟨x, y, hx, hy, hxy, rfl⟩
    have habsent :
        !(graph.testBit (nonloopEdgeBitIndex n x.val y.val)) = true := by
      have hforall := (List.all_eq_true.mp hall)
      exact hforall _ hmem
    simp [hbit] at habsent
  · intro hclosed
    apply List.all_eq_true.mpr
    intro bit hmem
    rcases (mem_crossingEdgeBitList_iff n bit S).1 hmem with
      ⟨x, y, hx, hy, hxy, rfl⟩
    have hnot :
        graph.testBit (nonloopEdgeBitIndex n x.val y.val) ≠ true := by
      intro hbit
      have hedge : maskRelation n graph x y :=
        (maskRelation_iff_testBit_of_ne n graph hxy).2 hbit
      exact hy (hclosed hx hedge)
    cases hb : graph.testBit (nonloopEdgeBitIndex n x.val y.val)
    · rfl
    · exact (hnot hb).elim

/-- Precomputed outgoing-edge-bit lists for every source/target-separating subset. -/
def separatorBitLists
    (n : Nat) (u v : MaskVertex n) : List (List Nat) :=
  (separatingVertexLists n u v).map (crossingEdgeBitList n)

/-- Graph test against the precomputed separator bit lists. -/
def noReachWithBitLists (graph : Nat) (families : List (List Nat)) : Bool :=
  families.any (noPresentEdgeBitListBool graph)

/-- A list separator carries exactly the same semantic conditions as a finite-set separator. -/
def ListForwardClosedSeparator
    (n graph : Nat) (u v : MaskVertex n) (S : List (MaskVertex n)) : Prop :=
  u ∈ S ∧
  v ∉ S ∧
  ∀ ⦃x y : MaskVertex n⦄, x ∈ S → maskRelation n graph x y → y ∈ S

/-- Accepted precomputed bit lists correspond to semantic list separators. -/
theorem noReachWithBitLists_eq_true_iff_exists_listSeparator
    (n graph : Nat) (u v : MaskVertex n) :
    noReachWithBitLists graph (separatorBitLists n u v) = true ↔
      ∃ S : List (MaskVertex n),
        S ∈ vertexSubsetLists n ∧
        ListForwardClosedSeparator n graph u v S := by
  simp only [
    noReachWithBitLists,
    separatorBitLists,
    separatingVertexLists,
    List.any_eq_true
  ]
  constructor
  · rintro ⟨bits, hbits, hnone⟩
    rcases List.mem_map.mp hbits with ⟨S, hSfiltered, rfl⟩
    have hSdata := List.mem_filter.mp hSfiltered
    have hsepbool := hSdata.2
    have hu : u ∈ S := by
      have := Bool.and_eq_true.mp hsepbool
      exact of_decide_eq_true this.1
    have hv : v ∉ S := by
      have := Bool.and_eq_true.mp hsepbool
      exact of_decide_eq_false (Bool.not_eq_true.mp this.2)
    refine ⟨S, hSdata.1, hu, hv, ?_⟩
    exact (noPresentCrossingEdgeBitListBool_eq_true_iff n graph S).1 hnone
  · rintro ⟨S, hSpow, hu, hv, hclosed⟩
    refine ⟨crossingEdgeBitList n S, ?_, ?_⟩
    · apply List.mem_map.mpr
      refine ⟨S, ?_, rfl⟩
      apply List.mem_filter.mpr
      refine ⟨hSpow, ?_⟩
      apply Bool.and_eq_true.mpr
      constructor
      · exact decide_eq_true hu
      · exact Bool.not_eq_true.mpr (decide_eq_false hv)
    · exact (noPresentCrossingEdgeBitListBool_eq_true_iff n graph S).2 hclosed

/-- Every semantic list separator yields a semantic finite-set separator. -/
theorem listSeparator_to_finsetSeparator
    (n graph : Nat) (u v : MaskVertex n) (S : List (MaskVertex n))
    (hS : ListForwardClosedSeparator n graph u v S) :
    FinsetForwardClosedSeparator n graph u v S.toFinset := by
  rcases hS with ⟨hu, hv, hclosed⟩
  refine ⟨?_, ?_, ?_⟩
  · simpa using hu
  · simpa using hv
  · intro x y hx hedge
    have hxList : x ∈ S := by simpa using hx
    have hyList : y ∈ S := hclosed hxList hedge
    simpa using hyList

/--
Every finite-set separator has a canonical list presentation obtained by
filtering the ordered finite carrier.
-/
theorem finsetSeparator_to_exists_listSeparator
    (n graph : Nat) (u v : MaskVertex n) (T : Finset (MaskVertex n))
    (hT : FinsetForwardClosedSeparator n graph u v T) :
    ∃ S : List (MaskVertex n),
      S ∈ vertexSubsetLists n ∧
      ListForwardClosedSeparator n graph u v S := by
  let S : List (MaskVertex n) :=
    (List.finRange n).filter fun x => decide (x ∈ T)
  have hmem_iff (x : MaskVertex n) : x ∈ S ↔ x ∈ T := by
    simp [S]
  refine ⟨S, ?_, ?_, ?_, ?_⟩
  · have hsub : S <+ List.finRange n := by
      exact List.filter_sublist
    simpa [vertexSubsetLists] using hsub
  · exact (hmem_iff u).2 hT.1
  · intro hv
    exact hT.2.1 ((hmem_iff v).1 hv)
  · intro x y hx hedge
    apply (hmem_iff y).2
    exact hT.2.2 ((hmem_iff x).1 hx) hedge

/-- List-separator existence is exactly finite-set-separator existence. -/
theorem exists_listSeparator_iff_exists_finsetSeparator
    (n graph : Nat) (u v : MaskVertex n) :
    (∃ S : List (MaskVertex n),
      S ∈ vertexSubsetLists n ∧
      ListForwardClosedSeparator n graph u v S) ↔
    (∃ T : Finset (MaskVertex n),
      FinsetForwardClosedSeparator n graph u v T) := by
  constructor
  · rintro ⟨S, _, hS⟩
    exact ⟨S.toFinset, listSeparator_to_finsetSeparator n graph u v S hS⟩
  · rintro ⟨T, hT⟩
    exact finsetSeparator_to_exists_listSeparator n graph u v T hT

/-- End-to-end semantic correctness of the fully computable precomputed checker. -/
theorem noReachWithBitLists_eq_true_iff
    (n graph : Nat) (u v : MaskVertex n) :
    noReachWithBitLists graph (separatorBitLists n u v) = true ↔
      ¬ RelationReach (maskRelation n graph) u v := by
  rw [noReachWithBitLists_eq_true_iff_exists_listSeparator]
  rw [exists_listSeparator_iff_exists_finsetSeparator]
  exact (not_maskRelationReach_iff_exists_finsetSeparator n graph u v).symm

end PrecategoryFormal
