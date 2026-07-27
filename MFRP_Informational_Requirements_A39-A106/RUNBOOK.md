# Reproduction Runbook

## 1. Supported environment

The archive was assembled and verified with:

- Python 3.13.5
- NumPy 2.3.5
- SciPy 1.17.0
- SymPy 1.14.0
- mpmath 1.3.0
- Matplotlib 3.10.8

The code should also work on nearby modern versions, but exact solver behavior and runtime may differ. For archival replication, use the pinned versions in `requirements-lock.txt` when wheels are available for your platform.

## 2. Install

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Verify committed outputs

```bash
python tools/verify_results.py
python -m unittest discover -s tests -v
```

This checks JSON parsing, PASS verdicts, Boolean gates, source compilation, the expected audit range, figures, and manifest consistency.

## 4. Regenerate figures

```bash
python tools/generate_english_figures.py
python tools/generate_a79_figure.py
python tools/generate_a80_figure.py
python tools/generate_a82_figure.py
python tools/generate_a83_figure.py
python tools/generate_a84_figure.py
python tools/generate_a85_figure.py
python tools/generate_a86_figure.py
python tools/generate_a87_figure.py
python tools/generate_a88_figure.py
python tools/generate_a89_figure.py
python tools/generate_a90_figure.py
python tools/generate_a91_figure.py
```

The figures are generated from committed JSON outputs. No OCR, web access, or external data download is used.

## 5. Materialize the historical flat runtime

Many audits were written as a sequential research notebook in script form. They expect helper scripts and previous JSON results in the same directory.

```bash
python tools/materialize_runtime.py
```

This creates `build/runtime/` and copies:

- all Python audit files;
- all result JSON files;
- all configuration templates.

## 6. Run selected audits

```bash
python tools/run_all_audits.py --from-audit 39 --to-audit 45
```

Run a single audit:

```bash
python tools/run_all_audits.py --from-audit 71 --to-audit 71
```

Run the complete sequence:

```bash
python tools/run_all_audits.py --from-audit 39 --to-audit 103
```

Run A81 or A82 directly:

```bash
python audits/a81_reduced_boundary_system_audit.py
python audits/a82_adjacent_contact_locator_audit.py
```

### Runtime warning

A complete replay is expensive. A62 contains bootstrap calibration/validation simulations. A63–A92 contain large LP catalogues and exact symbolic calculations; A71 ranks 84 designs exactly and uses multiprocessing, A78 classifies 9230 exact branches, A79 performs symbolic root isolation and complete KKT root censuses, A80 runs 20 isolated exact interval workers, A81 certifies 1,438 reduced contact systems, A82 classifies 1,367 exact adjacent objective comparisons, A84 extends the exact pointwise stress through `M=300`, A85 checks 1,746 exact transition-bracket core/residual comparisons, A86 performs 873 exact rational contact-strip classifications, A87 evaluates 1,746 exact local factors plus the complete 63,948-secant monotonicity census, A88 evaluates 8,019 exact local secants through `M=900` on nine probes, A89 verifies an exact rational continuum threshold with 45 regression cells, A90 evaluates 594,423 exact integer-scaled adjacent factors in 4,599 complete contact sequences, A91 re-evaluates the decisive offset-three factor in 4,563 eligible cells with exact four-core/residual comparisons, and A92 classifies 858 algebraic contact cells by adaptive rational interval arithmetic. Do not interpret a long runtime as a failed proof. Each runner log is stored under `logs/replay/`.

## 7. Exact versus numerical layers

- **Exact rational/symbolic:** SymPy rational LPs, determinant identities, Cramer certificates, root isolation, primal–dual equality, phase boundary divisibility, and sign proofs.
- **Numerical optimization:** SciPy HiGHS LP catalogues and cross-solver checks.
- **Monte Carlo/model-conditional:** A62 bootstrap calibration and validation.

The technical note for each audit distinguishes these layers.

## 8. Common platform issue

Some hosted Python environments inject unrelated spreadsheet-runtime startup hooks and print a warning to `stderr`. Such a warning appeared during A61/A71 packaging but did not originate in the research scripts. The repository verifier ignores no audit failure: a nonzero process exit remains a failure.

## 9. Publication workflow

Before a public GitHub release:

1. choose and add a license;
2. update repository URL in `CITATION.cff`;
3. create a tagged release;
4. archive the release on Zenodo if a DOI is desired;
5. preserve `MANIFEST.sha256` with the release asset.

## A84

```bash
python audits/a84_k_space_exponential_polynomial_stress_audit.py
python tools/generate_a84_figure.py
```

The A84 finite exact scan normally completes in tens of seconds.
## A85

```bash
python audits/a85_parity_dominant_balance_contact_localization_audit.py
python tools/generate_a85_figure.py
python tools/generate_a86_figure.py
python tools/generate_a87_figure.py
python tools/generate_a88_figure.py
python tools/generate_a89_figure.py
python tools/generate_a90_figure.py
python tools/generate_a91_figure.py
```

A85 reuses the committed A84 maximizer catalogue. Its exact rational layer is substantially smaller than the full A84 scan; the logarithmic offset diagnostic is high-precision numerical and is not a formal interval certificate.


## A86

```bash
python audits/a86_exact_rational_contact_strip_audit.py
python tools/generate_a86_figure.py
```

A86 reuses the committed A84 exact transition records. Its theorem gates use only integer arithmetic; no numerical logarithm is used to determine slope order or contact offsets.

## A87

```bash
python audits/a87_exact_secant_offset_classifier_audit.py
python tools/generate_a87_figure.py
```

A87 reads the committed A84–A86 layers and uses exact rational arithmetic. It evaluates two local factors per support/probe cell and separately audits the full finite factor sequences to reject global monotonicity.



## A88

```bash
python audits/a88_nine_term_secant_positivity_audit.py
python tools/generate_a88_figure.py
```

A88 uses exact `Fraction` arithmetic for 8,019 local-secant cells and can take tens of seconds. It proves finite positivity through `M=900` on nine rational probes and records positive parity-phase leading limits without claiming an explicit all-`M` remainder threshold.

## A89

```bash
python audits/a89_uniform_secant_threshold_audit.py
python tools/generate_a89_figure.py
```

A89 is an analytic tail certificate rather than a large finite scan. It proves positivity of the classifier local secant for every real `s` in `[129/1000,133/1000]` and every integer `M>=521`. The threshold is sufficient for the declared rational majorants and is not claimed minimal.
## A90

```bash
python audits/a90_prethreshold_all_k_one_variation_audit.py
python tools/generate_a90_figure.py
```

A90 performs a complete all-contact scan for `M=10,...,520` at nine exact rational probes. It uses denominator-cleared integer exponential sums, not floating-point sign decisions. The finite result preserves fifteen offset-three counterexamples to extending the A86 strip beyond its original range.


## A91

```bash
python audits/a91_exact_four_term_offset_three_mechanism_audit.py
python tools/generate_a91_figure.py
```

A91 uses exact rational arithmetic for the four-term/full-factor sign theorem. Its parity-corrected locator screen is explicitly stored as a 120-digit numerical diagnostic and is not part of the exact theorem gates.


## A92

```bash
python audits/a92_exact_continuum_offset_three_window_audit.py
python tools/generate_a92_figure.py
```

A92 uses exact integer comparisons to bracket algebraic `b`-cell boundaries and exact rational interval arithmetic to classify the complete decisive-factor atlas over the declared continuum interval. It certifies strict local maxima, not global continuum one-variation.

## A93

```bash
python audits/a93_exact_continuum_global_one_variation_audit.py
python tools/generate_a93_figure.py
```

A93 uses exact rational outer-hull interval arithmetic on all non-decisive adjacent factors in the twenty-five A92 cells. It uses multiprocessing but sorts output before serialization.

## A94

```bash
python audits/a94_exact_all_cell_continuum_one_variation_audit.py
python tools/generate_a94_figure.py
```

A94 certifies all 125,814 factor/cell pairs on the 858 A92 continuum cells. It uses multiprocessing, exact `Fraction` arithmetic, adaptive interval subdivision, and twelve strict-convexity fallbacks. Output is sorted before serialization.

## A96

```bash
python audits/a96_full_lp_active_set_resolution_audit.py
python tools/generate_a96_figure.py
```

A96 should return `PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M125` with 22/22 gates. The high-precision discovery record is provenance only; the committed result is established by the independent exact KKT audit.
## A97

A97 uses two memory-isolated exact phases:

```bash
mkdir -p provenance/a97_phase
python audits/a97_endpoint_released_interval_and_obstruction_audit.py --interval-only-output provenance/a97_phase/a97_interval_phase.json
python audits/a97_endpoint_released_interval_and_obstruction_audit.py --workers 16 --atlas-only-output provenance/a97_phase/a97_atlas_phase.json
python audits/a97_endpoint_released_interval_and_obstruction_audit.py
python tools/generate_a97_figure.py
```

Expected verdict: `PASS_ENDPOINT_RELEASED_M125_INTERVAL_AND_76_OF_83_OBSTRUCTION_RESOLUTION_WITH_SEVEN_Q0_ENTRY_RESIDUALS` with 19/19 gates.

## A101

```bash
python audits/a101_gamma_active_interval_and_residual_closure_audit.py
python tools/generate_a101_figure.py
```

A101 is deterministic and exact. It rebuilds the M443 symbolic interval certificate and the complete 2,873-condition atlas for the final three residual witnesses.
## A102

```bash
python audits/a102_complete_rational_witness_lift_atlas_audit.py --workers 8
python tools/generate_a102_figure.py
```

A102 merges all 1,063 A95 rational phase-segment witnesses. It validates the frozen A95–A101 certificate sources, independently replays all 83 post-A95 resolutions and a deterministic 100-record natural sample, and preserves pointwise scope. See `RUNBOOK_A102.md`.
## A103

```bash
python audits/a103_endpoint_released_continuum_segment_atlas_audit.py
python tools/generate_a103_figure.py
```

The committed five-chunk provenance already covers all 76 source segments. To recompute exact records, use the chunk commands in `RUNBOOK_A103.md`; then run the main command to assemble, hash-check, and gate the full atlas. Expected verdict: `PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_76_ENDPOINT_RELEASED_SEGMENTS_WITH_25_FULL_AND_51_PARTIAL_COMPONENTS`.
## A104

A104 is replayed as seven memory-isolated exact records followed by assembly:

```bash
for i in 0 1 2 3 4 5 6; do
  python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --record-index "$i"
done
python audits/a104_exceptional_q0q1_continuum_segment_atlas_audit.py --assemble-from-records
python tools/generate_a104_figure.py
```

Expected verdict: `PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_SEVEN_EXCEPTIONAL_Q0Q1_SEGMENTS_AS_TWO_SIDED_STRICT_SUBCOMPONENTS`. See `RUNBOOK_A104.md` for the complete contract and expected counts.


## A105 exact record-isolated continuum replay

Use `RUNBOOK_A105.md`. The forty exact records should be recomputed in separate processes and then assembled with `--assemble-from-record-dir`.


## A106 exact legacy gamma-minus continuum replay

Use `RUNBOOK_A106.md`. The eighteen exact records are replayed separately and assembled with `--assemble-from-record-dir`; the audit also performs 2,410 exact direct-matrix/rank-one witness regressions.
