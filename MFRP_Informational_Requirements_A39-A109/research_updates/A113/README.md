# A113 — global compressed one-variation in the analytic tail

This folder continues the finite-to-tail programme after A112.

If you are arriving here later, read the files in this order:

1. `session_artifacts/A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_THEOREM_20260911.md` — the theorem and proof map.
2. `session_artifacts/A113_INDEPENDENT_REPLICATION_REVIEW_20260911.md` — hostile review and independent exact reconstruction.
3. `A113_CORRECTIONS_AND_DEAD_ENDS_20260911.md` — false stronger claims, numerical false alarms, and why the final proof has its current form.
4. `audits/a113_tail_global_compressed_one_variation_certificate.py` — hardened exact certificate.
5. `audits/a113_independent_a84_crosscheck.py` — independent A84 reconstruction used only as a transcription/regression check.

## Where the science stands

A94 proved complete compressed-objective one-variation for the finite regime `14<=M<=520` on the full source window `129/1000<=s<=133/1000`.

A113 now proves the analytic tail `M>=521` on the same window.

Combined, they establish under the frozen reduced/compressed contract:

`M>=14 => the complete adjacent compressed-objective factor sequence has one positive-to-negative variation.`

The global compressed maximizer always belongs to `{b+1,b+2,b+3}`, where `b=ceil(M c(s))` and `c(s)=log(2)/(-2 log s)`.

## Important boundary

This is **not yet** global selection of the lifted LP active-set architecture.

A112 closes the gamma-plus lifted KKT mechanism once a strict compressed phase and the corresponding basis are fixed. A113 closes the compressed maximizer geometry. The next problem is to connect these layers globally and determine which lifted architecture is selected when the compressed maximizer does not lift to a strict gamma-plus KKT point.

In particular, A113 preserves genuine `b+3` compressed phases in the tail, while A112-A shows a strict tail gamma-plus KKT basis with both adjacent masses positive can occur only at `j=b+1` or `j=b+2`. That mismatch is not an error; it is the next structural question.

## Reproducibility

`MANIFEST_A113_20260911.sha256` records hashes of the theorem, certificates, review, cross-check and field notes.

No floating-point sign decision is used in the theorem certificate. High-precision numerical exploration was used only to find candidate claims and counterexamples, which were then rechecked exactly.
