# Modal Field / RZS Research Archive

**Author:** Felipe Gianini Romero (Felipe G. Romero)  
**Status:** formal research programme; not a confirmed fundamental physical theory.

This repository preserves the computational and formal development of a pre-categorical relational research programme. Its central question is not “how to fit a final theory to known physics,” but which mathematical structures are actually required before order, measure, refinement, transition, and coarse-grained flow can be defined without hidden assumptions.

## What is here

- exact graph and poset enumeration;
- order/measure identifiability results;
- `q`-gauge and operationalization audits;
- kernel-selection and lambda-status audits;
- refinement, multiplicity, and projective-measure results;
- effective-score and dynamic-closure results;
- noise-law selection and universality tests;
- observable-relative coarse-graining and occupancy obstruction;
- original failed protocols and their corrective versions;
- the A8.1 formal resolution of **5,234 versus 6,942**;
- manuscript PDFs and an explicit supersession notice.

## Central correction

For loopless labeled digraphs on five vertices:

- **6,942** = full labeled reflexive reachability preorders / complete labeled condensation structures;
- **5,234** = minimum-representative quotient-poset codes used in the original A8 implementation;
- **139** = fully unlabeled condensation preorders.

Both exact counts are independently reproduced by exhaustive enumeration and closed combinatorial formulas in A8.1. The original wording was ambiguous and the v1 preprint is marked superseded pending correction.

## Repository map

- `audits/` — scripts and exact/seeded outputs, including failed and corrective versions;
- `article/` — preserved manuscripts and erratum notice;
- `docs/AUDIT_INDEX.md` — audit-by-audit index;
- `docs/CANONICAL_VERSIONS.md` — which version should be treated as canonical;
- `docs/RESULT_CLASSIFICATION.md` — claim-level classification by evidence, novelty, allowed wording, and manuscript destination;
- `docs/SCIENTIFIC_STATUS.md` — established results and explicit nonclaims;
- `docs/REPRODUCIBILITY.md` — environment and execution instructions;
- `docs/CORRECTIONS.md` — correction history;
- `MANIFEST.csv` and `SHA256SUMS.txt` — integrity and completeness records.

## Quick start

```bash
git clone https://github.com/DevHabito/precategorical-modal-field-framework.git
cd precategorical-modal-field-framework
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cd audits
python a8_1_condensation_code_resolution.py
```

## Evidence discipline

The repository deliberately distinguishes proofs, exact enumeration, synthetic witnesses, Monte Carlo audits, regression tests, failed protocols, and corrective protocols. A numerical pass does not turn a classical identity into a new theorem, and a mathematically consistent construction is not by itself evidence that nature uses that construction.

## Current scientific boundary

The project has not derived physical spacetime, calibrated time, physical distance, curvature, gravity, matter, a physical lambda, or an experimental mapping for `q`, `mu`, or `pi`. See `docs/SCIENTIFIC_STATUS.md`.

## Citation and license

Please cite the repository release and the specific audit or manuscript used. Software in this repository is licensed under Apache-2.0. Scientific content, documentation, figures, tables, CSV files, JSON result files, reports, and other research outputs are licensed under CC BY 4.0. See `LICENSE.md`, `NOTICE`, and the `LICENSES/` directory.
