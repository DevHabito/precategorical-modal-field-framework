# A113 experimental Lean build gate — 2026-11-03

**Author:** Felipe Gianini Romero
**Branch:** \`research/2026-11-03-a113-evidence-ledger\`
**Status before CI:** Lean module sourced from a previously recorded, **uncompiled** candidate. No success is claimed in advance of the exact-head workflow result.

I copied the existing experimental proof from \`consolidation/candidates/A113SmallLeftClosure.candidate.lean\` into the Lean library under \`formal/lean/PrecategoryFormal/A113SmallLeftClosure.lean\` and added an import to the Lean root, on the dedicated research branch only. The canonical \`main\` and historical files are unchanged.

The goal is to expose actual Lean elaboration, tactic and dependency failures. The repository's original pinned \`leanprover/lean4:v4.33.1\` and mathlib manifest remain unchanged.

A branch-scoped review workflow in \`.github/workflows/a113-small-left-review.yml\` asks for a pinned \`lake build\`, an explicit \`sorry\`/\`admit\` rejection gate, theorem axiom traces and a module-specific \`leanchecker\` run. The two new theorem names are:

- \`PrecategoryFormal.a113ActualFactor_abs_error_lt_twenty_units\`
- \`PrecategoryFormal.a113ActualFactor_smallLeft_pos\`

The file \`formal/lean/AssuranceA113SmallLeftClosure.lean\` prints their transitive axiom dependencies.

**The presence of a workflow file is not evidence it ran or succeeded.** If the GitHub runner is unavailable or requires approval, the validation remains blocked. If any proof fails to elaborate, the failure is a legitimate result and must be kept; adjusting hypotheses or replacing real algebra with an unsupported computation is not an acceptable fix.

Source provenance and exact independent Python regressions remain in \`consolidation/A113_SMALL_LEFT_CLOSURE_CHECKPOINT_2026-11-03.md\` and \`tools/research_2026_11_03/\`.

### Merge gates

1. Run and inspect the pinned workflow for the **exact commit containing this module**.
2. Check the actual outputs of \`#print axioms\`, not merely the command's presence.
3. Run dedicated \`leanchecker\` and the complete previously declared formal module matrix.
4. Independently check that the formal A83/A84 definitions match the mathematical source, with both parity branches.
5. Refresh and check the root tracked-file integrity indexes on the final tree; preserve the known historical ZIP audit failures.
6. Obtain independent mathematical and bibliography review before upgrading theorem or originality labels.

This is scoped to the frozen small-left sector. It is not a proof of the full A113 theorem, lifted KKT conclusions, or a physical interpretation.
