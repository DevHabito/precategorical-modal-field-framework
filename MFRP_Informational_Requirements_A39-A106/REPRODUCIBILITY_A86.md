# A86 Reproducibility

A86 uses Python standard-library integer arithmetic for all theorem gates. The asymptotic slope is never evaluated with floating-point logarithms inside a certificate. Comparisons with a rational `p/q` are reduced to

```text
2^q * numerator(s)^(2p)  versus  denominator(s)^(2p).
```

Run:

```bash
python audits/a86_exact_rational_contact_strip_audit.py
```

The audit reads the committed A84 result file and writes two deterministic JSON outputs. Re-running the script must reproduce the same gate counts, contact offsets, finite thresholds, and verdict.
