# F3 review branch — first root-index job failure and correction

**Date:** 2026-11-03  
**Scope:** CI configuration only. The F3 mathematical statement, distributions and proof did not change.

The initial root-index workflow at source revision `48568987f95662ff0cd6c62753ea25d6ce09e428`, GitHub Actions run [41731419463](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41731419463), concluded **failure**. The workflow passed an escaped literal `\\\${{ github.sha }}` as the checkout ref, rather than GitHub's actual expression `\${{ github.sha }}`.

I made a one-line workflow-only correction in commit `cceef3cddaaf99d85da062d8117abdb4aad5626d`. The subsequent root-index workflow [41731490031](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/41731490031) passed the exact-head guard, index refresh/check, repository validation and restricted commit step.

This incident has no bearing on the mathematical truth of MF-R049 or the historical ZIP defects. It remains a recorded **CI configuration failure** rather than being relabeled as a successful initial run. The corrected workflow only writes `MANIFEST.csv` and `SHA256SUMS.txt` on the isolated review branch, never historical archives.
