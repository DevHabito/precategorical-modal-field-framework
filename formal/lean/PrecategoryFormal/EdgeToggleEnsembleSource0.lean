import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact compressed fixed-absent-edge counts for the four non-loop edges sourced at vertex 0. -/
theorem fixedEdgeNoReachFastCountFive_source0 :
    fixedEdgeNoReachFastCountFive 0 1 = 153600 ∧
    fixedEdgeNoReachFastCountFive 0 2 = 153600 ∧
    fixedEdgeNoReachFastCountFive 0 3 = 153600 ∧
    fixedEdgeNoReachFastCountFive 0 4 = 153600 := by
  native_decide

/-- Direct full-`2^20`-mask reproduction for the same four source-0 edges. -/
theorem fixedEdgeNoReachDirectCountFive_source0 :
    fixedEdgeNoReachDirectCountFive 0 1 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 0 2 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 0 3 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 0 4 = 153600 := by
  native_decide

/-- Direct full-mask subtotal for the four non-loop edges sourced at vertex 0. -/
def fixedEdgeNoReachDirectTotalFive_source0 : Nat :=
  fixedEdgeNoReachDirectCountFive 0 1 +
  fixedEdgeNoReachDirectCountFive 0 2 +
  fixedEdgeNoReachDirectCountFive 0 3 +
  fixedEdgeNoReachDirectCountFive 0 4

/-- Exact source-0 subtotal, derived only from the four direct certificates above. -/
theorem fixedEdgeNoReachDirectTotalFive_source0_exact :
    fixedEdgeNoReachDirectTotalFive_source0 = 614400 := by
  rcases fixedEdgeNoReachDirectCountFive_source0 with ⟨h01, h02, h03, h04⟩
  norm_num [fixedEdgeNoReachDirectTotalFive_source0, h01, h02, h03, h04]

end PrecategoryFormal
