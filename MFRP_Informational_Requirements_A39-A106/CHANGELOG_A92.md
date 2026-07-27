# A92 Changelog

## Added

- `audits/a92_exact_continuum_offset_three_window_audit.py`
- `results/a92_continuum_offset_three_window_results.json`
- `results/a92_continuum_offset_three_window_catalogue.json`
- `docs/technical_notes/MFRP_next_step_continuum_offset_three_window_atlas.md`
- `tools/generate_a92_figure.py`
- `figures/a92_continuum_offset_three_windows.png`

## Result

A92 partitions the full interval `129/1000 <= s <= 133/1000` into 858 exact algebraic `b = ceil(M c(s))` cells for `10 <= M <= 520`. Exact rational interval certificates classify the decisive factor `E_(M,b+2)` as 833 strictly negative cells, 14 strictly positive cells, and 11 cells containing one simple increasing root.

The positive portions yield 25 certified strict local compressed-maximizer windows. Ten supports—`360, 366, 425, 431, 437, 454, 466, 472, 478, 484`—were not sampled by the prior nine-probe grid. The result is explicitly local rather than a continuum global one-variation theorem.
