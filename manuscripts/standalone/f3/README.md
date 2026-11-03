# Standalone review unit: MF-R049 / C2

This directory isolates **one** mathematical result: failure of a mean-plus-single-log-Laplace-score macrostate to predict its own next score under a specified centered contraction. It is independent of the broader Modal Field ontology and does not change the historical MF-R049 examples.

**Reading paths:**

1. For a fresh reviewer: [statement-only problem](REVIEWER_PROBLEM.md), then submit a blind attempt.
2. Afterwards: [short manuscript](ARTICLE.md), giving the complete proof and scoped literature.
3. For assessing the proof: [review record template](REVIEW_FORM.md).
4. For checking provenance and open obligations: [verification ledger](STATUS.md).

Reproduce the exact rational checks from the repository root:

\`\`\`sh
python tools/f3_standalone_exact.py
\`\`\`

The checker uses only Python's standard library and does **not** claim to numerically verify the real logarithm or Lean's proof kernel. The historical Lean sources and their assurance evidence remain under \`formal/lean/\` and \`consolidation/\`.

This package is a **review invitation**, not an assertion of originality, peer review, independent external verification or physical discovery.
