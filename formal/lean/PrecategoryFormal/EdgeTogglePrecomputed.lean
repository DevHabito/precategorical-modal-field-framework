import PrecategoryFormal.EdgeToggleFastSemantic

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/--
Constructive powerset of a list. The order of generated subsets is irrelevant;
we use this only as a finite executable enumeration.
-/
def listPowerset {α : Type*} : List α → List (List α)
  | [] => [[]]
  | a :: l =>
      let ps := listPowerset l
      ps ++ ps.map (fun s => a :: s)

/-- Filtering any list selects one member of its constructive powerset. -/
theorem filter_mem_listPowerset {α : Type*}
    (p : α → Bool) (l : List α) :
    l.filter p ∈ listPowerset l := by
  induction l with
  | nil =>
      simp [listPowerset]
  | cons a l ih =>
      cases hp : p a <;>
        simp [listPowerset, hp, ih]

/-- All vertex-subset lists, generated constructively from the finite carrier. -/
def vertexSubsetLists (n : Nat) : List (List (MaskVertex n)) :=
  listPowerset (List.finRange n)

/-- Source/target-separating vertex lists. -/
def separatingVertexLists
    (n : Nat) (u v : MaskVertex n) : List (List (MaskVertex n)) :=
  (vertexSubsetLists n).filter fun S =>
    decide (u ∈ S ∧ v ∉ S)

/--
Directed non-loop edge-bit indices that leave a concrete vertex list.
This is fully computable and uses only `List` operations.
-/
def crossingEdgeBitList
    (n : Nat) (S : List (MaskVertex n)) : List Nat :=
  (List.finRange n).flatMap fun x =>
    (List.finRange n).filterMap fun y =>
      if x ∈ S ∧ y ∉ S ∧ x ≠ y then
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
  simp [crossingEdgeBitList, eq_comm, and_assoc]

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
    have habsent := (List.all_eq_true.mp hall) _ hmem
    simp [hbit] at habsent
  · intro hclosed
    apply List.all_eq_true.mpr
    intro bit hmem
    rcases (mem_crossingEdgeBitList_iff n bit S).1 hmem with
      ⟨x, y, hx, hy, hxy, rfl⟩
    cases hb : graph.testBit (nonloopEdgeBitIndex n x.val y.val)
    · rfl
    · exfalso
      have hedge : maskRelation n graph x y :=
        (maskRelation_iff_testBit_of_ne n graph hxy).2 hb
      exact hy (hclosed hx hedge)

/-- Precomputed outgoing-edge-bit lists for every source/target-separating subset. -/
def separatorBitLists
    (n : Nat) (u v : MaskVertex n) : List (List Nat) :=
  (separatingVertexLists n u v).map (crossingEdgeBitList n)

/-- Graph test against the precomputed separator bit lists. -/
def noReachWithBitLists (graph : Nat) (families : List (List Nat)) : Bool :=
  families.any (noPresentEdgeBitListBool graph)

/-- A list separator carries the same semantic closure conditions as a set separator. -/
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
    List.any_eq_true
  ]
  constructor
  · rintro ⟨bits, hbits, hnone⟩
    rcases List.mem_map.mp hbits with ⟨S, hSfiltered, rfl⟩
    have hSdata := List.mem_filter.mp hSfiltered
    have hsep : u ∈ S ∧ v ∉ S :=
      of_decide_eq_true hSdata.2
    refine ⟨S, hSdata.1, hsep.1, hsep.2, ?_⟩
    exact (noPresentCrossingEdgeBitListBool_eq_true_iff n graph S).1 hnone
  · rintro ⟨S, hSpow, hu, hv, hclosed⟩
    refine ⟨crossingEdgeBitList n S, ?_, ?_⟩
    · apply List.mem_map.mpr
      refine ⟨S, ?_, rfl⟩
      apply List.mem_filter.mpr
      exact ⟨hSpow, decide_eq_true ⟨hu, hv⟩⟩
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
Every finite-set separator has a canonical executable list presentation,
obtained by filtering the ordered finite carrier.
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
  · exact filter_mem_listPowerset
      (fun x : MaskVertex n => decide (x ∈ T)) (List.finRange n)
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
