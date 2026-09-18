import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact compressed fixed-absent-edge counts for the four non-loop edges sourced at vertex 1. -/
theorem fixedEdgeNoReachFastCountFive_source1 :
    fixedEdgeNoReachFastCountFive 1 0 = 153600 ∧
    fixedEdgeNoReachFastCountFive 1 2 = 153600 ∧
    fixedEdgeNoReachFastCountFive 1 3 = 153600 ∧
    fixedEdgeNoReachFastCountFive 1 4 = 153600 := by
  native_decide

/-- Direct full-`2^20`-mask reproduction for the four source-1 edges. -/
theorem fixedEdgeNoReachDirectCountFive_source1 :
    fixedEdgeNoReachDirectCountFive 1 0 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 1 2 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 1 3 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 1 4 = 153600 := by
  native_decide

/-- Direct full-mask subtotal for the four non-loop edges sourced at vertex 1. -/
def fixedEdgeNoReachDirectTotalFive_source1 : Nat :=
  fixedEdgeNoReachDirectCountFive 1 0 +
  fixedEdgeNoReachDirectCountFive 1 2 +
  fixedEdgeNoReachDirectCountFive 1 3 +
  fixedEdgeNoReachDirectCountFive 1 4

/-- Exact source-1 subtotal, derived only from the four direct certificates above. -/
theorem fixedEdgeNoReachDirectTotalFive_source1_exact :
    fixedEdgeNoReachDirectTotalFive_source1 = 614400 := by
  rcases fixedEdgeNoReachDirectCountFive_source1 with ⟨h10, h12, h13, h14⟩
  norm_num [fixedEdgeNoReachDirectTotalFive_source1, h10, h12, h13, h14]

end PrecategoryFormal
