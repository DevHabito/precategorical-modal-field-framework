# A110–A112 research update

This directory continues the frozen A107–A109 gamma-plus continuum program.

## Scientific status

- **A110 — finite structural theorem:** on the frozen A94/A95/A102 gamma-plus
  contract (`14 <= M <= 520`, `129/1000 <= s <= 133/1000`), the strict KKT
  component is controlled by the two adjacent basic masses `p_j` and
  `p_(j+1)`. The exhaustive structural calculation was independently
  replicated on all **1,870** A94-envelope `(M,j)` pairs with zero failures,
  and cross-checked against 240 exact H19 solver values with zero mismatch.
- **A111/A111B — finite tail reconnaissance:** no counterexample was found in
  preregistered exact checks beyond the finite cutoff, including selected
  stress cases through `M=5000`. This is finite evidence, not an all-M proof.
- **A112 — analytic tail:** **OPEN / INCONCLUSIVE**. The current reduction
  rewrites `RQ(2)` as a Schur-complement/pivot-square minor and as an augmented
  determinant with eight `s`-channels. The next target is a uniform
  boundary-ordering/interlacing proof using the exact compressed-contact
  localization.

No new canonical full-KKT/full-atlas outcome after rank 430 is used in these
structural/tail investigations.

## Contents

- `audits/a110_independent_replication.py` — independent exact replication
  program for the A110 finite closure.
- `session_artifacts/A110_FINITE_A109_STRUCTURAL_THEOREM.md` — finite theorem.
- `session_artifacts/A110_RIGOROUS_REPLICATION_REVIEW.md` — independent review.
- `session_artifacts/A110_INDEPENDENT_REPLICATION_AGGREGATE.json` — aggregate
  exact replication counts.
- `session_artifacts/A111_PREREGISTRATION.json` and
  `A111_RESULT_SUMMARY.json` — frozen tail reconnaissance and concise outcome.
- `session_artifacts/A111_TAIL_RECONNAISSANCE_NOTE.md` — interpretation and
  claim boundaries for A111/A111B.
- `session_artifacts/A112_PREREGISTRATION.json` — frozen A112 analytic-tail
  program.
- `session_artifacts/A112_PIVOT_SQUARE_STATUS_NOTE.md` — current exact
  structural reduction and next theorem target.

## Claim boundary

The established result here is a **finite structural theorem under the stated
architecture and finite parameter contract**. A112 is not yet an all-M
extension. No physical interpretation is claimed.
