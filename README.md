# Pre-Categorical Research Archive

**Author:** Felipe Gianini Romero (Felipe G. Romero)  
**Repository status:** mathematical/computational research archive under active consolidation.  
**Physical status:** no confirmed fundamental physical theory is claimed.

## Start here

The canonical reader entry point is now:

**[`consolidation/README.md`](consolidation/README.md)**

That page separates the repository into three logically distinct layers:

1. mathematical claims;
2. verification/reproducibility;
3. historical and speculative interpretation.

The chronological A-number sequence remains preserved for provenance, but it is no longer the preferred way to understand or review the work.

## Current mathematical core under consolidation

The strongest material is being compressed into a small number of self-contained result groups:

- finite combinatorics and encoding correction, including MF-R008/MF-R009/MF-R011;
- exact dynamic non-closure, MF-R049;
- frozen exponential-moment optimization, A112/A113, with A114 kept as a separate lifted layer pending governance normalization;
- target-deformed central nesting and boundary-layer results, A115-A119;
- fixed-interior rounding-phase staircase and resonance, A120-A122.

See [`consolidation/CORE_RESULTS_MAP.md`](consolidation/CORE_RESULTS_MAP.md) for scope and status. Novelty/priority is not inferred from mathematical correctness and remains conservative unless separately reviewed.

## Verification policy

The project distinguishes:

- deductive proof;
- exact finite enumeration;
- constructive counterexample;
- rigorous computer-assisted certificate;
- finite numerical/regression evidence;
- open conjecture.

A passed script is not automatically a theorem. A theorem verified from assumptions is not automatically a statement about nature.

Selected claims are now being prepared for independent Lean 4 formalization; see [`consolidation/FORMALIZATION_PLAN.md`](consolidation/FORMALIZATION_PLAN.md).

## Historical archive

The cumulative directories

- `MFRP_Informational_Requirements_A39-A71/`
- `MFRP_Informational_Requirements_A39-A77/`
- `MFRP_Informational_Requirements_A39-A106/`
- `MFRP_Informational_Requirements_A39-A109/`

are historical/provenance snapshots, not four competing canonical versions. They remain untouched during the first cleanup phase. The migration plan is documented in [`consolidation/ARCHIVE_PLAN.md`](consolidation/ARCHIVE_PLAN.md); redundant snapshots will only leave the default branch after equivalent Git tags/releases and migration links exist.

## Existing documentation

The repository still preserves detailed claim matrices, literature audits, manuscripts, protocols, exact scripts, failed routes, corrections, integrity manifests, and chronological research updates. In particular:

- `docs/RESULT_CLASSIFICATION.md` — claim-level evidence/wording matrix;
- `docs/SCIENTIFIC_STATUS.md` — scientific boundary and nonclaims;
- `docs/novelty/` — literature and novelty positioning;
- `manuscripts/` — manuscript work and claim maps;
- `protocols/` and `audits/` — reproducibility material;
- `MFRP_Informational_Requirements_A39-A109/research_updates/` — chronological A107-A122 development.

## Scientific boundary

The repository does **not** currently derive or empirically confirm physical spacetime, calibrated physical duration or distance, curvature, gravity, matter, quantum amplitudes, or a physical interpretation of the project variables. RZS/Modal Field language is historical or conjectural unless an explicit mathematical/empirical bridge is separately supplied.

## Consolidation freeze

During Consolidation 1.0, new chronological A-number packages are paused except when required to repair a contradiction or close an independent verification gap. The priority is compression, assumption minimization, formal verification, and short externally reviewable theorem units.

## Citation and license

Please cite the repository release and the specific theorem/audit/manuscript used. Software is licensed under Apache-2.0. Scientific content, documentation, figures, tables, CSV/JSON results, and reports are licensed under CC BY 4.0. See `LICENSE.md`, `NOTICE`, and `LICENSES/`.
