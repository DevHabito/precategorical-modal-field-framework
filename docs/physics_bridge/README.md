# Physical Bridge Pilot

## Canonical current summary

Start with **PHYSICAL_BRIDGE_V1_SYNTHESIS_20261111.md**. It consolidates the current physical-bridge claims, corrections, classical identifications, formal-verification status, and empirical boundary. The other files in this directory are component proofs, audits, preregistrations, or provenance notes.

This directory records a controlled attempt to connect the repository's provisional informational architecture

$$
(R,q,\mu,K,\pi)
$$

to established physical models.

The purpose is not to declare a physical interpretation for the framework. The question is narrower:

> In a physical system whose variables already have accepted operational meanings, which roles are independently observable, which are derivable from other roles, which are representation-dependent, and which remain necessary?

## Files

- **MARKOV_THERMAL_PILOT_20261111.md** — exact three-state diagnostic, reduction tests, and failure criteria.
- **markov_thermal_pilot_exact.py** — dependency-free exact audit for the three-state pilot.
- **markov_thermal_pilot_results.json** — frozen exact output.
- **SINGLE_ELECTRON_BOX_CALIBRATION_20261111.md** — retrospective calibration against the 2012 single-electron-box experiment.
- **single_electron_box_mapping_exact.py** — exact event-level mapping audit.
- **MULTIELECTRON_DOT_TRANSFORM_NONCLOSURE_20261111.md** — exact transform-evolution bridge derived from the published 2026 multi-electron master equation.
- **MULTIELECTRON_SCALAR_CLOSURE_PREREGISTRATION_20261111.md** — frozen held-out protocol for \(\lambda=c\), \(2c\), and the noncommensurate control \(3c/2\).
- **EXPONENTIAL_OBSERVABLE_CLOSURE_CLASSIFICATION_20261111.md** — necessity, sufficiency, and minimality of finite pure-exponential closures, plus the stationary score identity.
- **OBSERVABLE_SELECTIVE_CLOSURE_20261111.md** — exact comparison showing mean nonclosure versus scalar closure of the physically tuned exponential transform.
- **observable_selective_closure_exact.py** — rational three-state nonclosure audit.
- **multielectron_transform_nonclosure_exact.py** — exact four-state witness.
- **multielectron_transform_nonclosure_results.json** — frozen witness output.
- **multielectron_commensurate_closure_exact.py** — exact rational audit of the commensurate transform ladder.
- **multielectron_commensurate_closure_results.json** — frozen closure-audit output.
- **multielectron_stationary_transform_consistency_exact.py** — rational check that the stationary Gaussian and triangular hierarchy give the same transforms.
- **multielectron_stationary_transform_consistency_results.json** — frozen stationary-consistency output.
- **PHYSICAL_BRIDGE_LEDGER.md** — evidence/status ledger kept separate from mathematical claims.
- **NEXT_SYSTEM_SELECTION_20261111.md** — target-selection and reproducibility status.
- **LITERATURE_MAP_20261111.md** — literature boundary for stochastic thermodynamics, birth-death transforms, and closure.
- **CLASSICAL_DISCRETE_NORMAL_AND_STEIN_CONTEXT_20261111.md** — adversarial prior-art note identifying the stationary discrete-normal law, Stein-generator context, and the nearby alternative q-Charlier process.
- **STIELTJES_WIGERT_IDENTIFICATION_20261111.md** — exact change of variables showing that the constant-rate bridge generator is the classical Stieltjes-Wigert q-difference operator minus the identity.
- **DATA_REQUEST_SPECIFICATION_20261111.md** — exact numerical data and metadata needed to execute the corrected experimental test without figure digitization.
- **DATA_REQUEST_EMAIL_DRAFT_20261111.md** — concise draft request for the original numerical data; repository draft only, not sent.
- **OPEN_DATA_TARGET_SURVEY_20261111.md** — public-data search and reasons not to substitute a different experiment merely for convenience.
- **PHASE_AVERAGING_CLOSURE_OBSTRUCTION_20261111.md** — exact correction showing that random-phase marginalization introduces a rate-transform covariance and destroys generic scalar closure.
- **FLOQUET_STROBOSCOPIC_CLOSURE_20261111.md** — exact Floquet multipliers and phase-averaged stroboscopic recurrences that recover finite closure at integer drive periods.
- **HIDDEN_PHASE_FOURIER_HIERARCHY_20261111.md** — exact lifted phase equation showing that continuous-time marginalization generates an infinite Fourier hierarchy for nonzero drive.
- **PROTOCOL_MARGINALIZATION_CLOSURE_LEMMAS_20261111.md** — reusable classical lemmas separating continuous marginal nonclosure from stroboscopic recurrence closure.
- **UNIVERSAL_MARGINAL_CLOSURE_CRITERIA_20261111.md** — necessary-and-sufficient continuous and stroboscopic closure criteria for hidden-context linear systems.
- **PERSISTENT_VS_RESAMPLED_CONTEXT_20261111.md** — exact diagnostic showing how persistence of an external context changes ensemble dynamics even when its one-time distribution is unchanged.
- **BRIDGE_2_HIDDEN_DEGREES_RETROSPECTIVE_20261111.md** — independent Nature Physics control case: matched visible initial distributions with different future relaxation because of hidden environmental memory.
- **PHYSICAL_ARCHITECTURE_REFINEMENT_20261111.md** — governance refinement requiring every closure claim to declare full state, observation map, conditioning information, preparation class, and temporal resolution.
- **INFORMATION_THEORETIC_CLOSURE_DIAGNOSTIC_20261111.md** — uses established conditional mutual information to separate preparation-specific predictive sufficiency from universal/strong closure.
- **PREGEOMETRIC_TIME_ANTI_CIRCULARITY_GATE_20261111.md** — hard gate preventing memory or relaxation results that already assume time from being promoted as evidence that time emerges.
- **BLACKWELL_TIME_CANDIDATE_AUDIT_20261111.md** — first timeless-order candidate audit; rejects information degradation as a universal temporal order while retaining Blackwell comparison as a diagnostic.
- **OBSERVATIONAL_CAUSAL_ORDER_AUDIT_20261111.md** — second timeless-order audit; Markov equivalence blocks unique direction from observational conditional independences alone.
- **SCC_CONDENSATION_MACRO_ORDER_AUDIT_20261111.md** — connects the repository's SCC/quotient mathematics to a canonical acyclic macro-order while documenting its non-injectivity and failure as universal time.
- **STRICT_TIME_AND_DURATION_GATE_20261111.md** — proves the acyclicity requirement for strict temporal rank and separates relational order from metric duration/refinement scale.
- **PAGE_WOOTTERS_RELATIONAL_TIME_BENCHMARK_20261111.md** — classical reversible relational-time benchmark showing that external noise is not a necessary condition for relational temporal description.
- **ORDERABILITY_BEFORE_ORDER_GATE_20261111.md** — corrects the pregeometric milestone: test whether definite causal order is available before trying to derive one; benchmarks process matrices and indefinite causal order.
- **page_wootters_finite_benchmark.py** — finite periodic-clock regression for dimensions 2, 3, 4, 5, and 8.
- **page_wootters_finite_benchmark_results.json** — frozen numerical output of that classical benchmark.
- **stroboscopic_phase_average_exact.py** — rational regression audit of the phase-averaged Cayley-Hamilton recurrences.
- **phase_bridge_numerical_stress.py** — dependency-free 16-case integration stress test of continuous phase averaging versus exact stroboscopic closure.
- **phase_bridge_numerical_stress_results.json** — frozen output of that numerical regression.

## Scientific rule

No new physical variable or equation is introduced unless at least one of the following requires it:

1. an exact obstruction;
2. a symmetry or conservation law;
3. an operational measurement requirement;
4. incompatibility with an established physical limit;
5. prospective data that cannot be described without the additional structure.

A successful fit is not enough. Every proposed bridge must also state what would make it fail.

## Current status

The first exact pilot reduces the provisional architecture rather than confirming all of it:

- \(R\) can be redundant with the support of \(K\);
- a scalar potential-like \(q\) can be reconstructed from rate ratios only in a cycle-consistent sector;
- equilibrium occupancy may be derived from \(K\);
- current/transient occupancy can remain additional state information;
- coarse-grained rates can depend on occupancy;
- energy-like \(q\) and degeneracy-like \(\mu\) need not be separately identifiable.

Bridge 1A shows that a real two-state electronic experiment admits a non-circular operational mapping, but it cannot test C2.

Bridge 1B derives from a published multi-electron master equation an exact transform shift: one exponential transform generally couples to another transform at a shifted parameter. A four-state exact witness exposes the resulting closure problem. The same identity also reveals an exact positive result: at transform parameters \(\lambda=mc\), with \(c=2\beta E_{\rm C}\), the natural hierarchy closes after \(m\) levels; \(\lambda=c\) gives scalar closure.

This is still an analytic bridge. Raw experimental data for the 2026 system are not publicly available, so no empirical validation is claimed.

No spacetime, gravity, quantum-gravity, or ontological conclusion follows from the present bridge.
