# Reproducibility A85

## Primary command

```bash
python audits/a85_parity_dominant_balance_contact_localization_audit.py
```

Expected verdict:

```text
PASS_PARITY_DOMINANT_BALANCE_AND_ASYMPTOTIC_CONTACT_LOCALIZATION
```

## Figure

```bash
python tools/generate_a85_figure.py
```

## Evidence layers

A85 intentionally separates two evidence classes.

### Exact rational/symbolic layer

- the parity-leading coefficient identities are checked symbolically with SymPy;
- all 1,746 transition-bracket factor evaluations use Python `Fraction` arithmetic;
- all core/residual sign and magnitude comparisons are exact;
- the single four-term sign counterexample and the two strict-dominance failures are exact;
- the eight-term fallback is exact at every audited factor.

### High-precision diagnostic layer

The parity-corrected contact predictor uses `mpmath` at 80 or more decimal digits because it contains logarithms. The `864/864 within one contact` statement is a numerical diagnostic, not an interval-certified transcendental theorem. It is not used to prove the asymptotic rate result.

## Inputs

A85 reads the committed A84 result file:

```text
results/a84_k_space_exponential_polynomial_stress_results.json
```

and imports the exact A84 helper formulas from:

```text
audits/a84_k_space_exponential_polynomial_stress_audit.py
```

No network access, external dataset, random seed, or solver is used.

## Outputs

```text
results/a85_parity_dominant_balance_contact_localization_results.json
results/a85_transition_dominant_balance_catalogue.json
figures/a85_parity_asymptotic_contact_localization.png
```

## Claim boundary

The analytic asymptotic slope is derived under the declared reduced contract. The exact finite dominance result concerns only the two adjacent factors bracketing each A84 maximizer. A85 does not establish a unique all-support transition, a global four-term inequality for every contact, or an exact rounding rule for the selected integer contact.
