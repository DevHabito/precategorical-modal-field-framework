import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact fixed-absent-edge counts for the four non-loop edges sourced at vertex 0. -/
theorem fixedEdgeNoReachFastCountFive_source0 :
    fixedEdgeNoReachFastCountFive 0 1 = 153600 ∧
    fixedEdgeNoReachFastCountFive 0 2 = 153600 ∧
    fixedEdgeNoReachFastCountFive 0 3 = 153600 ∧
    fixedEdgeNoReachFastCountFive 0 4 = 153600 := by
  native_decide

end PrecategoryFormal
