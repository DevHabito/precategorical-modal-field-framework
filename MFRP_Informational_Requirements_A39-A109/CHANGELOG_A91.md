# A91 Changelog

## Added

- `audits/a91_exact_four_term_offset_three_mechanism_audit.py`
- `results/a91_four_term_offset_three_results.json`
- `results/a91_four_term_offset_three_catalogue.json`
- `docs/technical_notes/MFRP_next_step_four_term_offset_three_mechanism.md`
- `tools/generate_a91_figure.py`
- `figures/a91_offset_three_screen_and_exact_cases.png`

## Result

A91 identifies an exact four-channel discriminant for the fifteen A90 offset-three cells. In all 4,563 cells where the comparison between contacts `b+2` and `b+3` is admissible, the four-term core has the same sign as the full ten-term adjacent factor and strictly dominates the six-term residual. The minimum exact core-to-residual ratio is approximately `74.9243`.

The A85 parity-corrected continuous locator screens all fifteen offset-three cells but also produces fifty-four false positives. It is therefore retained as a high-precision diagnostic screen, not promoted to an exact rounding law.
