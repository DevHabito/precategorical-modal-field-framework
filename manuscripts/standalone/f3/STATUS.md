# MF-R049/F3 short-note verification ledger

**Date created:** 2026-11-03  
**Author:** Felipe Gianini Romero  
**Purpose:** a small, reviewable mathematical unit separated from the chronological research programme.

| Item | What was actually done | Status |
| --- | --- | --- |
| Source definitions | Read the existing \`DynamicNonclosure.lean\` and \`DynamicNonclosureTransport.lean\` at baseline \`8beff0808bf29c9d11467cd76a8b50a1c74a4174\` | SOURCE INSPECTED |
| Historical novelty | Read \`docs/novelty/MF-R049_dynamic_nonclosure.md\`; it marks this as a project-specific corollary, not a novel general theorem | PRIOR AUDIT READ |
| Human proof | Prepared a standalone proposition with exact rational calculations and a complete analytic log/exp transport step | DRAFT FOR REVIEW |
| Original Lean | Existing sources declare \`rationalScalarNonclosure\`; past logs in \`consolidation/F3_RATIONAL_NONCLOSURE_2026-10-19.md\` report passing proof checks | HISTORICALLY REPORTED; NEW CI MUST BE INSPECTED |
| Fresh rational implementation | Python standard library only: independent-from-project \`Fraction\` code, rank minor, 25 parameter-grid cases, equality and mutation controls | LOCAL PASS ON 2026-11-03 |
| Fresh GitHub Actions | Exact-code and Lean workflow created on the review branch | PENDING UNTIL ACTUAL RUN LOG IS INSPECTED |
| V2 blind rederivation | Challenge prepared; no outside derivation was solicited or received | OPEN |
| V4 external specialist review | Review form prepared; no third-party verdict has been received | OPEN |
| Theorem-level novelty check | Three background publications were opened/metadata-checked; no exhaustive equivalence comparison | OPEN |
| Physical application | No operational bridge, units or empirical prediction derived | NOT CLAIMED |

**Independence caution:** the new manuscript and checker were prepared after the underlying result and repository proof were inspected. They are a distinct presentation and separate executable implementation; **they are not a blind independent V2 rederivation by a new solver or an external reviewer**.

**Historical distinction:** the original MF-R049 construction at \(\lambda=\log2\) uses a square-root moment difference; the rational version here uses \(\lambda=2\log2\). Both demonstrate scoped nonclosure, but their coefficients and initial transform points differ.

**Merge policy:** keep this draft review branch separate from \`main\` and from the experimental A113 PR #21. Preserve all checks and any failing logs. Do not use successful CI as permission to mark V2 or V4 complete.
