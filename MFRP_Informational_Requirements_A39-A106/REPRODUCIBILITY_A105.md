# A105 reproducibility statement

A105 is deterministic and uses exact SymPy rational arithmetic for matrix inversion, rank-one updates, sparse polynomial coefficients, endpoint signs, root isolation, derivative signs, interval enclosures, exact bracket ordering, and outside counterexamples.

The forty records are committed separately under `provenance/a105_legacy_two_band_continuum_atlas/records/`. The final assembly verifies exact source routing, condition counts, key uniqueness, boundary mechanisms, root simplicity, competing-root ordering, core positivity, complete boundary-hull positivity, and negative outside witnesses.

The source family is fixed before the continuum test:

```text
P={0,j,M}, Q={1,h,h+1}, alpha+ and beta- active, gamma inactive.
```

No parameter or support is added after a boundary failure. A boundary is reported as a failure of that fixed basis beyond the selected root.

The theorem remains restricted to the forty A95/A102 rational source segments classified as `legacy_two_band_compressed`. It is not a continuum theorem for the complete 1,063-witness atlas, complete A92 cells, arbitrary support sizes, or physical models.

A standalone replay independently recomputed all forty record files. The forty records plus the consolidated result, catalogue, and figure produced 43/43 identical SHA-256 comparisons with the integrated repository.
