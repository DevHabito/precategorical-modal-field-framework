# Lean 4 theorem-level axiom trace — 2026-10-19

**Scope:** nine selected theorems from the frozen Consolidation 1.0 Lean project.  
**Toolchain:** pinned Lean 4.33.1; mathlib 4.33.1.  
**Provenance:** GitHub Actions [Lean formal verification run 39334714446](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39334714446), job 118341180916; successful `lake build` and `lake env lean AssuranceAxioms.lean` commands.

This table is transcribed programmatically from the emitted `#print axioms` trace. Counts are distinct **named native axioms within each theorem's transitive dependencies**, not a count of independent mathematical assumptions and not a count of all library axioms.

| Theorem | Native axioms | Assurance boundary |
|---|---:|---|
| `PrecategoryFormal.encodedPosetCount_five` | 1 | Native trust dependency |
| `PrecategoryFormal.representativeCodeCount_five_verified` | 1 | Native trust dependency |
| `PrecategoryFormal.natCard_literalRepresentativeCode_five` | 1 | Native trust dependency |
| `PrecategoryFormal.historicalRepresentativeCode_not_injective` | 4 | Native trust dependency |
| `PrecategoryFormal.mf_r009_graph_level_code_collision` | 66 | Native trust dependency |
| `PrecategoryFormal.changedPairCount_five` | 1 | Native trust dependency |
| `PrecategoryFormal.edgeToggleProbability_five_crossmul` | 2 | Native trust dependency |
| `PrecategoryFormal.reachCode_eq_iff_sameReachability5` | 1 | Native trust dependency |
| `PrecategoryFormal.addDirectedEdge_preserves_reachability_iff` | 0 | No axioms reported |

**Final verification update:** the same workflow run completed with **16/16 successful jobs**: one pinned Lean compilation/axiom-trace job and all 15 separately sharded `leanchecker` module jobs. This verifies replay of the submitted proof terms under their disclosed axioms; it does not remove the native-computation trust boundary.

The trace exposed 77 theorem-by-theorem appearances of native axiom names across these nine declarations; some are reused between theorems, so this total must **not** be read as a unique axiom count.

For the theorems with non-native axioms, the only other printed names were Lean's standard `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx` was observed in any of these nine outputs. This does not prove that every declaration in the entire project has been audited.

## Follow-up F3: exact dynamic nonclosure

At code revision `fb34f319aa4cb664b202e37068590e218e5c0376`,
the pinned Lean 4.33.1
[workflow run 39337980598](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/39337980598)
compiled both new F3 modules and printed the axiom dependencies
for five representative statements.

| New declaration | Native axioms | Other axiom dependencies |
|---|---:|---|
| `PrecategoryFormal.rationalMoment_difference` | 0 | `propext`, `Classical.choice`, `Quot.sound` |
| `PrecategoryFormal.rationalInitialDataAgree` | 0 | `propext`, `Classical.choice`, `Quot.sound` |
| `PrecategoryFormal.rationalRescaledMomentsDiffer` | 0 | `propext`, `Classical.choice`, `Quot.sound` |
| `PrecategoryFormal.affineFourExponentialMoment_factorization` | 0 | `propext`, `Classical.choice`, `Quot.sound` |
| `PrecategoryFormal.rationalScalarNonclosure` | 0 | `propext`, `Classical.choice`, `Quot.sound` |

The final workflow attempt completed **18/18 jobs successfully** after
rerunning two unrelated module jobs that originally failed while fetching
Lean from the distribution server (TLS connection failures). Neither
failure was in a proof term and no mathematics was changed to resolve them.

The `rationalScalarNonclosure` theorem asserts **equal initial mass,
mean and entropic score, but unequal next score** for an explicit pair of
strictly positive normalized four-point distributions. Its analytic bridge
defines the actual exponential sum of the affine-shifted support and proves
the factorization from `Real.exp_add`.

Unlike the earlier finite C1 enumerations, the F3 formalization depends
on no `native_decide` axioms. This stronger proof-assurance label applies
to the **declared F3 existence theorem only**, not all research claims.

## Interpretation

A Lean theorem can be accepted while relying on explicitly tracked native computation axioms. In Lean 4.33.1, `native_decide` places the evaluated finite calculation within the trusted native compiler rather than the small Lean kernel alone. A successful checker replay therefore does not erase those native axioms.

In particular, the mathematical conclusion `P5 = 75/256` is corroborated by independent exact integer enumeration, but its current *Lean evaluation proof* retains native trust. This is not evidence that the value is false. To claim a native-axiom-free proof of the finite result, a different kernel-reduced or mathematically deductive proof would be required.

The generic edge-addition reachability theorem has no axioms reported in this trace, unlike the finite counts. Keep that difference visible in the claim ledger.

**Remaining work:** audit all promoted Lean declarations, run the full checker matrix, independently verify statement-to-intended-semantics matching, and retain the exact printed trace. Axiom auditing does not by itself verify novelty, soundness of scientific assumptions, or physical relevance.

Official Lean reference: https://lean-lang.org/doc/reference/latest/ValidatingProofs/
