# A113 — global compressed one-variation in the analytic tail

This folder continues the finite-to-tail programme after A112.

If you are arriving here later, read the visible field notes in this order:

1. `session_artifacts/A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_THEOREM_20260911.md` — theorem and proof map.
2. `A113_CORRECTIONS_AND_DEAD_ENDS_20260911.md` — false stronger claims, numerical false alarms, and corrections.
3. `archives/A113_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip` — exact certificate script, machine-readable result, independent hostile review, theorem and field notes preserved together.

## Where the science stands

A94 proved complete compressed-objective one-variation for the finite regime `14<=M<=520` on the full source window `129/1000<=s<=133/1000`.

A113 proves the analytic tail `M>=521` on the same window.

Combined, under the frozen reduced/compressed contract:

`M>=14 => the complete adjacent compressed-objective factor sequence has one positive-to-negative variation.`

The global compressed maximizer belongs to `{b+1,b+2,b+3}`, where
`b=ceil(M c(s))` and `c(s)=log(2)/(-2 log s)`.

## What we learned while proving it

Two tempting stronger statements are false and remain recorded:

- `b+3` does **not** disappear in the tail; `M=561, s=129/1000` is an exact counterexample.
- `E_(b+1)-E_(b+2)>0` is **not** globally true; deep-tail examples have a negative second secant while preserving one-variation.

The successful structural quantity is

`E_(b+1)-2 E_(b+2)>0`.

## Boundary of the claim

A113 concerns the **compressed objective**. It does not by itself choose the lifted LP active-set architecture.

A114-A continues exactly from that gap and proves the lifted architecture in the strict `b+3` phase.

## Reproducibility

`MANIFEST_A113_20260912.sha256` hashes the visible promoted notes and the reproducibility archive.

No floating-point sign decision is used in the theorem certificate. Numerical exploration was used only to suggest claims or locate possible counterexamples; promoted claims were rechecked exactly.
