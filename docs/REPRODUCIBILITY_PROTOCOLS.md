# Canonical Audit Protocols

The repository's executable scripts and archived outputs are accompanied by frozen YAML protocol contracts in `protocols/`.

Each contract states the audit's evidence class, scientific claim IDs, source artifacts, SHA-256 locks, random seed, top-level parameters, data/control generators, ordered procedure, expected verdict and gates, key metric snapshot, output files, limitations, allowed claims, and forbidden overclaims.

Run from the repository root:

```bash
python tools/validate_protocols.py
```

A passing result means that the contracts are structurally complete and consistent with the currently archived scripts, summaries, outputs, and claim matrix. It does not independently prove the mathematical claims or establish a physical interpretation.
