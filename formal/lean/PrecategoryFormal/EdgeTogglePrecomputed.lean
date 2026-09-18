import PrecategoryFormal.EdgeToggleFastSemantic

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Generic checker that no bit in a finite edge-bit set is present in a graph mask. -/
def noPresentEdgeBitsBool (graph : Nat) (bits : Finset Nat) : Bool :=
  decide ((bits.filter fun bit => graph.testBit bit = true).card = 0)

/-- On an actual cut, the generic bit-set checker is definitionally the proved cut checker. -/
theorem noPresentEdgeBitsBool_crossing
    (n graph : Nat) (S : Finset (MaskVertex n)) :
    noPresentEdgeBitsBool graph (crossingEdgeBits n S) =
      noPresentCrossingEdgeBool n graph S := by
  rfl

/--
Precomputed outgoing-edge-bit families for all source/target-separating cuts.
The vertex subsets are discarded after their outgoing bit sets are built.
-/
def separatorBitFamilies
    (n : Nat) (u v : MaskVertex n) : List (Finset Nat) :=
  (separatingFinsets n u v).toList.map (crossingEdgeBits n)

/-- Test a graph against a precomputed family of separating cut edge sets. -/
def noReachWithBitFamilies (graph : Nat) (families : List (Finset Nat)) : Bool :=
  families.any (noPresentEdgeBitsBool graph)

/--
The precomputed family checker accepts exactly when a finite forward-closed
source/target separator exists.
-/
theorem noReachWithBitFamilies_eq_true_iff_exists
    (n graph : Nat) (u v : MaskVertex n) :
    noReachWithBitFamilies graph (separatorBitFamilies n u v) = true ↔
      ∃ S : Finset (MaskVertex n),
        FinsetForwardClosedSeparator n graph u v S := by
  simp only [noReachWithBitFamilies, List.any_eq_true]
  constructor
  · rintro ⟨bits, hbits, hnone⟩
    rcases List.mem_map.mp hbits with ⟨S, hSlist, rfl⟩
    have hSfin : S ∈ separatingFinsets n u v := by
      simpa using hSlist
    have hsep := (Finset.mem_filter.mp hSfin).2
    refine ⟨S, hsep.1, hsep.2, ?_⟩
    have hcross : noPresentCrossingEdgeBool n graph S = true := by
      rw [← noPresentEdgeBitsBool_crossing n graph S]
      exact hnone
    exact (noPresentCrossingEdgeBool_eq_true_iff n graph S).1 hcross
  · rintro ⟨S, hu, hv, hclosed⟩
    refine ⟨crossingEdgeBits n S, ?_, ?_⟩
    · apply List.mem_map.mpr
      refine ⟨S, ?_, rfl⟩
      have hSfin : S ∈ separatingFinsets n u v := by
        apply Finset.mem_filter.mpr
        exact ⟨by simp, hu, hv⟩
      simpa using hSfin
    · rw [noPresentEdgeBitsBool_crossing n graph S]
      exact (noPresentCrossingEdgeBool_eq_true_iff n graph S).2 hclosed

/-- End-to-end semantic correctness of the precomputed checker. -/
theorem noReachWithBitFamilies_eq_true_iff
    (n graph : Nat) (u v : MaskVertex n) :
    noReachWithBitFamilies graph (separatorBitFamilies n u v) = true ↔
      ¬ RelationReach (maskRelation n graph) u v := by
  rw [noReachWithBitFamilies_eq_true_iff_exists]
  exact (not_maskRelationReach_iff_exists_finsetSeparator n graph u v).symm

end PrecategoryFormal
