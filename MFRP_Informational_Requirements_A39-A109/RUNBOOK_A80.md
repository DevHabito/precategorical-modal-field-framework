# A80 Runbook

From the repository root:

```bash
python audits/a80_local_compression_window_atlas_audit.py
python tools/generate_a80_figure.py
```

The audit first generates 142 exact Cramer boundary polynomials. It then runs each of the 20 complete compression-window certificates in an isolated worker process:

```bash
python audits/a80_local_compression_window_worker.py 40 9
```

The isolated workers avoid cumulative symbolic-expression cache growth. A complete A80 replay normally takes a few minutes and writes:

- `results/a80_local_compression_window_atlas_results.json`
- `results/a80_boundary_polynomial_catalogue.json`
- `results/a80_interval_KKT_condition_certificates.json`
- `figures/a80_local_compression_window_atlas.png`

A PASS verdict requires all 16 top-level gates.
