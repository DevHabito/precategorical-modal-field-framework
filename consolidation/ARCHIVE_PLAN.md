# Consolidation 1.0 — non-destructive archive plan

The repository currently exposes cumulative snapshots such as

- `MFRP_Informational_Requirements_A39-A71/`
- `MFRP_Informational_Requirements_A39-A77/`
- `MFRP_Informational_Requirements_A39-A106/`
- `MFRP_Informational_Requirements_A39-A109/`

at the repository root. They preserve history, but they are poor navigation because later directories largely supersede earlier cumulative snapshots.

The cleanup must preserve reproducibility and priority records while removing these snapshots from the main reader path.

## Phase 1 — navigation cleanup

Do not delete or move historical files yet.

Actions:

- make `consolidation/README.md` the canonical start page;
- change the root README so historical A-number trees are labeled provenance/archive;
- freeze new A-number package creation during consolidation;
- direct readers to claims and theorem groups rather than chronology.

## Phase 2 — release/tag preservation

Before removing cumulative snapshots from the default branch:

- identify the commit corresponding to each meaningful historical snapshot;
- create immutable Git tags/releases for those states;
- record tag -> snapshot mapping in an archive index;
- preserve integrity manifests for released states;
- optionally create Zenodo-backed releases when the consolidated public artifacts are stable enough to merit a DOI.

Tags/releases are preferred to four cumulative copies in the default branch because Git already stores history efficiently.

## Phase 3 — default-branch simplification

Only after Phase 2 is verified:

- retain one canonical current source tree for legacy material;
- remove redundant cumulative snapshot directories from the default branch in one dedicated PR;
- do not squash away or rewrite the historical commits that contain them;
- add migration links from old path names to their corresponding release/tag in the archive index.

This is a repository-structure change only. It must not alter mathematical content.

## Proposed long-term top-level structure

```text
README.md
consolidation/
core/
  combinatorics/
  dynamic-nonclosure/
  exponential-moment-optimization/
verification/
  python/
  formal/lean/
manuscripts/
docs/
  literature/
  status/
archive/
  INDEX.md
interpretation/
  README.md
```

The actual move into this structure should happen only after the consolidated theorem documents exist and links can be migrated safely.

## What stays out of `core/`

The mathematical core must not use physical interpretation as a premise. RZS/Modal Field motivation, speculative physical bridges, historical failed protocols, and chronological research diaries belong under `interpretation/` or `archive/` unless a particular mathematical statement is independently extracted and proved.

## Safety rule

No deletion is justified merely because a file is old, embarrassing, failed, or superseded. Failed routes and corrections are scientifically useful. The objective is to move them out of the reader's critical path, not erase them.
