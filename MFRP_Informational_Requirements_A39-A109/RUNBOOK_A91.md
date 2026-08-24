# A91 Runbook

## Execute the audit

```bash
python audits/a91_exact_four_term_offset_three_mechanism_audit.py
```

Expected output:

- verdict: `PASS_EXACT_FOUR_TERM_OFFSET_THREE_CLASSIFIER_AND_PARITY_SCREENING_OBSTRUCTION`
- gates: `15/15`
- eligible cells: `4563`
- offset-three cells: `15`

## Regenerate the figure

```bash
python tools/generate_a91_figure.py
```

Output:

- `figures/a91_offset_three_screen_and_exact_cases.png`

## Required prior files

- `audits/a84_k_space_exponential_polynomial_stress_audit.py`
- `results/a90_prethreshold_all_k_one_variation_results.json`
- `results/a90_prethreshold_contact_sequence_catalogue.json`

## Evidence layers

The four-core theorem uses exact rational arithmetic. The parity-corrected locator screen is a separately labeled 120-digit numerical diagnostic and must not be cited as an exact theorem.
