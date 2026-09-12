# A114 — lifted active-set selection after compressed one-variation

A113 tells us **where the compressed maximum can live**. A114 asks the next question:

> Once the compressed maximizer is known, which lifted LP architecture actually satisfies the full strict KKT system?

This is deliberately separated from A113. A compressed maximum and a valid lifted basis are not the same statement.

## A114-A — the `b+3` phase

A114-A is now **PROVED** for the analytic tail

`M>=521`, `129/1000<=s<=133/1000`,

under the frozen contract.

If the strict compressed maximizer is

`j=b+3`,

then the lifted optimum is the endpoint-released architecture

`P={j-1,j,M}`,

`Q={1,h,h+1}`,

with `alpha+` and `beta-` active and gamma inactive.

Read in this order:

1. `session_artifacts/A114A_ANALYTIC_TAIL_ENDPOINT_RELEASED_LIFT_THEOREM_20260912.md` — theorem and proof map.
2. `session_artifacts/A114A_LOGICAL_COMPOSITION_AUDIT_20260912.md` — dependency and circularity audit.
3. `A114A_CORRECTIONS_AND_DEAD_ENDS_20260912.md` — mistakes, false stronger claims, and why the final proof has its current form.
4. `archives/A114A_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip` — final analytic certificate, 141/141 JSON result, standalone Fraction cross-check, logical audit scripts/results and promoted field notes.

## Why the negative control matters

The stronger statement

`j=b+3 => endpoint-released`

is false.

At `M=521, s=129/1000`, the arithmetic offset `j=b+3` is not a compressed maximum. The independent solver rejects the endpoint lift through `basic_p_92<0` and `reduced_cost_p_0<0`.

So the theorem's strict-compressed-maximizer premise is mathematically necessary, not decorative.

## Current frontier

A114-A closes the lifted `b+3` tail phase.

Still open are the global lifted architecture classifications inside the `b+1` and `b+2` compressed phases. The finite atlas suggests several architectures can appear there (gamma-plus, two-band, q0/q1, gamma-minus), but that finite history is a guide for theorem discovery, not an all-M proof.

## Field-note discipline

This folder keeps failed stronger claims and implementation mistakes on purpose. A future reader should be able to tell:

- what was observed;
- what was guessed;
- what was refuted;
- what was corrected;
- what is actually proved;
- what remains open.

`MANIFEST_A114A_20260912.sha256` hashes the visible promoted notes and the reproducibility archive.
