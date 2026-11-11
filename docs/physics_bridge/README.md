# Physical Bridge Pilot

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
- **multielectron_transform_nonclosure_exact.py** — exact four-state witness.
- **multielectron_transform_nonclosure_results.json** — frozen witness output.
- **multielectron_commensurate_closure_exact.py** — exact rational audit of the commensurate transform ladder.
- **multielectron_commensurate_closure_results.json** — frozen closure-audit output.
- **PHYSICAL_BRIDGE_LEDGER.md** — evidence/status ledger kept separate from mathematical claims.
- **NEXT_SYSTEM_SELECTION_20261111.md** — target-selection and reproducibility status.
- **LITERATURE_MAP_20261111.md** — literature boundary for stochastic thermodynamics, birth-death transforms, and closure.

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
