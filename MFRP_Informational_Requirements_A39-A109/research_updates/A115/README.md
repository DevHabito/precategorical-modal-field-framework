# A115 — target-node deformation

A115 tests which parts of the frozen A84/A113 compressed mechanism survive
when the target node is deformed from

\[
\tau=\frac12
\]

to a general rational target satisfying

\[
\beta<s<\tau<1.
\]

## Current status

**PASS_WITH_REFUTATION.**

Established:

- exact target-deformed central-Q formulas;
- exact scale-normalized noise formula inherited from the A64 rule;
- exact generalized \(J_{\tau,k}=E_k-\tau^{-1}E_{k+1}\) cancellation identity;
- exact reproduction of the frozen \(\tau=1/2\) A84/A113 contract;
- finite exact stress tests.

Refuted:

- `M>=521` is **not** a universal threshold guaranteeing
  \(J_{\tau,b_\tau+1}>0\) for every \(\beta<s<\tau<1\).

Open:

- eventual positivity for each fixed interior parameter pair;
- compact-uniform eventual positivity away from the collision surfaces.

No asymptotic theorem or physical interpretation is claimed.

## Files

- `A115_TARGET_NODE_DEFORMATION_EXACT_AUDIT_20260914.md` — formal claim ledger,
  derivations, finite evidence, counterexamples, corrections and nonclaims.
- `a115_target_deformation_exact_audit.py` — self-contained exact audit.
- `A115_TARGET_DEFORMATION_EXACT_RESULTS_20260914.json` — machine-readable output.
- `A115_CORRECTIONS_AND_DEAD_ENDS_20260914.md` — preserved failed routes and
  scope corrections.
- `MANIFEST_A115_20260914.sha256` — hashes of the A115 package.
