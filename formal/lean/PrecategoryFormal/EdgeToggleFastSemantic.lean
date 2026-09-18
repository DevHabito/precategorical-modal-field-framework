import PrecategoryFormal.EdgeToggleBridge

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Ordered non-loop vertex pairs that leave a concrete finite subset. -/
def crossingPairs
    (n : Nat) (S : Finset (MaskVertex n)) :
    Finset (MaskVertex n × MaskVertex n) :=
  ((Finset.univ : Finset (MaskVertex n)).product
      (Finset.univ : Finset (MaskVertex n))).filter fun xy =>
    xy.1 ∈ S ∧ xy.2 ∉ S ∧ xy.1 ≠ xy.2

/-- Bit positions of all directed non-loop edges leaving `S`. -/
def crossingEdgeBits
    (n : Nat) (S : Finset (MaskVertex n)) : Finset Nat :=
  (crossingPairs n S).image fun xy =>
    nonloopEdgeBitIndex n xy.1.val xy.2.val

/-- A mask-relation edge between distinct finite vertices is exactly its graph bit. -/
theorem maskRelation_iff_testBit_of_ne
    (n graph : Nat) {x y : MaskVertex n} (hxy : x ≠ y) :
    maskRelation n graph x y ↔
      graph.testBit (nonloopEdgeBitIndex n x.val y.val) = true := by
  have hval : x.val ≠ y.val := by
    intro h
    apply hxy
    exact Fin.ext h
  simp [maskRelation, maskHasDirectedEdge, x.isLt, y.isLt, hval]

/-- A concrete crossing pair contributes its row-major edge bit. -/
theorem edgeBit_mem_crossingEdgeBits
    (n : Nat) (S : Finset (MaskVertex n))
    {x y : MaskVertex n}
    (hx : x ∈ S) (hy : y ∉ S) (hxy : x ≠ y) :
    nonloopEdgeBitIndex n x.val y.val ∈ crossingEdgeBits n S := by
  apply Finset.mem_image.mpr
  refine ⟨(x, y), ?_, rfl⟩
  apply Finset.mem_filter.mpr
  exact ⟨by simp, hx, hy, hxy⟩

/-- Crossing edge bits that are actually present in the graph. -/
def presentCrossingEdgeBits
    (n graph : Nat) (S : Finset (MaskVertex n)) : Finset Nat :=
  (crossingEdgeBits n S).filter fun bit => graph.testBit bit = true

/--
There is no present crossing-edge bit exactly when `S` is forward closed
for the mathematical mask relation.
-/
theorem presentCrossingEdgeBits_card_eq_zero_iff
    (n graph : Nat) (S : Finset (MaskVertex n)) :
    (presentCrossingEdgeBits n graph S).card = 0 ↔
      ∀ ⦃x y : MaskVertex n⦄, x ∈ S → maskRelation n graph x y → y ∈ S := by
  rw [Finset.card_eq_zero]
  constructor
  · intro hempty x y hx hedge
    by_contra hy
    have hxy : x ≠ y := by
      intro h
      subst y
      exact hy hx
    have hbit :
        graph.testBit (nonloopEdgeBitIndex n x.val y.val) = true :=
      (maskRelation_iff_testBit_of_ne n graph hxy).1 hedge
    have hmem :
        nonloopEdgeBitIndex n x.val y.val ∈
          presentCrossingEdgeBits n graph S := by
      apply Finset.mem_filter.mpr
      exact ⟨edgeBit_mem_crossingEdgeBits n S hx hy hxy, hbit⟩
    rw [hempty] at hmem
    simp at hmem
  · intro hclosed
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro bit hmem
    have hfiltered := Finset.mem_filter.mp hmem
    rcases Finset.mem_image.mp hfiltered.1 with ⟨xy, hpair, rfl⟩
    have hcross := (Finset.mem_filter.mp hpair).2
    rcases hcross with ⟨hx, hy, hxy⟩
    have hedge : maskRelation n graph xy.1 xy.2 :=
      (maskRelation_iff_testBit_of_ne n graph hxy).2 hfiltered.2
    exact hy (hclosed hx hedge)

/-- Fast, constructive forward-closure checker using only the crossing edge bits. -/
def noPresentCrossingEdgeBool
    (n graph : Nat) (S : Finset (MaskVertex n)) : Bool :=
  decide ((presentCrossingEdgeBits n graph S).card = 0)

/-- The fast bit-list checker is semantically exact. -/
theorem noPresentCrossingEdgeBool_eq_true_iff
    (n graph : Nat) (S : Finset (MaskVertex n)) :
    noPresentCrossingEdgeBool n graph S = true ↔
      ∀ ⦃x y : MaskVertex n⦄, x ∈ S → maskRelation n graph x y → y ∈ S := by
  simp only [noPresentCrossingEdgeBool, decide_eq_true_eq]
  exact presentCrossingEdgeBits_card_eq_zero_iff n graph S

/-- Source/target-separating finite subsets. -/
def separatingFinsets
    (n : Nat) (u v : MaskVertex n) : Finset (Finset (MaskVertex n)) :=
  ((Finset.univ : Finset (MaskVertex n)).powerset).filter fun S =>
    u ∈ S ∧ v ∉ S

/-- Separators accepted by the fast crossing-edge checker. -/
def acceptedEdgeBitSeparators
    (n graph : Nat) (u v : MaskVertex n) :
    Finset (Finset (MaskVertex n)) :=
  (separatingFinsets n u v).filter fun S =>
    noPresentCrossingEdgeBool n graph S = true

/-- Fast semantic non-reachability checker. -/
def noReachEdgeBitBool
    (n graph : Nat) (u v : MaskVertex n) : Bool :=
  decide (0 < (acceptedEdgeBitSeparators n graph u v).card)

/-- The fast checker accepts exactly the finite forward-closed separators. -/
theorem noReachEdgeBitBool_eq_true_iff_exists
    (n graph : Nat) (u v : MaskVertex n) :
    noReachEdgeBitBool n graph u v = true ↔
      ∃ S : Finset (MaskVertex n),
        FinsetForwardClosedSeparator n graph u v S := by
  rw [show noReachEdgeBitBool n graph u v = true ↔
      0 < (acceptedEdgeBitSeparators n graph u v).card by
        simp [noReachEdgeBitBool]]
  rw [Finset.card_pos]
  constructor
  · rintro ⟨S, hS⟩
    have haccepted := Finset.mem_filter.mp hS
    have hsep := Finset.mem_filter.mp haccepted.1
    refine ⟨S, hsep.2.1, hsep.2.2, ?_⟩
    exact (noPresentCrossingEdgeBool_eq_true_iff n graph S).1 haccepted.2
  · rintro ⟨S, hu, hv, hclosed⟩
    refine ⟨S, ?_⟩
    apply Finset.mem_filter.mpr
    constructor
    · apply Finset.mem_filter.mpr
      exact ⟨by simp, hu, hv⟩
    · exact (noPresentCrossingEdgeBool_eq_true_iff n graph S).2 hclosed

/-- End-to-end semantic correctness of the fast non-reachability checker. -/
theorem noReachEdgeBitBool_eq_true_iff
    (n graph : Nat) (u v : MaskVertex n) :
    noReachEdgeBitBool n graph u v = true ↔
      ¬ RelationReach (maskRelation n graph) u v := by
  rw [noReachEdgeBitBool_eq_true_iff_exists]
  exact (not_maskRelationReach_iff_exists_finsetSeparator n graph u v).symm

end PrecategoryFormal
