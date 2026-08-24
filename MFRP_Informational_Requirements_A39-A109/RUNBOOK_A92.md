# A92 Runbook

## Execute the audit

```bash
python audits/a92_exact_continuum_offset_three_window_audit.py
```

Expected output:

- verdict: `PASS_EXACT_CONTINUUM_DECISIVE_FACTOR_ATLAS_AND_25_LOCAL_OFFSET_THREE_WINDOWS`
- gates: `18/18`
- nonempty algebraic cells: `858`
- classifications: `833 negative`, `14 positive`, `11 single-root`
- strict local windows: `25`
- additional supports beyond the A91 probe grid: `10`

## Regenerate the figure

```bash
python tools/generate_a92_figure.py
```

Output:

- `figures/a92_continuum_offset_three_windows.png`

## Evidence boundary

A92 certifies a complete continuum atlas for the decisive factor and immediate local-maximizer pattern. It does not certify the full adjacent-factor sequence on every continuum window and must not be cited as a global continuum one-variation theorem.
