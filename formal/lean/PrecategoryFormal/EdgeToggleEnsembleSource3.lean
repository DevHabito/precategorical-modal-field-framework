import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact compressed fixed-absent-edge counts for the four non-loop edges sourced at vertex 3. -/
theorem fixedEdgeNoReachFastCountFive_source3 :
    fixedEdgeNoReachFastCountFive 3 0 = 153600 ∧
    fixedEdgeNoReachFastCountFive 3 1 = 153600 ∧
    fixedEdgeNoReachFastCountFive 3 2 = 153600 ∧
    fixedEdgeNoReachFastCountFive 3 4 = 153600 := by
  native_decide

/-- Direct full-`2^20`-mask reproduction for the four source-3 edges. -/
theorem fixedEdgeNoReachDirectCountFive_source3 :
    fixedEdgeNoReachDirectCountFive 3 0 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 3 1 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 3 2 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 3 4 = 153600 := by
  native_decide

/-- Direct full-mask subtotal for the four non-loop edges sourced at vertex 3. -/
def fixedEdgeNoReachDirectTotalFive_source3 : Nat :=
  fixedEdgeNoReachDirectCountFive 3 0 +
  fixedEdgeNoReachDirectCountFive 3 1 +
  fixedEdgeNoReachDirectCountFive 3 2 +
  fixedEdgeNoReachDirectCountFive 3 4

/-- Exact source-3 subtotal, derived only from the four direct certificates above. -/
theorem fixedEdgeNoReachDirectTotalFive_source3_exact :
    fixedEdgeNoReachDirectTotalFive_source3 = 614400 := by
  rcases fixedEdgeNoReachDirectCountFive_source3 with ⟨h30, h31, h32, h34⟩
  norm_num [fixedEdgeNoReachDirectTotalFive_source3, h30, h31, h32, h34]

end PrecategoryFormal
