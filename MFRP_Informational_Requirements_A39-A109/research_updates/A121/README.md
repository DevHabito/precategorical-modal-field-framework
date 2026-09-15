# A121 — fixed-interior sign staircase

A121 extracts the phase geometry hidden in the A120 remote-factor asymptotic.

## Status

**PROVED under the inherited A120 fixed-interior contract; red-team PASS WITH SCOPE.**

A120 gives

\[
\Psi_{p,j}(\rho)=P_p s^{j+\rho}-Q_p.
\]

A121 defines

\[
\xi_p=\frac{\log(Q_p/P_p)}{\log s}
\]

and proves

\[
\operatorname{sign}\Psi_{p,j}(\rho)
=
\operatorname{sign}\bigl(\xi_p-(j+\rho)\bigr).
\]

Thus the limiting offset/rounding landscape is one strictly decreasing sign front.

Main consequences:

- one \(+\to-\) limiting transition across offsets;
- for every fixed offset,
  \[
  J^{(j)}_M=E_{b+j}-\tau^{-1}E_{b+j+1}>0
  \]
  eventually;
- every fixed finite offset window is therefore exactly one-variation for sufficiently large \(M\);
- away from resonance, the strict local compressed peak is at
  \[
  b+\lceil\xi_p-\rho\rceil;
  \]
- writing \(\xi_p=m+\theta\), the local peak can move only between the adjacent sites \(b+m\) and \(b+m+1\);
- the two irrational A120 examples yield infinite two-site local-peak alternation.

Exact hardening includes:

- 21 frozen \(\tau=1/2\) one-variation regressions;
- 8 exact even/odd two-site sentinels;
- an exact finite-\(M\) negative-\(J\) warning showing the theorem is genuinely eventual.

Files:

- `A121_FIXED_INTERIOR_SIGN_STAIRCASE_THEOREM_20260915.md`
- `a121_fixed_interior_sign_staircase_audit.py`
- `A121_EXACT_AUDIT_RESULTS_20260915.json`
- `A121_RED_TEAM_AUDIT_20260915.md`
- `A121_CORRECTIONS_AND_DEAD_ENDS_20260915.md`
- `MANIFEST_A121_GIT_BLOBS_20260915.txt`

Open:

- the resonant marginal factor \(j+\rho=\xi_p\);
- global target-deformed compressed-maximizer localization;
- collision scaling \(\tau-s=O(1/M)\) for remote factors;
- any target-deformed A114 lifted classification;
- novelty/priority certification;
- any physical or ontological interpretation.
