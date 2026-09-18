import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact fixed-absent-edge counts for the four non-loop edges sourced at vertex 3. -/
theorem fixedEdgeNoReachFastCountFive_source3 :
    fixedEdgeNoReachFastCountFive 3 0 = 153600 ∧
    fixedEdgeNoReachFastCountFive 3 1 = 153600 ∧
    fixedEdgeNoReachFastCountFive 3 2 = 153600 ∧
    fixedEdgeNoReachFastCountFive 3 4 = 153600 := by
  native_decide

end PrecategoryFormal
