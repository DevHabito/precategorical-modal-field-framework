# A106 reproducibility statement

A106 is deterministic and uses exact SymPy rational arithmetic for direct matrix inversion, Sherman-Morrison rank-one updates, sparse polynomial coefficients, endpoint signs, root isolation, derivative signs, interval enclosures, exact root ordering, and outside counterexamples.

The eighteen records are committed separately under `provenance/a106_legacy_gamma_minus_continuum_atlas/records/`. The final assembly checks exact source routing, condition counts, key uniqueness, 2,410 direct-matrix/rank-one witness equalities, boundary simplicity, competing-root ordering, core positivity, complete nonselected-boundary hull positivity, and negative outside witnesses.

The source family is fixed before the continuum test:

```text
P={0,j-1,j,M}, Q={1,h,h+1}, alpha+, beta-, and gamma- active.
```

No parameter, support atom, or active band is added after a boundary failure. A boundary is recorded as the end of validity of the frozen basis.

The theorem remains restricted to the eighteen A95/A102 source segments classified as `legacy_three_band_gamma_minus`. It is not a continuum theorem for the 922 gamma-plus records, the complete 1,063-witness atlas, complete A92 cells, arbitrary support sizes, or physical models.


A standalone package independently recomputed all eighteen record files and regenerated the consolidated result, catalogue, and figure. The eighteen record files plus the three consolidated artifacts produced 21/21 identical SHA-256 comparisons with the integrated repository.
