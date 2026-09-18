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

end PrecategoryFormal
