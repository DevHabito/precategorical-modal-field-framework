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

/--
Direct full-`2^20`-mask reproduction for the same four source-0 edges.
These counts do not use `insertZeroBit`.
-/
theorem fixedEdgeNoReachDirectCountFive_source0 :
    fixedEdgeNoReachDirectCountFive 0 1 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 0 2 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 0 3 = 153600 ∧
    fixedEdgeNoReachDirectCountFive 0 4 = 153600 := by
  native_decide

end PrecategoryFormal
