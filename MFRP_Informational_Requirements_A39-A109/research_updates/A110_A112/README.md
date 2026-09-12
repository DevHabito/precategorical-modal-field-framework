# A110–A112 research update

This directory is the working field notebook for the finite-to-tail gamma-plus structural program.

If you are arriving here for the first time, **start with `A112_CURRENT_STATUS_20260911.md`**. It is written as a human-readable map of where the research stands, what was proved, what failed on the way, and what remains open.

## Current scientific status

### A110 — finite structural theorem

On the frozen gamma-plus contract

`14 <= M <= 520`, `129/1000 <= s <= 133/1000`,

the strict KKT component is controlled by the two adjacent basic masses `p_j` and `p_(j+1)`. The independent replication covered all 1,870 A94-envelope `(M,j)` pairs with zero failures and matched 240 exact H19 solver values with zero mismatch.

### A111/A111B — finite tail reconnaissance

Preregistered exact checks found no counterexample in the tested tail regime, including selected stress cases through `M=5000`. These remain finite reconnaissance, not the analytic proof.

### A112 — analytic tail

**Current status: PROVED under the frozen gamma-plus family and strict compressed-phase hypotheses.**

For every

`M >= 521`, `129/1000 <= s <= 133/1000`,

within the frozen architecture

`P={0,j,j+1,M}`, `Q={1,h,h+1}`, `h=floor(M/2)`,

with active signs alpha+, beta-, gamma+, and with `j` a strict compressed maximizer, the full strict KKT conditions for that basis hold exactly where

`p_j > 0` and `p_(j+1) > 0`.

The common-positive set is one interval. Its only possible internal KKT boundaries are

- left: `p_(j+1)=0`;
- right: `p_j=0`.

The full theorem statement and proof map are in
`session_artifacts/A112_ANALYTIC_TAIL_STRUCTURAL_THEOREM_20260911.md`.

## Very important claim boundary

This is **not** a theorem that the gamma-plus architecture is globally selected among every possible LP architecture for all `(M,s)`.

It also does not cover other source windows, other support/band architectures, or any physical interpretation.

So the correct phrase is:

> local structural all-tail theorem for the frozen gamma-plus family,

not “global unrestricted A109 theorem”.

## How the tail proof is organized

The closure is deliberately split into small pieces so that each can be attacked independently:

- **A112-A:** adjacent positivity localizes the contact to `b+1` or `b+2`.
- **A112-B:** those positive adjacent masses force `RQ(2)>0` by exact determinant interlacing.
- **A112-C:** `RQ(2)>0` forces every nonbasic P/Q reduced cost positive.
- **A112-D:** strict compressed maximality forces all three active duals positive.
- **A112-E:** `p_(j+1)>0 => q_h>0`.
- **A112-F:** opposite adjacent slopes and the exact chain-rule derivative numerator.
- **A112-G:** branch regularity `A<0<B`, no pole, `t'(s)>0`, and `p_j>0 => q_1>0`.
- **Composition audit:** checks the A–G chain for circular assumptions and quantifier gaps, then closes the remaining basic variables pointwise.

## What changed since the old A112 status note

`session_artifacts/A112_PIVOT_SQUARE_STATUS_NOTE.md` is intentionally retained unchanged as a historical artifact. It records the earlier `OPEN / INCONCLUSIVE` state.

Do **not** delete it. It documents what was known before the tail closure.

The authoritative current state is now given by:

- `A112_CURRENT_STATUS_20260911.md` — human-readable current state;
- `A112_CORRECTIONS_AND_DEAD_ENDS_20260911.md` — failed stronger claims, discarded formulas and audit repairs;
- `session_artifacts/A112_ANALYTIC_TAIL_STRUCTURAL_THEOREM_20260911.md` — formal theorem statement and proof map;
- `session_artifacts/A112_LOGICAL_COMPOSITION_AUDIT_20260911.md` — dependency/quantifier audit;
- `session_artifacts/A112_LOGICAL_COMPOSITION_AUDIT_20260911.json` — machine-readable audit summary.

## Complete working set

The complete 2026-09-11 working set — final A112-B ... A112-G certificate scripts, JSON results, independent cross-checks, partial historical certificate, exploratory scratch calculations and the human notes — is preserved in:

`archives/A112_TAIL_CLOSURE_WORKING_SET_20260911.zip`

Its SHA-256 is recorded in `MANIFEST_A112_TAIL_CLOSURE_20260911.sha256`.

The archive intentionally includes exploratory material that is **not authoritative proof**. The human status/theorem/audit documents identify which artifacts are final certificates and which are only provenance.

## Research discipline

This repository should be read as a field notebook, not just a code dump.

When the scientific state changes:

1. keep the earlier artifact;
2. write a new dated status note;
3. record failed stronger claims and exact counterexamples;
4. keep theorem scripts and machine-readable results in the preserved working set;
5. add hashes;
6. say explicitly what is still open.

That way another researcher — or our future selves — can reconstruct the path without relying on memory.
