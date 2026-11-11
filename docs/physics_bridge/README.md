# Physical Bridge Pilot

This directory begins a controlled attempt to connect the repository's provisional informational architecture

[
(R,q,mu,K,pi)
]

to established physical models.

The purpose is not to declare a physical interpretation for the framework. The purpose is to ask a narrower question:

> In a physical system whose variables already have an accepted operational meaning, which parts of ((R,q,mu,K,pi)) are independently observable, which can be derived from other parts, which are representation-dependent, and which remain necessary?

The first test bed is a finite continuous-time Markov jump process in stochastic thermodynamics.

## Files

- `MARKOV_THERMAL_PILOT_20261111.md` — statement of the physical pilot, exact calculations, interpretation, failure modes, and next tests.
- `LITERATURE_MAP_20261111.md` — literature used to keep the bridge inside established stochastic thermodynamics.
- `markov_thermal_pilot_exact.py` — dependency-free exact arithmetic audit.
- `markov_thermal_pilot_results.json` — frozen output of the exact audit.
- `PHYSICAL_BRIDGE_LEDGER.md` — separate status ledger for exact diagnostics, classical mappings, and open physical hypotheses.

## Scientific rule

No new physical variable or equation is introduced in this bridge unless at least one of the following requires it:

1. an exact obstruction;
2. a symmetry or conservation law;
3. an operational measurement requirement;
4. incompatibility with an established physical limit;
5. prospective data that cannot be described without the additional structure.

A successful fit is not enough. Every proposed bridge must also state what would make it fail.

## Current status

This pilot is a **diagnostic bridge**, not an empirical validation.

The exact model shows that, in a reversible thermal Markov sector:

- the relational graph (R) is recoverable from the support of (K);
- a scalar free-energy-like potential can be reconstructed from rate ratios only when the cycle consistency condition holds;
- the equilibrium occupancy is determined by the reversible generator;
- transient or externally prepared occupancy remains additional state information;
- coarse-grained transition rates can depend on that occupancy;
- an energy-like mark and a degeneracy measure need not be separately identifiable from equilibrium weights.

The nonequilibrium perturbation deliberately breaks the cycle condition. The failure is useful: it shows that a single state scalar cannot encode arbitrary nonequilibrium thermodynamic driving.

No spacetime, gravity, quantum, or ontological claim follows from this pilot.
