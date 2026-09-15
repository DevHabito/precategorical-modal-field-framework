# A120 — remote-sign rounding phase

A120 studies the two remote factors that blocked a naive target-deformed A113 theorem.

## Status

**PROVED under the inherited A115 reduced-factor contract; red-team PASS WITH REFUTATION OF NAIVE STABILIZATION.**

Main theorem: for fixed interior `s<tau<beta/s`, fixed parity and fixed offset `j`,

\[
\frac{E_{M,b_M+j}}{\tau^{\lfloor M/2\rfloor}\tau^{b_M+j}}
=
\Psi_{p,j}(\rho_M)+o(1),
\]

where

\[
\rho_M=\lceil M c_\tau(s)\rceil-M c_\tau(s).
\]

The leading remote sign therefore retains a genuine ceiling/rounding phase.

Consequences:

- the naive eventual package `E_b>0`, `E_{b+3}<0` is false for arbitrary target deformation;
- `E_b` changes sign infinitely often for the fixed interior pair `s=131/1000, tau=1/5`;
- `E_{b+3}` changes sign infinitely often for `s=129/1000, tau=9/10`;
- A113 at `tau=1/2` is not refuted and is exactly regression-checked.

Files:

- `A120_REMOTE_SIGN_ROUNDING_PHASE_THEOREM_20260915.md`
- `a120_remote_sign_rounding_phase_audit.py`
- `A120_EXACT_AUDIT_RESULTS_20260915.json`
- `A120_RED_TEAM_AUDIT_20260915.md`
- `A120_CORRECTIONS_AND_DEAD_ENDS_20260915.md`
- `MANIFEST_A120_GIT_BLOBS_20260915.txt`

Open:

- remote-factor classification in the collision scaling `tau-s=O(1/M)`;
- any target-deformed A113 one-variation theorem under a revised phase-aware formulation;
- any target-deformed A114 lifted active-set theorem;
- novelty/priority certification;
- any physical or ontological interpretation.
