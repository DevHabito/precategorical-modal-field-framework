import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact compressed fixed-absent-edge counts for the four non-loop edges sourced at vertex 2. -/
theorem fixedEdgeNoReachFastCountFive_source2 :
    fixedEdgeNoReachFastCountFive 2 0 = 153600 ∧
    fixedEdgeNoReachFastCountFive 2 1 = 153600 ∧
    fixedEdgeNoReachFastCountFive 2 3 = 153600 ∧
    fixedEdgeNoReachFastCountFive 2 4 = 153600 := by
  native_decide

/-- Direct full-`2^20`-mask reproduction for the four source-2 edges. -/
theorem fixedEdgeNoReachDirectCountFive_source2 :
    fixedEdgeNoReachDirectCountFive 2 0 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 2 1 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 2 3 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 2 4 = 153600 := by
  native_decide

/-- Direct full-mask subtotal for the four non-loop edges sourced at vertex 2. -/
def fixedEdgeNoReachDirectTotalFive_source2 : Nat :=
  fixedEdgeNoReachDirectCountFive 2 0 +
  fixedEdgeNoReachDirectCountFive 2 1 +
  fixedEdgeNoReachDirectCountFive 2 3 +
  fixedEdgeNoReachDirectCountFive 2 4

/-- Exact source-2 subtotal, derived only from the four direct certificates above. -/
theorem fixedEdgeNoReachDirectTotalFive_source2_exact :
    fixedEdgeNoReachDirectTotalFive_source2 = 614400 := by
  rcases fixedEdgeNoReachDirectCountFive_source2 with ⟨h20, h21, h23, h24⟩
  norm_num [fixedEdgeNoReachDirectTotalFive_source2, h20, h21, h23, h24]

end PrecategoryFormal
