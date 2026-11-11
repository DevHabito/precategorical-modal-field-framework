# Physical Bridge Ledger

**Date:** 2026-11-11  
**Purpose:** keep physical mappings, exact diagnostics, and empirical claims separate.

This ledger does not promote any item into the repository's mathematical `CLAIM_LEDGER.md`. It tracks a different question: whether the provisional informational roles survive contact with established physical models.

| ID | Statement | Status | Evidence | Physical meaning | Next obligation |
|---|---|---|---|---|---|
| PB-M1 | In the declared CTMC representation, (R) is the support graph of positive transition rates in (K). | EXACT DEFINITIONAL MAPPING | direct definition | (R) is redundant if (K) is already primitive | test models where admissibility exists before rates are specified |
| PB-M2 | In the reversible three-state pilot, rate ratios reconstruct (q)-differences up to an additive constant. | EXACT DIAGNOSTIC; CLASSICAL STRUCTURE | rational rate ratios + detailed balance | a free-energy-like scalar can be derived from (K) in this sector | repeat with measured/published thermal rates |
| PB-M3 | A one-rate perturbation breaks cycle consistency, so no single state scalar (q) reproduces all rate ratios. | EXACT COUNTEREXAMPLE TO GLOBAL SCALAR REPRESENTATION | cycle products (48
eq96) | nonequilibrium driving may require cycle/edge/reservoir information | classify the minimum extra information for reservoir-resolved models |
| PB-M4 | The reversible equilibrium occupancy is determined by the declared generator. | EXACT DIAGNOSTIC; CLASSICAL | stationarity + detailed balance | (pi^{eq}) is not independent in this regime | distinguish equilibrium, NESS, and transient preparation |
| PB-M5 | The same (K) and partition give different macro rates under different source occupancies. | EXACT DIAGNOSTIC; CLASSICAL COARSE-GRAINING FACT | rates (1), (3), and equilibrium-weighted (5/3) | current (pi) remains relevant unless lumpability/preparation removes it | test a published non-lumpable physical chain |
| PB-M6 | Two different energy/degeneracy pairs yield the same equilibrium weights. | EXACT REPRESENTATION COUNTEREXAMPLE | identical rational canonical weights | energy-like (q) and multiplicity-like (mu) may collapse into an effective free energy | identify an experiment that measures them separately |
| PB-P1 | A physical system can be represented by the full tuple ((R,q,mu,K,pi)) with all five components independently measurable. | OPEN PHYSICAL HYPOTHESIS | none | not established | seek a system with independent operational maps |
| PB-P2 | The repository's dynamic non-closure theorem produces a measurable thermodynamic consequence beyond classical moment-closure facts. | OPEN PHYSICAL HYPOTHESIS | none | not established | derive a prospective observable before looking at data |
| PB-P3 | The informational architecture contributes a new physical prediction. | OPEN | none | no prediction yet | complete an out-of-sample test |
| PB-P4 | Any part of this pilot supports spacetime or pregeometric physics. | NOT ESTABLISHED | none | no such inference is licensed | requires a separate bridge after lower-level validation |

## Allowed labels

- **EXACT DIAGNOSTIC** — an exact calculation in a declared finite physical toy model.
- **CLASSICAL STRUCTURE** — established physics or mathematics used as a mapping constraint.
- **EXACT COUNTEREXAMPLE** — an explicit finite construction refuting a stronger mapping.
- **OPEN PHYSICAL HYPOTHESIS** — a proposed physical statement with no present validation.
- **EMPIRICALLY SUPPORTED** — reserved for a prospective comparison against physical data not used to define the mapping.
- **NOT ESTABLISHED** — wording that blocks an unsupported inference.

## Promotion rule

No physical-bridge item may be labeled `EMPIRICALLY SUPPORTED` unless all of the following are recorded before the target comparison:

1. the physical dataset or published model;
2. the map from measured quantities to repository variables;
3. calibration parameters and how they were obtained;
4. the observable held out from calibration;
5. the prediction and acceptance/failure criterion;
6. comparison with at least one simpler or established alternative model.

A successful post-hoc fit does not satisfy this rule.
