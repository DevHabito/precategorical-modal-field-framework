# Audit Protocol Contract Schema

Each canonical audit contract freezes the information required to reproduce and interpret one audit without reverse-engineering its script.

## Required sections

- `audit` — canonical ID, title, supersession history, evidence classes, and claim IDs.
- `source` — executable script, result directory, canonical summary, command, and implementation functions.
- `integrity` — SHA-256 of the script and canonical summary used to define this contract.
- `environment` — supported Python version and direct scientific dependencies.
- `randomness` — whether the audit is stochastic, the frozen seed, and RNG implementation.
- `parameters` — top-level protocol constants extracted from the source. Expressions are retained as source expressions when they are not literals.
- `generators` — named data/control generators and their implementation functions.
- `procedure` — ordered scientific procedure.
- `validation` — expected verdict, gate map, metric snapshot, and numerical tolerance.
- `expected_outputs` — archived output files with roles and SHA-256 hashes.
- `interpretation` — allowed claims, prohibited overclaims, and limitations.
- `reproduction` — clean-run, comparison, and mismatch policies.

## Evidence rule

A protocol contract freezes a computation. It does not upgrade a regression test into a theorem, a Monte Carlo result into a proof, or a mathematically consistent construction into a physical law.

## Canonicality rule

A corrective protocol does not erase the original failed protocol. It supersedes only the explicitly identified diagnostic or specification.

## Hash policy

If a source or canonical summary hash changes, the existing contract is stale. Update the protocol version or create a new audit version; do not silently replace the frozen artifact.
