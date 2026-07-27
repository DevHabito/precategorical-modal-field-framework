# A72–A77 Reproduction Runbook

## Environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Verification

```bash
python tools/verify_results.py
python -m unittest discover -s tests -v
```

## Flat runtime

Several scripts import helpers and read earlier JSON files by filename. Create a flat directory containing all files from `audits/` and `results/`. The exact generators and large neighborhood classifications can be computationally expensive.

## Main programs

- A72: `a72_local_pivot_diamond_audit.py`
- A73: `a73_complete_one_pivot_neighborhood_audit.py`
- A74: `a74_interval_gamma_bifurcation_audit.py`
- A75: `a75_parity_orientation_audit.py`
- A76: `a76_active_reentry_audit.py` plus its interval and neighborhood certificate scripts
- A77: `a77_fixed_family_parity_audit.py`, `a77_support_interval_certificate.py`, and `a77_one_pivot_contact_reset_certificate.py`

A77 is a multi-stage audit. The aggregate JSON combines the validated parity theorem, per-support certificates, and one-pivot neighborhood classification.
