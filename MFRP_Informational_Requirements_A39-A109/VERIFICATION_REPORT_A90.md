# A90 Verification Report

## Scope

This report records the final verification of the A39–A90 archive and the standalone A90 package.

## A90 execution

Command:

```bash
python audits/a90_prethreshold_all_k_one_variation_audit.py
```

Observed verdict:

```text
PASS_EXACT_PRETHRESHOLD_NINE_PROBE_ALL_K_ONE_VARIATION_AND_FOUR_CONTACT_STRIP
```

A90 gates:

```text
17/17 PASS
```

Declared finite result:

```text
M range: 10..520
rational probes: 9
complete sign sequences: 4,599
exact adjacent-factor evaluations: 594,423
strict one-variation sequences: 4,599
zero factors: 0
```

Exact offset census relative to `ceil(M c(s))`:

```text
offset 0: 9
offset 1: 1,207
offset 2: 3,368
offset 3: 15
```

The first offset-three certificate is:

```text
M=325, s=129/1000, ceil(Mc)=55, k*=58
```

The 45 denominator-clearing regression identities all match direct rational evaluation exactly.

## Repository integrity

Commands:

```bash
python -m unittest discover -s tests -v
python tools/verify_results.py
```

Expected final repository summary after manifest regeneration:

```text
52 audit results
682 registered gates
94 figures
29/29 integrity tests
0 verification failures
PASS
```

## Claim boundary

The verification establishes internal consistency and reproducibility of the declared finite grid. A90 does not prove one variation for every real probe in the interval, global all-contact unimodality for `M>=521`, or a universal four-contact strip. The fifteen offset-three records contradict only an extrapolation of A86 beyond its declared `M<=300` scope.
