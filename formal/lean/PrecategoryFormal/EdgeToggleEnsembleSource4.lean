import PrecategoryFormal.EdgeToggleEnsembleCore

set_option autoImplicit false
set_option warningAsError true

namespace PrecategoryFormal

/-- Exact fixed-absent-edge counts for the four non-loop edges sourced at vertex 4. -/
theorem fixedEdgeNoReachFastCountFive_source4 :
    fixedEdgeNoReachFastCountFive 4 0 = 153600 ∧
    fixedEdgeNoReachFastCountFive 4 1 = 153600 ∧
    fixedEdgeNoReachFastCountFive 4 2 = 153600 ∧
    fixedEdgeNoReachFastCountFive 4 3 = 153600 := by
  native_decide

end PrecategoryFormal
