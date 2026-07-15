# Reproducibility Protocol Contracts

This directory contains **16 canonical audit contracts** for the central results currently used to restructure the combinatorics and foundational manuscripts.

## Included protocols

- `A08_1.yaml` — Formal Resolution of 5,234 versus 6,942
- `A09.yaml` — Relational Clock Audit
- `A10.yaml` — Internal Duration Audit
- `A18_2.yaml` — Exact Order-Measure Identifiability Limit
- `A19.yaml` — Ensemble Copula Identifiability Limit
- `A23.yaml` — RZS q Primitive and Gauge Audit
- `A24_1.yaml` — Corrected q Operationalization Audit
- `A28.yaml` — q Score Selection and Context-Scale Incompatibility
- `A31.yaml` — Microscopic Multiplicity and Finite Refinement Measure
- `A32.yaml` — Infinite Refinement, Projective Limits, and Terminality
- `A33.yaml` — Projective Branch Fraction Law
- `A34.yaml` — Effective Score Closure Audit
- `A35.yaml` — Conditional Gaussian Closure Audit
- `A36_1.yaml` — Corrected Gaussian Noise Selection Diagnostic
- `A37_1.yaml` — Corrected Noise-Law Universality Audit
- `A38_1.yaml` — Corrected Observable-Relative Coarse-Graining Audit

## Validation

Install the YAML dependency if it is not already available:

```bash
pip install PyYAML>=6.0
```

From the repository root, run:

```bash
python tools/validate_protocols.py
```

The validator checks:

- required contract fields;
- unique canonical audit IDs;
- existence and SHA-256 of scripts and summaries;
- frozen seed, verdict, gates, and metric snapshots;
- existence and hashes of archived output files;
- validity of every `claim_id` against `docs/RESULT_CLASSIFICATION.json`.

## Scope

These contracts cover the central canonical sequence: A8.1, A9, A10, A18.2, A19, A23, A24.1, A28, and A31-A38.1. Historical methods A3-A6 and A11-A17 remain indexed but should receive contracts only if they are retained in a manuscript or methodological supplement.
