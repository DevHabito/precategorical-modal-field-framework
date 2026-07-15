# Novelty Audits

This directory records claim-level literature comparisons for results marked
as requiring novelty review in `docs/RESULT_CLASSIFICATION.md`.

## C1 scope

- `MF-R007_finite_preorder_count.md`
- `MF-R008_representative_code_count.md`
- `MF-R011_edge_flip_probability.md`
- `NOVELTY_AUDIT_C1_SUMMARY.md`
- `SEARCH_LOG.csv`
- `REFERENCES.bib`
- `RESULT_CLASSIFICATION_PATCH.csv`

## C2 scope

See `README_C2.md` for the foundational novelty audit covering MF-R036,
MF-R047, MF-R048, and MF-R049.

## Status vocabulary

- `CLASSICAL`: an explicit matching prior result was located.
- `PROJECT_SPECIFIC_NO_MATCH_FOUND`: the exact project formulation was not
  found, but priority is not certified.
- `APPARENTLY_UNREPORTED`: related work exists, but no exact match was located.
- `NOVELTY_NOT_CERTIFIED`: mandatory qualifier for all negative search results.

## Rule

No negative search result authorizes the wording “first ever” or “previously
unknown” without further specialist review.
